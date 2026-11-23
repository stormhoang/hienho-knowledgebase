"""Phát hiện URL mất impressions: có impressions trong 90d/30d nhưng = 0 trong 30d/7d gần nhất (GSC).

Usage: ./.venv/bin/python scripts/analyze_lost_impressions.py"""

import json, os, sys
from collections import defaultdict, Counter
from datetime import datetime, timedelta
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
                "position": r["position"]
            }
        start_row += len(rows)
        if len(rows) < batch_size:
            break
    return pages

print("Fetching GSC data for 7d, 30d, 90d...")
p7 = fetch_pages("2026-10-17", "2026-10-23")
p30 = fetch_pages("2026-09-24", "2026-10-23")
p90 = fetch_pages("2026-07-26", "2026-10-23")

rules = upr.load_rules()
inferred = upr.load_inferred_rules(rules)

# URLs having impressions in 90d but 0 in 30d
lost_in_30d = []
for u, d90 in p90.items():
    if u not in p30:
        proj = upr.resolve_primary(u, rules, inferred) or "Others"
        lost_in_30d.append({
            "url": u,
            "project": proj,
            "imp_90d": d90["impressions"],
            "clicks_90d": d90["clicks"],
            "pos_90d": round(d90["position"], 1)
        })

# URLs having impressions in 30d but 0 in 7d
lost_in_7d = []
for u, d30 in p30.items():
    if u not in p7:
        proj = upr.resolve_primary(u, rules, inferred) or "Others"
        lost_in_7d.append({
            "url": u,
            "project": proj,
            "imp_30d": d30["impressions"],
            "clicks_30d": d30["clicks"],
            "pos_30d": round(d30["position"], 1)
        })

print(f"\n1. TỔNG SỐ URL CÓ IMPRESSION TRONG 90 NGÀY NHƯNG MẤT SẠCH (0 IMP) TRONG 30 NGÀY: {len(lost_in_30d):,} URLs")
lost_in_30d.sort(key=lambda x: x["imp_90d"], reverse=True)
print("Top 12 URLs mất impression nặng nhất (90d -> 30d):")
for item in lost_in_30d[:12]:
    p = item["project"]
    imp = item["imp_90d"]
    clk = item["clicks_90d"]
    pos = item["pos_90d"]
    u = item["url"]
    print(f"  [{p}] {imp:,} imp | {clk} clk | pos {pos} -> {u}")

print(f"\n2. TỔNG SỐ URL CÓ IMPRESSION TRONG 30 NGÀY NHƯNG MẤT SẠCH (0 IMP) TRONG 7 NGÀY GẦN NHẤT: {len(lost_in_7d):,} URLs")
lost_in_7d.sort(key=lambda x: x["imp_30d"], reverse=True)
print("Top 12 URLs mất impression nặng nhất (30d -> 7d):")
for item in lost_in_7d[:12]:
    p = item["project"]
    imp = item["imp_30d"]
    clk = item["clicks_30d"]
    pos = item["pos_30d"]
    u = item["url"]
    print(f"  [{p}] {imp:,} imp | {clk} clk | pos {pos} -> {u}")

# Phân bổ theo Project
by_proj_lost_30d = Counter(x["project"] for x in lost_in_30d)
print("\nPhân bổ URLs mất impression theo dự án (90d -> 30d):")
for p, c in by_proj_lost_30d.most_common(12):
    print(f"  {p:<26} : {c:,} URLs")

# Save detailed output JSON for UI visualization
out_data = {
    "generated_at": datetime.now().isoformat(),
    "summary": {
        "lost_in_30d_count": len(lost_in_30d),
        "lost_in_7d_count": len(lost_in_7d),
        "total_active_90d": len(p90),
        "total_active_30d": len(p30),
        "total_active_7d": len(p7)
    },
    "by_project_lost_30d": dict(by_proj_lost_30d.most_common()),
    "top_lost_in_30d": lost_in_30d[:100],
    "top_lost_in_7d": lost_in_7d[:100],
    "all_lost_in_30d": lost_in_30d
}

out_file = os.path.join(BASE_DIR, "07_REPORTS", "data", "gsc_lost_impressions_detail.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)
print(f"\nĐã lưu chi tiết danh sách URL mất impression: {out_file}")

# Copy to react-web-momo
hub_data_dir = os.path.join(BASE_DIR, "..", "Web-Idea", "react-web-momo", "data", "analytics")
if os.path.exists(hub_data_dir):
    hub_file = os.path.join(hub_data_dir, "gsc-lost-impressions-detail.json")
    with open(hub_file, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    print(f"Đã đồng bộ sang react-web-momo: {hub_file}")
