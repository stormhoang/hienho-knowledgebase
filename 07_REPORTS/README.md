# QUY HOẠCH CẤU TRÚC THƯ MỤC BÁO CÁO (07_REPORTS DIRECTORY BLUEPRINT)

Tài liệu này định nghĩa cấu trúc phân cấp, vai trò và quy chuẩn lưu trữ của toàn bộ thư mục `07_REPORTS/` nhằm đảm bảo hệ thống báo cáo luôn gọn gàng, có tính quy hoạch chuẩn mực theo phong cách Product Lead / Tech Lead.

---

## 1. SƠ ĐỒ CÂY THƯ MỤC TỔNG THỂ

```
07_REPORTS/
├── README.md                            # Bản đồ kiến trúc & quy chuẩn thư mục (File này)
├── WEB_PERFORMANCE_TRACKING_MASTER.md   # [SSOT] Master Doc báo cáo hiệu suất, Run-rate Target & Formula
├── KEYWORD_INVENTORY_MASTER.md          # [SSOT] Danh mục phân bổ kho từ khóa toàn bộ 10 Hubs
├── QUICK_WINS_PORTFOLIO.md              # [SSOT] Danh mục 100 URL Quick Wins bứt phá thứ hạng SERP
├── CONTENT_PLAN_REFACTOR_REVIEW.md      # Đánh giá kiến trúc kế hoạch nội dung MoSpark
├── KEYWORD_REALLOCATION_REVIEW.md       # Báo cáo đánh giá và tái phân bổ từ khóa
│
├── web_performance_tracking.xlsx       # [SSOT] File Excel theo dõi hiệu suất MTD (Cập nhật từ BigQuery)
│
├── data/                                # Dữ liệu phân tích, cache và API endpoints
│   ├── analytics/                       # Ma trận phễu hợp nhất (Full-Funnel Matrix, W2A, Events)
│   ├── bing_ai/                         # Dữ liệu trích dẫn từ Microsoft Bing Copilot
│   ├── cache/                           # Bộ nhớ đệm API (GSC, GA4 Multi-channel cache)
│   ├── clarity/                         # Dữ liệu xuất từ Microsoft Clarity API (AI & Frustration)
│   ├── competitors/                     # Dữ liệu phân tích đối thủ & Content Gap
│   ├── credentials/                     # Khóa xác thực API bảo mật (GA4, GSC, Clarity token)
│   ├── dim/                             # Từ điển chuẩn hóa URL & Dự án BigQuery (web_dim_page_url.json)
│   ├── ga4/                             # Landing Pages GA4 thực tế xuất sang Web Hubs
│   ├── geo_entity_gaps/                 # Dữ liệu phân tích thực thể AI Search / GEO
│   ├── history/                         # Lưu trữ lịch sử dữ liệu theo ngày
│   └── suggestions/                     # Đề xuất tối ưu hóa từ khóa và nội dung
│
├── docs/                                # Báo cáo định kỳ, chuyên đề Hubs và tài liệu chiến lược
│   ├── INDEX.md                         # [Index SSOT] Danh mục tra cứu toàn bộ báo cáo lịch sử (T1 -> T10)
│   ├── report-thang-*.md                # Báo cáo kinh doanh hàng tháng (MBR)
│   ├── report-*-hub-*.md                # Báo cáo chuyên đề các Hub trọng điểm (Cinema, Financial, Vehicle)
│   ├── strategy/                        # Tài liệu chiến lược ngân sách, gamification, nghiên cứu tìm kiếm
│   └── presentations/                   # Bản trình chiếu slide thuyết trình định kỳ (PPTX)
│
├── templates/                           # Biểu mẫu báo cáo chuẩn hóa
│   ├── weekly_report_template.md        # Mẫu báo cáo tuần (WBR)
│   ├── monthly_report_template.md       # Mẫu báo cáo tháng (MBR)
│   └── sheets/                          # Mẫu bảng tính và cấu trúc dữ liệu cũ
│
├── technical_seo/                       # Dữ liệu hạ tầng kỹ thuật SEO
│   ├── crawl_stats/                     # Dữ liệu Googlebot Crawl Stats và phân tích ngân sách crawl
│   └── backlinks/                       # Hồ sơ backlink, domain giới thiệu và danh sách disavow
│
├── competitors/                         # Báo cáo nghiên cứu đối thủ theo ngành
└── geo_entity_gaps/                     # Blueprint thực thể chi tiết cho công cụ AI Search
```

---

## 2. QUY CHUẨN LƯU TRỮ VÀ TIẾP NHẬN FILE MỚI

Để tránh tình trạng thư mục bị phân mảnh, mọi file mới tạo ra bắt buộc phải được đặt đúng vị trí theo quy chuẩn sau:

1. **Thư mục gốc `07_REPORTS/`:** 
   - CHỈ lưu trữ các file SSOT cốt lõi được quy định trong `AGENTS.md`:
     - [`WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md): Báo cáo & dữ liệu quản trị hiệu suất Master Markdown.
     - [`web_performance_tracking.xlsx`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/web_performance_tracking.xlsx): File lưu trữ đối chiếu từ nguồn xuất BigQuery.
   - Các Master Portfolios phục vụ pipeline (`KEYWORD_INVENTORY_MASTER.md`, `QUICK_WINS_PORTFOLIO.md`, `CONTENT_PLAN_REFACTOR_REVIEW.md`, `KEYWORD_REALLOCATION_REVIEW.md`).
   - Tuyệt đối không lưu các file nháp, file Word (.docx), file Slide (.pptx) hoặc báo cáo tháng lẻ ở thư mục gốc.
2. **Báo cáo và Tài liệu phân tích:** 
   - Đưa vào `07_REPORTS/docs/` và phải đăng ký liên kết vào [`07_REPORTS/docs/INDEX.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/INDEX.md).
   - Tài liệu định hướng ngân sách / nghiên cứu dài hạn: Đặt trong `07_REPORTS/docs/strategy/`.
   - File thuyết trình (.pptx): Đặt trong `07_REPORTS/docs/presentations/`.
3. **Dữ liệu thô và Tệp JSON:** 
   - Tất cả dữ liệu đầu ra từ scripts và API bắt buộc lưu trong `07_REPORTS/data/<phân_loại>/`.
4. **Mẫu biểu:** 
   - Đặt trong `07_REPORTS/templates/`.
