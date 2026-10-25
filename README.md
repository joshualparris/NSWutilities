# NSW Utilities — NSW electricity, water and utility simulation research

## Current reference towns by utility

| Utility | Working reference |
|---|---|
| Electricity | **Menindee, NSW** |
| Sewerage and sanitary plumbing | **Narromine, NSW** |
| Water supply | **Orange, NSW** |

Gas/LPG; internet/telephone/radio/mobile; waste/recycling/bin collection; and fuel supply still need reference-town selection. These are separate service-specific cases, not one merged real-town network. See the [reference-town register](docs/REFERENCE_TOWNS.md) and [new Manus water comparison](docs/TOWN_DATA_COMPARISON_2026-10-25.md). [Original Manus PDF](imports/manus/2026-10-25/Repository_Town_selection__comparative_public_wate.pdf) and [import checksums](imports/manus/2026-10-25/manifest.json) are preserved alongside the original ZIP and Markdown attachments.

**As at 25 October 2026 | Public NSW data, real grid examples, open-source game-code audit and a playable Repository Town roadmap.**

**Status:** Source-based research committed. No completed, calibrated or deployed game electricity-grid implementation is claimed by this repository.

## Start here (verified files)

1. [NSW-ELEC-001 — Exhaustive deep research prompt](docs/DEEP_RESEARCH_PROMPT.md)
2. [Regional electricity and outage findings](docs/ELECTRICITY_RESEARCH_2026-10-25.md)
3. [Actual open-source game/engineering solver code audit](docs/OPEN_SOURCE_SIMULATION_AUDIT.md)
4. [Primary-source evidence register](docs/SOURCES.md)
5. [Public pole GIS and equipment visual evidence](docs/GIS_ASSET_EVIDENCE.md)
6. [Engineering architecture, type system, equations and 12 acceptance tests](docs/SIMULATION_ARCHITECTURE.md)
7. [Numbered master work queue NSW-ELEC-001–026](docs/TASKS.md)
8. [Earlier Repository Town baseline electricity research and existing power-grid snapshot](docs/ELECTRICAL_GRID_FINDINGS_2026-10-25.md)
9. [NSW-ELEC-007 — Real AEMO five-minute data, importer and verified quality](docs/NSW_ELEC_007_AEMO_DATA.md)
10. [AEMO 20 October 2026 derived time series](data/aemo/2026-10-20/nsw_nem_dispatch_5m.csv) and [quality report](data/aemo/2026-10-20/quality_report.json)

## NSW water supply, wastewater and modelling research

The [NSW water research synthesis](docs/WATER_RESEARCH_2026-10-25.md) describes catchments, storage and allocations, treatment, water quality, distribution, wastewater and reuse, regional-town examples, data limitations and practical modelling evidence. See the companion [source register](docs/WATER_SOURCES.md) and [13 proposed validation/modelling tasks](docs/WATER_TASKS.md).

These water tasks are **proposals, not completed implementations or assigned RTU work**. Published evidence does not establish a full street-level pipe/sewer network or a calibrated engineering simulator. Keep existing `NSW-ELEC-*` and `RTU-*` task identifiers unchanged; confirm cross-repository ownership before implementation.

The [source archive](imports/NSWutilities-water-2026-10-25.tar.bz2) is kept for reproducibility. All three Markdown files were extracted from the user-supplied bundle without modification; their Git blob hashes match the uploaded originals.

## Electricity reference and separate regional comparators

**Menindee, NSW**, within the unusually documented **Broken Hill / Far West** electrical supply area. Real publicly described regional transmission/feeder connections, AGL 50 MW/50 MWh battery, 53 MW solar plant, 200 MW wind farm, backup turbines and 2024 outage restoration chronology combine with Essential Energy zone datasets. **Bawley Point/Kioloa** is an important second case for islandable community solar/battery microgrids.

This is the **best-documented initial choice among assessed candidates**, not a claim that every town has been exhaustively ranked. **No true street-level electrical circuit can be asserted from the current regional planning diagram.** A public NSW `Essential_Energy_Poles` GIS feature service has been found but coverage and permitted reuse **remain unverified**.

## Cross-repository coordination

- [Repository Town central utility masterplan, branch document](https://github.com/joshualparris/JoshMemory/blob/docs/town-utilities-rtu-001-030/repository-town/docs/UTILITIES_MASTERPLAN_2026-10-25.md)
- [Repository Town original utility plan PR #199](https://github.com/joshualparris/JoshMemory/pull/199)

The existing `RTU-001–030` labels are **not replaced or renumbered**. `NSW-ELEC-*` labels identify research, modelling and acceptance here; agents implementing Repository Town must link the appropriate original RTU task and verify current PR/branch state.

## Next step

**NSW-ELEC-005:** the RTU-001 234-site building audit is already completed and mirrored, but a detailed light/pump/rail inventory is still needed. **NSW-ELEC-007:** reproducible AEMO 20 Oct 2026 upstream NSW demand, spot price and registered generator fuel data imported with passing GitHub Actions tests; more days remain. **NSW-ELEC-006:** Essential Energy 30-minute zone data import blocked by source HTTP 403 on GitHub runner. **NSW-ELEC-026:** independently validate NSW pole GIS rights and Menindee coverage before building the realistic physical network.

**Evidence rules:** keep source URLs, version/dates, geography, units, and factual/inferred/synthetic labels. Public documents may be copyright-restricted; use links and original 3D assets rather than re-uploading diagrams without permission. Grid physics, game approximation, and electrical-safety engineering are distinct layers.

## RTU-001 baseline audit completed

[234-location electrical source/runtime audit](docs/RTU_001_ELECTRICAL_AUDIT.md), [building CSV](audit/electricity/buildings.csv), [machine-readable evidence](audit/electricity/coverage.json) and [validation log](audit/electricity/validation.txt). Runtime baseline `19a13fe`; tool/evidence candidate `930cfab` in JoshMemory PR #199. No utility feature deployed. This covers RTU-001; NSW-ELEC-005's broader per-light/pump/rail asset registry remains open rather than treating grouped loads as individually mapped assets. Preserve the independent research and NSW-ELEC-026 priority above.


## All town systems and sewerage/plumbing research

[RT-SYS-001–016 system register](docs/UTILITY_SYSTEM_REGISTER.md) gives permanent names to utilities and essential services. Electricity research remains with the dedicated ChatGPT research session; water with Manus; sewerage with this ChatGPT Work research strand. [Sewerage report](docs/SEWERAGE_RESEARCH_2026-10-25.md) selects Narromine provisionally, distinguishes installed from operating reuse hardware, and specifies toilets/cisterns, drains, pumps, treatment, faults and overlays. [Sources](docs/SEWERAGE_SOURCES.md) and [RTSW-001–028 queue](docs/SEWERAGE_TASKS.md) include provenance, code/solver references, interfaces, dependencies and acceptance tests. Only research tasks RTSW-001/002 are complete; no new sewer gameplay deployed. Next: RTSW-003 fixture inventory, preserving the existing RTU-022–024 parents and reconciling concurrent inventory work before implementation.
