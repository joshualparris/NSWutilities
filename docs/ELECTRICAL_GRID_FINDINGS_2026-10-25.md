# Electrical-grid simulation findings
Date: 25 October 2026. Classification: PUBLIC project research.
Scope: findings from the initial Repo Town utilities investigation. This is not the requested future exhaustive town-selection or source-code audit.

## 1. What is already implemented in Repo Town
Source inspected: JoshMemory commit 19a13fe0b19f9960f8dd87e5dfcefa18670a0c82.
- repository-town/src/world/power-grid.js: ten capacity-limited directed edges and seven aggregate customers: clinic, waterworks, sewage, bakery, industry, west homes and east homes.
- Integer fictional power units, not physical kW or kWh; priority allocation and feeder fault accounting exist.
- Individual buildings do not each have their own service connection in this graph.
- life.js couples electricity to utility/production behaviour.
- Existing lighting code supports power-aware interior circuits; preserve this when changing supply modelling.
These observations describe that source snapshot, not guaranteed deployed behaviour or a full runtime audit.

## 2. Real electricity supply: sourced findings
AEMO describes wholesale generation transported over transmission networks and delivered through local distribution networks [S1]. AEMC distinguishes central generation (coal, gas, hydro, wind/solar) and distributed resources including rooftop PV and storage [S2].
Consequently, the proposed town should normally have an external grid connection rather than a coal station and hydro dam placed next to shops. That is a design inference, not a surveyed fact about a selected NSW town.
A regional distribution model needs a zone substation, medium-voltage feeders, distribution transformers, LV mains and individual service connections. Voltage and equipment choices require the selected distributor's documentation. The ACT Evoenergy manual covers 11 kV, 22 kV and 400 V networks [S3]; it is a comparator, not authority for a NSW town.
Essential Energy's development guide addresses overhead/underground infrastructure, drawings and easements [S4]; actual siting must be justified against these constraints.

## 3. Proposed simulation architecture (engineering requirements, not implemented)
### Spatial network
Every building must resolve to a stable ID, coordinates, service node/meter, phase or phases, upstream transformer and feeder, or an explicit off-grid/not-required reason.
Represent overhead spans and underground routes separately, including pole/cable/transformer/switch IDs, length, voltage class, status and verified asset reference.
Use a source -> zone substation -> MV feeder -> transformer -> LV main -> service cable -> meter/switchboard hierarchy. Allow explicit normally-open ties; avoid accidental closed loops.
Render the same graph used by the solver, so decorative poles do not imply nonexistent supply.

### Electrical fidelity ladder
A capacity-allocation graph is useful but cannot establish voltage compliance, phase imbalance, reactive power or fault levels.
For increased realism, research and validate unbalanced three-phase distribution power flow, line impedance, transformer losses/taps, phase allocation, power factor, voltage-dependent load and reverse power flow. Solver selection and benchmarks are pending.
Use a separate fast operational timestep and scheduled power-flow recalculation. Keep deterministic results under time acceleration and save/reload.
Do not treat steady-state load flow as transient frequency stability or relay/protection coordination. Those require separate models and acceptance.
No claim of an exact digital twin without real topology, calibrated loads and measured validation data.

### Units and accounting
Use kW for real power, kvar for reactive power, kVA for apparent/transformer rating and kWh for stored/delivered energy. Explicitly record voltage convention (phase-neutral versus phase-phase), simulated seconds/hours and SI conversions.
Battery update: stored energy changes by charge power * duration * charge efficiency minus discharge power * duration / discharge efficiency. Define whether capacity is usable or nominal and do not apply efficiency twice.
At each interval reconcile imports + generation + battery discharge = load served + battery charging + exports + network losses, with curtailment represented separately as available but ungenerated energy.
Keep energy, fuel inventories and money independently conserved.

### Generation and demand
Use per-building use/occupancy/time profiles, diversity, appliance loads, essential loads and scenario peak assumptions. Avoid summing every appliance's nameplate as continuous demand.
Represent upstream coal/gas/hydro/wind/utility solar as a declared external scenario or sourced time series, not invented current generation and not fuel-specific electrons physically routed to a house.
A local thermal generator needs fuel, efficiency, limits and outage/ramp assumptions. Hydro requires a water/head/flow model and justified geography. Batteries are storage, not a primary energy source.
Rooftop PV requires roof suitability, module count, azimuth/tilt, irradiance/weather, temperature/derating assumptions, inverter clipping and export limits. No generation at night.

### Storage, outages and protection
Battery capacity, state of charge, power limits, reserve, efficiency and export constraints must be explicit.
Grid-following PV must not be assumed to energise a dead feeder. Model anti-islanding and a separately isolated, suitably equipped backup circuit when supported.
A home battery is not automatically a grid-forming town microgrid. Black start, grid-forming capability, synchronization and controlled reconnection are separate design requirements.
Model protective zones, opened switches, isolated faults, delayed restoration and unaffected circuits. Critical loads need explicit backup equipment/capacity/fuel; a priority number alone does not guarantee supply.
Research fault-current/relay coordination before representing specific trip behaviour as realistic.

## 4. Exact equipment candidates and evidence limits
| Candidate | Established in initial search | Still required |
|---|---|---|
| Trina Vertex S+ TSM-NEG9R.28 | Manufacturer family datasheet advertises up to 450 W [S5] | Exact power bin, dimensions, electrical ratings, roof layout and paired inverter |
| Tesla Powerwall 3, Australian variant | Official Australian technical specification page identified [S6] | Pin capacity, continuous/backup power, efficiency, inverter/phase topology and backup configuration |
| Prysmian Australian LV XLPE cable families | Manufacturer technical guide identified [S7] | Exact conductor, impedance, ampacity with installation/temperature assumptions, age/version and suitability |

Do not substitute brand names for verification. Cable ampacity depends on installation conditions; matching voltage alone is insufficient. No claim that these products are installed by Essential Energy at the fictional sites. Poles, transformers, meters and switchgear remain uncatalogued.

## 5. Lessons from simulation games
Cities: Skylines II's official electricity/water feature describes generation and wastewater infrastructure [S8]. Borrow explicit networks and readable service overlays; this initial investigation has not inspected its source code and does not classify it as open source.
Factorio's official Fluids 2.0 article describes a connected-segment model without realistic local pipe flow [S9]. Its earlier article discusses realism and throughput trade-offs [S10]. These are developer design references, not proof of an open-source electrical solver.
**Open-source game code comparison remains outstanding.** Do not present Factorio or Cities: Skylines II as open-source implementations. Future comparisons must pin repository URL, commit, licence, file paths, equations, tests and reuse compatibility.
Compare open engineering solvers separately from games: the former can serve as numerical references; the latter demonstrate pacing, overlays, repair and causal feedback. No solver has been selected or integrated.

## 6. Overlay and gameplay requirements
Mutually exclusive Electricity/Water/Sewer/Gas/Off inspection modes.
Selected network remains bright, unrelated geometry dims, underground routes become visible only in inspection mode. Colour plus text/icons must distinguish supplied, limited, isolated, faulted and planned assets.
Inspect building -> service -> LV circuit -> transformer -> feeder -> intake; show kW/kVA loading, voltage/model confidence, losses, PV generation, battery SOC and outage cause.
Real outage state must drive lights, pumping and production. A selected overlay cannot itself alter physics.
Mobile controls, stable FPS, route legibility and no poles through accessible doorways require browser acceptance.

## 7. Acceptance and unresolved research
- Full building coverage: no duplicate/missing/orphan service IDs.
- Reference-network load-flow comparison with declared tolerances, including reverse flow and unbalanced loads if implemented.
- Peak evening demand, sunny low-demand export, night, clouds, overloaded transformer, feeder outage, partial isolation, battery depletion and restoration.
- Anti-islanding and essential-circuit isolation; no magical power transfer across disconnected edges.
- 28-day energy accounting, bounded SOC, deterministic save/reload and old-save migration.
- All numerical ratings trace to a source or explicitly labelled synthetic assumptions.
- Live public release fingerprint, actual overlay walk-through and real appliance outage acceptance.
- Select the NSW reference town only after comparing public asset/planning/reliability/microgrid documentation and available topology/load data. Do not claim any town is the best documented yet.
- Finish NSW-specific electrical, water, sewer and gas research; initial source discovery is not exhaustive.

## Sources
Initial web retrieval: 25 October 2026. Product/model versions must be pinned during catalogue work.
- [S1 AEMO: About the NEM](https://www.aemo.com.au/energy-systems/electricity/national-electricity-market-nem/about-the-national-electricity-market-nem)
- [S2 AEMC: Electricity system](https://www.aemc.gov.au/energy-system/electricity/electricity-system)
- [S3 Evoenergy overhead distribution design manual, ACT comparator](https://www.evoenergy.com.au/-/media/Project/Evoenergy/EVO/Documents/Manuals/PO07132-Overhead-Line-Distribution-Design-Manual.pdf)
- [S4 Essential Energy development guide](https://www.essentialenergy.com.au/-/media/Project/EssentialEnergy/Website/Files/Partners/DA-guide.pdf)
- [S5 Trina TSM-NEG9R.28 family datasheet](https://static.trinasolar.com/sites/default/files/230531_Datasheet_Vertex%20S%2B_NEG9R.28_EN_2023_B_web.pdf)
- [S6 Tesla Powerwall 3 Australian specifications](https://energylibrary.tesla.com/docs/Public/EnergyStorage/Powerwall/3/InstallManual/BackupGateway/2/en-au/GUID-168E141F-1B5E-4582-8115-32C1E63E344A.html)
- [S7 Prysmian Australian technical cable guide](https://australia.prysmian.com/sites/australia.prysmian.com/files/media/documents/TechCG_2015-AU-v4_LOWRES.pdf)
- [S8 Cities: Skylines II electricity and water](https://www.paradoxinteractive.com/zh-CN/games/cities-skylines-ii/features/electricity-water)
- [S9 Factorio Friday Facts 416](https://factorio.com/blog/post/fff-416)
- [S10 Factorio Friday Facts 260](https://factorio.com/blog/post/fff-260)

## Provenance and handover
Transferred from the initial Repo Town research session; original tasks RTU-001–030 remain in the linked JoshMemory plan. This document adds an explicit fidelity ladder and validation requirements as proposed engineering work, not additional verified empirical findings.
No game code or manufacturer assets copied. No licence granted over third-party materials by listing their URLs.
Next: complete RTU-001 audit and RTU-002 source verification/code comparison; preserve uncertainty rather than inventing details.
