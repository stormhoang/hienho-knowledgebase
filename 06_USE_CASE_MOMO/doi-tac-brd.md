# BRD: MoMo Merchant Page (MMP) Mini Web App

> - **Dự án:** MoMo Merchant Page (MMP) - Mini Web App (Phase 1)
> - **Nền tảng:** MoSpark
> - **Khối phụ trách:** GPD (Growth Platform Division)
> - **Owner:** GPD - Web Platform
> - **Phiên bản:** 3.0 - 2026-07-17 (Chuyển đổi định hướng MMP PRD)
> - **Trạng thái:** Phase 1 - Xây dựng công cụ Sales Enabler (Mobile Fast Creator)

---

## 1. PRODUCT OVERVIEW (Tổng Quan Sản Phẩm)

### 1.1 Vấn đề và Bối cảnh (Problem & Context)
Sự thiếu hụt nền tảng hiển thị đối tác (Merchant Detail Page) trên Web dẫn đến việc rò rỉ lượng truy cập có ý định giao dịch cao (High Purchase Intent) sang các trang danh bạ của bên thứ ba, đồng thời làm đứt gãy luồng tương tác Offline-to-Online (O2O) của hệ sinh thái MoMo (Ví Trả Sau, Soundbox).

Song song đó, **Đội ngũ Phát triển Thị trường (Salesman)** gặp khó khăn khi thuyết phục các chủ quán SME hợp tác liên kết với MoMo và sử dụng các sản phẩm tài chính/công nghệ. Salesman thiếu một công cụ hữu hình, trực quan để tạo ra giá trị cộng thêm lập tức tại hiện trường (như một trang web chuyên nghiệp cho chủ quán).

### 1.2 Product Statement
**MoMo Merchant Page (MMP)** là một Mini Web App được xây dựng trên nền tảng MoSpark, đóng vai trò như một **Sales Enabler Tool**. MMP hỗ trợ hàng trăm Salesman của MoMo trong quy trình bán hàng trực tiếp tại điểm bán: từ thu thập thông tin, trình diễn Case Study, đến việc **tạo nhanh một Merchant Page chuẩn SEO trong 10 phút** bằng công nghệ GenAI.

Sản phẩm này là "món quà" công nghệ số mà Salesman tặng cho SME để chốt deal liên kết thanh toán, qua đó cấp quyền cho Merchant chủ động quản lý sự hiện diện số của mình thông qua luồng duyệt Magic Link.

### 1.3 Product Goals (Phase 1)
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục tiêu</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tăng tỷ lệ chốt deal</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% Lead To Merchant Conversion</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tăng so với Baseline</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Rút ngắn Time-to-Live</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Từ lúc Sale gặp Merchant ➔ Page Live</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">≤ 1 ngày (10 phút gen AI)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tốc độ mở rộng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số lượng trang Merchant tạo mới/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">500 Pages / 2 tuần (Phase 1)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tỷ lệ Merchant Active</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% Merchant tự liên kết & share page lên Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">≥ 40%</td>
    </tr>
  </tbody>
</table>

## 2. USERS & ROLES (Phân Quyền Người Dùng)

Dự án có 3 nhóm người dùng tham gia vào quy trình (CMS Workflow):

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Số lượng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đăng nhập</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Quyền chính</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Salesman</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100 - 300 users</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Google SSO (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">@momo.vn</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quản lý danh sách merchants đang phụ trách, tạo mới trang (GenAI), trình chiếu Case Study, gửi link duyệt cho Merchant.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Merchant</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1000+ users</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Magic Link qua Zalo (SĐT)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xem bản xem trước (Preview), phê duyệt (Approve) hoặc yêu cầu chỉnh sửa, quản lý thông tin điểm bán của mình.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Manager</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2 - 5 users</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Google SSO (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">@momo.vn</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quản trị viên hệ thống, QA các trang sau khi Merchant duyệt, xuất bản lên Live (Approve Publish).</td>
    </tr>
  </tbody>
</table>

**Chi tiết Phân quyền:**
*   **Salesman:** Chỉ xem và quản lý merchants của mình; không thể trực tiếp xuất bản (Live) trang; tạo tài khoản/link cho merchant.
*   **Merchant:** Chỉ quản lý trang của chính mình thông qua link bảo mật; có thể duyệt hoặc gửi yêu cầu sửa.
*   **Manager:** Nhìn thấy toàn bộ merchants; có quyền duyệt cuối cùng (QA), quản lý tài khoản Salesman.

---

## 3. USER FLOWS (Hành Trình Người Dùng)

Hệ thống hoạt động dựa trên sự tương tác liên tục giữa 3 nhóm người dùng, bắt đầu từ điểm chạm offline:

### 3.1 Hành trình của Salesman (Đi thị trường)
1.  **Đăng nhập & Quản lý:** Truy cập `momo.vn/merchant/login` và đăng nhập bằng email công ty. Vào Dashboard trên Web App xem danh sách merchants.
2.  **Tạo thông tin Merchant Profile (Trước tư vấn):** Bấm "Thêm Merchant mới", điền Tên thương hiệu, Địa chỉ, Category. Hệ thống hiển thị Case Study, Sale Kit để Salesman chuẩn bị tư vấn và demo.
3.  **Tư vấn tại điểm bán:** Salesman tư vấn cho Merchant thành công và chuyển sang bước thu thập dữ liệu.
4.  **Thu thập Dữ liệu đầy đủ:** Điền form gồm Tên chủ cửa hàng, SĐT, giờ mở cửa, Location (định vị), chụp ảnh (Logo/chủ quán, 2 ảnh thực tế, ảnh menu), và thông tin Social. Hệ thống GenAI tạo trang trong 1 phút và Salesman chỉnh sửa trong 10 phút.
5.  **Merchant Onboarding:** Gửi thông tin Magic Link qua Zalo/Facebook để Merchant kích hoạt và preview trang trên điện thoại.
6.  **Merchant Approve:** Merchant xem và chỉnh sửa cơ bản. Sau khi approve, trạng thái chuyển sang "on preview".
7.  **Merchant Workflow:** Salesman và Manager vận hành luồng trạng thái. M4B active, sync MID, liên kết MID. Manager approve cho phép trang live.

### 3.2 Hành trình của Merchant (Chủ Quán)
1.  **Nhận & Click Link:** Nhận tin nhắn Zalo/Facebook kèm Magic Link từ Salesman.
2.  **Merchant Onboarding:** Click vào link, mở trang preview với đầy đủ Logo, tên, địa chỉ, story, ảnh... Bấm xác thực tài khoản và quản lý tài khoản của mình.
3.  **Merchant Approve:** Kiểm tra thông tin cá nhân, cửa hàng và có thể chỉnh sửa cơ bản, sau đó xác nhận.
4.  **Merchant Update:** Có thể login lại để yêu cầu chỉnh sửa thông tin (Tên Cửa Hàng, Địa Chỉ, Giờ mở cửa, SĐT, hình ảnh, Social Link). Submit ➔ Manager Approve ➔ cập nhật trong 24h.

### 3.3 Hành trình của Manager (QA & Publish)
1.  **QA Queue:** Manager vào QA Dashboard xem queue các trang đang chờ QA sau khi Merchant approve. Spot check 80% hoặc Full check 20%.
2.  **Hành động (Approve/Reject):**
    *   **Approve:** Trang tự động Live.
    *   **Reject:** Trả về kèm comment cho Salesman fix và Submit lại.
3.  **Monitor Dashboard:** Theo dõi throughput, status funnel, xem performance của Salesman.

---

## 4. MERCHANT PAGE STATUS LIFECYCLE (Vòng Đời Trạng Thái)

Toàn bộ quá trình từ lúc gặp Merchant đến lúc trang lên Live được số hóa qua các trạng thái:

1.  `✏️ DRAFT`: Salesman đang thu thập và điền form thông tin đầy đủ, chưa khởi tạo MMP.
2.  `🔄 GENERATING`: GenAI đang xử lý tạo MMP (10 - 20 phút).
3.  `👁️ PREVIEW`: Salesman đã edit thông tin và gửi link cho Merchant.
4.  `✅ ONBOARDING`: Merchant khởi tạo tài khoản và Approved MMP.
5.  `⏳ M4B_LINKED`: MID synced, Sale/Manager liên kết MMP với MID.
6.  `🔍 QA_REVIEW`: Chờ Manager duyệt nội dung.
7.  `🟢 PUBLISHED (LIVE)`: Trang chính thức công khai trên Google.

*(Nếu Manager Reject ở bước 6 ➔ Trạng thái lùi về `REVISION NEEDED` để Salesman fix).*

---

## 5. KIẾN TRÚC & TÍNH NĂNG CÔNG CỤ (MMP Tech Spec)

### 5.1 Tech Stack
*   **Frontend:** Next.js 14 (App Router) cho UI Salesman/Manager và Preview Page. Mobile-first UI.
*   **Backend/DB:** Supabase (PostgreSQL, Auth, Storage) với Row Level Security (Sales chỉ thấy số liệu của mình).
*   **GenAI Engine:**
    *   *Gemini Pro:* Viết mô tả chuẩn SEO, FAQ Schema theo Category.
    *   *Imagen / Canva API:* Sinh banner, tự động trích xuất màu thương hiệu, chèn logo MoMo & VTS.
*   **Auth:** Google SSO (cho Sales/Manager); Zalo ZNS / SMS Magic Link (cho Merchant).

### 5.2 GenAI Pipeline (Luồng tạo trang tự động)
1.  **Data Lookup:** Tìm Place ID qua Google Business, kéo rating, review.
2.  **Text Synthesis (Gemini):** Đọc ngành hàng (ví dụ F&B) + Tên quán ➔ Viết 300 từ PR chuẩn Local SEO, đề cập tự nhiên đến thanh toán bằng Ví Trả Sau.
3.  **Image Synthesis:** Dựng banner 1200x630, overlay màu nhận diện, đóng dấu xác thực MoMo.
4.  **Schema Structuring:** Tự động gen mã JSON-LD LocalBusiness, Breadcrumb, FAQPage chèn vào HTML để Google AI đọc.

---

## 6. SẢN PHẨM ĐẦU RA: MERCHANT DETAIL PAGE (Mặt Tiền Của Quán)

Mục tiêu cuối cùng của quy trình MMP là tạo ra một trang hiển thị (Digital Presence) cho đối tác tại địa chỉ `momo.vn/merchant/{slug}`. Trang này phải đạt tiêu chuẩn để hứng Traffic từ Google và kết nối O2O:

### 6.1 Giao diện & Thành phần
Trang đối tác là một Single-Page tối giản, gồm:
1.  **Co-branded Header:** Hình ảnh (Banner) sinh bởi AI kết hợp logo MoMo và Thương hiệu.
2.  **NAP & Map:** Tên, Địa chỉ, SĐT ẩn 4 số cuối (NĐ13, ấn nút "Xem" để hiển thị), Giờ mở cửa, Google Maps Mini.
3.  **Payment Badge:** Huy hiệu hiển thị các phương thức thanh toán ("Chấp nhận Ví Trả Sau", "Có MoMo Soundbox").
4.  **AI Description:** Bài giới thiệu quán do GenAI viết tự động.
5.  **O2O Promotion / VTS Module:** Widget hướng dẫn kích hoạt Ví Trả Sau hoặc hiển thị mã hoàn tiền (nếu có).

### 6.2 Vai trò Điểm Chạm (Consumer JTBD)
Dù tạo ra bằng công cụ nội bộ cho Sales, trang web hướng tới việc phục vụ User cuối (Consumer):
*   **Xác thực điểm thanh toán:** User search "Quán X có nhận Ví Trả Sau không?" ➔ Trang web xác nhận, loại bỏ rủi ro bị từ chối tại quầy.
*   **Kích hoạt O2O:** Tại quán, user quét QR code (tạo tự động từ hệ thống) dẫn về trang này để xem thực đơn hoặc ưu đãi.

---

## 7. SUCCESS METRICS & TIMELINE

### 7.1 Chỉ số Thành công (Phase 1)
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Expected Target</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nguồn đo lường</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Sales Conversion (Demo ➔ Page Created)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">≥ 80%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">DB Logs</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Merchant Approve Rate (Lần đầu)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">≥ 70%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">DB Logs</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tốc độ sinh trang (GenAI Pipeline)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">10 - 20 phút</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">System Performance</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>QA Pass Rate (Lần đầu)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">≥ 85%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Manager Dashboard</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Total Live Pages (2 tuần Launch)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">500 Pages</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Supabase DB</td>
    </tr>
  </tbody>
</table>

### 7.2 Timeline Triển khai (4 Tuần)
*   **Tuần 1:** Setup Database (Supabase), Auth, Dashboard Salesman, Magic Link Flow cơ bản.
*   **Tuần 2:** Tích hợp GenAI Pipeline (Gemini/Imagen), Google Business API. Hoàn thiện luồng tạo và gửi Preview.
*   **Tuần 3:** Xây dựng Merchant Preview Page, Manager QA Dashboard, luồng webhook từ M4B (sync MID).
*   **Tuần 4:** E2E Testing, Pilot nội bộ 5 Salesman, Go-live 20 merchants thật. Chuẩn bị Scale lên 500 merchants.

---

## Change Log

- **Tháng 7/2026 (v3.0):** Chuyển đổi định hướng MMP PRD thành Mini Web App trên nền tảng MoSpark, đóng vai trò công cụ Sales Enabler (Mobile Fast Creator).
