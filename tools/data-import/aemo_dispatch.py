#!/usr/bin/env python3
"""NSW-ELEC-007: reproducible AEMO five-minute DISPATCHIS + DISPATCHSCADA loader.

Uses only Python stdlib. Dates in NEM files are fixed UTC+10 (NEM/AEST), *not*
Australia/Sydney local DST time. The output does not attribute NEM generator
fuel types, or individual generator electricity, to NSW households.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import math
import statistics
import tempfile
import urllib.request
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

NEM_TZ = timezone(timedelta(hours=10))
SRC_BASE = "https://nemweb.com.au/Reports/ARCHIVE"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"


def read_zip_csv_records(zip_path):
    """Yield (source member, table name, row dictionary) from nested AEMO ZIPs."""
    with zipfile.ZipFile(zip_path) as outer:
        outer_members = sorted(x for x in outer.namelist() if x.upper().endswith((".ZIP", ".CSV")))
        if not outer_members:
            raise ValueError("archive has no ZIP/CSV members")
        for outer_name in outer_members:
            buf = outer.read(outer_name)
            if outer_name.upper().endswith(".ZIP"):
                with zipfile.ZipFile(io.BytesIO(buf)) as inner:
                    inner_names = [n for n in inner.namelist() if n.upper().endswith(".CSV")]
                    if not inner_names:
                        raise ValueError("nested archive missing CSV: " + outer_name)
                    for name in inner_names:
                        yield from decode_records(inner.read(name), outer_name + "/" + name)
            else:
                yield from decode_records(buf, outer_name)


def decode_records(data, source):
    schema = {}
    text = io.TextIOWrapper(io.BytesIO(data), encoding="utf-8-sig", errors="strict", newline="")
    for values in csv.reader(text):
        if len(values) < 4:
            continue
        kind, group, table, version = values[:4]
        key = (group, table, version)
        if kind == "I":
            schema[key] = [v.strip().upper() for v in values[4:]]
        elif kind == "D":
            header = schema.get(key)
            if header is None:
                raise ValueError(f"missing I schema for {key} in {source}")
            if len(values[4:]) != len(header):
                raise ValueError(f"row/header width mismatch for {key} in {source}")
            yield source, table.upper(), dict(zip(header, values[4:]))


def parse_nem_time(value):
    # Australian NEM market files use fixed UTC+10, even during NSW daylight savings.
    return datetime.strptime(value.strip(), DATE_FORMAT).replace(tzinfo=NEM_TZ)


def to_num(value, label):
    try:
        n = float(value)
        if not math.isfinite(n):
            raise ValueError("nonfinite")
        return n
    except (ValueError, TypeError) as exc:
        raise ValueError(f"non-numeric {label}: {value!r}") from exc


def inspect(scada_zip, dispatch_zip, day, strict=True):
    date = datetime.strptime(day, "%Y-%m-%d").date()
    records = {}
    scada = {}
    source_summary = {"duid_mwh": collections.defaultdict(float),
                      "duids_seen": set(), "scada_rows": 0,
                      "duplicate_duid_times": 0, "dispatch_region_rows": 0}
    seen_duid_times = set()
    seen_dispatch_times = set()
    duplicates = 0
    for _, table, row in read_zip_csv_records(scada_zip):
        if table != "UNIT_SCADA":
            continue
        instant = parse_nem_time(row["SETTLEMENTDATE"])
        if instant.date() != date:
            continue
        duid = row["DUID"].strip().upper()
        if not duid:
            continue
        pair = (instant, duid)
        if pair in seen_duid_times:
            source_summary["duplicate_duid_times"] += 1
            continue
        seen_duid_times.add(pair)
        mw = to_num(row["SCADAVALUE"], "SCADAVALUE")
        slot = scada.setdefault(instant, {"positive_scada_mw": 0.0, "negative_scada_mw": 0.0,
                                           "scada_unit_count": 0})
        slot["positive_scada_mw"] += max(mw, 0.0)
        slot["negative_scada_mw"] += min(mw, 0.0)
        slot["scada_unit_count"] += 1
        source_summary["duids_seen"].add(duid)
        source_summary["duid_mwh"][duid] += mw / 12  # five-minute *approximate* MWh
        source_summary["scada_rows"] += 1
    for _, table, row in read_zip_csv_records(dispatch_zip):
        if table != "REGIONSUM" or row.get("REGIONID", "").strip().upper() != "NSW1":
            continue
        instant = parse_nem_time(row["SETTLEMENTDATE"])
        if instant.date() != date:
            continue
        if instant in seen_dispatch_times:
            duplicates += 1
            continue
        seen_dispatch_times.add(instant)
        source_summary["dispatch_region_rows"] += 1
        records[instant] = {
            "nsw_total_demand_mw": to_num(row.get("TOTALDEMAND"), "TOTALDEMAND"),
            "nsw_spot_price_aud_per_mwh": to_num(row.get("RRP"), "RRP"),
        }
    expected = [datetime.combine(date, datetime.min.time(), tzinfo=NEM_TZ) + timedelta(minutes=5*i)
                for i in range(1, 289)]
    # 00:00 settlement instant marks the *preceding* 5-minute interval in daily archives;
    # compare only calendar-day settlement timestamps and record 00:00 as the first sample.
    expected = [datetime.combine(date, datetime.min.time(), tzinfo=NEM_TZ)
                + timedelta(minutes=5*i) for i in range(288)]
    missing_dispatch = [t.isoformat() for t in expected if t not in records]
    missing_scada = [t.isoformat() for t in expected if t not in scada]
    combined = []
    for t in sorted(set(records) | set(scada)):
        d = records.get(t, {})
        s = scada.get(t, {})
        combined.append({
            "nem_aest": t.strftime("%Y-%m-%dT%H:%M:%S+10:00"),
            "utc": t.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            **d, **s
        })
    report = {
        "task": "NSW-ELEC-007",
        "date_nem_aest": day,
        "source": "AEMO NEMWeb public archives, fixed market time UTC+10",
        "source_file_dispatch_sha256": hashlib.sha256(Path(dispatch_zip).read_bytes()).hexdigest(),
        "source_file_scada_sha256": hashlib.sha256(Path(scada_zip).read_bytes()).hexdigest(),
        "caveat": "SCADA spans entire NEM; summed positive SCADA is not NSW generation or NSW fuel mix. Five-minute SCADA MW integrated as MWh is approximate; source-to-house attribution is invalid.",
        "dispatch_nsw_intervals": len(records),
        "scada_nem_intervals": len(scada),
        "missing_nsw_intervals": missing_dispatch,
        "missing_scada_intervals": missing_scada,
        "duplicate_nsw_intervals": duplicates,
        "duplicate_duid_intervals": source_summary["duplicate_duid_times"],
        "unique_scada_duids": len(source_summary["duids_seen"]),
        "scada_unit_rows": source_summary["scada_rows"],
        "time_basis": "AEST UTC+10 no DST, NEM dispatch settlement timestamp",
        "fuel_mix_status": "NOT CLASSIFIED: official DUID-to-region-and-fuel register not yet integrated",
        "top_duids_by_approx_mwh_nem": [
            {"duid": k, "approx_mwh": round(v, 3)}
            for k, v in sorted(source_summary["duid_mwh"].items(),
                              key=lambda x: -abs(x[1]))[:12]
        ]
    }
    if records:
        demand = [r["nsw_total_demand_mw"] for r in records.values()]
        price = [r["nsw_spot_price_aud_per_mwh"] for r in records.values()]
        report["nsw_demand_mw_stats"] = {
            "min": round(min(demand), 3), "mean": round(statistics.mean(demand), 3),
            "max": round(max(demand), 3)
        }
        report["nsw_price_aud_per_mwh_stats"] = {
            "min": round(min(price), 3), "mean": round(statistics.mean(price), 3),
            "max": round(max(price), 3)
        }
    report["valid_complete_day"] = (not missing_dispatch and not missing_scada
                                     and not duplicates and not source_summary["duplicate_duid_times"])
    if strict and not report["valid_complete_day"]:
        raise ValueError("invalid or incomplete day: " + json.dumps({
            k: (len(v) if isinstance(v, list) else v) for k,v in report.items()
            if k.startswith("missing") or k.startswith("duplicate")
        }))
    return combined, report


def download(url, path):
    request = urllib.request.Request(url, headers={"User-Agent": "NSWutilities-source-audit/1.0"})
    with urllib.request.urlopen(request, timeout=120) as response:
        with open(path, "wb") as dest:
            import shutil
            shutil.copyfileobj(response, dest)
    if not zipfile.is_zipfile(path):
        raise ValueError(f"response for {url} is not a ZIP")


def write_outputs(rows, report, dest):
    dest.mkdir(parents=True, exist_ok=True)
    fields = ["nem_aest", "utc", "nsw_total_demand_mw", "nsw_spot_price_aud_per_mwh",
              "positive_scada_mw", "negative_scada_mw", "scada_unit_count"]
    with (dest / "nsw_nem_dispatch_5m.csv").open("w", newline="", encoding="utf-8") as fh:
        out = csv.DictWriter(fh, fieldnames=fields)
        out.writeheader()
        out.writerows(rows)
    (dest / "quality_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return dest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", default="2026-10-20")
    parser.add_argument("--scada-zip", type=Path)
    parser.add_argument("--dispatch-zip", type=Path)
    parser.add_argument("--out", type=Path, default=Path("out/aemo"))
    parser.add_argument("--allow-incomplete", action="store_true")
    args = parser.parse_args()
    if bool(args.scada_zip) != bool(args.dispatch_zip):
        parser.error("provide both --scada-zip and --dispatch-zip, or neither")
    with tempfile.TemporaryDirectory() as temp:
        scada_zip = args.scada_zip or Path(temp) / "scada.zip"
        dispatch_zip = args.dispatch_zip or Path(temp) / "dispatch.zip"
        if not args.scada_zip:
            ds = args.day.replace("-", "")
            download(f"{SRC_BASE}/Dispatch_SCADA/PUBLIC_DISPATCHSCADA_{ds}.zip", scada_zip)
            download(f"{SRC_BASE}/DispatchIS_Reports/PUBLIC_DISPATCHIS_{ds}.zip", dispatch_zip)
        rows, report = inspect(scada_zip, dispatch_zip, args.day,
                               strict=not args.allow_incomplete)
        write_outputs(rows, report, args.out)
        print(json.dumps({k: v for k, v in report.items()
                          if k.endswith("_intervals") and not isinstance(v, list)},
                         sort_keys=True))
        print("OUTPUT", args.out)
        print("FUEL_MIX", report["fuel_mix_status"])


if __name__ == "__main__":
    main()
