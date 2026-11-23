"""Phân tích URL GSC có impressions = 0 để phát hiện URL chết/chưa index.

Usage: ./.venv/bin/python scripts/analyze_gsc_zero_impressions.py"""

import json, re, os, sys
from collections import defaultdict, Counter
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(BASE_DIR, "scripts", "lib"))
import url_project_resolver as upr

live_path = os.path.join(BASE_DIR, "07_REPORTS", "data", "momo_live_urls.json")
live_urls_data = json.load(open(live_path, "r"))
live_urls = set(live_urls_data["urls"])
print(f"Total Live Sitemap URLs: {len(live_urls):,}")

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
                "impressions": r["impressions"]
            }
        start_row += len(rows)
        if len(rows) < batch_size:
            break
    return pages

print("Fetching GSC data for 7d (17/10 - 23/10)...")
p7 = fetch_pages("2026-10-17", "2026-10-23")
print(f"  Got {len(p7):,} pages")

print("Fetching GSC data for 30d (24/09 - 23/10)...")
p30 = fetch_pages("2026-09-24", "2026-10-23")
print(f"  Got {len(p30):,} pages")

print("Fetching GSC data for 90d (26/07 - 23/10)...")
p90 = fetch_pages("2026-07-26", "2026-10-23")
print(f"  Got {len(p90):,} pages")

norm_live = {upr.normalize_url(u): u for u in live_urls}
norm_p7 = {upr.normalize_url(u): data for u, data in p7.items()}
norm_p30 = {upr.normalize_url(u): data for u, data in p30.items()}
norm_p90 = {upr.normalize_url(u): data for u, data in p90.items()}

rules = upr.load_rules()
inferred = upr.load_inferred_rules(rules)

results = {
    "total_live": len(live_urls),
    "active_7d": 0, "zero_7d": 0,
    "active_30d": 0, "zero_30d": 0,
    "active_90d": 0, "zero_90d": 0,
}

by_project = defaultdict(lambda: {
    "total": 0,
    "active_7d": 0, "zero_7d": 0,
    "active_30d": 0, "zero_30d": 0,
    "active_90d": 0, "zero_90d": 0,
    "imp_30d": 0, "clicks_30d": 0
})

zero_90d_urls = []
zero_30d_urls = []

for nu, orig_u in norm_live.items():
    proj = upr.resolve_primary(orig_u, rules, inferred) or "Others"
    by_project[proj]["total"] += 1
    
    has_7 = nu in norm_p7
    has_30 = nu in norm_p30
    has_90 = nu in norm_p90

    if has_7:
        results["active_7d"] += 1
        by_project[proj]["active_7d"] += 1
    else:
        results["zero_7d"] += 1
        by_project[proj]["zero_7d"] += 1

    if has_30:
        results["active_30d"] += 1
        by_project[proj]["active_30d"] += 1
        by_project[proj]["imp_30d"] += norm_p30[nu]["impressions"]
        by_project[proj]["clicks_30d"] += norm_p30[nu]["clicks"]
    else:
        results["zero_30d"] += 1
        by_project[proj]["zero_30d"] += 1
        zero_30d_urls.append(orig_u)

    if has_90:
        results["active_90d"] += 1
        by_project[proj]["active_90d"] += 1
    else:
        results["zero_90d"] += 1
        by_project[proj]["zero_90d"] += 1
        zero_90d_urls.append(orig_u)

tot = results["total_live"]
z7 = results["zero_7d"]
a7 = results["active_7d"]
z30 = results["zero_30d"]
a30 = results["active_30d"]
z90 = results["zero_90d"]
a90 = results["active_90d"]

print("\n=== TỔNG QUAN TỶ LỆ KHÔNG CÓ IMPRESSION TRÊN SITEMAP ===")
print(f"Tổng số URL sitemap (Live): {tot:,}")
print(f"7 ngày  (17/10 - 23/10): Không có impression: {z7:,} ({z7/tot*100:.2f}%) | Có impression: {a7:,} ({a7/tot*100:.2f}%)")
print(f"30 ngày (24/09 - 23/10): Không có impression: {z30:,} ({z30/tot*100:.2f}%) | Có impression: {a30:,} ({a30/tot*100:.2f}%)")
print(f"90 ngày (26/07 - 23/10): Không có impression: {z90:,} ({z90/tot*100:.2f}%) | Có impression: {a90:,} ({a90/tot*100:.2f}%)")

print("\n=== PHÂN BỔ DỰ ÁN CÓ URL ZERO-IMPRESSION (TOP DỰ ÁN NHIỀU URL NHẤT) ===")
sorted_proj = sorted(by_project.items(), key=lambda x: x[1]["total"], reverse=True)
header = f"{'PROJECT':<26} | {'TOTAL':>7} | {'ZERO 7D':>10} | {'ZERO 30D':>10} | {'ZERO 90D':>10} | {'% ZERO 30D':>11}"
print(header)
print("-" * len(header))
for proj, d in sorted_proj:
    if d["total"] >= 10:
        z30_pct = (d["zero_30d"] / d["total"]) * 100
        line = f"{proj:<26} | {d['total']:>7,} | {d['zero_7d']:>10,} | {d['zero_30d']:>10,} | {d['zero_90d']:>10,} | {z30_pct:>10.1f}%"
        print(line)

summary_out = {
    "generated_at": datetime.now().isoformat(),
    "sitemap_total": tot,
    "timeframes": {
        "7d": {"active": a7, "zero": z7, "zero_pct": round(z7/tot*100, 2)},
        "30d": {"active": a30, "zero": z30, "zero_pct": round(z30/tot*100, 2)},
        "90d": {"active": a90, "zero": z90, "zero_pct": round(z90/tot*100, 2)},
    },
    "by_project": {p: d for p, d in sorted_proj},
    "zero_90d_count": len(zero_90d_urls),
    "zero_90d_urls": zero_90d_urls,
    "zero_30d_count": len(zero_30d_urls),
}

out_path = os.path.join(BASE_DIR, "07_REPORTS", "data", "gsc_zero_impression_analysis.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(summary_out, f, ensure_ascii=False, indent=2)
print(f"\nĐã lưu kết quả phân tích: {out_path}")
