# RTSM-001–002 — Stormwater, drainage and flood reference research

**Research status (25 October 2026):** documented foundations and design specification; **not** an exact Dubbo drainage GIS, calibrated hydraulic flood model, digital twin or deployed game feature.

## Decision and sample geography

- **RT-SYS-004 has no formally selected single reference town yet.** Dubbo provides a highly useful public stormwater asset-management *comparison*: Council reports **over 200 km of urban stormwater pipes**, **more than 6,500 pits**, **62 gross pollutant traps** and **over 70 retarding basins** across its local government area. The numbers are Council-described aggregate counts, not a site-by-site placement inventory. Source SW-S01.
- The existing project decision keeps **Menindee** for electricity, **Orange** for water, and **Narromine** for sewerage. Do not override or combine real infrastructures to fabricate one geographic town. Orange's documented stormwater harvesting can be used as a separate cross-utility case (SW-S12), distinguishing stages that were planned from assets already operating.
- A separate candidate matrix comparing Dubbo, Orange and another relevant town by public pit data, overland flood mapping, updated maintenance plans, geometry licences and identifiable inlet/outfall detail must precede formal stormwater town selection (RTSM-004).

## Source-to-outfall physical chain

Rainfall (observed or deliberately simulated) -> roof/gutter/downpipe and paved/permeable lots -> depression storage/infiltration/evapotranspiration, rainwater tanks and retained on-site runoff -> flow across yards/streets -> kerb/gutter/road side entry pits/catch pits -> underground drainage pipes/culverts and open swales/channels -> gross pollutant trap/pond/bioretention basin/wetland where actually specified -> controlled outfall to watercourse/floodplain. Separately, heavy overland water flows via the **major drainage path** even when pits cannot take all runoff. A creek or river may be receiving water and may flood independently of this local drainage network.

**Not sewerage:** sanitary toilet drainage/inspected sewer laterals have a separate network and ledger. Rainfall-driven infiltration/inflow into sewerage occurs only through an explicit fault/defect mechanism. Do not connect gutters or storm inlets directly into toilets or potable lines. Approved stormwater harvesting is a *separate treatment/storage/permission* boundary and must not become potable merely by changing a flag.

## Rainfall, runoff, storm event classes

Use observed rain gauges for historical events and a separately identified synthetic profile for game weather. **BoM design IFD rainfall** is a statistical estimate for a location, duration and annual exceedance probability; it is **not** actual observed precipitation or the chance of an individual house flood. Full Australian Rainfall and Runoff methodology includes losses, temporal patterns, areal adjustment and other inputs, not simply one raw IFD intensity (SW-S02/S03/S04/S14).

At each synthetic catchment c over timestep t:
- Rain-on-catchment L = rainfall-depth mm × area m² (because 1 mm over 1 m² = 1 L).
- Partition into intercepted/depression storage, infiltration, evaporation, roof tank capture, surface runoff, and explicit remaining storage; **do not apply a runoff coefficient again after losses have already been removed**.
- Impervious roof/road/soil/parks each have different permeability, roughness and detention; antecedent wetness matters for later events. Urban lots aren't automatically 100% impervious.
- Convey runoff with capacity and storage limits; pit bypass remains on the surface major route, not deleted.
- Riverine backwater (high creek/river level at outfall) and local intense downpour (flash/overland flooding) are separate mechanisms. Floodplain study layers may be outdated or have different datum and AEP.

## Realistic asset/maintenance behaviour

- Pipes/pits/manholes/headwalls: geometry and cover levels are different from invert/slope elevations. Clogged gratings, sediment, roots and crushed pipe can reduce capacity; cleaning creates a logged sediment/litter destination rather than deleting materials invisibly.
- Gross pollutant traps separate some trash/debris, not all contaminants or all stormwater volume; cleanout is limited by crew access and finite maintenance budget.
- Retarding basins temporarily store and meter water release; retention/rain gardens/bioretention, infiltration systems and constructed wetlands have **distinct** operating rules, not universal 100% flood protection.
- Roof-water tanks have finite storage and separate nominated permitted household reuse. A tank overflowing back into a drain must not create or destroy water.
- Exposed street junctions, footpaths, schools, clinic, station/crossings and vulnerable building floor thresholds should have individual asset effects when water accumulates.
- Where a drainage pump does exist, power outage must stop it unless documented backup; gravity-only pipes and swales still flow in darkness.

## Engineering and modelling boundary

**Fast game approximation:** topology, catchment volume balance, storage, finite pit/pipe capacities, deterministic runoff and overland ponding proxy. This gives an understandable game without claiming certified flood depth/velocity. **Reference engineering:** use a pinned EPA SWMM version with synthetic pipe/subcatchment input, compare runoff hydrographs, storage, surcharge and outfalls offline. A 2D overland flood solver and appropriate coupling would be required for detailed depths/velocities across terrain. The game's simpler topological model is not an equivalent of SWMM or a basis for building design, flood evacuation or council asset decisions.

**SWMM source audit:** the EPA solver is written in C; official source at SW-S06, documentation at SW-S05. It supports rainfall-runoff, storage, infiltration, low-impact development, network flows, kinematic/dynamic-wave routing, surface ponding and water quality. This is a *source-capability* review; no SWMM model was executed in this research publication. Assess the exact release, licence and benchmark reproducibility in RTSM-015.

## Data and licensing checklist

For measured town assets: source authority, component ID, geom/datum/CRS, size/grade, node connectivity, condition, asset owner, source year, update date, flood studies, access/redistribution licence and confidentiality. Unknowns stay **unknown** or synthetic. The 234 building/site entries in RTU-001 and NSW-WAT registry are **potential roofs and sites**, not a count of roof downpipes, flood drains or lawful connections.

For observed/design rainfall: date/time, station or site latitude/longitude, observation interval, mm versus mm/h, AEP/ARI distinction, local timezone/DST, missing/flagged samples and precision. For flood layers: study year, scenarios, grid resolution, hydraulic model assumptions, vertical datum, planning status and reuse rights.

## Safety and interface discipline

The NSW Government says local councils investigate, plan and manage local flood risks (SW-S07/S08) and NSW SES publishes public flood guidance (SW-S11). Never present a game flood overlay as a live warning or instructions for real floodwater entry/crossings. Stormwater flood symptoms in Repository Town may be realistic, but remain **fictional and training-only**. In the game, users should not be encouraged to enter drains or floodwater. Actual weather alerts come from official services, not from the game solver.

See [task queue](STORMWATER_TASKS.md), [architecture](STORMWATER_ARCHITECTURE.md), [sources](STORMWATER_SOURCES.md), and [cross-system roadmap audit](UTILITY_ROADMAP_AUDIT_2026-10-25.md).
