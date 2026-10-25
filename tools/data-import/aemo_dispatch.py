#!/usr/bin/env python3
"""NSW-ELEC-007: reproducible AEMO five-minute DISPATCHIS + DISPATCHSCADA loader.

Uses stdlib for NEMWeb and openpyxl for the official AEMO 2026 DUID-fuel
registry. Dates are fixed UTC+10 (NEM/AEST), not Sydney DST time.
Regional generation groups are *registered generator SCADA*, not rooftop PV
or physically traced energy delivered to NSW homes.
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
REGISTRATION_URL = (
    "https://www.aemo.com.au/-/media/files/electricity/nem/participant_information/"
    "nem-registration-and-exemption-list.xlsx"
    "?rev=ef75714f508b47f69449a056744d924a&sc_lang=en"
)
FUEL_TYPES = ("coal", "gas", "diesel_oil", "hydro", "wind", "solar",
              "battery", "biomass", "other")


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



def fuel_category(primary, descriptor, technology):
    text = " ".join((primary, descriptor, technology)).lower()
    if "battery" in text or "storage" in text:
        return "battery"
    if "solar" in text or "photovoltaic" in text:
        return "solar"
    if "wind" in text:
        return "wind"
    if "coal" in text and "gas" not in text:
        return "coal"
    if "diesel" in text or "fuel oil" in text:
        return "diesel_oil"
    if "gas" in text or "methane" in text:
        return "gas"
    if "hydro" in text or "water" in text:
        return "hydro"
    if "bio" in text or "bagasse" in text:
        return "biomass"
    return "other"


def load_registration(path):
    """Map official 'PU and Scheduled Loads' DUIDs to region and fuel group.

    Do not infer a region or fuel from a DUID spelling. Registration is a
    dated snapshot: cancelled/retired and recently registered units can be
    missing, and unregistered rooftop PV is not in this list.
    """
    import openpyxl
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        sheet = workbook["PU and Scheduled Loads"]
        it = sheet.values
        headers = [str(x).strip().lower() if x is not None else "" for x in next(it)]
        req = ("duid", "region", "fuel source - primary",
               "fuel source - descriptor", "technology type - primary")
        if any(col not in headers for col in req):
            raise ValueError("AEMO registration workbook expected columns missing: " + repr(headers))
        idx = {name: headers.index(name) for name in req}
        registry = {}
        conflicts = set()
        for row in it:
            name = str(row[idx["duid"]] or "").strip().upper()
            region = str(row[idx["region"]] or "").strip().upper()
            if not name or name in ("-", "N/A", "NA") or region not in ("NSW1","QLD1","VIC1","SA1","TAS1"):
                continue
            primary = str(row[idx["fuel source - primary"]] or "").strip()
            descriptor = str(row[idx["fuel source - descriptor"]] or "").strip()
            tech = str(row[idx["technology type - primary"]] or "").strip()
            entry = {"region": region, "fuel": fuel_category(primary,descriptor,tech),
                     "fuel_primary": primary, "fuel_descriptor": descriptor}
            if name in registry and (registry[name]["region"] != entry["region"]
                                     or registry[name]["fuel"] != entry["fuel"]):
                conflicts.add(name)
            else:
                registry[name] = entry
        conflicts.discard("-")
        registry.pop("-", None)
        for name in conflicts:
            registry.pop(name, None)  # ambiguous DUID: better unknown than incorrect
        if len(registry) < 100:
            raise ValueError("suspiciously small generator registry: " + str(len(registry)))
        return registry, sorted(conflicts)
    finally:
        workbook.close()

def inspect(scada_zip, dispatch_zip, day, strict=True, registry=None, registration_sha256=None, registry_conflicts=()):
    registry = registry or {}
    date = datetime.strptime(day, "%Y-%m-%d").date()
    start = datetime.combine(date, datetime.min.time(), tzinfo=NEM_TZ)
    end = start + timedelta(days=1)
    records = {}
    scada = {}
    source_summary = {"duid_mwh": collections.defaultdict(float),
                      "duids_seen": set(), "scada_rows": 0,
                      "duplicate_duid_times": 0, "dispatch_region_rows": 0,
                      "registry_matched_duids": set(), "unmatched_duids": set(),
                      "nsw_fuel_mwh": collections.defaultdict(float),
                      "nsw_storage_charge_mwh": 0.0}
    seen_duid_times = set()
    seen_dispatch_times = set()
    duplicates = 0
    for _, table, row in read_zip_csv_records(scada_zip):
        if table != "UNIT_SCADA":
            continue
        instant = parse_nem_time(row["SETTLEMENTDATE"])
        if not (start < instant <= end):
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
        entry = registry.get(duid)
        if entry:
            source_summary["registry_matched_duids"].add(duid)
            if entry["region"] == "NSW1":
                fuel = entry["fuel"]
                field = "nsw_scada_" + fuel + "_mw"
                slot[field] = slot.get(field, 0.0) + max(mw, 0.0)
                source_summary["nsw_fuel_mwh"][fuel] += max(mw, 0.0) / 12
                if fuel == "battery" and mw < 0:
                    slot["nsw_scada_battery_charging_mw"] = (
                        slot.get("nsw_scada_battery_charging_mw", 0.0) - mw)
                    source_summary["nsw_storage_charge_mwh"] += -mw / 12
        else:
            source_summary["unmatched_duids"].add(duid)
            slot["nem_scada_unmapped_positive_mw"] = (
                slot.get("nem_scada_unmapped_positive_mw", 0.0) + max(mw, 0.0))
        source_summary["duids_seen"].add(duid)
        source_summary["duid_mwh"][duid] += mw / 12  # five-minute *approximate* MWh
        source_summary["scada_rows"] += 1
    seen_price_times = set()
    duplicate_prices = 0
    for _, table, row in read_zip_csv_records(dispatch_zip):
        if table not in ("REGIONSUM", "PRICE") or row.get("REGIONID", "").strip().upper() != "NSW1":
            continue
        instant = parse_nem_time(row["SETTLEMENTDATE"])
        if not (start < instant <= end):
            continue
        if table == "REGIONSUM":
            if instant in seen_dispatch_times:
                duplicates += 1
                continue
            seen_dispatch_times.add(instant)
            source_summary["dispatch_region_rows"] += 1
            records.setdefault(instant, {})["nsw_total_demand_mw"] = to_num(
                row.get("TOTALDEMAND"), "TOTALDEMAND")
        else:
            if instant in seen_price_times:
                duplicate_prices += 1
                continue
            seen_price_times.add(instant)
            records.setdefault(instant, {})["nsw_spot_price_aud_per_mwh"] = to_num(
                row.get("RRP"), "RRP")
    # Dispatch settlement timestamps mark interval END. A trading day contains
    # 00:05 ... 23:55 and 00:00 the next calendar day (288 intervals).
    expected = [start + timedelta(minutes=5*i) for i in range(1, 289)]
    missing_dispatch = [t.isoformat() for t in expected if t not in seen_dispatch_times]
    missing_price = [t.isoformat() for t in expected if t not in seen_price_times]
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
        # Every registered fuel series has an explicit numerical zero when
        # no unit from that fuel produced energy in an interval.
        for fuel in FUEL_TYPES:
            combined[-1].setdefault("nsw_scada_" + fuel + "_mw", 0.0)
        combined[-1].setdefault("nsw_scada_battery_charging_mw", 0.0)
        combined[-1].setdefault("nem_scada_unmapped_positive_mw", 0.0)
    report = {
        "task": "NSW-ELEC-007",
        "date_nem_aest": day,
        "source": "AEMO NEMWeb public archives, fixed market time UTC+10",
        "source_file_dispatch_sha256": hashlib.sha256(Path(dispatch_zip).read_bytes()).hexdigest(),
        "source_file_scada_sha256": hashlib.sha256(Path(scada_zip).read_bytes()).hexdigest(),
        "source_file_registration_sha256": registration_sha256,
        "registration_source_url": REGISTRATION_URL if registry else None,
        "caveat": "NEM-wide SCADA totals are not NSW totals; separate NSW1 fuel groups use an AEMO DUID registry snapshot and exclude unmatched DUIDs and behind-the-meter rooftop solar. Five-minute SCADA MW integrated as MWh is approximate, storage charging must not count as generation, and the mix is NOT electricity physically traced to consumers.",
        "dispatch_nsw_intervals": len(records),
        "scada_nem_intervals": len(scada),
        "missing_nsw_intervals": missing_dispatch,
        "missing_nsw_prices": missing_price,
        "duplicate_nsw_prices": duplicate_prices,
        "missing_scada_intervals": missing_scada,
        "duplicate_nsw_intervals": duplicates,
        "duplicate_duid_intervals": source_summary["duplicate_duid_times"],
        "unique_scada_duids": len(source_summary["duids_seen"]),
        "scada_unit_rows": source_summary["scada_rows"],
        "time_basis": "AEST UTC+10 no DST, NEM dispatch settlement timestamp",
        "fuel_mix_status": (
            "PARTIAL REGISTERED NSW1 DUID FUEL MIX: excludes rooftop/unregistered generation;"
            " unmatched DUIDs remain unassigned, not presumed NSW"
            if registry else "NOT CLASSIFIED: official DUID-to-region-and-fuel register missing"
        ),
        "registration_duids": len(registry),
        "registration_conflicts": list(registry_conflicts),
        "matched_scada_duids": len(source_summary["registry_matched_duids"]),
        "unmatched_scada_duids": len(source_summary["unmatched_duids"]),
        "nsw_registered_scada_positive_mwh_by_fuel": {
            k: round(source_summary["nsw_fuel_mwh"][k], 3) for k in FUEL_TYPES
        },
        "nsw_registered_battery_charging_mwh": round(source_summary["nsw_storage_charge_mwh"], 3),
        "top_duids_by_approx_mwh_nem": [
            {"duid": k, "approx_mwh": round(v, 3)}
            for k, v in sorted(source_summary["duid_mwh"].items(),
                              key=lambda x: -abs(x[1]))[:12]
        ]
    }
    if records:
        demand = [r["nsw_total_demand_mw"] for r in records.values() if "nsw_total_demand_mw" in r]
        price = [r["nsw_spot_price_aud_per_mwh"] for r in records.values() if "nsw_spot_price_aud_per_mwh" in r]
        report["nsw_demand_mw_stats"] = {
            "min": round(min(demand), 3), "mean": round(statistics.mean(demand), 3),
            "max": round(max(demand), 3)
        }
        report["nsw_price_aud_per_mwh_stats"] = {
            "min": round(min(price), 3), "mean": round(statistics.mean(price), 3),
            "max": round(max(price), 3)
        }
    report["valid_complete_day"] = (not missing_dispatch and not missing_price
                                     and not missing_scada and not duplicates
                                     and not duplicate_prices and not source_summary["duplicate_duid_times"])
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
              "positive_scada_mw", "negative_scada_mw", "scada_unit_count",
              "nem_scada_unmapped_positive_mw"] + [
              "nsw_scada_" + x + "_mw" for x in FUEL_TYPES] + [
              "nsw_scada_battery_charging_mw"]
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
    parser.add_argument("--registration-xlsx", type=Path)
    parser.add_argument("--without-registration", action="store_true")
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
        reg_file = args.registration_xlsx or Path(temp) / "aemo-registration.xlsx"
        registry, conflicts, reg_sha = {}, [], None
        if not args.without_registration:
            if not args.registration_xlsx:
                download(REGISTRATION_URL, reg_file)
            registry, conflicts = load_registration(reg_file)
            reg_sha = hashlib.sha256(Path(reg_file).read_bytes()).hexdigest()
        rows, report = inspect(scada_zip, dispatch_zip, args.day,
                               strict=not args.allow_incomplete, registry=registry,
                               registration_sha256=reg_sha,
                               registry_conflicts=conflicts)
        write_outputs(rows, report, args.out)
        print(json.dumps({k: v for k, v in report.items()
                          if k.endswith("_intervals") and not isinstance(v, list)},
                         sort_keys=True))
        print("OUTPUT", args.out)
        print("FUEL_MIX", report["fuel_mix_status"])


if __name__ == "__main__":
    main()
