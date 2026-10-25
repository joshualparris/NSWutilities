# Water versus electricity — evidence and implementation parity audit

**Reviewed 25 October 2026.** Repository: NSWutilities `main`, cross-read with JoshMemory/Repository Town default branch. This report assesses *existing completed work*, not proposed features. Reference documents: [electricity architecture](SIMULATION_ARCHITECTURE.md), [electricity tasks](TASKS.md), [water synthesis](WATER_RESEARCH_2026-10-25.md), [water proposals](WATER_TASKS.md), [Repository Town utility plan](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/UTILITIES_MASTERPLAN_2026-10-25.md).

| Evidence dimension | Electricity found | Water before parity work | Response | Remaining gap |
| --- | --- | --- | --- | --- |
| NSW regulatory/supply research | Detailed source register + geographic analysis | 25.7 kB narrative + 41-source list | Retain and extend with Dubbo 2026 references | Every live operating detail needs verification |
| Geographic reference | Menindee/Broken Hill and Bawley case | Multiple regional examples but no selected end-to-end benchmark | Dubbo municipal drinking-water/wastewater **documentary analogue**, not actual town topology | Actual service routes/security/licence |
| Cross-component physics | Explicit kW/kWh, graph, faults, approximate voltage | No shared model equations/schema | [Water architecture](WATER_SIMULATION_ARCHITECTURE.md) + [reference model](../src/water/water-core.mjs) | EPANET/SWMM full hydraulics, calibrated curves |
| Source/code review | Micropolis, Simutrans, Mindustry, OpenDSS etc | Source-listed but not comparative | [Open model audit](WATER_OPEN_SOURCE_AUDIT.md) | Benchmark solver execution |
| Property coverage | 234 locations; 188 houses, 46 sites in RTU-001 | No property-level water/sewer records | 234-entry cross-service [inventory](../audit/water/building-service-inventory.json) from same baseline | Connections, meters, elevations unknown |
| Measurable data | AEMO 5-minute CSV + importer/test | Static research and dashboards | [data acquisition spec](WATER_DATA_AND_EVIDENCE.md) | No live licensed import verified yet |
| Tasks | Numbered NSW-ELEC-001+ with gates | 13 proposals without stable project IDs | [NSW-WAT-001…](WATER_IMPLEMENTATION_TASKS.md) preserving original 13 proposals | Most tasks remain open |
| Automated test | Electrical test specification and source snapshots | No water flow tests | Portable deterministic reference tests + CI | Town-game integration not yet tested |
| Live game | Partial aggregated power, no per-building grid | Aggregate water stock + sewage backlog | Explicit migration mapping and RTU-019…024 crosswalk | Runtime water, pipes, sewer and UI still NOT implemented |

## Observed Repository Town state (source inspection)

At `repository-town/src/world/life.js` lines ~692–719 on 25 October: `utilitiesHour` adds a **fictional 25 stock units/hour** if `gridPowered('waterworks')`, caps waterworks stock at **250**; required demand `round(9 + daytime3 + homes.water)`, delivered `min(demand,stock)`, and synthetic sewage `floor(got*0.8)`; wastewater plant deletes up to **22 stock units/hour** when powered; if stock >70 it adds pollution. These are **unitless gameplay tokens, NOT litres, kilolitres, physical wastewater or water quality**. The civic `waterOk` is town-wide. Current `power-grid.js` has separate waterworks/sewage electrical customers but no distribution service pipes. Treat this gameplay legacy as valid baseline behaviour; migrate with a versioned adapter, not by silently reinterpreting numbers.

`audit/electricity/coverage.json` contains 234 locations (188 house records, 46 sites), 99 modelled and 89 unmodelled household lots, **zero real physical service connections**. The new water inventory reuses the stable IDs/coordinates as *candidates only*: all water, sanitary, storm and trade connections are unknown pending audit. Not all lots should be presumed to require reticulated service; off-grid, vacant, public toilet, stormwater-only and commercial trade-waste situations require explicit decisions.

## Reference geography and confidence

**Preferred documentary benchmark for combined water+wastewater: Dubbo, NSW.** Council describes Macquarie River (~70% typical) and South Dubbo borefield (~30% typical, seven bores) contributing to Dubbo supply, John Gilbert WTP, and service reservoirs. **These are townwide historical/typical shares** published by Council, not a per-hour measured model input. Water infrastructure is different for Wellington and neighbouring villages. Council publishes environmental licence/monitoring for John Gilbert and Dubbo STP. A Council/Squadron Energy news item dated **8 September 2026** says a new advanced wastewater facility was completed, capacity *up to 700 ML/year*, while approval for dust suppression/concrete batching **was still in process** at the report date. Do not model completed approvals or potable reuse from that article.

**Secondary comparisons:** Orange (stormwater source diversification), Cobar–Nyngan (bulk pipeline), Broken Hill (remote supply complexity). Each has relevant evidence but less convenient published *combined* water/sewerage reference for our existing game's waterworks and wastewater works than Dubbo. This is a *project-fit selection*, not an exhaustive national evidence ranking.

References:
- Dubbo Regional Council water/sewer responsibilities: https://www.dubbo.nsw.gov.au/Our-Region-Environment/Water-Sewerage-and-Drainage/councils-water-and-sewer-obligation
- Dubbo 8 September 2026 recycled facility notice: https://www.dubbo.nsw.gov.au/news-and-media/news-and-resources/council-news/2026/water-security-a-reality-with-completion-of-advanced-wastewater-treatment-plant
- NSW Health drinking water utility requirements: https://www.health.nsw.gov.au/environment/water/Pages/water-utilities.aspx
- NSW plumbing code and standards advisory: https://www.nsw.gov.au/housing-and-construction/compliance-and-regulation/plumbers-and-drainers/standards-and-notes

## Explicit definition of parity

**Document/engineering-specification parity** requires: sourced geography, algorithms/units, system diagram, distinct wastewater/stormwater, code audits, 12+ acceptance scenarios, stable tasks and sources, asset inventory and honest limitations. **Runtime parity** requires property-level service graph, pipe/valve/pressure approximation, sewage gravity/overflow/pumps, coherent water/electricity coupling, acceptance suite and verified deployed gameplay. This commit can advance the former but must not be called the latter.
