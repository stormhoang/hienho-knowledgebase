#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CRON SCRIPT: THEME SEASONALITY INTELLIGENCE (5-YEAR GOOGLE TRENDS)
Contract SSOT: lib/content-plan/seasonality.ts (hubs-momo)
Target Output: 07_REPORTS/data/theme_seasonality.json

Quy tắc contract cốt lõi:
1. Timeframe 5 năm ('today 5-y') để bóc tách tính mùa vụ định kỳ lặp lại hàng năm,
   loại bỏ nhiễu ngẫu nhiên của dữ liệu 1 năm (12 tháng).
2. monthly gồm đúng 12 số nguyên, theo thứ tự từ T1 đến T12, chuẩn hoá max = 100.
3. 1 keyword/payload (tránh hiện tượng chuẩn hóa chéo làm méo dạng mùa vụ của keyword yếu).
4. theme_id trùng khớp chính xác id trong file cluster.
5. Tích hợp cơ chế Resume (bỏ qua theme đã crawl thành công) và Exponential Backoff khi gặp HTTP 429.
"""

import os
import sys
import json
import glob
import time
import random
import argparse
from datetime import datetime
import warnings

# Tắt warning phân tách dataframe không cần thiết của pandas/pytrends
warnings.filterwarnings("ignore")

try:
    from pytrends.request import TrendReq
except ImportError:
    sys.exit("❌ Thiếu thư viện pytrends. Vui lòng cài đặt: pip install pytrends")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEFAULT_OUTPUT = os.path.join(BASE_DIR, "07_REPORTS", "data", "theme_seasonality.json")
DEFAULT_HUBS_REPO = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo"
DEFAULT_CLUSTER_DIR = os.path.join(DEFAULT_HUBS_REPO, "data", "seo-clusters")
FALLBACK_INVENTORY_SUMMARY = os.path.join(BASE_DIR, "07_REPORTS", "data", "inventory_clusters_summary.json")
DEFAULT_INVENTORY_DIR = os.path.join(BASE_DIR, "05_HUBS", "inventory")

# Chuẩn hoá pillar & metadata cho các Theme trong inventory CSV
PILLAR_OVERRIDES = {
    "xskt": ("xskt", "Xổ Số Kiến Thiết", "Lottery"),
    "sim-so-dep": ("sim số đẹp", "Sim Số Đẹp", "telco"),
    "nap-the-game": ("nạp thẻ game", "Nạp Thẻ Game", "Entertainment"),
    "nap-xu-tiktok": ("nạp xu tiktok", "Nạp Xu TikTok", "Entertainment"),
    "cuu-ho-o-to": ("cứu hộ ô tô", "Cứu Hộ Ô Tô", "vehicle-hub"),
    "uob": ("ngân hàng uob", "Ngân Hàng UOB", "Financial"),
    "mang-5g": ("mạng 5g", "Mạng 5G", "telco"),
    "nap-card": ("nạp thẻ cào", "Nạp Thẻ Cào", "telco"),
    "mang-4g": ("mạng 4g", "Mạng 4G", "telco"),
    "bao-hiem-benh": ("bảo hiểm bệnh hiểm nghèo", "Bảo Hiểm Bệnh Hiểm Nghèo", "insurtech"),
    "bao-hiem-than-vo": ("bảo hiểm thân vỏ ô tô", "Bảo Hiểm Thân Vỏ Ô Tô", "insurtech"),
    "bao-hiem-vat-chat": ("bảo hiểm vật chất xe ô tô", "Bảo Hiểm Vật Chất Ô Tô", "insurtech"),
    "dong-bao-hiem": ("đóng bảo hiểm xã hội", "Đóng Bảo Hiểm Xã Hội", "insurtech"),
    "thu-nhap": ("thuế thu nhập cá nhân", "Thu Nhập & Thuế TNCN", "Financial"),
    "ncb": ("ngân hàng ncb", "Ngân Hàng NCB", "Financial"),
    "bao-hiem": ("bảo hiểm", "Bảo Hiểm", "insurtech"),
    "bao-hiem-xe": ("bảo hiểm xe", "Bảo Hiểm Xe", "insurtech"),
    "bao-hiem-y-te": ("bảo hiểm y tế", "Bảo Hiểm Y Tế", "insurtech"),
    "bien-so": ("biển số xe", "Biển Số Xe", "vehicle-hub"),
    "garage-o-to": ("garage ô tô", "Garage Ô Tô", "vehicle-hub"),
    "no": ("nợ", "Nợ & Quản Lý Dư Nợ", "Financial"),
    "tiet-kiem": ("tiết kiệm", "Tiết Kiệm", "Financial"),
    "tinh-bmi": ("tính bmi", "Tính BMI", "hospital"),
    "vang": ("giá vàng", "Giá Vàng", "Financial"),
    "vcb": ("vcb", "VCB", "Financial"),
    "viet-bank": ("vietbank", "VietBank", "Financial"),
    "viettinbank": ("viettinbank", "VietinBank", "Financial"),
}


def parse_args():
    parser = argparse.ArgumentParser(description="Cron Theme Seasonality (5-year Google Trends)")
    parser.add_argument("--cluster-dir", default=DEFAULT_CLUSTER_DIR, help="Đường dẫn thư mục cluster json")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Đường dẫn file json xuất ra")
    parser.add_argument("--sector", default=None, help="Lọc theo Sector (vd: Financial, Lottery, vehicle-hub, insurtech...)")
    parser.add_argument("--themes", default=None, help="Danh sách theme_id cần chạy (cách nhau bởi dấu phẩy)")
    parser.add_argument("--limit", type=int, default=None, help="Giới hạn số lượng theme cần crawl")
    parser.add_argument("--delay-min", type=float, default=4.0, help="Thời gian chờ tối thiểu giữa các requests (giây)")
    parser.add_argument("--delay-max", type=float, default=8.0, help="Thời gian chờ tối đa giữa các requests (giây)")
    parser.add_argument("--force", action="store_true", help="Ghi đè, không dùng cache resume")
    parser.add_argument("--dry-run", action="store_true", help="Chỉ hiển thị danh sách theme, không gọi Google Trends")
    return parser.parse_args()


def load_theme_candidates(cluster_dir: str, sector_filter=None, theme_filter=None, inventory_dir: str = DEFAULT_INVENTORY_DIR):
    """
    Thu thập danh sách themes từ thư mục seo-clusters, fallback inventory_clusters_summary.json,
    và kho CSV inventory tại 05_HUBS/inventory.
    """
    themes = []
    seen_ids = set()

    def normalize_sector(s: str) -> str:
        s_clean = s.strip()
        if s_clean.upper() == "PS":
            return "Entertainment"
        return s_clean

    # Cách 1: Quét file json modular tại cluster_dir/*/*.json
    pattern = os.path.join(cluster_dir, "*", "*.json")
    files = glob.glob(pattern)

    if files:
        for p in sorted(files):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    t = json.load(f)
                theme_id = t.get("id")
                if not theme_id or theme_id in seen_ids:
                    continue

                sector = normalize_sector(t.get("sector", ""))
                if sector_filter and sector.lower() != sector_filter.lower():
                    continue

                if theme_filter and theme_id.lower() not in theme_filter:
                    continue

                pillar_kw = t.get("pillar_keyword", {}).get("keyword", "")
                # Cho phép override pillar nếu có trong PILLAR_OVERRIDES (vd: sửa ncb)
                if theme_id in PILLAR_OVERRIDES:
                    pillar_kw = PILLAR_OVERRIDES[theme_id][0]

                if not pillar_kw:
                    continue

                themes.append({
                    "theme_id": theme_id,
                    "name": t.get("name", theme_id),
                    "sector": sector,
                    "pillar": pillar_kw.strip(),
                    "volume": int(t.get("total_volume", 0)),
                })
                seen_ids.add(theme_id)
            except Exception as e:
                print(f"⚠️ Không thể đọc file cluster {p}: {e}")

    # Cách 2: Bổ sung từ fallback inventory summary nếu có
    if os.path.exists(FALLBACK_INVENTORY_SUMMARY):
        try:
            with open(FALLBACK_INVENTORY_SUMMARY, "r", encoding="utf-8") as f:
                data = json.load(f)
            for t in data.get("usecases", []):
                theme_id = t.get("id")
                if not theme_id or theme_id in seen_ids:
                    continue

                sector = normalize_sector(t.get("sector", ""))
                if sector_filter and sector.lower() != sector_filter.lower():
                    continue

                if theme_filter and theme_id.lower() not in theme_filter:
                    continue

                pillar_kw = t.get("pillar_keyword", {}).get("keyword", "")
                if theme_id in PILLAR_OVERRIDES:
                    pillar_kw = PILLAR_OVERRIDES[theme_id][0]

                if not pillar_kw:
                    continue

                themes.append({
                    "theme_id": theme_id,
                    "name": t.get("name", theme_id),
                    "sector": sector,
                    "pillar": pillar_kw.strip(),
                    "volume": int(t.get("total_volume", 0)),
                })
                seen_ids.add(theme_id)
        except Exception as e:
            print(f"⚠️ Lỗi đọc fallback inventory summary: {e}")

    # Cách 3: Bổ sung các Theme từ kho CSV 05_HUBS/inventory/*/*.csv
    if os.path.exists(inventory_dir):
        csv_files = glob.glob(os.path.join(inventory_dir, "*", "*.csv"))
        for cp in sorted(csv_files):
            fname = os.path.basename(cp).replace(".csv", "").strip()
            theme_id = fname
            if theme_id in seen_ids:
                continue

            folder_sector = normalize_sector(cp.split(os.sep)[-2])
            
            # Kiểm tra nếu có trong PILLAR_OVERRIDES
            if theme_id in PILLAR_OVERRIDES:
                override_pillar, override_name, override_sec = PILLAR_OVERRIDES[theme_id]
                sec = normalize_sector(override_sec or folder_sector)
                if sector_filter and sec.lower() != sector_filter.lower():
                    continue
                if theme_filter and theme_id.lower() not in theme_filter:
                    continue
                
                # Tính tổng volume từ CSV
                vol = 0
                try:
                    import csv
                    with open(cp, "r", encoding="utf-8-sig", errors="ignore") as f:
                        r = csv.reader(f)
                        next(r, None)
                        for row in r:
                            if len(row) > 1:
                                try:
                                    vol += int(float(row[1].replace(",", "").replace("=", "").replace("\"", "").strip()))
                                except:
                                    pass
                except:
                    pass

                themes.append({
                    "theme_id": theme_id,
                    "name": override_name,
                    "sector": sec,
                    "pillar": override_pillar,
                    "volume": vol,
                })
                seen_ids.add(theme_id)

    return themes


def fetch_seasonality_5y(py: TrendReq, pillar: str, max_retries: int = 3, initial_backoff: float = 30.0):
    """
    Truy vấn Google Trends 5 năm cho 1 keyword duy nhất.
    Tính trung bình interest theo từng tháng (T1..T12) và chuẩn hoá max = 100.
    """
    retries = 0
    backoff = initial_backoff

    while retries <= max_retries:
        try:
            # 1 keyword duy nhất/payload theo đúng contract
            py.build_payload([pillar], timeframe="today 5-y", geo="VN")
            df = py.interest_over_time()

            if df.empty or pillar not in df.columns or df[pillar].sum() == 0:
                return [0] * 12, True

            by_month = df[pillar].groupby(df.index.month).mean()
            mx = by_month.max()

            if mx <= 0:
                return [0] * 12, True

            monthly = [int(round(by_month.get(m, 0) / mx * 100)) for m in range(1, 13)]
            # Đảm bảo tháng cao nhất luôn là 100
            peak_val = max(monthly)
            if peak_val > 0 and peak_val != 100:
                monthly = [int(round(v / peak_val * 100)) for v in monthly]

            return monthly, False

        except Exception as e:
            err_msg = str(e)
            if "429" in err_msg or "TooManyRequests" in err_msg or "ResponseError" in err_msg:
                retries += 1
                if retries <= max_retries:
                    print(f"  ⚠️ HTTP 429 Rate Limit cho '{pillar}'. Backoff {backoff:.0f}s (Lần thử {retries}/{max_retries})...")
                    time.sleep(backoff)
                    backoff *= 2.0
                    continue
                else:
                    print(f"  ❌ Đạt giới hạn retry 429 cho '{pillar}'. Đánh dấu insufficient_data.")
                    return [0] * 12, True
            else:
                print(f"  ⚠️ Lỗi Pytrends với từ khóa '{pillar}': {err_msg}")
                return [0] * 12, True

    return [0] * 12, True


def save_dataset(output_path: str, themes_data: list):
    """
    Lưu dataset chuẩn contract sang output_path
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    clean_themes = []
    for t in themes_data:
        item = dict(t)
        sec = item.get("sector", "")
        if sec.upper() == "PS":
            item["sector"] = "Entertainment"
        clean_themes.append(item)

    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "geo": "VN",
        "timeframe": "today 5-y",
        "themes": clean_themes,
    }
    temp_path = output_path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    os.replace(temp_path, output_path)


def main():
    args = parse_args()
    print("=" * 65)
    print("🚀 BẮT ĐẦU CRON THEME SEASONALITY (5-YEAR GOOGLE TRENDS)")
    print("=" * 65)
    print(f"📁 Cluster dir : {args.cluster_dir}")
    print(f"📄 Output file : {args.output}")

    target_themes = [t.strip().lower() for t in args.themes.split(",")] if args.themes else None
    candidates = load_theme_candidates(args.cluster_dir, args.sector, target_themes)

    if not candidates:
        print("❌ Không tìm thấy theme nào phù hợp điều kiện lọc.")
        sys.exit(1)

    # Sắp xếp theo volume giảm dần để ưu tiên các themes lớn trước
    candidates.sort(key=lambda x: x["volume"], reverse=True)
    if args.limit:
        candidates = candidates[:args.limit]

    print(f"📊 Tổng số themes được chọn: {len(candidates)}")

    if args.dry_run:
        print("🔍 [DRY RUN] Danh sách themes sẽ xử lý:")
        for idx, c in enumerate(candidates, 1):
            print(f"  {idx:3d}. [{c['sector']:12s}] {c['theme_id']:25s} -> '{c['pillar']}' (Vol: {c['volume']:,})")
        return

    # Tải cache resume từ file output hiện tại nếu có
    existing_map = {}
    if os.path.exists(args.output) and not args.force:
        try:
            with open(args.output, "r", encoding="utf-8") as f:
                old_data = json.load(f)
            for item in old_data.get("themes", []):
                t_id = item.get("theme_id")
                m = item.get("monthly", [])
                # Coi là hợp lệ nếu có đúng 12 tháng và có dữ liệu (không phải [0]*12 trừ khi insufficient_data)
                if t_id and len(m) == 12:
                    existing_map[t_id] = item
            print(f"🔄 Tìm thấy cache resume: {len(existing_map)} themes đã có sẵn dữ liệu.")
        except Exception as e:
            print(f"⚠️ Không đọc được cache resume từ {args.output}: {e}")

    # Khởi tạo TrendReq
    print("🌐 Khởi tạo kết nối Google Trends (hl=vi-VN, tz=-420)...")
    py = TrendReq(hl="vi-VN", tz=-420, timeout=(10, 25))

    # Lưu trữ toàn bộ kết quả theo cơ chế Upsert (bảo toàn các theme đã chạy trước đó)
    current_themes_map = dict(existing_map)
    fetched_count = 0
    skipped_count = 0

    for idx, c in enumerate(candidates, 1):
        t_id = c["theme_id"]
        pillar = c["pillar"]

        # Kiểm tra Resume (chỉ bỏ qua nếu đã có cache hợp lệ và cùng pillar keyword)
        cached = existing_map.get(t_id)
        if not args.force and cached and not cached.get("insufficient_data", False) and cached.get("pillar") == pillar:
            skipped_count += 1
            current_themes_map[t_id] = cached
            print(f"[{idx}/{len(candidates)}] ⏭️ Bỏ qua (đã có cache): {t_id} (Peak T{cached['monthly'].index(max(cached['monthly'])) + 1})")
            continue

        print(f"[{idx}/{len(candidates)}] ⏳ Đang kéo 5-y Trends: {t_id} (Pillar: '{pillar}')...", end="", flush=True)

        monthly, insufficient = fetch_seasonality_5y(py, pillar)
        peak_str = f"Peak T{monthly.index(max(monthly)) + 1}" if not insufficient else "Không đủ data"
        print(f" ✅ {peak_str} -> {monthly}")

        theme_record = {
            "theme_id": t_id,
            "name": c["name"],
            "sector": c["sector"],
            "pillar": pillar,
            "volume": c["volume"],
            "monthly": monthly,
            "insufficient_data": insufficient,
        }
        current_themes_map[t_id] = theme_record
        fetched_count += 1

        # Lưu lũy kế toàn bộ dataset sau mỗi theme (upsert an toàn)
        save_dataset(args.output, list(current_themes_map.values()))

        # Nghỉ ngơi có jitter để tránh bị Google chặn IP (429)
        sleep_sec = random.uniform(args.delay_min, args.delay_max)
        time.sleep(sleep_sec)

    # Đảm bảo lưu bản ghi hoàn tất cuối cùng
    final_list = list(current_themes_map.values())
    save_dataset(args.output, final_list)

    print("\n" + "=" * 65)
    print("🎉 HOÀN TẤT CRON THEME SEASONALITY!")
    print(f"📊 Tổng themes trong file : {len(final_list)}")
    print(f"⚡ Mới truy vấn Google   : {fetched_count}")
    print(f"⏭️ Tái sử dụng từ cache  : {skipped_count}")
    print(f"💾 File kết quả đã ghi     : {args.output}")
    print("=" * 65)


if __name__ == "__main__":
    main()
