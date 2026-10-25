# Repository Town utilities and essential-service designations
PUBLIC project register. 25 October 2026. Stable system IDs, not completion claims or a renumbering of existing tasks.
Electricity research remains with the user's ChatGPT electricity research session. Drinking-water research remains with Manus. This session covers sewerage/plumbing research only. These are the user's stated assignments, not confirmation of another agent's progress.

| System ID | System | Category | Research ownership | Existing work / scope |
|---|---|---|---|---|
| **RT-SYS-001** | Electricity | utility | ChatGPT electricity deep-research session | RTU-001–018; Grid, generation, solar, storage, meters, circuits, faults and restoration |
| **RT-SYS-002** | Drinking and non-potable water | utility | Manus (user-assigned) | RTU-019–021; Sources, treatment, storage, pressure, mains, meters, hydrants; separately labelled reclaimed supply |
| **RT-SYS-003** | Sewerage and sanitary plumbing | utility | ChatGPT Work sewerage research (this session) | RTU-022–024; Toilets/cisterns, traps/vents, drains, laterals, gravity sewers, lift stations, treatment, effluent and biosolids |
| **RT-SYS-004** | Stormwater and flood drainage | utility | Unassigned | RTU-022 interface; dedicated implementation unassigned; Roof downpipes, street pits, culverts, detention and receiving waters; separate sanitary network |
| **RT-SYS-005** | Gas and LPG | utility | Unassigned | RTU-025–027; Reticulated gas only where evidenced, or bottles/bulk LPG, regulators, meters and appliance supplies |
| **RT-SYS-006** | Fixed internet and telephone | utility | Unassigned | No existing dedicated RTU parent; NBN access technologies, premises terminals, exchanges/cabinets, backhaul and backup power |
| **RT-SYS-007** | Mobile communications | utility | Unassigned | No existing dedicated RTU parent; Towers, radios, backhaul, coverage, capacity, batteries/generators and outage effects |
| **RT-SYS-008** | Solid waste, recycling and organics | municipal service | Unassigned | RTU-029 integration; existing waste simulation; Bins, collection, transfer, sorting, FOGO, landfill and authorised residual disposal |
| **RT-SYS-009** | Fuel supply and logistics | supply chain | Unassigned | RTU-005/010/013/029 interfaces; Petrol/diesel/LPG imports, deliveries, tanks, service stations and backup fuel |
| **RT-SYS-010** | Roads, rail and public transport | essential infrastructure | Unassigned | Existing town/transport work; no new RTU ID; Roads/bridges/footpaths, rail, crossings, freight and passenger transport |
| **RT-SYS-011** | Public lighting and traffic controls | essential infrastructure | Unassigned | RTU-011–015; preserve existing RLT tasks; Streetlight circuits, illuminated signs, traffic signals and crossing controls |
| **RT-SYS-012** | Emergency services and warning systems | public service | Unassigned | Existing emergency/justice modules; Police, fire, ambulance, dispatch, emergency communications and response dependencies |
| **RT-SYS-013** | Health, education and civic facilities | public service | Unassigned | Existing civic modules; RTU per-building interfaces; Clinic, school/TAFE/university, council, library, public toilets and service continuity |
| **RT-SYS-014** | Heating, cooling and thermal services | building service / optional utility | Unassigned | RTU-006/012 plus water/gas interfaces; Per-building hot water/HVAC; shared district heating/cooling only if justified |
| **RT-SYS-015** | Post and parcel delivery | public/commercial service | Unassigned | Existing post/depot simulation; Sorting, mail/parcel routing, delivery and facility dependencies |
| **RT-SYS-016** | Broadcasting and public information | communications service | Unassigned | RT-SYS-006/007/012 interfaces; Radio/TV transmitters, receivers, public announcements and warnings |

## Rules for agents
- RT-SYS IDs name systems; RTU-001–030 and all earlier RTD/RLT/etc IDs keep their meaning. RTSW-001–028 are new sewerage research/implementation children; research completion does not complete RTU-022–024.
- A facility may consume several services. Use existing H:/B: property keys and distinct fixture/node/edge IDs rather than identifying a circuit by display name.
- Physical sewerage (RT-SYS-003) and stormwater (RT-SYS-004) are separate graphs. Rain-related infiltration is a fault/inflow mechanism, not permission to connect downpipes to sanitary sewers.
- Water delivered by Manus must be counted once. Sewerage receives actual fixture discharge; irrigation, evaporation and stored cistern water are not automatically sewage. Reclaimed water remains separately labelled and never becomes potable by changing a flag.
- Electricity supplies individual lift pumps, treatment equipment and telemetry; a blackout does not directly stop a gravity toilet or gravity pipe.
- Gas/LPG is not assumed present in every town/building. District heat, vacuum sewers and pressure pods are optional, evidence-backed scenarios, not universal NSW infrastructure.
- Utilities, municipal services, supply chains and public services are distinguished in the Category column; all are included for coherent town simulation.
- No owner is authorised to overwrite another researcher's runtime work by this register. Cross-system APIs below are proposals until implementations are reconciled.

## Agent entry point
Sewerage: read SEWERAGE_RESEARCH_2026-10-25.md, SEWERAGE_SOURCES.json and SEWERAGE_TASKS.json. Next implementation task: RTSW-003 fixture inventory, then RTSW-004 water/power contracts. Electricity and water can continue independently within their existing assignments.
