# RTU-001 — electrical simulation baseline audit

PUBLIC engineering audit, 25 October 2026. Runtime source baseline: `19a13fe0b19f9960f8dd87e5dfcefa18670a0c82`.

**Scope complete: source, inventory and controlled Node/Three.js audit. No electrical gameplay feature was changed or deployed. Hosted production behaviour is not inferred from this audit.**

## Reproduce

In a checkout of `joshualparris/JoshMemory` at audit candidate `930cfab0adb07e661ad18f30e9df81bb0b11a0f2`, from `repository-town/`, run `npm ci --ignore-scripts`, then:

```sh
node tools/audit-electricity.mjs
node tools/audit-electricity.mjs --check
node tests/power-grid.mjs
node tests/household.mjs
node tests/lighting.mjs
node tests/directional-addresses.mjs
node tests/town-simulation.mjs
```

The generator reads the real repository-house inventory and PLACE_DEFS, builds each house's actual exterior doorway geometry, constructs every civic interior, instantiates TownLife with all houses, and executes controlled fault/save probes. No AI, browser, paid CI, live service or secrets required. `--check` regenerates in memory and rejects snapshot drift. Update evidence intentionally after runtime changes. Confirm the dependencies in the repository lockfile; this command does not install Chromium.

Outputs:

- [234-row building register](../audit/electricity/buildings.csv): existing H:/B: property IDs, physical plot addresses, demand, production/cold-chain/lighting mapping and missing services.
- [Machine-readable coverage and probes](../audit/electricity/coverage.json): door/lot geometry, all ten fault scenarios, lighting callback inspection, source-line evidence and SHA-256 fingerprints.
- [Read-only audit tool](https://github.com/joshualparris/JoshMemory/blob/930cfab0adb07e661ad18f30e9df81bb0b11a0f2/repository-town/tools/audit-electricity.mjs).

Private repository names, slugs, descriptions and brief text are excluded. House records use existing plot coordinates, not invented service meters. Generated source evidence contains only public game code. Registered farm sites and Market Square are counted as sites, not falsely described as 46 enclosed buildings. Fields, railway corridor references and planning slots do not create additional meters.

## Coverage

| Measure | Observed |
|---|---:|
| Repository-house lots | 188 |
| Civic/business/farm sites | 46 |
| Registered locations audited | 234 |
| Simulated worker household models | 99 |
| House lots without a household demand model | 89 |
| Power graph edges | 10 |
| Aggregate power customers | 7 |
| Individual physical building services/meters in graph | 0 |
| Civic interiors with registered lighting callbacks | 38 |
| Civic interiors without registered lighting callbacks | 8 |

Household assignment uses the live constructor's deterministic selection of homes. Counts are not estimates of real residents or demand. Houses have exact rendered door positions; civic site records use runtime door positions, and south-side site centres are left unknown rather than fabricated. This is an audit export, not RTU-003's operational service registry.

## Electrical consumer and asset inventory

| Existing component | Current implementation | Missing realism |
|---|---|---|
| Household loads | Per-worker fridge, freezer, lights, climate control, oven, TV, computer, washer and hot water; hourly meter and bills | Independent requested demand, all properties, appliance ratings/duty cycles, individual service and phase |
| Water Works | Specific `waterworks` customer gates refill; tank stock buffers supply | Physical motor/pump load, pipe pressure and calibrated quantities |
| Wastewater Works | Specific `sewage` customer gates treatment; backlog creates pollution | Lift-station circuits, motor loads and hydraulic network |
| Mill and bakery | Both production processes use `bakery` customer | Separate property loads/circuits; mill interior mapping disagrees |
| Foundry and plant-drink processing | `industry` gates production; soy work also depends on water | Separate motors, process profiles and service connections |
| Retail cold rooms | Six COUNTERS share `bakery`; soy processing cooler uses `industry` | Site-specific supply, calibrated thermal model and complete save state |
| Clinic | Allocated two fictional units with priority | Clinical equipment/essential-circuit behaviour and backup not modelled |
| Streetlights, exterior windows and signs | Global positive delivery flag plus time schedules | Per-feeder circuit membership and metered lamp demand |
| Registered civic lighting | Shared-shell circuit callbacks; 38 interiors can be switched off directly | Electrical load rating and correct individual customer mapping |
| Eight other civic interiors | Positive-intensity lights remain without registered callback | Explicit power connection and outage rendering |
| Repository-house interior lighting | Generated Hemisphere/Point lights | No supply callback; visible electric lighting can persist during power loss |
| Power station exterior/interior | Decorative panels, generator plant, battery racks and inverter/controller exhibits | No panel placement/output linkage, battery SOC, charging, efficiency or backup dispatch |
| Other electric-looking props and toys | Authored exhibits/radios/computers/arcades can be interactive | Not independently metered or power-gated; a prop is not evidence of a simulated electrical load |
| Wires, service meters, transformers and poles | No geographic electrical graph/asset register driving per-property supply | Voltage classes, conductor impedance, ratings, spatial routes, phase assignment and protection |

Relevant code is fingerprinted in coverage.json. `power-grid.js`, `life.js`, `household.js`, `cold-chain.js`, `store-batches.js`, `soy-chain.js`, `government.js`, `townlife.js`, `town.js`, `lighting.js`, `interior.js`, `power-interior.js`, `townpanels.js`, `main.js`, trade modules and save code were inspected. Per-site rows distinguish production, refrigeration and rendering: a single “powered” column would conceal contradictions.

## Confirmed gaps, ranked without renumbering existing RTU tasks

| Priority | Finding | Evidence / consequence | Existing implementation tasks |
|---|---|---|---|
| P0 | Missing physical connections | All 234 locations lack dedicated graph service/meter nodes; 89 house lots have no household model | RTU-003–007 |
| P0 | Requested demand collapses during blackout | Identical 99-household fixture reports 13.86 power units when supplied, zero after both household feeder cuts. `utilitiesHour` uses this result to size generation | RTU-006/007 |
| P0 | Retail outage timer lost on save | Store `coldOff=120` before snapshot, undefined after restore: two hours of cold-chain interruption disappear | RTU-016/017 |
| P1 | Global lights remain on during local feeder failure | `served > 0` drives exterior lights/signs/windows; one working customer enables town-wide electric glow | RTU-011–013 |
| P1 | Eight civic interiors lack circuit callbacks | Bakery, Market Square, Farmhouse, Railway Hotel, Foundry, Security Office, Security HQ and Locksmith retain lights in direct-off inspection | RTU-012/017 |
| P1 | Repository interiors are independently lit | Interior generator adds lights without a supply callback; household state and visible room lighting can disagree | RTU-012/017 |
| P1 | Mill's two power identities disagree | Production uses `bakery`; interior mapping uses `industry` | RTU-003/012 |
| P1 | Demand partition ignores actual household allocation | 60 west versus 39 east households in baseline; remaining aggregate load is split 50/50 rather than summed by feeder | RTU-006/007 |
| P1 | Invalid customer silently falls back | `gridPowered('not-a-service')` returns global supply status; missing mappings can look supplied | RTU-004/007 |
| P1 | Battery exhibits promise absent functionality | Battery and controller text claim solar shifting; no stored energy, charge/discharge, reserve or island state in active dispatch | RTU-008–010 |
| P2 | Generic generation and units | Daytime solar is a weather lookup; fuel provides demand remainder at one drum/15 units, no external grid or voltage/loss equations | RTU-005–010 |
| P2 | Hourly, binary service model | One-hour utility updates, immediate graph faults, full-demand binary `gridPowered`, fixed capacities and priority order | RTU-007/013/017 |
| P2 | No world utility inspection layer | Plot atlas/HUD/ledger exist, but no selectable geographic electrical/water/sewer/gas overlay | RTU-014/015 |

The eight custom interiors and the 38 callbacks were inspected as actual Three.js objects; this is not an inference from file names. A callback working directly does not prove the game passes it the correct feeder state. Decorative emissive materials, phones, room sound and individual exhibits are not all measured by light-intensity inspection; those remain downstream appliance/rendering work.

## Working systems to preserve

- Capacity-limited allocation, deterministic priority, supply/demand reconciliation and named feeder faults.
- Independent waterworks/sewage dependencies and finite storage/backlog consequences.
- Household climate, refrigeration, food spoilage, meters and bills; six retail cold rooms and soy processing cooling.
- Government repair request -> inspection/authorisation -> finite funds/parts -> worker completion -> restored feeder and event log.
- Snapshot version 2 and accepted legacy restore paths; feeder faults and power event history survive tested reload.
- Lighting intensity budgets, day/night schedules, independent civic fixtures and real movement/building geometry.

## Runtime and save observations

`utilitiesHour` runs household usage first, then computes demand/generation and redistributes supply. Thus household usage sees the preceding supply state. Solar is 25/14/18/8 fictional units for sunny/cloudy/windy/rainy, only from 07:00–18:59 inclusive by hour index. Thermal generation supplies the remaining demand if enough fuel and service health exist. There is no named coal/gas/hydro source or external NEM import/export, and “fuel drum” does not identify a fuel chemistry/energy content.

`townPowerDemands` allocates clinic 2, waterworks 4, sewage 3, bakery 5 and industry 2, then splits the remainder between west/east. Extra base facilities/lighting demand is not separately metered. Allocation sorts equal priorities by customer ID; it is not electrical impedance-based load flow. Voltage, kvar, phase imbalance, frequency, network losses, transformer loading and power quality are absent.

Save snapshots contain civic state, feeder failures, events, household state and selected place fields. Existing tests exercise v1/v2 restore and budgeted repairs. Shop `coldOff` is not in the place tuple: this new probe confirms the gap even though the existing household suite passes. This audit deliberately leaves that regression visible for implementation instead of silently patching runtime during research.

Water and sewage are coupled stock/production systems, not routed per-property pipe networks. Gas/LPG reticulation was not found in the inspected utility model. No inference about real NSW town gas supply is made.

## Verification and limits

Ten controlled probes are reproducible: healthy supply, every one of ten line faults, household demand suppression, west/east partition, water/sewer independence, unknown customer fallback, fault/event reload, retail cold-room reload, renderer source gating and mill circuit mismatch. Confirmed gaps are recorded as observed baseline behaviour, not presented as successful feature acceptance.

Existing power-grid, household, lighting, directional-address and town-simulation regressions are run separately and their terminal results recorded in `audit/electricity/validation.txt`. No browser handset, hosted-production outage, real power-flow solver, actual infrastructure survey or calibrated device wattage is claimed. This task changes audit tooling/documentation only; publishing a game build would not add the missing simulation features.

## Exact next step

**RTU-002: complete primary-source and open-code comparison before choosing voltage/equipment/solver assumptions.** Then **RTU-003** builds the operational service registry from this 234-location inventory, distinguishing requested demand from supplied load and mapping each production, refrigeration and lighting consumer to one service. Use existing property IDs and preserve save migrations. Do not retrofit real units onto fictional capacities by renaming the labels.

RTU-001 is complete as an audit when the generator/snapshot and regression evidence are published and re-read. RTU-002–030 remain open. Read the [master utility plan](https://github.com/joshualparris/JoshMemory/blob/930cfab0adb07e661ad18f30e9df81bb0b11a0f2/repository-town/docs/UTILITIES_MASTERPLAN_2026-10-25.md) for dependencies and acceptance. Research findings are also maintained in [NSWutilities](https://github.com/joshualparris/NSWutilities).
