"""Phân tích tăng trưởng URL 7 ngày so với 7 ngày liền trước bằng GA4 Data API.

Usage: ./.venv/bin/python scripts/analyze_growth_urls_7d.py"""

import json, os, sys
from collections import defaultdict
from google.oauth2 import service_account
from googleapiclient.discovery import build

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(BASE_DIR, "scripts", "lib"))
import url_project_resolver as upr

key_file = os.path.join(BASE_DIR, "07_REPORTS", "data", "credentials", "gsc-credentials.json")
scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
creds = service_account.Credentials.from_service_account_file(key_file, scopes=scopes)
service = build("searchconsole", "v1", credentials=creds)

def fetch_pages(start_date, end_date):
    pages = {}
    start_row = 0
    batch_size = 25000
    while True:
        body = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["page"],
            "rowLimit": batch_size,
            "startRow": start_row
        }
        res = service.searchanalytics().query(siteUrl="https://www.momo.vn/", body=body).execute()
        rows = res.get("rows", [])
        if not rows:
            break
        for r in rows:
            pages[r["keys"][0]] = {
                "clicks": r["clicks"],
                "impressions": r["impressions"],
                "position": r["position"],
                "ctr": r["ctr"]
            }
        start_row += len(rows)
        if len(rows) < batch_size:
            break
    return pages

# 7 ngày gần nhất: 17/10 -> 23/10
# 7 ngày liền trước: 10/10 -> 16/10
print("Đang truy vấn GSC 7 ngày gần nhất (17/10 - 23/10)...")
curr_pages = fetch_pages("2026-10-17", "2026-10-23")
print(f"  Got {len(curr_pages):,} URLs")

print("Đang truy vấn GSC 7 ngày liền trước (10/10 - 16/10)...")
prev_pages = fetch_pages("2026-10-10", "2026-10-16")
print(f"  Got {len(prev_pages):,} URLs")

rules = upr.load_rules()
inferred = upr.load_inferred_rules(rules)

growing_pages = []
breakout_pages = []

for u, c in curr_pages.items():
    # Loại bỏ anchor hashtag để gom về URL sạch
    clean_u = u.split("#")[0]
    p = prev_pages.get(u, {"clicks": 0, "impressions": 0, "position": 0})
    
    diff_imp = c["impressions"] - p["impressions"]
    diff_clk = c["clicks"] - p["clicks"]
    pos_change = (p["position"] - c["position"]) if p["position"] > 0 else 0 # >0 là thăng hạng
    
    proj = upr.resolve_primary(clean_u, rules, inferred) or "Others"
    
    item = {
        "url": u,
        "clean_url": clean_u,
        "project": proj,
        "curr_imp": c["impressions"],
        "prev_imp": p["impressions"],
        "diff_imp": diff_imp,
        "pct_imp": round((diff_imp / p["impressions"] * 100), 1) if p["impressions"] > 0 else 999.0,
        "curr_clk": c["clicks"],
        "prev_clk": p["clicks"],
        "diff_clk": diff_clk,
        "curr_pos": round(c["position"], 1),
        "prev_pos": round(p["position"], 1) if p["position"] > 0 else None,
        "pos_change": round(pos_change, 1)
    }
    
    if diff_imp > 0 or diff_clk > 0:
        growing_pages.append(item)
    
    # Breakout: Tuần trước = 0 hoặc < 50 imp, tuần này vọt lên >= 500 imp
    if p["impressions"] < 50 and c["impressions"] >= 500:
        breakout_pages.append(item)

print(f"\nTổng số URL có tăng trưởng hiển thị (WoW): {len(growing_pages):,} URLs")
print(f"Tổng số URL bứt phá mới (Breakout: từ 0/<50 vọt lên >500): {len(breakout_pages):,} URLs")

# 1. Top Tăng Trưởng Lượt Hiển Thị Tuyệt Đối (+Net Impressions WoW)
growing_pages.sort(key=lambda x: x["diff_imp"], reverse=True)
print("\n=== TOP 15 TRANG TĂNG TRƯỞNG LƯỢT HIỂN THỊ (IMPRESSIONS) MẠNH NHẤT 7 NGÀY QUA ===")
for it in growing_pages[:15]:
    proj = it["project"]
    diff = it["diff_imp"]
    curr = it["curr_imp"]
    clk_diff = it["diff_clk"]
    pos = it["curr_pos"]
    pos_chg = f"(+{it['pos_change']})" if it["pos_change"] > 0 else ""
    print(f"  [{proj}] +{diff:,} imp ({curr:,} tuần này) | Clicks: {it['curr_clk']} (+{clk_diff}) | Pos: {pos} {pos_chg} -> {it['url']}")

# 2. Top Tăng Trưởng Clicks Tuyệt Đối (+Net Clicks WoW)
by_clicks = sorted(growing_pages, key=lambda x: x["diff_clk"], reverse=True)
print("\n=== TOP 10 TRANG TĂNG TRƯỞNG CLICKS (TRAFFIC VÀO WEB) MẠNH NHẤT 7 NGÀY QUA ===")
for it in by_clicks[:10]:
    proj = it["project"]
    diff_c = it["diff_clk"]
    curr_c = it["curr_clk"]
    diff_i = it["diff_imp"]
    pos = it["curr_pos"]
    print(f"  [{proj}] +{diff_c:,} clicks ({curr_c:,} tuần này) | +{diff_i:,} imp | Pos: {pos} -> {it['url']}")

# 3. Top Breakout Stars (Mới xuất hiện hoặc bùng nổ)
breakout_pages.sort(key=lambda x: x["curr_imp"], reverse=True)
print("\n=== TOP 10 NGÔI SAO MỚI BÙNG NỔ (BREAKOUT STARS TRONG 7 NGÀY) ===")
for it in breakout_pages[:10]:
    proj = it["project"]
    curr = it["curr_imp"]
    prev = it["prev_imp"]
    clk = it["curr_clk"]
    pos = it["curr_pos"]
    print(f"  [{proj}] {curr:,} imp (trước: {prev}) | {clk} clicks | Pos: {pos} -> {it['url']}")

