#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC PAID ADS & UTM PERFORMANCE (GA4 DATA API)
Truy vấn trực tiếp từ GA4 Data API (Property 270743103):
- Bóc tách toàn bộ trang web đang chạy Ads (Landing Pages)
- Chi tiết kênh Media phân bổ (Google Search, TikTok, Meta Ads, Admicro, Zalo...)
- Mẫu quảng cáo (utm_content) và chiến dịch (utm_campaign)
- Hiệu suất chuyển đổi Web-to-App (click_to_app, in-game installs)
- Tự động xuất JSON SSOT và Markdown Report tổng quan
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.sync_ga4_to_hubs import get_access_token, PROPERTY_ID, run_ga4_report

# Output paths
JSON_OUTPUT = BASE_DIR / "07_REPORTS" / "data" / "analytics" / "paid_ads_performance.json"
MD_OUTPUT = BASE_DIR / "07_REPORTS" / "docs" / "PAID_ADS_TRACKING_LATEST.md"

def classify_hub(page_path: str, host_name: str = "www.momo.vn") -> str:
    if "napthengay.vn" in host_name:
        return "Nạp Thẻ Ngay (Telco & Game)"
    path = page_path.lower()
    if any(k in path for k in ["/game/", "/nap-xu-tiktok", "/nap-the-game", "/uu-dai-icloud", "nap-game"]):
        return "Game & Telco"
    if any(k in path for k in ["/diem-tin-dung", "/vi-tra-sau", "/tai-chinh", "cic", "no-xau", "the-tin-dung", "vay"]):
        return "Financial Hub"
    if any(k in path for k in ["vietlott", "xo-so", "power-6-55", "mega-6-45", "max-3d"]):
        return "Lottery Hub"
    if any(k in path for k in ["bao-hiem", "phat-nguoi", "xe-may", "o-to", "gara"]):
        return "Vehicle & Insurtech"
    if any(k in path for k in ["loa-thong-bao", "merchant", "doi-tac"]):
        return "Merchant Hub"
    if any(k in path for k in ["/cinema", "rap", "phim", "ve-xem-phim"]):
        return "Cinema Hub"
    if path == "/" or "thong-cao-bao-chi" in path or "better-choice" in path:
        return "Branding & PR"
    return "Other / General"

def fetch_paid_ads(start_date: str, end_date: str):
    token = get_access_token()
    print(f"-> Truy van GA4 Data API Property {PROPERTY_ID} cho ky {start_date} -> {end_date}...")

    # 1. Truy vấn Pageviews, Sessions, Users theo HostName, Page, SourceMedium, Campaign, Content
    body_ads = {
        "dateRanges": [{"startDate": start_date, "endDate": end_date}],
        "dimensions": [
            {"name": "hostName"},
            {"name": "pagePath"},
            {"name": "sessionSourceMedium"},
            {"name": "sessionCampaignName"},
            {"name": "sessionManualAdContent"}
        ],
        "metrics": [
            {"name": "screenPageViews"},
            {"name": "sessions"},
            {"name": "totalUsers"}
        ],
        "dimensionFilter": {
            "orGroup": {
                "expressions": [
                    {"filter": {"fieldName": "sessionMedium", "stringFilter": {"matchType": "EXACT", "value": "cpc"}}},
                    {"filter": {"fieldName": "sessionMedium", "stringFilter": {"matchType": "EXACT", "value": "paid"}}},
                    {"filter": {"fieldName": "sessionMedium", "stringFilter": {"matchType": "EXACT", "value": "NativeAds"}}},
                    {"filter": {"fieldName": "sessionMedium", "stringFilter": {"matchType": "EXACT", "value": "ads"}}},
                    {"filter": {"fieldName": "sessionCampaignName", "stringFilter": {"matchType": "EXACT", "value": "(cross-network)"}}}
                ]
            }
        },
        "orderBys": [{"metric": {"metricName": "screenPageViews"}, "desc": True}],
        "limit": 1000
    }
    res_ads = run_ga4_report(token, body_ads)
    rows_ads = res_ads.get("rows", [])
    print(f"✓ Nhan {len(rows_ads)} ban ghi Ads phu hop tu GA4.")

    # 2. Truy vấn sự kiện chuyển đổi Web-to-App (click_to_app & in-game installs)
    body_conv = {
        "dateRanges": [{"startDate": start_date, "endDate": end_date}],
        "dimensions": [
            {"name": "hostName"},
            {"name": "pagePath"},
            {"name": "eventName"},
            {"name": "sessionSourceMedium"}
        ],
        "metrics": [{"name": "eventCount"}],
        "dimensionFilter": {
            "orGroup": {
                "expressions": [
                    {"filter": {"fieldName": "eventName", "stringFilter": {"matchType": "EXACT", "value": "click_to_app"}}},
                    {"filter": {"fieldName": "eventName", "stringFilter": {"matchType": "EXACT", "value": "gmc_1vuquyt_install"}}},
                    {"filter": {"fieldName": "eventName", "stringFilter": {"matchType": "EXACT", "value": "gmc_1vuquyt_clickplay"}}}
                ]
            }
        },
        "limit": 1000
    }
    res_conv = run_ga4_report(token, body_conv)
    rows_conv = res_conv.get("rows", [])

    # Map chuyển đổi theo (host, path)
    page_conv = defaultdict(lambda: {"w2a_clicks": 0, "installs": 0, "clickplay": 0, "by_source": defaultdict(int)})
    for r in rows_conv:
        host = r["dimensionValues"][0]["value"]
        path = r["dimensionValues"][1]["value"]
        evt = r["dimensionValues"][2]["value"]
        sm = r["dimensionValues"][3]["value"]
        cnt = int(r["metricValues"][0]["value"])
        key = (host, path)
        if evt == "click_to_app":
            page_conv[key]["w2a_clicks"] += cnt
            page_conv[key]["by_source"][sm] += cnt
        elif evt == "gmc_1vuquyt_install":
            page_conv[key]["installs"] += cnt
        elif evt == "gmc_1vuquyt_clickplay":
            page_conv[key]["clickplay"] += cnt

    # 3. Tổng hợp dữ liệu
    total_paid_pv = 0
    total_paid_sessions = 0
    pages_map = defaultdict(lambda: {
        "pv": 0,
        "sessions": 0,
        "users": 0,
        "channels": defaultdict(int),
        "campaigns": set(),
        "creatives": set()
    })
    channels_summary = defaultdict(lambda: {"pv": 0, "sessions": 0, "pages": set()})

    for r in rows_ads:
        host = r["dimensionValues"][0]["value"]
        path = r["dimensionValues"][1]["value"]
        sm = r["dimensionValues"][2]["value"]
        camp = r["dimensionValues"][3]["value"]
        ad = r["dimensionValues"][4]["value"]
        pv = int(r["metricValues"][0]["value"])
        sess = int(r["metricValues"][1]["value"])
        u = int(r["metricValues"][2]["value"])

        total_paid_pv += pv
        total_paid_sessions += sess

        key = (host, path)
        p = pages_map[key]
        p["pv"] += pv
        p["sessions"] += sess
        p["users"] += u
        p["channels"][sm] += pv
        if camp and camp not in ["(not set)", "(organic)", "(referral)"]:
            p["campaigns"].add(camp)
        if ad and ad not in ["(not set)", "(none)"]:
            p["creatives"].add(ad)

        channels_summary[sm]["pv"] += pv
        channels_summary[sm]["sessions"] += sess
        channels_summary[sm]["pages"].add(f"{host}{path}")

    # Chuyển đổi pages_map thành danh sách
    pages_list = []
    for (host, path), data in pages_map.items():
        hub = classify_hub(path, host)
        conv = page_conv[(host, path)]
        w2a = conv["w2a_clicks"] or conv["installs"]
        cvr = round((w2a / data["sessions"] * 100), 2) if data["sessions"] > 0 else 0.0

        top_channels = sorted(data["channels"].items(), key=lambda x: x[1], reverse=True)
        full_url = f"https://{host}{path}"
        pages_list.append({
            "host_name": host,
            "page_path": path,
            "full_url": full_url,
            "hub": hub,
            "pageviews": data["pv"],
            "sessions": data["sessions"],
            "users": data["users"],
            "w2a_conversions": w2a,
            "cvr_percent": cvr,
            "primary_channel": top_channels[0][0] if top_channels else "N/A",
            "channels_breakdown": dict(top_channels),
            "campaigns": list(data["campaigns"])[:5],
            "creatives": list(data["creatives"])[:5]
        })

    pages_list.sort(key=lambda x: x["pageviews"], reverse=True)

    # Channels list
    channels_list = []
    for sm, cdata in channels_summary.items():
        share = round((cdata["pv"] / total_paid_pv * 100), 2) if total_paid_pv > 0 else 0.0
        channels_list.append({
            "channel": sm,
            "pageviews": cdata["pv"],
            "sessions": cdata["sessions"],
            "share_percent": share,
            "active_pages_count": len(cdata["pages"])
        })
    channels_list.sort(key=lambda x: x["pageviews"], reverse=True)

    # Build payload
    payload = {
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "date_range": {"start_date": start_date, "end_date": end_date},
        "summary": {
            "total_paid_pageviews": total_paid_pv,
            "total_paid_sessions": total_paid_sessions,
            "active_landing_pages_count": len(pages_list),
            "active_channels_count": len(channels_list)
        },
        "channels": channels_list,
        "landing_pages": pages_list
    }

    # 4. Ghi file JSON SSOT
    JSON_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(JSON_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"✓ Đã lưu SSOT JSON: {JSON_OUTPUT}")

    # 5. Ghi file Markdown Report
    generate_markdown_report(payload)

    # 6. In Terminal Report chuẩn Tech/Product Lead
    print_terminal_report(payload)

def generate_markdown_report(data):
    pvs = data["summary"]["total_paid_pageviews"]
    sess = data["summary"]["total_paid_sessions"]
    cnt = data["summary"]["active_landing_pages_count"]
    dr = data["date_range"]

    md = f"""# BÁO CÁO THEO DÕI PAID ADS & UTM WEB PLATFORM
> **Chu kỳ đo lường:** `{dr['start_date']}` -> `{dr['end_date']}`  
> **Cập nhật lúc:** `{data['updated_at']}` | **Nguồn:** GA4 Data API (Property 270743103)  
> **Tổng Paid Pageviews:** **{pvs:,} PV** | **Paid Sessions:** **{sess:,}** | **Số trang nhận Ads:** **{cnt} trang**

---

## 1. PHÂN BỔ LƯU LƯỢNG THEO KÊNH MEDIA TRẢ PHÍ

| Kênh Media (`Source / Medium`) | Pageviews (PV) | Sessions | Tỷ trọng PV | Số Landing Pages |
| :--- | :--- | :--- | :--- | :--- |
"""
    for ch in data["channels"][:10]:
        md += f"| `{ch['channel']}` | **{ch['pageviews']:,}** | {ch['sessions']:,} | {ch['share_percent']}% | {ch['active_pages_count']} |\n"

    md += """
---

## 2. TOP TRANG WEB ĐANG CHẠY ADS (XẾP THEO PAGEVIEW)

| Trang Web (`Domain + Path`) | Hub sản phẩm | Kênh chủ đạo | Pageviews Ads | W2A Convs | CVR (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
"""
    for p in data["landing_pages"][:30]:
        display_name = f"{p['host_name']}{p['page_path']}"
        md += f"| [`{display_name}`]({p['full_url']}) | {p['hub']} | `{p['primary_channel']}` | **{p['pageviews']:,}** | {p['w2a_conversions']:,} | {p['cvr_percent']}% |\n"

    md += """
---

## 3. ĐÁNH GIÁ CHẤT LƯỢNG & RỦI RO
- **Phân định tên miền SSOT:** GA4 Property 270743103 ghi nhận đồng thời cả `www.momo.vn` và cổng nạp `napthengay.vn`. Các đường dẫn phễu thanh toán như `/order/first-buy/`, `/confirmorder`, `/payments` thuộc về `napthengay.vn` (không phải `www.momo.vn`).
- **Kênh Google Search Ads:** Chiếm phần lớn ngân sách, phục vụ các trang có ý định chuyển đổi trực tiếp (Nạp xu, Điểm tín dụng, Mở ví, Mua bảo hiểm).
- **TikTok Ads & Affiliate Entercode:** Lưu ý kiểm tra tỷ lệ cài đặt/chuyển đổi thực tế trên các trang game/quảng bá để tránh lãng phí ngân sách.
- **Admicro Native Ads:** Phục vụ chủ đạo bài truyền thông PR thương hiệu.
"""
    MD_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(MD_OUTPUT, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✓ Đã xuất bản Markdown Report: {MD_OUTPUT}")

def print_terminal_report(data):
    s = data["summary"]
    dr = data["date_range"]
    print("\n" + "=" * 80)
    print("BÁO CÁO HIỆU SUẤT PAID ADS & UTM WEB PLATFORM")
    print(f"Chu kỳ: {dr['start_date']} -> {dr['end_date']} | Cập nhật: {data['updated_at']}")
    print(f"Tổng Paid PV: {s['total_paid_pageviews']:,} | Sessions: {s['total_paid_sessions']:,} | Số trang chạy Ads: {s['active_landing_pages_count']}")
    print("=" * 80)

    print("\n[1] PHÂN BỔ THEO KÊNH MEDIA:")
    for ch in data["channels"][:6]:
        print(f" - {ch['channel']:<35} : {ch['pageviews']:>8,} PV ({ch['share_percent']:>5.1f}%) | {ch['active_pages_count']:>2} pages")

    print("\n[2] TOP 15 TRANG ĐANG CHẠY ADS LỚN NHẤT:")
    for idx, p in enumerate(data["landing_pages"][:15], 1):
        display_name = f"{p['host_name']}{p['page_path']}"
        print(f" {idx:02d}. {display_name:<50} [{p['hub']}]")
        print(f"     PV: {p['pageviews']:>7,} | Kênh chính: {p['primary_channel']:<22} | W2A: {p['w2a_conversions']:>5,} (CVR: {p['cvr_percent']}%)")
    print("=" * 80 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Sync Paid Ads & UTM tracking from GA4 API")
    now = datetime.now()
    default_start = f"{now.year}-{now.month:02d}-01"
    parser.add_argument("--start", default=default_start, help=f"Start date (default: {default_start})")
    parser.add_argument("--end", default="today", help="End date (default: today)")
    args = parser.parse_args()

    fetch_paid_ads(args.start, args.end)

if __name__ == "__main__":
    main()
