# NSW-ELEC — Simulation architecture and acceptance specification

**Research/specification only — not implemented or field-calibrated.** Updated 25 Oct 2026.  
Companion: [sourced regional evidence](./ELECTRICITY_RESEARCH_2026-10-25.md), [open-source code audit](./OPEN_SOURCE_SIMULATION_AUDIT.md), [earlier Repository Town audit](./ELECTRICAL_GRID_FINDINGS_2026-10-25.md), [tasks](./TASKS.md).

## 1. Three fidelity tiers, never confuse them

**Tier 1 (playable first):** switch-aware topological graph + energy balance, branch and transformer thermal envelopes, synthetic demand curves, solar/battery energy budgeting and faults. This is a **fast approximation** and not proof of safe real-world operation. It must handle every building and streetlight separately.

**Tier 2 (distribution engineering reference):** as much validated electrical data as available; explicit nominal bus kV, per-phase loads, P/Q, series impedance R+jX, shunts, transformer ratio/tap, losses, reverse flow, seasonal thermal ratings. Use approximate phase-aware radial feeder loadflow in game; compare with unbalanced OpenDSS or selected validated reference cases **offline**. A switch closure that creates a mesh must trigger safe fallback to an appropriate solver or a clearly labelled unsupported approximation.

**Tier 3 (advanced / optional):** protection coordination, relay/transformer time delay, black start, frequency transients, grid-forming inverter dispatch, network resilience and market/cost optimisation. Time-domain fault currents and electromagnetics are not solved by Tier 1/2; do not claim literal real-world realism.

## 2. Architecture

```text
              SOURCES (time-stamped and provenance-labelled)
  Essential Energy DAPR / pole GIS?    Essential Energy zone 30-min loads
  AEMO 5-min dispatch/SCADA            BOM weather/solar irradiance
  manufacturer product datasheets     town world geometry / buildings
                       | NORMALISE, LICENCE-CHECK
               data/reference/*.json or parquet
                       |
        +--------------+----------------------+
        |                                     |
    ASSET REGISTRY                        REFERENCE RUNNER
  buses, poles, lines,                   OpenDSS/pandapower
  services, phases, loads                comparison scenarios
  switches, transformers                         |
        |                                  expected ranges
        +---------------+---------------------+
                        |
                GAME GRID CORE
          topology -> electrical states
          daily profiles, generation/storage
          scheduled solver + event state
                        |
         +--------------+-------------------+
         |              |                   |
      OVERLAYS         VISUALS              CONSEQUENCES
   flow/voltage/SOC    poles/wires/PV       town lights/pumps
   outage boundaries   plant/batteries      NPCs, rail, economy
```

Data acquisition never mutates a running graph. Import provenance/source references in a versioned dataset, validate units, then build deterministic immutable topology + versioned mutable state. Game must run with offline synthetic fixtures if network source endpoints disappear.

## 3. Stable model types (TypeScript design sketch)

```ts
type Evidence = 'documented' | 'inferred' | 'synthetic';
type Phase = 'A'|'B'|'C'|'N';
type AssetKind =
  | 'source' | 'bus' | 'pole' | 'line' | 'cable' | 'switch'
  | 'fuse' | 'recloser' | 'transformer' | 'meter' | 'load'
  | 'pv' | 'battery' | 'diesel' | 'gas' | 'community-bess';
type Provenance = {
  evidence: Evidence;
  sourceId?: string; // SOURCES.md or source registry key
  sourceDate?: string; retrievalDate?: string; page?: number;
  assumptions?: string[];
};
type Loc = {worldX:number;worldY:number; elevationM?:number};
type Asset = {id:string; kind:AssetKind; loc?:Loc; geo?:{lat:number;lon:number}; provenance:Provenance};
type Bus = Asset & {kind:'bus'; nominalKVLL:number; phases:Phase[]};
type Branch = Asset & {
  kind:'line'|'cable'|'switch'|'fuse'|'recloser';
  fromBusId:string; toBusId:string; phases:Phase[];
  lengthKm?:number; rOhmPerKm?:number; xOhmPerKm?:number;
  ampacityA?:number; closed:boolean; faulted:boolean;
  normallyOpen?:boolean; protectionZoneId?:string;
};
type Transformer = Asset & {
  kind:'transformer'; hvBusId:string; lvBusId:string;
  kvaRated:number; kvHV:number; kvLV:number; available:boolean;
  tapPercent?:number; phaseConfiguration?:string;
};
type Load = Asset & {
  kind:'load'; buildingId:string; busId:string; phases:Phase[];
  criticality:'normal'|'important'|'critical';
  profileId:string; pKW:number; qKVar:number; servedFraction:number;
};
type PV = Asset & {
  kind:'pv'; busId:string; dcKWp:number; acKWLimit:number;
  phase:Phase[]; orientationDeg:number; tiltDeg:number;
  gridFollowing:boolean; exportLimitKW?:number;
};
type Battery = Asset & {
  kind:'battery'|'community-bess'; busId:string;
  usableKWh:number; socKWh:number; minReserveKWh:number;
  chargeLimitKW:number; dischargeLimitKW:number;
  etaCharge:number; etaDischarge:number;
  gridForming:boolean; allowedIslandId?:string;
};
type Event =
  | {type:'FAULT';branchId:string;tick:number;scenarioId:string}
  | {type:'OPEN'|'CLOSE';branchId:string;tick:number}
  | {type:'REPAIR';assetId:string;tick:number}
  | {type:'IMPORT_LOSS'|'IMPORT_RESTORED';sourceId:string;tick:number};
```

All numerical quantities store **units in field names**. Store P in kW, Q in kVAr, S in kVA, E in kWh, time in hours for energy equations, V in V or kV explicitly and angles in degrees. `kVLL` explicitly means **line-to-line nominal RMS**; avoid confusion with phase-neutral voltage. All source-specific numbers must have `provenance`; **never claim phase, voltage or pole-to-property connections are actual when inferred**.

## 4. Deterministic time and physics pipeline

**Rendering:** 30–60 FPS independent from calculation. **Primary electrical tick:** 5 simulated minutes (`dtH=5/60`) or smaller when scenario requires. **Events:** immediate on simulated fault/switch/load change; recompute affected islands within next simulation microtick. Solar/cloud demand curves can be interpolated from coarse observed half-hourly zone readings. **Persistence:** store game seed, snapshot, timestep, scenario dataset hash and append-only ordered event log.

Per tick:
1. Drain ordered events, apply fault to branch, invoke abstract protective behaviour; no real switching advice.
2. Union/DFS/BFS on **closed, healthy** branches with phase compatibility, separate electrical islands; identify external grid bus or **qualified configured** local grid-forming supply for each.
3. Create per-load 5-min demand/P and Q with stochastic but deterministic seed; schedule critical/normal and interrupted equipment.
4. Compute PV from irradiance/temperature/orientation/shade; cap by inverter AC and export power and disconnect **grid-following-only** sources in dead island.
5. Dispatch external grid, available fuel generators, battery (power AND energy bounded), then shed/curtail as necessary.
6. Estimate branch P/Q flow and voltage using radial approximation (Tier 1/2); detect ampacity/transformer overload or voltage deviation, trigger controlled response rather than instantly giving every node 100%.
7. Update battery/backup fuel inventories, generator ramps, transformer thermal proxy, cost/emissions, and event log.
8. Publish immutable snapshot for rendering, overlays and downstream lights/water/sewer etc. Assert conservation and bounded SOC.

### Power balance and storage

For every island and timestep (in kW):

```text
P_import + P_gen + P_batt_discharge =
P_load_served + P_batt_charge + P_export + P_loss
```

Available-but-curtailed renewable capacity does **not** count as generated electrical energy.

For battery with `dtH` **hours** and all P in kW:

```text
SOC_next_kWh = clamp(
    SOC_kWh + charge_kW * etaCharge * dtH
            - discharge_kW * dtH / etaDischarge,
    minReserveKWh, usableKWh
)
```

Cap charging by `(usableKWh-SOC)/(dtH*etaCharge)` and discharge by `(SOC-minReserve)*etaDischarge/dtH`, in addition to kW nameplate. Export-only connection restrictions apply to *point of connection*, not magically at each generator. Household backup with transfer/isolator is a **distinct electrical island**, never an unregulated backfeed to a street.

### Approximate feeder physics (not full AC solution)

For radial branch between buses `i,j`, balanced conceptual form using **consistent per-unit bases**:

```text
P_ij = sum_downstream(load P - generation P) + losses_P
Q_ij = sum_downstream(load Q - generation Q) + losses_Q
V_j^2 ≈ V_i^2 - 2(R_ij*P_ij + X_ij*Q_ij)
```

This simplified DistFlow omits quadratic terms; incorporate losses `I^2R` and compare against full OpenDSS before defining acceptable voltage thresholds. For a 3-phase unbalanced model, use **phase-specific impedances, voltages and injections**, with coupling or an appropriate validated solver. Directly using the balanced formula on three separate phases without coupling is an acknowledged approximation, not certified distribution-system analysis.

Cross-phase transformer interactions, regulator taps and loop/ties should be either implemented by validated solver or explicitly downgraded in model confidence.

## 5. Electricity import and generation realism

Treat **upstream NEM power mix** as state-level aggregate dispatch information. Do **not** trace generation-source electricity physically to a particular house. A small town such as Menindee generally imports power from the regional grid via real documented voltage hierarchy where known; local rooftop PV, batteries, backup gensets and any documented commercial installations are separately modelled.

**Broken Hill reference**:
- X2 **220kV** upstream backbone in public reports; DAPR regional schematic shows multiple 66/33/22kV areas; do not invent one serial chain between every asset.
- BESS `50 MW / 50 MWh` is **power and energy** respectively, has a ~1-hour nominal full-rated discharge ignoring constraints/losses; connected at 22kV, not necessarily able to island by itself.
- Two `25 MVA` turbine nameplates are **apparent power**, not necessarily each 25MW continuously; factor availability, ambient derating, dispatch and power factor.
- Wind and solar nameplate are **regional plant** and are weather/connection constrained. Broken Hill 2024 outage cases involve generator/BESS restoration restrictions.

## 6. Outage / protection models

```text
HEALTHY -> FAULT_DETECTED -> TRIPPED -> ISOLATED
                                        |
                 CREW_DISPATCH -> SAFETY_CLEARANCE
                                        |
                            REPAIRED -> TESTED
                                        |
                         CONTROLLED_RECONNECT -> HEALTHY
```

- A fault on one line removes the **energised reachable network downstream**, respecting switching topology. Other source-fed islands remain powered where safe and physically configured.
- Fuses/reclosers abstract time-current protection and lockout **as configurable gameplay rules**, not actual utility settings.
- On overcurrent, low voltage or limited local generator, shed explicit noncritical demand first. Store deferred demand and cascading effects; not all normal loads may restart simultaneously.
- Critical loads have *documented/synthetic explicit* backup circuits, capacity, fuel and transfer delays; criticality doesn't fabricate generation.
- Battery/inverter grid-forming and generator black-start require eligible source and isolated/protected circuit; household grid-following solar cannot sustain dead street feeder.
- Restoration after incident is **not** auto-instant: faults isolated, repair performed, protection checked, control reclose then gradual energisation.

## 7. Actual NSW spatial world design

Each in-world light/pump/building has:
```text
world-asset-id -> meter-id -> LV service -> transformer LV bus
-> transformer HV bus -> MV feeder -> supply/substation
```

No orphaned buildings unless recorded as off-grid/fictional/no-service. Streets can have pole/underground lines and substations, with visual world meshes **generated from same assets** as solver (so visible wire is never unrelated decoration). Electrical overlay filters `transmission`, `regional HV`, `MV`, `LV`, `service`, `generation`, `solar`, `BESS`, `breaker/fault`, `voltage`, `loading`, `energy-flow`, `blackout`, `crew route`; mobile UI offers legible one-layer-at-a-time option.

GIS: NSW-hosted `Essential_Energy_Poles` point dataset exists. **Coverage, permission and reliability for Menindee must be validated under NSW-ELEC-026**. A pole point is **not** proof of wire topology or phase/transformer attachment. Never join points merely by nearest distance and label edges actual. Show `documented / inferred / synthetic` distinctly.

## 8. Deterministic acceptance fixture (all synthetic, not a claimed real NSW street)

```text
[External grid bus 22 kV]
     [MV breaker] --- [MV line]
                         |
                [100 kVA transformer] -> [LV 400 V phase A/B/C bus]
                        +---- House 1: demand variable + 6 kWp PV + 13.5 kWh battery
                        +---- House 2: demand variable, no backup
                        +---- Clinic: critical (with explicit 8 kW / 20 kWh backup)
                        +---- Streetlight: dusk-night load
```

Numbers are **test fixture only** and not actual Menindee hardware. 100kVA must constrain apparent power; a 6kWp PV array cannot necessarily export 6kW AC; house 1 battery is **not** presumed islandable across the street; clinic backup only serves its defined backup circuits.

### Required automated tests

1. Disconnect sole MV breaker: all downstream public LV load unserved; house PV must not energise dead feeder; clinic explicit isolated backup survives only according to declared SOC and circuits.
2. Feeder fault plus alternate energised but **normally open** tie: nothing backfeeds without controlled topology change; when switching correctly reconfigured, only eligible customers restore.
3. Force P/Q load near transformer kVA rating: overload threshold triggers over time, loading tracked in kVA, not simply P kW.
4. Bright solar midday: visible reverse P possible within export bounds; weak LV feeder experiences voltage-rise response, no invented infinite export.
5. Evening peak after solar ends: battery energy decays at correct power/time (include roundtrip efficiency) and reaches reserve, then sheds.
6. Long storm + gas generation unavailability + restricted community island: reproduce **broad sequence** of 2024 backup/load shedding/temporary sources/BESS reconnection, not exact confidential SCADA timeline.
7. One feeder out: unaffected feeder and independent source remain energised.
8. Day/night: streetlight energised **and** dusk sensor/on schedule required to produce light. During blackout, physical luminance disappears except true backup circuit.
9. Save/load at same tick: stable event order yields bytewise deterministic simulation snapshot, regardless of UI FPS.
10. 28 day calendar: energy imbalance integral within declared numerical tolerance; SOC never negative or exceeds usable maximum; no power unaccounted for.
11. 1,000+ synthetic building fixtures: CPU and mobile FPS thresholds specified against a real Repository Town build.
12. Evidence audit: all real-labelled assets carry source IDs and date; synthetic generated assets cannot masquerade as genuine electrical locations.

## 9. Rollout aligned to permanent tasks

**Now:** NSW-ELEC-005 building-level Registry / RTU-001, NSW-ELEC-026 GIS coverage and rights, NSW-ELEC-006 zone-demand import, NSW-ELEC-007 AEMO input. Then NSW-ELEC-008 types, 009 synthetic local network / RTU-003, 010 graph, 011 demand, 012 electrical constraints, 013 DER/BESS; 014 Broken Hill blackout replay; 015 Bawley microgrid scenario; 016 reliability; 018–020 visual and dependent services; 021 reference validation and 022 live game playtest/deployment. Detailed IDs in [TASKS.md](./TASKS.md).

**Acceptance means implementation + tests + production playtest evidence**. A polished drawing/markdown page by itself does not satisfy simulator implementation.
