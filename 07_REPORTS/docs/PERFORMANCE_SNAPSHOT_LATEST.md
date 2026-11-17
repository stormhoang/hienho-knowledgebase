# BẢN GHI TÓM TẮT HIỆU SUẤT MỚI NHẤT (PERFORMANCE SNAPSHOT)

> **Cập nhật:** 17/11/2026 | **Kỳ dữ liệu:** Tháng 11/2026 (MTD 16 ngày: 01/11 - 16/11/2026, Chuẩn hóa BigQuery DWH SSOT `WEB_L4_EVENT_PAGE_MASTER` & GA4 Data API)
> **Chính sách dữ liệu:** Đã loại bỏ hoàn toàn domain đối tác napthengay.vn; chuẩn hóa theo cơ chế khử trùng lặp `DISTINCT event_id` của BigQuery SSOT tập đoàn (2.861.286 PV).
> **Nguồn:** `07_REPORTS/data/monthly_11_2026_mtd_16d.json` & `07_REPORTS/data/summary.json`
> **Mục đích:** Bản ghi tinh gọn (Low-token) giúp AI Agents và quy trình tự động đọc số liệu nhanh mà không cần tải toàn bộ tài liệu lịch sử.

---

## 1. CHỈ SỐ TOÀN NỀN TẢNG (PLATFORM TOTALS)

| Chỉ số | Giá trị | Ghi chú & Đánh giá |
| :--- | :---: | :--- |
| **Target Tháng 11** | 3.829.155 PVs | Chỉ tiêu giao đầu tháng |
| **Thực tế Lũy kế MTD 16 ngày (BigQuery SSOT)** | **2.861.286 PVs** | Đạt **74.72%** Target (sau 53.33% thời gian) |
| **Nhịp vận hành ngày (Daily Pace)** | **178.830 PV/ngày** | Duy trì tiến độ hoàn thành kế hoạch tháng an toàn |
| **Forecast cuối tháng (Forecast 30d)** | **5.364.911 PVs** | Dự báo đạt **140.11%** Target |
| **Tháng 10 gần nhất (Last Full)** | 3.618.356 PVs | Hoàn thành ~98.7% Target Tháng 10 (3.665.607 PVs) |
| **Users / Sessions MTD 16d (www.momo.vn)** | 842.989 / 1.098.482 | Tỷ lệ sessions/user ~1.30 |

---

## 2. CƠ CẤU NGUỒN LƯU LƯỢNG (NON-PAID VS. PAID DICHOTOMY)

> **Quy chuẩn chuẩn hóa:** Tách riêng 2 khối độc lập **Paid** (Marketing trả phí) và **Non-Paid** (Lưu lượng tự nhiên); trong đó Non-Paid gồm 4 kênh cốt lõi: Organic, Direct, AI Traffic (bóc tách từ GA4 AI Assistant) và Referral (đã gộp toàn bộ mạng xã hội tự nhiên, đối tác PR, Unassigned).

| Phân Loại Traffic Source | Lũy kế MTD 16d (PVs) | Tỷ trọng (%) | Xu hướng & Đánh giá Tín hiệu |
| :--- | :---: | :---: | :--- |
| **NON-PAID TRAFFIC** | **2.246.310** | **78.51%** | Động cơ tăng trưởng cốt lõi trên website momo.vn |
| -- Organic Search | 1.307.096 | 45.68% | Kênh tìm kiếm tự nhiên chủ lực |
| -- Direct Traffic | 732.391 | 25.60% | Lượng truy cập trực tiếp |
| -- Referral *(đã gộp Phần còn lại)* | 206.823 | 7.23% | Đối tác/backlink, in-app, PR, Organic Social (130.973 Ref + 75.850 Others) |
| -- AI Traffic (GEO, tính trong Non-Paid) | 21.151 | 0.74% | Lượng truy cập từ các nền tảng AI |
| **PAID TRAFFIC** | **614.976** | **21.49%** | Ngân sách Ads trên website momo.vn |
| **TỔNG LƯU LƯỢNG (BigQuery SSOT)** | **2.861.286** | **100.00%** | Khớp 100% Data Warehouse tập đoàn |

---

## 3. CƠ CẤU THEO 4 ZONES & HUBS (HUBS-MOMO MAPPING)

| Zone Phân loại | Hub | Lũy kế MTD 16d (PVs) | Target Tháng 11 | % Đạt Target |
| :--- | :--- | :---: | :---: | :---: |
| **Performance** | **Cinema Hub** | 693.106 | 1.294.630 | **53.54%** |
| **Transformation** | **Financial Hub** | 297.482 | 700.000 | **42.50%** |
| **Transformation** | **Vehicle Hub** | 225.172 | 100.000 | **225.17%** |
| **Transformation** | **New User Hub** | 167.037 | 300.000 | **55.68%** |
| **Incubator** | **Insurance Hub** | 70.864 | 50.000 | **141.73%** |
| **Incubator** | **Student Hub** | 2.476 | 100.000 | **2.48%** |

### Cơ Cấu Sub-pages Cinema Hub (Quy Chuẩn Tracking Mới):
- **Trang Rạp phim (`Cinema_Cineplex`):** **468.528 PVs** (67.6% Hub)
- **Trang phim chi tiết (`Cinema_Page`):** **150.609 PVs** (21.7% Hub)
- **Cinema_Home Page (Trang chủ Cinema):** **44.177 PVs** (6.4% Hub)
- **Cinema_Blog:** **26.931 PVs** (3.9% Hub)
- **Cinema_Landing Page:** **2.328 PVs** (0.3% Hub)
- **Tin tức (`Cinema_News`):** **533 PVs** (0.1% Hub)

---

## 4. TÍN HIỆU KỸ THUẬT & HỒ SƠ TÊN MIỀN (TECHNICAL SEO SIGNALS)

> **Trạng thái:** Số liệu dưới đây là export kỳ **10/2026**, CHƯA có export GSC mới cho T11. Chỉ dùng tham chiếu xu hướng, không kết luận hiện trạng.

- **GSC Crawl Stats (01/10 - 06/10/2026):**
  * Tốc độ: **14.850 req/ngày** (sụt giảm **-29.7%** so với Tháng 9; Download giảm -72%).
  * Mã trạng thái: 200 OK đạt 94.11%; **404 Not Found chiếm 4.14%** (lãng phí ~860 req/ngày).
  * Mục đích: Refresh 95.97% / **Discovery chỉ 4.03%** (bị chèn ép nội dung mới).
  * Rủi ro: Lag 2-6 tuần; tác động sụt giảm crawl dự kiến bộc lộ vào Organic traffic cuối T10/đầu T11 - **cần kiểm chứng trên số liệu T11**.
- **GSC Backlink Profile (10/10/2026):**
  * Quy mô: 1.000 referring sites, 118.757 linking pages.
  * Tập trung cực đoan: Top 2 site (TopCV + CVS) chiếm **79.9%** linking pages.
  * Authority bẫy: 94.925 link trỏ vào 7-11 URL careers, 0 link trỏ vào Hub thương mại.
  * Disavow Audit: **147 domain candidate** (353 linking pages), trong đó có 67 site cờ bạc/casino (A1 Gambling).

---

## 5. PHỄU CHUYỂN ĐỔI WEB-TO-APP (NEW USER ACQUISITION - APPSFLYER GPD)

> **Nguồn:** `07_REPORTS/data/analytics/gpd_momo_web_nov_2026.csv` | **Kỳ dữ liệu:** 01/11/2026 - 10/11/2026 (MTD 10 ngày)

| Tầng Phễu Chuyển Đổi | Lũy Kế MTD 10d | Nhịp Ngày (Daily Pace) | Dự Báo 30 Ngày | So Với T10 (Full: 11.143) | Đánh Giá Tín Hiệu |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Cài đặt ứng dụng (App Install)** | **3.171** | 317 lượt/ngày | 9.513 | -14,6% vs T10 | Tải app ổn định, nhịp đạt 317 lượt/ngày |
| **2. Đăng ký tài khoản (New Reg)** | **864** | 86 user/ngày | 2.592 | -33,6% vs T10 | CVR Install -> REG đạt 27,2% |
| **3. Liên kết ngân hàng (Map Bank)** | **533** | 53 user/ngày | **1.599** | -33,1% vs T10 | CVR REG -> Map giữ vững 61,7% (tương đương T10: 61,2%) |
| **4. Người dùng kích hoạt (Active MAU)** | **314** | 31 user/ngày | 942 | -26,6% vs T10 | Tỷ lệ kích hoạt đạt 58,9% trên Map Bank |

### Cơ Cấu Phễu Theo Nhóm Chiến Dịch (Campaign Placement):
| Nhóm Kênh / Placement | Installs | Tỷ Trọng | REG | CVR REG | Map Bank | CVR Map | Active MAU | End-to-End CVR |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **C.CHAOMOMO (Banner đại trà)** | 2.763 | 87,1% | 772 | 27,9% | 479 | 62,0% | 275 | 10,0% |
| **Cinema Hub (Rạp phim & Lotte)** | 224 | 7,1% | 58 | 25,9% | 38 | 65,5% | 27 | 12,1% |
| **WEB_BRT_C.CHAOMOMO (Đổi quà)** | 58 | 1,8% | 16 | 27,6% | 8 | 50,0% | 5 | 8,6% |
| **Bảo Hiểm (InsurTech)** | 53 | 1,7% | 13 | 24,5% | 6 | 46,2% | 5 | 9,4% |
| **Merchant Hub (Đối tác)** | 42 | 1,3% | 3 | 7,1% | 1 | 33,3% | 1 | 2,4% |
| **Financial Health** | 31 | 1,0% | 2 | 6,5% | 1 | 50,0% | 1 | 3,2% |
| **TỔNG CỘNG MTD 10 NGÀY** | **3.171** | **100,0%** | **864** | **27,2%** | **533** | **61,7%** | **314** | **9,9%** |

- **Phân bổ theo hệ điều hành:** Android đạt 1.651 Installs (52,1%) / 238 Map Bank (CVR 53,8%); iOS đạt 1.520 Installs (47,9%) / 295 Map Bank (CVR 69,9%, End-to-End CVR đạt 12,2% so với Android là 7,8%).
- **Điểm sáng Cinema Hub:** End-to-End CVR đạt 12,1%, dẫn đầu toàn bộ các nhóm vị trí đặt.
