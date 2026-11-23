# -*- coding: utf-8 -*-
from pathlib import Path

report_path = Path("07_REPORTS/docs/weekly-report-2026-10-26-11-01.md")
with open(report_path) as f:
    text = f.read()

old_v2 = text[text.find("### 2. Các Nền Tảng Kỹ Thuật (Platform Projects)"):]

new_v2 = """### 2. Các Nền Tảng Kỹ Thuật (Platform Projects - duy.tran2 & hieu.nguyen8)
- **Admin Panel & Web-in-App (hieu.nguyen8 & duy.tran2):**
  - [P0] Thực hiện build Production Phase 2 Admin Panel cùng nhánh BMC vào ngày 02/11/2026 (All-in-One Editor, phân quyền duyệt bài).
  - [P0] Theo dõi vận hành sau đợt build prod và hỗ trợ các Cell Teams làm quen với các khối nội dung in-app mới (Mã khuyến mãi Voucher, Hướng dẫn từng bước, Live Mobile Preview).
- **Cổng Tìm Kiếm & Hồ Danh Mục URL (hieu.nguyen8):**
  - [P0] Triển khai giai đoạn 1 của Hồ danh mục URL toàn website: tạo bảng dữ liệu trên môi trường phát triển và nạp dữ liệu 51 trang tìm kiếm ban đầu.
  - [P1] Đo lường tỷ lệ người dùng sử dụng thẻ Chuyển tiền qua SĐT và banner Người dùng mới trên `/tim-kiem`.
- **Hệ Thống Trí Tuệ Nhân Tạo & Cơ Sở Tri Thức (duy.tran2):**
  - [P1] Hoàn thiện bộ tiêu chí đánh giá chất lượng câu trả lời của Chatbot và theo dõi tỷ lệ bao phủ tri thức (% Coverage) trên các trang dịch vụ trọng điểm.
- **Hạ Tầng & Vận Hành MoMo API (hieu.nguyen8):**
  - [P0] Theo dõi độ ổn định của hệ thống API sau khi cập nhật cấu hình kết nối trung tâm dữ liệu và môi trường dev.
  - [P0] Phối hợp triển khai lớp máy chủ trung gian (Server-side Proxy) cho luồng dữ liệu Merchant.
- **Trang Dịch Vụ Vé Số Trên Web (duy.tran2):**
  - [P1] Hướng dẫn PO vé số thao tác cấu hình nội dung tĩnh trên Staging và giám sát tải hệ thống trong khung giờ mở thưởng 18h00 hàng ngày.
"""

text = text[:text.find("### 2. Các Nền Tảng Kỹ Thuật (Platform Projects)")] + new_v2

with open(report_path, "w") as f:
    f.write(text)

hubs_path = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/reports/weekly-report-2026-10-26-11-01.md")
with open(hubs_path, "w") as f:
    f.write(text)

print("Updated Section V.2 in both files successfully.")
