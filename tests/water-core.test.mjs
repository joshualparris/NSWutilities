import test from 'node:test';
import assert from 'node:assert/strict';
import { stepWater, validateWaterNetwork } from '../src/water/water-core.mjs';
const fixture = () => ({
  tanks:[{id:'treated-tank',capacityL:150,inletLph:25,inletPowerAssetId:'wtp',leakLph:0}],
  junctions:[{id:'water-main'}],
  links:[
    {id:'feeder',fromId:'treated-tank',toId:'water-main',capacityLph:100,open:true},
    {id:'home-a-pipe',fromId:'water-main',toId:'H:A1',capacityLph:30,open:true},
    {id:'home-b-pipe',fromId:'water-main',toId:'H:B1',capacityLph:30,open:true}
  ],
  services:[
    {id:'H:A1',demandLph:20,returnFraction:.8,waterClass:'potable-model'},
    {id:'H:B1',demandLph:20,returnFraction:.5,waterClass:'potable-model'}
  ],
  wastewater:{capacityL:70,treatmentLph:22,treatmentElectricAssetId:'stp',infiltrationLph:0}
});
const starting = () => ({tanks:{'treated-tank':100},wastewaterL:0});
const power = {wtp:true,stp:true};
const run = (f=fixture(),s=starting(),p=power) => stepWater(f,s,{hours:1,powered:p});
const conserved = x => {assert.ok(Math.abs(x.ledger.potable.imbalanceL)<1e-8);assert.ok(Math.abs(x.ledger.sanitary.imbalanceL)<1e-8)};
test('baseline: individual meters, litres and separate wastewater balance',()=>{
  const x=run(); assert.equal(x.deliveries['H:A1'],20);assert.equal(x.deliveries['H:B1'],20);
  assert.equal(x.state.tanks['treated-tank'],85);assert.equal(x.ledger.sanitary.generatedL,26);
  assert.equal(x.ledger.sanitary.treatedL,22);assert.equal(x.state.wastewaterL,4);conserved(x);
});
test('power cut stops water production but cannot erase tank water instantly',()=>{
  const x=run(fixture(),starting(),{wtp:false,stp:true});
  assert.equal(x.ledger.potable.treatedInputL,0);
  assert.equal(x.ledger.potable.deliveredL,40);assert.equal(x.state.tanks['treated-tank'],60);conserved(x);
});
test('closed individual service valve only interrupts affected building',()=>{
  const f=fixture();f.links.find(x=>x.id==='home-a-pipe').open=false;
  const x=run(f);assert.equal(x.deliveries['H:A1'],0);assert.equal(x.unmet['H:A1'],20);
  assert.equal(x.deliveries['H:B1'],20);conserved(x);
});
test('finite feeder capacity creates unmet water demand',()=>{
  const f=fixture(); f.links[0].capacityLph=10;
  const x=run(f); assert.equal(x.ledger.potable.deliveredL,10);assert.equal(Object.values(x.unmet).reduce((a,b)=>a+b,0),30);conserved(x);
});
test('tank leak is metered as loss and cannot produce negative storage',()=>{
  const f=fixture();f.tanks[0].leakLph=200;f.tanks[0].inletLph=0;
  const x=run(f);assert.equal(x.ledger.potable.leakL,100);assert.equal(x.ledger.potable.deliveredL,0);conserved(x);
});
test('water production above full tank capacity reports discarded overflow',()=>{
  const f=fixture();f.tanks[0].inletLph=100;const s=starting();s.tanks['treated-tank']=140;
  const x=run(f,s);assert.equal(x.ledger.potable.tankOverflowL,90);conserved(x);
});
test('sewer blackout allows sewage to accumulate and overflow finite wet well',()=>{
  const f=fixture();f.wastewater.capacityL=10;
  const x=run(f,starting(),{wtp:true,stp:false});
  assert.equal(x.ledger.sanitary.treatedL,0);assert.equal(x.ledger.sanitary.overflowL,16);conserved(x);
});
test('sanitary I&I is a separate explicitly modelled inlet, not rainfall secretly added',()=>{
  const f=fixture();f.wastewater.infiltrationLph=5;
  const x=run(f);assert.equal(x.ledger.sanitary.infiltrationL,5);assert.equal(x.ledger.sanitary.afterL,9);conserved(x);
});
test('powered pipe shuts when motor unavailable, not when upstream gravity works',()=>{
  const f=fixture();f.links.find(x=>x.id==='home-b-pipe').pumpElectricAssetId='booster';
  const x=run(f,starting(),power);assert.equal(x.deliveries['H:A1'],20);assert.equal(x.deliveries['H:B1'],0);conserved(x);
});
test('reverse-only link cannot backfeed household, validation rejects recycled pipe',()=>{
  const f=fixture(); f.links.find(x=>x.id==='home-b-pipe').fromId='H:B1';
  f.links.find(x=>x.id==='home-b-pipe').toId='water-main';
  assert.equal(run(f).deliveries['H:B1'],0);
  f.links[0].waterClass='recycled';
  assert.throws(()=>validateWaterNetwork(f),/Cross connection/);
});
test('unavailable water quality and pressure are not asserted safe',()=>{
  const x=run();assert.equal(x.pressureKPa,null);assert.equal(x.waterQualityAssessment,'not-assessed');
});
test('fixed input and power yield byte-for-byte deterministic snapshots',()=>{
  const first=run();const again=run();assert.equal(JSON.stringify(first),JSON.stringify(again));
  assert.equal(JSON.stringify(starting()),JSON.stringify(starting()));
});
test('bad references, duplicate IDs, unrealistic units and state are rejected',()=>{
  const orphan=fixture();orphan.links[0].fromId='not-a-source';assert.throws(()=>run(orphan),/Orphan/);
  const duplicated=fixture();duplicated.services[1].id='H:A1';assert.throws(()=>run(duplicated),/duplicate/);
  const negative=fixture();negative.tanks[0].inletLph=-1;assert.throws(()=>run(negative),/non-negative/);
  assert.throws(()=>run(fixture(),{tanks:{'treated-tank':999},wastewaterL:0}),/exceeds capacity/);
});
test('audited source IDs 234 remain unique; all water service labels unknown, not fictionalised as real',async()=>{
  const {readFile} = await import('node:fs/promises');
  const data=JSON.parse(await readFile(new URL('../audit/water/building-service-inventory.json',import.meta.url),'utf8'));
  assert.equal(data.records.length,234);assert.equal(new Set(data.records.map(x=>x.id)).size,234);
  assert.equal(data.counts.houses,188);assert.equal(data.counts.sites,46);
  assert.ok(data.records.every(x=>x.water.status==='unknown'&&x.sanitary.status==='unknown'&&x.storm.status==='unknown'));
});
