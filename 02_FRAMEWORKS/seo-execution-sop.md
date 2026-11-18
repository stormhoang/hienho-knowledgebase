# 🚀 Quy trình Triển khai SEO Dự án (MoSpark Ecosystem)

## Mục tiêu tài liệu
Tài liệu này là Framework thực thi (SOP) dành riêng cho các dự án Web Content tại MoMo (sử dụng nền tảng MoSpark).
Mục tiêu: Đảm bảo 100% nội dung xuất bản đạt chuẩn **E-E-A-T**, tối ưu hóa **Web-to-App Pipeline**, và tuân thủ chặt chẽ tiêu chuẩn kiểm duyệt của hệ thống.

---

## Nguyên tắc cốt lõi (MoMo Standard)
1. **User Intent First, Search Engine Second:** Phục vụ trực tiếp JTBD của người dùng MoMo (Vay Nhanh, Đóng Phạt Nguội, Tìm Merchant...).
2. **MoSpark Compliance:** Mọi trang đều phải qua Gatekeeper. **Chỉ golive khi SEO/GEO Score > 80**.
3. **GenAI Automation:** Nội dung YMYL cần expert review trước khi xuất bản. Hai prompt cũ đã được loại bỏ khỏi quy trình; không còn là nguồn bắt buộc cho Agent.
4. **Data-Driven Handoff:** Không publish nếu chưa chốt Event Spec với team DA. SEO tại MoMo đo lường bằng **Conversion (App Open/Transaction)**, không chỉ đo Traffic.

---

## Quy trình 8 bước thực thi trên MoSpark

### 1. Discovery & JTBD Analysis
*   **Action:** Đọc tài liệu Use Case BRD (Ví dụ: `doi-tac-brd.md`, `phat-nguoi-brd.md`).
*   **Xác định JTBD:** Người dùng muốn giải quyết rào cản thao tác hoặc nhu cầu gì? (Ví dụ: "Quán này có cho thanh toán Ví Trả Sau không?").
*   **Gate Check:** Xác định xem chủ đề này có vi phạm chính sách **YMYL** (Your Money or Your Life) không. Nếu có, trigger `momo-ymyl-guideline.md`.

### 2. Research & Intent Mapping
*   **Action:** Gom cụm từ khóa (Keyword Clustering).
*   **Xác định phễu:** Map các cụm từ khóa vào Web2App Funnel (Awareness ➔ Consideration ➔ App Open).
*   **Khởi tạo dự án:** Tạo biến `Project: [Tên Use Case]` trên MoSpark để bắt đầu track resources.

### 3. Information Architecture (Thiết kế Cấu trúc)
*   **Action:** Phân bổ URL Structure (Landing Page, Hub, Detail/Microsite).
*   **Internal Link Strategy:** Đảm bảo dòng chảy PageRank hướng về trang Conversion chính (vd: Trang hướng dẫn thanh toán QR).
*   **SME Digital Presence (Nếu áp dụng):** Với các dự án như Merchant, cấu trúc trang phải là Standalone Microsite theo chuẩn Local SEO NAP.

### 4. Content Strategy & GenAI Briefing
*   **Action:** Dùng AI (ChatGPT/Claude) kết hợp với các **Skill Prompts** của MoMo để sinh Outline hàng loạt.
*   **Quy định:** Mỗi trang phải giải quyết dứt điểm 1 Search Question. Cấm nhồi nhét Intent.
*   **Output:** Bộ Brief được duyệt, sẵn sàng đẩy vào hệ thống MoSpark GenAI.

### 5. Technical SEO & Platform QA (Nút thắt quan trọng)
*   **Action:** Audit trên môi trường Staging.
*   **Gatekeeper Check:** Điểm SEO & GEO Score phải > 80.
*   **Bot Access:** Đảm bảo `llms.txt` và `robots.txt` đã mở cửa (Allow) cho các bot quan trọng: `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`.
*   **Core Web Vitals:** Tốc độ tải trang LCP < 2.5s (Mobile-first).

### 6. Production, Tracking & Handoff
*   **Action:** Bơm nội dung lên hệ thống.
*   **Event Spec:** Chốt với Hải (Team DA) các cờ tracking (`momo-deep-link-click`, `cta_install`). Đảm bảo `web-tracking.md` được tuân thủ.
*   **Publish:** Đóng băng URL và release bản Live.

### 7. Đo lường Web-to-App (Post-launch)
*   **Action:** Mở dashboard hằng tuần.
*   **Metrics chính:**
    * CTR (Google Search Console).
    * Tỷ lệ App Open (Click Deep-link).
    * Số lượng Merchant quét mã thành công từ O2O loop (Nếu là Merchant Page).

### 8. Optimize & Maintenance (Vòng lặp 30 ngày)
*   **Action:** Cập nhật nội dung theo thuật toán mới hoặc tính năng sản phẩm mới của MoMo.
*   **AI Citation Audit:** Hỏi thử các công cụ AI (ChatGPT, Perplexity) xem chúng có trích dẫn đúng thông tin từ trang của MoMo hay không. Sửa `llms.txt` nếu cần.

---

## 🛑 Bảng kiểm "Tử thần" (Sign-off Checklist)
Tuyệt đối KHÔNG BẤM PUBLISH nếu thiếu 1 trong 4 điều kiện sau:
- [ ] Điểm MoSpark Gatekeeper SEO/GEO < 80.
- [ ] Các claims về tài chính/lãi suất chưa được Pháp chế/Product duyệt (YMYL Violation).
- [ ] Chưa chốt Event ID tracking với team DA.
- [ ] Nút CTA Deep-link bị hỏng trên thiết bị Mobile.
