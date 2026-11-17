#!/usr/bin/env python3
"""
Tự động tạo danh mục Ads Segment chuẩn hóa cho Ads Manager từ DIM_URL.

Quy tắc chuẩn hóa:
1. Gộp toàn bộ các phân hệ Cinema (Cinema_Home Page, Cinema_Page, Cinema_Blog,
   Cinema_Cineplex Page, Cinema_Landing Page, Cinema_News) thành 1 Segment duy nhất: 'Cinema'.
2. Loại bỏ các trang nội dung chung (Blog, Tin Tức, Hỏi đáp, Guide, TnC, Home MoMo)
   khỏi danh mục Segment, vì đây là Page Type (loại trang), không phải Segment dịch vụ.
3. Gom nhóm Segment theo Hub phân cấp để phục vụ UI dropdown trong Ads Manager.
"""

import json
import csv
import re
import unicodedata
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "07_REPORTS" / "data" / "web_dim_page_url.csv"
MAPPING_JSON = ROOT / "07_REPORTS" / "data" / "url_project_mapping.json"
OUT_JSON = ROOT / "04_MOSPARK_PLATFORM" / "data" / "ads_segments.json"
OUT_MD = ROOT / "04_MOSPARK_PLATFORM" / "ADS_SEGMENT_DICTIONARY.md"

EXCLUDE_AS_PAGE_TYPES = {
    "Blog", "Tin Tức", "Hỏi đáp", "Guide", "TnC", "Home MoMo", "Download", "Others", ""
}

HUB_CATALOG = {
    "financial": {"id": "financial", "name": "Financial Hub", "display_vn": "Dịch vụ Tài chính"},
    "insurance": {"id": "insurance", "name": "Insurance Hub", "display_vn": "Bảo hiểm"},
    "travel": {"id": "travel", "name": "Travel Hub", "display_vn": "Du lịch và Đi lại"},
    "cinema": {"id": "cinema", "name": "Cinema Hub", "display_vn": "Phim và Giải trí"},
    "telco": {"id": "telco", "name": "Telco Hub", "display_vn": "Viễn thông và Nạp thẻ"},
    "vehicle": {"id": "vehicle", "name": "Vehicle Hub", "display_vn": "Xe và Tiện ích Giao thông"},
    "billpay": {"id": "billpay", "name": "Billpay Hub", "display_vn": "Hóa đơn và Đời sống"},
    "merchant": {"id": "merchant", "name": "Merchant Hub", "display_vn": "Đối tác và Doanh nghiệp"},
    "game": {"id": "game", "name": "Game Hub", "display_vn": "Cộng đồng Game"},
    "payment": {"id": "payment", "name": "Payment Hub", "display_vn": "Thanh toán và Chuyển tiền"},
    "student": {"id": "student", "name": "Student Hub", "display_vn": "Gói Sinh viên"},
    "new_user": {"id": "new_user", "name": "New User Hub", "display_vn": "Khách hàng mới"},
    "lottery": {"id": "lottery", "name": "Lottery Hub", "display_vn": "Vé số"},
    "general": {"id": "general", "name": "General Platform", "display_vn": "Tiện ích Nền tảng chung"}
}

def get_hub(proj_name: str) -> str:
    p = proj_name.lower()
    if "cinema" in p:
        return "cinema"
    if any(k in p for k in [
        "vay", "ví trả sau", "tiết kiệm", "túi thần tài", "chứng khoán", 
        "quản lý chi tiêu", "tài chính", "thẻ tín dụng", "ngân hàng", 
        "tỷ giá", "giá vàng", "lãi suất", "apple", "quỹ", "sàn đầu tư"
    ]):
        return "financial"
    if "bảo hiểm" in p:
        return "insurance"
    if any(k in p for k in ["vé xe", "ota", "cross border"]):
        return "travel"
    if any(k in p for k in ["sim", "data", "esim", "airtime", "nạp tiền điện thoại"]):
        return "telco"
    if any(k in p for k in [
        "phạt nguội", "giao thông", "phí không dừng", "xe", "xăng", 
        "trạm sạc", "csgt", "garage"
    ]):
        return "vehicle"
    if any(k in p for k in [
        "điện", "nước", "billpay", "internet", "truyền hình", 
        "chung cư", "học phí", "phí xét tuyển"
    ]):
        return "billpay"
    if any(k in p for k in ["merchant", "soundbox"]):
        return "merchant"
    if any(k in p for k in ["game"]):
        return "game"
    if any(k in p for k in [
        "p2p", "liên kết", "tiktok", "application", "hoàn tiền", 
        "chuyển tiền", "xu"
    ]):
        return "payment"
    if "student" in p:
        return "student"
    if "new user" in p:
        return "new_user"
    if "vé số" in p:
        return "lottery"
    return "general"

def normalize_segment_name(raw_name: str) -> str:
    raw_name = raw_name.strip()
    if raw_name.startswith("Cinema_") or raw_name == "Cinema":
        return "Cinema"
    return raw_name

def make_code(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("utf-8")
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s).strip("_").lower()
    return f"seg_{s}" if not s.startswith("seg_") else s

def build_segments():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Missing {CSV_PATH}")

    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        raw_rules = list(reader)

    mapping_counts = defaultdict(int)
    if MAPPING_JSON.exists():
        with open(MAPPING_JSON, "r", encoding="utf-8") as f:
            mapping_data = json.load(f)
            for item in mapping_data.get("mapping", []):
                prim = item.get("primary", "").strip()
                if prim in EXCLUDE_AS_PAGE_TYPES:
                    continue
                seg_name = normalize_segment_name(prim)
                mapping_counts[seg_name] += 1

    segments = {}

    for r in raw_rules:
        p = r["project_name"].strip()
        if p in EXCLUDE_AS_PAGE_TYPES:
            continue
        
        seg_name = normalize_segment_name(p)
        pt = r.get("page_type", "").strip()
        rule = r.get("page_rule", "").strip()
        t = r.get("type", "").strip()
        
        if seg_name not in segments:
            hub_key = get_hub(seg_name)
            hub_meta = HUB_CATALOG.get(hub_key, HUB_CATALOG["general"])
            segments[seg_name] = {
                "segment_id": make_code(seg_name),
                "segment_name": seg_name,
                "hub_id": hub_meta["id"],
                "hub_name": hub_meta["name"],
                "hub_display_vn": hub_meta["display_vn"],
                "page_types_supported": set(),
                "rules_count": 0,
                "matched_urls_count": 0,
                "rules": []
            }
        
        segments[seg_name]["rules_count"] += 1
        if pt:
            segments[seg_name]["page_types_supported"].add(pt)
        segments[seg_name]["rules"].append({
            "rule": rule,
            "match_type": t,
            "page_type": pt
        })

    # Update matched url counts
    for seg_name, seg_data in segments.items():
        seg_data["matched_urls_count"] = mapping_counts[seg_name]
        seg_data["page_types_supported"] = sorted(list(seg_data["page_types_supported"]))

    # Prepare JSON serializable output
    sorted_segments = sorted(segments.values(), key=lambda x: (x["hub_id"], -x["rules_count"]))
    
    # Group by Hub
    by_hub = defaultdict(list)
    for s in sorted_segments:
        by_hub[s["hub_id"]].append(s)

    output_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "description": "Từ điển phân khúc (Segment Dictionary) chuẩn hóa cho Ads Manager dựa trên DIM_URL",
        "rules_enforced": [
            "Hợp nhất toàn bộ Cinema_* vào 1 Segment duy nhất: 'Cinema'",
            "Loại bỏ Blog, Tin Tức, Hỏi đáp, Guide khỏi Segment (đây là Page Type, không phải Segment)",
            "Đồng bộ trực tiếp với DIM_URL và performance.sqlite"
        ],
        "total_segments": len(sorted_segments),
        "total_rules": sum(s["rules_count"] for s in sorted_segments),
        "total_matched_urls": sum(s["matched_urls_count"] for s in sorted_segments),
        "hubs_count": len(by_hub),
        "segments": sorted_segments
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"-> Đã tạo {OUT_JSON} ({len(sorted_segments)} segments)")

    # Build Markdown documentation
    lines = []
    lines.append("# ADS SEGMENT DICTIONARY (TỪ ĐIỂN PHÂN KHÚC ADS MANAGER)")
    lines.append("")
    lines.append("> **Quy chuẩn nguồn sự thật duy nhất (SSOT):** Toàn bộ danh mục Segment trong Ads Manager được chuẩn hóa trực tiếp từ `project_name` trong bảng `DIM_URL` (`web_dim_page_url.csv`).")
    lines.append("")
    lines.append("## 1. Nguyên Tắc Phân Định: Segment (Dịch Vụ) vs Page Type (Loại Trang)")
    lines.append("")
    lines.append("Trong kiến trúc nhắm mục tiêu (Targeting) của Ads Manager, hệ thống phân biệt rạch ròi 2 khái niệm:")
    lines.append("")
    lines.append("- **Segment (Dịch vụ / Sản phẩm kinh doanh):** Đại diện cho nghiệp vụ kinh doanh của MoMo (ví dụ: `Vay Nhanh`, `Ví Trả Sau`, `Bảo Hiểm Xe Máy`, `Cinema`, `Vé Xe`, `OTA`, `Túi Thần Tài`). Đây là trường chính mà PM/Marketer lựa chọn khi tạo chiến dịch quảng cáo.")
    lines.append("- **Page Type (Loại trang / Định dạng nội dung):** Đại diện cho loại hình trang hiển thị (ví dụ: `Blog`, `Tin Tức`, `Hỏi đáp`, `Guide`, `Landing Page`, `Home Page`). Các định dạng này **không phải là Segment độc lập** mà là trường lọc phụ (Secondary Filter) nằm ngang qua các Segment.")
    lines.append("")
    lines.append("### Điểm Chuẩn Hóa Cốt Lõi:")
    lines.append("1. **Hợp nhất Cinema:** Toàn bộ các nhánh con (`Cinema_Home Page`, `Cinema_Page`, `Cinema_Blog`, `Cinema_Cineplex Page`, `Cinema_Landing Page`, `Cinema_News`) được quy tụ về một Segment duy nhất mang tên **`Cinema`** (mã `seg_cinema`).")
    lines.append("2. **Bóc tách Blog, Tin Tức, Hỏi đáp:** Các nhãn `Blog`, `Tin Tức`, `Hỏi đáp`, `Guide` được chuyển về đúng bản chất là `Page Type`. Khi muốn đặt Ads trên bài viết blog về Vay Nhanh, PM sẽ chọn `Segment = Vay Nhanh` và tùy chọn `Page Type = Blog`.")
    lines.append("")
    lines.append(f"## 2. Thống Kê Tổng Quan (Cập nhật: {datetime.now(timezone.utc).strftime('%Y-%m-%d')})")
    lines.append("")
    lines.append(f"- **Tổng số Segment hợp lệ:** {len(sorted_segments)} dịch vụ.")
    lines.append(f"- **Tổng số Quy tắc URL bao phủ:** {sum(s['rules_count'] for s in sorted_segments):,} rules.")
    lines.append(f"- **Tổng số URL đã phân loại:** {sum(s['matched_urls_count'] for s in sorted_segments):,} URLs trên toàn bộ website momo.vn.")
    lines.append(f"- **Phân bổ:** 14 Hub dịch vụ.")
    lines.append("")
    lines.append("## 3. Danh Mục Segment Chi Tiết Theo Hub")
    lines.append("")

    for hub_id, hub_info in HUB_CATALOG.items():
        hub_segs = by_hub.get(hub_id, [])
        if not hub_segs:
            continue
        lines.append(f"### {hub_info['name']} ({hub_info['display_vn']})")
        lines.append("")
        lines.append("| Tên Segment | Mã ID | Số Rules | Số URL Khớp | Page Types Hỗ Trợ | URL Mẫu |")
        lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
        for s in hub_segs:
            sample_rule = s["rules"][0]["rule"] if s["rules"] else ""
            if len(sample_rule) > 45:
                sample_rule = sample_rule[:42] + "..."
            types_str = ", ".join(s["page_types_supported"][:3])
            if len(s["page_types_supported"]) > 3:
                types_str += f" (+{len(s['page_types_supported']) - 3})"
            lines.append(f"| **{s['segment_name']}** | `{s['segment_id']}` | {s['rules_count']} | {s['matched_urls_count']:,} | {types_str} | `{sample_rule}` |")
        lines.append("")

    lines.append("## 4. Hướng Dẫn Tích Hợp Vào Ads Manager UI & Runtime")
    lines.append("")
    lines.append("### Cấu trúc Schema Ad Campaign:")
    lines.append("```json")
    lines.append("{")
    lines.append('  "campaign_id": "camp_2026_q2_vaynhanh_01",')
    lines.append('  "ad_name": "Banner Vay Nhanh 10 Trieu",')
    lines.append('  "target_segment": "seg_vay_nhanh",')
    lines.append('  "target_page_types": ["Blog", "Landing Page"],')
    lines.append('  "exclude_urls": ["/vay-nhanh/dieu-khoan"]')
    lines.append("}")
    lines.append("```")
    lines.append("")
    lines.append("### Cơ chế Khớp tại Trình Duyệt (Runtime Matcher):")
    lines.append("1. Khi người dùng vào trang (ví dụ `momo.vn/vay-nhanh/blog/mua-sh-tra-gop-2717`), script Ads Manager đọc URL và đối chiếu với tập rules của `ads_segments.json`.")
    lines.append("2. Khớp đúng rule của `seg_vay_nhanh` với page_type là `Blog`.")
    lines.append("3. Tải và hiển thị ngay các quảng cáo nhắm mục tiêu vào `seg_vay_nhanh`.")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"-> Đã tạo {OUT_MD}")

if __name__ == "__main__":
    build_segments()
