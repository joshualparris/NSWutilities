# NSW Utilities — electricity grid research and simulation

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

## Best small-town reference found so far

**Menindee, NSW**, within the unusually documented **Broken Hill / Far West** electrical supply area. Real publicly described regional transmission/feeder connections, AGL 50 MW/50 MWh battery, 53 MW solar plant, 200 MW wind farm, backup turbines and 2024 outage restoration chronology combine with Essential Energy zone datasets. **Bawley Point/Kioloa** is an important second case for islandable community solar/battery microgrids.

This is the **best-documented initial choice among assessed candidates**, not a claim that every town has been exhaustively ranked. **No true street-level electrical circuit can be asserted from the current regional planning diagram.** A public NSW `Essential_Energy_Poles` GIS feature service has been found but coverage and permitted reuse **remain unverified**.

## Cross-repository coordination

- [Repository Town central utility masterplan, branch document](https://github.com/joshualparris/JoshMemory/blob/docs/town-utilities-rtu-001-030/repository-town/docs/UTILITIES_MASTERPLAN_2026-10-25.md)
- [Repository Town original utility plan PR #199](https://github.com/joshualparris/JoshMemory/pull/199)

The existing `RTU-001–030` labels are **not replaced or renumbered**. `NSW-ELEC-*` labels identify research, modelling and acceptance here; agents implementing Repository Town must link the appropriate original RTU task and verify current PR/branch state.

## Next step

**NSW-ELEC-005:** inspect all Repository Town buildings and non-building loads with stable references. **NSW-ELEC-026 (new P0):** separately validate public GIS pole-data licence/completeness *before* claiming geolocated service lines. Other immediate independent tasks: NSW-ELEC-006 import Essential Energy 30-minute datasets and NSW-ELEC-007 import AEMO five-minute data.

**Evidence rules:** keep source URLs, version/dates, geography, units, and factual/inferred/synthetic labels. Public documents may be copyright-restricted; use links and original 3D assets rather than re-uploading diagrams without permission. Grid physics, game approximation, and electrical-safety engineering are distinct layers.