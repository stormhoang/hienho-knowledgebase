# -*- coding: utf-8 -*-
"""
BASELINE ANCHOR RECONCILIATION ENGINE
Quản lý mốc quy chiếu cố định (Anchor Baseline) và cơ chế cộng dồn lũy kế từng ngày
cho các tháng có chốt số liệu với Data Warehouse BigQuery SSOT.

Quy chuẩn:
- Tháng 11/2026: MTD Ngày 1..16 đã chốt số liệu BigQuery SSOT = 2.861.286 PV.
- Từ Ngày 17 trở đi: Tự động kéo lưu lượng phát sinh từ ngày 17 đến ngày N và cộng dồn
  trực tiếp vào mốc 2.861.286 PV (cùng cơ cấu kênh và Hub tương ứng).
"""

import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[2]

def get_anchor_config(month_str="2026-11"):
    suffix = month_str.replace("-", "_")
    anchor_file = BASE_DIR / "07_REPORTS" / "data" / f"baseline_mtd_anchor_{suffix}.json"
    if anchor_file.exists():
        try:
            with open(anchor_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Anchor] Cảnh báo đọc file anchor: {e}")
    return None

def compute_incremental_mtd(month_str, days_elapsed, ga4_token, run_ga4_report_fn):
    """
    Nếu có anchor config cho tháng hiện tại:
    - Nếu days_elapsed <= anchor_day (ví dụ 16): Trả về nguyên mốc anchor 2.861.286 PV.
    - Nếu days_elapsed > anchor_day (ví dụ 17): Kéo GA4 từ ngày 17 đến ngày N và cộng dồn vào anchor.
    Trả về dict chứa metrics đã hợp nhất, hoặc None nếu không có anchor config.
    """
    anchor = get_anchor_config(month_str)
    if not anchor:
        return None

    anchor_day = anchor.get("anchor_day", 16)
    anchor_pv = anchor.get("anchor_pv", 2861286)
    anchor_channels = anchor.get("channels", {})
    anchor_hubs = anchor.get("hubs", {})
    anchor_cinema = anchor.get("cinema_breakdown", {})

    if days_elapsed <= anchor_day:
        return {
            "is_anchored": True,
            "anchor_day": anchor_day,
            "days_elapsed": days_elapsed,
            "total_pv": anchor_pv,
            "channels": anchor_channels,
            "hubs": anchor_hubs,
            "cinema_breakdown": anchor_cinema,
            "incremental_pv": 0,
            "note": f"MTD {days_elapsed}d chốt chuẩn BigQuery SSOT = {anchor_pv:,} PV"
        }

    # Ngày lớn hơn anchor_day: Kéo phát sinh từ (anchor_day + 1) đến days_elapsed
    inc_start = f"{month_str}-{anchor_day + 1:02d}"
    inc_end = f"{month_str}-{days_elapsed:02d}"
    print(f"[Anchor-Incremental] Phát hiện mốc chốt Ngày 1..{anchor_day} ({anchor_pv:,} PV).")
    print(f"[Anchor-Incremental] Đang kéo phát sinh lũy kế mới ({inc_start} -> {inc_end}) để cộng dồn...")

    # 1. Kéo tổng PV phát sinh
    q_prop = {
        "dateRanges": [{"startDate": inc_start, "endDate": inc_end}],
        "metrics": [{"name": "screenPageViews"}, {"name": "sessions"}, {"name": "totalUsers"}],
        "dimensionFilter": {"filter": {"fieldName": "hostName", "stringFilter": {"value": "www.momo.vn"}}}
    }
    res_p = run_ga4_report_fn(ga4_token, q_prop)
    rows_p = res_p.get("rows", [{}])[0].get("metricValues", [])
    inc_total_pv = int(rows_p[0]["value"]) if rows_p else 0
    inc_sessions = int(rows_p[1]["value"]) if len(rows_p) > 1 else 0
    inc_users = int(rows_p[2]["value"]) if len(rows_p) > 2 else 0

    # 2. Kéo phân bổ kênh phát sinh
    q_ch = {
        "dateRanges": [{"startDate": inc_start, "endDate": inc_end}],
        "dimensions": [{"name": "sessionDefaultChannelGroup"}, {"name": "sessionSource"}],
        "metrics": [{"name": "screenPageViews"}],
        "dimensionFilter": {"filter": {"fieldName": "hostName", "stringFilter": {"value": "www.momo.vn"}}},
        "limit": 10000
    }
    res_ch = run_ga4_report_fn(ga4_token, q_ch)
    inc_org = 0
    inc_dir = 0
    inc_paid = 0
    inc_ref = 0
    inc_oth = 0
    inc_ai = 0

    ai_sources = [
        "chatgpt.com", "perplexity.ai", "gemini.google.com", 
        "copilot.microsoft.com", "android-app://com.openai.chatgpt",
        "claude.ai", "duck.ai", "deepseek"
    ]

    for r in res_ch.get("rows", []):
        ch = r["dimensionValues"][0]["value"]
        src = r["dimensionValues"][1]["value"]
        pv = int(r["metricValues"][0]["value"])
        cn = ch.lower()
        sn = src.lower()

        if any(ai in sn for ai in ai_sources) or cn == "ai assistant":
            inc_ai += pv
        if sn == "in_app" or sn.startswith("in_app") or "referral" in cn:
            inc_ref += pv
        elif "organic search" in cn:
            inc_org += pv
        elif "direct" in cn:
            inc_dir += pv
        elif any(k in cn for k in ["paid", "cpc", "display", "cross-network"]):
            inc_paid += pv
        else:
            inc_oth += pv

    inc_merged_ref = max(0, inc_ref + inc_oth - inc_ai)

    # Tổng hợp cộng dồn: Anchor + Incremental
    comb_total_pv = anchor_pv + inc_total_pv
    comb_org = anchor_channels.get("organic", 0) + inc_org
    comb_dir = anchor_channels.get("direct", 0) + inc_dir
    comb_paid = anchor_channels.get("paid", 0) + inc_paid
    comb_ref = anchor_channels.get("referral", 0) + inc_ref
    comb_oth = anchor_channels.get("others", 0) + inc_oth
    comb_merged_ref = anchor_channels.get("merged_referral", 0) + inc_merged_ref
    comb_ai = anchor_channels.get("ai_traffic", 0) + inc_ai
    comb_non_paid = comb_org + comb_dir + comb_ai + comb_merged_ref

    # Cân bằng làm tròn nếu có lệch
    diff_ch = comb_total_pv - (comb_paid + comb_non_paid)
    if diff_ch != 0:
        comb_non_paid += diff_ch
        comb_merged_ref += diff_ch

    print(f"  ✓ Đã cộng dồn thành công: {anchor_pv:,} (Gốc N1..16) + {inc_total_pv:,} (Phát sinh N{anchor_day+1}..{days_elapsed}) = {comb_total_pv:,} PV")

    return {
        "is_anchored": True,
        "anchor_day": anchor_day,
        "days_elapsed": days_elapsed,
        "total_pv": comb_total_pv,
        "incremental_pv": inc_total_pv,
        "inc_sessions": inc_sessions,
        "inc_users": inc_users,
        "channels": {
            "organic": comb_org,
            "direct": comb_dir,
            "paid": comb_paid,
            "referral": comb_ref,
            "others": comb_oth,
            "merged_referral": comb_merged_ref,
            "ai_traffic": comb_ai,
            "non_paid": comb_non_paid
        },
        "hubs": anchor_hubs, # Sẽ được update chi tiết
        "cinema_breakdown": anchor_cinema
    }
