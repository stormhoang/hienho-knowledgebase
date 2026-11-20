#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ONE-OFF GA4 PULL: Snapshot MTD 15 ngày tháng 11/2026 cho Board Monthly Report.
Kéo trực tiếp GA4 Data API (Property 270743103), chỉ ghi vào repo này
(07_REPORTS/data/ga4_nov_mtd15_analysis.json). Không đụng repo Hubs.
"""

import sys
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.sync_ga4_to_hubs import get_access_token, run_ga4_report
from scripts.build_full_funnel_matrix import build_theme_matcher

START = "2026-11-01"
END = "2026-11-15"
OUT = BASE_DIR / "07_REPORTS" / "data" / "ga4_nov_mtd15_analysis.json"

HOST_FILTER = {
    "filter": {"fieldName": "hostName", "stringFilter": {"value": "www.momo.vn"}}
}

AI_SOURCES = [
    "chatgpt.com", "perplexity.ai", "gemini.google.com",
    "copilot.microsoft.com", "android-app://com.openai.chatgpt",
    "claude.ai", "duck.ai", "deepseek",
]


def totals(token, host_filter):
    q = {
        "dateRanges": [{"startDate": START, "endDate": END}],
        "metrics": [
            {"name": "screenPageViews"},
            {"name": "sessions"},
            {"name": "totalUsers"},
            {"name": "engagedSessions"},
            {"name": "userEngagementDuration"},
        ],
    }
    if host_filter:
        q["dimensionFilter"] = host_filter
    r = run_ga4_report(token, q)
    row = r["rows"][0]["metricValues"]
    return {
        "pv": int(row[0]["value"]),
        "sessions": int(row[1]["value"]),
        "users": int(row[2]["value"]),
        "engaged_sessions": int(row[3]["value"]),
        "engagement_duration": float(row[4]["value"]),
    }


def daily_by_host(token):
    q = {
        "dateRanges": [{"startDate": START, "endDate": END}],
        "dimensions": [{"name": "date"}, {"name": "hostName"}],
        "metrics": [{"name": "screenPageViews"}],
        "limit": 10000,
    }
    res = run_ga4_report(token, q)
    out = {}
    for r in res.get("rows", []):
        d = r["dimensionValues"][0]["value"]
        h = r["dimensionValues"][1]["value"]
        pv = int(r["metricValues"][0]["value"])
        out.setdefault(d, {})[h] = pv
    return out


def channels(token):
    q = {
        "dateRanges": [{"startDate": START, "endDate": END}],
        "dimensions": [
            {"name": "sessionDefaultChannelGroup"},
            {"name": "sessionSource"},
        ],
        "metrics": [
            {"name": "screenPageViews"},
            {"name": "sessions"},
            {"name": "totalUsers"},
        ],
        "dimensionFilter": HOST_FILTER,
        "limit": 10000,
    }
    res = run_ga4_report(token, q)
    stats = {}
    agg = {"organic": 0, "direct": 0, "ai": 0, "referral": 0, "others": 0, "paid": 0, "non_paid": 0}
    for r in res.get("rows", []):
        ch = r["dimensionValues"][0]["value"]
        src = r["dimensionValues"][1]["value"]
        pv = int(r["metricValues"][0]["value"])
        sess = int(r["metricValues"][1]["value"])
        us = int(r["metricValues"][2]["value"])
        key = f"{ch} | {src}"
        stats[key] = {"pv": pv, "sessions": sess, "users": us}
        cn = ch.lower()
        sn = src.lower()
        if any(ai in sn for ai in AI_SOURCES) or cn == "ai assistant":
            agg["ai"] += pv
        if sn == "in_app" or sn.startswith("in_app") or "referral" in cn:
            agg["referral"] += pv
            agg["non_paid"] += pv
        elif "organic search" in cn:
            agg["organic"] += pv
            agg["non_paid"] += pv
        elif "direct" in cn:
            agg["direct"] += pv
            agg["non_paid"] += pv
        elif any(k in cn for k in ["paid", "cpc", "display", "cross-network"]):
            agg["paid"] += pv
        else:
            agg["others"] += pv
            agg["non_paid"] += pv
    agg["referral_plus_others"] = agg["referral"] + agg["others"]
    return {"by_pair": stats, "agg": agg}


def hubs(token):
    q = {
        "dateRanges": [{"startDate": START, "endDate": END}],
        "dimensions": [{"name": "landingPage"}],
        "metrics": [{"name": "screenPageViews"}],
        "dimensionFilter": HOST_FILTER,
        "limit": 10000,
    }
    res = run_ga4_report(token, q)
    matcher = build_theme_matcher()
    hubs_pv = {"cinema": 0, "financial": 0, "new_user": 0, "vehicle": 0,
               "insurance": 0, "student": 0, "others": 0}
    cinema_sub = {
        "Trang Rạp phim": 0, "Trang phim chi tiết": 0, "Cinema_Home Page": 0,
        "Cinema_Blog": 0, "Cinema_Landing Page": 0, "Tin tức": 0, "Others": 0,
    }
    fin_sub = {}
    veh_sub = {}
    nu_sub = {}
    for r in res.get("rows", []):
        lp = r["dimensionValues"][0]["value"]
        pv = int(r["metricValues"][0]["value"])
        t_info = matcher(lp)
        h_name = t_info[4] if t_info else "Khác"
        sec = t_info[2] if t_info else ""
        if h_name == "Cinema" or h_name.startswith("Cinema") or sec == "cinema":
            hubs_pv["cinema"] += pv
            clean_lp = lp.split("?")[0].rstrip("/")
            if clean_lp == "/cinema":
                cinema_sub["Cinema_Home Page"] += pv
            elif clean_lp.startswith("/cinema/rap"):
                cinema_sub["Trang Rạp phim"] += pv
            elif "/blog" in clean_lp or "/review" in clean_lp:
                cinema_sub["Cinema_Blog"] += pv
            elif "/tin-tuc" in clean_lp:
                cinema_sub["Tin tức"] += pv
            elif any(k in clean_lp for k in ["tang-", "ve-mien-phi", "uu-dai", "khuyen-mai", "landing"]):
                cinema_sub["Cinema_Landing Page"] += pv
            elif clean_lp.startswith("/cinema/"):
                cinema_sub["Trang phim chi tiết"] += pv
            else:
                cinema_sub["Others"] += pv
        elif h_name in ["Ví Trả Sau", "Điểm Tín Dụng", "Vay Nhanh", "Tiết Kiệm Online", "Mở Thẻ Tín Dụng", "Trung Tâm Tài Chính", "Chứng Chỉ Quỹ", "Chứng Khoán"] or sec == "Financial":
            hubs_pv["financial"] += pv
            key = lp.split("?")[0].rstrip("/")
            seg = "/".join(key.strip("/").split("/")[:3]) or "/"
            fin_sub[seg] = fin_sub.get(seg, 0) + pv
        elif h_name in ["New User"] or (sec == "Brand" and ("/tai-app" in lp or "/chao-ban-moi" in lp)):
            hubs_pv["new_user"] += pv
            key = lp.split("?")[0].rstrip("/")
            seg = "/".join(key.strip("/").split("/")[:2]) or "/"
            nu_sub[seg] = nu_sub.get(seg, 0) + pv
        elif h_name in ["Phạt Nguội", "Tiện Ích Giao Thông", "Phí Không Dừng", "Bảo Hiểm Ô Tô", "Bảo Hiểm Xe Máy", "Giá xăng", "Cây xăng", "Trạm sạc"] or sec == "vehicle-hub" or ("ô tô" in h_name.lower() or "xe máy" in h_name.lower()):
            hubs_pv["vehicle"] += pv
            key = lp.split("?")[0].rstrip("/")
            seg = "/".join(key.strip("/").split("/")[:3]) or "/"
            veh_sub[seg] = veh_sub.get(seg, 0) + pv
        elif h_name in ["Bảo Hiểm", "Bảo Hiểm Y Tế", "Bảo Hiểm Sức Khỏe", "Bảo Hiểm Xã Hội"] or sec == "insurtech" or "bảo hiểm" in h_name.lower():
            hubs_pv["insurance"] += pv
        elif h_name in ["Student Hub", "Student Pass"] or sec == "student":
            hubs_pv["student"] += pv
        else:
            hubs_pv["others"] += pv
    return {"hubs": hubs_pv, "cinema_sub": cinema_sub,
            "financial_top": dict(sorted(fin_sub.items(), key=lambda x: -x[1])[:25]),
            "vehicle_top": dict(sorted(veh_sub.items(), key=lambda x: -x[1])[:25]),
            "new_user_top": dict(sorted(nu_sub.items(), key=lambda x: -x[1])[:15])}


def main():
    token = get_access_token()
    print("[1/5] Totals strict-momo (www.momo.vn)...")
    t_strict = totals(token, HOST_FILTER)
    print("[2/5] Totals all-hosts + host breakdown...")
    t_all = totals(token, None)
    daily_host = daily_by_host(token)
    print("[3/5] Channel breakdown...")
    ch = channels(token)
    print("[4/5] Hub breakdown...")
    hb = hubs(token)

    result = {
        "period": f"{START} -> {END}",
        "strict_momo": t_strict,
        "all_hosts": t_all,
        "napthengay_pv": t_all["pv"] - t_strict["pv"],
        "daily_by_host": daily_host,
        "channels": ch,
        "hubs": hb,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[5/5] Saved -> {OUT}")
    print(json.dumps({k: result[k] for k in ["strict_momo", "all_hosts", "napthengay_pv"]}, ensure_ascii=False, indent=2))
    print("channels agg:", json.dumps(ch["agg"], ensure_ascii=False))
    print("hubs:", json.dumps(hb["hubs"], ensure_ascii=False))


if __name__ == "__main__":
    main()
