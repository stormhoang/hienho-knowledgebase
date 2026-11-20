#!/usr/bin/env python3
"""
Ingest GSC MTD manual export (ZIP or extracted folder) into:
1. 07_REPORTS/data/analytics/gsc_mtd_performance_2026.json (Macro MTD analytics)
2. 07_REPORTS/data/analytics/page_mtd.json (Schema v2 with updated GSC metrics)
3. Syncs to react-web-momo/data/analytics/page_mtd.json

Compliance:
- SPEC-page-mtd.md: Strict 10 clean steps, GSC field omission, coverage & checks.
- AGENTS.md: No external API calls, pure local processing.
"""

import os
import sys
import json
import csv
import zipfile
import io
import re
import urllib.request
import urllib.parse
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import scripts.lib.url_project_resolver as upr

KB_DATA_DIR = BASE_DIR / "07_REPORTS" / "data"
GSC_EXPORTS_DIR = KB_DATA_DIR / "gsc_exports"
ANALYTICS_DIR = KB_DATA_DIR / "analytics"
PAGE_MTD_KB = ANALYTICS_DIR / "page_mtd.json"
PAGE_MTD_HUB = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/analytics/page_mtd.json")
HUB_MAP_PATH = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/hub-map.json")

def get_sheets_token():
    """Lấy token xác thực Google OAuth có quyền truy cập Drive / Sheets."""
    tpath = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
    cpath = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json.disabled"
    if not cpath.exists():
        cpath = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"

    with open(tpath, "r", encoding="utf-8") as f:
        tdata = json.load(f)
    with open(cpath, "r", encoding="utf-8") as f:
        cdata = json.load(f).get("installed", {})

    data = urllib.parse.urlencode({
        "client_id": cdata["client_id"],
        "client_secret": cdata["client_secret"],
        "refresh_token": tdata["refresh_token"],
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())["access_token"]

def download_sheet_csv(sheet_url, dest_csv_path):
    """Tải file CSV từ Google Sheets URL qua OAuth Bearer Token."""
    m_id = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", sheet_url)
    if not m_id:
        raise ValueError(f"Không nhận diện được Spreadsheet ID từ URL: {sheet_url}")
    sheet_id = m_id.group(1)

    m_gid = re.search(r"[#&?]gid=([0-9]+)", sheet_url)
    gid = m_gid.group(1) if m_gid else str(get_latest_sas_gid(sheet_url))

    token = get_sheets_token()
    export_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    req_export = urllib.request.Request(export_url, headers={"Authorization": f"Bearer {token}"})

    with urllib.request.urlopen(req_export, timeout=60) as resp:
        content = resp.read()

    dest_csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_csv_path, "wb") as f:
        f.write(content)

    print(f"✓ Đã tải {len(content):,} bytes từ Google Sheets ({sheet_id}, gid={gid}) -> {dest_csv_path.name}")
    return dest_csv_path

def get_latest_sas_gid(sheet_url):
    """Tự động tìm tab mới nhất có tên dạng SAS_YYYY-MM-DD_... trong spreadsheet."""
    m_id = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", sheet_url)
    if not m_id:
        raise ValueError(f"Không nhận diện được Spreadsheet ID từ URL: {sheet_url}")
    sheet_id = m_id.group(1)

    token = get_sheets_token()
    meta_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}?fields=sheets.properties.title,sheets.properties.sheetId"
    req = urllib.request.Request(meta_url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        meta = json.loads(resp.read().decode())

    sas_tabs = [s["properties"] for s in meta.get("sheets", [])
                if s["properties"].get("title", "").startswith("SAS_")]
    if not sas_tabs:
        raise RuntimeError(f"Không tìm thấy tab SAS_* nào trong spreadsheet {sheet_id}")
    sas_tabs.sort(key=lambda t: t["title"], reverse=True)
    latest = sas_tabs[0]
    print(f"📑 Tab GSC mới nhất: {latest['title']} (gid={latest['sheetId']})")
    return latest["sheetId"]

def load_hub_map():
    proj_to_hub = {}
    if HUB_MAP_PATH.exists():
        with open(HUB_MAP_PATH, "r", encoding="utf-8") as f:
            hm = json.load(f)
            for h in hm.get("hubs", []):
                hname = h["name"]
                for p in h.get("projects", []):
                    proj_to_hub[p.lower()] = hname
    return proj_to_hub

def ingest_gsc(zip_or_dir_path, start_override=None, end_override=None, push_hubs=False):
    target_path = Path(zip_or_dir_path)
    if not target_path.exists():
        print(f"❌ File/thư mục không tồn tại: {target_path}")
        sys.exit(1)

    # 1. Trích xuất hoặc xác định thư mục CSV
    export_dir = None
    source_filename = target_path.name
    
    if target_path.is_file() and target_path.suffix == ".zip":
        export_date = "2026-11-20"
        export_dir = GSC_EXPORTS_DIR / export_date
        export_dir.mkdir(parents=True, exist_ok=True)
        print(f"📦 Đang giải nén {target_path} vào {export_dir}...")
        with zipfile.ZipFile(target_path, "r") as z:
            z.extractall(export_dir)
    elif target_path.is_dir():
        export_dir = target_path
    else:
        print(f"❌ Không hỗ trợ định dạng: {target_path}")
        sys.exit(1)

    # Đọc các file CSV
    chart_file = export_dir / "Chart.csv"
    pages_file = export_dir / "Pages_full_20k.csv" if (export_dir / "Pages_full_20k.csv").exists() else (export_dir / "Pages.csv")
    queries_file = export_dir / "Queries.csv"
    countries_file = export_dir / "Countries.csv"
    devices_file = export_dir / "Devices.csv"
    search_app_file = export_dir / "Search appearance.csv"
    filters_file = export_dir / "Filters.csv"

    # 2. Đọc Filters để xác định date range
    date_filter = "Nov 1, 2026-Nov 19, 2026"
    if filters_file.exists():
        with open(filters_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                if r.get("Filter") == "Date":
                    date_filter = r.get("Value")
    print(f"📅 Filter date: {date_filter}")

    # 3. Phân tích Chart.csv (Daily)
    daily_chart = []
    total_clicks = 0
    total_impressions = 0
    weighted_pos_sum = 0.0

    if chart_file.exists():
        with open(chart_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                dt = r["Date"]
                c = int(r["Clicks"])
                imp = int(r["Impressions"])
                pos = float(r["Position"])
                ctr = float(r["CTR"].replace("%", ""))
                total_clicks += c
                total_impressions += imp
                weighted_pos_sum += pos * imp
                daily_chart.append({
                    "date": dt,
                    "clicks": c,
                    "impressions": imp,
                    "ctr_pct": ctr,
                    "position": pos
                })

    avg_ctr = (total_clicks / total_impressions * 100) if total_impressions else 0.0
    avg_pos = (weighted_pos_sum / total_impressions) if total_impressions else 0.0

    start_date = daily_chart[0]["date"] if daily_chart else (start_override or "")
    end_date = daily_chart[-1]["date"] if daily_chart else (end_override or "")
    if not start_date or not end_date:
        print("❌ Thiếu Chart.csv và không có --start/--end. Truyền: --start YYYY-MM-DD --end YYYY-MM-DD")
        sys.exit(1)

    # 4. Phân tích Devices.csv
    devices_data = []
    if devices_file.exists():
        with open(devices_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                devices_data.append({
                    "device": r["Device"],
                    "clicks": int(r["Clicks"]),
                    "impressions": int(r["Impressions"]),
                    "ctr_pct": float(r["CTR"].replace("%", "")),
                    "avg_position": float(r["Position"])
                })

    # 5. Phân tích Search Appearance
    search_app_data = []
    if search_app_file.exists():
        with open(search_app_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                search_app_data.append({
                    "appearance": r["Search Appearance"],
                    "clicks": int(r["Clicks"]),
                    "impressions": int(r["Impressions"]),
                    "ctr_pct": float(r["CTR"].replace("%", "")),
                    "avg_position": float(r["Position"])
                })

    # 6. Phân tích Top Queries
    top_queries = []
    if queries_file.exists():
        with open(queries_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, r in enumerate(reader):
                if i >= 20: break
                top_queries.append({
                    "query": r["Top queries"],
                    "clicks": int(r["Clicks"]),
                    "impressions": int(r["Impressions"]),
                    "ctr_pct": float(r["CTR"].replace("%", "")),
                    "position": float(r["Position"])
                })

    # 7. Phân tích Pages.csv và Map Hub
    rules = upr.load_rules()
    inferred = upr.load_inferred_rules()
    proj_to_hub = load_hub_map()

    hub_stats = {}
    gsc_pages_dict = {}
    top_pages = []

    if pages_file.exists():
        print(f"📄 Đang xử lý tệp Pages: {pages_file.name}...")
        with open(pages_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, r in enumerate(reader):
                url = r.get("Top pages") or r.get("Page")
                if not url:
                    continue
                c = int(str(r["Clicks"]).replace(",", "").strip())
                imp = int(str(r["Impressions"]).replace(",", "").strip())
                pos = float(str(r["Position"]).strip())
                ctr_raw = str(r["CTR"]).replace("%", "").strip()
                ctr = float(ctr_raw) if ctr_raw else 0.0

                if i < 20:
                    top_pages.append({
                        "url": url,
                        "clicks": c,
                        "impressions": imp,
                        "ctr_pct": ctr,
                        "position": pos
                    })

                # Chuẩn hóa path cho page_mtd
                u = urlparse(url)
                p = u.path or "/"
                if p != "/" and p.endswith("/"):
                    p = p[:-1]

                if p not in gsc_pages_dict:
                    gsc_pages_dict[p] = {"clicks": 0, "impressions": 0, "weighted_pos": 0.0}
                gsc_pages_dict[p]["clicks"] += c
                gsc_pages_dict[p]["impressions"] += imp
                gsc_pages_dict[p]["weighted_pos"] += pos * imp

                # Map Hub
                res = upr.resolve(url, rules, inferred)
                proj = res.get("primary") or "Others"
                hub = proj_to_hub.get(proj.lower(), "Khác")

                if hub not in hub_stats:
                    hub_stats[hub] = {"pages": 0, "clicks": 0, "impressions": 0, "weighted_pos": 0.0}
                hub_stats[hub]["pages"] += 1
                hub_stats[hub]["clicks"] += c
                hub_stats[hub]["impressions"] += imp
                hub_stats[hub]["weighted_pos"] += pos * imp

    performance_by_hub = []
    for hub, d in sorted(hub_stats.items(), key=lambda x: x[1]["clicks"], reverse=True):
        w_pos = round(d["weighted_pos"] / d["impressions"], 2) if d["impressions"] else 0.0
        h_ctr = round(d["clicks"] / d["impressions"] * 100, 2) if d["impressions"] else 0.0
        performance_by_hub.append({
            "hub_name": hub,
            "pages_count": d["pages"],
            "clicks": d["clicks"],
            "impressions": d["impressions"],
            "ctr_pct": h_ctr,
            "avg_position": w_pos
        })

    # 8. Tạo file analytics macro MTD
    macro_mtd_data = {
        "_meta": {
            "title": f"MoMo Web Platform Google Search Console MTD Performance ({len(daily_chart) or 'MTD'} Days)",
            "source_archive": str(target_path),
            "period": f"{start_date} to {end_date}",
            "days_elapsed": len(daily_chart),
            "updated_at": __import__("datetime").date.today().isoformat(),
            "total_clicks": total_clicks,
            "total_impressions": total_impressions,
            "average_ctr_pct": round(avg_ctr, 2),
            "average_position": round(avg_pos, 2)
        },
        "devices": devices_data,
        "search_appearance": search_app_data,
        "performance_by_hub": performance_by_hub,
        "top_pages": top_pages,
        "top_queries": top_queries,
        "daily_trend": daily_chart
    }

    macro_out_file = ANALYTICS_DIR / "gsc_mtd_performance_2026.json"
    with open(macro_out_file, "w", encoding="utf-8") as f:
        json.dump(macro_mtd_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã ghi GSC MTD Macro Analytics: {macro_out_file}")

    # 9. Cập nhật GSC vào page_mtd.json (Schema v2)
    if not PAGE_MTD_KB.exists():
        print(f"❌ Không tìm thấy {PAGE_MTD_KB}")
        return

    with open(PAGE_MTD_KB, "r", encoding="utf-8") as f:
        page_mtd = json.load(f)

    # Cập nhật gsc_period
    page_mtd["gsc_period"] = {"start": start_date, "end": end_date}
    # gsc_prev_period tương ứng tháng trước (1-19/10)
    # Cùng kỳ ngày tháng trước
    from datetime import date as _date
    _e = _date.fromisoformat(end_date); _s = _date.fromisoformat(start_date)
    _pm = _e.month - 1 or 12; _py = _e.year - (1 if _e.month == 1 else 0)
    import calendar as _cal
    _pend = _date(_py, _pm, min(_e.day, _cal.monthrange(_py, _pm)[1]))
    _pstart = _date(_py, _pm, min(_s.day, _cal.monthrange(_py, _pm)[1]))
    page_mtd["gsc_prev_period"] = {"start": _pstart.isoformat(), "end": _pend.isoformat()}

    # Thêm source file
    source_files = page_mtd.get("source", {}).get("files", [])
    if source_filename not in source_files:
        source_files.append(source_filename)
        page_mtd["source"]["files"] = source_files
    page_mtd["source"]["exported_at"] = __import__("datetime").date.today().isoformat()

    # Cập nhật từng trang: Trang có GSC thì gán, không có thì BỎ HẲN trường GSC
    gsc_pages_count = 0
    gsc_clicks_sum = 0

    for p in page_mtd.get("pages", []):
        path = p.get("path")
        if path in gsc_pages_dict:
            g_data = gsc_pages_dict[path]
            p["clicks"] = g_data["clicks"]
            p["impressions"] = g_data["impressions"]
            p["position"] = round(g_data["weighted_pos"] / g_data["impressions"], 1) if g_data["impressions"] else None
            gsc_pages_count += 1
            gsc_clicks_sum += g_data["clicks"]
        else:
            # Bỏ hẳn theo SPEC bước 5
            for fld in ["clicks", "impressions", "position", "clicks_prev", "impressions_prev", "position_prev"]:
                p.pop(fld, None)

    # Cập nhật coverage
    page_mtd["coverage"]["gsc_pages"] = gsc_pages_count
    page_mtd["coverage"]["gsc_clicks"] = gsc_clicks_sum

    # Kiểm tra an toàn checks (ngưỡng 1%)
    checks = page_mtd.get("checks", {})
    ga4_pv = checks.get("ga4_pv", 0)
    sum_pv = checks.get("sum_pv", 0)
    ga4_pv_prev = checks.get("ga4_pv_prev", 0)
    sum_pv_prev = checks.get("sum_pv_prev", 0)

    diff_pv = abs(sum_pv - ga4_pv) / ga4_pv * 100 if ga4_pv else 0
    diff_pv_prev = abs(sum_pv_prev - ga4_pv_prev) / ga4_pv_prev * 100 if ga4_pv_prev else 0

    if diff_pv > 1.0 or diff_pv_prev > 1.0:
        print(f"❌ Lệch quá 1%: ga4_pv={ga4_pv}, sum_pv={sum_pv} ({diff_pv:.2f}%), ga4_pv_prev={ga4_pv_prev}, sum_pv_prev={sum_pv_prev} ({diff_pv_prev:.2f}%)")
        sys.exit(1)

    # Ghi file KB
    with open(PAGE_MTD_KB, "w", encoding="utf-8") as f:
        json.dump(page_mtd, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã cập nhật KB page_mtd.json: {PAGE_MTD_KB}")

    # Đồng bộ Hub Dashboard
    if PAGE_MTD_HUB.parent.exists():
        with open(PAGE_MTD_HUB, "w", encoding="utf-8") as f:
            json.dump(page_mtd, f, ensure_ascii=False, indent=2)
        print(f"✅ Đã đồng bộ sang Hub Dashboard: {PAGE_MTD_HUB}")

        # Commit và Push sang Git remote của Hubs (chi khi co --push-hubs)
        if push_hubs:
            hub_repo = PAGE_MTD_HUB.parents[2]
            commit_files = ["data/analytics/page_mtd.json"]
            commit_msg = f"data(gsc): update MTD page metrics ({start_date} to {end_date}) into Hubs dashboard"
            try:
                import subprocess
                subprocess.run(["git", "-C", str(hub_repo), "add"] + commit_files, check=True)
                diff_chk = subprocess.run(["git", "-C", str(hub_repo), "diff", "--cached", "--quiet"])
                if diff_chk.returncode != 0:
                    subprocess.run(["git", "-C", str(hub_repo), "commit", "-m", commit_msg], check=True)
                    push_res = subprocess.run(["git", "-C", str(hub_repo), "push", "origin", "main"], capture_output=True, text=True)
                    if push_res.returncode == 0:
                        print(f"  ✓ Đã commit và push page_mtd.json sang GitHub vanhien26/hubs-momo:main")
                    else:
                        print(f"  ⚠ Lưu ý push GitHub: {push_res.stderr.strip()}")
                else:
                    print("  ✓ Dữ liệu page_mtd.json trên Hubs repo đã ở trạng thái mới nhất, không có commit mới.")
            except Exception as ge:
                print(f"  ⚠ Lỗi commit/push Hubs: {ge}")
        else:
            print("  ℹ Bỏ qua git commit/push Hubs (dùng --push-hubs để bật). File page_mtd.json đã ghi local.")

    print("\n==================================================")
    print(f"HOÀN THÀNH INGEST GSC MTD:")
    print(f"  - Date range: {start_date} đến {end_date}")
    print(f"  - Total Clicks: {total_clicks:,}")
    print(f"  - Total Impressions: {total_impressions:,}")
    print(f"  - Avg CTR: {avg_ctr:.2f}% | Avg Pos: {avg_pos:.2f}")
    print(f"  - Top Pages GSC Clicks: {gsc_clicks_sum:,} trên {gsc_pages_count} trang")
    print("==================================================")

GSC_SHEET_URL = "https://docs.google.com/spreadsheets/d/18yAcvhcA6YEx1TiqF5KsH40LmJBlkqN-wwvUUI5ajOA/edit"

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Ingest GSC MTD từ manual export hoặc Google Sheet")
    ap.add_argument("target", nargs="?", default=GSC_SHEET_URL,
                    help="ZIP export GSC, thư mục CSV, hoặc Google Sheet URL/ID (mặc định: sheet GSC-MTD)")
    ap.add_argument("--start", help="Override start date YYYY-MM-DD (khi thiếu Chart.csv)")
    ap.add_argument("--end", help="Override end date YYYY-MM-DD")
    ap.add_argument("--push-hubs", action="store_true", help="Commit + push page_mtd.json sang repo Hubs (mặc định KHÔNG push)")
    args = ap.parse_args()

    if args.target.startswith("http://") or args.target.startswith("https://"):
        export_date = __import__("datetime").date.today().isoformat()
        export_dir = GSC_EXPORTS_DIR / export_date
        export_dir.mkdir(parents=True, exist_ok=True)
        dest_csv = export_dir / "Pages_full_20k.csv"
        download_sheet_csv(args.target, dest_csv)
        ingest_gsc(export_dir, start_override=args.start, end_override=args.end, push_hubs=args.push_hubs)
    else:
        ingest_gsc(args.target, start_override=args.start, end_override=args.end, push_hubs=args.push_hubs)
