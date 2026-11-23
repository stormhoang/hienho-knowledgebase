---
name: read-latest-tracking-report
description: Quy trình tự động quét, đọc file Excel tracking mới nhất trong /Users/hienhv/Downloads/ và đồng bộ số liệu hiệu suất Web Platform.
---

# SKILL: AUTOMATED TRACKING REPORT SYNCHRONIZATION

## 1. MỤC TIÊU & TRIGGER
Khi người dùng đưa ra câu lệnh:
- *"Đọc tracking report mới nhất"*
- *"Lấy số Web Performance Tracking mới nhất"*
- *"Check file tracking mới nhất trong Downloads"*
- Hoặc bất kỳ yêu cầu cập nhật số liệu hiệu suất Kênh Web.

## 2. QUY TRÌNH XỬ LÝ TỰ ĐỘNG (AUTOMATED WORKFLOW)

1. **Chạy Script Tự Động Quét & Trích Xuất:**
   - Thực thi lệnh: `./.venv/bin/python scripts/sync_tracking_report.py`
   - Script tự động tìm file mới nhất trong `/Users/hienhv/Downloads/` có dạng `*[Ww]eb*[Pp]erformance*[Tt]racking*.xlsx` theo thời gian `mtime`.
   - Tự động nhận diện số ngày lũy kế MTD (MTD Days).
   - Tự động lưu bản ghi sạch vào SSOT [web_performance_tracking.xlsx](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/web_performance_tracking.xlsx).
   - Tự động khởi tạo JSON Snapshot tại `07_REPORTS/data/monthly_MM_YYYY_mtd_XXd.json`.

2. **Cập Nhật Tài Liệu SSOT Trong Repository:**
   - Cập nhật [WEB_PERFORMANCE_TRACKING_MASTER.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md).
   - Cập nhật [hienho_master_doc.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/hienho_master_doc.md) (Thêm dòng Changelog).
   - Cập nhật sheet `Performance` trong các file Roadmap Excel (`cinema-hub-roadmap.xlsx`, `financial-hub-roadmap.xlsx`, `vehicle-hub-roadmap.xlsx`).
   - Cập nhật phần số liệu MTD trong tài liệu BRD 3 Hubs (`cinema-hub-brd.md`, `financial-hub-brd.md`, `vehicle-hub-brd.md`).

3. **Báo Cáo Trực Tiếp Cho Người Dùng (Executive Report):**
   - Trình bày bảng chỉ số tổng quan Kênh Web (Total PVs, % Target, Daily Pace, Run-rate Forecast 30d).
   - Trình bày bảng phân bổ Kênh Traffic theo 2 nhóm: Non-Paid gồm đúng 4 kênh (Organic, Direct, Referral, AI Traffic (GEO)) và Paid Ads.
   - Trình bày bảng Dashboard 5 Strategic Hubs (New User, Cinema, Financial, Vehicle, Student).
   - Đảm bảo tuân thủ phong cách Product/Tech Lead: **KHÔNG dùng Emoji/Icon**, **KHÔNG nêu tên riêng cá nhân**, sử dụng **Markdown Tables**.

## 4. QUY CHUẨN ĐẶT TÊN SUB-PAGES CINEMA HUB (CINEMA TRACKING NAMING CONVENTION)
Khi trích xuất, phân tích hoặc trình bày dữ liệu Cinema Hub trong các báo cáo Web Tracking, bắt buộc tuân thủ đúng quy chuẩn:
- `Cinema_home Page` / `Cinema_Home Page` ➔ **Cinema_Home Page (Trang chủ Cinema)** (giữ nguyên mã kỹ thuật, thêm ghi chú trong ngoặc đơn).
- `Cinema_Cineplex` / `Cinema_Cineplex Page` ➔ **Trang Rạp phim**.
- `Cinema_News` ➔ **Tin tức**.
- `Cinema_Page` ➔ **Trang phim chi tiết**.
- `Cinema_Blog` ➔ **Cinema_Blog**.
- `Cinema_Landing Page` ➔ **Cinema_Landing Page**.

