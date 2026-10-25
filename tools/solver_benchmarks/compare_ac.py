#!/usr/bin/env python3
"""NSW-ELEC-004: cross-engine *actual* AC loadflow sanity fixture.

Stand-alone 2-bus 11kV synthetic one-line example. This IS NOT Menindee.
Required dependencies: pandapower, PyPSA, numpy. Never copy a regulated feeder.
"""
import json
import math
import platform
from pathlib import Path

def compare():
    import pandapower as pp
    import pypsa

    rated_kv = 11.0
    r_ohm, x_ohm = 0.32, 0.08
    p_mw, q_mvar = 0.20, 0.06

    # Same public/synthetic single-phase-balanced AC equivalent in each engine.
    ppnet = pp.create_empty_network()
    src = pp.create_bus(ppnet, vn_kv=rated_kv, name="source")
    consumer = pp.create_bus(ppnet, vn_kv=rated_kv, name="consumer")
    pp.create_ext_grid(ppnet, bus=src, vm_pu=1.0)
    pp.create_line_from_parameters(ppnet, from_bus=src, to_bus=consumer,
                                   length_km=1, r_ohm_per_km=r_ohm,
                                   x_ohm_per_km=x_ohm, c_nf_per_km=0,
                                   max_i_ka=0.2)
    pp.create_load(ppnet, bus=consumer, p_mw=p_mw, q_mvar=q_mvar)
    pp.runpp(ppnet, algorithm="nr", numba=False)
    assert ppnet.converged, "pandapower NR nonconvergent"
    pp_vm = float(ppnet.res_bus.vm_pu.loc[consumer])
    pp_losses = float(ppnet.res_line.pl_mw.iloc[0])

    psnet = pypsa.Network()
    psnet.add("Bus", "source", v_nom=rated_kv)
    psnet.add("Bus", "consumer", v_nom=rated_kv)
    psnet.add("Line", "line", bus0="source", bus1="consumer",
              r=r_ohm, x=x_ohm, s_nom=5.0)
    psnet.add("Generator", "slack", bus="source", p_nom=5.0, control="Slack")
    psnet.add("Load", "house", bus="consumer", p_set=p_mw, q_set=q_mvar)
    info=psnet.pf()
    if isinstance(info, dict) and "converged" in info:
        status = info["converged"]
        assert bool(status.all().all()), "PyPSA nonconvergent"
    ps_vm=float(psnet.buses_t.v_mag_pu["consumer"].iloc[0])
    ps_losses=float(psnet.lines_t.p0["line"].iloc[0] + psnet.lines_t.p1["line"].iloc[0])

    assert math.isfinite(pp_vm) and math.isfinite(ps_vm)
    assert 0.90 < pp_vm < 1.05 and 0.90 < ps_vm < 1.05
    assert pp_losses >= 0 and ps_losses >= 0
    assert abs(pp_vm - ps_vm) < 0.01, f"engine disagreement >1% pu: {pp_vm} vs {ps_vm}"
    assert abs(pp_losses - ps_losses) < 0.002, f"line MW loss difference >2kW: {pp_losses} vs {ps_losses}"
    return {
      "task":"NSW-ELEC-004", "status":"passed",
      "source":"self-contained synthetic 2-bus single-line AC loadflow; NOT real NSW geometry",
      "parameter": {"kv":rated_kv,"line_km":1,
                    "line_r_ohm_per_km":r_ohm,"line_x_ohm_per_km":x_ohm,
                    "load_mw":p_mw,"load_mvar":q_mvar},
      "engines":{"pandapower": pp.__version__,"pypsa":pypsa.__version__},
      "python_version":platform.python_version(),
      "results":{"pandapower":{"load_voltage_pu":pp_vm,"line_losses_mw":pp_losses},
                 "pypsa":{"load_voltage_pu":ps_vm,"line_losses_mw":ps_losses}},
      "absolute_vm_pu_delta":abs(pp_vm-ps_vm),
      "absolute_line_loss_mw_delta":abs(pp_losses-ps_losses),
      "acceptance":{"vm_pu_delta_lt":0.01, "loss_mw_delta_lt":0.002}
    }

if __name__ == "__main__":
    result=compare()
    path=Path("data/solver_benchmarks/002bus_11kv_result.json")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2,sort_keys=True))
