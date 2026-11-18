#!/usr/bin/env python3
"""
scripts/export_financial_monthly_pv_ga4.py
=============================================================================
Xuất file 05_HUBS/financial/data/financial_monthly_pv_ga4.json chuẩn schema GA4:
- Kéo trực tiếp từ Google Analytics 4 (Property 270743103).
- Định nghĩa Financial Hub thống nhất toàn chuỗi 2026:
  ^/(tai-chinh|tro-thu-tai-chinh|trung-tam-tai-chinh|vay-nhanh|vi-tra-sau|diem-tin-dung|the-tin-dung|mo-the-tin-dung|thanh-toan-the-tin-dung|thanh-toan-khoan-vay|tiet-kiem-online|tiet-kiem|tui-than-tai|tui-sinh-loi|chung-khoan|chung-chi-quy|san-dau-tu|tiem-vang-online|tra-gop|quan-ly-chi-tieu|quy-nhom|nhan-tien-quoc-te|ty-gia|gia-vang|lai-suat|uu-dai-vi-tra-sau|qua-ban-moi-ttkhoanvay)
- Phân nhóm kênh:
  paid = Paid Search + Paid Social + Paid Other + Cross-network
  non_paid = pageviews - paid
  sum(channels) == pageviews
- Tháng 11/2026 đang chạy:
  + Lũy kế 9 ngày sạch (01-09/11/2026), loại trừ dữ liệu nhiễu vòng lặp GTM ngày 10-11/11.
  + mtd: true, updatedDay: 9.
  + raw_11d ghi nhận đủ số 11 ngày phục vụ đối soát.
=============================================================================
"""

import json
import urllib.request
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CREDS_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
PROPERTY_ID = "270743103"
OUTPUT_FILE = BASE_DIR / "05_HUBS" / "financial" / "data" / "financial_monthly_pv_ga4.json"

FINANCIAL_PATH_REGEX = "^/(tai-chinh|tro-thu-tai-chinh|trung-tam-tai-chinh|vay-nhanh|vi-tra-sau|diem-tin-dung|the-tin-dung|mo-the-tin-dung|thanh-toan-the-tin-dung|thanh-toan-khoan-vay|tiet-kiem-online|tiet-kiem|tui-than-tai|tui-sinh-loi|chung-khoan|chung-chi-quy|san-dau-tu|tiem-vang-online|tra-gop|quan-ly-chi-tieu|quy-nhom|nhan-tien-quoc-te|ty-gia|gia-vang|lai-suat|uu-dai-vi-tra-sau|qua-ban-moi-ttkhoanvay)"

PAID_CHANNELS = {"Paid Search", "Paid Social", "Paid Other", "Cross-network"}


def get_access_token():
    with open(CREDS_FILE, "r", encoding="utf-8") as f:
        cdata = json.load(f)
    client_info = cdata.get("installed") or cdata.get("web")

    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        tdata = json.load(f)

    data = urllib.parse.urlencode({
        "client_id": client_info["client_id"],
        "client_secret": client_info["client_secret"],
        "refresh_token": tdata["refresh_token"],
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))["access_token"]


def query_ga4_monthly(token, start_date, end_date):
    body = {
        "dateRanges": [{"startDate": start_date, "endDate": end_date}],
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "metrics": [{"name": "screenPageViews"}],
        "dimensionFilter": {
            "filter": {
                "fieldName": "pagePath",
                "stringFilter": {
                    "matchType": "PARTIAL_REGEXP",
                    "value": FINANCIAL_PATH_REGEX
                }
            }
        }
    }
    req = urllib.request.Request(
        f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport",
        data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))

    channels = {}
    total_pv = 0
    paid_pv = 0

    for r in res.get("rows", []):
        cname = r["dimensionValues"][0]["value"]
        pv = int(r["metricValues"][0]["value"])
        channels[cname] = pv
        total_pv += pv
        if cname in PAID_CHANNELS:
            paid_pv += pv

    # Sắp xếp channels theo thứ tự PV giảm dần
    sorted_channels = dict(sorted(channels.items(), key=lambda x: -x[1]))
    non_paid_pv = total_pv - paid_pv

    # Kiểm tra tính toàn vẹn toán học
    assert paid_pv + non_paid_pv == total_pv, "paid + non_paid != total_pv"
    assert sum(sorted_channels.values()) == total_pv, "sum(channels) != total_pv"

    return total_pv, paid_pv, non_paid_pv, sorted_channels


def main():
    print("▶ Khởi động trích xuất GA4 Financial Hub Monthly Performance...")
    token = get_access_token()

    months_config = [
        ("2026-01", "2026-01-01", "2026-01-31", False, None),
        ("2026-02", "2026-02-01", "2026-02-28", False, None),
        ("2026-03", "2026-03-01", "2026-03-31", False, None),
        ("2026-04", "2026-04-01", "2026-04-30", False, None),
        ("2026-05", "2026-05-01", "2026-05-31", False, None),
        ("2026-06", "2026-06-01", "2026-06-30", False, None),
        ("2026-07", "2026-07-01", "2026-07-31", False, None),
        ("2026-08", "2026-08-01", "2026-08-31", False, None),
        ("2026-09", "2026-09-01", "2026-09-30", False, None),
        ("2026-10", "2026-10-01", "2026-10-31", False, None),
        # Tháng 11: Lũy kế 9 ngày sạch (01-09/11/2026), loại trừ vòng lặp GTM 10-11/11
        ("2026-11", "2026-11-01", "2026-11-09", True, 9),
    ]

    output_data = []

    for month_str, start_d, end_d, is_mtd, updated_day in months_config:
        print(f"  - Đang truy vấn {month_str} ({start_d} đến {end_d})...")
        tot, paid, non_paid, chs = query_ga4_monthly(token, start_d, end_d)

        obj = {
            "month": month_str,
            "pageviews": tot,
            "paid": paid,
            "non_paid": non_paid,
            "mtd": is_mtd,
            "channels": chs
        }

        if is_mtd:
            obj["updatedDay"] = updated_day
            obj["note"] = "Lũy kế 9 ngày sạch (01-09/11/2026), loại trừ dữ liệu nhiễu vòng lặp GTM ngày 10-11/11."
            
            # Lấy thêm raw 11 ngày đối soát
            print("  - Đang truy vấn raw 11 ngày tháng 11 để lưu metadata đối soát...")
            raw_tot, raw_paid, raw_non_paid, _ = query_ga4_monthly(token, "2026-11-01", "2026-11-11")
            obj["raw_11d"] = {
                "pageviews": raw_tot,
                "paid": raw_paid,
                "non_paid": raw_non_paid,
                "updatedDay": 11
            }

        output_data.append(obj)
        pct_paid = (paid / tot * 100) if tot else 0
        pct_non = (non_paid / tot * 100) if tot else 0
        print(f"    PV: {tot:,} | Paid: {paid:,} ({pct_paid:.1f}%) | Non-Paid: {non_paid:,} ({pct_non:.1f}%) | Channels: {len(chs)}")

    # Ghi file JSON
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Đã xuất thành công file: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
