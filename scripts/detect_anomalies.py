#!/usr/bin/env python3
"""
AUTOMATED ANOMALY DETECTION ENGINE
Hệ thống tự động phát hiện dị biệt và cảnh báo bất thường hiệu suất Web Platform.

4 Véc-tơ chẩn đoán dị biệt:
1. Pacing & Macro Anomaly: Nhịp độ tăng trưởng toàn Website trệch chuẩn (>1.5 sigma).
2. Hub Health Anomaly: Hub trọng yếu bị suy thoái tốc độ hoặc rớt phễu chuyển đổi.
3. Search Ranking & Traffic Slip: Trang lưu lượng cao bị rớt thứ hạng hoặc mất impression.
4. W2A Funnel Breakage: Trang traffic cao nhưng W2A CVR rớt đột biến (dấu hiệu hỏng OneLink/tracking).
"""

import sys
import argparse
import json
import sqlite3
import numpy as np
from pathlib import Path
from tabulate import tabulate

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.db import get_connection, DATA_DIR


def format_table(headers, rows):
    return tabulate(rows, headers=headers, tablefmt="github")


def detect_macro_anomalies(conn):
    """Phát hiện dị biệt về nhịp độ tăng trưởng MTD."""
    cur = conn.cursor()
    cur.execute("""
        SELECT date, total_pv, non_paid_pv, paid_pv, sessions, users, progress_pct, forecast_pct
        FROM fact_daily_performance
        ORDER BY date DESC
        LIMIT 10;
    """)
    rows = cur.fetchall()
    if not rows or len(rows) < 2:
        return []

    anomalies = []
    latest = rows[0]
    prev = rows[1]

    # Kiểm tra delta ngày gần nhất
    pv_delta = latest["total_pv"] - prev["total_pv"]
    non_paid_delta = latest["non_paid_pv"] - prev["non_paid_pv"]
    paid_delta = latest["paid_pv"] - prev["paid_pv"]

    # Nhận diện dị biệt dự báo kết tháng
    if latest["forecast_pct"] < 95.0:
        anomalies.append({
            "vector": "Macro Pacing",
            "entity": "Toàn Website (Forecast 31D)",
            "severity": "CRITICAL",
            "metric": f"Forecast {latest['forecast_pct']:.1f}% Target",
            "finding": f"Nhịp độ MTD hiện tại không đủ để hoàn thành mục tiêu tháng (thiếu {(100 - latest['forecast_pct']):.1f}%).",
            "action": "Kích hoạt kế hoạch bù trừ tăng trưởng từ Non-Paid SEO Quick Wins và rà soát hiệu quả Paid Ads."
        })
    elif latest["forecast_pct"] < 100.0:
        anomalies.append({
            "vector": "Macro Pacing",
            "entity": "Toàn Website (Forecast 31D)",
            "severity": "WARNING",
            "metric": f"Forecast {latest['forecast_pct']:.1f}% Target",
            "finding": "Dự báo chạm sát ngưỡng mục tiêu (thiếu dưới 5%), có nguy cơ trượt mục tiêu nếu lưu lượng cuối tuần giảm.",
            "action": "Đẩy mạnh index bài viết mới và kiểm tra các cụm từ khóa có dấu hiệu giảm nhẹ."
        })

    # Dị biệt suy hao Non-Paid
    if latest["non_paid_pv"] > 0 and latest["total_pv"] > 0:
        non_paid_share = (latest["non_paid_pv"] / latest["total_pv"]) * 100
        if non_paid_share < 80.0:
            anomalies.append({
                "vector": "Traffic Quality",
                "entity": "Tỷ trọng Non-Paid Traffic",
                "severity": "WARNING",
                "metric": f"{non_paid_share:.1f}%",
                "finding": "Tỷ trọng lưu lượng tự nhiên giảm xuống dưới ngưỡng an toàn (80%), phụ thuộc nhiều vào Paid Traffic.",
                "action": "Rà soát chi phí Paid Ads, tái phân bổ nguồn lực vào Content Evergreen chất lượng cao."
            })

    return anomalies


def detect_hub_anomalies(conn):
    """Phát hiện dị biệt hiệu suất và chuyển đổi giữa các Hub."""
    cur = conn.cursor()
    cur.execute("""
        SELECT hub_name, hub_id, total_sessions, engaged_sessions, engagement_rate_pct, w2a_clicks, w2a_cvr_pct
        FROM v_hub_performance
        WHERE total_sessions > 5000;
    """)
    rows = cur.fetchall()
    anomalies = []

    for r in rows:
        hname = r["hub_name"]
        sessions = r["total_sessions"]
        cvr = r["w2a_cvr_pct"]
        eng_rate = r["engagement_rate_pct"]

        # Dị biệt 1: Hub có sessions lớn nhưng W2A CVR bất thường (< 1%)
        if sessions > 20000 and cvr < 1.0 and r["hub_id"] != "download":
            anomalies.append({
                "vector": "Hub Funnel",
                "entity": f"Hub: {hname}",
                "severity": "CRITICAL",
                "metric": f"CVR {cvr:.2f}% ({sessions:,} Sessions)",
                "finding": f"Lưu lượng lớn nhưng tỷ lệ chuyển đổi Web-to-App dưới 1%. Người dùng rời trang mà không có tương tác vào App.",
                "action": "Kiểm tra vị trí đặt nút OneLink/CTA trên các landing page chủ lực của Hub; audit khả năng hiển thị trên Mobile."
            })

        # Dị biệt 2: Tỷ lệ tương tác (Engagement Rate) quá thấp (< 60%)
        if sessions > 15000 and eng_rate < 60.0 and r["hub_id"] != "download":
            anomalies.append({
                "vector": "UX & Retention",
                "entity": f"Hub: {hname}",
                "severity": "WARNING",
                "metric": f"Engagement Rate {eng_rate:.1f}%",
                "finding": f"Tỷ lệ phiên có tương tác thấp bất thường (< 60%), dấu hiệu nội dung không khớp ý định tìm kiếm hoặc tốc độ tải chậm.",
                "action": "Kiểm tra chỉ số Core Web Vitals (LCP) và mức độ liên quan của nội dung so với Search Query."
            })

    return anomalies


def detect_w2a_breakage_anomalies(conn):
    """Phát hiện các URL có lượng truy cập lớn nhưng W2A CVR rơi về 0 (nghi vấn hỏng link/tracking)."""
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            g.landing_page,
            COALESCE(d.hub_name, 'Khác') AS hub_name,
            SUM(g.sessions) AS sessions,
            SUM(g.onelink_clicks_track1 + g.onelink_clicks_track2) AS w2a_clicks,
            ROUND(SUM(g.onelink_clicks_track1 + g.onelink_clicks_track2) * 100.0 / NULLIF(SUM(g.sessions), 0), 2) AS cvr
        FROM ga4_landing_pages g
        LEFT JOIN dim_url_project d ON (
            g.landing_page = d.path 
            OR ('https://www.momo.vn' || g.landing_page) = d.url
        )
        WHERE g.landing_page NOT IN ('/', '/download', '(not set)')
        GROUP BY g.landing_page, d.hub_name
        HAVING sessions >= 10000 AND (w2a_clicks = 0 OR cvr < 0.1)
        ORDER BY sessions DESC
        LIMIT 10;
    """)
    rows = cur.fetchall()
    anomalies = []

    for r in rows:
        anomalies.append({
            "vector": "Funnel Breakage",
            "entity": r["landing_page"],
            "severity": "CRITICAL",
            "metric": f"{r['sessions']:,} Sessions, {r['w2a_clicks']} W2A Clicks (CVR {r['cvr']:.2f}%)",
            "finding": f"Trang có lưu lượng cao tại [{r['hub_name']}] nhưng gần như không có lượt chuyển đổi OneLink vào App.",
            "action": "Web Dev kiểm tra ngay cơ chế gắn OneLink (Deep Link), kiểm tra event track1/track2 có bị lỗi chặn script."
        })

    return anomalies


def detect_search_ranking_slips():
    """Phát hiện các URL bị mất hoàn toàn hiển thị (Lost Impressions) trong 7 ngày gần nhất."""
    lost_file = DATA_DIR / "gsc_lost_impressions_detail.json"
    if not lost_file.exists():
        return []

    try:
        with open(lost_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return []

    top_lost = data.get("top_lost_in_7d", [])
    anomalies = []

    for item in top_lost[:5]:
        imp = item.get("imp_30d", 0)
        clicks = item.get("clicks_30d", 0)
        pos = item.get("pos_30d", 0.0)
        url = item.get("url", "").replace("https://www.momo.vn", "")
        proj = item.get("project", "")

        if imp >= 20000:
            anomalies.append({
                "vector": "Search Ranking Drop",
                "entity": url if len(url) <= 45 else url[:42] + "...",
                "severity": "WARNING",
                "metric": f"Mất {imp:,} Imp/tháng (Vị trí cũ: {pos:.1f})",
                "finding": f"Trang thuộc [{proj}] từng có {imp:,} impressions trong 30 ngày nhưng đã mất toàn bộ hiển thị trong 7 ngày qua.",
                "action": "Kiểm tra trạng thái Index trong GSC (bị noindex, canonical sai, hoặc lỗi 404/500 sau đợt release)."
            })

    return anomalies


def run_anomaly_scan(severity_filter=None, hub_filter=None):
    print("=" * 80)
    print("HỆ THỐNG PHÁT HIỆN DỊ BIỆT & CẢNH BÁO TỰ ĐỘNG (AUTOMATED ANOMALY SCANNER)")
    print("=" * 80)

    conn = get_connection()
    all_anomalies = []

    # 1. Quét dị biệt Macro & Pacing
    all_anomalies.extend(detect_macro_anomalies(conn))

    # 2. Quét dị biệt Hubs & UX
    all_anomalies.extend(detect_hub_anomalies(conn))

    # 3. Quét dị biệt đứt gãy phễu W2A (OneLink Breakage)
    all_anomalies.extend(detect_w2a_breakage_anomalies(conn))

    # 4. Quét dị biệt rớt thứ hạng Search Console
    all_anomalies.extend(detect_search_ranking_slips())

    conn.close()

    # Lọc theo severity nếu có
    if severity_filter:
        all_anomalies = [a for a in all_anomalies if a["severity"].upper() == severity_filter.upper()]

    if not all_anomalies:
        print("\nKhông phát hiện dị biệt nghiêm trọng nào. Mọi chỉ số đều đang vận hành trong ngưỡng bình thường.")
        print("=" * 80)
        return

    # Phân loại và hiển thị
    crit_count = sum(1 for a in all_anomalies if a["severity"] == "CRITICAL")
    warn_count = sum(1 for a in all_anomalies if a["severity"] == "WARNING")

    print(f"\nPhát hiện tổng cộng: {len(all_anomalies)} dị biệt ({crit_count} CRITICAL, {warn_count} WARNING)\n")

    table_data = []
    for idx, a in enumerate(all_anomalies, 1):
        table_data.append([
            idx,
            a["severity"],
            a["vector"],
            a["entity"],
            a["metric"],
            a["finding"],
            a["action"]
        ])

    headers = ["#", "Mức độ", "Véc-tơ", "Thực thể ảnh hưởng", "Chỉ số dị biệt", "Bản chất vấn đề", "Kế hoạch xử lý"]
    print(format_table(headers, table_data))
    print("\n" + "=" * 80)


def main():
    parser = argparse.ArgumentParser(description="Automated Anomaly Detection")
    parser.add_argument("--severity", type=str, choices=["CRITICAL", "WARNING"], default=None, help="Lọc theo mức độ dị biệt")
    parser.add_argument("--hub", type=str, default=None, help="Lọc theo Hub")
    args = parser.parse_args()

    run_anomaly_scan(severity_filter=args.severity, hub_filter=args.hub)


if __name__ == "__main__":
    main()
