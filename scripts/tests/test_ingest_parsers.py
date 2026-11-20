import tempfile
import unittest
from pathlib import Path

from scripts.ingest_paid_ads import (
    classify_hub,
    detect_file_kind,
    is_paid_source_medium,
    norm_header,
    parse_ga4_csv,
    pick_col,
    to_int,
)
from scripts.ingest_ga4_daily import find_latest_ga4_export, parse_ga4_daily_csv
from scripts.ingest_gsc_mtd import load_hub_map


class PaidAdsParserTests(unittest.TestCase):
    def test_norm_header_collapses_whitespace_and_case(self):
        self.assertEqual(norm_header("  Session  Default\nChannel   Group "), "session default channel group")

    def test_parse_ga4_csv_skips_comment_lines(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "export.csv"
            p.write_text(
                "# Bao cao GA4 Explore\n"
                "# Xuat ngay 2026-11-19\n"
                "Session default channel group,Landing page,Views\n"
                "(direct),/tai-chinh,100\n"
                "# Tong ket\n"
                "(cpc),/cinema,50\n",
                encoding="utf-8",
            )
            headers, rows = parse_ga4_csv(p)
            self.assertEqual(headers, ["session default channel group", "landing page", "views"])
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["views"], "100")

    def test_to_int_handles_separators_and_empty(self):
        self.assertEqual(to_int("1,234,567"), 1234567)
        self.assertEqual(to_int("708.298"), 708298)
        self.assertEqual(to_int(""), 0)
        self.assertEqual(to_int(None), 0)
        self.assertEqual(to_int("abc"), 0)

    def test_pick_col_skips_previous_period_columns(self):
        rec = {
            "views": "100",
            "views (previous)": "90",
            "sessions": "10",
        }
        self.assertEqual(pick_col(rec, "view"), "100")
        self.assertEqual(pick_col(rec, "session"), "10")
        self.assertEqual(pick_col(rec, "nonexistent"), "")

    def test_classify_hub_routes_known_sections(self):
        self.assertEqual(classify_hub("/cinema/rap/CGV"), "Cinema Hub")
        self.assertEqual(classify_hub("/tai-chinh/vay-nhanh"), "Financial Hub")
        self.assertEqual(classify_hub("/vietlott"), "Lottery Hub")
        self.assertEqual(classify_hub("/bao-hiem/xe-may"), "Vehicle & Insurtech")
        self.assertEqual(classify_hub("/"), "Branding & PR")
        self.assertEqual(classify_hub("/unknown-path"), "Other / General")
        self.assertEqual(classify_hub(""), "Branding & PR")

    def test_is_paid_source_medium(self):
        self.assertTrue(is_paid_source_medium("google / cpc"))
        self.assertTrue(is_paid_source_medium("facebook / paid"))
        self.assertTrue(is_paid_source_medium("cpc"))
        self.assertFalse(is_paid_source_medium("google / organic"))
        self.assertFalse(is_paid_source_medium(""))

    def test_detect_file_kind(self):
        self.assertEqual(
            detect_file_kind(["session default channel group", "landing page", "views"]),
            "traffic",
        )
        self.assertEqual(
            detect_file_kind(["event name", "page path", "event count"]),
            "events",
        )
        self.assertEqual(detect_file_kind(["date", "clicks"]), "unknown")


class Ga4DailyParserTests(unittest.TestCase):
    FIXTURE = (
        "GA4 Explore export\n"
        "Date range: 20261118-20261118\n"
        "Hostname,Event name,Page path + query string,Session default channel group,Views\n"
        "www.momo.vn,page_view,/cinema,Organic Search,300\n"
        "www.momo.vn,page_view,/tai-chinh/vay-nhanh,Direct,200\n"
        "www.momo.vn,page_view,/landing-ads,Paid Search,100\n"
        "evil.example.com,page_view,/spam,Organic Search,999\n"
        "www.momo.vn,page_view,Grand total,Organic Search,600\n"
    )

    def _write(self, d: str) -> Path:
        p = Path(d) / "ga4_daily.csv"
        p.write_text(self.FIXTURE, encoding="utf-8")
        return p

    def test_parse_ga4_daily_csv_aggregates(self):
        with tempfile.TemporaryDirectory() as d:
            result = parse_ga4_daily_csv(self._write(d))
        self.assertEqual(result["date"], "2026-11-18")
        self.assertEqual(result["month_str"], "2026-11")
        # 300 + 200 + 100; host khac va Grand total bi loai
        self.assertEqual(result["daily_pv"], 600)
        self.assertEqual(result["channels_pv"]["organic"], 300)
        self.assertEqual(result["channels_pv"]["direct"], 200)
        self.assertEqual(result["channels_pv"]["paid"], 100)
        self.assertEqual(result["page_views"]["/cinema"], 300)
        self.assertNotIn("/spam", result["page_views"])

    def test_parse_ga4_daily_csv_missing_header_raises(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "bad.csv"
            p.write_text("no header here\nfoo,bar\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                parse_ga4_daily_csv(p)

    def test_find_latest_ga4_export_picks_newest_matching(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            old = root / "old.csv"
            new = root / "new.csv"
            old.write_text("MoMo.vn data\n", encoding="utf-8")
            new.write_text("Hostname,Page path\n", encoding="utf-8")
            # ép mtime: new moi hon old
            import os
            os.utime(old, (1000, 1000))
            os.utime(new, (2000, 2000))
            unrelated = root / "unrelated.csv"
            unrelated.write_text("random,data\n", encoding="utf-8")
            self.assertEqual(find_latest_ga4_export(root), new)

    def test_find_latest_ga4_export_none_when_empty(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(find_latest_ga4_export(d))


class GscMtdSmokeTests(unittest.TestCase):
    def test_load_hub_map_returns_lowercase_mapping_or_empty(self):
        # HUB_MAP_PATH tro sang repo react-web-momo; co the khong ton tai
        # tren moi moi truong -> chap nhan dict rong, nhung neu co thi key phai lowercase.
        mapping = load_hub_map()
        self.assertIsInstance(mapping, dict)
        for k in mapping:
            self.assertEqual(k, k.lower())


if __name__ == "__main__":
    unittest.main()
