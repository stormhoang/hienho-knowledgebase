# BRD: Báo Cáo Lừa Đảo & Bản Tin An Toàn Bảo Mật (Trust - Report Scam & Security Newsletter)

> - **Project:** Use Case Báo Cáo Lừa Đảo (Trust) - Web Growth & Media Team Web Platform
> - **Main URL:** momo.vn/report-scam & momo.vn/atbm/ban-tin/{quy-nam}
> - **Division:** Risk & Security (GPD Web Platform)
> - **Version:** 1.3 · Tháng 6/2026
> - **Status:** Active (Scope: Landing Page báo cáo, Form nhập tay tĩnh & Bản tin ATBM Quý - S-P-A Framework)
> - **PRD Specs (Report Scam):** [09_PRD/trust-prd.md](../09_PRD/trust-prd.md)
> - **PRD Specs (Bản tin ATBM):** [09_PRD/ban-tin-atbm-prd.md](../09_PRD/ban-tin-atbm-prd.md)

---

> **Problem:** Mỗi tháng có hàng ngàn người dùng ngoài hệ sinh thái MoMo (Non-MoMo Users) bị lừa đảo trực tuyến tìm kiếm nơi tố giác kẻ lừa đảo hoặc cảnh báo cộng đồng. Tuy nhiên, họ gặp rào cản lớn khi phải tải app, đăng ký, đăng nhập tài khoản MoMo mới có thể gửi báo cáo trên Miniapp. Điều này làm lãng phí nguồn dữ liệu cảnh báo khổng lồ từ cộng đồng và làm tăng chi phí xử lý thủ công của CS (2.000-3.000 tickets/tháng).
> **KPI Owned:** Số lượng báo cáo lừa đảo ẩn danh được tiếp nhận thành công trên Web thông qua Landing Page (làm phong phú cơ sở dữ liệu cảnh báo cộng đồng và giảm tải vận hành CS).
> **Conversion Flow:** Người dùng truy cập Landing Page `/report-scam` (giới thiệu tính năng An toàn cùng MoMo) → Nhấn nút gửi báo cáo → Điền thông tin vào Form thu thập dữ liệu (nhập tay các trường cơ bản) → Người dùng gửi báo cáo → Submit thành công (Không yêu cầu đăng nhập/OTP, bảo đảm ẩn danh).

---

## 1. Executive Summary

### 1.0 Strategic Framework: Trust-Led Growth (Tăng trưởng bằng Niềm Tin)
Dự án Trust (Báo cáo lừa đảo & Bản tin ATBM) được định vị là dự án tiên phong đại diện cho mô hình chuyển dịch tăng trưởng chiến lược của MoMo (đạt mức *"Đủ trưởng thành, đủ sức mạnh để lựa chọn cách làm đúng"*):
*   **Promotion-led Growth:** Khuyến mãi giúp khách hàng **biết đến MoMo**.
*   **Product-led Growth:** Sản phẩm giúp khách hàng **ở lại với MoMo**.
*   **Trust-led Growth:** Niềm tin giúp khách hàng **nói về MoMo** (chia sẻ và lan tỏa thương hiệu).

Xây dựng niềm tin số toàn diện từ trong ra ngoài (Inside out) dựa trên **6 chiều kích cốt lõi (The 6 Dimensions)**:
1.  **Security & Data Privacy:** Bảo vệ dữ liệu cá nhân, sinh trắc học thông minh và phòng chống lừa đảo đa tầng (đạt benchmark **4.02/5**).
2.  **App Performance:** Tối ưu hóa hiệu năng, phản hồi siêu tốc và giảm trễ giao dịch (đạt benchmark **3.97/5**).
3.  **Customer Service:** Giải quyết triệt để thắc mắc khách hàng ngay lần đầu (FCR).
4.  **Transparency:** Minh bạch cơ chế bảo mật và thu thập thông tin (Nghị định 13).
5.  **UI & UX:** Giao diện tinh giản, luồng báo cáo/tương tác dễ dùng.
6.  **Branding:** Thương hiệu tài chính an tâm, đáng tin cậy.

*Nguyên lý vận hành:* *"Trust is not owned by one team. It's the collective impact from each of us."* Niềm tin số được cấu thành từ nỗ lực phối hợp của Central Team cùng toàn bộ các Business Unit (BU) trong hệ sinh thái.

*Đối tượng xây dựng Niềm tin:* Trust không chỉ là câu chuyện của MoMo với khách hàng hiện tại, mà hướng tới **toàn bộ hệ sinh thái** với 5 đối tượng cốt lõi:
1.  **Current Users:** Người dùng hiện tại cần cảm thấy an tâm và được bảo vệ.
2.  **Potential Users:** Người dùng tiềm năng tìm kiếm giải pháp an toàn để quyết định sử dụng.
3.  **Merchants:** Đối tác bán hàng cần an tâm kinh doanh và nhận các gói hỗ trợ tài chính/Soundbox.
4.  **Partners:** Các tổ chức tài chính/đối tác chiến lược liên kết dịch vụ.
5.  **Regulators:** Các cơ quan quản lý nhà nước giám sát tính tuân thủ (như Nghị định 13/2023/NĐ-CP).

### 1.1 Elegant Problem Framing
*   **Vấn đề cốt lõi:** Nạn nhân lừa đảo trực tuyến thường có tâm lý e ngại trình báo do thủ tục phức tạp, sợ bị lộ danh tính. Việc bắt buộc tải app MoMo và thực hiện KYC chỉ để gửi báo cáo là rào cản quá lớn đối với Non-MoMo users.
*   **Giải pháp (The "What"):** Xây dựng Landing Page tĩnh `/report-scam` nhằm giới thiệu tính năng cảnh báo và tiếp nhận báo cáo lừa đảo ẩn danh. Tích hợp một Form thu thập thông tin đơn giản cho phép người dùng tự điền tay (Manual Input) các trường cần thiết mà không cần đăng nhập/OTP, đảm bảo tính ẩn danh và tuân thủ pháp lý.

### 1.2 Situation
*   Hệ thống CS của MoMo tiếp nhận thủ công khoảng 2.000-3.000 ticket liên quan đến lừa đảo mỗi tháng.
*   Cần một Landing Page độc lập trên Web để giới thiệu các tính năng an toàn bảo mật của MoMo, tăng độ tin cậy thương hiệu (chỉ số Mức độ Tin cậy của người dùng đạt kỷ lục mới **4.18/5** tính đến hết Q1/2026, tăng trưởng liên tục qua các quý), đồng thời kêu gọi người dùng đóng góp thông tin tố giác kẻ lừa đảo.

### 1.3 Complication
*   Người dùng có xu hướng bỏ dở điền form (drop rate cao) nếu form quá dài hoặc đòi hỏi xác thực OTP phức tạp.
*   Hệ thống cần thu thập tối giản các trường thông tin nhưng vẫn phải đảm bảo tính hợp lệ để Risk và CS có thể xác minh.

### 1.4 Resolution (S-P-A Framework Implementation)
*   **reSearch (Giai đoạn 1):** Nghiên cứu giao diện và cấu trúc Landing Page mẫu [An Toan MoMo - Landing](file:///Users/hienhv/Downloads/An%20Toan%20MoMo%20-%20Landing%20%28standalone%29%20%281%29.html). Định hình bộ trường dữ liệu tối thiểu cần thu thập trong Form (SĐT kẻ lừa đảo, STK ngân hàng, Tên ngân hàng thụ hưởng, Số tiền tổn thất, kịch bản mô tả, và ảnh chụp bằng chứng). Nghiên cứu giải pháp tuân thủ pháp lý về thu thập dữ liệu cá nhân tự nguyện (Nghị định 13/2023/NĐ-CP).
*   **Pilot (Giai đoạn 2):** Triển khai Landing Page giới thiệu tĩnh tại `/report-scam` tích hợp Form báo cáo thủ công đơn giản (không có AI, không đăng nhập). Chạy thử nghiệm trong nội bộ hoặc quy mô nhỏ để kiểm tra tính ổn định của luồng submit và đo lường tỷ lệ điền hết form (Completion Rate).
*   **Action (Giai đoạn 3):** Vận hành Landing Page chính thức rộng rãi. Kết nối API Gateway để đẩy dữ liệu form trực tiếp về cơ sở dữ liệu của Risk Team và phân phối tạo ticket tự động cho CS xử lý.

---

## 2. Bối Cảnh Hiện Tại

### 2.1 Hiện trạng Web Assets

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Asset</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trạng thái</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/report-scam</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa build</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing page giới thiệu và thu thập báo cáo lừa đảo ẩn danh (Form nhập tay)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản tin ATBM Quý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/atbm/ban-tin/{quy-nam}</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa build</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing page long-form content tương tác giới thiệu hoạt động & số liệu ATBM từng Quý</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AEO/GEO Document</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/report-scam/llms.txt</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa build</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuẩn hóa thông tin cảnh báo an toàn cho AI Search Engines</td>
    </tr>
  </tbody>
</table>

### 2.2 Phạm vi dự án (Scope & Out-of-Scope)
*   **In-Scope:**
    *   Phát triển Landing Page `/report-scam` dựa trên giao diện mẫu giới thiệu về tính năng "An Toàn Cùng MoMo".
    *   Tích hợp Form thu thập báo cáo lừa đảo đơn giản với các trường nhập tay:
        *   Thông tin kẻ lừa đảo (SĐT hoặc Số tài khoản + Ngân hàng thụ hưởng).
        *   Số tiền bị lừa.
        *   Hình ảnh/Tệp đính kèm bằng chứng (chụp màn hình chat, hóa đơn chuyển tiền).
        *   Nội dung mô tả ngắn kịch bản lừa đảo.
    *   Cơ chế gửi ẩn danh hoàn toàn (các trường SĐT/Email của người gửi là tùy chọn và đi kèm checkbox đồng thuận tuân thủ Nghị định 13).
    *   **Phát triển Bản tin ATBM định kỳ Quý (momo.vn/atbm/ban-tin/{quy-nam}):**
        *   Landing page dạng Long Form Content có tính năng tương tác phục vụ chiến dịch Survey (tăng 30% cho 2 câu hỏi khảo sát cốt lõi).
        *   Khối 3 Flip Cards tương tác, cho phép người dùng tải trực tiếp tệp ảnh thẻ từ CDN về máy.
        *   Khối Tính Năng (Feature Highlights) với các nút bấm/hyperlinks mở app MoMo (Web-to-App) để kích hoạt/cài đặt tính năng in-app.
        *   Khối Highlight Con Số động (CountUp) thể hiện trực quan các con số tác động an toàn bảo mật.
        *   Liên kết điều hướng chéo giữa trang chủ ATBM, bản tin các quý và nhúng widget bản tin ở vị trí cố định trên trang chủ ATBM (dưới Certification, trên FAQ).
*   **Out-of-Scope (Các phase tiếp theo):**
    *   Tích hợp GenAI bóc tách thực thể (Autofill) từ văn bản tự do.
    *   SEO Planning diện rộng, các trang tra cứu lừa đảo động (pSEO) `/report-scam/tra-cuu/*`.
    *   Đồng bộ API tự động với các đối tác ngoài (như A05).

---

## 3. Quy Trình S-P-A (reSearch ➔ Pilot ➔ Action)

### 3.1 Giai đoạn 1: reSearch (Khảo sát & Thiết kế)
*   **Nhiệm vụ chi tiết:**
    1.  **Phân tích Landing Page Mẫu:** Khảo sát cấu trúc giao diện file mẫu [An Toan MoMo - Landing](file:///Users/hienhv/Downloads/An%20Toan%20MoMo%20-%20Landing%20%28standalone%29%20%281%29.html) để đồng nhất ngôn ngữ thiết kế thương hiệu (Brand Guidelines), các thành phần Call-to-Action (CTA) kêu gọi gửi thông tin.
    2.  **Chuẩn hóa các trường thông tin Form:** Thống nhất với Risk và CS về các trường dữ liệu tối thiểu bắt buộc để có thể thực hiện hậu kiểm (ví dụ: SĐT/STK kẻ lừa đảo, Tên ngân hàng). Các trường khác như Số tiền, nội dung mô tả sẽ ở dạng tùy chọn để giảm rào cản thao tác điền form.
    3.  **Compliance Legal:** Thiết kế nội dung tuyên bố miễn trừ trách nhiệm và các điều khoản đồng thuận tự nguyện theo Nghị định 13/2023/NĐ-CP khi người dùng gửi báo cáo ẩn danh.

### 3.2 Giai đoạn 2: Pilot (Thử nghiệm MVP)
*   **Nhiệm vụ chi tiết:**
    1.  **Xây dựng Landing Page MVP:** Phát triển Landing Page giới thiệu tĩnh tích hợp Form nhập liệu tĩnh trực tiếp tại đường dẫn `/report-scam`.
    2.  **Kiểm thử luồng submit:** Kết nối submit form về endpoint API tạm thời để kiểm tra tính ổn định của luồng truyền nhận file bằng chứng (ảnh chụp màn hình) và dữ liệu dạng text.
    3.  **Đo lường Pilot:** Chạy thử nghiệm trên nhóm nhỏ người dùng mẫu (~50-100 người) để đo lường tỷ lệ điền hết form (Completion Rate) và thu thập phản hồi về các rào cản trải nghiệm (UX Friction).

### 3.3 Giai đoạn 3: Action (Vận hành Rộng rãi)
*   **Nhiệm vụ chi tiết:**
    1.  **Go-live Landing Page:** Triển khai chính thức Landing Page rộng rãi trên hạ tầng Web Platform.
    2.  **Đồng bộ DB Risk & CS:** Đẩy dữ liệu báo cáo hoàn thành về Risk DB để làm giàu tập dữ liệu phòng chống gian lận và tạo ticket tự động cho bộ phận nghiệp vụ CS tiến hành hậu kiểm.
    3.  **Đo lường & Tối ưu:** Theo dõi tỷ lệ chuyển đổi (Conversion Rate) của Landing Page, thiết lập nền tảng đo lường để chuẩn bị cho các phase nâng cấp tiếp theo (ví dụ: bổ sung GenAI Autofill hoặc các trang tra cứu pSEO sau này).

---

## 4. JTBD (Jobs-to-be-Done) Analysis

### Job #TRUST-02 - Tố cáo nhanh chóng không cần đăng nhập (Scam Victim)
*   > "Tôi muốn tố cáo nhanh thông tin kẻ lừa đảo mà không muốn mất thời gian tải app MoMo hay đăng ký tài khoản, để tôi có thể cảnh báo cộng đồng và hạn chế thiệt hại mà không gặp rào cản công nghệ."

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Functional</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Đọc và hiểu tính năng giới thiệu an toàn của MoMo.<br>- Điền nhanh các trường thông tin cơ bản về kẻ lừa đảo (SĐT/STK, hình ảnh bằng chứng) và nhấn gửi ẩn danh hoàn tất dưới 2 phút.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Emotional</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Cảm thấy an tâm vì không bắt buộc để lại danh tính thực.<br>- Giải tỏa tâm lý muốn tố cáo nhanh khi vừa bị lừa đảo.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Social</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Đóng góp thông tin hữu ích giúp bảo vệ cộng đồng khỏi kẻ lừa đảo.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trigger</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Người dùng (Non-MoMo) vừa phát hiện hoặc bị lừa đảo chuyển khoản qua tài khoản ví MoMo/Ngân hàng.</td>
    </tr>
  </tbody>
</table>

---

## 5. Success Metrics

Do dự án tập trung vào Landing Page giới thiệu và thu thập thủ công tĩnh, các chỉ số thành công sẽ tập trung vào hiệu suất Landing Page và tỷ lệ hoàn thành form:

*   **Landing Page Conversion Rate (CTR to Form):** Đạt >= 40% (Tỷ lệ người dùng truy cập Landing Page nhấn vào nút gửi báo cáo).
*   **Form Completion Rate:** Đạt >= 70% (Tỷ lệ người dùng mở Form hoàn thành việc điền thông tin và bấm Submit thành công).
*   **Average Submission Time:** Dưới 120 giây (Thời gian trung bình người dùng hoàn tất điền form thủ công).
*   **CS Ticket Generation Success Rate:** 100% dữ liệu submit hợp lệ được tạo ticket tự động thành công trên hệ thống nghiệp vụ CS.
*   **End-to-End Processing Latency (Thời gian xử lý E2E):**
    *   *Client-side Submission:* Dưới **3 giây** (từ lúc nhấn gửi biểu mẫu kèm tối đa 5 file bằng chứng đến khi hiển thị màn hình hoàn tất).
    *   *System-side Processing:* Dưới **5 giây** (từ lúc gửi thành công đến khi ticket nghiệp vụ được khởi tạo hoàn tất trên Risk System).

---

## 6. Dependencies & Constraints

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dependency</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Bộ phận</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trạng thái</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Risk & Security Team</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Risk</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Duyệt các trường dữ liệu tối thiểu và logic xác thực báo cáo lừa đảo thủ công.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pending</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Legal & Compliance</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Legal</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Duyệt nội dung điều khoản miễn trừ trách nhiệm và tuân thủ Nghị định 13.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Pending</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Frontend/Backend Dev</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tech</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Triển khai giao diện tĩnh theo file thiết kế mẫu và API tiếp nhận submit form.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Active</td>
    </tr>
  </tbody>
</table>

---

## Change Log
- **Tháng 6/2026 (v1.0):** Khởi tạo dự thảo tài liệu BRD.
- **22/06/2026 (v1.1):** Thu hẹp scope tập trung vào Landing Page và GenAI Autofill (S-P-A Framework).
- **22/06/2026 (v1.2):** Cập nhật thu hẹp scope tối đa theo file thiết kế mẫu [An Toan MoMo - Landing](file:///Users/hienhv/Downloads/An%20Toan%20MoMo%20-%20Landing%20%28standalone%29%20%281%29.html). **Chỉ xây dựng Landing Page giới thiệu và Form thu thập báo cáo nhập tay (thủ công)**. Loại bỏ toàn bộ GenAI Autofill, pSEO tra cứu, và kết nối A05 khỏi scope hiện tại, chuyển chúng thành kế hoạch dài hạn.
