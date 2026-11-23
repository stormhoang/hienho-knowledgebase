#!/usr/bin/env python3
"""
AUTOMATED PRIORITIZATION ENGINE (RICE & ICE SCORING)
Tự động hóa chấm điểm và phân loại thứ tự ưu tiên hành động cho Web Platform.

Công thức tính RICE dựa trên dữ liệu thời gian thực từ SQLite Data Mart:
- Reach: Impressions thực tế từ Search Console hoặc Search Volume từ Inventory.
- Impact: Trọng số chuyển đổi của Hub (Home MoMo: 5.0, Financial: 4.5, Payment/Game: 3.5, Cinema: 2.5, Khác: 1.5).
- Confidence: Độ tin cậy thăng hạng theo vị trí hiện tại (Top 4-10: 100%, Top 11-20: 80%, Top 21-50: 50%).
- Effort: Độ phức tạp triển khai (Tối ưu Title/Meta: 1, Mở rộng bài Spoke: 3, Xây mới Pillar/Widget: 8).
- RICE Score = (Reach * Impact * Confidence) / Effort
"""

import sys
import argparse
import sqlite3
from pathlib import Path
from tabulate import tabulate

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.db import get_connection


def format_table(headers, rows):
    return tabulate(rows, headers=headers, tablefmt="github")


# Trọng số tác động kinh doanh (Impact Weight) theo Hub dựa trên W2A CVR và giá trị người dùng
HUB_IMPACT_WEIGHT = {
    "Home MoMo": 5.0,
    "Financial Hub": 4.5,      # Người dùng tài chính có giá trị trọn đời (LTV) cao nhất
    "New User Hub": 4.0,      # Trực tiếp thu hút người dùng mới vào App
    "Payment Hub": 3.5,
    "Game Hub": 3.5,
    "Support Hub": 3.0,
    "Vehicle Hub": 3.0,
    "Cinema Hub": 2.5,        # Volume lớn nhưng CVR thấp hơn
    "Billpay Hub": 3.0,
    "Insurance Hub": 3.0,
    "Download": 1.0,
    "Khác / Chưa phân loại": 2.0
}


def get_confidence_score(position: float) -> float:
    """Vị trí càng gần Top 3 thì xác suất tối ưu thành công càng cao."""
    if position <= 10.0:
        return 1.0
    elif position <= 20.0:
        return 0.8
    elif position <= 30.0:
        return 0.6
    return 0.4


def prioritize_quick_wins(limit=15, hub_filter=None):
    """Xếp hạng các cơ hội Quick Wins từ Search Console (Pos 4-20, Imp cao, CTR thấp)."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            g.query,
            g.page_url,
            COALESCE(d.hub_name, 'Khác / Chưa phân loại') AS hub_name,
            COALESCE(d.primary_project, 'Khác') AS project,
            g.impressions,
            g.clicks,
            ROUND(g.ctr * 100, 2) AS ctr_pct,
            ROUND(g.position, 1) AS position
        FROM gsc_search_analytics g
        LEFT JOIN dim_url_project d ON (
            g.page_url = d.url 
            OR g.page_url = ('https://www.momo.vn' || d.path)
        )
        WHERE g.position BETWEEN 4.0 AND 20.0
          AND g.impressions >= 10000
          AND g.ctr < 0.04
        ORDER BY g.impressions DESC
        LIMIT 100;
    """)
    rows = cur.fetchall()
    conn.close()

    scored_items = []
    for r in rows:
        hname = r["hub_name"]
        if hub_filter and hub_filter.lower() not in hname.lower():
            continue

        reach = r["impressions"]
        impact = HUB_IMPACT_WEIGHT.get(hname, 2.0)
        confidence = get_confidence_score(r["position"])
        # Quick win chỉ cần chỉnh sửa Title/Snippet nên Effort = 1
        effort = 1.0

        rice_score = (reach * impact * confidence) / effort
        
        # Phân loại tiến độ triển khai
        if rice_score >= 100000:
            priority = "Triển khai ngay"
        elif rice_score >= 40000:
            priority = "Ưu tiên kế tiếp"
        else:
            priority = "Xem xét sau"

        scored_items.append({
            "query": r["query"],
            "url": r["page_url"].replace("https://www.momo.vn", ""),
            "hub": hname,
            "project": r["project"],
            "reach": reach,
            "clicks": r["clicks"],
            "ctr": r["ctr_pct"],
            "pos": r["position"],
            "rice": int(rice_score),
            "priority": priority,
            "action": "Tối ưu thẻ Title, Meta Description và thêm FAQ Schema"
        })

    # Sắp xếp theo điểm RICE giảm dần
    scored_items.sort(key=lambda x: x["rice"], reverse=True)
    return scored_items[:limit]


def show_prioritized_initiatives(limit=15, hub=None):
    items = prioritize_quick_wins(limit=limit, hub_filter=hub)
    if not items:
        print("Không tìm thấy sáng kiến nào phù hợp tiêu chí lọc.")
        return

    print("=" * 85)
    print(f"BẢNG XẾP HẠNG ƯU TIÊN HÀNH ĐỘNG THEO RICE SCORE (TOP {len(items)} SÁNG KIẾN)")
    print("=" * 85)

    table_data = []
    for idx, item in enumerate(items, 1):
        q = item["query"] if len(item["query"]) <= 25 else item["query"][:22] + "..."
        u = item["url"] if len(item["url"]) <= 32 else item["url"][:29] + "..."
        table_data.append([
            idx,
            item["priority"],
            q,
            u,
            item["hub"],
            f"{item['reach']:,}",
            f"{item['ctr']:.2f}%",
            f"{item['pos']:.1f}",
            f"{item['rice']:,}",
            item["action"]
        ])

    headers = ["#", "Ưu tiên", "Từ khóa", "Đường dẫn", "Hub", "Reach (Imp)", "CTR", "Pos", "Điểm RICE", "Hành động đề xuất"]
    print(format_table(headers, table_data))
    print("\n" + "=" * 85)


def main():
    parser = argparse.ArgumentParser(description="Automated Prioritization Engine (RICE)")
    parser.add_argument("--hub", type=str, default=None, help="Lọc theo Hub (ví dụ: Financial, Cinema)")
    parser.add_argument("--limit", type=int, default=15, help="Giới hạn số lượng sáng kiến")
    args = parser.parse_args()

    show_prioritized_initiatives(limit=args.limit, hub=args.hub)


if __name__ == "__main__":
    main()
