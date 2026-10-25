# Open-source electricity simulation code audit

**Date:** 2026-10-25  
**Scope:** Examine **actual public source-code files**, compare playable-game mechanics against engineering simulators, and identify realistic reusable designs. Do **not** mistake an electricity game mechanic for a validated physical power-flow model.

## A. Actual games — inspected code

### 1. Micropolis / original open-source SimCity (GPLv3 and additional terms)

- Repo: https://github.com/osgcc/simcity
- **Actual electricity source:** https://github.com/osgcc/simcity/blob/master/src/sim/s_power.c
- **Scheduling/scan:** https://github.com/osgcc/simcity/blob/master/src/sim/s_sim.c (`DoPowerScan()`)
- Observed: tile/neighbour power scan propagates source electricity across connected conductive map tiles. The simulation maintains a power-status map and updates it periodically.
- Useful: very efficient **connected/not-connected** world overlay, grid damage affecting downstream tiles, historic city-builder gameplay readability.
- Insufficient: no evidence this module numerically solves AC loadflow, 3-phase voltage drop, transformer saturation or inverter grid-forming stability. Need entirely new network physics if seeking NSW realism.
- Reuse: study algorithms; copyright and original GPL/additional terms matter before copying code.

### 2. Simutrans (open-source transport game, Artistic License notice in inspected source)

- Repo: https://github.com/simutrans/simutrans
- **Actual supply/demand network source:** https://github.com/simutrans/simutrans/blob/master/src/simutrans/dataobj/powernet.cc
- **Actual line/substation source:** https://github.com/simutrans/simutrans/blob/master/src/simutrans/obj/leitung2.cc
- Observed: `powernet_t::step_all(delta_t)` iterates electrically connected subnets; `step()` computes normalized supply and demand; networks aggregate production/consumption with fixed-point fractional precision (16). `leitung2.cc` implements spatial power-line connectivity and transformer hookups to industries.
- Useful: players can *see* a network, link substations and industries; distinct electrical islands emerge; incremental network editing, simple capacity planning, efficient topology updates.
- Insufficient: aggregate subnet supply balance alone does not prove voltage, phase, congestion or conductor heating; add branch-aware flows/impedances.

### 3. Mindustry (GPLv3)

- Repo: https://github.com/Anuken/Mindustry
- **Actual source inspected:** https://github.com/Anuken/Mindustry/blob/master/core/src/mindustry/world/blocks/power/PowerGraph.java
- **Actual power-block definitions:** https://github.com/Anuken/Mindustry/blob/master/core/src/mindustry/content/Blocks.java
- Observed: each `PowerGraph` holds `producers`, `consumers`, `batteries`, `all`; `update()` aggregates production/need, charges excess into batteries, discharges deficit, then `distributePower()` determines fraction of load satisfied. Graphs merge/split as structures connect/disconnect.
- Useful: responsive gameplay, real-time visible power overlays, accurate notion of *energy storage as capacity over time* (relative to arbitrary game units), robust graph invalidation and island recomputation.
- Insufficient: each network shares a common satisfaction fraction; no inherent distance-aware line drop, AC reactive power or phase-specific overload. NSW utility simulation must extend graph mechanics significantly.

### 4. The Powder Toy (GPLv3)

- Repo: https://github.com/The-Powder-Toy/The-Powder-Toy
- Verified repository and C++ source exists; electricity in a local particle sandbox is useful mainly for **visible local electrical response** and fault visual effects. A street-scale 50 Hz three-phase grid is not the same model.
- Follow-up: inspect exact SPARK/metal conductor files and time-step behaviour before adopting any mechanism.

### 5. OpenTTD (GPLv2)

- Repo: https://github.com/OpenTTD/OpenTTD
- Verified transport-game source, construction/tools and industry systems exist. The game focuses on **transport**, not realistic distribution-grid electrical flow. Use as a reference for infrastructure overlays, building menus, path readability and persistent worlds; **do not claim it has a detailed power-grid engine**.

### 6. Cytopia and Citybound (status: mechanism not verified)

- Citybound: https://github.com/citybound/citybound — open-source city simulator; architecture can inform large-scale deterministic agent systems, but a working electrical engine has **not** been source-verified in this pass.
- Cytopia: confirm exact official repository and power feature implementation before citing it as functional. Do not fabricate a relevant engine solely because its description mentions utilities.

## B. Scientific engines — source and documented capabilities

| Engine | Public code | Best use | Limitations / deployment decision |
|---|---|---|---|
| **OpenDSS / DSS-Extensions** | https://github.com/dss-extensions/dss_capi | Multi-phase distribution circuit analysis, PV, battery, feeder voltages, annual quasi-static time series | Strong candidate for **reference/calibration runner**, not direct 60 FPS browser loop |
| **GridLAB-D** | https://github.com/gridlab-d/gridlab-d | Smart-grid distribution plus residential end-use and weather behaviours; feeder case studies | Detailed models/environment add integration weight |
| **pandapower** | https://github.com/e2nIEE/pandapower | Transparent bus/line/transformer/switch power flow, time series, automated tests and validation | Default common powerflow often balanced; verify asymmetrical model support for explicit per-phase requirements |
| **PyPSA** | https://github.com/PyPSA/PyPSA | NSW/NEM-level generation mix, economic dispatch, storage constraints, hydro, variable renewables, contingency and bulk powerflow | Not a substitute for detailed LV household phase simulation |
| **MATPOWER** | https://github.com/MATPOWER/matpower | Reproducible OPF, IEEE cases and comparison on bulk/balanced networks | MATLAB/Octave integration; research/validation use |
| **OpenModelica** | https://github.com/OpenModelica/OpenModelica | Research-level control/dynamic simulation for special generators | Too heavy for main browser game simulation |
| **pandapipes** | https://github.com/e2nIEE/pandapipes | Later gas, water and pipe pressure networks, sibling architecture to pandapower | Distinct domain, not electricity solver |

**Evidence:** PyPSA official repo documents generator dispatch, linear/AC powerflow, hydro and storage. EPRI OpenDSS documentation explicitly documents multi-phase circuits, snapshot/daily/yearly runs and PV integration. pandapower documentation shows buses, external grid, transformers, lines and numeric results.

## C. Recommended hybrid for Repository Town

1. **Playable runtime** (TypeScript or engine-native equivalent): network component IDs + geographic adjacency + connection graph + cached feeder trees. Fast graph splits/merges inspired by Mindustry/Simutrans **concepts**, not copied code.
2. **Energy timestep** (5 game minutes): collect realistic loads and weather; calculate local PV; enforce storage kW/kWh/efficiency, available import and backfeed constraints; calculate approximate radial branch flows/losses and low voltage.
3. **Protection timestep** (event-driven): transient gameplay events update breakers, fuses, grid availability, failures and restoration eligibility; no fictitious AC waveform solver running every rendered frame.
4. **Offline reference model** (Python/OpenDSS/pandapower, optional PyPSA): generate reference feeder scenarios with phase imbalance, voltage limits and sensitivity checks; use these to measure surrogate-runtime accuracy.
5. **Presentation**: physically placed power poles, underground segments, service wires, transformers, substation and PV/BESS meshes; toggleable per-element diagnostic overlays; lights and NPC world react to losses.
6. **Story/gameplay**: repair crew/priority workflow, controls at safe *abstract level*, blackout consequences, difficult resource trade-offs and weather/time-of-day dynamics. No disclosure of real switch operating instructions.

## D. What not to do

- Do not flood-fill a building's `powered=true` without checking supply, transformer, upstream branch and protected island.
- Do not model 50 MW battery as 50 MWh of instantaneous **power** or 50 MW for indefinite duration.
- Do not show a wind/coal/hydro station physically in Menindee merely to explain the state-wide fuel mix.
- Do not blindly copy GPLv2/GPLv3 code into a different-license Repository Town distribution. Reimplement ideas cleanly, and document licensing.
- Do not run a detailed loadflow for each render frame; cache static topology and solve at sensible simulated time/event boundaries.

## E. Follow-up code-review checkboxes

- [x] Inspect concrete Micropolis `s_power.c` and periodic scan call.
- [x] Inspect concrete Simutrans `powernet.cc` and `leitung2.cc`.
- [x] Inspect concrete Mindustry `PowerGraph.java`.
- [x] Identify relevant engineering engine repositories and documented features.
- [ ] Run isolated benchmarks of sample networks in OpenDSS and pandapower.
- [ ] Measure game performance vs feeder count and street-pole count.
- [ ] Verify exact current licences of **all** packages, including transitive licensing, before using dependency source.
- [ ] Confirm whether Cytopia or Citybound actually implements electricity; do not rank as a working reference without source evidence.
