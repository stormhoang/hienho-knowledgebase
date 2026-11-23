# BÁO CÁO TỔNG HỢP DOANH THU GMV TOÀN NỀN TẢNG WEB NĂM 2026 (SSOT)

> **Cập nhật:** 18/11/2026 | **Phiên bản:** v1.0 (Master Portfolio SSOT)  
> **Kỳ dữ liệu:** Lũy kế năm 2026 (Chốt đến Tháng 10 / Giữa Tháng 11/2026)  
> **Nguồn dữ liệu:** BigQuery DWH SSOT, Dashboard In-App MoMo, Dữ liệu Đối soát BU Movies, Báo cáo Đánh giá InsurTech và Dữ liệu Kế hoạch Ngân sách 2027  
> **Tệp dữ liệu gốc (JSON):** [`07_REPORTS/data/analytics/web_gmv_2026.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/analytics/web_gmv_2026.json)

---

## 1. TỔNG QUAN HIỆU SUẤT GMV TOÀN NỀN TẢNG WEB

Tính đến giữa Tháng 11/2026, nền tảng Web MoMo đã đóng góp chính thức **19.490.178.292 VNĐ (~19,49 tỷ VNĐ)** tổng giá trị giao dịch (GMV thực thu) trên toàn bộ danh mục sản phẩm có luồng mua hàng và thanh toán.

So với toàn bộ năm 2025 (~12,66 tỷ VNĐ), GMV kênh Web năm 2026 đã tăng trưởng **+53,9%**, tạo ra hơn **83.000 đơn hàng thành công** và mang lại tệp người dùng giao dịch chất lượng cao từ môi trường ngoài ứng dụng (Out-App).

### Bảng Tổng Hợp GMV Danh Mục Kênh Web Năm 2026:

| Nhóm ngành hàng / Khối sản phẩm | Dịch vụ cụ thể | GMV 2026 Thực Tế (VND) | Tỷ trọng (%) | Khối lượng chuyển đổi | Benchmark 2025 | Tăng trưởng YoY | Nguồn đối soát SSOT |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Điện Ảnh (Cinema Hub)** | Vé xem phim rạp | **15.913.125.000 đ** | 81,6% | 77.625 đơn (168.884 vé) | 10.723.755.000 đ | **+48,4%** (Đạt 148% cả năm 2025) | Dashboard In-App range T1-T10 |
| **2. Bảo Hiểm (InsurTech)** | **Bảo hiểm Y tế (BHYT)** | **2.665.621.310 đ** | 13,7% | 2.643 người mua (86% chốt trên Web) | 1.614.064.484 đ | **+65,15%** | Data Đối soát InsurTech |
| | **BH Thân vỏ Ô tô (VCX)** | **462.000.000 đ** | 2,4% | 71 đơn thành công (2.118 leads) | Chưa bóc tách riêng | Ước tính từ 71 đơn | GA4 Funnel & Đối soát BH |
| | **BH Xe máy (XMBB)** | **289.031.982 đ** | 1,5% | 1.948 đơn App / 1.750 người Web | 326.157.507 đ | **-11,38%** | Data Đối soát InsurTech |
| *Tiểu kết Khối Bảo Hiểm* | *3 sản phẩm InsurTech* | **3.416.653.292 đ** | *17,5%* | *136.819 users tiếp cận (+32%)* | *1.940.221.991 đ* | **+76,1%** | *Tổng hợp khối Bảo hiểm* |
| **3. Du Lịch (Travel Hub)** | **eSIM Du Lịch** | **160.400.000 đ** | 0,8% | 824 đơn hàng (CR 3,18%) | Mới triển khai | 100% Organic (0đ Ads) | Báo cáo Chuyển đổi Web |
| | **Vé xe khách (/ve-xe)** | Đang đối soát BU | - | 3.787 MAU giao dịch | - | Theo mùa vụ | GA4 /ve-xe Funnel |
| **TỔNG CỘNG DANH MỤC WEB** | **Toàn bộ kênh Web** | **19.490.178.292 đ** | **100,0%** | **>83.000 đơn hàng thành công** | **~12,66 tỷ VNĐ** | **+53,9%** | **Master Portfolio SSOT** |

*(Ghi chú: Nếu tính Cinema theo số cộng dồn từng tháng riêng lẻ là 16.413.560.000 đ do chênh lệch đối soát Tháng 7, tổng GMV toàn kênh Web là **19.990.613.292 đ**, tức xấp xỉ **~19,99 tỷ VNĐ**).*

---

## 2. CHI TIẾT TỪNG KHỐI KINH DOANH

### 2.1. Cinema Hub (Điện Ảnh & Giải Trí - Cột Trụ Doanh Số)
- **Doanh thu GMV:** **15.913.125.000 VNĐ** (chốt theo Dashboard In-App range T1-T10, ngày 18/11/2026).
- **Khối lượng giao dịch:**
  - 60.378 khách hàng giao dịch (W2A MAU không trùng lặp toàn kỳ).
  - 201.517 lượt tương tác phễu bán vé (W2A MEU).
  - 77.625 đơn hàng thành công (bình quân 1,286 đơn / khách hàng).
  - 168.884 vé xuất rạp (bình quân 2,18 vé / đơn hàng).
  - Giá trị đơn hàng trung bình (AoV): ~205.000 VNĐ / đơn.
- **Hiệu suất đơn vị:** Cứ 1.000 PageViews mang lại **~1,75 triệu VNĐ GMV** (8,5 đơn hàng và 18,6 vé).
- **So sánh 2025:** Cả năm 2025 đạt 10,72 tỷ VNĐ (52.311 đơn, 111.422 vé). Lũy kế 10 tháng năm 2026 đã đạt **148,4%** thành tích năm trước.
- **Dự báo cả năm 2026 (Kịch bản cơ sở):** Đạt 103.240 đơn hàng và **21,16 tỷ VNĐ GMV** (+97,4% YoY).

### 2.2. Khối Bảo Hiểm Trực Tuyến (InsurTech - Trụ Cột Tăng Trưởng Mới)
Kênh Web mang về **136.819 người dùng tiếp cận bảo hiểm** (tăng +32% so với cả năm 2025). Đáng chú ý, **44% đến 51% người mua bảo hiểm trên Web chưa từng có tài khoản ví MoMo**, chứng minh Web là kênh thu hút khách hàng mới ngoài App hiệu quả.

- **Bảo hiểm Y tế (BHYT) - Điểm sáng tăng trưởng:**
  - GMV 2026: **2.665.621.310 VNĐ** (so với 1,61 tỷ VNĐ năm 2025, tăng **+65,15% YoY**).
  - Lưu lượng đạt 196.198 PVs (gấp 4,4 lần năm 2025).
  - Thu hút 2.643 người mua thành công.
  - Điểm đột phá về sản phẩm: **86% người dùng hoàn tất thanh toán trực tiếp trên Web (Native Web Payment)** mà không cần điều hướng vào ứng dụng.
  - Chi phí đầu tư SEO và SEM chỉ 150 triệu VNĐ, tương đương chi phí chỉ khoảng 57.000 đ cho mỗi người mua, là mức chi phí hiệu quả nhất trong khối bảo hiểm.
- **Bảo hiểm Thân vỏ Ô tô (VCX) - Giá trị hợp đồng cao:**
  - GMV 2026: **~462.000.000 VNĐ** ước tính từ 71 đơn hàng thành công.
  - Tạo ra 2.118 leads từ 162.304 lượt truy cập Web (+46% vs 2025).
  - Tỷ lệ chuyển đổi từ lead sang đơn đạt 3,3% (điểm cần tối ưu quy trình tư vấn so với mục tiêu 7-10%).
  - Chi phí đầu tư SEO và SEM: 1,05 tỷ VNĐ.
- **Bảo hiểm Xe máy Bắt buộc (XMBB):**
  - GMV 2026: **289.031.982 VNĐ** (so với 326 triệu VNĐ năm 2025, giảm 11,38% YoY).
  - Ghi nhận 1.948 đơn hàng chuyển tiếp về App và 1.750 người mua trực tiếp trên Web từ 90.522 PVs.
  - Chi phí đầu tư SEO và SEM: 350 triệu VNĐ.

### 2.3. Khối Du Lịch & Di Chuyển (Travel & Connectivity)
- **eSIM Du Lịch:**
  - GMV 10 tháng 2026: **160.400.000 VNĐ** từ **824 giao dịch thành công**.
  - Tỷ lệ chuyển đổi đạt 3,18% hoàn toàn tự nhiên từ công cụ tra cứu thông tin (0 đồng ngân sách quảng cáo).
  - Tiềm năng phát triển: Mục tiêu tổng mảng eSIM theo BRD là 27,4 tỷ VNĐ, trong đó kênh Web đặt mục tiêu đóng góp trên 10% (>2,7 tỷ VNĐ GMV).
- **Vé Xe Khách (/ve-xe):**
  - Ghi nhận 3.787 người dùng giao dịch (MAU) qua luồng chuyển tiếp Web-to-App. Dữ liệu GMV chi tiết đang được tổng hợp cùng đối soát từ BU Travel.

### 2.4. Khối Dịch Vụ Tài Chính & Tiện Ích Giao Thông (Phễu Chuyển Đổi Không Đo Bằng GMV)
- **Financial Hub (CIC, Vay Nhanh, Tích Lũy, Chứng Khoán):**
  - Không quy đổi thành GMV bán lẻ do bản chất sản phẩm tài chính là hạn mức tín dụng và số dư tích lũy.
  - Đóng góp: Tạo ra **84.000 đến 113.000 lượt chuyển tiếp vào App** để mở hồ sơ vay hoặc kích hoạt tài khoản đầu tư.
- **Vehicle Hub (Tra cứu Phạt Nguội, Đăng Kiểm):**
  - Đóng vai trò sản phẩm dẫn dắt (PLG Utility) tạo dựng lưu lượng tự nhiên với hơn 660 trích dẫn từ các hệ thống AI.
  - Đóng góp vào kết quả **11.143 lượt cài đặt ứng dụng mới (New User Installs)** trong Tháng 10/2026.

---

## 3. PHÂN TÍCH THỰC CHẤT VÀ Ý NGHĨA KINH DOANH (SO WHAT)

1. **Khẳng định Web Platform là kênh tạo GMV độc lập:**
   - Với gần 19,5 tỷ VNĐ GMV trong 10 tháng năm 2026, Web Platform không chỉ dừng lại ở vai trò làm nội dung quảng bá thương hiệu (Branding) hay cung cấp thông tin, mà đã trở thành một kênh phân phối thương mại trực tiếp.
2. **Sức mạnh của mô hình Thanh toán Trực tiếp trên Web (Native Web Checkout):**
   - Kết quả từ BHYT (86% chốt ngay trên Web mang về 2,67 tỷ VNĐ GMV) chứng minh rằng: khi loại bỏ rào cản bắt buộc mở ứng dụng, tỷ lệ hoàn tất giao dịch của người dùng tăng vượt trội. Đây là tiền đề để mở rộng luồng Native Checkout sang Vé xem phim, Vé xe và eSIM trong năm 2027.
3. **Giá trị kéo tệp khách hàng mới ngoài App (New User Acquisition via Commerce):**
   - Hơn 50% người mua bảo hiểm trên Web chưa có ví MoMo. Kênh Web giúp tập đoàn mở rộng thị phần sang những khách hàng quen giao dịch trên máy tính hoặc trình duyệt di động mà không cần tốn chi phí khuyến mãi cài đặt ban đầu.
4. **Phân biệt chuẩn xác giữa GMV và Doanh thu ròng (Net Revenue):**
   - 19,49 tỷ VNĐ là tổng giá trị giao dịch mà khách hàng chi trả. Doanh thu thực của MoMo phụ thuộc vào tỷ lệ hoa hồng chiết khấu (Take-rate) từ các đối tác rạp chiếu phim, công ty bảo hiểm và nhà mạng viễn thông.

---

## 4. KẾ HOẠCH HÀNH ĐỘNG VÀ QUẢN TRỊ (NOW WHAT)

1. **Định kỳ cập nhật báo cáo GMV hợp nhất (Master GMV Ledger):**
   - Duy trì tệp dữ liệu [`07_REPORTS/data/analytics/web_gmv_2026.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/analytics/web_gmv_2026.json) làm nguồn chuẩn duy nhất (SSOT) cho các kỳ báo cáo kinh doanh của Web Platform.
2. **Tối ưu tỷ lệ chuyển đổi cho các mảng có giá trị cao:**
   - **Bảo hiểm Thân vỏ (VCX):** Chuẩn hóa lại luồng báo giá tự động và bàn giao lead cho đội ngũ tư vấn để nâng tỷ lệ chuyển đổi từ 3,3% lên 7-10%, tương xứng với chi phí marketing đã chi ra.
   - **Bảo hiểm Xe máy (XMBB):** Ứng dụng trải nghiệm mua nhanh một chạm tương tự BHYT để đảo ngược đà sụt giảm của năm 2026.
3. **Thúc đẩy Native Web Checkout cho Cinema Hub và eSIM:**
   - Triển khai tính năng giữ ghế và thanh toán trực tiếp trên trang rạp phim, giảm phụ thuộc vào việc điều hướng OneLink sang App, kỳ vọng tăng trưởng thêm 30% tỷ lệ chuyển đổi đơn hàng.
4. **Phối hợp đối soát cùng các BU chuyên môn:**
   - Làm việc định kỳ cùng BU Movies, BU InsurTech và BU Travel để chốt số liệu đối soát giao dịch và hoa hồng thực nhận trước ngày 15 hàng tháng.

---

## 5. TÀI LIỆU VÀ LIÊN KẾT LIÊN QUAN

- Báo cáo Kế hoạch Ngân sách 2027: [`07_REPORTS/docs/strategy/Budget 2027 - 2026 Reflection - Web Platform.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/strategy/Budget%202027%20-%202026%20Reflection%20-%20Web%20Platform.md)
- Báo cáo Hiệu suất Tuần Cinema Hub: [`07_REPORTS/docs/weekly-report-2026-11-02-11-08.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/weekly-report-2026-11-02-11-08.md)
- Bảng đối soát Bảo hiểm YoY: [`05_HUBS/vehicle/INSURANCE_GMV_YOY_2026.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle/INSURANCE_GMV_YOY_2026.md)
- Đặc tả Sản phẩm Cinema W2A GMV: [`05_HUBS/cinema/CINEMA_W2A_GMV_PERFORMANCE_2026.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/cinema/CINEMA_W2A_GMV_PERFORMANCE_2026.md)
