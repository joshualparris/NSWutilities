# Public GIS, hardware, and real asset placement — investigation

**Date:** 25 October 2026  
**New finding:** A public NSW ArcGIS server currently exposes an `Essential_Energy_Poles` **FeatureServer** and **MapServer** layer. It may make actual pole-based visual placement possible where coverage, permission, currency and quality are confirmed.

## 1. Public spatial data (verified that service/layer schema exists; NOT yet downloaded or locality-verified)

**Official NSW data-hosted service:** https://portal.data.nsw.gov.au/arcgis/rest/services/Hosted/Essential_Energy_Poles/FeatureServer  
**Pole layer metadata:** https://portal.data.nsw.gov.au/arcgis/rest/services/Hosted/Essential_Energy_Poles/FeatureServer/3  
**Public map viewer:** https://portal.data.nsw.gov.au/arcgis/rest/services/Hosted/Essential_Energy_Poles/MapServer

The publicly displayed layer metadata reports:
- Geometry: `esriGeometryPoint`, spatial reference `EPSG:3857`, query support, max 2000 records per response and pagination.
- Attributes include `asset_id`, `label`, `depot`, `feeder`, `fdr_area`, `function_`, `highest_v`, `gps_source`, `locality`, `material`, `length_`, `strength`, `region`, `status`, `owner`, `date_e`.
- The layer being queryable **does not establish its licence, freshness, accuracy, Menindee completeness, or suitability for a game**. No pole records or personal/customer data were imported in this research pass. Do not publish sensitive internal asset attributes or inferred operational weakness pathways.

**Immediate next verification**: query only aggregate count/coverage by locality through the service under its usage terms, confirm `locality` values/records exist in chosen town, investigate data ownership and open reuse permission, then inspect **non-sensitive geometry** and compare against public road alignments. Fail gracefully to plausible synthetic pole spacing and keep every observed/synthetic segment labelled.

**Note on limits**: A point layer of poles does not itself document the wire edges between poles, electrical switch states, fuse coordination, which property connects to which phase, or actual service-line routes. Never create true operational network claims by connecting all spatially adjacent dots.

**Official Essential Energy mapping portal:** https://www.essentialenergy.com.au/maps and https://www.essentialenergy.com.au/our-network/managing-the-network  
Essential Energy describes a Network Information Portal with pole/network-route access and optionally requested network data. https://engage.essentialenergy.com.au/access-to-network-data
The official DAPR data portal https://dapr.essentialenergy.com.au/ supports voltage-category line overlays (220/132/110/66/33/22/19.1/12.7/11/6.6/6.35 kV), bulk points and zone substation layers. These are **general planning layers**, with their own usage disclaimer.

## 2. Typical visual assets confirmed

**Essential Energy** *Quick Reference Guide: Working near Essential Energy assets*, **1 July 2024**, p5 **Figure 2**, directly depicts real asset appearances: roadside padmount substations, underground cabling, green electricity pillars, pole-mounted streetlights and local overhead distribution structures.  
Public reference (link only, image licensing not established): https://www.essentialenergy.com.au/-/media/Project/EssentialEnergy/Website/Files/Safety/Quick-Reference-Guide-Working-near-Essential-Energy-Assets.pdf?rev=a4c31af962e44b728a5857034e57a76c

Use shape/convention as **visual reference**, create original 3D models rather than redistributing sourced photos/assets. Structural clearance figures are engineering/safety-dependent and *not* safe-to-build advice or unconditionally universal.

## 3. Specific actual hardware, verified

- **Broken Hill grid battery:** AGL 50 MW / 50 MWh installed and in service Aug 2024; 22 kV cable to Broken Hill substation. AGL's 27 Sep 2024 ARENA public report identifies **EPC Power** grid-forming-capable inverters and **Fluence/Valmec** EPC contractor. This substantiates real manufacturer involvement, **but not an exact inverter SKU or every battery-cell make**.
- **Bawley Point/Kioloa:** Endeavour Energy public status documents approximately 3 MW community BESS, distributed customer PV/battery systems and DERMS; an Endeavour notification says work involved replacement of inverters. **Do not infer specific home-battery brand or installed panel models without datasheets and project records**.
- **Menindee homes:** 2022 community plan indicates aerial service drops and pole-mounted lighting, but does not confirm pole manufacturer and exact line dimensions.

## 4. Solar safety and compliance source facts

Essential Energy requires connection assessment/approval and provides guidance on voltage rise, export limits, inverter make/model and battery kWh/kW declarations:
- Solar: https://www.essentialenergy.com.au/at-home/micro-embedded-generation
- Batteries: https://www.essentialenergy.com.au/at-home/battery-storage
- Network connection classes: https://www.essentialenergy.com.au/getting-started
- State solar connection guide: https://www.nsw.gov.au/housing-and-construction/building-or-renovating-a-home/during-building-process/guide-to-solar-panels

The historical **November 2018 NSW Service and Installation Rules** PDF https://www.energy.nsw.gov.au/sites/default/files/2022-08/2018_11_NSW_ServiceAndInstallationRulesOfNSW_unmarked.pdf is stamped **SUPERSEDED — FOR REFERENCE ONLY**, so **DO NOT** use that file as proof of current 2026 requirements. Research the latest rules and AS/NZS standards under NSW-ELEC-017.

## 5. Follow-up needed

- [ ] Verify GIS dataset licence, timestamp, scope and update method.
- [ ] Check Menindee/selected locality coverage without disclosing real vulnerabilities.
- [ ] Compare actual pole points against roads and buildings; document offsets and misses.
- [ ] Determine documented spans/line routing separately; infer only when labelled.
- [ ] Read current distributor overhead asset type references and up-to-date 2026 standards.
- [ ] Verify actual make/model/datasheet for typical Australian rooftop PV and BESS; do not automatically assign brand to real households.
- [ ] Implement optional `spatial_evidence` provenance and an explicit fallback to synthetic wiring.

**Implementation constraint:** Never make an engineering claim from a GIS map alone, and never treat public regional pole locations as permission for operational asset control or security analysis.
