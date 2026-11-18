> - **Project:** S-P-A Framework (Quy trình Hợp tác & Tăng trưởng Use Case)
> - **Main URL:** N/A (Internal Framework)
> - **Division:** GPD - Web Platform
> - **Owner:** Web Platform Team
> - **Governance:** Head of Web Platform & Web Product Lead
> - **Version:** 2.0 · Tháng 07/2026
> - **Status:** Chính thức ban hành
> - **Business Model:** Platform-as-a-Service (PaaS) nội bộ

> **Problem:** Các Cell Team muốn thu hút user mới từ kênh Search tự nhiên nhưng thiếu quy trình chuẩn, dẫn đến việc xây dựng Web manh mún, không đạt chuẩn SEO/GEO và không đo lường được hiệu quả Web-to-App (W2A).
> **KPI Owned:** W2A Conversion Rate, Số lượng Use Case Onboard → attributed via Appsflyer, Umami
> **Conversion Flow:** Cell Team Request → reSearch (S) → Pilot (P) → Action (A) → Live Web Product → User Search → App open

---

### 1. Executive Summary

**Situation:** Các Cell Teams (Ví Trả Sau, Bảo Hiểm, Dịch Vụ Công...) ngày càng có nhu cầu mạnh mẽ trong việc đẩy mạnh thu hút người dùng mới (New Users) và tăng tương tác (MAU/MEU) thông qua các kênh tìm kiếm tự nhiên (Google Search, AI Search).

**Complication:** Việc Cell Team tự phát triển Web hoặc làm việc với Web Platform theo kiểu "nhờ dev code giúp" mang lại nhiều rủi ro: chất lượng nội dung không đạt chuẩn E-E-A-T, SEO/GEO kém, thiếu trải nghiệm UX/UI nhất quán và tiêu tốn nhiều nguồn lực. Web Platform trước đây chỉ đóng vai trò hỗ trợ kỹ thuật thụ động, chưa cung cấp được một "playbook" trọn gói để scale up hiệu quả và kiểm soát chất lượng ở quy mô lớn.

**Resolution:** Web Platform ban hành **S-P-A Framework (reSearch - Pilot - Action)**, chính thức chuyển đổi vai trò thành Nhà cung cấp Dịch vụ Sản phẩm (Product Service Provider - PaaS). Framework cung cấp gói giải pháp tăng trưởng 3 giai đoạn kèm các chốt kiểm duyệt (Stage Gates) nghiêm ngặt, giúp chuẩn hoá và tối ưu hoá việc đưa bất kỳ Use Case nào lên Web với cam kết mang lại W2A CR > 5%.

---

### 2. Bối Cảnh Thị Trường (Internal Context)

- **Hiện trạng vận hành:** Thiếu một quy chuẩn chung giữa GPD và các Cell Team. Yêu cầu làm Web thường là các task rời rạc, dẫn đến lãng phí tài nguyên và tạo ra các "Orphan Pages" hoặc "Zero-Traffic URLs".
- **Nhu cầu nội bộ (Market Demand):** Cell Team cần traffic và conversion, nhưng không có chuyên môn về SEO/GEO và hệ thống GenAI pipeline.
- **Định vị mới của Web Platform:** Chuyển từ "Dev Support" sang "Growth Partner".

---

### 3. Định Hướng Dự Án (Product Job Cốt Lõi)

**3.1 Product Job Cốt Lõi**
- "Cell Team có nhu cầu tăng trưởng ngoài App - gửi yêu cầu theo chuẩn - nhận được gói giải pháp (Discovery/Pilot/Growth) từ Web Platform - triển khai Mini Web/Widget đạt chuẩn và thu về W2A conversion thực tế."

*N outcomes phát sinh:*
- Tiêu chuẩn hoá toàn bộ tài sản Web của MoMo.
- Tối ưu hoá chi phí sản xuất (Sử dụng chung GenAI Pipeline và SEO Inventory).

**3.2 Dự Án Này KHÔNG Phải**
- KHÔNG phải là luồng yêu cầu hỗ trợ IT Helpdesk thông thường (sửa text, đổi ảnh nhỏ lẻ).
- KHÔNG áp dụng cho các landing page chiến dịch ngắn hạn (dưới 1 tháng) không có mục tiêu SEO/GEO (các page này dùng LP Builder M1).
- KHÔNG chạy các dự án nằm ngoài tên miền `momo.vn`.

**3.3 Pre-conditions Gate**
Thiếu 1 trong các điều kiện sau - dừng lại không chuyển giai đoạn:

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">File Business Context (12 fields) phải được điền đầy đủ và duyệt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bắt buộc trước Gate 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell Team PO</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PC2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PO Cell Team ký cam kết dành tối thiểu 2 giờ/tuần duyệt content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bắt buộc trước Gate 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell Team PO</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PC3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ngân sách chạy Off-page/Vendor phải được phê duyệt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bắt buộc trước Gate 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell Team Head</td>
    </tr>
  </tbody>
</table>

---

### 4. JTBD Analysis (Dành cho Internal Users - Cell Teams)

#### Job #1: Đánh giá cơ hội thị trường (reSearch - Discovery)
> "Tôi muốn biết dịch vụ của tôi có tiềm năng trên Web không trước khi đổ tiền và dev vào làm."

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell Team cần biết Search Volume, Market Cap và dự báo W2A của Use Case.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tự tin đưa ra quyết định đầu tư, không sợ lãng phí nguồn lực.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chứng minh được với Management rằng đây là kênh acquisition tiềm năng.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khi có mục tiêu tăng trưởng OKR mới nhưng kênh In-app đã bão hòa.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giải pháp Flow</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Điền Requirement Form → Nhận SEO/GEO Proposal Deck & Keyword Map (Miễn phí).</td>
    </tr>
  </tbody>
</table>

#### Job #2: Thử nghiệm an toàn (Pilot - Plan)
> "Tôi muốn chạy thử một bản MVP nhanh nhất có thể để chứng minh W2A CR có đạt như kỳ vọng không."

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần một Mini Web/Widget có tracking đầy đủ (Appsflyer, Umami) lên live trong thời gian ngắn.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">An tâm vì rủi ro thấp, chỉ cần bỏ ra thời gian review, chưa tốn tiền chạy ads/vendor.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cầm số liệu thực tế (Baseline) đi xin ngân sách mở rộng dễ dàng hơn.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khi Gate 1 pass và Proposal Deck được thông qua.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giải pháp Flow</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform build MVP → GenAI 10-15 bài → Live & Track W2A.</td>
    </tr>
  </tbody>
</table>

---

### 5. Kiến Trúc & Phạm Vi Build (S-P-A Flow)

Framework S-P-A hoạt động theo cơ chế "Bóc vỏ hành" với 3 chặng và 2 cổng kiểm soát (Stage Gates).

**Quy trình 3 Giai Đoạn:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Stage</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giải pháp</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Output (Deliverable)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chi phí cho Cell Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>S (reSearch)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Discovery</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO/GEO Proposal Deck + Bản đồ từ khóa.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0đ (Brief 60 phút).</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>P (Pilot)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MVP Plan</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Live Mini Web/Widget + Dashboard đo lường W2A.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nguồn lực PO (2h/tuần).</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>A (Action)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Growth</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic quy mô lớn + Báo cáo đóng góp MAU/MEU.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">100% ngân sách Vendor/Media.</td>
    </tr>
  </tbody>
</table>

**Cổng Kiểm Soát (Stage Gates):**

- **Gate 1 (S → P):** Search Volume > 10,000/tháng + Có Business Context + Cam kết 2h/tuần.
- **Gate 2 (P → A):** W2A CR thực tế > 5% + Tracking (Appsflyer) chính xác + Có ngân sách Vendor.

---

### 6. Success Metrics

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lane</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Timeframe</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tracking</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Average W2A CR (Pilot phase)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility / Payment</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">> 5%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">30 ngày sau Pilot</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer + GA4</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Số lượng Use Case Onboard</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">N/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">10 Use Cases</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cuối 2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Internal Jira / MoSpark</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Time-to-Market (S to P)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">N/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">< 14 ngày</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ongoing</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Internal Tool</td>
    </tr>
  </tbody>
</table>

---

### 7. Dependencies & Constraints

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nguồn lực Web Platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Team GPD phải đủ dev để build MVP Widget/Mini Web cho các Cell Team.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang vận hành</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer / Onelink Setup</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cơ sở hạ tầng tracking W2A phải chuẩn xác để qua Gate 2.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đã sẵn sàng</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GenAI Content Pipeline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần cho giai đoạn sinh 10-15 bài Pilot test nhanh.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đã tích hợp</td>
    </tr>
  </tbody>
</table>

- **Constraints:**
  - Quy trình này đòi hỏi sự kỷ luật cao từ Cell Team (cung cấp Business Context chuẩn, review content đúng hạn).
  - Không thể bypass Gate 2 nếu W2A CR < 5% (phải sửa MVP đến khi đạt mới được scale).

---

## Change Log
- **Tháng 07/2026 (v2.0):** Cấu trúc lại toàn bộ tài liệu S-P-A Framework theo chuẩn CEO BRD Standard, định hình framework như một "Internal Product" của Web Platform.
- **Tháng 05/2026 (v1.0):** Ban hành phiên bản đầu tiên của S-P-A Framework dưới dạng quy trình văn bản.
