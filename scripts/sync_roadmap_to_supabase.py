#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[DEPRECATED / ARCHIVED] SYNC ROADMAP & SHIP RELEASES TO SUPABASE
LƯU Ý: Luồng /roadmap và /board bên Web Hubs (react-web-momo) đã bị xóa hoàn toàn.
Script này được giữ lại chỉ phục vụ tham khảo lịch sử, không đẩy sang Hubs nữa.
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SSOT_FILE = os.path.join(BASE_DIR, "14_ROADMAP", "ship_releases.json")
HUBS_LOCAL_JSON = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/roadmap.json"
HUBS_ENV_FILE = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/.env.local"
LOCAL_ENV_FILE = os.path.join(BASE_DIR, ".env")

VALID_STATUSES = {"planned", "in_progress", "launched", "delayed"}

def load_env_variables():
    """Đọc URL và Service Role Key từ .env cục bộ hoặc .env.local của Hubs."""
    env_vars = {}
    for path in [LOCAL_ENV_FILE, HUBS_ENV_FILE]:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        clean_k = k.strip()
                        clean_v = v.strip().strip('"').strip("'")
                        if clean_k not in env_vars:
                            env_vars[clean_k] = clean_v

    supabase_url = env_vars.get("NEXT_PUBLIC_SUPABASE_URL") or os.environ.get("NEXT_PUBLIC_SUPABASE_URL")
    service_key = (
        env_vars.get("SUPABASE_SERVICE_ROLE_KEY")
        or env_vars.get("NEXT_PUBLIC_SUPABASE_ANON_KEY")
        or os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    )
    return supabase_url, service_key

def validate_releases(items):
    """Kiểm tra tính hợp lệ của dữ liệu release."""
    errors = []
    seen_ids = set()
    for idx, item in enumerate(items, 1):
        rel_id = item.get("id")
        if not rel_id:
            errors.append(f"Mục #{idx}: Thiếu trường 'id'")
        elif rel_id in seen_ids:
            errors.append(f"Mục #{idx}: Trùng lặp id '{rel_id}'")
        else:
            seen_ids.add(rel_id)

        # Validate ngày làm việc (chỉ Thứ 2 đến Thứ 6)
        date_str = item.get("date")
        if not date_str:
            errors.append(f"Release '{rel_id}': Thiếu trường 'date'")
        else:
            try:
                dt = datetime.strptime(date_str, "%Y-%m-%d")
                if dt.weekday() >= 5:
                    day_vn = "Thứ 7" if dt.weekday() == 5 else "Chủ Nhật"
                    errors.append(
                        f"Release '{rel_id}': Ngày '{date_str}' rơi vào {day_vn}. "
                        "Lịch ship chỉ được xếp vào ngày làm việc (Thứ 2 đến Thứ 6)."
                    )
            except ValueError:
                errors.append(f"Release '{rel_id}': Định dạng date '{date_str}' không hợp lệ (chuẩn YYYY-MM-DD)")

        # Validate trạng thái
        status = item.get("status")
        if status not in VALID_STATUSES:
            errors.append(f"Release '{rel_id}': Trạng thái '{status}' không hợp lệ ({', '.join(VALID_STATUSES)})")

        if not item.get("name"):
            errors.append(f"Release '{rel_id}': Thiếu trường 'name'")
        if not item.get("tag"):
            errors.append(f"Release '{rel_id}': Thiếu trường 'tag' (Hub name)")

    return errors

def sync_to_supabase(url, key, items):
    """Upsert danh sách releases lên Supabase qua PostgREST API."""
    endpoint = f"{url.rstrip('/')}/rest/v1/ship_releases"
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "resolution=merge-duplicates,return=representation"
    }

    payload = json.dumps(items).encode("utf-8")
    req = urllib.request.Request(endpoint, data=payload, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return True, len(data), "Thành công"
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        return False, 0, f"HTTP {e.code}: {err_msg}"
    except Exception as e:
        return False, 0, str(e)

def sync_to_fallback_json(items):
    """Đồng bộ bản sao sạch sang data/roadmap.json của react-web-momo để làm fallback an toàn."""
    if os.path.exists(os.path.dirname(HUBS_LOCAL_JSON)):
        # Chuẩn hóa để tương thích giao diện cũ nếu cần
        fallback_data = []
        for it in items:
            fallback_data.append({
                "id": it.get("id"),
                "date": it.get("date"),
                "name": it.get("name"),
                "description": it.get("description", ""),
                "status": it.get("status", "planned"),
                "tag": it.get("tag", "Platform"),
                "theme": it.get("theme", ""),
                "scope": it.get("scope", []),
                "owner_team": it.get("owner_team", "Web Dev"),
                "doc_url": it.get("doc_url", ""),
                "live_url": it.get("live_url", "")
            })
        with open(HUBS_LOCAL_JSON, "w", encoding="utf-8") as f:
            json.dump(fallback_data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Đồng bộ lịch ship sản phẩm từ Hienho_MoMo-Base lên Supabase")
    parser.add_argument("--dry-run", action="store_true", help="Kiểm tra tính hợp lệ dữ liệu mà không đẩy lên DB")
    args = parser.parse_args()

    print("\n--- BẮT ĐẦU ĐỒNG BỘ SHIP RELEASES ROADMAP ---")
    if not os.path.exists(SSOT_FILE):
        print(f"Lỗi: Không tìm thấy file SSOT tại: {SSOT_FILE}")
        sys.exit(1)

    with open(SSOT_FILE, "r", encoding="utf-8") as f:
        try:
            items = json.load(f)
        except Exception as e:
            print(f"Lỗi cú pháp JSON trong file SSOT: {e}")
            sys.exit(1)

    # 1. Kiểm tra tính hợp lệ
    errors = validate_releases(items)
    if errors:
        print(f"\nPhát hiện {len(errors)} lỗi dữ liệu:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print(f"Kiểm tra thành công: {len(items)} hạng mục ship hợp lệ.")

    # Thống kê nhanh theo trạng thái
    status_counts = {}
    for it in items:
        status_counts[it["status"]] = status_counts.get(it["status"], 0) + 1

    print("\nPhân bổ theo trạng thái:")
    for st, count in status_counts.items():
        print(f"  - {st:<12}: {count:>2} sản phẩm")

    if args.dry_run:
        print("\nChế độ [dry-run]: Hoàn thành kiểm tra cú pháp và logic, không ghi vào database.")
        sys.exit(0)

    # 2. Đồng bộ bản sao sang repo Hubs (High Availability fallback)
    fallback_ok = sync_to_fallback_json(items)
    if fallback_ok:
        print(f"\nĐã đồng bộ bản sao fallback sang: {HUBS_LOCAL_JSON}")

    # 3. Đẩy lên Supabase
    supabase_url, service_key = load_env_variables()
    if not supabase_url or not service_key:
        print("\nCảnh báo: Thiếu thông tin kết nối Supabase (NEXT_PUBLIC_SUPABASE_URL hoặc SUPABASE_SERVICE_ROLE_KEY).")
        print("Dữ liệu chỉ được cập nhật vào file fallback JSON cục bộ.")
        sys.exit(1)

    print(f"\nKết nối Supabase: {supabase_url}")
    success, count, msg = sync_to_supabase(supabase_url, service_key, items)

    if success:
        print(f"Đã đồng bộ thành công {count} releases lên Supabase table 'ship_releases'.")
        print("Calendar tại Web Hubs (/roadmap) sẽ tự động hiển thị dữ liệu mới nhất.")
    else:
        print(f"\nChưa thể ghi vào Supabase: {msg}")
        if "PGRST205" in msg or "Could not find the table" in msg:
            print("Gợi ý: Bảng 'ship_releases' chưa được tạo trên Supabase.")
            print("Vui lòng thực thi file SQL tại: react-web-momo/supabase/create-ship-releases.sql")
        sys.exit(1)

if __name__ == "__main__":
    sys.path.insert(0, BASE_DIR)
    from scripts.lib.hub_sync_lock import hub_sync_lock
    with hub_sync_lock("sync_roadmap_to_supabase"):
        main()
