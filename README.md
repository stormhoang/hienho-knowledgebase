# WEB PLATFORM WORKSPACE & ANALYTICS TOOLS

Tài liệu kỹ thuật và bộ công cụ tự động hóa phân tích dữ liệu phục vụ nghiên cứu, theo dõi hiệu suất và tối ưu hóa trải nghiệm trên nền tảng Web.

---

## 1. GIỚI THIỆU CHUNG

Kho lưu trữ này chứa các tài liệu nghiên cứu kỹ thuật, tài nguyên cấu trúc thông tin và các kịch bản (scripts) tự động hóa phục vụ các tác vụ:
- Phân tích và xử lý dữ liệu lưu lượng truy cập (Web Analytics & Search Insights).
- Đo lường và kiểm soát các chỉ số trải nghiệm người dùng (Core Web Vitals, UX Signals).
- Xây dựng cấu trúc thông tin (Information Architecture) và phân loại dữ liệu chuyên mục.
- Tự động hóa quy trình tổng hợp số liệu và báo cáo định kỳ.

---

## 2. CẤU TRÚC THƯ MỤC CƠ BẢN

```
.
├── 01_STRATEGIC_PLAN/     # Kế hoạch và định hướng kỹ thuật
├── 02_FRAMEWORKS/         # Các khung phương pháp luận và tài liệu kỹ thuật
├── 03_SKILLS/             # Bộ quy chuẩn tài liệu và kỹ năng vận hành
├── 04_MOSPARK_PLATFORM/   # Hướng dẫn kỹ thuật và quy chuẩn tracking
├── 05_HUBS/               # Tài nguyên phân loại dữ liệu theo chuyên mục
├── 06_USE_CASE_MOMO/      # Hồ sơ nghiên cứu và tối ưu cấu trúc nội dung
├── 07_REPORTS/            # Báo cáo kỹ thuật và dữ liệu phân tích định kỳ
├── 08_DECISION_LOG/       # Nhật ký ghi nhận các quyết định kiến trúc
├── 09_PRD/                # Tài liệu đặc tả yêu cầu kỹ thuật
├── growth_reporting_tool/ # Giao diện MCP Server tích hợp công cụ
└── scripts/               # Bộ công cụ và kịch bản Python tự động hóa
```

---

## 3. CÀI ĐẶT & MÔI TRƯỜNG VẬN HÀNH

### Yêu cầu hệ thống:
- Python 3.12 trở lên
- Môi trường ảo Python (`venv`)

### Các bước cài đặt:
```bash
# 1. Khởi tạo môi trường ảo
python3.12 -m venv .venv

# 2. Cài đặt các thư viện phụ thuộc (luôn gọi qua ./.venv/bin/python, không dùng python/python3 trần)
./.venv/bin/python -m pip install -r scripts/requirements.txt
```

---

## 4. HƯỚNG DẪN THỰC THI CƠ BẢN

Các công cụ phân tích và tự động hóa được đóng gói trong thư mục `scripts/`:

```bash
# 1. Chạy chẩn đoán và phân tích dữ liệu hiệu suất
./.venv/bin/python scripts/diagnose_performance.py

# 2. Kiểm tra dị biệt và tính toàn vẹn liên kết
./.venv/bin/python scripts/detect_anomalies.py

# 3. Phân tích dữ liệu chiến dịch và nguồn truy cập
./.venv/bin/python scripts/sync_paid_ads.py

# 4. Khởi chạy MCP Server phục vụ tích hợp công cụ
./.venv/bin/python growth_reporting_tool/mcp_server.py
```

---

## 5. QUY CHUẨN AN TOÀN & BẢO MẬT

- **Bảo mật Credentials:** Tuyệt đối không commit các tệp cấu hình chứa khóa bí mật (API Keys, OAuth Tokens, Private Keys, file `.env`) vào hệ thống quản lý phiên bản Git.
- **Tuân thủ quy chuẩn dữ liệu:** Đảm bảo toàn bộ quy trình thu thập và xử lý dữ liệu tuân thủ nguyên tắc Zero-PII (không ghi nhận thông tin định danh cá nhân của người dùng).
- **Cập nhật tài liệu:** Khi cập nhật logic phân tích trong thư mục `scripts/`, cần đồng bộ các tài liệu đặc tả kỹ thuật tương ứng.
