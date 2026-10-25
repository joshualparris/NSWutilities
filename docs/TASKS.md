# NSW electricity research and implementation queue

**Date:** 2026-10-25
**Architecture:** [Detailed types, physical approximations, outage logic and tests](./SIMULATION_ARCHITECTURE.md)  
**Scope:** `NSW-ELEC-*` tracks research/reference-model work in **NSWutilities**. This is **not a renumbering** of the existing `RTU-001` through `RTU-030` tasks in Repository Town's masterplan; these new IDs cover the source/reference research and validation strand. Implementation in Repository Town must link the matching RTU ID and avoid duplicate agent ownership.  
**Prioritisation:** P0 = blocks useful simulation; P1 = realism essentials; P2 = expansion. Claim one task at a time with branch/issue and completion evidence.

| Order | Permanent ID | Priority | Task | Prerequisite | Done when |
|---|---|---|---|---|---|
| 1 | NSW-ELEC-001 | P0 | Publish exhaustive research prompt | None | [x] `DEEP_RESEARCH_PROMPT.md` committed |
| 2 | NSW-ELEC-002 | P0 | Select town and document electrical evidence matrix | 001 | [x] **SCOPED COMPLETE:** transparent 8-candidate primary-source decision matrix selects small-town Menindee, with Kioloa microgrid benchmark. [Decision and alternatives](./NSW_ELEC_002_TOWN_SELECTION.md). **Not a universal ranking of every NSW town.** |
| 3 | NSW-ELEC-003 | P0 | Compile primary source evidence and map backed regional topology | 002 | [x] **REGIONAL RESEARCH COMPLETE:** verified Menindee **66/22kV** and **5B1:SUN 66kV** connection from official 2025 DAPR p53; 20 labelled regional reference nodes / 13 schematic links, 2024 outage, battery. [Detailed evidence](./NSW_ELEC_003_VERIFIED_TOPOLOGY.md) · [JSON](../data/menindee_regional_reference_2025.json). [ ] Actual street-by-street poles/phases/service links not published/verified (NSW-ELEC-024/026, RTU-003). |
| 4 | NSW-ELEC-004 | P0 | Audit at least three actual open-source games and three engineering engines | 001 | [x] **SOURCE+LICENCE AUDIT COMPLETE:** Micropolis/Simutrans/Mindustry and pandapower/PyPSA/GridLAB-D actual solver files/licences traced with source SHAs. [Comparison](./NSW_ELEC_004_SOLVER_CODE_AND_LICENSE.md). [x] live CI two-solver **pandapower 3.5.6 / PyPSA 1.2.4 AC benchmark PASS** with matched losses/voltage ([exact result](../data/solver_benchmarks/002bus_11kv_result.json)); [ ] GridLAB-D binary build and licence compatibility before direct reuse (not needed for this source-code audit). |
| 5 | NSW-ELEC-005 | P0 | Audit Repository Town's current electrical assets and all buildings | 003 | [x] **RTU-001 building/site audit finished** with 234-site CSV/JSON, 188 houses + 46 other sites and 10 probes; [ ] **NSW-ELEC-005 full asset inventory still requires individual light/pump/rail asset identifiers**. Individual service meters remain zero (RTU-003). **Treat 005 as already being worked on rather than unclaimed** |
| 6 | NSW-ELEC-006 | P0 | Import historical Essential Energy zone-substation power series | 003 | [ ] **BLOCKED**: published 2024-25 combined ZIP returned HTTP 403 in GitHub Actions; verified failure run 40152890078; alternative access and licence/date checks still required |
| 7 | NSW-ELEC-007 | P0 | Import real AEMO market and generation profiles | 003 | [x] **one verified 20 Oct 2026 day**, 288 NSW demand/price records + generator SCADA DUID-to-fuel group; source SHA256 + CI + regression tests. [ ] multiple dates, final fuel registry chronology; [research/data evidence](./NSW_ELEC_007_AEMO_DATA.md) |
| 8 | NSW-ELEC-008 | P0 | Draft canonical node/edge/phase/transformer/storage schemas with source provenance | 005 | [ ] JSON Schema/TS types; tests for ID uniqueness, phase connection, upstream edges |
| 9 | NSW-ELEC-009 | P0 | Generate *labelled synthetic* Menindee-scale LV network using NSW conventions | 006,008 | [ ] poles, distribution transformers, service drops and building registry connected with deterministic fixture tests; cross-ref **RTU-003** |
| 10 | NSW-ELEC-010 | P0 | Implement fast network topology and island recomputation | 008,009 | [ ] branch open/close, recomputed sources, phase-aware reachability and loop guards; cross-ref RTU task |
| 11 | NSW-ELEC-011 | P0 | Implement dispatch and demand curves from real data | 006,007,010 | [ ] conservation of energy, varying loads per building, validated time zones |
| 12 | NSW-ELEC-012 | P0 | Implement line loading, transformer limits, voltage drop and losses | 010,011 | [ ] per-branch ampacity, bounded numerical algorithm, benchmark/reference comparison |
| 13 | NSW-ELEC-013 | P0 | Model PV inverters, battery SOC and anti-islanding restrictions | 011,012 | [ ] solar irradiance, export, conversion loss, kW/kWh caps, daylight/shade, backup behaviour tests |
| 14 | NSW-ELEC-014 | P1 | Reproduce Oct 2024 Broken Hill–Menindee grid loss/restoration as event simulation | 012,013 | [ ] deterministic timeline/outage effect/load shedding/source switching; compare documented broad chronology |
| 15 | NSW-ELEC-015 | P1 | Reproduce Bawley Point/Kioloa renewable island microgrid | 013 | [ ] 3 MW/approx 3 MWh scenario; Kioloa automation vs other operator restoration status verified against latest dated newsletter |
| 16 | NSW-ELEC-016 | P1 | Implement failure/weather and restoration state machines | 012 | [ ] protection boundaries, rain/wind/heat, isolated repair/reclose and crew priority tests |
| 17 | NSW-ELEC-017 | P1 | Exact dated Australian solar, inverter, battery and transformer product registry | 003 | [ ] manufacturer PDF/model/version/electrical rating/appearance/licence per device; no unsourced placements |
| 18 | NSW-ELEC-018 | P1 | 3D poles, wires, service drop, transformer and rooftop PV representation | 009,017 | [ ] NSW-scaled in game, game camera and wiring physical conventions, no floating wires |
| 19 | NSW-ELEC-019 | P1 | Toggle overlays (HV/MV/LV, voltages, load, source, storage, protection) | 010,012 | [ ] independent toggles, labels, directions, colours and legible phone performance |
| 20 | NSW-ELEC-020 | P1 | Integrate actual night-time lights, businesses, water, sewerage and rail consequences | 013,016,019 | [ ] live fixtures prove individual building/lighting outcomes on outages |
| 21 | NSW-ELEC-021 | P1 | Compare runtime surrogate to OpenDSS/pandapower reference feeders | 012 | [ ] error tolerances quantified in fixture report; never claim certified powerflow based on a flood-fill |
| 22 | NSW-ELEC-022 | P1 | End-to-end automated, gameplay, mobile and deployment acceptance | 014–021 | [ ] scenarios pass, performance budget met, actual deployed game verified |
| 23 | NSW-ELEC-023 | P2 | Fuel logistics, generator operation, emissions, repair costs and procurement | 016 | [ ] data-grounded scenarios, dispatch/run-time/fuel limits |
| 24 | NSW-ELEC-024 | P2 | Street-by-street real asset mapping from legally accessible evidence | 003,009 | [ ] clear evidence for each validated asset; retain synthetic placeholders elsewhere |
| 25 | NSW-ELEC-025 | P2 | Expand utility-engine pattern to gas, water and wastewater cross-dependencies | 020 | [ ] separate fluid-flow reference model and blackout effects on pumping |

| 26 | NSW-ELEC-026 | **P0** | **Validate public NSW Essential Energy poles GIS layer for Menindee, coverage, rights and freshness before spatial import** | 002,003 | [ ] aggregate locality count / scope and licence documented; non-sensitive map geometry compared with roads; missing areas remain labelled synthetic |

**Triage amendment, 25 October:** NSW-ELEC-026 is newly discovered P0; its identifier is appended to preserve every previous ID. Agents should execute it **immediately after NSW-ELEC-005** and *before* NSW-ELEC-009. The work queue's table order is not the total priority ordering after this amendment; use this explicit dependency note. See [GIS_ASSET_EVIDENCE.md](./GIS_ASSET_EVIDENCE.md).

## Cross-repository rules

- Existing Repository Town `RTU-001–030` tasks live in [utilities masterplan PR #199](https://github.com/joshualparris/JoshMemory/pull/199) as referenced by the NSWutilities README. **Check whether that PR is merged before using that branch link as the canonical task state.**
- Do not invent missing RTU numbers or edit their existing identifiers.
- Each NSW-ELEC issue/PR must link the corresponding RTU task if its implementation modifies Repository Town.
- Source provenance classification: **documented**, **inferred**, **synthetic**; each item stores `source_id`, as-of date, confidence and document page.
- Completion means code/tests/commits as applicable, not merely a plan.
- Research, the 234-site source-derived inventory and an AEMO one-day source-backed CSV/quality-report import have been verified. Essential Energy historical substation loads remain blocked (403). A full building electrical-service registry, working realistic physical power flow and production gameplay verification remain **unimplemented**.

## Next agent's immediate instruction

**Next available: NSW-ELEC-026**, then NSW-ELEC-008 and -009 with their prerequisites. NSW-ELEC-005 has a completed 234-site baseline, but a truly exhaustive separate inventory of streetlights, pumps and railway electricity assets still needs to be finished; do not duplicate an agent already owning this extension. NSW-ELEC-007 has one real AEMO sample day and reusable importer; additional historic days remain an enhancement. NSW-ELEC-006 should be separately unblocked using licensed Essential Energy data. Do not assign implementation to agents currently working on the same RTU IDs.
