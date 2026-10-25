# NSW-WAT — Permanent numbered implementation queue

**Date:** 25 Oct 2026. IDs `NSW-WAT-001`–`NSW-WAT-030` are new to NSWutilities. **Do not rename, edit, or renumber** the 13 original proposals in [WATER_TASKS.md](WATER_TASKS.md), nor existing `NSW-ELEC-*` or Repository Town `RTU-*`. This is a traceable implementation layer mapped onto those earlier proposals. All tasks OPEN except explicitly marked completed with evidence. Research preparation isn't an implemented gameplay feature. Priority P0 first.

| Order | ID | P | Exact deliverable | Upstream / Repository Town alignment | Acceptance |
|---|---|---|---|---|---|
| 1 | NSW-WAT-001 | P0 | Full water deep research prompt | Original water proposal 1; RTU-002 | [x] Research brief committed |
| 2 | NSW-WAT-002 | P0 | Water/electricity parity report & scope | Proposals 1, 11; RTU-002 | [x] Dated gap matrix, evidence rules |
| 3 | NSW-WAT-003 | P0 | Town-specific source evidence and choice | Proposals 6, 8; RTU-019 | [x] Provisional Dubbo reference; [ ] operating source claims independently validated |
| 4 | NSW-WAT-004 | P0 | Open source water & sewer engines audit | RTU-002 | [x] EPANET/WNTR/SWMM capability and source URLs; [ ] execute reference fixtures |
| 5 | NSW-WAT-005 | P0 | Full town water/sewer service registry | RTU-003/019/022 | [x] 234 source asset candidates with unknown service labels; [ ] actual connections/meter IDs, fixture demands and terrain |
| 6 | NSW-WAT-006 | P0 | Define pressure/tank/pipe/sewer/reuse schemas & conservation | RTU-004/019/022 | [x] Design schema and equations; [ ] validated executable schema |
| 7 | NSW-WAT-007 | P0 | Bounded deterministic fast surrogate and regression | RTU-020/023 | [x] Simple standalone graph/volume core + unit tests (after CI confirms); [ ] validated in game |
| 8 | NSW-WAT-008 | P0 | Data/source register and permissions audit | Proposals 2, 4, 13 | [x] acquisition spec; [ ] snapshot download, owner, legal reuse |
| 9 | NSW-WAT-009 | P0 | Real source/catchment/allocation evidence crosswalk | Proposals 3, 4, 6 | [ ] specific basins, allocations, drought statuses and source fixtures |
| 10 | NSW-WAT-010 | P0 | Correctly import rainfall/river/groundwater time series | Proposals 2,4; RTU-019 | [ ] reproducible timestamps, QC, missing values, unit tests |
| 11 | NSW-WAT-011 | P0 | Real site geometry & elevation provenance | Proposal 10; RTU-022 | [ ] source and permission per usable geometry; no fictional topology marked real |
| 12 | NSW-WAT-012 | P0 | Create all 234 connection decisions | RTU-003/019/022 | [ ] connected/private/not-required/unknown, evidence and water/sewer/storm distinctions |
| 13 | NSW-WAT-013 | P0 | Generate synthetic routed network and metre/valve fixture | RTU-020 | [ ] continuous supply paths; source-stamped synthetic routes |
| 14 | NSW-WAT-014 | P0 | Water volume and demand per property | RTU-019/020 | [ ] L/h, L, day/night, industry/parks and sensible demand diversity tests |
| 15 | NSW-WAT-015 | P0 | Pump/tank controls and power dependency | RTU-020; NSW-ELEC-020 | [ ] tank depletion, electricity outage, restart scenarios |
| 16 | NSW-WAT-016 | P1 | Pipe headloss/pressure and elevation approximation | RTU-020 | [ ] EPANET fixture tolerances, fail-safe on unknown pressures |
| 17 | NSW-WAT-017 | P1 | Water quality/treatment telemetry abstraction | Proposal 7; RTU-019 | [ ] CCP state, warnings not potable safety or compliance conclusion |
| 18 | NSW-WAT-018 | P1 | Stormwater independent catchment model | RTU-022/023 | [ ] rain volume, detention, flows/flood causes, separated sewers |
| 19 | NSW-WAT-019 | P0 | Property internal fixtures/toilet model | RTU-019/022 | [ ] cistern, taps, hot water, traps/vent assumptions, sewer return ledger |
| 20 | NSW-WAT-020 | P0 | Gravity sewer + lateral/manhole elevations | RTU-022/023 | [ ] invert fall, catchments, sewer connection validation |
| 21 | NSW-WAT-021 | P0 | Sewage lift stations and surcharging/overflows | RTU-023 | [ ] pump shutdown, storage, overflows, repaired service |
| 22 | NSW-WAT-022 | P1 | STP treatment and sludge/reuse destinations | RTU-023/024 | [ ] explicit treated/discharged/reused accounting and licence gating |
| 23 | NSW-WAT-023 | P1 | Materials/equipment exact public variant catalogue | RTU-008/019/022 | [ ] pump/pipe/valve/tank model, rating and visual rights |
| 24 | NSW-WAT-024 | P1 | In-game 3D pipes/works, overlays and inspector | RTU-014/021/024 | [ ] legible individual valve/pump/meter/source paths |
| 25 | NSW-WAT-025 | P1 | Legacy migration and deterministic saves | RTU-016 | [ ] unitless stocks converted once, no phantom volume or save corruption |
| 26 | NSW-WAT-026 | P1 | Named faults, repairs and cross-utility cases | RTU-028/029 | [ ] electricity/tank/pump/blockage/leak/rain gameplay acceptance |
| 27 | NSW-WAT-027 | P1 | EPANET/WNTR/SWMM offline validation | Proposal 11 | [ ] pinned versions, fixtures, error/tolerance report |
| 28 | NSW-WAT-028 | P1 | Whole town service coverage machine tests | RTU-029/030 | [ ] all 234 decisions validated, zero silent unknown connection |
| 29 | NSW-WAT-029 | P1 | Hosted mobile/desktop playtesting | RTU-030 | [ ] real live release, recorded version SHA, observed flows |
| 30 | NSW-WAT-030 | P2 | Document ongoing changes, owners and review dates | Proposal 13 | [ ] as-of date + regression and source-change log |

**Next unblocked engineering work:** NSW-WAT-012 (individual decisions) in parallel with NSW-WAT-010 (water data) and NSW-WAT-011 (open geometry/terrain). No agent should mark water 'implemented' from docs or the standalone surrogate alone. Temporary test models must carry synthetic flags. All data-provenance and public-health limitations in [architecture](WATER_SIMULATION_ARCHITECTURE.md) remain mandatory.

## Coordination with RTSW and Manus (25 October update)

A separate concurrent sewerage research programme has **RTSW-001–028** under RT-SYS-003 and RTU-022–024: [sewer research](SEWERAGE_RESEARCH_2026-10-25.md), [sewer implementation queue](SEWERAGE_TASKS.md), [system register](UTILITY_SYSTEM_REGISTER.md). It provisionally uses **Narromine** for measured wastewater/operating details, complementing the **Dubbo drinking-water and combined-utility** analogy here. The user's earlier assignment gives drinking water to Manus and sewer research to a separate ChatGPT research strand; do not claim that these teams' work has been deployed.

**Ownership rule:** NSW-WAT-019 through -022 and -026 through -029 are **interface/reference requirements** for water-to-sewer coupling. Implementation of sanitary pipes, toilets, wastewater pumps, treatment and sewer release is owned by **RTSW-003–028 / RTU-022–024** (after checking COORDINATION). NSW-WAT remains the dated water-data/evidence, potable supply, cross-network contract and validation work; mark its sewer-related requirements satisfied *by linked RTSW evidence* instead of writing duplicate gameplay code. Water model's `sewageGeneratedL` is a **synthetic catchment aggregate only** and cannot replace the RTSW per-fixture sewer ledger.
