# MoSpark - Chatbot
Trợ lý AI tư vấn và hỗ trợ người dùng toàn trang Web

> - **Project Name:** MoSpark Web Platform
> - **Division:** GPD (Growth Platform Division)
> - **Owner:** Bảo
> - **PIC:** Duy (Tech)
> - **Version:** 1.1 · June 2026

---

## 1. Mục Đích & Vai Trò Chiến Lược

### 1.1. Bối cảnh
Với định hướng phát triển của MoSpark, website momo.vn ngày càng đa dạng với hàng chục Use Case (Ví Trả Sau, Vay Nhanh, Bảo Hiểm, Phạt Nguội, Đối tác...) và lượng thông tin đồ sộ. Tuy nhiên, người dùng thường có xu hướng "lười đọc" toàn bộ nội dung tĩnh mà chỉ muốn tìm nhanh thông tin để giải quyết một JTBD cụ thể (VD: "Phí bảo hiểm xe máy là bao nhiêu?", "Nợ xấu có mở Ví Trả Sau được không?").

Việc không tìm thấy thông tin nhanh chóng trên một trang web lớn dẫn đến tỷ lệ thoát trang (bounce rate) cao và mất cơ hội chuyển đổi Web-to-App (W2A).

### 1.2. Giải pháp: mospark_chatbot - Agentic Web Chatbot
Định vị không phải là một công cụ trò chuyện mở (open-domain chat), mà là một **PLG Tool (Utility)** được nhúng trên **toàn bộ website momo.vn**.

**4 Nguyên tắc thiết kế cốt lõi:**
1. **Zero-Scripting (Contextual Grounding):** Dù người dùng đang ở bất kỳ trang nào, Chatbot tự động nhận diện ngữ cảnh (URL) để load đúng Knowledge Base (Business Context 12 fields + Content + LLM) của dự án/Use Case tương ứng để dẫn dắt và giải quyết JTBD. Không cấu hình kịch bản thủ công.
2. **Intent-First:** Cung cấp sẵn các Quick Replies thay đổi linh hoạt theo trang người dùng đang xem để họ chạm là ra kết quả (Không bắt ép phải gõ phím).
3. **Conversion-Driven:** Mọi tương tác của chatbot đều hướng đến việc điều hướng người dùng mở App (OneLink) để hoàn tất luồng (Ví dụ: "Mở Ví Trả Sau", "Nộp Phạt Ngay", "Thanh toán ngay").
4. **MoSpark Qwen & RAG Engine:** Vận hành trực tiếp trên mô hình Qwen nội bộ kết hợp với cơ sở dữ liệu vector RAG Knowledge Base. Toàn bộ dữ liệu sản phẩm, biểu phí và hướng dẫn được vector hóa bằng Qwen Embedding trên hạ tầng MoSpark, giúp Chatbot phản hồi tức thì với chi phí 0 đồng và bảo mật tuyệt đối dữ liệu nội bộ.

---

## 2. Nhu Cầu Người Dùng & JTBD (Jobs-To-Be-Done)

Chatbot được thiết kế để giải quyết các nhu cầu (JTBD) phổ biến nhất khi người dùng duyệt website. Dưới đây là ví dụ minh họa cơ chế:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhu cầu (Intent)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lựa chọn (Quick Reply)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hành động của Chatbot (Từ Knowledge Base)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Call-to-Action (CTA) kỳ vọng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tìm hiểu USP/Tính năng nổi bật</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Sản phẩm này có gì đặc biệt?</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trích xuất USPs từ Business Context.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xem chi tiết trên App</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Kiểm tra điều kiện tham gia</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Tôi có đủ điều kiện không?</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đối chiếu điều kiện từ nội dung YMYL/Disclaimer.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mở App / Xác thực</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hỗ trợ thực hiện tác vụ/JTBD</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Hướng dẫn cách làm</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hướng dẫn từng bước dựa trên bài Blog/How-to.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thực hiện ngay trên App</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tra cứu thông tin Merchant (O2O)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Quán này có nhận Ví Trả Sau không? Giờ mở cửa?</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Truy xuất từ Structured Custom Fields (Địa chỉ, Giờ, Payment) của trang Đối tác.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thanh toán / Kích hoạt Ví Trả Sau</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hỏi đáp thông tin cụ thể</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>[Câu hỏi cụ thể]</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LLM truy vấn Knowledge Base để trả lời chính xác.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mở dịch vụ tương ứng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tóm tắt nhanh toàn bộ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Tóm tắt thông tin</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gom ý chính thành 3-4 bullet points.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuyển đổi / Mở App</td>
    </tr>
  </tbody>
</table>

---

## 3. Kiến Trúc Luồng Identity & Web-to-App Tracking

Đây là tính năng bắt buộc để chứng minh ROI của Chatbot (Đóng góp vào M11 - Revenue Attribution Pipeline của MoSpark). Mục tiêu: Liên kết toàn trình từ *Web Anonymous User → Chatbot Interaction → OneLink Click → App Conversion*.

### 3.1. Luồng xử lý kỹ thuật (5 Tầng)

1. **Tầng 1 - User Identification Request:**
   - Khi người dùng truy cập bất kỳ trang nào trên momo.vn, Edge Middleware đọc HttpOnly Cookie.
2. **Tầng 2 - Identity Generation:**
   - Đã login Web: Sử dụng `hashed_uid` từ cookie.
   - Chưa login (Anonymous): Gọi hàm `generateAnonId()`.
   - Kết xuất ra một `Identity Object { identityId, userType }` chuẩn hóa.
3. **Tầng 3 - Analytics Tracking:**
   - Init Chatbot Session: Push `identity_init` lên DataLayer (GTM ➔ GA4) và gọi `umami.identify(identityId)`.
   - Track các event: `chatbot_opened`, `quick_reply_clicked`, `question_asked`.
4. **Tầng 4 - CTA Distribution (Crucial Step):**
   - Mọi Onelink được Chatbot sinh ra hoặc hiển thị trên khung chat **phải được tự động gắn tham số `wui`**.
   - Định dạng: `https://onelink.momo.vn/.../?wui=<identityId>&ref=web_chatbot`
5. **Tầng 5 - App Attribution:**
   - Khi mở App qua OneLink, App MoMo tiếp nhận `wui` và map với `IdentityId`.
   - Data pipeline (Appsflyer + BigQuery) sẽ khâu nối: Hành vi hỏi Chatbot trên Web ➔ Giao dịch/thanh toán trên App.

---

## 4. Giao Diện (UI/UX) & Placement

- **Format:** Nút Floating (Balloon) ở góc phải dưới toàn màn hình website, có notification badge để thu hút sự chú ý.
- **Trải nghiệm:** Bấm vào mở dạng Bottom Sheet (Mobile) hoặc Slide-out Panel (Desktop).
- **Thiết kế mặc định:** Khi mở ra, hiển thị ngay 5 nút bấm Quick Replies (tương ứng với các JTBD của Use Case đó) thay vì bắt người dùng gõ câu hỏi.

---

## 5. Quy Trình Vận Hành (Content & Quality Governance)

Đảm bảo tuân thủ chuẩn MoSpark (Layer 3 - Quality Gate):

1. **Nguồn dữ liệu (Dynamic Knowledge Base):** Chatbot tự động nội suy câu trả lời từ kho dữ liệu tương ứng với trang web hiện tại:
   - **Đối với bài viết/Blog/Use Case chung:** Lấy từ trường thông tin `Business Context` (12 fields) và nội dung Content dài đang thuộc về Use Case đó.
   - **Đối với trang Merchant (Đối tác):** Chatbot ưu tiên đọc dữ liệu tĩnh được bóc tách tự động từ luồng GenAI Single-Pass của MoSpark (Structured Custom Fields bao gồm `merchant_address`, `price_range`, `operating_hours`, `amenities_services`, `payment_policy`) thông qua Webhook API. Cơ chế cấu trúc hóa này giúp tối ưu token (RAG) và chống hallucination (bịa thông tin).
   - **Tích hợp Qwen RAG & Hybrid Retrieval:** Chatbot kết nối trực tiếp với RAG Knowledge Base đã được vector hóa bởi mô hình Qwen nội bộ trên MoSpark. Khi người dùng đặt câu hỏi, hệ thống tự động lọc metadata theo URL hiện hành (Contextual Pre-filtering) kết hợp tìm kiếm kết hợp (Hybrid Search: Vector Qwen + Keyword BM25) để trích xuất các đoạn thông tin chuẩn xác nhất trước khi gửi tới Qwen LLM sinh câu trả lời.
2. **Anti-Hallucination:** System Prompt của LLM bắt buộc chứa rule: *"Chỉ trả lời dựa trên Knowledge Base được cung cấp của trang hiện hành. Nếu thông tin không có, trả lời 'Hiện tại chưa có thông tin này' thay vì bịa ra."*
3. **Quality Gate:** Trang web hiện tại phải đạt điểm SEO/GEO Scoring >= 60 mới được kích hoạt tính năng trả lời tự động bằng AI (vì nội dung gốc rác thì AI trả lời cũng rác).

---

## 5.5. Kế hoạch Nâng cấp Tính năng H2/2026

Trong H2/2026, hệ thống Chatbot sẽ được nâng cấp các năng lực thông minh và kịch bản tương tác chuyên sâu sau:

1. **Qualitative Data Ingestion Pipeline (Meeting Notes RAG):** Thiết lập pipeline tự động thu thập, phân tích ngữ nghĩa và vector hóa dữ liệu định tính (Qualitative Data) từ các tài liệu ghi chú khảo sát khách hàng (2H Customer Meeting Notes dưới dạng Markdown) để nạp vào cơ sở dữ liệu tri thức của RAG, giúp Chatbot tư vấn sâu sát và thực tế hơn.
2. **Scenario Mapping Engine (Typebot v2):** Phát triển engine kéo thả kịch bản hội thoại thông minh tự động, hỗ trợ phân nhánh sâu và cá nhân hóa câu trả lời theo hành vi nhập liệu của user đối với các Use Case tài chính/bảo hiểm phức tạp.

---

## 6. Measurement-First: Hypothesis & KPIs

### 6.1. AB Test Hypothesis
- **Hypothesis:** "Việc đặt Chatbot (có khả năng nhận diện ngữ cảnh trang + Onelink tracking `wui`) trên toàn website sẽ làm tăng tỷ lệ Click-to-App (W2A CR) lên ít nhất 15% so với việc chỉ để người dùng tự duyệt web."
- **Variant A (Baseline):** Website chuẩn, không có Chatbot.
- **Variant B:** Website + Floating Chatbot Widget (mospark_chatbot).

### 6.2. Metrics Tracked (Umami & Appsflyer)
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định nghĩa</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Chatbot Interaction Rate</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% Session có click mở chatbot</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">> 20% traffic trang</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Quick Reply Usage</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% Session mở chatbot có bấm vào ít nhất 1 Quick Reply</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">> 60% (chứng minh tính hữu dụng)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>W2A Chatbot CTR</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lượt click OneLink trong Chatbot / Tổng số session mở Chatbot</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">> 10%</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>End-to-End Conversion</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">App Install / App Open thành công mang theo <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">wui</code> từ Chatbot</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đo lường baseline sau 1 tháng</td>
    </tr>
  </tbody>
</table>

---
*Tài liệu này được lập theo chuẩn quy trình Spec của MoSpark Platform. Web Platform team sẽ dựa vào mục 3 và 6 để tiến hành setup schema trước khi build UI.*
