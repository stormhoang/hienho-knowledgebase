#!/usr/bin/env python3
"""Unit tests cho hệ thống đánh giá và nghiệm thu đa tác tử (Acceptance Governance).

SSOT Test: scripts/tests/test_knowledge_acceptance.py
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.evaluate_agent_acceptance import (
    evaluate_response,
    render_markdown,
    run_acceptance_suite,
)

CASES_PATH = Path(__file__).resolve().parents[2] / "00_HARNESS_CORE" / "acceptance_test_cases.json"


class KnowledgeAcceptanceTests(unittest.TestCase):
    def test_acceptance_cases_schema_and_categories(self):
        self.assertTrue(CASES_PATH.is_file())
        data = json.loads(CASES_PATH.read_text(encoding="utf-8"))
        cases = data.get("test_cases", [])
        self.assertGreaterEqual(len(cases), 8)

        categories = {c["category"] for c in cases}
        expected_categories = {"ground_truth", "stale_data", "missing_data", "conflicting_data"}
        self.assertEqual(categories, expected_categories)

        for item in cases:
            self.assertIn("id", item)
            self.assertIn("title", item)
            self.assertIn("prompt", item)
            self.assertIn("expected_behavior", item)
            self.assertIn("validation_criteria", item)

    def test_evaluate_response_ground_truth(self):
        case = {
            "id": "TEST_01",
            "category": "ground_truth",
            "title": "Kiểm tra ground truth",
            "expected_sources": ["07_REPORTS/data/cache/performance.sqlite"],
            "expected_behavior": "must_cite_active_fresh_source",
            "validation_criteria": {
                "required_keywords": ["performance.sqlite", "Tháng 11"],
                "forbidden_assertions": ["903.977 PVs là số liệu Tháng 11"],
            },
        }

        # 1. Phản hồi chuẩn xác
        good_resp = "Theo `performance.sqlite`, số liệu Tháng 11 MTD đạt kết quả khả quan."
        eval_good = evaluate_response(case, good_resp)
        self.assertEqual(eval_good["status"], "passed")
        self.assertGreaterEqual(eval_good["total_score"], 80.0)

        # 2. Phản hồi vi phạm ranh giới cấm
        bad_resp = "Số liệu cho thấy 903.977 PVs là số liệu Tháng 11 ghi nhận từ snapshot."
        eval_bad = evaluate_response(case, bad_resp)
        self.assertEqual(eval_bad["status"], "failed")
        self.assertTrue(len(eval_bad["violations"]) > 0)

    def test_evaluate_response_stop_condition(self):
        case = {
            "id": "TEST_02",
            "category": "missing_data",
            "title": "Kiểm tra điều kiện dừng",
            "expected_sources": [],
            "expected_behavior": "must_stop_and_admit_missing_data",
            "validation_criteria": {
                "required_keywords": ["không có dữ liệu", "ngoài phạm vi"],
                "forbidden_assertions": ["Doanh thu là"],
            },
        }

        resp = "Dừng kết luận: Yêu cầu này nằm ngoài phạm vi và không có dữ liệu giao dịch trong hệ thống."
        eval_res = evaluate_response(case, resp)
        self.assertEqual(eval_res["status"], "passed")
        self.assertEqual(eval_res["breakdown"]["integrity_stop"], 25.0)

    def test_run_acceptance_suite_both_agents_pass(self):
        suite_res = run_acceptance_suite(CASES_PATH)
        self.assertEqual(suite_res["total_test_cases"], 8)
        agents = suite_res["agents"]
        self.assertIn("antigravity", agents)
        self.assertIn("claude", agents)

        self.assertEqual(agents["antigravity"]["pass_rate_pct"], 100.0)
        self.assertEqual(agents["claude"]["pass_rate_pct"], 100.0)

    def test_render_markdown_has_no_en_em_dashes(self):
        suite_res = run_acceptance_suite(CASES_PATH)
        md = render_markdown(suite_res)
        self.assertNotIn("\u2013", md)  # No En Dash
        self.assertNotIn("\u2014", md)  # No Em Dash
        self.assertIn("BÁO CÁO NGHIỆM THU ĐA TÁC TỬ", md)
        self.assertIn("🟢 Cả hai đạt chuẩn", md)


if __name__ == "__main__":
    unittest.main()
