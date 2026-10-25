# RT-SYS-004 — Stormwater & flood drainage implementation roadmap

**Date:** 2026-10-25. Permanent child IDs RTSM-001–030, new and separate from pre-existing RTSW sewerage, NSW-WAT water, NSW-ELEC electricity and RTU-001–030 town parent IDs. RTU-022 covers stormwater/sanitary separation; RTU-029/030 cover cross-utility acceptance. No previous IDs changed, and publishing a task is **not** implementation. The work is **not assigned** to an AI agent yet; check COORDINATION before code edits.

**Next unblocked implementation task: RTSM-003** (234-site roofs/pits/outfalls audit), in parallel with **RTSM-004** (reference-town selection) and **RTSM-007** (rainfall data definitions). Scope begins with full asset audit and synthetic designs; do **not** place actual public infrastructure geometry without verified licence/accuracy.

| Priority order | Permanent ID | Priority | Scope | Depends on | Related existing parent | Status | Done when |
|---|---|---|---|---|---|---|---|
| 1 | RTSM-001 | P0 | Publish primary NSW stormwater source register and evidence boundary | None | RTU-002 | research-doc-complete | Dated URLs, provenance rules, documented aggregate counts; no fabricated GIS |
| 2 | RTSM-002 | P0 | Specify distinct stormwater, overland, sanitary and potable architecture | RTSM-001 | RTU-004/022 | research-doc-complete | Versioned schemas, physics limits and 22 explicit acceptance cases |
| 3 | RTSM-003 | P0 | Audit 234 Repository Town roofs, roads, gutter outlets, existing pits and open drains | RTSM-002 | RTU-003 | open | Machine-readable per-asset ID, world position, mode and uncertainty; no silent house connection |
| 4 | RTSM-004 | P0 | Select best documented NSW stormwater reference using scored town evidence matrix | RTSM-001 | RTU-002 | open | At least Dubbo/Orange/third town, drainage/flood reports, licences, freshness and documented limitations |
| 5 | RTSM-005 | P0 | Validate public council/flood GIS, datum, privacy and redistribution licence | RTSM-004 | RTU-003/022 | open | Metadata and reuse rights per feature; unavailable geometry remains synthetic |
| 6 | RTSM-006 | P0 | Create synthetic terrain elevation / invert / overland direction model | RTSM-003 | RTU-022 | open | Stable elevations and no uphill gravity edges; synthetic labels; measured inverts not invented |
| 7 | RTSM-007 | P0 | Build observed rainfall and design IFD/ARR dataset provenance matrix | RTSM-001 | RTU-022 | open | Station/site/date/units/AEP and ARR inputs; no observed/design conflation |
| 8 | RTSM-008 | P0 | Implement rainfall ingestion with UTC time, DST, mm vs mm/h and missing-value tests | RTSM-007 | RTU-029 | open | Repeatable versioned fixtures with event depth and interval quality report |
| 9 | RTSM-009 | P0 | Derive roof/road/lot catchments, areas and impervious fractions per site | RTSM-003, RTSM-006 | RTU-003/022 | open | Reconciled areas; pervious/impervious distinction; each of 234 addressed |
| 10 | RTSM-010 | P0 | Generate deterministic synthetic storm graph (pits, gutters, pipes, culverts, outfalls) | RTSM-005, RTSM-006, RTSM-009 | RTU-022 | open | All chosen nodes connected or explicit unknown; geometry overlays align with graph |
| 11 | RTSM-011 | P0 | Implement runoff / infiltration / evap / depression-storage volume ledger | RTSM-008, RTSM-009 | RTU-029 | open | Conservation within tolerance, no double count of rainfall, all units explicit |
| 12 | RTSM-012 | P1 | Implement rainwater roof tanks and legal site capture / overflow paths | RTSM-011 | RTU-019/022 | open | Finite tank volume, rainwater separate from potable/reuse approvals |
| 13 | RTSM-013 | P0 | Implement inlet, pipe/culvert capacity, detention and bypass into surface | RTSM-010, RTSM-011 | RTU-022 | open | Excess water visible and conserved; shared pipe bottlenecks accounted |
| 14 | RTSM-014 | P1 | Model receiving water and high-tailwater drainage restriction | RTSM-013 | RTU-022 | open | Blocked outfall scenario and explicit upstream ponding, no invented river sensor |
| 15 | RTSM-015 | P0 | Build offline SWMM reference fixtures and numerical comparison | RTSM-007, RTSM-013 | RTU-022/030 | open | Pin solver SHA/version, run synthetic .inp, publish error/tolerance report |
| 16 | RTSM-016 | P1 | Implement green infrastructure: swales, raingardens, infiltration and retention | RTSM-011, RTSM-013 | RTU-022 | open | Saturation and retention state; volume ledger reconciles |
| 17 | RTSM-017 | P1 | Implement gross pollutant traps, build-up/capture and service removal | RTSM-013 | RTU-029 | open | Separate pollutant ledger and waste disposal maintenance task; not full water quality approval |
| 18 | RTSM-018 | P1 | Implement retarding basin, release gate and overflow spill routing | RTSM-013 | RTU-022 | open | Finite capacity/outlet, correct downstream effect and staged recovery |
| 19 | RTSM-019 | P0 | Implement surface ponding and flood proxy with mapped building/road consequences | RTSM-006, RTSM-013 | RTU-029 | open | Visible flood extent with modelled/uncertain depth and threshold; no safety claim |
| 20 | RTSM-020 | P0 | Bridge only explicit sanitary infiltration/inflow defects to RTSW sewer engine | RTSM-011, RTSM-019 | RTU-022/023 | open | One transfer debited from storm and credited to sewer, no gutters-to-toilets plumbing |
| 21 | RTSM-021 | P1 | Bridge separately authorised stormwater harvesting to NSW-WAT water service | RTSM-012, RTSM-016 | RTU-019/020 | open | Nonpotable and treatment/permit gating, finite water and single delivery |
| 22 | RTSM-022 | P1 | Wire powered stormwater pumps and sensors to actual electrical circuits | RTSM-013 | RTU-012/029 | open | Blackout stops only powered equipment; gravity network still routes runoff |
| 23 | RTSM-023 | P1 | Render matched 3D street gutters, inlets, drains, headwalls and basins | RTSM-010, RTSM-019 | RTU-014 | open | Every visible asset has matching network ID, collision/door access and phone checks |
| 24 | RTSM-024 | P1 | Add Stormwater/Surface overlay, property inspector and fault explanations | RTSM-013, RTSM-023 | RTU-014 | open | Layers separate water/sewer/electricity, colourblind/mobile controls |
| 25 | RTSM-025 | P1 | Connect roof/yard/footpath/shop flooding, pumps and NPC building consequences | RTSM-019, RTSM-024 | RTU-029 | open | Per-building paths and thresholds; no townwide magic water availability |
| 26 | RTSM-026 | P1 | Model route disruption, road/rail crossing closures and recovery logic | RTSM-019, RTSM-025 | RTU-029 | open | Directed road closure/flood retreat, no unsupported live public warning |
| 27 | RTSM-027 | P1 | Add maintenance crews, blocked drains, pit cleanouts, parts, costs and alarms | RTSM-017, RTSM-019 | RTU-028 | open | Finite labour/parts, condition recovery, debris disposal and auditable logs |
| 28 | RTSM-028 | P0 | Version saved stormwater state and deterministic multi-event replay | RTSM-011, RTSM-013, RTSM-020 | RTU-016 | open | Legacy save intact, fixed seed/time, no duplicated rainfall or phantom stores |
| 29 | RTSM-029 | P0 | Full CI, mobile/game playtest and verified public deployment | RTSM-015, RTSM-020, RTSM-024, RTSM-028 | RTU-030 | open | 22 scenario cases, source SHA, Android/desktop actual hosted behaviour verified |
| 30 | RTSM-030 | P2 | Publish validation, limits, change log and maintain source/data freshness | RTSM-029 | RTU-030 | open | Independent limits, licence status, model assumptions and unresolved unknowns linked |

## Ownership / non-overlap

- RTSM owns stormwater source-to-outfall and overland flood *game simulation* only.
- **RTSW-001–028** own sanitary plumbing/wastewater, not gutter drains; transfer I&I once via explicit defect interface.
- **NSW-WAT-001–030** own source/treated household water and any permitted stormwater harvest interface; Orange remains selected *water* reference.
- **NSW-ELEC** owns power circuit/pump feed and electric network physics.
- Existing RTU, lighting, road/rail and Repository Town gameplay work must be coordinated before touching src/world or scene/camera assets.
- The stormwater **reference town is not yet formally selected**. Dubbo is a documentary starting example, not a claim that Repository Town depicts its exact system.

## Definition of completion

A planning document alone can complete RTSM-001 or -002 research publications only. Any executable/scene integration task requires committed code, validation logs, regression tests and a recorded game/playtest source SHA. "All utilities complete" requires preserved compatibility with existing power/water/sewer saves and deployment. See [research](STORMWATER_RESEARCH_2026-10-25.md), [architecture](STORMWATER_ARCHITECTURE.md), [sources](STORMWATER_SOURCES.md), and [machine-readable tasks](STORMWATER_TASKS.json).
