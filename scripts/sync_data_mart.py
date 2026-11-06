#!/usr/bin/env python3
"""
DATA MART SYNC SCRIPT
Nạp và đồng bộ toàn diện các bảng phân tích vào SQLite Data Mart SSOT:
- dim_url_project: Ánh xạ 28,000+ URL sang Project và Hub
- dim_theme_seasonality: Chu kỳ mùa vụ 12 tháng của 236 Theme
- fact_daily_performance: Lũy kế hiệu suất MTD và xu hướng lịch sử
"""

import os
import sys
import json
import time
import re
import calendar
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.db import get_connection, init_db, DEFAULT_DB_PATH, DATA_DIR


def load_hub_map():
    hub_map_path = REPO_ROOT.parent / "Web-Idea" / "react-web-momo" / "lib" / "dashboard" / "hub-map.json"
    if not hub_map_path.exists():
        hub_map_path = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/hub-map.json")
    
    proj_to_hub = {}
    if hub_map_path.exists():
        try:
            with open(hub_map_path, "r", encoding="utf-8") as f:
                hm = json.load(f)
            for h in hm.get("hubs", []):
                hid = h.get("id", "").strip()
                hname = h.get("name", "").strip()
                for p in h.get("projects", []):
                    p_clean = p.strip()
                    proj_to_hub[p_clean.lower()] = (hid, hname, p_clean)
        except Exception as e:
            print(f"[WARN] Không nạp được hub-map.json: {e}")
    return proj_to_hub


def sync_dim_url_project(conn, proj_to_hub) -> int:
    mapping_file = DATA_DIR / "url_project_mapping.json"
    if not mapping_file.exists():
        print(f"[SKIP] Không tìm thấy {mapping_file}")
        return 0

    print(f"\n[1/3] Đang nạp {mapping_file.name}...")
    start = time.time()
    with open(mapping_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    mappings = data.get("mapping", [])
    print(f"  -> Đã đọc {len(mappings):,} URLs trong {time.time() - start:.2f}s")

    synced_at = datetime.utcnow().isoformat()
    rows = []
    for item in mappings:
        url = item.get("url", "").strip()
        if not url:
            continue
        primary_proj = (item.get("primary") or "").strip()
        match_type = item.get("match_type", "")
        
        # Bóc tách path tương đối để join với GA4 landing_page
        parsed = urlparse(url)
        path = parsed.path
        if not path:
            path = "/"
        
        hub_info = proj_to_hub.get(primary_proj.lower())
        if hub_info:
            hub_id, hub_name, canonical_proj = hub_info
        else:
            hub_id = "others"
            hub_name = "Khác"
            canonical_proj = primary_proj

        rows.append((url, path, canonical_proj, hub_id, hub_name, match_type, synced_at))

    print(f"  -> Đang nạp {len(rows):,} bản ghi vào dim_url_project...")
    t_ins = time.time()
    with conn:
        conn.executemany("""
            INSERT OR REPLACE INTO dim_url_project 
            (url, path, primary_project, hub_id, hub_name, match_type, synced_at)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """, rows)
    print(f"  -> Hoàn thành dim_url_project trong {time.time() - t_ins:.2f}s")
    return len(rows)


def sync_dim_theme_seasonality(conn) -> int:
    season_file = DATA_DIR / "theme_seasonality.json"
    if not season_file.exists():
        print(f"[SKIP] Không tìm thấy {season_file}")
        return 0

    print(f"\n[2/3] Đang nạp {season_file.name}...")
    start = time.time()
    with open(season_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    themes = data.get("themes", [])
    print(f"  -> Đã đọc {len(themes):,} themes trong {time.time() - start:.2f}s")

    synced_at = datetime.utcnow().isoformat()
    rows = []
    for t in themes:
        tid = t.get("theme_id", "")
        name = t.get("name", "")
        sector = t.get("sector", "")
        pillar = t.get("pillar", "")
        vol = int(t.get("volume", 0))
        m = t.get("monthly", [0] * 12)
        if len(m) < 12:
            m = m + [0] * (12 - len(m))
        rows.append((tid, name, sector, pillar, vol, m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], synced_at))

    print(f"  -> Đang nạp {len(rows):,} bản ghi vào dim_theme_seasonality...")
    t_ins = time.time()
    with conn:
        conn.executemany("""
            INSERT OR REPLACE INTO dim_theme_seasonality
            (theme_id, name, sector, pillar, volume, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, synced_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, rows)
    print(f"  -> Hoàn thành dim_theme_seasonality trong {time.time() - t_ins:.2f}s")
    return len(rows)


def sync_fact_daily_performance(conn) -> int:
    print(f"\n[3/3] Đang quét và đồng bộ fact_daily_performance từ snapshots MTD...")
    synced_at = datetime.utcnow().isoformat()
    rows = []

    for p in sorted(DATA_DIR.glob("monthly_*_*_mtd_*d.json")):
        try:
            match = re.fullmatch(r"monthly_(\d{2})_(\d{4})_mtd_(\d+)d\.json", p.name)
            if not match:
                continue
            month, year, file_days = map(int, match.groups())
            month_length = calendar.monthrange(year, month)[1]
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
            days = d.get("days_elapsed", 0)
            if days != file_days or not 1 <= days <= month_length:
                continue
            date_str = f"{year:04d}-{month:02d}-{days:02d}"
            total_pv = d.get("actual_mtd_pv", 0)
            target_pv = d.get("target_pv", d.get("target_oct_pv"))
            if target_pv is None:
                continue
            progress_pct = d.get("progress_pct", 0.0)
            forecast_pv = d.get("forecast_31d", 0.0)
            forecast_pct = d.get("forecast_pct", 0.0)
            sessions = d.get("sessions", 0)
            users = d.get("users", 0)

            ch = d.get("channels", {})
            org = ch.get("organic", {}).get("pv", 0)
            dir_pv = ch.get("direct", {}).get("pv", 0)
            paid_pv = ch.get("paid", {}).get("pv", 0)
            ref_pv = ch.get("referral", {}).get("pv", 0)
            oth_pv = ch.get("others", {}).get("pv", 0)
            non_paid = ch.get("non_paid_total", {}).get("pv", 0)

            rows.append((
                date_str, days, month_length, total_pv, target_pv, org, dir_pv, paid_pv,
                ref_pv, oth_pv, non_paid, sessions, users, progress_pct,
                forecast_pv, forecast_pct, synced_at
            ))
        except Exception as e:
            print(f"[WARN] Bỏ qua {p.name}: {e}")

    if rows:
        with conn:
            conn.executemany("""
                INSERT OR REPLACE INTO fact_daily_performance
                (date, days_elapsed, days_in_month, total_pv, target_pv, organic_pv,
                 direct_pv, paid_pv, referral_pv, others_pv, non_paid_pv, sessions,
                 users, progress_pct, forecast_pv, forecast_pct, synced_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, rows)
        print(f"  -> Đã nạp {len(rows)} ngày hiệu suất vào fact_daily_performance.")
    return len(rows)


def main():
    print("=" * 70)
    print("KHỞI TẠO VÀ ĐỒNG BỘ LOCAL DATA MART (SQLITE SSOT)")
    print(f"Database Target: {DEFAULT_DB_PATH}")
    print("=" * 70)

    init_db()
    conn = get_connection()
    proj_to_hub = load_hub_map()

    t0 = time.time()
    n_urls = sync_dim_url_project(conn, proj_to_hub)
    n_themes = sync_dim_theme_seasonality(conn)
    n_days = sync_fact_daily_performance(conn)
    conn.close()

    print("\n" + "=" * 70)
    print(f"TỔNG KẾT ĐỒNG BỘ DATA MART HOÀN TẤT ({time.time() - t0:.2f}s):")
    print(f"- dim_url_project: {n_urls:,} bản ghi")
    print(f"- dim_theme_seasonality: {n_themes:,} themes")
    print(f"- fact_daily_performance: {n_days} mốc ngày MTD")
    print("=" * 70)


if __name__ == "__main__":
    main()
