# NSW electricity research and implementation queue

**Date:** 2026-10-25  
**Scope:** `NSW-ELEC-*` tracks research/reference-model work in **NSWutilities**. This is **not a renumbering** of the existing `RTU-001` through `RTU-030` tasks in Repository Town's masterplan; these new IDs cover the source/reference research and validation strand. Implementation in Repository Town must link the matching RTU ID and avoid duplicate agent ownership.  
**Prioritisation:** P0 = blocks useful simulation; P1 = realism essentials; P2 = expansion. Claim one task at a time with branch/issue and completion evidence.

| Order | Permanent ID | Priority | Task | Prerequisite | Done when |
|---|---|---|---|---|---|
| 1 | NSW-ELEC-001 | P0 | Publish exhaustive research prompt | None | [x] `DEEP_RESEARCH_PROMPT.md` committed |
| 2 | NSW-ELEC-002 | P0 | Select town and document electrical evidence matrix | 001 | [x] **Provisional** Menindee / Broken Hill selection with candidate matrix; [ ] verify exhaustive stronger alternatives |
| 3 | NSW-ELEC-003 | P0 | Compile primary source evidence and map backed regional topology | 002 | [x] first-pass 30 sources and published regional schematic; [ ] fully reconcile Menindee voltages and actual service specifics |
| 4 | NSW-ELEC-004 | P0 | Audit at least three actual open-source games and three engineering engines | 001 | [x] original Micropolis `s_power.c`, Simutrans `powernet.cc`/`leitung2.cc`, Mindustry `PowerGraph.java` inspected; [ ] run source and licence integration verification |
| 5 | NSW-ELEC-005 | P0 | Audit Repository Town's current electrical assets and all buildings | 003 | [ ] machine-readable audit mapping each building, light, pump, rail, etc to stable ID; cross-ref **RTU-001** |
| 6 | NSW-ELEC-006 | P0 | Import historical Essential Energy zone-substation power series | 003 | [ ] data pipeline + interval quality report, AEST handling, CSV schema, plots and tests |
| 7 | NSW-ELEC-007 | P0 | Import real AEMO market and generation profiles | 003 | [ ] reproducible 5-minute snapshots and NEM source mix (regional not building attribution) |
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

## Cross-repository rules

- Existing Repository Town `RTU-001–030` tasks live in [utilities masterplan PR #199](https://github.com/joshualparris/JoshMemory/pull/199) as referenced by the NSWutilities README. **Check whether that PR is merged before using that branch link as the canonical task state.**
- Do not invent missing RTU numbers or edit their existing identifiers.
- Each NSW-ELEC issue/PR must link the corresponding RTU task if its implementation modifies Repository Town.
- Source provenance classification: **documented**, **inferred**, **synthetic**; each item stores `source_id`, as-of date, confidence and document page.
- Completion means code/tests/commits as applicable, not merely a plan.
- Currently **only first-pass research is verified committed**. No zone time series download, real building registry, working power simulation or production gameplay verification has occurred in this run.

## Next agent's immediate instruction

**Start NSW-ELEC-005**: inspect Repository Town's latest default branch and utility masterplan, enumerate *all* actual buildings and municipal loads, export a stable CSV/JSON asset list with grid references and accurate world coordinates, cross-check with scene data, and post unit tests or an audit fixture. In parallel, **NSW-ELEC-006** is data-only and can be assigned independently to another agent. Do not assign implementation to agents currently working on the same RTU IDs.
