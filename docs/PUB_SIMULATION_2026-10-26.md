# Pub simulation and physical remediation — 26 October 2026

[Final merged release and hosted acceptance evidence](PUB_SIMULATION_RELEASE_2026-10-26.md).

This is a fictional, playable engineering approximation, not an approved building design or a surveyed digital twin. PUB-CODE and RTPUB formal compliance tasks remain open. Their identifiers are separate from the PUB-SIM tasks below. Existing source evidence and the formal matrix remain authoritative about unverified approvals.

## Reference cases and evidence boundaries

The following are reference studies, not real connections from these distant towns to one fictional pub. Access/review date: 26 October 2026. Public facts are separated from game assumptions. Links are primary sources; linked documents retain publisher copyright. No protected standards text or non-public network maps are redistributed.

| System | Reference case | Public source and supported fact | Confidence / remaining uncertainty |
|---|---|---|---|
| Electricity | Menindee (provisional) | [Essential Energy network](https://www.essentialenergy.com.au/about-us/our-network-area), regional network context | Town-specific feeder configuration, impedances, transformer and load calibration not established here; do not infer actual circuits |
| Sewerage | Narromine | [Council water/sewerage](https://www.narromine.nsw.gov.au/residents/water-sewerage), public service and environmental reporting | Reference for municipal treatment; fictional pub lateral and grease arrestor are not surveyed Narromine assets |
| Water | Orange | [Treatment plant](https://www.orange.nsw.gov.au/water/water-treatment-plant/), [supply system](https://www.orange.nsw.gov.au/water/oranges-water-supply/) | Public regional treatment/supply descriptions; no verified premises pressure, pipe sizing or backflow hazard assessment |
| Gas | Forbes | [Jemena flooding impact](https://www.jemena.com.au/media/forbes-flooding-impact-on-gas-services2/) | Documents real gas service disruption/isolation; does not establish pipe route, appliance compatibility or pub connection |
| Internet / telephone | Tamworth | [nbn fibre upgrades](https://www.nbnco.com.au/residential/upgrades/more-fibre/faqs) | Regional upgrade context does not prove FTTP at a specific address; game models upstream link, router, UPS, ATA and handset |
| Radio / television | Orange | [ACMA broadcast transmitter data](https://www.acma.gov.au/list-transmitters-licence-broadcast) | Public station inventory available; transmitter rows/terrain not calibrated in this implementation; no invented frequency/site |
| Mobile | Wagga Wagga | [ACCC 2026 infrastructure report](https://www.accc.gov.au/by-industry/telecommunications-and-internet/mobile-services-regulation/mobile-infrastructure-report/mobile-infrastructure-report-2026), [ACMA coverage standard](https://www.acma.gov.au/mobile-network-coverage-maps-standard) | Nationwide comparison framework; no proven indoor reception at a pub; carrier and battery availability are independent game inputs |
| Waste / recycling | Orange, provisional; Narromine comparison | [Narromine waste](https://www.narromine.nsw.gov.au/residents/waste-management) | Commercial collection contract, routes and Orange-specific calibration remain unverified |
| Fuel / deliveries | Regional boundary, town not selected | Forbes gas evidence above supports separation of utility supply from onsite fuel | Finite LPG/beer supplier inventories and timed delivery are fictional abstractions, not surveyed truck routes; no onsite petrol/diesel tank |

## Implemented model

Twelve switchable schematic layers distinguish electricity, water, sewerage, gas, internet, telephone, mobile, radio, television, waste, stormwater and fuel. Typed node/edge faults isolate individual branches. The overlay is a readable game schematic, not an installation drawing. Existing electricity supply uses the town grid model; other networks remain availability/flow/accounting approximations rather than full hydraulic or electromagnetic solvers.

LPG and optional natural gas are alternative appliance scenarios. Conversion isolates gas for a timed gasfitter scenario and leaves the valve closed afterwards. They cannot simultaneously fuel the cooker. A finite depot reserves a 45 kg exchange before a 120 town-minute delivery. Natural gas energy uses a declared approximation of 10.83 kWh/m³. Pipe pressure, combustion products, regulator capacity and certified commissioning remain future work.

Potable water, sanitary sewer, grease-arrested trade waste and stormwater have separate graph paths and accounting. Kitchen service stops on branch isolation, unsafe food state or exhausted clean plates. The automatic washer uses a three-minute, six-item batch, 3 L trade waste and 0.1 kWh; these are declared gameplay coefficients, not a selected commercial appliance specification. It requires connected electrical/water/trade branches, water availability and hot water. Full temperature/time sanitisation validation remains unimplemented.

Finite stock starts with a 50 L keg, 48 sealed bottles, 40 glasses and 40 plates. Successful purchases reserve beer and glassware exactly once; actual consumption returns glassware to dirty stock. Food plates return after a simplified hour. Keg/case exchanges reserve finite supplier stock and record residual keg waste. This is material accounting, not a brewery simulation. A 425 mL fictional 4.8% beer is about 1.61 Australian standard drinks; the conservative game service cap is not a BAC model or legal intoxication determination. [Australian standard drinks guide](https://www.health.gov.au/topics/alcohol/about-alcohol/standard-drinks-guide).

Actual scheduled pub workers Nora and Celia receive pub-only uniforms. Onsite presence and current simulated RSA endorsement gate alcohol service. Records are explicitly fictional, cannot issue qualifications and contain no real card numbers. [NSW hotel licensing](https://www.nsw.gov.au/business-and-economy/liquor-and-gaming/liquor-licensing/licence-types/hotel), [competency cards](https://www.nsw.gov.au/business-and-economy/liquor-and-gaming/training/competency-cards). NSW uses **RCG**, rather than a generic RSG label. The game conservatively requires RCG plus Keno induction for its demo; this is not a claim that every Keno-only employee legally requires RCG. [RCG](https://www.nsw.gov.au/business-and-economy/liquor-and-gaming/training/responsible-conduct-gambling), [Keno training unit SITHGAM004](https://training.gov.au/training/details/SITHGAM004).

Pool is a two-player, fixed 1/240 s equal-mass disc simulation with friction, cushions, pockets, cue placement, groups, scratches and black-ball outcome. It omits spin, jumps, cue elevation and complete competition rules. The panel replays a shot resolved atomically, preserving saved outcomes if closed. Keno is an educational free draw: choose 1–10 of 80, draw 20 unique numbers at the next three-town-minute boundary, at most five tickets per town day. No money, prizes, operator account or autoplay. [Operator game guide](https://www.keno.com.au/keno-pdfs/NSW_Game%20Guide.pdf), [Keno Classic](https://www.keno.com.au/NSW/keno-classic). This limited demo is not a complete licensed Keno product.

## Physical changes and deliberate limits

The existing 14 × 18 m single-storey envelope accommodates 32 bistro chairs and seven bar stools, 39 registered seats. The conservative 24-person gameplay admission limit is retained; a furniture count is not an approved occupancy determination. No extra storey/cellar was required to add seating. Adding stairs without floor openings, accessible vertical circulation, structural support, protected egress and exterior envelope changes would create more defects, so those remain a separate design project.

Door hinge offsets and swing directions avoid fixed colliders in sampled full 90-degree sweeps. Rear dado panels stop at the exit, and panic hardware travels with the door. Side-wall TV/menu-board depth follows the wall plane and the TV is clear of the window. Removed duplicate floating chair backs and intrusive bar details; relocated the lowered bar section and fixtures. Four fans rotate with electricity and coast after failure. Successful beer/meal events show a pour stream, glass/plate, tray and uniformed staff route. This is bounded presentation of the first active service event, not yet a multi-waiter queue or full skeletal hand/grip animation. Multiple purchases still conserve inventory independently.

## Permanent tasks

| ID | Priority | Dependencies | Affected code | Acceptance / completion evidence |
|---|---|---|---|---|
| PUB-SIM-001 | P0 | Baseline PUB-CODE matrix | pub-standards, utilities, service-visuals | Independent typed utility paths; existing utilities/completion tests; retain unverified formal approvals |
| PUB-SIM-002 | P1 | 001 | pub-venue, utilities | Finite LPG depot, reserved delivery, isolated conversion, metered gas; pub-venue tests |
| PUB-SIM-003 | P1 | 001 | pub-venue, standards, life | Actual onsite worker qualification gate, refusal without payment; pub-venue tests |
| PUB-SIM-004 | P1 | 001 | pool model/panel | Momentum, energy loss, pockets, fouls, saved state; pub-venue and gameplay checks |
| PUB-SIM-005 | P1 | 003 | venue model/panel | Free scheduled unique Keno draw, adult/self-exclusion/network/worker gates; pub-venue and gameplay checks |
| PUB-SIM-006 | P0 | 001 | host QA wrapper | No launcher header/buttons from first paint; iframe fills phone/desktop; hosted verification |
| PUB-SIM-007 | P1 | 001–005 | life, utilities, venue | Finite beer/glassware/plates, resource use and stock delivery; pub-simulation-layout tests |
| PUB-SIM-008 | P0 | All implemented tasks | tests, audit matrix, release | Full release/privacy gate, real desktop/emulated phone, exact hosted fingerprint; only mark verified when evidence recorded |
| PUB-SIM-009 | P0 | Existing envelope | pub-interior, plant | 39 seats, sampled unobstructed swings, rear exit, window geometry, powered fans; pub-simulation-layout plus visual gameplay |
| PUB-SIM-010 | P1 | 003,007,009 | pub-presentation, main | Uniforms and physical successful-service props, routed staff, emergency halt; layout test and gameplay |
| PUB-SIM-011 | P1 | 001, public data | future calibrated engines | Public asset/parameter evidence and unit-consistent electrical, pressure, drainage, RF and outage calibration; currently OPEN |
| PUB-SIM-012 | P1 | 009,010 | future staff task scheduler | Concurrent table-assigned orders, articulated grip/walking and clearing, no service overlap; currently OPEN |
| PUB-SIM-013 | P1 | Formal matrix | future professional review | Fire/access/food/ventilation/electrical/gas/structural/licensing design evidence and genuine inspection approvals; OPEN, cannot be issued by game code |

## Standards boundary

As of this review NSW's published adoption guidance identifies NCC 2022 Amendment 2 as current and NCC 2025 adoption on 1 May 2027. [NSW adoption guidance](https://www.nsw.gov.au/housing-and-construction/compliance-and-regulation/how-to-comply-national-construction-code). Fire maintenance changes from 13 February 2026 are documented by [Building Commission NSW](https://www.nsw.gov.au/departments-and-agencies/building-commission/industry-changes). An official current edition check and project-specific assessment are essential before any real building conclusion. Simulated notices, drills, licences, induction and inspections are gameplay records, not approvals. Full food-safe sanitisation, engineered ventilation, fire design, supply pressure, gas certification, structural assessment and liquor/food-business authorisation are not proved by passing automated tests.

## Reproduce

From repository-town: `node tests/pub-venue.mjs`, `node tests/pub-simulation-layout.mjs`, `node tests/pub-completion.mjs`, `npm run build:release`, then `node tests/pub-compliance-browser.mjs` against the built server and hosted URL. Source blob hashes in the formal audit matrix must match committed code. Record source SHA, release content hash, screenshots and hosted workflow links in the completion checkpoint. A release must not be called complete solely because a PR or local build exists.
