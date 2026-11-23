> - **Dự án:** OTA - BUS (Đặt vé xe khách)
> - **URL chính:** momo.vn/ve-xe
> - **Khối phụ trách:** GPD - OTA (Non-Air)
> - **Owner:** Web Platform
> - **Phê duyệt:** Web Product Lead (Hiến)
> - **Phiên bản:** 2.0 - Tháng 05/2026
> - **Trạng thái:** Draft
> - **Business Model:** Marketplace - MoMo là nền tảng tra cứu, đặt và thanh toán vé xe khách; thu phí từ nhà xe đối tác

---

> **Problem:** Hàng triệu người Việt tìm vé xe khách mỗi tháng - không tìm thấy MoMo, dù MoMo đang bán vé của hơn 500 nhà xe.
>
> **KPI Owned:** Transactions (số vé bán được) từ web channel → attributed via Appsflyer
>
> **Conversion Flow:** Search "vé xe A đi B" → momo.vn/ve-xe → Chọn nhà xe + giờ đi → Mở MoMo App → Thanh toán vé

---

## 1. Executive Summary

**Situation**

Người dùng Việt Nam có nhu cầu đặt vé xe khách rất lớn và đang tìm kiếm trên Google với tổng lượng tìm kiếm ước tính hơn 5 triệu lượt/tháng (theo Media Team Plan 2025). Hành vi tìm kiếm trải dài qua nhiều intent: tuyến đường cụ thể ("vé xe Sài Gòn đi Đà Lạt"), nhà xe cụ thể ("vé xe Phương Trang"), điểm đến ("xe đi Đà Lạt"), và seasonal peak (vé xe Tết). MoMo hiện là đối tác đặt vé của hơn 500 nhà xe và đã có sản phẩm hoạt động trong App, nhưng web channel gần như vắng mặt trên Search - traffic organic năm 2024 chỉ đạt 84.466 sessions toàn năm, tương đương chưa đến 1,7% market share.

**Complication**

Khoảng cách giữa inventory MoMo (hơn 500 nhà xe) và số user thực sự đặt được vé qua web là rất lớn. Ba lý do từ góc nhìn người dùng:

Thứ nhất, user search "vé xe Phương Trang đi Nha Trang" không gặp trang MoMo nào. Họ vào VeXeRe - dù MoMo có đầy đủ nhà xe đó - vì momo.vn chưa có trang riêng cho từng tuyến đường và từng nhà xe.

Thứ hai, user vào được momo.vn/ve-xe nhưng không đủ thông tin để quyết định: thiếu lịch khởi hành, thiếu giá, thiếu đánh giá nhà xe. Họ thoát ra và tìm chỗ khác.

Thứ ba, user muốn đặt vé nhưng không biết bước tiếp theo - không có luồng rõ ràng từ web vào App để hoàn tất booking.

**Resolution**

Product job cốt lõi: Người dùng tìm vé xe trên Google gặp đúng trang momo.vn với thông tin họ cần - nhà xe, giờ đi, giá, đánh giá - ra quyết định ngay, sau đó mở MoMo App hoàn tất đặt vé trong một flow liền mạch không cần nhập lại.

Nền tảng để đáp ứng toàn bộ search intent: 8 loại trang (Routes, Destination, Bus Operator, Bus Operator + Route, Bus Terminal, Bus Terminal + Destination, Bus Type/Limousine, Vé Xe Tết) - kết hợp blog content dẫn về các trang giao dịch và booking entry point trực tiếp trên trang.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Market Size

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giá trị</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổng lượng search/tháng (ước tính)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~5.000.000 searches</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Media Team Plan 2025 [cần verify GSC + Ahrefs]</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Market share momo.vn hiện tại (2024)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~1,7%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">84.466 sessions / 5M market</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Target market share 2025 (Base Case 1)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4,4%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.035.000 sessions</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Target market share 2025 (Base Case 3)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5,2%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.500.000 sessions</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số nhà xe trên MoMo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">500+</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Theo PPTX slide 4</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tickets processed (top merchant)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">571.861 (xe Phương Trang)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dashboard BUS Performance</td>
    </tr>
  </tbody>
</table>

### 2.2 Hiện Trạng Traffic

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Năm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Total Sessions</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Click to App</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">CR W2A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2022</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~17.886</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa có data</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2023</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">75.266</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3.319</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~4,4%</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2024</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">84.466</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">9.085</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~10,8%</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2025 (Base Case 1 target)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.035.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">73.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~7,1%</td>
    </tr>
  </tbody>
</table>

*Nhận xét: CR W2A 2024 đạt 10,8% là tín hiệu tốt - người dùng đến từ organic có intent cao. Vấn đề là volume traffic quá thấp. Growth 2022-2024 chủ yếu đến từ tự nhiên, chưa có đầu tư có hệ thống.*

### 2.3 Competitive Landscape

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đối thủ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm mạnh</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm yếu so với MoMo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">VeXeRe (vexere.com)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàng nghìn trang programmatic, domain authority cao, blog du lịch tốt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không có super-app ecosystem, không có MoMo Pay</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BusMap</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">App-first, dữ liệu realtime tốt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web channel yếu hơn VeXeRe</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Baolau.vn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO blog mạnh, coverage tuyến đường rộng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ít nhà xe hơn MoMo</td>
    </tr>
  </tbody>
</table>

**MoMo's moat:** Inventory nhà xe lớn (500+), hệ sinh thái thanh toán, user trust. Chưa được khai thác qua web channel.

### 2.4 Keyword Clusters

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Intent</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ví dụ keyword</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Volume Est.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Routes</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Commercial - Do</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vé xe Sài Gòn đi Đà Lạt"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus Operator</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Commercial - Do</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vé xe Phương Trang", "xe Điền Linh"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational + Commercial</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"xe đi Đà Lạt", "vé xe đi Nha Trang"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus Terminal</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"bến xe Miền Tây", "bến xe Miền Đông"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus Type</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Commercial</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"xe limousine Sài Gòn Đà Lạt"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Seasonal - Tết</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Commercial - High urgency</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vé xe Tết 2026", "vé xe tết Sài Gòn"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Spike cao theo mùa</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog / Guide</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"kinh nghiệm đi xe khách", "nhà xe uy tín"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
    </tr>
  </tbody>
</table>

---

## 3. Định Hướng Dự Án

### Product Job Cốt Lõi

Người dùng search vé xe trên Google - tìm thấy momo.vn với đúng thông tin họ cần (nhà xe, tuyến đường, giá, đánh giá) - đưa ra quyết định ngay trên web - mở App để thanh toán nhanh.

3 outcomes phát sinh từ product job này:
- New user acquisition: người dùng chưa có MoMo App install App để thanh toán vé
- Re-engagement: người dùng đã có App quay lại dùng tính năng vé xe
- Brand recall: MoMo Travel - BUS được associate với search intent vé xe khách

### Dự án này KHÔNG phải là:

- Một chiến dịch paid traffic hay remarketing
- Một tính năng App mới - web là entry point, App là transaction layer
- Blog travel thuần túy - content phải anchor vào booking intent
- Một project độc lập: BUS web là một phần của hệ sinh thái OTA (phối hợp với Air, Hotel)

### PLG Hook

PLG hook của BUS là **Search Widget + Booking Flow liền mạch trên web**. Cụ thể:

User search tuyến đường → vào trang Routes → thấy danh sách nhà xe kèm giá realtime → chọn chuyến → deep link mở MoMo App với pre-fill thông tin → thanh toán trong App.

Khác với use case Vay Nhanh hay BH có calculator giúp user convert mà không cần login, BUS có booking flow tự nhiên dẫn vào App - đây là PLG hook mạnh vì user đã ở bước "muốn mua" khi vào trang.

### Pre-conditions - Phải Giải Quyết Trước Khi Commit Build

**Thiếu 1 trong 4 - dừng lại.**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pre-condition</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trạng thái</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner giải quyết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PC1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Các landing pages (Routes, Destination, Operator...) hoàn thành xây dựng và được Google index trước thời điểm T</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang triển khai</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform + Dev</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PC2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content API hoặc ChatGPT-generated content pipeline hoạt động và phủ đủ trang programmatic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pilot - chưa confirm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Media Team + Tech</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PC3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Internal Link API hoặc cơ chế thay thế giữa các page types được cấu hình đúng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa giải quyết</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tech</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">P4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tracking web (GA4 event + Appsflyer W2A) được setup trước khi launch để có baseline data</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa setup</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Data Tracking</td>
    </tr>
  </tbody>
</table>

---

## 4. JTBD Analysis

### Job 1: "Tôi cần tìm chuyến xe cụ thể từ A đến B, chọn nhà xe và giờ đi phù hợp"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chi tiết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu chuyến xe theo tuyến đường + ngày đi, xem nhà xe, giờ khởi hành, giá vé</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần đi về quê, đi du lịch, đi công tác - thường lên kế hoạch 1-7 ngày trước</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Muốn chắc chắn chọn được nhà xe uy tín, không bị miss chuyến</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua vé xong chia sẻ link lên nhóm chat cho cả nhà confirm giờ đi</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vé xe Sài Gòn Đà Lạt" → /ve-xe/ve-xe-khach-tu-ho-chi-minh-di-da-lat → Chọn chuyến → Mở App → Thanh toán</td>
    </tr>
  </tbody>
</table>

### Job 2: "Tôi đã biết nhà xe muốn đi, cần xem lịch + đặt vé nhanh"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chi tiết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search tên nhà xe, xem tất cả tuyến đường nhà xe đó chạy, chọn tuyến phù hợp</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đã dùng nhà xe này trước đó và hài lòng, muốn dùng lại</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tiết kiệm thời gian so sánh - đã có preference nhà xe</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhắn bạn: "Đi Phương Trang là ổn, mình hay đặt trên MoMo" - không cần giải thích thêm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vé xe Phương Trang" / "xe Điền Linh Limousine" → /ve-xe/xe-phuong-trang → Chọn tuyến + chuyến → Mở App</td>
    </tr>
  </tbody>
</table>

### Job 3: "Tôi muốn đến một điểm đến cụ thể, chưa biết chọn nhà xe nào"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chi tiết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xem tất cả nhà xe có tuyến đến điểm đến mình muốn, so sánh giá và thời gian</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lên kế hoạch chuyến đi chưa rõ lịch trình - đang ở giai đoạn khám phá</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Muốn có overview toàn diện trước khi quyết định</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Share link trang Đà Lạt cho cả nhóm cùng chọn nhà xe và chuyến đi</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"xe đi Đà Lạt", "vé xe đến Nha Trang" → /ve-xe/da-lat → Chọn nhà xe → Mở App</td>
    </tr>
  </tbody>
</table>

### Job 4: "Tôi cần đặt vé xe Tết sớm trước khi hết chỗ"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chi tiết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xem vé xe Tết còn hay hết, nhà xe nào còn chỗ, giá bao nhiêu</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gần đến Tết (tháng 11-12) + nghe người quen nói vé sắp hết</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lo lắng không có vé về quê - high urgency, high anxiety</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhắn anh chị: "Còn vé Tết đó, đặt ngay đi trước khi hết" - tự mình đã check rồi</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"vé xe Tết 2026", "mua vé xe Tết sớm" → /ve-xe/ve-xe-tet → Booking → Mở App</td>
    </tr>
  </tbody>
</table>

### Job 5: "Tôi muốn đi xe limousine/VIP cho chuyến đi thoải mái hơn"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chi tiết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tìm nhà xe có dịch vụ limousine cho tuyến cụ thể, xem chất lượng xe</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuyến đi xa (>3 giờ), đi cùng đối tác/người lớn tuổi, không muốn vé bình thường</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Muốn thoải mái, thể hiện mình chọn lựa tốt</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Book limousine cho cả team đi công tác - chọn MoMo trông chuyên nghiệp hơn đặt lẻ từng người</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"xe limousine Sài Gòn Đà Lạt" → /ve-xe/limousine-tu-ho-chi-minh-di-da-lat → Mở App</td>
    </tr>
  </tbody>
</table>

### Job 6: "Tôi cần thông tin về bến xe (giờ mở cửa, bến nào phù hợp, xe nào xuất phát từ bến này)"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chi tiết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xem nhà xe xuất phát từ bến xe cụ thể, giờ chạy, cách di chuyển đến bến</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không rõ mình nên ra bến nào, cần chọn bến gần nơi ở</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lo lắng ra sai bến, miss xe</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tự tìm được thông tin bến xe mà không cần hỏi người quen - chủ động lộ trình</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"bến xe Miền Đông đi Đà Nẵng" → /ve-xe/ben-xe-mien-dong-di-da-nang → Chọn nhà xe → Mở App</td>
    </tr>
  </tbody>
</table>

---

## 5. Kiến Trúc Web / Phạm Vi Build

### 5.1 Sitemap - Hub & Spoke

```
/ve-xe                              (Hub - Home)
├── /ve-xe/ve-xe-khach-tu-[A]-di-[B]      (Routes - pSEO)
├── /ve-xe/[tinh-thanh-pho]               (Destination - pSEO)
├── /ve-xe/xe-[nha-xe]                    (Bus Operator - pSEO)
├── /ve-xe/nha-xe-[nha-xe]-tu-[A]-di-[B]  (Bus Operator + Route - pSEO)
├── /ve-xe/ben-xe-[ben-xe]                (Bus Terminal - pSEO)
├── /ve-xe/ben-xe-[ben-xe]-di-[diem-den]  (Bus Terminal + Destination - pSEO)
├── /ve-xe/limousine-tu-[A]-di-[B]        (Bus Type - pSEO)
├── /ve-xe/ve-xe-tet                      (LDP Seasonal)
├── /ve-xe/khuyen-mai                     (Promotions)
├── /ve-xe/blog                           (Blog Hub)
│   └── /ve-xe/blog/[slug]               (Blog Articles)
└── /ve-xe/tra-cuu-ve                     (Search Tool)
```

### 5.2 URL Architecture

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Page Type</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Pattern</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đợt Triển Khai</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Volume Potential</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Số URL ước tính</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Home</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao (head term)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Routes</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe/ve-xe-khach-tu-[A]-di-[B]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rất cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">500-1.000+</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe/[tinh-thanh-pho]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">63 tỉnh thành</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus Operator</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe/xe-[nha-xe]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">500+ nhà xe</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus Operator + Route</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe/nha-xe-[nha-xe]-tu-[A]-di-[B]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rất cao (long-tail)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.000+</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus Terminal</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe/ben-xe-[ben-xe]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">50-100 bến xe</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus Terminal + Destination</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe/ben-xe-[ben-xe]-di-[diem-den]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">200+</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus Type (Limousine)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe/limousine-tu-[A]-di-[B]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100-200</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LDP Tết</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe/ve-xe-tet</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 1 (seasonal)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Spike cao tháng 11-1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1 (evergreen URL)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe/blog + articles</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình - dài hạn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">200-800 bài</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Promotions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/ve-xe/khuyen-mai</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
    </tr>
  </tbody>
</table>

### 5.3 On-Page Component Anatomy (Các trang Đợt 1)

**Routes Page - /ve-xe/ve-xe-khach-tu-[A]-di-[B]**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Block</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">SEO Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Breadcrumb</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo > Vé xe khách > Vé xe đi từ A đến B</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Schema BreadcrumbList</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">H1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Danh sách các chuyến xe từ A đi B"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Primary keyword target</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search Widget (Product)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Module tìm vé theo ngày/người</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PLG hook - booking entry</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Long Content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Top XX nhà xe từ A đi B - có Table of Contents, outline từng nhà xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Semantic depth, internal linking</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Navigation Block</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">20 anchor text Routes liên quan (B đi C, D đi B...)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Internal linking, crawl depth</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog Embed</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3-4 bài blog liên quan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">EEAT, semantic relevance</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5 câu hỏi về tuyến đường</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQPage schema, AEO</td>
    </tr>
  </tbody>
</table>

**Bus Operator Page - /ve-xe/xe-[nha-xe]**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Block</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">SEO Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Breadcrumb</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo > Vé xe khách > Nhà xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Schema BreadcrumbList</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">H1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Đặt vé xe [Tên nhà xe] với mức giá tốt nhất trên MoMo"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Brand + commercial intent</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giới thiệu nhà xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mô tả sơ lược, ảnh nhà xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">E-E-A-T</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Long Content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">XX tuyến đường nhà xe hoạt động</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Programmatic content</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5 câu hỏi về nhà xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQPage schema</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog Embed</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bài blog liên quan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Internal linking</td>
    </tr>
  </tbody>
</table>

### 5.4 Schema Requirements

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Page Type</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Schema</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Routes, Bus Operator + Route</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BusTrip, BusStop, Product, Offer</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ItemList, Place</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus Operator</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LocalBusiness, Review</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus Terminal</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Place, LocalBusiness</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Article, BreadcrumbList</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LDP Tết</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Event, Offer</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tất cả</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQPage (trên các trang có FAQ block)</td>
    </tr>
  </tbody>
</table>

---

## 6. Success Metrics

### North Star Metric

**Transactions (số vé bán được) từ web channel - được tracked via Appsflyer**

Lý do chọn Transactions thay vì W2A: W2A đo việc user mở App nhưng chưa xác nhận mua vé. Transactions = vé bán thành công sau thanh toán - đây mới là bước tạo revenue trực tiếp cho MoMo từ web channel. W2A và Organic Sessions là Tier B metrics đo tiến trình funnel.

*KPI Alignment Note: Giai đoạn đầu khi Transactions baseline chưa có - track W2A làm proxy. Sau 30 ngày đủ data Appsflyer thì chuyển North Star về Transactions.*

### Targets (Base Case 1 - Recommended)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lane</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target 2025</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Timeframe</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tracking</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactions (vé bán được)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">North Star</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Establish baseline T+1, set target T+3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T+12</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Click to App (W2A)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier B</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">73.100 clicks</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T+12</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 + Appsflyer</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic Sessions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier B</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.035.000 sessions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T+12</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC + GA4</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">W2A Conversion Rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier B</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~7,1%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">EOY 2025</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic Market Share</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier B</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4,4% của 5M search/month</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T+12</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC + SEO tools</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Keyword Top 10 (Routes)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier B</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[cần define số lượng cụ thể]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T+6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Indexed Pages</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier B</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[cần define - ước tính 2.000+ URLs]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T+3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC</td>
    </tr>
  </tbody>
</table>

---

## 7. Dependencies & Constraints

### Dependencies

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dependency</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Blocker?</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform - Page Build</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hoàn thành build 8 loại page types trước thời điểm T launch</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang triển khai</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tech - Google Indexing</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Các trang phải được Google index trước T để có thời gian rank</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phụ thuộc Pre-condition PC1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tech - Content Pipeline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ChatGPT pipeline hoặc Content API generate long content cho programmatic pages</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pilot chưa confirm</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tech - Internal Link API</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cơ chế cross-link tự động giữa Routes/Operator/Destination</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa giải quyết</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">App Data Tracking</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer setup W2A attribution cho BUS</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa setup</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Tracking (GA4)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Event tracking setup trước launch: page view, CTA click, booking initiation</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa setup</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BU/PO OTA</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xác nhận danh sách nhà xe, tuyến đường, giá realtime được expose qua API cho web</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần confirm</td>
    </tr>
  </tbody>
</table>

### Constraints

- KHÔNG can thiệp UX/UI của booking flow - Media Team chỉ đề xuất Canonical, không yêu cầu chỉnh sửa trang payment
- KHÔNG build mobile app riêng cho BUS web - toàn bộ transaction xảy ra trong MoMo App
- Canonical phải được set đúng trên tất cả trang parameter (date, number of passengers) về trang canonical Routes/Operator
- Content có liên quan đến giá vé phải được cập nhật realtime hoặc ghi rõ disclaimer "giá tham khảo, có thể thay đổi" để tránh YMYL violation
- Google Core Algorithm Updates có thể tác động đến ranking tại 4 thời điểm/năm (tháng 3, 6, 9, 12) - không thể kiểm soát

---

## Change Log

- **Tháng 05/2025 (v1.0):** Khởi tạo BRD từ 3 input: Dashboard BUS Performance, Media Team Plan 2025, Advanced Mini Web PPTX. Base Case 1 được chọn làm reference target chính.
- **Tháng 05/2026 (v2.0):** Apply BRD CEO Standard - (1) Fix Problem Statement: bỏ SEO language, reframe user-centric; (2) Fix Complication: bỏ technical SEO, giữ user experience framing; (3) Fix Resolution: product job first, không liệt kê features trước; (4) Fix North Star: W2A → Transactions; (5) Fix 6 Social JTBD: bữa tối test; (6) Remove Section 5.5 Technical Foundation (→ PRD); (7) Remove Quarterly Ramp + Pilot Gate (→ Action Plan); (8) Remove Backlink Budget + SEM Support khỏi Dependencies (→ Action Plan) (Hiến).
