# PRD: Bản Tin An Toàn Bảo Mật (ATBM) - Q2/2026 & Quarterly Cycle

> - **Use Case:** Bản Tin An Toàn Bảo Mật (Trust Product Campaign)
> - **URL chính:** momo.vn/atbm/ban-tin/{quy-nam} (Ví dụ: `momo.vn/atbm/ban-tin/q2-2026`)
> - **Khối phụ trách:** Risk & Security (GPD Web Platform)
> - **Phiên bản:** 1.0 · Tháng 6/2026
> - **Trạng thái:** [DRAFT] - Sẵn sàng cho phát triển (Tháng 7/2026 Release)

---

## 1. Overview & Business Value

### 1.1 Business Goals
*   **Mục tiêu chiến lược:** Định hình sản phẩm theo mô hình **Trust-led Growth** (Niềm tin giúp khách hàng nói về MoMo), xây dựng niềm tin số toàn diện từ trong ra ngoài (Inside out) bám sát 6 chiều kích cốt lõi (Security & Data Privacy, App Performance, Customer Service, Transparency, UI/UX, Branding).
*   **Mục tiêu cốt lõi:** Phục vụ trực tiếp cho chương trình khảo sát (Survey) thương hiệu chạy từ Tháng 5 đến hết Tháng 8/2026.
*   **Chỉ số đo lường (KPI):** Tăng **30%** tỷ lệ đồng thuận của người dùng đối với hai câu hỏi khảo sát an toàn bảo mật cốt lõi:
    1. *“Tôi cảm thấy dùng MoMo an toàn hơn.”*
    2. *“Tôi thấy MoMo có nhiều công cụ an toàn bảo mật.”*
*   **Tần suất phát hành:** Mỗi quý 1 bản tin (Quarterly Cycle).

### 1.2 Target Audience
*   Người dùng ví MoMo và cộng đồng khách hàng đại chúng quan tâm đến các giải pháp bảo vệ tài sản trực tuyến, cần nâng cao nhận thức phòng chống lừa đảo mạng.

---

## 2. Detailed Specifications (Landing Page Features)

Bản tin được thiết kế dưới dạng **Long Form Content** với các khối tính năng tương tác sinh động để tăng tính gắn kết (Engagement):

### 2.1 Cấu trúc Navigation & Điều hướng
*   Tích hợp thanh Menu điều hướng tại đầu trang và chân trang Bản tin:
    *   Hyperlink dẫn về trang chủ An Toàn Bảo Mật chung (`momo.vn/atbm`).
    *   Widget danh sách liên kết đến các số Bản tin ATBM của các quý khác (Dự kiến: số tiếp theo Q3/2026, Q4/2026...).

### 2.2 Khối 3 Flip Cards (Thẻ lật tương tác)
*   **Mô tả:** 3 thẻ thông tin tương tác (lật mặt trước/mặt sau) chứa nội dung cảnh báo hoặc tips bảo mật.
*   **Nút Download Asset:**
    *   Mỗi thẻ lật đi kèm một nút bấm tải ảnh riêng biệt (Ví dụ: "Tải thẻ này về máy").
    *   *Yêu cầu kỹ thuật:* Khi click, hệ thống tự động tải xuống (download) trực tiếp tệp hình ảnh gốc (Asset file) của thẻ đó về máy (không phải ảnh chụp màn hình screenshot toàn bộ trang Web). Điều này phục vụ nhu cầu lưu trữ và tự chia sẻ (share) thủ công của người dùng.
    *   *Tính năng tương lai (Next Version):* Nghiên cứu tích hợp App Developer APIs để hỗ trợ chia sẻ trực tiếp lên các mạng xã hội.

### 2.3 Khối Tính Năng (Feature Highlights)
*   **Mô tả:** Giới thiệu các công cụ an toàn bảo mật thực tế hiện có trên ứng dụng MoMo (như Khiên Bảo Vệ, Chặn giao dịch lạ, Xác thực sinh trắc học).
*   **Điều hướng Web-to-App:** Mỗi tính năng đi kèm một nút bấm hoặc hyperlink chứa Deep Link mở App MoMo để điều hướng trực tiếp người dùng đến đúng màn hình cài đặt/kích hoạt tính năng đó in-app.

### 2.4 Khối Highlight Con Số (Social Proof Dashboard)
*   **Mô tả:** Sử dụng cấu trúc hiển thị số liệu động (đếm số chạy tăng dần - CountUp) để biểu diễn các chỉ số tác động ấn tượng của hệ thống bảo mật MoMo:
    *   *Chỉ số Mức độ Tin cậy của người dùng (Q1/2026):* Đạt kỷ lục mới, niềm tin số gia tăng bền vững qua các quý (e.g., `4.18/5`).
    *   *Số lượng người dùng được bảo vệ:* Hiển thị số lượng MAU được bảo vệ (e.g., `1.2M+`).
    *   *Dòng tiền lừa đảo đã chặn:* Hiển thị số tiền đã được ngăn chặn thành công (e.g., `320 tỷ₫`).
    *   *Số xấu bị gắn cờ cảnh báo:* Số lượng tài khoản xấu bị nhận diện (e.g., `89K+`).
    *   *Tần suất tiếp nhận báo cáo:* Chu kỳ hoạt động liên tục (e.g., `24/7`).
*   **Tham chiếu Giao diện & CSS (Codebase Reference):**

```javascript
const IMPACT = [
  { end: 4.18, max: 5, decimalPlaces: 2, label: "chỉ số mức độ tin cậy của người dùng", icon: "star-half" },
  { end: 1245678, label: "người dùng được bảo vệ", icon: "users" },
  { end: 320, suffix: " tỷ₫", label: "dòng tiền lừa đảo đã chặn", icon: "shield-check" },
  { end: 89420, label: "số xấu bị gắn cờ cảnh báo", icon: "flag" },
  { end: 24, suffix: "/7", label: "tiếp nhận báo cáo liên tục", icon: "clock" },
];
```

---

## 3. Quy Hoạch Vị Trí Tích Hợp (Trang Chủ ATBM)

Đường dẫn/Widget giới thiệu Bản tin ATBM sẽ được nhúng trực tiếp vào Trang Chủ An Toàn Bảo Mật (`momo.vn/atbm`) theo phân cấp vị trí nghiêm ngặt:

*   **Vị trí hiển thị:** Nằm **dưới** mục Chứng chỉ quốc tế (Certification - *nêu bật các quy chuẩn bảo mật PCI-DSS, ISO 27001...*) và nằm **trên** mục Giải đáp thắc mắc (FAQ - *giải đáp các câu hỏi thường gặp*).

```
[ Trang Chủ An Toàn Bảo Mật ]
┌───────────────────────────────┐
│ ...                           │
├───────────────────────────────┤
│ 1. Chứng chỉ quốc tế (Cert)   │
├───────────────────────────────┤
│ >>> WIDGET BẢN TIN ATBM <<<   │
├───────────────────────────────┤
│ 2. Giải đáp thắc mắc (FAQ)    │
├───────────────────────────────┤
│ ...                           │
└───────────────────────────────┘
```

---

## 4. Technical & Tracking Requirements

### 4.1 Asset Storage & Download logic
*   Hình ảnh mặt trước/mặt sau của Flip Cards phải được lưu trữ trên CDN với chất lượng tối ưu (dung lượng vừa phải để tải trang nhanh nhưng đủ nét khi người dùng tải về điện thoại).
*   Sử dụng HTML5 `download` attribute hoặc FileSaver.js để kích hoạt luồng tải tệp ảnh trực tiếp từ URL CDN của hình ảnh.

### 4.2 Tracking Metrics
*   **Flip Card Interactions:** Đo lường số lượt lật thẻ và số lượt nhấn nút "Tải thẻ".
*   **Feature Link Clicks:** Đo lường số lượt click điều hướng mở App MoMo (W2A clicks).
*   **Newsletter Navigation:** Đo lường số lượt chuyển đổi qua lại giữa bản tin các quý và tỷ lệ cuộn đọc hết trang (Scroll depth).

### 4.3 Performance & End-to-End Latency Monitoring (Đo lường thời gian xử lý E2E)
*   **Mục tiêu:** Đo lường và giám sát chặt chẽ thời gian phản hồi đầu-cuối (End-to-End) của các tính năng tương tác trên Bản tin nhằm tối ưu hiệu suất ứng dụng.
*   **Các mốc đo lường chính:**
    1.  **Asset Download E2E Time (Tải thẻ lật):** Thời gian từ khi người dùng click "Tải thẻ" đến khi file ảnh bắt đầu được tải xuống máy hoàn tất qua CDN. *Tiêu chuẩn:* **< 1.5 giây** (nhờ cơ chế CDN Caching).
    2.  **Smart CTA Web-to-App Routing E2E Time:** Thời gian từ lúc người dùng click nút mở app đến khi app nhận diện được schema deep link. *Tiêu chuẩn:* Phản hồi tức thì **< 500ms** trên client.
