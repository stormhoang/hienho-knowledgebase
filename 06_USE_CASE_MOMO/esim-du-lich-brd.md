# BRD: eSIM Du Lịch

> - **Dự án:** eSIM Du Lịch - Web Growth & SEO/GEO
> - **URL chính:** momo.vn/esim-du-lich
> - **Khối phụ trách:** PS (Payment Services) - Telco
> - **Phiên bản:** 1.4 · Tháng 6/2026
> - **Trạng thái:** Active (Scope: Outbound & Media Team eSIM - Migration to MoSpark)

---

## 1. Executive Summary

### 1.1 Elegant Problem Framing
- **Vấn đề cốt lõi:** Khi chuẩn bị đi du lịch nước ngoài, người Việt cực kỳ sợ bị "mất kết nối mạng" khi hạ cánh, hoặc sợ "phát sinh cước ngoài ý muốn" roaming. Mua SIM vật lý thì rườm rà, cài eSIM quốc tế (Airalo) thì rào cản ngôn ngữ và khó thanh toán.
- **Giải pháp (The "What"):** Biến MoMo thành kênh mua eSIM du lịch "Nhanh - Tiện - An Tâm". Thanh toán 1-chạm bằng ví, nhận mã QR và cài đặt ngay tại nhà, xuống máy bay là có mạng.

### 1.2 Situation & Complication
MoMo phân phối eSIM qua đối tác Gohub (150+ quốc gia). Tuy nhiên, MoMo chưa được định vị trong đầu user là kênh mua SIM du lịch - mindshare thuộc về Airalo, Klook, Gohub. Keyword pool ~38.050 SV/tháng đang bị bỏ ngỏ vì không có Web touchpoint. MoMo có lợi thế distribution rõ ràng (12.8M user, thanh toán seamless) nhưng Web contribution vào tổng Trans hiện tiệm cận 0%.

### 1.3 Resolution
Dự án xây dựng cluster web eSIM Du Lịch gồm 1 Hub page, 10 Destination pages, và Blog cluster theo mô hình Intent-based Filtering. Lợi thế cạnh tranh của MoMo không nằm ở bản thân gói eSIM mà ở **distribution + payment seamless + trust** từ hệ sinh thái Fintech lớn nhất VN.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Thị trường

- eSIM global: $2.45B (2024), CAGR 14% đến 2032
- Thị trường SIM du lịch Việt Nam: 1K-1.5K tỷ VNĐ/năm, tăng trưởng nhanh
- 9 tháng đầu 2025: 5.44 triệu lượt người Việt xuất cảnh (+33.1% YoY)
- 22M+ thiết bị hỗ trợ eSIM tại Việt Nam
- Xu hướng người Việt mua eSIM trước chuyến đi phù hợp funnel digital của MoMo

### 2.2 Competitive Landscape

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Player</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm mạnh</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm yếu vs MoMo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Gohub</strong> (đối tác)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dẫn đầu thị trường, 195+ quốc gia</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Brand awareness thấp với user phổ thông</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Gloka</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">B2C mạnh, SEO tốt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không có siêu app distribution</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Airalo</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Global #1, brand quốc tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không bản địa hóa cho người Việt</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Klook</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">OTA distribution, SV đáng kể</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không phải core product</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Traveloka</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">OTA lớn, đông user Việt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SIM du lịch không phải core</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Sàn TMĐT</strong> (Shopee, Lazada)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đa dạng gói, giá cạnh tranh, review nhiều</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CSKH yếu, không chuyên SIM</td>
    </tr>
  </tbody>
</table>

**Strategic position:** MoMo không cạnh tranh trên sản phẩm eSIM - cạnh tranh trên **distribution, UX, và trust**. User MoMo sẵn có ví và thẻ liên kết - friction mua thấp hơn bất kỳ competitor nào.

**SWOT:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Strengths</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Weaknesses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tệp 12.8M A30 users, traffic tự nhiên cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa được định vị "chuyên du lịch" trong đầu user</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lợi thế thanh toán all-in-one</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa có USP khác biệt, dễ bị so sánh giá</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Brand awareness cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chi phí marketing hạn chế</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Danh mục rộng (105+ quốc gia), đa dạng khoảng giá</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SIM phụ thuộc chính sách viễn thông đối tác</td>
    </tr>
  </tbody>
</table>

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Opportunities</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Threats</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Người Việt xuất cảnh tăng >33% (2025)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhiều player lâu năm (Klook, Traveloka, Trip.com)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xu hướng mua eSIM trước chuyến đi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sàn TMĐT dễ cạnh tranh giá</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">22M+ thiết bị hỗ trợ eSIM</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhanh mất thị phần nếu không có chiến lược đặc biệt</td>
    </tr>
  </tbody>
</table>

### 2.3 Keyword Opportunity (450 từ khóa, 50.850 SV/tháng)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">SV/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">eSIM Chung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8.510</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub page</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Việt Nam (Media Team)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">12.800</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination page cho khách nước ngoài vào VN</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">eSIM + SIM Trung Quốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">7.850</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang lớn nhất - có GFW caveat</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sim Ngoại Quốc Chung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4.100</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub + blog</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thái Lan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3.930</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination page</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhật Bản</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.950</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination page</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Singapore</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.530</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination page</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cẩm nang / How-to</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.430</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog cluster</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàn Quốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.160</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination page</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Châu Âu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.090</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination page</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mỹ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">900</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination page</td>
    </tr>
  </tbody>
</table>

**SEM keyword data (bổ sung):**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster SEM</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tổng SV</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Keywords tiêu biểu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sim Trung Quốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5.510</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">sim trung quốc</code> (1.600), <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">mua sim trung quốc</code> (1.000)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Travel Sim Overall</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4.080</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim du lịch</code> (1.300), <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">sim du lịch</code> (880)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sim Hàn Quốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.450</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">sim hàn quốc</code> (320), <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim hàn quốc</code> (320)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vietnam eSIM (Media Team)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">12.800</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">vietnam esim</code> (9.900), <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">best esim for vietnam</code> (1.900)</td>
    </tr>
  </tbody>
</table>

**4 Strategic Observations:**

1. **Intercept competitor intent:** `cách chuyển vùng quốc tế viettel` (1.000 SV) + `mobi` (260 SV) = 1.260 SV user đang tìm giải pháp thay thế - moment dễ convert nhất. Cần 1 bài blog comparison capture query này.
2. **Bilingual queries đáng kể:** `esim thailand` (480), `china esim` (170), `korea esim` (110) - người Việt search tiếng Anh khi biết rõ điểm đến. Xử lý bằng bilingual title tag + H2 trong body, không cần trang riêng.
3. **Loại keyword sai intent:** `mua sim trung quốc vĩnh viễn` (390 SV) - nhu cầu SIM vật lý dài hạn, không match eSIM du lịch. Loại khỏi danh sách.
4. **Branded competitor keywords:** `sim klook` (50), `esim gigago` (70) - chỉ intercept qua blog comparison, cần approval trước khi viết.

---

## 3. Business Context & Market Intelligence

### 3.1 User Funnel (A30 Base)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Stage</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Số lượng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">% Base</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">CR sang stage tiếp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổng A30 Users</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">12.8M</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Du lịch nước ngoài (2025)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">771K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6.0%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6%</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dùng SIM kết nối mạng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">331K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.6%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">43%</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trực tiếp mua SIM</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">159K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.2%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">48%</td>
    </tr>
  </tbody>
</table>

*Lưu ý: Chỉ 48% người dùng SIM trực tiếp mua - phần còn lại mua hộ người khác hoặc 1 người phát hotspot cho cả nhó.*

### 3.2 Market Sizing

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giá trị</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TAM (tổng chi tiêu SIM du lịch A30)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~171 tỷ VNĐ/năm</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SAM (nhóm mua SIM online)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~143.5 tỷ VNĐ/năm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo GMV hiện tại (2025)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">16 tỷ VNĐ (~11% SAM)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Target GMV 2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">48 tỷ VNĐ (+300%)</td>
    </tr>
  </tbody>
</table>

### 3.3 KPI Targets Q3/2026

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KPI</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">T7/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">T8/2026 (PEAK)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">T9/2026 (PEAK)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Q3 Total</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">vs Q2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MAU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">32.520</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">31.219</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">43.707</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">107.446</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">+77%</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trans</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">48.780</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">46.829</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">65.560</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">161.169</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">+77%</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GMV (VNĐ)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8.29 tỷ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">7.96 tỷ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">11.15 tỷ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">27.4 tỷ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">+77%</td>
    </tr>
  </tbody>
</table>

### 3.4 Web Contribution Target

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">T7/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">T8/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">T9/2026</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web % contribution</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">10%</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Trans (absolute)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.951</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.810</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6.556</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web GMV</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">331.7M VNĐ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">477.6M VNĐ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.114.5M VNĐ</td>
    </tr>
  </tbody>
</table>

### 3.5 Destination Data - Lượt khách Việt xuất cảnh (2024)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Quốc gia</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lượt khách VN</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">FIT ratio</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Est. FIT</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Audience chính</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung Quốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~1.400.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">62%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">868.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FIT + GIT</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thái Lan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~920.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">58%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">533.600</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FIT</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhật Bản</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~710.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">35%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">248.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GIT</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàn Quốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~615.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">62%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">381.300</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FIT</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Singapore</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~480.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">75%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">360.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FIT</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Malaysia</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~420.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">65%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">273.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FIT</td>
    </tr>
  </tbody>
</table>

*FIT = Free Independent Traveler (tự đi, target chính cho eSIM online). GIT = Group Inclusive Tour (đi đoàn, thường guide lo SIM).*

### 3.6 Định vị MoMo cho SIM Du Lịch

> "MoMo là kênh mua SIM du lịch **nhanh - giá hợp lý - an tâm sử dụng**"

- **Mua nhanh - ít bước:** flow mua SIM đơn giản, chỉ 2 bước
- **Giá hợp lý:** đảm bảo không cao hơn thị trường quá 10-20K
- **An tâm sử dụng:** HDSD rõ ràng, hỗ trợ 24/7, đồng hành suốt chuyến đi

### 3.7 Định hướng tăng trưởng 2026

- **Product-led growth:** Cải tiến tập trung vào NHANH-TIỆN tạo khác biệt, tối đa CR
- **SKU & Promotion:** Đa dạng gói, giá cạnh tranh
- **Marketing & Communication:** Cross Border phục vụ toàn bộ hành trình du lịch, tập trung community/UGC/authentic review
- **Partnership:** Hợp tác chặt chẽ với Gohub
- **Source of Growth mới:** **Kênh Web** - dựa trên hành vi tìm kiếm Google của khách du lịch (đây là scope BRD này)

### 3.8 Market Research & Content Plan: Media Team eSIM (Khách vào Việt Nam)

*   **Market Research:**
    *   **Dung lượng thị trường:** Việt Nam đón 12.7 triệu lượt khách quốc tế năm 2024, dự kiến tăng lên 18 triệu lượt vào năm 2026. Tỷ lệ khách du lịch tự túc (FIT) chiếm hơn 70%, đây là đối tượng chính có nhu cầu cao về kết nối internet ngay khi hạ cánh.
    *   **Hành vi tìm kiếm:** Khách du lịch nước ngoài thường tìm kiếm các giải pháp eSIM trước chuyến bay để kích hoạt tiện lợi. Các từ khóa tiếng Anh chiếm ưu thế tuyệt đối: `vietnam esim` (9.900 SV), `best esim for vietnam` (1.900 SV), `vietnam travel sim` (1.000 SV).
    *   **Định vị sản phẩm:** Cung cấp eSIM data chất lượng cao chạy trên hạ tầng mạng của các nhà mạng lớn tại Việt Nam (Viettel/Vinaphone), hỗ trợ thanh toán quốc tế liền mạch (Credit Card, Apple Pay, Google Pay) và nhận mã kích hoạt QR tức thì.
*   **Content Plan (Chiến lược nội dung):**
    *   **Trang Destination:** `/esim-du-lich/viet-nam` (Thiết kế hoàn toàn bằng tiếng Anh phục vụ khách nước ngoài).
    *   **Nội dung chính:** Bảng so sánh các gói cước (Dung lượng, thời hạn, tốc độ 4G/5G), hướng dẫn kích hoạt chi tiết (How-to) cho iOS/Android và các câu hỏi thường gặp (FAQ) của khách du lịch khi đến Việt Nam.

---

## 4. User Insight & Hành vi mua

### 4.1 Bản chất hành vi mua SIM du lịch (FCB Model)

SIM du lịch thuộc nhóm **Habitual** trong FCB Grid:
- **Low involvement + Thinking** → Do → Learn → Feel
- Quyết định nhanh, ít cân nhắc phức tạp; mua vì tiện, thường sát ngày đi (~1 tuần trước bay)

**Implication cho web content:**
- Destination pages phải siêu lean (<800 từ body) - user không muốn đọc nhiều
- CTA phải rõ ràng và immediate - giảm friction tối đa
- Blog cluster phục vụ AWARENESS stage, không phải decision stage
- Giá là tiêu chí loại trừ nhanh - phải hiển thị giá rõ ràng, competitive

### 4.2 Kênh mua & Phân bổ User

- **85% user** đã mua ít nhất 1 kênh online; 15% chỉ mua offline
- Trong nhóm online: **74% mua eSIM**, 26% SIM vật lý
- Trong nhóm offline: 38% eSIM, **62% SIM vật lý**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm Online (85%)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm Offline (15%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Profile</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nữ, trẻ, độc thân/chưa có con, đi DL thường xuyên</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nam, lớn tuổi, có con, ít đi DL</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số SIM/lần mua</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mean 2.13 SIM/người</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mean 1.78 SIM/người</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dung lượng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mean 2.66 GB/ngày (1-3GB chủ yếu)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mean 3.66 GB/ngày (>5GB)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giá trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">213.586 VNĐ/SIM</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">284.381 VNĐ/SIM</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hành vi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhạy cảm giá, tối ưu gói phù hợp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sẵn sàng chi, cần HDSD rõ ràng</td>
    </tr>
  </tbody>
</table>

*Insight: Nhóm online mua trung bình 2+ SIM/lần (mua hộ). Web nên highlight combo/multi-buy. Dung lượng 1-3GB/ngày là sweet spot cho pricing display.*

### 4.3 Đánh giá kênh mua (User feedback)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Kênh</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm hài lòng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm không hài lòng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>MoMo</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giao dịch nhanh & tiện, dễ thao tác, tin tưởng brand</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giá chưa rẻ nhất, ít voucher, thiếu HDSD kích hoạt</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Sàn TMĐT</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đa dạng gói, giá tốt, nhiều review</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CSKH kém, khó liên hệ shop</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>App du lịch</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tiện lợi, nhận eSIM nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ít khuyến mãi</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Website SIM</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tư vấn hỗ trợ 24/7, dễ mua/sử dụng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
  </tbody>
</table>

**Leverage cho web:** MoMo mạnh ở "giao dịch nhanh + trust" nhưng yếu ở "giá & hướng dẫn". Web content phải address cả hai: (1) Hướng dẫn kích hoạt rõ ràng trong How-to section; (2) Nhấn mạnh "giá hợp lý" thay vì "giá rẻ nhất" - tránh cuộc chiến giá.

---

## 5. Customer Journey & JTBD

### 5.1 Main JTBD

> "Khi tôi chuẩn bị cho một chuyến đi quốc tế và cần đảm bảo có internet xuyên suốt hành trình, tôi muốn có một giải pháp kết nối phù hợp với điểm đến - mua nhanh, kích hoạt dễ và dùng ổn định từ lúc hạ cánh đến khi về nước, để tôi có thể tự tin tận hưởng chuyến đi mà không lo phí roaming, không panic vì mất sóng và không bị động trước những tình huống cần kết nối ở nước ngoài."

### 5.2 Bản Đồ Hành Trình Khách Hàng Chi Tiết (CJM 9 Bước)

Bản đồ chi tiết hành trình người dùng khi mua và sử dụng eSIM Du Lịch trên MoMo, chỉ rõ các điểm chạm, nhiệm vụ (Jobs) và giải pháp MoMo-specific để thu hẹp khoảng trống trải nghiệm:

#### Bước 1: Khám phá /AWARENESS
- **Hành động:** User chuẩn bị chuyến đi quốc tế (vé đã book hoặc đang plan ~7-14 ngày trước bay) bắt đầu nhận thức nhu cầu kết nối khi ra nước ngoài. Đây là moment "trip is now real" - intent cao nhưng đa kênh, MoMo phải cạnh tranh top-of-mind với Klook/Trip/Traveloka/ roaming nhà mạng.
- **Touchpoint MoMo:**
    App MoMo: Home banner, Mini app, Discovery feed, Push notification, Travel section.

    [GAP] Travel cluster (vé MB / khách sạn / bảo hiểm/QR Quốc tế) chưa cross-trigger mạnh sang SIM du lịch.
- **Customer Jobs-to-be-Done (JTBD):**
  - *Functional:* Hiểu landscape connectivity quốc tế (roaming nhà mạng, eSIM, SIM vật lý sân bay, Pocket Wi-Fi) và quy đổi nhanh về chi phí + tiện lợi cho lifestyle cụ thể.

    MoMo serve: △ TB
    Có Mini App nhưng không có education layer; user vẫn phải Google để hiểu eSIM vs SIM vật lý."
  - *Social:* Tự định vị là "người du lịch thông thái" - không bị động trước phí roaming; không "biến mất" với nhóm đi cùng và người thân ở nhà.

    MoMo serve: ✗ Yếu
    Brand MoMo = fintech, không phải "travel-savvy badge" so với Airalo/Klook trong mindshare gen Z
  - *Emotional:* Giảm pre-trip anxiety ("nếu không có internet thì sao?"); chuyển từ trạng thái lo lắng sang "có kế hoạch B".

    MoMo serve: ✗ Yếu
    Không có pre-trip checklist proactive; user vẫn lo lắng và phải tự research - MoMo không tham gia hành trình giảm anxiety.
- **MoMo Leverage (Lợi thế sẵn có):**
    ASSET ĐỘC NHẤT: Booking cluster (vé MB / khách sạn / bảo hiểm / đổi ngoại tệ) + giao dịch Visa quốc tế = trigger contextual.
    Direction: Du lịch quốc tế gom "trip kit"
- **Điểm đau & Cảm xúc người dùng:**
  - *Pain points:* Awareness gap top-of-mind: MoMo không là "first thought" cho SIM du lịch. Mindshare đang ở Airalo/Klook (gen Z tech-savvy) và roaming nhà mạng (segment trung niên). Không có cross-trigger từ booking cluster.

    Mức độ: CAO
  - *Trạng thái cảm xúc:* Băn khoăn (chưa biết phương án nào tối ưu) - Lo lắng nhẹ (sợ phí roaming) - Tò mò (eSIM là gì? an toàn không?).
- **Cơ hội & Solution Mapping (MoMo-specific):**
    - Travel Hub + "Trip Kit" bundle (vé máy bay, khách sạn và sim du lịch): cross-sell rule-based khi user vừa book quốc tế.
    - Pre-trip checklist notification 7-10 ngày trước bay (booking data làm trigger).
    - Education snippet ngắn ngay tại booking confirmation: "Bạn đã có internet cho chuyến đi chưa?".

---

#### Bước 2: Tìm quốc gia/CONSIDERATION
- **Hành động:** User search điểm đến cụ thể (vd "esim Nhật", "sim du lịch Hàn") hoặc browse list quốc gia phổ biến để xác nhận MoMo có giải pháp cho điểm đến của mình.   Mental model: nghĩ theo quốc gia trước, gói SIM sau.
- **Touchpoint MoMo:**
    TRONG MoMo: Global search home MoMo, Search bar in app, Mini App listing, Travel section.

    [GAP] Global search MoMo yếu, không suggest SKU best choice cho quốc gia đang tìm kiếm
- **Customer Jobs-to-be-Done (JTBD):**
  - *Functional:* Confirm MoMo có phục vụ sim cho điểm đến của tôi, narrow down danh sách option phù hợp mà không cần đoán nhà mạng/độ phủ.

    MoMo serve: △ TB
    Search MoMo hoạt động nhưng synonym/intent yếu; chưa có suggest SKU top of mind/peak/best choice nên user vẫn phải scan thủ công."
  - *Social:* Có "câu trả lời sẵn sàng" cho nhóm bạn khi được hỏi "đã lo SIM chưa?", "đi Nhật xài gì?".

    MoMo serve: ✗ Yếu
    User mất kiên nhẫn search → không có moment "tự hào đã lo xong/ bà hoàng săn deal" để khoe nhóm.
  - *Emotional:* Cảm giác "MoMo hiểu chuyến đi của mình" - chuyển từ ngờ vực sang tin tưởng. Đây là moment quyết định ở lại hay rời app.

    MoMo serve: ✗ Yếu
    Search không khớp intent → user nghi ngờ "MoMo có thực sự phục vụ travel không?"; mất trust ngay từ moment đầu.
- **MoMo Leverage (Lợi thế sẵn có):**
    Search history + booking cluster: nếu user đã book vé Nhật → suggest "esim Nhật" ngay khi mở mini-app.
    Country-first leverage được mental model du lịch của user
- **Điểm đau & Cảm xúc người dùng:**
  - *Pain points:* Search relevance không suggest SKU ("esim Nhật" chỉ suggest quốc gia, ko suggest SKU peak của quốc gia); thiếu hub quốc gia tổng hợp; user phải scan từng gói để đoán cover quốc gia mình đi.

    Mức độ: CAO
  - *Trạng thái cảm xúc:* Bối rối nếu search không trả kết quả -Mất kiên nhẫn ("sao tìm khó vậy?") -Có nguy cơ rời app rất cao.
- **Cơ hội & Solution Mapping (MoMo-specific):**
    - Country-first: "Bạn đi đâu? → list quốc gia phổ biến với badge giá rẻ nhất".
    - Search synonym tuning (esim, sim du lịch, internet quốc tế, 4G + tên QG).
    - Smart suggest SKU từ booking history: "Suggested for your trip to Tokyo".
    - Moni hỗ trợ full flow từ khi khách hàng chưa biết muốn đặt gì cho đến khi họ hoàn thành thanh toán trên MoMo

---

#### Bước 3: Tìm gói/CONSIDERATION
- **Hành động:** User compare các gói trong cùng quốc gia (dung lượng × ngày × giá × nhà mạng cover) trên MoMo và mở thêm tab so sánh với Klook/Trip/Traveloka/ roaming nhà mạng. Đây là khâu evaluation quan trọng nhất pre-purchase.
- **Touchpoint MoMo:**
    TRONG MoMo: PDP Mini App, Filter, Pricing display.

    [GAP] Không có review/rating, không có comparison view, không có brand partner badge.
- **Customer Jobs-to-be-Done (JTBD):**
  - *Functional:* Chọn được gói "đủ dùng - đáng giá" cho lifestyle: light (3-5GB), heavy (10GB+), work-from-anywhere (unlimited).

    MoMo Serve: △ TB
    Đủ thông tin cơ bản (giá, dung lượng, ngày); thiếu recommendation engine và comparison view nên quyết định khó.
  - *Social:* Tránh bị "hớ" khi share kinh nghiệm với bạn ("tao mua cái này, đắt mà ít data"); thể hiện sense về giá trị.

    MoMo serve: ✗ Yếu
    Không có review/rating nên user không có evidence để "khoe" lựa chọn của mình với bạn bè.
  - *Emotional:* Tự tin quyết định không bị hớ; loại bỏ cảm giác phải so sánh hàng giờ; giảm regret về sau.

    MoMo serve: ✗ Yếu
    Trust gap + decision paralysis → user phân vân, dễ procrastinate ("để mai tính") → silent abandonment.
- **MoMo Leverage (Lợi thế sẵn có):**
    - Brand lending: badge "Đối tác chính thức của MoMo" + brand partner logo
    - Reviews từ user MoMo cùng route (geographic + duration matched) -  social proof độc nhất.
- **Điểm đau & Cảm xúc người dùng:**
  - *Pain points:* Trust gap nghiêm trọng - Mini App không support review/rating/social proof natively. Decision paralysis bởi quá nhiều SKU giống nhau (5GB-7d vs 5GB-10d vs 7GB-7d). Không có comparison view, user phải screenshot tự note.

    Mức độ: RẤT CAO (conversion bottleneck quan trọng nhất pre-purchase)
  - *Trạng thái cảm xúc:* Phân vân - Nghi ngờ - Mệt mỏi (so sánh nhiều) - Có xu hướng "để mai tính" (procrastination = silent abandonment).
- **Cơ hội & Solution Mapping (MoMo-specific):**
    - Curated recommendation: "Most popular for [Country -Days]" với social proof ("152 user MoMo đã mua tuần này").
    - Comparison view 2-3 gói side-by-side.
    - Review close-the-loop từ chuyến đã đi.
    - Brand partner page "borrow trust" từ Airalo/Bytesim.
    - Lưu lại thông tin đã xem ➔ giúp user quay lại có thể tiếp tục hành trình mua data/sim trên MoMo dưới dạng shortcuts hoặc pop-up notification
    - Auto detect device suitable for e-sim or not (reference Klook)

---

#### Bước 4: Chọn gói/DECISION
- **Hành động:** User chọn gói cụ thể, click "Mua ngay" - đã commit về quyết định nhưng chưa hoàn tất giao dịch. Trạng thái commit cao nhưng vẫn dễ bị "pre-checkout abandonment" nếu rào cản xuất hiện.
- **Touchpoint MoMo:**
    TRONG MoMo: PDP "Mua ngay", Cart Mini App.

    [GAP] Quá nhiều gói tương tự, Không rõ sự khác biệt giữa các gói, Không có recommendation hoặc “best choice”; không có multi-buy SKU cho group travel.
- **Customer Jobs-to-be-Done (JTBD):**
  - *Functional:* Lock-in lựa chọn (gói + ngày kích hoạt) chính xác để tránh sai sót dẫn đến refund hoặc đổi gói hoặc sử dụng không đủ dẫn đến hết gói giữa chừng

    MoMo Serve: ✓ Tốt
    Buy flow nhanh, one-tap có sẵn; PDP đầy đủ thông tin để commit.
  - *Social:* Khẳng định vai trò "người lo logistics" trong nhóm; tự tin chốt cho cả đoàn nếu mua chung.

    MoMo serve: △ TB
    Có thể mua được nhưng không có flow mua cho nhóm (multi-buy SKU); mất cơ hội thể hiện vai trò.
  - *Emotional:* Cảm giác progress - tiến gần đến trạng thái "sẵn sàng đi". Endorphin moment nhỏ.

    MoMo serve: ✓ Tốt
    Tap "Mua ngay" tạo cảm giác progress rõ rệt; user thấy mình tiến gần đến "sẵn sàng đi".
- **MoMo Leverage (Lợi thế sẵn có):**
    - One-tap "Buy now" với saved payment.
    - Smart suggest ngày kích hoạt từ booking vé (vé bay 5/7 → default activation 5/7).
    - Multi-buy SKU cho group travel.
- **Điểm đau & Cảm xúc người dùng:**
  - *Pain points:* Date picker không liên kết booking (user phải tự nhớ ngày bay); không có upsell/multi-buy mạch lạc cho group travel.

    Mức độ: TRUNG BÌNH (ảnh hưởng AOV không CR chính)
  - *Trạng thái cảm xúc:* Thoả mãn nhẹ - Vẫn còn buyer's hesitation cuối ("liệu mình có chọn đúng?").
- **Cơ hội & Solution Mapping (MoMo-specific):**
    - Booking-based smart default ngày kích hoạt.
    - Multi-buy SKU ("Mua thêm SIM cho bạn cùng đi?").
    - Cross-sell relevant: bảo hiểm du lịch / đổi ngoại tệ - tận dụng "trip kit" mindset.

---

#### Bước 5: Nhập thông tin
- **Hành động:** User nhập thông tin nhận hàng: email (cho QR eSIM), SĐT, tên đầy đủ, địa chỉ giao (SIM vật lý). Đây là silent trở ngại killer -user complete mua nhưng có thể nhận sai/không nhận được.
- **Touchpoint MoMo:**
    TRONG MoMo: Form input Mini App (email, SĐT, tên, địa chỉ), reuse KYC level đã verified.

    [GAP NẶNG] Điền lại thông tin sau mỗi lần check out, Không lưu lại thông tin đã input của user và auto fill (ko serve được cho trường hợp mua hộ người khác)
- **Customer Jobs-to-be-Done (JTBD):**
  - *Functional:* - Cung cấp thông tin chính xác để chắc chắn nhận sản phẩm - đặc biệt email/SĐT phải đúng vì QR thường gửi qua các kênh này.
    - Tự động hóa, điền sẵn thông tin, giảm số bước trong quy trình checkout

    MoMo Serve: ✗ Yếu
    Không save và auto suggest từ previous profiles; risk nhập sai email cao = không nhận QR - đây là silent killer
  - *Social:* Không bị bẽ mặt vì sai email/SĐT dẫn đến không nhận được QR ngày bay - đặc biệt khi đi cùng người khác.

    MoMo serve: ✗ Yếu
    Form thủ công làm tăng probability sai sót khi đi nhóm → mất face với team đồng hành.
  - *Emotional:* Lo lắng nhẹ về data privacy (phải nhập email); cần feeling "MoMo đã có data này, sao bắt nhập lại".

    MoMo serve: ✗ Yếu
    User cảm thấy "không được tôn trọng thời gian" ("sao phải nhập lại?"); gãy positive flow tâm lý.
- **MoMo Leverage (Lợi thế sẵn có):**
    - Aggressive auto-fill từ MoMo profile (email, SĐT, tên, KYC level đã verified) → giảm form từ 3-5 trường còn 1 confirm.
    - KYC reuse: user đã verified trong MoMo → không cần fill-in lại.
- **Điểm đau & Cảm xúc người dùng:**
  - *Pain points:* Form dài, user phải nhập lại thông tin MoMo đã có; không có realtime validation; risk lớn: nhập sai email = không nhận QR = panic ở sân bay; không có "preview thông tin" pre-confirm.

    Mức độ: CAO (silent killer -user complete giao dịch nhưng nhận sai)
  - *Trạng thái cảm xúc:* Hơi bực ("sao phải nhập lại?") - Lo lắng về sai sót - Cảm thấy không được "tôn trọng thời gian".
- **Cơ hội & Solution Mapping (MoMo-specific):**
    - Aggressive auto-fill từ MoMo profile + KYC reuse (skip duplicate verification).
    - Inline validation realtime: "QR sẽ gửi đến: thuy***@gmail.com -xác nhận?".
    - "Save info for next trip" để future trips chỉ còn 1-tap.

---

#### Bước 6: Thanh toán / CONVERSION
- **Hành động:** User chọn nguồn thanh toán (Ví MoMo/NH liên kết/VTS), apply voucher, xác nhận. Đây là step MoMo có lợi thế cạnh tranh cốt lõi.
- **Touchpoint MoMo:**
    TRONG MoMo: Checkout, Payment selection, Voucher slot, Confirmation screen, Notification.
    → ĐÂY LÀ TOUCHPOINT MẠNH NHẤT của MoMo, hệ sinh thái thanh toán đầy đủ.
- **Customer Jobs-to-be-Done (JTBD):**
  - *Functional:* Hoàn tất thanh toán nhanh, an toàn, tận dụng tối đa voucher/cashback.

    MoMo Serve: ✓ Tốt
    Thanh toán 1 chạm, voucher, refund nhanh -best-in-class fintech UX, là điểm mạnh gốc của MoMo.
  - *Social:* Cảm thấy mình "đỉnh điên" - dùng ví thông minh, thanh toán không lóng ngóng (mạnh ở segment trẻ/gen Z).

    MoMo serve: ✓ Tốt
    Đặc biệt với gen Z, dùng MoMo = "modern payment badge"; thanh toán nhanh trước team = social win.
  - *Emotional:* An tâm về security; voucher = "win" tâm lý; hoàn tất = relief.

    MoMo serve: ✓ Tốt
    Security trust + voucher win = positive emotional moment lớn nhất toàn journey hiện tại.
- **MoMo Leverage (Lợi thế sẵn có):**
    ĐIỂM MẠNH: thanh toán 1 chạm, voucher MoMo Travel, cashback, refund nhanh khi lỗi.
    Trust as fintech: user đã tin MoMo về payment - đây là step lowest trở ngại.
- **Điểm đau & Cảm xúc người dùng:**
  - *Pain points:* Confirmation flow chưa rõ "sản phẩm sẽ về đâu" (email vs in-app); voucher Travel không proactive offered (user phải tự apply code).

    Mức độ: THẤP - TRUNG BÌNH (bước tốt nhất hiện nay, chỉ có gap nhỏ về UX confirmation)
  - *Trạng thái cảm xúc:* Smooth - Hài lòng - Phấn khích nếu voucher tốt (đây là khoảnh khắc tích cực nhất hiện tại).
- **Cơ hội & Solution Mapping (MoMo-specific):**
    - Confirmation rõ về điểm nhận hàng (in-app + email).
    - Auto-apply best voucher Travel (không bắt user nhập code).
    - Insurance / data-roaming cross-sell ở cuối checkout.

---

#### Bước 7: Kích hoạt/Cài đặt
- **Hành động:** Nhận QR code qua email + in-app, cài đặt eSIM lên device theo OS (iOS scan / Android có 2-3 luồng) hoặc lắp SIM vật lý. Thường thực hiện trước/khi vừa hạ cánh ở sân bay quốc tế.
- **Touchpoint MoMo:**
    TRONG MoMo: hiển thị mã QR in app hoặc email.

    [GAP RẤT NẶNG]:  5+ bước kích hoạt thủ công sau khi mua, Yêu cầu thiết bị thứ hai để quét QR → OS Settings để add eSIM ➔  quy trình nhiều bước, dễ mắc lỗi, dẫn đến tỉ lệ bỏ cuộc cao. Không có luồng kích hoạt in-app.
- **Customer Jobs-to-be-Done (JTBD):**
  - *Functional:* Kích hoạt SIM tự động, thành công đúng moment cần dùng - ngay sau hạ cánh hoặc trước đó để test.

    MoMo Serve: △ TB
    QR hợp lệ nhưng user phải rời app để cài đặt; hướng dẫn không adaptive theo OS → success rate giảm.
  - *Social:* Có thể giúp bạn đồng hành cùng setup eSIM -thể hiện thành thạo công nghệ; tránh để mọi người chờ ở sân bay.

    MoMo serve: ✗ Yếu
    User tự lúng túng setup → không thể đóng vai "tech-savvy" trong nhóm; có khi còn cản trở team.
  - *Emotional:* MOMENT ANXIETY CAO NHẤT trong toàn journey. Nếu lỗi ở sân bay nước ngoài → panic; thành công → relief lớn.

    MoMo serve: ✗ Yếu
    ANXIETY PEAK của journey nhưng không có pre-trip reminder, không có offline guide, không có in-app support → MoMo vắng mặt đúng lúc cần nhất.
- **MoMo Leverage (Lợi thế sẵn có):**
    - "My TravelSIM" in-app: lưu QR + hướng dẫn cài đặt adaptive theo iOS/Android, offline-ready.
    - Pre-trip reminder trước ngày bay.
    - In-app chat support call qua Wi-Fi sân bay -tránh tốn phí roaming.
- **Điểm đau & Cảm xúc người dùng:**
  - *Pain points:* GAP LỚN NHẤT TOÀN JOURNEY: user phải rời MoMo (vào Gmail) để lấy QR hoặc dowload mã QR tại in app MoMo. Sau đó phải dùng thiết bị thứ 2 để scan QR (đôi với iOS); hướng dẫn không adaptive theo OS, dạng text dài; không có offline guide; không có pre-trip reminder; không có test mode.

    Mức độ: RẤT CAO (single biggest pain point - kéo NPS xuống đáy)
  - *Trạng thái cảm xúc:* STRESS PEAK, Hồi hộp → Panic (nếu lỗi giữa sân bay) → Relief (nếu thành công). BIÊN ĐỘ CẢM XÚC CAO NHẤT JOURNEY
- **Cơ hội & Solution Mapping (MoMo-specific):**
    - "My Travel SIM" in-app: QR + auto cài adaptive iOS/Android
    - Pre-trip reminder 1  ngày trước đi
    - Test mode: kích hoạt thử trước khi bay.
    - Live chat in-app khi user đang ở sân bay (qua Wi-Fi).

---

#### Bước 8: Sử dụng ở nước ngoài
- **Hành động:** User dùng internet trong chuyến đi (GG Maps, social, video call về nhà), theo dõi data còn lại; nếu sắp hết phải top-up hoặc mua gói mới. Đây là moment trải nghiệm "sống còn" với satisfaction.
- **Touchpoint MoMo:**
    TRONG MoMo: (gần như không có touchpoint native).

    [GAP NẶNG]: Chưa hỗ trợ xem data usage, Hotline quốc tế (support).
    Không có usage dashboard, không có in-app top-up, không có in-app chat.
- **Customer Jobs-to-be-Done (JTBD):**
  - *Functional:* Có internet ổn định liên tục; biết chính xác data còn lại; nạp thêm dễ dàng khi sắp hết.

    MoMo Serve: ✗ Yếu
    Internet chạy nhưng tracking và top-up đều ngoài MoMo (qua app nhà cung cấp chính),  -MoMo không sở hữu trải nghiệm.
  - *Social:* Chia sẻ vị trí/ảnh/video real-time, gọi video về nhà - làm tròn vai " nhà du lịch sành sỏi".

    MoMo serve: △ TB
    Phụ thuộc gói có đủ data không; MoMo không liên quan đến social moment chia sẻ này.
  - *Emotional:* Tự do, kết nối, tận hưởng. Nhưng nếu hết data đột ngột → bực bội + hoảng loạn (offline ở nước ngoài).

    MoMo serve: △ TB
    Khi tốt thì tốt; khi hết data MoMo không nhận biết để hỗ trợ → cảm xúc tiêu cực không được chặn.
- **MoMo Leverage (Lợi thế sẵn có):**
    - Usage dashboard realtime trong pocket (cần API integration với partner).
    - Hệ thống chủ động cảnh báo khi còn 20%/10%; one-tap top-up bằng Ví MoMo.
    - In-app chat multi-language cho lỗi sóng.
- **Điểm đau & Cảm xúc người dùng:**
  - *Pain points:* Không có usage tracking native (user phải dùng app telco riêng); không có top-up flow trong MoMo; không có alert chủ động; không có in-app support khi lỗi giữa chuyến.

    Mức độ: CAO (loyalty leak quan trọng -đây là moment xây ấn tượng)
  - *Trạng thái cảm xúc:* Phấn khích/Tự do (khi tốt) → Bực bội/Hoảng loạn (nếu hết data bất ngờ).
- **Cơ hội & Solution Mapping (MoMo-specific):**
    - API integration với  partner để pull usage realtime.
    - Proactive notification 20%/10% + one-tap top-up.
    - In-app chat multi-language (EN + JP/KR/TH cho top markets).
    - Smart recommend gói top-up dựa trên pattern sử dụng còn lại của chuyến

---

#### Bước 9: Sau về nước
- **Hành động:** User về nước, eSIM hết hạn, có thể đánh giá / share trải nghiệm / chuẩn bị cho chuyến đi tiếp theo. Đây là khâu quyết định Lifetime value và word-of-mouth.
- **Touchpoint MoMo:**
    TRONG MoMo: (không proactive) -không có touchpoint trigger sau chuyến.
    [GAP]: Trip ended quietly; không có review prompt, không có CRM travel-specific, không có loyalty Travel tier.
- **Customer Jobs-to-be-Done (JTBD):**
  - *Functional:* Dọn dẹp eSIM cũ; lưu thông tin chuyến cho lần sau; quyết định có quay lại MoMo không.

    MoMo Serve: ✗ Yếu
    Không hướng dẫn xoá eSIM cũ; không lưu trip history để pre-fill cho lần sau.
  - *Social:* Recommend cho bạn bè, đăng review trên MXH, xây personal brand "người du lịch thông thái".

    MoMo serve: ✗ Yếu
    Không có referral mechanism; user có ý định share nhưng không được trigger và không có incentive.
  - *Emotional:* Hài lòng (hoặc thất vọng) với trải nghiệm tổng thể; xây thói quen quay lại MoMo cho chuyến đi kế tiếp.

    MoMo serve: ✗ Yếu
    Không có post-trip touchpoint → không xây dựng được thói quen "next trip = MoMo"; emotional bond không hình thành.
- **MoMo Leverage (Lợi thế sẵn có):**
    - Travel CRM: nhắc trước chuyến đi (dùng booking history mới).
    - Loyalty Travel tier (Explorer/Globetrotter/Nomad) tích điểm theo chi tiêu cluster Travel.
    - Referral cho bạn cùng đi: "Mời bạn cùng mua eSIM, cả hai có voucher".
- **Điểm đau & Cảm xúc người dùng:**
  - *Pain points:* Không có retention loop chuyên biệt cho travel; không leverage data chuyến đi để predict next trip; không có review collection để feed lại trust signals.

    Mức độ: CAO (LTV leak -mỗi user phải re-acquire cho từng chuyến đi)
  - *Trạng thái cảm xúc:* Trung tính nếu không trigger - Tích cực + loyalty nếu MoMo nhắc đúng thời điểm.
- **Cơ hội & Solution Mapping (MoMo-specific):**
    - Travel-specific CRM với trip prediction (dùng booking history + flight return signal).
    - Loyalty Travel tier (Explorer/Globetrotter/Nomad).
    - Referral cho bạn cùng đi (incentive 2 chiều).
    - Incentivized review để feed back trust signals cho user mới.
    - Trip recap trong app: "Bạn đã đi 3 nước với MoMo năm 2026" → tạo emotional bond

---

### 5.3 Pain Points chi tiết liên quan đến Web Scope

**GĐ 1 - Khám phá:** MoMo không phải "first thought" cho SIM du lịch. User phải tự Google để hiểu eSIM vs SIM vs roaming. → Blog "eSIM là gì", "Chuyển vùng vs eSIM" capture search intent.

**GĐ 2 - Tìm quốc gia:** User nghĩ theo quốc gia trước, gói SIM sau (mental model). Search Google bằng "[quốc gia] + sim/esim" rất phổ biến. → Destination pages với URL pattern `/esim-du-lich/{country}`.

**GĐ 3 - Tìm gói:** Trust gap (không có review/rating/social proof); Decision paralysis (quá nhiều SKU giống nhau). → Product Table với highlight "Bán chạy nhất", FAQ giải đáp concerns, AEO content.

### 5.4 Các Tính Năng JTBD Mới (Q3/2026)

Nhằm giải quyết các pain points của user khi chuẩn bị và trong lúc đi du lịch, dự án bổ sung các idea JTBD sau:
- **Smart Package Recommender:** Khách hàng lo ngại không biết chọn gói nào phù hợp trong hành trình. ➔ User nhập ngày đi/ngày về, hệ thống show gói data phù hợp nhất.
- **Check Device Compatibility:** Khách hàng muốn biết thiết bị hiện tại có hỗ trợ eSIM hay không trước khi thanh toán. ➔ Tích hợp tool check nhanh khả năng hỗ trợ eSIM của thiết bị.
- **In-App Travel Guide (Cẩm nang check-in & Cảnh báo Internet):** Khách hàng mua SIM để lướt mạng và sống ảo. ➔ Gợi ý các địa điểm check-in/sống ảo nổi tiếng, đồng thời cảnh báo (aware) người dùng về các ứng dụng bị chặn theo từng quốc gia (VD: chặn mạng xã hội).
- **MoMo Overseas Merchants (Bản đồ thanh toán):** MoMo cho phép thanh toán hơn 60 quốc gia qua Alipay. ➔ Hiển thị danh sách/bản đồ merchant tại vị trí hiện tại ở nước ngoài để user biết và sử dụng MoMo thanh toán.

---

## 6. Định Hướng Dự Án

### Dự án phục vụ điều gì?

Xây dựng cluster web eSIM Du Lịch thành kênh organic acquisition hiệu quả, convert traffic thành lượt mở app và mua hàng, contribute vào target web 4-10% Trans từ T7/2026. Đây là Source of Growth mới dựa trên hành vi tìm kiếm Google của khách du lịch - touchpoint web hiện MoMo chưa có.

### 6.1 Intent-based Filtering Framework (Trang Phạm Standard)
Phân loại rạch ròi luồng traffic dựa trên Search Intent để điều hướng vào đúng Product Lane/Content:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">User Segment</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đặc tính nhu cầu (Intent Filter)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Volume indicator</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FIT (tự đi, chuẩn bị trước)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua eSIM theo quốc gia cụ thể (Transact intent)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cluster destination pages</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Người so sánh giải pháp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">eSIM vs roaming vs SIM vật lý (Compare intent)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog comparison, hub FAQ</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Người mua hộ cho nhóm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần minh bạch giá, gói đa dạng (Research intent)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Product table + FAQ</td>
    </tr>
  </tbody>
</table>

### Trong scope

- Hub Page: `/esim-du-lich` - 1 trang, full component build
- Destination Pages: 10 trang theo URL `/esim-du-lich/{country-slug}`
- Blog Cluster: ~10 bài theo 3 tier (education, destination, comparison)
- Deep Link Integration: Web → MoMo App (iOS + Android), fallback App Store nếu chưa cài
- Schema Markup: FAQPage, HowTo, Product, AggregateOffer, BreadcrumbList trên tất cả trang
- Gohub API Integration: fetch giá và danh sách gói real-time (không hardcode)
- GA4 Event Tracking + UTM Framework chuẩn hóa

### Ngoài scope

- App-side UI/UX cho màn hình eSIM trong MoMo App
- Hệ thống inventory / fulfillment phía Gohub/Xplori/Mobi Media Team
- Social media / paid campaign cho eSIM cluster
- Đa ngôn ngữ (chỉ tiếng Việt + bilingual title/H2 khi cần)
- Trang so sánh competitor trực tiếp (cần approval riêng)
- Subdomain esim.momo.vn - dùng subdirectory `/esim-du-lich/` để giữ domain authority

---

## 7. Kiến Trúc & Scope Build

### 7.1 URL Architecture

**Hub:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">SV/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Content Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8.510+</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub Pillar - navigation + education + AEO</td>
    </tr>
  </tbody>
</table>

**Destination Pages (11 trang):**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">SV/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/trung-quoc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">7.850</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GFW disclaimer bắt buộc - không publish trước khi confirm với Gohub</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/viet-nam</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">12.800</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Media Team eSIM cho khách du lịch nước ngoài vào Việt Nam</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/thai-lan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3.930</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/nhat-ban</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.950</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/singapore</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.530</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/han-quoc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.160</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/chau-au</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.090</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1 gói cover toàn Schengen</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/my</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">900</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/uc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">790</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/dai-loan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">700</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/malaysia</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">610</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
  </tbody>
</table>

**Blog Cluster:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target keyword</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">SV</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/esim-la-gi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim du lịch là gì</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~200</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AEO priority, HowTo schema</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/esim-vs-chuyen-vung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">cách chuyển vùng quốc tế viettel/mobi</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.260</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Intercept competitor query</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/cach-mua-esim-tren-momo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">mua esim du lịch</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~200</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">How-to focus</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/dien-thoai-ho-tro-esim-2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">điện thoại hỗ trợ esim</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~50</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Update 6 tháng/lần</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/esim-trung-quoc-co-vao-google-khong</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim trung quốc</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~790</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Publish đồng thời với /trung-quoc</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/esim-thai-lan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim thailand</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">sim dtac thái lan</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~530</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/kinh-nghiem-esim-nhat-ban</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim nhật bản</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~340</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/esim-chau-au</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim du lịch châu âu</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~220</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/klook-esim-vs-momo-esim</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">klook esim</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần legal approval trước khi viết</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/blog/airalo-vs-gohub-vs-momo-esim</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim airalo</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần legal approval + verify giá đối thủ</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/esim-du-lich/llms.txt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AEO/GEO Standard</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuẩn hóa AI Indexing (Bắt buộc theo VP GPD)</td>
    </tr>
  </tbody>
</table>

**URL Rules:**
- Lowercase, hyphenated, không dấu tiếng Việt
- Không query params trong URL cấu trúc
- Tối đa 75 ký tự (không tính domain)
- **Lưu ý SEM:** SEM sitelinks hiện dùng `/esim-du-lich/khu-vuc/{country}` - cần align hoặc redirect trước khi launch tránh duplicate content.

### 7.2 Hub Page Anatomy

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Section</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thành phần</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Schema</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hero</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">H1 + 3 trust signals (QR · 150+ quốc gia · Hoàn tiền) + CTA Primary + CTA Secondary</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">WebPage, BreadcrumbList</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Answer Block</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"eSIM Du Lịch Là Gì?" - 60-80 từ + bảng so sánh 3 cột (eSIM/SIM vật lý/Roaming)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQPage</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination Grid</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">10 card: Flag + Quốc gia + Giá từ [X]đ + Link đến destination page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">How-to 4 bước</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mở app → Chọn gói → Thanh toán → Nhận QR/kích hoạt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">HowTo</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQ Block</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8 câu AEO priority (xem Appendix A)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQPage</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cross-sell</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Link Bảo hiểm du lịch + Blog cards</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
  </tbody>
</table>

### 7.3 Destination Page Anatomy

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Section</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thành phần</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Schema</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hero</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">H1 pattern: "eSIM [Quốc Gia] ([EN Name]) - [Gói phổ biến] / Từ [Giá]đ" + Breadcrumb</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Product, BreadcrumbList</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Product Table</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thời hạn · Dung lượng · Tốc độ · Giá (từ API) · CTA "Mua Ngay" - highlight "Bán chạy nhất"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AggregateOffer, PriceSpecification</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Country Context</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100-150 từ về đặc thù kết nối tại quốc gia</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQPage</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5-7 câu riêng theo quốc gia</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQPage</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Related Destinations</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3-4 trang liên quan về địa lý/trip pattern</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sticky CTA</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Floating button visible toàn scroll: "[Flag] Mua eSIM [Quốc Gia]"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
    </tr>
  </tbody>
</table>

**Bilingual title spec (địa chỉ bilingual queries):**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Destination</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Title tag</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">H2 bilingual trong body</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Việt Nam</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Vietnam eSIM (eSIM Việt Nam) - Best Travel Data Plans for Tourists"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Best Vietnam eSIM Plans for International Travelers"</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thái Lan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"eSIM Thái Lan (Thailand eSIM) - Gói Cước & Mua Ngay"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Thailand eSIM Plans for Vietnamese Travelers"</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung Quốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"eSIM Trung Quốc (China eSIM) - Kết Nối Không Giới Hạn"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"China eSIM - What You Need to Know"</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hàn Quốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"eSIM Hàn Quốc (Korea eSIM) - Mua Nhanh Kích Hoạt Ngay"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Korea eSIM - Compare Plans"</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Singapore</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"eSIM Singapore - Gói Data & Giá Tốt Nhất 2026"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Singapore eSIM Options Compared"</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Châu Âu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"eSIM Châu Âu (Europe eSIM) - 1 Gói Cho Cả Schengen"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Europe eSIM - Cover Multiple Countries"</td>
    </tr>
  </tbody>
</table>

### 7.4 Content Strategy

**Tone & Voice:** MoMo là người bạn hiểu công nghệ đang giúp chuẩn bị chuyến đi - không phải travel blogger, không phải sales rep. Thân thiện + có chuyên môn. Ngắn gọn nhưng đủ để quyết định (FCB Habitual).

**Rules bắt buộc:**
- Câu đầu mỗi đoạn = point chính (không warm-up)
- Claim phải có evidence (số liệu, so sánh giá cụ thể)
- Mỗi comparison section kết thúc bằng verdict 1 câu "Chọn X nếu... Chọn Y nếu..."
- Giá không hardcode nếu có thể thay đổi
- Tuyệt đối không address Great Firewall trong trang Trung Quốc nếu chưa confirm với Gohub

**Blog Tier:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tier</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Word count</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Schema</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Education - phải có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.000-2.000 từ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Article, FAQPage, HowTo</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Destination-specific</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">800-1.500 từ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Article, FAQPage</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier 3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Competitor comparison</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.200-2.000 từ + bảng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Article, FAQPage + Legal approval</td>
    </tr>
  </tbody>
</table>

### 7.4.1 Kế Hoạch Nội Dung Google SEM Ads (Mẫu Quảng Cáo)

Các tiêu đề (Headlines) và mô tả (Descriptions) được tối ưu hóa cho chiến dịch Google Search Ads, tương ứng với các landing pages trong Web Cluster:

#### Chiến dịch SEM: Travel Sim Overall
- **Final URL:** `eSIM du lịch quốc tế tiện lợi`
- **Mẫu Tiêu Đề (Headlines) tiêu biểu:**
  - Mua eSIM du lịch giá tốt
  - Sim du lịch dùng 4G/5G ổn định
  - Mua eSIM data siêu tốc
  - Mua eSIM data online dễ dàng
  - eSIM data cho chuyến du lịch
  - eSIM quốc tế giá rẻ, cực tiện
  - Mua SIM/eSIM du lịch ngay trên MoMo. Dễ dàng, nhanh chóng, dùng được ngay!
  - Ưu đãi lên đến 40% cho eSIM/SIM du lịch quốc tế trên MoMo. Nhập TRAVELSIM giảm thêm 50%.
  - Đã có eSIM du lịch quốc tế trên MoMo, sẵn sàng kết nối Data tốc độ cao hơn 105+ quốc gia.
- **Mẫu Mô Tả (Descriptions):**
  - SIM du lịch 200+ quốc gia
  - momo.vn/esim-du-lịch
  - Mua nhanh -rẻ, nhiều gói cước
  - Nhập VUIXUAN giảm đến 100K

#### Chiến dịch SEM: Sim Trung Quốc
- **Final URL:** `Sim du lịch nhận online`
- **Mẫu Tiêu Đề (Headlines) tiêu biểu:**
  - Sim du lịch Thái Lan dễ dùng
  - Mua eSIM data online dễ dàng
  - Kết nối mạng Trung dễ dàng
  - Mua eSIM data siêu tốc
  - Mua eSIM data quốc tế online
  - eSIM data cho chuyến du lịch
  - Mua sim Trung Quốc truy cập dễ dàng tại mọi khu vực, kết nối mạng tốc độ cao
  - SIM du lịch tại hơn 105 quốc gia - kết nối mạnh mẽ, tha hồ lướt mạng ở nước ngoài
  - Giảm đến 40% mọi eSIM/SIM du lịch nước ngoài trên MoMo. Nhập TRAVESIM giảm thêm 50%.
- **Mẫu Mô Tả (Descriptions):**

#### Chiến dịch SEM: Sim Thái Lan
- **Final URL:** `Sim 4G Thái Lan không giới hạn`
- **Mẫu Tiêu Đề (Headlines) tiêu biểu:**
  - Sim du lịch Thái Lan tiện lợi
  - Mua SIM truemove thái lan
  - Mua SIM DTAC thái lan
  - SIM 4G dùng ở Thái
  - SIM Thái giá rẻ
  - SIM Thái cho người nước ngoài
  - Mua sim Thái Lan 4G tốc độ cao - dùng ngay khi đến nơi, không cần xếp hàng nhận SIM
  - eSIM Thái Lan nhận ngay sau thanh toán - tiện lợi, ưu đãi siêu hời chỉ từ 60K
  - Ưu đãi tháng 04 chỉ có trên MoMo SIM Thái Lan chỉ từ 10K
- **Mẫu Mô Tả (Descriptions):**

#### Chiến dịch SEM: Sim Hàn Quốc
- **Final URL:** `eSIM du lịch là gì`
- **Mẫu Tiêu Đề (Headlines) tiêu biểu:**
  - SIM du lịch đa quốc gia
  - SIM du lịch kích hoạt ngay
  - Mua eSIM dùng ở Trung Quốc
  - Mua eSIM nước ngoài uy tín
  - Cách kích hoạt eSIM nhanh
  - Nên mua eSIM hay SIM vật lý
  - Mua sim du lịch Hàn Quốc nhận eSIM online ngay qua ứng dụng MoMo, không cần đợi ship.
  - SIM du lich không giới hạn data, ưu đãi 11% giảm thêm 50% khi nhập mã TRAVELSIM.
  - Mua SIM Hàn Quốc tốc độ 4G/5G ổn định, mua và kích hoạt online đơn giản qua ứng dụng MoMo
- **Mẫu Mô Tả (Descriptions):**

#### Chiến dịch SEM: Sim Việt Nam (Media Team)
- **Final URL:** `eSIM Việt Nam dùng liền`
- **Mẫu Tiêu Đề (Headlines) tiêu biểu:**
  - Sim du lịch Việt Nam giá tốt
  - Sim Việt cho khách nước ngoài
  - Mua SIM Việt cho khách du lịch
  - Mua SIM du lịch Việt Nam
  - Kết nối mạng tại Việt Nam
  - Sim data Việt Nam giá rẻ
  - SIM du lịch Việt Nam dành cho khách nước ngoài, dung lượng khủng. Nhập TRAVELSIM giảm 50%
  - SIM Mobi cho khách nước ngoài dùng tại Việt Nam. Mua và nhận eSIM kích hoạt ngay trên MoMo
  - Mua sim Việt Nam trên MoMo cho khách nước ngoài - nhận mã kích hoạt eSIM ngay
- **Mẫu Mô Tả (Descriptions):**

### 7.5 SEM-SEO Feedback Loop

SEM đang live cho SIM Du Lịch. Dữ liệu SEM bổ sung liên tục cho SEO:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Action</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Top performing SEM queries → SEO target</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Queries có CTR + conversion cao từ SEM ưu tiên trong SEO content</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEM landing page migration</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khi cluster live, redirect SEM destination URLs sang trang mới trong cluster</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEM negative keywords → SEO exclude</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Keywords SEM đã loại vì sai intent → loại khỏi SEO target</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEM ad copy testing → SEO title/meta</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Headlines SEM có CTR cao → test làm title tag/meta description</td>
    </tr>
  </tbody>
</table>

**Organic traffic baseline (thực tế):**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">T1/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">T3/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">T6/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">T9/2026 (target)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">25.724</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">31.992</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">27.391</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">42.907</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Paid traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">41.224</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">14.116</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">51.594</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">55.635</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CR MAU/Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4.98%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8.23%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6.64%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">7.85%</td>
    </tr>
  </tbody>
</table>

*Insight: Organic traffic dao động 25-43K/tháng nhưng không growth. Web cluster cần tạo organic growth engine ổn định, giảm phụ thuộc paid.*

### 7.6 Technical Standards (Gate bắt buộc)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Standard</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Requirement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LCP</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">< 2.5s (mobile 4G)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CLS</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">< 0.1 - lưu ý khi API load async</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">INP</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">< 200ms</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Schema validation</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0 error trên Google Rich Results Test trước publish</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Deep link</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Test pass iOS + Android, cả installed và not installed</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giá</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Fetch từ Gohub API (không hardcode) - fallback "Xem giá trong app" nếu API timeout</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobile CTA</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sticky button visible toàn scroll, không bị overlap bởi browser chrome (iOS Safari)</td>
    </tr>
  </tbody>
</table>

### 7.7 Product Roadmap Alignment

Web cluster là một phần trong chiến lược tăng trưởng tổng thể. Các in-app features quan trọng cần track để align content:

**Wave 1 (May-Aug 2026) - Quick Wins:**
- Auto-fill + Save profile + Price breakdown
- Smart Feature Tags (Hotspot/App/Speed)
- Persistent Entry Point + Smart Search
- In-app eSIM Activation (pain point lớn nhất - sẽ giảm từ 5+ bước xuống 1 chạm)
- Smart Package Comparison

**Wave 2 (Aug-Nov 2026) - Growth Lever:**
- Cross-trigger từ Booking (vé, khách sạn)
- Social Proof Layer (review, rating)
- Data Usage Dashboard
- Pre-trip Reminder System

**Wave 3 (Q3/2026) - MoSpark Migration & JTBD Expansion:**
- Migration nền tảng Admin Tool qua MoSpark.
- Kiểm tra toàn diện API, độ ổn định hệ thống (Load Testing) và luồng thanh toán trên Mobile/Desktop.
- Revamp lại toàn bộ UI/UX trang chủ eSIM và trang chi tiết quốc gia.
- Triển khai bộ tính năng JTBD: Smart Package Recommender, Device Compatibility Check, In-App Travel Guide (Check-in spots & Internet Awareness), Bản đồ thanh toán MoMo Overseas (Alipay).

**Web ↔ Product Dependencies:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Web Feature</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phụ thuộc Product Feature</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Highlight "Bán chạy nhất" trong Product Table</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Smart Package Comparison</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dùng cùng logic "most popular"</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog "Cách kích hoạt eSIM"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">In-app eSIM Activation</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cập nhật content khi tính năng live</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQ "Mua eSIM ở đâu uy tín"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social Proof Layer</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bổ sung data khi feature live</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cross-sell Block trên Hub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cross-trigger Booking</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Align danh sách cross-sell</td>
    </tr>
  </tbody>
</table>

---

### 7.8 Bảng Ánh Xạ Mã Lỗi Hệ Thống (Error Codes Mapping)

Bảng đối chiếu mã lỗi của đối tác Gohub, Xplori, Mobi Media Team và cách xử lý hiển thị ở phía Backend/Frontend để đưa ra các thông báo thân thiện với người dùng (localized error messages):

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">No.</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhà Cung Cấp</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lỗi Đối Tác</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thông Điệp Đối Tác</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mã Lỗi BE</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">BE Msg (User-facing)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">200 or 201</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Create order successfully</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thành công</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">400</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Invalid email Invalid quantity Invalid phone</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giao dịch thất bại</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">401</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Unauthorized</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giao dịch thất bại</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">404</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Resource not found</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giao dịch thất bại</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">405</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Method not allowed</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giao dịch thất bại</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">409</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Duplicate resource</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giao dịch thất bại</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">430</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">The request has already been handled, sending the same payload again is not allowed.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa map</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Server internal error</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giao dịch thất bại</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">9</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xplori</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">200</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thành công</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">10</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xplori</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><>200</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giao dịch thất bại</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">11</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thành công</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">12</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">13</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">14</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">15</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">16</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-60</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">17</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-61</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">18</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-62</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">19</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-63</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">20</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-65</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">21</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-69</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">22</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-70</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">23</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-71</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">24</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-72</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">25</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-73</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">26</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-74</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">27</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-75</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">28</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-76</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">29</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-77</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">30</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-78</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">31</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-79</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">32</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-81</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">33</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-82</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">34</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mobi media team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-999</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1006</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi hệ thống</td>
    </tr>
  </tbody>
</table>

## 8. Success Metrics

### Objective
Xây dựng cluster web eSIM Du Lịch thành kênh organic acquisition hiệu quả, contribute 4-10% Trans từ T7/2026.

### Key Results

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KR</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tracking</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">KR1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic Clicks - <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/esim-du-lich/*</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">+40% vs baseline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">KR2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Average Position - top 5 keywords</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Top 10</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">KR3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Overview Appearances</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">≥ 3 FAQ queries cited</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC / Manual audit</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">KR4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Click-to-App Rate (web → app, mobile)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">> 3%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 + Appsflyer</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">KR5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">New Users từ eSIM Funnel</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Grow MoM</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">KR6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQ Schema Eligibility</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0 error, ≥ 5 FAQ indexed/trang</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC Enhancements</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR7</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Trans contribution</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>4% T7 → 10% T9/2026</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>GA4 + Appsflyer</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR8</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web GMV</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>≥ 1.1 tỷ VNĐ (T9/2026)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>GA4 + Internal</strong></td>
    </tr>
  </tbody>
</table>

*Baseline measurement: đo toàn bộ metrics ngay sau khi publish Hub + 2 destination pages đầu tiên.*

### 8.1 Mandatory Tracking & AB Test Hypothesis (MoSpark Standard)
- **Hypothesis (Giả thuyết test):** Nếu đặt "Bảng so sánh chi phí eSIM MoMo vs Roaming" ở First Fold thay vì liệt kê gói data thông thường, W2A Conversion sẽ tăng ít nhất 40% vì đánh trúng tâm lý sợ Phát Sinh Cước Ngoài Ý Muốn (Fear-driven intent).
- **Tracking Event Schema:** Bắt buộc track `esim_compare_view`, `esim_cta_click`, `esim_deeplink_click` đổ về GA4 và Appsflyer để đo Funnel drop-off.

### 8.2 GA4 Events

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Event</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trigger</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Key Parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim_cta_click</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Click bất kỳ CTA trong cluster</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">page_type, country, cta_position</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim_deeplink_click</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Click deep link → app</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">country, source_page</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim_faq_expand</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Expand FAQ accordion</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">question_id, page_type</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim_product_view</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User scroll đến product table</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">country, packages_loaded</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">esim_blog_cta_click</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Click CTA trong blog</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">blog_slug, cta_position</td>
    </tr>
  </tbody>
</table>

---

## 9. Dependencies & Constraints

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dependency</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Blocker?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub API spec (endpoint, auth, response format)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần trước khi Dev build product table</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub xác nhận gói VPN cho trang Trung Quốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không publish <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/esim-du-lich/trung-quoc</code> trước khi có thông tin này</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Deep link scheme từ App team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CTA trên web không hoạt động nếu thiếu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CMS support schema injection</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xác nhận trước khi build để plan effort</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Legal approval cho Blog Tier 3 (comparison)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog comparison bị delay nếu không có sớm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">No</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEM URL migration alignment</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần quyết định URL pattern <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/khu-vuc/</code> vs <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/</code> trước khi build</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">DA Team - GA4 events setup</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phải có trước khi publish để có baseline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Yes</td>
    </tr>
  </tbody>
</table>

### 9.1 Go-to-Market: SPA Framework (Service Productization)
- **reSearch / Strategy:** Phân tích nhu cầu 50K SV/tháng (gồm cả Outbound & Media Team) và các đối thủ (Airalo, Klook, Gohub).
- **Pilot / Plan (T6/2026):**
  - Di chuyển toàn bộ Microsite eSIM hiện tại sang nền tảng MoSpark, cam kết **giữ nguyên cấu trúc URL hiện tại** (URL Structure giữ nguyên) để bảo toàn thứ hạng SEO và tránh ảnh hưởng dòng chảy traffic.
  - Rollout Hub page + 11 Destination pages (Thái, Trung, Nhật, Việt Nam...) trên MoSpark.
- **Action / Amplify (Q3/2026):**
  - Pitch BU Telco đổ budget SEM để scale traffic vào Hub, push W2A.
  - Hoàn tất Migration Admin Tool qua MoSpark. Đảm bảo API ổn định và luồng thanh toán mượt mà trên Mobile/Desktop.
  - Revamp UI/UX tổng thể cho trang eSIM và tung ra các tính năng JTBD bổ sung (Gợi ý gói cước, Check thiết bị, Cẩm nang check-in, Bản đồ thanh toán MoMo).

### 9.2 Operational Constraints
- Gói eSIM Trung Quốc: không publish trang nếu chưa xác nhận khả năng bypass GFW từ Gohub.
- Giá không được hardcode bất kỳ đâu - phải fetch từ API.
- Không tạo subdomain - dùng subdirectory `/esim-du-lich/` để giữ domain authority.
- Blog comparison competitor cần legal approval và verify giá đối thủ trước khi publish.

---

### 9.3 Kế Hoạch Media Outreach & Social Seeding

Chiến lược tiếp cận thông qua KOLs (TikTok) và seeding cộng đồng (Facebook Groups) để tối ưu hóa truyền miệng (Word-of-Mouth):

#### Danh sách KOLs Hợp Tác (TikTok):
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KOL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Kênh</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Follower</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai Trò & Content Angle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Jayni Travel</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TikTok</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">69.2K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sản xuất video ngắn trải nghiệm eSIM MoMo khi du lịch Thái Lan/Nhật Bản</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đoá Qua</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TikTok</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">166K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sản xuất video review so sánh eSIM MoMo vs SIM vật lý sân bay</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đi cùng Thy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TikTok</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">219K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review sự tiện lợi và tốc độ của eSIM MoMo ở Châu Âu/Đài Loan</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bửu Vi Vu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TikTok</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">258K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Video hướng dẫn cài đặt eSIM 1 phút trên app MoMo</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Myngccc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TikTok</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">20K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trải nghiệm mua eSIM du lịch siêu rẻ chỉ từ 10K trên MoMo</td>
    </tr>
  </tbody>
</table>

#### Cộng Đồng Du Lịch Nhắm Mục Tiêu (Facebook Groups Seeding):
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Group Facebook</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thành viên</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Link Nhóm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target Topic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ăn chơi Đài Loan 台灣 - 去哪吃啥?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">229K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><a href="https://www.facebook.com/groups/anchoidailoan/">Link</a></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review kết nối và sóng eSIM MoMo tại Đài Loan</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Du lịch tự do Đài Loan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">173K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><a href="https://www.facebook.com/groups/867394263291528/">Link</a></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chia sẻ kinh nghiệm mua SIM du lịch online giá rẻ</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">REVIEW DU LỊCH HONG KONG 🇭🇰</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">89K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><a href="https://www.facebook.com/groups/dulichhongkong/">Link</a></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hỏi đáp/chia sẻ sóng eSIM khi đi Hong Kong</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review Kinh Nghiệm Du Lịch Hàn Quốc ✅</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">417K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><a href="https://www.facebook.com/groups/reviewkinhnghiemdulichhanquoc/">Link</a></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Kinh nghiệm kích hoạt eSIM Hàn Quốc trên MoMo</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Du lịch Hàn tự túc: 100% Real Review</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">51.6K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><a href="https://www.facebook.com/groups/dulichhantutuc/">Link</a></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đánh giá chất lượng mạng eSIM Hàn Quốc của đối tác Gohub</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review du lịch có tâm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">306.6K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><a href="https://www.facebook.com/groups/728586307582132/">Link</a></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Seeding bài viết tổng hợp mua eSIM đi nhiều nước trên MoMo</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Du Lịch Thái Lan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">446.3K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><a href="https://www.facebook.com/groups/1439141509745393/">Link</a></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Voucher giảm giá eSIM Thái Lan chỉ từ 10K trên MoMo</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NHÀ TRUNG 🇨🇳 Cộng đồng du lịch Trung Quốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">130K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><a href="https://www.facebook.com/groups/nhatrung/">Link</a></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lưu ý sử dụng eSIM Trung Quốc bypass GFW để vào Google/Facebook</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CHÂU ÂU REVIEW TẤT TẦN TẬT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">102.2K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><a href="https://www.facebook.com/groups/633019552066467">Link</a></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chia sẻ kinh nghiệm mua eSIM Schengen 1 gói đi nhiều nước</td>
    </tr>
  </tbody>
</table>

## 10. Risk Assessment

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Rủi ro</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khả năng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Impact</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mitigation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gohub API không stable, timeout thường xuyên</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Medium</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">High</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Fallback "Xem giá trong app" + cache 15 phút</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gói eSIM TQ không bypass GFW - user disappointed</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">High</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">High</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Disclaimer rõ ràng bắt buộc, xác nhận với Gohub trước publish</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CMS không support schema injection</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Medium</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Medium</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dev inject qua code thay vì CMS plugin</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Deep link fail trên device cụ thể</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Low</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Medium</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Test matrix đủ device, có fallback URL</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Competitor publish trang tốt hơn trong thời gian build</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Medium</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Medium</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ưu tiên Hub + TQ + Thái Lan live trước</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEM/SEO URL conflict tạo duplicate content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Medium</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Medium</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quyết định URL pattern trước khi build, redirect cái còn lại</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web cluster launch delay → miss web contribution target T7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Medium</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">High</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Scope tối thiểu khả thi: Hub + 1 Destination + 1 Blog</td>
    </tr>
  </tbody>
</table>

---

## Appendix A: 8 AEO Priority Questions (Hub FAQ)

*Format: 40-60 từ per answer, câu đầu = answer trực tiếp.*

**Q1. eSIM du lịch là gì? Khác SIM vật lý thế nào?**
eSIM (embedded SIM) là SIM điện tử tích hợp sẵn trong điện thoại, kích hoạt qua QR code mà không cần cắm SIM vật lý. Khi đi du lịch, bạn mua eSIM online, nhận QR code, quét là có mạng ngay khi xuống máy bay - không cần xếp hàng mua SIM tại sân bay.

**Q2. Nên mua eSIM hay chuyển vùng quốc tế?**
eSIM du lịch rẻ hơn chuyển vùng từ 60-80% và không cần đăng ký hay hủy gói sau chuyến đi. Chuyển vùng quốc tế phù hợp nếu bạn chỉ đi 1-2 ngày và cần giữ số điện thoại Việt Nam để nhận OTP liên tục.

**Q3. Điện thoại nào hỗ trợ eSIM?**
iPhone XS (2018) trở lên, Samsung Galaxy S21 trở lên, Google Pixel 3 trở lên đều hỗ trợ eSIM. Đến 2025-2026, hầu hết flagship đều tương thích. Kiểm tra nhanh: vào Cài đặt → Thông tin điện thoại → xem có mục "eSIM" hay không.

**Q4. Mua eSIM bao lâu trước chuyến đi?**
Nên mua eSIM trước 1-3 ngày để có thời gian cài đặt và test kết nối. eSIM MoMo giao trong vài phút qua QR code - nhưng không nên để sát giờ bay vì cần kiểm tra thiết bị tương thích.

**Q5. eSIM Trung Quốc có dùng được Google, Facebook không?**
Trung Quốc chặn Google, Facebook, Instagram (Great Firewall). eSIM thông thường không bypass được trừ khi gói eSIM đó có tích hợp VPN. Trước khi mua, xác nhận với nhà cung cấp gói có support VPN hay không.

**Q6. 1 eSIM dùng được mấy máy?**
Mỗi eSIM du lịch chỉ dùng được cho 1 thiết bị. Sau khi quét QR code và cài vào máy, mã QR đó không thể dùng lại trên máy khác. Nếu đi cùng nhiều người, mỗi người cần mua 1 gói riêng.

**Q7. Mua eSIM du lịch ở đâu uy tín?**
Có thể mua qua MoMo, Airalo, Gohub, Klook. MoMo cung cấp eSIM qua đối tác Gohub, hỗ trợ 150+ quốc gia, thanh toán bằng ví MoMo, hoàn tiền nếu không kết nối được.

**Q8. Cách kích hoạt eSIM như thế nào?**
Sau khi mua: (1) Vào Cài đặt → Điện thoại → Thêm eSIM; (2) Chọn "Quét QR code"; (3) Quét mã nhận được sau khi mua; (4) Xác nhận cài đặt. Toàn bộ quá trình mất khoảng 2-3 phút. Nên kích hoạt khi còn ở Việt Nam để test trước.

---

## Appendix B: Destination FAQ Samples

### `/esim-du-lich/trung-quoc`
- eSIM Trung Quốc có bypass được Great Firewall (Google, Facebook) không?
- Gói nào trên MoMo có hỗ trợ VPN tại Trung Quốc?
- Tôi có thể dùng Google Maps ở TQ với eSIM này không?
- Nên tải VPN trước khi đi hay sau khi đến TQ?

### `/esim-du-lich/thai-lan`
- eSIM Thái Lan gói Unlimited có thực sự không giới hạn không?
- AIS hay True Move H - gói nào tốt hơn?
- eSIM có dùng được ở đảo Koh Samui, Koh Phangan không?
- Có thể chia sẻ hotspot (tethering) từ eSIM Thái Lan không?

### `/esim-du-lich/nhat-ban`
- eSIM Nhật Bản có nhắn tin SMS về Việt Nam được không?
- Coverage ở Hokkaido và vùng nông thôn có ổn không?
- eSIM có dùng được trên Shinkansen không?
- Gói nào phù hợp cho chuyến 10 ngày Tokyo-Osaka-Kyoto?

### `/esim-du-lich/chau-au`
- 1 gói eSIM Châu Âu dùng được bao nhiêu nước?
- Croatia, Albania, Montenegro có nằm trong vùng phủ sóng không?
- Tôi đi 3 tuần qua 6 nước Schengen - nên mua 1 gói hay mua từng nước?
- eSIM có hoạt động ở Anh (UK) sau Brexit không?

---

## Change Log
- **Tháng 5/2026 (v1.0):** Khởi tạo - keyword research, competitive analysis, URL architecture.
- **Tháng 5/2026 (v1.2):** Bổ sung Business Context & Market Intelligence, User Insight, Customer Journey & JTBD, SEM-SEO Feedback Loop, Product Roadmap Alignment.
- **Tháng 5/2026 (v1.3):** Chuẩn hóa tài liệu - loại bỏ liên kết nội bộ, tên nhân sự, code blocks kỹ thuật, FR codes, Sprint Plan, Definition of Done; chuẩn bị cho Head of BU / C-Level review.
- **Tháng 7/2026 (v1.4):** Cập nhật kế hoạch Q3/2026, bao gồm Migration Admin Tool qua MoSpark, Revamp UI/UX và bổ sung các use-case JTBD mới.
