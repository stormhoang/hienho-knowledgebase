# BRD: Soundbox

> - **Dự án:** Soundbox Web D2C - Website Order Loa Báo Chuyển Khoản MoMo
> - **Khối phụ trách:** PS (Payment Services) | SME Offline
> - **URL chính:** momo.vn/loa-thong-bao-chuyen-khoan
> - **Owner:** Web Platform
> - **Phê duyệt:** Web Product Lead (Hiến)
> - **Phiên bản:** 2.0 - Tháng 05/2026
> - **Trạng thái:** Draft - Chờ stakeholder review

---

> **Problem:** Chủ quán và tiểu thương đang tìm "loa thông báo chuyển khoản" mỗi ngày - nhưng không có trang momo.vn nào cho họ đặt hàng. 46.000 searches/tháng đang chảy về đối thủ hoặc bị bỏ ngỏ hoàn toàn.
> **KPI Owned:** Số Soundbox đặt hàng qua web (Web Order Volume) = f(Traffic × CR%)
> **Conversion Flow:** Search "loa thông báo chuyển khoản" → momo.vn/loa-thong-bao-chuyen-khoan → Product info + CTA → ipos.vn checkout → Purchase confirmed

---

## 1. Executive Summary

### Situation

Chủ quán, tiểu thương, người bán online đang nhận tiền chuyển khoản mà không có cách xác nhận tức thì - điện thoại trong túi, tay bận giao hàng, thông báo đến trễ, khách đã đi. Họ đang tìm giải pháp: search volume "loa thông báo chuyển khoản" tăng x10 trong 12 tháng, đạt ~46.000 lượt/tháng. MoMo có đúng sản phẩm họ cần - nhưng không có D2C web channel để capture intent đó.

### Complication

Kênh bán hàng hiện tại chỉ đi qua in-app MoMo, tạo ra ba rào cản nghiêm trọng:

1. Bỏ sót hoàn toàn nhóm Non-MoMo Users dù nhu cầu tìm kiếm đang ở ~30.000 lượt/quý.
2. Deep-link từ Ads/Affiliate bị đứt tracking khiến không đo được ROAS.
3. Việc xây dựng luồng E-commerce native trên momo.vn đòi hỏi nhiều nguồn lực, trong khi Cell Team cần một giải pháp MVP nhanh chóng để test đơn.

Song song, sự kiện thay đổi URL ngày 11/05/2025 đã phá vỡ ranking đã build từ 2024 - organic traffic sụt từ đỉnh ~6.900 sessions (T12/2024) xuống còn ~2.500 sessions (T06/2025), mất ~64% trong 6 tháng. Competitors mới (MB Bank, Techcombank, Vietcombank, Loa Ting Ting, Loa Thần Tài Mobifone) liên tục tăng market share.

### Resolution

Xây dựng kênh D2C qua website với hai luồng song song: (1) Tối ưu và khôi phục Landing Page momo.vn để phục vụ MoMo users, capture organic traffic và làm phễu điều hướng (push traffic); (2) Tận dụng trang `loathongbao.ipos.vn` do Cell Team tự build để làm đích đến cho nút "Mua ngay", qua đó test đơn và khép kín tracking phễu MVP trước khi build luồng native trên Web.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Hiện Trạng Web & Traffic

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Kênh</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trạng thái</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vấn đề</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MiniWeb MoMo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">momo.vn/loa-thong-bao-chuyen-khoan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang hoạt động, đang phục hồi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL đổi 11/5/2025 phá ranking; chưa có checkout</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">IPOS Web</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">loathongbao.ipos.vn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang hoạt động</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Do Cell Team tự build, dùng làm trang hứng traffic test đơn từ momo.vn</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">In-App MoMo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Luồng đặt hàng nội bộ app</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang hoạt động</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chỉ reach MoMo users; tracking bị gián đoạn</td>
    </tr>
  </tbody>
</table>

### 2.2 Traffic Historical Data

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giai đoạn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Organic Sessions</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Click to App</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">CR%</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T08/2024</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">184</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">77</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">41.8%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MiniWeb launch</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T10/2024</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4.800</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.414</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">50.3%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tăng tốt</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T12/2024</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6.900</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.666</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">24.1%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Peak</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T01/2025</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5.700</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">930</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">16.3%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sau Tết drop</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">T06/2025</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.500</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">362</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">14.5%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Điểm đáy sau URL change</td>
    </tr>
  </tbody>
</table>

**Nhận xét:** CR% sụt mạnh từ 41-50% (T8-T10/2024) xuống còn 14-16% (H1/2025). Vấn đề không chỉ là traffic mà là chất lượng landing và intent matching.

### 2.3 Market Landscape

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giá trị</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Total search volume thị trường</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~46.000 lượt/tháng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tăng trưởng thị trường (12 tháng)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">x10 lần so với 06/2024</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số lượng từ khoá tracked</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">627 từ khoá</td>
    </tr>
  </tbody>
</table>

**Top competitor clusters:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Volume ước tính</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loa Thông Báo Chuyển Khoản (generic)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~8.000+/tháng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loa MoMo (branded)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~2.500+/tháng</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loa Ngân Hàng (Vietcombank, MB, Techcombank, BIDV, Vietinbank)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~8.000+/tháng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loa Ting Ting / Thần Tài Mobifone / Tingee</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~2.500+/tháng</td>
    </tr>
  </tbody>
</table>

**Nhận định:** Nhóm loa ngân hàng là threat lớn nhất - các ngân hàng có authority domain cực cao và tặng loa miễn phí khi mở tài khoản. MoMo không thể thắng ở nhóm brand intent ngân hàng, nhưng có thể dominate nhóm generic intent và how-to intent.

---

## 3. Định Hướng Dự Án

### 3.1 Product Job Cốt Lõi

**Tiểu thương tìm loa báo chuyển khoản - tìm thấy momo.vn - xem giá, tính năng, đặt hàng ngay - nhận loa, xác nhận giao dịch tức thì, bán hàng tự tin hơn.**

Web closes the D2C loop: từ search intent đến confirmed purchase mà không cần vào app, không cần gặp sales.

4 outcome phát sinh từ loop này:

**① SME Acquisition:** Capture Non-MoMo Users đang search generic intent - nhóm không thể reach qua in-app funnel.

**② Tracking Completeness:** ipos.vn checkout domain cho phép đo ROAS đầy đủ - mở khoá Performance Marketing.

**③ Ranking Recovery:** Khôi phục link equity bị mất do sự kiện URL 11/5/2025, rebuild organic foundation cho toàn cluster.

**④ Competitive Moat:** Chiếm generic intent "loa thông báo chuyển khoản" + how-to cluster trước khi ngân hàng dominate hoàn toàn.

### 3.2 Dự Án Này KHÔNG Phải

- Không build mobile app hay cải tiến in-app ordering flow
- Không phải dự án brand awareness (KPI đo conversion, không đo impressions)
- Không cover toàn bộ danh mục thiết bị phần cứng MoMo - chỉ focus Soundbox
- Chưa triển khai luồng E-commerce Native trực tiếp trên momo.vn trong giai đoạn MVP (mặc dù đã có license TMĐT) nhằm tiết kiệm nguồn lực.

---

## 4. JTBD Analysis

### Job #1: Tìm Giải Pháp Xác Nhận Thanh Toán Tức Thì

> "Tôi đang bán hàng, khách chuyển khoản xong tôi không nghe được có tiền vào không. Cần thiết bị đọc to để tôi biết ngay."

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xác nhận giao dịch nhận tiền tức thì, hands-free, không phụ thuộc điện thoại</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tự tin khi bán hàng; tránh bị khách "giả chuyển khoản" lừa</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuyên nghiệp hơn trong mắt khách hàng - quầy có thiết bị bài bản, không cầm điện thoại suốt</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mất tiền vì không nghe thông báo; hoặc thấy shop khác dùng</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"loa thông báo chuyển khoản", "loa momo" → momo.vn/loa-thong-bao-chuyen-khoan → "Đặt hàng ngay" → ipos.vn checkout (Non-MoMo) hoặc App MoMo (MoMo user) → Purchase confirmed</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** Landing Page chính + Product Page D2C với đầy đủ specs, giá, CTA đặt hàng.

---

### Job #2: So Sánh Và Chọn Giữa Các Thương Hiệu

> "Tôi thấy có nhiều loại loa, không biết loa nào tốt hơn - nhất là loa ngân hàng tặng miễn phí vs loa MoMo phải mua."

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiểu sự khác biệt; đưa ra quyết định mua đúng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không muốn chọn sai - mất tiền hoặc trải nghiệm kém</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bạn bè hay đồng nghiệp cùng ngành hỏi "loa nào ngon hơn" - cần câu trả lời tự tin từ so sánh thực tế, không phải phỏng đoán</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bị overwhelmed bởi quá nhiều lựa chọn; thấy quảng cáo từ nhiều nguồn</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"loa momo vs ting ting", "so sánh loa báo chuyển khoản", "loa ngân hàng nào tốt" → /blog/so-sanh-loa-momo-vs-ting-ting → CTA "Đặt loa MoMo" → ipos.vn checkout</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** Blog so sánh trung lập (MoMo vs Ting Ting, MoMo vs Loa Thần Tài Mobifone); landing page theo competitor intent.

---

### Job #3: Cài Đặt, Kết Nối & Troubleshoot

> "Tôi đã mua rồi nhưng setup không được - không biết connect wifi thế nào, loa không đọc."

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sản phẩm hoạt động đúng như mong đợi</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không muốn cảm thấy "mua nhầm"; muốn tự xử lý được</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không muốn gọi hotline rồi bị thấy là "không biết dùng đồ công nghệ" trước mặt nhân viên hay hàng xóm</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sản phẩm không work sau khi mua; hoặc đổi điện thoại/số tài khoản</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"cách cài đặt loa momo", "kết nối wifi loa momo không được", "reset loa momo" → /blog/cai-dat-loa-momo → Hướng dẫn từng bước + CTA upsell cho user chưa có loa</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** Blog how-to + FAQ page trên miniWeb; hỗ trợ retention user đang dùng.

---

### Job #4: Xác Định Giá & Điều Kiện Sở Hữu

> "Loa MoMo có miễn phí không? Hay phải mua? Mua ở đâu? Điều kiện là gì?"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Biết chính xác chi phí sở hữu trước khi ra quyết định</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lo ngại chi phí ẩn; muốn minh bạch</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấy shop cạnh bên có loa mà mình chưa có - không muốn thua kém về sự chuyên nghiệp trong mắt khách</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấy giá quảng cáo khác nhau ở nhiều nơi; chưa rõ điều kiện đăng ký</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"loa momo giá bao nhiêu", "mua loa momo ở đâu", "điều kiện đăng ký loa momo" → momo.vn/loa-thong-bao-chuyen-khoan#pricing → Pricing section rõ ràng → "Đặt hàng ngay" → ipos.vn</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** Pricing section rõ ràng trên LP; FAQ về phí, điều kiện đăng ký; CTA "Đặt hàng ngay" với price visible.

---

### Job #5: Khám Phá Tính Năng & Ứng Dụng Thực Tế

> "Tôi mới nghe đến soundbox - không rõ nó là cái gì, dùng cho trường hợp nào."

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hiểu product fit trước khi consider mua</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không muốn mua thứ "không cần thiết"; cần thấy use case cụ thể giống mình</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấy hàng xóm hay người bán cùng chợ dùng - muốn hiểu xem mình có cần không trước khi hỏi họ</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấy quảng cáo hoặc nghe người khác nhắc đến</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"soundbox là gì", "loa thông báo chuyển khoản là gì", "cách dùng loa báo tiền" → Educational blog/FAQ → CTA xem sản phẩm → momo.vn LP → ipos.vn đặt hàng</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** Educational blog + FAQ section trên LP + video/visual minh họa use case thực tế.

---

## 5. Kiến Trúc Web

### 5.1 Kiến Trúc 2 Domain (MVP Pilot)

```text
momo.vn/loa-thong-bao-chuyen-khoan  [SEO & Traffic Hub]
├── Main Landing Page (revamp - optimize conversion)
├── Nút "Mua Ngay" (CTA)
└── Redirect ➔ Trang nhập thông tin mua hàng trên loathongbao.ipos.vn

loathongbao.ipos.vn                  [D2C Checkout Pilot]
├── Form nhập thông tin mua hàng (Cell Team build)
└── Ghi nhận đơn & test tỷ lệ chuyển đổi
```

**Logic phân tách MVP:** momo.vn (đã có license TMĐT) đóng vai trò là SEO hub, capture organic và push traffic. Để test nhu cầu nhanh, nút "Mua ngay" sẽ link sang `loathongbao.ipos.vn` do Cell Team vận hành. Khi volumn đủ lớn, sẽ tiến hành build luồng E-commerce Native trực tiếp trên momo.vn.

### 5.2 Workstreams

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">WST</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng mục</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">WST1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MiniWeb MoMo - Tối ưu & Khôi phục</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Revamp LP hiện tại; bổ sung long content; optimize onpage; cải thiện CR từ organic traffic</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">WST2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">IPOS Web - D2C Channel cho Non-MoMo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Build/optimize web bán hàng trên domain có phép TMĐT, tích hợp checkout đầy đủ</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">WST3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tracking Integration</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khép kín tracking toàn bộ phễu: Click → LP → Checkout → Purchase. Phục vụ SEO analytics và Ads optimization</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">WST4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO/Content Scale</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phục hồi ranking + mở rộng content cluster (blog, comparison, how-to) để capture mid-funnel và top-funnel</td>
    </tr>
  </tbody>
</table>

### 5.3 Content Structure

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Content Type</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Intent</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Volume</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Channel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Main LP Revamp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transaction</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~8.000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">momo.vn</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Comparison Pages (8 URLs)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Comparison/Buy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~15.000/tháng aggregate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">momo.vn</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">How-to / Setup Guides (5 URLs)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Do/Technical</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~2.500/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">momo.vn/blog</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pricing & FAQ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Know/Buy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~2.000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">momo.vn + ipos</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Educational Blog</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Know</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~1.500/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">momo.vn/blog</td>
    </tr>
  </tbody>
</table>

---

## 6. Success Metrics

### 6.1 North Star Metric

**Số lượng Soundbox đặt hàng qua web** = f(Web Traffic × CR%)

**Funnel:**
```
Search → momo.vn LP → CTA click → ipos.vn checkout → Purchase confirmed
```

### 6.2 KPI Framework

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Baseline</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target (EOY 2026)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Monthly organic sessions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~2.500/tháng (T06/2025)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">40.000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC + GA4</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Market share (traffic/total volume)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dưới 10% ước tính</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">20% market share</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC vs Keyword tool</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CR (sessions → đặt hàng thành công)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0% (chưa có D2C checkout)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 + IPOS analytics</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số đơn hàng/tháng qua web</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~1.200 đơn/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">IPOS order system</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Keywords ranking Top 5 (volume 500+/tháng)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang đo baseline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">10 keywords</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC + SEO tool</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Keywords ranking Top 10 (volume 200+/tháng)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang đo baseline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">25 keywords</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC + SEO tool</td>
    </tr>
  </tbody>
</table>

---

## 7. Dependencies & Constraints

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quyết định Build E-commerce</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mặc dù momo.vn đã có License TMĐT, việc build Native E-commerce cần nhiều thời gian. Solution: Dùng loathongbao.ipos.vn làm trang test luồng (MVP)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Workaround</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell Team (IPOS)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vận hành và tối ưu form nhập thông tin mua hàng trên loathongbao.ipos.vn để hứng traffic từ momo.vn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL Canonicalization sau sự kiện 11/5/2025</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần confirm 301 redirect từ URL cũ về URL mới đã được setup đúng chưa. Nếu sai → link equity bị mất</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hard</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Onelink / Appsflyer tracking setup</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Setup tracking parameter đầy đủ cho toàn bộ phễu từ web → app (MoMo users) và web → checkout (Non-MoMo users)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hard</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BU Soundbox - Content Brief</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần BU cung cấp: danh sách tính năng sản phẩm, lỗi thường gặp + cách xử lý, pricing chính thức, điều kiện đặt hàng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Legal review comparison pages</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8 comparison pages mention competitor brands cần Legal approve trước khi publish</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
    </tr>
  </tbody>
</table>

**Constraints:**
- Checkout tạm thời đi qua `loathongbao.ipos.vn` để test tỷ lệ chuyển đổi, trước khi đưa ra quyết định đầu tư nguồn lực build luồng E-commerce Native trên momo.vn.
- Nội dung mention competitor brand (ngân hàng, Ting Ting...) bắt buộc qua legal review
- URL 301 redirect phải được verify trước khi làm bất kỳ SEO optimization nào (để không mất link equity thêm)

---

## Change Log

- **Tháng 5/2026 (v2.0):** Apply CEO BRD Standard: Thêm Problem Statement block, rewrite Situation theo user-centric, thêm Product Job Cốt Lõi (Section 3.1), thêm Search → App + Social dimension vào tất cả JTBD. Xóa Risk Assessment (Section 8). Xóa Appendix A Keyword Clusters.
- **Tháng 5/2026 (v1.0):** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.
