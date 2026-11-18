#!/usr/bin/env python3
"""Unit tests cho động cơ gom cụm từ khóa thích ứng 3 tầng (Adaptive Clustering v2).

SSOT Test: scripts/tests/test_keyword_clustering.py
"""

from __future__ import annotations

import unittest
from scripts.lib.adaptive_clustering import (
    assign_intent_tier,
    build_adaptive_clusters_v2,
    clean_seed_name,
    merge_shells,
    mine_entities,
    name_has_overlap,
)


class KeywordClusteringTests(unittest.TestCase):
    def test_intent_tier_specificity(self):
        rules = [
            ("Lãi suất ngân hàng", ["lãi suất"]),
            ("Lãi suất Vietcombank", ["lãi suất vietcombank"]),
        ]
        items = [
            {"keyword": "lãi suất vietcombank hôm nay", "volume": 1000},
            {"keyword": "lãi suất chung", "volume": 500},
        ]
        assigned, residual = assign_intent_tier(items, rules)
        self.assertEqual(len(assigned), 2)
        # Item 0 phải khớp trigger dài hơn "lãi suất vietcombank"
        self.assertEqual(assigned[0][0], "Lãi suất Vietcombank")
        self.assertEqual(assigned[1][0], "Lãi suất ngân hàng")
        self.assertEqual(len(residual), 0)

    def test_clean_seed_name(self):
        self.assertEqual(clean_seed_name("mua vàng pnj online"), "Mua Vàng Pnj Online")
        self.assertEqual(clean_seed_name("lãi suất vietcombank 12 tháng năm 2026", max_words=3), "Lãi Suất Vietcombank")

    def test_name_has_overlap(self):
        items = [{"keyword": "giá vàng sjc hôm nay"}]
        self.assertTrue(name_has_overlap("Vàng SJC", items))
        self.assertFalse(name_has_overlap("Bất Động Sản", items))

    def test_merge_shells(self):
        clusters = [
            {"cluster_name": "Vietcombank", "count": 10, "members": [{"kw": "a"}] * 10},
            {"cluster_name": "Vietcombank Online", "count": 2, "members": [{"kw": "b"}] * 2},
        ]
        merged = merge_shells(clusters, min_kw=5)
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["count"], 12)

    def test_build_adaptive_clusters_v2_end_to_end(self):
        sample_keywords = [
            {"keyword": "giá vàng sjc", "volume": 50000, "opportunity_score": 90, "intent": "Informational"},
            {"keyword": "giá vàng pnj", "volume": 30000, "opportunity_score": 85, "intent": "Informational"},
            {"keyword": "giá vàng nhẫn 9999", "volume": 20000, "opportunity_score": 80, "intent": "Informational"},
            {"keyword": "bảng giá vàng thế giới", "volume": 15000, "opportunity_score": 75, "intent": "Informational"},
            {"keyword": "biểu đồ giá vàng", "volume": 10000, "opportunity_score": 70, "intent": "Informational"},
            {"keyword": "mua vàng pnj", "volume": 8000, "opportunity_score": 65, "intent": "Transactional"},
            {"keyword": "tiệm vàng mi hồng", "volume": 7000, "opportunity_score": 60, "intent": "Navigational"},
            {"keyword": "tiệm vàng ngọc thẩm", "volume": 6000, "opportunity_score": 55, "intent": "Navigational"},
            {"keyword": "giá vàng 18k", "volume": 5000, "opportunity_score": 50, "intent": "Informational"},
            {"keyword": "giá vàng 24k", "volume": 4000, "opportunity_score": 45, "intent": "Informational"},
        ]
        rules = [
            ("Giá Vàng SJC & Miếng", ["sjc", "vàng miếng"]),
            ("Giá Vàng Nhẫn & 9999", ["nhẫn", "9999"]),
        ]
        res = build_adaptive_clusters_v2(
            sample_keywords,
            sector="Financial",
            usecase_slug="gia-vang",
            usecase_name="Giá Vàng",
            rules=rules,
            top_n_clusters=5
        )
        self.assertGreater(len(res), 0)
        self.assertLessEqual(len(res), 5)
        # Đảm bảo mỗi cluster đều có top_keywords
        for c in res:
            self.assertIn("cluster_name", c)
            self.assertIn("count", c)
            self.assertIn("top_keywords", c)
            self.assertGreater(len(c["top_keywords"]), 0)


if __name__ == "__main__":
    unittest.main()
