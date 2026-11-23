"""Audit các URL actionable (top URLs cần kiểm tra index/ranking) từ dữ liệu GSC/GA4.

Usage: ./.venv/bin/python scripts/audit_actionable_urls.py"""

import json, urllib.request, urllib.error, concurrent.futures, os, sys
from collections import defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(BASE_DIR, "scripts", "lib"))
import url_project_resolver as upr

with open("07_REPORTS/data/gsc_lost_impressions_detail.json") as f:
    data = json.load(f)

lost_30d = data["top_lost_in_30d"] # top 100
lost_7d = data["top_lost_in_7d"] # top 100

# Combine top URLs to check
candidates = {}
for item in lost_30d[:80]:
    u = item["url"].split("#")[0]
    if u not in candidates:
        candidates[u] = item

for item in lost_7d[:50]:
    u = item["url"].split("#")[0]
    if u not in candidates:
        candidates[u] = item

print(f"Total candidate URLs to audit HTTP status: {len(candidates)}")

def check_url(item):
    u = item["url"].split("#")[0]
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        resp = urllib.request.urlopen(req, timeout=4)
        final_u = resp.geturl()
        is_redirect = (final_u.rstrip("/") != u.rstrip("/"))
        return {"url": u, "status": resp.status, "redirect": is_redirect, "final_url": final_u, "item": item}
    except urllib.error.HTTPError as e:
        return {"url": u, "status": e.code, "redirect": False, "final_url": u, "item": item}
    except Exception as e:
        return {"url": u, "status": "ERROR", "redirect": False, "final_url": u, "item": item, "err": str(e)}

results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(check_url, item) for item in candidates.values()]
    for f in concurrent.futures.as_completed(futures):
        results.append(f.result())

by_status = defaultdict(list)
for r in results:
    by_status[r["status"]].append(r)

print("\n=== KẾT QUẢ AUDIT TRẠNG THÁI HTTP CÁC TRANG MẤT IMPRESSION LỚN NHẤT ===")
for status, items in sorted(by_status.items(), key=lambda x: str(x[0])):
    print(f"Status {status}: {len(items)} URLs")

dead_404 = by_status.get(404, [])
print(f"\n[NHÓM 1 - LỖI 404 TRANG CHẾT] Có {len(dead_404)} URLs đang làm bốc hơi traffic:")
for r in dead_404:
    it = r["item"]
    imp = it.get("imp_90d", it.get("imp_30d", 0))
    clk = it.get("clicks_90d", it.get("clicks_30d", 0))
    proj = it["project"]
    u = r["url"]
    print(f"  [{proj}] {imp:,} imp | {clk} clk -> {u}")

live_dropped = [r for r in by_status.get(200, []) if not r["redirect"]]
print(f"\n[NHÓM 2 - TRANG SỐNG NHƯNG RỚT TOP SERP VỀ 0 IMPRESSION] Có {len(live_dropped)} URLs:")
live_dropped.sort(key=lambda x: x["item"].get("imp_90d", x["item"].get("imp_30d", 0)), reverse=True)
for r in live_dropped[:15]:
    it = r["item"]
    imp = it.get("imp_90d", it.get("imp_30d", 0))
    clk = it.get("clicks_90d", it.get("clicks_30d", 0))
    proj = it["project"]
    u = r["url"]
    print(f"  [{proj}] {imp:,} imp | {clk} clk -> {u}")

redirected = [r for r in by_status.get(200, []) if r["redirect"]]
print(f"\n[NHÓM 3 - REDIRECT ĐÃ XỬ LÝ] Có {len(redirected)} URLs đã được 301 chuyển tiếp an toàn.")
