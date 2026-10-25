# Repository Town selection: comparative public water-data basis

**Decision date:** 25 October 2026  
**Recommendation:** Select **Orange, NSW** as the single base town if the deciding criterion is the strongest publicly evidenced water-data basis. Retain Menindee only as a separate electrical-case study or comparative context; do not present Menindee and Broken Hill as one town. This is a comparative recommendation based on six supplied town audits, not an exhaustive statewide census or a claim that Orange has the most open operational telemetry.

## Executive finding

Orange has the strongest overall public evidence among the six candidates because it combines multiple town-attributed, recurrent source-operation and environmental-monitoring publications with drinking-water, supply planning, stormwater, sewerage and reuse documentation. Especially differentiating are quarterly Decision Support Tool (DST) reports, monthly source-extraction reports, and annual hydrology, aquatic-environment and groundwater monitoring reports, alongside dated drinking-water results and asset-management plans. The evidence is unusually broad and regularly refreshed for Orange, though much of it remains PDF/HTML rather than structured feeds. [1–5]

This is a recommendation for **best evidence base**, not a finding of best data openness in every dimension. No candidate demonstrated a complete, openly licensed utility asset GIS, town-wide SCADA/telemetry, normalized drinking-water laboratory history, or comprehensive wastewater/reuse operating series. Orange's lead is chiefly its breadth, town attribution and recurring operationally informative reporting—not a verified raw-data API or complete asset dataset.

## Rubric defined before comparative scoring

Scores are evidence-weighted, qualitative judgments on a 1–5 scale. A score of 1 means little directly evidenced public material in the dimension; 3 means useful but incomplete or mixed evidence; 5 means comparatively strong and directly evidenced coverage. Half-points distinguish close judgments. Scores describe the **public evidence located in the audits**, not underlying utility capability or absolute data completeness.

| Dimension | Weight | What is scored (and what is not) |
|---|---:|---|
| Public material breadth / source richness | 15% | Number and diversity of distinct relevant public source categories (supply, quality, security, wastewater, hydrology, etc.). Volume of documents alone does not establish operational value. |
| Town-specific operational utility | 30% | Direct attribution to the named town and usefulness for understanding measured operations, as distinct from general plans, proposed projects, utility-wide aggregates, or regional context. |
| Machine-readable spatial / hydrological access | 25% | Verified or credibly documented access to structured downloads, APIs, station observations or spatial services, with town/station relevance. General portal existence earns limited credit; a specific station/time series not verified is not treated as established. |
| Temporal depth and update | 20% | Recurrence, historical span and evidence of recent refresh for town-relevant observations/report series. Static plans and project announcements alone score lower. |
| Reuse-term clarity | 10% | Evidence of explicit dataset-level open terms. Public viewing or download without an identified licence is not counted as clearly reusable. |

**Calculation:** weighted score = sum of (dimension score × weight), on a 5-point scale. The result is rounded to one decimal and remains a comparative heuristic. Breadth is deliberately only 15% so a large stack of plans cannot outweigh weak operational specificity, machine access, or time depth. No separate “raw document count” score is used because the audits do not offer a uniform document census.

## Comparative scoring

| Candidate | Breadth (15%) | Town operational utility (30%) | Machine-readable spatial / hydro (25%) | Temporal depth (20%) | Reuse terms (10%) | Weighted result |
|---|---:|---:|---:|---:|---:|---:|
| **Orange** | 4.5 | 4.0 | 3.0 | 4.5 | 2.0 | **3.8 / 5** |
| **Broken Hill** | 4.0 | 4.0 | 3.0 | 3.5 | 2.0 | **3.5 / 5** |
| **Menindee / Broken Hill corridor** | 4.0 | 3.5 | 3.0 | 4.0 | 2.0 | **3.4 / 5** |
| **Dubbo** | 3.5 | 3.5 | 3.0 | 3.0 | 2.5 | **3.2 / 5** |
| **Tamworth** | 3.5 | 3.5 | 2.5 | 3.0 | 2.5 | **3.1 / 5** |
| **Cobar–Nyngan** | 3.0 | 3.0 | 2.5 | 2.5 | 2.0 | **2.8 / 5** |

Scores are not statistically precise. In particular, access portals were not exhaustively queried station-by-station, licensing was not audited item-by-item, and the candidate scopes differ. A difference of a few tenths should not be read as a validated rank interval. The decimals make the rubric reproducible, not the evidence more certain.

## Why Orange leads

Orange's strongest comparative advantage is evidence across multiple water-system stages with repeated publication. Council's water-supply page links quarterly source-operation/DST reports, water-use summaries, annual raw-water/hydrology/aquatic-environment and groundwater reports, plus monthly source-extraction reports. These offer more recurring, town-attributed operational context than static strategy documents alone, even though publication as individual PDFs prevents treating them as a clean machine-readable time series. [1, 4]

The evidence also spans treatment quality (the 2024 Icely Road report with sample counts and summarized physical, chemical, microbiological and PFAS results), supply infrastructure and asset planning, stormwater-harvesting schemes, and sewerage/reuse planning. The Orange source material is broader and more temporally recurrent than the strongest alternatives, while explicitly identifying limitations: no verified Council asset GIS, no confirmed station-specific WaterNSW/BOM series for Orange, no raw sample-level drinking-water export, and no comprehensive wastewater/reuse or stormwater operating series. [2–6]

State hydrology portals and statewide spatial layers provide useful potential context but cannot be credited as confirmed Orange observations without station-level validation. The statewide NSW Foundation Spatial Data Framework Water theme is explicitly CC BY 4.0, but that does not license Council's reports or establish Orange utility network geometry. [7, 8]

## Strongest runner-up: Broken Hill

Broken Hill is the closest single-town challenger. Its town-specific quarterly and annual drinking-water reports extend through recent years; Essential Water also publishes wastewater-treatment monitoring and licence material with stated monthly Wills Street and quarterly South sampling, and town-specific supply documentation. BOM groundwater discovery/downloads and WaterNSW data/API paths add potentially useful machine access, although no definitive supply-relevant groundwater time series was validated and the API's documentation/testing requires registration. Much of the local utility evidence is PDF/web-based, and no complete local network GIS or broad town operational telemetry was verified. [9–13]

Broken Hill loses to Orange on the selected rubric because Orange's audited evidence has a stronger combination of recurrent source-operation reporting (quarterly and monthly), annual hydrology/ecology/groundwater reports, stormwater harvesting documentation and sewerage asset planning. Broken Hill's repeated drinking-water and wastewater compliance reporting is a real strength, but does not close the machine-readable and network-asset gaps, and its water-security research includes older investigation rather than a current operational groundwater series. The two are close enough that a future validation of machine-readable exports or local station history could narrow or change the ranking.

## Apples-to-apples limits and the combined-corridor issue

The candidates are not perfectly comparable units. Orange, Dubbo, Tamworth and Broken Hill are town-centered audits, while **Cobar–Nyngan** spans two councils and **Menindee / Broken Hill supply corridor** combines distinct settlements, suppliers and supply contexts. Comparing a two-town corridor's aggregate source inventory with one town can inflate breadth and temporal coverage. Conversely, a town-specific utility may report through a larger council or utility boundary, making town attribution weaker than its publication volume suggests.

The corridor must not be collapsed into a fictional single town: Essential Water's sources distinguish Menindee's Darling River supply from Broken Hill's Murray River supply via the Wentworth pipeline (following a 2019 source change). Menindee Lakes are relevant to regional resource and historical/security context, but their gauges and storages are not direct measurement of Broken Hill's delivered treated water. Corridor-wide gauge observations and reports cannot be counted as town-network telemetry. [9, 10]

For this reason, the table scores the corridor conservatively on town operational utility, and the standalone Broken Hill score is shown separately rather than merged with it. A true combined regional case may be appropriate for a study of interconnected source security; it is not a like-for-like choice of one Repository Town.

## Recommendation on the existing Menindee electrical case

**Shift the single base town to Orange** if maximum public water-data evidence is the priority. Keep the existing Menindee electrical case intact as a separate electrical-focused case, or as a clearly labeled cross-case comparator; do not silently relabel it as Orange, and do not claim Menindee is the best water-data base on the present evidence. Orange and Menindee have different systems and evidence profiles, so this is a scope change, not a data merge.

If the repository cannot support two cases and continuity of the existing Menindee work is a hard constraint, the defensible fallback is to retain Menindee for the electrical case while explicitly accepting a weaker/uneven public water-data basis. The current audit does not support claiming Menindee alone beats Orange for water-data evidence. The recommendation prioritizes the stated maximum-public-water-data criterion over convenience or prior electrical-case continuity.

## Evidence limitations and validation before implementation

The underlying audits explicitly describe themselves as focused inventories, not exhaustive searches. This comparison inherits that boundary and the supplied source judgments; it has not independently re-extracted every portal, verified every PDF, or tested all downloads. Most important unresolved checks are: (1) whether Orange's periodic reports contain extractable, consistently defined underlying tables; (2) which Orange-area WaterNSW/BOM stations have relevant parameters and date coverage; (3) whether any candidate utility has since exposed operational data or asset GIS absent from the audits; and (4) dataset-specific licence and attribution terms. Those checks could affect machine-readability and reuse scoring. Proposed infrastructure is never treated here as commissioned operation. Groundwater/resource context is not conflated with town supply operations.

Before ingesting data, record the actual file/page version and observation period, custodian, geography, measurement unit, missingness/quality flags, and item-level reuse terms. Treat published PDF summaries as citations/context unless data have been extracted and checked; do not infer continuous observations from periodic reports.

## References

1. Orange City Council, [Orange’s water supply](https://www.orange.nsw.gov.au/water/oranges-water-supply/) — DST archive, source-operation and monitoring entry point.
2. Orange City Council, [Drinking Water Monitoring Report Orange City Council 2024](https://www.orange.nsw.gov.au/wp-content/uploads/2025/01/OCC-Water-Quality-Report-2024.pdf).
3. Orange City Council, [Water Supply Asset Management Plan 2020–2049](https://www.orange.nsw.gov.au/wp-content/uploads/2020/08/2020-21-Water-Supply-AMP.pdf).
4. Orange City Council, [Macquarie River to Orange Pipeline reports and monthly extraction reports](https://www.orange.nsw.gov.au/water/macquarie-pipeline).
5. Orange City Council, [Sewerage Asset Management Plan 2023–2052](https://www.orange.nsw.gov.au/wp-content/uploads/2024/04/Sewerage-AMP-2023.pdf) and [stormwater harvesting documentation](https://www.orange.nsw.gov.au/water/stormwater/).
6. Orange City Council, [treatment plant and PFAS information](https://www.orange.nsw.gov.au/water/water-treatment-plant); [PRW demonstration-plant business-case tender](https://www.orange.nsw.gov.au/water/tender-let-for-purified-recycled-water-demonstration-plant/) (proposal-stage, not operating-data evidence).
7. NSW DCCEEW, [water monitoring stations](https://www.water.dcceew.nsw.gov.au/our-work/science-data-and-modelling/maps/water-monitoring-stations); WaterNSW, [real-time water data](https://realtimedata.waternsw.com.au/); BOM, [Water Data Online](https://www.bom.gov.au/waterdata/).
8. NSW Government, [Foundation Spatial Data Framework Water theme and licensing](https://www.nsw.gov.au/environment-land-and-water/spatial-data-and-mapping/foundation-spatial-data-framework/water).
9. Essential Water, [service and supply description](https://essentialwater.com.au/about-us/who-we-are-and-what-we-do/) and [water-quality reports](https://essentialwater.com.au/water-insights/water-quality-reports/).
10. Essential Water, [wastewater treatment plant monitoring and EPL documents](https://essentialwater.com.au/water-insights/waste-water-treatment-plant-monitoring-data/); [IWCM strategy page](https://essentialwater.com.au/about-us/iwcm-strategy/).
11. WaterNSW, [water data and API information](https://www.waternsw.com.au/water-services/water-data); BOM, [Australian Groundwater Explorer](https://www.bom.gov.au/water/groundwater/explorer/).
12. NSW DCCEEW, [local water utility performance](https://www.water.dcceew.nsw.gov.au/our-work/local-water-utilities/local-water-utility-performance).
13. Geoscience Australia, [Broken Hill Managed Aquifer Recharge project](https://www.ga.gov.au/about/projects/water/broken-hill-managed-aquifer-recharge).
14. Dubbo Regional Council, [Water Quality and Treatment](https://www.dubbo.nsw.gov.au/Our-Region-Environment/Water-sewerage-and-drainage/water-quality-treatment); [advanced wastewater plant completion notice](https://www.dubbo.nsw.gov.au/news-and-media/news-and-resources/council-news/2026/water-security-a-reality-with-completion-of-advanced-wastewater-treatment-plant).
15. Tamworth Regional Council, [Water Supplies](https://www.tamworth.nsw.gov.au/live/water-and-wastewater/water-supplies) and [Wastewater](https://www.tamworth.nsw.gov.au/live/water-and-wastewater/wastewater).
16. Cobar Shire Council, [Water Supplies Asset Management Plan](https://www.cobar.nsw.gov.au/wp-content/uploads/2021/11/06_-_Water_Asset_Management_Plan.pdf); Bogan Shire Council, [drinking-water quality management report](https://bogan.nsw.gov.au/everyday-living/water-sewer/drinking-water-quality-management-report).
17. WaterNSW, [Menindee Lakes](https://www.waternsw.com.au/nsw-dams/regional-nsw-dams/menindee-lakes); BOM Murray–Darling Basin Water Information Portal, [Lower Darling](https://mdbwip.bom.gov.au/lower-darling).
