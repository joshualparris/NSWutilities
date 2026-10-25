# NSW-ELEC-002 — Evidence-led NSW reference-town selection (25 October 2026)

**Decision:** Use **Menindee**, in Essential Energy's **Broken Hill/Far West regional supply system**, as the primary *small-town* physical and outage reference for Repository Town. Pair it with **Bawley Point/Kioloa** as the complementary islandable community microgrid / rooftop PV case. This is a **bounded, reproducible comparison** among eight well-motivated NSW candidates, NOT a provable census of every settlement in NSW or evidence of restricted/internal utility records being public.

## Scoring method (evidence, not fictional town quality)

A score of 0–3 in each column: 0 = no source located in this review; 1 = general or indirect source only; 2 = town/system-specific sourced details; 3 = primary technical evidence with named assets, configuration, or an event chronology. This is a **qualitative research-ranking tool**, not a statistical measurement. All primary evidence below available by 25 October 2026.

| Candidate | Regional network topology /3 | Outage and recovery /3 | Generation, BESS, islanding /3 | Critical utilities and electricity dependencies /3 | Town-level node/feeder details /3 | Public load/time-series pathway /3 | Total /18 |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Menindee (+ Broken Hill regional system)** | **3** | **3** | **3** | **3** | **2** | **2** | **16** |
| **Bawley Point / Kioloa** | 2 | 2 | **3** | 1 | 2 | 1 | 11 |
| Cobargo | 2 | **3** | 2 | **3** | 2 | 1 | 13 |
| Bega | **3** | 2 | 2 | **3** | 2 | 2 | 14 |
| Parkes / Peak Hill | **3** | 1 | **3** | 1 | 2 | 2 | 12 |
| Nyngan / Nevertire | **3** | 1 | **3** | 1 | 2 | 2 | 12 |
| White Cliffs / Wilcannia | **3** | **3** | 2 | 2 | 1 | 2 | 13 |
| Broken Hill (itself, a regional city) | **3** | **3** | **3** | **3** | **3** | 2 | **17** |

**Selection rule:** small-town-scale first; maximise accessible combined documentation for topology, failures, storage, generation and municipal dependencies. **Broken Hill itself scores higher but is not the target small town**; Menindee inherits *regional* engineering and incident evidence, not Broken Hill's buildings, substations or demand figures. The table does **not** invent an actual town LV feeder map.

## Source-to-score audit and alternative assessment

**Menindee/Far West**:
- Essential Energy [Distribution Annual Planning Report (DAPR) 2025 pp. 52–53](https://www.essentialenergy.com.au/-/media/Project/EssentialEnergy/Website/Files/Our-Network/DAPR-Essential-Energy-2025.pdf?rev=929391b9ac8a4885b9fdca4e5a998b81): Menindee 66/22 kV zone substation, 66 kV 5B1:SUN route via Sunset Strip, adjacent dedicated Menindee Boost Pump, upstream Broken Hill 220/22kV, 66/33/22kV and 33kV SWER branches elsewhere, named asset codes and separate solar/wind plants. The **66/22 label comes from the Menindee circle and legend, not a general-area guess**.
- [NSW Far West Oct 2024 post-event review](https://www.energy.nsw.gov.au/sites/default/files/2025-09/NSW-Far-West-Power-Outage-Review-Report.pdf), pp. 7–9: tower failure, backup generators, rural outages, restoration/critical service prioritisation.
- [Essential Energy 2024–25 annual operations report](https://www.essentialenergy.com.au/ext/ar2025/cover/operations-and-performance/our-operations/): emergency restoration and dedicated 3.5 MVA generation at Pinnacles Place for outlying communities.
- [AGL/ARENA BESS project](https://arena.gov.au/projects/agl-broken-hill-grid-forming-battery/): Broken Hill **50MW/50MWh** storage (NOT installed in Menindee).
- [Essential Energy zone-substation historic load downloads](https://www.essentialenergy.com.au/our-network/network-projects/zone-substation-reports): public 30-minute kW/kVAr AEST (subject to actual zone selection and dataset access). **Download returned HTTP 403 in CI**; public web listing ≠ successful data import.

**Bawley Point/Kioloa**:
- [Endeavour Energy project and December 2025/April 2026 newsletters](https://www.endeavourenergy.com.au/community/our-projects/bawley-point-microgrid): 3 MW grid battery and residential PV/batteries; **December 2025 published status says Kioloa automation became live, and specific event isolation is conditional**. Do not claim both communities automatically island during *every* outage.
- [Endeavour 11kV feeder briefing](https://www.endeavourenergy.com.au/about-us/newsroom/people-power-the-south-coast): two 11kV feeders over ~75km; strong second candidate for distribution-island logic, not an upstream coal/wind/hydro reference.

**Cobargo**:
- [AER Energy Innovation Toolkit Cobargo case study](https://www.energyinnovationtoolkit.gov.au/knowledge-sharing/cobargo): 2019–20 bushfire effects on water, sewerage, fuel, EFTPOS and communications; islanding proposal/feasibility and regulatory dependencies. **Proposed and feasibility-stage designs must not be silently treated as commissioned infrastructure**.
- [Essential Energy DAPR 2025 Bega network map p.65](https://www.essentialenergy.com.au/-/media/Project/EssentialEnergy/Website/Files/Our-Network/DAPR-Essential-Energy-2025.pdf?rev=929391b9ac8a4885b9fdca4e5a998b81): Cobargo/Bermagui 33kV network and named sections.

**Bega**:
- [DAPR 2025 pp.64–65](https://www.essentialenergy.com.au/-/media/Project/EssentialEnergy/Website/Files/Our-Network/DAPR-Essential-Energy-2025.pdf?rev=929391b9ac8a4885b9fdca4e5a998b81): Bega 132/66kV system, upstream Steeple Flat, named 66kV and 33kV substations/feeders. A larger centre, more detailed than a tiny town.
- [Bega Valley Energy Resilience Project](https://www.begavalley.nsw.gov.au/About-Council/Council-Projects/Bega-Valley-Energy-Resilience-Project): named council water pump, sewage treatment and water treatment sites with planned batteries and EV charging. **Construction/commissioning is scheduled into 2027, not operational by Oct 2026**.

**Parkes/Peak Hill**:
- [DAPR 2025 pp.58–59](https://www.essentialenergy.com.au/-/media/Project/EssentialEnergy/Website/Files/Our-Network/DAPR-Essential-Energy-2025.pdf?rev=929391b9ac8a4885b9fdca4e5a998b81): 132/66kV BSP, 66kV 89L/89G ring to Parkes Town, Peak Hill and Tomingley Mine; 11kV and generation sites. Strong topology and solar benchmark; fewer published outage restoration/event traces located in this pass.

**Nyngan/Nevertire**:
- [DAPR 2025 pp.50–51](https://www.essentialenergy.com.au/-/media/Project/EssentialEnergy/Website/Files/Our-Network/DAPR-Essential-Energy-2025.pdf?rev=929391b9ac8a4885b9fdca4e5a998b81): 132kV 94W / 94J-9GU, 66kV ring/backup, Nyngan Solar 102MW and named settlements. Strong precedent for alternate supply and utility topology.

**White Cliffs/Wilcannia**:
- Shares same high-quality Far West DAPR and 2024 outage evidence but 33kV and remote SWER details remain incomplete at the community-level; strong remote backup stress test, less ideal for typical denser town footprint.

**Broken Hill**:
- Strongest regional node/battery/outage evidence; **not an appropriate small-town template for every property and critical load** because it is the regional hub, not the small downstream settlement.

## Evidence sufficiency and honest conclusion

**Pass for NSW-ELEC-002's project-specific selection decision:** yes; eight relevant contenders, primary citations, explicit criteria and runner-up are recorded. **Global claim that Menindee is objectively 'the most documented NSW town': not established and not reasonably provable from public search alone.** The precise research goal is a realistic, playable small town informed by the best available combined *public* regional evidence—not copying restricted internal operational plans.

### Deficiencies to carry forward (do not fabricate)

1. A town-specific LV transformer/phase/service-drop circuit diagram has **not** been publicly established for Menindee or the other candidates.
2. Feeder labels from DAPR identify upstream network asset routes, not which precise house sits on which phase.
3. Public NSW pole GIS licensing/completeness checks belong to **NSW-ELEC-026**.
4. The historic 30-minute Essential Energy zone data needs real successful import (**NSW-ELEC-006**).
5. Underground services, behind-the-meter batteries, rooftop solar and critical building circuits must be marked **SYNTHETIC** until real evidence is supplied.

The primary public-asset research will use Menindee as reference **without pretending Repository Town geographically replicates Menindee**.
