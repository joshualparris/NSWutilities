# Water/wastewater open-source solver comparison (NSW-WAT-004)

**Date:** 25 October 2026. This is a *capability/source-location audit* based on official project repositories, **not proof that we ran the solvers, ported code or reproduced their output**. No code copied into NSWutilities.

| Engine | Code and scope | What transfers to Repository Town | Boundary |
|---|---|---|---|
| **EPANET 2.2 / EPA EPANET engine** | https://github.com/USEPA/EPANET2.2 and https://github.com/USEPA/epanet-engine — pressurised potable pipes, pressure-dependent demand, head loss, pumps, valves, tanks, quality/water age, extended-period simulation | Distinguish pressure head, water age, headloss, pump curves and tank limits; benchmark with synthetic .inp network offline | Not a sanitary sewer/treatment-process solver; game graph reachability alone does not solve pressures |
| **WNTR (EPA)** | https://github.com/USEPA/WNTR ; docs https://usepa.github.io/WNTR/ — network resilience, repairs, leaks, pressure-dependent delivery, EPANET compatibility | Outage/vulnerability fixtures and comparison of delivered vs requested water, leak recovery and resilience metrics | Check WNTR/package licence at chosen version; not automatically game-portable |
| **EPA SWMM** | https://github.com/USEPA/Stormwater-Management-Model ; https://www.epa.gov/water-research/storm-water-management-model-swmm — rainfall/runoff, open-channel/drain/pipe conveyance, sanitary/combined networks, pollutant routing | Rainfall runoff, detention and infiltration, sanitary gravity/plausible surcharge, routing and overflow test conditions | Separate from potable pressurised distribution; SWMM is not evidence that all NSW towns use combined sewers |
| **Game UI comparator** | https://www.paradoxinteractive.com/games/cities-skylines-ii/features/electricity-water | Source capacity and connected-building overlays, fault symptoms, service maps | Game documentation is NOT a real engineering textbook |

**No false equivalence:** (1) pressurised water hydraulics solves network pressures/flows; (2) gravity sewer hydraulics/transport solves grades and surcharge; (3) land-surface stormwater adds runoff and flooding; (4) wastewater treatment requires process/quality models beyond SWMM conveyance. No full calibrated solver is included here.

**Licences:** EPA EPANET page describes public-domain software and EPA GitHub archive describes MIT for the archived distribution; EPA engine is described as public domain. Verify *exact tree/version* and any incorporated files before distribution. SWMM EPA source is public-domain per EPA repo. WNTR licence should be checked in its own release file. This repo links code but does not republish it.

**Future reproducibility acceptance:** pin release+SHA, supply tiny synthetic .inp fixture with 3 junctions, reservoir, pump, tank, valve and two demands, run EPANET/WNTR on CI, assert Q, P, tank levels against an engineering-tolerance report; build separate SWMM .inp for one subcatchment and sewer wet well, validate wet-weather overflow. Existing [water core](../src/water/water-core.mjs) is a **non-hydraulic fast surrogate** and deliberately reports no pressure.
