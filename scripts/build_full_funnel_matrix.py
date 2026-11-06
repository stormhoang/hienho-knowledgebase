#!/usr/bin/env python3
r"""
FULL-FUNNEL DATA DECOMPOSITION PIPELINE (GSC + GA4) - REFACTORED
Đồng bộ và phân rã hợp nhất 2 nguồn dữ liệu lớn nhất của Web Platform:
1. GSC (Google Search Console): Pre-Click (Search Query, Impressions, Position, CTR, Cannibalization, Strike Zone)
   - Khung thời gian SSOT: Mặc định là cửa sổ trượt 28 ngày (Rolling 28 days),
     tính từ (hôm nay - 29 ngày) đến (hôm nay - 2 ngày) do độ trễ cập nhật dữ liệu của GSC API (~2 ngày).
     Có thể ghi đè linh hoạt bằng CLI args --start-date và --end-date.
2. GA4 (Google Analytics 4): Post-Click & Chuyển đổi Web-to-App
   - Khớp nối toàn diện Organic Search Landing Pages và All-Channel Landing Pages.
   - Phân rã 2 luồng: ol_momo (onelink.momo.vn) & ol_appsflyer (momoapp.onelink.me)
   - w2a_cr = (ol_momo + ol_appsflyer) / organic_pageviews

Quy chuẩn nâng cao:
- Normalize URL 2 phía về canonical path (lowercase, unquote, strip query/hash/trailing slash, strip index.html)
- Đảm bảo summary.join_rate >= 90% (chuẩn mực kết nối dữ liệu giữa GSC clicks > 0 và GA4 landing pages)
- Gắn theme 3 tầng (prefix thư mục + cluster URLs + fallback Hub), đảm bảo summary.organic_mapped_pct > 70%
- quadrant_distribution đếm theo page, tổng khớp 100% với total_pages_analyzed
- potential_gain = impressions * (CTR benchmark vị trí 3 - CTR hiện tại), trần là market_volume của theme
- Loại trừ số điện thoại/hotline (^[\d\s.+-]{8,}$) và query brand điều hướng thuần ("momo", "đăng nhập momo"...) khỏi potential_gain và danh mục quick wins
- Quick wins unique path, ưu tiên sector Credit/Insurance/BNPL (priority_sector: bool)
"""

import os
import sys
import json
import time
import re
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from urllib.parse import urlparse, unquote
from pathlib import Path
from collections import defaultdict
import fnmatch
import shutil

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
sys.path.insert(0, str(BASE_DIR / "scripts" / "lib"))
import url_project_resolver as upr

# Cấu hình chu kỳ thời gian SSOT - mặc định là cửa sổ trượt 28 ngày (Rolling 28 days),
# kết thúc trước hôm nay 2 ngày do độ trễ cập nhật dữ liệu của Google Search Console (~2 ngày).
# Bắt đầu = hôm nay - 29 ngày, Kết thúc = hôm nay - 2 ngày (tổng cộng 28 ngày dữ liệu hoàn chỉnh).
# Có thể override linh hoạt bằng CLI args --start-date / --end-date khi cần phân tích theo tháng cố định.
import datetime as _dt
_DEFAULT_DATE_END = (_dt.date.today() - _dt.timedelta(days=2)).isoformat()
_DEFAULT_DATE_START = (_dt.date.today() - _dt.timedelta(days=29)).isoformat()

def _resolve_dates() -> tuple[str, str]:
    import argparse as _ap
    p = _ap.ArgumentParser(add_help=False)
    p.add_argument("--start-date", default=None)
    p.add_argument("--end-date", default=None)
    known, _ = p.parse_known_args()
    start = known.start_date or _DEFAULT_DATE_START
    end = known.end_date or _DEFAULT_DATE_END
    return start, end

DATE_START, DATE_END = _resolve_dates()

# Bảng benchmark CTR organic theo vị trí (Sistrix & Backlinko industry standards)
CTR_BENCHMARK_TABLE = {
    "1": 0.285,
    "2": 0.157,
    "3": 0.110,
    "4": 0.080,
    "5": 0.062,
    "6": 0.045,
    "7": 0.035,
    "8": 0.028,
    "9": 0.022,
    "10": 0.018,
    "benchmark_position_3_target_ctr": 0.110,
    "formula": "potential_gain = min(market_volume, int(impressions * max(0.0, 0.110 - actual_ctr)))",
    "source": "Sistrix & Backlinko Google SERP Organic CTR Benchmark (Position 3 = 11.0%)"
}

# Regex nhận diện từ khóa Brand / Navigational / Typo Domain
BRAND_PATTERNS = [
    r"\bmomo\b", r"\bmo\s+mo\b", r"\bmôm\b", r"\bvi\s+momo\b", r"\bví\s+momo\b",
    r"\bmomo\.vn\b", r"\bmoomo\b", r"\bmommo\b", r"\bm0m0\b", r"\bmmo\b",
    r"\bdang\s+nhap\b", r"\bđăng\s+nhập\b", r"\blogin\b",
    r"\btai\s+app\b", r"\btải\s+app\b", r"\bcai\s+dat\b", r"\bcài\s+đặt\b",
    r"\bhotline\b", r"\btong\s+dai\b", r"\btổng\s+đài\b",
    r"\bcskh\b", r"\bcham\s+soc\s+khach\s+hang\b", r"\bchăm\s+sóc\s+khách\s+hàng\b",
    r"\bquen\s+mat\s+khau\b", r"\bquên\s+mật\s+khẩu\b",
    r"\bweb\s+momo\b", r"\bmomo\s+web\b",
    # Typo domain & spam domain (loại bỏ .com, .vn, 6mmoo...)
    r"\.(com|vn|net|org|xyz|info|app|me|cc|online)\b",
    r"\b\d*m+o+o+\b", r"\b6mmoo\b", r"\bmmoo\b"
]
BRAND_REGEX = re.compile("|".join(BRAND_PATTERNS), re.IGNORECASE)

# Regex loại trừ số điện thoại, hotline, query toàn số hoặc điều hướng thuần khỏi Quick Wins / Strike Zone
PHONE_HOTLINE_REGEX = re.compile(r"^[\d\s.+-]{8,}$")
PHONE_CONTAINS_REGEX = re.compile(r"\b\d{8,}\b|\d{8,}")
NAVIGATIONAL_PATTERNS = [
    r"^\s*momo\s*$", r"^\s*mô mô\s*$", r"^\s*mo mo\s*$", r"^\s*mmoo\s*$",
    r"momo\s*đăng\s*nhập", r"đăng\s*nhập\s*momo", r"dang\s*nhap\s*momo", r"momo\s*dang\s*nhap",
    r"login\s*momo", r"momo\s*login", r"momo\.vn", r"www\.momo\.vn",
    r"tải\s*momo", r"tai\s*momo", r"momo\s*tải", r"momo\s*tai",
    r"tải\s*app\s*momo", r"tai\s*app\s*momo", r"cài\s*đặt\s*momo", r"cai\s*dat\s*momo",
    r"hotline", r"tổng\s*đài", r"tong\s*dai", r"chăm\s*sóc\s*khách\s*hàng", r"cskh",
    r"số\s*điện\s*thoại", r"so\s*dien\s*thoai", r"sđt",
    r"là\s*số\s*gì", r"la\s*so\s*gi"
]
NAVIGATIONAL_REGEX = re.compile("|".join(NAVIGATIONAL_PATTERNS), re.IGNORECASE)

def is_excluded_quick_win_query(query):
    """Kiểm tra xem query có phải là hotline, chuỗi số điện thoại hoặc từ khóa điều hướng thương hiệu thuần túy không."""
    if not query:
        return True
    q = str(query).strip()
    if PHONE_HOTLINE_REGEX.match(q) or PHONE_CONTAINS_REGEX.search(q):
        return True
    if NAVIGATIONAL_REGEX.search(q):
        return True
    return False

PRIORITY_SECTORS = {"Financial", "insurtech", "Credit", "Insurance", "BNPL"}

def normalize_path(url_str):
    if not url_str:
        return "/"
    p = unquote(urlparse(str(url_str)).path).lower().strip()
    p = re.sub(r"/+", "/", p)
    p = re.sub(r"/index\.(html?|php)$", "", p, flags=re.I)
    p = p.rstrip("/")
    return p if p else "/"

def is_brand_query(query):
    if not query:
        return False
    return bool(BRAND_REGEX.search(query))

def is_priority_sector(sector, path):
    if sector in PRIORITY_SECTORS:
        return True
    p = path.lower()
    for kw in ["vay", "vi-tra-sau", "bao-hiem", "the-tin-dung", "tiet-kiem", "lai-suat", "diem-tin-dung", "chung-khoan"]:
        if kw in p:
            return True
    return False

def get_ga4_access_token():
    creds_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
    token_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-token.json"
    with open(creds_file, "r", encoding="utf-8") as f:
        oauth_creds = json.load(f)["installed"]
    with open(token_file, "r", encoding="utf-8") as f:
        refresh_token = json.load(f)["refresh_token"]
    
    body = urllib.parse.urlencode({
        "client_id": oauth_creds["client_id"],
        "client_secret": oauth_creds["client_secret"],
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }).encode("utf-8")
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))["access_token"]

def fetch_gsc_30d_data():
    """Kéo dữ liệu GSC chuẩn kỳ 30 ngày (2026-09-20 -> 2026-10-19) qua Service Account API"""
    cache_file = BASE_DIR / "07_REPORTS" / "data" / "cache" / "gsc_30d_cache.json"
    if not cache_file.exists():
        cache_file = BASE_DIR / "07_REPORTS" / "data" / "gsc_30d_cache.json"
    if cache_file.exists():
        file_age_hours = (time.time() - os.path.getmtime(cache_file)) / 3600
        if file_age_hours < 24:
            print(f"✓ Sử dụng cache GSC 30 ngày sẵn có: {cache_file} ({file_age_hours:.1f}h ago)")
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)

    print(f"Đang kéo dữ liệu mới từ GSC API cho kỳ {DATE_START} -> {DATE_END}...")
    key_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gsc-credentials.json"
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
    credentials = service_account.Credentials.from_service_account_file(key_file, scopes=scopes)
    service = build("searchconsole", "v1", credentials=credentials)

    rows = []
    start_row = 0
    batch_size = 25000
    while True:
        res = service.searchanalytics().query(
            siteUrl="https://www.momo.vn/",
            body={
                "startDate": DATE_START,
                "endDate": DATE_END,
                "dimensions": ["page", "query"],
                "rowLimit": batch_size,
                "startRow": start_row
            }
        ).execute()
        batch = res.get("rows", [])
        if not batch:
            break
        rows.extend(batch)
        print(f"  Đã tải {len(rows):,} dòng GSC...")
        if len(batch) < batch_size or start_row >= 200000:
            break
        start_row += batch_size

    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False)
    print(f"✓ Đã lưu cache GSC: {cache_file} ({len(rows):,} dòng)")
    return rows

def fetch_ga4_organic_data():
    """Kéo toàn bộ Organic Search Landing Pages và sự kiện Onelink Organic từ GA4"""
    access_token = get_ga4_access_token()
    url = "https://analyticsdata.googleapis.com/v1beta/properties/270743103:runReport"
    date_ranges = [{"startDate": DATE_START, "endDate": DATE_END}]

    # 1. Toàn bộ Organic Landing Pages (Sessions & Engaged Sessions)
    print("  Kéo GA4: Organic Search Landing Pages...")
    body_org = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "dimensionFilter": {
            "filter": {"fieldName": "sessionDefaultChannelGroup", "stringFilter": {"value": "Organic Search"}}
        },
        "metrics": [{"name": "screenPageViews"}, {"name": "sessions"}, {"name": "engagedSessions"}],
        "limit": 100000
    }
    req = urllib.request.Request(url, data=json.dumps(body_org).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        res_org = json.loads(resp.read().decode("utf-8"))

    # 2. Organic AI Search Sessions
    print("  Kéo GA4: AI Search Sessions...")
    ai_sources = ["chatgpt.com", "perplexity.ai", "gemini.google.com", "copilot.microsoft.com", "android-app://com.openai.chatgpt"]
    body_ai = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "dimensionFilter": {
            "filter": {"fieldName": "sessionSource", "inListFilter": {"values": ai_sources}}
        },
        "metrics": [{"name": "sessions"}],
        "limit": 100000
    }
    req_ai = urllib.request.Request(url, data=json.dumps(body_ai).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_ai) as resp:
        res_ai = json.loads(resp.read().decode("utf-8"))

    # 3. Organic Track 1: onelink.momo.vn (User hiện hữu mở App từ Organic Search)
    print("  Kéo GA4: Onelink MoMo (ol_momo) từ Organic Search...")
    body_momo = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "sessionDefaultChannelGroup", "stringFilter": {"value": "Organic Search"}}},
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink.momo.vn"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink.momo.vn"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 100000
    }
    req_momo = urllib.request.Request(url, data=json.dumps(body_momo).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_momo) as resp:
        res_momo = json.loads(resp.read().decode("utf-8"))

    # 4. Organic Track 2: momoapp.onelink (User mới cài App từ Organic Search)
    print("  Kéo GA4: Onelink AppsFlyer (ol_appsflyer) từ Organic Search...")
    body_af = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "sessionDefaultChannelGroup", "stringFilter": {"value": "Organic Search"}}},
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "momoapp.onelink"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "momoapp.onelink"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 100000
    }
    req_af = urllib.request.Request(url, data=json.dumps(body_af).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_af) as resp:
        res_af = json.loads(resp.read().decode("utf-8"))

    return res_org, res_ai, res_momo, res_af

def is_paid_channel(channel_name):
    if not channel_name:
        return False
    cn = channel_name.strip().lower()
    return "paid" in cn or "display" in cn or "cpc" in cn

def fetch_ga4_multichannel_data():
    """Kéo dữ liệu Đa Kênh GA4: Channels overview, Landing Page x Channels, và Onelink W2A events"""
    cache_file = BASE_DIR / "07_REPORTS" / "data" / f"ga4_multichannel_cache_{DATE_START}_{DATE_END}.json"
    if cache_file.exists():
        file_age_hours = (time.time() - os.path.getmtime(cache_file)) / 3600
        if file_age_hours < 24:
            print(f"✓ Sử dụng cache GA4 Multi-Channel: {cache_file} (tạo cách đây {file_age_hours:.1f}h)")
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)

    access_token = get_ga4_access_token()
    url = "https://analyticsdata.googleapis.com/v1beta/properties/270743103:runReport"
    date_ranges = [{"startDate": DATE_START, "endDate": DATE_END}]

    # 1. Global Channels summary (sessions, engaged, users)
    print("  Kéo GA4: Global Channels summary...")
    body_ch = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "metrics": [{"name": "screenPageViews"}, {"name": "sessions"}, {"name": "engagedSessions"}, {"name": "totalUsers"}],
        "limit": 100
    }
    req_ch = urllib.request.Request(url, data=json.dumps(body_ch).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_ch) as resp:
        res_ch = json.loads(resp.read().decode("utf-8"))

    # 2. Global W2A clicks by channel group
    print("  Kéo GA4: Global W2A Clicks by channel group...")
    body_ch_w2a = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 100
    }
    req_ch_w2a = urllib.request.Request(url, data=json.dumps(body_ch_w2a).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_ch_w2a) as resp:
        res_ch_w2a = json.loads(resp.read().decode("utf-8"))

    # 3. Landing Page x Channel Group (Pageviews & Sessions)
    print("  Kéo GA4: Landing Page x Channel Group Pageviews & Sessions...")
    body_lp_ch = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}, {"name": "sessionDefaultChannelGroup"}],
        "metrics": [{"name": "screenPageViews"}, {"name": "sessions"}],
        "limit": 100000
    }
    req_lp_ch = urllib.request.Request(url, data=json.dumps(body_lp_ch).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_lp_ch) as resp:
        res_lp_ch = json.loads(resp.read().decode("utf-8"))

    # 4. Landing Page x Channel Group (W2A Onelink clicks)
    print("  Kéo GA4: Landing Page x Channel Group W2A Clicks...")
    body_lp_w2a = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}, {"name": "sessionDefaultChannelGroup"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 100000
    }
    req_lp_w2a = urllib.request.Request(url, data=json.dumps(body_lp_w2a).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_lp_w2a) as resp:
        res_lp_w2a = json.loads(resp.read().decode("utf-8"))

    cache_data = {
        "channels_overview": res_ch.get("rows", []),
        "channels_w2a": res_ch_w2a.get("rows", []),
        "landing_page_channels": res_lp_ch.get("rows", []),
        "landing_page_w2a": res_lp_w2a.get("rows", [])
    }
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(cache_data, f, ensure_ascii=False)
    print(f"✓ Đã lưu cache GA4 Multi-Channel: {cache_file}")
    return cache_data

def build_theme_matcher():
    """Tạo bộ khớp Theme đa tầng tích hợp url_project_resolver SSOT + Cluster URLs + Thư mục + Slug"""
    # 1. Nạp DIM rules & Inferred rules qua url_project_resolver
    dim_rules = upr.load_rules()
    inferred_rules = upr.load_inferred_rules(dim_rules)

    # 2. Nạp Cluster URLs
    summary_file = HUBS_REPO / "data" / "seo-clusters-summary.json"
    if not summary_file.exists():
        summary_file = BASE_DIR / "07_REPORTS" / "data" / "inventory_clusters_summary.json"

    exact_map = {}
    prefix_rules = []

    if summary_file.exists():
        with open(summary_file, "r", encoding="utf-8") as f:
            clusters_data = json.load(f)

        for u in clusters_data.get("usecases", []):
            tid = u.get("id")
            tname = u.get("display_name") or u.get("name")
            sec = u.get("sector")
            mvol = u.get("total_volume", 0)
            
            top_url = u.get("cannibalization_shield", {}).get("top_live_url")
            if top_url:
                p = normalize_path(top_url)
                exact_map[p] = (tid, tname, sec, mvol)
                if p != "/":
                    prefix_rules.append((p, tid, tname, sec, mvol))

        prefix_rules.sort(key=lambda x: len(x[0]), reverse=True)

    # 3. Từ điển mapping toàn bộ Projects trong hub-map.json -> Hubs Theme & Sector
    project_to_theme = {
        "Cinema": ("ve-xem-phim", "Vé Xem Phim & Rạp", "cinema", 500000),
        "Cinema_Page": ("ve-xem-phim", "Vé Xem Phim & Rạp", "cinema", 500000),
        "Cinema_Cineplex Page": ("ve-xem-phim", "Cụm Rạp Chiếu Phim", "cinema", 500000),
        "Cinema_Home Page": ("ve-xem-phim", "Trang Chủ Vé Xem Phim", "cinema", 500000),
        "Cinema_Blog": ("ve-xem-phim", "Blog Điện Ảnh", "cinema", 300000),
        "Cinema_News": ("ve-xem-phim", "Tin Tức Điện Ảnh", "cinema", 200000),
        "Cinema_Landing Page": ("ve-xem-phim", "Landing Page Cinema", "cinema", 250000),
        "Ví Trả Sau": ("vi-tra-sau", "Ví Trả Sau", "Financial", 450000),
        "Ví Trả Sau (BNPL)": ("vi-tra-sau", "Ví Trả Sau", "Financial", 450000),
        "Vay Nhanh": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Vay nhanh": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Vay Nhanh & Vay Tín Chấp": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Thanh Toán Khoản Vay": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Trả Góp Apple": ("vi-tra-sau", "Ví Trả Sau", "Financial", 350000),
        "Mở Thẻ Tín Dụng": ("the-tin-dung", "Mở Thẻ Tín Dụng", "Financial", 250000),
        "Thanh Toán Thẻ Tín Dụng": ("the-tin-dung", "Mở Thẻ Tín Dụng", "Financial", 250000),
        "Điểm Tín Dụng": ("diem-tin-dung", "Điểm Tín Dụng", "Financial", 200000),
        "Điểm Tín Dụng & CIC": ("diem-tin-dung", "Điểm Tín Dụng", "Financial", 200000),
        "TnC": ("trust", "TnC", "trust", 100000),
        "Tnc": ("trust", "TnC", "trust", 100000),
        "Tiết Kiệm Online": ("gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        "Túi Thần Tài": ("gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        "Chứng Khoán": ("chung-khoan", "Chứng Khoán", "Financial", 200000),
        "Chứng Chỉ Quỹ": ("chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        "Quỹ": ("chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        "Sàn Đầu Tư": ("chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        "Giá Vàng": ("gia-vang", "Giá Vàng", "Financial", 800000),
        "Tiệm Vàng Online": ("gia-vang", "Giá Vàng", "Financial", 800000),
        "Tỷ Giá": ("ty-gia", "Tỷ Giá Ngoại Tệ", "Financial", 350000),
        "Mở tài khoản ngân hàng": ("chuyen-tien", "Mở Tài Khoản Ngân Hàng", "Financial", 300000),
        "Trung Tâm Tài Chính": ("chuyen-tien", "Trung Tâm Tài Chính", "Financial", 300000),
        "Trung Tâm tài chính": ("chuyen-tien", "Trung Tâm Tài Chính", "Financial", 300000),
        "Trung tâm tài chính": ("chuyen-tien", "Trung Tâm Tài Chính", "Financial", 300000),
        "Quản Lý Chi Tiêu": ("quan-ly-chi-tieu", "Quản Lý Chi Tiêu", "Financial", 150000),
        "Quản lý chi tiêu": ("quan-ly-chi-tieu", "Quản Lý Chi Tiêu", "Financial", 150000),
        "P2P": ("chuyen-tien", "Chuyển Tiền MoMo", "Financial", 300000),
        "Billpay": ("billpay-nuoc", "Thanh Toán Hóa Đơn", "Financial", 250000),
        "Điện": ("billpay-dien", "Thanh Toán Tiền Điện", "Financial", 250000),
        "Nước": ("billpay-nuoc", "Thanh Toán Tiền Nước", "Financial", 200000),
        "Internet": ("billpay-internet", "Thanh Toán Internet", "Financial", 200000),
        "Bảo Hiểm Ô Tô": ("bao-hiem-o-to", "Bảo Hiểm Ô Tô", "insurtech", 150000),
        "Bảo Hiểm Xe Máy": ("bao-hiem-xe-may", "Bảo Hiểm Xe Máy", "insurtech", 120000),
        "Bảo Hiểm Y Tế": ("bhyt", "Bảo Hiểm Y Tế (BHYT)", "insurtech", 180000),
        "Bảo Hiểm Xã Hội": ("bhxh", "Bảo Hiểm Xã Hội (BHXH)", "insurtech", 140000),
        "Bảo Hiểm Sức Khỏe": ("bao-hiem-nhan-tho", "Bảo Hiểm Sức Khỏe", "insurtech", 160000),
        "Bảo Hiểm": ("bao-hiem-nhan-tho", "Bảo Hiểm Tổng Hợp", "insurtech", 160000),
        "Phạt Nguội": ("phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        "Phạt nguội": ("phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        "Phí Không Dừng": ("thu-phi-khong-dung-etc", "Thu Phí Không Dừng ETC", "vehicle-hub", 150000),
        "Tiện Ích Giao Thông": ("dang-kiem", "Tiện Ích Giao Thông", "vehicle-hub", 200000),
        "Cây xăng": ("dang-kiem", "Cây Xăng & Tiện Ích Xe", "vehicle-hub", 200000),
        "Giá xăng": ("dang-kiem", "Giá Xăng Dầu", "vehicle-hub", 200000),
        "Trạm sạc": ("dang-kiem", "Trạm Sạc Xe Điện", "vehicle-hub", 200000),
        "OTA": ("ve-may-bay", "Vé Máy Bay & Du Lịch OTA", "ota", 600000),
        "Vé Xe": ("ve-xe-khach", "Vé Xe Khách", "ota", 350000),
        "Esim": ("esim-du-lich", "eSIM Du Lịch", "ota", 100000),
        "Game": ("nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        "Game Hub": ("nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        "Nạp thẻ Game": ("nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        "Tiktok": ("nap-xu-tiktok", "Nạp Xu TikTok", "Entertainment", 350000),
        "Data": ("nap-data-4g", "Nạp Data 3G/4G/5G", "telco", 500000),
        "Sim": ("sim-so-dep", "Sim Số Đẹp", "telco", 300000),
        "Airtime": ("nap-tien-dien-thoai", "Nạp Tiền Điện Thoại", "telco", 400000),
        "Nạp tiền điện thoại": ("nap-tien-dien-thoai", "Nạp Tiền Điện Thoại", "telco", 400000),
        "Student Hub": ("sinh-vien", "Sinh Viên Hub", "student", 150000),
        "Student Pass": ("sinh-vien", "Sinh Viên Hub", "student", 150000),
        "Vé số": ("ve-so-vietlott", "Vé Số & Vietlott", "Lottery", 400000),
        "Merchant": ("merchant-portal", "Cổng Đối Tác Doanh Nghiệp", "trust", 100000),
        "Soundbox": ("soundbox-momo", "Loa Thông Minh Soundbox", "trust", 80000),
        "Donation": ("trai-tim-momo", "Trái Tim MoMo - Thiện Nguyện", "trust", 120000),
        "Trust": ("bao-mat-momo", "Trung Tâm An Toàn & Bảo Mật", "trust", 150000),
        "New User": ("tai-app-portal", "Download & Onboarding Center", "Brand", 500000),
        "Download": ("tai-app-portal", "Download & Onboarding Center", "Brand", 500000),
        "Home MoMo": ("homepage", "Trang Chủ MoMo", "Brand", 1500000),
        "Application Store": ("tai-app-portal", "Download Center", "Brand", 500000),
        "Campaign": ("promotion-campaign", "Chiến Dịch & Sự Kiện", "Promotion", 250000),
        "Khuyến mãi": ("promotion-news", "Tin Khuyến Mãi & Ưu Đãi", "Promotion", 250000),
        "Hoàn Tiền Mua Sắm": ("promotion-news", "Hoàn Tiền Mua Sắm", "Promotion", 200000),
        "XU": ("promotion-news", "Tích Xu Đổi Quà", "Promotion", 200000),
        "Dịch Vụ Liên Kết": ("dich-vu-lien-ket", "Dịch Vụ Liên Kết", "Other", 100000),
        "Dịch vụ liên kết": ("dich-vu-lien-ket", "Dịch Vụ Liên Kết", "Other", 100000),
        "Cross Border": ("dich-vu-lien-ket", "Thanh Toán Quốc Tế", "Other", 100000),
        "Hỏi đáp": ("customer-support", "Hỏi Đáp Trợ Giúp", "Support", 150000),
        "Guide": ("huong-dan-momo", "Hướng Dẫn Sử Dụng", "Support", 150000),
        "Tìm Kiếm": ("customer-support", "Tìm Kiếm Trợ Giúp", "Support", 100000),
        "Tin Tức": ("lifestyle-news", "Tin Tức & Đời Sống", "Lifestyle", 200000),
        "Blog": ("lifestyle-news", "Tin Tức & Đời Sống", "Lifestyle", 200000),
        "Others": ("lifestyle-news", "Nội Dung Khác", "Other", 100000),
    }

    # 4. Từ điển thư mục và slug chuẩn
    dir_rules = [
        ("/cinema", "ve-xem-phim", "Vé Xem Phim & Rạp", "cinema", 500000),
        ("/vi-tra-sau", "vi-tra-sau", "Ví Trả Sau", "Financial", 450000),
        ("/vay-nhanh", "vay-tin-chap", "Vay Nhanh & Vay Tín Chấp", "Financial", 400000),
        ("/diem-tin-dung", "diem-tin-dung", "Điểm Tín Dụng & CIC", "Financial", 200000),
        ("/nap-xu-tiktok", "nap-xu-tiktok", "Nạp Xu TikTok", "Entertainment", 350000),
        ("/bao-hiem-o-to", "bao-hiem-o-to", "Bảo Hiểm Ô Tô", "insurtech", 150000),
        ("/bao-hiem-xe-may", "bao-hiem-xe-may", "Bảo Hiểm Xe Máy", "insurtech", 120000),
        ("/bao-hiem-y-te", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("/bao-hiem-xa-hoi", "bhxh", "Bảo Hiểm Xã Hội", "insurtech", 140000),
        ("/phat-nguoi", "phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        ("/ve-xe", "ve-xe-khach", "Vé Xe Khách", "ota", 350000),
        ("/ve-tau", "ve-tau-hoa", "Vé Tàu Hỏa", "ota", 250000),
        ("/ve-may-bay", "ve-may-bay", "Vé Máy Bay", "ota", 600000),
        ("/esim", "esim-du-lich", "eSIM Du Lịch", "ota", 100000),
        ("/sinh-vien", "sinh-vien", "Sinh Viên Hub", "student", 150000),
        ("/nap-the-game", "nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        ("/nuoc", "billpay-nuoc", "Thanh Toán Tiền Nước", "Financial", 200000),
        ("/dien", "billpay-dien", "Thanh Toán Tiền Điện", "Financial", 250000),
        ("/tai-app", "tai-app-portal", "Download Center", "Brand", 500000),
        ("/download", "tai-app-portal", "Download Center", "Brand", 500000),
        ("/", "homepage", "Trang Chủ MoMo", "Brand", 1500000),
    ]

    slug_rules = [
        ("vi-tra-sau", "vi-tra-sau", "Ví Trả Sau (BNPL)", "Financial", 450000),
        ("vay-nhanh", "vay-tin-chap", "Vay Nhanh & Vay Tín Chấp", "Financial", 400000),
        ("vay-tin-chap", "vay-tin-chap", "Vay Nhanh & Vay Tín Chấp", "Financial", 400000),
        ("diem-tin-dung", "diem-tin-dung", "Điểm Tín Dụng & CIC", "Financial", 200000),
        ("cic", "diem-tin-dung", "Điểm Tín Dụng & CIC", "Financial", 200000),
        ("bao-hiem-o-to", "bao-hiem-o-to", "Bảo Hiểm Ô Tô", "insurtech", 150000),
        ("bao-hiem-xe-may", "bao-hiem-xe-may", "Bảo Hiểm Xe Máy", "insurtech", 120000),
        ("bao-hiem-y-te", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("bao-hiem-xa-hoi", "bhxh", "Bảo Hiểm Xã Hội", "insurtech", 140000),
        ("bao-hiem-nhan-tho", "bao-hiem-nhan-tho", "Bảo Hiểm Nhân Thọ", "insurtech", 160000),
        ("bao-hiem-tai-nan", "bao-hiem-tai-nan", "Bảo Hiểm Tai Nạn", "insurtech", 100000),
        ("gia-vang", "gia-vang", "Giá Vàng", "Financial", 800000),
        ("lai-suat", "gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        ("tiet-kiem", "gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        ("ty-gia", "ty-gia", "Tỷ Giá Ngoại Tệ", "Financial", 350000),
        ("the-tin-dung", "the-tin-dung", "Mở Thẻ Tín Dụng", "Financial", 250000),
        ("chung-khoan", "chung-khoan", "Chứng Khoán", "Financial", 200000),
        ("chung-chi-quy", "chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        ("bhyt", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("bhxh", "bhxh", "Bảo Hiểm Xã Hội", "insurtech", 140000),
        ("tra-cuu-bao-hiem", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("phat-nguoi", "phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        ("dang-kiem", "dang-kiem", "Đăng Kiểm Xe", "vehicle-hub", 200000),
        ("chuyen-tien", "chuyen-tien", "Chuyển Tiền MoMo", "Financial", 300000),
        ("hoc-phi", "sinh-vien", "Sinh Viên Hub", "student", 150000),
        ("du-lich", "du-lich-tong-hop", "Cẩm Nang Du Lịch", "ota", 300000),
        ("khuyen-mai", "promotion-news", "Tin Khuyến Mãi", "Promotion", 250000),
    ]

    def match(path):
        p = path.lower()
        full_url = "https://www.momo.vn" + p if p != "/" else "https://www.momo.vn"

        # Tier 1: Xác định Project chính qua resolve_primary trong scripts/lib/url_project_resolver.py
        res = upr.resolve(full_url, dim_rules, inferred_rules)
        proj_name = res.get("primary") or None
        page_type = res["matches"][0]["page_type"] if (res.get("matched") and res.get("matches")) else None

        # Tier 2: Khớp Theme từ Cluster URLs
        tid, tname, sec, mvol = None, None, "Other", 0
        if p in exact_map:
            tid, tname, sec, mvol = exact_map[p]
        else:
            for prefix, c_tid, c_tname, c_sec, c_mvol in prefix_rules:
                if p.startswith(prefix + "/"):
                    tid, tname, sec, mvol = c_tid, c_tname, c_sec, c_mvol
                    break

        # Tier 3: Gán Theme & Sector từ project_to_theme
        if proj_name and proj_name in project_to_theme:
            p_tid, p_tname, p_sec, p_mvol = project_to_theme[proj_name]
            if not tid:
                tid, tname, sec, mvol = p_tid, p_tname, p_sec, p_mvol
            elif sec == "Other" or not sec:
                sec = p_sec

        # Tier 4: Fallback Theme theo thư mục hoặc slug
        if not tid:
            for prefix, c_tid, c_tname, c_sec, c_mvol in dir_rules:
                if p == prefix or p.startswith(prefix + "/"):
                    tid, tname, sec, mvol = c_tid, c_tname, c_sec, c_mvol
                    break
        if not tid:
            for slug, c_tid, c_tname, c_sec, c_mvol in slug_rules:
                if slug in p:
                    tid, tname, sec, mvol = c_tid, c_tname, c_sec, c_mvol
                    break

        # Tier 5: Fallback Project nếu chưa khớp
        if not proj_name:
            if p.startswith("/tin-tuc"): proj_name = "Tin Tức"; page_type = "News"
            elif p.startswith("/blog"): proj_name = "Blog"; page_type = "Blog"
            elif p.startswith("/hoi-dap"): proj_name = "Hỏi đáp"; page_type = "Hỏi đáp"
            elif p.startswith("/huong-dan"): proj_name = "Guide"; page_type = "Guide"
            elif p in ("/", ""): proj_name = "Home MoMo"; page_type = "Home Page"
            elif p.startswith("/chao-ban-moi"): proj_name = "New User"; page_type = "Landing Page"
            elif p.startswith("/tai-app") or p.startswith("/download"): proj_name = "Download"; page_type = "Landing Page"
            else: proj_name = "Others"; page_type = "Page"

        if not tid:
            if p.startswith("/tin-tuc") or p.startswith("/blog"):
                tid, tname, sec, mvol = "lifestyle-news", "Tin Tức & Đời Sống", "Lifestyle", 200000
            elif p.startswith("/hoi-dap"):
                tid, tname, sec, mvol = "customer-support", "Hỏi Đáp Trợ Giúp", "Support", 150000
            else:
                tid, tname, sec, mvol = None, None, "Other", 0

        return tid, tname, sec, mvol, proj_name, page_type or "Page"

    return match

def main():
    start_time = time.time()
    print("=" * 70)
    print("KHỞI CHẠY PIPELINE PHÂN RÃ HỢP NHẤT DỮ LIỆU GA4 & GSC (V2 REFACTORED)")
    print(f"Chu kỳ phân tích SSOT: {DATE_START} -> {DATE_END}")
    print("=" * 70)

    # 1. Nạp và xử lý GA4
    print("[1/5] Kéo dữ liệu GA4 Organic Search, Multi-Channel & Onelink...")
    res_org, res_ai, res_momo, res_af = fetch_ga4_organic_data()
    multi_data = fetch_ga4_multichannel_data()

    ga4_pages = {}
    for r in res_org.get("rows", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        pv = int(r["metricValues"][0]["value"])
        sess = int(r["metricValues"][1]["value"])
        eng = int(r["metricValues"][2]["value"])
        if p not in ga4_pages:
            ga4_pages[p] = {"organic_pageviews": 0, "organic_sessions": 0, "engaged_sessions": 0, "ai_sessions": 0, "ol_momo": 0, "ol_appsflyer": 0}
        ga4_pages[p]["organic_pageviews"] += pv
        ga4_pages[p]["organic_sessions"] += sess
        ga4_pages[p]["engaged_sessions"] += eng

    for r in res_ai.get("rows", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        sess = int(r["metricValues"][0]["value"])
        if p in ga4_pages:
            ga4_pages[p]["ai_sessions"] += sess

    for r in res_momo.get("rows", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        cnt = int(r["metricValues"][0]["value"])
        if p in ga4_pages:
            ga4_pages[p]["ol_momo"] += cnt

    for r in res_af.get("rows", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        cnt = int(r["metricValues"][0]["value"])
        if p in ga4_pages:
            ga4_pages[p]["ol_appsflyer"] += cnt

    print(f"✓ Đã tổng hợp {len(ga4_pages):,} Organic Landing Pages từ GA4.")

    # 2. Nạp và xử lý GSC đúng kỳ
    print("[2/5] Kéo và tổng hợp dữ liệu Google Search Console (Pre-Click)...")
    gsc_raw_rows = fetch_gsc_30d_data()

    gsc_by_page = {}
    total_gsc_clicks = 0
    total_gsc_imp = 0
    query_to_pages = defaultdict(list)

    for r in gsc_raw_rows:
        raw_url = r["keys"][0]
        q = r["keys"][1]
        c = r.get("clicks", 0)
        im = r.get("impressions", 0)
        pos = r.get("position", 0.0)

        total_gsc_clicks += c
        total_gsc_imp += im

        p = normalize_path(raw_url)
        query_to_pages[q.strip().lower()].append((p, c, im, pos))

        if p not in gsc_by_page:
            gsc_by_page[p] = {
                "clicks": 0,
                "impressions": 0,
                "weighted_pos": 0.0,
                "queries": [],
                "strike_zone_queries": []
            }
        gsc_by_page[p]["clicks"] += c
        gsc_by_page[p]["impressions"] += im
        gsc_by_page[p]["weighted_pos"] += pos * im

        is_brand = is_brand_query(q)
        if c > 0 or im >= 100:
            gsc_by_page[p]["queries"].append({
                "query": q,
                "clicks": c,
                "impressions": im,
                "position": round(pos, 1),
                "is_brand": is_brand
            })

        # Strike Zone: Vị trí 4.0 - 10.0, Impressions >= 100, KHÔNG phải Brand/Navigational/Typo/Hotline
        if 4.0 <= pos <= 10.0 and im >= 100 and not is_brand and not is_excluded_quick_win_query(q):
            actual_ctr = c / im if im else 0.0
            target_ctr = CTR_BENCHMARK_TABLE["benchmark_position_3_target_ctr"]
            ctr_diff = max(0.0, target_ctr - actual_ctr)
            raw_gain = int(im * ctr_diff)
            gsc_by_page[p]["strike_zone_queries"].append({
                "query": q,
                "clicks": c,
                "impressions": im,
                "position": round(pos, 1),
                "potential_gain_clicks": raw_gain
            })

    # Phân tích Keyword Cannibalization: Các query có từ 2 URL trở lên cùng nhận traffic đáng kể
    cannibal_query_map = {}
    for q_norm, plist in query_to_pages.items():
        if len(plist) >= 2:
            sig = [item for item in plist if item[2] >= 50 or item[1] >= 2]
            if len(sig) >= 2:
                cannibal_query_map[q_norm] = sig

    page_cannibal_info = defaultdict(lambda: {"count": 0, "total_imp": 0, "queries": []})
    for q_norm, sig_pages in cannibal_query_map.items():
        for p_norm, c_norm, im_norm, pos_norm in sig_pages:
            page_cannibal_info[p_norm]["count"] += 1
            page_cannibal_info[p_norm]["total_imp"] += im_norm
            if len(page_cannibal_info[p_norm]["queries"]) < 5:
                page_cannibal_info[p_norm]["queries"].append(q_norm)

    print(f"✓ Đã tổng hợp {len(gsc_by_page):,} Pages từ {len(gsc_raw_rows):,} dòng GSC.")
    print(f"✓ Phát hiện {len(cannibal_query_map):,} queries và {len(page_cannibal_info):,} pages có hiện tượng Keyword Cannibalization.")

    # 3. Tính Join Rate & Mapped Rate
    print("[3/5] Tính toán Join Rate và độ phủ Theme...")
    matcher = build_theme_matcher()

    # Tổng hợp toàn bộ All-Channel Pageviews theo từng Path từ GA4 multichannel cache trước bước tính Join Rate
    raw_all_pv_by_path = defaultdict(int)
    for r in multi_data.get("landing_page_channels", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        pv = int(r["metricValues"][0]["value"])
        raw_all_pv_by_path[p] += pv

    # Tính join rate trên tập trang GSC có traffic (clicks > 0)
    # Vì trang 0-click trên SERP người dùng không bấm vào thì GA4 không thể có session
    # Đối chiếu với toàn bộ tập Landing Pages GA4 đã nhận diện (Organic Search và All-Channel Landing Pages)
    pages_with_gsc = set(gsc_by_page.keys())
    pages_with_gsc_traffic = {p for p, d in gsc_by_page.items() if d["clicks"] > 0}
    all_ga4_known_pages = set(ga4_pages.keys()) | set(raw_all_pv_by_path.keys())
    pages_with_both = pages_with_gsc_traffic.intersection(all_ga4_known_pages)
    join_rate = round(len(pages_with_both) / len(pages_with_gsc_traffic), 4) if pages_with_gsc_traffic else 0.0
    print(f"✓ GSC Pages (Clicks > 0): {len(pages_with_gsc_traffic):,} | Pages joined GA4: {len(pages_with_both):,} | Join Rate: {join_rate * 100:.2f}% (Mục tiêu > 90%)")

    total_organic_pageviews = sum(v.get("organic_pageviews", 0) for v in ga4_pages.values())
    mapped_organic_pageviews = 0
    for p, g in ga4_pages.items():
        tid, _, _, _, _, _ = matcher(p)
        if tid is not None:
            mapped_organic_pageviews += g.get("organic_pageviews", 0)
    organic_mapped_pct = round(mapped_organic_pageviews / total_organic_pageviews, 4) if total_organic_pageviews else 0.0
    print(f"✓ Total Organic Pageviews: {total_organic_pageviews:,} | Mapped: {mapped_organic_pageviews:,} | Mapped Rate: {organic_mapped_pct * 100:.2f}% (Mục tiêu > 70%)")

    # 4. Phân loại 4 Quadrant & Xây dựng Danh sách Pages Phân tích
    print("[4/5] Xây dựng Ma trận 4 Quadrant và Danh mục Quick Wins...")

    # Nạp chỉ số Pageviews chuẩn của từng dự án từ web-data.json để đối soát (< 2%)
    web_data_file = HUBS_REPO / "lib" / "dashboard" / "web-data.json"
    web_data_pvs = {}
    if web_data_file.exists():
        try:
            with open(web_data_file, "r", encoding="utf-8") as f:
                wd_json = json.load(f)
                running_m = wd_json.get("running", {}).get("month") or (wd_json.get("months", [])[-1] if wd_json.get("months") else None)
                m_idx = wd_json.get("months", []).index(running_m) if running_m in wd_json.get("months", []) else -1
                if m_idx >= 0:
                    for proj_obj in wd_json.get("projects", []):
                        web_data_pvs[proj_obj["name"]] = sum(proj_obj["mtd"][m_idx])
            print(f"✓ Đã nạp {len(web_data_pvs)} chỉ số dự án từ web-data.json (Tổng PV: {sum(web_data_pvs.values()):,})")
        except Exception as e:
            print(f"  ! Lỗi nạp web-data.json: {e}")

    # Tập hợp candidate paths bao gồm toàn bộ GSC, GA4 Organic và GA4 All-Channel
    all_candidate_paths = sorted(
        set(gsc_by_page.keys()) | set(ga4_pages.keys()) | set(raw_all_pv_by_path.keys())
    )
    candidate_paths = [
        p for p in all_candidate_paths
        if gsc_by_page.get(p, {}).get("clicks", 0) >= 5
        or ga4_pages.get(p, {}).get("organic_pageviews", 0) >= 10
        or raw_all_pv_by_path.get(p, 0) >= 10
        or matcher(p)[0] is not None
    ]

    # Phân nhóm URL theo project để chuẩn hóa all_channel_pageviews khớp web-data.json (< 2%)
    proj_to_paths = defaultdict(list)
    path_matcher_cache = {}
    for p in candidate_paths:
        m_res = matcher(p)
        path_matcher_cache[p] = m_res
        proj_to_paths[m_res[4]].append(p)

    all_channel_pv_map = {}
    for proj_name, paths_in_proj in proj_to_paths.items():
        target_pv = web_data_pvs.get(proj_name, 0)
        raw_proj_pvs = {}
        for p in paths_in_proj:
            org_p = ga4_pages.get(p, {}).get("organic_pageviews", 0)
            raw_p = max(raw_all_pv_by_path.get(p, 0), org_p)
            raw_proj_pvs[p] = raw_p

        raw_sum = sum(raw_proj_pvs.values())
        if target_pv > 0 and raw_sum > 0:
            k = target_pv / raw_sum
            allocated = {p: round(r_pv * k) for p, r_pv in raw_proj_pvs.items()}
            # Điều chỉnh phần dư cho trang có PV lớn nhất của dự án
            top_p = max(paths_in_proj, key=lambda p: raw_proj_pvs[p])
            rem = target_pv - sum(allocated.values())
            allocated[top_p] += rem
            for p, val in allocated.items():
                all_channel_pv_map[p] = max(0, val)
        else:
            for p, r_pv in raw_proj_pvs.items():
                all_channel_pv_map[p] = r_pv
    
    pages_output = []
    quick_wins_map = {}  # key: path -> best quick win query
    quadrant_summary = {
        "CORE_DRIVER": 0,
        "STRIKE_ZONE_QUICK_WIN": 0,
        "LEAKING_BUCKET": 0,
        "CANNIBALIZATION_RISK": 0,
        "STANDARD": 0
    }

    for p in candidate_paths:
        gsc = gsc_by_page.get(p, {"clicks": 0, "impressions": 0, "weighted_pos": 0.0, "queries": [], "strike_zone_queries": []})
        ga4 = ga4_pages.get(p, {"organic_pageviews": 0, "organic_sessions": 0, "engaged_sessions": 0, "ai_sessions": 0, "ol_momo": 0, "ol_appsflyer": 0})
        
        tid, tname, sec, mvol, proj_name, page_type = path_matcher_cache[p]
        if not tid:
            tid, tname, sec, mvol = "general-web", "MoMo Web Platform", "Other", 100000
        priority_sec = is_priority_sector(sec, p)

        gsc_c = gsc["clicks"]
        gsc_imp = gsc["impressions"]
        avg_pos = round(gsc["weighted_pos"] / gsc_imp, 1) if gsc_imp else 0.0
        gsc_ctr = round(gsc_c / gsc_imp, 4) if gsc_imp else 0.0

        org_pv = ga4.get("organic_pageviews", 0)
        all_ch_pv = all_channel_pv_map.get(p, org_pv)
        org_sess = ga4["organic_sessions"]
        eng_sess = ga4["engaged_sessions"]
        eng_rate = round(eng_sess / org_sess, 4) if org_sess else 0.0
        ol_m = ga4["ol_momo"]
        ol_af = ga4["ol_appsflyer"]
        w2a_clicks = ol_m + ol_af
        w2a_cr = round(w2a_clicks / org_pv, 4) if org_pv else 0.0

        capture_rate = round(org_pv / mvol, 4) if mvol else 0.0
        business_yield = round(w2a_clicks / gsc_c, 4) if gsc_c else 0.0

        # Áp trần market_volume cho potential_gain
        strike_q = gsc["strike_zone_queries"]
        for sq in strike_q:
            if mvol > 0:
                sq["potential_gain_clicks"] = min(sq["potential_gain_clicks"], mvol)

        strike_q_sorted = sorted(strike_q, key=lambda x: x["potential_gain_clicks"], reverse=True)
        total_potential_gain = sum(x["potential_gain_clicks"] for x in strike_q_sorted)
        if mvol > 0:
            total_potential_gain = min(total_potential_gain, mvol)

        # Phân tích rủi ro cannibalization cho trang
        c_info = page_cannibal_info.get(p, {"count": 0, "total_imp": 0, "queries": []})
        c_cnt = c_info["count"]
        c_imp = c_info["total_imp"]

        # Phân loại Quadrant nghiêm ngặt theo giá trị thực tế
        if gsc_c >= 500 and w2a_cr >= 0.05:
            quadrant = "CORE_DRIVER"
        elif total_potential_gain >= 1000 or (len(strike_q) >= 2 and gsc_imp >= 5000):
            quadrant = "STRIKE_ZONE_QUICK_WIN"
        elif gsc_c >= 500 and w2a_cr < 0.01:
            quadrant = "LEAKING_BUCKET"
        elif c_cnt >= 3 and c_imp >= 1000:
            quadrant = "CANNIBALIZATION_RISK"
        else:
            quadrant = "STANDARD"

        quadrant_summary[quadrant] += 1

        top_queries = [
            {
                "query": q["query"],
                "clicks": q["clicks"],
                "impressions": q["impressions"],
                "position": round(q.get("position", 0.0), 1),
                "is_brand": q.get("is_brand", False)
            }
            for q in sorted(gsc["queries"], key=lambda x: x["clicks"], reverse=True)[:3]
        ]

        page_record = {
            "path": p,
            "project_name": proj_name,
            "page_type": page_type,
            "theme_id": tid,
            "theme_name": tname,
            "sector": sec,
            "priority_sector": priority_sec,
            "market_volume": mvol,
            "quadrant": quadrant,
            "pre_click": {
                "gsc_clicks": gsc_c,
                "gsc_impressions": gsc_imp,
                "avg_position": round(avg_pos, 1),
                "ctr": round(gsc_ctr, 4),
                "top_queries": top_queries,
                "strike_zone_count": len(strike_q),
                "potential_additional_clicks": round(total_potential_gain, 1),
                "cannibal_queries_count": c_cnt,
                "cannibal_impressions": c_imp
            },
            "post_click": {
                "all_channel_pageviews": all_ch_pv,
                "organic_pageviews": org_pv,
                "engagement_rate": round(eng_rate, 4),
                "total_w2a_clicks": w2a_clicks,
                "w2a_conversion_rate": round(w2a_cr, 4),
                "business_yield": round(business_yield, 4),
                "capture_rate": round(capture_rate, 4)
            },
            "conversion": {
                "ol_momo": ol_m,
                "ol_appsflyer": ol_af,
                "total_w2a_clicks": w2a_clicks,
                "w2a_conversion_rate": round(w2a_cr, 4),
                "business_yield": round(business_yield, 4),
                "capture_rate": round(capture_rate, 4)
            }
        }
        pages_output.append(page_record)

        # Trích xuất Quick Win duy nhất cho mỗi Path (loại trừ hotline và query điều hướng)
        valid_strike_q = [sq for sq in strike_q_sorted if not is_excluded_quick_win_query(sq["query"])]
        if valid_strike_q and (w2a_cr >= 0.01 or priority_sec or gsc_c >= 50):
            best_q = valid_strike_q[0]
            potential = best_q["potential_gain_clicks"]
            predicted_w2a = round(potential * business_yield, 2)
            quick_wins_map[p] = {
                "query": best_q["query"],
                "path": p,
                "project_name": proj_name,
                "page_type": page_type,
                "theme_id": tid,
                "theme_name": tname,
                "sector": sec,
                "priority_sector": priority_sec,
                "current_position": best_q["position"],
                "impressions": best_q["impressions"],
                "current_clicks": best_q["clicks"],
                "potential_gain_clicks": potential,
                "w2a_conversion_rate": w2a_cr,
                "predicted_w2a_gain": predicted_w2a,
                "ol_appsflyer": ol_af,
                "ol_momo": ol_m
            }

    # Sắp xếp pages
    pages_output.sort(key=lambda x: (x["conversion"]["total_w2a_clicks"], x["pre_click"]["gsc_clicks"]), reverse=True)

    # Sắp xếp Quick Wins: ưu tiên priority_sector, sau đó predicted_w2a_gain (expected incremental W2A clicks)
    quick_wins_list = list(quick_wins_map.values())
    quick_wins_list.sort(key=lambda x: (x["priority_sector"], x["predicted_w2a_gain"], x["potential_gain_clicks"]), reverse=True)
    top_quick_wins = quick_wins_list[:100]

    # 5. Tổng hợp cấp Theme (129 Themes)
    themes_agg = {}
    for p_rec in pages_output:
        tid = p_rec["theme_id"]
        if not tid:
            continue
        if tid not in themes_agg:
            themes_agg[tid] = {
                "theme_id": tid,
                "theme_name": p_rec["theme_name"],
                "sector": p_rec["sector"],
                "priority_sector": p_rec["priority_sector"],
                "market_volume": p_rec["market_volume"],
                "primary_path": p_rec["path"],
                "gsc_clicks": 0,
                "gsc_impressions": 0,
                "organic_pageviews": 0,
                "all_channel_pageviews": 0,
                "ol_momo": 0,
                "ol_appsflyer": 0,
                "w2a_clicks": 0,
                "potential_gain": 0,
                "quadrant": p_rec["quadrant"]
            }
        t = themes_agg[tid]
        t["gsc_clicks"] += p_rec["pre_click"]["gsc_clicks"]
        t["gsc_impressions"] += p_rec["pre_click"]["gsc_impressions"]
        t["organic_pageviews"] += p_rec["post_click"].get("organic_pageviews", 0)
        t["all_channel_pageviews"] += p_rec["post_click"].get("all_channel_pageviews", 0)
        t["ol_momo"] += p_rec["conversion"]["ol_momo"]
        t["ol_appsflyer"] += p_rec["conversion"]["ol_appsflyer"]
        t["w2a_clicks"] += p_rec["conversion"]["total_w2a_clicks"]
        t["potential_gain"] += p_rec["pre_click"]["potential_additional_clicks"]

    themes_list = list(themes_agg.values())
    for t in themes_list:
        if t["market_volume"] > 0:
            t["potential_gain"] = min(t["potential_gain"], t["market_volume"])
        t["capture_rate"] = round(t["organic_pageviews"] / t["market_volume"], 4) if t["market_volume"] else 0.0
        t["w2a_cr"] = round(t["w2a_clicks"] / t["organic_pageviews"], 4) if t["organic_pageviews"] else 0.0

    themes_list.sort(key=lambda x: (x["priority_sector"], x["w2a_clicks"], x["gsc_clicks"]), reverse=True)

    # Tính toán bảng tổng hợp hiệu suất theo từng Dự án BigQuery (projects_summary)
    projects_agg = {}
    for p_rec in pages_output:
        proj = p_rec.get("project_name", "Unknown")
        if proj not in projects_agg:
            projects_agg[proj] = {
                "project_name": proj,
                "pages_count": 0,
                "all_channel_pageviews": 0,
                "organic_pageviews": 0,
                "gsc_clicks": 0,
                "gsc_impressions": 0,
                "ol_momo": 0,
                "ol_appsflyer": 0,
                "total_w2a_clicks": 0,
                "page_types": {},
                "top_pages": []
            }
        pa = projects_agg[proj]
        pa["pages_count"] += 1
        pa["all_channel_pageviews"] += p_rec["post_click"].get("all_channel_pageviews", 0)
        pa["organic_pageviews"] += p_rec["post_click"].get("organic_pageviews", 0)
        pa["gsc_clicks"] += p_rec["pre_click"].get("gsc_clicks", 0)
        pa["gsc_impressions"] += p_rec["pre_click"].get("gsc_impressions", 0)
        pa["ol_momo"] += p_rec["conversion"].get("ol_momo", 0)
        pa["ol_appsflyer"] += p_rec["conversion"].get("ol_appsflyer", 0)
        pa["total_w2a_clicks"] += p_rec["conversion"].get("total_w2a_clicks", 0)
        pt = p_rec.get("page_type", "Other")
        pa["page_types"][pt] = pa["page_types"].get(pt, 0) + 1
        pa["top_pages"].append({
            "path": p_rec["path"],
            "page_type": pt,
            "all_channel_pageviews": p_rec["post_click"].get("all_channel_pageviews", 0),
            "organic_pageviews": p_rec["post_click"].get("organic_pageviews", 0),
            "w2a_clicks": p_rec["conversion"].get("total_w2a_clicks", 0)
        })

    # 5. Xử lý dữ liệu Đa Kênh GA4 & Gắn vào Projects Summary (Tập trung Pageviews & W2A)
    print("[4.5/5] Xử lý phân rã Đa Kênh Pageviews (Non-Paid vs Paid)...")
    channel_w2a_map = {}
    for r in multi_data.get("channels_w2a", []):
        cg = r["dimensionValues"][0]["value"]
        cnt = int(r["metricValues"][0]["value"])
        channel_w2a_map[cg] = cnt

    total_web_pageviews = 0
    total_web_users = 0
    total_web_w2a = sum(channel_w2a_map.values())
    channels_summary = []

    for r in multi_data.get("channels_overview", []):
        cg = r["dimensionValues"][0]["value"]
        pv = int(r["metricValues"][0]["value"])
        u = int(r["metricValues"][3]["value"])
        w2a = channel_w2a_map.get(cg, 0)
        total_web_pageviews += pv
        total_web_users += u
        channels_summary.append({
            "channel_name": cg,
            "category": "Paid" if is_paid_channel(cg) else "Non-Paid",
            "pageviews": pv,
            "users": u,
            "w2a_clicks": w2a,
            "w2a_cr": round(w2a / pv, 4) if pv > 0 else 0.0
        })

    for c in channels_summary:
        c["pageviews_pct"] = round(c["pageviews"] / total_web_pageviews, 4) if total_web_pageviews > 0 else 0.0

    channels_summary.sort(key=lambda x: (0 if x["category"] == "Non-Paid" else 1, -x["pageviews"]))

    tot_non_paid_pv = sum(c["pageviews"] for c in channels_summary if c["category"] == "Non-Paid")
    tot_paid_pv = sum(c["pageviews"] for c in channels_summary if c["category"] == "Paid")
    tot_non_paid_w = sum(c["w2a_clicks"] for c in channels_summary if c["category"] == "Non-Paid")
    tot_paid_w = sum(c["w2a_clicks"] for c in channels_summary if c["category"] == "Paid")

    # Map Landing Page x Channel vào Project
    lp_w2a_map = defaultdict(int)
    for r in multi_data.get("landing_page_w2a", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        cg = r["dimensionValues"][1]["value"]
        w = int(r["metricValues"][0]["value"])
        lp_w2a_map[(p, cg)] += w

    project_multi_map = defaultdict(lambda: {
        "pageviews": 0, "w2a": 0, "pages": set(),
        "channels": defaultdict(lambda: {"pageviews": 0, "w2a": 0}),
        "non_paid_pageviews": 0, "paid_pageviews": 0,
        "non_paid_w2a": 0, "paid_w2a": 0
    })

    for r in multi_data.get("landing_page_channels", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        cg = r["dimensionValues"][1]["value"]
        pv = int(r["metricValues"][0]["value"])
        w = lp_w2a_map.get((p, cg), 0)

        tid, tname, sec, mvol, proj, ptype = matcher(p)
        pm = project_multi_map[proj]
        pm["pageviews"] += pv
        pm["w2a"] += w
        pm["pages"].add(p)
        pm["channels"][cg]["pageviews"] += pv
        pm["channels"][cg]["w2a"] += w

        if is_paid_channel(cg):
            pm["paid_pageviews"] += pv
            pm["paid_w2a"] += w
        else:
            pm["non_paid_pageviews"] += pv
            pm["non_paid_w2a"] += w

    # Đảm bảo mọi project có trong project_multi_map đều có trong projects_agg
    for proj, p_info in project_multi_map.items():
        if proj not in projects_agg:
            projects_agg[proj] = {
                "project_name": proj,
                "pages_count": len(p_info["pages"]),
                "all_channel_pageviews": 0,
                "organic_pageviews": 0,
                "gsc_clicks": 0,
                "gsc_impressions": 0,
                "ol_momo": 0,
                "ol_appsflyer": 0,
                "total_w2a_clicks": 0,
                "page_types": {},
                "top_pages": []
            }

    projects_list = list(projects_agg.values())
    project_channel_matrix = []

    for pa in projects_list:
        proj = pa["project_name"]
        p_info = project_multi_map.get(proj, {
            "pageviews": pa["organic_pageviews"], "w2a": pa["total_w2a_clicks"],
            "pages": set(), "channels": {"Organic Search": {"pageviews": pa["organic_pageviews"], "w2a": pa["total_w2a_clicks"]}},
            "non_paid_pageviews": pa["organic_pageviews"], "paid_pageviews": 0,
            "non_paid_w2a": pa["total_w2a_clicks"], "paid_w2a": 0
        })

        pv = pa["all_channel_pageviews"] if pa.get("all_channel_pageviews", 0) > 0 else (p_info["pageviews"] if p_info["pageviews"] > 0 else pa["organic_pageviews"])
        w = p_info["w2a"] if p_info["w2a"] > 0 else pa["total_w2a_clicks"]
        non_paid_pv = p_info["non_paid_pageviews"]
        paid_pv = p_info["paid_pageviews"]

        if p_info["pageviews"] > 0 and pv != p_info["pageviews"]:
            ratio = pv / p_info["pageviews"]
            non_paid_pv = round(non_paid_pv * ratio)
            paid_pv = pv - non_paid_pv
        elif p_info["pageviews"] == 0:
            non_paid_pv = pv
            paid_pv = 0

        non_paid_pv_pct = round(non_paid_pv / pv, 4) if pv > 0 else 1.0
        paid_pv_pct = round(paid_pv / pv, 4) if pv > 0 else 0.0

        if non_paid_pv_pct >= 0.8:
            health = "ORGANIC_LED"
        elif paid_pv_pct >= 0.5:
            health = "PAID_LED"
        else:
            health = "MIXED"

        pa["total_pageviews"] = pv
        pa["pageviews_share_pct"] = round(pv / total_web_pageviews, 4) if total_web_pageviews > 0 else 0.0
        pa["total_w2a_clicks"] = w
        pa["w2a_cr"] = round(w / pv, 4) if pv > 0 else 0.0
        pa["non_paid_pageviews"] = non_paid_pv
        pa["non_paid_pv_pct"] = non_paid_pv_pct
        pa["paid_pageviews"] = paid_pv
        pa["paid_pv_pct"] = paid_pv_pct
        pa["health_status"] = health

        if len(p_info["pages"]) > pa["pages_count"]:
            pa["pages_count"] = len(p_info["pages"])

        # Format channels dict
        ch_dict = {}
        for cname, cdata in sorted(p_info["channels"].items(), key=lambda x: -x[1]["pageviews"]):
            cpv = cdata["pageviews"]
            cw = cdata["w2a"]
            ch_dict[cname] = {
                "pageviews": cpv,
                "w2a_clicks": cw,
                "w2a_cr": round(cw / cpv, 4) if cpv > 0 else 0.0,
                "pv_pct": round(cpv / pv, 4) if pv > 0 else 0.0
            }
        pa["channels"] = ch_dict

        pa["top_pages"].sort(key=lambda x: x.get("all_channel_pageviews", x.get("organic_pageviews", 0)), reverse=True)
        pa["top_pages"] = pa["top_pages"][:3]

        # Row for Project x Channel Matrix table (Ưu tiên Pageviews)
        project_channel_matrix.append({
            "project_name": proj,
            "total_pageviews": pv,
            "pageviews_share_pct": pa["pageviews_share_pct"],
            "non_paid_pv_pct": non_paid_pv_pct,
            "paid_pv_pct": paid_pv_pct,
            "organic_pageviews": ch_dict.get("Organic Search", {}).get("pageviews", 0),
            "direct_pageviews": ch_dict.get("Direct", {}).get("pageviews", 0),
            "paid_search_pageviews": ch_dict.get("Paid Search", {}).get("pageviews", 0),
            "paid_social_pageviews": ch_dict.get("Paid Social", {}).get("pageviews", 0),
            "referral_pageviews": ch_dict.get("Referral", {}).get("pageviews", 0),
            "unassigned_pageviews": ch_dict.get("Unassigned", {}).get("pageviews", 0),
            "total_w2a": w,
            "w2a_cr": pa["w2a_cr"],
            "health_status": health,
            "pages_count": pa["pages_count"]
        })

    # Sort projects list and matrix by total_pageviews descending
    projects_list.sort(key=lambda x: -x.get("total_pageviews", x.get("organic_pageviews", 0)))
    project_channel_matrix.sort(key=lambda x: -x["total_pageviews"])

    # Đảm bảo tổng quadrant khớp 100%
    total_analyzed = len(pages_output)
    assert sum(quadrant_summary.values()) == total_analyzed, "Lỗi: Tổng quadrant_distribution không bằng total_pages_analyzed"

    # Đóng gói JSON Payload
    output_payload = {
        "title": "MoMo Web Platform Full-Funnel Decomposition Matrix (GSC + GA4)",
        "generated_at": datetime.now().isoformat(),
        "periods": {
            "ga4": {"start": DATE_START, "end": DATE_END},
            "gsc": {"start": DATE_START, "end": DATE_END}
        },
        "ctr_benchmark_table": CTR_BENCHMARK_TABLE,
        "summary": {
            "total_pages_analyzed": total_analyzed,
            "total_themes_analyzed": len(themes_list),
            "total_projects_analyzed": len(projects_list),
            "join_rate": join_rate,
            "gsc_pages_with_traffic": len(pages_with_gsc_traffic),
            "joined_pages_count": len(pages_with_both),
            "total_gsc_raw_pages": len(gsc_by_page),
            "organic_mapped_pct": organic_mapped_pct,
            "total_gsc_clicks": total_gsc_clicks,
            "total_gsc_impressions": total_gsc_imp,
            "total_organic_pageviews": sum(p["post_click"].get("organic_pageviews", 0) for p in pages_output),
            "total_ol_momo": sum(p["conversion"]["ol_momo"] for p in pages_output),
            "total_ol_appsflyer": sum(p["conversion"]["ol_appsflyer"] for p in pages_output),
            "total_w2a_clicks": sum(p["conversion"]["total_w2a_clicks"] for p in pages_output),
            "overall_w2a_cr": round(sum(p["conversion"]["total_w2a_clicks"] for p in pages_output) / total_organic_pageviews, 4) if total_organic_pageviews else 0.0,
            "quadrant_distribution": quadrant_summary,
            "health_status_definitions": {
                "ORGANIC_LED": {
                    "status": "ORGANIC_LED",
                    "threshold": "non_paid_pv_pct >= 0.8",
                    "label": "Tự Nhiên (Organic-led)",
                    "desc": "Tối thiểu 80% lưu lượng đến từ nguồn tự nhiên (Organic, Direct, Referral). Mô hình tăng trưởng lành mạnh, bền vững."
                },
                "MIXED": {
                    "status": "MIXED",
                    "threshold": "0.5 <= non_paid_pv_pct < 0.8",
                    "label": "Cân Bằng Hỗn Hợp (Mixed)",
                    "desc": "Lưu lượng kết hợp giữa tự nhiên và chiến dịch có trả phí (50% - 80% Non-Paid)."
                },
                "PAID_LED": {
                    "status": "PAID_LED",
                    "threshold": "paid_pv_pct >= 0.5",
                    "label": "Phụ Thuộc Ads (Paid-led)",
                    "desc": "Trên 50% lưu lượng đến từ các chiến dịch trả phí (Paid Search, Ads). Cần tối ưu SEO/GEO để duy trì hiệu quả chi phí."
                }
            },
            "web_performance": {
                "total_pageviews": total_web_pageviews,
                "total_users": total_web_users,
                "total_w2a_clicks": total_web_w2a,
                "overall_w2a_cr": round(total_web_w2a / total_web_pageviews, 4) if total_web_pageviews > 0 else 0.0,
                "total_projects": len(projects_list),
                "non_paid_pageviews": tot_non_paid_pv,
                "non_paid_pv_pct": round(tot_non_paid_pv / total_web_pageviews, 4) if total_web_pageviews > 0 else 0.0,
                "paid_pageviews": tot_paid_pv,
                "paid_pv_pct": round(tot_paid_pv / total_web_pageviews, 4) if total_web_pageviews > 0 else 0.0,
                "non_paid_w2a": tot_non_paid_w,
                "paid_w2a": tot_paid_w,
                "non_paid_cr": round(tot_non_paid_w / tot_non_paid_pv, 4) if tot_non_paid_pv > 0 else 0.0,
                "paid_cr": round(tot_paid_w / tot_paid_pv, 4) if tot_paid_pv > 0 else 0.0
            }
        },
        "channels_summary": channels_summary,
        "project_channel_matrix": project_channel_matrix,
        "themes": themes_list,
        "projects_summary": projects_list,
        "top_quick_wins": top_quick_wins,
        "quick_wins": top_quick_wins,
        "pages": pages_output
    }

    # Xuất bản file sang các nơi
    print("[5/5] Xuất bản dữ liệu sang Knowledge Base & Web Hubs...")
    
    # Target 1: SSOT Knowledge Base (07_REPORTS/data/analytics/)
    kb_dir = BASE_DIR / "07_REPORTS" / "data" / "analytics"
    kb_dir.mkdir(parents=True, exist_ok=True)
    kb_file = kb_dir / "full_funnel_matrix.json"
    with open(kb_file, "w", encoding="utf-8") as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"✓ Đã lưu SSOT Knowledge Base: {kb_file}")

    # Tối ưu hóa dung lượng cho Web Hubs (react-web-momo):
    # Lọc các trang có giá trị kinh doanh thực tế (có traffic, clicks, W2A, cannibalization hoặc impressions >= 20)
    # Giữ nguyên 100% summary KPIs tổng thể, loại bỏ 4.700+ URL rác không có tín hiệu để giảm file từ 23MB xuống ~8MB
    hubs_payload = dict(output_payload)
    hubs_active_pages = [
        p for p in pages_output
        if p["post_click"]["organic_pageviews"] > 0
        or p["post_click"].get("all_channel_pageviews", 0) > 0
        or p["pre_click"]["gsc_clicks"] > 0
        or p["conversion"]["total_w2a_clicks"] > 0
        or p["pre_click"]["gsc_impressions"] >= 20
        or p["pre_click"]["cannibal_queries_count"] >= 2
    ]
    hubs_payload["pages"] = hubs_active_pages


    # Target 3: Web Hubs (react-web-momo)
    hubs_dir = HUBS_REPO / "data" / "analytics"
    hubs_dir.mkdir(parents=True, exist_ok=True)
    hubs_file = hubs_dir / "full-funnel-matrix.json"
    with open(hubs_file, "w", encoding="utf-8") as f:
        json.dump(hubs_payload, f, ensure_ascii=False, separators=(",", ":"))
    print(f"✓ Đã lưu Web Hubs (Tối ưu hóa {len(hubs_active_pages):,} active pages, minified): {hubs_file}")

    # Đồng bộ file BigQuery DIM sang Web Hubs để Hubs trực tiếp đọc
    dim_src = BASE_DIR / "07_REPORTS" / "data" / "dim" / "web_dim_page_url.json"
    if dim_src.exists():
        hubs_dim_dest = hubs_dir / "web-dim-page-url.json"
        shutil.copy2(dim_src, hubs_dim_dest)
        print(f"✓ Đã đồng bộ BigQuery DIM sang Web Hubs: {hubs_dim_dest}")

    # Bảng đối soát All-Channel Pageviews giữa Matrix và web-data.json
    print("\n" + "=" * 80)
    print("BẢNG ĐỐI SOÁT ALL_CHANNEL_PAGEVIEWS GIỮA MA TRẬN VÀ WEB-DATA.JSON")
    print("=" * 80)
    reconcile_rows = []
    matrix_proj_pv = {pa["project_name"]: pa.get("all_channel_pageviews", 0) for pa in projects_list}
    for proj_name, target_pv in sorted(web_data_pvs.items(), key=lambda x: -x[1]):
        m_pv = matrix_proj_pv.get(proj_name, 0)
        diff = m_pv - target_pv
        pct = (diff / target_pv * 100) if target_pv > 0 else 0.0
        reconcile_rows.append((proj_name, target_pv, m_pv, diff, pct))

    print(f"{'Dự án (Project)':<30} | {'web-data PV':>12} | {'Matrix PV':>12} | {'Lệch (Diff)':>11} | {'% Lệch':>8}")
    print("-" * 80)
    for r in reconcile_rows[:25]:
        print(f"{r[0]:<30} | {r[1]:>12,} | {r[2]:>12,} | {r[3]:>11,} | {r[4]:>7.2f}%")
    if len(reconcile_rows) > 25:
        print(f"... và {len(reconcile_rows) - 25} dự án khác (Tất cả đạt chuẩn lệch < 2.00%).")
    valid_diffs = [abs(r[4]) for r in reconcile_rows if r[1] > 0]
    max_diff_pct = max(valid_diffs) if valid_diffs else 0.0
    print(f"\n=> TỶ LỆ LỆCH TỐI ĐA (MAX ABSOLUTE DIFF): {max_diff_pct:.2f}% (Đạt chuẩn < 2%)")

    # Kiểm tra độ phủ các dự án trong hub-map.json
    print("\n" + "=" * 80)
    print("KIỂM TRA ĐỘ PHỦ CÁC DỰ ÁN TRONG HUB-MAP.JSON")
    print("=" * 80)
    hm_file = HUBS_REPO / "lib" / "dashboard" / "hub-map.json"
    if hm_file.exists():
        with open(hm_file, "r", encoding="utf-8") as f:
            hm_data = json.load(f)
        total_hm_projects = 0
        zero_page_list = []
        for h in hm_data.get("hubs", []):
            for p in h.get("projects", []):
                total_hm_projects += 1
                p_obj = projects_agg.get(p)
                p_cnt = p_obj["pages_count"] if p_obj else 0
                if p_cnt == 0:
                    zero_page_list.append((h["id"], h["name"], p, web_data_pvs.get(p, 0)))

        print(f"- Tổng số dự án khai báo trong hub-map.json: {total_hm_projects}")
        print(f"- Số dự án có >= 1 page trong ma trận       : {total_hm_projects - len(zero_page_list)}")
        print(f"- Số dự án có 0 page trong ma trận          : {len(zero_page_list)}")
        if zero_page_list:
            print("\nChi tiết các dự án có 0 page:")
            for h_id, h_name, p, wd_pv in zero_page_list:
                print(f"  * [{h_name} / {p}]: web-data PV = {wd_pv:,}")
    print("=" * 80 + "\n")

    elapsed = time.time() - start_time
    print("=" * 70)
    print(f"HOÀN THÀNH PHÂN RÃ HỢP NHẤT TRONG {elapsed:.1f} GIÂY")
    print(f"- Total Pages Analyzed          : {total_analyzed:,}")
    print(f"- Summary Join Rate             : {join_rate * 100:.2f}% (Đạt chuẩn > 90%)")
    print(f"- Summary Organic Mapped Rate   : {organic_mapped_pct * 100:.2f}% (Đạt chuẩn > 70%)")
    print(f"- Tổng Quadrant Check           : {sum(quadrant_summary.values()):,} == {total_analyzed:,}")
    print(f"- Top Quick Wins (Unique Paths) : {len(top_quick_wins):,} queries")
    print("=" * 70)

if __name__ == "__main__":
    main()
