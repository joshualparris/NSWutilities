# NSW-ELEC-003 — Menindee / Far West electrical topology evidence and limits

**As-of:** 25 October 2026. **Deliverable:** verified voltage/path findings and a machine-readable register of **20 labelled regional assets and 13 diagram-derived logical connections**: [JSON](../data/menindee_regional_reference_2025.json). The official [Essential Energy DAPR 2025 page 53](https://www.essentialenergy.com.au/-/media/Project/EssentialEnergy/Website/Files/Our-Network/DAPR-Essential-Energy-2025.pdf?rev=929391b9ac8a4885b9fdca4e5a998b81) has been visually inspected, not simply word-searched. **The record is a geographical *planning schematic*, not confidential/as-built switch drawings or the local distribution LV network.**

## High-confidence public evidence and corrected exact voltage chain

| Regional component | Confirmed public information | Level of certainty |
|---|---|---|
| Upstream Buronga → Broken Hill | **Transgrid X2**, 220kV, 7 transmission towers damaged in October 2024 | documented: [DAPR p.53](https://www.essentialenergy.com.au/-/media/Project/EssentialEnergy/Website/Files/Our-Network/DAPR-Essential-Energy-2025.pdf?rev=929391b9ac8a4885b9fdca4e5a998b81), [Far West review p.7](https://www.energy.nsw.gov.au/sites/default/files/2025-09/NSW-Far-West-Power-Outage-Review-Report.pdf) |
| Broken Hill receiving substation | Transgrid **220/22 kV**; Essential Energy uses two **22kV** lines stepped to **66 kV** for distant substations | documented in [DAPR p.52](https://www.essentialenergy.com.au/-/media/Project/EssentialEnergy/Website/Files/Our-Network/DAPR-Essential-Energy-2025.pdf?rev=929391b9ac8a4885b9fdca4e5a998b81) |
| Broken Hill / Mt Gipps line | DAPR schematic labels **66kV 5B1:PPL** to Pinnacles Place, **5B1:MTG** via Mt Gipps and toward Sunset Strip | diagram-derived logical paths, **not accurate GIS polyline** |
| Sunset Strip | Schematic symbol corresponds to **66/33/22kV**; **33kV SUN4B1** branch runs toward Wilcannia, **SUN4B2** toward Lake Tandou | diagram and legend p.53 |
| **Menindee zone substation** | Explicit circle on right of diagram; legend corresponds to **66/22kV**, fed over **66kV 5B1:SUN** line from Sunset Strip | diagram-derived exact *nominal voltage category*, not transformer serial/rating |
| **Menindee Boost Pump** | Separate labelled electricity-dependent boost pump with its own high-voltage-zone supply symbol in regional diagram | documented presence and schematic connection; **exact motor kW, phase and metering unavailable** |
| Two Broken Hill backup turbines | **Two 25 MVA** generator units at Broken Hill ZS on **22 kV** bus | DAPR p.53; 25 MVA ≠ 25 MW, needs PF and derating |
| Broken Hill PV | **53 MW** on Broken Hill Transgrid 22 kV bus | DAPR p.52; not a Menindee rooftop array |
| Silverton Wind Farm | **200 MW** nameplate in regional DAPR diagram | regional generation, not Menindee local wind |
| Broken Hill grid battery | **50 MW / 50 MWh**, 22 kV underground connection, in grid-forming research program | [ARENA technical lessons report pp.7ff](https://arena.gov.au/assets/2024/11/AGL-AGL-Broken-Hill-Grid-Forming-Battery-Lessons-Learnt-Report-2.pdf); the older **50MW/100MWh approved development** is *not* the installed storage energy rating |
| Separate emergency supply | Essential Energy deployed **3.5 MVA** generation at Pinnacles Place for outlying communities in 2024 | [Essential Energy annual operations 2024–25](https://www.essentialenergy.com.au/ext/ar2025/cover/operations-and-performance/our-operations/) |

**Correct interpretation of Menindee feed:** `220kV X2 transmission → Broken Hill 220/22kV → 22/66kV transformation → 66kV 5B1:PPL/MTG/SUN regional lines → Sunset Strip → 66kV 5B1:SUN → Menindee 66/22kV zone substation → UNKNOWN 22kV local primary feeders → UNKNOWN LV transformers/service circuits → homes/shops/pumps`. The intermediate regional sequence is **diagram interpretation**; it must not be treated as exact operating switching positions or line routing. The separate Menindee Boost Pump may connect via the regional 66kV line and is **not** an ordinary residential 22kV load.

## What the 2024 outage really validates

Sources: [NSW Government post-event report April 2025, pp.7–9](https://www.energy.nsw.gov.au/sites/default/files/2025-09/NSW-Far-West-Power-Outage-Review-Report.pdf), [Essential Energy annual report](https://www.essentialenergy.com.au/ext/ar2025/cover/operations-and-performance/our-operations/), [AER December 2025 proceedings notice](https://www.aer.gov.au/news/articles/news-releases/aer-institutes-proceedings-against-transgrid-following-2024-broken-hill-outages) and [NSW Government 1 Nov 2024 restoration](https://www.environment.nsw.gov.au/news/broken-hill-and-far-west-communities-back-power-grid).

- **17 Oct 2024 approximately 00:29 AEDT:** severe weather damages 7 X2 towers; more than 10,000 connections lose electricity.
- **18 Oct 2024:** backup generation partly restores region; damaged **66kV** Essential Energy line delays re-energisation outside Broken Hill until after 18:00 AEDT; available generator cannot meet all demand, requiring **load shedding** in two segments for under two hours.
- **21 Oct:** generator trip causes another disruption; restart and staged restoration reported on 22 Oct.
- **30–31 Oct:** temporary X2 transmission restoration and transition; some remote consumers experienced a distinct brief transfer outage, unlike Broken Hill itself.
- The emergency record demonstrates **two independent fault layers** (HV transmission and downstream distributor), backup-unit availability, capacity-constrained load shedding, temporary units, communications/water/fuel dependencies, and *separate* restoration of remote towns. Do not create exact SCADA switching timestamps beyond the source.

## Truth table for later modelling

| Fact required to accurately simulate individual Menindee buildings | Publicly verified? | Required handling |
|---|---|---|
| Regional 220/22/66/33/22 kV boundary and Menindee 66/22 kV ZS | YES, schematic | documented, source and page tagged |
| All actual 22kV Menindee outgoing feeder codes and sectionaliser positions | **NO** | **UNKNOWN; synthetic** labelled route only |
| Poles, line length, conductor type, phase, line impedance, transformer kVA | **NO** on inspected regional schematic | synthetic calibrated *candidate* physical data, no claims of actual circuit |
| Each house/building address, LV phase and real meter | **NO** | Repository Town existing building inventory; assign synthetic ID/phase only if clearly synthetic |
| Booster pump operating schedule/motor power | **NO** | explicitly parameterised and validated later; critical-load dependency, not fixed guess |
| Zone half-hour historical kW/kVAr | Public portal offers dataset, **download blocked HTTP 403** | NSW-ELEC-006 pending; no false import |
| Large grid battery could island Menindee through network fault | **NOT established** | NO by default; model capabilities, protection and topology separately |
| Water pressure, wastewater pumps, telecom BTS backup autonomy | **NOT established** | cross-utility scenario variables, not fact |
| 2024 event as true timeline to emulate | YES, regional high-level | scenario events; preserve multi-day unknown intervals |

## Required implementation boundaries

1. Give every *actual published regional asset* a stable **REG-** ID in JSON. Keep regional voltage conversion, sources and backup dependencies separate from fictional Repository Town premises. Source fields are mandatory and machine-auditable.
2. As-built service wiring is not exposed by this report. **Do not reverse-engineer critical live switching locations** or claim the arbitrary diagram edges have surveyed coordinates.
3. Use tiered simulation: (A) documented regional outline, (B) explicitly **synthetic** small-town 22kV/415V/230V distribution, (C) measured time-series reference when accessible. Import controls must reject undocumented phase service ratings as 'actual'.
4. Generate credible blackout states: X2 tower fault; extra distributor 66kV damage; 1 of 2 generators unavailable; temporary emergency supply limited by 3.5MVA; transfer to restored HV with a distinct downstream interruption; solar PV trips without island reference; battery state-of-charge and kW/kWh guardrails.
5. Link urban building audit to [NSW-ELEC-005](./TASKS.md) and [RTU-001 CSV](../audit/electricity/buildings.csv) but **do not invent a Menindee LV mapping** to Repository Town geometry.

## Acceptance result, scoped accurately

[x] Review actual map and date/page; identify Menindee zone class and regional nominal voltages.  
[x] Resolve AGL battery **50MW/50MWh** operating rating versus planning **50MW/100MWh** consent.  
[x] Map published assets and source-labelled logical connections in machine-readable format; preserve source provenance.  
[x] Find multi-stage real blackout and downstream impacts.  
[ ] **Exact last-mile Menindee circuit/service details are not publicly verified and remain UNKNOWN**, hence a claim of a complete actual physical network would be false. This remains follow-on research during NSW-ELEC-024/026, with synthetic grid implementation in NSW-ELEC-009.

**NSW-ELEC-003 regional research deliverable complete, not an as-built engineering survey.** Acceptance must never be read as 'every Menindee pole and consumer is known'.
