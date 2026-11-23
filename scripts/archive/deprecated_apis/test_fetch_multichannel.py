import sys
import json
import time
import os
import urllib.request
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
try:
    from scripts.build_full_funnel_matrix import get_ga4_access_token, build_theme_matcher, normalize_path
except ImportError:
    pass

def clean_dim_project(name):
    return (name or "").strip()

DATE_START = "2026-10-01"
DATE_END = "2026-10-31"

def fetch_and_test():
    cache_file = BASE_DIR / "07_REPORTS" / "data" / "ga4_multichannel_cache.json"
    if cache_file.exists():
        print(f"Loading from cache {cache_file}...")
        with open(cache_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        print("Fetching fresh GA4 multi-channel data...")
        access_token = get_ga4_access_token()
        url = "https://analyticsdata.googleapis.com/v1beta/properties/270743103:runReport"
        date_ranges = [{"startDate": DATE_START, "endDate": DATE_END}]

        body_ch = {
            "dateRanges": date_ranges,
            "dimensions": [{"name": "sessionDefaultChannelGroup"}],
            "metrics": [{"name": "sessions"}, {"name": "engagedSessions"}, {"name": "totalUsers"}],
            "limit": 100
        }
        req_ch = urllib.request.Request(url, data=json.dumps(body_ch).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
        with urllib.request.urlopen(req_ch) as resp:
            res_ch = json.loads(resp.read().decode("utf-8"))

        body_ch_w2a = {
            "dateRanges": date_ranges,
            "dimensions": [{"name": "sessionDefaultChannelGroup"}],
            "dimensionFilter": {
                "andGroup": {
                    "expressions": [
                        {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                        {
                            "orGroup": {
                                "expressions": [
                                    {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}},
                                    {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}}
                                ]
                            }
                        }
                    ]
                }
            },
            "metrics": [{"name": "eventCount"}],
            "limit": 100
        }
        req_ch_w2a = urllib.request.Request(url, data=json.dumps(body_ch_w2a).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
        with urllib.request.urlopen(req_ch_w2a) as resp:
            res_ch_w2a = json.loads(resp.read().decode("utf-8"))

        body_lp_ch = {
            "dateRanges": date_ranges,
            "dimensions": [{"name": "landingPage"}, {"name": "sessionDefaultChannelGroup"}],
            "metrics": [{"name": "sessions"}],
            "limit": 100000
        }
        req_lp_ch = urllib.request.Request(url, data=json.dumps(body_lp_ch).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
        with urllib.request.urlopen(req_lp_ch) as resp:
            res_lp_ch = json.loads(resp.read().decode("utf-8"))

        body_lp_w2a = {
            "dateRanges": date_ranges,
            "dimensions": [{"name": "landingPage"}, {"name": "sessionDefaultChannelGroup"}],
            "dimensionFilter": {
                "andGroup": {
                    "expressions": [
                        {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                        {
                            "orGroup": {
                                "expressions": [
                                    {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}},
                                    {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}}
                                ]
                            }
                        }
                    ]
                }
            },
            "metrics": [{"name": "eventCount"}],
            "limit": 100000
        }
        req_lp_w2a = urllib.request.Request(url, data=json.dumps(body_lp_w2a).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
        with urllib.request.urlopen(req_lp_w2a) as resp:
            res_lp_w2a = json.loads(resp.read().decode("utf-8"))

        data = {
            "channels_overview": res_ch.get("rows", []),
            "channels_w2a": res_ch_w2a.get("rows", []),
            "landing_page_channels": res_lp_ch.get("rows", []),
            "landing_page_w2a": res_lp_w2a.get("rows", [])
        }
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        print(f"Cached to {cache_file}")

    # Process channels
    def is_paid(cg):
        c = (cg or "").lower()
        return "paid" in c or "display" in c or "cpc" in c

    channel_w2a_map = {}
    for r in data["channels_w2a"]:
        cg = r["dimensionValues"][0]["value"]
        cnt = int(r["metricValues"][0]["value"])
        channel_w2a_map[cg] = cnt

    total_web_sessions = 0
    total_web_users = 0
    total_web_w2a = sum(channel_w2a_map.values())
    channels_summary = []

    for r in data["channels_overview"]:
        cg = r["dimensionValues"][0]["value"]
        s = int(r["metricValues"][0]["value"])
        eng = int(r["metricValues"][1]["value"])
        u = int(r["metricValues"][2]["value"])
        w2a = channel_w2a_map.get(cg, 0)
        total_web_sessions += s
        total_web_users += u
        channels_summary.append({
            "channel_name": cg,
            "category": "Paid" if is_paid(cg) else "Non-Paid",
            "sessions": s,
            "engaged_sessions": eng,
            "users": u,
            "w2a_clicks": w2a,
            "w2a_cr": round(w2a / s, 4) if s > 0 else 0.0
        })

    for c in channels_summary:
        c["sessions_pct"] = round(c["sessions"] / total_web_sessions, 4) if total_web_sessions > 0 else 0.0

    channels_summary.sort(key=lambda x: (0 if x["category"] == "Non-Paid" else 1, -x["sessions"]))

    # Match projects
    matcher = build_theme_matcher()
    project_data = defaultdict(lambda: {
        "sessions": 0, "w2a": 0, "pages": set(),
        "channels": defaultdict(lambda: {"sessions": 0, "w2a": 0}),
        "non_paid_sessions": 0, "paid_sessions": 0,
        "non_paid_w2a": 0, "paid_w2a": 0,
        "top_pages": defaultdict(lambda: {"sessions": 0, "w2a": 0})
    })

    # W2A by (path, channel)
    lp_w2a_map = defaultdict(int)
    for r in data["landing_page_w2a"]:
        p = normalize_path(r["dimensionValues"][0]["value"])
        cg = r["dimensionValues"][1]["value"]
        w = int(r["metricValues"][0]["value"])
        lp_w2a_map[(p, cg)] += w

    for r in data["landing_page_channels"]:
        p = normalize_path(r["dimensionValues"][0]["value"])
        cg = r["dimensionValues"][1]["value"]
        s = int(r["metricValues"][0]["value"])
        w = lp_w2a_map.get((p, cg), 0)

        tid, tname, sec, mvol, proj, ptype = matcher(p)
        project_data[proj]["sessions"] += s
        project_data[proj]["w2a"] += w
        project_data[proj]["pages"].add(p)
        project_data[proj]["channels"][cg]["sessions"] += s
        project_data[proj]["channels"][cg]["w2a"] += w
        project_data[proj]["top_pages"][p]["sessions"] += s
        project_data[proj]["top_pages"][p]["w2a"] += w

        if is_paid(cg):
            project_data[proj]["paid_sessions"] += s
            project_data[proj]["paid_w2a"] += w
        else:
            project_data[proj]["non_paid_sessions"] += s
            project_data[proj]["non_paid_w2a"] += w

    projects_summary = []
    for proj, p_info in project_data.items():
        s = p_info["sessions"]
        w = p_info["w2a"]
        non_paid_s = p_info["non_paid_sessions"]
        paid_s = p_info["paid_sessions"]
        non_paid_pct = round(non_paid_s / s, 4) if s > 0 else 0.0
        paid_pct = round(paid_s / s, 4) if s > 0 else 0.0

        if non_paid_pct >= 0.8:
            health = "HEALTHY_ORGANIC"
        elif paid_pct >= 0.5:
            health = "PAID_DEPENDENT"
        else:
            health = "BALANCED"

        # Format top 3 pages
        top_p = sorted(p_info["top_pages"].items(), key=lambda x: -x[1]["sessions"])[:3]
        top_pages_list = [{"path": tp[0], "sessions": tp[1]["sessions"], "w2a_clicks": tp[1]["w2a"]} for tp in top_p]

        # Convert channels dict to regular dict
        channels_clean = {}
        for cname, cmetrics in sorted(p_info["channels"].items(), key=lambda x: -x[1]["sessions"]):
            cs = cmetrics["sessions"]
            cw = cmetrics["w2a"]
            channels_clean[cname] = {
                "sessions": cs,
                "w2a_clicks": cw,
                "w2a_cr": round(cw / cs, 4) if cs > 0 else 0.0,
                "pct": round(cs / s, 4) if s > 0 else 0.0
            }

        projects_summary.append({
            "project_name": proj,
            "pages_count": len(p_info["pages"]),
            "total_sessions": s,
            "sessions_share_pct": round(s / total_web_sessions, 4) if total_web_sessions > 0 else 0.0,
            "total_w2a_clicks": w,
            "w2a_cr": round(w / s, 4) if s > 0 else 0.0,
            "non_paid_sessions": non_paid_s,
            "non_paid_pct": non_paid_pct,
            "paid_sessions": paid_s,
            "paid_pct": paid_pct,
            "health_status": health,
            "channels": channels_clean,
            "top_pages": top_pages_list
        })

    projects_summary.sort(key=lambda x: -x["total_sessions"])

    print(f"Total Projects Processed: {len(projects_summary)}")
    print(f"Total Web Sessions: {total_web_sessions:,}")
    print(f"Total Web W2A: {total_web_w2a:,} (CR: {total_web_w2a/total_web_sessions*100:.2f}%)")
    print(f"Total Web Users: {total_web_users:,}")

    # Non-paid vs Paid totals
    tot_non_paid_s = sum(c["sessions"] for c in channels_summary if c["category"] == "Non-Paid")
    tot_paid_s = sum(c["sessions"] for c in channels_summary if c["category"] == "Paid")
    tot_non_paid_w = sum(c["w2a_clicks"] for c in channels_summary if c["category"] == "Non-Paid")
    tot_paid_w = sum(c["w2a_clicks"] for c in channels_summary if c["category"] == "Paid")

    print(f"Non-Paid Traffic : {tot_non_paid_s:,} sessions ({tot_non_paid_s/total_web_sessions*100:.1f}%) | {tot_non_paid_w:,} W2A (CR: {tot_non_paid_w/tot_non_paid_s*100:.2f}%)")
    print(f"Paid Traffic     : {tot_paid_s:,} sessions ({tot_paid_s/total_web_sessions*100:.1f}%) | {tot_paid_w:,} W2A (CR: {tot_paid_w/tot_paid_s*100:.2f}%)")

if __name__ == "__main__":
    fetch_and_test()
