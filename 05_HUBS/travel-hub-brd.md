# BRD: Travel Hub (MoMo Travel) - Trung Tâm Cẩm Nang & Đặt Vé Du Lịch - Đi Lại

> - **Dự án:** Travel Hub (Cổng Thông Tin & Đặt Dịch Vụ Du Lịch - Đi Lại)
> - **URL chính:** momo.vn/du-lich-di-lai
> - **Khối phụ trách:** Growth Platform Division (GPD)
> - **Owner:** Web Platform Team (GPD)

## 1. BUSINESS CONTEXT & PRODUCT OVERVIEW

### 1.0 Executive Overview & Product Statement
**Travel Hub (MoMo Travel)** là trung tâm cẩm nang và đặt dịch vụ du lịch đa nền tảng trên Web Platform  do Web Platform (GPD) làm chủ. Hub kết nối các bài cẩm nang du lịch tự túc pSEO chất lượng cao với công cụ đặt eSIM du lịch quốc tế nhận mã QR tức thì, trình so sánh vé máy bay, vé xe khách liên tỉnh và khách sạn, giúp MoMo đón đầu hành vi tìm kiếm tự nhiên từ Google và thúc đẩy doanh thu mảng du lịch.

### 1.1 Market Sizing & Target Audience
* **Bối cảnh:** Nhu cầu du lịch tự túc nội địa & quốc tế tăng cao. Khách du lịch luôn tìm kiếm cẩm nang điểm đến, so sánh vé máy bay, vé xe khách, khách sạn và SIM du lịch trước chuyến đi.
* **Đối tượng:** Khách du lịch tự túc nội địa & outbound quốc tế, người đi công tác, HSSV & gia đình di chuyển tựu trường/lễ tết.

### 1.2 Product Vision & Statement
**Travel Hub (MoMo Travel)** là trung tâm du lịch trên Web Platform  do Web Platform (GPD) làm chủ. Hub kết nối cẩm nang du lịch tự túc với các công cụ so sánh & đặt vé máy bay, xe khách, khách sạn và eSIM du lịch quốc tế, đón đầu hành vi tìm kiếm tự nhiên và dẫn dắt giao dịch chuyển đổi Web-to-App.

### 1.3 Product-Led Growth (PLG) Strategy
* **Content-led Booking:** Người dùng đọc Cẩm nang du lịch trên Web ──► Thấy Widget gợi ý lịch trình kèm nút *"Đặt SIM eSIM Thái Lan nhận QR tức thì"* hoặc *"So sánh vé máy bay giá rẻ"* ──► Mua trực tiếp trên Web hoặc mở App MoMo thanh toán.

### 1.4 Goals & Key Metrics
* **eSIM Revenue:** Đạt 107.446 MAU; 161.169 Giao dịch; **27,4 tỷ VNĐ GMV** từ eSIM du lịch.
* **Web Traffic:** >250.000 PageViews/tháng cho cẩm nang du lịch pSEO.
* **Hotel Cross-sell:** Tỷ lệ bán chéo khách sạn từ cẩm nang >15%.

## 2. TARGET PERSONAS & JTBD

### 2.1 Target Personas
1. **Khách du lịch Outbound quốc tế:** Cần mua eSIM Data nhận QR tức thì để có mạng ngay khi hạ cánh, xem cẩm nang ăn chơi tự túc.
2. **Khách du lịch nội địa / Đi công tác:** So sánh vé máy bay giá tốt, đặt vé xe khách liên tỉnh, đặt phòng khách sạn/homestay.

### 2.2 Jobs-to-be-Done (JTBD) & Pain Points
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm người dùng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pain Points</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoMo Solution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Khách đi nước ngoài</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lo mất kết nối internet khi hạ cánh; Đổi SIM vật lý rắc rối</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua eSIM du lịch online trên Web 1-click ──► Nhận mã QR kích hoạt qua Email/App.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Khách đặt vé di chuyển</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giá vé máy bay/xe khách biến động, khó so sánh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trình so sánh giá vé máy bay/xe khách đa hãng minh bạch.</td>
    </tr>
  </tbody>
</table>

## 3. USER FLOWS & ARCHITECTURE

### 3.1 Web Onboarding Flow
```
[1. Chọn Nước Đến trên Web Platform (Thái Lan, Nhật, Hàn...)] ──► [2. Chọn Gói Cước Data & Số Ngày]
                                                                            │
                                                                            ▼
[4. Nhận Mã QR Kích Hoạt eSIM Qua Email / App MoMo] ◄── [3. Thanh Toán 1-Click Trực Tiếp Trên Web]
```

## 4. DETAILED USE CASES & KPIS

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Use Case</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả & Luồng sử dụng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KPIs Cam kết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Travel eSIM Checkout</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu gói Data eSIM quốc tế, chọn số ngày và thanh toán nhận mã QR tức thì.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">107k MAU; 27,4 tỷ GMV; Tỷ lệ đóng góp Web GMV >10%.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Flight Search Engine</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tìm kiếm, so sánh giá vé máy bay nội địa & quốc tế đa hãng hàng không.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic Clicks từ khóa "Vé máy bay"; Tỷ lệ chuyển đổi W2A CR.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bus & Train Booking</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu tuyến đường, lịch trình nhà xe liên tỉnh và đặt vé xe khách/tàu hỏa.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phủ trang pSEO tuyến đường hot; Lượt đặt vé xe liên tỉnh.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hotel & Homestay Finder</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tìm kiếm, so sánh giá phòng và đặt khách sạn/homestay tại các điểm du lịch.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">>250k PageViews/tháng cẩm nang; Cross-sell Rate >15%.</td>
    </tr>
  </tbody>
</table>

## 5. CONTENT & SEO/GEO STRATEGY

* **Cẩm nang pSEO Du lịch:** Tạo hệ thống bài cẩm nang lịch trình tự túc chuẩn SEO (`momo.vn/travel/cam-nang-thai-lan`).
* **Tối ưu GEO (AI Search):** Cấu trúc danh sách *"Top địa điểm phải đi tại Bangkok"* giúp ChatGPT/Gemini trích dẫn nguồn MoMo.

## 6. GAMIFICATION & PROMOTIONS

* **Vòng Quay Mùa Du Lịch:** Trúng voucher giảm 50% vé máy bay hoặc miễn phí eSIM du lịch khi chia sẻ cẩm nang chuyến đi.

## 7. COMPLIANCE & RISK MANAGEMENT

* **Quy định du lịch:** Hiển thị rõ ràng chính sách hoàn/hủy/đổi vé máy bay & xe khách theo quy định nhà cung cấp.
* **Bảo mật eSIM:** Mã QR eSIM mã hóa và gửi đến đúng email/tài khoản mua.

