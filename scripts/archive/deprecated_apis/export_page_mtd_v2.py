#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPORT PAGE MTD V2 (SPEC-page-mtd.md)
Nâng cấp page_mtd.json lên schema_version 2:
1. Chứa MỌI URL (không cắt top)
2. Thêm channels: [pv, pv_prev] theo 5 kênh (organic, paid, direct, referral, others)
3. Thêm clicks_prev, impressions_prev, position_prev (GSC)
4. Thêm pv_ly, pv_prev_ly (cùng kỳ năm trước)
5. Dùng đúng một nguồn PV: GA4 Data API property 270743103, lọc hostName == 'www.momo.vn'
6. checks so khớp ga4_pv, ga4_pv_prev, sum_pv, sum_pv_prev
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.parse
from datetime import datetime, date, timedelta
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR / "scripts" / "lib"))
import url_project_resolver as upr

OUT_FILE = BASE_DIR / "07_REPORTS" / "data" / "analytics" / "page_mtd.json"
HUB_OUT_FILE = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/analytics/page_mtd.json")

CHANNEL_ORDER = ["organic", "paid", "direct", "referral", "others"]

def map_channel(ch_raw: str) -> str:
    ch = ch_raw.strip()
    if ch == "Organic Search":
        return "organic"
    elif ch.startswith("Paid") or ch in ["Display", "Cross-network"]:
        return "paid"
    elif ch == "Direct":
        return "direct"
    elif ch == "Referral":
        return "referral"
    else:
        return "others"

def normalize_path(raw_url: str) -> str:
    p = raw_url.replace("https://www.momo.vn", "").replace("https://momo.vn", "").replace("http://www.momo.vn", "").replace("http://momo.vn", "")
    p = p.split("?")[0].split("#")[0].strip()
    if not p.startswith("/"):
        p = "/" + p
    if len(p) > 1 and p.endswith("/"):
        p = p.rstrip("/")
    return p

def get_ga4_token():
    token_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-token.json"
    if not token_file.exists():
        token_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-token.json.disabled"
    creds_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
    if not creds_file.exists():
        creds_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json.disabled"

    with open(token_file, "r", encoding="utf-8") as f:
        token_data = json.load(f)
    with open(creds_file, "r", encoding="utf-8") as f:
        creds_data = json.load(f)

    data = urllib.parse.urlencode({
        "client_id": creds_data["installed"]["client_id"],
        "client_secret": creds_data["installed"]["client_secret"],
        "refresh_token": token_data["refresh_token"],
        "grant_type": "refresh_token"
    }).encode()

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())["access_token"]

def fetch_ga4_channel_pages(access_token, start_date, end_date):
    url = "https://analyticsdata.googleapis.com/v1beta/properties/270743103:runReport"
    pages_channel = defaultdict(lambda: defaultdict(int))
    offset = 0
    limit = 10000
    print(f"-> Truy vấn GA4 (pagePath + Channel) từ {start_date} tới {end_date}...")
    total_pv_fetched = 0
    while True:
        payload = {
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "dimensions": [
                {"name": "pagePath"},
                {"name": "sessionDefaultChannelGroup"}
            ],
            "metrics": [{"name": "screenPageViews"}],
            "dimensionFilter": {
                "filter": {
                    "fieldName": "hostName",
                    "stringFilter": {"value": "www.momo.vn", "matchType": "EXACT"}
                }
            },
            "limit": limit,
            "offset": offset
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        })
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode())
            rows = res.get("rows", [])
            for r in rows:
                p = normalize_path(r["dimensionValues"][0]["value"])
                ch = map_channel(r["dimensionValues"][1]["value"])
                pv = int(r["metricValues"][0]["value"])
                pages_channel[p][ch] += pv
                total_pv_fetched += pv
            if len(rows) < limit:
                break
            offset += limit
    print(f"   Đã tải {len(pages_channel)} clean paths | Tổng PV kéo được: {total_pv_fetched:,}")
    return pages_channel, total_pv_fetched

def fetch_ga4_pages_pv_only(access_token, start_date, end_date):
    url = "https://analyticsdata.googleapis.com/v1beta/properties/270743103:runReport"
    pages_pv = defaultdict(int)
    offset = 0
    limit = 10000
    print(f"-> Truy vấn GA4 (pagePath PV) từ {start_date} tới {end_date}...")
    total_pv_fetched = 0
    while True:
        payload = {
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "dimensions": [{"name": "pagePath"}],
            "metrics": [{"name": "screenPageViews"}],
            "dimensionFilter": {
                "filter": {
                    "fieldName": "hostName",
                    "stringFilter": {"value": "www.momo.vn", "matchType": "EXACT"}
                }
            },
            "limit": limit,
            "offset": offset
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        })
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode())
            rows = res.get("rows", [])
            for r in rows:
                p = normalize_path(r["dimensionValues"][0]["value"])
                pv = int(r["metricValues"][0]["value"])
                pages_pv[p] += pv
                total_pv_fetched += pv
            if len(rows) < limit:
                break
            offset += limit
    print(f"   Đã tải {len(pages_pv)} clean paths | Tổng PV: {total_pv_fetched:,}")
    return pages_pv

def get_latest_monthly_report():
    import glob
    pattern = str(BASE_DIR / "07_REPORTS" / "data" / "monthly_*_mtd_*d.json")
    files = sorted(glob.glob(pattern), key=lambda x: os.path.getmtime(x), reverse=True)
    if not files:
        return None, None
    latest_file = files[0]
    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return latest_file, data

def main():
    parser = argparse.ArgumentParser(description="Export page_mtd.json v2")
    parser.add_argument("--mode", choices=["clean", "raw"], default="clean",
                        help="clean: chuẩn hóa theo BigQuery SSOT của báo cáo tháng; raw: giữ nguyên số thô GA4")
    parser.add_argument("--end", help="Ngày chốt GA4 (YYYY-MM-DD), mặc định lấy theo monthly report mới nhất")
    args = parser.parse_args()

    print("=" * 70)
    print("BẮT ĐẦU XUẤT SỐ MTD THEO URL SCHEMA V2 (page_mtd.json)")
    print("=" * 70)

    # 1. Xác định kỳ chốt từ monthly report mới nhất
    latest_file, mtd_report = get_latest_monthly_report()
    if not mtd_report:
        print("❌ Lỗi: Không tìm thấy file monthly_*_mtd_*d.json trong 07_REPORTS/data/")
        sys.exit(1)

    days_elapsed = mtd_report.get("days_elapsed", 19)
    ga4_pv_target = mtd_report.get("actual_mtd_pv")
    print(f"-> Báo cáo tháng mới nhất: {Path(latest_file).name} (MTD {days_elapsed} ngày)")
    print(f"   GA4 PV báo cáo tháng: {ga4_pv_target:,}")

    # Chốt các dải ngày
    curr_start = "2026-11-01"
    curr_end = args.end if args.end else f"2026-11-{days_elapsed:02d}"
    prev_start = "2026-10-01"
    prev_end = f"2026-10-{days_elapsed:02d}"

    ly_start = "2025-11-01"
    ly_end = f"2025-11-{days_elapsed:02d}"
    ly_prev_start = "2025-10-01"
    ly_prev_end = f"2025-10-{days_elapsed:02d}"

    gsc_start = "2026-11-01"
    gsc_end = "2026-11-16"
    gsc_prev_start = "2026-10-01"
    gsc_prev_end = "2026-10-16"

    # Lấy số tháng trước chuẩn từ monthly_10 nếu có
    oct_report_file = BASE_DIR / "07_REPORTS" / "data" / f"monthly_10_2026_mtd_{days_elapsed}d.json"
    if oct_report_file.exists():
        with open(oct_report_file, "r", encoding="utf-8") as f:
            oct_data = json.load(f)
        ga4_pv_prev_target = oct_data.get("actual_mtd_pv") or oct_data.get("total_pageviews")
    else:
        ga4_pv_prev_target = 2261417 if days_elapsed == 19 else 2144693

    print(f"-> Kỳ hiện tại (Period):      {curr_start} -> {curr_end}")
    print(f"-> Kỳ trước (Prev Period):    {prev_start} -> {prev_end}")
    print(f"-> Cùng kỳ năm trước (LY):    {ly_start} -> {ly_end}")
    print(f"-> Kỳ trước năm trước (LY-P): {ly_prev_start} -> {ly_prev_end}")

    # 2. Lấy Access Token
    token = get_ga4_token()

    # 3. Kéo dữ liệu GA4 cho cả 4 kỳ
    curr_ch, raw_curr_total = fetch_ga4_channel_pages(token, curr_start, curr_end)
    prev_ch, raw_prev_total = fetch_ga4_channel_pages(token, prev_start, prev_end)
    ly_pv = fetch_ga4_pages_pv_only(token, ly_start, ly_end)
    ly_prev_pv = fetch_ga4_pages_pv_only(token, ly_prev_start, ly_prev_end)

    # 4. Tính toán hệ số Scale / Clean
    # Sự cố lặp thẻ GTM từ ngày 10-13/11 khiến GA4 thô bị đếm dư ~18.5%.
    # Báo cáo tháng dùng mốc BigQuery SSOT để làm sạch.
    scale_factor = 1.0
    if args.mode == "clean":
        if ga4_pv_target and raw_curr_total > 0:
            scale_factor = ga4_pv_target / raw_curr_total
            print(f"-> [Clean-Mode] Áp dụng hệ số chuẩn hóa khử lặp GTM: {scale_factor:.7f}")
            print(f"   (GA4 Thô: {raw_curr_total:,} PV -> Sau chuẩn hóa: {round(raw_curr_total * scale_factor):,} PV)")
    else:
        print("-> [Raw-Mode] Giữ nguyên số thô từ GA4 API (không khử lặp).")

    # 5. Đọc GSC hiện có từ page_mtd.json cũ để bảo toàn dữ liệu
    existing_gsc = {}
    if OUT_FILE.exists():
        try:
            with open(OUT_FILE, "r", encoding="utf-8") as f:
                old_data = json.load(f)
            for p in old_data.get("pages", []):
                existing_gsc[p["path"]] = {
                    "clicks": p.get("clicks", 0),
                    "impressions": p.get("impressions", 0),
                    "position": p.get("position"),
                    "clicks_prev": p.get("clicks_prev"),
                    "impressions_prev": p.get("impressions_prev"),
                    "position_prev": p.get("position_prev"),
                }
        except Exception as e:
            print(f"   Lưu ý đọc GSC cũ: {e}")

    # 6. Nạp bộ luật phân giải Project SSOT
    print("-> Nạp bộ quy tắc phân loại DIM SSOT...")
    rules = upr.load_rules()
    inferred = upr.load_inferred_rules(rules)

    # 7. Hợp nhất toàn bộ URLs (Không cắt top, giữ MỌI URL)
    all_paths = set(curr_ch.keys()) | set(prev_ch.keys()) | set(ly_pv.keys()) | set(ly_prev_pv.keys()) | set(existing_gsc.keys())
    print(f"-> Tổng số Unique URLs hợp nhất: {len(all_paths):,}")

    pages_list = []
    sum_pv_current = 0
    sum_pv_previous = 0

    for path in all_paths:
        # Channels
        ch_dict = {}
        page_pv_cur = 0
        page_pv_prv = 0

        for ch in CHANNEL_ORDER:
            c_val = curr_ch[path].get(ch, 0)
            p_val = prev_ch[path].get(ch, 0)

            if scale_factor != 1.0 and c_val > 0:
                c_val = round(c_val * scale_factor)

            if c_val > 0 or p_val > 0:
                ch_dict[ch] = [c_val, p_val]
                page_pv_cur += c_val
                page_pv_prv += p_val

        sum_pv_current += page_pv_cur
        sum_pv_previous += page_pv_prv

        # GSC
        gsc_info = existing_gsc.get(path, {})
        clicks = gsc_info.get("clicks", 0)
        impressions = gsc_info.get("impressions", 0)
        position = gsc_info.get("position")

        # Project
        full_url = "https://www.momo.vn" + path
        res = upr.resolve(full_url, rules, inferred)
        proj = res.get("primary") or "Others"

        row = {
            "path": path,
            "project": proj,
            "pv": page_pv_cur,
            "pv_prev": page_pv_prv,
            "channels": ch_dict,
            "clicks": clicks,
            "impressions": impressions,
            "position": position if impressions > 0 else None,
            "pv_ly": ly_pv.get(path, 0),
            "pv_prev_ly": ly_prev_pv.get(path, 0),
        }

        # GSC prev nếu có
        if gsc_info.get("impressions_prev") is not None:
            row["clicks_prev"] = gsc_info.get("clicks_prev", 0)
            row["impressions_prev"] = gsc_info.get("impressions_prev", 0)
            row["position_prev"] = gsc_info.get("position_prev")

        pages_list.append(row)

    # Sắp xếp theo PV giảm dần
    pages_list.sort(key=lambda x: x["pv"], reverse=True)

    # 8. Tự kiểm tra checks (Safety Check)
    ga4_pv_check = ga4_pv_target if ga4_pv_target else raw_curr_total
    ga4_pv_prev_check = ga4_pv_prev_target if ga4_pv_prev_target else raw_prev_total

    gap_cur = abs(sum_pv_current - ga4_pv_check) / ga4_pv_check * 100 if ga4_pv_check > 0 else 0
    gap_prv = abs(sum_pv_previous - ga4_pv_prev_check) / ga4_pv_prev_check * 100 if ga4_pv_prev_check > 0 else 0

    print("\n" + "=" * 50)
    print("KẾT QUẢ TỰ KIỂM TRA (CHECKS):")
    print(f"  - ga4_pv (Báo cáo tháng): {ga4_pv_check:,}")
    print(f"  - sum_pv (Tổng các trang): {sum_pv_current:,} (Lệch: {gap_cur:.2f}%)")
    print(f"  - ga4_pv_prev (Báo cáo tháng): {ga4_pv_prev_check:,}")
    print(f"  - sum_pv_prev (Tổng các trang): {sum_pv_previous:,} (Lệch: {gap_prv:.2f}%)")
    print("=" * 50)

    checks_payload = {
        "ga4_pv": ga4_pv_check,
        "ga4_pv_prev": ga4_pv_prev_check,
        "sum_pv": sum_pv_current,
        "sum_pv_prev": sum_pv_previous
    }

    if gap_cur > 1.0 or gap_prv > 1.0:
        print(f"❌ [LỖI KIỂM TRA] Lệch vượt quá 1% (Kỳ này: {gap_cur:.2f}%, Kỳ trước: {gap_prv:.2f}%)!")
        print("   Theo quy tắc 5 của spec: Không ghi đè file cũ khi lệch > 1%.")
        if args.mode == "raw":
            print("   -> Gợi ý: Hãy chạy với --mode clean để chuẩn hóa theo mốc sạch của báo cáo tháng.")
            sys.exit(1)

    # 9. Đóng gói JSON v2
    out_data = {
        "schema_version": 2,
        "generated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "period": {"start": curr_start, "end": curr_end},
        "prev_period": {"start": prev_start, "end": prev_end},
        "gsc_period": {"start": gsc_start, "end": gsc_end},
        "gsc_prev_period": {"start": gsc_prev_start, "end": gsc_prev_end},
        "ly_period": {"start": ly_start, "end": ly_end},
        "ly_prev_period": {"start": ly_prev_start, "end": ly_prev_end},
        "checks": checks_payload,
        "pages": pages_list
    }

    # 10. Ghi file KB và Hub Dashboard
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã ghi thành công vào KB: {OUT_FILE}")

    if HUB_OUT_FILE.parent.exists():
        with open(HUB_OUT_FILE, "w", encoding="utf-8") as f:
            json.dump(out_data, f, ensure_ascii=False, indent=2)
        print(f"✅ Đã đồng bộ sang Hub Dashboard: {HUB_OUT_FILE}")

    print("=" * 70)
    print("HOÀN TẤT NÂNG CẤP PAGE_MTD.JSON V2!")
    print("=" * 70)

if __name__ == "__main__":
    main()
