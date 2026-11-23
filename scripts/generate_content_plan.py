#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONTENT PLAN GENERATOR ENGINE (V2 - BATCH & SHIELDED)
Quy chuẩn Lọc đa tín hiệu, Chống Cannibalization và Tự động sinh Content Plan chuẩn Product/Tech Lead
Hỗ trợ sinh đơn lẻ (1 theme) hoặc sinh hàng loạt (1 Hub / toàn bộ Hub).
"""

import sys
import os
import glob
import csv
import re
import json
import argparse
import unicodedata
from collections import defaultdict, Counter

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INVENTORY_DIR = os.path.join(BASE_DIR, "05_HUBS", "inventory")
OUTPUT_DIR = os.path.join(BASE_DIR, "06_USE_CASE_MOMO", "content-plans")

sys.path.insert(0, BASE_DIR)
from scripts.lib.keyword_intelligence import (
    MultiSignalIntentClassifier,
    SemanticDomainFilter,
    SERPCannibalizationShield,
    StructuredSchemaGenerator,
    ContentBriefGenerator,
    InternalLinkingTopologyEngine,
    GEODirectAnswerGenerator,
    clean_val,
    normalize_text,
    calculate_opportunity_score,
    classify_priority
)

# clean_val / normalize_text / calculate_opportunity_score / classify_priority
# da duoc chuan hoa ve scripts/lib/keyword_intelligence.py (SSOT) - import o tren.


def production_wave(code):
    """Đổi mã ưu tiên nội bộ (P0/P1/P2) sang nhãn hiển thị 'Đợt n' theo quy chuẩn không gắn nhãn P trong tài liệu."""
    m = re.match(r"P(\d)", str(code))
    return f"Đợt {int(m.group(1)) + 1}" if m else str(code)

def determine_funnel(intent):
    if intent in ['Tool/Calculator', 'Transactional']:
        return 'BOFU'
    elif intent == 'Commercial':
        return 'MOFU'
    return 'TOFU'

def recommend_format(intent, is_pillar=False):
    if is_pillar:
        return 'Pillar Hub Page + Interactive Widget'
    if intent == 'Tool/Calculator':
        return 'Interactive Calculator / Lookup Tool'
    elif intent == 'Commercial':
        return 'Comparison Table & Evaluation'
    elif intent == 'Transactional':
        return 'Step-by-step How-to & Action Form'
    return 'Educational Guide & FAQ'

from scripts.lib.content_plan_config import (
    get_concrete_cta_hook,
    SUB_CLUSTER_RULES,
    SECTOR_RULES,
    FALLBACK_INTENT_CLUSTERS,
    make_norm_key,
    remove_accents,
    HEAD_SYNONYM_PHRASES,
    THRESHOLD,
    UMBRELLA_THEMES,
    BRAND_THEMES,
)
from scripts.sync_inventory_to_hubs import VIETNAMESE_THEME_NAMES, MERGE_MAP

def recommend_cta_hook(usecase_slug, intent=None):
    return get_concrete_cta_hook(usecase_slug)

def canonical_theme(csv_path):
    """Theme đích của 1 CSV theo MERGE_MAP (đồng bộ với sync_inventory_to_hubs)."""
    raw_slug = os.path.splitext(os.path.basename(csv_path))[0]
    clean_s = re.sub(r'[\s_]*\(\d+\)$', '', raw_slug).strip()
    return MERGE_MAP.get(clean_s, MERGE_MAP.get(clean_s.lower(), clean_s))


def theme_csv_group(csv_path):
    """Mọi CSV cùng Hub cùng theme đích: 1 theme = 1 content plan, kể cả khi dữ liệu nằm ở nhiều CSV."""
    target = canonical_theme(csv_path)
    sec_dir = os.path.dirname(csv_path)
    group = [p for p in sorted(glob.glob(os.path.join(sec_dir, '*.csv'))) if canonical_theme(p) == target]
    return target, group or [csv_path]


def _read_keyword_rows(path):
    with open(path, 'r', encoding='utf-8-sig', errors='replace') as f:
        for row in csv.DictReader(f):
            if row.get('Keyword'):
                yield row


def theme_tokens(theme_slug):
    return set(head_variant_key(theme_slug.replace('-', ' ')).split())


_HUB_CACHE = {}


def hub_themes(sector_dir):
    """Toàn bộ theme của 1 Hub: {theme: {'toks', 'keys', 'rows': [(kw, row)]}} (gộp CSV theo MERGE_MAP)."""
    if sector_dir not in _HUB_CACHE:
        hub = {}
        for p in sorted(glob.glob(os.path.join(sector_dir, '*.csv'))):
            t = canonical_theme(p)
            entry = hub.setdefault(t, {'toks': theme_tokens(t), 'keys': set(), 'rows': []})
            for row in _read_keyword_rows(p):
                kw = normalize_text(clean_val(row['Keyword']))
                entry['rows'].append((kw, row))
                entry['keys'].add(make_norm_key(kw))
        _HUB_CACHE[sector_dir] = hub
    return _HUB_CACHE[sector_dir]


def _phrase_in(phrase, text):
    """Khớp nguyên cụm từ (không khớp chuỗi con): 'giá' không khớp 'giám định', 'mua' không khớp 'mùa'."""
    return re.search(r'(?<!\w)' + re.escape(phrase) + r'(?!\w)', text) is not None


def brand_owner(kw, hub):
    """Theme thương hiệu (BRAND_THEMES) có mặt trong Hub mà từ khóa nhắc tới, None nếu không có."""
    plain = head_variant_key(kw)
    for theme, aliases in BRAND_THEMES.items():
        if theme in hub and any(_phrase_in(remove_accents(a.lower()), plain) for a in aliases):
            return theme
    return None


def keyword_owner(kw, origin, hub):
    """Theme sở hữu từ khóa (None = giữ ở theme gốc). Mỗi từ khóa trong Hub chỉ thuộc 1 plan.

    - Theme gốc là theme tổng (UMBRELLA_THEMES): nhường cho theme con có từ khóa này trong CSV.
    - Theme thường: nhường cho theme khác (không phải theme tổng) khi từ khóa chứa đủ head term của theme đó và
      (theme đó chuyên biệt hơn, hoặc từ khóa không chứa token riêng nào của theme gốc).
      Theme nhận sẽ kéo từ khóa về kể cả khi CSV của nó không có (không mất dữ liệu).
      Vd 'bảo hiểm pvi xe ô tô' (không có 'xe máy') rời bao-hiem-xe-may sang bao-hiem-o-to;
      'lãi suất tiết kiệm' vẫn ở gui-tiet-kiem vì còn token riêng 'tiết kiệm'.
    - Nhiều theme cùng khớp: chọn theme có head term dài nhất (cụ thể nhất).
    """
    brand = brand_owner(kw, hub)
    if brand is not None:
        return None if brand == origin else brand
    key = make_norm_key(kw)
    kw_toks = set(head_variant_key(kw).split())
    own_toks = hub[origin]['toks']
    best, best_len = None, 0
    for sib, info in hub.items():
        if sib == origin:
            continue
        sib_toks = info['toks']
        if origin in UMBRELLA_THEMES:
            if key in info['keys'] and sib not in UMBRELLA_THEMES:
                return sib
            continue
        if sib in UMBRELLA_THEMES or not sib_toks or not sib_toks <= kw_toks:
            continue
        if sib_toks > own_toks or not (kw_toks & (own_toks - sib_toks)):
            if len(sib_toks) > best_len:
                best, best_len = sib, len(sib_toks)
    if best is not None or origin in UMBRELLA_THEMES:
        return best
    # Phân xử cuối: từ khóa có trong CSV của nhiều theme ngang cấp -> theme khớp nhiều token head term hơn,
    # hòa thì theme có tên đứng trước (tất định, cho cùng kết quả dù xét từ phía theme nào)
    rivals = [t for t, info in hub.items()
              if t != origin and t not in UMBRELLA_THEMES and key in info['keys']]
    if not rivals:
        return None
    winner = min(rivals + [origin], key=lambda t: (-len(kw_toks & hub[t]['toks']), t))
    return None if winner == origin else winner


_OWNER_CACHE = {}


def hub_keyword_owners(sector_dir):
    """Bảng sở hữu toàn Hub: {key từ khóa: theme}. Mỗi key đúng 1 theme, tính 1 lần cho cả Hub.

    keyword_owner() xét từng lần xuất hiện nên không bắc cầu (A nhường B, nhưng bản ở C lại giữ ở C).
    Ở đây gom mọi ứng viên của cùng key rồi chọn 1: theme khớp nhiều token với từ khóa hơn,
    rồi head term cụ thể hơn, rồi tên theme. Theme tổng chỉ thắng khi không còn ứng viên nào khác.
    """
    if sector_dir not in _OWNER_CACHE:
        hub = hub_themes(sector_dir)
        cands, toks_of = defaultdict(set), {}
        for origin, info in hub.items():
            for kw, _ in info['rows']:
                key = make_norm_key(kw)
                cands[key].add(keyword_owner(kw, origin, hub) or origin)
                toks_of.setdefault(key, set(head_variant_key(kw).split()))
        owners = {}
        for key, themes in cands.items():
            brand = next((t for t in themes if t in BRAND_THEMES), None)
            if brand is not None:
                owners[key] = brand
                continue
            pool = [t for t in themes if t not in UMBRELLA_THEMES] or list(themes)
            kw_toks = toks_of[key]
            owners[key] = min(pool, key=lambda t: (-len(kw_toks & hub[t]['toks']), -len(hub[t]['toks']), t))
        _OWNER_CACHE[sector_dir] = owners
    return _OWNER_CACHE[sector_dir]


def head_term_keys(usecase_slug, usecase_name):
    """Các dạng head term của theme: slug, tên hiển thị, phần trước/trong ngoặc, từng vế nối bằng '&'."""
    keys = {make_norm_key(usecase_slug)}
    base = re.sub(r'\(.*?\)', '', usecase_name)
    parts = [usecase_name, base] + re.findall(r'\((.*?)\)', usecase_name) + base.split('&')
    keys.update(make_norm_key(x) for x in parts if x.strip())
    keys.discard('')
    return keys


def _tokens(text):
    return re.findall(r'[a-z0-9]+', remove_accents(text.lower()))


def head_variant_key(text):
    """Dạng chuẩn để so biến thể head term: không dấu, đã quy đồng nghĩa (xe hơi/oto -> ô tô...)."""
    s = ' ' + ' '.join(_tokens(text)) + ' '
    for src, dst in HEAD_SYNONYM_PHRASES:
        s = s.replace(f' {src} ', f' {dst} ')
    return ' '.join(s.split())


def _is_subsequence(needle, hay):
    it = iter(hay)
    return all(tok in it for tok in needle)


def pick_head_keyword(deduped_keywords, usecase_slug, usecase_name):
    """Pillar nhắm head term khớp URL theme (vd /bao-hiem-o-to/ -> 'bảo hiểm ô tô'), không nhắm long-tail volume cao nhất.

    Ứng viên: (a) khớp nguyên dạng slug / tên hiển thị / phần trong ngoặc, hoặc
    (b) chuỗi token là dãy con có thứ tự của tên hiển thị và chứa đủ token của slug
        (vd 'lịch chiếu phim' cho /lich-phim/ 'Lịch Chiếu Phim Rạp'; loại 'phim chiếu rạp' cho /rap/).
    Chọn ứng viên volume cao nhất; không có ứng viên thì lấy từ khóa volume cao nhất.
    """
    keys = head_term_keys(usecase_slug, usecase_name)
    name_toks = _tokens(re.sub(r'\(.*?\)', '', usecase_name).replace('&', ' '))
    slug_toks = set(_tokens(usecase_slug))
    matches = []
    for k in deduped_keywords:
        toks = _tokens(k['keyword'])
        if make_norm_key(k['keyword']) in keys or (toks and slug_toks <= set(toks) and _is_subsequence(toks, name_toks)):
            matches.append(k)
    return max(matches, key=lambda k: k['volume']) if matches else deduped_keywords[0]


def build_content_plan(csv_path):
    usecase_slug, group_paths = theme_csv_group(csv_path)
    usecase_name = VIETNAMESE_THEME_NAMES.get(usecase_slug, usecase_slug.replace('-', ' ').replace('_', ' ').title())
    sector = os.path.basename(os.path.dirname(csv_path))
    
    raw_keywords = []
    outliers_filtered = 0
    routed_to_child = 0
    pulled_from_siblings = 0
    sector_dir = os.path.dirname(os.path.abspath(csv_path))
    hub = hub_themes(sector_dir)
    owners = hub_keyword_owners(sector_dir)

    # Gom từ khóa thuộc theme này trên toàn Hub (CSV của theme + từ khóa theme khác nhường lại).
    # Cùng một từ khóa xuất hiện nhiều nơi chỉ giữ dòng volume cao nhất.
    best_rows = {}
    kw_freq = Counter()  # số lần một cách viết xuất hiện trong Hub: dùng chọn cách viết chuẩn khi gộp biến thể
    for origin, info in hub.items():
        for kw, row in info['rows']:
            owner = owners[make_norm_key(kw)]
            if origin == usecase_slug:
                if owner != usecase_slug:
                    routed_to_child += 1
                    continue
            elif owner != usecase_slug:
                continue
            else:
                pulled_from_siblings += 1
            try:
                vol = int(clean_val(row.get('Volume', '0')) or 0)
            except ValueError:
                vol = 0
            kw_freq[kw] += 1
            prev = best_rows.get(kw)
            if prev is None or vol > prev[0]:
                best_rows[kw] = (vol, row)

    for kw, (_, row) in best_rows.items():
        # Lọc từ khóa ngoài ngành và từ khóa rác cụt
        if kw in ['kiệm', 'nhiêu', 'thoại', 'khoản', 'toán', 'phẩm', 'vụ']:
            outliers_filtered += 1
            continue
            
        is_out, _ = SemanticDomainFilter.is_outlier(kw, sector, usecase_slug)
        if is_out:
            outliers_filtered += 1
            continue
            
        try:
            vol = int(clean_val(row.get('Volume', '0')) or 0)
        except ValueError:
            vol = 0
        try:
            cpc = float(clean_val(row.get('CPC', '0')) or 0.0)
        except ValueError:
            cpc = 0.0
        comp = clean_val(row.get('PPC Competition', 'Low'))
        
        intent_res = MultiSignalIntentClassifier.classify(kw)
        intent = intent_res['intent']
        score = calculate_opportunity_score(vol, cpc, comp, intent)
        priority = classify_priority(vol, comp, intent)
        
        raw_keywords.append({
            'keyword': kw,
            'volume': vol,
            'cpc': cpc,
            'competition': comp,
            'intent': intent,
            'intent_confidence': intent_res['confidence'],
            'score': score,
            'priority': priority
        })
        
    if not raw_keywords:
        return None, "Không tìm thấy từ khóa hợp lệ sau khi lọc.", []
        
    # Gộp biến thể chính tả: lấy max volume, lưu variants[]
    variant_groups = defaultdict(list)
    for k in raw_keywords:
        n_key = make_norm_key(k['keyword'])
        variant_groups[n_key].append(k)
        
    deduped_keywords = []
    variants_merged_count = 0
    for n_key, items in variant_groups.items():
        if len(items) > 1:
            variants_merged_count += (len(items) - 1)
            max_v = max(it['volume'] for it in items)
            max_cpc = max(it['cpc'] for it in items)
            def sort_key(x):
                kw_str = x['keyword']
                is_brand = 1 if kw_str in ['vietlott', 'epass', 'vetc', 'mbbank', 'vietcombank', 'techcombank'] else 0
                has_acc = 1 if (kw_str != make_norm_key(kw_str)) else 0
                # Hòa volume: ưu tiên cách viết phổ biến hơn, rồi cách viết đủ dấu hơn ('y tế' thắng 'y tê')
                marks = sum(1 for ch in unicodedata.normalize('NFKD', kw_str) if unicodedata.combining(ch))
                return (is_brand, has_acc, x['volume'], kw_freq[kw_str], marks, len(kw_str.split()))
            sorted_it = sorted(items, key=sort_key, reverse=True)
            leader = sorted_it[0]
            leader['volume'] = max_v
            leader['cpc'] = max_cpc
            leader['variants'] = [it['keyword'] for it in items if it['keyword'] != leader['keyword']]
            deduped_keywords.append(leader)
        else:
            it = items[0]
            it['variants'] = []
            deduped_keywords.append(it)
            
    deduped_keywords.sort(key=lambda x: x['volume'], reverse=True)
    top_overall_kw = pick_head_keyword(deduped_keywords, usecase_slug, usecase_name)
    
    # Phân cụm ngữ nghĩa động
    assigned_clusters = defaultdict(list)
    theme_rules = SUB_CLUSTER_RULES.get(usecase_slug) or SECTOR_RULES.get(sector) or []
    unassigned = []
    
    head_key = head_variant_key(top_overall_kw['keyword'])
    pillar_owned = []  # từ khóa không có trang riêng: thuộc về pillar
    for k in deduped_keywords:
        if k is top_overall_kw:
            continue  # head term thuộc riêng pillar, không đưa vào cụm con
        if head_variant_key(k['keyword']) == head_key:
            pillar_owned.append(k)  # biến thể đồng nghĩa của head term (vd 'bảo hiểm xe ô tô')
            continue
        kw_l = k['keyword'].lower()
        matched = False
        for rule in theme_rules:
            c_name, triggers, c_slug = rule
            if any(_phrase_in(tr, kw_l) for tr in triggers):
                assigned_clusters[(c_name, c_slug)].append(k)
                matched = True
                break
        if not matched:
            unassigned.append(k)
            
    for k in unassigned:
        intent = k['intent']
        fb = next((f for f in FALLBACK_INTENT_CLUSTERS if f[1] == intent), FALLBACK_INTENT_CLUSTERS[3])
        assigned_clusters[(fb[0], fb[2])].append(k)
        
    pillar_cta = get_concrete_cta_hook(usecase_slug)

    # Xây dựng các trang Con từ Sub-clusters thực tế (Ngưỡng >= 500)
    child_pages = []
    pruned_clusters = []
    sorted_clusters = sorted(assigned_clusters.items(), key=lambda x: sum(k['volume'] for k in x[1]), reverse=True)
    
    for (c_name, c_slug), cluster_kws in sorted_clusters:
        cluster_kws.sort(key=lambda x: x['volume'], reverse=True)
        tot_vol = sum(k['volume'] for k in cluster_kws)
        primary_k = cluster_kws[0]
        p_vol = primary_k['volume']
        
        # Chỉ có 1 cụm: không tách trang con, toàn bộ thuộc pillar
        if len(sorted_clusters) == 1:
            pillar_owned.extend(cluster_kws)
            continue

        if tot_vol < THRESHOLD and p_vol < THRESHOLD:
            pruned_clusters.append((c_name, tot_vol))
            pillar_owned.extend(cluster_kws)
            continue
            
        majority_intent = Counter(k['intent'] for k in cluster_kws).most_common(1)[0][0]
        prio = classify_priority(tot_vol, primary_k['competition'], majority_intent)
        funnel = determine_funnel(majority_intent)
        fmt = recommend_format(majority_intent)
        
        child_pages.append({
            'slug': f"/{usecase_slug}/{c_slug}/",
            'title': f"{c_name} {usecase_name}: Hướng Dẫn & Tra Cứu Chi Tiết",
            'primary_kw': primary_k['keyword'],
            'secondary_kws': [k['keyword'] for k in cluster_kws[1:5]],
            'volume': tot_vol,
            'intent': majority_intent,
            'format': fmt,
            'funnel': funnel,
            'priority': prio,
            'cta_hook': pillar_cta,
            'shielded_count': len(primary_k.get('variants', []))
        })
        
    # Pillar Hub: head term + các cụm không đủ ngưỡng lên trang riêng.
    # Mỗi từ khóa chỉ thuộc đúng 1 URL (không lặp giữa pillar và trang con).
    pillar_owned.sort(key=lambda x: x['volume'], reverse=True)
    pillar_plan = {
        'slug': f"/{usecase_slug}/",
        'title': f"Cẩm Nang & Bảng Tra Cứu {usecase_name} Toàn Diện",
        'primary_kw': top_overall_kw['keyword'],
        'secondary_kws': [k['keyword'] for k in pillar_owned[:4]],
        'volume': top_overall_kw['volume'] + sum(k['volume'] for k in pillar_owned),
        'intent': top_overall_kw['intent'],
        'format': 'Pillar Hub Page + Interactive Widget',
        'funnel': 'TOFU',
        'priority': 'P0',
        'cta_hook': pillar_cta,
        'shielded_count': len(top_overall_kw.get('variants', []))
    }

    full_plan = [pillar_plan] + child_pages
    stats = {
        'total_raw_keywords': len(raw_keywords) + outliers_filtered + routed_to_child,
        'outliers_pruned': outliers_filtered,
        'canonical_topics_count': len(deduped_keywords),
        'cannibalized_merged': variants_merged_count,
        'pruned_sub_clusters_count': len(pruned_clusters),
        'routed_to_child_themes': routed_to_child,
        'pulled_from_siblings': pulled_from_siblings,
        'source_csvs': [os.path.basename(p) for p in group_paths],
        'total_cluster_volume': sum(p['volume'] for p in full_plan),
        'sector': sector
    }
    return full_plan, stats, []


def export_content_plan_markdown(plan, stats, merge_log, usecase_slug, sector=None):
    usecase_name = VIETNAMESE_THEME_NAMES.get(usecase_slug, usecase_slug.replace('-', ' ').replace('_', ' ').title())
    target_dir = os.path.join(OUTPUT_DIR, sector) if sector else OUTPUT_DIR
    os.makedirs(target_dir, exist_ok=True)
    out_file = os.path.join(target_dir, f"{usecase_slug}-content-plan.md")
    
    extra_lines = ""
    if stats.get('total_cluster_volume', 0) == 0:
        extra_lines += ("- **Cảnh báo dữ liệu:** CSV nguồn chưa có Search Volume (toàn bộ = 0). Thứ tự ưu tiên, primary keyword "
                        "và Đợt Sản Xuất trong plan này chưa đáng tin cậy; cần cập nhật volume trong inventory rồi sinh lại.\n")
    if len(stats.get('source_csvs', [])) > 1:
        extra_lines += f"- **Nguồn dữ liệu gộp theo theme:** {', '.join(stats['source_csvs'])}\n"
    if stats.get('routed_to_child_themes'):
        extra_lines += f"- **Từ khóa nhường cho theme khác cùng Hub (chống trùng giữa các plan):** {stats['routed_to_child_themes']:,} từ khóa\n"
    if stats.get('pulled_from_siblings'):
        extra_lines += f"- **Từ khóa nhận từ CSV theme khác cùng Hub:** {stats['pulled_from_siblings']:,} từ khóa\n"

    md = f"""# KẾ HOẠCH NỘI DUNG CHUẨN (CONTENT PLAN V2 - SHIELDED) - THEME: {usecase_name.upper()}

- **Theme:** {usecase_name}
- **Hub:** {sector or 'General'}
- **URL Pillar Hub:** `{plan[0]['slug']}`
- **Tổng từ khóa thô ban đầu:** {stats['total_raw_keywords']:,} từ khóa
- **Từ khóa nhiễu bị loại bỏ:** {stats['outliers_pruned']:,} từ khóa
{extra_lines}- **Từ khóa trùng Intent được gom cụm (Shielded):** {stats['cannibalized_merged']:,} từ khóa
- **Số lượng URLs phân bổ:** {len(plan)} URLs (1 Pillar Hub + {len(plan)-1} Cluster Pages)
- **Quy tắc bảo vệ:** Mỗi URL giải quyết duy nhất 1 Intent độc lập. Các từ khóa cùng Intent đã được gom thành Secondary Synonyms (Zero Keyword Cannibalization).

---

## 1. BẢNG KẾ HOẠCH BÀI VIẾT CHI TIẾT (ACTIONABLE CONTENT PLAN)

| STT | URL Slug | Tiêu Đề Bài Viết / Trang Đích | Primary Keyword | Secondary Synonyms (Đã Gom Chống Ăn Thịt) | Search Volume | Search Intent | Định Dạng Nội Dung | Phễu | Đợt Sản Xuất | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |
"""
    for idx, p in enumerate(plan, 1):
        sec_str = ", ".join(p['secondary_kws'][:3]) if p['secondary_kws'] else "Đã bao hàm toàn cụm"
        md += f"| {idx} | `{p['slug']}` | {p['title']} | `{p['primary_kw']}` | {sec_str} | {p['volume']:,} | `{p['intent']}` | {p['format']} | `{p['funnel']}` | `{production_wave(p['priority'])}` | {p['cta_hook']} |\n"

    md += """\n---

## 2. NHẬT KÝ BẢO VỆ CHỐNG ĂN THỊT TỪ KHÓA (CANNIBALIZATION SHIELD LOG)

Dưới đây là các từ khóa có Search Intent và thực thể trùng lặp đã được tự động gom về bài viết tương ứng thay vì tách bài mới:

| STT | Từ Khóa Bị Trùng Lặp (Merged) | Gom Về Primary Keyword | Lý Do Hợp Nhất (Canonical Fingerprint / Similarity) | Volume Được Bảo Toàn |
| :---: | :--- | :--- | :--- | :---: |
"""
    for idx, m in enumerate(merge_log[:15], 1):
        md += f"| {idx} | `{m['merged_keyword']}` | `{m['canonical_primary']}` | {m['reason']} | {m['volume_added']:,} |\n"

    md += """\n---

## 3. NGUYÊN TẮC LIÊN KẾT NỘI BỘ (INTERNAL LINKING ARCHITECTURE)

1. **Liên kết 2 chiều Pillar <-> Cluster:**
   - Trang Pillar (`""" + plan[0]['slug'] + """`) liên kết bối cảnh tới tất cả các Cluster Pages.
   - 100% Cluster Pages bắt buộc đặt anchor text tự nhiên trong 100 từ đầu tiên dẫn về Pillar Page.
2. **Liên kết ngang giữa các Cluster:**
   - Trang Tính toán (`cong-cu-tinh-toan/`) liên kết sang trang So sánh (`so-sanh-danh-gia/`).
   - Trang Thủ tục (`thu-tuc-huong-dan/`) trỏ sang trang An toàn bảo mật (`an-toan-bao-mat/`).
3. **Móc chuyển đổi Web-to-App:**
   - Tích hợp Widget tương tác trực tiếp trên Web. Deeplink dẫn vào App MoMo để kích hoạt dịch vụ thực tế.

---

## 4. CONTENT BRIEF & DÀN Ý H2/H3 ENTITY CHECKLIST CHO TỪNG BÀI

Dưới đây là cấu trúc dàn ý chuẩn E-E-A-T và chỉ tiêu dung lượng bài viết để đội ngũ nội dung triển khai:
"""
    for idx, p in enumerate(plan, 1):
        wc = ContentBriefGenerator.estimate_word_count(p['format'], p['intent'], p['volume'])
        outline = ContentBriefGenerator.generate_outline_checklist(p, usecase_name)
        outline_str = "\n".join([f"   - {item}" for item in outline])
        md += f"""
### Bài {idx}: `{p['title']}`
- **URL Slug:** `{p['slug']}`
- **Chỉ tiêu độ dài:** `{wc['min_words']:,} - {wc['target_words']:,} từ` (Cấp bậc: `{wc['tier']}`)
- **Primary Keyword:** `{p['primary_kw']}`
- **Secondary Synonyms:** {", ".join(p['secondary_kws'][:4]) if p['secondary_kws'] else "Bao hàm ngữ nghĩa"}
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
{outline_str}
"""

    # 5. Sinh Schema JSON-LD mẫu cho Pillar Hub
    faq_qa = []
    for p in plan[1:4]:
        faq_qa.append((
            f"{p['title']}?",
            f"Thông tin chi tiết về {p['primary_kw']} được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
        ))
    faq_schema = StructuredSchemaGenerator.generate_faq_jsonld(usecase_name, faq_qa)
    breadcrumb_schema = StructuredSchemaGenerator.generate_breadcrumb_jsonld(sector or "Dịch Vụ", usecase_name, plan[0]['slug'])

    md += f"""\n---

## 5. DỮ LIỆU CẤU TRÚC JSON-LD (STRUCTURED DATA SCHEMA) CHO WEB DEV

Đội ngũ Frontend tại `hubs-momo` có thể sao chép trực tiếp 2 khối Schema này vào thẻ `<script type="application/ld+json">` của trang:

### A. BreadcrumbList Schema:
```json
{json.dumps(breadcrumb_schema, ensure_ascii=False, indent=2)}
```

### B. FAQPage Schema:
```json
{json.dumps(faq_schema, ensure_ascii=False, indent=2)}
```
"""

    # 6. Mạng lưới liên kết nội bộ phân tầng (Internal Linking & Silo Matrix)
    summary_path = os.path.join(BASE_DIR, "07_REPORTS", "data", "inventory_clusters_summary.json")
    all_usecases_cache = []
    if os.path.exists(summary_path):
        try:
            with open(summary_path, 'r', encoding='utf-8') as f:
                all_usecases_cache = json.load(f).get('usecases', [])
        except Exception:
            pass

    cur_uc_mock = {
        'id': usecase_slug,
        'name': usecase_name,
        'sector': sector or 'other',
        'top_opportunities': [{'keyword': p['primary_kw']} for p in plan]
    }
    silo_matrix = InternalLinkingTopologyEngine.build_silo_matrix(cur_uc_mock, all_usecases_cache)

    md += f"""\n---

## 6. KIẾN TRÚC LIÊN KẾT NỘI BỘ (INTERNAL LINKING & SILO MATRIX)

Phân tầng dòng chảy uy tín trang (PageRank) và định vị chuyên môn chủ đề (Topic Authority):

### A. Parent Hub Pillar:
- **Trang Cột Trụ Cấp 1:** `[{silo_matrix['parent_hub']['title']}]({silo_matrix['parent_hub']['url']})`
- **Anchor Text Mỏ Neo:** `"{silo_matrix['parent_hub']['anchor']}"`

### B. Liên kết ngang cùng Hub (Peer In-Silo):
| Thứ tự | Theme Bổ Trợ | Đường Dẫn Khuyến Nghị | Anchor Text Tự Nhiên | Độ Tương Đồng | Search Volume |
| :---: | :--- | :--- | :--- | :---: | :---: |
"""
    for idx, peer in enumerate(silo_matrix['peer_in_silo'], 1):
        md += f"| {idx} | `{peer['target_name']}` | `{peer['target_url']}` | `{peer['suggested_anchor']}` | `{peer['similarity_score']}` | {peer['volume']:,} |\n"

    md += """\n### C. Cầu nối liên kết xuyên Hub (Cross-Silo Bridges):
| Thứ tự | Theme Đích | Hub | Đường Dẫn Khuyến Nghị | Anchor Text Móc Nối | Search Volume |
| :---: | :--- | :--- | :--- | :--- | :---: |
"""
    for idx, bridge in enumerate(silo_matrix['cross_silo_bridges'], 1):
        md += f"| {idx} | `{bridge['target_name']}` | `{bridge['target_sector']}` | `{bridge['target_url']}` | `{bridge['suggested_anchor']}` | {bridge['volume']:,} |\n"

    # 7. Tối ưu hóa Tìm kiếm Tạo sinh (GEO & AI Direct Answers)
    primary_kw = plan[0]['primary_kw']
    primary_intent = plan[0]['intent']
    geo_snippet = GEODirectAnswerGenerator.generate_direct_answer_snippet(usecase_name, primary_kw, primary_intent, sector or 'other')
    entity_facts = GEODirectAnswerGenerator.generate_entity_factsheet(usecase_name, sector or 'other', primary_intent)

    md += f"""\n---

## 7. TỐI ƯU HÓA TÌM KIẾM TẠO SINH (GEO & AI DIRECT ANSWERS)

Cung cấp sẵn khối thông tin trích dẫn phục vụ trực tiếp cho Google AI Overviews, SearchGPT, Perplexity và Gemini:

### A. Đoạn trích dẫn trực tiếp (Direct Answer Snippet - 40-60 từ):
> "{geo_snippet}"

### B. Bảng thuộc tính thực thể (Entity Knowledge Graph Factsheet):
| Thuộc Tính Thực Thể | Giá Trị Chuẩn Hóa |
| :--- | :--- |
"""
    for fact in entity_facts:
        md += f"| {fact['entity_field']} | {fact['value']} |\n"

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(md)
    return out_file

def process_file(csv_path):
    usecase_slug = canonical_theme(csv_path)
    sector = os.path.basename(os.path.dirname(csv_path))
    plan, stats, merge_log = build_content_plan(csv_path)
    if not plan:
        return None, stats
    out_file = export_content_plan_markdown(plan, stats, merge_log, usecase_slug, sector)
    return out_file, stats

def main():
    parser = argparse.ArgumentParser(description="Content Plan Generator Engine (Batch & Shielded)")
    parser.add_argument("target", nargs="?", help="Tên file CSV cụ thể hoặc slug của theme")
    parser.add_argument("--all", action="store_true", help="Sinh Content Plan cho toàn bộ theme của mọi Hub")
    parser.add_argument("--sector", help="Chỉ sinh Content Plan cho một Hub cụ thể (ví dụ: Financial, vehicle-hub, insurtech)")
    args = parser.parse_args()

    if args.all:
        print(f"Bắt đầu sinh hàng loạt Content Plan cho toàn bộ theme tại: {INVENTORY_DIR}")
        csv_files = sorted(glob.glob(os.path.join(INVENTORY_DIR, "**", "*.csv"), recursive=True))
        success_count = 0
        total_vol = 0
        done_themes = set()  # nhiều CSV cùng theme (MERGE_MAP) chỉ sinh 1 plan
        for idx, f in enumerate(csv_files, 1):
            theme_key = (os.path.dirname(f), canonical_theme(f))
            if theme_key in done_themes:
                continue
            done_themes.add(theme_key)
            out_file, stats = process_file(f)
            if out_file:
                success_count += 1
                total_vol += stats['total_cluster_volume']
                print(f"[{idx}/{len(csv_files)}] {os.path.basename(out_file)}: {stats['canonical_topics_count']} topics | Gom {stats['cannibalized_merged']:,} cannibalized | Vol {stats['total_cluster_volume']:,}")
        print(f"\nHoàn tất! Đã xuất bản {success_count}/{len(csv_files)} Content Plans tại: {OUTPUT_DIR}")
        build_index_markdown()
        return

    if args.sector:
        sec_dir = os.path.join(INVENTORY_DIR, args.sector)
        if not os.path.exists(sec_dir):
            print(f"Lỗi: Không tìm thấy Hub '{args.sector}'")
            sys.exit(1)
        csv_files = sorted(glob.glob(os.path.join(sec_dir, "*.csv")))
        print(f"Bắt đầu sinh Content Plan cho Hub '{args.sector}' ({len(csv_files)} CSV)...")
        done_themes = set()  # nhiều CSV cùng theme (MERGE_MAP) chỉ sinh 1 plan
        for idx, f in enumerate(csv_files, 1):
            theme_key = (os.path.dirname(f), canonical_theme(f))
            if theme_key in done_themes:
                continue
            done_themes.add(theme_key)
            out_file, stats = process_file(f)
            if out_file:
                print(f"[{idx}/{len(csv_files)}] {os.path.basename(out_file)} - Topics: {stats['canonical_topics_count']} - Vol: {stats['total_cluster_volume']:,}")
        build_index_markdown()
        return

    if not args.target:
        parser.print_help()
        sys.exit(1)

    target = args.target
    csv_file = target
    if not os.path.exists(csv_file):
        matches = glob.glob(os.path.join(INVENTORY_DIR, "**", f"*{target}*.csv"), recursive=True)
        if matches:
            csv_file = matches[0]
        else:
            print(f"Lỗi: Không tìm thấy file từ khóa cho '{target}'")
            sys.exit(1)

    print(f"Đang xử lý tệp đơn lẻ: {csv_file}")
    out_file, stats = process_file(csv_file)
    if out_file:
        print(f"Đã xuất bản thành công Content Plan tại: {out_file}")
        print(f"- Tổng từ khóa sạch: {stats['total_raw_keywords'] - stats['outliers_pruned']:,} (Loại bỏ {stats['outliers_pruned']} nhiễu)")
        print(f"- Số từ khóa gom cụm chống ăn thịt: {stats['cannibalized_merged']:,}")
        print(f"- Tổng volume cụm được bảo toàn: {stats['total_cluster_volume']:,} lượt/tháng")
        build_index_markdown()

def build_index_markdown():
    """
    Tự động quét toàn bộ các file Content Plan Markdown trong OUTPUT_DIR
    và tạo tệp mục lục điều hướng trung tâm 06_USE_CASE_MOMO/content-plans/INDEX.md
    """
    plan_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "**", "*.md"), recursive=True))
    plan_files = [f for f in plan_files if not f.endswith("INDEX.md")]
    
    entries = []
    for pf in plan_files:
        rel_path = os.path.relpath(pf, OUTPUT_DIR)
        parts = rel_path.split(os.sep)
        sector = parts[0] if len(parts) > 1 else "Root"
        slug = os.path.splitext(os.path.basename(pf))[0]
        
        total_vol = 0
        canonical_count = 0
        usecase_title = ""
        sector_name = sector
        in_plan_table = False  # Chỉ cộng volume ở bảng kế hoạch (mục 1), bỏ qua các bảng liên kết chéo phía sau
        with open(pf, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('## '):
                    in_plan_table = line.startswith('## 1.') or 'CONTENT PLAN)' in line
                if "**Theme:**" in line:
                    usecase_title = line.split("**Theme:**")[-1].strip()
                elif "**Hub:**" in line:
                    sector_name = line.split("**Hub:**")[-1].strip()
                elif "**Số lượng URLs phân bổ:**" in line:
                    m = re.search(r'(\d+)', line)
                    if m:
                        canonical_count = int(m.group(1))
                elif in_plan_table and line.strip().startswith('|'):
                    cols = [c.strip() for c in line.split('|')]
                    if len(cols) >= 8:
                        val = cols[6].replace(',', '').strip()
                        if val.isdigit():
                            total_vol += int(val)
        entries.append({
            'sector': sector_name,
            'slug': slug.replace('-content-plan', ''),
            'rel_path': rel_path,
            'total_vol': total_vol,
            'canonical_count': canonical_count,
            'title': usecase_title or slug
        })

    entries.sort(key=lambda x: (x['sector'], -x['total_vol']))
    
    idx_content = f"""# MỤC LỤC CHIẾN LƯỢC NỘI DUNG TOÀN DIỆN (CONTENT PLANS DIRECTORY)

Trang mục lục tra cứu toàn bộ các bản kế hoạch nội dung (Content Plans) của MoMo Web Platform. Được tạo lập và đồng bộ tự động từ kho dữ liệu Semantic Keyword Inventory.

- **Tổng số Content Plans đã xuất bản:** {len(entries)} bản kế hoạch
- **Tổng dung lượng tìm kiếm phục vụ:** {sum(e['total_vol'] for e in entries):,} lượt/tháng

---

## DANH SÁCH CHI TIẾT THEO HUB

| Hub | Theme | Số Lượng Topic Clusters | Dung Lượng Tìm Kiếm | Liên Kết Chi Tiết |
| :--- | :--- | :---: | :---: | :--- |
"""
    for e in entries:
        idx_content += f"| `{e['sector']}` | **{e['slug']}** | {e['canonical_count']} topics | {e['total_vol']:,} | [{e['slug']}.md]({e['rel_path']}) |\n"

    index_path = os.path.join(OUTPUT_DIR, "INDEX.md")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(idx_content)
    print(f"Đã cập nhật tệp Mục Lục Trung Tâm tại: {index_path}")

if __name__ == '__main__':
    main()

