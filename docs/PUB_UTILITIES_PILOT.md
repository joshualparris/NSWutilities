# Merged Branch: one-building utilities pilot

Public project engineering notes, 25 October 2026. Fictional pub, not an as-built real pub or an installation design. Baseline canonical source 59139c4. No real private property survey or hidden asset location is asserted.

## Audit and scope

Before: 14 × 18 m shared shell; decorative taps, fridge and cold-room door; bar, seating and pool; no usable toilet, kitchen, metered building services or service isolation. Town supply uses abstract integer power allocations and water units, not a hydraulic or AC solver.

The pilot keeps the pub at its existing plot and preserves entry/exit. Pool moves forward to open the rear service corridor. Rear-right sanitary compartment has WC, cistern, basin and soap/towel fixture; rear-left cooking/preparation zone has sink and extraction hood. Existing bar stays usable. This is not a certified accessible layout: manoeuvring space, fixtures, fire egress, waterproofing and development approval need specialist design before any real construction.

## Every designated system

| Designation | Pub boundary and next realism requirement |
|---|---|
| RT-SYS-001 electricity | Existing industry/business allocation supplies pub breaker; model meters 1.2 kW refrigeration, 0.3 kW lights/extraction approximation, 40 W communications, 3.6 kW thermostat-controlled storage heater. No individual surveyed transformer/service, phases, protection coordination or voltage calculation yet. No solar/BESS invented. |
| RT-SYS-002 potable water | Existing town water-availability flag → isolation valve → cistern, kitchen and basins. Litre accounting and finite hot tank. Actual pressure, backflow device selection, mains topology and town stock units unresolved. |
| RT-SYS-003 sewer | WC/basin sanitary branch and kitchen trade-waste branch counted separately; kitchen grease inventory intercepts fats. Both lead conceptually to town sewer. Sewer isolation prevents use. Gravity drain does not require pub power. Pipe diameters, grades, vents, traps, ORG, downstream surcharge and pump topology not solved. |
| RT-SYS-004 stormwater | Roof runoff estimate: rain mm/h × 252 m² × 0.9 gives L/h, separate from sanitary sewer. Rain forcing is a modelling parameter, not yet connected to town weather; gutters, downpipes, legal discharge point, tank, flood routing and evaporation are outstanding. |
| RT-SYS-005 gas/LPG | Fictional two-cylinder 90 kg initial LPG inventory; valve, 18 kW burner-equivalent × 10 min/meal, 12.8 kWh/kg conversion. No natural-gas main is asserted. Delivery, regulator, changeover, vaporisation and clearances remain to model. |
| RT-SYS-006 fixed internet/phone | Fictional FTTP-style endpoint/router/VoIP/EFTPOS dependency on local power and upstream availability. 120 Wh UPS at 40 W lasts three ideal hours, no conversion loss assumed. No claimed real carrier, line rate or premises coverage. |
| RT-SYS-007 mobile | Existing town behaviour unchanged; no fake claim that Wi-Fi or UPS guarantees mobile service. Tower load, coverage, backhaul and backup remain tasks. |
| RT-SYS-008 waste/recycling/organics | Meal waste, recycling, used cooking oil and grease tracked separately. Capacity can stop cooking. Contractor collection and pump-out explicitly recorded as manual scenarios, not simulated trucks. Separate food organics route still required. |
| RT-SYS-009 fuel | Finite LPG use; no petrol/diesel connection at pub. No automatic refuel. Cylinder delivery/fuel-depot chain outstanding. |
| RT-SYS-010 transport | Preserve existing frontage and town logistics; dedicated safe delivery access and loading hours outstanding. |
| RT-SYS-011 lighting/traffic | Interior electric lights follow pub breaker and aggregate supply; street signals remain town-owned. Emergency battery/exit lighting is not implemented. |
| RT-SYS-012 emergency | Existing town response unchanged. Add fire detection, suppression, alarm backup, emergency lighting and lawful occupancy model. |
| RT-SYS-013 civic/health | Food hygiene dependencies modelled; this is not council approval or food safety certification. |
| RT-SYS-014 thermal | Finite hot-water energy and cold-room warming/cooling; HVAC, ventilation air rates, kitchen heat gains and room envelope not solved. |
| RT-SYS-015 post | Existing town post unchanged; pub parcel and invoice delivery not integrated. |
| RT-SYS-016 broadcasting | Decorative screen remains; antenna, receiver power and transmitter outage dependency outstanding. No actual broadcast signal model. |

## Source registry and applicability

All retrieved 2026-10-25; original publisher material remains at source. No licence to reproduce full standards or diagrams assumed; use short derived engineering descriptions only. Web-page observations are primary evidence; the numerical model below is synthetic.

- PUB-S01 NSW Food Authority, **Hand washing in food businesses**, https://www.foodauthority.nsw.gov.au/help/hand-washing-food-businesses — warm running potable water, accessible food preparation hand basins and washing near toilets. High confidence public guidance; exact fixture sizing not inferred.
- PUB-S02 NSW government, **Liquid Trade Waste Management Guidelines 2021**, https://water.dpie.nsw.gov.au/__data/assets/pdf_file/0010/147088/trade-waste-management-guidelines.pdf — source identified and relevant passage located; entire document not audited. Regional council approval and trade-waste pre-treatment must be checked for the chosen service area.
- PUB-S03 Sydney Water, **Plumbing for retail food businesses**, https://www.sydneywater.com.au/content/dam/sydneywater/documents/plumbing-for-retail-food-businesses.pdf — food preparation drainage and grease pre-treatment. Sydney Water jurisdiction, illustrative engineering reference only; not evidence that Sydney Water supplies this fictional regional pub.
- PUB-S04 Sydney Water, **Retail food trade wastewater**, https://www.sydneywater.com.au/your-business/managing-trade-wastewater/commercial-trade-wastewater/retail-food-trade-wastewater.html — collect used cooking oil separately for off-site recycling. Public operating guidance, not a pub asset inventory.
- PUB-S05 nbn, **Prepare for an emergency**, https://www.nbnco.com.au/learn/what-happens-in-a-power-blackout/emergencies-and-outages — customer devices need their own backup; local battery cannot guarantee upstream service.
- PUB-S06 nbn, **What happens in a power blackout?**, https://www.nbnco.com.au/learn/what-happens-in-a-power-blackout — access technology and upstream equipment affect availability.

## Explicit numerical assumptions

6 L cistern with 3 L half flush, 3 L/min refill; initial stored water not billed twice. 160 L hot tank starts 60 °C, ambient 18 °C, specific water heating energy 0.001163 kWh/L/K. Standing loss proportional to temperature difference; thermostat heating capped at 60 °C. Each wash uses 2 L; demonstration wash-up 8 L/meal; glass cycle 3 L and 0.1 kWh. Hot outflow is replaced by cold water and mixed. Cold room starts 3 °C, outage warming tends toward 24 °C with 180 min time constant; powered recovery 0.15 °C/min. Crossing 5 °C stops new cooking; no claim this alone captures food time/temperature safety. LPG, waste, UPS and roof values are design assumptions, not measured commercial equipment specifications. No manufacturer branding until actual datasheets, capacities and suitability are verified.

Meters retain units; pub kWh/litres must NOT be added to existing abstract town power/water units without an explicit calibrated conversion. Overlays are colour-coded schematic routes above head height, not physically installed wiring or plumbing. They are mutually exclusive and toggle off. They do not claim to reveal hidden real infrastructure.

## Permanent tasks and acceptance

| ID | Priority | Dependencies | Scope and acceptance | Status |
|---|---|---|---|---|
| RTPUB-001 | P1 | — | Source/layout audit, all 16 utility boundaries, evidence and uncertainty | Documented |
| RTPUB-002 | P1 | 001 | Finite inventories, SI units, service dependencies, time integration, save/reload tests | Implemented; test evidence below |
| RTPUB-003 | P1 | 002 | Toilet/basin/kitchen props, collision-clear routes, entrance preserved | Implemented; geometry tests; browser acceptance pending |
| RTPUB-004 | P1 | 002 | Real paid hot orders and NPC dinners consume utilities and reject unavailable kitchen before debit | Implemented; broader acceptance pending |
| RTPUB-005 | P2 | 002–003 | Individual layer toggles and building electric-light outage response | Implemented; browser acceptance pending |
| RTPUB-006 | P1 | 002–005 | Local desktop/Android playtest, movement, fixture interaction, failures, restore, errors and screenshots | Pending |
| RTPUB-007 | P1 | 006 | Full release/privacy gates, reviewed merge, exact live fingerprint and hosted playtest | Pending |
| RTPUB-008 | P2 | 007 | Physical town mains/service topology, phase demand, hydraulic sewer pressure, stormwater forcing, automatic patrons/fixtures, deliveries/collection, mobile, broadcasts, fire/HVAC, brands and calibration | Open; do not claim every utility complete |

Affected code: `src/world/pub-utilities.js`, `pub-interior.js`, `life.js`, `src/ui/pub-utilities-panel.js`, `src/main.js`; tests `tests/pub-utilities.mjs` and browser acceptance. Stable RTPUB IDs supplement, never replace, existing RTU, NSW-ELEC, NSW-WAT, RTSW or stormwater tasks.

## Verification record

Node regression verifies stored flush without water supply, insufficient cistern rejection, refill and litre accounting, sewer isolation, finite LPG, waste production, three-hour UPS exhaustion, cold-room warming/recovery, upstream outage despite local power, geometry pathfinding from entrance to all new hotspots, exclusive overlay and TownLife save/restore. Existing 45-interior suite and public build/privacy scan passed during development. Final evidence and remaining failures must be appended before completion claims.
