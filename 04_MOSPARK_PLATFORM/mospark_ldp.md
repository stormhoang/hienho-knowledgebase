# MoSpark - Landing Page Builder (M1)
## Business Requirement Document (BRD)

> - **Owner:** Bảo / Web Platform
> - **Key Stakeholder:** Huy Lê (VP User Growth Platform)
> - **Version:** v2.0
> - **Updated:** 2026-06-03
> - **Status:** Draft

---

## 1. Elegant Problem Statement
**Vấn đề:** Các Growth Analysts và PM/PO cần tung hàng chục chiến dịch khuyến mãi mỗi tuần, nhưng phụ thuộc hoàn toàn vào Dev/Media Team để tạo Landing Page. Điều này gây thắt cổ chai, làm tăng Time-to-Market từ 1-2 ngày lên 1-2 tuần, lãng phí tài nguyên và làm giảm động lực testing.
**Giải pháp:** MoSpark Landing Page Builder định hình lại cách làm việc theo mô hình **Agentic Org**. Thay vì tự tay tạo trang, PM/PO đóng vai trò "người điều phối" (Orchestrator) ra lệnh cho các AI Agents tự động tạo trang, lắp ráp hình ảnh, viết Thể lệ (TnC) và tích hợp Scheme khuyến mãi. Trải nghiệm "One-click Publish" giúp rút ngắn thời gian launch xuống còn 1-2 ngày với sự kiểm soát chặt chẽ về Brand và Pháp lý.

## 2. Đối tượng sử dụng & Use Cases
Dự án phục vụ những người làm chủ kết quả (Outcome Owner):
- **Growth Analysts (Full-stack):** Người nắm logic chiến dịch, dữ liệu và chịu trách nhiệm trực tiếp về KPI.
- **Product Managers (PM/PO):** Nhóm "non-tech" cần công cụ hiện thực hóa ý tưởng nhanh chóng.

**Phân loại Use Cases:**
- **In-app:** Promotion Pages (Chiến dịch ngắn hạn), Feature Promotion (Giới thiệu tính năng App), T&C & Program Details (Lưu trữ điều khoản cho CS).
- **Out-app:** Growth Marketing (Landing page chạy Ads SEO/SEM), Service Pages (Always-on authority pages), Merchant Pages (Trang cho SME).

## 3. Job-To-Be-Done (JTBD) & Bối cảnh
- **Core JTBD:** *"Khi tôi chạy một chiến dịch, tôi cần một công cụ tự động hóa khâu tạo trang, gắn tracking và tích hợp thể lệ, để tôi có thể tập trung vào việc đo lường KPI (W2A) thay vì ngồi chờ Dev code."*
- Bối cảnh: 66.7% PM "ngại cái mới" và không dám cam kết KPI nếu không có công cụ hỗ trợ chuẩn. Do đó, Builder phải đi kèm với onboarding và template có sẵn.

## 4. Phạm vi tính năng cốt lõi (MVP Core Features)
- **AI-assisted Generation:** Nhập brief (mục tiêu, đối tượng, KPI) ➔ Builder Agent tự sinh cấu trúc và copy.
- **Asset Integration:** Asset Agent tự động lấy hình ảnh/banner từ thư viện chuẩn Brand MoMo (MoBase V2).
- **Scheme & PFM Integration:** Module quản lý Promotion Scheme độc lập được "plug" thẳng vào Builder, đảm bảo dữ liệu quà tặng luôn chính xác và đã duyệt trước.
- **WYSIWYG Editor:** Chỉnh sửa trực quan không cần code.
- **Traffic/Click Dashboard:** Dashboard đo lường theo thời gian thực (Traffic/Click/Source) cho từng trang.

## 5. Quy trình Đưa sản phẩm ra Production (Agentic Workflow)
Chuyển dịch từ việc "tự làm" sang "điều phối AI". Quy trình 7 bước (rút ngắn từ 2 tuần xuống 1-2 ngày):
1. **Khởi tạo (Briefing):** Analyst/PM nhập bối cảnh kinh doanh, mục tiêu và KPI vào AI.
2. **AI Sản xuất (Drafting & Asset):** Builder Agent tạo trang từ template; Asset Agent chèn media chuẩn Brand.
3. **Tích hợp dữ liệu (Integration):** Tự động liên kết các Scheme khuyến mãi hoặc luồng PFM.
4. **Gate A - Review & Edit (Con người):** Analyst chỉnh sửa WYSIWYG (nếu cần), duyệt bản nháp. (QA Agent chạy ngầm check lỗi link, tracking, PII).
5. **Gate B - Phê duyệt (Compliance):**
   - Content: Team Nội dung (BMC) duyệt.
   - Legal: Kiểm tra pháp lý & TnC.
   - Design: Đảm bảo chuẩn Brand.
   *(Lưu ý: Nếu Scheme/TnC đã được duyệt trước offline, bước này có thể Bypass để đẩy nhanh tốc độ).*
6. **Xuất bản (One-click Publish):** Đẩy lên Production, tự động kích hoạt tracking.
7. **Theo dõi (Monitor):** Analytics Agent stream data về Dashboard theo thời gian thực.

## 6. Cơ chế A/B Testing & Tối ưu chuyển đổi (M10 Integration)
Để tối đa hóa tỷ lệ chuyển đổi (W2A) thay vì chỉ ra mắt trang tĩnh, hệ thống tích hợp sẵn luồng A/B Testing (thuộc M10 - Experiment Engine) ngay trên Builder:

### 6.1. Giải pháp Kỹ thuật (Edge-based MAB)
- **Edge Routing chống Flicker:** Việc chia traffic (phân luồng A/B) được thực hiện ở tầng Edge Middleware (Server-side) để tránh giật lag màn hình khi user truy cập, đảm bảo an toàn tuyệt đối cho Core Web Vitals.
- **Thuật toán MAB (Multi-Armed Bandit):** Hệ thống không chỉ test 50/50 thụ động mà tự động nhận diện biến thể chiến thắng (Winner) và bẻ dần traffic về biến thể đó, giúp tránh mất mát chuyển đổi trong suốt vòng đời chiến dịch.

### 6.2. Workflow cho PM/PO
1. **Tạo biến thể:** Từ trang gốc (Variant A), PM ấn `Create A/B Test` để nhân bản thành Variant B.
2. **Chỉnh sửa UI/UX:** Kéo thả sửa Headline, thay đổi KV, màu sắc nút CTA trên Variant B. *(Lưu ý: Các Data Block về Scheme Khuyến mãi và Thể lệ sẽ bị khóa cứng để tránh rủi ro pháp lý).*
3. **Thiết lập:** Nhập Giả thuyết (Hypothesis) bắt buộc và chọn mô hình phân bổ traffic.
4. **Auto-Publish (Fast-track):** Nếu Variant B chỉ thay đổi UI/UX, AI Quality Gate sẽ check chuẩn Brand và cho phép Auto-Live mà không cần xin duyệt lại từ đầu (Bypass Gate B).

## 7. Điểm Tối ưu & Guardrails (Rào cản kiểm soát)
- **Tự động hóa Business Constraints:** Build "ẩn" các ràng buộc Brand/SEO vào trong công cụ. PM chỉ cần prompt, kết quả tự động đúng chuẩn.
- **Cơ chế Phê duyệt Tinh gọn:** Giảm tải thủ công bằng các "Guardrails" quét tự động (Quality Gate).
- **Economic Mechanism (Token Economy):** Cấp Token theo Tier/Ngân sách BU để kiểm soát chi phí gọi AI API.
- **Life-cycle Management (Auto-Sunset):** Tránh "Zombie URLs" bằng tính năng nuôi trang hoặc tự động đóng/chuyển hướng (301/410) trang cũ để giữ vững Topical Authority.

### 7.1. A/B Testing Compliance Matrix
Để cân bằng giữa tốc độ Go-to-market và tính tuân thủ pháp lý (YMYL), tính năng A/B Testing bị ràng buộc bởi bộ quy tắc sau:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng mục thay đổi trên Variant B</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Quyền của PM/PO</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cấp độ Phê duyệt (Gate B)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hệ quả rủi ro</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thay đổi CTA (Màu sắc, Text)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cho phép toàn quyền</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Auto-Pass</strong> (Không cần duyệt)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đổi Headline, Copywriting</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cho phép toàn quyền</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Auto-Pass</strong> (AI check ngôn từ cấm)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thay Banner / Key Visual</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cho phép toàn quyền</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Auto-Pass</strong> (Nếu dùng hình từ MoBase)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thay đổi Điều khoản & Điều kiện (TnC)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Khóa (Disabled)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phải submit luồng duyệt Legal (24h)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rất cao (Pháp lý)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đổi Scheme Khuyến mãi / Giá trị quà</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Khóa (Disabled)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phải submit luồng duyệt BU Head</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rất cao (Tài chính)</td>
    </tr>
  </tbody>
</table>

## 8. Key Success Metrics (Chỉ số đo lường)
- **Time-to-launch:** Thời gian từ Brief ➔ Live Page (Mục tiêu: < 1-2 ngày).
- **Self-serve rate:** % trang campaign được tạo không cần raise ticket cho Media Team.
- **KPI-committed pages:** % trang có gắn mục tiêu KPI rõ ràng (Chuyển đổi từ Requester sang Owner).
- **Cost avoided:** Số giờ Dev/Media Team tiết kiệm được (Đóng góp vào bài toán Build-vs-Buy).
- *Guardrail Metric:* Tỷ lệ vi phạm Compliance/Brand bị từ chối tại Gate B.

## 9. Lộ trình Phát triển & Go-To-Market (Next Steps)
Chiến lược tiếp cận "Beachhead": Bắt đầu từ nhóm 15% PM "Serious" có nhu cầu cao (3-5 trang/tháng) làm Design Partners.
- **Giai đoạn 1 - Validate & Funding:** Giải quyết bài toán Build-vs-Buy (chi phí), chuẩn hóa TCO.
- **Giai đoạn 2 - MVP Build:** Tập trung xây dựng tính năng Core (4A) và Workflow đơn lẻ (5A).
- **Giai đoạn 3 - Assisted Rollout:** Đưa bộ Starter Template và quy trình Onboarding để phá vỡ rào cản 66.7% PM "ngại cái mới".
- **Giai đoạn 4 - Scale & Integrate:** Scale lên workflow tự động hóa hàng loạt (Variant fan-out, A/B Testing, Multi-tenant) và tích hợp sâu PFM data.

## 9.5. Kế hoạch Nâng cấp Tính năng trong H2/2026

Trong H2/2026, nền tảng Landing Page Builder sẽ tập trung nâng cấp các tính năng hỗ trợ tự chủ vận hành cho Cell Teams và chuẩn hóa chất lượng trang:

1. **Mở rộng Kho Templates:** Phát triển và bổ sung nhiều mẫu thiết kế Landing Page (Templates) chuẩn hóa theo nhận diện thương hiệu MoMo, tối ưu riêng cho từng mục tiêu chiến dịch (khuyến mãi, giới thiệu dịch vụ, đăng ký thông tin).
2. **Tiêu chuẩn Giao diện & Tự động hóa Nội dung:**
   *   *Mặc định Header/Footer:* Mọi trang Landing Page khởi tạo mới sẽ được nhúng sẵn khối Header/Footer chuẩn của msite (vẫn cho phép Editor chỉnh sửa nội dung hoặc ẩn đi nếu cần thiết).
   *   *Auto-mapping Blog/News:* Hỗ trợ tính năng kéo và hiển thị tự động danh sách các bài viết Blog/Tin tức liên quan trực tiếp từ các dự án Microsite tương ứng mà không cần PM cấu hình liên kết thủ công.
3. **Instant Live Preview (Xem Demo nhanh):** Cung cấp trình live preview trực tiếp trên Admin Dashboard để PM kiểm tra hiển thị trên Mobile/Desktop tức thì mà không cần xuất source code (tách source) hay chạy thử ở môi trường local.

---

## 10. Open Considerations (Các vấn đề cần chốt)
- **Build-vs-buy economics:** Cần số liệu chi phí TCO thực tế để xin Funding (Đang chờ xác minh).
- **Tính pháp lý của Data-capture:** Tính năng thu thập SĐT cần qua bài test về Privacy/Consent (PII) trước khi live.
- **Where pages live:** Quyết định chiến lược hạ tầng (Own domain, Webview hay In-app).
- **Replace vs Complement:** Công cụ này sẽ thay thế hoàn toàn hay chỉ bổ trợ cho luồng in-app promotion hiện tại? (Sẽ thay đổi toàn bộ câu chuyện Value Story).
- **Phạm vi A/B Testing:** PM chỉ được test ở mức độ UI/UX/Copywriting hay được phép test luôn cơ cấu giải thưởng / Scheme khuyến mãi (vốn sẽ làm flow duyệt Compliance phức tạp hơn)?

---

## 11. Prototype Brief: Luồng Thiết lập A/B Testing trên Builder

Để đảm bảo team Dev hiểu rõ cách thức vận hành hệ thống A/B Testing (M10) khi nhúng vào Landing Page Builder (M1), dưới đây là mô tả Prototype Brief cho tính năng này.

### 11.1. User Jobs (JTBD)
- **J1 - Khởi tạo thử nghiệm nhanh:** PM muốn tạo một bản sao của trang hiện tại để thay đổi một vài yếu tố mà không cần phải setup lại toàn bộ Data và Scheme từ đầu.
- **J2 - Phân bổ traffic an toàn:** PM muốn chỉ cho 10% người dùng xem bản thử nghiệm để tránh rủi ro mất chuyển đổi nếu bản mới quá tệ.
- **J3 - Tự động hóa chiến thắng:** PM không muốn phải canh chừng dashboard mỗi ngày, hệ thống cần tự biết bản nào tốt hơn và dồn traffic về bản đó.

### 11.2. Trải nghiệm giao diện (UI/UX Flow)
1. **Trạng thái Mặc định:** Tại giao diện Editor của Variant A (trang gốc), có nút `[Create A/B Test]` ở thanh Top Bar, cạnh nút Publish.
2. **Khởi tạo Variant B:** Khi click, hệ thống sinh ra một bản Duplicate hoàn chỉnh. Tab bar phía trên sẽ hiển thị: `[Variant A (Original)]` | `[Variant B (Draft)]`.
3. **Locked Elements (Khóa thành phần):** Khi PM đang ở Variant B, nếu họ click vào các component chứa Thể Lệ hoặc Quà tặng, component sẽ hiện overlay màu xám với biểu tượng 🔒 *Locked for Compliance*. PM chỉ có thể sửa Headline, Image, Button Color.
4. **Màn hình Setup Test:** Khi bấm Publish Variant B, hệ thống hiện Modal:
   - **Hypothesis (Giả thuyết):** Khung nhập text bắt buộc.
   - **Traffic Split Rule:**
     - *Option 1:* Auto-Optimize (Multi-Armed Bandit) - Khuyên dùng.
     - *Option 2:* Fixed Split (Thanh trượt kéo thả từ 1% đến 99%).
5. **Dashboard Thống kê:** Màn hình Analytics của trang sẽ có thêm tab `[A/B Test Results]`. Hiển thị biểu đồ dạng phễu (Views ➔ CTA Clicks) của 2 biến thể song song, và một chỉ báo "Bayesian Probability of Beating Baseline" (VD: *98% cơ hội Variant B tốt hơn*). Nút `[Deploy Winner]` sẽ sáng lên khi hệ thống xác nhận.
