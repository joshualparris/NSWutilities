# NSW-WAT — Water supply, plumbing, sewerage and stormwater reference architecture

**Engineering-specification tier; as of 25 October 2026.** Companion: [source synthesis](WATER_RESEARCH_2026-10-25.md), [parity audit](WATER_PARITY_AUDIT_2026-10-25.md), [open engines](WATER_OPEN_SOURCE_AUDIT.md), [tasks](WATER_IMPLEMENTATION_TASKS.md). No true Dubbo street pipes, calibrations, water quality certification or deployed Repository Town water implementation are claimed.

## 1. Fidelity and clear system boundaries

- **Tier 0 / existing game:** hourly, unitless `waterworks.stock.water` stock; `waterOk` global and `sewage.stock.wastewater` backlog. Retain as *legacy*, never relabel its units litres.
- **Tier 1 / proposed playable:** every property has separate meter/service IDs, explicit source/intake, treatment throughput, tanks, valves, pumps, pipe graph, finite volumes, energy dependencies, sewage capture, wastewater storage/treatment/overflow and independent storm runoff; visually readable symptoms and deterministic restoration. **Does not assert calculated node pressures**, nor safety of tap water.
- **Tier 2 / reference model:** EPANET for demand-driven or pressure-dependent head/flow/quality, WNTR for burst/repair reliability; SWMM for catchment/sewer/conduit/wet-weather hydraulics. Validate synthetic comparator fixtures (document solver version and numerical tolerances) *before* using head/flow estimates in game.
- **Tier 3 / optional:** uncertainty bands, pump curves/efficiency, treatment unit process capacity, real-time scenarios from licensed evidence, water age and chlorine proxies, pressure-zone transients and hydrologic/soil model. No engineering or public health operational certification.

## 2. End-to-end topology (networks are separate)

```text
MACQUARIE RIVER / BORES (documented regional analogy, fictional placement)
  -> licensed/raw abstractions -> screening -> raw pumps -> treatment + backwash
  -> clearwater tank -> high lift pump / gravity reservoir -> pressure zones
  -> trunk & reticulation mains -> meter/backflow -> internal cold water
                                           |-> hot water heater -> taps/shower
                                           |-> toilet cistern -> flush
                                           |-> clinic/bakery/fire service as applicable
  -> sanitary fixtures -> traps/vents -> boundary drainage -> sewer lateral
  -> gravity mains + manholes -> lift stations/rising mains if needed
  -> STP screens/grit -> biological -> clarification -> disinfection when applicable
                        |-> sludge/biosolids -> managed destination
                        |-> approved discharge to receiving environment
                        |-> advanced treatment -> separate recycled-water storage
                                                -> **licensed approved** nonpotable uses
RAIN -> roofs/gutters/pits/drains -> detention/creek/floodplain (separate storm layer)
```

In NSW, applicable backflow control and sewer connections must be assessed using the **Plumbing Code of Australia as adopted in NSW**, AS/NZS 3500 provisions and the council's connection conditions. Never encode a literal code-compliance claim from this high-level diagram. Nonpotable pipes/cross-connections must not join potable mains. Council describes Dubbo source shares (~70% river, ~30% borefield; historical typical mix); this is **not** a per-timestep meter, and the fictional town should not claim exact identity.

## 3. Versioned canonical schema (design sketch)

```ts
type Evidence = "documented" | "inferred" | "synthetic";
type Provenance = { evidence:Evidence; sourceId?:string; retrievedAt?:string; sourceDate?:string; assumptions?:string[] };
type WaterNode = {
  id:string; kind:"raw-source"|"intake"|"treatment"|"clearwell"|"tank"|"reservoir"|"junction"|"meter"|"customer";
  waterClass:"raw"|"potable-model"|"recycled"|"storm"|"sanitary"|"trade-waste";
  elevationM?:number; storedL?:number; maxStoredL?:number;
  demandLph?:number; inletLph?:number; outletCapLph?:number;
  pressureHeadM?:number; // only when solver-derived
  worldX?:number; worldZ?:number; provenance:Provenance;
};
type WaterLink = {
  id:string; fromNodeId:string; toNodeId:string;
  kind:"main"|"service"|"valve"|"pump"|"check-valve"|"drain"|"sewer"|"rising-main";
  lengthM?:number; insideDiameterMm?:number; invertUpM?:number; invertDownM?:number;
  roughness?:number; capacityLph?:number; open:boolean; poweredByElectricAssetId?:string;
  sourceId?:string; provenance:Provenance;
};
type PropertyService = {
  buildingId:string; potableMeterId?:string; sanitaryConnectionId?:string;
  stormConnectionId?:string; recycledMeterId?:string; serviceDecision:"connected"|"not-required"|"private"|"unknown";
  tariffClass?:string; fixtures?:{toiletCount?:number; showers?:number; hotWater?:boolean};
  demandProfileId?:string; sewageReturnFraction?:number; provenance:Provenance;
};
```

All assets have unique IDs; geometry uses real units and preserves source/ref metadata; game coordinates and geographic coordinates have separate transforms. A missing physical connection is represented as unknown, not silently connected. Every pipe, valve, node and meter has distinct network-layer membership. Model **litres L**, flows **L/h** (or explicitly L/s), head **m**, pressure **kPa** only when justified, energy **kWh**, pump draw **kW**, timestep **hours**. Sewer grades require invert elevations not decorative mesh elevations; retain ground elevation separately.

## 4. Fast Tier 1 runtime algorithm (conserves liquid, not pressure)

At each deterministic interval `dtH`:
1. Apply stateful faults/power outages, isolate valves/pressure zones and identify reachable, *directionally permitted* meter connections. No unprotected backfeed; failed pump is impassable unless verified gravity/bypass path exists.
2. Raw intake/WT output and tank replenishment are separately capped by flow source limits, treatment plant limits, capacity, power and treatment-operating state; declare discarded raw/backwash and physical losses separately.
3. For each served customer (deterministic stable ordering), allocate tank volume by connected path pipe capacities and prioritised demand; **never imply an unpowered booster can pass water automatically**.
4. Track losses/leaks on explicitly connected assets, conservation and tank upper/lower bound. Household delivered water may continue after upstream power loss while reservoir volume remains if gravitating and isolation permits.
5. From actual property fixtures, calculate indoor sanitary wastewater using separately documented return factors, excluding outdoor irrigation and accounting for infiltration/inflow separately. Route via gravity capacity, pump wet wells (separately electrical), treatment and finite sewage storage. Overflow **always recorded**, not deleted.
6. Rain/runoff storm layer: `rainVolumeL = rainfallMm * effectiveCatchmentM2` because 1 mm on 1 m² = 1 L; multiply runoff coefficient and subtract infiltration/detention appropriately. Do not add all rainfall directly to sanitary sewer.
7. Produce immutable per-asset snapshot, energy consumption and event/quality-alert logs; save seed/time/graph version and load without side effects. Emit visible results only for calculated properties.
8. Tier 1 **never outputs numeric pressure** from connectivity; show `unknown/not-solved` until a justified Tier 2 pressure computation or clearly identified gameplay approximation is added.

**Potable water ledger** (L): `storedBefore + treatedInput = deliveredAtMeters + physicalLeaks + discardedOverflow + storedAfter`. If tank fills past capacity, overflow is explicitly logged. Source abstractions and treatment losses have their **own upstream** balance.

**Sanitary ledger** (L): `sewageStoredBefore + fixtureReturn + infiltrationInflow = treated + sanitaryOverflow + sewageStoredAfter`. Treated wastewater has receiving environment, reuse, sludge and losses in **downstream** ledgers—treated is not automatically potable.

**Pump:** `P_electric_kW ≈ (rho * g * Q_m3ps * H_m)/(efficiency * 1000)`. Account for motor efficiency; no pump head or efficiency can be inferred from a symbol on a game map. **Pressure:** a reference solver must consider elevations and head losses (Darcy–Weisbach/Hazen–Williams and pipe/valve minor losses); pressure at one junction is not globally uniform.

**Gravity sewage concept:** directional links require upstream invert > downstream invert for normal gravity, unless a force main/pumped link. Manning depth/flow and hydraulic grade require validated geometry; do not assert capacity = diameter alone.

## 5. Treatment/quality states and safety

Raw vs nominal treated vs independently verified safe water are different concepts. Represent simulated treatment state and sampling/critical control point alerts; **never output 'safe to drink' as an engineering or health conclusion**. NSW Health requires DWMS/quality assurance programs and critical control points, with review/audit. An explicit advisory is a simulated event from the fictional water authority, not actionable advice; actual users must consult their water provider.

Disinfection, coagulation, membrane and UV are not universal for all real NSW WTPs. The J8 Water Works interior's membrane/UV display is an *illustrative design choice*, not proof of Dubbo's exact process train.

The **Dubbo advanced wastewater plant** was announced completed 8 Sep 2026; up to 700 ML/year is rated annual capacity. Approval for some recycled-water uses was still being sought at that time; do not feed recycled water to game buildings before modelling an explicit **fictional approval**, separate purple-pipe network, and end-use restriction.

## 6. Electricity / water / sewer / storm cross-dependencies

- Power loss -> raw/treated pumping ceases unless tested standby supply; gravity-fed tank water persists until depleted. Power fault at J8 cannot instantly turn off all city taps.
- Power loss at L8 -> treatment stops, **sewage still arrives** by gravity; wet wells fill. Lift-station fail causes upstream surcharge/overflow; independent healthy gravity catchments may remain functional.
- A failed water main affects only downstream served properties and explicit parallel-loop/bypass; unaffected zone continues. Contaminant precaution may be wider but must be set as explicit authority event.
- Toilet requires water at cistern (unless already full), gravity drain/path or functioning ejector where applicable, usable downstream sanitary capacity, and an appropriate plumbing layout; a flushing event moves *finite stored cistern litres* into wastewater.
- Rain may increase wastewater through I&I faults, but normal stormwater network stays separate. Stormwater flood effects are governed by rainfall/runoff and ground topology.
- Backflow protection prevents reverse contamination; no instant house-to-street redistribution without a legitimate network.
- Reconnect/start pumps and treatment with configurable lag; mains repair is not automatically a declaration of potable safety; sample/clearance steps may be required in simulated scenario.
- Water/sewer states must update at same simulated timestamp as electrical snapshot. Use `electricity -> water pumps -> water delivery -> sanitary flow -> sewage pumps/treatment` ordering and avoid cyclic instantaneous updates.

## 7. Required synthetic acceptance suite (NOT claims about real Dubbo installations)

1. Every property candidate has stable ID + explicit service decision, including vacant lots and separate storm paths.
2. Two homes connected to tank with pipe capacity; total delivered ≤ water available; unmet demand explicit.
3. Pump power loss: tank volume remains and gravity-fed demand continues; refill ceases.
4. Water plant outage with zero tank: taps lose service; no instant 'water creation'.
5. Closed zone valve affects only downstream connected properties.
6. Parallel supply loop is not falsely disabled by a single break (if documented fixture supports loop).
7. Pipeline leak water is visible as loss; tank mass balance holds.
8. Attempted cross-connection from recycled/sanitary to potable rejected by validator.
9. Pressure/head output absent at Tier 1; comparator EPANET tracks supply under low pressure.
10. Sanitary total: served indoor demands × return ratios + wet-weather I&I = treated + overflow + storage delta.
11. Sewer pump outage: sewage piles up and overflows where storage limit; independent catchment unaffected.
12. Gravity drains have invert fall on each selected link, else flagged for redesign.
13. Rain→storm runoff using mm × m², no sanitary jump without explicit I&I.
14. Blackout during high irrigation vs a full toilet cistern yields distinct symptoms.
15. Treatment power loss with partial standby capacity; no potable 'safe' claim.
16. Reuse treatment outputs stored separately; expired/absent licence blocks consumers.
17. Save/reload mid-fault produces byte-equivalent next step with fixed IDs/seed/time.
18. DST and hourly time-series import have unambiguous UTC; no duplicated/skipped local hour.
19. Every record claiming a real asset has dated source URL and reuse rights.
20. EPANET/SWMM benchmark fixture comparison with version, tolerances and documented differences.
21. 1,000 synthetic buildings performance under mobile constraints; FPS independent of slow solver.
22. Hosted game playtest: tank outage, leak, blocked sewer, powered lift station, inspection overlays and mobile rendering all actually observed.

## 8. Integration path

Crosswalk to Repository Town's pre-existing `RTU-019…024` and `RTU-029…030` in [the masterplan](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/UTILITIES_MASTERPLAN_2026-10-25.md), preserving all RTU IDs. `src/water/water-core.mjs` and tests here are a deterministic **model feasibility/reference module** only, not wired into Repository Town gameplay. An adapter must translate existing **unitless** gameplay stocks into new versioned per-property L/h state, with explicit one-time migration assumption, never change old saves silently. Only claim complete after integrated tests and verified live release.
