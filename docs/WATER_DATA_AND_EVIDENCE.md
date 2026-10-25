# NSW-WAT — Source provenance and data-import requirements

**As of 25 October 2026; verification stage:** URLs and publisher claims located, dataset retrieval + permissions + schema validation *not yet done*. The [earlier 41-source register](WATER_SOURCES.md) remains authoritative for its original synthesis; below are additional exact primary evidence targets and realistic import gates.

| Source | Asset / metric and temporal grain | Evidence / date | Licence and integration gate |
| --- | --- | --- | --- |
| Dubbo Regional Council water/sewer responsibilities | Macquarie River/bore source shares, John Gilbert / Wellington works, wastewater licence/monitoring, historic monthly extracts | Live council narrative; historic/typical shares not continuous sensor values | Published text is not granted GIS reuse permission; licence check |
| Dubbo Council advanced reuse plant notice | Completed 8 Sep 2026; up to **700 ML/year capacity**; reuse approvals still being sought for concrete/dust applications | [Council announcement](https://www.dubbo.nsw.gov.au/news-and-media/news-and-resources/council-news/2026/water-security-a-reality-with-completion-of-advanced-wastewater-treatment-plant) | **Design/nameplate capacity only**. Do not treat as operating daily delivered volume or authorised end-use |
| WaterNSW real-time monitoring | Surface water levels/flows, bores, rainfall, storage and quality; varying station and intervals | https://realtimedata.waternsw.com.au/ | Verify station IDs, available parameters, missing/quality codes, retrieval date, API usage and [attribution](https://api-portal.waternsw.com.au/data-attribution) |
| NSW DCCEEW allocations | Legal/accounting allocation and licences, distinct from physical intake flows | https://www.water.dcceew.nsw.gov.au/our-work/allocations-and-availability/allocations/allocations-dashboard | Don't infer a property entitlement from a dam's percent full |
| BoM rainfall | Daily, hourly or station-specific observed precipitation; local zone selection | https://www.bom.gov.au/climate/data/ | Timestamp/timezone (Australia/Sydney with DST) and site-distance metadata essential |
| Council sewage/water licences | Pollutant measurements at reported discharge sites | https://www.dubbo.nsw.gov.au/Our-Region-Environment/Water-Sewerage-and-Drainage/councils-water-and-sewer-obligation | Discharge compliance observations are **not** household tap water readings; never back-calculate potable safety |
| NSW Health DWMS | Drinking-water quality assurance program and critical control points | https://www.health.nsw.gov.au/environment/water/Pages/water-utilities.aspx | No operational water-quality decision from simulation |
| NSW plumbing/standards | NSW Plumbing Code; PCA/AS/NZS 3500 edition and adoption | https://www.nsw.gov.au/housing-and-construction/compliance-and-regulation/plumbers-and-drainers/standards-and-notes | Standards text/licence and current adoption must be checked; avoid publishing copyrighted text |

## Canonical acquisition schema

Each observation: `{ sourceId, sourceUrl, publisher, parameter, value, unit, stationId, observedAtUtc, retrievedAtUtc, zone:"Australia/Sydney", qualityFlag, licenceId, snapshotHash, evidence:"documented" }`. Missing values are `null`, never `0`. No interpolation over source outages unless clearly `modelled`. Validate monotonic timestamps; time windows across daylight savings; physically meaningful unit conversions (ML→1e6 L; L/s→3,600 L/h); downstream `recordQuality` and missing-station report. Save original immutable files/checksums and transformed public aggregates only with reuse permission.

## Do not conflate

- **Treatment plant capacity (ML/yr)** ≠ measured output ML/day ≠ legal allocation ≠ community consumption.
- **River level (m)** ≠ discharge (ML/day) without site-specific rating relationship.
- **Electrical pump nameplate (kW)** ≠ water moved (L/s) without pump/system curves.
- **Residual disinfectant / regulatory sampling** ≠ a yes/no health certification by the game.
- **Town map river line** ≠ asset pipe geometry. Derive a synthetic pipe graph if open asset evidence is inadequate and label it accordingly.

**Status:** No live WaterNSW/BoM download, calibration or data-import tests have been verified. Must remain an open NSW-WAT task.
