#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INGEST GA4 DAILY EXPORT (OFFLINE RAW DATA PIPELINE)
Quy trình nạp dữ liệu thô hàng ngày từ file CSV xuất từ GA4 Explore.
Thay thế hoàn toàn luồng gọi API GA4 tự động.

Quy trình:
1. Đọc tệp CSV xuất từ GA4 Explore (mặc định tìm trong ~/Downloads/).
2. Trích xuất ngày ghi nhận (VD: 20261119 -> ngày 19).
3. Lưu trữ bản sao dữ liệu thô vào 07_REPORTS/data/ga4_daily/YYYY-MM-DD.csv.
4. Bóc tách 6 Kênh lưu lượng và 6 Hubs nội dung.
5. Cộng dồn phát sinh ngày mới vào mốc MTD ngày hôm trước.
6. Cập nhật đồng loạt:
   - Snapshot MTD JSON: 07_REPORTS/data/monthly_{month}_mtd_{day}d.json
   - summary.json & PERFORMANCE_SNAPSHOT_LATEST.md
   - Local Excel SSOT: web_performance_tracking.xlsx & web_platform_performance.xlsx
   - Hub Dashboard: react-web-momo/lib/dashboard/web-data.json
"""

import os
import sys
import csv
import json
import shutil
import re
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.lib.theme_matcher import build_theme_matcher
from scripts.lib.excel_patcher import patch_excel_dynamic

DAILY_DIR = BASE_DIR / "07_REPORTS" / "data" / "ga4_daily"
SNAPSHOT_DIR = BASE_DIR / "07_REPORTS" / "data"
SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
DAILY_DIR.mkdir(parents=True, exist_ok=True)

TARGET_MONTHLY_PV = 3829155
HUB_TARGETS_NOV = {
    "cinema": 1294630,
    "financial": 700000,
    "new_user": 300000,
    "vehicle": 100000,
    "insurance": 50000,
    "student": None
}

def find_latest_ga4_export(download_dir=None):
    if download_dir is None:
        download_dir = Path.home() / "Downloads"
    else:
        download_dir = Path(download_dir)

    candidates = []
    for f in download_dir.glob("*.csv"):
        try:
            with open(f, "r", encoding="utf-8", errors="ignore") as fp:
                first_lines = "".join(fp.readline() for _ in range(8))
                if "MoMo.vn" in first_lines or "Hostname" in first_lines:
                    candidates.append((f.stat().st_mtime, f))
        except Exception:
            continue

    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]

def parse_ga4_daily_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    date_str = None
    for line in lines[:10]:
        m = re.search(r"(\d{8})-(\d{8})", line)
        if m:
            date_str = m.group(1) # YYYYMMDD
            break

    if not date_str:
        # Fallback to file creation date
        date_str = datetime.now().strftime("%Y%m%d")

    year = int(date_str[:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])
    iso_date = f"{year}-{month:02d}-{day:02d}"
    month_str = f"{year}-{month:02d}"

    header_idx = -1
    for i, line in enumerate(lines[:20]):
        if "Hostname" in line and "Page path" in line:
            header_idx = i
            break

    if header_idx == -1:
        raise ValueError(f"Không tìm thấy dòng tiêu đề chuẩn (Hostname, Page path...) trong {file_path}")

    raw_header_cols = next(csv.reader([lines[header_idx]]))
    header_lower = [c.strip().lower() for c in raw_header_cols]

    host_col = next((i for i, c in enumerate(header_lower) if "hostname" in c), -1)
    event_col = next((i for i, c in enumerate(header_lower) if "event" in c), -1)
    lp_col = next((i for i, c in enumerate(header_lower) if "page path" in c), -1)
    ch_col = next((i for i, c in enumerate(header_lower) if "channel" in c), -1)
    pv_col = next((i for i, c in enumerate(header_lower) if "view" in c), -1)

    if lp_col == -1 or pv_col == -1:
        raise ValueError(f"Không xác định được cột Page path hoặc Views trong tiêu đề: {raw_header_cols}")

    min_required_len = max(host_col if host_col >= 0 else 0, lp_col, pv_col, ch_col if ch_col >= 0 else 0) + 1

    reader = csv.reader(lines[header_idx+1:])
    matcher = build_theme_matcher()

    daily_pv = 0
    channels_pv = {
        "organic": 0,
        "direct": 0,
        "paid": 0,
        "referral": 0,
        "ai_traffic": 0,
        "others": 0
    }
    hubs_pv = {
        "cinema": 0,
        "financial": 0,
        "new_user": 0,
        "vehicle": 0,
        "insurance": 0,
        "student": 0,
        "others": 0
    }
    cinema_sub = {
        "Trang Rạp phim": 0,
        "Trang phim chi tiết": 0,
        "Cinema_Home Page": 0,
        "Cinema_Blog": 0,
        "Cinema_Landing Page": 0,
        "Tin tức": 0,
        "Others": 0
    }
    page_views = {}

    for r in reader:
        if not r or any("Grand total" in str(x) for x in r):
            continue
        if len(r) >= min_required_len:
            host = r[host_col].strip() if host_col >= 0 else "www.momo.vn"
            if host != "www.momo.vn":
                continue
            event = r[event_col].strip() if event_col >= 0 else "page_view"
            lp = r[lp_col].strip() if lp_col >= 0 else ""
            ch = r[ch_col].strip() if ch_col >= 0 else ""
            try:
                pv = int(r[pv_col].strip().replace(",", ""))
            except Exception:
                pv = 0

            daily_pv += pv
            page_views[lp] = page_views.get(lp, 0) + pv

            # Channel categorization
            ch_lower = ch.lower()
            if "ai referrals" in ch_lower or ch_lower == "ai assistant":
                channels_pv["ai_traffic"] += pv
            elif "organic search" in ch_lower:
                channels_pv["organic"] += pv
            elif "direct" in ch_lower:
                channels_pv["direct"] += pv
            elif any(k in ch_lower for k in ["paid", "cpc", "cross-network", "display"]):
                channels_pv["paid"] += pv
            elif any(k in ch_lower for k in ["referral", "app referral"]):
                channels_pv["referral"] += pv
            else:
                channels_pv["others"] += pv

            # Hub categorization
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
            elif h_name in ["New User"] or (sec == "Brand" and ("/tai-app" in lp or "/chao-ban-moi" in lp)):
                hubs_pv["new_user"] += pv
            elif h_name in ["Phạt Nguội", "Tiện Ích Giao Thông", "Phí Không Dừng", "Bảo Hiểm Ô Tô", "Bảo Hiểm Xe Máy", "Giá xăng", "Cây xăng", "Trạm sạc"] or sec == "vehicle-hub" or ("ô tô" in h_name.lower() or "xe máy" in h_name.lower()):
                hubs_pv["vehicle"] += pv
            elif h_name in ["Bảo Hiểm", "Bảo Hiểm Y Tế", "Bảo Hiểm Sức Khỏe", "Bảo Hiểm Xã Hội"] or sec == "insurtech" or "bảo hiểm" in h_name.lower():
                hubs_pv["insurance"] += pv
            elif h_name in ["Student Hub", "Student Pass"] or sec == "student":
                hubs_pv["student"] += pv
            else:
                hubs_pv["others"] += pv

    return {
        "date": iso_date,
        "year": year,
        "month": month,
        "day": day,
        "month_str": month_str,
        "daily_pv": daily_pv,
        "channels_pv": channels_pv,
        "hubs_pv": hubs_pv,
        "cinema_sub": cinema_sub,
        "page_views": page_views
    }

def ingest_daily_report(csv_path=None, dry_run=False):
    if csv_path is None:
        csv_path = find_latest_ga4_export()
        if not csv_path:
            raise FileNotFoundError("Không tìm thấy tệp CSV xuất từ GA4 trong ~/Downloads/. Vui lòng chỉ định đường dẫn qua --file.")

    csv_path = Path(csv_path)
    print("=" * 75)
    print(f"KHỞI CHẠY QUY TRÌNH NẠP DỮ LIỆU GA4 THÔ HÀNG NGÀY (OFFLINE INGESTION)")
    print(f"Tệp nguồn: {csv_path}")
    print("=" * 75)

    data = parse_ga4_daily_csv(csv_path)
    day = data["day"]
    month_str = data["month_str"]
    daily_pv = data["daily_pv"]
    iso_date = data["date"]

    print(f"[1/5] Đã bóc tách dữ liệu ngày {iso_date}: {daily_pv:,} PV (www.momo.vn)")
    print(f"  - Non-Paid: {sum(data['channels_pv'][k] for k in ('organic', 'direct', 'referral', 'ai_traffic', 'others')):,} PV")
    print(f"  - Paid    : {data['channels_pv']['paid']:,} PV")

    # Lưu bản sao lưu trữ dữ liệu thô
    archive_path = DAILY_DIR / f"{iso_date}.csv"
    if not dry_run:
        shutil.copy2(csv_path, archive_path)
        print(f"  ✓ Đã lưu trữ bản sao dữ liệu thô: {archive_path}")

    # Tìm snapshot MTD của ngày hôm trước
    prior_day = day - 1
    prior_snapshot_file = SNAPSHOT_DIR / f"monthly_{data['month']:02d}_{data['year']}_mtd_{prior_day}d.json"
    
    if not prior_snapshot_file.exists():
        # Fallback: tìm snapshot mtd lớn nhất hiện có nhỏ hơn day
        candidates = sorted(SNAPSHOT_DIR.glob(f"monthly_{data['month']:02d}_{data['year']}_mtd_*d.json"))
        candidates = [c for c in candidates if int(re.search(r"mtd_(\d+)d", c.name).group(1)) < day]
        if candidates:
            prior_snapshot_file = candidates[-1]
            prior_day = int(re.search(r"mtd_(\d+)d", prior_snapshot_file.name).group(1))
        else:
            raise FileNotFoundError(f"Không tìm thấy snapshot MTD trước đó cho tháng {month_str}")

    print(f"[2/5] Nạp mốc MTD hôm trước từ {prior_snapshot_file.name} (MTD {prior_day}d)...")
    with open(prior_snapshot_file, "r", encoding="utf-8") as f:
        prior_data = json.load(f)

    prior_pv = prior_data["actual_mtd_pv"]
    accumulated_pv = prior_pv + daily_pv

    # Cộng dồn channels
    acc_channels = {}
    for ch_k in ["organic", "direct", "paid", "referral", "others", "ai_traffic"]:
        p_val = prior_data.get("channels", {}).get(ch_k, {}).get("pv", 0)
        d_val = data["channels_pv"].get(ch_k, 0)
        acc_channels[ch_k] = {
            "pv": p_val + d_val,
            "pct": round((p_val + d_val) / accumulated_pv * 100, 2)
        }
    non_paid_tot = acc_channels["organic"]["pv"] + acc_channels["direct"]["pv"] + acc_channels["referral"]["pv"] + acc_channels["ai_traffic"]["pv"] + acc_channels["others"]["pv"]
    acc_channels["non_paid_total"] = {
        "pv": non_paid_tot,
        "pct": round(non_paid_tot / accumulated_pv * 100, 2)
    }

    # Cộng dồn hubs
    acc_hubs = {}
    for h_id in ["cinema", "financial", "new_user", "vehicle", "insurance", "student"]:
        p_val = prior_data.get("hubs", {}).get(h_id, {}).get("pv", 0)
        d_val = data["hubs_pv"].get(h_id, 0)
        tot_h = p_val + d_val
        targ = HUB_TARGETS_NOV.get(h_id)
        acc_hubs[h_id] = {
            "pv": tot_h,
            "target": targ,
            "pct": round(tot_h / targ * 100, 2) if targ else None
        }

    # Cộng dồn cinema breakdown
    acc_cinema = {}
    for c_k in ["Trang Rạp phim", "Trang phim chi tiết", "Cinema_Home Page", "Cinema_Blog", "Cinema_Landing Page", "Tin tức", "Others"]:
        p_val = prior_data.get("cinema_breakdown", {}).get(c_k, 0)
        d_val = data["cinema_sub"].get(c_k, 0)
        acc_cinema[c_k] = p_val + d_val

    # Tính toán tiến độ tháng
    days_in_month = 30
    target_pv = TARGET_MONTHLY_PV
    progress_pct = round(accumulated_pv / target_pv * 100, 2)
    daily_pace = round(accumulated_pv / day, 2)
    daily_needed = round((target_pv - accumulated_pv) / max(1, days_in_month - day), 2)
    forecast_30d = round(daily_pace * days_in_month, 1)
    forecast_pct = round(forecast_30d / target_pv * 100, 2)

    new_snapshot = {
        "file_source": f"GA4 Daily Ingest (CSV: {csv_path.name})",
        "read_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "report_type": f"MTD {day} Ngày (01/{data['month']:02d} - {day:02d}/{data['month']:02d}/{data['year']})",
        "days_elapsed": day,
        "days_in_month": days_in_month,
        "target_pv": target_pv,
        "actual_mtd_pv": accumulated_pv,
        "progress_pct": progress_pct,
        "daily_pace": daily_pace,
        "daily_needed": daily_needed,
        "forecast_31d": forecast_30d,
        "forecast_pct": forecast_pct,
        "users": prior_data.get("users", 0),
        "sessions": prior_data.get("sessions", 0),
        "channels": acc_channels,
        "hubs": acc_hubs,
        "cinema_breakdown": acc_cinema
    }

    new_snapshot_file = SNAPSHOT_DIR / f"monthly_{data['month']:02d}_{data['year']}_mtd_{day}d.json"
    summary_file = SNAPSHOT_DIR / "summary.json"

    print(f"[3/5] Tính toán lũy kế MTD {day} ngày hoàn tất:")
    print(f"  - Mốc trước (MTD {prior_day}d) : {prior_pv:,} PV")
    print(f"  - Phát sinh ngày {day}        : +{daily_pv:,} PV")
    print(f"  => Lũy kế MTD {day}d mới       : {accumulated_pv:,} PV (Tiến độ {progress_pct}% target)")

    if not dry_run:
        with open(new_snapshot_file, "w", encoding="utf-8") as f:
            json.dump(new_snapshot, f, ensure_ascii=False, indent=2)
        print(f"  ✓ Đã ghi snapshot MTD: {new_snapshot_file.name}")

        # Cập nhật summary.json
        if summary_file.exists():
            with open(summary_file, "r", encoding="utf-8") as f:
                sum_data = json.load(f)
            sum_data["running"] = {
                "month": month_str,
                "daysElapsed": day,
                "daysInMonth": days_in_month,
                "report": new_snapshot_file.name,
                "pv": accumulated_pv,
                "target": target_pv,
                "dailyPace": round(daily_pace),
                "dailyNeeded": round(daily_needed),
                "forecast": round(forecast_30d),
                "forecastPct": forecast_pct
            }
            sum_data["hubs"] = [
                {"id": "cinema", "name": "Cinema Hub", "pv": acc_hubs["cinema"]["pv"]},
                {"id": "financial", "name": "Financial Hub", "pv": acc_hubs["financial"]["pv"]},
                {"id": "new_user", "name": "New User Hub", "pv": acc_hubs["new_user"]["pv"]},
                {"id": "vehicle", "name": "Vehicle Hub", "pv": acc_hubs["vehicle"]["pv"]},
                {"id": "insurance", "name": "Insurance Hub", "pv": acc_hubs["insurance"]["pv"]},
                {"id": "student", "name": "Student Hub", "pv": acc_hubs["student"]["pv"]}
            ]
            sum_data["channels"] = {
                "organic": acc_channels["organic"]["pv"],
                "direct": acc_channels["direct"]["pv"],
                "referral": acc_channels["referral"]["pv"],
                "paid": acc_channels["paid"]["pv"],
                "others": acc_channels["others"]["pv"]
            }
            with open(summary_file, "w", encoding="utf-8") as f:
                json.dump(sum_data, f, ensure_ascii=False, indent=2)
            print("  ✓ Đã cập nhật summary.json")

    # 4. Cập nhật Excel SSOT nội bộ
    print("[4/5] Cập nhật bảng tính Excel nội bộ (Offline)...")
    if not dry_run:
        hubs_pv_plain = {k: v["pv"] for k, v in acc_hubs.items()}
        for excel_file in ["web_performance_tracking.xlsx", "web_platform_performance.xlsx"]:
            fp = BASE_DIR / "07_REPORTS" / excel_file
            if fp.exists():
                try:
                    patch_excel_dynamic(
                        file_path=fp,
                        month_str=month_str,
                        target_pv=target_pv,
                        days_elapsed=day,
                        total_pv=accumulated_pv,
                        organic_pv=acc_channels["organic"]["pv"],
                        paid_pv=acc_channels["paid"]["pv"],
                        direct_pv=acc_channels["direct"]["pv"],
                        referral_pv=acc_channels["referral"]["pv"],
                        others_pv=acc_channels["others"]["pv"],
                        non_paid_pv=acc_channels["non_paid_total"]["pv"],
                        hubs_pv=hubs_pv_plain,
                        cinema_sub=acc_cinema
                    )
                except Exception as e:
                    print(f"  ⚠ Lưu ý patch {excel_file}: {e}")

    # 5. Dựng lại Hub Dashboard web-data.json
    print("[5/5] Cập nhật Hub Dashboard (react-web-momo/lib/dashboard/web-data.json)...")
    if not dry_run:
        try:
            sys.path.insert(0, str(BASE_DIR / "scripts" / "lib"))
            from hubs_dashboard import rebuild_dashboard
            rebuild_dashboard()
            # Đồng bộ trực tiếp summary.json sang cả 2 vị trí của repo Hubs
            hub_repo = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
            if hub_repo.exists():
                dst1 = hub_repo / "lib" / "dashboard" / "summary.json"
                dst2 = hub_repo / "data" / "analytics" / "summary.json"
                if dst1.parent.exists(): shutil.copy2(summary_file, dst1)
                if dst2.parent.exists(): shutil.copy2(summary_file, dst2)

                # Commit và Push sang Git remote của Hubs
                commit_files = ["data/analytics/summary.json", "lib/dashboard/summary.json", "lib/dashboard/web-data.json"]
                commit_msg = f"data(ga4): update MTD {day}d ({accumulated_pv:,} PV) from daily raw ingest"
                try:
                    import subprocess
                    subprocess.run(["git", "-C", str(hub_repo), "add"] + commit_files, check=True)
                    diff_chk = subprocess.run(["git", "-C", str(hub_repo), "diff", "--cached", "--quiet"])
                    if diff_chk.returncode != 0:
                        subprocess.run(["git", "-C", str(hub_repo), "commit", "-m", commit_msg], check=True)
                        push_res = subprocess.run(["git", "-C", str(hub_repo), "push", "origin", "main"], capture_output=True, text=True)
                        if push_res.returncode == 0:
                            print(f"  ✓ Đã commit và push trực tiếp sang GitHub vanhien26/hubs-momo:main")
                        else:
                            print(f"  ⚠ Lưu ý push GitHub: {push_res.stderr.strip()}")
                    else:
                        print("  ✓ Dữ liệu trên Hubs repo đã ở trạng thái mới nhất, không có commit mới.")
                except Exception as ge:
                    print(f"  ⚠ Lỗi commit/push Hubs: {ge}")
            print("  ✓ Đã làm mới web-data.json và summary.json cho Hubs Dashboard")
        except Exception as e:
            print(f"  ⚠ Lưu ý rebuild dashboard: {e}")

    print("=" * 75)
    print(f"HOÀN THÀNH NẠP DỮ LIỆU GA4 THÔ CHO NGÀY {iso_date}")
    print(f"- Lũy kế MTD {day} ngày : {accumulated_pv:,} PV (Đạt {progress_pct}% target)")
    print(f"- Nhịp vận hành ngày : {daily_pace:,.0f} PV/ngày | Dự báo 30d: {forecast_30d:,.0f} PV ({forecast_pct}%)")
    print(f"- Non-Paid           : {non_paid_tot:,} PV ({acc_channels['non_paid_total']['pct']}%) | Paid: {acc_channels['paid']['pv']:,} PV ({acc_channels['paid']['pct']}%)")
    print("=" * 75)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Ingest GA4 Daily CSV Export into MTD Pipeline")
    parser.add_argument("--file", type=str, default=None, help="Đường dẫn file CSV (mặc định tìm file mới nhất trong ~/Downloads/)")
    parser.add_argument("--dry-run", action="store_true", help="Chạy thử nghiệm không ghi file")
    args = parser.parse_args()

    ingest_daily_report(csv_path=args.file, dry_run=args.dry_run)
