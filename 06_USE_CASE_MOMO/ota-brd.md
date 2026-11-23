# BRD: Destination Promotion Hub (MoMo Travel)

> - **Dự án:** Destination Promotion Hub (DPH) - MoMo Travel (Vé máy bay quốc tế)
> - **URL chính:** momo.vn/ve-may-bay/uu-dai-diem-den
> - **Khối phụ trách:** OTA (Online Travel Agent) - MDS
> - **Phiên bản:** 1.1 · Tháng 7/2026
> - **Trạng thái:** Draft / Review (Updated to align with Destination Hub PRD)
> - **Business Model:** OTA Marketplace (Flight, Hotel, Experience, Visa, Insurance)

---

> **Problem:** Khách hàng có nhu cầu đi du lịch quốc tế phải tự tìm kiếm rời rạc nhiều dịch vụ, không có nhận biết rõ ràng việc MoMo Travel bán vé quốc tế, và thiếu một nơi tổng hợp ưu đãi liên quan đến điểm đến cụ thể.
>
> **KPI Owned:** Conversion Rate (booking/visit DPH vs trang tìm kiếm thường), Average Order Value (% đơn hàng cross-sell khởi tạo từ DPH), MAU Travel (% user vào Travel xem ít nhất 1 trang DPH/tháng).
>
> **Conversion Flow:** Banner/Push/Search results  ➔  Landing Page DPH (theo điểm đến cụ thể)  ➔  Chọn chặng bay/Khách sạn/Trải nghiệm giá tốt  ➔  Prefill thông tin tìm kiếm  ➔  Thanh toán trọn gói trên MoMo.

---

## 1. Executive Summary

### 1.1 Elegant Problem Framing
- **Vấn đề cốt lõi:** Người dùng du lịch quốc tế (outbound) thường phải thực hiện hành trình tìm kiếm và đặt dịch vụ rất rời rạc. Việc MoMo Travel phân phối vé quốc tế chưa có nhận diện tốt trong tâm trí khách hàng. Các ưu đãi lớn từ đối tác (ngân hàng, hãng bay, Tổng cục du lịch) chạy lẻ tẻ theo từng chiến dịch, không được tái sử dụng tối ưu.
- **Giải pháp (The "What"):** Xây dựng **Destination Promotion Hub (DPH)** làm Landing Page chuyên biệt theo điểm đến (Đài Loan, Nhật Bản, Thái Lan...). Nơi đây hợp nhất toàn bộ thông tin hành trình và ưu đãi đa bên (Hãng bay + Bank + Tổng cục du lịch) và hỗ trợ bán chéo trọn gói (Vé bay, Khách sạn, Tour trải nghiệm, Visa, Bảo hiểm).

### 1.2 Situation & Complication
- Trang chủ Vé máy bay hiện hiển thị ưu đãi dạng banner/carousel rời rạc, chưa có cấu trúc theo chặng/điểm đến cụ thể.
- Nhận biết của người dùng về việc MoMo Travel bán vé máy bay quốc tế còn hạn chế.
- Các đối thủ trực tiếp như **Trip.com** (trang Deals/Destination) và **Traveloka** (Destination promotion) đều đã tổ chức trang khuyến mãi theo trục điểm đến hoặc chủ đề du lịch rất tốt, đáp ứng trực tiếp nhu cầu mua sắm trọn gói.

### 1.3 Resolution
- Xây dựng template DPH chuẩn hóa, áp dụng cho các điểm đến quốc tế trọng điểm ở giai đoạn 1 (Top 8-10 điểm đến theo doanh thu).
- Sử dụng cấu trúc module hóa qua CMS để đội ngũ Marketing/Partnership tự vận hành thay đổi nội dung, banner, coupon mà không cần can thiệp kỹ thuật sâu.
- Tạo lợi thế riêng biệt cho MoMo bằng cách hợp nhất ưu đãi đa đối tác (lợi thế hệ sinh thái thanh toán ví điện tử).

---

## 2. Bối Cảnh Thị Trường & Insight Đối Thủ

### 2.1 Hiện trạng MoMo Travel
- Giao diện chủ yếu hiển thị coupon rời rạc, khách hàng tìm ưu đãi theo điểm đến phải nhập thủ công.
- Marketing chạy các chiến dịch ngân hàng hay TCDL độc lập, thiếu một "hub" cố định để duy trì lâu dài.

### 2.2 Insight từ Trip.com & Traveloka

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tiêu chí</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trip.com</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Traveloka</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoMo Travel DPH (Đề xuất)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cấu trúc trang</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing page theo chủ đề lớn (vd: "Go China")</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing page theo 1 điểm đến cụ thể (vd: Taiwan)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing page theo điểm đến cụ thể kết hợp Hub tổng hợp</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nội dung chính</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vé bay + Khách sạn + Trải nghiệm + Nội dung truyền cảm hứng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mức giảm giá nổi bật, khung thời gian áp dụng, CTA</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vé bay giá tốt + Khách sạn + Trải nghiệm + Ưu đãi đa đối tác</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cách dùng dữ liệu</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trộn editorial và dữ liệu giá thực tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tập trung hoàn toàn vào ưu đãi/giá rẻ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giá thực tế real-time kết hợp block coupon động từ CMS</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Điểm mạnh</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gắn use-case theo hành trình, tăng dwell-time</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thông điệp rõ ràng, dễ tạo cảm giác cấp bách (urgency)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Lợi thế thanh toán ví điện tử & đối tác tài chính đa dạng</strong></td>
    </tr>
  </tbody>
</table>

---

## 3. Mục Tiêu & KPI Đo Lường

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục tiêu</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chỉ số đo (KPI)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phương pháp đo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tăng nhận diện (Awareness) vé quốc tế</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% user vào app Travel có xem ít nhất 1 trang DPH/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tracking pageview DPH / MAU Travel</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tăng tỷ lệ chuyển đổi chặng quốc tế</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tỷ lệ chuyển đổi (booking/visit) trên trang DPH so với trang tìm kiếm thường</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">A/B Testing chênh lệch CVR</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tăng giá trị đơn hàng trung bình (AOV)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% đơn hàng có cross-sell (khách sạn/trải nghiệm/bảo hiểm)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gắn UTM/source_id theo từng entry point trên DPH</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hiệu quả khai thác đối tác</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số lượng & doanh thu campaign bank/hãng bay/TCDL gắn trên DPH</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Báo cáo theo banner_id / partner_id</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tối ưu vận hành nội dung</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thời gian dựng 1 trang điểm đến mới (Target: ≤ X ngày)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Theo dõi quy trình cấu hình trên CMS nội bộ</td>
    </tr>
  </tbody>
</table>

---

## 4. Phạm Vi & Đối Tượng Người Dùng

### 4.1 Trong phạm vi (In-scope)
- Xây dựng hệ thống template DPH cho 8-10 điểm đến quốc tế trọng điểm.
- Thiết lập cơ chế tổng hợp ưu đãi đa nguồn: Vé máy bay, khách sạn, tour, visa, bảo hiểm, mã giảm giá bank/hãng bay.
- Phát triển hệ thống quản lý nội dung (CMS) cho phép Marketing/Partnership cấu hình độc lập.
- Thiết lập các entry point chuyển tiếp từ màn hình chính của Vé máy bay và kết quả tìm kiếm.

### 4.2 Ngoài phạm vi (Out-of-scope giai đoạn 1)
- Cá nhân hóa gợi ý điểm đến dựa trên hành vi chi tiết (dự kiến đưa vào Phase 2).
- Áp dụng DPH cho các điểm đến nội địa (giữ nguyên luồng Hot deals nội địa hiện tại).
- Tích hợp đặt chỗ thời gian thực nếu đối tác dịch vụ bên thứ ba chưa sẵn sàng API (cho phép dùng link-out hoặc trang thông tin tĩnh).

---

## 5. Đề Xuất Giải Pháp Kỹ Thuật & UX

### 5.1 Nguyên tắc thiết kế
1. **MECE theo điểm đến:** Mỗi trang đại diện cho 1 quốc gia/điểm đến duy nhất, tránh trùng lặp nội dung.
2. **Một điểm chạm - Đa nguồn ưu đãi:** Chuẩn hóa các ưu đãi từ nhiều nguồn lực khác nhau vào cùng một layout.
3. **Action-first (Ưu tiên hành động):** Giá vé tốt nhất và Search Bar luôn nằm ở phần nửa trên màn hình (above the fold).
4. **Vận hành phi kỹ thuật:** Marketing tự quản lý và cấu hình thông qua CMS module hóa.
5. **Nhất quán thiết kế:** Sử dụng đúng bảng màu chủ đạo (magenta/pink) và font chữ hiện tại của MoMo, không làm lệch nhận diện thương hiệu.

### 5.2 Cấu trúc thông tin (Information Architecture)
Trang DPH sẽ hiển thị các block module hóa theo thứ tự từ trên xuống dưới:

1. **Hero Banner:** Ảnh điểm đến, thông điệp ưu đãi chính, thời hạn áp dụng.
2. **Thanh tìm vé nhanh (Prefill):** Form tìm kiếm rút gọn điền sẵn điểm đến chặng bay.
3. **Vé máy bay giá rẻ (Real-time Fare):** Danh sách 4-6 mức giá rẻ nhất theo ngày kết nối trực tiếp với Fare API.
4. **Ưu đãi từ hãng bay:** Mã giảm giá riêng của các hãng bay khai thác chặng đó.
5. **Ưu đãi thanh toán / Ngân hàng:** Voucher giảm giá qua thẻ/ví điện tử.
6. **Ưu đãi từ Tổng cục Du lịch (TCDL):** Các chương trình kích cầu du lịch nước sở tại.
7. **Khách sạn giá tốt:** Đề xuất 4-6 khách sạn tiêu biểu kèm giá.
8. **Vé trải nghiệm/Tour:** Hoạt động giải trí, tham quan tại điểm đến.
9. **Sự kiện & Mùa vụ đặc trưng:** Cung cấp thông tin du lịch theo mùa (lễ hội, mùa hoa...).
10. **Dịch vụ bổ trợ (Bảo hiểm & Visa):** Tích hợp bán chéo bảo hiểm du lịch và visa.
11. **FAQ & Quy định nhập cảnh:** Dạng accordion thu gọn để tối ưu hóa không gian hiển thị.

*Lưu ý:* Các block từ 4 đến 6 chỉ render khi có chương trình đang chạy. Giao diện sẽ tự động co giãn đẩy các block phía dưới lên để chống khoảng trống (anti-whitespace).

---

## 6. Nguồn Dữ Liệu & Đối Tác Phối Hợp

- **Vé máy bay:** Search/Fare API nội bộ MoMo Travel.
- **Ưu đãi hãng bay:** Bộ phận Online Sales làm việc với đối tác hãng hàng không.
- **Ưu đãi Bank:** Payment/Bank Partnership Team.
- **Ưu đãi TCDL:** Bộ phận BD đối ngoại kết nối với Tổng cục Du lịch các nước.
- **Khách sạn / Trải nghiệm / Visa & Bảo hiểm:** Đồng bộ tự động từ hệ thống API của đối tác liên kết hiện có.

---

## 7. Yêu Cầu Nghiệp Vụ (Functional Requirements)

### 7.1 Hệ thống CMS
- Cho phép tạo mới trang DPH bằng thao tác chọn điểm đến, cập nhật ảnh hero, text và kích hoạt các block cần thiết.
- Cho phép lập lịch hiển thị (bắt đầu - kết thúc) cho từng coupon/banner.
- Hỗ trợ thay đổi thứ tự hiển thị của các block tùy thuộc vào đặc tính điểm đến và thời vụ du lịch.

### 7.2 Hiển thị & Cá nhân hóa cơ bản
- Tự động điền điểm đi dựa trên vị trí GPS hoặc lịch sử tìm kiếm gần nhất của người dùng.
- Đồng bộ giá vé real-time với hệ thống tìm kiếm cốt lõi của MoMo Travel.
- Tự động ẩn các block rỗng để tối ưu hóa diện tích hiển thị (Logic anti-whitespace).

### 7.3 Đo lường & Analytics
- Tracking chi tiết UTM/source_id của từng click và giao dịch thành công phát sinh từ DPH để đánh giá hiệu quả bán chéo.
- Đo lường Scroll-depth và CTR của từng block để làm căn cứ tối ưu hóa thứ tự hiển thị ở các giai đoạn sau.

---

## 8. Đề Xuất Lộ Trình Triển Khai (Roadmap)

```
├── 📅 Phase 0: Chuẩn bị (Tuần 1-2)
│   └── Thống nhất BRD, lựa chọn 2-3 điểm đến pilot (Đài Loan, Thái Lan, Nhật Bản).
│
├── 📅 Phase 1: Pilot (Tuần 3-6)
│   └── Hoàn thiện thiết kế UI/UX, phát triển hệ thống CMS cơ bản và chạy thử nghiệm.
│
├── 📅 Phase 2: Tối ưu hóa (Tuần 7-10)
│   └── Đo lường KPIs, A/B Testing các entry point, điều chỉnh logic CMS dựa theo dữ liệu thực tế.
│
└── 📅 Phase 3: Mở rộng (Tuần 11+)
    └── Hoàn thiện CMS tự vận hành, phủ rộng Top 8-10 điểm đến và tích hợp cá nhân hóa nâng cao.
```

---

## 9. Rủi Ro & Giải Pháp Giảm Thiểu

- **Chậm trễ ưu đãi đối tác:** BD/Partnership đàm phán chậm dẫn đến thiếu coupon.
  * *Giải pháp:* Luôn chuẩn bị sẵn các chương trình ưu đãi mặc định từ MoMo Travel (hoặc đối tác bank dài hạn) làm phương án dự phòng.
- **Sai lệch giá hiển thị:** Lệch giá giữa trang DPH và trang kết quả tìm kiếm chi tiết do cơ chế cache dữ liệu.
  * *Giải pháp:* Thiết lập tần suất dọn dẹp cache (cache invalidation) tối đa 15-30 phút/lần cho các điểm đến trọng điểm.
- **Nghẽn cổ chai Engineering ở Phase 1:** CMS chưa hoàn thiện kịp tiến độ chạy thử nghiệm.
  * *Giải pháp:* Xây dựng phiên bản MVP CMS cực giản (chỉ hỗ trợ bật/tắt On/Off block và thay đổi banner/text tĩnh) ở giai đoạn đầu.

---

## Change Log

- **Tháng 7/2026 (v1.1):** Đồng bộ định hướng từ PRD MoMo Destination Hub: Xác lập vai trò dự án do Media Team điều phối triển khai chính, dưới sự phối hợp, theo dõi và kiểm soát hạ tầng kỹ thuật của Web Platform; định hình bộ chỉ số đo lường chi tiết (Traffic > 250k views, W2A > 12%, Cross-sell > 15% eSIM/Khách sạn) và tích hợp thêm widget tỷ giá ngoại tệ, QR thanh toán quốc tế (PromptPay, NETS).
