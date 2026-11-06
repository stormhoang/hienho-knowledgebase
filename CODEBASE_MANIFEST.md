# CODEBASE MANIFEST & AGENT OPERATING BLUEPRINT
> MoMo Web Platform Knowledge OS & Strategic Decision Copilot  
> Target: Mandatory Entrypoint & Knowledge Scanning File for all AI Agents & Human Operators

---

## 1. ĐỊNH DANH & BẢN CHẤT CỦA CODEBASE (REPOSITORY IDENTITY)

Kho lưu trữ này không phải là một thư viện tài liệu tĩnh hay một website thông thường. Đây là **Hệ điều hành Tri thức (Knowledge OS) và Bộ não Tham mưu Tăng trưởng (Growth & Decision Copilot)** của Nền tảng Web MoMo (`momo.vn`).

### 1.1. Mục tiêu cốt lõi (North Star):
1. **Tối ưu hóa Tìm kiếm Thế hệ mới (SEO & GEO):** Chuyển dịch từ SEO từ khóa truyền thống sang Semantic Topic Clusters, Direct Answers và tối ưu hiện diện trên các công cụ tìm kiếm AI (Google AI Overviews, Bing Copilot, Perplexity).
2. **Khai thác Nhu cầu Thị trường & Mùa vụ (Market & Seasonality Intelligence):** Phân tích hơn 3.7 triệu lượt tìm kiếm hàng tháng từ 236 Themes và giải mã chu kỳ mùa vụ 5 năm từ Google Trends.
3. **Phễu Tăng trưởng Sản phẩm (Product-Led Growth & Web-to-App Funnel):** Thu hút lưu lượng tự nhiên (Non-Paid Traffic) qua các công cụ, tiện ích công cộng (Utilities, Calculators) và chuyển đổi thành người dùng Mobile App thông qua OneLink an toàn, không thu thập PII.

### 1.2. Ranh giới vận hành (What This Repo Is NOT):
- **KHÔNG PHẢI Data Platform cấp tập đoàn:** Không sao chép các hạ tầng data warehouse khổng lồ (BigQuery/Databricks) mà tập trung vào **Local Analytical Data Mart** gọn nhẹ, tốc độ cao.
- **KHÔNG PHẢI Media Trading Desk:** Không tự ý tối ưu hóa chi tiêu quảng cáo Paid Ads bằng các mô hình phức tạp; số liệu Paid chỉ dùng để đo lường tỷ trọng phân rã (Non-Paid vs Paid).
- **KHÔNG PHẢI Bloomberg Terminal:** Không kéo các API tài chính vĩ mô ngoài phạm vi phục vụ trực tiếp cho tiện ích Web Hubs.

---

## 2. BẢN ĐỒ KIẾN TRÚC THƯ MỤC (DIRECTORY TOPOLOGY)

```text
Hienho_MoMo-Base/
├── CODEBASE_MANIFEST.md      # [SSOT ENTRYPOINT] File quét tổng quan bắt buộc cho mọi Agent
├── AGENTS.md                 # Quy chuẩn vận hành, bảng định tuyến nhanh (Fast Routing) & prompt rules
├── README.md                 # Giới thiệu kỹ thuật và hướng dẫn khởi động nhanh
├── 00_HARNESS_CORE/          # Giao thức tư duy (momo-thinking-protocol), quy tắc paraphrase và routing
├── 01_STRATEGIC_PLAN/        # OKRs 2026, chiến lược tăng trưởng Web Platform
├── 02_FRAMEWORKS/            # Bộ khung tư duy: First Principles, JTBD, 80/20 Growth, 4 Zones, Pyramid
├── 03_SKILLS/                # Tài liệu kỹ năng chuẩn hóa: SEO-GEO guideline, tracking, product frameworks
├── 04_MOSPARK_PLATFORM/      # Kiến trúc nền tảng MoSpark, schema tracking Umami, specs kỹ thuật
├── 05_HUBS/                  # Dữ liệu từ khóa ngành (Inventory: Financial, Vehicle, Cinema, Insurance...)
├── 06_USE_CASE_MOMO/         # Kế hoạch nội dung (Content Plans), PRD cho từng use case nghiệp vụ
├── 07_REPORTS/               # Trung tâm Dữ liệu Hiệu suất, báo cáo định kỳ và SQLite Data Mart
│   ├── data/                 # Raw data caches, snapshots MTD, mapping URLs
│   │   └── cache/performance.sqlite  # [DATA MART SSOT] Cơ sở dữ liệu phân tích tập trung
│   └── WEB_PERFORMANCE_TRACKING_MASTER.md # Báo cáo hiệu suất lũy kế tháng
├── 08_DECISION_LOG/          # Sổ cái ghi nhận các quyết định rẽ nhánh chiến lược và kiến trúc
├── scripts/                  # Toàn bộ mã nguồn Python & Node.js vận hành hệ thống
│   ├── lib/                  # Thư viện dùng chung (db.py, vi_nlp.py, forecast_engine.py...)
│   └── *.py                  # Các CLI tools chẩn đoán, quét dị biệt, đồng bộ dữ liệu
└── .venv/                    # Môi trường ảo Python 3.12 chuẩn hóa

Agent operating layer:
├── AGENT_OPERATING_CONTRACT.md
└── 00_HARNESS_CORE/
    ├── AGENT_CAPABILITIES.yaml
    ├── AGENT_SAFETY_CONTRACT.yaml
    └── AGENT_OUTPUT_CONTRACT.md

Evidence validation:
├── 00_HARNESS_CORE/EVIDENCE_CONTRACT.md
└── scripts/validate_evidence.py
```

---

## 3. KIẾN TRÚC DỮ LIỆU SINGLE SOURCE OF TRUTH (DATA MART SSOT)

Toàn bộ dữ liệu hiệu suất của Kênh Web được gom tụ tại cơ sở dữ liệu SQLite cục bộ:  
**Đường dẫn:** `07_REPORTS/data/cache/performance.sqlite`

### 3.1. Các bảng dữ liệu cốt lõi:
- **`dim_url_project` (28,270 bản ghi):** Ánh xạ 1:1 mọi URL sang Project và Hub theo danh mục chuẩn `hub-map.json`.
- **`dim_theme_seasonality` (236 bản ghi):** Chuỗi trọng số mùa vụ 12 tháng (5-year normalized average) của từng Theme.
- **`fact_daily_performance`:** Lũy kế hiệu suất MTD theo ngày (PV, Sessions, Users, Organic, Paid, Direct, Forecast, Target).
- **`ga4_landing_pages` (5,059 bản ghi):** Hiệu suất trang đích GA4, phân rã theo kênh và số lượt click OneLink (track1 + track2).
- **`gsc_search_analytics` (209,981 bản ghi):** Dữ liệu tìm kiếm tự nhiên: URL, Query, Clicks, Impressions, CTR, Position.
- **`gsc_keyword_ranking` (257,266 bản ghi):** Thứ hạng và điểm cơ hội từ khóa toàn bộ hệ sinh thái.
- **`decision_audit_trail`:** Sổ cái theo dõi quyết định chiến lược và đối soát kết quả sau 14 - 30 ngày.

### 3.2. Analytical Views:
- **`v_hub_performance`:** Tổng hợp Sessions, Engagement Rate, W2A Clicks, và W2A CVR (%) cho từng Hub.
- **`v_keyword_quick_wins`:** Tự động lọc từ khóa xếp hạng vị trí 4.0 - 15.0 có Impressions >= 500 và CTR < 5%.

---

## 4. BỘ CÔNG CỤ DÒNG LỆNH CHUYÊN BIỆT (CLI ENGINES & SCRIPTS)

Mọi thao tác phân tích, chẩn đoán và dự báo đều được tự động hóa qua các script Python đặt trong thư mục `scripts/`.  
**Yêu cầu bắt buộc:** Luôn gọi thông qua `./.venv/bin/python <script_path>`.

| Script | Mục đích nghiệp vụ | Lệnh thực thi mẫu |
| :--- | :--- | :--- |
| **`scripts/diagnose_performance.py`** | Chẩn đoán nguyên nhân gốc rễ (RCA) 4 bước: Hiện tượng -> Phân rã -> Nguyên nhân -> Đơn thuốc hành động kèm quét dị biệt. | `./.venv/bin/python scripts/diagnose_performance.py` |
| **`scripts/detect_anomalies.py`** | Quét 4 véc-tơ dị biệt: Nhịp độ MTD, UX Hub, đứt gãy OneLink W2A, rớt thứ hạng GSC. | `./.venv/bin/python scripts/detect_anomalies.py --severity CRITICAL` |
| **`scripts/query_analytics.py`** | Truy vấn dữ liệu đa chiều tức thì (<0.2s): Hubs, Top W2A Drivers, Quick Wins, Cannibalization hoặc SQL tự do. | `./.venv/bin/python scripts/query_analytics.py --hubs`<br>`./.venv/bin/python scripts/query_analytics.py --w2a` |
| **`scripts/prioritize_initiatives.py`** | Tự động chấm điểm RICE và phân loại ưu tiên P0/P1/P2 dựa trên dữ liệu Search Console thực tế. | `./.venv/bin/python scripts/prioritize_initiatives.py --limit 15` |
| **`scripts/lib/scenario_simulator.py`** | Mô phỏng kịch bản What-If: Dịch chuyển Hub, Cắt giảm Paid Ads, Tối ưu CTR Title/Meta, Nâng CVR phễu UX. | `./.venv/bin/python scripts/lib/scenario_simulator.py --scenario all` |
| **`scripts/lib/ab_test_evaluator.py`** | Kiểm định ý nghĩa thống kê A/B test (Z-test, P-value, 95% CI) và tính toán cỡ mẫu tối thiểu cần thiết (MDE). | `./.venv/bin/python scripts/lib/ab_test_evaluator.py --na 50000 --xa 500 --nb 50000 --xb 650` |
| **`scripts/lib/forecast_engine.py`** | Dự báo kết tháng đa kịch bản (Linear, Seasonality Weighted, Conservative) dựa trên trọng số mùa vụ 5 năm. | `./.venv/bin/python scripts/lib/forecast_engine.py --forecast` |
| **`scripts/track_decisions.py`** | Sổ cái theo dõi quyết định chiến lược, tự động đối soát kết quả thực tế sau 14 - 30 ngày (Closed-Loop). | `./.venv/bin/python scripts/track_decisions.py --list`<br>`./.venv/bin/python scripts/track_decisions.py --audit` |
| **`scripts/sync_ga4_master.py`** | Kéo số liệu GA4 MTD trực tiếp từ API, cập nhật Excel, Markdown, Hubs `/dashboard` và Google Sheets SSOT. | `./.venv/bin/python scripts/sync_ga4_master.py` |
| **`scripts/sync_cinema_roadmap_sheet.py`** | Đồng bộ hai chiều Google Sheet Roadmap Cinema Hub (ID `1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg`) và Google Drive Desktop. | `./.venv/bin/python scripts/sync_cinema_roadmap_sheet.py` |
| **`scripts/sync_data_mart.py`** | Nạp và đồng bộ lại toàn bộ dữ liệu 28k URLs, 236 theme mùa vụ và snapshots vào SQLite Data Mart. | `./.venv/bin/python scripts/sync_data_mart.py` |

---

## 5. NGUYÊN TẮC VẬN HÀNH DÀNH RIÊNG CHO AI AGENTS (MANDATORY RULES)

Trước khi xử lý yêu cầu, Agent phải đọc `AGENT_OPERATING_CONTRACT.md`, sau đó tra capability tương ứng trong `00_HARNESS_CORE/AGENT_CAPABILITIES.yaml`. Các thao tác ghi hoặc đồng bộ bên ngoài tuân thủ `00_HARNESS_CORE/AGENT_SAFETY_CONTRACT.yaml` và `00_HARNESS_CORE/AGENT_OUTPUT_CONTRACT.md`.

Bất kỳ AI Agent nào khi đọc hiểu và làm việc trong repo này **BẮT BUỘC TUÂN THỦ 100% CÁC QUY TẮC SAU**:

### 5.1. Chế độ vận hành: Problem -> Optimal Answer (Không tự động chạy lan man)
- Không tự ý triển khai, không chạy tác vụ dài hơi khi chưa được yêu cầu rõ.
- Luôn suy nghĩ với Chain of Thought: Phân tích bản chất -> Dẫn chứng số liệu -> Kết luận và Đơn thuốc hành động cụ thể.

### 5.2. Chuẩn mực Ngôn ngữ & Văn phong (Writing Style Constraints):
- **Phong cách:** Thực tế, cô đọng, sắc bén, chuẩn mực Product Lead / Tech Lead. Đi thẳng vào bản chất và gạch đầu dòng.
- **TUYỆT ĐỐI KHÔNG DÙNG CÁC TỪ:** "sàn", "sàn Web", "toàn sàn". Bắt buộc chỉ dùng: **"Kênh Web"**, **"toàn Website"**, **"nền tảng Web"**, **"Web Platform"** hoặc **"Web"**.
- **TUYỆT ĐỐI KHÔNG dùng Emoji / Icon:** Trong tiêu đề, bảng biểu, danh sách của các bài báo cáo, phân tích và tài liệu kỹ thuật.
- **TUYỆT ĐỐI KHÔNG đề cập tên riêng cá nhân / PIC:** Thay thế bằng tên đội ngũ chuyên môn (`Web Dev`, `SEO Vendor`, `Content Team`, `Product Lead`, `Media Team`...).
- **Không văn chương sáo rỗng kiểu AI:** Tránh các từ ngữ như *"bệ phóng phát triển"*, *"bứt phá ngoạn mục"*, *"hành trình chuyển đổi"*.

### 5.3. Quy tắc phân loại nguồn lưu lượng (Traffic Dichotomy SSOT):
- Luôn chia tách rõ rệt 2 nhóm lớn:
  1. **Non-Paid Traffic (Tự nhiên - Bền vững):** Gồm `Organic Search`, `Direct`, `Referral`, `Others`. Đây là động cơ tăng trưởng cốt lõi của Web Platform.
  2. **Paid Traffic (Quảng cáo):** Gồm `Paid Search`, `Google Ads`, `Campaign Ads`.
- Không liệt kê Paid nằm xen kẽ ngang hàng giữa các kênh tự nhiên trong bảng số liệu.

### 5.4. Quy tắc Môi trường Thực thi (Python Runtime SSOT):
- Tuyệt đối không dùng lệnh `python` hoặc `python3` trần (tránh việc macOS tự fallback về Python 3.9 hệ thống gây thiếu thư viện `underthesea`, `pytrends`).
- Bắt buộc gọi trực tiếp qua môi trường ảo: `./.venv/bin/python <script_path>`.

---

## 6. CHEAT SHEET: BẢNG TRA CỨU HÀNH ĐỘNG NHANH CHO AGENT

| Khi Người Dùng Yêu Cầu... | Hành Vi Chuẩn Xác Của Agent |
| :--- | :--- |
| **Chẩn đoán hiệu suất, tìm nguyên nhân tụt traffic** | Chạy ngay: `./.venv/bin/python scripts/diagnose_performance.py` |
| **Quét dị biệt, kiểm tra URL rớt hạng hoặc đứt gãy OneLink** | Chạy ngay: `./.venv/bin/python scripts/detect_anomalies.py` |
| **Tra cứu số liệu Hubs, Top trang chuyển đổi W2A** | Chạy ngay: `./.venv/bin/python scripts/query_analytics.py --hubs` hoặc `--w2a` |
| **Lập danh sách ưu tiên tối ưu từ khóa / Quick Wins** | Chạy ngay: `./.venv/bin/python scripts/prioritize_initiatives.py --limit 15` |
| **Mô phỏng kịch bản What-If (cắt Ads, đổi nguồn lực Hubs)** | Chạy ngay: `./.venv/bin/python scripts/lib/scenario_simulator.py --scenario all` |
| **Đánh giá kết quả A/B Test hoặc tính cỡ mẫu** | Chạy ngay: `./.venv/bin/python scripts/lib/ab_test_evaluator.py [tham số]` |
| **Kiểm tra sổ cái quyết định và tiến độ thực tế** | Chạy ngay: `./.venv/bin/python scripts/track_decisions.py --list` |
| **Đồng bộ số liệu GA4 MTD mới nhất** | Chạy ngay: `./.venv/bin/python scripts/sync_ga4_master.py` |
| **Đồng bộ / Kiểm tra Roadmap & Minigame Cinema Hub (Google Drive)** | Chạy ngay: `./.venv/bin/python scripts/sync_cinema_roadmap_sheet.py` |
| **Kiểm tra tình hình chiến dịch Paid Ads / UTM** | Chạy ngay: `./.venv/bin/python scripts/sync_paid_ads.py` |
| **Hỏi kỹ thuật, code review, debug, logic thông thường** | **Zero context file load**. Trả lời trực tiếp vào trọng tâm, không nạp file bối cảnh lớn. |
