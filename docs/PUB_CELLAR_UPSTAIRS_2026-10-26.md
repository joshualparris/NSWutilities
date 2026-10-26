# PUB-EXP cellar and upstairs dining — 26 October 2026

PUBLIC fictional game design. This supersedes the single-storey geometry decision in the earlier 002/024 envelope report. It does not supersede outstanding professional assessment or issue a real building approval.

## Built scope and dimensions

The main envelope remains 14 × 18 m. There are two above-ground storeys and one cellar. Separate collision scenes share the same footprint and physical elevations: ground 0 m, upstairs +4.8 m, cellar −3.2 m. The upper facade has actual aligned windows and a matching raised roof. A separate rear escape stair occupies a nominal 3.4 × 5.5 m yard annex, clear of the side discharge route. The rear accessible-design path extends to z=−18.2 m before turning around the new stair annex; its paving and collision sampling follow that revised route. Actual cadastral boundaries, structural bearing, excavation, waterproofing, fire resistance and approvals remain unverified.

Ground furniture falls from 39 to **19 seats**; upstairs has **32**, for 51 total. The original 24-patron game admission limit is retained across the venue. Extra seats do not spawn extra NPCs or establish an approved occupancy. Ground-floor accessible-design sanitary facilities and kitchen remain. Upstairs has dining, an office, a refuge call point, access to the passenger lift, main stair and a separate rear escape stair. Cellar has finite keg/beer/wine stock, chiller, low-level gas detector, extraction ducts, sanitary basin and pumped holding tank. LPG and beverage-gas cylinders remain outside.

The dogleg public stair has two flights of 14 risers per storey: rise 4.8/28 = 171.4 mm, going 280 mm, nominal clear flight 1.25 m, 1.35 m mid-landing, handrails and stringers. Cellar flights use 160 mm risers. Shaft holes are actually cut out of floor/ceiling slab meshes, with colliders preventing falls. The existing game walks on flat 2D collision scenes: Use at a stair landing changes the active scene/elevation. Continuous foot-by-foot 3D stair climbing is not claimed. Lift landings and tested routes use a 1.2 m design corridor; the model is not an AS 1428 circulation certificate.

A fictional 630 kg passenger lift serves 8 m total travel. It is not a low-rise platform lift and not an evacuation lift. Trips take distance/1 m/s plus two seconds of door time and add mgh/0.65 plus 0.006 kWh to the shared pub meter. Only completed trips are charged; regenerative drives, counterweight dynamics and interrupted-trip energy are not simulated. Isolation, branch faults, mains failure and emergencies block lift travel. Closing the panel or leaving the scene cancels the pending ride. Stairs and secondary exits remain available. The refuge call checks real on-site simulated staff before a simplified staff-assisted ground transfer; this is not a verified PEEP, rescue procedure or independent escape solution for a real building.

## Cellar simulation and utility boundaries

The cellar shares existing pub stocks rather than spawning free kegs. Wine starts at 36 bottles; six-bottle transfers conserve cellar + bar stock and change visible rack contents. Beverage gas starts at 4.5 kg outside, with finite 45 kg supplier boundary stock. Dispensing a 425 mL beer uses an assumed 0.00085 kg gas. Exchanges require isolation and retain residual returned gas in accounting. Leak, dispensed, returned, depot and onsite gas are conserved.

A declared 200 m³ well-mixed zone uses ambient 420 ppm, assumed 0.54 m³ CO2/kg and 6 air changes/hour. A leak scenario depletes the actual cylinder. A conservative **2500 ppm gameplay interlock**, not an occupational exposure limit, latches an alarm and shuts beverage gas. Cellar entry requires mains-powered working extraction and a healthy monitor; exits are never disabled by the atmosphere interlock. Reset needs the leak stopped, ventilation/monitoring restored and model concentration below 1000 ppm. This one-zone model does not simulate stratification, oxygen displacement, gas mixtures, exposure dose or actual safe-entry certification.

Cellar hand washing uses 2 L potable water into a 60 L sanitary holding tank. Only an electrically powered connected pump discharges it to the sanitary lateral at an assumed maximum 20 L/min. A full tank refuses new inflow. Cellar sanitary discharge never enters the kitchen grease branch or stormwater. The existing ground/upper sewer is gravity-modelled independently. Chiller, extraction, upper lights, sump and passenger lift have independent typed electrical branches. An additional 0.5 kW baseline plus 0.5 kW trading load is added to the pub's existing feeder demand approximation; the 75 kVA synthetic connection is preserved. Detailed motor starting, pressure, ventilation sizing, protection and certified plant selection remain open.

Upstairs food orders use the existing real pub menu, staff and till; collect at the ground-floor bar. This release does not invent extra waiting staff or a complete multi-floor waiter/dumbwaiter simulation. PUB-SIM-012 remains open.

## Primary-source basis

Reviewed 26 October 2026. Documents are linked, not reproduced; publisher copyright/licences apply. These sources inform design choices, not a compliance conclusion.

| Evidence | Publisher / precise reference | Application and limit |
|---|---|---|
| [Current NSW NCC edition](https://www.nsw.gov.au/housing-and-construction/compliance-and-regulation/how-to-comply-national-construction-code) | NSW Government, “What edition of the BCA applies?” | NCC 2022 Amendment 2 basis; project-specific approvals absent |
| [NSW adoption announcement](https://www.nsw.gov.au/ministerial-releases/nsw-to-adopt-new-national-construction-code-may-2027) | NSW Government, 25 March 2026 | NCC 2025 adoption 1 May 2027; do not assume 2025 rules already apply |
| [Premises access standards](https://www.legislation.gov.au/F2010L00668/2024-11-23/2024-11-23/text/original/epub/OEBPS/document_1/document_1.html) | Commonwealth, Access Code lift provisions | Lift type/travel and accessible features need assessment; choose passenger lift, not unsupported platform-lift claim |
| [Lifts used during evacuation handbook](https://www.abcb.gov.au/sites/default/files/resources/2022/Handbook-lifts-used-during-evacuation-2013.pdf) | ABCB, 2013 handbook | Ordinary passenger lift is not assumed safe for evacuation; full evacuation strategy unverified |
| [Cellar gas safety alert](https://www.safework.nsw.gov.au/safety-alerts/safety-alerts/gases-in-cellars-and-cool-rooms) | SafeWork NSW, recommended controls | Outdoor gas storage, extraction and low-level monitoring; detector modelled at 450 mm, external warning indication; actual commissioning/AS 5034 compliance unverified |
| [Confined spaces](https://www.safework.nsw.gov.au/hazards-a-z/confined-spaces) | SafeWork NSW, ventilation/testing/entry guidance | Does not determine that this fictional room is legally a confined space; no real entry authorisation or rescue directions |

## Stable implementation tasks

| ID | Scope | Dependencies | Acceptance |
|---|---|---|---|
| PUB-EXP-001 | Envelope, floor slabs, stair/lift core and cellar | Existing 002/024 geometry | Aligned elevations/facade; real shaft openings; isolated floor collisions; no fabricated approval |
| PUB-EXP-002 | Upstairs dining/office and ground decongestion | 001 | Exactly 19 + 32 registered seats; 1.2 m routes to lift/stairs/refuge/secondary exit; collision-safe landings |
| PUB-EXP-003 | Cellar stocks, gas/extraction, chiller and pump | 001 | Finite mass/volume accounting; no LPG underground; typed branch failures; safe entry refusal, unrestricted exits; saved state validation |
| PUB-EXP-004 | Powered passenger lift and second egress | 001,003 | Timed successful trips; isolation/power/emergency refusal; panel-cancel guard; stairs work during blackout; separate yard discharge |
| PUB-EXP-005 | Standards/audit/reference reconciliation | 001–004 | Replace outdated single-storey assertions; retain all legal hold points; update source blob evidence |
| PUB-EXP-006 | Review, merge, hosted desktop/phone acceptance | 001–005 | Full release/privacy, source checks, real 3D stair/lift/cellar/seat/fault/exit gameplay, exact public manifest, header absent from outset |

PUB-EXP-001–006 are complete within the declared playable-model scope. The [release acceptance report](PUB_CELLAR_UPSTAIRS_RELEASE_2026-10-26.md) records exact tested source, all seven source checks, publisher, actual hosted desktop/phone tests, URL and limitations. Human handset, acoustics/listening, full crowd and professional engineering verification remain separate.
