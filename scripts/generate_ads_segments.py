#!/usr/bin/env python3
"""
Tự động tạo danh mục Ads Segment chuẩn hóa cho Ads Manager từ DIM_URL.

Quy tắc chuẩn hóa phiên bản 2.0 (Bổ sung toàn diện):
1. Hợp nhất Cinema: Gộp toàn bộ các nhánh con Cinema_* thành 'Cinema'.
2. Hợp nhất các dịch vụ phân mảnh:
   - Student Pass + Student Hub -> 'Student'
   - Game + Nạp thẻ Game -> 'Game'
   - Phạt Nguội + Nộp Phạt CSGT -> 'Phạt Nguội'
3. Sửa phân loại lệch Hub:
   - 'Điểm Tín Dụng', 'Tiệm Vàng Online' -> Financial Hub
   - 'Nhận Tiền Quốc Tế' -> Payment Hub
4. Bổ sung 6 Segment dịch vụ còn thiếu:
   - Y Tế (Bệnh viện, Viện phí, Đặt lịch khám)
   - Dịch Vụ Công (Cổng DVCQG, Thủ tục hành chính, Phí lệ phí)
   - Vé Tàu (Đường sắt Việt Nam, Vé tàu hỏa)
   - Bảo Hiểm Du Lịch (Bảo hiểm du lịch nội địa và quốc tế)
   - Đăng Kiểm (Đăng kiểm ô tô và xe cơ giới)
   - Tiện Ích Đời Sống (Thần số học, Tử vi, Lịch vạn niên, Phong thủy)
5. Xử lý 2.281 URL từ Blog, Tin Tức, Hỏi đáp, Guide:
   - Bóc tách theo quy tắc từ khóa để gán về đúng Segment dịch vụ tương ứng.
   - Các trang thông tin tài khoản, chính sách, CSKH chung -> Gán vào Segment 'Toàn Website'.
6. Page Type (Blog, Tin Tức, Hỏi đáp, Guide, Landing Page...) được tách làm trường lọc phụ.
"""

import json
import csv
import re
import unicodedata
import sqlite3
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "07_REPORTS" / "data" / "web_dim_page_url.csv"
MAPPING_JSON = ROOT / "07_REPORTS" / "data" / "url_project_mapping.json"
DB_PATH = ROOT / "07_REPORTS" / "data" / "cache" / "performance.sqlite"
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
    "general": {"id": "general", "name": "General Platform", "display_vn": "Nền tảng và Tiện ích chung"}
}

ORPHANED_KEYWORD_RULES = [
    (r"vietlott|ve-so|xo-so|xskt|power-6-55|mega-6-45", "Vé số"),
    (r"game|nap-the-game|nph-game|free-fire|lien-quan|pubg|roblox|genshin|mot-mua-quyt", "Game"),
    (r"vay-nhanh|vay-tien|khoan-vay|lai-suat-vay|vay-tieu-dung|vay-tra-gop|vay-von|vay-tin-dung|vay-online|vay-tien-nhanh", "Vay Nhanh"),
    (r"vi-tra-sau|tra-sau", "Ví Trả Sau"),
    (r"tiet-kiem|lai-suat-ngan-hang|gui-tiet-kiem", "Tiết Kiệm Online"),
    (r"tui-than-tai", "Túi Thần Tài"),
    (r"the-tin-dung|mo-the-tin-dung", "Mở Thẻ Tín Dụng"),
    (r"chuyen-tien|chuyen-khoan|p2p|li-xi|lixi", "P2P"),
    (r"nhan-tien-quoc-te|chuyen-tien-quoc-te|remittance|western-union", "Nhận Tiền Quốc Tế"),
    (r"ve-tau|tau-hoa|duong-sat", "Vé Tàu"),
    (r"ve-xe|xe-khach|xe-buyt|bus|xe-do", "Vé Xe"),
    (r"ve-may-bay|chuyen-bay|hang-khong|flight|san-bay|khach-san|hotel|homestay|resort|du-lich|tour-du-lich", "OTA"),
    (r"bao-hiem-du-lich", "Bảo Hiểm Du Lịch"),
    (r"bao-hiem-xe-may|bhxm", "Bảo Hiểm Xe Máy"),
    (r"bao-hiem-o-to|bhoto|vat-chat-xe|than-vo-xe", "Bảo Hiểm Ô Tô"),
    (r"bao-hiem-y-te|bhyt", "Bảo Hiểm Y Tế"),
    (r"bao-hiem-suc-khoe", "Bảo Hiểm Sức Khỏe"),
    (r"bao-hiem-xa-hoi|bhxh", "Bảo Hiểm Xã Hội"),
    (r"bao-hiem", "Bảo Hiểm"),
    (r"sim|esim|data|4g|5g|nap-the-dien-thoai|nap-tien-dien-thoai|viettel|vinaphone|mobifone|airtime", "Data"),
    (r"phat-nguoi|csgt|vi-pham-giao-thong|nop-phat-csgt", "Phạt Nguội"),
    (r"phi-khong-dung|vetc|epass", "Phí Không Dừng"),
    (r"dang-kiem", "Đăng Kiểm"),
    (r"benh-vien|kham-benh|vien-phi|dat-lich-kham", "Y Tế"),
    (r"dich-vu-cong|hanh-chinh-cong|thue-truoc-ba", "Dịch Vụ Công"),
    (r"dien|tien-dien|evn", "Điện"),
    (r"nuoc|tien-nuoc|sawaco", "Nước"),
    (r"internet|fpt|vnpt", "Internet"),
    (r"truyen-hinh", "Truyền Hình"),
    (r"hoc-phi|ssc|hoc-sinh|sinh-vien|dai-hoc|truong|thpt|thcs", "Học Phí"),
    (r"gia-vang|vang-mieng|sjc|tiem-vang", "Giá Vàng"),
    (r"ty-gia|ngoai-te|usd|eur|jpy", "Tỷ Giá"),
    (r"chung-khoan|co-phieu|trai-phieu", "Chứng Khoán"),
    (r"chung-chi-quy|quy-dau-tu", "Chứng Chỉ Quỹ"),
    (r"than-so-hoc|tu-vi|tarot|lich-am|phong-thuy|cung-hoang-dao|tuong-so", "Tiện Ích Đời Sống"),
    (r"merchant|soundbox|chu-cua-hang|ma-qr-thanh-toan", "Merchant"),
    (r"cinema|phim|rap-chieu-phim|cgv|lotte|galaxy|bhd|ve-xem-phim", "Cinema")
]

def normalize_segment_name(raw_name: str) -> str:
    raw = raw_name.strip()
    if raw.startswith("Cinema_") or raw == "Cinema":
        return "Cinema"
    if raw in ["Student Pass", "Student Hub"]:
        return "Student"
    if raw in ["Game", "Nạp thẻ Game"]:
        return "Game"
    if raw in ["Phạt Nguội", "Nộp Phạt CSGT"]:
        return "Phạt Nguội"
    return raw

def get_hub(proj_name: str) -> str:
    p = proj_name.lower()
    if "cinema" in p:
        return "cinema"
    if any(k in p for k in [
        "vay", "ví trả sau", "tiết kiệm", "túi thần tài", "chứng khoán", 
        "quản lý chi tiêu", "tài chính", "thẻ tín dụng", "ngân hàng", 
        "tỷ giá", "giá vàng", "tiệm vàng", "điểm tín dụng", "lãi suất", 
        "apple", "quỹ", "sàn đầu tư"
    ]):
        return "financial"
    if "bảo hiểm" in p:
        return "insurance"
    if any(k in p for k in ["vé xe", "ota", "vé tàu", "cross border"]):
        return "travel"
    if any(k in p for k in ["sim", "data", "esim", "airtime", "nạp tiền điện thoại"]):
        return "telco"
    if any(k in p for k in [
        "phạt nguội", "giao thông", "phí không dừng", "đăng kiểm", "xe", "xăng", 
        "trạm sạc", "csgt", "garage"
    ]):
        return "vehicle"
    if any(k in p for k in [
        "điện", "nước", "billpay", "internet", "truyền hình", 
        "chung cư", "học phí", "phí xét tuyển", "dịch vụ công", "y tế", "bệnh viện"
    ]):
        return "billpay"
    if any(k in p for k in ["merchant", "soundbox"]):
        return "merchant"
    if any(k in p for k in ["game"]):
        return "game"
    if any(k in p for k in [
        "p2p", "liên kết", "tiktok", "application", "hoàn tiền", 
        "chuyển tiền", "nhận tiền", "xu"
    ]):
        return "payment"
    if "student" in p:
        return "student"
    if "new user" in p:
        return "new_user"
    if "vé số" in p:
        return "lottery"
    return "general"

def make_code(name: str) -> str:
    s = name.replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("utf-8")
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s).strip("_").lower()
    return f"seg_{s}" if not s.startswith("seg_") else s

def build_segments():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Missing {CSV_PATH}")

    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        raw_rules = list(reader)

    # Đọc mapping hiện tại
    mapping_counts = defaultdict(int)
    if MAPPING_JSON.exists():
        with open(MAPPING_JSON, "r", encoding="utf-8") as f:
            mapping_data = json.load(f)
            for item in mapping_data.get("mapping", []):
                u = item.get("url", "").lower()
                prim = item.get("primary", "").strip()
                
                # Bóc tách đặc thù nếu URL thuộc 6 dịch vụ mới
                if "benh-vien" in u or "vien-phi" in u:
                    seg_name = "Y Tế"
                elif "dang-kiem" in u:
                    seg_name = "Đăng Kiểm"
                elif "bao-hiem-du-lich" in u:
                    seg_name = "Bảo Hiểm Du Lịch"
                elif "ve-tau" in u or "tau-hoa" in u:
                    seg_name = "Vé Tàu"
                elif "dich-vu-cong" in u:
                    seg_name = "Dịch Vụ Công"
                elif prim in EXCLUDE_AS_PAGE_TYPES:
                    continue
                else:
                    seg_name = normalize_segment_name(prim)
                    
                mapping_counts[seg_name] += 1

    segments = {}

    def ensure_segment(name: str):
        if name not in segments:
            hub_key = get_hub(name)
            hub_meta = HUB_CATALOG.get(hub_key, HUB_CATALOG["general"])
            segments[name] = {
                "segment_id": make_code(name),
                "segment_name": name,
                "hub_id": hub_meta["id"],
                "hub_name": hub_meta["name"],
                "hub_display_vn": hub_meta["display_vn"],
                "page_types_supported": set(),
                "rules_count": 0,
                "matched_urls_count": 0,
                "rules": []
            }
        return segments[name]

    # 1. Khởi tạo 6 Segment dịch vụ mới + Toàn Website
    new_segments_seed = {
        "Y Tế": [
            {"rule": "https://www.momo.vn/thanh-toan-momo-benh-vien-*", "match_type": "Dynamic", "page_type": "Landing Page"},
            {"rule": "https://www.momo.vn/benh-vien/*", "match_type": "Dynamic", "page_type": "Page"}
        ],
        "Dịch Vụ Công": [
            {"rule": "https://www.momo.vn/dich-vu-cong/*", "match_type": "Dynamic", "page_type": "Page"},
            {"rule": "https://www.momo.vn/nop-thue/*", "match_type": "Dynamic", "page_type": "Landing Page"}
        ],
        "Vé Tàu": [
            {"rule": "https://www.momo.vn/ve-tau/*", "match_type": "Dynamic", "page_type": "Page"},
            {"rule": "https://www.momo.vn/ve-tau-hoa", "match_type": "Static", "page_type": "Landing Page"}
        ],
        "Bảo Hiểm Du Lịch": [
            {"rule": "https://www.momo.vn/bao-hiem-du-lich", "match_type": "Static", "page_type": "Product Page"},
            {"rule": "https://www.momo.vn/bao-hiem-du-lich-quoc-te", "match_type": "Static", "page_type": "Product Page"}
        ],
        "Đăng Kiểm": [
            {"rule": "https://www.momo.vn/dang-kiem/*", "match_type": "Dynamic", "page_type": "Page"},
            {"rule": "https://www.momo.vn/dang-kiem-xe-o-to", "match_type": "Static", "page_type": "Landing Page"}
        ],
        "Tiện Ích Đời Sống": [
            {"rule": "https://www.momo.vn/blog/than-so-hoc-*", "match_type": "Dynamic", "page_type": "Blog"},
            {"rule": "https://www.momo.vn/lich-van-nien", "match_type": "Static", "page_type": "Tool Page"}
        ],
        "Toàn Website": [
            {"rule": "https://www.momo.vn/", "match_type": "Static", "page_type": "Home Page"},
            {"rule": "https://www.momo.vn/hoi-dap/*", "match_type": "Dynamic", "page_type": "Hỏi đáp"},
            {"rule": "https://www.momo.vn/huong-dan/*", "match_type": "Dynamic", "page_type": "Guide"}
        ]
    }

    for name, seed_rules in new_segments_seed.items():
        seg = ensure_segment(name)
        for sr in seed_rules:
            seg["rules"].append(sr)
            seg["rules_count"] += 1
            seg["page_types_supported"].add(sr["page_type"])

    # 2. Xử lý các rules từ web_dim_page_url.csv
    for r in raw_rules:
        p = r["project_name"].strip()
        pt = r.get("page_type", "").strip()
        rule = r.get("page_rule", "").strip()
        t = r.get("type", "").strip()
        rule_lower = rule.lower()

        # Bóc tách nếu rule thuộc các dịch vụ mới
        if "benh-vien" in rule_lower:
            seg_name = "Y Tế"
        elif "dang-kiem" in rule_lower:
            seg_name = "Đăng Kiểm"
        elif "bao-hiem-du-lich" in rule_lower:
            seg_name = "Bảo Hiểm Du Lịch"
        elif "ve-tau" in rule_lower:
            seg_name = "Vé Tàu"
        elif p in EXCLUDE_AS_PAGE_TYPES:
            continue
        else:
            seg_name = normalize_segment_name(p)
        
        seg = ensure_segment(seg_name)
        seg["rules_count"] += 1
        if pt:
            seg["page_types_supported"].add(pt)
        seg["rules"].append({
            "rule": rule,
            "match_type": t,
            "page_type": pt
        })

    # 3. Phân loại 2.297 URLs bị vô thừa nhận từ DB
    if DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT path, primary_project FROM dim_url_project 
            WHERE primary_project IN ('Blog', 'Tin Tức', 'Hỏi đáp', 'Guide', '', 'others')
        """)
        orphaned_rows = cursor.fetchall()

        for path, old_proj in orphaned_rows:
            p_lower = path.lower()
            target_seg = None
            for pattern, s_name in ORPHANED_KEYWORD_RULES:
                if re.search(pattern, p_lower):
                    target_seg = s_name
                    break
            
            if not target_seg:
                target_seg = "Toàn Website"
            
            seg = ensure_segment(target_seg)
            seg["matched_urls_count"] += 1

            # Xác định Page Type
            pt_name = "Page"
            if "/blog/" in path or old_proj == "Blog":
                pt_name = "Blog"
            elif "/tin-tuc/" in path or old_proj == "Tin Tức":
                pt_name = "Tin Tức"
            elif "/hoi-dap/" in path or old_proj == "Hỏi đáp":
                pt_name = "Hỏi đáp"
            elif "/huong-dan/" in path or old_proj == "Guide":
                pt_name = "Guide"
            
            seg["page_types_supported"].add(pt_name)

    # 4. Cập nhật matched_urls_count từ mapping file gốc
    for seg_name, count in mapping_counts.items():
        if seg_name in segments:
            segments[seg_name]["matched_urls_count"] += count

    # 5. Format & Sort
    for seg in segments.values():
        seg["page_types_supported"] = sorted(list(seg["page_types_supported"]))

    sorted_segments = sorted(segments.values(), key=lambda x: (x["hub_id"], -x["rules_count"]))
    by_hub = defaultdict(list)
    for s in sorted_segments:
        by_hub[s["hub_id"]].append(s)

    output_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "version": "2.0",
        "description": "Từ điển phân khúc (Segment Dictionary) chuẩn hóa toàn diện cho Ads Manager",
        "rules_enforced": [
            "Hợp nhất Cinema: Gộp toàn bộ Cinema_* vào 1 Segment duy nhất 'Cinema'",
            "Hợp nhất phân mảnh: Student (Pass+Hub), Game (Game+Nạp thẻ), Phạt Nguội (Phạt nguội+CSGT)",
            "Sửa lệch Hub: Điểm Tín Dụng & Tiệm Vàng Online về Financial Hub; Nhận Tiền Quốc Tế về Payment Hub",
            "Bổ sung 6 Segment còn thiếu: Y Tế, Dịch Vụ Công, Vé Tàu, Bảo Hiểm Du Lịch, Đăng Kiểm, Tiện Ích Đời Sống",
            "Bổ sung Segment 'Toàn Website' để quy tụ các trang tài khoản, bảo mật, CSKH chung",
            "Phân loại lại 2.297 URL trước đây bị gán nhãn thô là Blog, Tin Tức, Hỏi đáp về đúng Segment dịch vụ"
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

    # 6. Viết Markdown Documentation
    lines = []
    lines.append("# ADS SEGMENT DICTIONARY (TỪ ĐIỂN PHÂN KHÚC ADS MANAGER - PHIÊN BẢN 2.0)")
    lines.append("")
    lines.append("> **Quy chuẩn nguồn sự thật duy nhất (SSOT):** Bảng danh mục Segment dịch vụ chuẩn hóa dùng chung cho toàn bộ nền tảng Ads Manager và Web Platform momo.vn.")
    lines.append("")
    lines.append("## 1. Nguyên Tắc Phân Định: Segment (Dịch Vụ) vs Page Type (Loại Trang)")
    lines.append("")
    lines.append("- **Segment (Dịch vụ / Sản phẩm kinh doanh):** Đại diện cho dịch vụ kinh doanh cụ thể (ví dụ: `Vay Nhanh`, `Ví Trả Sau`, `Cinema`, `Vé Xe`, `Y Tế`, `Dịch Vụ Công`). Đây là trường chính mà PM/Marketer lựa chọn khi tạo chiến dịch quảng cáo.")
    lines.append("- **Page Type (Loại trang / Định dạng nội dung):** Đại diện cho loại hình trang hiển thị (ví dụ: `Blog`, `Tin Tức`, `Hỏi đáp`, `Guide`, `Landing Page`, `Home Page`). Đây là trường lọc phụ để thu hẹp phạm vi nhắm mục tiêu.")
    lines.append("")
    lines.append("### Các Chuẩn Hóa Cốt Lõi Được Áp Dụng:")
    lines.append("1. **Hợp nhất Cinema:** Toàn bộ rạp chiếu phim, bài đánh giá phim, trang cụm rạp CGV/Lotte/Galaxy/BHD quy tụ về 1 Segment duy nhất: `Cinema` (`seg_cinema`).")
    lines.append("2. **Hợp nhất phân mảnh:** `Student Pass` + `Student Hub` gộp thành `Student`; `Game` + `Nạp thẻ Game` gộp thành `Game`; `Phạt Nguội` + `Nộp Phạt CSGT` gộp thành `Phạt Nguội`.")
    lines.append("3. **Sửa lệch Hub:** `Điểm Tín Dụng`, `Tiệm Vàng Online` chuyển về `Financial Hub`; `Nhận Tiền Quốc Tế` chuyển về `Payment Hub`.")
    lines.append("4. **Bổ sung 6 Segment còn thiếu:** `Y Tế`, `Dịch Vụ Công`, `Vé Tàu`, `Bảo Hiểm Du Lịch`, `Đăng Kiểm`, `Tiện Ích Đời Sống`.")
    lines.append("5. **Bổ sung Segment Toàn Website:** Nhận diện các trang CSKH, bảo mật, giới thiệu ví chung (`seg_toan_website`).")
    lines.append("6. **Giải cứu 2.297 URL vô thừa nhận:** Tự động phân loại toàn bộ bài viết trong `/blog/`, `/tin-tuc/`, `/hoi-dap/`, `/huong-dan/` về đúng Segment tương ứng.")
    lines.append("")
    lines.append(f"## 2. Thống Kê Tổng Quan (Cập nhật: {datetime.now(timezone.utc).strftime('%Y-%m-%d')})")
    lines.append("")
    lines.append(f"- **Tổng số Segment hợp lệ:** {len(sorted_segments)} dịch vụ kinh doanh.")
    lines.append(f"- **Tổng số Quy tắc URL bao phủ:** {sum(s['rules_count'] for s in sorted_segments):,} rules.")
    lines.append(f"- **Tổng số URL đã phân loại:** {sum(s['matched_urls_count'] for s in sorted_segments):,} URLs trên toàn bộ website momo.vn.")
    lines.append(f"- **Số lượng Hub:** {len(by_hub)} Hub dịch vụ.")
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

    lines.append("## 4. Hướng Dẫn Tích Hợp Vào Ads Manager")
    lines.append("")
    lines.append("### Cấu trúc Payload Campaign khi tạo Ad:")
    lines.append("```json")
    lines.append("{")
    lines.append('  "campaign_id": "camp_2026_q2_vaynhanh_01",')
    lines.append('  "ad_name": "Floating Dock - Khoản vay nhanh 10 triệu",')
    lines.append('  "target_segment": "seg_vay_nhanh",')
    lines.append('  "target_page_types": ["Blog", "Landing Page"],')
    lines.append('  "exclude_urls": ["/vay-nhanh/dieu-khoan"]')
    lines.append("}")
    lines.append("```")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"-> Đã tạo {OUT_MD}")

if __name__ == "__main__":
    build_segments()
