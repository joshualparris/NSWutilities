# NSW-ELEC-007 — Reproducible AEMO five-minute NSW demand and generation data

**As of:** 25 October 2026. **Reference trading day:** 20 October 2026 in fixed NEM market time (AEST UTC+10; independent of NSW daylight saving). **Status:** Executable source-backed import with automated tests; one full sample trading day published. This is **not** a calibrated Menindee feeder and **not** the entire historic NEM archive.

## Source and provenance

- [AEMO public daily DISPATCHIS nested ZIP](https://nemweb.com.au/Reports/ARCHIVE/DispatchIS_Reports/PUBLIC_DISPATCHIS_20261020.zip): five-minute `DISPATCH,REGIONSUM` records for `NSW1.TOTALDEMAND` (MW), and `DISPATCH,PRICE` records for `NSW1.RRP` (AUD/MWh).
- [AEMO public daily DISPATCHSCADA nested ZIP](https://nemweb.com.au/Reports/ARCHIVE/Dispatch_SCADA/PUBLIC_DISPATCHSCADA_20261020.zip): five-minute `DISPATCH,UNIT_SCADA` readings by `DUID` (MW), spanning all NEM regions; these are not a NSW supply mix without matching to an official register.
- [AEMO official NEM registration and exemption XLSX](https://www.aemo.com.au/-/media/files/electricity/nem/participant_information/nem-registration-and-exemption-list.xlsx?rev=ef75714f508b47f69449a056744d924a&sc_lang=en): `PU and Scheduled Loads` worksheet, `DUID`, `Region`, `Fuel Source - Primary`, `Fuel Source - Descriptor`, `Technology Type - Primary`. Its snapshot can be revised independently; SHA256 captured at import time. Registration may lag the historic SCADA date. Ambiguous/unknown DUIDs remain unclassified.
- Original archives are **not** committed; reproducible source URLs and source-file checksums are recorded in the JSON quality report.

## Files and reproduction

- `tools/data-import/aemo_dispatch.py`: downloads two daily AEMO archives plus registration workbook, reads every nested CSV, joins separate NSW demand and price, aggregates NEM SCADA and **registered NSW1 generation** by source/fuel, and exports local AEST and UTC timestamps.
- `tools/data-import/test_aemo_dispatch.py`: deterministic ZIP fixture tests for schema, full 288-interval day, missing intervals, daylight saving, no cross-region generation counts and fuel classification.
- `data/aemo/2026-10-20/nsw_nem_dispatch_5m.csv`: 288 interval rows with demand/price, fuel-specific NSW1 generation estimates (MW), battery charging and NEM-wide raw SCADA summaries.
- `data/aemo/2026-10-20/quality_report.json`: SHA256 hashes, source coverage, missing/duplicate intervals and fuel classification.
- `.github/workflows/nsw-elec-006.yml`: executes Python unit tests, live source import, interval completeness check, uploads a verification artifact and commits the derived dataset on the task branch.

```sh
python -m pip install openpyxl
python -m unittest discover -s tools/data-import -p 'test_*.py' -v
python tools/data-import/aemo_dispatch.py --day 2026-10-20 --out data/aemo/2026-10-20
```

For other dates, change `--day YYYY-MM-DD`; only archive dates actually present on AEMO NEMWeb can be used. `--scada-zip`, `--dispatch-zip`, and `--registration-xlsx` allow offline/local replay. `--allow-incomplete` records gaps instead of rejecting a source day; never silently fill missing observations.

## First-day baseline (from actual AEMO files)

- **288/288** five-minute NSW1 dispatch demand observations, matching prices and matching full-NEM SCADA intervals, **no missing/duplicate interval entries** in the tested day.
- **517** unique SCADA unit IDs, **148,889** unique time-unit observations. An official AEMO workbook matches **481** of those IDs; remaining **36** unclassified, and not assumed to be NSW.
- NSW demand: **min 4387.13 MW**, **mean 6447.14 MW**, **max 8353.59 MW**.
- NSW spot price: **min -$10.50/MWh**, **mean $101.862/MWh**, **max $201.17/MWh**.
- These are historical NEM operational figures for the date, not an electrical prediction for 2026 today.

## Correct interpretation

This data gives a realistic upstream NSW **market and generation reference layer**, **not the actual currents feeding an individual NSW town**:

1. Registered `NSW1` generator SCADA is grouped by official primary fuel/descriptor: coal, gas, diesel/oil, hydro, wind, solar, battery, biomass and other. It is an **observed dispatch-unit proxy**, not all generated electricity.
2. Rooftop PV, unregistered generation, cross-border exchanges and unclassified DUIDs prevent these groups from equalling NSW consumption or physical grid imports. AEMO regional demand is a distinct series.
3. `NSW_scada_battery_mw` is *positive measured discharge*; `NSW_scada_battery_charging_mw` is measured charging shown separately and must **not** count toward generation.
4. Many resource types are not directly schedulable on a fictional town feeder; Repository Town's local solar, loads, outages, line ratings and topology are distinct.
5. AEMO records are **5-minute interval-ending AEST**; Sydney local clock can be AEDT, so keep fixed market time for reproducibility.

## Acceptance and remaining scope

[x] Official real daily NEMWeb sources accessible, nested tables decoded.  
[x] Test suite with missing-data assertions and source class/region mapping.  
[x] A complete reference day saved with source fingerprints and tests.  
[ ] Import and validate many representative days (summer/winter, outages) and archive calendar.  
[ ] Validate generator-fuel classifications against dated registration changes and ownership.  
[ ] Couple reference demand/market conditions to an implemented Repository Town grid (separate NSW-ELEC-011).  
[ ] NSW-ELEC-006 zone substation 30-minute records remain blocked by distributor HTTP 403 from GitHub runner; **do not falsely mark it finished**.

This document is part of the same numbered task stream as [TASKS.md](./TASKS.md). No unverified mobile/game deployment is claimed.
