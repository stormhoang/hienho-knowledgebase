# HỆ THỐNG ĐÓNG GÓI BÁO CÁO WEB PLATFORM (REPORT PACKAGING ARCHITECTURE)

Tài liệu này xác lập cấu trúc tổ chức, nguồn dữ liệu Single Source of Truth (SSOT) và quy trình đóng gói số liệu định kỳ (Weekly & Monthly Reports) cho toàn bộ nền tảng Web Platform.

---

## 1. BA TRỤ CỘT DỮ LIỆU ĐÓNG GÓI BÁO CÁO (3 DATA PILLARS)

Báo cáo Web Platform không chỉ dừng lại ở số liệu Pageviews bề nổi, mà bắt buộc phải hợp nhất **3 Trụ Cột Dữ Liệu** để cung cấp góc nhìn toàn diện cho Ban Giám Đốc và Executive Leadership:

```
┌────────────────────────────────────────────────────────────────────────┐
│             HỆ THỐNG ĐÓNG GÓI BÁO CÁO TỔNG HỢP (REPORT PACKAGING)       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┼───────────────────────────────┐
    ▼                               ▼                               ▼
[TRỤ CỘT 1: HIỆU SUẤT TĂNG TRƯỞNG]  [TRỤ CỘT 2: SỨC KHỎE CRAWL GSC] [TRỤ CỘT 3: HỒ SƠ BACKLINK]
- File: Web Performance Tracking    - GSC Crawl Stats               - GSC Top Linking Sites
- MTD Days, Target vs Actual        - Volume: Req/ngày, Download/ngày- Mật độ tập trung (TopCV, CVS)
- Run-rate Forecast 31d             - Chất lượng: 200 OK, 404 Waste - Authority dồn vào Careers
- Phân bổ 5 Kênh Traffic           - Purpose: Discovery vs Refresh - Rà soát 147 site toxic link
- Dashboard 5 Strategic Hubs        - Cảnh báo: Breakpoint 01/10    - Disavow file chuẩn GSC
    └───────────────────────────────┬───────────────────────────────┘
                                    │
                                    ▼
            [CONSOLIDATED REPORT PACKAGES (EXECUTIVE READY)]
            - Weekly Report (7 ngày - gửi anh Công)
            - Monthly Business Review (Chuẩn 4 phần - gửi anh Tường)
```

---

## 2. CHI TIẾT 3 NGUỒN DỮ LIỆU ĐẦU VÀO

### Trụ Cột 1: Hiệu Suất Tăng Trưởng & cơ cấu (Performance & Channels)
- **Nguồn trích xuất:** File `Web Performance Tracking (2).xlsx` (tại `/Users/hienhv/Downloads/`).
- **File SSOT lưu trữ:** [`07_REPORTS/web_performance_tracking.xlsx`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/web_performance_tracking.xlsx).
- **Snapshot tự động:** [`07_REPORTS/data/monthly_MM_YYYY_mtd_XXd.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data).
- **Chỉ số trọng yếu:**
  - Tổng Pageviews lũy kế (Actual MTD), Số ngày MTD (MTD Days).
  - Tốc độ vận hành ngày (Daily Pace) và dự báo cuối tháng (Run-rate Forecast 31d).
  - Phân bổ Kênh: Organic, Direct, Referral, Paid, Others.
  - Phân bổ 5 Strategic Hubs: Cinema Hub, Financial Hub, Vehicle Hub, New User Hub, Student Hub.

### Trụ Cột 2: Sức Khỏe Kỹ Thuật & Crawl Budget (Technical Health & GSC Crawl Stats)
- **Nguồn trích xuất:** Google Search Console Crawl Stats (`www.momo.vn`).
- **Snapshot dữ liệu:** [`07_REPORTS/technical_seo/crawl_stats/gsc_crawl_stats_latest.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/technical_seo/crawl_stats/gsc_crawl_stats_latest.json).
- **Chỉ số trọng yếu:**
  - Số lượng requests/ngày (14.850 req/ngày T10 vs 21.114 req/ngày T9).
  - Dung lượng tải xuống/ngày (564 MB/ngày) và dung lượng trung bình (38.9 KB/req).
  - Tỷ lệ mã phản hồi: 200 OK (94.11%), 404 Not Found (4.14% ~ lãng phí 860 req/ngày), 301 (1.71%).
  - Mục đích crawl: Refresh (95.97%) vs Discovery (4.03%).
  - Cơ cấu User-Agent: Smartphone Bot (51.2%), Desktop Bot (12.54%), AdsBot (15.3%), Page Resources (20.14%).
  - Cảnh báo rủi ro: Breakpoint ngày 01/10 và độ trễ phản ánh vào Organic traffic cuối tháng 10.

### Trụ Cột 3: Uy Tín Tên Miền & Hồ Sơ Liên Kết (Domain Authority & Backlink Profile)
- **Nguồn trích xuất:** Google Search Console Top Linking Sites & Audit liên kết ngoài.
- **Snapshot dữ liệu:** [`07_REPORTS/technical_seo/backlinks/backlink_profile_latest.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/technical_seo/backlinks/backlink_profile_latest.json).
- **Tập tin chi tiết:**
  - Bảng phân loại chi tiết: [`07_REPORTS/technical_seo/backlinks/backlink_audit_detail_2026-10-10.csv`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/technical_seo/backlinks/backlink_audit_detail_2026-10-10.csv).
  - File Disavow chuẩn GSC: [`07_REPORTS/technical_seo/backlinks/backlink_disavow_candidates_2026-10-10.txt`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/technical_seo/backlinks/backlink_disavow_candidates_2026-10-10.txt).
- **Chỉ số trọng yếu:**
  - Tổng số 1.000 referring sites và 118.757 linking pages.
  - Mức độ tập trung: Top 2 site (topcv.vn, cvs.vn) chiếm 79.9%; Top 5 site chiếm 87.4%.
  - Nghịch lý Authority: 94.925 links dồn vào 7-11 trang tuyển dụng (careers), 0 link trỏ vào Hubs thương mại.
  - Tỷ trọng trang tin chính thống (Editorial News) chỉ đạt ~5%.
  - Danh mục cờ đỏ: 147 domains candidate (353 linking pages), trong đó có 67 site cờ bạc/casino (A1 Gambling).

---

## 3. CẤU TRÚC THƯ MỤC CHUẨN HÓA CỦA 07_REPORTS

```
07_REPORTS/
├── REPORT_SYSTEM_STRUCTURE.md               # Kiến trúc hệ thống dữ liệu báo cáo (File này)
├── WEB_PERFORMANCE_TRACKING_MASTER.md       # SSOT Master (Tracking, Crawl Stats & Backlinks)
├── web_performance_tracking.xlsx            # File SSOT Excel đồng bộ từ Downloads
│
├── data/                                    # Kho lưu trữ JSON Snapshots theo ngày MTD
│   ├── monthly_10_2026_mtd_9d.json          # Snapshot tracking thuần MTD 9 ngày
│   ├── monthly_10_2026_consolidated.json    # Snapshot hợp nhất (Tracking + Crawl + Backlinks)
│   └── ...                                  # Snapshots các mốc thời gian trước
│
├── technical_seo/                           # Báo cáo Sức khỏe Kỹ thuật & Hạ tầng SEO
│   ├── crawl_stats/                         # Dữ liệu & Báo cáo GSC Crawl Stats
│   │   └── gsc_crawl_stats_latest.json      # Snapshot chi tiết Crawl Budget & Status Codes
│   └── backlinks/                           # Dữ liệu Hồ sơ Liên kết & Audit Disavow
│       ├── backlink_profile_latest.json     # Snapshot cấu trúc nồng độ liên kết
│       ├── backlink_audit_detail_2026-10-10.csv
│       ├── backlink_disavow_candidates_2026-10-10.txt
│       └── backlink_disavow_baseline_2026-10-10.csv
│
├── packages/                                # Bộ Báo cáo Điều hành (Executive Packages)
│   ├── monthly/                             # Báo cáo Tháng (Chuẩn Agenda 4 phần gửi BOM)
│   │   ├── report-thang-08-2026.md
│   │   ├── report-thang-09-2026.md
│   │   └── report-thang-10-2026-mtd-9d.md
│   └── weekly/                              # Báo cáo Tuần (Gửi Executive Leadership)
│
├── docs/                                    # Báo cáo chuyên đề lịch sử & biên bản tổng kết
├── sheets/                                  # Templates & file mẫu bảng tính
└── scripts/                                 # Công cụ đóng gói tự động
    ├── sync_tracking_report.py              # Script đồng bộ Excel Downloads
    └── package_consolidated_report.py       # Script đóng gói hợp nhất 3 trụ cột
```

---

## 4. QUY TRÌNH ĐÓNG GÓI BÁO CÁO TỰ ĐỘNG (PACKAGING PIPELINE)

1. **Bước 1: Đồng bộ dữ liệu Excel:** Chạy `python3 scripts/sync_tracking_report.py` để quét file mới nhất trong `/Users/hienhv/Downloads/` và cập nhật SSOT Excel cùng JSON tracking.
2. **Bước 2: Hợp nhất Dữ liệu Kỹ thuật:** Script tự động nạp `gsc_crawl_stats_latest.json` và `backlink_profile_latest.json` để tạo file snapshot hợp nhất `monthly_10_2026_consolidated.json`.
3. **Bước 3: Cập nhật Master Document:** Đồng bộ các số liệu mới nhất vào [WEB_PERFORMANCE_TRACKING_MASTER.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md).
4. **Bước 4: Xuất bản Executive Report:** Đóng gói bản báo cáo hoàn chỉnh vào `07_REPORTS/packages/monthly/` theo chuẩn văn phong Product Lead / Tech Lead:
   - Không sử dụng Emoji/Icon.
   - Không dùng từ "sàn Web" (chỉ dùng "nền tảng Web", "Kênh Web", "Web Platform").
   - Không nêu tên riêng cá nhân PIC trong báo cáo.
   - Áp dụng nguyên tắc "So What?" (tập trung vào bản chất dịch chuyển, nguyên nhân và hành động).
