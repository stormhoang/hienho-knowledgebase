#!/usr/bin/env python3
"""
AUTOMATED ROOT CAUSE ANALYSIS (RCA) ENGINE
Phân tích nguyên nhân gốc rễ và đề xuất hành động tối ưu cho Web Platform.

Quy trình chẩn đoán 4 bước chuẩn Product Lead:
1. Hiện tượng (Symptom): Đo lường độ lệch giữa thực tế (Actual) và mục tiêu (Target).
2. Phân rã đa chiều (Decomposition): Non-Paid vs Paid -> Hubs -> URLs -> Search Queries.
3. Nguyên nhân gốc rễ (Root Cause): Tách bạch giữa sụt giảm lưu lượng (Top of funnel) hay sụt giảm CVR (Bottom of funnel).
4. Đơn thuốc hành động (Prescription): Kế hoạch hành động P0/P1/P2 kèm đội ngũ chịu trách nhiệm và ROI kỳ vọng.
"""

import sys
import argparse
import json
import calendar
from datetime import date
from pathlib import Path
from tabulate import tabulate

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.db import (
    get_connection,
    DEFAULT_DB_PATH,
    DATA_DIR,
    query_hubs_summary,
    query_top_w2a_drivers,
    query_quick_wins
)
from scripts.detect_anomalies import (
    detect_macro_anomalies,
    detect_hub_anomalies,
    detect_w2a_breakage_anomalies,
    detect_search_ranking_slips
)


def format_table(headers, rows):
    return tabulate(rows, headers=headers, tablefmt="github")


def validate_snapshot(data, as_of):
    errors = []
    actual = data.get("actual_mtd_pv")
    target = data.get("target_pv", data.get("target_oct_pv"))
    channels = data.get("channels", {})
    if data.get("days_in_month") != calendar.monthrange(as_of.year, as_of.month)[1]:
        errors.append("days_in_month không khớp lịch")
    if not isinstance(actual, (int, float)) or not isinstance(target, (int, float)) or target <= 0:
        errors.append("thiếu actual_mtd_pv hoặc target_pv hợp lệ")
        return errors
    try:
        non_paid = channels["non_paid_total"]["pv"]
        paid = channels["paid"]["pv"]
        parts = sum(channels[key]["pv"] for key in ("organic", "direct", "referral", "others"))
        if non_paid + paid != actual or parts != non_paid:
            errors.append("tổng kênh không khớp tổng PV")
    except (KeyError, TypeError):
        errors.append("thiếu phân rã kênh")
    if abs(data.get("progress_pct", 0) - actual / target * 100) > 0.02:
        errors.append("progress_pct không khớp actual/target")
    if abs(data.get("daily_pace", 0) - actual / as_of.day) > 1:
        errors.append("daily_pace không khớp actual/days_elapsed")
    if abs(data.get("forecast_31d", 0) - actual / as_of.day * data["days_in_month"]) > 2:
        errors.append("forecast không khớp số ngày trong tháng")
    return errors


def select_snapshot(month=None, data_dir=DATA_DIR, today=None):
    today = today or date.today()
    month = month or today.strftime("%Y-%m")
    year, month_number = map(int, month.split("-"))
    prefix = f"monthly_{month_number:02d}_{year}"
    candidates = list(data_dir.glob(f"{prefix}_mtd_*d.json"))
    candidates += list(data_dir.glob(f"{prefix}_consolidated.json"))
    if not candidates:
        raise ValueError(f"Không có snapshot cho {month}; không dùng dữ liệu tháng khác.")
    def rank(path):
        with path.open(encoding="utf-8") as handle:
            payload = json.load(handle)
        return payload.get("days_elapsed", -1), path.stat().st_mtime
    path = max(candidates, key=rank)
    data = json.loads(path.read_text(encoding="utf-8"))
    days = data.get("days_elapsed")
    if not isinstance(days, int) or not 1 <= days <= calendar.monthrange(year, month_number)[1]:
        raise ValueError(f"Snapshot {path.name} có days_elapsed không hợp lệ")
    if (year, month_number) == (today.year, today.month) and days > today.day:
        raise ValueError(f"Snapshot {path.name} ghi nhận ngày tương lai")
    return path, data, date(year, month_number, days)


def run_full_diagnosis(target_hub=None, month=None):
    print("=" * 80)
    print("HỆ THỐNG CHẨN ĐOÁN HIỆU SUẤT VÀ NGUYÊN NHÂN GỐC RỄ (ROOT CAUSE ANALYSIS)")
    print("=" * 80)

    # 1. Nạp snapshot MTD mới nhất (ưu tiên file consolidated SSOT)
    latest_snapshot_file, mtd_data, data_as_of = select_snapshot(month)
    errors = validate_snapshot(mtd_data, data_as_of)
    if errors:
        raise ValueError(f"Snapshot {latest_snapshot_file.name} không nhất quán: {', '.join(errors)}")
    print(f"Nguồn: {latest_snapshot_file.relative_to(REPO_ROOT)} | Dữ liệu đến: {data_as_of}")

    days_elapsed = mtd_data.get("days_elapsed", 0)
    days_in_month = mtd_data.get("days_in_month", 31)
    target_pv = mtd_data.get("target_pv", mtd_data.get("target_oct_pv"))
    if not target_pv:
        raise ValueError(f"Snapshot {latest_snapshot_file.name} thiếu target_pv")
    actual_pv = mtd_data.get("actual_mtd_pv", 0)
    progress_pct = mtd_data.get("progress_pct", 0.0)
    daily_pace = mtd_data.get("daily_pace", 0.0)
    daily_needed = mtd_data.get("daily_needed", 0.0)
    forecast_31d = mtd_data.get("forecast_31d", 0.0)
    forecast_pct = mtd_data.get("forecast_pct", 0.0)

    # BƯỚC 1: TRIỆU CHỨNG (SYMPTOM)
    print("\n[BƯỚC 1: ĐO LƯỜNG TRIỆU CHỨNG & TIẾN ĐỘ MỤC TIÊU]")
    symptom_table = [
        ["Chu kỳ đánh giá", f"MTD {days_elapsed} ngày (tiến độ thời gian: {days_elapsed/days_in_month*100:.1f}%)"],
        ["Mục tiêu tháng (Target)", f"{target_pv:,} PV"],
        ["Thực tế lũy kế (Actual)", f"{actual_pv:,} PV ({progress_pct:.2f}% target)"],
        ["Nhịp độ hiện tại (Pace)", f"{daily_pace:,.0f} PV/ngày"],
        ["Nhịp độ cần đạt (Required)", f"{daily_needed:,.0f} PV/ngày"],
        ["Dự báo kết tháng (Forecast)", f"{forecast_31d:,.0f} PV ({forecast_pct:.2f}% target)"],
    ]
    print(format_table(["Chỉ số", "Giá trị thực tế"], symptom_table))

    status = "ON TRACK" if forecast_pct >= 100.0 else "AT RISK"
    gap = forecast_31d - target_pv
    print(f"\n-> Nhận định vĩ mô: Trạng thái [{status}], Chênh lệch dự báo: {gap:+,.0f} PV.")

    # BƯỚC 2: PHÂN RÃ ĐA CHIỀU (DECOMPOSITION)
    print("\n" + "-" * 80)
    print("[BƯỚC 2: PHÂN RÃ NGUỒN LƯU LƯỢNG & CƠ CẤU HUBS]")
    
    # 2.1 Non-Paid vs Paid
    ch = mtd_data.get("channels", {})
    non_paid = ch.get("non_paid_total", {})
    paid = ch.get("paid", {})
    org = ch.get("organic", {})
    direct = ch.get("direct", {})
    ref = ch.get("referral", {})
    others = ch.get("others", {})

    channel_table = [
        ["Non-Paid Traffic (Tự nhiên)", f"{non_paid.get('pv', 0):,}", f"{non_paid.get('pct', 0):.2f}%", "Động cơ bền vững cốt lõi"],
        ["  - Organic Search", f"{org.get('pv', 0):,}", f"{org.get('pct', 0):.2f}%", "Kênh chủ lực"],
        ["  - Direct", f"{direct.get('pv', 0):,}", f"{direct.get('pct', 0):.2f}%", "Sức mạnh thương hiệu"],
        ["  - Referral", f"{ref.get('pv', 0):,}", f"{ref.get('pct', 0):.2f}%", "Đối tác ngoài"],
        ["  - Others", f"{others.get('pv', 0):,}", f"{others.get('pct', 0):.2f}%", "Traffic chưa gắn UTM"],
        ["Paid Traffic (Quảng cáo)", f"{paid.get('pv', 0):,}", f"{paid.get('pct', 0):.2f}%", "Traffic mua bổ trợ"],
    ]
    print(format_table(["Phân tầng Kênh", "Lũy kế PV", "Tỷ trọng %", "Định vị"], channel_table))

    # 2.2 Hub Breakdown
    hubs = mtd_data.get("hubs", {})
    hub_table = []
    lagging_hubs = []
    for hkey, hinfo in hubs.items():
        hpv = hinfo.get("pv", 0)
        htarget = hinfo.get("target", 0)
        hpct = hinfo.get("pct", 0.0)
        # Kỳ vọng tuyến tính theo ngày
        expected_pct = (days_elapsed / days_in_month) * 100
        delta_pct = hpct - expected_pct
        status_hub = "Đạt pace" if delta_pct >= 0 else "Chậm tiến độ"
        if delta_pct < -5.0:
            lagging_hubs.append((hkey, delta_pct, hpv, htarget))
        hub_table.append([
            hkey.upper(),
            f"{hpv:,}",
            f"{htarget:,}" if htarget else "N/A",
            f"{hpct:.1f}%",
            f"{expected_pct:.1f}%",
            f"{delta_pct:+.1f}%",
            status_hub
        ])
    print("\nBảng phân rã tiến độ các Hubs:")
    print(format_table(["Hub", "Lũy kế PV", "Target Tháng", "Tiến độ đạt", "Tiến độ chuẩn", "Độ lệch %", "Trạng thái"], hub_table))

    # BƯỚC 3: PHÂN TÍCH NGUYÊN NHÂN GỐC RỄ (ROOT CAUSE)
    print("\n" + "-" * 80)
    print("[BƯỚC 3: CHẨN ĐOÁN NGUYÊN NHÂN GỐC RỄ (ROOT CAUSE)]")
    
    conn = get_connection()
    db_latest = conn.execute("SELECT MAX(date) FROM fact_daily_performance").fetchone()[0]
    fact = conn.execute("SELECT total_pv FROM fact_daily_performance WHERE date = ?", (data_as_of.isoformat(),)).fetchone()
    if db_latest != data_as_of.isoformat() or not fact or fact[0] != actual_pv:
        conn.close()
        print(f"\n[DATA GAP] Fact Data Mart chỉ đến {db_latest} hoặc khác snapshot {data_as_of}. Không phân tích nguyên nhân gốc rễ khác kỳ.")
        return
    print("\n[DATA GAP] GA4 landing pages và GSC search analytics không có period_start/period_end. Chưa thể xác nhận cùng kỳ với snapshot; không phân tích phễu, ranking hoặc nguyên nhân gốc rễ.")
    conn.close()
    return
    cur = conn.cursor()

    # 3.1 Funnel Health: Traffic Volume vs W2A Conversion
    cur.execute("""
        SELECT 
            hub_name,
            total_sessions,
            engaged_sessions,
            engagement_rate_pct,
            w2a_clicks,
            w2a_cvr_pct
        FROM v_hub_performance
        WHERE total_sessions > 10000
        ORDER BY total_sessions DESC;
    """)
    hub_funnel = cur.fetchall()

    print("\n1. Phân tích chất lượng phễu (Traffic vs. Chuyển đổi Web-to-App):")
    funnel_rows = []
    for hf in hub_funnel:
        funnel_rows.append([
            hf["hub_name"],
            f"{hf['total_sessions']:,}",
            f"{hf['engagement_rate_pct']:.1f}%",
            f"{hf['w2a_clicks']:,}",
            f"{hf['w2a_cvr_pct']:.2f}%"
        ])
    print(format_table(["Hub Name", "Sessions", "Engagement Rate", "W2A Clicks", "W2A CVR"], funnel_rows))

    # 3.2 Tách bạch nguyên nhân của Hub chậm tiến độ
    print("\n2. Xác định điểm nghẽn của các Hub chậm tiến độ:")
    if lagging_hubs:
        for lh in lagging_hubs:
            hname, diff, pv, tgt = lh
            print(f"-> Hub [{hname.upper()}]: Tiến độ thực tế đang trễ {abs(diff):.1f}% so với tiến độ chuẩn.")
            if hname == "financial":
                print("   * Bản chất: Nhu cầu tìm kiếm bị phân tán, thiếu các Content Cluster bao phủ ngách tài chính cá nhân.")
                print("   * Điểm nghẽn: Tỷ lệ index các bài blog mới chậm và thiếu liên kết nội bộ (Internal Silo) từ các bài traffic cao sang landing page chuyển đổi.")
            elif hname == "new_user":
                print("   * Bản chất: Phụ thuộc vào các chương trình khuyến mãi ngắn hạn; thiếu các trang tiện ích evergreen thu hút người dùng mới tự nhiên.")
            elif hname == "vehicle":
                print("   * Bản chất: Lưu lượng tập trung 85% vào trang Phạt Nguội; chưa khai thác hết ngách Phí không dừng và Đăng kiểm.")
    else:
        print("-> Toàn bộ các Hub chính đều đang duy trì nhịp độ bám sát hoặc vượt chỉ tiêu.")

    # 3.3 Quick Wins Opportunities (Search Engine Signals)
    cur.execute("""
        SELECT query, page_url, impressions, clicks, ctr_pct, avg_position, potential_gain
        FROM v_keyword_quick_wins
        WHERE impressions >= 50000
        ORDER BY potential_gain DESC
        LIMIT 5;
    """)
    qw_rows = cur.fetchall()
    print("\n3. Cơ hội tăng trưởng nhanh từ Search Console (High Impressions, Position 4-15, Low CTR):")
    qw_table = []
    for r in qw_rows:
        path = r["page_url"].replace("https://www.momo.vn", "")
        if len(path) > 35:
            path = path[:32] + "..."
        qw_table.append([
            r["query"],
            path,
            f"{r['impressions']:,}",
            f"{r['clicks']:,}",
            f"{r['ctr_pct']:.2f}%",
            f"{r['avg_position']:.1f}",
            f"{int(r['potential_gain']):,}"
        ])
    print(format_table(["Query", "URL Path", "Impressions", "Clicks", "CTR", "Pos", "Potential PV Gain"], qw_table))

    # 3.4 Quét dị biệt tự động (Automated Anomaly Alerts)
    anomalies = []
    anomalies.extend(detect_macro_anomalies(conn))
    anomalies.extend(detect_hub_anomalies(conn))
    anomalies.extend(detect_w2a_breakage_anomalies(conn))
    anomalies.extend(detect_search_ranking_slips())

    print("\n4. Cảnh báo dị biệt hệ thống tự động phát hiện:")
    if anomalies:
        anom_table = []
        for a in anomalies[:5]:
            anom_table.append([a["severity"], a["vector"], a["entity"], a["metric"], a["action"]])
        print(format_table(["Mức độ", "Véc-tơ", "Thực thể", "Chỉ số", "Khuyến nghị xử lý"], anom_table))
    else:
        print("-> Không phát hiện dị biệt nghiêm trọng nào.")

    # BƯỚC 4: ĐƠN THUỐC HÀNH ĐỘNG (PRESCRIPTION)
    print("\n" + "-" * 80)
    print("[BƯỚC 4: ĐƠN THUỐC HÀNH ĐỘNG CỤ THỂ (ACTIONABLE PRESCRIPTION)]")
    
    actions = [
        ["P0", "SEO Vendor & Content Team", "Tối ưu CTR Title/Meta Snippet cho 5 cụm từ khóa Quick Wins (>50K imp, Pos 4-10)", "Ước tính mang lại +15,000 đến +25,000 clicks tự nhiên trong 14 ngày mà không tốn chi phí Ads."],
        ["P0", "Web Dev", "Kiểm tra và chuẩn hóa tracking OneLink W2A trên các trang tin tức/khuyến mãi có CVR cao (>15%)", "Bảo toàn số liệu chuyển đổi New User thực chất, tránh suy hao attribution."],
        ["P1", "Product Lead & Content Team", "Mở rộng 15 Topic Clusters ngách cho Financial Hub (Theme Vay, Tỷ giá, Tiết kiệm)", "Kéo tiến độ Financial Hub từ 44% lên 75% target cuối tháng 11."],
        ["P1", "Web Dev & Tech Lead", "Tối ưu hóa Core Web Vitals (LCP < 2.5s) cho nhóm Top 20 Landing Pages rạp phim Cinema", "Giữ vững vị thế Top 1 Google cho mùa phim bom tấn cuối năm."],
        ["P2", "Media Team", "Rà soát hiệu quả Paid Ads, cắt giảm các chiến dịch có W2A CVR < 1.0% và tái phân bổ sang Non-Paid content", "Tối ưu hóa ngân sách và gia tăng tỷ trọng Non-Paid Traffic lên trên 88%."]
    ]
    print(format_table(["Ưu tiên", "Đội ngũ chịu trách nhiệm", "Hành động cụ thể", "Tác động kinh doanh dự kiến (ROI)"], actions))
    print("=" * 80)
    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Automated RCA Engine")
    parser.add_argument("--hub", type=str, default=None, help="Chỉ định Hub cần chẩn đoán chuyên sâu")
    parser.add_argument("--month", type=str, help="Kỳ YYYY-MM, mặc định tháng hiện tại")
    args = parser.parse_args()

    try:
        run_full_diagnosis(target_hub=args.hub, month=args.month)
    except ValueError as exc:
        parser.exit(2, f"[ERROR] {exc}\n")


if __name__ == "__main__":
    main()
