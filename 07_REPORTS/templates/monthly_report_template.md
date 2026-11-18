# BÁO CÁO KINH DOANH & HIỆU SUẤT THÁNG [MM/YYYY] - WEB PLATFORM

> **Phân loại:** Monthly Business Review (Pre-read: `[R]`, Thảo luận: `[D]`, Tham khảo: `[F]`)  
> **Nguyên tắc:** Report để cung cấp thông tin, Meeting để thảo luận và ra quyết định.  
> **Quy chuẩn áp dụng:** `03_SKILLS/momo-reporting-guidelines.md`  
> **Thời gian dữ liệu:** [01/MM] - [DD/MM/YYYY] (MTD [X] ngày)  
> **Tháng báo cáo:** Xác định theo kỳ dữ liệu, không theo thời điểm gửi.  
> **Nguồn SSOT:** `07_REPORTS/data/summary.json` & `07_REPORTS/web_performance_tracking.xlsx` (Sync với hubs-momo)  
> **Nguồn | Owner | Chốt số liệu:** [BU] | [tên] | [dd/mm/yyyy]  

---

## 1. CHỦ ĐỀ THẢO LUẬN BAN GIÁM ĐỐC (DISCUSSION TOPICS) `[D]`

> **Mục đích:** Nội dung cần thảo luận hoặc phê duyệt trong cuộc họp, và cần quyết định gì.

**Tiêu đề:** [n] chủ đề: [x] Discuss, [y] Approve

| # | Chủ đề | Loại | Cần CEO/BOM quyết định hoặc hỗ trợ gì | Tác động lượng hóa | Hạn | Ưu tiên | Chi tiết |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | [Chủ đề 1, một dòng] | Approve | [Duyệt ngân sách/chính sách/nhân sự X] | [x] tỷ revenue | [dd/mm] | CAO | Mục 1.1 |
| 2 | [Chủ đề 2, một dòng] | Discuss | [Thống nhất hướng đi giữa A và B] | [x]% KPI | [dd/mm] | TRUNG BINH | Mục 1.2 |

Tối đa 3-5 chủ đề. Chủ đề không cần quyết định thì chuyển sang `[R]` hoặc `[F]`.

### 1.1. [Chủ đề 1]: [vấn đề một câu kèm số liệu] - cần [Discuss/Approve] về [nội dung] `[D]`

> **Mục đích:** Trình bày vấn đề cần xin phê duyệt hoặc ý kiến.

- **Problem Statement:** [Vấn đề là gì, xảy ra ở đâu, quy mô bao nhiêu]
- **Bối cảnh:** [Vì sao xảy ra, đã thử gì, số liệu minh chứng]
- **Tác động:** [Revenue / cost / KPI / rủi ro, có lượng hóa]

| Phương án | Nội dung | Ưu điểm | Rủi ro / chi phí |
| :--- | :--- | :--- | :--- |
| A - [tên] | [mô tả ngắn] | [...] | [...] |
| B - [tên] | [mô tả ngắn] | [...] | [...] |

- **Đề nghị với CEO/BOM:** [nội dung cần thảo luận hoặc phê duyệt]
- **Khuyến nghị của BU:** Phương án [X] vì [lý do chính]
- **Nếu không quyết định:** [Hệ quả lượng hóa] nếu chậm quyết định sau [dd/mm]

---

## 2. THEO DÕI ACTION KỲ TRƯỚC (FOLLOW-UP) `[R]`

> **Mục đích:** Theo dõi kết quả xử lý các action từ cuộc họp trước để đảm bảo đóng vòng.

**Tiêu đề:** [x/y] action từ meeting minutes trước đã hoàn thành; [action trễ] cần hỗ trợ

| Action / quyết định kỳ trước | Owner | Hạn | Trạng thái | Cập nhật mới nhất |
| :--- | :--- | :---: | :---: | :--- |
| [Action 1] | [Đội ngũ] | [dd/mm] | Hoàn thành | [Kết quả + số liệu] |
| [Action 2] | [Đội ngũ] | [dd/mm] | Đang làm | [Tiến độ, vướng mắc] |
| [Action 3] | [Đội ngũ] | [dd/mm] | Trễ | [Nguyên nhân, hạn mới] |

Action còn mở mà cần quyết định thì đưa lên mục 1.

---

## 3. TÓM TẮT ĐIỀU HÀNH (EXECUTIVE SUMMARY) `[R]`

> **Mục đích:** Cho Ban Giám Đốc nắm kết quả tháng và vấn đề trọng yếu trong một trang.

**Điểm nổi bật**
- [Ý 1: số liệu + driver + tác động + việc tiếp theo]
- [Ý 2]
- [Ý 3]

**Vấn đề cần cải thiện**
- [Vấn đề 1: số liệu so Target + nguyên nhân + hướng xử lý + owner + hạn]
- [Vấn đề 2]

Khối thứ hai bắt buộc có nội dung.

---

## 4. TỔNG QUAN HIỆU SUẤT NỀN TẢNG (PLATFORM SUMMARY) `[R]`

> **Mục đích:** Cho thấy nền tảng Web đạt bao nhiêu phần trăm Target tháng và phần chênh lệch đến từ đâu.

| Chỉ số Cốt lõi | Tháng Trước (Full) | Tháng Này (Target) | Lũy Kế MTD ([X]d) | Forecast Cuối Tháng | Đánh Giá Tỷ Lệ Đạt |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Total Pageviews** | [pv_prev] | [target_month] | [actual_mtd] | [forecast_month] | **[%_target]** |
| **Tốc Độ Ngày (Pace)** | [pace_prev]/ngày | [req_pace]/ngày | [daily_pace]/ngày | - | [pace_status] |
| **Chênh Lệch (Net Add)** | - | - | - | [gap_pv] | [so_what_net_add] |

### Phân Bổ Kênh Lưu Lượng (Traffic Dichotomy Split):
#### 1. Kênh Tự Nhiên (Non-Paid Traffic):
- **Organic Search:** [pv_org] ([%_org]%) - [Đánh giá sức khỏe lưu lượng tìm kiếm tự nhiên]
- **Direct:** [pv_dir] ([%_dir]%) - [Đánh giá lượng truy cập tiện ích trực tiếp]
- **Referral:** [pv_ref] ([%_ref]%) - [Đánh giá luồng giới thiệu đối tác; toàn bộ nguồn vãng lai/nguồn khác gộp vào Referral, không tách dòng Others]
- **AI Traffic (GEO):** [pv_ai_traffic] ([%_ai]%) - [Đánh giá lưu lượng từ các công cụ AI Search / AI Engine: Perplexity, ChatGPT, Gemini, Copilot]

#### 2. Kênh Trả Phí (Paid Traffic):
- **Paid Ads:** [pv_paid] ([%_paid]%) - [Đánh giá hiệu quả ngân sách quảng cáo và co-marketing, tách biệt hoàn toàn khỏi kênh tự nhiên]

---

## 5. HIỆU SUẤT THEO 4 ZONES CHIẾN LƯỢC (HUBS-MOMO MAPPING) `[R]`

> **Mục đích:** Cho thấy hub nào đang kéo tăng trưởng, hub nào hụt Target và vì sao.

### A. Performance Zone: Cinema Hub
- **Lưu lượng MTD:** [pv_cinema] PVs / Target [target_cinema] PVs (Forecast: [fc_cinema] PVs - **[%_cinema]%**)
- **Key Highlights:** [Tối ưu CWV LCP, Mini Game tương tác, tiến độ migration rạp]
- **Next Shipments:** [Đầu việc cam kết ship trong tuần kế tiếp]

### B. Transformation Zone: Financial, Vehicle & New User Hubs
- **Financial Hub:** [pv_fin] PVs / Target [target_fin] PVs (Forecast: [fc_fin] PVs - **[%_fin]%**)
  * *Tiến độ công cụ:* [Trang chủ /tai-chinh, sub-pages tỷ giá, giá vàng, tích hợp API CCQ & tiết kiệm]
- **Vehicle Hub:** [pv_veh] PVs / Target [target_veh] PVs (Forecast: [fc_veh] PVs - **[%_veh]%**)
  * *Tiến độ:* [Trang Model xe Vinfast, API Phạt Nguội, Database Garage Cell Team]
- **New User Hub:** [pv_nu] PVs / Target [target_nu] PVs (Forecast: [fc_nu] PVs - **[%_nu]%**)
  * *Phễu Web-to-App:* [Game Quýt 2D/3D, cải tiến trang Download & Bonbon]

### C. Foundation Zone: Payment Hub
- **Lưu lượng MTD:** [pv_payment] PVs - [Game, Tiktok, Billpay, P2P, Data...] vận hành ổn định.

### D. Incubator Zone: Student & Travel Hubs
- **Student Hub:** [pv_student] PVs / Target [target_student] PVs - [Tiến độ gói hội viên sinh viên]
- **Travel Hub:** [pv_travel] PVs - [Tiến độ vé máy bay, vé tàu, khách sạn, eSIM]

---

## 6. TÍN HIỆU KỸ THUẬT & TÊN MIỀN (TECHNICAL SIGNALS) `[F]`

> **Mục đích:** Tham khảo, không thảo luận trong họp. Nêu rủi ro nền tảng có thể ảnh hưởng lưu lượng các tháng tới.

- **GSC Crawl Budget:** [req_per_day] req/ngày (Biến động: [delta_vs_last_month]%). Mã 200 OK đạt [pct_200]%; lãng phí 404 là [pct_404]% (~[wasted_req]/ngày). Tỷ lệ Discovery: [pct_discovery]%.
- **Backlink Authority:** [total_linking_pages] pages từ [total_ref_domains] domains. Nồng độ Top 2 site: [pct_top2]%. Danh mục toxic link cần disavow: [total_disavow_candidates] domains.

---

## 7. KIỂM TRA TRƯỚC KHI GỬI

Rà theo checklist tại `03_SKILLS/web-platform-reporting-framework.md` mục 8, nhóm A trước nhóm B.

Các chủ đề cần Ban Giám Đốc quyết định nằm ở mục 1, đầu báo cáo, không đặt ở cuối.
