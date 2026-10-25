# Sewerage implementation queue
25 October 2026. **RT-SYS-003**. Existing parent IDs RTU-022/023/024 are unchanged and remain open. Research children RTSW-001/002 are complete as documents; no runtime task is completed by this publication.
**Start RTSW-003**, checking concurrent NSW-ELEC-005 inventory work and COORDINATION before implementation. Coordinate with Manus for water and the dedicated ChatGPT electricity researcher. No later task is preclaimed.
Machine-readable dependencies, affected code, tests and evidence are in SEWERAGE_TASKS.json.

| ID | Priority | Task | Depends on | Status |
|---|---|---|---|---|
| RTSW-001 | P0 | Compare public NSW reference towns | None | complete-research |
| RTSW-002 | P0 | Publish sourced toilet-to-treatment architecture and current runtime gaps | RTSW-001 | complete-research |
| RTSW-003 | P0 | Inventory every actual fixture and property service mode | RTSW-002 | open |
| RTSW-004 | P0 | Reconcile water and power transaction contracts with their owners | RTSW-003 | open |
| RTSW-005 | P0 | Implement versioned sanitary schema and validation | RTSW-004 | open |
| RTSW-006 | P0 | Generate labelled synthetic terrain/inverts and service connections | RTSW-005 | open |
| RTSW-007 | P0 | Build one playable house-to-main vertical slice | RTSW-006 | open |
| RTSW-008 | P0 | Implement finite cistern, dual flush, refill and leaks | RTSW-007 | open |
| RTSW-009 | P1 | Implement trap/vent/relief and backwater failure states | RTSW-008 | open |
| RTSW-010 | P0 | Implement conservative gravity routing and storage | RTSW-006 | open |
| RTSW-011 | P0 | Add water and pollutant balance ledgers | RTSW-010, RTSW-008 | open |
| RTSW-012 | P0 | Implement wet wells, duty/standby pumps and rising mains | RTSW-011 | open |
| RTSW-013 | P0 | Wire asset-level electrical outage and backup behaviour | RTSW-012, RTSW-004 | open |
| RTSW-014 | P1 | Implement rainfall-derived infiltration and separate stormwater boundary | RTSW-011 | open |
| RTSW-015 | P1 | Implement obstructions, backpressure, surface spills and alarms | RTSW-012, RTSW-009 | open |
| RTSW-016 | P1 | Implement declared treatment/effluent/sludge scenario | RTSW-011, RTSW-013 | open |
| RTSW-017 | P1 | Add trade-waste and grease-pretreatment lifecycle | RTSW-016 | open |
| RTSW-018 | P2 | Add explicit off-sewer septic/onsite branch | RTSW-016 | open |
| RTSW-019 | P0 | Migrate saves and replay all fixture/network states | RTSW-015, RTSW-016 | open |
| RTSW-020 | P1 | Add sewer and building-plumbing inspection overlays | RTSW-015 | open |
| RTSW-021 | P1 | Render fixtures, service connections, access points and pump sites | RTSW-020 | open |
| RTSW-022 | P1 | Connect NPC routine usage and public-toilet availability | RTSW-008, RTSW-019 | open |
| RTSW-023 | P1 | Connect inspections, maintenance, repairs and tanker logistics | RTSW-015, RTSW-019 | open |
| RTSW-024 | P0 | Run pinned SWMM reference fixture comparison | RTSW-010, RTSW-012 | open |
| RTSW-025 | P0 | Run full town multi-day fault/time-acceleration regression | RTSW-019, RTSW-022, RTSW-024 | open |
| RTSW-026 | P0 | Playtest actual fixture and sewer overlay journeys | RTSW-020, RTSW-021, RTSW-023, RTSW-025 | open |
| RTSW-027 | P0 | Publish privacy-safe tested sewer release | RTSW-026 | open |
| RTSW-028 | P1 | Close sewer commissioning with evidence and limitations | RTSW-027 | open |

Dependency order is deliberate: P0 reference testing RTSW-024 starts as soon as fixtures/routing exist, not only after all graphics. Release/closure tasks cannot be skipped. Product/field sizing and standards uncertainties in the research report must be resolved where each acceptance requires them.
