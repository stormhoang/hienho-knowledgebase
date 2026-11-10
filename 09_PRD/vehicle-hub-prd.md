# ĐẶC TẢ YÊU CẦU SẢN PHẨM (PRD) - VEHICLE HUB (KÊNH WEB & HỒ SƠ PHƯƠNG TIỆN)

> **Mục đích:** Tài liệu Đặc tả Yêu cầu Sản phẩm Kênh Web (Web Product PRD) chính thức dành cho dự án **Vehicle Hub - Tiện Ích Giao Thông**, xây dựng theo chuẩn 4 Phần Tiêu Chuẩn: Overview, Market Research, Product Structure (Site, Content & Umami Touchpoints) và SEO/GEO On-Page.

## THÔNG TIN TỔNG QUAN (METADATA)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng Mục</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chi Tiết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tên Sản Phẩm / Use Case</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tiện Ích Giao Thông (Vehicle Hub Web Platform & Vehicle Identity)</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Canonical Root URL</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/tien-ich-giao-thong/</code> & <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/phat-nguoi/</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trạng Thái Tài Liệu</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>APPROVED (Execution Phase)</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Governance</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Product Lead:</strong> Hien.ho \</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Lead Engineer:</strong> Web Platform Tech Lead \</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Business Owners:</strong> VTTI Lead x Insurtech Lead</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Mốc Tiến Độ Dự Kiến</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Kick-off: <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">06/07/2026</code>  ➔  Build Phase 1: <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">01/08/2026</code>  ➔  Pilot: <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">01/09/2026</code>  ➔  Go-Live: <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">30/09/2026</code></td>
    </tr>
  </tbody>
</table>

## 1. PRODUCT OVERVIEW

### 1.1 Elegant Framing
### 1.1 Elegant Framing
Hàng triệu chủ xe ô tô và xe máy tại Việt Nam đang bị phân mảnh thông tin, phải chuyển qua lại giữa 5-7 ứng dụng và website rời rạc chỉ để xử lý các nhu cầu thiết yếu: tra phạt nguội, xem giá xăng, nạp tiền ETC, theo dõi hạn đăng kiểm, tìm trạm sạc và mua bảo hiểm. Nếu chỉ cung cấp dịch vụ trong ứng dụng di động đóng (App-only ecosystem), MoMo sẽ hoàn toàn vô hình trước hơn **20.1 triệu lượt tìm kiếm tự nhiên/tháng** (từ bộ 11.104 từ khóa độc lập) ngoài Open Web.

**Vehicle Hub trên Web (`momo.vn/tien-ich-giao-thong`)** ra đời với định vị cốt lõi là **"Cổng Tiện Ích Giao Thông All-in-One"** dành cho chủ xe ô tô và xe máy tại Việt Nam, đóng vai trò là **Điểm đến Tiện ích Xe Mở & Cổng Định Danh Thẻ Xe Số**. Bằng cách cung cấp các công cụ tiện ích tra cứu công cộng tốc độ cao (0-CAPTCHA real-time, bảng giá xăng, trạm sạc EV) kết hợp cùng **Nội dung bài viết GenAI Content (Dự án PLG Project)**, Kênh Web giải quyết tức thời nhu cầu của chủ xe ngoài Open Web, khởi tạo Hồ sơ phương tiện (Vehicle Profile) và điều hướng giữ chân người dùng trong hệ sinh thái MoMo.

### 1.2 Product Vision, Flywheel & Strategic Model

#### A. Bảng Ma Trận Phân Định Ranh Giới: Kênh Web (Web Vehicle Hub) vs In-App Mini App (In-App Vehicle Hub)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng Mục So Sánh</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Kênh Web (Web Vehicle Hub)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">In-App Mini App (In-App Vehicle Hub)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tên Sản Phẩm / Kênh</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cổng Tiện Ích Giao Thông (Web Platform)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Vehicle Center Mini App (In-App)</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Địa Chỉ / Nền Tảng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trình duyệt Web (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/tien-ich-giao-thong</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/phat-nguoi</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ứng dụng di động MoMo (iOS & Android Mini App)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đơn Vị Chịu Trách Nhiệm (Owner)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Platform Team (GPD)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>VTTI Cell Team x InsurTech Cell Team</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Định Vị & Vai Trò Cốt Lõi</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phễu Hứng Traffic Tự Nhiên & Định Danh (Acquisition Feeder)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Điểm Đến Giữ Chân, Tự Động Hóa & Thương Mại (Retention & Monetization Destination)</strong></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trải Nghiệm Người Dùng (UX)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu công cộng 0-CAPTCHA, không yêu cầu đăng nhập trước, <strong>KHÔNG giữ chân ở Web</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lưu Thẻ Xe Số (Vehicle Profile), tự động hóa Push Notification, Auto-Topup ePass, mua bảo hiểm Auto-fill.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cơ Chế Chuyển Đổi (Conversion)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web-to-App (W2A)</strong> via Universal Link & Deep Link</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>In-App Transaction & Retention</strong> (Thanh toán Ví MoMo/Ví Trả Sau)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Mục Tiêu Key Metrics (KPI)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• <strong>315.000 Visits</strong> (Organic Search Traffic Phase 1)<br>• <strong>CVR Web-to-App ≥ 0.5%</strong><br>• <strong>SEO Ranking Top 1 - 10 Google</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• <strong>100.000 Saved Vehicles Level 1</strong><br>• <strong>140.000 Vehicles Level 2 (OCR)</strong><br>• <strong>20.000 Vehicles Level 3 (Ô tô)</strong><br>• <strong>≥ 200.000 Active Vehicle Users</strong><br>• <strong>335 đơn VCX + 707 đơn TNDS</strong></td>
    </tr>
  </tbody>
</table>

#### B. Chu Trình Tăng Trưởng Flywheel 6 Bước (VTTI + INS + MoMo Platform)
1. **MoMo Level:** Tăng Customer Stickiness tệp chủ xe  ➔  Khởi tạo tài sản dữ liệu Vehicle Profile  ➔  Tăng tỷ lệ tái sử dụng Data (Data Reuse).
2. **VTTI Level:** Chuyển đổi Hub thành điểm đến (Destination) thay vì danh sách tiện ích  ➔  Tăng attach rate Phạt nguội/ETC/Đăng kiểm  ➔  Tăng Revisit & Traffic.
3. **INS Level:** Chuẩn hóa dữ liệu xe cho TNDS/VCX  ➔  Prefill giảm friction mua bảo hiểm  ➔  Mở rộng Cross-sell theo lifecycle chủ xe  ➔  Nâng cao chất lượng Lead.
4. **Kích Hoạt Utility:** Tự động kích hoạt thông báo Phạt nguội, ePass Auto-topup, Nhắc hạn Đăng kiểm.
5. **Tăng Revisit & Active Vehicle Users:** Đạt chỉ tiêu ≥ 200.000 Active Vehicles.
6. **Insurance Monetization Layer:** Prefill tự động điền dữ liệu  ➔  Tăng doanh thu thương mại  ➔  Reinvest & Scale.

## 2. MARKET RESEARCH

### 2.1 Market Sizing & Opportunity
* **Dung lượng thị trường phương tiện tại Việt Nam:**
  * **Ô tô:** Hơn 5,5 triệu ô tô lưu hành toàn quốc.
  * **Xe máy:** Hơn 72 triệu xe máy đăng ký.
* **Tài sản dữ liệu sẵn có trên hệ thống MoMo:**
  * MoMo sở hữu dữ liệu phương tiện của **~600.000 ô tô** và **~2.000.000 xe máy** (trong đó có hơn **150.000+ ô tô** được định danh chi tiết bằng OCR Cà vẹt).
  * Tỷ lệ trùng lặp dữ liệu giữa mảng Bảo hiểm (FS) và Phạt nguội/ePass (VTTI) hiện rất thấp (**0,3% - 3%**), chứng minh dư địa bán chéo (Cross-sell) cực lớn khi hợp nhất dữ liệu vào Hồ sơ xe.

### 2.2 Competitor Gap Analysis
* **Thực trạng đối thủ bên thứ ba:**
  * Cổng thông tin Cục CSGT (`csgt.vn`) thường xuyên quá tải, chậm cập nhật và yêu cầu mã CAPTCHA phức tạp.
  * Các trang web tra cứu bên thứ ba (như `phatnguoi.com`) chứa nhiều quảng cáo rác, UX kém và **không có khả năng lưu hồ sơ xe hay kết nối thanh toán In-App**.
* **Cơ hội bứt phá của MoMo (MoMo Advantage):**
  * Tra cứu Phạt Nguội tốc độ cao **0-CAPTCHA** real-time.
  * Tích hợp kho bài viết chuẩn tư vấn luật giao thông và mẹo bảo dưỡng sinh tự động từ **GenAI Content Engine (PLG Project)**.
  * Trải nghiệm liền mạch **Web-to-App (W2A)**: Nhập biển số xe 1 lần trên Web  ➔  Tự động tạo Hồ sơ xe trong App và kích hoạt cảnh báo vi phạm mới qua MoMo.

### 2.3 User Pain Points & Search Demand Inventory

#### A. Rào cản lớn nhất của người dùng (User Pain Points)
1. **Trải nghiệm phân mảnh:** Phải gõ lại biển số xe và thông tin cá nhân nhiều lần trên nhiều website độc lập.
2. **Lo sợ vi phạm phạt nguội:** Không biết xe mình có bị dính lỗi phạt nguội hay không cho đến khi đi đăng kiểm.
3. **Thiếu thông tin tư vấn giao thông:** Thiếu nguồn bài viết tư vấn luật giao thông và mẹo bảo dưỡng xe đáng tin cậy.

#### B. Ma trận nhu cầu tìm kiếm trên Open Web (Search Demand Inventory - 11.104 KWs)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm Nhu Cầu (Search Cluster)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Volume Search / Tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Số Lượng KW</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại Intent (Search Intent)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Giá Xăng Dầu</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>10.517.130</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2.790</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Freshness / Commercial</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tra Cứu Phạt Nguội</strong> <em>(Kênh Cốt Lõi)</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>~6.100.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Master Gate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional / High-Intent</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trạm Sạc Xe Điện EV</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>1.237.970</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">144</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Local GEO / High-ARPU</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Sửa Chữa & Bảo Dưỡng Xe</strong> <em>(Hợp nhất Gara, Garage, Sửa xe, Bảo dưỡng)</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>933.600</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">4.901</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Local GEO / Emergency</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cây Xăng (Bản Đồ Local)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>550.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Local GEO / O2O</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Rửa Xe & Chăm Sóc Xe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>283.610</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1.376</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Local GEO / Car Care</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bãi Đỗ Xe & Giữ Xe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>180.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">178</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Local GEO / Utility</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đăng Kiểm Xe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>182.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Baseline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility / Inspection</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cứu Hộ Đường Bộ 24/7</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>171.660</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">819</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Local GEO / Emergency 24/7</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phí Không Dừng (ePass/VETC)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>94.520</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">478</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility / Auto-Topup</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Thuế Trước Bạ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>44.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Baseline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Financial / Car Registration</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phí Đường Bộ</strong> <em>(Nội dung Blog & Cẩm Nang)</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>13.630</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">120</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Knowledge SEO / Blog Content</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Định Giá Xe Cũ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>14.300</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">308</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Financial Lead / Calculator</td>
    </tr>
  </tbody>
</table>

## 3. PRODUCT STRUCTURE

### 3.1 Site Structure (Silo Sitemap & Routing Rules)

Hệ thống URL Kênh Web Vehicle Hub được quy hoạch thành **2 Nhóm Cấu Trúc Rõ Ràng**:

```
                       ┌─────────────────────────────────────────┐
                       │  MASTER HUB: /tien-ich-giao-thong/      │
                       └────────────────────┬────────────────────┘
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
┌───────────────────────────┐   ┌───────────────────────────┐   ┌───────────────────────────┐
│ GROUP A: SPOKE PAGES      │   │ GROUP A: LOCAL GEO PAGES  │   │ GROUP B: STANDALONE PAGES │
│ /gia-xang/                │   │ /tram-sac/                │   │ /phat-nguoi/              │
│ /dang-kiem/               │   │ /cay-xang/                │   │ /bao-hiem-o-to/           │
│ /hang-xe/                 │   │ /garage/                  │   │ /bao-hiem-xe-may/         │
│ /dinh-gia-xe/             │   │ /bai-do-xe/               │   │ /phi-khong-dung/          │
│ /cuu-ho/                  │   └─────────────┬─────────────┘   └───────────────────────────┘
│ /blog/ (GenAI Content)    │                 │
└───────────────────────────┘                 ▼
                                ┌───────────────────────────┐
                                │ MERCHANT DETAIL PAGES     │
                                │ /merchant/{merchant-slug}/│
                                └───────────────────────────┘
```

#### Bảng Phân Loại 3 Lớp Function Kênh Web (Chuyển Giao Traffic Về Vehicle Hub In-App)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm Function</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định Hướng & Mức Độ Ưu Tiên</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Các Tính Năng & Use Cases</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cơ Chế Điều Hướng Web-to-App (W2A)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nhóm 1: Magnet + Transaction</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Ưu tiên 1</strong><br>Hứng nhu cầu tra cứu tức thì & nộp phạt/đặt lịch</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Tra phạt nguội  ➔  Nộp phạt online<br>• Tra hạn đăng kiểm  ➔  Đặt lịch trung tâm kiểm định</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1-Click mở App MoMo để nộp phạt qua Cổng DVC hoặc hoàn tất đặt lịch giữ chỗ đăng kiểm.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nhóm 2: Retention</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Retention Magnet</strong><br>Duy trì tần suất truy cập lặp lại hàng tuần/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Bảng giá xăng dầu (cập nhật thứ 5 hàng tuần)<br>• Cây xăng Petrolimex/PVOil gần đây<br>• Trạm sạc xe điện EV VinFast/V-Green<br>• Tra cứu & nạp số dư ePass/VETC<br>• Tra cứu thông tin xe theo biển số</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Form đăng ký SĐT nhận Push Notification trước kỳ điều hành giá xăng.<br>• Mở App MoMo cài Auto-Topup ePass & xem bản đồ chỉ đường.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nhóm 3: Calculator & Guide</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>High Intent Capture</strong><br>Hứng nhu cầu tính toán chi phí & hướng dẫn pháp lý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Tính thuế/phí trước bạ (xe mới)<br>• Hướng dẫn sang tên xe (xe cũ)<br>• Tính phí đăng kiểm & phí đường bộ<br>• Công cụ định giá xe cũ (11K volume/tháng)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Banner khơi gợi & W2A CTA: <em>"Khởi tạo Thẻ Xe Số trên MoMo để tự động tính toán chi phí nuôi xe mỗi tháng."</em></td>
    </tr>
  </tbody>
</table>

#### Nhóm A: Trang Chủ Hub & Các Spoke Pages Trực Thuộc (`/tien-ich-giao-thong/*`)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">STT</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Nhóm Trang / Dịch Vụ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Canonical</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Phân Cấp Routing</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai Trò & Chức Năng Trong Cấu Trúc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trang Chủ Vehicle Hub</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Master Hub Root</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cổng tổng điều hướng 360°, định danh Thẻ Xe Số</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Giá Xăng Dầu</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/gia-xang/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cập nhật giá xăng Petrolimex/PVOil thời gian thực</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trạm Sạc Xe Điện</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/tram-sac/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ vị trí trạm sạc VinFast, V-Green toàn quốc</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cây Xăng Gần Đây</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/cay-xang/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ vị trí cây xăng Petrolimex/PVOil kết nối phễu M4B</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Garage Sửa Xe & Bảo Dưỡng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/garage/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Danh sách garage, trung tâm chăm sóc ô tô uy tín địa phương</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đăng Kiểm Xe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/dang-kiem/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu hạn đăng kiểm, lịch hẹn trung tâm kiểm định</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hãng Xe & Dòng Xe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/hang-xe/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Master Data 35 Hãng Xe & 264 Dòng Xe</strong> (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/hang-xe/{brand}/{model}</code>). Thông số kỹ thuật, chi phí nuôi xe & phễu báo giá Bảo hiểm TNDS/Thân vỏ.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bãi Đỗ Xe & Giữ Xe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/bai-do-xe/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ điểm trông giữ xe ô tô / xe máy</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">9</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cứu Hộ Đường Bộ 24/7</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/cuu-ho/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổng đài cứu hộ ô tô, cẩu xe, kích bình ắc quy khẩn cấp</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">10</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Định Giá Xe Cũ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/dinh-gia-xe/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Công cụ định giá xe ô tô/xe máy cũ, phễu Vay & Bảo hiểm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">11</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Blog Tiện Ích Giao Thông</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/blog/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>GenAI Content (PLG Project).</strong> Kho bài viết tư vấn luật & mẹo bảo dưỡng xe</td>
    </tr>
  </tbody>
</table>

#### Nhóm B: 4 Trang Use Case Độc Lập (Top-Level Standalone Canonical Pages)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">STT</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Use Case Standalone</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Canonical</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Phân Cấp Routing</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai Trò & Điểm Khác Biệt Trong Cấu Trúc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tra Cứu Phạt Nguội</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/phat-nguoi/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Root Standalone</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility độc lập Top 1 Google, tra cứu 0-CAPTCHA real-time</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bảo Hiểm Ô Tô</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-o-to/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Root Standalone</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang bán hàng độc lập cho Bảo hiểm TNDS & Thân vỏ ô tô</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bảo Hiểm Xe Máy</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-xe-may/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Root Standalone</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang bán hàng độc lập cho Bảo hiểm TNDS xe máy online</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phí Không Dừng (ETC)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/phi-khong-dung/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Root Standalone</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang tiện ích nạp tiền & kiểm tra số dư ePass / VETC</td>
    </tr>
  </tbody>
</table>

### 3.2 Product Architecture Classification (Component, Utilities & Merchant Routing)

#### A. API-Driven Components (Thành Phần Tích Hợp API Dữ Liệu Realtime từ In-App Mini App MoMo)
> *Nguyên tắc hạ tầng (Single Source of Truth):* Toàn bộ các API tra cứu trên Kênh Web được đồng bộ trực tiếp từ hệ thống API Micro-services của **In-App Vehicle Center Mini App (MoMo App)**, đảm bảo tính nhất quán dữ liệu 100% giữa Web & App, không xây dựng backend riêng.

* **Giá Xăng Dầu:** API Sync realtime từ Mini App MoMo (dữ liệu cập nhật kỳ điều hành giá xăng Liên Bộ).
* **Tra Cứu Phạt Nguội:** API Tra cứu vi phạm 0-CAPTCHA đồng bộ từ Mini App MoMo (kết nối dữ liệu CSGT/Cục Đăng Kiểm).
* **Định Giá Xe:** API định giá thị trường xe cũ & định giá biển số đồng bộ từ Mini App MoMo.

#### B. Calculators & Lookup Utilities (Công Cụ Tính Toán & Dự Toán Nghiệp Vụ)
* **Tính Giá Tiền Nuôi Xe Hơi (Car Ownership Cost Calculator):** Input `Dòng xe` + `Số km đi/tháng` + `Phí gửi xe`  ➔  Tính tổng chi phí nuôi xe hàng tháng & chi phí trung bình/km.
* **Tính Lít Xăng & Hao Phí Nhiên Liệu (Fuel Consumption Calculator):** Input `Dòng xe` + `Số km lộ trình` + `Loại xăng`  ➔  Tính tổng số lít xăng tiêu hao & tổng tiền xăng dự toán.
* **Tính Khấu Hao & Hao Mòn Xe (Car Depreciation Calculator):** Input `Giá mua xe gốc` + `Năm sử dụng`  ➔  Tính giá trị tài sản xe còn lại & dự báo mốc thay thế phụ tùng.
* **Tính Thuế Trước Bạ & Phí Lăn Bánh (Car Registration Calculator):** Input `Giá xe` + `Tỉnh thành đăng ký`  ➔  Tính tổng chi phí lăn bánh xe mới chính xác theo từng địa phương.

#### C. Merchant Listing & Routing Pages (Trang Danh Mục Địa Điểm & Dẫn Đường)
Dạng trang **Merchant Listing (Danh mục cửa hàng/đối tác M4B)** kết hợp **Local GEO Map & Routing Engine (Chỉ đường qua Google Maps / Navigation API)**:
* **Garage Sửa Xe Ô Tô & Tiệm Sửa Xe Máy:** Danh mục tiệm sửa xe, garage bảo dưỡng  ➔  Bấm *"Chỉ đường"* mở điều hướng lộ trình tới điểm gần nhất.
* **Trạm Sạc Xe Điện:** Danh sách trạm sạc VinFast, V-Green khả dụng  ➔  Dẫn đường chính xác tới trụ sạc còn trống.
* **Rửa Xe & Chăm Sóc Xe:** Danh sách tiệm rửa xe, trung tâm detailing  ➔  Chỉ đường & hiển thị trạng thái thanh toán Ví MoMo.
* **Cây Xăng:** Danh sách cây xăng Petrolimex/PVOil chấp nhận thanh toán MoMo  ➔  Dẫn đường tới trụ bơm gần nhất.

#### D. Quy Tắc Cấu Trúc URL & Định Hướng SEO/GEO
* **Không dùng URL sub-path Tỉnh/thành (`{tinh-thanh}`):** Nhu cầu tìm kiếm địa phương được xử lý bằng Interactive Map + Filter Widget định vị GPS trên trang Canonical Gốc.
* **Duy nhất trang Hãng xe / Dòng xe mở rộng URL sub-path:** `/tien-ich-giao-thong/hang-xe/{hang-xe}/{dong-xe}` (dành cho hệ thống 1.500+ pSEO pages).
* **Phí Đường Bộ:** Không tạo trang dịch vụ riêng, định hướng phát triển bài viết Cẩm Nang trên Blog (`/tien-ich-giao-thong/blog/*`).

### 3.3 Content Structure Từng Trang (Functions, Components & UI Specifications)

#### A. Cấu Trúc Nội Dung Trang Chủ Master Hub (`/tien-ich-giao-thong/`)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">STT</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Component / UI Section</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhu Cầu Người Dùng (JTBD)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giải Pháp Cấu Trúc (Solution)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thành Phần UI (UI Components) & Functions Chi Tiết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hero & Phạt Nguội Utility Search</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn tra phạt nguội không CAPTCHA hoặc tìm tiện ích xe tức thì."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Form tra cứu phạt nguội 0-CAPTCHA 1-click đặt tại vị trí trung tâm Hero, trả kết quả tức thì.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Headline H1 chuẩn SEO.<br>• Selector chọn loại phương tiện: <strong>Ô tô / Xe máy</strong>.<br>• Input field nhập Biển số xe.<br>• Nút CTA <em>"Tra Cứu Phạt Nguội 0-CAPTCHA"</em> 1-click.<br>• Output kết quả: Xe sạch  ➔  CTA đăng ký <strong>Gói Cảnh Báo Phạt Nguội 9k/năm</strong>; Có lỗi  ➔  <strong>Nộp Phạt Online 1-Click</strong>.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Quick Utilities Grid (6 Spokes)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn truy cập nhanh các dịch vụ giao thông thiết yếu."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Grid 6 Card phím tắt chứa Icon & Tiêu đề điều hướng trực tiếp đến 6 Spoke cốt lõi.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Grid 6 Card phím tắt: <strong>Tra Phạt Nguội</strong>, <strong>Bảng Giá Xăng</strong>, <strong>Phí Không Dừng ePass</strong>, <strong>Trạm Sạc EV</strong>, <strong>Tìm Garage</strong>, <strong>Cứu Hộ 24/7</strong>.<br>• Huy hiệu nhãn mác (Badge): <em>"Real-time"</em>, <em>"0-CAPTCHA"</em>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Instant Insurance Quote & Auto-Fill Widget</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn xem nhanh báo giá và mua bảo hiểm ô tô / xe máy ngay trên trang chủ."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Widget báo giá tức thì Bảo hiểm TNDS & Thân vỏ ô tô / xe máy tích hợp cơ chế Auto-fill dữ liệu xe.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Selector chọn loại bảo hiểm (TNDS Ô tô, Thân vỏ Ô tô, TNDS Xe máy).<br>• Bảng so sánh báo giá & quyền lợi từ PVI, Bảo Việt, MIC, PTI...<br>• Nút CTA <em>"Mua Ngay - Cấp Ấn Chỉ Điện Tử Trong 30s"</em> (Tự động điền dữ liệu từ Vehicle Profile).</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Live Fuel Feed & E10 Compatibility Tool</strong> <em>(Học hỏi từ <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">e10.vn</code>)</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn xem giá xăng hôm nay và tra xem xe tôi có đi được xăng E10 không."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Live Feed giá xăng Petrolimex/PVOil Vùng 1 & 2 kết hợp Biểu đồ lịch sử + Công cụ tra cứu tương thích nhiên liệu.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Bảng niêm yết giá xăng RON 95-III, E5 RON 92, Dầu Diesel.<br>• <strong>Biểu đồ biến động giá xăng 3-6 tháng gần nhất</strong>.<br>• Form đăng ký SĐT nhận Push tin báo giá trước 15 phút chiều thứ 5.<br>• <strong>Tool Tra Cứu Tương Thích Xăng E10 (e10.vn Benchmark):</strong> Nhập Dòng xe/Hãng xe  ➔  Kiểm tra mức độ tương thích xăng sinh học E10 & dầu nhớt tối ưu.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Lifecycle Utilities Hub (Đăng Kiểm, ETC, Định Giá Xe)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn kiểm tra hạn đăng kiểm, nạp tiền ePass và định giá chiếc xe của tôi."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cụm 3 Card tiện ích vận hành vòng đời xe kết hợp công cụ định giá xe cũ (11K volume/tháng).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• <strong>Card 1 (Đăng Kiểm):</strong> Tra hạn kiểm định, cảnh báo ngăn chặn đăng kiểm, nút <em>"Đặt Lịch Trạm Kiểm Định"</em>.<br>• <strong>Card 2 (ETC ePass/VETC):</strong> Tra số dư tài khoản BOT, nút <em>"Cài Auto-Topup Nạp Tiền"</em>.<br>• <strong>Card 3 (Định Giá Xe Cũ):</strong> Công cụ tra khoảng giá xe cũ theo năm  ➔  Kích hoạt gói vay / hạn mức Ví Trả Sau.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>O2O Station & Garage Finder Map</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn tìm cây xăng Petrolimex hoặc garage bảo dưỡng gần vị trí tôi đứng."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ GPS tương tác định vị các địa điểm cây xăng Petrolimex/PVOil & Garage uy tín lân cận.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Mini Map GPS hiển thị 3 cây xăng / trạm sạc EV VinFast & V-Green / Garage gần nhất.<br>• Nút CTA <em>"Chỉ Đường Google Maps"</em> & <em>"Đặt Lịch Bảo Dưỡng"</em>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Vehicle Profile Value Proposition Cards</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn hiểu rõ lợi ích của việc lưu Thẻ Xe Số trên App MoMo."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3 Thẻ minh họa trực quan giá trị tự động hóa của Hồ sơ phương tiện (Vehicle Profile).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Card 1: <em>Tự động quét & phát thông báo phạt nguội qua MoMo</em>.<br>• Card 2: <em>Nhắc lịch hạn đăng kiểm trước 30/15/7 ngày</em>.<br>• Card 3: <em>Cài đặt Auto-Topup tự động nạp tiền ePass/VETC</em>.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>GenAI Blog & Cẩm Nang Featured Grid</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn đọc các bài viết hướng dẫn luật giao thông và mẹo bảo dưỡng uy tín."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Grid 3 bài viết nổi bật được cấp bởi <strong>GenAI Content Engine (PLG Project)</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Grid 3 Card bài viết: Ảnh đại diện, Tiêu đề H3, Sapo tóm tắt, Thẻ danh mục.<br>• Nút CTA <em>"Xem Tất Cả Bài Viết Cẩm Nang"</em>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">9</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>FAQ Accordion & Structural Footer Block</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn được giải đáp các thắc mắc thường gặp về quản lý xe trên MoMo."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khối FAQ Accordion khai báo mã Schema <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">FAQPage</code> chuẩn Google AI Search.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Accordion danh sách 5 câu hỏi thường gặp & câu trả lời chuẩn 25-40 từ.<br>• Footer Links liên kết sitemap nội bộ.</td>
    </tr>
  </tbody>
</table>

#### B. Đặc Tả Chi Tiết Nội Dung Văn Bản (Content & Copywriting Specifications) Trang Chủ

1. **Hero Section Copy (Định Vị Cổng Tiện Ích Giao Thông):**
   * **Thẻ H1:** `Tiện Ích Giao Thông MoMo - Cổng Tra Cứu & Quản Lý Xe Toàn Diện`
   * **Đoạn Sapo Sub-headline:** `Cổng tiện ích giao thông chính thức: Tra cứu phạt nguội 0-CAPTCHA real-time, cập nhật giá xăng hôm nay, định vị trạm sạc xe điện & tự động hóa quản lý chiếc xe của bạn.`
   * **Nút Tra Cứu (CTA):** `"Tra Cứu Phạt Nguội 0-CAPTCHA (Miễn Phí)"`

2. **Khối 3 Card Giá Trị Thẻ Xe Số (Vehicle Profile Value Prop Copy):**
   * **Card 1 (Phạt Nguội):** `Tự Động Báo Phạt Nguội`  ➔  *"MoMo tự động quét dữ liệu CSGT hàng tuần cho biển số xe của bạn & phát thông báo ngay qua MoMo khi dính lỗi mới."*
   * **Card 2 (Đăng Kiểm):** `Nhắc Lịch Đăng Kiểm Smart`  ➔  *"Tự động theo dõi thời hạn kiểm định, cảnh báo sớm trước 30/15/7 ngày & hỗ trợ đặt lịch hẹn trung tâm đăng kiểm."*
   * **Card 3 (Phí BOT ePass):** `Auto-Topup ePass / VETC`  ➔  *"Tự động nạp tiền tài khoản giao thông khi số dư dưới 50k, di chuyển thông suốt không lo kẹt trạm thu phí."*

3. **Direct Answer Block (Dành cho Google AI Overview & Generative Search):**
   > **"Cổng tiện ích giao thông MoMo (momo.vn/tien-ich-giao-thong) là nền tảng tiện ích giao thông trực tuyến cho phép chủ xe ô tô và xe máy tra cứu phạt nguội 0-CAPTCHA real-time từ Cục CSGT, theo dõi bảng giá xăng Petrolimex hôm nay, định vị trạm sạc xe điện VinFast/V-Green, kiểm tra số dư ETC và đăng ký mua bảo hiểm TNDS/Thân vỏ online với dữ liệu tự động điền trong 30 giây."**

4. **Nội Dung Accordion 5 Câu Hỏi Thường Gặp (FAQ Copy Spec - Schema `FAQPage`):**
   * **Q1:** *Làm thế nào để tra cứu phạt nguội không cần nhập mã CAPTCHA trên MoMo?*
     * **A1:** Bạn chỉ cần nhập biển số xe (ví dụ: 30F-12345) vào ô tra cứu trên trang Tiện ích giao thông MoMo. Hệ thống tự động kết nối dữ liệu Cục CSGT và trả kết quả tức thì trong 3 giây mà không yêu cầu nhập mã CAPTCHA.
   * **Q2:** *Tôi có thể nộp tiền phạt nguội online trực tiếp qua MoMo được không?*
     * **A2:** Có. Nếu kết quả tra cứu hiển thị lỗi vi phạm, bạn nhấp vào nút "Nộp phạt ngay" để mở App MoMo, kiểm tra chi tiết quyết định xử phạt và thanh toán 1-click qua Ví MoMo hoặc Ví Trả Sau.
   * **Q3:** *Gói Cảnh Báo Phạt Nguội Tự Động 9k/năm của MoMo hoạt động như thế nào?*
     * **A3:** Khi đăng ký Gói 9.000đ/năm, MoMo sẽ tự động quét dữ liệu CSGT định kỳ hàng tuần cho biển số xe của bạn và phát thông báo trực tiếp qua App MoMo ngay khi phát sinh lỗi vi phạm mới.
   * **Q4:** *MoMo có hỗ trợ tự động điền thông tin khi mua bảo hiểm ô tô / xe máy không?*
     * **A4:** Có. Khi bạn đã lưu Thẻ Xe Số (Vehicle Profile), toàn bộ thông tin biển số, số khung, số máy và dòng xe sẽ được tự động điền (Auto-fill >80%) khi đăng ký mua bảo hiểm TNDS hoặc Thân vỏ.
   * **Q5:** *Làm sao để tìm vị trí cây xăng Petrolimex hoặc trạm sạc xe điện gần nhất?*
     * **A5:** Bạn truy cập chuyên trang Cây Xăng (`/cay-xang`) hoặc Trạm Sạc (`/tram-sac`), bật vị trí GPS. Hệ thống hiển thị bản đồ định vị các trạm gần bạn nhất kèm chỉ đường Google Maps.
   * **Q6:** *Làm thế nào để kiểm tra xe của tôi có dùng được xăng sinh học E10 hay không?*
     * **A6:** Bạn nhập Hãng xe và Dòng xe vào Công cụ Tra Cứu Tương Thích Xăng E10 trên Trang Chủ Tiện Ích Giao Thông MoMo. Hệ thống sẽ đối soát dữ liệu đăng kiểm và khuyến nghị loại xăng (E10 hay RON 95) cùng cấp dầu nhớt tối ưu cho xe của bạn.

#### C. Cấu Trúc Nội Dung Các Trang Spoke & Standalone Use Cases

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trang / Nhóm Dịch Vụ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Component / Section</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhu Cầu Người Dùng (JTBD)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giải Pháp Cấu Trúc (Solution)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thành Phần UI (UI Components) & Functions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tra Cứu Phạt Nguội</strong><br><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/phat-nguoi/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hero & Tool Input</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn kiểm tra lỗi phạt nguội tức thì."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Form tra cứu trực tiếp bằng Biển số xe không yêu cầu nhập CAPTCHA.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Selector Ô tô/Xe máy + Input Biển số xe + Nút Tra cứu 1-click</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Result & Smart CTA</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn xem chi tiết lỗi và nộp phạt online."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Output kết quả: Xe sạch  ➔  CTA lưu biển số & mua Gói Cảnh báo Tự động (9k/năm); Có lỗi  ➔  Nộp Phạt 1-Click.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Màn hình trả lỗi vi phạm + Banner CTA Universal Link mở App MoMo mua Gói Cảnh báo (9k/năm) / Đóng phạt</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>DVC Guide & SEO Block</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn biết quy trình nộp phạt online chuẩn."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bài viết hướng dẫn 4 bước nộp phạt qua Cổng DVCQG & App MoMo + Bảng tiền phạt.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hướng dẫn nộp phạt online & Bảng tra cứu mức phạt lỗi phổ biến</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Blog & Cẩm Nang</strong><br><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/blog/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Content Index</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn đọc các bài viết tư vấn luật và bảo dưỡng xe."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Kho bài viết được cung cấp bởi <strong>GenAI Content Engine (PLG Project)</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Danh mục bài viết + Grid bài viết + Banner CTA mở App</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Article Detail</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn đọc hướng dẫn luật/mẹo bảo dưỡng chi tiết."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giao diện chi tiết bài viết tư vấn giao thông chuẩn SEO kèm CTA mở App MoMo.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tiêu đề H1 + Nội dung bài viết GenAI + In-Article Smart W2A Widget</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Giá Xăng Dầu</strong><br><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/gia-xang/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Live Price Banner</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn biết giá xăng hôm nay tăng hay giảm."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Banner tự động đồng bộ giá xăng Petrolimex/PVOil Vùng 1 & Vùng 2 thời gian thực.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảng giá xăng RON 95-III, E5 RON 92-II, Dầu Diesel hôm nay</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Price History Chart</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn xem lịch sử biến động giá xăng."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Biểu đồ tương tác theo dõi biến động giá xăng trong 3-6 tháng.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Biểu đồ tương tác biến động giá xăng 3-6 tháng gần nhất</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Station Finder Map</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn tìm cây xăng Petrolimex gần nhất."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ GPS định vị cây xăng Petrolimex/PVOil nhận Ví MoMo.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ tương tác + Danh sách cây xăng nhận MoMo gần bạn</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Smart Push CTA</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn nhận tin báo giá xăng trước khi điều chỉnh."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Form nhập SĐT nhận Push Notification trước kỳ điều hành 15 phút.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Form đăng ký nhận tin báo giá xăng tự động chiều thứ 5</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>GEO Local Pages</strong><br><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tram-sac/</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/garage/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Filter Bar & Map View</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn lọc trạm sạc/garage đúng nhu cầu."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thanh lọc trạm sạc xe điện (VinFast, V-Green & các đối tác / công suất kW) hoặc garage.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bộ lọc Tỉnh/Thành, Quận/Huyện, Loại trạm sạc hoặc Dịch vụ garage</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Map & Location Grid</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn xem bản đồ kèm khoảng cách thực tế."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ tương tác đồng bộ danh sách địa điểm O2O kèm khoảng cách $km$.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ tương tác + Danh sách địa điểm kèm khoảng cách ($km$), địa chỉ</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Merchant Card Snippet</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn chọn địa điểm uy tín và dẫn đường ngay."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Merchant Card gồm điểm rating, nhãn MoMo Verified, nút Dẫn đường & Đặt chỗ.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thẻ địa điểm: Rating, Huy hiệu <em>"Chấp nhận Ví MoMo"</em>, nút Dẫn đường</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bảo Hiểm Ô Tô</strong><br><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-o-to/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hero & Instant Quote</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn tính nhanh phí bảo hiểm TNDS/Thân vỏ."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Form tính phí tức thì hỗ trợ tự động điền (Auto-fill) dữ liệu từ Vehicle Profile.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Form chọn gói bảo hiểm (TNDS / Thân vỏ), chọn Dòng xe</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Comparison Matrix</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn so sánh giá và quyền lợi 9 công ty bảo hiểm."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảng so sánh báo giá & quyền lợi trực quan từ PVI, Bảo Việt, MIC...</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảng so sánh mức phí & quyền lợi bảo hiểm từ 9 nhà bảo hiểm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Purchase CTA & E-Card</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn mua bảo hiểm nhận ấn chỉ điện tử ngay."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nút "Mua Ngay - Cấp Ấn Chỉ Điện Tử Trong 30s" kết nối API nhà bảo hiểm.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nút <em>"Mua Ngay - Cấp Ấn Chỉ Điện Tử Trong 30s"</em></td>
    </tr>
  </tbody>
</table>

### 3.3 Umami Event Tracking theo Luồng Tương Tác (User Journey Events)

Đặc tả các sự kiện Umami bắn về hệ thống theo đúng luồng trải nghiệm người dùng (Touchpoint Journey):

#### A. Luồng Tra Cứu Phạt Nguội & Nộp Phạt (Core Journey on `/tien-ich-giao-thong/` & `/phat-nguoi/`)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Bước (Step)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Touchpoint / Vị Trí</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hành Động Người Dùng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Umami Event Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>Step 1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vehicle Type Selector</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chọn loại phương tiện (Ô tô / Xe máy)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">select_vehicle_type</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>Step 2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Input & Submit Button</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhập Biển số xe (BSX) & Bấm Tra cứu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">submit_license_plate</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>Step 3A</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Result Screen (Xe Sạch)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiển thị màn hình kết quả: Không có lỗi vi phạm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">view_result_clean</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>Step 3B</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Result Screen (Vi Phạm)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiển thị màn hình kết quả: Có lỗi vi phạm phạt nguội</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">view_result_violation</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>Step 4</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Action CTA Button</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bấm Nộp phạt online / Mở App MoMo xử lý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">click_pay_fine</code></td>
    </tr>
  </tbody>
</table>

#### B. Các Luồng Tương Tác Tính Năng Phụ (Secondary Feature Touchpoints)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm Tính Năng / Page</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Touchpoint / Vị Trí</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hành Động Người Dùng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Umami Event Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Quick Grid</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility Cards</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bấm phím tắt chuyển đến các Spoke Pages</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">click_utility_item</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Blog & Cẩm Nang</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">In-Article Smart CTA</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bấm CTA trong bài viết blog mở App MoMo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">click_blog_cta</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Giá Xăng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Subscribe Form</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">nhấp vào nút đăng ký nhận tin báo giá xăng tự động</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">subscribe_gas_price</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trạm Sạc / Garage</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GEO Filter Bar</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chọn Tỉnh/Thành, Quận/Huyện hoặc Loại trạm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">select_geo_filter</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trạm Sạc / Garage</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Merchant Card</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bấm thẻ địa điểm để chỉ đường hoặc đặt chỗ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">click_merchant_item</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bảo Hiểm</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quote / Purchase Button</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bấm xem báo giá / Mua bảo hiểm Ô tô, Xe máy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">click_buy_insurance</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cứu Hộ 24/7</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hotline Button</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">nhấp vào nút gọi tổng đài Cứu hộ 24/7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">click_call_rescue</code></td>
    </tr>
  </tbody>
</table>

## 4. SEO / GEO ONPAGE

### 4.1 Meta Data (Title, Description, Headings, OpenGraph & Social Cards)

#### A. Bảng Công Thức Meta Tag Standards

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại Trang</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Công Thức Tag <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><title></code> (Max 60 chars)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Công Thức <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><meta description></code> (150-160 chars)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Master Hub</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Tiện Ích Giao Thông MoMo - Tra Cứu & Quản Lý Xe 3 Phút</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Cổng tiện ích giao thông MoMo: Tra cứu phạt nguội 0-CAPTCHA, xem giá xăng hôm nay, vị trí trạm sạc VinFast, cây xăng Petrolimex và mua bảo hiểm ô tô online.</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phạt Nguội</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">`Tra Cứu Phạt Nguội CSGT Toàn Quốc (Không CAPTCHA)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo`</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Tra cứu phạt nguội ô tô, xe máy toàn quốc không cần nhập CAPTCHA. Cập nhật dữ liệu từ Cục CSGT real-time. Hướng dẫn nộp phạt online nhanh gọn qua MoMo.</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Blog Article Page</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">`[Tiêu Đề Bài Viết]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cẩm Nang Giao Thông MoMo`</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Mô tả tóm tắt bài viết 150 ký tự chứa từ khóa chính.]</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Giá Xăng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">`Bảng Giá Xăng Dầu Hôm Nay (Mới Nhất Vùng 1 & 2)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo`</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Cập nhật bảng giá xăng dầu RON 95-III, E5 RON 92, Dầu Diesel hôm nay mới nhất theo kỳ điều hành. Danh sách cây xăng Petrolimex/PVOil chấp nhận Ví MoMo.</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trạm Sạc EV</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">`Bản Đồ Trạm Sạc Xe Điện VinFast & V-Green Gần Đấu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo`</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Định vị trạm sạc xe điện VinFast, V-Green gần nhất. Lọc theo cổng sạc, công suất kW, giờ mở cửa và chỉ đường Google Maps nhanh chóng qua MoMo.</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bảo Hiểm Ô Tô</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">`Bảo Hiểm Ô Tô Online (TNDS & Thân Vỏ) - Mua Ngay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo`</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Mua bảo hiểm ô tô TNDS bắt buộc và bảo hiểm thân vỏ online. Báo giá từ 9 công ty bảo hiểm uy tín (PVI, Bảo Việt, MIC), cấp ấn chỉ điện tử tức thì qua MoMo.</code></td>
    </tr>
  </tbody>
</table>

#### B. Quy Chuẩn Heading Hierarchy (H1 - H4)
* **Quy tắc H1:** Mỗi trang có duy nhất **1 thẻ `<h1>`** đặt tại Hero Section chứa từ khóa chính.
* **Cấu trúc phân cấp chuẩn:**
  ```text
  H1: [Từ khóa chính trang]
     ├── H2: [Tính năng / Công cụ tra cứu cốt lõi]
     ├── H2: [Bảng thông tin / Dữ liệu thời gian thực]
     ├── H2: [Hướng dẫn chi tiết luồng sử dụng]
     │      ├── H3: [Bước 1: ...]
     │      └── H3: [Bước 2: ...]
     └── H2: [Câu hỏi thường gặp (FAQ Accordion)]
  ```

### 4.2 Schema.org JSON-LD Specifications

Mỗi loại trang bắt buộc khai báo mã JSON-LD chuẩn trong thẻ `<head>`:

#### A. Master Hub Page (`/tien-ich-giao-thong/`)
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://momo.vn/#website",
      "url": "https://momo.vn/",
      "name": "MoMo"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://momo.vn/" },
        { "@type": "ListItem", "position": 2, "name": "Tiện ích giao thông", "item": "https://momo.vn/tien-ich-giao-thong/" }
      ]
    }
  ]
}
```

#### B. Blog Article Page (`/tien-ich-giao-thong/blog/{article-slug}/`)
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "[Tiêu đề bài viết]",
  "image": "https://img.mservice.io/vehicle-hub/blog-[article-slug].jpg",
  "author": { "@type": "Organization", "name": "MoMo Vehicle Hub Team" },
  "publisher": { "@type": "Organization", "name": "MoMo", "logo": { "@type": "ImageObject", "url": "https://img.mservice.io/logo.png" } },
  "datePublished": "2026-08-01",
  "description": "[Mô tả bài viết]"
}
```

### 4.3 Sitemap & Technical SEO

1. **Cấu trúc Sub-Sitemaps Index (`sitemap_index.xml`):**
   * `sitemap-vehicle-hub.xml`: Trang chủ `/tien-ich-giao-thong/` và các Spoke Pages (`/gia-xang/`, `/tram-sac/`, `/cay-xang/`, `/garage/`) (`priority: 1.0`, `changefreq: daily`).
   * `sitemap-phat-nguoi.xml`: Trang Tra Cứu Phạt Nguội (`/phat-nguoi/`) (`priority: 0.9`, `changefreq: daily`).
   * `sitemap-blog.xml`: Bài viết cẩm nang giao thông (`priority: 0.8`, `changefreq: daily`).
   * `sitemap-bao-hiem.xml`: Trang Bảo Hiểm Ô Tô (`/bao-hiem-o-to/`) & Xe Máy (`/bao-hiem-xe-may/`) (`priority: 0.9`, `changefreq: weekly`).
   * `sitemap-merchant.xml`: Các trang chi tiết Merchant đối tác (`priority: 0.6`, `changefreq: weekly`).
2. **Quy tắc Quản lý Crawl Budget:** Trả mã HTTP `410 Gone` và xóa khỏi Sitemap đối với các trang Merchant ngưng hoạt động.
3. **Canonical Rules:** 100% trang có thẻ canonical tự tham chiếu tuyệt đối.

### 4.4 GEO / AIO (Generative Engine Optimization cho AI Search)

Để tối ưu khả năng xuất hiện trên Google AI Overview, ChatGPT, Perplexity và Gemini:

1. **Direct Answer Block (25 - 40 từ):** Ngay dưới mỗi tiêu đề `<h2>` của khối FAQ hoặc Hướng dẫn, bắt buộc chứa 1 câu trả lời tóm tắt trực tiếp định dạng Entity-Attribute-Value:
   * *Ví dụ:* **"Tra cứu phạt nguội trên MoMo cho phép người dùng kiểm tra lỗi vi phạm giao thông bằng biển số xe trực tiếp 0-CAPTCHA trong 3 giây, tự động đồng bộ dữ liệu từ Cục CSGT."**
2. **Minified HTML Tables:** Đóng gói toàn bộ dữ liệu so sánh phí bảo hiểm, giá xăng dầu, bảng tiền phạt vi phạm bằng thẻ `<table>` HTML chuẩn với `<thead>` và `<tbody>` rõ ràng để AI Bot dễ trích xuất.
3. **Authoritative Citations:** Chèn dẫn nguồn tham chiếu trực tiếp đến các cổng thông tin chính phủ / văn bản pháp luật / đối tác chính thức (Nghị định 100/2019/NĐ-CP, Cục CSGT, Cổng DVCQG).

## 5. CHANGE LOG

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Phiên bản</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Ngày cập nhật</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Người thực hiện</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung thay đổi chính</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>v2.0</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>04/08/2026</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>Web Product Lead</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cập nhật Toàn bộ Kiến trúc & Keyword Dataset Mới:</strong><br>• Cập nhật tổng quy mô phễu tìm kiếm Open Web lên <strong>>20.1M lượt/tháng</strong> từ bộ <strong>11.104 từ khóa độc lập</strong> (17 CSV files).<br>• Bổ sung <strong>Mục 3.2 Product Architecture Classification</strong>: Phân định rõ 3 nhóm (API Components, Calculators & Merchant Routing Pages).<br>• Cập nhật quy tắc <strong>Sync API 100% từ In-App Mini App MoMo</strong> (Single Source of Truth).<br>• Chuẩn hóa quy tắc <strong>KHÔNG dùng URL sub-path Tỉnh/thành</strong> (loại bỏ <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">{tinh-thanh}</code>), giữ duy nhất Hãng xe/Dòng xe có URL mở rộng.<br>• Định vị Phí Đường Bộ thuộc bài viết Blog & Cẩm Nang (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/blog/*</code>).</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>v1.0</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">29/07/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Web Product Lead</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khởi tạo tài liệu PRD Vehicle Hub Web Platform.</td>
    </tr>
  </tbody>
</table>
