import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from scripts.diagnose_performance import select_snapshot, validate_snapshot
from scripts.validate_evidence import validate


class EvidencePeriodTests(unittest.TestCase):
    def test_snapshot_rejects_channel_and_forecast_mismatch(self):
        source = Path("07_REPORTS/data/monthly_11_2026_mtd_4d.json")
        data = json.loads(source.read_text(encoding="utf-8"))
        self.assertEqual(validate_snapshot(data, date(2026, 11, 4)), [])
        data["channels"]["paid"]["pv"] += 1
        self.assertTrue(any("tổng kênh" in issue for issue in validate_snapshot(data, date(2026, 11, 4))))
        data["channels"]["paid"]["pv"] -= 1
        data["forecast_31d"] += 100
        self.assertTrue(any("forecast" in issue for issue in validate_snapshot(data, date(2026, 11, 4))))

    def test_missing_month_never_falls_back(self):
        with tempfile.TemporaryDirectory() as folder:
            Path(folder, "monthly_10_2026_consolidated.json").write_text(
                json.dumps({"days_elapsed": 31}), encoding="utf-8"
            )
            with self.assertRaisesRegex(ValueError, "Không có snapshot cho 2026-11"):
                select_snapshot("2026-11", Path(folder), date(2026, 11, 5))

    def test_snapshot_period_and_mtd_delta(self):
        base = "07_REPORTS/data/monthly_11_2026_mtd_"
        def claim(identifier, days, value):
            return {
                "id": identifier, "claim": identifier, "metric": f"mtd_{days}",
                "value": value, "unit": "PV", "source": f"{base}{days}d.json",
                "source_field": "actual_mtd_pv",
                "period": f"2026-11-01/2026-11-{days:02d}",
                "evidence_type": "fact", "confidence": "high",
            }
        payload = {"as_of": "2026-11-05", "claims": [
            claim("day4", 4, 370310), claim("day3", 3, 279547),
            {"id": "delta", "claim": "PV ngày 04/11", "metric": "daily_pv",
             "value": 90763, "unit": "PV", "source": f"{base}4d.json",
             "period": "2026-11-04", "evidence_type": "inference",
             "confidence": "high", "calculation": {"operator": "subtract", "inputs": ["day4", "day3"]}},
        ]}
        self.assertEqual(validate(payload, today=date(2026, 11, 5)), [])
        payload["claims"][0]["period"] = "2026-10-01/2026-10-04"
        self.assertTrue(any("period" in error for error in validate(payload, today=date(2026, 11, 5))))
        payload["claims"][0]["period"] = "2026-11-01/2026-11-04"
        payload["claims"][2]["value"] = 90000
        self.assertTrue(any("phép trừ" in error for error in validate(payload, today=date(2026, 11, 5))))


if __name__ == "__main__":
    unittest.main()
