#!/usr/bin/env python3
"""
Sync CCQ to Phase 3 (November 2026) and realign Phase timeline:
1. Local Excel: 05_HUBS/financial/financial-hub-roadmap.xlsx (Sheets: Roadmap, Sitemap)
2. Google Sheets: 1_AG4otSTXH7ontpPL0zjylYgVfxOozvoSc5PziUPM6A (Tabs: Product Roadmap, Sitemap)
3. BRD: 05_HUBS/financial/financial-hub-brd.md (Section 10)
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

# =========================================================================
# RESTRUCTURED ROADMAP DATA (22 items)
# =========================================================================
NEW_ROADMAP_DATA = [
    ["Giai Đoạn (Phase)", "Thời Gian", "Cụm Sản Phẩm (Track)", "Tên Tính Năng / Sản Phẩm", "Mô Tả Công Cụ & Sub-Pages Trong Sitemap", "Trạng Thái"],
    # PHASE 0
    ["Phase 0", "Tháng 7/2026", "Tín Dụng & Tiêu Dùng", "Ví Trả Sau (/vi-tra-sau)",
     "Tool tính trả góp Ví Trả Sau. Nhập giá trị món hàng và kỳ hạn (3 - 12 tháng) để xem số tiền thanh toán mỗi tháng, phí chuyển đổi và so sánh phương án miễn lãi 45 ngày. Giữ nguyên URL root độc lập.", "Done"],
    ["Phase 0", "Tháng 7/2026", "Tín Dụng & Cho Vay", "Vay Nhanh (/vay-nhanh)",
     "Tool tính lịch trả nợ vay tiêu dùng. Nhập số tiền vay (5 - 100 triệu) và kỳ hạn (6 - 48 tháng) để tính số tiền trả hàng tháng theo dư nợ giảm dần, chi tiết tiền gốc, tiền lãi và tổng lãi thực tế. Giữ nguyên URL root độc lập.", "Done"],
    # PHASE 1 (Tháng 8/2026)
    ["Phase 1", "Tháng 8/2026", "Master Gateway", "Financial Hub (/tai-chinh)",
     "Cổng trung tâm điều hướng dịch vụ tài chính Kênh Web theo 4 trụ cột (Tín Dụng, Tích Lũy, Đầu Tư, Chi Tiêu). Đã triển khai Mega Menu Header responsive toàn cục.", "Done"],
    ["Phase 1", "Tháng 8/2026", "Sức Khỏe Tín Dụng", "Điểm Tín Dụng (/diem-tin-dung)",
     "Tool tự đánh giá điểm tín dụng CIC (thang điểm 150 - 750), xếp hạng nhóm nợ 1-5 và nhận gợi ý cải thiện hồ sơ vay. Giữ nguyên URL root độc lập.", "Done"],
    ["Phase 1", "Tháng 8/2026", "Đầu Tư & Vàng", "Bảng Giá Vàng (/tai-chinh/gia-vang)",
     "Bảng tra cứu giá vàng trực tuyến (SJC, DOJI, PNJ, nhẫn trơn 9999) theo thời gian thực kèm biểu đồ lịch sử và tool quy đổi chỉ, lượng ra tiền mặt.", "Done"],
    ["Phase 1", "Tháng 8/2026", "Thu Nhập & Lao Động", "Tính Lương Gross - Net (/tai-chinh/tinh-luong)",
     "Tool tính lương Net từ lương Gross (tự động khấu trừ 10.5% bảo hiểm bắt buộc và thuế TNCN lũy tiến 7 bậc 2026 trên cùng một giao diện, kèm tính năng chuyển đổi ngược lại).", "Done"],
    ["Phase 1", "Tháng 8/2026", "Hưu Trí & Lao Động", "Dự Toán Lương Hưu & BHXH (/tai-chinh/luong-huu)",
     "Tool dự toán lương hưu và tuổi nghỉ hưu theo lộ trình luật mới, tích hợp tiện ích tính tiền trợ cấp một lần (tích hợp trực tiếp trong trang Lương Hưu, không tạo URL bảo hiểm độc lập).", "Done"],
    # PHASE 1 (Tháng 9/2026)
    ["Phase 1", "Tháng 9/2026", "Tiền Tệ & Ngoại Hối", "Cổng Tỷ Giá Master (/tai-chinh/ty-gia)",
     "Đã Go-live: Cổng tra cứu tỷ giá thị trường và tool quy đổi ngoại tệ (30+ đồng tiền từ 20+ ngân hàng).", "Done"],
    ["Phase 1", "Tháng 9/2026", "Tiền Tệ & Ngoại Hối", "5 Sub-pages Tỷ Giá Cặp Tiền",
     "Đã Go-live 5 cặp tiền tệ phổ biến nhất: USD/VND, EUR/VND, JPY/VND, GBP/VND, CNY/VND kèm tool đổi tiền trực tiếp, bảng tỷ giá đa ngân hàng và biểu đồ biến động.", "Done"],
    ["Phase 1", "Tháng 9/2026", "Quản Lý Chi Tiêu", "Phân Bổ Lương 50/30/20 (/tai-chinh/phan-bo-luong)",
     "Đã Go-live: Tool lập ngân sách chi tiêu và chia hũ tiền lương theo quy tắc 50/30/20 và mô hình 6 Hũ tài chính, kết nối Hũ Chi Tiêu in-app.", "Done"],
    ["Phase 1", "Tháng 9/2026", "Tiết Kiệm & Lãi Suất", "Bảng Lãi Suất 40 Ngân Hàng (/tai-chinh/lai-suat)",
     "Đã Go-live: Bảng tra cứu lãi suất 40 ngân hàng toàn cảnh thị trường và công cụ tính lãi gửi tiết kiệm theo số tiền, tự động hiển thị ngân hàng có lãi suất tối ưu nhất.", "Done"],
    # PHASE 2 (Tháng 10/2026) - Hoàn thành 100%
    ["Phase 2", "Tháng 10/2026", "Tăng Trưởng Nội Dung", "Cỗ Máy Content Engine Always-on",
     "Đã hoàn thành Go-live: Cụm Blog Hub (/tai-chinh/blog) và hệ thống bài viết chi tiết (/tai-chinh/blog/[slug]), duy trì nhịp xuất bản chuẩn E-E-A-T nuôi dưỡng traffic tự nhiên.", "Done"],
    # PHASE 3 (Tháng 11/2026) - Current Active Sprint
    ["Phase 3", "Tháng 11/2026", "Đầu Tư & Tích Sản", "Chứng Chỉ Quỹ (/tai-chinh/chung-chi-quy)",
     "Đẩy qua Tháng 11/2026: Triển khai Cổng tra cứu giá NAV và công cụ đầu tư định kỳ từ 10.000đ/ngày. Go-live Phase 1 với dữ liệu danh mục tĩnh/bán tự động của 30 quỹ mở đối tác CVS, kết nối phễu mở tài khoản in-app theo định hướng đồng thuận.", "In Progress"],
    ["Phase 3", "Tháng 11/2026", "Thu Nhập & Thuế", "Thuế Thu Nhập Cá Nhân (/tai-chinh/thue-thu-nhap-ca-nhan)",
     "Tool tính thuế TNCN, tra cứu mức giảm trừ gia cảnh 2026 (bản thân 11tr/15.5tr, người phụ thuộc 4.4tr/6.2tr), giải đáp biểu thuế lũy tiến từng phần 7 bậc và công cụ tính hoàn thuế TNCN. Chuẩn hóa URL không viết tắt.", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Thu Nhập & Thuế", "Thuế Hộ Kinh Doanh (/tai-chinh/thue-ho-kinh-doanh)",
     "Bổ sung mới: Tool tính thuế khoán và thuế kê khai hộ kinh doanh cá thể theo Thông tư 40/2021/TT-BTC. Tự động tính thuế GTGT, thuế TNCN và lệ phí môn bài theo doanh thu và lĩnh vực (phân phối 1.5%, dịch vụ 7%, sản xuất 4.5%...), kết nối giải pháp tài khoản thanh toán và MoMo QR kinh doanh.", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Kiến Trúc & Tái Định Tuyến URL", "Di Chuyển & 301 Redirect 7 Trang Standalone",
     "Đẩy qua Tháng 11/2026: Lập bảng mapping và rule Edge CDN 301 Redirect cho các trang standalone về /tai-chinh/* (/nhan-tien-quoc-te, /quy-nhom, /thanh-toan-the-tin-dung, /quan-ly-chi-tieu, /chung-khoan, /chung-chi-quy, /tui-sinh-loi). Cam kết giữ nguyên URL root CreditTech. Hiện trạng chưa triển khai di chuyển.", "Not Started"],
    ["Phase 3", "Tháng 11/2026", "Đầu Tư & Cổ Phiếu", "Cổng Chứng Khoán Master & 30 Profiles VN30",
     "Xây dựng Cổng Master /tai-chinh/chung-khoan và 30 trang Dynamic Ticker Profile cho rổ VN30 (/tai-chinh/chung-khoan/[ticker]). Tích hợp máy tính Stock DCA Backtester và Thước đo Sức khỏe MoMo Stock Health Score 1-100 phục vụ tích sản cổ phiếu lô lẻ từ 10.000đ. Đang pending phản hồi nghiệp vụ từ Cell Team (FinHub BU / CVS), dời mốc Go-live sang Tháng 11/2026.", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Tiết Kiệm & Lãi Suất", "Gửi Tiết Kiệm Online (/tai-chinh/gui-tiet-kiem)",
     "Hoàn tất thẩm định API lãi suất tiền gửi ưu đãi đối tác (+0.2% Bản Việt, VPBank) và tích hợp cổng mở sổ online, so sánh gói gửi tiết kiệm sinh lời.", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Dòng Tiền & Tiêu Dùng", "Quản Lý Dòng Tiền & Quỹ Khẩn Cấp (/tai-chinh/dong-tien)",
     "Tool tính dòng tiền tự do (Free Cash Flow), quy mô quỹ dự phòng rủi ro cần có (3 - 6 tháng chi phí) và số tháng tài chính cầm cự nếu mất nguồn thu. Định tuyến trang /tai-chinh/dong-tien trong Sitemap.", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Tích Sản & Hưu Trí", "Đầu Tư & Tích Sản FIRE (/tai-chinh/tu-do-tai-chinh)",
     "Tool lập kế hoạch tự do tài chính và nghỉ hưu sớm. Tạo trang độc lập /tai-chinh/tu-do-tai-chinh trong Sitemap theo quy tắc rút 4% an toàn và lộ trình tích sản hàng tháng.", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Ngân Hàng & Đối Tác", "pSEO Cổng Danh Bạ 34 Ngân Hàng (/tai-chinh/ngan-hang/*)",
     "Đòn bẩy tăng trưởng 700K Traffic: Triển khai Programmatic SEO cho Cổng Danh bạ và 34 Sub-page ngân hàng chi tiết (/tai-chinh/ngan-hang/[bank-slug]), đánh chiếm dung lượng tìm kiếm 19.49M volume/tháng từ mạng lưới chi nhánh, hotline và mã ngân hàng.", "Planned"],
    # PHASE 4 (Tháng 12/2026)
    ["Phase 4", "Tháng 12/2026", "Chuyển Đổi Nâng Cao", "Trợ Lý MoMo AI Suggestion Engine",
     "Đòn bẩy tăng trưởng 1M Traffic: Triển khai engine gợi ý thông minh tính toán chênh lệch lợi suất thực (Net Yield Gap) nhúng trực tiếp vào các tiện ích tính toán, tự động gợi ý giải pháp tài chính MoMo tối ưu theo mức tiền người dùng nhập vào.", "Planned"]
]

# =========================================================================
# RESTRUCTURED SITEMAP DATA (116 items, 6 columns)
# =========================================================================
SITEMAP_HEADER = [
    "STT",
    "Giai Đoạn (Phase)",
    "Thời Gian",
    "Loại Trang",
    "Định Tuyến URL Chuẩn Hóa (Canonical URL)",
    "Trạng Thái"
]

SITEMAP_ROWS = [
    # -------------------------------------------------------------------------
    # PHASE 0: THÁNG 7/2026 (3 URLs - Done)
    # -------------------------------------------------------------------------
    ["Phase 0", "Tháng 7/2026", "Độc Lập Root", "/vi-tra-sau", "Done"],
    ["Phase 0", "Tháng 7/2026", "Độc Lập Root", "/vay-nhanh", "Done"],
    ["Phase 0", "Tháng 7/2026", "Độc Lập Root", "/the-tin-dung", "Done"],

    # -------------------------------------------------------------------------
    # PHASE 1: THÁNG 8/2026 (6 URLs - Done)
    # -------------------------------------------------------------------------
    ["Phase 1", "Tháng 8/2026", "Cổng Master Hub", "/tai-chinh", "Done"],
    ["Phase 1", "Tháng 8/2026", "Cổng Tiện Ích", "/tai-chinh/cong-cu", "Done"],
    ["Phase 1", "Tháng 8/2026", "Độc Lập Root", "/diem-tin-dung", "Done"],
    ["Phase 1", "Tháng 8/2026", "Công Cụ Tiện Ích", "/tai-chinh/gia-vang", "Done"],
    ["Phase 1", "Tháng 8/2026", "Công Cụ Tiện Ích", "/tai-chinh/tinh-luong", "Done"],
    ["Phase 1", "Tháng 8/2026", "Công Cụ Tiện Ích", "/tai-chinh/luong-huu", "Done"],

    # -------------------------------------------------------------------------
    # PHASE 1: THÁNG 9/2026 (12 URLs - Done)
    # -------------------------------------------------------------------------
    ["Phase 1", "Tháng 9/2026", "Cổng Danh Mục", "/tai-chinh/ty-gia", "Done"],
    ["Phase 1", "Tháng 9/2026", "Template Chi Tiết", "/tai-chinh/ty-gia/[pair-slug]", "Done"],
    ["Phase 1", "Tháng 9/2026", "Sub-page Cặp Tiền", "/tai-chinh/ty-gia/usd-vnd", "Done"],
    ["Phase 1", "Tháng 9/2026", "Sub-page Cặp Tiền", "/tai-chinh/ty-gia/eur-vnd", "Done"],
    ["Phase 1", "Tháng 9/2026", "Sub-page Cặp Tiền", "/tai-chinh/ty-gia/jpy-vnd", "Done"],
    ["Phase 1", "Tháng 9/2026", "Sub-page Cặp Tiền", "/tai-chinh/ty-gia/gbp-vnd", "Done"],
    ["Phase 1", "Tháng 9/2026", "Sub-page Cặp Tiền", "/tai-chinh/ty-gia/cny-vnd", "Done"],
    ["Phase 1", "Tháng 9/2026", "Sub-page Cặp Tiền", "/tai-chinh/ty-gia/krw-vnd", "Done"],
    ["Phase 1", "Tháng 9/2026", "Sub-page Cặp Tiền", "/tai-chinh/ty-gia/aud-vnd", "Done"],
    ["Phase 1", "Tháng 9/2026", "Sub-page Cặp Tiền", "/tai-chinh/ty-gia/sgd-vnd", "Done"],
    ["Phase 1", "Tháng 9/2026", "Công Cụ Tiện Ích", "/tai-chinh/phan-bo-luong", "Done"],
    ["Phase 1", "Tháng 9/2026", "Công Cụ Tiện Ích", "/tai-chinh/lai-suat", "Done"],

    # -------------------------------------------------------------------------
    # PHASE 2: THÁNG 10/2026 (2 URLs - Done)
    # -------------------------------------------------------------------------
    ["Phase 2", "Tháng 10/2026", "Danh Mục Blog", "/tai-chinh/blog", "Done"],
    ["Phase 2", "Tháng 10/2026", "Kho Bài Viết", "/tai-chinh/blog/[slug]", "Done"],

    # -------------------------------------------------------------------------
    # PHASE 3: THÁNG 11/2026 (CURRENT ACTIVE SPRINT - 93 URLs)
    # -------------------------------------------------------------------------
    # A. Cụm Chứng Chỉ Quỹ (Đẩy qua Tháng 11/2026 - In Progress / Planned)
    ["Phase 3", "Tháng 11/2026", "Trang Dịch Vụ", "/tai-chinh/chung-chi-quy", "In Progress"],
    ["Phase 3", "Tháng 11/2026", "Template Chi Tiết", "/tai-chinh/chung-chi-quy/[fund-slug]", "In Progress"],
    ["Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích", "/tai-chinh/chung-chi-quy/tich-san-dinh-ky", "In Progress"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Quỹ Mở", "/tai-chinh/chung-chi-quy/dcds", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Quỹ Mở", "/tai-chinh/chung-chi-quy/vesaf", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Quỹ Mở", "/tai-chinh/chung-chi-quy/veof", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Quỹ Mở", "/tai-chinh/chung-chi-quy/vcbf-mgf", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Quỹ Mở", "/tai-chinh/chung-chi-quy/vcbf-bcf", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Quỹ Mở", "/tai-chinh/chung-chi-quy/ssi-sca", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Quỹ Mở", "/tai-chinh/chung-chi-quy/bvbf", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Quỹ Mở", "/tai-chinh/chung-chi-quy/dcbc", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Quỹ Mở", "/tai-chinh/chung-chi-quy/vdef", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Quỹ Mở", "/tai-chinh/chung-chi-quy/vmeef", "Planned"],

    # B. Cụm Standalone Migration Chuyển Về /tai-chinh/* (Chưa triển khai)
    ["Phase 3", "Tháng 11/2026", "Trang Dịch Vụ", "/tai-chinh/tui-sinh-loi", "Not Started"],
    ["Phase 3", "Tháng 11/2026", "Trang Dịch Vụ", "/tai-chinh/nhan-tien-quoc-te", "Not Started"],
    ["Phase 3", "Tháng 11/2026", "Trang Dịch Vụ", "/tai-chinh/quy-nhom", "Not Started"],
    ["Phase 3", "Tháng 11/2026", "Trang Dịch Vụ", "/tai-chinh/thanh-toan-the-tin-dung", "Not Started"],
    ["Phase 3", "Tháng 11/2026", "Trang Dịch Vụ", "/tai-chinh/quan-ly-chi-tieu", "Not Started"],

    # C. Cụm Tiện Ích Thuế & Dòng Tiền (Planned)
    ["Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích", "/tai-chinh/thue-thu-nhap-ca-nhan", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích", "/tai-chinh/thue-ho-kinh-doanh", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích", "/tai-chinh/ma-so-thue", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích", "/tai-chinh/gui-tiet-kiem", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích", "/tai-chinh/dong-tien", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích", "/tai-chinh/tu-do-tai-chinh", "Planned"],

    # D. Cụm Chứng Khoán & 30 Profiles VN30 (Pending Chờ Cell Team CVS)
    ["Phase 3", "Tháng 11/2026", "Trang Dịch Vụ", "/tai-chinh/chung-khoan", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Template Chi Tiết", "/tai-chinh/chung-khoan/[ticker]", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Công Cụ Tiện Ích", "/tai-chinh/chung-khoan/lich-co-tuc", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/fpt", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/vnm", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/hpg", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/vcb", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/mwg", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/tcb", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/mbb", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/acb", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/bid", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/ctg", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/stb", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/vpb", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/tpb", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/hdb", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/vib", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/shb", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/ssb", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/ssi", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/plx", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/pow", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/sab", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/bvh", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/bcm", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/gvr", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/vjc", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/msn", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/vic", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/vhm", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/vre", "Pending"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Cổ Phiếu VN30", "/tai-chinh/chung-khoan/gas", "Pending"],

    # E. Cụm Danh Bạ 34 Ngân Hàng pSEO (Planned)
    ["Phase 3", "Tháng 11/2026", "Cổng Danh Bạ", "/tai-chinh/ngan-hang", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Template Chi Tiết", "/tai-chinh/ngan-hang/[bank-slug]", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/vietinbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/vietcombank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/techcombank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/nam-a-bank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/vpbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/agribank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/mbbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/vrb", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/acb", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/bidv", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/msb", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/tpbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/scb", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/shb", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/sacombank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/abbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/ocb", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/shinhan-bank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/ncb", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/bvbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/seabank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/eximbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/vib", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/hdbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/vietbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/pvcombank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/donga-bank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/bac-a-bank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/lpbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/kienlongbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/baovietbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/indovina-bank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/oceanbank", "Planned"],
    ["Phase 3", "Tháng 11/2026", "Sub-page Ngân Hàng", "/tai-chinh/ngan-hang/saigonbank", "Planned"]
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


def update_local_excel():
    print(f"1. Updating local Excel workbook: {EXCEL_PATH}")
    wb = openpyxl.load_workbook(EXCEL_PATH)

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

    # -------------------------------------------------------------
    # A. Rebuild Sheet: Roadmap
    # -------------------------------------------------------------
    if "Roadmap" in wb.sheetnames:
        del wb["Roadmap"]
    ws_r = wb.create_sheet("Roadmap", index=2)

    for r_idx, row_vals in enumerate(NEW_ROADMAP_DATA, 1):
        for c_idx, val in enumerate(row_vals, 1):
            cell = ws_r.cell(r_idx, c_idx, val)
            cell.border = border_thin

            if r_idx == 1:
                cell.font = font_header
                cell.fill = fill_header
                align_h = "center" if c_idx in [1, 2, 6] else "left"
                cell.alignment = Alignment(horizontal=align_h, vertical="center")
            else:
                align_h = "center" if c_idx in [1, 2, 6] else "left"
                wrap = True if c_idx == 5 else False
                cell.alignment = Alignment(horizontal=align_h, vertical="center", wrap_text=wrap)

                if c_idx in [3, 4]:
                    cell.font = font_bold
                elif c_idx == 6:
                    if val == "Done":
                        cell.fill = fill_done
                        cell.font = font_done
                    elif val == "In Progress":
                        cell.fill = fill_progress
                        cell.font = font_progress
                    elif val == "Pending":
                        cell.fill = fill_pending
                        cell.font = font_pending
                    elif val == "Not Started":
                        cell.fill = fill_not_started
                        cell.font = font_not_started
                    else:
                        cell.fill = fill_planned
                        cell.font = font_planned
                else:
                    cell.font = font_default

        ws_r.row_dimensions[r_idx].height = 24 if r_idx > 1 else 26

    col_widths_r = {1: 15, 2: 15, 3: 26, 4: 36, 5: 68, 6: 15}
    for col_idx, width in col_widths_r.items():
        ws_r.column_dimensions[get_column_letter(col_idx)].width = width
    ws_r.freeze_panes = "A2"

    # -------------------------------------------------------------
    # B. Rebuild Sheet: Sitemap (6 columns)
    # -------------------------------------------------------------
    if "Sitemap" in wb.sheetnames:
        del wb["Sitemap"]
    ws_s = wb.create_sheet("Sitemap", index=3)

    for c_idx, h in enumerate(SITEMAP_HEADER, 1):
        cell = ws_s.cell(1, c_idx, h)
        cell.font = font_header
        cell.fill = fill_header
        cell.border = border_thin
        align_h = "center" if c_idx in [1, 2, 3, 6] else "left"
        cell.alignment = Alignment(horizontal=align_h, vertical="center")
    ws_s.row_dimensions[1].height = 26

    for r_idx, item in enumerate(SITEMAP_ROWS, 2):
        stt = r_idx - 1
        row_vals = [stt] + item
        for c_idx, val in enumerate(row_vals, 1):
            cell = ws_s.cell(r_idx, c_idx, val)
            cell.border = border_thin
            align_h = "center" if c_idx in [1, 2, 3, 6] else "left"
            cell.alignment = Alignment(horizontal=align_h, vertical="center")

            if c_idx == 5:
                cell.font = font_bold
            elif c_idx == 6:
                if val == "Done":
                    cell.fill = fill_done
                    cell.font = font_done
                elif val == "In Progress":
                    cell.fill = fill_progress
                    cell.font = font_progress
                elif val == "Pending":
                    cell.fill = fill_pending
                    cell.font = font_pending
                elif val == "Not Started":
                    cell.fill = fill_not_started
                    cell.font = font_not_started
                else:
                    cell.fill = fill_planned
                    cell.font = font_planned
            else:
                cell.font = font_default

        ws_s.row_dimensions[r_idx].height = 24

    col_widths_s = {1: 8, 2: 16, 3: 16, 4: 26, 5: 42, 6: 18}
    for col_idx, width in col_widths_s.items():
        ws_s.column_dimensions[get_column_letter(col_idx)].width = width
    ws_s.freeze_panes = "A2"

    wb.save(EXCEL_PATH)
    print("Local Excel workbook updated successfully with realigned Roadmap & Sitemap!")


def update_google_sheets():
    print("2. Updating Google Sheets...")
    token = get_access_token()

    url_meta = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?fields=sheets(properties)"
    req_meta = urllib.request.Request(url_meta, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req_meta) as resp:
        meta = json.loads(resp.read().decode("utf-8"))

    sheet_map = {s["properties"]["title"]: s["properties"]["sheetId"] for s in meta["sheets"]}
    roadmap_id = sheet_map.get("Product Roadmap")
    sitemap_id = sheet_map.get("Sitemap")

    # -------------------------------------------------------------
    # A. Update Tab: Product Roadmap
    # -------------------------------------------------------------
    print("Updating Google Sheet Tab: Product Roadmap...")
    clear_range(token, "Product Roadmap!A1:Z50")
    num_rows_r = len(NEW_ROADMAP_DATA)
    update_values(token, f"Product Roadmap!A1:F{num_rows_r}", NEW_ROADMAP_DATA)

    reqs_r = []
    reqs_r.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": roadmap_id,
                "gridProperties": {
                    "frozenRowCount": 1,
                    "rowCount": max(50, num_rows_r + 5),
                    "columnCount": 10
                }
            },
            "fields": "gridProperties(frozenRowCount,rowCount,columnCount)"
        }
    })

    widths_r = [120, 120, 190, 260, 560, 120]
    for c_idx, w in enumerate(widths_r):
        reqs_r.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": roadmap_id,
                    "dimension": "COLUMNS",
                    "startIndex": c_idx,
                    "endIndex": c_idx + 1
                },
                "properties": {"pixelSize": w},
                "fields": "pixelSize"
            }
        })

    # Header
    reqs_r.append({
        "repeatCell": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 6
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
    for c_idx in [0, 1, 5]:
        reqs_r.append({
            "repeatCell": {
                "range": {
                    "sheetId": roadmap_id,
                    "startRowIndex": 0,
                    "endRowIndex": 1,
                    "startColumnIndex": c_idx,
                    "endColumnIndex": c_idx + 1
                },
                "cell": {"userEnteredFormat": {"horizontalAlignment": "CENTER"}},
                "fields": "userEnteredFormat.horizontalAlignment"
            }
        })

    # Data formatting
    reqs_r.append({
        "repeatCell": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 1,
                "endRowIndex": num_rows_r,
                "startColumnIndex": 0,
                "endColumnIndex": 6
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
    for r_idx in range(1, num_rows_r):
        bg = {"red": 0.97, "green": 0.98, "blue": 0.99} if r_idx % 2 == 1 else {"red": 1.0, "green": 1.0, "blue": 1.0}
        reqs_r.append({
            "repeatCell": {
                "range": {
                    "sheetId": roadmap_id,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 5
                },
                "cell": {"userEnteredFormat": {"backgroundColor": bg}},
                "fields": "userEnteredFormat.backgroundColor"
            }
        })

    for c_idx in [0, 1]:
        reqs_r.append({
            "repeatCell": {
                "range": {
                    "sheetId": roadmap_id,
                    "startRowIndex": 1,
                    "endRowIndex": num_rows_r,
                    "startColumnIndex": c_idx,
                    "endColumnIndex": c_idx + 1
                },
                "cell": {"userEnteredFormat": {"horizontalAlignment": "CENTER"}},
                "fields": "userEnteredFormat.horizontalAlignment"
            }
        })
    reqs_r.append({
        "repeatCell": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 1,
                "endRowIndex": num_rows_r,
                "startColumnIndex": 3,
                "endColumnIndex": 4
            },
            "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
            "fields": "userEnteredFormat.textFormat.bold"
        }
    })
    reqs_r.append({
        "repeatCell": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 1,
                "endRowIndex": num_rows_r,
                "startColumnIndex": 4,
                "endColumnIndex": 5
            },
            "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP"}},
            "fields": "userEnteredFormat.wrapStrategy"
        }
    })

    # Badges Roadmap
    for r_idx in range(1, num_rows_r):
        st = NEW_ROADMAP_DATA[r_idx][5]
        if st == "Done":
            bg = {"red": 0.86, "green": 0.98, "blue": 0.90}
            fg = {"red": 0.08, "green": 0.50, "blue": 0.24}
        elif st == "In Progress":
            bg = {"red": 0.99, "green": 0.95, "blue": 0.78}
            fg = {"red": 0.71, "green": 0.33, "blue": 0.04}
        elif st == "Pending":
            bg = {"red": 1.0, "green": 0.89, "blue": 0.90}
            fg = {"red": 0.75, "green": 0.07, "blue": 0.24}
        elif st == "Not Started":
            bg = {"red": 0.945, "green": 0.96, "blue": 0.976}
            fg = {"red": 0.28, "green": 0.33, "blue": 0.41}
        else:
            bg = {"red": 0.88, "green": 0.91, "blue": 1.0}
            fg = {"red": 0.26, "green": 0.22, "blue": 0.79}

        reqs_r.append({
            "repeatCell": {
                "range": {
                    "sheetId": roadmap_id,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 5,
                    "endColumnIndex": 6
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

    border_style = {"style": "SOLID", "width": 1, "color": {"red": 0.85, "green": 0.88, "blue": 0.92}}
    reqs_r.append({
        "updateBorders": {
            "range": {
                "sheetId": roadmap_id,
                "startRowIndex": 0,
                "endRowIndex": num_rows_r,
                "startColumnIndex": 0,
                "endColumnIndex": 6
            },
            "top": border_style, "bottom": border_style, "left": border_style, "right": border_style,
            "innerHorizontal": border_style, "innerVertical": border_style
        }
    })
    batch_update_spreadsheet(token, reqs_r)
    print("Google Sheet Tab: Product Roadmap updated successfully!")

    # -------------------------------------------------------------
    # B. Update Tab: Sitemap (6 columns)
    # -------------------------------------------------------------
    print("Updating Google Sheet Tab: Sitemap...")
    clear_range(token, "Sitemap!A1:Z200")

    full_table_s = [SITEMAP_HEADER] + [[idx + 1] + item for idx, item in enumerate(SITEMAP_ROWS)]
    num_rows_s = len(full_table_s)
    num_cols_s = len(SITEMAP_HEADER)

    update_values(token, f"Sitemap!A1:F{num_rows_s}", full_table_s)

    reqs_s = []
    reqs_s.append({
        "updateSheetProperties": {
            "properties": {
                "sheetId": sitemap_id,
                "gridProperties": {
                    "frozenRowCount": 1,
                    "rowCount": max(150, num_rows_s + 10),
                    "columnCount": 8
                }
            },
            "fields": "gridProperties(frozenRowCount,rowCount,columnCount)"
        }
    })

    col_widths_s = [60, 120, 120, 200, 340, 140]
    for c_idx, w in enumerate(col_widths_s):
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

    # Header Row
    reqs_s.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols_s
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
    for c_idx in [0, 1, 2, 5]:
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

    # Data formatting
    reqs_s.append({
        "repeatCell": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 1,
                "endRowIndex": num_rows_s,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols_s
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
    for r_idx in range(1, num_rows_s):
        bg = {"red": 0.97, "green": 0.98, "blue": 0.99} if r_idx % 2 == 1 else {"red": 1.0, "green": 1.0, "blue": 1.0}
        reqs_s.append({
            "repeatCell": {
                "range": {
                    "sheetId": sitemap_id,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 5
                },
                "cell": {"userEnteredFormat": {"backgroundColor": bg}},
                "fields": "userEnteredFormat.backgroundColor"
            }
        })

    for c_idx in [0, 1, 2]:
        reqs_s.append({
            "repeatCell": {
                "range": {
                    "sheetId": sitemap_id,
                    "startRowIndex": 1,
                    "endRowIndex": num_rows_s,
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
                "endRowIndex": num_rows_s,
                "startColumnIndex": 4,
                "endColumnIndex": 5
            },
            "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
            "fields": "userEnteredFormat.textFormat.bold"
        }
    })

    # Badges Sitemap
    for r_idx in range(1, num_rows_s):
        st = full_table_s[r_idx][5]
        if st == "Done":
            bg = {"red": 0.86, "green": 0.98, "blue": 0.90}
            fg = {"red": 0.08, "green": 0.50, "blue": 0.24}
        elif st == "In Progress":
            bg = {"red": 0.99, "green": 0.95, "blue": 0.78}
            fg = {"red": 0.71, "green": 0.33, "blue": 0.04}
        elif st == "Pending":
            bg = {"red": 1.0, "green": 0.89, "blue": 0.90}
            fg = {"red": 0.75, "green": 0.07, "blue": 0.24}
        elif st == "Not Started":
            bg = {"red": 0.945, "green": 0.96, "blue": 0.976}
            fg = {"red": 0.28, "green": 0.33, "blue": 0.41}
        else:
            bg = {"red": 0.88, "green": 0.91, "blue": 1.0}
            fg = {"red": 0.26, "green": 0.22, "blue": 0.79}

        reqs_s.append({
            "repeatCell": {
                "range": {
                    "sheetId": sitemap_id,
                    "startRowIndex": r_idx,
                    "endRowIndex": r_idx + 1,
                    "startColumnIndex": 5,
                    "endColumnIndex": 6
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

    reqs_s.append({
        "updateBorders": {
            "range": {
                "sheetId": sitemap_id,
                "startRowIndex": 0,
                "endRowIndex": num_rows_s,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols_s
            },
            "top": border_style, "bottom": border_style, "left": border_style, "right": border_style,
            "innerHorizontal": border_style, "innerVertical": border_style
        }
    })

    batch_update_spreadsheet(token, reqs_s)
    print("Google Sheet Tab: Sitemap updated successfully!")


def generate_brd_section_10_html():
    html = [
        "## 10. LỘ TRÌNH TRIỂN KHAI TOÀN DIỆN CÁC DỰ ÁN FINANCIAL HUB (THỰC TẾ TRIỂN KHAI)\n",
        '<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.85em;">',
        "  <thead>",
        '    <tr style="background-color:#1e3a5f; color:#ffffff;">',
        '      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Giai Đoạn (Phase)</th>',
        '      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Thời Gian</th>',
        '      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Cụm Sản Phẩm (Track)</th>',
        '      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Tên Tính Năng / Sản Phẩm</th>',
        '      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Chi Tiết Triển Khai & Nhiệm Vụ Kỹ Thuật</th>',
        '      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Trạng Thái</th>',
        "    </tr>",
        "  </thead>",
        "  <tbody>"
    ]

    for item in NEW_ROADMAP_DATA[1:]:
        phase, time, track, name, desc, status = item

        if status == "Done":
            st_style = "color:#15803d; background-color:#dcfce7; font-weight:700; text-align:center;"
            row_bg = "background-color:#f0fdf4;"
        elif status == "In Progress":
            st_style = "color:#b45309; background-color:#fef9c3; font-weight:700; text-align:center;"
            row_bg = "background-color:#fefce8;"
        elif status == "Pending":
            st_style = "color:#be123c; background-color:#ffe4e6; font-weight:700; text-align:center;"
            row_bg = "background-color:#fff1f2;"
        elif status == "Not Started":
            st_style = "color:#475569; background-color:#f1f5f9; font-weight:700; text-align:center;"
            row_bg = "background-color:#f8fafc;"
        else:
            st_style = "color:#4338ca; background-color:#e0e7ff; font-weight:700; text-align:center;"
            row_bg = "background-color:#f8fafc;"

        html.append(f'    <tr style="{row_bg}">')
        html.append(f'      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700;"><strong>{phase}</strong></td>')
        html.append(f'      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">{time}</td>')
        html.append(f'      <td style="border:1px solid #94a3b8; padding:6px; font-weight:600;">{track}</td>')
        html.append(f'      <td style="border:1px solid #94a3b8; padding:6px; font-weight:700;">{name}</td>')
        html.append(f'      <td style="border:1px solid #94a3b8; padding:6px;">{desc}</td>')
        html.append(f'      <td style="border:1px solid #94a3b8; padding:6px; {st_style}">{status}</td>')
        html.append("    </tr>")

    html.append("  </tbody>")
    html.append("</table>\n")
    return "\n".join(html)


def update_brd_file():
    print("3. Updating 05_HUBS/financial/financial-hub-brd.md Section 10...")
    content = BRD_PATH.read_text(encoding="utf-8")
    s10_start = content.find("## 10. LỘ TRÌNH")
    if s10_start != -1:
        tbl_end = content.find("</table>", s10_start)
        if tbl_end != -1:
            new_s10 = generate_brd_section_10_html()
            content = content[:s10_start] + new_s10 + content[tbl_end + 8:]
            BRD_PATH.write_text(content, encoding="utf-8")
            print("BRD Section 10 updated successfully!")


def main():
    update_local_excel()
    update_google_sheets()
    update_brd_file()
    print("\nAll CCQ & Roadmap Phase timeline realignments completed successfully!")


if __name__ == "__main__":
    main()
