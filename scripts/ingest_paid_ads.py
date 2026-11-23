#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nạp dữ liệu Paid Ads thủ công từ file export GA4 Explore (CSV).

Thay thế scripts/sync_paid_ads.py (GA4 Data API) đã archive do policy cấm API.

Cách dùng:
    # Cách 1: chỉ định file trực tiếp
    ./.venv/bin/python scripts/ingest_paid_ads.py traffic.csv [events.csv] --start 2026-11-01 --end 2026-11-19

    # Cách 2: không tham số -> tự quét ~/Downloads tìm CSV GA4 Explore mới nhất
    ./.venv/bin/python scripts/ingest_paid_ads.py

Yêu cầu export GA4 Explore (Free form):
    Traffic file:
        Dimensions: Page path, Session source / medium
                    (+ tùy chọn: Session campaign, Session manual ad content)
        Metrics:    Views, Sessions, Total users
        Filter:     Session medium in (cpc, paid, NativeAds, ads)
                    hoặc Session default channel group = Paid
    Events file (tùy chọn, để tính W2A CVR):
        Dimensions: Event name, Page path
        Metrics:    Event count
        Filter:     Event name in (click_to_app, gmc_1vuquyt_install, gmc_1vuquyt_clickplay)

Output: 07_REPORTS/data/analytics/paid_ads_performance.json (ghi đè snapshot cũ)
"""

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
JSON_OUTPUT = BASE_DIR / "07_REPORTS" / "data" / "analytics" / "paid_ads_performance.json"
DOWNLOADS = Path.home() / "Downloads"

PAID_MEDIUMS = {"cpc", "paid", "nativeads", "ads", "ppc"}
W2A_EVENTS = {"click_to_app", "gmc_1vuquyt_install", "gmc_1vuquyt_clickplay"}


def norm_header(h: str) -> str:
    return re.sub(r"\s+", " ", h.strip().lower())


def parse_ga4_csv(path: Path):
    """Đọc GA4 Explore CSV: bỏ dòng comment '#', trả (headers, rows dict)."""
    rows = list(csv.reader(open(path, encoding="utf-8-sig")))
    header_idx = None
    for i, r in enumerate(rows):
        if r and not r[0].strip().startswith("#") and any(c.strip() for c in r):
            header_idx = i
            break
    if header_idx is None:
        raise ValueError(f"{path}: không tìm thấy header row")
    headers = [norm_header(c) for c in rows[header_idx]]
    data = []
    for r in rows[header_idx + 1:]:
        if not r or not any(c.strip() for c in r):
            continue
        if r[0].strip().startswith("#"):
            continue
        rec = {}
        for j, h in enumerate(headers):
            rec[h] = r[j].strip() if j < len(r) else ""
        data.append(rec)
    return headers, data


def to_int(v) -> int:
    if v is None:
        return 0
    s = str(v).strip().replace(",", "").replace(".", "")
    # GA4 export đôi khi dùng dấu . phân cách nghìn kiểu VN hoặc để trống
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    s2 = str(v).strip().replace(",", "")
    try:
        return int(float(s2))
    except ValueError:
        return 0


def pick_col(rec: dict, *keywords: str) -> str:
    """Tìm giá trị cột đầu tiên có header chứa đủ các keyword. Bỏ qua cột '(previous)'."""
    for h, v in rec.items():
        if "previous" in h:
            continue
        if all(k in h for k in keywords):
            return v
    return ""


def classify_hub(page_path: str) -> str:
    path = (page_path or "/").lower()
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


def is_paid_source_medium(sm: str) -> bool:
    medium = sm.split("/")[-1].strip().lower() if "/" in sm else ""
    return medium in PAID_MEDIUMS or sm.strip().lower() in PAID_MEDIUMS


def detect_file_kind(headers: list) -> str:
    has_sm = any("source" in h and "medium" in h for h in headers)
    has_ch = any("channel group" in h or "default channel" in h for h in headers)
    has_evt = any("event name" in h for h in headers)
    has_page = any("page" in h for h in headers)
    if has_evt and has_page:
        return "events"
    if (has_sm or has_ch) and has_page:
        return "traffic"
    return "unknown"


def find_candidate_files():
    """Quét ~/Downloads: CSV có header chứa page + source/medium hoặc event name."""
    cands = []
    for p in sorted(DOWNLOADS.glob("*.csv"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            with open(p, encoding="utf-8-sig") as f:
                head = "".join([next(f, "") for _ in range(8)])
            low = head.lower()
            if "page" in low and ("source" in low or "event name" in low):
                cands.append(p)
        except Exception:
            continue
    return cands


def main():
    ap = argparse.ArgumentParser(description="Nạp Paid Ads từ GA4 Explore CSV export")
    ap.add_argument("files", nargs="*", help="CSV export(s). Bỏ trống = tự quét ~/Downloads")
    ap.add_argument("--start", help="Start date YYYY-MM-DD (ghi vào meta)")
    ap.add_argument("--end", help="End date YYYY-MM-DD (ghi vào meta)")
    ap.add_argument("--output", default=str(JSON_OUTPUT))
    args = ap.parse_args()

    files = [Path(f) for f in args.files] if args.files else find_candidate_files()
    if not files:
        print("Không tìm thấy CSV GA4 Explore phù hợp trong ~/Downloads.")
        sys.exit(1)

    traffic_path = events_path = None
    traffic_rows = events_rows = None
    for p in files:
        if not p.exists():
            print(f"Bỏ qua {p}: không tồn tại")
            continue
        headers, data = parse_ga4_csv(p)
        kind = detect_file_kind(headers)
        print(f"  {p.name}: {len(data)} rows, kind={kind}")
        if kind == "traffic" and traffic_path is None:
            traffic_path, traffic_rows = p, data
        elif kind == "events" and events_path is None:
            events_path, events_rows = p, data

    if traffic_path is None:
        print("Thiếu file traffic (cần cột Page path + Session source/medium).")
        sys.exit(1)

    # ---- Aggregate traffic ----
    channels = defaultdict(lambda: {"pv": 0, "sessions": 0, "users": 0, "pages": set()})
    pages = defaultdict(lambda: {
        "pv": 0, "sessions": 0, "users": 0,
        "channels": defaultdict(int), "campaigns": set(), "creatives": set(),
    })
    total_pv = total_sess = 0

    for rec in traffic_rows:
        page = pick_col(rec, "page path") or pick_col(rec, "page")
        sm = pick_col(rec, "source", "medium") or pick_col(rec, "source / medium") or pick_col(rec, "session source")
        if not page or page in ("(not set)", "(data not available)"):
            continue
        # Nếu export không có source/medium mà có channel group -> dùng channel group
        medium = sm.split("/")[-1].strip() if "/" in sm else ""
        channel_group = pick_col(rec, "channel group") or pick_col(rec, "default channel")
        if is_paid_source_medium(sm):
            pass
        elif "paid" in channel_group.lower():
            sm = sm or f"(channel) {channel_group}"
        else:
            continue

        pv = to_int(pick_col(rec, "views") or pick_col(rec, "screen page views") or pick_col(rec, "pageviews"))
        sess = to_int(pick_col(rec, "sessions"))
        users = to_int(pick_col(rec, "total users") or pick_col(rec, "users"))
        campaign = pick_col(rec, "campaign")
        creative = pick_col(rec, "ad content") or pick_col(rec, "manual ad content") or pick_col(rec, "creative")

        sm = sm or "(unknown)"
        channels[sm]["pv"] += pv
        channels[sm]["sessions"] += sess
        channels[sm]["users"] += users
        channels[sm]["pages"].add(page)

        pg = pages[page]
        pg["pv"] += pv
        pg["sessions"] += sess
        pg["users"] += users
        pg["channels"][sm] += pv
        if campaign and campaign not in ("(not set)", "(data not available)"):
            pg["campaigns"].add(campaign)
        if creative and creative not in ("(not set)", "(data not available)"):
            pg["creatives"].add(creative)
        total_pv += pv
        total_sess += sess

    # ---- W2A conversions từ events file ----
    page_conv = defaultdict(lambda: {"w2a_clicks": 0, "installs": 0, "clickplay": 0})
    if events_path:
        for rec in events_rows:
            evt = pick_col(rec, "event name")
            page = pick_col(rec, "page path") or pick_col(rec, "page")
            cnt = to_int(pick_col(rec, "event count") or pick_col(rec, "events"))
            if evt == "click_to_app":
                page_conv[page]["w2a_clicks"] += cnt
            elif evt == "gmc_1vuquyt_install":
                page_conv[page]["installs"] += cnt
            elif evt == "gmc_1vuquyt_clickplay":
                page_conv[page]["clickplay"] += cnt

    # ---- Build landing_pages ----
    landing_pages = []
    for path, d in pages.items():
        conv = page_conv.get(path, {"w2a_clicks": 0, "installs": 0, "clickplay": 0})
        w2a = conv["w2a_clicks"] + conv["installs"] + conv["clickplay"]
        primary = max(d["channels"].items(), key=lambda x: x[1])[0] if d["channels"] else ""
        landing_pages.append({
            "host_name": "www.momo.vn",
            "page_path": path,
            "full_url": f"https://www.momo.vn{path}",
            "hub": classify_hub(path),
            "pageviews": d["pv"],
            "sessions": d["sessions"],
            "users": d["users"],
            "w2a_conversions": w2a,
            "w2a_clicks": conv["w2a_clicks"],
            "installs": conv["installs"],
            "clickplay": conv["clickplay"],
            "cvr_percent": round(w2a / d["pv"] * 100, 2) if d["pv"] else 0.0,
            "primary_channel": primary,
            "channels_breakdown": dict(sorted(d["channels"].items(), key=lambda x: -x[1])),
            "campaigns": sorted(d["campaigns"])[:20],
            "creatives": sorted(d["creatives"])[:20],
        })
    landing_pages.sort(key=lambda x: -x["pageviews"])

    channels_out = []
    for sm, d in sorted(channels.items(), key=lambda x: -x[1]["pv"]):
        channels_out.append({
            "channel": sm,
            "pageviews": d["pv"],
            "sessions": d["sessions"],
            "users": d["users"],
            "share_percent": round(d["pv"] / total_pv * 100, 2) if total_pv else 0.0,
            "active_pages_count": len(d["pages"]),
        })

    payload = {
        "updated_at": date.today().isoformat(),
        "source": "manual_ga4_explore_csv",
        "date_range": {"start_date": args.start or "", "end_date": args.end or ""},
        "input_files": [str(p) for p in files if p.exists()],
        "summary": {
            "total_paid_pageviews": total_pv,
            "total_paid_sessions": total_sess,
            "active_landing_pages_count": len(landing_pages),
            "active_channels_count": len(channels_out),
        },
        "channels": channels_out,
        "landing_pages": landing_pages,
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    json.dump(payload, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    s = payload["summary"]
    print(f"\n=== PAID ADS INGEST SUCCESS ===")
    print(f"Traffic file : {traffic_path.name}")
    print(f"Events file  : {events_path.name if events_path else '(không có - W2A = 0)'}")
    print(f"Tổng Paid PV: {s['total_paid_pageviews']:,} | Sessions: {s['total_paid_sessions']:,} | Pages: {s['active_landing_pages_count']} | Channels: {s['active_channels_count']}")
    print(f"Output       : {out}")
    print("\nTop 5 kênh:")
    for c in channels_out[:5]:
        print(f"  {c['channel']:<35} {c['pageviews']:>10,} PV ({c['share_percent']}%)")


if __name__ == "__main__":
    main()
