# -*- coding: utf-8 -*-
"""
THEME MATCHER (SSOT) - trích xuất từ build_full_funnel_matrix.py
Bộ khớp URL -> Theme/Project/Sector đa tầng (Cluster URLs + DIM resolver +
project_to_theme + dir/slug rules). Dùng chung cho ingest_ga4_daily và các
pipeline phân tích local. KHÔNG gọi API ngoài.
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote

BASE_DIR = Path(__file__).resolve().parents[2]
HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")
sys.path.insert(0, str(BASE_DIR / "scripts" / "lib"))
import url_project_resolver as upr

def normalize_path(url_str):
    if not url_str:
        return "/"
    p = unquote(urlparse(str(url_str)).path).lower().strip()
    p = re.sub(r"/+", "/", p)
    p = re.sub(r"/index\.(html?|php)$", "", p, flags=re.I)
    p = p.rstrip("/")
    return p if p else "/"


def build_theme_matcher():
    """Tạo bộ khớp Theme đa tầng tích hợp url_project_resolver SSOT + Cluster URLs + Thư mục + Slug"""
    # 1. Nạp DIM rules & Inferred rules qua url_project_resolver
    dim_rules = upr.load_rules()
    inferred_rules = upr.load_inferred_rules(dim_rules)

    # 2. Nạp Cluster URLs
    summary_file = HUBS_REPO / "data" / "seo-clusters-summary.json"
    if not summary_file.exists():
        summary_file = BASE_DIR / "07_REPORTS" / "data" / "inventory_clusters_summary.json"

    exact_map = {}
    prefix_rules = []

    if summary_file.exists():
        with open(summary_file, "r", encoding="utf-8") as f:
            clusters_data = json.load(f)

        for u in clusters_data.get("usecases", []):
            tid = u.get("id")
            tname = u.get("display_name") or u.get("name")
            sec = u.get("sector")
            mvol = u.get("total_volume", 0)
            
            top_url = u.get("cannibalization_shield", {}).get("top_live_url")
            if top_url:
                p = normalize_path(top_url)
                exact_map[p] = (tid, tname, sec, mvol)
                if p != "/":
                    prefix_rules.append((p, tid, tname, sec, mvol))

        prefix_rules.sort(key=lambda x: len(x[0]), reverse=True)

    # 3. Từ điển mapping toàn bộ Projects trong hub-map.json -> Hubs Theme & Sector
    project_to_theme = {
        "Cinema": ("ve-xem-phim", "Vé Xem Phim & Rạp", "cinema", 500000),
        "Cinema_Page": ("ve-xem-phim", "Vé Xem Phim & Rạp", "cinema", 500000),
        "Cinema_Cineplex Page": ("ve-xem-phim", "Cụm Rạp Chiếu Phim", "cinema", 500000),
        "Cinema_Home Page": ("ve-xem-phim", "Trang Chủ Vé Xem Phim", "cinema", 500000),
        "Cinema_Blog": ("ve-xem-phim", "Blog Điện Ảnh", "cinema", 300000),
        "Cinema_News": ("ve-xem-phim", "Tin Tức Điện Ảnh", "cinema", 200000),
        "Cinema_Landing Page": ("ve-xem-phim", "Landing Page Cinema", "cinema", 250000),
        "Ví Trả Sau": ("vi-tra-sau", "Ví Trả Sau", "Financial", 450000),
        "Ví Trả Sau (BNPL)": ("vi-tra-sau", "Ví Trả Sau", "Financial", 450000),
        "Vay Nhanh": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Vay nhanh": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Vay Nhanh & Vay Tín Chấp": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Thanh Toán Khoản Vay": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Trả Góp Apple": ("vi-tra-sau", "Ví Trả Sau", "Financial", 350000),
        "Mở Thẻ Tín Dụng": ("the-tin-dung", "Mở Thẻ Tín Dụng", "Financial", 250000),
        "Thanh Toán Thẻ Tín Dụng": ("the-tin-dung", "Mở Thẻ Tín Dụng", "Financial", 250000),
        "Điểm Tín Dụng": ("diem-tin-dung", "Điểm Tín Dụng", "Financial", 200000),
        "Điểm Tín Dụng & CIC": ("diem-tin-dung", "Điểm Tín Dụng", "Financial", 200000),
        "TnC": ("trust", "TnC", "trust", 100000),
        "Tnc": ("trust", "TnC", "trust", 100000),
        "Tiết Kiệm Online": ("gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        "Túi Thần Tài": ("gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        "Chứng Khoán": ("chung-khoan", "Chứng Khoán", "Financial", 200000),
        "Chứng Chỉ Quỹ": ("chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        "Quỹ": ("chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        "Sàn Đầu Tư": ("chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        "Giá Vàng": ("gia-vang", "Giá Vàng", "Financial", 800000),
        "Tiệm Vàng Online": ("gia-vang", "Giá Vàng", "Financial", 800000),
        "Tỷ Giá": ("ty-gia", "Tỷ Giá Ngoại Tệ", "Financial", 350000),
        "Mở tài khoản ngân hàng": ("chuyen-tien", "Mở Tài Khoản Ngân Hàng", "Financial", 300000),
        "Trung Tâm Tài Chính": ("chuyen-tien", "Trung Tâm Tài Chính", "Financial", 300000),
        "Trung Tâm tài chính": ("chuyen-tien", "Trung Tâm Tài Chính", "Financial", 300000),
        "Trung tâm tài chính": ("chuyen-tien", "Trung Tâm Tài Chính", "Financial", 300000),
        "Quản Lý Chi Tiêu": ("quan-ly-chi-tieu", "Quản Lý Chi Tiêu", "Financial", 150000),
        "Quản lý chi tiêu": ("quan-ly-chi-tieu", "Quản Lý Chi Tiêu", "Financial", 150000),
        "P2P": ("chuyen-tien", "Chuyển Tiền MoMo", "Financial", 300000),
        "Billpay": ("billpay-nuoc", "Thanh Toán Hóa Đơn", "Financial", 250000),
        "Điện": ("billpay-dien", "Thanh Toán Tiền Điện", "Financial", 250000),
        "Nước": ("billpay-nuoc", "Thanh Toán Tiền Nước", "Financial", 200000),
        "Internet": ("billpay-internet", "Thanh Toán Internet", "Financial", 200000),
        "Bảo Hiểm Ô Tô": ("bao-hiem-o-to", "Bảo Hiểm Ô Tô", "insurtech", 150000),
        "Bảo Hiểm Xe Máy": ("bao-hiem-xe-may", "Bảo Hiểm Xe Máy", "insurtech", 120000),
        "Bảo Hiểm Y Tế": ("bhyt", "Bảo Hiểm Y Tế (BHYT)", "insurtech", 180000),
        "Bảo Hiểm Xã Hội": ("bhxh", "Bảo Hiểm Xã Hội (BHXH)", "insurtech", 140000),
        "Bảo Hiểm Sức Khỏe": ("bao-hiem-nhan-tho", "Bảo Hiểm Sức Khỏe", "insurtech", 160000),
        "Bảo Hiểm": ("bao-hiem-nhan-tho", "Bảo Hiểm Tổng Hợp", "insurtech", 160000),
        "Phạt Nguội": ("phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        "Phạt nguội": ("phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        "Phí Không Dừng": ("thu-phi-khong-dung-etc", "Thu Phí Không Dừng ETC", "vehicle-hub", 150000),
        "Tiện Ích Giao Thông": ("dang-kiem", "Tiện Ích Giao Thông", "vehicle-hub", 200000),
        "Cây xăng": ("dang-kiem", "Cây Xăng & Tiện Ích Xe", "vehicle-hub", 200000),
        "Giá xăng": ("dang-kiem", "Giá Xăng Dầu", "vehicle-hub", 200000),
        "Trạm sạc": ("dang-kiem", "Trạm Sạc Xe Điện", "vehicle-hub", 200000),
        "OTA": ("ve-may-bay", "Vé Máy Bay & Du Lịch OTA", "ota", 600000),
        "Vé Xe": ("ve-xe-khach", "Vé Xe Khách", "ota", 350000),
        "Esim": ("esim-du-lich", "eSIM Du Lịch", "ota", 100000),
        "Game": ("nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        "Game Hub": ("nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        "Nạp thẻ Game": ("nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        "Tiktok": ("nap-xu-tiktok", "Nạp Xu TikTok", "Entertainment", 350000),
        "Data": ("nap-data-4g", "Nạp Data 3G/4G/5G", "telco", 500000),
        "Sim": ("sim-so-dep", "Sim Số Đẹp", "telco", 300000),
        "Airtime": ("nap-tien-dien-thoai", "Nạp Tiền Điện Thoại", "telco", 400000),
        "Nạp tiền điện thoại": ("nap-tien-dien-thoai", "Nạp Tiền Điện Thoại", "telco", 400000),
        "Student Hub": ("sinh-vien", "Sinh Viên Hub", "student", 150000),
        "Student Pass": ("sinh-vien", "Sinh Viên Hub", "student", 150000),
        "Vé số": ("ve-so-vietlott", "Vé Số & Vietlott", "Lottery", 400000),
        "Merchant": ("merchant-portal", "Cổng Đối Tác Doanh Nghiệp", "trust", 100000),
        "Soundbox": ("soundbox-momo", "Loa Thông Minh Soundbox", "trust", 80000),
        "Donation": ("trai-tim-momo", "Trái Tim MoMo - Thiện Nguyện", "trust", 120000),
        "Trust": ("bao-mat-momo", "Trung Tâm An Toàn & Bảo Mật", "trust", 150000),
        "New User": ("tai-app-portal", "Download & Onboarding Center", "Brand", 500000),
        "Download": ("tai-app-portal", "Download & Onboarding Center", "Brand", 500000),
        "Home MoMo": ("homepage", "Trang Chủ MoMo", "Brand", 1500000),
        "Application Store": ("tai-app-portal", "Download Center", "Brand", 500000),
        "Campaign": ("promotion-campaign", "Chiến Dịch & Sự Kiện", "Promotion", 250000),
        "Khuyến mãi": ("promotion-news", "Tin Khuyến Mãi & Ưu Đãi", "Promotion", 250000),
        "Hoàn Tiền Mua Sắm": ("promotion-news", "Hoàn Tiền Mua Sắm", "Promotion", 200000),
        "XU": ("promotion-news", "Tích Xu Đổi Quà", "Promotion", 200000),
        "Dịch Vụ Liên Kết": ("dich-vu-lien-ket", "Dịch Vụ Liên Kết", "Other", 100000),
        "Dịch vụ liên kết": ("dich-vu-lien-ket", "Dịch Vụ Liên Kết", "Other", 100000),
        "Cross Border": ("dich-vu-lien-ket", "Thanh Toán Quốc Tế", "Other", 100000),
        "Hỏi đáp": ("customer-support", "Hỏi Đáp Trợ Giúp", "Support", 150000),
        "Guide": ("huong-dan-momo", "Hướng Dẫn Sử Dụng", "Support", 150000),
        "Tìm Kiếm": ("customer-support", "Tìm Kiếm Trợ Giúp", "Support", 100000),
        "Tin Tức": ("lifestyle-news", "Tin Tức & Đời Sống", "Lifestyle", 200000),
        "Blog": ("lifestyle-news", "Tin Tức & Đời Sống", "Lifestyle", 200000),
        "Others": ("lifestyle-news", "Nội Dung Khác", "Other", 100000),
    }

    # 4. Từ điển thư mục và slug chuẩn
    dir_rules = [
        ("/cinema", "ve-xem-phim", "Vé Xem Phim & Rạp", "cinema", 500000),
        ("/vi-tra-sau", "vi-tra-sau", "Ví Trả Sau", "Financial", 450000),
        ("/vay-nhanh", "vay-tin-chap", "Vay Nhanh & Vay Tín Chấp", "Financial", 400000),
        ("/diem-tin-dung", "diem-tin-dung", "Điểm Tín Dụng & CIC", "Financial", 200000),
        ("/nap-xu-tiktok", "nap-xu-tiktok", "Nạp Xu TikTok", "Entertainment", 350000),
        ("/bao-hiem-o-to", "bao-hiem-o-to", "Bảo Hiểm Ô Tô", "insurtech", 150000),
        ("/bao-hiem-xe-may", "bao-hiem-xe-may", "Bảo Hiểm Xe Máy", "insurtech", 120000),
        ("/bao-hiem-y-te", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("/bao-hiem-xa-hoi", "bhxh", "Bảo Hiểm Xã Hội", "insurtech", 140000),
        ("/phat-nguoi", "phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        ("/ve-xe", "ve-xe-khach", "Vé Xe Khách", "ota", 350000),
        ("/ve-tau", "ve-tau-hoa", "Vé Tàu Hỏa", "ota", 250000),
        ("/ve-may-bay", "ve-may-bay", "Vé Máy Bay", "ota", 600000),
        ("/esim", "esim-du-lich", "eSIM Du Lịch", "ota", 100000),
        ("/sinh-vien", "sinh-vien", "Sinh Viên Hub", "student", 150000),
        ("/nap-the-game", "nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        ("/nuoc", "billpay-nuoc", "Thanh Toán Tiền Nước", "Financial", 200000),
        ("/dien", "billpay-dien", "Thanh Toán Tiền Điện", "Financial", 250000),
        ("/tai-app", "tai-app-portal", "Download Center", "Brand", 500000),
        ("/download", "tai-app-portal", "Download Center", "Brand", 500000),
        ("/", "homepage", "Trang Chủ MoMo", "Brand", 1500000),
    ]

    slug_rules = [
        ("vi-tra-sau", "vi-tra-sau", "Ví Trả Sau (BNPL)", "Financial", 450000),
        ("vay-nhanh", "vay-tin-chap", "Vay Nhanh & Vay Tín Chấp", "Financial", 400000),
        ("vay-tin-chap", "vay-tin-chap", "Vay Nhanh & Vay Tín Chấp", "Financial", 400000),
        ("diem-tin-dung", "diem-tin-dung", "Điểm Tín Dụng & CIC", "Financial", 200000),
        ("cic", "diem-tin-dung", "Điểm Tín Dụng & CIC", "Financial", 200000),
        ("bao-hiem-o-to", "bao-hiem-o-to", "Bảo Hiểm Ô Tô", "insurtech", 150000),
        ("bao-hiem-xe-may", "bao-hiem-xe-may", "Bảo Hiểm Xe Máy", "insurtech", 120000),
        ("bao-hiem-y-te", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("bao-hiem-xa-hoi", "bhxh", "Bảo Hiểm Xã Hội", "insurtech", 140000),
        ("bao-hiem-nhan-tho", "bao-hiem-nhan-tho", "Bảo Hiểm Nhân Thọ", "insurtech", 160000),
        ("bao-hiem-tai-nan", "bao-hiem-tai-nan", "Bảo Hiểm Tai Nạn", "insurtech", 100000),
        ("gia-vang", "gia-vang", "Giá Vàng", "Financial", 800000),
        ("lai-suat", "gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        ("tiet-kiem", "gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        ("ty-gia", "ty-gia", "Tỷ Giá Ngoại Tệ", "Financial", 350000),
        ("the-tin-dung", "the-tin-dung", "Mở Thẻ Tín Dụng", "Financial", 250000),
        ("chung-khoan", "chung-khoan", "Chứng Khoán", "Financial", 200000),
        ("chung-chi-quy", "chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        ("bhyt", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("bhxh", "bhxh", "Bảo Hiểm Xã Hội", "insurtech", 140000),
        ("tra-cuu-bao-hiem", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("phat-nguoi", "phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        ("dang-kiem", "dang-kiem", "Đăng Kiểm Xe", "vehicle-hub", 200000),
        ("chuyen-tien", "chuyen-tien", "Chuyển Tiền MoMo", "Financial", 300000),
        ("hoc-phi", "sinh-vien", "Sinh Viên Hub", "student", 150000),
        ("du-lich", "du-lich-tong-hop", "Cẩm Nang Du Lịch", "ota", 300000),
        ("khuyen-mai", "promotion-news", "Tin Khuyến Mãi", "Promotion", 250000),
    ]

    def match(path):
        p = path.lower()
        full_url = "https://www.momo.vn" + p if p != "/" else "https://www.momo.vn"

        # Tier 1: Xác định Project chính qua resolve_primary trong scripts/lib/url_project_resolver.py
        res = upr.resolve(full_url, dim_rules, inferred_rules)
        proj_name = res.get("primary") or None
        page_type = res["matches"][0]["page_type"] if (res.get("matched") and res.get("matches")) else None

        # Tier 2: Khớp Theme từ Cluster URLs
        tid, tname, sec, mvol = None, None, "Other", 0
        if p in exact_map:
            tid, tname, sec, mvol = exact_map[p]
        else:
            for prefix, c_tid, c_tname, c_sec, c_mvol in prefix_rules:
                if p.startswith(prefix + "/"):
                    tid, tname, sec, mvol = c_tid, c_tname, c_sec, c_mvol
                    break

        # Tier 3: Gán Theme & Sector từ project_to_theme
        if proj_name and proj_name in project_to_theme:
            p_tid, p_tname, p_sec, p_mvol = project_to_theme[proj_name]
            if not tid:
                tid, tname, sec, mvol = p_tid, p_tname, p_sec, p_mvol
            elif sec == "Other" or not sec:
                sec = p_sec

        # Tier 4: Fallback Theme theo thư mục hoặc slug
        if not tid:
            for prefix, c_tid, c_tname, c_sec, c_mvol in dir_rules:
                if p == prefix or p.startswith(prefix + "/"):
                    tid, tname, sec, mvol = c_tid, c_tname, c_sec, c_mvol
                    break
        if not tid:
            for slug, c_tid, c_tname, c_sec, c_mvol in slug_rules:
                if slug in p:
                    tid, tname, sec, mvol = c_tid, c_tname, c_sec, c_mvol
                    break

        # Tier 5: Fallback Project nếu chưa khớp
        if not proj_name:
            if p.startswith("/tin-tuc"): proj_name = "Tin Tức"; page_type = "News"
            elif p.startswith("/blog"): proj_name = "Blog"; page_type = "Blog"
            elif p.startswith("/hoi-dap"): proj_name = "Hỏi đáp"; page_type = "Hỏi đáp"
            elif p.startswith("/huong-dan"): proj_name = "Guide"; page_type = "Guide"
            elif p in ("/", ""): proj_name = "Home MoMo"; page_type = "Home Page"
            elif p.startswith("/chao-ban-moi"): proj_name = "New User"; page_type = "Landing Page"
            elif p.startswith("/tai-app") or p.startswith("/download"): proj_name = "Download"; page_type = "Landing Page"
            else: proj_name = "Others"; page_type = "Page"

        if not tid:
            if p.startswith("/tin-tuc") or p.startswith("/blog"):
                tid, tname, sec, mvol = "lifestyle-news", "Tin Tức & Đời Sống", "Lifestyle", 200000
            elif p.startswith("/hoi-dap"):
                tid, tname, sec, mvol = "customer-support", "Hỏi Đáp Trợ Giúp", "Support", 150000
            else:
                tid, tname, sec, mvol = None, None, "Other", 0

        return tid, tname, sec, mvol, proj_name, page_type or "Page"

    return match
