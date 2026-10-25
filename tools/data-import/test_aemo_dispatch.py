#!/usr/bin/env python3
"""NSW-ELEC-007 deterministic fixture tests; no network access."""
import importlib.util
import io
import json
import tempfile
import unittest
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("aemo_dispatch", HERE / "aemo_dispatch.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def make_archive(path, kind, instants):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as outer:
        for i, dt in enumerate(instants):
            stamp = dt.strftime("%Y/%m/%d %H:%M:%S")
            if kind == "scada":
                lines = [
                    "C,NEMP.WORLD,DISPATCHSCADA,AEMO,PUBLIC",
                    "I,DISPATCH,UNIT_SCADA,1,SETTLEMENTDATE,DUID,SCADAVALUE,LASTCHANGED",
                    f'D,DISPATCH,UNIT_SCADA,1,"{stamp}",TEST_COAL,100,"{stamp}"',
                    f'D,DISPATCH,UNIT_SCADA,1,"{stamp}",TEST_BATT,-5,"{stamp}"',
                ]
            else:
                lines = [
                    "C,NEMP.WORLD,DISPATCHIS,AEMO,PUBLIC",
                    "I,DISPATCH,REGIONSUM,5,SETTLEMENTDATE,REGIONID,TOTALDEMAND",
                    f'D,DISPATCH,REGIONSUM,5,"{stamp}",NSW1,9000',
                    f'D,DISPATCH,REGIONSUM,5,"{stamp}",QLD1,4500',
                    "I,DISPATCH,PRICE,5,SETTLEMENTDATE,REGIONID,RRP",
                    f'D,DISPATCH,PRICE,5,"{stamp}",NSW1,82.25',
                    f'D,DISPATCH,PRICE,5,"{stamp}",QLD1,60',
                ]
            inner_bytes = io.BytesIO()
            with zipfile.ZipFile(inner_bytes, "w", zipfile.ZIP_DEFLATED) as nested:
                nested.writestr(f"{kind}-{i}.CSV", "\n".join(lines) + "\n")
            outer.writestr(f"{kind}-{i}.zip", inner_bytes.getvalue())


class AemoImportTests(unittest.TestCase):
    def test_nem_aest_is_fixed_through_nsw_daylight_saving(self):
        clock = mod.parse_nem_time("2026/10/20 12:00:00")
        self.assertEqual(clock.utcoffset(), timedelta(hours=10))
        self.assertEqual(clock.astimezone(timezone.utc).hour, 2)

    def test_source_uses_real_schema_rows_not_header_guesswork(self):
        source = b"I,DISPATCH,UNIT_SCADA,1,SETTLEMENTDATE,DUID,SCADAVALUE\nD,DISPATCH,UNIT_SCADA,1,2026/10/20 00:05:00,T1,40\n"
        data = list(mod.decode_records(source, "fixture"))
        self.assertEqual(data[0][1], "UNIT_SCADA")
        self.assertEqual(data[0][2]["SCADAVALUE"], "40")

    def test_partial_day_reports_gaps_and_preserves_negative_scada(self):
        instants = [datetime(2026, 10, 20, 0, 5), datetime(2026, 10, 21, 0, 0)]
        with tempfile.TemporaryDirectory() as p:
            base = Path(p)
            make_archive(base/"s.zip", "scada", instants)
            make_archive(base/"d.zip", "dispatch", instants)
            rows, quality = mod.inspect(base/"s.zip", base/"d.zip", "2026-10-20", strict=False)
            self.assertEqual(len(rows), 2)
            self.assertEqual(quality["dispatch_nsw_intervals"], 2)
            self.assertEqual(quality["scada_nem_intervals"], 2)
            self.assertEqual(len(quality["missing_nsw_intervals"]), 286)
            self.assertEqual(rows[0]["positive_scada_mw"], 100)
            self.assertEqual(rows[0]["negative_scada_mw"], -5)
            self.assertEqual(rows[-1]["nem_aest"], "2026-10-21T00:00:00+10:00")
            self.assertEqual(rows[0]["utc"], "2026-10-19T14:05:00Z")
            self.assertEqual(quality["fuel_mix_status"].startswith("NOT CLASSIFIED"), True)

    def test_complete_288_interval_trading_day(self):
        start = datetime(2026, 10, 20)
        instants = [start + timedelta(minutes=5*i) for i in range(1, 289)]
        with tempfile.TemporaryDirectory() as p:
            base = Path(p)
            make_archive(base/"s.zip", "scada", instants)
            make_archive(base/"d.zip", "dispatch", instants)
            rows, quality = mod.inspect(base/"s.zip", base/"d.zip", "2026-10-20", strict=True)
            self.assertTrue(quality["valid_complete_day"])
            self.assertEqual(len(rows), 288)
            self.assertEqual(quality["scada_unit_rows"], 576)
            mod.write_outputs(rows, quality, base/"out")
            self.assertEqual(len((base/"out/nsw_nem_dispatch_5m.csv").read_text().splitlines()), 289)
            self.assertEqual(json.loads((base/"out/quality_report.json").read_text())["unique_scada_duids"], 2)


if __name__ == "__main__":
    unittest.main()
