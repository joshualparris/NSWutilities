# NSW regional electricity: source-backed findings (25 October 2026)

**Status:** First-pass source-based research and an implementable modelling direction. This is not a detailed field survey, certified engineering model or production game implementation.  
**Small-town pilot:** **Menindee, NSW**, within the **Broken Hill/Far West supply area**. Broken Hill is a regional centre, *not* the small town chosen for the first playable neighbourhood.  
**Complementary case:** Bawley Point/Kioloa microgrid for sophisticated solar, battery, DERMS and islanding behaviour.

## 1. Town evidence comparison (provisional, not a census of every town)

| Area | Verified public evidence | Main gap | Use |
| --- | --- | --- | --- |
| **Menindee within Broken Hill area** | Essential Energy 2025 DAPR p53 regional network schematic and labelled lines; 2022 Menindee community infrastructure plan (power and streetlights); Essential Energy 30-minute zone-substation datasets; NSW Apr 2025 post-event report; Parliament Jun 2025 outage investigation; Transgrid line restoration reports; AGL/ARENA battery reports | Exact street-by-street pole/phase/transformer/customer mappings and site-level outage records not publicly established | **Chosen small-town exemplar**, with larger Broken Hill for upstream supply, BESS and outage replay |
| **Bawley Point / Kioloa** | Endeavour Energy DAPR 2024 p62 public system description; 3 MW/approx 3 MWh community battery, local PV and home batteries, DERMS and microgrid, newsletters covering testing and commissioning, operator vs automated restoration | Full public feeder circuit diagram, individual customers, verified voltage/impedance data | **Second scenario:** intentional islanding / community energy |
| **Bega / Cobargo** | Essential Energy DAPR includes Bega supply area; resilience context | Comparable detailed outage/DER-specific evidence not yet collected in this pass | Future candidate |
| **Parkes** | Essential Energy DAPR has Parkes supply area; historical zone load data | Less integrated publicly reviewed microgrid/outage evidence found so far | Conventional rural-grid comparator |

*Reason for selection*: Far West supplies uniquely complementary public **topology + time series + major event + restoration + generator + BESS + solar/wind** sources. Not claiming unique global/local documentation superiority without further comparative inventory.

## 2. Verified upstream and town infrastructure

- **Supply dependency:** A publicly documented 220 kV Transgrid line X2 between Buronga and Broken Hill is a critical connection. IPART's Dec 2024 investigation says the area has no second direct transmission supply from the national grid in that configuration. Do not label X2 an arbitrary multiple redundant connection.
- **Transformations:** Essential Energy's **2025 DAPR p53** gives Broken Hill a **220/22 kV Transgrid** zone symbol and identifies **66 kV, 33 kV and 22 kV** components throughout the surrounding supply area. It labels feeders **BHL32 South** and **BHL82 Cockburn**, zone substations including Menindee, and several SWER loads. This *schematic* is not the actual street-level pole layout.
- **Backup plant:** DAPR p53 notes **two 25 MVA gas turbine generators** connected to the Broken Hill zone substation **22 kV busbar**. Treat MVA as apparent-power nameplate, not MW output; generator availability and operating conditions vary.
- **Distant resources:** Public schematic labels **Silverton Wind Farm 200 MW** and **Broken Hill Solar Plant 53 MW**. They connect in the regional system; do not equate nameplate with momentary available output or assume renewables could automatically energise an isolated grid.
- **Broken Hill BESS:** AGL/ARENA document **50 MW / 50 MWh** as-built and grid-forming-capability study, operational from **August 2024**. ARENA's project report states a **22 kV connection** to the Broken Hill substation and documents grid-forming/grid-following technical restrictions. NSW planning consent once described **50 MW / 100 MWh** proposal; distinguish *approved project envelope* from *built operating plant*.
- **Menindee local characteristics:** The publicly accessible *Menindee Community Housing and Environmental Health Plan*, section 9.7 (dated 5 July 2022), describes connection via regional supply, aerial service cables to dwellings, and pole-mounted streetlights. Its substation voltage description may differ from diagram legend/line labels in more recent DAPR: **reconcile source versions before claiming Menindee transformer winding specifics**.
- **Regional reactive loading:** Zone datasets include half-hourly **kW and kVAr** measurements where publishable, generally October–September year blocks, and need filtering by selected zone substation and source data-quality notes.
- **Network operator:** Essential Energy is the relevant regional **distribution** operator, Transgrid the major transmission operator. AEMO dispatches and coordinates the National Electricity Market. Retailers are not power-line owners. This matters for simulated repair responsibility.

### Minimal evidence-backed reference topology (not a street-level as-built map)

```text
NEM generation across NSW/interconnectors
  coal, hydro, gas, wind, solar, storage + interstate power flows
        |
   220 kV transmission (regional X2 supply to Broken Hill)
        |
   Broken Hill Transgrid substation / 22 kV bus (published)
        +---- backup gas turbines [2 x 25 MVA nameplates]
        +---- BESS [50 MW / 50 MWh; 22 kV connection]
        +---- Broken Hill local distribution [BHL32, BHL82]
        +---- regional subtransmission (66 kV / 33 kV feeders)
                    |
              zone substations
                    |
              Menindee distribution feeders
                    |
           [synthetic, to be built and labelled]
           street transformers -> LV lines -> meters -> buildings
```

**Important:** This intentionally compresses the district schematic: the BESS and wind/solar projects have different specific grid interconnections and must not be drawn as a single shared feeder without evidence. More detailed edges must be reconciled from published one-line sources.

## 3. Outage 17–31 October 2024: reproducible scenario

Government's April 2025 post-event report and parliamentary review establish:
1. **17 October:** extreme weather damages **seven 220 kV transmission structures**, isolating Broken Hill and far-west communities; **10,000+** customer connections affected.
2. **18 October:** backup gas turbine re-energises many customers after a substantial initial blackout; there are damaged distribution assets and generation/load-shedding constraints.
3. **20–25 October:** maintenance and plant/controls/fuel-pump difficulties cause further outages and scheduled load shedding; some customers are deliberately disconnected when insufficient power is available.
4. **24 October:** temporary generator bank at **Pinnacles Place** supports an isolated remote-community microgrid supplying places including **Menindee, Wilcannia, White Cliffs and Tibooburra**; occasional trips occurred.
5. **26 October:** AGL battery reconnected to the isolated network, per parliamentary chronology. It is wrong to assume the battery was seamlessly operating throughout the entire initial event.
6. **31 October:** repaired transmission line was energised and communities progressively transitioned back to main-grid supply (local time and exact per-town interruption profiles differ).

**Replay mechanics:** model line fault -> trip/isolate -> blackout dependent loads -> emergency generation limited by available capacity -> intentional load shedding -> temporary source with restricted island size -> BESS reconnection only when configuration permits -> final grid restoration. Actual switch positions, relay timings and protected asset lists are **not** public and must be synthetic; make these choices clear in game and docs.

## 4. Alternate resilience case: Bawley Point/Kioloa

Endeavour Energy describes **~3 MW** community BESS combined with rooftop solar, household batteries and a Distributed Energy Resources Management System (DERMS). Its 2024 DAPR describes approximately **3 MVA / 3 MWh**; a 2025/2026 public page reports ~100 subsidised homes rather than assuming all homes participate. Different documents may describe different participation counts or project phases. Holiday tourism produces local peak-load pressure. **Dec 2025 newsletter** says Kioloa has an **automatic restoration scheme** for specific outage conditions, while Bawley Point and Termeil rely on operator restoration under the described status. Do not portray islanding as unconditional or instant for every neighbourhood. Use this site to teach: grid-forming inverter, transfer/isolation point, protected island, SOC/time-to-empty and load prioritisation.

## 5. How to simulate electricity correctly

### Data model

- `Asset`: immutable ID, `source_ref`, geometry, owner, `documented|inferred|synthetic`, as-of date, subtype and manufacturer/model only when sourced.
- `Bus`: AC nominal line-line voltage, phase set, source region.
- `Branch`: from/to bus, impedance or approximate conductor type/length, phase, ampacity, open/closed, fault state.
- `Transformer`: HV/LV buses, kVA nameplate, winding/configuration where known, taps, loading and thermal model.
- `Generator`: technology, output kW, max kW, fuel/weather constraints, availability, ramp, grid-forming and emissions.
- `PV`: DC kWp, AC inverter kVA, irradiance/orientation/shading, export limit, anti-islanding capability.
- `Battery`: kW charge/discharge rating, usable kWh, SOC, min reserve, charging/discharging efficiencies, thermal derate, backup/islanding role.
- `Load`: building/service, single/three-phase connection, p_kW, q_kVAr, priority, time/weather curves, critical circuit constraints.
- `Protection` and `Switch`: simplified state machines, safe fault-isolation logic, recloser/fuse event, restoration eligibility.
- `Snapshot/Event`: 5-minute economic/demand timestep with immediate fault events, deterministic seeded weather and event replay.

### Physics and electrical state

For each building:
- **Demand:** `P_load(t) = baseline(type,time,season,occupancy) + temperature_effect + device_events`; assign a probability distribution, not one uniform building wattage.
- **PV:** `P_pv_ac <= min(inverter_ac_limit, solar_kwp * irradiance_fraction * derates)`; cloud/thermal/shade/weather and islanding constraints change output.
- **Battery:** `E_next = clamp(E + P_charge * eta_charge * dt - P_discharge * dt / eta_discharge, E_min, E_max)`, with **dt in hours** and P in kW. Charging/discharging limited separately by kW, not just kWh.
- **System balance:** `P_grid_import + sum(P_generation) + sum(P_battery_discharge) = sum(P_load_served) + sum(P_battery_charge) + P_losses + P_grid_export`.
- **Branch model:** first pass radial LinDistFlow/voltage drop and thermal ratings; use OpenDSS/three-phase method for actual unbalanced feeders. Do **not** interpret a simple flood-fill of wired buildings as proof of delivered power quality.
- **Critical loads:** water pumping, sewerage, clinic, telecoms, level crossings, refrigeration and streetlights react differently to low voltage, complete trip and generator connection.
- **State machine:** `energised -> faulted/tripped -> isolated -> repaired -> tested -> reclosed -> energised`; loop sources and backfeed must be handled, not blindly energised.
- **Island constraint:** normal grid-following rooftop solar must shut down absent a valid grid reference. Only properly configured transfer/backup systems or grid-forming microgrids can legitimately continue operating with an isolated network.

### Scheduling

- Game UI can render continuously at normal FPS.
- Network topology updates whenever assets change or breakers trip.
- Run 5-minute-equivalent dispatch, demand, weather and storage updates (advance game time); display interpolate between snapshots.
- Switch/fault events are simulated immediately in game time; don't try to compute a full electromagnetic transient for every wire.
- Backend reference scenarios use engineering solver and cross-check against public substation curves.

## 6. Distant coal and hydro must be handled truthfully

A small town does **not** have a dedicated hydro station, coal boiler, wind turbine and gas plant for every fuel category. It imports a time-varying combination of energy through the **NSW grid**, where coal, hydro, solar, wind, gas, storage and interconnectors contribute under constraints. The simulation should show upstream NEM generation mix, prices and wholesale availability **separately** from local physical generation. Public AEMO five-minute dispatch and individual unit generation/SCADA files can provide real reference patterns.

## 7. Visual, playability and acceptance

Render street poles and spans in physically plausible alignments, transformers on appropriate poles/pads, HV/MV/LV distinct, junctions at roads, connections to roofs and at least some rooftop solar + metering. Add separate toggle layers for **transmission, regional distribution, local distribution, transformers, phases, building demand, generated power, solar, batteries, line loading, voltage, faults, outage zones, restoration crews and time-series replay**.

Acceptance scenario: sever a documented *synthetic model edge*; only downstream electrically dependent structures lose lights/power, affected smart streetlights turn off at night, and critical loads fail or transfer only if protected generators exist. If an isolated generator runs at its limit, shed lower-priority blocks; rooftop PV must not magically restore an unsafe dead grid; BESS dies at the correct MWh depletion and recharges respecting kW/efficiency constraints.

## 8. Uncertainty / limitations to resolve

- No published street-level Menindee pole/transformer-to-customer register verified; generate synthetic alignments from town street positions and real rural construction conventions.
- Regional diagram is a schematic; exact asset GIS geometry, switch configuration and phase connectivity *not* established.
- DAPR nameplate MVA figures are not turbine electrical MW at incident temperatures/fuel limitations.
- Regulatory consent for 50/100 MWh BESS is *not* proof that 100 MWh was installed; verified operating 50/50 is stronger evidence.
- AEMO NEM dispatch does not trace specific electrons from a coal/hydro plant to each building.
- Equipment-specific modern standards, current manufacturers and exact 2026 retail cost data require follow-up verified datasheets.
- This first pass has **not** imported the half-hourly Essential Energy datasets or calibrated load against them.
- No real-world security-sensitive substation control information is needed for the playable design.

See [SOURCES.md](./SOURCES.md), [OPEN_SOURCE_SIMULATION_AUDIT.md](./OPEN_SOURCE_SIMULATION_AUDIT.md), and [TASKS.md](./TASKS.md).
