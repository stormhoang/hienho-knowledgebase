#!/usr/bin/env python3
"""Unit tests cho hệ thống kiểm soát độ mới tri thức (Freshness Governance).

SSOT Test: scripts/tests/test_knowledge_freshness.py
"""

from __future__ import annotations

import json
import sqlite3
import tempfile
import unittest
from datetime import date
from pathlib import Path

from scripts.check_knowledge_freshness import (
    evaluate_freshness,
    extract_json_metadata,
    extract_markdown_metadata,
    extract_sqlite_metadata,
    parse_date_str,
    render_markdown,
    scan_registry_freshness,
)


class KnowledgeFreshnessTests(unittest.TestCase):
    def test_parse_date_formats(self):
        self.assertEqual(parse_date_str("2026-11-07"), date(2026, 11, 7))
        self.assertEqual(parse_date_str("2026-11-07 14:30:00"), date(2026, 11, 7))
        self.assertEqual(parse_date_str("2026-11-07T14:30:00Z"), date(2026, 11, 7))
        self.assertEqual(parse_date_str("07/11/2026"), date(2026, 11, 7))
        self.assertEqual(parse_date_str("10/10/2026 17:45"), date(2026, 10, 10))
        self.assertIsNone(parse_date_str("invalid-date"))
        self.assertIsNone(parse_date_str(None))

    def test_extract_markdown_metadata(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            
            # Case 1: Blockquote Header
            md_file1 = root / "snapshot.md"
            md_file1.write_text(
                "# Tiêu đề\n\n"
                "> **Cập nhật:** 10/10/2026 17:45 | **Kỳ dữ liệu:** Tháng 10/2026 (MTD 9 ngày)\n"
                "Nội dung báo cáo...",
                encoding="utf-8",
            )
            d1, period1, m1 = extract_markdown_metadata(md_file1)
            self.assertEqual(d1, date(2026, 10, 10))
            self.assertEqual(period1, "Tháng 10/2026 (MTD 9 ngày)")
            self.assertEqual(m1, "markdown_header:Cập nhật")

            # Case 2: GSC Heading
            md_file2 = root / "gsc.md"
            md_file2.write_text("## 7. CRAWL BUDGET (GSC DATA EXPORT 15/10/2026)\n", encoding="utf-8")
            d2, period2, m2 = extract_markdown_metadata(md_file2)
            self.assertEqual(d2, date(2026, 10, 15))
            self.assertEqual(m2, "markdown_heading:gsc_export")

            # Case 3: Table ISO dates
            md_file3 = root / "decisions.md"
            md_file3.write_text(
                "| **2026-10-14** | Quyết định A |\n| **2026-10-20** | Quyết định B |\n",
                encoding="utf-8",
            )
            d3, period3, m3 = extract_markdown_metadata(md_file3)
            self.assertEqual(d3, date(2026, 10, 20))
            self.assertEqual(m3, "markdown_table:max_date")

    def test_extract_json_metadata(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)

            # Case 1: updated_at with date_range
            f1 = root / "ads.json"
            f1.write_text(
                json.dumps({
                    "updated_at": "2026-10-25 14:16:24",
                    "date_range": {"start_date": "2026-10-01", "end_date": "today"},
                }),
                encoding="utf-8",
            )
            d1, period1, m1 = extract_json_metadata(f1)
            self.assertIsNone(d1)
            self.assertIsNone(period1)

            # Case 2: running month & daysElapsed
            f2 = root / "summary.json"
            f2.write_text(
                json.dumps({"running": {"month": "2026-11", "daysElapsed": 6}}),
                encoding="utf-8",
            )
            d2, period2, m2 = extract_json_metadata(f2)
            self.assertEqual(d2, date(2026, 11, 6))
            self.assertEqual(period2, "MTD đến 2026-11-06")

            # Case 3: List of records with date
            f3 = root / "releases.json"
            f3.write_text(
                json.dumps([{"date": "2026-10-01"}, {"date": "2026-10-30"}, {"date": "2026-10-15"}]),
                encoding="utf-8",
            )
            d3, period3, m3 = extract_json_metadata(f3)
            self.assertEqual(d3, date(2026, 10, 30))

    def test_extract_sqlite_metadata(self):
        with tempfile.TemporaryDirectory() as folder:
            db_path = Path(folder) / "test.sqlite"
            conn = sqlite3.connect(db_path)
            conn.execute("CREATE TABLE fact_daily_performance (date TEXT, synced_at TEXT)")
            conn.execute("INSERT INTO fact_daily_performance VALUES ('2026-11-04', '2026-11-05T02:00:00')")
            conn.execute("INSERT INTO fact_daily_performance VALUES ('2026-11-02', '2026-11-03T02:00:00')")
            conn.commit()
            conn.close()

            d, p, m = extract_sqlite_metadata(db_path)
            self.assertEqual(d, date(2026, 11, 4))
            self.assertIn("2026-11-04", p)
            self.assertEqual(m, "sqlite:fact_daily_performance")

    def test_evaluate_freshness_lifecycle(self):
        ref_date = date(2026, 11, 7)
        entry = {"id": "test_metric", "freshness_days": 7, "status": "active"}

        # 1. Fresh (age <= 7)
        meta_fresh = {
            "data_as_of": date(2026, 11, 4),
            "data_period": "Tuần 45",
            "file_mtime_date": date(2026, 11, 5),
            "file_modified_at": "2026-11-05T00:00:00Z",
            "extraction_method": "test",
        }
        res_fresh = evaluate_freshness(entry, meta_fresh, ref_date)
        self.assertEqual(res_fresh["status"], "fresh")
        self.assertEqual(res_fresh["age_days"], 3)
        self.assertIsNone(res_fresh["warning"])

        # 2. Lag reconciled (7 < age <= 10)
        meta_lag = {
            "data_as_of": date(2026, 10, 29),
            "data_period": "Cuối tháng 10",
            "file_mtime_date": date(2026, 10, 30),
            "file_modified_at": "2026-10-30T00:00:00Z",
            "extraction_method": "test",
        }
        res_lag = evaluate_freshness(entry, meta_lag, ref_date)
        self.assertEqual(res_lag["status"], "lag_reconciled")
        self.assertEqual(res_lag["age_days"], 9)
        self.assertIn("độ trễ", res_lag["warning"])

        # 3. Stale (age > 10)
        meta_stale = {
            "data_as_of": date(2026, 10, 10),
            "data_period": "Tháng 10",
            "file_mtime_date": date(2026, 11, 7),
            "file_modified_at": "2026-11-07T00:00:00Z",
            "extraction_method": "test",
        }
        res_stale = evaluate_freshness(entry, meta_stale, ref_date)
        self.assertEqual(res_stale["status"], "stale")
        self.assertEqual(res_stale["age_days"], 28)
        self.assertEqual(res_stale["mtime_drift_days"], 28)
        self.assertIn("CẢNH BÁO ĐỘ MỚI", res_stale["warning"])
        self.assertIsNotNone(res_stale["drift_notice"])

        # 4. Historical entry
        entry_hist = {"id": "hist_source", "status": "historical"}
        res_hist = evaluate_freshness(entry_hist, meta_stale, ref_date)
        self.assertEqual(res_hist["status"], "historical")

        # 5. Normative entry (no freshness_days)
        entry_norm = {"id": "contract", "status": "active"}
        res_norm = evaluate_freshness(entry_norm, meta_fresh, ref_date)
        self.assertEqual(res_norm["status"], "normative")

    def test_render_markdown_has_no_en_em_dashes(self):
        payload = {
            "reference_date": "2026-11-07",
            "mode": "observe",
            "summary": {
                "total_sources_checked": 2,
                "time_sensitive_sources": 1,
                "fresh_count": 1,
                "stale_count": 0,
                "lag_reconciled_count": 0,
                "normative_count": 1,
                "historical_count": 0,
                "unknown_count": 0,
            },
            "sources": [
                {
                    "id": "source_a",
                    "path": "data/a.json",
                    "domain": "performance",
                    "owner": "Web Platform",
                    "authority": "primary",
                    "entry_status": "active",
                    "freshness_threshold_days": 7,
                    "data_as_of": "2026-11-04",
                    "data_period": "Kỳ 01/11 - 04/11/2026",
                    "file_modified_at": "2026-11-05T00:00:00Z",
                    "file_mtime_date": "2026-11-05",
                    "age_days": 3,
                    "file_age_days": 2,
                    "mtime_drift_days": 1,
                    "status": "fresh",
                    "warning": None,
                    "drift_notice": None,
                },
                {
                    "id": "source_b",
                    "path": "docs/b.md",
                    "domain": "agent_governance",
                    "owner": "Web Product Lead",
                    "authority": "primary",
                    "entry_status": "active",
                    "freshness_threshold_days": None,
                    "data_as_of": None,
                    "data_period": "Quy chuẩn",
                    "file_modified_at": "2026-11-01T00:00:00Z",
                    "file_mtime_date": "2026-11-01",
                    "age_days": None,
                    "file_age_days": 6,
                    "mtime_drift_days": 0,
                    "status": "normative",
                    "warning": None,
                    "drift_notice": None,
                },
            ],
            "warnings": [],
        }
        md = render_markdown(payload)
        self.assertNotIn("\u2013", md)  # No En Dash
        self.assertNotIn("\u2014", md)  # No Em Dash
        self.assertIn("BÁO CÁO KIỂM SOÁT ĐỘ MỚI", md)
        self.assertIn("`source_a`", md)
        self.assertIn("🟢 Đạt chuẩn (Fresh)", md)


if __name__ == "__main__":
    unittest.main()
