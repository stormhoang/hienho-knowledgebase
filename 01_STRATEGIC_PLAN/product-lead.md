# Web Product Lead - Strategic & OKRs H2 2026

> - **Tài liệu:** Web Product Lead - Strategic & OKRs H2 2026
> - **Khối phụ trách:** Growth Platform Division (GPD)
> - **Đơn vị:** Web Platform
> - **Nhóm:** Out-App Traffic Team
> - **Vai trò:** Web Product Lead
> - **Owner:** Văn Hiến
> - **Quản lý trực tiếp:** Head of Web Platform
> - **Phiên bản:** 1.1 · July 2026
> - **Trạng thái:** Active
> - **Cập nhật:** 2026-07-13

---

## I. STRATEGIC CONTEXT

### 1.1. Bối cảnh Thị trường & Thách thức GEO (AI Search)
*   **Sự dịch chuyển của Search:** Hành vi tìm kiếm đang thay đổi nhanh chóng khi lượng tìm kiếm trên Google giảm ~20% YoY (2025), trong khi ChatGPT đạt 700M người dùng hàng tuần và Perplexity đạt 780M truy vấn/tháng. AI Overviews (SGE) hiện xuất hiện trên 13-30% truy vấn, đặc biệt là nhóm tài chính/fintech.
*   **Thực trạng của MoMo:** Bước đầu ghi nhận tín hiệu GEO tích cực với hơn **660 citations** và lượng traffic thực tế từ ChatGPT nhờ triển khai pilot `llms.txt` trên dự án Phạt Nguội. Tuy nhiên, tỉ lệ trích dẫn tổng thể trên toàn domain vẫn ở mức sơ khởi. Trước xu thế dịch chuyển mạnh mẽ của người dùng sang các công cụ AI Search và Chatbot thế hệ mới, MoMo cần nhanh chóng hoàn thiện và scale up hạ tầng GEO (`llms.txt` & AI-native content pipeline) để chủ động đón đầu và chiếm lĩnh lưu lượng truy cập từ kênh tìm kiếm thế hệ mới này.
*   **Vấn đề cốt lõi:** Kênh Web momo.vn chưa thể tự chủ tăng trưởng khi PM/PO phụ thuộc hoàn toàn vào Dev để phát triển trang mới, nội dung do AI sinh ra chưa có bộ lọc kiểm soát tự động, và chưa có hệ thống đo lường thị phần tìm kiếm (Share of Voice).
*   **Sự tiến hóa từ Product-Led SEO sang Agent-Led Search:** Không còn chỉ dừng lại ở việc xếp hạng (ranking) trang web trên các SERPs truyền thống. Mục tiêu chiến lược của Web Product Lead là biến momo.vn thành một **nguồn dữ liệu đáng tin cậy (Trusted Data Source)** để các AI Agents (Gemini, GPT, Perplexity) cào, trích xuất, tin dùng và trích dẫn (cite). Sự tiến hóa này đòi hỏi 4 yếu tố quyết định: (1) Brand authority mạnh (E-E-A-T cao, định danh entity rõ ràng), (2) Cấu trúc dữ liệu tốt (Schema markup chuyên sâu), (3) Nội dung giải quyết sâu sắc JTBD (Jobs-to-be-Done), chính xác (factual) và dễ parse bởi AI, (4) Độ tươi mới (data freshness) và độ chính xác của thông tin ở mức cao nhất.

### 1.2. Thực trạng H1/2026 & Định hướng Hành động H2/2026
*   **Thực trạng H1/2026 (Nền tảng đã hoàn thành):**
    *   *Traffic & Conversion:* Mang lại 5.9M click tự nhiên. Phễu chuyển đổi Ads Website (New to MoMo) đạt kết quả thực tế 36.8K Installs ➔ 7K MAU.
    *   *Công cụ PLG:* Rollout giai đoạn 1 Use Case Phạt Nguội (tích hợp API kiểm tra vi phạm), CIC Simulator widget và hoàn tất thiết kế wireframe các công cụ giả lập tài chính Finhub. Hoàn thành thử nghiệm Local SEO cho 39 đối tác (Merchant).
    *   *Hạ tầng & Chất lượng:* Vận hành hệ thống MoSpark CMS; loại bỏ hơn 3.670 URL rác để tối ưu Crawl Budget; hoàn thành tích hợp Identity Platform (Edge Cookie) để định danh và đo lường hành vi người dùng ẩn danh từ Web vào App.
*   **Định hướng Hành động H2/2026 (Mục tiêu thực thi):**
    *   *Tự động hóa & Kiểm soát nội dung:* Vận hành quy trình sinh nội dung tự động end-to-end trên MoSpark, áp dụng bộ lọc SEO/GEO Scoring Gate (yêu cầu đạt ≥ 80 điểm) trước khi xuất bản nhằm kiểm soát rủi ro thông tin YMYL tài chính.
    *   *Triển khai công cụ PLG:* Phát hành chính thức các công cụ giả lập tài chính Finhub; tự động hóa tạo trang Local SEO quy mô lớn cho các Merchant (Ví Trả Sau); tối ưu hóa tỉ lệ chuyển đổi Web-to-App.
    *   *Hỗ trợ Cell Teams tự vận hành:* Ban hành tài liệu hướng dẫn (Platform Guidelines) và thực thi kiểm duyệt qua cổng Publish Gate để Cell Teams tự triển khai Mini Web đúng quy chuẩn kỹ thuật mà không cần Dev Web Platform hỗ trợ trực tiếp.
    *   *Bảo mật & Quản trị domain:* Rà soát hiệu quả cào dữ liệu của Googlebot, kiểm soát cấu trúc sơ đồ lập chỉ mục tối ưu cho AI bots (AI Crawler Policy) và rà quét disavow các backlink spam để duy trì độ tin cậy tên miền (Domain Authority).

### 1.3. 3 Vai trò Chiến lược (Mandate Chiến lược) của Website momo.vn
Website momo.vn không còn là corporate site hay blog SEO đơn thuần. MoSpark được xây dựng để hiện thực hóa 3 vai trò chiến lược dưới sự quản trị của Web Product Lead:
1.  **Financial & Payment Authority:** Xây dựng momo.vn thành website tin cậy và có độ phủ thông tin hàng đầu trong ngành tài chính và thanh toán tại Việt Nam thông qua kiểm duyệt chất lượng nghiêm ngặt (Quality Gate, Named Author Policy và tiêu chuẩn YMYL).
2.  **Website Growth Traffic & MAU:** Thúc đẩy lưu lượng truy cập tự nhiên (Organic Traffic) ngoài App và tối ưu hóa phễu chuyển đổi Web-to-App nhằm gia tăng người dùng mới (New User/MAU) cho MoMo.
3.  **Product-Led Growth theo JTBD:** Phát triển các công cụ tiện ích tương tác (Calculators/Simulators) giải quyết trực tiếp nhu cầu tìm kiếm thực tế (Jobs-to-be-Done) của người dùng trên Web, làm động lực tăng trưởng tự nhiên dựa trên giá trị sử dụng của sản phẩm Web.

### 1.4. Nguyên tắc cốt lõi: Product-Led Growth (PLG)
*   **Product-Led Growth (PLG):** Tăng trưởng kênh Web dựa trên giá trị sử dụng thực tế của sản phẩm Web. Các công cụ tương tác và tiện ích (Calculator, Simulator, Checker) giải quyết trực tiếp nhu cầu (JTBD) của người dùng ngay trên Web. Nội dung bài viết đóng vai trò hỗ trợ khả năng hiển thị (discoverability) và cung cấp thông tin. Trải nghiệm sản phẩm hữu ích sẽ chuyển đổi người dùng sang App (New User/MAU) qua các luồng liên kết tối ưu (Smart CTA, truyền dữ liệu pre-fill), thay vì sử dụng các phương thức quảng cáo đại trà hoặc xuất bản nội dung không có giá trị (thin content).
*   **Quy tắc bất biến:** Mỗi Use Case mới trên Web phải phát triển tối thiểu một công cụ tiện ích (Utility tool) tương ứng và tuân thủ phễu chuyển đổi PLG:
    ```
    Content → Keywords → Ranking → Use Case → User Journey → App/Transaction (New User / MAU)
    ```

---

## II. VISION & STRATEGIC FRAMEWORK

### 2.1. Web Platform Vision
> **Scale MoMo to Vietnam's #1 financial destination with 6M monthly visitors via an Agentic, SEO/GEO-first platform that turns underserved market needs into high-authority traffic.**

### 2.2. Strategic Framework - 3 Value Layers (Khung Chiến lược - 3 Lớp Giá trị)
Chiến lược Web được tổ chức theo 3 lớp mục tiêu nhằm chuyển đổi lưu lượng truy cập từ ngoài App vào App:
*   **Layer 1 - MoMo (Brand & Authority Governance):** Bảo vệ và gia tăng độ tin cậy tên miền (Domain Authority) của momo.vn:
    *   *Content Authority:* Sở hữu các Use Cases chiến lược thuộc thị trường chưa được khai thác tốt ngoài App (Phạt Nguội, Bảo hiểm ô tô, eSIM du lịch, Cinema) để MoMo chiếm thứ hạng cao trên các công cụ tìm kiếm.
    *   *AI-powered (GEO):* Định dạng cấu trúc dữ liệu chuẩn semantic để các công cụ tìm kiếm AI trích dẫn nội dung MoMo làm nguồn tham chiếu.
    *   *Kết quả:* Chuyển hóa thị trường tiềm năng ngoài App (Phạt Nguội, Bảo hiểm ô tô, eSIM du lịch, Cinema...) thành traffic chất lượng có tỷ lệ chuyển đổi cao.
*   **Layer 2 - User (Product-Led Growth - PLG):** Giải quyết nhu cầu tìm kiếm thông tin và công cụ của người dùng:
    *   *Mọi sản phẩm Web đi theo tinh thần PLG:* Định hướng tất cả các sản phẩm xây dựng trên Website momo.vn đều bám sát triết lý tăng trưởng dẫn dắt bởi sản phẩm, tập trung phát triển các tiện ích tương tác với trọng tâm là các công cụ tiện ích tài chính (Financial Utilities) nói riêng và các giải pháp PLG nói chung (như các công cụ tài chính Finhub, CIC Simulator, Phạt Nguội Checker).
    *   *Kết quả:* Người dùng giải quyết được nhu cầu ngay trên Web, tạo trải nghiệm tích cực và thúc đẩy chuyển đổi tự nhiên vào App (New User/MAU) qua Smart CTA và truyền dữ liệu pre-fill.
*   **Layer 3 - Cell Team (Platform-as-a-Service - PaaS):** Hỗ trợ các Cell Teams tiếp cận thị trường ngoài App:
    *   *Mô hình PaaS:* Cung cấp giải pháp kỹ thuật, quy trình xuất bản, nền tảng (MoSpark, SPA Framework, boilerplate mẫu, hướng dẫn kỹ thuật SEO/GEO) và kiểm soát chất lượng qua Quality Gate.
    *   *Kết quả:* Các Cell Teams làm chủ công cụ, chủ động quản trị nội dung của Cell Team, đảm bảo Website được tối ưu hóa chuẩn SEO/GEO và đo lường chính xác hiệu suất của các hoạt động truyền thông.

### 2.3. 4 Growth Pillars (Kiến trúc Thị trường)
momo.vn không tổ chức theo BU mà theo Product/Search Ecosystem. 4 Pillars đại diện cho 4 growth engine độc lập sở hữu các vertical thị trường dưới sự kiểm duyệt kỹ thuật của Web Product Lead:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pillar</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Use Cases tiêu biểu</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chiến lược Content</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ràng buộc quản trị (Hiến sở hữu & audit)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trụ cột 1 - Tài chính & Tín dụng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CIC Score, Ví Trả Sau, Vay Nhanh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub-Spoke kết hợp các Interactive Tools (Tính lãi, Mô phỏng CIC)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Named Author Policy</strong> - Gate kiểm duyệt cứng bắt buộc trước khi launch</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trụ cột 2 - Bảo hiểm Công nghệ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo hiểm xe máy, BHYT, BHXH, Bảo hiểm ô tô</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Neutral Aggregator - Cổng so sánh trung lập</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Không dùng geo-based URL</strong> cho bảo hiểm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trụ cột 3 - Dịch vụ Công & Tiện ích</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phạt Nguội, Thanh toán Hóa đơn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">API real-time kết hợp programmatic SEO (pSEO) cho 63 tỉnh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>GEO Optimization ready</strong> trước khi rollout</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trụ cột 4 - Đời sống & Merchant</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cinema, OTA, eSIM, Merchant</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Intent-first, trang chi tiết Merchant (Merchant Detail Page)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Noindex mandatory</strong> cho các URL hết hạn</td>
    </tr>
  </tbody>
</table>
---

## III. OKRS H2/2026 - WEB PRODUCT LEAD

### Objective 1: Xây dựng giải pháp tăng trưởng và thúc đẩy mục tiêu tăng trưởng Web Traffic và MAU
*Focus: Traffic acquisition, conversion optimization, and simulation hooks.*

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KR</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chỉ số cốt lõi</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tiêu chuẩn hoàn thành (H2/2026 Target)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò của Hiến (Web Product Lead)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 1.1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Platform Projects (Own Use Cases)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đạt <strong>Top 3 Ranking</strong> cho nhóm từ khóa Phạt Nguội; scale-up Local SEO cho <strong>500 Merchant Pages</strong> (phát triển Merchant Detail và Merchant Listing định hướng Location Page giải quyết JTBD từ PLG Project).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quản lý vòng đời sản phẩm Phạt Nguội (API realtime, cảnh báo vi phạm) và scale-up Local SEO cho hệ thống Merchant.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 1.2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cell Team Growth Projects</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Các dự án Cell Team (Vehicle Hub, Cinema, eSIM, Bảo hiểm Ô tô) - trừ các dự án Media Team tham gia - đóng góp <strong>3.0M PageViews/tháng</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hỗ trợ cấu trúc kỹ thuật web, pSEO và tracking cho các Cell Teams để đảm bảo ROI tăng trưởng.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 1.3</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Overall Web-to-App Funnel</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tối ưu phễu Web-to-App và scale-up traffic hướng tới mục tiêu đột phá đạt <strong>1.0M MAU/tháng</strong> vào cuối H2/2026 (lũy kế H2 đạt <strong>>4.0M MAU</strong>), đạt tỷ lệ chuyển đổi trung bình <strong>>10%</strong> (hướng tới target <strong>12.5%</strong>).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chịu trách nhiệm tối ưu phễu chuyển đổi W2A và hạ tầng tracking của Web Platform.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 1.4</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>User Growth Contribution</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phối hợp cùng User Growth triển khai dự án Ads Website đóng góp <strong>>20K New Users</strong> (REG) và <strong>>14K New User MAU</strong> thực tế.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phối hợp kỹ thuật cùng User Growth tối ưu cơ chế Smart CTA, Universal Links.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 1.5</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Financial Authority (Finhub)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hướng tới mục tiêu xây dựng toàn bộ hệ thống Utilities Tools về Finance tại MoMo thông qua việc phát hành thành công bộ <strong>10 công cụ giả lập tài chính Finhub</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thiết lập logic toán học, kịch bản JTBD và thiết kế wireframe cho các công cụ giả lập để làm phễu organic traffic.</td>
    </tr>
  </tbody>
</table>

---

### Objective 2: Xây dựng và phát triển MoSpark trở thành nền tảng AI-Powered trong hoạt động GenAI Content
*Focus: AI-powered scale, automation flow, content quality gate, and merchant data enrichment.*

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KR</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chỉ số cốt lõi</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tiêu chuẩn hoàn thành (H2/2026 Target)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò của Hiến (Web Product Lead)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 2.1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>PLG Project</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vận hành nền tảng quản trị <strong>Topic Cluster</strong>; ứng dụng GenAI để sản xuất nội dung theo <strong>Content Plan</strong> nhằm phục vụ mục tiêu tăng trưởng <strong>Ranking & Traffic (PageViews)</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quản trị cấu trúc hệ thống, thiết lập content plan theo JTBD và trực tiếp giám sát chất lượng sản xuất/chỉ số traffic.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 2.2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>GenAI Content</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Áp dụng các Model AI để sản xuất đa dạng định dạng nội dung, cắt giảm tối đa thời gian sản xuất, đảm bảo chuẩn business context và luôn tối ưu chi phí token.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thiết lập framework prompt chuẩn hóa business context, tham gia đánh giá chất lượng đầu ra của Model AI và tối ưu chi phí token.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 2.3</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Merchant-Led Growth</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xây dựng chiến lược tăng trưởng thông qua các trang <strong>Location Listing (Merchant Listing)</strong> giải quyết JTBD từ <strong>PLG Project</strong> cho <strong>500 Merchant Pages</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thiết kế cấu trúc các trang Location Listing trên MoSpark CMS để tối ưu Local SEO.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 2.4</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Ads Manager & Utilities Tool</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khai thác quảng cáo và điều phối hiển thị Dynamic placement banner tự động theo ngữ cảnh; phát triển các công cụ tiện ích/widget tra cứu (Calculator, Simulator tính lãi suất/trả góp, và tiện ích theo dõi Giá Vàng) làm phễu gián tiếp dẫn lưu lượng về các dịch vụ tài chính (Tiết kiệm, Đầu tư).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tham gia tư vấn, điều phối inventory quảng cáo và phối hợp phát triển các công cụ tiện ích (Utilities).</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 2.5</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Content Quality Gate</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đảm bảo <strong>100% nội dung AI sinh ra đạt điểm số chất lượng ≥ 80 điểm</strong> (không lỗi Core Web Vitals, không trùng lặp/lỗi SEO).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quản trị bộ quy tắc chấm điểm (5 blocks) và cơ chế Hard-Block ngăn chặn xuất bản nội dung lỗi trên CMS.</td>
    </tr>
  </tbody>
</table>

---

### Objective 3: Thiết lập quy chuẩn vận hành, quản trị an toàn thông tin & sức khỏe tên miền (Technical & Content Governance)
*Focus: Quality gates, publish approvals, domain health, crawl budget optimization, and Agent-led search infrastructure.*

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KR</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chỉ số cốt lõi</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tiêu chuẩn hoàn thành (H2/2026 Target)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò của Hiến (Web Product Lead)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 3.1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Platform Guidelines</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ban hành đầy đủ tài liệu quy chuẩn kỹ thuật (SEO/GEO standard, tracking rule) cho các Cell Teams.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quản trị, cập nhật và đào tạo SOP, Playbook giúp Cell Teams tự vận hành sản phẩm Web đúng chuẩn.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 3.2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Quality Gate (Publish Approval)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phê duyệt kỹ thuật & nội dung nghiêm ngặt <strong>100% dự án Web mới trước khi Go-live</strong>, đáp ứng chuẩn Agent-Led Search.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thực thi cổng duyệt Publish Gate, trực tiếp sign-off kỹ thuật (Schema markup, E-E-A-T entity, Named Author policy).</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 3.3</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Domain & Backlink Security</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rà quét định kỳ, kiểm soát và <strong>ngăn chặn triệt để các nguồn backlink xấu</strong> (spam links) để bảo vệ Domain Authority.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chịu trách nhiệm bảo vệ sức khỏe link profile của tên miền momo.vn, thực hiện disavow spam links định kỳ.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 3.4</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>URL Governance & Crawl Budget</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rà soát định kỳ loại bỏ nội dung cũ lỗi thời để duy trì độ tươi mới (<strong>Data Freshness</strong>) và xử lý dứt điểm URL rác.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loại bỏ crawl waste (chặn query parameter rác), tối ưu ngân sách cào dữ liệu của Googlebot và các AI Search crawlers.</td>
    </tr>
  </tbody>
</table>

---

### Objective 4: Tư vấn giải pháp tăng trưởng và thúc đẩy năng lực triển khai cho các chiến dịch & Cell Teams (Growth Advisory & Enablement)
*Focus: Growth consulting, conversion flow design, campaign support, and SPA framework enablement.*

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KR</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chỉ số cốt lõi</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tiêu chuẩn hoàn thành (H2/2026 Target)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò của Hiến (Web Product Lead)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 4.1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Conversion Performance Support</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hỗ trợ Cell Teams giám sát chỉ số Web Performance (Core Web Vitals), <strong>ngăn chặn các lỗi nghiêm trọng làm suy giảm CTR/CR</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giám sát sức khỏe trang đích của đối tác nội bộ, gửi technical request tối ưu hiệu suất sang Web Platform.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 4.2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Growth Advisory & W2A Flow</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tư vấn thiết kế sitemap, cấu trúc cluster và luồng chuyển đổi W2A cho các dự án Media Team phụ trách: <strong>Ví Trả Sau, Vay Nhanh, Destination Promotion Hub (MoMo Travel)</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đảm bảo cấu trúc thông tin chuẩn và tích hợp tối ưu CTA/deep-link để thúc đẩy chuyển đổi người dùng sang App.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 4.3</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Campaign & Insurance Support</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đồng hành cố vấn giải pháp kỹ thuật, cấu trúc SEO và tối ưu chuyển đổi cho các chiến dịch/dự án do Media Team làm Owner: <strong>Bảo hiểm Y tế (BHYT), Bảo hiểm xe máy (BHXM)</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PM kỹ thuật hỗ trợ Media Team, đảm bảo hạ tầng web, disavow spam links và tối ưu hóa onpage/offpage cho các dự án bảo hiểm.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>KR 4.4</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Growth Framework (SPA)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thẩm định tính khả thi (Feasibility) và tư vấn tăng trưởng cho các dự án mới của Cell Teams theo quy trình <strong>SPA</strong>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tư vấn hướng tiếp cận pSEO, cấu trúc SEO Inventory và kịch bản JTBD giúp Cell Teams tự triển khai Mini Web đúng hướng.</td>
    </tr>
  </tbody>
</table>

---

## IV. STRATEGIC ACTIONS & KEY METHODOLOGY FOR H2/2026

1.  **Vận hành Quy chuẩn YMYL & Named Author Policy:**
    *   Enforce quy chuẩn Named Author Policy bắt buộc cho các bài viết thuộc Pillar 1 (Tài chính & Tín dụng) nhằm vượt qua thuật toán đánh giá chất lượng khắt khe của Google và AI Search.
2.  **Đồng bộ Hóa Use Case ID qua Hệ thống Platform:**
    *   Áp dụng Use Case ID làm định danh gốc để liên kết toàn bộ dữ liệu Content, Ads và Analytics, xóa bỏ các Silo của hệ thống cũ.
3.  **Triển khai Thử nghiệm và Tối ưu hóa GEO (AI Citation):**
    *   Áp dụng chính sách quản lý AI Crawler (AI Crawler Policy) nâng cao nhằm kiểm soát ngân sách cào dữ liệu của AI Bots, hướng tới tối đa hóa citation rate của MoMo trong Google AI Overviews, ChatGPT và Perplexity.
4.  **Enforce Tiêu chuẩn Quality Gate trên MoSpark CMS:**
    *   Sử dụng công thức chấm điểm 5-Block (100 điểm) trực tiếp trên CMS MoSpark. Thực thi hard block đối với các lỗi Core Web Vitals và kỹ thuật SEO nghiêm trọng trước khi xuất bản.
5.  **Duy trì Vòng lặp Test SPA (reSearch - Pilot - Action):**
    *   Bảo đảm mọi giải pháp và tính năng mới đều đi qua chu trình nghiên cứu chuyên sâu (Feasibility & Demand), thử nghiệm thực tế (Pilot), và sau đó mới scale-up trên diện rộng.
6.  **Chuẩn bị cho Sự tiến hóa Agent-Led Search:**
    *   Tối ưu hóa momo.vn thành "Trusted Data Source" cho AI Agents thông qua việc tăng cường Brand Authority (xây dựng Entity, nâng cao E-E-A-T), chuẩn hóa Schema markup chuyên sâu, và cấu trúc nội dung giải quyết triệt để bài toán JTBD của người dùng với độ chính xác cao và thông tin luôn cập nhật (freshness).

---

*Tài liệu được biên soạn và bảo trì bởi **Văn Hiến - Web Product Lead**.*
