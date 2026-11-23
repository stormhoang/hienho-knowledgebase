#!/usr/bin/env python3
"""
CLI ANALYTICS QUERY TOOL
Cong cu tra cuu so lieu da chieu tuc thi tu SQLite Data Mart SSOT.
Cho phep truy van SQL tu do hoac chay cac goc nhin phan tich chuan hoa:
- Hieu suat Hubs & Chuyen doi W2A
- Top Landing Pages tao chuyen doi App
- Tu khoa Quick Wins (Top 4-15, nhieu impression, low CTR)
- Phan tich tu khoa canh tranh noi bo (Cannibalization)
- Chan doan Pheu chuyen doi Hub (Funnel Drop-off Diagnostics)
- Dinh luong dung luong thi truong & Co hoi Thuong mai (Market Sizing for BD)
"""

import sys
import argparse
import sqlite3
from pathlib import Path
from tabulate import tabulate

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.db import (
    get_connection,
    DEFAULT_DB_PATH,
    query_hubs_summary,
    query_top_w2a_drivers,
    query_quick_wins,
    query_gsc_hubs_summary,
    query_gsc_devices
)


def format_table(headers, rows):
    """Format markdown table without emojis."""
    return tabulate(rows, headers=headers, tablefmt="github")


def show_hubs():
    rows = query_hubs_summary()
    if not rows:
        print("Khong co du lieu Hubs.")
        return
    table_data = []
    for r in rows:
        table_data.append([
            r["hub_name"],
            f"{r['active_pages']:,}",
            f"{r['total_sessions']:,}",
            f"{r['engagement_rate_pct']:.1f}%",
            f"{r['w2a_clicks']:,}",
            f"{r['w2a_cvr_pct']:.2f}%"
        ])
    headers = ["Hub Name", "Active Pages", "Sessions", "Engagement Rate", "W2A Clicks", "W2A CVR"]
    print("\n--- BAO CAO HIEU SUAT TONG THE CAC HUBS ---")
    print(format_table(headers, table_data))


def show_seo_hubs():
    rows = query_gsc_hubs_summary()
    if not rows:
        print("Khong co du lieu SEO Hubs.")
        return
    table_data = []
    for r in rows:
        table_data.append([
            r["hub_name"],
            f"{r['pages_count']:,}",
            f"{r['total_clicks']:,}",
            f"{r['total_impressions']:,}",
            f"{r['avg_ctr']:.2f}%",
            f"{r['avg_position']:.2f}"
        ])
    headers = ["Hub Name", "Top Pages", "Total Clicks", "Total Imp", "Avg CTR", "Avg Pos"]
    print("\n--- HIỆU SUẤT SEO GOOGLE SEARCH CONSOLE 2026 THEO HUBS ---")
    print(format_table(headers, table_data))


def show_devices():
    rows = query_gsc_devices()
    if not rows:
        print("Khong co du lieu thiet bi.")
        return
    table_data = []
    total_clicks = sum(r["clicks"] for r in rows)
    for r in rows:
        share = (r["clicks"] / total_clicks * 100) if total_clicks > 0 else 0
        table_data.append([
            r["device"],
            f"{r['clicks']:,}",
            f"{share:.2f}%",
            f"{r['impressions']:,}",
            f"{r['ctr']:.2f}%",
            f"{r['position']:.2f}"
        ])
    headers = ["Thiết Bị", "Lượt Clicks", "Tỷ Trọng Clicks", "Lượt Hiển Thị", "CTR", "Vị Trí TB"]
    print("\n--- PHÂN TẦNG THIẾT BỊ GOOGLE SEARCH CONSOLE 2026 ---")
    print(format_table(headers, table_data))


def show_top_w2a(limit=15):
    rows = query_top_w2a_drivers(limit=limit)
    if not rows:
        print("Khong co du lieu W2A.")
        return
    table_data = []
    for r in rows:
        lp = r["landing_page"]
        if len(lp) > 45:
            lp = lp[:42] + "..."
        table_data.append([
            lp,
            r["hub_name"],
            r["primary_project"],
            f"{r['sessions']:,}",
            f"{r['total_w2a']:,}",
            f"{r['w2a_cvr_pct']:.2f}%"
        ])
    headers = ["Landing Page", "Hub", "Project", "Sessions", "W2A Clicks", "CVR"]
    print(f"\n--- TOP {limit} TRANG CHUYEN DOI WEB-TO-APP CAO NHAT ---")
    print(format_table(headers, table_data))


def show_quick_wins(limit=15, min_imp=1000):
    rows = query_quick_wins(min_impressions=min_imp, limit=limit)
    if not rows:
        print("Khong co tu khoa Quick Wins thoa dieu kien.")
        return
    table_data = []
    for r in rows:
        q = r["query"]
        if len(q) > 30:
            q = q[:27] + "..."
        url = r["page_url"].replace("https://www.momo.vn", "")
        if len(url) > 35:
            url = url[:32] + "..."
        table_data.append([
            q,
            url,
            f"{r['impressions']:,}",
            f"{r['clicks']:,}",
            f"{r['ctr_pct']:.2f}%",
            f"{r['avg_position']:.1f}",
            f"{int(r['potential_gain']):,}"
        ])
    headers = ["Query", "Path", "Impressions", "Clicks", "CTR", "Pos", "Potential Gain"]
    print(f"\n--- TOP {limit} TU KHOA QUICK WINS (POS 4-15, IMP >= {min_imp:,}) ---")
    print(format_table(headers, table_data))


def show_cannibalization(min_pages=2, limit=15):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            query,
            COUNT(DISTINCT page_url) AS page_count,
            SUM(impressions) AS total_imp,
            SUM(clicks) AS total_clicks,
            ROUND(AVG(position), 1) AS avg_pos
        FROM gsc_search_analytics
        GROUP BY query
        HAVING page_count >= ? AND total_imp >= 2000
        ORDER BY page_count DESC, total_imp DESC
        LIMIT ?;
    """, (min_pages, limit))
    rows = cur.fetchall()
    conn.close()

    table_data = []
    for r in rows:
        q = r["query"]
        if len(q) > 35:
            q = q[:32] + "..."
        table_data.append([
            q,
            r["page_count"],
            f"{r['total_imp']:,}",
            f"{r['total_clicks']:,}",
            f"{r['avg_pos']:.1f}"
        ])
    headers = ["Query", "Conflicting URLs", "Total Imp", "Total Clicks", "Avg Pos"]
    print(f"\n--- TOP {limit} TU KHOA CANH TRANH NOI BO (CANNIBALIZATION) ---")
    print(format_table(headers, table_data))


def show_funnel(hub_name):
    """Data Analyst: Bóc tách phễu 3 tầng và chẩn đoán điểm nghẽn Drop-off của Hub."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT hub_name, active_pages, total_sessions, engaged_sessions, engagement_rate_pct, w2a_clicks, w2a_cvr_pct
        FROM v_hub_performance
        WHERE LOWER(hub_name) LIKE LOWER(?)
        LIMIT 1;
    """, (f"%{hub_name}%",))
    hub_row = cur.fetchone()

    if not hub_row:
        print(f"Không tìm thấy Hub nào khớp với từ khóa: '{hub_name}'.")
        conn.close()
        return

    h_name = hub_row["hub_name"]
    sessions = hub_row["total_sessions"]
    engaged = hub_row["engaged_sessions"]
    w2a = hub_row["w2a_clicks"]
    cvr = hub_row["w2a_cvr_pct"]
    eng_rate = hub_row["engagement_rate_pct"]

    drop_off_1 = 100.0 - eng_rate if sessions > 0 else 0.0
    drop_off_2 = 100.0 - (w2a * 100.0 / engaged) if engaged > 0 else 100.0

    print(f"\n========================================================")
    print(f"  CHẨN ĐOÁN PHỄU CHUYỂN ĐỔI (FUNNEL DIAGNOSTICS): {h_name.upper()}")
    print(f"========================================================")

    funnel_data = [
        ["Tầng 1: Tổng lượt truy cập (Total Visits)", f"{sessions:,}", "100.0%", "Gốc phễu (Baseline)"],
        ["Tầng 2: Phiên có tương tác (Engaged Sessions)", f"{engaged:,}", f"{eng_rate:.1f}%", f"Rớt {drop_off_1:.1f}% từ Tầng 1"],
        ["Tầng 3: Click OneLink mở/cài App (W2A Clicks)", f"{w2a:,}", f"{cvr:.2f}%", f"Rớt {drop_off_2:.1f}% từ Tầng 2"]
    ]
    print(format_table(["Nấc Phễu (Funnel Stage)", "Số Lượng", "Tỷ Lệ / Tổng", "Tỷ Lệ Rớt (Drop-off)"], funnel_data))

    # Top 5 landing pages của Hub
    cur.execute("""
        SELECT 
            p.path,
            SUM(g.sessions) AS lp_sessions,
            SUM(g.engaged_sessions) AS lp_engaged,
            (COALESCE(SUM(g.onelink_clicks_track1), 0) + COALESCE(SUM(g.onelink_clicks_track2), 0)) AS lp_w2a,
            ROUND((COALESCE(SUM(g.onelink_clicks_track1), 0) + COALESCE(SUM(g.onelink_clicks_track2), 0)) * 100.0 / NULLIF(SUM(g.sessions), 0), 2) AS lp_cvr
        FROM ga4_landing_pages g
        JOIN dim_url_project p ON g.landing_page = p.path OR g.landing_page = p.url
        WHERE LOWER(p.hub_name) LIKE LOWER(?)
        GROUP BY p.path
        ORDER BY lp_sessions DESC
        LIMIT 5;
    """, (f"%{hub_name}%",))
    top_lps = cur.fetchall()
    conn.close()

    if top_lps:
        lp_data = []
        for lp in top_lps:
            path_str = lp["path"]
            if len(path_str) > 40:
                path_str = path_str[:37] + "..."
            lp_data.append([
                path_str,
                f"{lp['lp_sessions']:,}",
                f"{lp['lp_engaged']:,}",
                f"{lp['lp_w2a']:,}",
                f"{lp['lp_cvr']:.2f}%"
            ])
        print(f"\n--- TOP 5 TRANG ĐÍCH CHIẾM LƯU LƯỢNG CAO NHẤT CỦA {h_name} ---")
        print(format_table(["Trang Đích (Path)", "Sessions", "Engaged", "W2A Clicks", "CVR"], lp_data))

    # Data Analyst Root Cause Analysis (RCA)
    print("\n--- NHẬN ĐỊNH CỦA DATA ANALYST (RCA INSIGHTS) ---")
    if drop_off_1 > 50.0:
        print(f"[!] CẢNH BÁO TẦNG 1: Tỷ lệ thoát ngay (Drop-off) lên đến {drop_off_1:.1f}%.")
        print("    -> Nguyên nhân: Nội dung trang đích chưa khớp với Search Intent của người dùng hoặc tốc độ tải trang chậm.")
    else:
        print(f"[+] TẦNG 1 TỐT: Tỷ lệ giữ chân người dùng đạt {eng_rate:.1f}% (trên mức chuẩn 50%).")

    if drop_off_2 > 95.0:
        print(f"[!] CẢNH BÁO TẦNG 2: Người dùng có tương tác nhưng rớt đến {drop_off_2:.1f}% ở bước click OneLink.")
        print("    -> Nguyên nhân: Lời kêu gọi hành động (CTA) mờ nhạt, thiếu ưu đãi hấp dẫn hoặc chưa tích hợp công cụ tiện ích giữ chân.")
    else:
        print(f"[+] TẦNG 2 KHẢ QUAN: Tỷ lệ chuyển đổi từ phiên tương tác sang OneLink đạt {100.0 - drop_off_2:.1f}%.")


def show_market_sizing(query_or_theme, month=11):
    """Business Development: Định lượng dung lượng thị trường & Tiềm năng Thương mại."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT theme_id, name, sector, pillar, volume, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12
        FROM dim_theme_seasonality
        WHERE LOWER(name) LIKE LOWER(?) OR LOWER(pillar) LIKE LOWER(?) OR LOWER(sector) LIKE LOWER(?)
        ORDER BY volume DESC
        LIMIT 5;
    """, (f"%{query_or_theme}%", f"%{query_or_theme}%", f"%{query_or_theme}%"))
    themes = cur.fetchall()

    if not themes:
        print(f"Không tìm thấy Theme mùa vụ nào khớp với: '{query_or_theme}'. Đang quét tiếp Search Console...")
        cur.execute("""
            SELECT query, clicks, impressions, position
            FROM gsc_keyword_ranking
            WHERE LOWER(query) LIKE LOWER(?)
            ORDER BY impressions DESC
            LIMIT 5;
        """, (f"%{query_or_theme}%",))
        gsc_rows = cur.fetchall()
        conn.close()

        if not gsc_rows:
            print("Không tìm thấy dữ liệu từ khóa tương ứng.")
            return

        print(f"\n--- DỮ LIỆU TỪ KHÓA TỪ SEARCH CONSOLE CHO '{query_or_theme}' ---")
        gsc_table = []
        for r in gsc_rows:
            gsc_table.append([r["query"], f"{r['impressions']:,}", f"{r['clicks']:,}", f"{r['position']:.1f}"])
        print(format_table(["Query", "Impressions", "Clicks", "Position"], gsc_table))
        return

    conn.close()

    # Benchmark AOV & Hoa hồng theo ngành
    sector_benchmarks = {
        "Lottery": {"aov": 50000, "comm": 0.05, "cvr": 0.035, "partners": "Vietlott, Đại lý XSKT"},
        "Cinema": {"aov": 85000, "comm": 0.07, "cvr": 0.025, "partners": "Lotte Cinema, Beta Cinema, BHD, Cinestar"},
        "Entertainment": {"aov": 85000, "comm": 0.07, "cvr": 0.025, "partners": "NPH Game, K+, VieON, FPT Play"},
        "Insurtech": {"aov": 450000, "comm": 0.20, "cvr": 0.015, "partners": "Bảo Việt, PVI, PTI, Liberty"},
        "insurtech": {"aov": 450000, "comm": 0.20, "cvr": 0.015, "partners": "Bảo Việt, PVI, PTI, Liberty"},
        "vehicle-hub": {"aov": 350000, "comm": 0.15, "cvr": 0.065, "partners": "Trung tâm đăng kiểm, Cứu hộ, Đại lý phụ tùng"},
        "Financial": {"aov": 500000, "comm": 0.08, "cvr": 0.035, "partners": "VPBank, Shinhan Bank, Mirae Asset, VIB"},
        "ota": {"aov": 1200000, "comm": 0.05, "cvr": 0.040, "partners": "Vietnam Airlines, Bamboo, Vietjet, Khách sạn"},
        "Default": {"aov": 150000, "comm": 0.10, "cvr": 0.035, "partners": "Đối tác ngành hàng liên quan"}
    }

    print(f"\n========================================================")
    print(f"  ĐỊNH LƯỢNG DUNG LƯỢNG THỊ TRƯỜNG (MARKET SIZING): '{query_or_theme.upper()}'")
    print(f"========================================================")

    sizing_rows = []
    for t in themes:
        vol = t["volume"]
        sector = t["sector"]
        bm = sector_benchmarks.get(sector, sector_benchmarks["Default"])

        # Mùa vụ tháng đang xét
        month_col = f"m{month}"
        m_val = t[month_col] if month_col in t.keys() else 50
        sum_m = sum([t[f"m{i}"] for i in range(1, 13) if f"m{i}" in t.keys()]) or 1200

        projected_month_search = int(vol * (m_val / sum_m))
        potential_clicks = int(projected_month_search * 0.15)  # Giả định Top 1-3 đạt 15% CTR
        potential_w2a_users = int(potential_clicks * bm["cvr"])
        potential_gmv = potential_w2a_users * bm["aov"]
        potential_comm = int(potential_gmv * bm["comm"])

        sizing_rows.append([
            t["name"],
            sector,
            f"{vol:,}",
            f"{projected_month_search:,}",
            f"{potential_clicks:,}",
            f"{potential_w2a_users:,}",
            f"{potential_gmv / 1_000_000:.1f} tr",
            f"{potential_comm / 1_000_000:.1f} tr",
            bm["partners"]
        ])

    headers = [
        "Theme Mùa Vụ", "Sector", "Nhu Cầu Năm", f"Dự Kiến T{month}",
        "Organic Clicks", "W2A Users", "Tiềm Năng GMV", "Tiềm Năng Phí", "Đối Tác Mục Tiêu"
    ]
    print(format_table(headers, sizing_rows))

    print("\n--- LUẬN ĐIỂM KINH DOANH CHO BUSINESS DEVELOPMENT (BD STRATEGY) ---")
    print("1. Dung lượng thực tế: Thị trường có nhu cầu tìm kiếm tự nhiên rất lớn, không phụ thuộc vào việc chạy Ads.")
    print("2. Lợi thế đàm phán với Đối tác: Web MoMo có thể đóng vai trò kênh phân phối độc quyền hoặc ưu tiên,")
    print("   giúp đối tác tiếp cận tệp người dùng có nhu cầu sẵn sàng chi trả với chi phí thấp hơn tự mua quảng cáo.")
    print("3. Khuyến nghị mô hình thương mại: Đàm phán mức chia sẻ doanh thu (CPS) trên giao dịch hoàn tất hoặc gói đồng thương hiệu.")


def run_custom_sql(sql):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        if not rows:
            print("Query thực thi thành công nhưng không trả về dòng dữ liệu nào.")
            return
        headers = [desc[0] for desc in cur.description]
        formatted_rows = []
        for r in rows[:50]:
            formatted_rows.append([str(v) if v is not None else "NULL" for v in r])
        print(f"\n--- KẾT QUẢ SQL QUERY (Hiển thị tối đa 50 dòng) ---")
        print(format_table(headers, formatted_rows))
        if len(rows) > 50:
            print(f"... và còn {len(rows) - 50} dòng nữa.")
    except Exception as e:
        print(f"[ERROR] Lỗi thực thi SQL: {e}")
    finally:
        conn.close()


def main():
    parser = argparse.ArgumentParser(description="CLI Analytics Query Tool")
    parser.add_argument("--hubs", action="store_true", help="Hiển thị hiệu suất các Hubs")
    parser.add_argument("--seo-hubs", action="store_true", help="Hiển thị hiệu suất SEO Search Console 2026 theo Hubs")
    parser.add_argument("--devices", action="store_true", help="Hiển thị phân bổ thiết bị Mobile vs Desktop Search Console 2026")
    parser.add_argument("--w2a", action="store_true", help="Hiển thị Top trang chuyển đổi Web-to-App")
    parser.add_argument("--quick-wins", action="store_true", help="Hiển thị từ khóa Quick Wins")
    parser.add_argument("--cannibalization", action="store_true", help="Hiển thị từ khóa ăn thịt lẫn nhau")
    parser.add_argument("--funnel", type=str, help="Data Analyst: Bóc tách phễu và chẩn đoán điểm nghẽn Drop-off theo Hub")
    parser.add_argument("--market-sizing", type=str, help="Business Development: Định lượng dung lượng thị trường và tiềm năng GMV")
    parser.add_argument("--month", type=int, default=11, help="Tháng xét mùa vụ (1-12, mặc định là 11)")
    parser.add_argument("--sql", type=str, help="Chạy câu truy vấn SQL tùy ý")
    parser.add_argument("--limit", type=int, default=15, help="Giới hạn số dòng hiển thị")

    args = parser.parse_args()

    if args.sql:
        run_custom_sql(args.sql)
    elif args.funnel:
        show_funnel(args.funnel)
    elif args.market_sizing:
        show_market_sizing(args.market_sizing, month=args.month)
    elif args.seo_hubs:
        show_seo_hubs()
    elif args.devices:
        show_devices()
    elif args.hubs:
        show_hubs()
    elif args.w2a:
        show_top_w2a(limit=args.limit)
    elif args.quick_wins:
        show_quick_wins(limit=args.limit)
    elif args.cannibalization:
        show_cannibalization(limit=args.limit)
    else:
        # Mặc định hiển thị bảng tổng quan Hubs và Top W2A
        show_hubs()
        show_top_w2a(limit=10)


if __name__ == "__main__":
    main()

