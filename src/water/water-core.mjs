/**
 * NSW-WAT-007: intentionally *non-hydraulic*, deterministic, directed
 * L/h + L reference surrogate for a synthetic Repository Town fixture.
 * Not a potable-water safety model or an EPANET/SWMM replacement.
 * Never produces a pressure (kPa) or claims real NSW asset locations.
 */
const finiteNonnegative = (n, where) => {
  if (typeof n !== 'number' || !Number.isFinite(n) || n < 0)
    throw new Error(`Expected finite non-negative number at ${where}`);
  return n;
};
const sorted = xs => [...xs].sort((a,b) => a.id.localeCompare(b.id, 'en'));
const powerOK = (electricAssetId, powered) =>
  !electricAssetId || powered[electricAssetId] === true;

export function validateWaterNetwork(network) {
  if (!network || !Array.isArray(network.tanks) || !Array.isArray(network.links) || !Array.isArray(network.services))
    throw new Error('Missing tanks, links or services');
  const ids = new Set();
  const add = (id, where) => {
    if (typeof id !== 'string' || !id.trim() || ids.has(id))
      throw new Error(`Missing or duplicate asset ID at ${where}: ${id}`);
    ids.add(id);
  };
  for (const t of network.tanks) {
    add(t.id, 'tank');
    finiteNonnegative(t.capacityL, 'tank capacity');
    finiteNonnegative(t.inletLph ?? 0, 'tank inlet');
    finiteNonnegative(t.leakLph ?? 0, 'tank leak');
  }
  for (const j of network.junctions || []) add(j.id, 'junction');
  for (const s of network.services) {
    add(s.id,'service');
    finiteNonnegative(s.demandLph,'service demand');
    finiteNonnegative(s.returnFraction ?? 0, 'sewer fraction');
    if ((s.returnFraction ?? 0) > 1) throw new Error('Sewer return fraction above 1');
    if (s.waterClass && s.waterClass !== 'potable-model')
      throw new Error('Cross connection or unapproved water class in potable fixture');
  }
  const edgeIds = new Set();
  for (const e of network.links) {
    if (typeof e.id !== 'string' || !e.id.trim() || edgeIds.has(e.id)) throw new Error('Duplicate link ID');
    edgeIds.add(e.id);
    if (!ids.has(e.fromId) || !ids.has(e.toId)) throw new Error(`Orphan pipe ${e.id}`);
    finiteNonnegative(e.capacityLph,'link capacity');
    if (typeof e.open !== 'boolean') throw new Error('Pipe open must be Boolean');
    if (e.waterClass && e.waterClass !== 'potable-model')
      throw new Error('Cross connection to sanitary/recycled network');
  }
  if (!network.wastewater || typeof network.wastewater !== 'object')
    throw new Error('Missing explicit wastewater store');
  finiteNonnegative(network.wastewater.capacityL,'sewer capacity');
  finiteNonnegative(network.wastewater.treatmentLph,'sewer treatment rate');
  finiteNonnegative(network.wastewater.infiltrationLph ?? 0,'sewer infiltration rate');
  return true;
}

const close = value => Math.abs(value) < 1e-10 ? 0 : value;
/** Runs ONE time step. All demand/throughput/rain-infiltration rates in L/hour. */
export function stepWater(network, inputState, {hours=1, powered={}}={}) {
  validateWaterNetwork(network);
  finiteNonnegative(hours,'step hours');
  if (!hours || hours > 24) throw new Error('Step must be > 0 and <= 24 hours');
  if (!inputState || typeof inputState !== 'object') throw new Error('Missing saved state');
  const state = {
    tanks:{}, wastewaterL:finiteNonnegative(inputState.wastewaterL, 'saved wastewater')
  };
  if (state.wastewaterL > network.wastewater.capacityL) throw new Error('Saved sewer exceeds capacity');
  const tanks = sorted(network.tanks), edges = sorted(network.links), services = sorted(network.services);
  const remainingCap = new Map(edges.map(e=>[e.id,e.capacityLph*hours]));
  let beforeL=0, treatedInputL=0, tankOverflowL=0, leakL=0;
  for (const t of tanks) {
    const before=finiteNonnegative(inputState.tanks?.[t.id],`saved tank ${t.id}`);
    if (before>t.capacityL) throw new Error('Saved tank exceeds capacity');
    beforeL+=before;
    const produced=powerOK(t.inletPowerAssetId,powered)?t.inletLph*hours:0;
    const added=Math.min(produced,t.capacityL-before);
    tankOverflowL+=produced-added;
    treatedInputL+=produced;
    let usable=before+added;
    const leak=Math.min(usable,(t.leakLph??0)*hours);
    usable-=leak; leakL+=leak;
    state.tanks[t.id]=usable;
  }
  const deliveries={}, unmet={}, routes={}, requested={};
  let deliveredL=0, sewerGeneratedL=0;
  const outgoing=new Map();
  for (const e of edges) {
    if (!e.open || !powerOK(e.pumpElectricAssetId,powered)) continue;
    if (!outgoing.has(e.fromId)) outgoing.set(e.fromId,[]);
    outgoing.get(e.fromId).push(e);
  }
  // Simple directed reachable path with residual *volumetric* capacity.
  // No node head/pressure, distributed hydraulics, or loop flow solution.
  function findPath(from, target) {
    const queue=[{node:from,path:[]}],seen=new Set([from]);
    for(let p=0;p<queue.length;p++) {
      const step=queue[p];
      if (step.node===target) return step.path;
      for(const e of outgoing.get(step.node)??[]) {
        if((remainingCap.get(e.id)??0)<=1e-10 || seen.has(e.toId)) continue;
        seen.add(e.toId);
        queue.push({node:e.toId,path:[...step.path,e]});
      }
    }
    return null;
  }
  for(const service of services) {
    const required=service.demandLph*hours;
    requested[service.id]=required;
    let remaining=required;
    deliveries[service.id]=0;routes[service.id]=[];
    for(const tank of tanks) {
      if(remaining<=1e-10)break;
      const path=findPath(tank.id,service.id);
      if(!path || state.tanks[tank.id]<=0)continue;
      const bottleneck=Math.min(...path.map(e=>remainingCap.get(e.id)));
      const allocated=Math.max(0,Math.min(remaining,state.tanks[tank.id],bottleneck));
      if(allocated<=0)continue;
      for(const e of path)remainingCap.set(e.id,close(remainingCap.get(e.id)-allocated));
      state.tanks[tank.id]=close(state.tanks[tank.id]-allocated);
      deliveries[service.id]+=allocated;
      routes[service.id].push({tankId:tank.id,linkIds:path.map(e=>e.id),litres:allocated});
      remaining-=allocated;
    }
    deliveries[service.id]=close(deliveries[service.id]);
    unmet[service.id]=close(Math.max(0,required-deliveries[service.id]));
    deliveredL+=deliveries[service.id];
    sewerGeneratedL+=deliveries[service.id]*(service.returnFraction??0);
  }
  const afterL=Object.values(state.tanks).reduce((a,b)=>a+b,0);
  const waterImbalanceL=close(beforeL+treatedInputL-deliveredL-leakL-tankOverflowL-afterL);
  // This is a single synthetic sewage basin, NOT a sewer pipe graph.
  const sewerBeforeL=inputState.wastewaterL;
  const infiltrationL=network.wastewater.infiltrationLph*hours||0;
  const available=sewerBeforeL+sewerGeneratedL+infiltrationL;
  const treatedL=powerOK(network.wastewater.treatmentElectricAssetId,powered)
    ?Math.min(available,network.wastewater.treatmentLph*hours):0;
  const pending=available-treatedL;
  state.wastewaterL=Math.min(pending,network.wastewater.capacityL);
  const sewerOverflowL=Math.max(0,pending-state.wastewaterL);
  const sewerImbalanceL=close(sewerBeforeL+sewerGeneratedL+infiltrationL-treatedL-sewerOverflowL-state.wastewaterL);
  if (Math.abs(waterImbalanceL)>1e-7 || Math.abs(sewerImbalanceL)>1e-7)
    throw new Error('Conservation of volume failure');
  return {
    state, deliveries, unmet, requested, routes,
    pressureKPa:null, waterQualityAssessment:'not-assessed',
    ledger:{
      potable:{beforeL,treatedInputL,deliveredL,leakL,tankOverflowL,afterL,imbalanceL:waterImbalanceL},
      sanitary:{beforeL:sewerBeforeL,generatedL:sewerGeneratedL,infiltrationL,treatedL,
        overflowL:sewerOverflowL,afterL:state.wastewaterL,imbalanceL:sewerImbalanceL}
    }
  };
}
