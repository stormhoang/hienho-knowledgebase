"""Kiểm thử chọn head term pillar và quy tắc 1 từ khóa = 1 URL của generate_content_plan."""
import unittest

import glob
import os

from scripts.generate_content_plan import (
    INVENTORY_DIR,
    _phrase_in,
    brand_owner,
    hub_keyword_owners,
    hub_themes,
    head_variant_key,
    keyword_owner,
    pick_head_keyword,
    theme_tokens,
)
from scripts.lib.content_plan_config import make_norm_key
from scripts.lib.keyword_intelligence import SemanticDomainFilter, normalize_text


def kw(text, volume):
    return {'keyword': text, 'volume': volume}


def hub_of(themes):
    """themes: {slug: [keyword,...]} -> cấu trúc giống hub_themes()."""
    return {
        slug: {
            'toks': theme_tokens(slug),
            'keys': {make_norm_key(k) for k in kws},
            'rows': [(k, {}) for k in kws],
        }
        for slug, kws in themes.items()
    }


class HeadTermTests(unittest.TestCase):
    def test_pillar_targets_head_term_not_long_tail(self):
        kws = [kw('bảo hiểm thân vỏ ô tô', 2400), kw('bảo hiểm ô tô', 1900), kw('bảo hiểm xe ô tô', 1600)]
        head = pick_head_keyword(kws, 'bao-hiem-o-to', 'Bảo Hiểm Ô Tô (TNDS & Vật Chất)')
        self.assertEqual(head['keyword'], 'bảo hiểm ô tô')

    def test_head_term_follows_display_name_order(self):
        kws = [kw('phim chiếu rạp', 301000), kw('rạp chiếu phim', 90500)]
        head = pick_head_keyword(kws, 'rap', 'Rạp Chiếu Phim & Cụm Rạp')
        self.assertEqual(head['keyword'], 'rạp chiếu phim')

    def test_head_term_prefers_higher_volume_name_match(self):
        kws = [kw('lịch chiếu phim', 74000), kw('lịch phim', 3870)]
        head = pick_head_keyword(kws, 'lich-phim', 'Lịch Chiếu Phim Rạp')
        self.assertEqual(head['keyword'], 'lịch chiếu phim')

    def test_synonym_variants_share_head_key(self):
        self.assertEqual(head_variant_key('bảo hiểm xe hơi'), head_variant_key('bảo hiểm ô tô'))
        self.assertEqual(head_variant_key('bảo hiểm xe ô tô'), head_variant_key('bảo hiểm ô tô'))


class KeywordOwnerTests(unittest.TestCase):
    def setUp(self):
        self.hub = hub_of({
            'bao-hiem': ['bảo hiểm', 'bảo hiểm xã hội'],
            'bhxh': ['bảo hiểm xã hội'],
            'bhyt': ['bảo hiểm y tế'],
            'bao-hiem-o-to': ['bảo hiểm ô tô xe máy'],
            'bao-hiem-xe-may': ['bảo hiểm pvi xe ô tô', 'bảo hiểm ô tô xe máy', 'bảo hiểm xe'],
        })

    def test_umbrella_yields_to_child_theme(self):
        self.assertEqual(keyword_owner('bảo hiểm xã hội', 'bao-hiem', self.hub), 'bhxh')
        self.assertIsNone(keyword_owner('bảo hiểm', 'bao-hiem', self.hub))

    def test_never_routes_into_umbrella(self):
        self.assertIsNone(keyword_owner('bảo hiểm xe', 'bao-hiem-xe-may', self.hub))

    def test_keyword_without_own_tokens_moves_to_matching_theme(self):
        self.assertEqual(keyword_owner('bảo hiểm pvi xe ô tô', 'bao-hiem-xe-may', self.hub), 'bao-hiem-o-to')

    def test_more_specific_theme_wins(self):
        self.assertEqual(keyword_owner('phí đóng bảo hiểm y tế', 'bhxh', self.hub), 'bhyt')

    def test_shared_keyword_has_exactly_one_owner(self):
        text = 'bảo hiểm ô tô xe máy'
        owners = {t for t in ('bao-hiem-o-to', 'bao-hiem-xe-may')
                  if keyword_owner(text, t, self.hub) is None}
        self.assertEqual(len(owners), 1)


class HubOwnershipTests(unittest.TestCase):
    def test_every_hub_key_has_one_existing_owner(self):
        sector = os.path.join(INVENTORY_DIR, 'insurtech')
        if not glob.glob(os.path.join(sector, '*.csv')):
            self.skipTest('Không có inventory insurtech')
        hub, owners = hub_themes(sector), hub_keyword_owners(sector)
        self.assertTrue(owners)
        self.assertTrue(all(t in hub for t in owners.values()))
        self.assertNotIn('bao-hiem', {owners.get(make_norm_key('bảo hiểm y tế')), owners.get(make_norm_key('bảo hiểm ô tô'))})


class ClusterAndBrandTests(unittest.TestCase):
    def test_trigger_matches_whole_phrase_only(self):
        self.assertFalse(_phrase_in('giá', 'giám định bhyt'))
        self.assertTrue(_phrase_in('giá', 'giá bảo hiểm y tế'))
        self.assertTrue(_phrase_in('power 6 55', 'xổ số power 6 55 hôm nay'))

    def test_brand_theme_beats_generic_category(self):
        hub = hub_of({'vietlott': ['vietlott'], 'xo-so': ['xổ số'], 've-so': ['vé số']})
        self.assertEqual(brand_owner('xổ số vietlott', hub), 'vietlott')
        self.assertEqual(keyword_owner('xổ số mega', 'xo-so', hub), 'vietlott')
        self.assertIsNone(keyword_owner('xổ số vietlott', 'vietlott', hub))
        self.assertIsNone(brand_owner('xổ số miền bắc', hub))

    def test_brand_rule_only_inside_hub_with_brand_theme(self):
        hub = hub_of({'rap': ['rạp'], 'lich-phim': ['lịch phim']})
        self.assertIsNone(brand_owner('rạp mega gs', hub))


class OutlierFilterTests(unittest.TestCase):
    def test_vehicle_hub_folder_uses_vehicle_rules(self):
        self.assertTrue(SemanticDomainFilter.is_outlier('biển số xe gta', 'vehicle-hub', 'bien-so-xe')[0])

    def test_piracy_sites_filtered_in_cinema(self):
        self.assertTrue(SemanticDomainFilter.is_outlier('phimmoi chill', 'cinema', 'phim')[0])
        self.assertFalse(SemanticDomainFilter.is_outlier('phim chiếu rạp', 'cinema', 'phim')[0])

    def test_vietlott_products_not_filtered(self):
        self.assertFalse(SemanticDomainFilter.is_outlier('xổ số mega', 'Lottery', 'vietlott')[0])

    def test_tra_cuu_typo_fixed(self):
        self.assertEqual(normalize_text('Trả cứu BHYT'), 'tra cứu bhyt')


if __name__ == '__main__':
    unittest.main()
