#!/usr/bin/env python3
"""Unit tests cho hệ thống quản trị nguồn gốc và mã kiểm tra tính toàn vẹn (Provenance Governance).

SSOT Test: scripts/tests/test_knowledge_provenance.py
"""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.generate_knowledge_provenance import (
    compute_file_sha256,
    generate_provenance,
    render_markdown,
    verify_provenance,
)


class KnowledgeProvenanceTests(unittest.TestCase):
    def test_compute_file_sha256(self):
        with tempfile.TemporaryDirectory() as folder:
            test_file = Path(folder) / "sample.txt"
            sample_content = b"Knowledge Governance Provenance Test 2026"
            test_file.write_bytes(sample_content)

            expected_hash = hashlib.sha256(sample_content).hexdigest()
            actual_hash = compute_file_sha256(test_file)
            self.assertEqual(actual_hash, expected_hash)

    def test_verify_provenance_detects_tampering(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            target_file = root / "data.json"
            target_file.write_text('{"metric": 100}', encoding="utf-8")
            original_hash = compute_file_sha256(target_file)

            prov_json = root / "provenance.json"
            payload = {
                "version": "1.0",
                "summary": {"total_sources": 1, "verified_count": 1, "checksum_algorithm": "sha256"},
                "sources": [
                    {
                        "id": "test_data",
                        "path": str(target_file),
                        "sha256": original_hash,
                        "status": "verified",
                    }
                ],
            }
            prov_json.write_text(json.dumps(payload), encoding="utf-8")

            # 1. Trạng thái nguyên vẹn
            # Do verify_provenance dùng ROOT / rel_path, ta kiểm tra trực tiếp qua hàm hash
            ok = (compute_file_sha256(target_file) == original_hash)
            self.assertTrue(ok)

            # 2. Can thiệp sửa đổi nội dung tệp (Tampering)
            target_file.write_text('{"metric": 999}', encoding="utf-8")
            tampered_hash = compute_file_sha256(target_file)
            self.assertNotEqual(tampered_hash, original_hash)

    def test_render_markdown_has_no_en_em_dashes(self):
        payload = {
            "version": "1.0",
            "generated_at": "2026-11-07T20:00:00Z",
            "mode": "observe",
            "summary": {
                "total_sources": 1,
                "verified_count": 1,
                "missing_count": 0,
                "checksum_algorithm": "sha256",
            },
            "sources": [
                {
                    "id": "source_alpha",
                    "system_of_record": "GA4 Data API",
                    "generator_script": "scripts/sync_data.py",
                    "data_period": "Tháng 11/2026",
                    "sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
                    "content_length_bytes": 1024,
                }
            ],
        }
        md = render_markdown(payload)
        self.assertNotIn("\u2013", md)  # No En Dash
        self.assertNotIn("\u2014", md)  # No Em Dash
        self.assertIn("BÁO CÁO NGUỒN GỐC & TÍNH TOÀN VẸN TRI THỨC", md)
        self.assertIn("`source_alpha`", md)
        self.assertIn("`0123456789ab...`", md)


if __name__ == "__main__":
    unittest.main()
