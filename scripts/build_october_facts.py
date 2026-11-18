#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TẠO SNAPSHOT SỐ LIỆU THÁNG 10/2026 (SSOT) CHO TOÀN BỘ BÁO CÁO

Mục đích: chấm dứt tình trạng mỗi báo cáo (PPTX, Markdown, Hub) giữ một bộ số
hardcode khác nhau. Mọi artifact tháng 10 đều đọc từ file facts này.

Nguồn:
  1. GA4 Data API MTD 30 ngày: 07_REPORTS/data/monthly_10_2026_consolidated.json
  2. GA4 Data API tháng 9:     07_REPORTS/data/monthly_09_2026_full_month_30d.json
  3. Excel SSOT Hub/Project:   07_REPORTS/web_performance_tracking.xlsx
     -> phản chiếu tại react-web-momo/lib/dashboard/web-data.json (pivot Full month)
  4. Danh mục project theo Hub: react-web-momo/lib/dashboard/hub-map.json

Cách dùng:
    ./.venv/bin/python scripts/build_october_facts.py
    ./.venv/bin/python scripts/build_october_facts.py --check   # chỉ in, không ghi
"""

import argparse
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_DIR = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
if not HUBS_DIR.exists():
    HUBS_DIR = Path("/Users/hienhv/Hienhv/Klaus/Web-Idea/react-web-momo")

OUT_PATH = BASE_DIR / "07_REPORTS" / "data" / "october_2026_facts.json"
DAYS_ELAPSED = 31
DAYS_IN_MONTH = 31


def pct(cur, prev):
    return round((cur / prev - 1) * 100, 1) if prev else None


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="In kết quả, không ghi file")
    args = parser.parse_args()

    oct_ga4 = load(BASE_DIR / "07_REPORTS" / "data" / "monthly_10_2026_consolidated.json")
    sep_ga4 = load(BASE_DIR / "07_REPORTS" / "data" / "monthly_09_2026_full_month_30d.json")
    web = load(HUBS_DIR / "lib" / "dashboard" / "web-data.json")
    hub_map = load(HUBS_DIR / "lib" / "dashboard" / "hub-map.json")

    months = web["months"]
    oct_i, sep_i = months.index("2026-10"), months.index("2026-09")
    proj = {p["name"]: p for p in web["projects"]}

    total_oct = sum(sum(p["full"][oct_i]) for p in web["projects"])
    total_sep = sum(sum(p["full"][sep_i]) for p in web["projects"])
    target = int(oct_ga4["target_mtd_pv"]) if oct_ga4.get("target_mtd_pv") else 3665607
    forecast = round(total_oct / DAYS_ELAPSED * DAYS_IN_MONTH)

    channels = {}
    for key in ("organic", "paid", "direct", "referral", "others"):
        cur = oct_ga4["channels"][key]["pv"]
        prev = sep_ga4["channels"][key]["pv"]
        channels[key] = {"oct": cur, "sep": prev, "mom_pct": pct(cur, prev)}
    channels["non_paid"] = {
        "oct": oct_ga4["channels"]["non_paid_total"]["pv"],
        "sep": sum(sep_ga4["channels"][k]["pv"] for k in ("organic", "direct", "referral", "others")),
    }
    channels["non_paid"]["mom_pct"] = pct(channels["non_paid"]["oct"], channels["non_paid"]["sep"])

    def hub_block(hub_id):
        projects = [n for n in next(h["projects"] for h in hub_map["hubs"] if h["id"] == hub_id) if n in proj]
        cur = [0] * 5
        prev = [0] * 5
        for n in projects:
            for i in range(5):
                cur[i] += proj[n]["full"][oct_i][i]
                prev[i] += proj[n]["full"][sep_i][i]
        oct_pv, sep_pv = sum(cur), sum(prev)
        return {
            "oct_pv": oct_pv,
            "sep_pv": sep_pv,
            "mom_pct": pct(oct_pv, sep_pv),
            "forecast": round(oct_pv / DAYS_ELAPSED * DAYS_IN_MONTH),
            "organic_pv": cur[0],
            "organic_share": round(cur[0] / oct_pv * 100, 1) if oct_pv else None,
            "organic_share_sep": round(prev[0] / sep_pv * 100, 1) if sep_pv else None,
            "non_paid_pv": oct_pv - cur[1],
            "non_paid_share": round((oct_pv - cur[1]) / oct_pv * 100, 1) if oct_pv else None,
            "non_paid_share_sep": round((sep_pv - prev[1]) / sep_pv * 100, 1) if sep_pv else None,
            "paid_pv": cur[1],
            "projects": {n: sum(proj[n]["full"][oct_i]) for n in projects},
        }

    def project_block(name):
        p = proj[name]
        cur = sum(p["full"][oct_i])
        prev = sum(p["full"][sep_i])
        return {
            "oct_pv": cur,
            "sep_pv": prev,
            "delta": cur - prev,
            "mom_pct": pct(cur, prev),
            "organic_pv": p["full"][oct_i][0],
            "paid_pv": p["full"][oct_i][1],
            "paid_sep_pv": p["full"][sep_i][1],
        }

    rank = [
        p["name"]
        for p in sorted(web["projects"], key=lambda x: -sum(x["full"][oct_i]))
    ]

    facts = {
        "period": {
            "month": "2026-10",
            "start": "2026-10-01",
            "end": "2026-10-30",
            "days_elapsed": DAYS_ELAPSED,
            "days_in_month": DAYS_IN_MONTH,
        },
        "total": {
            "oct_pv": total_oct,
            "sep_pv": total_sep,
            "target": target,
            "achievement_rate": round(total_oct / target * 100, 1),
            "forecast": forecast,
            "forecast_rate": round(forecast / target * 100, 1),
            "mom_pct": pct(total_oct, total_sep),
            "daily_pace": round(total_oct / DAYS_ELAPSED),
        },
        "channels": channels,
        "geo_ai": {
            "oct": 18547, "sep": 13596, "mom_pct": pct(18547, 13596), "verified": True,
            "source": "GA4 sessionSource, 31 ngày, cùng danh sách nguồn cho tháng 9",
            "breakdown": {
                "ChatGPT": {"oct": 17739, "sep": 12589},
                "Perplexity": {"oct": 284, "sep": 239},
                "Gemini": {"oct": 467, "sep": 704},
                "Khác (Claude, Copilot.com, OpenAI, Meta)": {"oct": 57, "sep": 64},
            },
        },
        "minigame_mot_mua_quyt": {"active_players": 7097, "period": "2026-10-15/2026-10-25"},
        "hubs": {"cinema": hub_block("cinema"), "financial": hub_block("financial")},
        "projects": {
            n: project_block(n)
            for n in (
                "Cinema_Cineplex Page",
                "Cinema_Page",
                "Cinema_Blog",
                "Cinema_Home Page",
                "Vay Nhanh",
                "Ví Trả Sau",
                "Trung Tâm Tài Chính",
                "Điểm Tín Dụng",
                "Quản Lý Chi Tiêu",
                "Phạt Nguội",
            )
        },
        "sources": {
            "total_and_channels": "GA4 Data API 01-30/10 (monthly_10_2026_consolidated.json) + T9 full month",
            "hubs_and_projects": "07_REPORTS/web_performance_tracking.xlsx pivot Full month, tên project chuẩn hóa theo hub-map.json",
        },
    }
    facts["projects"]["Phạt Nguội"]["rank"] = rank.index("Phạt Nguội") + 1
    facts["projects"]["Phạt Nguội"]["rank_total"] = len(rank)

    cinema = facts["hubs"]["cinema"]
    cinema["target"] = 1117378
    cinema["achievement_rate"] = round(cinema["oct_pv"] / cinema["target"] * 100, 1)
    cinema["cineplex"] = facts["projects"]["Cinema_Cineplex Page"]
    cinema["cineplex"]["share_of_hub"] = round(cinema["cineplex"]["oct_pv"] / cinema["oct_pv"] * 100, 1)
    cinema["cineplex"]["organic_sep"] = proj["Cinema_Cineplex Page"]["full"][sep_i][0]

    financial = facts["hubs"]["financial"]
    financial["target"] = 250000
    financial["achievement_rate"] = round(financial["oct_pv"] / financial["target"] * 100, 1)

    text = json.dumps(facts, ensure_ascii=False, indent=2)
    if args.check:
        print(text)
        return
    OUT_PATH.write_text(text, encoding="utf-8")
    print(f"Đã ghi: {OUT_PATH}")
    print(f"  Tổng T10: {total_oct:,} PV | Target {target:,} | Đạt {facts['total']['achievement_rate']}% "
          f"| Forecast {forecast:,} ({facts['total']['forecast_rate']}%) | MoM {facts['total']['mom_pct']}%")
    for hid in ("cinema", "financial"):
        h = facts["hubs"][hid]
        print(f"  {hid:10} {h['oct_pv']:>10,} PV | MoM {h['mom_pct']:+.1f}% | đạt {h['achievement_rate']}% target")
    pn = facts["projects"]["Phạt Nguội"]
    print(f"  Phạt Nguội {pn['oct_pv']:,} PV | MoM {pn['mom_pct']:+.1f}% | hạng {pn['rank']}/{pn['rank_total']}")


if __name__ == "__main__":
    main()
