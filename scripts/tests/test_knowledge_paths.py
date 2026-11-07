import tempfile
import unittest
from pathlib import Path

from scripts.detect_knowledge_conflicts import scan, render_markdown
from scripts.triage_knowledge_conflicts import classify, render_yaml
import yaml


class KnowledgePathsTests(unittest.TestCase):
    def test_directory_and_jsonl_are_not_missing_json(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'data').mkdir()
            (root / 'docs.md').write_text(
                f'[directory](file://{root}/data)\nlog: data/push_log.jsonl\n')
            self.assertEqual(scan(root), [])

    def test_triage_preserves_evidence_and_code_uncertainty(self):
        finding = {'kind': 'code_path_reference', 'reference': 'data/output.json',
                   'raw_reference': 'data/output.json', 'sources': ['scripts/generate.py'],
                   'source': 'scripts/generate.py',
                   'line': 12, 'reason': 'code_runtime_or_generated_path',
                   'message': 'Runtime path candidate'}
        item = classify(finding)
        self.assertEqual(item['category'], 'code_path_review')
        payload = {'version': '1.0', 'generated_at': '2026-11-07',
                   'mode': 'observe', 'resolved': False, 'items': [item]}
        restored = yaml.safe_load(render_yaml(payload))['items'][0]
        for key in ('line', 'raw_reference', 'reason', 'sources'):
            self.assertEqual(restored[key], item[key])

    def test_relative_absolute_alias_and_generated_reports(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'docs').mkdir()
            (root / 'target.md').touch()
            (root / 'docs/source.md').write_text(
                f'[relative](../target.md) [absolute](file://{root}/target.md) '
                '[alias](Base/target.md) [missing](missing/file.md)\n'
                '[template](monthly_MM_YYYY/file.md)', encoding='utf-8')
            (root / 'knowledge_conflict_triage.yaml').write_text('bad/generated.md')
            findings = scan(root)
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0]['reference'], 'missing/file.md')
            self.assertEqual(findings[0]['line'], 1)

    def test_external_path_and_code_output_are_candidates(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'source.md').write_text('[outside](../../outside/data.json)')
            (root / 'generate.py').write_text('output = "data/generated.json"')
            self.assertEqual({item['kind'] for item in scan(root)},
                             {'external_reference', 'code_path_reference'})

    def test_template_placeholders_and_ignored_packages_are_skipped(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'docs').mkdir()
            (root / 'bold-template-pack').mkdir()
            (root / 'docs/guide.md').write_text(
                'Lệnh: `15_DISPATCH/<date>-<slug>.json`\n'
                'Đường dẫn: `data/snapshot-<id>.json`\n'
                'Tệp mẫu: `templates/<token>/config.yaml`\n'
                'Template pack: `bold-template-pack/design.md`\n',
                encoding='utf-8'
            )
            (root / 'bold-template-pack/preview.md').write_text(
                'Sub-template: `templates/preview/design.md`\n',
                encoding='utf-8'
            )
            self.assertEqual(scan(root), [])

    def test_markdown_rendering_contains_source_line_and_reason(self):
        payload = {
            'generated_at': '2026-11-07T20:00:00+00:00',
            'mode': 'observe',
            'conflict_count': 1,
            'conflicts': [{
                'kind': 'broken_reference',
                'reference': 'missing/path.md',
                'source': '00_HARNESS_CORE/test.md',
                'sources': ['00_HARNESS_CORE/test.md'],
                'line': 42,
                'reason': 'unresolved_internal_path',
                'message': 'Đường dẫn nội bộ không tìm thấy tệp đích trong repository.',
            }]
        }
        md = render_markdown(payload)
        self.assertIn('### `00_HARNESS_CORE/test.md`', md)
        self.assertIn('Dòng 42:', md)
        self.assertIn('`missing/path.md`', md)
        self.assertIn('unresolved_internal_path', md)
