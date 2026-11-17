import unittest

from scripts.validate_knowledge_registry import validate


def _entry(**overrides):
    entry = {'id': 'local_db', 'path': '07_REPORTS/data/cache/missing.sqlite', 'domain': 'performance',
             'type': 'analytical_data_mart', 'authority': 'primary', 'status': 'active',
             'used_for': ['performance_analysis']}
    entry.update(overrides)
    return entry


class ValidateRegistryTests(unittest.TestCase):
    def test_missing_source_is_reported(self):
        errors = validate({'entries': [_entry()]})
        self.assertIn('Không tìm thấy source: 07_REPORTS/data/cache/missing.sqlite', errors)

    def test_local_only_source_may_be_absent_in_ci(self):
        self.assertEqual(validate({'entries': [_entry(local_only=True)]}), [])

    def test_local_only_still_rejects_path_outside_repository(self):
        errors = validate({'entries': [_entry(path='../outside.sqlite', local_only=True)]})
        self.assertTrue(any('repository boundary' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
