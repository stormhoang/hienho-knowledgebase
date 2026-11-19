#!/usr/bin/env python3
"""
Rebuild Sitemap Sheet for Financial Hub:
- Local Excel: 05_HUBS/financial/financial-hub-roadmap.xlsx (Sheet: Sitemap)
- Google Sheet: 1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A (Tab: Sitemap)
- Also align Product Roadmap status for standalone migration to 'Chưa triển khai'.
- Update BRD Section 10.
"""

import json
import urllib.parse
import urllib.request
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_PATH = BASE_DIR / "05_HUBS" / "financial" / "financial-hub-roadmap.xlsx"
BRD_PATH = BASE_DIR / "05_HUBS" / "financial" / "financial-hub-brd.md"
CREDS_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
TOKEN_FILE = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gdrive-token.json"
SPREADSHEET_ID = "1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A"

SITEMAP_HEADER = [
    "STT",
    "Giai Đoạn (Phase)",
    "Thời Gian",
    "Phân Cấp / Loại Trang",
    "Tên Trang Cần Tạo (H1 / Title)",
    "Định Tuyến URL Chuẩn Hóa (Canonical URL)",
    "Trạng Thái",
    "Hiện Trạng & Ghi Chú Kỹ Thuật"
]

SITEMAP_ITEMS = [
    # =========================================================================
    # PHASE 0: THÁNG 7/2026 - TÍN DỤNG & TIÊU DÙNG ĐỘC LẬP ROOT (3 URLs)
    # =========================================================================
    [
        "Phase 0", "Tháng 7/2026", "Trang Độc Lập Root (Không Đổi URL)",
        "Ví Trả Sau MoMo & Mua Sắm Trả Góp 0% (Root URL)", "/vi-tra-sau",
        "Done", "Đã Go-live độc lập tại root. Tool tính trả góp 3-12 tháng và so sánh miễn lãi 45 ngày."
    ],
    [
        "Phase 0", "Tháng 7/2026", "Trang Độc Lập Root (Không Đổi URL)",
        "Vay Tiêu Dùng Nhanh Trực Tuyến (Root URL)", "/vay-nhanh",
        "Done", "Đã Go-live độc lập tại root. Tool tính lịch trả nợ dư nợ giảm dần 5-100 triệu."
    ],
    [
        "Phase 0", "Tháng 7/2026", "Trang Độc Lập Root (Không Đổi URL)",
        "Thẻ Tín Dụng Quốc Tế Hoàn Tiền (Root URL)", "/the-tin-dung",
        "Done", "Đã Go-live độc lập tại root. Cổng mở thẻ tín dụng và so sánh đối tác ngân hàng."
    ],

    # =========================================================================
    # PHASE 1: THÁNG 8/2026 - MASTER GATEWAY & TIỆN ÍCH CỐT LÕI (6 URLs)
    # =========================================================================
    [
        "Phase 1", "Tháng 8/2026", "Cổng Trung Tâm (Master Hub)",
        "Financial Master Hub MoMo", "/tai-chinh",
        "Done", "Đã Go-live trên Production. Mega Menu Header responsive toàn cục 4 trụ cột tài chính."
    ],
    [
        "Phase 1", "Tháng 8/2026", "Cổng Danh Mục Tiện Ích (Tools Hub)",
        "Tổng Hợp Công Cụ & Tiện Ích Tài Chính MoMo", "/tai-chinh/cong-cu",
        "Done", "Đã Go-live. Cổng quy tụ toàn bộ 26+ tiện ích tính toán và so sánh tài chính."
    ],
    [
        "Phase 1", "Tháng 8/2026", "Trang Độc Lập Root (Không Đổi URL)",
        "Điểm Tín Dụng & Tra Cứu CIC (Root URL)", "/diem-tin-dung",
        "Done", "Đã Go-live độc lập tại root. Tool tự đánh giá điểm tín dụng CIC (150-750) và xếp hạng nhóm nợ."
    ],
    [
        "Phase 1", "Tháng 8/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Bảng Giá Vàng SJC, 9999 Realtime & Công Cụ Quy Đổi", "/tai-chinh/gia-vang",
        "Done", "Đã Go-live. Tra cứu giá vàng trực tuyến (SJC, DOJI, PNJ, 9999) và tool quy đổi chỉ, lượng."
    ],
    [
        "Phase 1", "Tháng 8/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Tính Lương Gross Sang Net & Ngược Lại 2026", "/tai-chinh/tinh-luong",
        "Done", "Đã Go-live. Tool khấu trừ 10.5% bảo hiểm bắt buộc và thuế TNCN lũy tiến 7 bậc 2026."
    ],
    [
        "Phase 1", "Tháng 8/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Dự Toán Lương Hưu & Tuổi Nghỉ Hưu Luật Mới", "/tai-chinh/luong-huu",
        "Done", "Đã Go-live. Tool dự toán lương hưu và tính tiền trợ cấp BHXH một lần tích hợp trực tiếp."
    ],

    # =========================================================================
    # PHASE 1: THÁNG 9/2026 - TIỀN TỆ, NGÂN SÁCH & LÃI SUẤT THỊ TRƯỜNG (12 URLs)
    # =========================================================================
    [
        "Phase 1", "Tháng 9/2026", "Cổng Danh Mục Under /tai-chinh",
        "Cổng Tỷ Giá Ngoại Tệ 20+ Ngân Hàng", "/tai-chinh/ty-gia",
        "Done", "Đã Go-live. Cổng tra cứu tỷ giá thị trường và tool quy đổi ngoại tệ 30+ đồng tiền."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Trang Con Chi Tiết (Programmatic Spoke)",
        "Hệ Thống Quy Đổi Ngoại Tệ Theo Cặp Tiền ([Đồng Tiền]/VND)", "/tai-chinh/ty-gia/[pair-slug]",
        "Done", "Master template chuẩn SEO/GEO phục vụ sinh tự động các trang cặp tiền tệ chi tiết."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Trang Con Cặp Tiền (Programmatic Subpage)",
        "Tỷ Giá USD/VND Hôm Nay", "/tai-chinh/ty-gia/usd-vnd",
        "Done", "Đã Go-live. Bảng so sánh tỷ giá USD tại 20+ ngân hàng và tool quy đổi USD sang VND."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Trang Con Cặp Tiền (Programmatic Subpage)",
        "Tỷ Giá EUR/VND Hôm Nay", "/tai-chinh/ty-gia/eur-vnd",
        "Done", "Đã Go-live. Bảng so sánh tỷ giá EUR tại 20+ ngân hàng và tool quy đổi EUR sang VND."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Trang Con Cặp Tiền (Programmatic Subpage)",
        "Tỷ Giá Yên Nhật JPY/VND Hôm Nay", "/tai-chinh/ty-gia/jpy-vnd",
        "Done", "Đã Go-live. Bảng so sánh tỷ giá JPY tại 20+ ngân hàng và tool quy đổi JPY sang VND."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Trang Con Cặp Tiền (Programmatic Subpage)",
        "Tỷ Giá Bảng Anh GBP/VND Hôm Nay", "/tai-chinh/ty-gia/gbp-vnd",
        "Done", "Đã Go-live. Bảng so sánh tỷ giá GBP tại 20+ ngân hàng và tool quy đổi GBP sang VND."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Trang Con Cặp Tiền (Programmatic Subpage)",
        "Tỷ Giá Nhân Dân Tệ CNY/VND Hôm Nay", "/tai-chinh/ty-gia/cny-vnd",
        "Done", "Đã Go-live. Bảng so sánh tỷ giá CNY tại 20+ ngân hàng và tool quy đổi CNY sang VND."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Trang Con Cặp Tiền (Programmatic Subpage)",
        "Tỷ Giá Won Hàn KRW/VND Hôm Nay", "/tai-chinh/ty-gia/krw-vnd",
        "Done", "Đã Go-live. Bảng so sánh tỷ giá KRW tại 20+ ngân hàng và tool quy đổi KRW sang VND."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Trang Con Cặp Tiền (Programmatic Subpage)",
        "Tỷ Giá Đô Úc AUD/VND Hôm Nay", "/tai-chinh/ty-gia/aud-vnd",
        "Done", "Đã Go-live. Bảng so sánh tỷ giá AUD tại 20+ ngân hàng và tool quy đổi AUD sang VND."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Trang Con Cặp Tiền (Programmatic Subpage)",
        "Tỷ Giá Đô Singapore SGD/VND Hôm Nay", "/tai-chinh/ty-gia/sgd-vnd",
        "Done", "Đã Go-live. Bảng so sánh tỷ giá SGD tại 20+ ngân hàng và tool quy đổi SGD sang VND."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Phân Bổ Lương 50/30/20 & Hũ Tài Chính", "/tai-chinh/phan-bo-luong",
        "Done", "Đã Go-live. Tool chia hũ tiền lương theo quy tắc 50/30/20 và mô hình 6 Hũ tài chính."
    ],
    [
        "Phase 1", "Tháng 9/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Bảng Tra Cứu Lãi Suất 40 Ngân Hàng Toàn Cảnh Thị Trường", "/tai-chinh/lai-suat",
        "Done", "Đã Go-live. Bảng so sánh lãi suất tiền gửi 40 ngân hàng và tool tính tiền lãi tối ưu."
    ],

    # =========================================================================
    # PHASE 2: THÁNG 10/2026 - TÁI ĐỊNH TUYẾN STANDALONE, CONTENT ENGINE & QUỸ MỞ (20 URLs)
    # =========================================================================
    # A. 6 Trang Standalone Chuyển Về /tai-chinh/* (Chưa triển khai)
    [
        "Phase 2", "Tháng 10/2026", "Trang Dịch Vụ Under /tai-chinh",
        "Túi Sinh Lời (Túi Thần Tài) - Tích Lũy Sinh Lời Mỗi Ngày", "/tai-chinh/tui-sinh-loi",
        "Chưa triển khai", "URL standalone gốc /tui-than-tai đang live độc lập tại root; chưa triển khai chuyển đổi & 301 redirect về /tai-chinh/*."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Dịch Vụ Under /tai-chinh",
        "Cổng Chuyển Tiền & Nhận Tiền Quốc Tế MoMo", "/tai-chinh/nhan-tien-quoc-te",
        "Chưa triển khai", "URL standalone gốc /nhan-tien-quoc-te đang live độc lập tại root; chưa triển khai chuyển đổi & 301 redirect về /tai-chinh/*."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Dịch Vụ Under /tai-chinh",
        "Quỹ Nhóm & Quản Lý Quỹ Chung MoMo", "/tai-chinh/quy-nhom",
        "Chưa triển khai", "URL standalone gốc /quy-nhom đang live độc lập tại root; chưa triển khai chuyển đổi & 301 redirect về /tai-chinh/*."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Dịch Vụ Under /tai-chinh",
        "Thanh Toán Dư Nợ Thẻ Tín Dụng Đa Ngân Hàng", "/tai-chinh/thanh-toan-the-tin-dung",
        "Chưa triển khai", "URL standalone gốc /thanh-toan-the-tin-dung đang live độc lập tại root; chưa triển khai chuyển đổi & 301 redirect về /tai-chinh/*."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Dịch Vụ Under /tai-chinh",
        "Cổng Quản Lý Chi Tiêu Cá Nhân MoMo", "/tai-chinh/quan-ly-chi-tieu",
        "Chưa triển khai", "URL standalone gốc /quan-ly-chi-tieu đang live độc lập tại root; chưa triển khai chuyển đổi & 301 redirect về /tai-chinh/*."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Dịch Vụ Under /tai-chinh",
        "Cổng Tra Cứu Giá NAV & Tích Sản Quỹ Mở MoMo", "/tai-chinh/chung-chi-quy",
        "Chưa triển khai", "URL standalone gốc /chung-chi-quy đang live độc lập tại root; đang review API NAV từ CVS, chưa triển khai chuyển đổi về /tai-chinh/*."
    ],
    # B. Cụm Quỹ Mở Sub-pages (Chưa triển khai)
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Chi Tiết (Programmatic Spoke)",
        "Hệ Thống Trang Chi Tiết 30 Quỹ Mở Đối Tác CVS ([Tên Quỹ])", "/tai-chinh/chung-chi-quy/[fund-slug]",
        "Chưa triển khai", "Master template cho 30 trang quỹ mở chi tiết; chưa triển khai do đang chờ kết nối dữ liệu API NAV."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Máy Tính Giả Lập Tích Sản Định Kỳ Quỹ Mở Từ 10.000đ", "/tai-chinh/chung-chi-quy/tich-san-dinh-ky",
        "Chưa triển khai", "Công cụ tính lãi kép tích sản quỹ mở từ 10.000đ/ngày; chưa triển khai dựng trang."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Quỹ Mở (Programmatic CCQ)",
        "Quỹ Đầu Tư Doanh Nghiệp Hàng Đầu Dragon Capital (DCDS)", "/tai-chinh/chung-chi-quy/dcds",
        "Chưa triển khai", "Trang thông tin quỹ mở Dragon Capital DCDS; chưa triển khai."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Quỹ Mở (Programmatic CCQ)",
        "Quỹ Đầu Tư Cổ Phiếu Tiếp Cận Thị Trường VinaCapital (VESAF)", "/tai-chinh/chung-chi-quy/vesaf",
        "Chưa triển khai", "Trang thông tin quỹ mở VinaCapital VESAF; chưa triển khai."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Quỹ Mở (Programmatic CCQ)",
        "Quỹ Đầu Tư Cổ Phiếu Hưng Thịnh VinaCapital (VEOF)", "/tai-chinh/chung-chi-quy/veof",
        "Chưa triển khai", "Trang thông tin quỹ mở VinaCapital VEOF; chưa triển khai."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Quỹ Mở (Programmatic CCQ)",
        "Quỹ Đầu Tư Cổ Phiếu Tăng Trưởng VCBF (VCBF-MGF)", "/tai-chinh/chung-chi-quy/vcbf-mgf",
        "Chưa triển khai", "Trang thông tin quỹ mở VCBF-MGF; chưa triển khai."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Quỹ Mở (Programmatic CCQ)",
        "Quỹ Đầu Tư Cổ Phiếu Hàng Đầu VCBF (VCBF-BCF)", "/tai-chinh/chung-chi-quy/vcbf-bcf",
        "Chưa triển khai", "Trang thông tin quỹ mở VCBF-BCF; chưa triển khai."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Quỹ Mở (Programmatic CCQ)",
        "Quỹ Đầu Tư Lợi Thế Cạnh Tranh Bền Vững SSI (SSI-SCA)", "/tai-chinh/chung-chi-quy/ssi-sca",
        "Chưa triển khai", "Trang thông tin quỹ mở SSI-SCA; chưa triển khai."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Quỹ Mở (Programmatic CCQ)",
        "Quỹ Đầu Tư Cổ Phiếu Triển Vọng Bảo Việt (BVBF)", "/tai-chinh/chung-chi-quy/bvbf",
        "Chưa triển khai", "Trang thông tin quỹ mở BVBF; chưa triển khai."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Quỹ Mở (Programmatic CCQ)",
        "Quỹ Đầu Tư Chứng Khoán Năng Động Dragon Capital (DCBC)", "/tai-chinh/chung-chi-quy/dcbc",
        "Chưa triển khai", "Trang thông tin quỹ mở DCBC; chưa triển khai."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Quỹ Mở (Programmatic CCQ)",
        "Quỹ Đầu Tư Cổ Phiếu Cổ Tức VinaCapital (VDEF)", "/tai-chinh/chung-chi-quy/vdef",
        "Chưa triển khai", "Trang thông tin quỹ mở VDEF; chưa triển khai."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Trang Con Quỹ Mở (Programmatic CCQ)",
        "Quỹ Đầu Tư Cổ Phiếu Kinh Tế Hiện Đại VinaCapital (VMEEF)", "/tai-chinh/chung-chi-quy/vmeef",
        "Chưa triển khai", "Trang thông tin quỹ mở VMEEF; chưa triển khai."
    ],
    # C. Cụm Content Engine Always-on (In Progress)
    [
        "Phase 2", "Tháng 10/2026", "Trang Danh Mục Blog (Blog Listing)",
        "Cẩm Nang Tài Chính Cá Nhân & Đầu Tư MoMo", "/tai-chinh/blog",
        "In Progress", "Đang vận hành và xuất bản bài viết cẩm nang kiến thức tài chính cá nhân."
    ],
    [
        "Phase 2", "Tháng 10/2026", "Kho Bài Viết Chi Tiết (Blog Details)",
        "Kho 100 Bài Viết Chi Tiết Chuẩn SEO & GEO (50 T9 + 50 T10)", "/tai-chinh/blog/[slug]",
        "In Progress", "Đang duy trì nhịp độ sản xuất 5 bài/ngày chuẩn E-E-A-T vào Blog Hub."
    ],

    # =========================================================================
    # PHASE 3: THÁNG 11/2026 - MỞ RỘNG THUẾ, CHỨNG KHOÁN VN30 & pSEO 34 BANK (75 URLs)
    # =========================================================================
    # A. Tiện Ích Thuế & Kế Hoạch Tài Chính (Planned)
    [
        "Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Tính Thuế Thu Nhập Cá Nhân & Giảm Trừ Gia Cảnh 2026", "/tai-chinh/thue-thu-nhap-ca-nhan",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Tool tính thuế TNCN 7 bậc và tra cứu giảm trừ gia cảnh 2026."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Tính Thuế Hộ Kinh Doanh Cá Thể & Lệ Phí Môn Bài", "/tai-chinh/thue-ho-kinh-doanh",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Tool tính thuế khoán, thuế kê khai và lệ phí môn bài TT40/2021."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Cổng Tra Cứu & Xác Thực Mã Số Thuế Cá Nhân", "/tai-chinh/ma-so-thue",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Tiện ích tra cứu MST cá nhân và thông tin người nộp thuế."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Gửi Tiết Kiệm Online MoMo & Lãi Suất Ưu Đãi Đối Tác", "/tai-chinh/gui-tiet-kiem",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Tích hợp cổng mở sổ tiết kiệm online (+0.2% lãi suất đối tác)."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Quản Lý Dòng Tiền Tự Do & Quỹ Dự Phòng Khẩn Cấp", "/tai-chinh/dong-tien",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Tool tính Free Cash Flow và quy mô quỹ dự phòng rủi ro 3-6 tháng."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Bộ Giả Lập Tự Do Tài Chính & Tích Sản FIRE", "/tai-chinh/tu-do-tai-chinh",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Tool lập kế hoạch FIRE theo quy tắc rút 4% an toàn."
    ],
    # B. Cụm Chứng Khoán & 30 Dynamic Profiles VN30 (Pending Chờ Cell Team CVS)
    [
        "Phase 3", "Tháng 11/2026", "Trang Dịch Vụ Under /tai-chinh",
        "Cổng Master Chứng Khoán & Tích Sản Cổ Phiếu Lô Lẻ Từ 10.000đ", "/tai-chinh/chung-khoan",
        "Pending", "URL gốc /chung-khoan đang live độc lập tại root; kế hoạch chuyển sang /tai-chinh/chung-khoan đang pending phản hồi nghiệp vụ từ Cell Team CVS / FinHub BU."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Chi Tiết (Programmatic Spoke)",
        "Hệ Thống Dynamic Profile 30 Mã VN30 ([Mã Cổ Phiếu])", "/tai-chinh/chung-khoan/[ticker]",
        "Pending", "Master template cho 30 mã VN30; pending phản hồi nghiệp vụ từ Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích Under /tai-chinh",
        "Bảng Theo Dõi Lịch Cổ Tức Tiền Mặt Doanh Nghiệp", "/tai-chinh/chung-khoan/lich-co-tuc",
        "Pending", "Tiện ích theo dõi lịch trả cổ tức tiền mặt doanh nghiệp niêm yết; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu FPT - CTCP FPT", "/tai-chinh/chung-khoan/fpt",
        "Pending", "Dynamic Profile cổ phiếu FPT; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu VNM - CTCP Sữa Việt Nam (Vinamilk)", "/tai-chinh/chung-khoan/vnm",
        "Pending", "Dynamic Profile cổ phiếu VNM; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu HPG - Tập Đoàn Hòa Phát", "/tai-chinh/chung-khoan/hpg",
        "Pending", "Dynamic Profile cổ phiếu HPG; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu VCB - Ngân Hàng TMCP Ngoại Thương Việt Nam", "/tai-chinh/chung-khoan/vcb",
        "Pending", "Dynamic Profile cổ phiếu VCB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu MWG - CTCP Đầu Tư Thế Giới Di Động", "/tai-chinh/chung-khoan/mwg",
        "Pending", "Dynamic Profile cổ phiếu MWG; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu TCB - Ngân Hàng TMCP Kỹ Thương Việt Nam", "/tai-chinh/chung-khoan/tcb",
        "Pending", "Dynamic Profile cổ phiếu TCB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu MBB - Ngân Hàng TMCP Quân Đội", "/tai-chinh/chung-khoan/mbb",
        "Pending", "Dynamic Profile cổ phiếu MBB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu ACB - Ngân Hàng TMCP Á Châu", "/tai-chinh/chung-khoan/acb",
        "Pending", "Dynamic Profile cổ phiếu ACB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu BID - Ngân Hàng TMCP Đầu Tư & Phát Triển Việt Nam", "/tai-chinh/chung-khoan/bid",
        "Pending", "Dynamic Profile cổ phiếu BID; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu CTG - Ngân Hàng TMCP Công Thương Việt Nam", "/tai-chinh/chung-khoan/ctg",
        "Pending", "Dynamic Profile cổ phiếu CTG; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu STB - Ngân Hàng TMCP Sài Gòn Thương Tín", "/tai-chinh/chung-khoan/stb",
        "Pending", "Dynamic Profile cổ phiếu STB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu VPB - Ngân Hàng TMCP Việt Nam Thịnh Vượng", "/tai-chinh/chung-khoan/vpb",
        "Pending", "Dynamic Profile cổ phiếu VPB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu TPB - Ngân Hàng TMCP Tiên Phong", "/tai-chinh/chung-khoan/tpb",
        "Pending", "Dynamic Profile cổ phiếu TPB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu HDB - Ngân Hàng TMCP Phát Triển TP.HCM", "/tai-chinh/chung-khoan/hdb",
        "Pending", "Dynamic Profile cổ phiếu HDB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu VIB - Ngân Hàng TMCP Quốc Tế Việt Nam", "/tai-chinh/chung-khoan/vib",
        "Pending", "Dynamic Profile cổ phiếu VIB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu SHB - Ngân Hàng TMCP Sài Gòn - Hà Nội", "/tai-chinh/chung-khoan/shb",
        "Pending", "Dynamic Profile cổ phiếu SHB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu SSB - Ngân Hàng TMCP Đông Nam Á (SeABank)", "/tai-chinh/chung-khoan/ssb",
        "Pending", "Dynamic Profile cổ phiếu SSB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu SSI - CTCP Chứng Khoán SSI", "/tai-chinh/chung-khoan/ssi",
        "Pending", "Dynamic Profile cổ phiếu SSI; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu PLX - Tập Đoàn Xăng Dầu Việt Nam (Petrolimex)", "/tai-chinh/chung-khoan/plx",
        "Pending", "Dynamic Profile cổ phiếu PLX; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu POW - Tổng Công Ty Điện Lực Dầu Khí Việt Nam", "/tai-chinh/chung-khoan/pow",
        "Pending", "Dynamic Profile cổ phiếu POW; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu SAB - Tổng CTCP Bia - Rượu - Nước Giải Khát Sài Gòn", "/tai-chinh/chung-khoan/sab",
        "Pending", "Dynamic Profile cổ phiếu SAB; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu BVH - Tập Đoàn Bảo Việt", "/tai-chinh/chung-khoan/bvh",
        "Pending", "Dynamic Profile cổ phiếu BVH; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu BCM - Tổng Công Ty Đầu Tư & Phát Triển Công Nghiệp", "/tai-chinh/chung-khoan/bcm",
        "Pending", "Dynamic Profile cổ phiếu BCM; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu GVR - Tập Đoàn Công Nghiệp Cao Su Việt Nam", "/tai-chinh/chung-khoan/gvr",
        "Pending", "Dynamic Profile cổ phiếu GVR; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu VJC - CTCP Hàng Không Vietjet", "/tai-chinh/chung-khoan/vjc",
        "Pending", "Dynamic Profile cổ phiếu VJC; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu MSN - CTCP Tập Đoàn Masan", "/tai-chinh/chung-khoan/msn",
        "Pending", "Dynamic Profile cổ phiếu MSN; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu VIC - Tập Đoàn Vingroup", "/tai-chinh/chung-khoan/vic",
        "Pending", "Dynamic Profile cổ phiếu VIC; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu VHM - CTCP Vinhomes", "/tai-chinh/chung-khoan/vhm",
        "Pending", "Dynamic Profile cổ phiếu VHM; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu VRE - CTCP Vincom Retail", "/tai-chinh/chung-khoan/vre",
        "Pending", "Dynamic Profile cổ phiếu VRE; pending Cell Team CVS."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Cổ Phiếu (Programmatic VN30)",
        "Cổ Phiếu GAS - Tổng Công Ty Khí Việt Nam", "/tai-chinh/chung-khoan/gas",
        "Pending", "Dynamic Profile cổ phiếu GAS; pending Cell Team CVS."
    ],
    # C. Cụm Danh Bạ 34 Ngân Hàng pSEO (Planned)
    [
        "Phase 3", "Tháng 11/2026", "Cổng Danh Mục Master",
        "Danh Bạ 34 Ngân Hàng Việt Nam (Lãi Suất & Hotline)", "/tai-chinh/ngan-hang",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Cổng danh bạ tổng hợp mạng lưới 34 ngân hàng."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Chi Tiết (Programmatic Spoke)",
        "Hệ Thống Trang Chi Tiết 34 Ngân Hàng Đối Tác ([Tên Ngân Hàng])", "/tai-chinh/ngan-hang/[bank-slug]",
        "Planned", "Master template Programmatic SEO cho 34 ngân hàng chi tiết."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "VietinBank - Ngân Hàng TMCP Công Thương Việt Nam", "/tai-chinh/ngan-hang/vietinbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng VietinBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Vietcombank - Ngân Hàng TMCP Ngoại Thương Việt Nam", "/tai-chinh/ngan-hang/vietcombank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Vietcombank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Techcombank - Ngân Hàng TMCP Kỹ Thương Việt Nam", "/tai-chinh/ngan-hang/techcombank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Techcombank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Nam A Bank - Ngân Hàng TMCP Nam Á", "/tai-chinh/ngan-hang/nam-a-bank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Nam A Bank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "VPBank - Ngân Hàng TMCP Việt Nam Thịnh Vượng", "/tai-chinh/ngan-hang/vpbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng VPBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Agribank - Ngân Hàng Nông Nghiệp & PTNT Việt Nam", "/tai-chinh/ngan-hang/agribank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Agribank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "MBBank - Ngân Hàng TMCP Quân Đội", "/tai-chinh/ngan-hang/mbbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng MBBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "VRB - Ngân Hàng Liên Doanh Việt - Nga", "/tai-chinh/ngan-hang/vrb",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng VRB."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "ACB - Ngân Hàng TMCP Á Châu", "/tai-chinh/ngan-hang/acb",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng ACB."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "BIDV - Ngân Hàng TMCP Đầu Tư & Phát Triển Việt Nam", "/tai-chinh/ngan-hang/bidv",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng BIDV."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "MSB - Ngân Hàng TMCP Hàng Hải Việt Nam", "/tai-chinh/ngan-hang/msb",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng MSB."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "TPBank - Ngân Hàng TMCP Tiên Phong", "/tai-chinh/ngan-hang/tpbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng TPBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "SCB - Ngân Hàng TMCP Sài Gòn", "/tai-chinh/ngan-hang/scb",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng SCB."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "SHB - Ngân Hàng TMCP Sài Gòn - Hà Nội", "/tai-chinh/ngan-hang/shb",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng SHB."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Sacombank - Ngân Hàng TMCP Sài Gòn Thương Tín", "/tai-chinh/ngan-hang/sacombank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Sacombank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "ABBank - Ngân Hàng TMCP An Bình", "/tai-chinh/ngan-hang/abbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng ABBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "OCB - Ngân Hàng TMCP Phương Đông", "/tai-chinh/ngan-hang/ocb",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng OCB."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Shinhan Bank - Ngân Hàng TNHH MTV Shinhan Việt Nam", "/tai-chinh/ngan-hang/shinhan-bank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Shinhan Bank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "NCB - Ngân Hàng TMCP Quốc Dân", "/tai-chinh/ngan-hang/ncb",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng NCB."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Bản Việt (BVBank) - Ngân Hàng TMCP Bản Việt", "/tai-chinh/ngan-hang/bvbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Bản Việt."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "SeABank - Ngân Hàng TMCP Đông Nam Á", "/tai-chinh/ngan-hang/seabank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng SeABank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Eximbank - Ngân Hàng TMCP Xuất Nhập Khẩu Việt Nam", "/tai-chinh/ngan-hang/eximbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Eximbank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "VIB - Ngân Hàng TMCP Quốc Tế Việt Nam", "/tai-chinh/ngan-hang/vib",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng VIB."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "HDBank - Ngân Hàng TMCP Phát Triển TP.HCM", "/tai-chinh/ngan-hang/hdbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng HDBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "VietBank - Ngân Hàng TMCP Việt Nam Thương Tín", "/tai-chinh/ngan-hang/vietbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng VietBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "PVcomBank - Ngân Hàng TMCP Đại Chúng Việt Nam", "/tai-chinh/ngan-hang/pvcombank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng PVcomBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "DongA Bank - Ngân Hàng TMCP Đông Á", "/tai-chinh/ngan-hang/donga-bank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng DongA Bank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Bac A Bank - Ngân Hàng TMCP Bắc Á", "/tai-chinh/ngan-hang/bac-a-bank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Bac A Bank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "LPBank - Ngân Hàng TMCP Lộc Phát Việt Nam", "/tai-chinh/ngan-hang/lpbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng LPBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "KienlongBank - Ngân Hàng TMCP Kiên Long", "/tai-chinh/ngan-hang/kienlongbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng KienlongBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "BaoViet Bank - Ngân Hàng TMCP Bảo Việt", "/tai-chinh/ngan-hang/baovietbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng BaoViet Bank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Indovina Bank - Ngân Hàng TNHH Indovina (IVB)", "/tai-chinh/ngan-hang/indovina-bank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Indovina Bank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "OceanBank - Ngân Hàng Thương Mại TNHH MTV Đại Dương", "/tai-chinh/ngan-hang/oceanbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng OceanBank."
    ],
    [
        "Phase 3", "Tháng 11/2026", "Trang Con Ngân Hàng (Programmatic Bank)",
        "Saigonbank - Ngân Hàng TMCP Sài Gòn Công Thương", "/tai-chinh/ngan-hang/saigonbank",
        "Planned", "Kế hoạch Go-live Tháng 11/2026. Subpage ngân hàng Saigonbank."
    ]
]


def get_access_token():
    with open(CREDS_FILE, "r", encoding="utf-8") as f:
        cdata = json.load(f)
    client_info = cdata.get("installed") or cdata.get("web")

    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        tdata = json.load(f)

    data = urllib.parse.urlencode({
        "client_id": client_info["client_id"],
        "client_secret": client_info["client_secret"],
        "refresh_token": tdata["refresh_token"],
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data, method="POST")
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        return res["access_token"]


def batch_update_spreadsheet(token, requests):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}:batchUpdate"
    body = json.dumps({"requests": requests}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def clear_range(token, range_name):
    encoded_range = urllib.parse.quote(range_name)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{encoded_range}:clear"
    req = urllib.request.Request(
        url,
        data=b"{}",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def update_values(token, range_name, values):
    encoded_range = urllib.parse.quote(range_name)
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{encoded_range}?valueInputOption=USER_ENTERED"
    body = json.dumps({"values": values}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def rebuild_local_excel():
    print(f"1. Updating local Excel workbook: {EXCEL_PATH}")
    wb = openpyxl.load_workbook(EXCEL_PATH)

    # A. Update Roadmap item 12 status: "Chưa triển khai"
    ws_r = wb["Roadmap"]
    for r in range(2, ws_r.max_row + 1):
        if "7 Trang Standalone" in str(ws_r.cell(r, 4).value or ""):
            ws_r.cell(r, 6, "Chưa triển khai")
            ws_r.cell(r, 6).fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
            ws_r.cell(r, 6).font = Font(name="Arial", size=9.5, bold=True, color="475569")
            print("Updated Roadmap item 12 status to 'Chưa triển khai' in local Excel!")
            break

    # B. Rebuild Sheet: Sitemap
    if "Sitemap" in wb.sheetnames:
        del wb["Sitemap"]
    ws_s = wb.create_sheet("Sitemap", index=3)

    font_header = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    fill_header = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")

    font_default = Font(name="Arial", size=9.5, color="1E293B")
    font_bold = Font(name="Arial", size=9.5, bold=True, color="1E293B")

    border_thin = Border(
        left=Side(style="thin", color="CBD5E1"),
        right=Side(style="thin", color="CBD5E1"),
        top=Side(style="thin", color="CBD5E1"),
        bottom=Side(style="thin", color="CBD5E1")
    )

    fill_done = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
    font_done = Font(name="Arial", size=9.5, bold=True, color="15803D")

    fill_progress = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
    font_progress = Font(name="Arial", size=9.5, bold=True, color="B45309")

    fill_pending = PatternFill(start_color="FFE4E6", end_color="FFE4E6", fill_type="solid")
    font_pending = Font(name="Arial", size=9.5, bold=True, color="BE123C")

    fill_planned = PatternFill(start_color="E0E7FF", end_color="E0E7FF", fill_type="solid")
    font_planned = Font(name="Arial", size=9.5, bold=True, color="4338CA")

    fill_not_started = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    font_not_started = Font(name="Arial", size=9.5, bold=True, color="475569")

    # Header row
    for c_idx, h in enumerate(SITEMAP_HEADER, 1):
        cell = ws_s.cell(1, c_idx, h)
        cell.font = font_header
        cell.fill = fill_header
        cell.border = border_thin
        align_h = "center" if c_idx in [1, 2, 3, 7] else "left"
        cell.alignment = Alignment(horizontal=align_h, vertical="center")
    ws_s.row_dimensions[1].height = 26

    # Data rows
    for r_idx, item in enumerate(SITEMAP_ITEMS, 2):
        stt = r_idx - 1
        row_vals = [stt] + item
        for c_idx, val in enumerate(row_vals, 1):
            cell = ws_s.cell(r_idx, c_idx, val)
            cell.border = border_thin

            align_h = "center" if c_idx in [1, 2, 3, 7] else "left"
            wrap = True if c_idx in [5, 8] else False
            cell.alignment = Alignment(horizontal=align_h, vertical="center", wrap_text=wrap)

            if c_idx in [5, 6]:
                cell.font = font_bold
            elif c_idx == 7:  # Status column
                if val == "Done":
                    cell.fill = fill_done
                    cell.font = font_done
                elif val == "In Progress":
                    cell.fill = fill_progress
                    cell.font = font_progress
                elif val == "Pending":
                    cell.fill = fill_pending
                    cell.font = font_pending
                elif val == "Chưa triển khai":
                    cell.fill = fill_not_started
                    cell.font = font_not_started
                else:  # Planned
                    cell.fill = fill_planned
                    cell.font = font_planned
            else:
                cell.font = font_default

        ws_s.row_dimensions[r_idx].height = 24

    # Column widths
    col_widths = {1: 8, 2: 14, 3: 15, 4: 26, 5: 38, 6: 34, 7: 16, 8: 52}
    for col_idx, width in col_widths.items():
        ws_s.column_dimensions[get_column_letter(col_idx)].width = width

    ws_s.freeze_panes = "A2"
    wb.save(EXCEL_PATH)
    print("Local Excel workbook updated successfully! Total rows in Sitemap:", len(SITEMAP_ITEMS) + 1)


def rebuild_google_sheets():
    print("2. Updating Google Sheets...")
    token = get_access_token()

    url_meta = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets(properties)"
    req_meta = urllib.request.Request(url_meta, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req_meta) as resp:
        meta = json.loads(resp.read().decode("utf-8"))

    sheet_map = {s["properties"]["title"]: s["properties"]["sheetId"] for s in meta["sheets"]}
    roadmap_id = sheet_map.get("Product Roadmap")
    sitemap_id = sheet_map.get("Sitemap")

    # A. Update Roadmap item 12 status to "Chưa triển khai" on Google Sheets
    update_values(token, "Product Roadmap!F13", [["Chưa triển khai"]])
    req_rm = [{
        "repeatCell": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 12,
                "endRowIndex": 13,
                "startColumnIndex": 5,
                "endColumnIndex": 6
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.945, "green": 0.96, "blue": 0.976},  # slate 100
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 10,
                        "bold": True,
                        "foregroundColor": {"red": 0.28, "green": 0.33, "blue": 0.41}   # slate 600
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
        }
    }]
    batch_update_spreadsheet(token, req_rm)
    print("Updated Roadmap item 12 status to 'Chưa triển khai' on Google Sheets!")

    # B. Rebuild Tab: Sitemap
    print("Clearing and rebuilding Google Sheet Tab: Sitemap...")
    clear_range(token, "Sitemap!A1:H200")

    full_table = [SITEMAP_HEADER] + [[idx + 1] + item for idx, item in enumerate(SITEMAP_ITEMS)]
    num_rows = len(full_table)
    num_cols = len(SITEMAP_HEADER)

    update_values(token, f"Sitemap!A1:H{num_rows}", full_table)

    reqs_s = []
    # Grid properties
    reqs_s.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": sitemap_id,
                "gridProperties": {
                    "frozenRowCount": 1,
                    "rowCount": max(150, num_rows + 10),
                    "columnCount": 10
                }
            },
            "fields": "gridProperties(frozenRowCount,rowCount,columnCount)"
        }
    })

    # Column widths: STT (60), Phase (100), Time (110), Type (200), Title (280), URL (260), Status (120), Note (450)
    col_widths = [60, 100, 110, 200, 280, 260, 120, 450]
    for c_idx, w in enumerate(col_widths):
        reqs_s.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sitemap_id,
                    "dimension": "COLUMNS",
                    "startIndex": c_idx,
                    "endIndex": c_idx + 1
                },
                "properties": {"pixelSize": w},
                "fields": "pixelSize"
            }
        })

    # Header Row 1 formatting
    reqs_s.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.12, "green": 0.31, "blue": 0.47},
                    "horizontalAlignment": "LEFT",
                    "verticalAlignment": "MIDDLE",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 10,
                        "bold": True,
                        "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0}
                    }
                }
            },
            "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
        }
    })
    for c_idx in [0, 1, 2, 6]:
        reqs_s.append({
            "repeatCell": {
                "range": {
                    "sheetId": sitemap_id,
                    "startRowIndex": 0,
                    "endRowIndex": 1,
                    "startColumnIndex": c_idx,
                    "endColumnIndex": c_idx + 1
                },
                "cell": {"userEnteredFormat": {"horizontalAlignment": "CENTER"}},
                "fields": "userEnteredFormat.horizontalAlignment"
            }
        })

    # Data rows basic formatting
    reqs_s.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 1,
                "endRowIndex": num_rows,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols
            },
            "cell": {
                "userEnteredFormat": {
                    "verticalAlignment": "MIDDLE",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 10,
                        "foregroundColor": {"red": 0.12, "green": 0.16, "blue": 0.23}
                    }
                }
            },
            "fields": "userEnteredFormat(verticalAlignment,textFormat)"
        }
    })

    # Zebra striping
    for r_idx in range(1, num_rows):
        bg = {"red": 0.97, "green": 0.98, "blue": 0.99} if r_idx % 2 == 1 else {"red": 1.0, "green": 1.0, "blue": 1.0}
        reqs_s.append({
            "repeatCell": {
                "range": {
                    "sheetId": sitemap_id,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 6
                },
                "cell": {"userEnteredFormat": {"backgroundColor": bg}},
                "fields": "userEnteredFormat.backgroundColor"
            }
        })
        reqs_s.append({
            "repeatCell": {
                "range": {
                    "sheetId": sitemap_id,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 7,
                    "endColumnIndex": 8
                },
                "cell": {"userEnteredFormat": {"backgroundColor": bg}},
                "fields": "userEnteredFormat.backgroundColor"
            }
        })

    # Alignment
    for c_idx in [0, 1, 2]:
        reqs_s.append({
            "repeatCell": {
                "range": {
                    "sheetId": sitemap_id,
                    "startRowIndex": 1,
                    "endRowIndex": num_rows,
                    "startColumnIndex": c_idx,
                    "endColumnIndex": c_idx + 1
                },
                "cell": {"userEnteredFormat": {"horizontalAlignment": "CENTER"}},
                "fields": "userEnteredFormat.horizontalAlignment"
            }
        })
    reqs_s.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 1,
                "endRowIndex": num_rows,
                "startColumnIndex": 4,
                "endColumnIndex": 5
            },
            "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
            "fields": "userEnteredFormat.textFormat.bold"
        }
    })
    reqs_s.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 1,
                "endRowIndex": num_rows,
                "startColumnIndex": 7,
                "endColumnIndex": 8
            },
            "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP"}},
            "fields": "userEnteredFormat.wrapStrategy"
        }
    })

    # Status Badges
    for r_idx in range(1, num_rows):
        st = full_table[r_idx][6]
        if st == "Done":
            bg = {"red": 0.86, "green": 0.98, "blue": 0.90}
            fg = {"red": 0.08, "green": 0.50, "blue": 0.24}
        elif st == "In Progress":
            bg = {"red": 0.99, "green": 0.95, "blue": 0.78}
            fg = {"red": 0.71, "green": 0.33, "blue": 0.04}
        elif st == "Pending":
            bg = {"red": 1.0, "green": 0.89, "blue": 0.90}
            fg = {"red": 0.75, "green": 0.07, "blue": 0.24}
        elif st == "Chưa triển khai":
            bg = {"red": 0.945, "green": 0.96, "blue": 0.976}
            fg = {"red": 0.28, "green": 0.33, "blue": 0.41}
        else:  # Planned
            bg = {"red": 0.88, "green": 0.91, "blue": 1.0}
            fg = {"red": 0.26, "green": 0.22, "blue": 0.79}

        reqs_s.append({
            "repeatCell": {
                "range": {
                    "sheetId": sitemap_id,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 6,
                    "endColumnIndex": 7
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": bg,
                        "horizontalAlignment": "CENTER",
                        "verticalAlignment": "MIDDLE",
                        "textFormat": {
                            "fontFamily": "Arial",
                            "fontSize": 10,
                            "bold": True,
                            "foregroundColor": fg
                        }
                    }
                },
                "fields": "userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
            }
        })

    # Borders
    border_style = {"style": "SOLID", "width": 1, "color": {"red": 0.85, "green": 0.88, "blue": 0.92}}
    reqs_s.append({
        "updateBorders": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 0,
                "endRowIndex": num_rows,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols
            },
            "top": border_style, "bottom": border_style, "left": border_style, "right": border_style,
            "innerHorizontal": border_style, "innerVertical": border_style
        }
    })

    batch_update_spreadsheet(token, reqs_s)
    print("Google Sheet Tab: Sitemap rebuilt and formatted successfully!")


def update_brd_file():
    print("3. Updating 05_HUBS/financial/financial-hub-brd.md...")
    content = BRD_PATH.read_text(encoding="utf-8")

    # Update row in Section 10 for Standalone migration from In Progress to Chưa triển khai
    old_target = """      <td style="border:1px solid #94a3b8; padding:6px; font-weight:700;">Di Chuyển & 301 Redirect 7 Trang Standalone</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Lập bảng mapping và rule Edge CDN 301 Redirect cho 7 trang standalone về /tai-chinh/* (/nhan-tien-quoc-te, /quy-nhom, /thanh-toan-the-tin-dung, /quan-ly-chi-tieu, /chung-khoan, /chung-chi-quy, /tui-sinh-loi). Cam kết giữ nguyên URL root CreditTech.</td>
      <td style="border:1px solid #94a3b8; padding:6px; color:#b45309; background-color:#fef9c3; font-weight:700; text-align:center;">In Progress</td>"""

    new_target = """      <td style="border:1px solid #94a3b8; padding:6px; font-weight:700;">Di Chuyển & 301 Redirect 7 Trang Standalone</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Lập bảng mapping và rule Edge CDN 301 Redirect cho 7 trang standalone về /tai-chinh/* (/nhan-tien-quoc-te, /quy-nhom, /thanh-toan-the-tin-dung, /quan-ly-chi-tieu, /chung-khoan, /chung-chi-quy, /tui-sinh-loi). Cam kết giữ nguyên URL root CreditTech. Hiện trạng chưa triển khai di chuyển.</td>
      <td style="border:1px solid #94a3b8; padding:6px; color:#475569; background-color:#f1f5f9; font-weight:700; text-align:center;">Chưa triển khai</td>"""

    if old_target in content:
        content = content.replace(old_target, new_target)
        BRD_PATH.write_text(content, encoding="utf-8")
        print("Updated BRD Section 10 for Standalone migration!")
    else:
        print("Note: old target not directly matched, checked Section 10 table.")


def main():
    rebuild_local_excel()
    rebuild_google_sheets()
    update_brd_file()
    print("\nAll Sitemap rewrite tasks completed successfully!")


if __name__ == "__main__":
    main()
