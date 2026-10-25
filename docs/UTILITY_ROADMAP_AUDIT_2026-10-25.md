# Whole-utility numbered roadmap coverage audit

**Snapshot:** 25 October 2026, scoped to the 16 RT-SYS named systems in [UTILITY_SYSTEM_REGISTER.md](UTILITY_SYSTEM_REGISTER.md). Checked NSWutilities and Repository Town visible default-branch file trees and the existing RTU masterplan. **Dedicated** means stable task IDs, dependencies/ordering, concrete done-when tests and status. Broad RTU parent tasks and unrelated app task numbers are not sufficient. A partial/prototype may already have numbered work, but not a verified comprehensive implementation roadmap.

| ID | System | Coverage | Dedicated task file | Existing / remaining note |
|---|---|---|---|---|
| RT-SYS-001 | Electricity | dedicated | [Open](docs/TASKS.md) | NSW-ELEC-*; RTU-001–018 |
| RT-SYS-002 | Drinking and non-potable water | dedicated | [Open](docs/WATER_IMPLEMENTATION_TASKS.md) | NSW-WAT-001–030; RTU-019–021 |
| RT-SYS-003 | Sewerage and sanitary plumbing | dedicated | [Open](docs/SEWERAGE_TASKS.md) | RTSW-001–028; RTU-022–024 |
| RT-SYS-004 | Stormwater and flood drainage | dedicated | [Open](docs/STORMWATER_TASKS.md) | RTSM-001–030; RTU-022 interface |
| RT-SYS-005 | Gas and LPG | parent-only | — | RTU-025–027 broad tasks; no dedicated gas/LPG engineering sub-queue verified |
| RT-SYS-006 | Fixed internet and telephone | scope-only | — | RT-SYS-006 designated, no separate implementation queue |
| RT-SYS-007 | Mobile communications | scope-only | — | RT-SYS-007 designated, no separate implementation queue |
| RT-SYS-008 | Solid waste, recycling and organics | prototype-parent | — | RTU-029 cross-system and existing waste simulation, no dedicated queue verified |
| RT-SYS-009 | Fuel supply and logistics | prototype-parent | — | RTU-005/010/013/029 power/fuel interfaces, no dedicated queue verified |
| RT-SYS-010 | Roads, rail and public transport | prototype-parent | — | Existing road/rail work, no dedicated complete system-specific queue verified |
| RT-SYS-011 | Public lighting and traffic controls | existing-numbered-partial | — | Existing RLT lighting and RTU-011–015 tasks; verify depth/coverage before considering full plan |
| RT-SYS-012 | Emergency services and warning systems | prototype-parent | — | Existing emergency modules, no dedicated system-specific queue verified |
| RT-SYS-013 | Health, education and civic facilities | prototype-parent | — | Existing civic facilities, no single dedicated utility-continuity roadmap verified |
| RT-SYS-014 | Heating, cooling and thermal services | prototype-parent | — | RTU-006/012 household thermal interfaces; no dedicated HVAC roadmap |
| RT-SYS-015 | Post and parcel delivery | prototype-parent | — | Existing post/depot simulation, no dedicated system-specific roadmap |
| RT-SYS-016 | Broadcasting and public information | scope-only | — | RT-SYS-016 designation; no dedicated broadcasting implementation queue |

## Audit conclusion

- **4 of 16** have dedicated implementation queues *after this commit*: electricity, water, sewerage and now stormwater.
- **12 of 16** still lack a verified full system-specific roadmap, even though several have already-numbered RTU parent tasks, narrower RLT work or existing gameplay prototypes. This count concerns **roadmap completeness**, not whether that utility is needed for a playable town.
- **RT-SYS-005 Gas/LPG is next** in register sequence. It already has RTU-025–027 parents but needs detailed equipment/data/reference town, per-property service decision, natural-gas-versus-LPG choice, storage, leak/failure boundaries, numbered engineering child tasks and acceptance tests.
- Continue RT-SYS-006/007 fixed/mobile networks next; treat RT-SYS-016 radio/TV as a connected but distinct system. Preserve existing references: Menindee electricity, Orange water, Narromine sewer; stormwater selection remains open.
- No unowned system is automatically assigned to an agent. Review COORDINATION, source evidence and the master triage before editing gameplay.

See [machine-readable audit](UTILITY_ROADMAP_AUDIT_2026-10-25.json) and [RT-SYS register](UTILITY_SYSTEM_REGISTER.json). Status means document existence/coverage, not fully implemented utilities.
