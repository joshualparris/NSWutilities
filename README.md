# NSW utilities — electrical-grid simulation research
Public engineering research, transferred 25 October 2026.

## Start here
This repository collects sourced findings for a realistic NSW-inspired town electricity simulation.
**Status: preliminary research and design requirements, not an implemented or validated electrical network.**
No NSW town has yet been proved to have the most complete public documentation. No real feeder topology, equipment placement or live generation mix is asserted here.

- [Electrical simulation findings](docs/ELECTRICAL_GRID_FINDINGS_2026-10-25.md)
- [Repository Town utility plan and original RTU-001–030 IDs](https://github.com/joshualparris/JoshMemory/blob/docs/town-utilities-rtu-001-030/repository-town/docs/UTILITIES_MASTERPLAN_2026-10-25.md)
- [Original plan PR #199](https://github.com/joshualparris/JoshMemory/pull/199)

## Next work
1. Complete the building/consumer audit (existing RTU-001).
2. Complete primary-source research, exact equipment datasheets and game-code comparison (RTU-002).
3. Build the per-building service registry (RTU-003) before network sizing and runtime implementation.
Keep the existing RTU IDs; this research repo does not imply their implementation is complete.

## Evidence rules
Record source URL, publication/version, retrieval date, geography and units for each dataset.
Separate verified source statements, inferred design choices and synthetic scenario inputs.
Use public documents; never present an inferred network as a distributor's actual asset register.
Manufacturer families are candidates until the exact Australian variant and datasheet are pinned.
Game simulation, engineering power flow and electrical protection analysis have different validation needs.
