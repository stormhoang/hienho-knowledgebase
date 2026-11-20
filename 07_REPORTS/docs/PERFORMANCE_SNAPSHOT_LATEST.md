# BẢN GHI TÓM TẮT HIỆU SUẤT MỚI NHẤT (PERFORMANCE SNAPSHOT)

> **Cập nhật:** 20/11/2026 | **Kỳ dữ liệu:** Tháng 11/2026 (MTD 19 ngày hoàn chỉnh: 01/11 - 19/11/2026, Luồng nạp dữ liệu thô hàng ngày từ GA4 Explore CSV)
> **Chính sách dữ liệu:** Đã loại bỏ hoàn toàn domain đối tác napthengay.vn; chuẩn hóa theo cơ chế neo nền tảng BigQuery SSOT 16 ngày (2.861.286 PV) cộng dồn phát sinh mới 3 ngày 17-19/11; restate 20/11/2026: cộng thêm 22.684 PV AI Traffic vào Non-Paid và tổng PV (canonical schema) đạt tổng cộng 3.255.620 PV.
> **Nguồn:** `07_REPORTS/data/monthly/monthly_11_2026_mtd_19d.json` & `07_REPORTS/data/summary.json`
> **Mục đích:** Bản ghi tinh gọn (Low-token) giúp AI Agents và quy trình tự động đọc số liệu nhanh mà không cần tải toàn bộ tài liệu lịch sử.

---

## 1. CHỈ SỐ TOÀN NỀN TẢNG (PLATFORM TOTALS)

| Chỉ số | Giá trị | Ghi chú & Đánh giá |
| :--- | :---: | :--- |
| **Target Tháng 11** | 3.829.155 PVs | Chỉ tiêu giao đầu tháng |
| **Thực tế Lũy kế MTD 19 ngày (BigQuery SSOT + Lũy kế)** | **3.255.620 PVs** | Đạt **85.02%** Target (sau 63.33% thời gian) |
| **Nhịp vận hành ngày (Daily Pace)** | **171.348 PV/ngày** | Duy trì tiến độ hoàn thành kế hoạch tháng an toàn |
| **Forecast cuối tháng (Forecast 30d)** | **5.140.453 PVs** | Dự báo đạt **134.25%** Target |
| **Tháng 10 gần nhất (Last Full)** | 3.618.356 PVs | Hoàn thành ~98.7% Target Tháng 10 (3.665.607 PVs) |
| **Users / Sessions MTD 19d (www.momo.vn)** | 960.337 / 1.275.577 | Tỷ lệ sessions/user ~1.33 |

---

## 2. CƠ CẤU NGUỒN LƯU LƯỢNG (NON-PAID VS. PAID DICHOTOMY)

> **Quy chuẩn chuẩn hóa:** Tách riêng 2 khối độc lập **Paid** (Marketing trả phí) và **Non-Paid** (Lưu lượng tự nhiên); trong đó Non-Paid gồm 4 kênh cốt lõi: Organic, Direct, AI Traffic (bóc tách từ GA4 AI Assistant) và Referral (đã gộp toàn bộ mạng xã hội tự nhiên, đối tác PR, Unassigned).

| Phân Loại Traffic Source | Lũy kế MTD 19d (PVs) | Tỷ trọng (%) | Xu hướng & Đánh giá Tín hiệu |
| :--- | :---: | :---: | :--- |
| **NON-PAID TRAFFIC** | **2.544.804** | **78.17%** | Động cơ tăng trưởng cốt lõi trên website momo.vn |
| -- Organic Search | 1.455.898 | 44.72% | Kênh tìm kiếm tự nhiên chủ lực |
| -- Direct Traffic | 823.795 | 25.30% | Lượng truy cập trực tiếp |
| -- Referral *(đã gộp Phần còn lại)* | 241.660 | 7.42% | Đối tác/backlink, in-app, PR, Organic Social (156.437 Ref + 85.223 Others) |
| -- AI Traffic (GEO, tính trong Non-Paid) | 23.451 | 0.72% | Lượng truy cập từ các nền tảng AI |
| **PAID TRAFFIC** | **710.816** | **21.83%** | Ngân sách Ads trên website momo.vn |
| **TỔNG LƯU LƯỢNG** | **3.255.620** | **100.00%** | Đã restate gồm AI Traffic trong Non-Paid và tổng PV |

---

## 3. CƠ CẤU THEO 4 ZONES & HUBS (HUBS-MOMO MAPPING)

| Zone Phân loại | Hub | Lũy kế MTD 19d (PVs) | Target Tháng 11 | % Đạt Target |
| :--- | :--- | :---: | :---: | :---: |
| **Performance** | **Cinema Hub** | 785.079 | 1.294.630 | **60.64%** |
| **Transformation** | **Financial Hub** | 330.996 | 700.000 | **47.29%** |
| **Transformation** | **Vehicle Hub** | 269.494 | 100.000 | **269.49%** |
| **Transformation** | **New User Hub** | 179.972 | 300.000 | **59.99%** |
| **Incubator** | **Insurance Hub** | 78.889 | 50.000 | **157.78%** |
| **Incubator** | **Student Hub** | 2.808 | 100.000 | **2.81%** |

### Cơ Cấu Sub-pages Cinema Hub (Quy Chuẩn Tracking Mới):
- **Trang Rạp phim (`Cinema_Cineplex`):** **525.721 PVs** (67.0% Hub)
- **Trang phim chi tiết (`Cinema_Page`):** **171.076 PVs** (21.8% Hub)
- **Cinema_Home Page (Trang chủ Cinema):** **49.088 PVs** (6.3% Hub)
- **Cinema_Blog:** **36.041 PVs** (4.6% Hub)
- **Cinema_Landing Page:** **2.560 PVs** (0.3% Hub)
- **Tin tức (`Cinema_News`):** **593 PVs** (0.1% Hub)

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

> **Nguồn:** `07_REPORTS/data/analytics/gpd_momo_web_nov_2026.csv` | **Kỳ dữ liệu:** 01/11/2026 - 19/11/2026 (MTD 19 ngày)

| Tầng Phễu Chuyển Đổi | Lũy Kế MTD 19d | Nhịp Ngày (Daily Pace) | Dự Báo 30 Ngày | So Với T10 (Full: 11.143) | Đánh Giá Tín Hiệu |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Cài đặt ứng dụng (App Install)** | **6.177** | 325 lượt/ngày | 9.753 | -12,5% vs T10 | Nhịp cài đặt tăng tốc lên 325 lượt/ngày (so với 317 lượt/ngày ở MTD 10d) |
| **2. Đăng ký tài khoản (New Reg)** | **1.941** | 102 user/ngày | 3.065 | -21,5% vs T10 | CVR Install -> REG phục hồi lên 31,4% (so với 27,2% ở MTD 10d) |
| **3. Liên kết ngân hàng (Map Bank)** | **1.248** | 66 user/ngày | **1.971** | -17,5% vs T10 | CVR REG -> Map bứt phá lên 64,3% (vượt mức 61,2% của T10) |
| **4. Người dùng kích hoạt (Active MAU)** | **768** | 40 user/ngày | **1.213** | -5,5% vs T10 | Tỷ lệ kích hoạt đạt 61,5% trên Map Bank; End-to-End CVR đạt 12,4% (vượt T10: 11,5%) |

### Cơ Cấu Phễu Theo Nhóm Chiến Dịch (Campaign Placement):
| Nhóm Kênh / Placement | Installs | Tỷ Trọng | REG | CVR REG | Map Bank | CVR Map | Active MAU | End-to-End CVR |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **C.CHAOMOMO (Banner đại trà)** | 5.240 | 84,8% | 1.670 | 31,9% | 1.091 | 65,3% | 665 | 12,7% |
| **Cinema Hub (Rạp phim & Lotte)** | 419 | 6,8% | 140 | 33,4% | 92 | 65,7% | 60 | 14,3% |
| **WEB_BRT_C.CHAOMOMO (Đổi quà)** | 118 | 1,9% | 33 | 28,0% | 18 | 54,5% | 13 | 11,0% |
| **Bảo Hiểm (InsurTech)** | 111 | 1,8% | 40 | 36,0% | 14 | 35,0% | 10 | 9,0% |
| **Merchant Hub (Đối tác)** | 108 | 1,7% | 23 | 21,3% | 12 | 52,2% | 8 | 7,4% |
| **Một Mùa Quýt (Financial Health)** | 93 | 1,5% | 14 | 15,1% | 9 | 64,3% | 5 | 5,4% |
| **/tai-app (Landing Page Tải App Mới)** | 88 | 1,4% | 21 | 23,9% | 12 | 57,1% | 7 | 8,0% |
| **TỔNG CỘNG MTD 19 NGÀY** | **6.177** | **100,0%** | **1.941** | **31,4%** | **1.248** | **64,3%** | **768** | **12,4%** |

- **Phân bổ theo hệ điều hành:** Android đạt 3.255 Installs (52,7%) / 583 Map Bank (CVR Map/REG 58,0%) / 350 MAU (End-to-End CVR 10,8%); iOS đạt 2.922 Installs (47,3%) / 665 Map Bank (CVR Map/REG 71,1%) / 418 MAU (End-to-End CVR đạt 14,3%).
- **Điểm sáng chất lượng cao:** Cinema Hub duy trì End-to-End CVR ấn tượng 14,3% (riêng iOS Cinema đạt 16,2%), chứng minh tệp người dùng tra cứu vé rạp có động lực cài và giao dịch vượt trội.
- **Tín hiệu luồng mới `/tai-app` (Test Campaign):** Đạt 88 Installs (68 Android, 20 iOS), chuyển đổi 21 REG, 12 Map Bank và 7 New MAU (End-to-End CVR 8,0%). Điểm rơi chuyển đổi nằm ở khâu Install -> REG (23,9%), cần tối ưu hóa onboarding để tăng tỷ lệ đăng ký.

---

## 6. BÓC TÁCH ĐỘNG LỰC TĂNG TRƯỞNG MOM (THÁNG 11 VS THÁNG 10 MTD 18 NGÀY)

> **Kỳ dữ liệu đối soát:** 01/11/2026 - 18/11/2026 vs 01/10/2026 - 18/10/2026 (18 ngày like-for-like)
> **Nguồn SSOT:** `07_REPORTS/data/analytics/mom_growth_drivers_11_vs_10_18d.json`
> **Kết luận chủ đạo:** Lũy kế MTD 18 ngày Tháng 11 đạt **3.124.987 PV** (đã restate gồm AI Traffic), tăng **+980.294 PV (+45,70% MoM)** so với mức **2.144.693 PV** cùng kỳ Tháng 10. Mức tăng trưởng ròng phân bổ giữa Non-Paid (+520K PV, chiếm 53,0%) và Paid (+461K PV, chiếm 47,0%).

### 6.1 Biến động theo kênh lưu lượng (Channel Delta):
| Kênh lưu lượng | MTD 18d T10 | MTD 18d T11 | Biến động tuyệt đối | % MoM | Đóng góp vào mức tăng |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **NON-PAID (Tự nhiên)** | **1.930.753 PV** | **2.450.534 PV** | **+519.781 PV** | **+26,92%** | **53,02%** |
| - Organic Search | 1.142.226 PV | 1.403.639 PV | +261.413 PV | +22,89% | 26,66% |
| - Direct Traffic | 535.574 PV | 796.552 PV | +260.978 PV | +48,73% | 26,62% |
| - AI Traffic (GEO) | 8.379 PV | 22.684 PV | +14.305 PV | +170,72% | 1,46% |
| - Referral & Khác | 244.574 PV | 204.975 PV | -39.599 PV | -16,19% | -4,13% |
| **PAID TRAFFIC (Quảng cáo)** | **213.940 PV** | **674.453 PV** | **+460.513 PV** | **+215,25%** | **46,98%** |
| **TỔNG LƯU LƯỢNG TOÀN WEBSITE** | **2.144.693 PV** | **3.124.987 PV** | **+980.294 PV** | **+45,70%** | **100,00%** |

### 6.2 Top dự án và trang đích có mức tăng trưởng lớn nhất (Top Gainers):
1. **Cụm Tiện ích Tra cứu Phạt Nguội (Vehicle Hub): Tăng +187.292 PV**
   - `/phat-nguoi/o-to`: Tăng +117.756 PV (từ 491 lên 118.247 PV).
   - `/phat-nguoi/xe-may`: Tăng +69.536 PV (từ 524 lên 70.060 PV).
   - Động lực: Chiến dịch Google Search Ads `tracuuphatnguoi` (+187K PV) kết hợp SEO leo top 1-3 SERP.
2. **Tiện ích Nạp Xu TikTok (`/nap-xu-tiktok`): Tăng +180.524 PV**
   - Từ 120.435 lên 300.959 PV (+149,9%). Thúc đẩy bởi Google Ads SEM và nhu cầu nạp xu xem livestream mua sắm cuối năm.
3. **Trang chủ momo.vn (`/`): Tăng +180.523 PV**
   - Từ 170.728 lên 351.251 PV (+105,7%). Tăng chủ yếu qua Direct (+110K PV) và Organic (+53K PV) nhờ nhận diện thương hiệu dịp lễ hội 11.11.
4. **Dàn Phim Chiếu Rạp Mới Tháng 11 (Cinema Hub): Tăng hơn +150.000 PV**
   - Loạt phim mới ra mắt: *Ngày còn con mẹ* (+43.632 PV), *Bò sữa bay* (+29.294 PV), *Chị chị em em 3* (+27.415 PV), *Godzilla trừ không* (+26.193 PV).
5. **Minigame & Chiến dịch Khuyến mại Mùa vụ: Tăng +177.721 PV**
   - Minigame Một Mùa Quýt (`/game/mot-mua-quyt`): Tăng +90.373 PV.
   - Siêu Sale Du Lịch 11.11: Đóng góp +38.967 PV.
   - Giới thiệu bạn bè (MGM): Tăng +28.205 PV.
6. **Khách hàng Doanh nghiệp & Bảo hiểm (Merchant & InsurTech): Tăng +104.367 PV**
   - Loa thông báo chuyển khoản (`/loa-thong-bao-chuyen-khoan`): Tăng +64.106 PV.
   - Tra cứu Bảo hiểm Y tế bằng CCCD (`/blog/tra-cuu-bao-hiem-y-te-bang-cccd-c116dt2833`): Tăng +40.261 PV (gấp 4,4 lần).
   - Thanh toán hóa đơn nước (`/nuoc`): Tăng +59.518 PV.

### 6.3 Ba nguyên nhân cốt lõi (Root Cause):
1. **Google Search Ads đúng nhu cầu nóng (SEM Intent):** BU Vehicle và BU TikTok/Game mở rộng ngân sách quảng cáo tìm kiếm có chủ đích (`tracuuphatnguoi` +187K PV, `TikTok Coin` +145K PV).
2. **Năng lực SEO tự nhiên leo Top SERP (Organic SEO):** Trang Tra cứu BHYT CCCD và Phạt Nguội giữ top 1-3 Google, mang về lượng truy cập tự nhiên lớn mà không tốn chi phí duy trì.
3. **Tính mùa vụ cuối năm và phát hành phim:** Chu kỳ thanh toán hóa đơn giữa tháng cộng hưởng với lễ hội mua sắm 11.11 và loạt phim rạp gia đình/bom tấn ra mắt đầu tháng 11.

---

## 7. CƠ SỞ ĐỐI SOÁT VĨ MÔ DÀI HẠN (ANNUAL MACRO BASELINE: 10/2025 - 11/2026)

> **Nguồn trích xuất:** File GA4 Explore chính thức `/Users/hienhv/Downloads/download (1).csv`  
> **Quy mô ghi nhận:** 100.000 dòng dữ liệu tối đa | Tổng cộng **45.305.639 lượt xem trang (Views)**  
> **Tệp dữ liệu SSOT lưu trữ:** `07_REPORTS/data/analytics/ga4_macro_annual_baseline_2025_2026.json`

### 7.1 Phân bổ theo năm và cơ cấu kênh năm 2026:
- **Năm 2025 (Q4):** 8.421.827 Views (chiếm 18,73%).
- **Năm 2026 (10,5 tháng đến 19/11):** 36.535.137 Views (chiếm 81,27%).
- **Cơ cấu kênh năm 2026:**
  * **Lưu lượng tự nhiên (Non-Paid):** **27.661.366 Views (75,71%)**
    - Organic Search: 17.929.822 Views (49,08% toàn Website).
    - Direct Traffic: 6.377.679 Views (17,46%).
    - App Referral: 2.627.612 Views (7,19%).
    - Organic Social: 607.405 Views (1,66%).
    - AI Referrals: 118.848 Views (0,33%).
  * **Lưu lượng trả phí (Paid Ads):** **7.741.673 Views (21,19%)**
    - Paid Search (Google SEM): 5.609.097 Views (15,35%).
    - Paid Social (Facebook Ads): 1.773.357 Views (4,85%).
    - Cross-network (PMax): 198.601 Views (0,54%).
    - Paid Other: 160.618 Views (0,44%).
  * **Chưa phân loại (Unassigned):** 1.110.253 Views (3,04%).

### 7.2 Top trang đích tích lũy lớn nhất năm 2026:
1. Trang chủ (`/`): 2.715.967 Views (7,43%).
2. Cổng tải ứng dụng (`/download`): 2.636.679 Views (7,22%).
3. Nạp xu TikTok (`/nap-xu-tiktok`): 2.213.035 Views (6,06%).
4. Khuyến mại Nạp game (`/tin-tuc/.../nap-game-sieu-hoi-8081`): 1.012.242 Views (2,77%).
5. Tra cứu Phạt nguội (`/phat-nguoi`): 977.412 Views (2,68%).
6. Ví Trả Sau (`/vi-tra-sau`): 887.599 Views (2,43%).
7. Vay Nhanh (`/vay-nhanh`): 716.201 Views (1,96%).
8. Hóa đơn nước (`/nuoc`): 439.092 Views (1,20%).

---

## 8. TOÀN CẢNH HIỆU SUẤT TÌM KIẾM GOOGLE SEARCH CONSOLE 2026 & PHÂN TẦNG THIẾT BỊ

> **Nguồn trích xuất:** Tệp Google Search Console chính thức `https___www.momo.vn_-Performance-on-Search-2026-11-19.zip`  
> **Dải thời gian:** 01/01/2026 đến 18/11/2026 (322 ngày liên tục) | Web Search (Text-based)  
> **Quy mô ghi nhận:** **10.765.499 Clicks** | **370.609.259 Lượt hiển thị (Impressions)** | CTR trung bình **2,90%** | Vị trí trung bình **6,32**  
> **Tệp dữ liệu SSOT lưu trữ:** `07_REPORTS/data/analytics/gsc_macro_performance_2026.json`

### 8.1 Phân bổ theo loại thiết bị (Device Breakdown):
- **Điện thoại (Mobile):** **9.424.737 Clicks (chiếm 87,55%)** | 291.138.641 Impressions (78,56%) | CTR: **3,24%** | Vị trí trung bình: **5,78**.
- **Máy tính (Desktop):** **1.269.085 Clicks (chiếm 11,79%)** | 75.827.254 Impressions (20,46%) | CTR: **1,67%** | Vị trí trung bình: **8,32**.
- **Máy tính bảng (Tablet):** **71.677 Clicks (chiếm 0,67%)** | 3.643.364 Impressions (0,98%) | CTR: **1,97%** | Vị trí trung bình: **8,04**.

### 8.2 Đóng góp lưu lượng tìm kiếm tự nhiên theo từng Hub nghiệp vụ:
1. **Cinema Hub:** 324 trang, mang về **3.849.618 clicks** (chiếm 35,76% toàn Web), 120,55M impressions, CTR 3,19%, Vị trí 7,04.
2. **Home MoMo:** 94 trang, mang về **1.152.117 clicks**, 23,50M impressions, CTR 4,90%, Vị trí 5,89.
3. **Financial Hub:** 107 trang, mang về **1.016.528 clicks**, 34,03M impressions, CTR 2,99%, Vị trí 7,46.
4. **Payment Hub:** 27 trang, mang về **951.216 clicks**, 28,62M impressions, CTR 3,32%, Vị trí 6,11.
5. **Game Hub:** 14 trang, mang về **674.075 clicks**, 23,18M impressions, CTR 2,91%, Vị trí 5,60.
6. **Support Hub:** 125 trang, mang về **634.203 clicks**, 14,08M impressions, CTR 4,50%, Vị trí 5,43.
7. **Travel Hub:** 93 trang, mang về **301.397 clicks**, 16,98M impressions, CTR 1,78%, Vị trí 6,81.
8. **Insurance Hub:** 34 trang, mang về **161.421 clicks**, 7,29M impressions, CTR 2,21%, Vị trí 7,57.
9. **Vehicle Hub:** 15 trang, mang về **101.851 clicks**, 1,95M impressions, CTR **5,22%** (dẫn đầu nhóm chuyên môn), Vị trí 4,30.
10. **New User Hub (bao gồm `/tai-app`):** 6 trang, mang về **67.725 clicks**, 2,37M impressions. Riêng `momo.vn/tai-app` đạt **1.858 clicks, 37.569 impressions, CTR 4,95% và Vị trí Top 1,91**.

