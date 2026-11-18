#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SERP COMPETITOR ANALYZER ENGINE (Single Intent & Keyword Analysis)
Công cụ cào và phân tích đối thủ cạnh tranh theo một Intent tìm kiếm:
1. Thu thập Top 5-10 kết quả tìm kiếm tự nhiên (Organic SERP Results).
2. Cào sâu On-page của Top 3-5 đối thủ dẫn đầu (Title, H1, H2, H3, Word Count, Schemas).
3. Phân tích Khoảng trống nội dung (Competitor Content Gaps).
4. Thiết lập Chiến lược vượt mặt đối thủ cho MoMo Web Platform (Winning Blueprint).
"""

import sys
import os
import re
import json
import time
import ssl
import argparse
import urllib.request
import urllib.parse
from collections import Counter
import lxml.html

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(BASE_DIR, "scripts", "lib"))
from keyword_intelligence import MoMoDomainSERPShield
from keyword_extractor import analyze_content_gap, HAS_KEYBERT, HAS_ST, HAS_PYVI

# Bỏ qua kiểm tra chứng chỉ SSL cho các cổng thông tin Việt Nam
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

REPORTS_DIR = os.path.join(BASE_DIR, "07_REPORTS", "competitors")
DATA_DIR = os.path.join(BASE_DIR, "07_REPORTS", "data", "competitors")

USER_AGENTS = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15'
]

STOPWORDS = {
    'và', 'là', 'của', 'ở', 'tại', 'cho', 'với', 'trong', 'các', 'những',
    'được', 'có', 'ra', 'khi', 'về', 'này', 'đó', 'từ', 'theo', 'như',
    'để', 'lại', 'thì', 'người', 'cái', 'làm', 'hay', 'bao', 'nhiêu',
    'gì', 'sao', 'nao', 'nào', 'mấy', 'một', 'hai', 'ba', 'bốn', 'năm'
}

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def slugify(text: str) -> str:
    # Slug ASCII không dấu, thống nhất với content_plan_config.slugify (tránh sinh song song file có dấu và không dấu)
    from content_plan_config import slugify as ascii_slugify
    return ascii_slugify(text)

def fetch_page_text(url: str, limit: int = 20000) -> str:
    """Cào và làm sạch nội dung text của 1 URL (dùng cho trang MoMo hiện hữu)."""
    if not url:
        return None
    print(f"Đang lấy nội dung trang MoMo hiện hữu: {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENTS[0]})
        with urllib.request.urlopen(req, timeout=15, context=ssl_ctx) as resp:
            html_content = resp.read().decode('utf-8', errors='ignore')
        tree = lxml.html.fromstring(html_content)
        for bad in tree.xpath('//script | //style | //nav | //footer | //header | //noscript'):
            parent = bad.getparent()
            if parent is not None:
                parent.remove(bad)
        containers = tree.xpath('//article | //main')
        if not containers:
            body = tree.xpath('//body')
            containers = body if body else [tree]
        return clean_text(containers[0].text_content())[:limit]
    except Exception as e:
        print(f"   Cảnh báo: Không lấy được nội dung MoMo ({url}): {e}")
        return None

class SERPFetcher:
    """Thu thập kết quả tìm kiếm tự nhiên từ SERP và phát hiện vị thế momo.vn"""
    @classmethod
    def fetch_serp_results(cls, query: str, limit: int = 5) -> tuple:
        print(f"Đang truy vấn bảng xếp hạng tìm kiếm cho: '{query}'...")
        headers = {
            'User-Agent': USER_AGENTS[0],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        
        # Sử dụng DuckDuckGo HTML Engine vì chuẩn kết quả tiếng Việt
        data = urllib.parse.urlencode({'q': query, 'kl': 'vn-vi'}).encode('utf-8')
        req = urllib.request.Request('https://html.duckduckgo.com/html/', data=data, headers=headers)
        
        serp_items = []
        momo_ranking = None
        organic_counter = 0

        try:
            with urllib.request.urlopen(req, timeout=12, context=ssl_ctx) as resp:
                html_content = resp.read().decode('utf-8', errors='ignore')
                tree = lxml.html.fromstring(html_content)
                
                for r in tree.xpath('//div[contains(@class, "result__body")]'):
                    a = r.xpath('.//a[contains(@class, "result__url")]')
                    snippet_el = r.xpath('.//a[contains(@class, "result__snippet")]')
                    title_el = r.xpath('.//h2[contains(@class, "result__title")]//a')
                    
                    if title_el and a:
                        raw_url = a[0].get('href', '').strip()
                        # Chuẩn hóa url từ DuckDuckGo redirect nếu có
                        if '/l/?kh=-1&uddg=' in raw_url:
                            parsed_target = urllib.parse.parse_qs(urllib.parse.urlparse(raw_url).query).get('uddg')
                            if parsed_target:
                                raw_url = parsed_target[0]
                        
                        domain = urllib.parse.urlparse(raw_url).netloc.lower()
                        if any(ign in domain for ign in ['duckduckgo.com', 'youtube.com', 'facebook.com', 'tiktok.com']):
                            continue
                        if 'y.js' in raw_url or 'ad_provider' in raw_url:
                            continue
                        
                        organic_counter += 1
                        title = clean_text(title_el[0].text_content())
                        snippet = clean_text(snippet_el[0].text_content()) if snippet_el else ""
                        
                        # Phát hiện vị thế momo.vn trên SERP (Không tính vào đối thủ ngoại vi)
                        if 'momo.vn' in domain:
                            if not momo_ranking:
                                momo_ranking = {
                                    'rank': organic_counter,
                                    'title': title,
                                    'url': raw_url,
                                    'domain': domain,
                                    'snippet': snippet
                                }
                            continue

                        serp_items.append({
                            'rank': organic_counter,
                            'title': title,
                            'url': raw_url,
                            'domain': domain,
                            'snippet': snippet
                        })
                        if len(serp_items) >= limit:
                            break
        except Exception as e:
            print(f"Lỗi khi cào SERP: {e}")
            
        return serp_items, momo_ranking

class CompetitorPageParser:
    """Cào sâu cấu trúc On-Page của từng trang đối thủ"""
    @classmethod
    def parse_page(cls, item: dict) -> dict:
        url = item['url']
        print(f"Đang bóc tách On-page: [{item['rank']}] {item['domain']}...")
        headers = {
            'User-Agent': USER_AGENTS[item['rank'] % len(USER_AGENTS)],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'vi-VN,vi;q=0.9,en;q=0.8'
        }
        
        parsed_data = {
            'rank': item['rank'],
            'title': item['title'],
            'url': item['url'],
            'domain': item['domain'],
            'snippet': item['snippet'],
            'h1': [],
            'h2': [],
            'h3': [],
            'word_count': 0,
            'schemas': [],
            'has_table': False,
            'has_form_or_tool': False,
            'format_type': 'Article Guide'
        }
        
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10, context=ssl_ctx) as resp:
                html_content = resp.read().decode('utf-8', errors='ignore')
                tree = lxml.html.fromstring(html_content)
                
                # Trích xuất thẻ tiêu đề chính
                page_title = tree.xpath('//title/text()')
                if page_title:
                    parsed_data['page_title'] = clean_text(page_title[0])
                
                parsed_data['h1'] = [clean_text(h.text_content()) for h in tree.xpath('//h1') if clean_text(h.text_content())]
                
                # Trích xuất H2 và H3 (chỉ lấy các đề mục có ý nghĩa thực tế > 6 ký tự)
                h2_list = [clean_text(h.text_content()) for h in tree.xpath('//h2')]
                h2_filtered = [h for h in h2_list if len(h) >= 8 and not any(nav in h.lower() for nav in ['menu', 'tìm kiếm', 'liên hệ', 'bình luận', 'tin liên quan', 'bài viết khác'])]
                parsed_data['h2'] = h2_filtered[:12]
                
                h3_list = [clean_text(h.text_content()) for h in tree.xpath('//h3')]
                h3_filtered = [h for h in h3_list if len(h) >= 8 and not any(nav in h.lower() for nav in ['menu', 'đăng nhập', 'chia sẻ', 'xem thêm'])]
                parsed_data['h3'] = h3_filtered[:15]
                
                # Đếm số từ bài viết (tập trung vào body / article / main container)
                main_containers = tree.xpath('//article | //main | //div[contains(@class, "content") or contains(@class, "post") or contains(@class, "detail")]')
                target_container = main_containers[0] if main_containers else tree.xpath('//body')[0]
                text_content = target_container.text_content()
                words = re.findall(r'\b\w+\b', text_content)
                parsed_data['word_count'] = len(words)
                # Lưu body text (giới hạn 20.000 ký tự) phục vụ trích xuất keyword/entity
                parsed_data['body_text'] = clean_text(text_content)[:20000]
                
                # Kiểm tra yếu tố tương tác (Table, Form, Tool)
                parsed_data['has_table'] = len(tree.xpath('//table')) > 0
                parsed_data['has_form_or_tool'] = len(tree.xpath('//form | //input | //select | //button[contains(@class, "calc") or contains(text(), "Tính")]')) > 0
                
                if parsed_data['has_form_or_tool']:
                    parsed_data['format_type'] = 'Interactive Tool / Calculator'
                elif parsed_data['has_table']:
                    parsed_data['format_type'] = 'Comparison & Data Table'
                elif any('hỏi' in h.lower() or 'faq' in h.lower() for h in parsed_data['h2']):
                    parsed_data['format_type'] = 'FAQ & In-depth Guide'
                
                # Trích xuất Schema JSON-LD
                for s in tree.xpath('//script[@type="application/ld+json"]'):
                    try:
                        s_text = s.text_content().strip()
                        if s_text:
                            data = json.loads(s_text)
                            if isinstance(data, dict):
                                stype = data.get('@type')
                                if stype:
                                    parsed_data['schemas'].append(stype)
                            elif isinstance(data, list):
                                for d in data:
                                    if isinstance(d, dict) and d.get('@type'):
                                        parsed_data['schemas'].append(d.get('@type'))
                    except Exception:
                        pass
                parsed_data['schemas'] = list(set(parsed_data['schemas']))
                
        except Exception as e:
            print(f"   ⚠️ Lỗi cào trang {url}: {e}")
            parsed_data['error'] = str(e)
            
        return parsed_data

class ContentGapAnalyzer:
    """Phân tích khoảng trống nội dung và thiết kế chiến lược vượt mặt đối thủ"""
    @classmethod
    def analyze_gap_and_strategy(cls, query: str, competitor_pages: list, use_keybert: bool = True, momo_text: str = None) -> dict:
        valid_pages = [p for p in competitor_pages if p.get('word_count', 0) > 0]
        if not valid_pages:
            return {'error': 'Không thu thập được trang đối thủ hợp lệ'}
            
        # 1. Tính toán Word Count Benchmark
        word_counts = [p['word_count'] for p in valid_pages]
        avg_word_count = round(sum(word_counts) / len(word_counts))
        max_word_count = max(word_counts)
        recommended_target_words = max(round(max_word_count * 1.15), round(avg_word_count * 1.3), 1800)
        
        # 2. Bóc tách chủ đề chung (Common Subtopics từ H2)
        all_h2s = []
        for p in valid_pages:
            all_h2s.extend(p.get('h2', []))

        # 2b. Trích xuất Keyphrase & Thực thể chuẩn hóa (YAKE + RAKE + Semantic Rerank)
        kg = analyze_content_gap(valid_pages, momo_text=momo_text, top_n=20, use_keybert=use_keybert)
        top_entities = [e['entity'] for e in kg.get('entities', {}).get('brand_org', [])]
        if not top_entities:
            # Fallback: thống kê token H2 nếu không phát hiện thực thể thương hiệu/tổ chức
            h2_token_counter = Counter()
            for h2 in all_h2s:
                tokens = [t.lower() for t in re.findall(r'\b\w{3,}\b', h2) if t.lower() not in STOPWORDS]
                h2_token_counter.update(tokens)
            top_entities = [t for t, _ in h2_token_counter.most_common(10)]
        
        # 3. Phân loại định dạng dẫn đầu (Dominant SERP Format)
        format_counts = Counter(p['format_type'] for p in valid_pages)
        dominant_format = format_counts.most_common(1)[0][0]
        
        # 4. Xác định khoảng trống (Missing Gaps) mà đối thủ thường thiếu
        has_calculator = any(p['has_form_or_tool'] for p in valid_pages)
        has_faq_schema = any('FAQPage' in p.get('schemas', []) for p in valid_pages)
        
        gaps_detected = []
        if not has_calculator:
            gaps_detected.append("Thiếu công cụ tính toán / tra cứu tương tác trực tiếp (đa số trang chỉ có bài viết chữ đơn thuần).")
        if not has_faq_schema:
            gaps_detected.append("Chưa tối ưu Schema FAQPage để chiếm đoạt vị trí Rich Snippets trên kết quả tìm kiếm.")
        gaps_detected.append("Thiếu cơ chế chuyển tiếp liền mạch sang ứng dụng tài chính / giao dịch tức thì (Web-to-App).")
        gaps_detected.append("Thiếu bảng đối soát so sánh trực quan đa chiều giữa các phương án.")
        
        # 5. Thiết lập Dàn ý Vượt Trội của MoMo (Beating Outline Blueprint)
        beating_outline = [
            f"## H2 1: Tổng quan & Định nghĩa chuẩn xác về {query}",
            f"## H2 2: Bảng so sánh chi tiết & Tiêu chí lựa chọn tối ưu nhất",
            f"## H2 3: Công cụ tính toán / Tra cứu trực tuyến trên Nền tảng Web MoMo (Vượt trội đối thủ)",
            f"### H3 3.1: Hướng dẫn các bước thao tác và tính toán kết quả theo thời gian thực",
            f"## H2 4: Hướng dẫn quy trình & Thủ tục thực hiện từng bước đơn giản",
            f"## H2 5: 5 Lưu ý quan trọng & Rủi ro thường gặp cần phòng tránh",
            f"## H2 6: Giải đáp thắc mắc thường gặp (FAQs chuẩn Schema)",
            f"## H2 7: Giải pháp liên kết và nhận quyền lợi tối đa qua Ứng dụng MoMo"
        ]
        
        return {
            'query': query,
            'competitors_crawled': len(valid_pages),
            'avg_word_count': avg_word_count,
            'max_word_count': max_word_count,
            'recommended_target_words': recommended_target_words,
            'dominant_format': dominant_format,
            'top_competitor_entities': top_entities,
            'gaps_detected': gaps_detected,
            'beating_outline': beating_outline,
            'keyword_extraction': {
                'engines': kg.get('engines', {}),
                'excluded_low_quality_pages': kg.get('excluded_low_quality_pages', 0),
                'table_stakes': kg.get('table_stakes', []),
                'differentiators': kg.get('differentiators', []),
                'top_keyphrases': kg.get('top_keyphrases', []),
                'entities': kg.get('entities', {}),
                'per_page': kg.get('per_page', []),
            },
            'information_gain': kg.get('information_gain', {}),
            'content_gap': kg.get('content_gap', {}),
        }

def export_analysis_markdown(query: str, competitor_pages: list, analysis: dict, domain_shield: dict = None) -> str:
    """Xuất bản báo cáo phân tích đối thủ định dạng Markdown chuẩn Tech/Product Lead"""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    out_file = os.path.join(REPORTS_DIR, f"{slugify(query)}-competitor-analysis.md")
    
    shield_info = domain_shield or {}
    momo_rank_text = f"Top {shield_info['serp_rank']} (`{shield_info.get('ranking_url', '')}`)" if shield_info.get('serp_rank') else "Chưa có URL trong Top 20 Organic SERP"
    momo_live_text = f"`{shield_info.get('top_live_url')}`" if shield_info.get('top_live_url') else "Chưa phát hiện URL chính thức trên hệ thống"

    md = f"""# BÁO CÁO PHÂN TÍCH ĐỐI THỦ SERP & CHIẾN LƯỢC VƯỢT MẶT (COMPETITOR INTELLIGENCE)

- **Truy Vấn Tìm Kiếm (Intent Query):** `{query}`
- **Thời Gian Phân Tích:** {time.strftime('%Y-%m-%d %H:%M:%S')}
- **Đánh Giá Tự Ăn Thịt (Cannibalization Risk):** `{shield_info.get('risk_level', 'ZERO')}` (Hành động: `{shield_info.get('action', 'ALLOCATE_NEW')}`)
- **Số Lượng Đối Thủ Cào Chi Tiết:** {analysis.get('competitors_crawled', 0)} trang
- **Định Dạng Thống Trị SERP (Dominant Format):** `{analysis.get('dominant_format', 'N/A')}`
- **Chỉ Tiêu Độ Dài MoMo Khuyến Nghị:** `{analysis.get('recommended_target_words', 0):,} từ` (Vượt trội mức trung bình đối thủ: `{analysis.get('avg_word_count', 0):,} từ`)

---

## 1. VỊ THẾ HIỆN TẠI CỦA MOMO.VN & ĐỐI SOÁT TỰ ĂN THỊT TỪ KHÓA (DOMAIN SERP CANNIBALIZATION)

| Hạng Mục Đánh Giá | Chi Tiết Trạng Thái | Ý Nghĩa Kỹ Thuật & Vận Hành |
| :--- | :--- | :--- |
| **Mức độ Rủi ro (Risk Level)** | `{shield_info.get('risk_level', 'ZERO')}` | Đánh giá khả năng xung đột thứ hạng với bài viết hiện có của MoMo |
| **Quyết định Phân bổ (Verdict)** | `{shield_info.get('verdict', 'SAFE_TO_ALLOCATE')}` | Cho phép hoặc chặn việc tạo mới URL trên Web Platform |
| **Hành động Khuyến nghị (Action)** | `{shield_info.get('action', 'ALLOCATE_NEW')}` | Hành động tối ưu nhất (Protect & Link / Refresh Old URL / Allocate New) |
| **Thứ hạng SERP Thực tế** | {momo_rank_text} | Vị trí Organic hiện tại của momo.vn trên Google/SERP |
| **URL Đã Xuất Bản Trong Hệ Thống** | {momo_live_text} | URL đối soát từ kho Live Sitemap SSOT của momo.vn |

> **Cơ sở Ra Quyết Định Chiến Lược (Rationale):**
> {shield_info.get('rationale', 'Đủ điều kiện phân bổ từ khóa mới.')}

---

## 2. BẢNG SO SÁNH CẤU TRÚC TOP ĐỐI THỦ DẪN ĐẦU (SERP LEADERBOARD)

| Thứ Hạng | Tên Miền (Domain) | Tiêu Đề Bài Viết (Title Tag) | Độ Dài (Words) | Định Dạng Trang | Cấu Trúc H2 Đáng Chú Ý | Schema JSON-LD |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- |
"""
    for p in competitor_pages:
        h2_preview = ", ".join([f"`{h[:35]}...`" if len(h) > 35 else f"`{h}`" for h in p.get('h2', [])[:3]]) if p.get('h2') else "Không có H2 rõ ràng"
        schemas_str = ", ".join(p.get('schemas', [])) if p.get('schemas') else "Trống"
        md += f"| Top {p['rank']} | `{p['domain']}` | {p['title']} | {p.get('word_count', 0):,} | {p.get('format_type', 'N/A')} | {h2_preview} | {schemas_str} |\n"

    md += """\n---

## 3. BÓC TÁCH CHI TIẾT CẤU TRÚC HEADING (H2/H3) TỪNG ĐỐI THỦ
"""
    for p in competitor_pages:
        md += f"""
### Top {p['rank']}: `{p['domain']}` - [{p['title']}]({p['url']})
- **Độ dài bài viết:** `{p.get('word_count', 0):,} từ`
- **H1:** `{p.get('h1', ['N/A'])[0] if p.get('h1') else 'N/A'}`
- **Dàn ý H2 đối thủ triển khai:**
"""
        if p.get('h2'):
            for h2 in p.get('h2', []):
                md += f"  - `{h2}`\n"
        else:
            md += "  - *(Không phát hiện cấu trúc H2 chuẩn)*\n"

    md += f"""\n---

## 4. PHÂN TÍCH KHOẢNG TRỐNG NỘI DUNG (CONTENT GAPS)

Qua đối soát cấu trúc On-Page của các đối thủ dẫn đầu, hệ thống phát hiện các điểm yếu và khoảng trống sau:

"""
    for idx, gap in enumerate(analysis.get('gaps_detected', []), 1):
        md += f"{idx}. **Khoảng trống {idx}:** {gap}\n"

    md += f"""
- **Các thực thể ngữ nghĩa trọng tâm đối thủ tập trung:** {", ".join([f"`{e}`" for e in analysis.get('top_competitor_entities', [])])}

---

## 5. TRÍCH XUẤT KEYWORD & THỰC THỂ ĐỐI THỦ (CONTENT GAP & INFORMATION GAIN)
"""
    ke = analysis.get('keyword_extraction', {})
    engines = ke.get('engines', {})
    md += f"""
- **Engine trích xuất:** YAKE `{engines.get('yake')}` | RAKE `{engines.get('rake')}` | Semantic Rerank `{engines.get('semantic_rerank')}` (model: `{engines.get('embedding_model') or 'n/a'}`)
- **Số trang đối thủ phân tích:** {analysis.get('competitors_crawled', 0)} (loại bỏ {ke.get('excluded_low_quality_pages', 0)} trang rác/thiếu nội dung)

### 5.1. Bộ từ khóa bắt buộc (Table Stakes - xuất hiện ở >= 1/2 số trang đối thủ)

| # | Cụm từ khóa (Concept) | Độ phủ (trang) | Tỷ lệ phủ | Loại câu hỏi | Biến thể khác |
| :---: | :--- | :---: | :---: | :---: | :--- |
"""
    ts = ke.get('table_stakes', [])
    if ts:
        for i, item in enumerate(ts, 1):
            q = 'Có' if item.get('is_question') else '-'
            variants = ", ".join([f"`{v}`" for v in item.get('variants', [])[1:4]])
            md += f"| {i} | `{item.get('phrase')}` | {item.get('coverage')} | {item.get('coverage_pct')}% | {q} | {variants or '-'} |\n"
    else:
        md += "| - | *(Không phát hiện cụm từ bắt buộc)* | - | - | - | - |\n"

    md += """
### 5.2. Điểm khác biệt của từng đối thủ (Differentiators - chỉ xuất hiện ở 1 trang)

"""
    dif = ke.get('differentiators', [])
    if dif:
        for item in dif:
            md += f"- `{item.get('phrase')}`\n"
    else:
        md += "- *(Không phát hiện điểm khác biệt đáng kể)*\n"

    ents = ke.get('entities', {})
    md += """
### 5.3. Thực thể trọng tâm (Entity Extraction)

| Nhóm thực thể | Thực thể (tần suất) |
| :--- | :--- |
"""
    brand = ", ".join([f"`{e['entity']}` ({e['count']})" for e in ents.get('brand_org', [])]) or "Trống"
    numeric = ", ".join([f"`{e['entity']}` ({e['count']})" for e in ents.get('numeric', [])]) or "Trống"
    md += f"| Tổ chức / Thương hiệu | {brand} |\n"
    md += f"| Dữ liệu định lượng (số, %, kỳ hạn) | {numeric} |\n"

    ig = analysis.get('information_gain', {})
    md += """
### 5.4. Khoảng trống Information Gain (Góc dữ liệu độc quyền MoMo - Anti-LLM Moat)

**Câu hỏi/nhóm ý đối thủ bỏ trống (độ phủ thấp):**

"""
    qg = ig.get('question_gaps', [])
    if qg:
        for g in qg:
            md += f"- `{g}`\n"
    else:
        md += "- *(Đối thủ đã bao phủ phần lớn nhóm câu hỏi)*\n"

    md += """
**Đề xuất điểm chạm nội dung vượt trội (Recommended Unique Angles):**

"""
    for a in ig.get('recommended_unique_angles', []):
        md += f"- {a}\n"

    cg = analysis.get('content_gap', {})
    md += """
### 5.5. Content Gap - Đối chiếu trang MoMo hiện hữu với đối thủ (Concept-level)

"""
    if cg.get('momo_analyzed'):
        md += f"""- **URL MoMo đối chiếu:** `{shield_info.get('top_live_url', 'n/a')}`
- **Tổng Concept đối thủ:** {cg.get('competitor_concepts')} | **MoMo đã phủ:** {cg.get('momo_covered')} | **Còn thiếu:** {cg.get('missing_in_momo')} ({cg.get('gap_pct')}%)

**Concept đối thủ phủ nhưng MoMo còn thiếu (ưu tiên bổ sung):**

| # | Concept thiếu | Độ phủ đối thủ | Tỷ lệ phủ | Câu hỏi |
| :---: | :--- | :---: | :---: | :---: |
"""
        miss = cg.get('missing_concepts', [])
        if miss:
            for i, m in enumerate(miss, 1):
                q = 'Có' if m.get('is_question') else '-'
                md += f"| {i} | `{m.get('phrase')}` | {m.get('coverage')} | {m.get('coverage_pct')}% | {q} |\n"
        else:
            md += "| - | *(MoMo đã phủ toàn bộ Concept đối thủ)* | - | - | - |\n"

        md += """
**Concept MoMo đã phủ (giữ vững & tối ưu):**

"""
        cov = cg.get('momo_covered_concepts', [])
        if cov:
            for c in cov:
                md += f"- `{c.get('phrase')}` (khớp: `{c.get('matched_momo_phrase')}`, sim: {c.get('similarity')})\n"
        else:
            md += "- *(Chưa phát hiện concept nào khớp giữa MoMo và đối thủ)*\n"
    else:
        md += "- *(Không lấy được nội dung trang MoMo hiện hữu để đối chiếu Content Gap)*\n"

    md += f"""
---

## 6. CHIẾN LƯỢC VƯỢT MẶT ĐỐI THỦ CHO MOMO WEB PLATFORM (WINNING BLUEPRINT)

Để đưa trang MoMo Web Platform chiếm lĩnh vị trí **Top 1 Google** và **Trích dẫn ưu tiên trên Google AI Overviews**, bài viết bắt buộc phải tuân thủ quy chuẩn sau:

### A. Chỉ tiêu định lượng kỹ thuật:
- **Hạn mức độ dài bài viết:** Tối thiểu `{analysis.get('recommended_target_words', 2200):,} từ`.
- **Dữ liệu cấu trúc bắt buộc:** Nhúng đầy đủ `BreadcrumbList` và `FAQPage` Schema.
- **Điểm chạm chuyển đổi (UX Hook):** Bắt buộc tích hợp Widget tra cứu / tính toán trực tiếp trên Web kết hợp Deeplink chuyển đổi sang App MoMo.

### B. Dàn ý H2/H3 vượt trội (Beating Outline Blueprint):
"""
    for item in analysis.get('beating_outline', []):
        md += f"- {item}\n"

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"\nĐã xuất bản báo cáo phân tích đối thủ tại: {out_file}")
    return out_file

def main():
    parser = argparse.ArgumentParser(description="SERP Competitor Analyzer Engine (Single Intent & Keyword)")
    parser.add_argument("query", help="Từ khóa hoặc Intent tìm kiếm cần phân tích đối thủ")
    parser.add_argument("--limit", type=int, default=5, help="Số lượng đối thủ SERP cần cào sâu (Mặc định: 5)")
    parser.add_argument("--json", action="store_true", help="Xuất file JSON thô vào 07_REPORTS/data/competitors/")
    parser.add_argument("--fast", action="store_true", help="Tắt Semantic Rerank (KeyBERT embedding), chỉ dùng YAKE + RAKE (nhanh hơn)")
    args = parser.parse_args()
    use_keybert = not args.fast

    query = args.query.strip()
    print(f"\n=== KHỞI ĐỘNG PHÂN TÍCH ĐỐI THỦ SERP CHO TRUY VẤN: '{query}' ===\n")
    
    # Bước 1: Cào kết quả SERP & phát hiện vị thế momo.vn
    serp_items, momo_ranking = SERPFetcher.fetch_serp_results(query, limit=args.limit)
    
    # Bước 1b: Đối soát Domain SERP Cannibalization qua MoMoDomainSERPShield
    domain_shield = MoMoDomainSERPShield.evaluate_cannibalization_risk(query, check_live_serp=False)
    if momo_ranking:
        domain_shield['serp_rank'] = momo_ranking['rank']
        domain_shield['ranking_url'] = momo_ranking['url']
        domain_shield['ranking_title'] = momo_ranking['title']
        if momo_ranking['rank'] <= 3:
            domain_shield['risk_level'] = "CRITICAL"
            domain_shield['verdict'] = "BLOCK_NEW_URL"
            domain_shield['action'] = "PROTECT_AND_LINK"
            domain_shield['rationale'] = f"MoMo đang xếp hạng Top {momo_ranking['rank']} trên SERP ({momo_ranking['url']}). Tuyệt đối KHÔNG tạo URL mới vì sẽ gây hiện tượng tự ăn thịt thứ hạng (Self-Cannibalization). Hành động: Giữ URL hiện tại, cắm widget tra cứu/chuyển đổi và tối ưu internal link."
        elif momo_ranking['rank'] <= 20:
            domain_shield['risk_level'] = "MODERATE"
            domain_shield['verdict'] = "BLOCK_NEW_URL"
            domain_shield['action'] = "REFRESH_EXISTING_URL"
            domain_shield['rationale'] = f"MoMo đang xếp hạng Top {momo_ranking['rank']} trên SERP ({momo_ranking['url']}) ở cự ly Striking Distance. Tuyệt đối KHÔNG tạo URL mới. Cần nâng cấp On-page và Content Refresh trên URL hiện tại để bứt phá vào Top 3."
            
    print(f"[DOMAIN SHIELD VERDICT] Rủi ro: {domain_shield['risk_level']} | Quyết định: {domain_shield['verdict']} | Hành động: {domain_shield['action']}")
    if domain_shield.get('top_live_url'):
        print(f" -> URL MoMo hiện hữu: {domain_shield['top_live_url']}")

    if not serp_items:
        print("Không thể thu thập kết quả tìm kiếm đối thủ từ SERP. (Có thể do giới hạn kết nối hoặc bot block).")
        # Vẫn tạo phân tích cơ sở dựa trên Domain Shield
        analysis = {
            'query': query,
            'competitors_crawled': 0,
            'avg_word_count': 1800,
            'max_word_count': 2200,
            'recommended_target_words': 2200,
            'dominant_format': 'Interactive Utility Guide',
            'top_competitor_entities': [query],
            'gaps_detected': [
                "Cần tích hợp công cụ tính toán / tra cứu tương tác trực tiếp trên MoMo Web Platform.",
                "Cần nhúng Schema FAQPage và BreadcrumbList chuẩn Google Search Central.",
                "Cần xây dựng điểm chạm chuyển đổi Web-to-App MoMo liền mạch."
            ],
            'beating_outline': [
                f"## H2 1: Tổng quan & Định nghĩa chuẩn xác về {query}",
                f"## H2 2: Bảng so sánh chi tiết & Tiêu chí lựa chọn tối ưu nhất",
                f"## H2 3: Công cụ tính toán / Tra cứu trực tuyến trên Nền tảng Web MoMo",
                f"## H2 4: Hướng dẫn quy trình & Thủ tục thực hiện từng bước đơn giản",
                f"## H2 5: Giải đáp thắc mắc thường gặp (FAQs chuẩn Schema)",
                f"## H2 6: Giải pháp liên kết và nhận quyền lợi tối đa qua Ứng dụng MoMo"
            ],
            'keyword_extraction': {'engines': {}, 'table_stakes': [], 'differentiators': [],
                                   'top_keyphrases': [], 'entities': {}, 'per_page': []},
            'information_gain': {},
            'content_gap': {},
        }
        competitor_pages = []
    else:
        print(f"Đã phát hiện Top {len(serp_items)} đối thủ trên bảng xếp hạng.")
        
        # Bước 2: Cào sâu On-Page từng đối thủ
        competitor_pages = []
        for item in serp_items:
            page_data = CompetitorPageParser.parse_page(item)
            competitor_pages.append(page_data)
            time.sleep(0.5) # Giãn cách an toàn
            
        # Bước 2b: Cào nội dung trang MoMo hiện hữu (nếu có) để tính Content Gap
        momo_text = fetch_page_text(domain_shield.get('top_live_url'))

        # Bước 3: Phân tích khoảng trống nội dung & Chiến lược MoMo
        analysis = ContentGapAnalyzer.analyze_gap_and_strategy(
            query, competitor_pages, use_keybert=use_keybert, momo_text=momo_text
        )
    
    # Bước 4: Xuất báo cáo Markdown
    out_md = export_analysis_markdown(query, competitor_pages, analysis, domain_shield=domain_shield)
    
    # Bước 5: Lưu dữ liệu JSON (nếu có yêu cầu hoặc mặc định lưu SSOT)
    os.makedirs(DATA_DIR, exist_ok=True)
    slug = slugify(query)
    json_path = os.path.join(DATA_DIR, f"{slug}.json")
    
    top1 = None
    other_comps = []
    if competitor_pages:
        p1 = competitor_pages[0]
        top1 = {
            "domain": p1.get("domain", ""),
            "name": p1.get("domain", "").split(".")[0].title(),
            "real_url": p1.get("url", ""),
            "current_rank": p1.get("rank", 1),
            "page_title": p1.get("page_title") or p1.get("title", ""),
            "actual_word_count": p1.get("word_count", 0),
            "format_detected": p1.get("format_type", "Article Guide")
        }
        for p in competitor_pages[1:]:
            other_comps.append({
                "domain": p.get("domain", ""),
                "rank": p.get("rank", 0)
            })
    else:
        top1 = {
            "domain": "google.com.vn",
            "name": "Google SERP",
            "real_url": f"https://www.google.com/search?q={urllib.parse.quote(query)}",
            "current_rank": 1,
            "page_title": f"Kết quả tìm kiếm cho {query}",
            "actual_word_count": 1500,
            "format_detected": "Interactive Search Tool / Guide"
        }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'query': query,
            'usecase_id': slug,
            'generated_at': time.strftime('%Y-%m-%d %H:%M:%S'),
            'serp_realtime': {
                'top1_competitor': top1,
                'other_competitors': other_comps
            },
            'analysis': analysis,
            'domain_cannibalization_shield': domain_shield,
            'competitors': competitor_pages
        }, f, ensure_ascii=False, indent=2)
    print(f"Đã lưu Snapshot dữ liệu đối thủ tại: {json_path}")
    
    print("\n=== HOÀN TẤT PHÂN TÍCH ĐỐI THỦ SERP ===")

if __name__ == '__main__':
    main()
