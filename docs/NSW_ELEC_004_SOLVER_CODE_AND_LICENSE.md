# NSW-ELEC-004 — Code-level audit of three playable grids and three physics engines

**Verified:** 25 October 2026. Actual repository source and licence files inspected using GitHub, with file-level source links. **No third-party source code was copied into NSWutilities or Repository Town.** A separate [two-solver AC reference fixture](../tools/solver_benchmarks/compare_ac.py) exercises real installed engineering libraries in GitHub Actions; the game binaries themselves and GridLAB-D C++ have **not** been compiled here.

## Three actual open-source *games*, code inspected

| Game / licence | Real source examined | Electrical representation | Suitable reuse and limitations |
|---|---|---|---|
| [Micropolis GPLv3 + EA trademark notices](https://github.com/micropolis/MicropolisCore/blob/main/MicropolisEngine/src/power.cpp) — [licence](https://github.com/micropolis/MicropolisCore/blob/main/LICENSE) | `MicropolisEngine/src/power.cpp` (Git blob SHA `18db0acb33c45cf581dbc398299791f199a6cc35`) | Connected/powered tile propagation, supply capacity and light/dark city behaviour. It is **not** AC power flow or per-phase voltage. | Use as *conceptual* inspiration for cheap topology/island reachability only. GPLv3 and extra trademark conditions mean **do not paste** this code into a differently licensed town game without legal review. |
| [Simutrans Artistic Licence](https://github.com/simutrans/simutrans/blob/master/LICENSE.txt) | [`src/simutrans/dataobj/powernet.cc`](https://github.com/simutrans/simutrans/blob/master/src/simutrans/dataobj/powernet.cc) (SHA `5d427bb2ae8977d30df96de1fa05445e1528a690`) | A power network maintains supply/demand and normalises power availability for buildings, separate from actual reactive power and voltage. | Useful town-wide production/demand economy layer, **not** validating transformers, voltage drop or protection. Artistic licence has modification obligations; independent implementation preferred. |
| [Mindustry GPLv3](https://github.com/Anuken/Mindustry/blob/master/LICENSE) | [`core/src/mindustry/world/blocks/power/PowerGraph.java`](https://github.com/Anuken/Mindustry/blob/master/core/src/mindustry/world/blocks/power/PowerGraph.java) (SHA `f37fa08a66c09dce478a3141ea7b10c6294617ff`) | Producers, consumers, batteries in dynamically changing graphs; charge/discharge and balance managed per game tick. | Best game-side *architecture* for blackout islands, balancing and storage **concepts**; no actual three-phase AC physical solver. GPL source cannot simply be embedded without respecting licence terms. |

**Do not claim these games simulate electricity accurately:** all three are gameplay approximations. Micropolis may model tile connection with capacity but not Kirchhoff/line impedance. Simutrans has normalised production/demand but no meaningful per-conductor electrical current. Mindustry power network tick models supply and storage, not NSW distribution phasing/protection.

## Three actual *engineering* engines, code and licensing inspected

| Engine/licence evidence | Actual solver source and tests | What it solves | Repository Town use |
|---|---|---|---|
| [pandapower](https://github.com/e2nIEE/pandapower/blob/develop/LICENSE) **BSD 3-Clause** | [`pandapower/powerflow.py`](https://github.com/e2nIEE/pandapower/blob/develop/pandapower/powerflow.py) SHA `aa3c22eb9d36171e64ed20c5b64017560935b10a` dispatches NR and BFS; [`pandapower/pf/run_bfswpf.py`](https://github.com/e2nIEE/pandapower/blob/develop/pandapower/pf/run_bfswpf.py) SHA `ab1dbc186c5f9901872bf565faa708cfcaeba447` constructs bus-injection → branch-current and branch-current → voltage relationships | AC nonlinear Newton–Raphson and distribution-focused backward-forward sweep; line and transformer ratings, voltage, losses | **Recommended primary off-line numerical truth** for a radial, low-voltage synthetic feeder; benchmark simplified TS physics against outputs (separate phase model validation required). |
| [PyPSA](https://github.com/PyPSA/PyPSA/blob/master/LICENSE) **MIT** | [`pypsa/network/power_flow.py`](https://github.com/PyPSA/PyPSA/blob/master/pypsa/network/power_flow.py) SHA `999c401a0e56d2679323ef792e8bfca844e778d8`; [cross-test against pandapower](https://github.com/PyPSA/PyPSA/blob/master/test/test_pf_against_pandapower.py) SHA `b29f6c9a14ad270f346b25de82cede692f19bc3c` | AC loadflow plus linear optimisation, generator availability, storage and dispatch over hours | **Recommended wholesale/regional dispatch reference** and independent AC voltage benchmark; do not substitute a DC/linear dispatch solution for full distribution voltage calculations. |
| [GridLAB-D](https://github.com/gridlab-d/gridlab-d/blob/master/LICENSE) **Battelle GridLAB-D License v5.3 (Oct 2024)** | [`powerflow/solver_nr.cpp`](https://github.com/gridlab-d/gridlab-d/blob/master/powerflow/solver_nr.cpp) SHA `2a942d5fe6c561b78d24c0215bd72df3c8f9d36b`; [`powerflow/transformer.cpp`](https://github.com/gridlab-d/gridlab-d/blob/master/powerflow/transformer.cpp) SHA `aa990dc478637203db7ea26ce8725bcf6db0cb10`; [test network](https://github.com/gridlab-d/gridlab-d/blob/master/powerflow/autotest/test_powerflow_NR_network.glm) | Rich distribution phasing and transformer delta/wye/split-centre-tapped modelling, dynamic loads and time-stepping | **Recommended next-phase unbalanced three-phase/phase-loss reference**. Check module-level licences/dependencies as needed: repository labels may mention LGPL, while the inspected root legal text says **Battelle**. We did **not** compile it. |

### Reuse/compatibility rule

- There is **no automatic permission** to copy GPLv3 game code into a differently licensed project merely because its GitHub repo is public. Copy mechanics as ideas, implement original code, retain attribution where appropriate, and get legal review before direct reuse.
- pandapower BSD, PyPSA MIT and GridLAB-D root Battelle notices permit broad reuse subject to actual copyright/notice obligations. **Submodules, compiled dependencies and graphics may have different licences**; do not assume entire game bundles are compatible from a top-level badge.
- Don’t bundle a 100+MB solver directly into the 3D browser game. Use these engines **offline in CI** to create **source-controlled numeric truth fixtures** for a fast TypeScript runtime.

## Runnable controlled comparison

The new [reference script](../tools/solver_benchmarks/compare_ac.py) builds *one identical synthetic balanced two-bus electrical feeder* in two independently maintained AC engines:

- Source bus **11 kV**, nominal voltage **1.0 pu**.
- One 1 km line with **R=0.32 Ω/km**, **X=0.08 Ω/km**, deliberately zero shunt capacitance for equivalence, 0.2 kA rating in pandapower.
- Consumer load **0.20 MW**, **0.06 MVAr**.
- Run pandapower NR AC solution and PyPSA AC power flow. Check voltage magnitude and line losses are finite, stable and within tolerances **ΔV < 0.01 pu** and **ΔP_loss < 0.002 MW**.
- Both use physically defined line impedance; this is **not** a Menindee real feeder and should never be presented as live operating data.
- GitHub Actions [workflow](../.github/workflows/nsw-elec-004.yml) installs the engines, tests schema provenance and produces `data/solver_benchmarks/002bus_11kv_result.json` as an artifact. Package versions are recorded in the result. **Real CI execution status must be checked before declaring the benchmark passed**.

## Decision and remaining tests

**Architecture decision:** (1) Mindustry-style game-side network topology and battery state semantics, independently rewritten; (2) pandapower distribution truth fixture; (3) PyPSA dispatch/AC cross-check; (4) GridLAB-D unbalanced three-phase and transformer verification in a later task. Bind to the sourced Menindee regional model; the town LV grid remains explicitly synthetic.

- [x] Inspect three real game source files and identify feature/physics limits.
- [x] Inspect source of **three** engineering solvers and their actual root licences, with SHA and concrete file paths.
- [x] Supply an executable benchmark harness and GitHub CI configuration.
- [ ] **CI must actually pass** for the two-solver benchmark; verify run/artifact rather than assume.
- [ ] Compile/run GridLAB-D unbalanced reference case and/or review licence scope of optional modules **before any direct engine integration**.
- [ ] Compare runtime Repository Town AC approximation against engineering truth with tolerance dataset (NSW-ELEC-021); not part of this source-audit completion claim.

**NSW-ELEC-004 *code-audit acceptance* is completed; all-engine execution and runtime parity tests remain separate, explicitly open milestones.**
