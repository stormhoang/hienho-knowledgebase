#!/usr/bin/env python3
"""
BUILD WEB GROWTH BENCHMARKS
Tính baseline định lượng từ Data Mart SQLite (GA4 landing pages + GSC + hub view)
để các phân tích growth có điểm so sánh thay vì đánh giá cảm tính.

Output: 07_REPORTS/data/benchmarks/web_growth_benchmarks.json
Kèm bảng markdown tóm tắt ra stdout.

Lưu ý độ chính xác:
- ga4_landing_pages là snapshot tại synced_at (một lần sync), KHÔNG phải chuỗi thời gian.
- Nhãn period trong output phản ánh đúng synced_at, không suy diễn cửa sổ ngày.
"""

import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from statistics import median

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.db import get_connection, DEFAULT_DB_PATH

OUT_PATH = REPO_ROOT / "07_REPORTS" / "data" / "benchmarks" / "web_growth_benchmarks.json"

# Mapping channel_group (GA4) -> nhóm Traffic SSOT.
# Non-Paid chuẩn: Organic, Direct, AI Traffic (GEO), Referral.
# Paid: Paid Search, Google Ads, Campaign Ads.
# GA4 channel_group không map 1:1 - các nhóm 'Organic *' và 'AI Assistant' xấp xỉ
# phía Non-Paid; 'Paid *' và 'Cross-network' xấp xỉ phía Paid. 'Unassigned' tách riêng.
NON_PAID_GROUPS = {"Direct", "Organic Search", "Organic Social", "Organic Video", "AI Assistant", "Referral"}
PAID_GROUPS = {"Paid Search", "Paid Social", "Paid Other", "Cross-network"}


def pct(num, den):
    return round(num * 100.0 / den, 3) if den else None


def percentile(sorted_vals, p):
    if not sorted_vals:
        return None
    k = (len(sorted_vals) - 1) * p / 100.0
    f = int(k)
    c = min(f + 1, len(sorted_vals) - 1)
    return round(sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * (k - f), 3)


def build_overall(cur):
    row = cur.execute("""
        SELECT COUNT(DISTINCT landing_page) AS pages,
               SUM(sessions) AS sessions,
               SUM(engaged_sessions) AS engaged,
               SUM(onelink_clicks_track1) AS t1,
               SUM(onelink_clicks_track2) AS t2
        FROM ga4_landing_pages;
    """).fetchone()
    sessions = row["sessions"] or 0
    w2a = (row["t1"] or 0) + (row["t2"] or 0)
    return {
        "active_landing_pages": row["pages"],
        "sessions": sessions,
        "engaged_sessions": row["engaged"] or 0,
        "engagement_rate_pct": pct(row["engaged"] or 0, sessions),
        "onelink_clicks_track1": row["t1"] or 0,
        "onelink_clicks_track2": row["t2"] or 0,
        "w2a_clicks": w2a,
        "w2a_cvr_pct": pct(w2a, sessions),
    }


def build_by_channel(cur):
    rows = cur.execute("""
        SELECT channel_group,
               SUM(sessions) AS sessions,
               SUM(engaged_sessions) AS engaged,
               SUM(onelink_clicks_track1 + onelink_clicks_track2) AS w2a
        FROM ga4_landing_pages
        GROUP BY channel_group
        ORDER BY sessions DESC;
    """).fetchall()

    out = {}
    for r in rows:
        grp = "non_paid" if r["channel_group"] in NON_PAID_GROUPS else \
              "paid" if r["channel_group"] in PAID_GROUPS else "unassigned"
        bucket = out.setdefault(grp, {"sessions": 0, "engaged": 0, "w2a": 0, "channels": {}})
        bucket["sessions"] += r["sessions"] or 0
        bucket["engaged"] += r["engaged"] or 0
        bucket["w2a"] += r["w2a"] or 0
        bucket["channels"][r["channel_group"]] = {
            "sessions": r["sessions"] or 0,
            "w2a_clicks": r["w2a"] or 0,
            "w2a_cvr_pct": pct(r["w2a"] or 0, r["sessions"] or 0),
        }
    for grp, b in out.items():
        b["engagement_rate_pct"] = pct(b["engaged"], b["sessions"])
        b["w2a_cvr_pct"] = pct(b["w2a"], b["sessions"])
        b["sessions_share_pct"] = pct(b["sessions"], sum(x["sessions"] for x in out.values()))

    # Tách riêng source='in_app' (webview trong app MoMo - existing users deep-link
    # ngược vào app) khỏi nhóm unassigned. CVR của nhóm này ~26% là engagement
    # user cũ, KHÔNG phải acquisition - đưa chung sẽ inflate benchmark W2A.
    in_app = cur.execute("""
        SELECT SUM(sessions) AS sess, SUM(engaged_sessions) AS engaged,
               SUM(onelink_clicks_track1 + onelink_clicks_track2) AS w2a,
               COUNT(DISTINCT landing_page) AS pages
        FROM ga4_landing_pages WHERE source = 'in_app' OR source LIKE 'in_app%';
    """).fetchone()
    out["in_app_webview"] = {
        "sessions": in_app["sess"] or 0,
        "engaged_sessions": in_app["engaged"] or 0,
        "w2a_clicks": in_app["w2a"] or 0,
        "active_landing_pages": in_app["pages"] or 0,
        "note": "Existing users trong app webview; CVR cao là deep-link engagement, không tính vào acquisition benchmark",
    }
    out["in_app_webview"]["w2a_cvr_pct"] = pct(in_app["w2a"] or 0, in_app["sess"] or 0)

    # Trừ in_app khỏi unassigned để còn 'unassigned_thật' (Admicro, not set, AI referrer, UTM rác)
    if "unassigned" in out:
        ua = out["unassigned"]
        ua_sessions = max((ua["sessions"] or 0) - (in_app["sess"] or 0), 0)
        ua_w2a = max((ua["w2a"] or 0) - (in_app["w2a"] or 0), 0)
        out["unassigned_ex_in_app"] = {
            "sessions": ua_sessions,
            "w2a_clicks": ua_w2a,
            "w2a_cvr_pct": pct(ua_w2a, ua_sessions),
            "note": "Admicro (paid chưa map), (not set), AI referrer, UTM double-encoded - cần fix classification",
        }
    return out


def build_by_hub(cur):
    rows = cur.execute("""
        SELECT hub_name, active_pages, total_sessions, engagement_rate_pct,
               w2a_clicks, w2a_cvr_pct
        FROM v_hub_performance
        ORDER BY total_sessions DESC;
    """).fetchall()
    return [dict(r) for r in rows]


def build_page_cvr_distribution(cur, min_sessions=500):
    """Phân vị W2A CVR của landing pages có đủ traffic - làm benchmark 'trang tốt/xấu'."""
    rows = cur.execute("""
        SELECT landing_page, sessions,
               ROUND((onelink_clicks_track1 + onelink_clicks_track2) * 100.0
                     / NULLIF(sessions, 0), 3) AS w2a_cvr_pct
        FROM ga4_landing_pages
        WHERE sessions >= ?;
    """, (min_sessions,)).fetchall()
    cvrs = sorted(r["w2a_cvr_pct"] for r in rows if r["w2a_cvr_pct"] is not None)
    return {
        "min_sessions_threshold": min_sessions,
        "pages_count": len(cvrs),
        "w2a_cvr_p25_pct": percentile(cvrs, 25),
        "w2a_cvr_median_pct": percentile(cvrs, 50),
        "w2a_cvr_p75_pct": percentile(cvrs, 75),
        "w2a_cvr_p90_pct": percentile(cvrs, 90),
        "interpretation": "CVR >= p75 = top quartile (benchmark tốt); <= p25 = cần xem xét UX/funnel",
    }


def build_gsc_overall(cur):
    row = cur.execute("""
        SELECT SUM(impressions) AS imp, SUM(clicks) AS clicks,
               ROUND(SUM(clicks) * 100.0 / NULLIF(SUM(impressions), 0), 3) AS ctr_pct,
               ROUND(SUM(position * impressions) * 1.0
                     / NULLIF(SUM(impressions), 0), 1) AS avg_pos
        FROM gsc_search_analytics;
    """).fetchone()
    return {
        "impressions": row["imp"] or 0,
        "clicks": row["clicks"] or 0,
        "ctr_pct": row["ctr_pct"],
        "avg_position": row["avg_pos"],
    }


def main():
    parser = argparse.ArgumentParser(description="Build Web Growth Benchmarks từ Data Mart")
    parser.add_argument("--min-page-sessions", type=int, default=500,
                        help="Ngưỡng sessions tối thiểu để tính phân vị CVR landing page")
    args = parser.parse_args()

    conn = get_connection()
    cur = conn.cursor()

    synced_at = cur.execute("SELECT MAX(synced_at) FROM ga4_landing_pages").fetchone()[0]
    benchmarks = {
        "as_of": (synced_at or "")[:10],
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_db": str(DEFAULT_DB_PATH.relative_to(REPO_ROOT)),
        "period_note": "ga4_landing_pages là snapshot tại synced_at; fact_daily_performance là MTD daily. Không suy diễn cửa sổ ngày ngoài các trường trên.",
        "overall": build_overall(cur),
        "by_channel_group": build_by_channel(cur),
        "by_hub": build_by_hub(cur),
        "landing_page_cvr_distribution": build_page_cvr_distribution(cur, args.min_page_sessions),
        "gsc_overall": build_gsc_overall(cur),
    }
    conn.close()

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(benchmarks, ensure_ascii=False, indent=2), encoding="utf-8")

    o = benchmarks["overall"]
    print(f"\n=== WEB GROWTH BENCHMARKS (as_of {benchmarks['as_of']}) ===")
    print(f"Sessions: {o['sessions']:,} | Engagement: {o['engagement_rate_pct']}% | "
          f"W2A CVR: {o['w2a_cvr_pct']}% ({o['w2a_clicks']:,} clicks / {o['active_landing_pages']:,} pages)")
    for grp, b in benchmarks["by_channel_group"].items():
        extra = " (existing users, loại khỏi acquisition)" if grp == "in_app_webview" else ""
        print(f"  [{grp}] sessions {b['sessions']:,} | W2A CVR {b['w2a_cvr_pct']}% | engagement {b.get('engagement_rate_pct')}%{extra}")
        if grp == "unassigned_ex_in_app":
            print(f"    -> unassigned sau khi trừ in_app: {b['sessions']:,} sess, CVR {b['w2a_cvr_pct']}%")
    d = benchmarks["landing_page_cvr_distribution"]
    print(f"Page CVR distribution (n={d['pages_count']}, sessions>={d['min_sessions_threshold']}): "
          f"p25={d['w2a_cvr_p25_pct']}% median={d['w2a_cvr_median_pct']}% "
          f"p75={d['w2a_cvr_p75_pct']}% p90={d['w2a_cvr_p90_pct']}%")
    g = benchmarks["gsc_overall"]
    print(f"GSC: {g['impressions']:,} imp | {g['clicks']:,} clicks | CTR {g['ctr_pct']}% | pos {g['avg_position']}")
    print(f"\n[OK] Đã ghi benchmarks -> {OUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
