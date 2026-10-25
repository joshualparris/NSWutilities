# Stormwater and flood drainage — NSW evidence register

**Date:** 25 October 2026. All links are public primary-source publisher pages or the official/open-source engine repositories. Source URLs were checked during this research session; **the full linked PDFs, raw GIS, model parameters, licence and any real asset geometry have NOT been ingested or independently quality-assured**. Do not treat public visibility as redistribution permission.

### SW-S01 — Stormwater network and management overview
Publisher: Dubbo Regional Council
URL: https://www.dubbo.nsw.gov.au/Our-Region-Environment/Water-sewerage-and-drainage/stormwater
Research relevance: Council describes >200 km urban pipes, >6,500 pits, 62 GPTs and >70 retarding basins across the LGA; total counts, not GIS geometry.

### SW-S02 — Design Rainfalls / IFD
Publisher: Bureau of Meteorology
URL: https://www.bom.gov.au/water/designRainfalls/
Research relevance: IFD depth vs intensity, duration and AEP; historical design statistics are not an observed event forecast.

### SW-S03 — Australian Rainfall and Runoff 2019 guidance
Publisher: Geoscience Australia / Engineers Australia
URL: https://arr.ga.gov.au/arr-guideline
Research relevance: National design estimation methodology and associated data; version/rights of downloads to verify.

### SW-S04 — Australian Rainfall and Runoff purpose and updates
Publisher: Geoscience Australia
URL: https://www.ga.gov.au/scientific-topics/community-safety/data-and-products/arr
Research relevance: ARR revision, flood hydrographs and climate-change considerations.

### SW-S05 — Storm Water Management Model (SWMM)
Publisher: US EPA
URL: https://www.epa.gov/water-research/storm-water-management-model-swmm
Research relevance: Engine features: hydrology, LID, kinematic/dynamic wave, ponding, quality; not an Australian calibrated model.

### SW-S06 — SWMM solver source (public domain per README)
Publisher: US EPA GitHub
URL: https://github.com/USEPA/Stormwater-Management-Model
Research relevance: Source review and offline benchmark candidate; pin SHA/version.

### SW-S07 — Managing floodplains: council responsibilities
Publisher: NSW Environment and Heritage
URL: https://www.environment.nsw.gov.au/topics/water/floodplains/managing-floodplains
Research relevance: Council flood risk study, development and works responsibilities; does not establish Repository Town hazard zones.

### SW-S08 — Flood risk management framework guidance
Publisher: NSW Environment and Heritage
URL: https://www.environment.nsw.gov.au/publications/delivery-under-flood-risk-management-framework
Research relevance: Emergency and floodplain management planning principles (framework, not a game solver).

### SW-S09 — Planning resource documents and flood studies
Publisher: Dubbo Regional Council
URL: https://www.dubbo.nsw.gov.au/Builders-Developers/Planning-Controls-Tools-and-Resources/planning-resource-documents
Research relevance: Flood resource listings; individual maps have dates and copyright restrictions.

### SW-S10 — Dubbo Regional Council listings
Publisher: NSW Flood Data Portal
URL: https://flooddata.ses.nsw.gov.au/organization/dubbo-regional-council
Research relevance: Published studies, local-specific scopes/dates; portal does not validate underground pipe topology.

### SW-S11 — Dubbo regional flood preparedness
Publisher: NSW SES
URL: https://www.ses.nsw.gov.au/local-information/dubbo-regional
Research relevance: Flood warnings/community hazards; don't turn game simulation into real flood advice.

### SW-S12 — Orange stormwater harvesting project update, 7 Jan 2026
Publisher: NSW DCCEEW
URL: https://www.water.nsw.gov.au/news/boost-orange-stormwater-harvesting
Research relevance: Orange shows specific stormwater-to-water-source integration; planned new stage ≠ completed operating supply.

### SW-S13 — Open-source SWMM solver fork
Publisher: Open Water Analytics
URL: https://github.com/SWMM-Project/swmm-solver
Research relevance: Secondary code audit with distinct licensing; no reuse without checking exact licence.

### SW-S14 — 2016 IFD method information
Publisher: Bureau of Meteorology
URL: https://www.bom.gov.au/water/designRainfalls/ifd/index.shtml
Research relevance: Design rainfalls derived statistically; must combine with relevant ARR design inputs.

## Import and provenance requirements

For each real claim or dataset, keep source ID, publisher, URI, publication date, retrieval time, units, Australian time zone (Australia/Sydney where applicable), site or LGA scope, licence, sensitivity/redistribution status, measured-versus-design-versus-synthetic flag, version and schema/hash. Weather/rainfall observations, design IFD statistics, historic inundation layers, public infrastructure totals and measured stormwater pipe connections are **different evidence classes**. No surveyed real pipe route or floor level is established here. Do not import confidential exact critical-asset geolocation into the public repository.
