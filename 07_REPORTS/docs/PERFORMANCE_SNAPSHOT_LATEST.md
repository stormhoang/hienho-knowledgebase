# BẢN GHI TÓM TẮT HIỆU SUẤT MỚI NHẤT (PERFORMANCE SNAPSHOT)

> **Cập nhật:** 19/11/2026 | **Kỳ dữ liệu:** Tháng 11/2026 (MTD 18 ngày: 01/11 - 18/11/2026, Chuẩn hóa BigQuery DWH SSOT `WEB_L4_EVENT_PAGE_MASTER` & GA4 Data API)
> **Chính sách dữ liệu:** Đã loại bỏ hoàn toàn domain đối tác napthengay.vn; chuẩn hóa theo cơ chế neo nền tảng BigQuery SSOT 16 ngày (2.861.286 PV) cộng dồn phát sinh mới 2 ngày 17-18/11 (+241.017 PV) đạt tổng cộng 3.102.303 PV.
> **Nguồn:** `07_REPORTS/data/monthly_11_2026_mtd_18d.json` & `07_REPORTS/data/summary.json`
> **Mục đích:** Bản ghi tinh gọn (Low-token) giúp AI Agents và quy trình tự động đọc số liệu nhanh mà không cần tải toàn bộ tài liệu lịch sử.

---

## 1. CHỈ SỐ TOÀN NỀN TẢNG (PLATFORM TOTALS)

| Chỉ số | Giá trị | Ghi chú & Đánh giá |
| :--- | :---: | :--- |
| **Target Tháng 11** | 3.829.155 PVs | Chỉ tiêu giao đầu tháng |
| **Thực tế Lũy kế MTD 18 ngày (BigQuery SSOT + Lũy kế)** | **3.102.303 PVs** | Đạt **81.02%** Target (sau 60.00% thời gian) |
| **Nhịp vận hành ngày (Daily Pace)** | **172.350 PV/ngày** | Duy trì tiến độ hoàn thành kế hoạch tháng an toàn |
| **Forecast cuối tháng (Forecast 30d)** | **5.170.505 PVs** | Dự báo đạt **135.03%** Target |
| **Tháng 10 gần nhất (Last Full)** | 3.618.356 PVs | Hoàn thành ~98.7% Target Tháng 10 (3.665.607 PVs) |
| **Users / Sessions MTD 18d (www.momo.vn)** | 960.337 / 1.275.577 | Tỷ lệ sessions/user ~1.33 |

---

## 2. CƠ CẤU NGUỒN LƯU LƯỢNG (NON-PAID VS. PAID DICHOTOMY)

> **Quy chuẩn chuẩn hóa:** Tách riêng 2 khối độc lập **Paid** (Marketing trả phí) và **Non-Paid** (Lưu lượng tự nhiên); trong đó Non-Paid gồm 4 kênh cốt lõi: Organic, Direct, AI Traffic (bóc tách từ GA4 AI Assistant) và Referral (đã gộp toàn bộ mạng xã hội tự nhiên, đối tác PR, Unassigned).

| Phân Loại Traffic Source | Lũy kế MTD 18d (PVs) | Tỷ trọng (%) | Xu hướng & Đánh giá Tín hiệu |
| :--- | :---: | :---: | :--- |
| **NON-PAID TRAFFIC** | **2.427.850** | **78.26%** | Động cơ tăng trưởng cốt lõi trên website momo.vn |
| -- Organic Search | 1.403.639 | 45.25% | Kênh tìm kiếm tự nhiên chủ lực |
| -- Direct Traffic | 796.552 | 25.68% | Lượng truy cập trực tiếp |
| -- Referral *(đã gộp Phần còn lại)* | 227.659 | 7.34% | Đối tác/backlink, in-app, PR, Organic Social (149.430 Ref + 78.229 Others) |
| -- AI Traffic (GEO, tính trong Non-Paid) | 22.684 | 0.73% | Lượng truy cập từ các nền tảng AI |
| **PAID TRAFFIC** | **674.453** | **21.74%** | Ngân sách Ads trên website momo.vn |
| **TỔNG LƯU LƯỢNG (BigQuery SSOT + Lũy kế)** | **3.102.303** | **100.00%** | Khớp 100% Data Warehouse tập đoàn |

---

## 3. CƠ CẤU THEO 4 ZONES & HUBS (HUBS-MOMO MAPPING)

| Zone Phân loại | Hub | Lũy kế MTD 18d (PVs) | Target Tháng 11 | % Đạt Target |
| :--- | :--- | :---: | :---: | :---: |
| **Performance** | **Cinema Hub** | 747.924 | 1.294.630 | **57.77%** |
| **Transformation** | **Financial Hub** | 321.390 | 700.000 | **45.91%** |
| **Transformation** | **Vehicle Hub** | 255.329 | 100.000 | **255.33%** |
| **Transformation** | **New User Hub** | 175.752 | 300.000 | **58.58%** |
| **Incubator** | **Insurance Hub** | 76.102 | 50.000 | **152.20%** |
| **Incubator** | **Student Hub** | 2.705 | 100.000 | **2.71%** |

### Cơ Cấu Sub-pages Cinema Hub (Quy Chuẩn Tracking Mới):
- **Trang Rạp phim (`Cinema_Cineplex`):** **504.037 PVs** (67.4% Hub)
- **Trang phim chi tiết (`Cinema_Page`):** **160.290 PVs** (21.4% Hub)
- **Cinema_Home Page (Trang chủ Cinema):** **47.894 PVs** (6.4% Hub)
- **Cinema_Blog:** **32.684 PVs** (4.4% Hub)
- **Cinema_Landing Page:** **2.458 PVs** (0.3% Hub)
- **Tin tức (`Cinema_News`):** **561 PVs** (0.1% Hub)

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

---

## 6. BÓC TÁCH ĐỘNG LỰC TĂNG TRƯỞNG MOM (THÁNG 11 VS THÁNG 10 MTD 18 NGÀY)

> **Kỳ dữ liệu đối soát:** 01/11/2026 - 18/11/2026 vs 01/10/2026 - 18/10/2026 (18 ngày like-for-like)
> **Nguồn SSOT:** `07_REPORTS/data/analytics/mom_growth_drivers_11_vs_10_18d.json`
> **Kết luận chủ đạo:** Lũy kế MTD 18 ngày Tháng 11 đạt **3.102.303 PV**, tăng **+957.610 PV (+44,65% MoM)** so với mức **2.144.693 PV** cùng kỳ Tháng 10. Mức tăng trưởng ròng phân bổ đồng đều giữa Non-Paid (+497K PV, chiếm 51,9%) và Paid (+460K PV, chiếm 48,1%).

### 6.1 Biến động theo kênh lưu lượng (Channel Delta):
| Kênh lưu lượng | MTD 18d T10 | MTD 18d T11 | Biến động tuyệt đối | % MoM | Đóng góp vào mức tăng |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **NON-PAID (Tự nhiên)** | **1.930.753 PV** | **2.427.850 PV** | **+497.097 PV** | **+25,75%** | **51,91%** |
| - Organic Search | 1.142.226 PV | 1.403.639 PV | +261.413 PV | +22,89% | 27,30% |
| - Direct Traffic | 535.574 PV | 796.552 PV | +260.978 PV | +48,73% | 27,25% |
| - AI Traffic (GEO) | 8.379 PV | 22.684 PV | +14.305 PV | +170,72% | 1,49% |
| - Referral & Khác | 244.574 PV | 204.975 PV | -39.599 PV | -16,19% | -4,13% |
| **PAID TRAFFIC (Quảng cáo)** | **213.940 PV** | **674.453 PV** | **+460.513 PV** | **+215,25%** | **48,09%** |
| **TỔNG LƯU LƯỢNG TOÀN WEBSITE** | **2.144.693 PV** | **3.102.303 PV** | **+957.610 PV** | **+44,65%** | **100,00%** |

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
