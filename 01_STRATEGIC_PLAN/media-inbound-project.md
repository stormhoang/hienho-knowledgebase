# Khung Chiến Lược Tái Cấu Trúc Vận Hành, Tự Động Hóa & Align Scope Dự Án BMC - Media Inbound

> - **Tài liệu:** Media Inbound Project - Executive Operational Restructuring, Automation & Scope Framework
> - **Khối phụ trách:** Growth Platform Division (GPD) x Web Platform x Division BMC - Media (Inbound)
> - **Phiên bản:** 3.1
> - **Cập nhật:** 2026-08-13
> - **Trạng thái:** APPROVED - Khung chiến lược tái cấu trúc vận hành chính thức thống nhất giữa Executive Leadership, BMC (Inbound) x Web Platform

---

## 1. Context & Bối Cảnh Chỉ Đạo Từ Executive Leadership & Senior Web Manager

### 1.1 Quy Tắc Không Tính In-App Traffic Vào Web KPI (Executive Directive - Anh Công)
Từ các cuộc trao đổi chiến lược, Ban Giám Đốc (anh Công) đã chỉ đạo định hướng thiết lập đội ngũ vận hành chạy thử nghiệm trên nền tảng Web Platform và ban hành **quy tắc đo lường cốt lõi**:
- **Quy tắc đo lường In-App:** **Lượng traffic In-app KHÔNG được tính vào chỉ số đo lường tổng của website (KPI Web Platform)**.
- **Vận hành In-App:** Luồng vận hành In-app hoàn toàn thuộc quyền tự quyết và quản lý của PO Mini App / In-App Platform và các BU liên quan.

### 1.2 Phân Định Ranh Giới KPI Web Platform vs Business Units (Senior Web Manager POV)
- **Web Platform chỉ kiểm soát số liệu tổng ngang (Top-of-Funnel):** Bao gồm 3 chỉ số cơ bản: **Traffic (Visitor/Pageview), Click (CTA CTR) và Login App (Agent ID Sync)**.
- **Web Platform KHÔNG nhận KPI chuyển đổi sâu cuối phễu (Bottom-of-Funnel):** Các chỉ số như số lượng giao dịch, mở khoản vay hay giải ngân thuộc 100% trách nhiệm của các Business Units (BU) do không thể đo lường liên kết nhân quả trực tiếp từ traffic web ban đầu với hành vi In-app cuối cùng.
- **Quản lý theo Dự án Kinh doanh (Vertical Business Projects):** Quy đổi các mục tiêu tổng thành từng dự án kinh doanh cụ thể của BU (như Financial Services, Trust Project) để quản lý hiệu quả.

### 1.3 Cảnh Báo Không Cho BU Tự Dựng Mini Web Hoàn Toàn ("Nát Hết") & Vai Trò Điều Phối BMC
- **Cảnh báo nguy cơ chất lượng ("Nát hết"):** **Nếu giao 100% việc dựng Mini Web cho BU tự làm sẽ làm sụt giảm nghiêm trọng chất lượng trải nghiệm ("nát hết")**. Việc dựng web (kể cả dùng Template) vẫn đòi hỏi kỹ năng chuyên môn kỹ thuật sâu: UI/UX layout, tiêu chuẩn hình ảnh, cấu hình tính năng, tối ưu tốc độ tải trang và tiêu chuẩn Google Ad/SEO.
- **BMC Inbound BẮT BUỘC giữ vai trò Điều phối (Single Ownership):** Team Inbound mảng BMC phải chịu trách nhiệm 100% về kiểm soát chất lượng hàng ngang, quản lý phân quyền Admin Panel và phê duyệt nội dung trước khi xuất bản. Web Platform không có nhân sự và chuyên môn về content, chỉ đóng vai trò hỗ trợ kỹ thuật và xây dựng công cụ tăng năng suất.

### 1.4 Tự Động Hóa Webview T&C Dạng TLDR & Hệ Thống Guardrails
- **Chuẩn hóa Webview Điều khoản (T&C):** Tự động hóa bài Webview T&C khuyến mãi theo thiết kế **TLDR**: Headline + Sub-headline + Tóm tắt ngắn gọn 3-4 dòng chính ở trên cùng để thu hút người dùng hành động ngay; phần điều khoản pháp lý compliance chuyển xuống dưới cùng.
- **Hệ thống Guardrails Tự động:** Xây dựng bộ lọc tự động kiểm soát bài viết Out-App để ngăn chặn rủi ro xuất bản URL rác làm ảnh hưởng đến chỉ số SEO tổng thể của website (`momo.vn`).

---

## 2. Thực Trạng Các Workstreams Web Platform Đang Hỗ Trợ BMC Inbound

Web Platform Team phụ trách **4 nhóm Workstreams kỹ thuật & giải pháp** chính theo đúng ranh giới chuyên môn:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm Workstream</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng Mục Hỗ Trợ Kỹ Thuật (Active Support Scope)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô Hình Vận Hành & Trách Nhiệm Phê Duyệt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>1. Công Cụ & Nền Tảng (Tools & Athena/TLDR Enablement)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Xây dựng Template Engine tự động hóa bài T&C dạng **TLDR**.<br/>- Tích hợp Athena làm môi trường chung sản xuất nội dung, hình ảnh và luồng duyệt Legal/Creative.<br/>- AI Co-pilot hỗ trợ BU tự động tạo nội dung/hình ảnh chuẩn UI/UX và tốc độ tải trang.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform cấp công cụ; **BMC Inbound kiểm soát chất lượng & phê duyệt**.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>2. Tracking (Attribution & Identity Gateway)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Triển khai cổng gắn tracking độc quyền 100% dự án Inbound: Cấu hình Onelink Engine, Edge Cookie Identity Sync (Agent ID), Custom Event Tag Injection, Umami & BigQuery Data Attribution.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Single Infrastructure Gateway cho 100% mã tracking OutApp/Miniweb.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>3. Campaign (Miniweb Ops: Template vs Custom)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- <strong>Template (37%):</strong> Cung cấp Modular Landing Page Builder cho BU nhập liệu dưới sự duyệt chất lượng của BMC.<br/>- <strong>Custom (63%):</strong> Trực tiếp tư vấn wireframe, dựng trang phức tạp & cài mã tracking cho chiến dịch lớn (Lắc Xì, Mega Summer...).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Self-serve Template (BMC kiểm soát); Co-building cho trang Custom.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>4. Platform (Technical Risk & Guardrails System)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Xây dựng hệ thống **Automated Guardrails** lọc bài viết rác bảo vệ SEO `momo.vn`.<br/>- Mở rộng phân quyền Admin Panel theo từng Cell Team.<br/>- Bảo đảm hạ tầng kỹ thuật: Captcha Shield chống bot/fraud, Core Web Vitals, Spike Traffic Protection.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hệ thống Guardrails tự động & Phân quyền Admin Panel do BMC quản trị xuất bản.</td>
    </tr>
  </tbody>
</table>

---

## 3. Mô Hình Internal Marketing Agency & Single Ownership

### 3.1 Mô Hình Marketing Agency Nội Bộ Phía BMC
BMC Inbound giữ vai trò như một **Marketing Agency nội bộ** cho các dự án kinh doanh lớn:
- **Tập trung dự án kinh doanh (Vertical Focus):** Chuyển từ hỗ trợ tràn lan sang tập trung sâu vào từng dự án cụ thể (như Financial Services, Trust Project).
- **Cam kết dài hạn 1+ năm:** Đồng hành tối thiểu 1 năm cho mỗi dự án chiến lược để bảo đảm đo lường được giá trị kinh doanh thực sự.

### 3.2 Phân Định Single Ownership
- **BMC Media (Inbound):** Sở hữu 100% chỉ số Share of Voice (SoV), Search Keyword Ranking, Chất lượng nội dung truyền thông và Phê duyệt xuất bản bài viết.
- **Web Platform Team:** Sở hữu 100% Hạ tầng Nền tảng Kỹ thuật, Tốc độ tải trang, Phân quyền Admin Panel, Hệ thống Guardrails tự động và Cổng Gắn Tracking Độc quyền.

---

## 4. Khung Phân Định Scope Đề Xuất (Proposed Scope Division - v3.1)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng Mục Scope</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phạm Vi Scope Thuộc WEB PLATFORM (Technical Infrastructure & Tools)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phạm Vi Scope Thuộc BMC MEDIA / PO MINI APP / CELL TEAMS (BU)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>InApp Webview & T&C News (82% Workload)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cung cấp Admin Panel và Template T&C chuẩn TLDR. Không kéo thả hay copy-paste thủ công. *Lưu ý: Traffic In-App không tính vào Web KPI.*</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>PO Mini App:</strong> Phát triển Native In-App Comm Tools.<br/><strong>Cell Teams (BU):</strong> Tự nhập bài T&C theo định dạng TLDR.<br/><strong>BMC Inbound:</strong> Kiểm soát chất lượng & phân quyền.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>OutApp News & SEO Content (18% Workload)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xây dựng **Hệ thống Guardrails tự động** (lọc URL rác) và mở rộng phân quyền Self-serve CMS trên Admin Tool. Gắn sẵn mã Tracking Base.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cell Teams (BU):</strong> Nhập nội dung Out-App.<br/><strong>BMC Media (Inbound):</strong> Giám sát chất lượng hàng ngang, phê duyệt bài xuất bản & chịu 100% KPI SoV/Ranking.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Mini Web Template (37% Workload)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đóng gói Modular Landing Page Builder & hệ thống Template chuẩn hóa về UI/UX và tốc độ trang.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cell Teams (BU):</strong> Nhập nội dung trên Template sẵn.<br/><strong>BMC Media (Inbound):</strong> Kiểm soát chất lượng UI/UX & phê duyệt xuất bản (tránh giao 100% gây "nát hết").</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Mini Web Custom (63% Workload)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Triển khai Dựng Web Custom & Gắn Tracking:</strong> Đảm nhận 100% kỹ thuật dựng trang phức tạp, tích hợp Utility/API và **trực tiếp cài đặt các mã Tracking Script/Events**.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>BMC Media (Inbound):</strong> Điều phối dự án, định nghĩa Biz KPI, phối hợp thiết kế Wireframe, review SEO & thẩm định Event Tracking Matrix.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tracking & Infrastructure Gateway</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cổng Triển Khai Tracking Độc Quyền (Single Gateway):</strong> Cấu hình Onelink Engine, Edge Cookie Identity Sync, Custom Tag Injection, Umami & BigQuery Data Attribution.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>BMC Media & BU:</strong> Cung cấp ma trận sự kiện (Event Matrix) cần đo lường cho từng chiến dịch để Web Platform gắn mã.</td>
    </tr>
  </tbody>
</table>

---

## 5. Quy Trình Vận Hành Phân Luồng InApp vs OutApp (Chuẩn TLDR & BMC Quality Control)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Bước</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Giai Đoạn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trải Nghiệm & Thao Tác Thực Hiện</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạ Tầng / Cơ Chế Kỹ Thuật</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đội Ngũ Phụ Trách (Ownership)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content Creation (TLDR & Athena)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BU tạo nội dung trên Athena (sử dụng AI Co-pilot), định dạng T&C theo mẫu TLDR (headline + tóm tắt ngắn trên cùng).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Athena Environment / AI Co-pilot Engine</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cell Teams (BU) x BMC Media (Inbound)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Guardrails & BMC Quality Audit</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Bài OutApp chạy qua <strong>Automated Guardrails System</strong>.<br/>- BMC Inbound thực hiện kiểm soát chất lượng hàng ngang (UI/UX, tiêu chuẩn ảnh, SEO).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Automated Guardrails Filter / Admin Access Control</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform System (Tự động) x BMC Media (Điều phối kiểm duyệt)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Technical Building & Tracking Injection</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform dựng Miniweb Custom trên Admin Panel và <strong>gắn toàn bộ mã Tracking Script, Onelink & Custom Events</strong>. BMC Media review SEO & test tracking.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tracking Tag Injection / Edge Cookie Sync / SEO Audit Tool</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform Team (Dựng Web & Gắn Tracking) x BMC Media (Review SEO)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Publishing Approval & Security Audit</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BMC Inbound phê duyệt xuất bản công khai trên Web (`momo.vn`) hoặc Native App. Kiểm tra hạ tầng an toàn.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Captcha Shield / Deployment Engine</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BMC Media (Duyệt Xuất Bản) x Software Engineering Team</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tracking & Business Value Dashboard</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ghi nhận Traffic, Click, Agent ID Login App và hiển thị Dashboard báo cáo Business Value cho dự án (FS/Trust).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Onelink Standardization / Edge Cookie Sync / Umami / BigQuery</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Data Analytics Team & Web Platform Team</td>
    </tr>
  </tbody>
</table>

---

## 6. Action Items Lộ Trình Triển Khai (Align Biên Bản Họp 13/08/2026)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đợt Triển Khai</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hành Động Trọng Tâm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội Dung Chi Tiết Thực Thi</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đội Ngũ Thực Hiện</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đợt 1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rà Soát & Đóng Gói Template T&C Chuẩn TLDR</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform Lead phối hợp với Inbound Lead rà soát toàn bộ template hiện có, đóng gói mẫu T&C dạng TLDR và phân định danh mục 37% Template tự động hóa.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform Lead x Inbound Lead (BMC)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đợt 2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thiết Lập Hệ Thống Guardrails & Quy Trình Duyệt Chất Lượng BMC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Xây dựng <strong>Automated Guardrails System</strong> lọc bài viết rác bảo vệ SEO `momo.vn`.<br/>- Thiết lập quy trình BMC Inbound điều phối phê duyệt xuất bản (tránh giao BU tự làm gây "nát hết").</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform Lead x SE Team x Inbound Lead (BMC)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đợt 3</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Họp Solution Deep-Dive Về Công Cụ Self-Service Cho BU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổ chức buổi làm việc kỹ thuật chuyên sâu để chốt chi tiết tính năng, giao diện Admin Panel và tích hợp Athena/AI Co-pilot cho công cụ self-service của BU.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform Team x BMC Inbound x Cell Teams (BU)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đợt 4</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thống Nhất Single Ownership KPI & Biz Value Dashboard</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xác định rõ chủ sở hữu (Single Owner) cho từng chỉ số KPI kinh doanh theo dự án (Financial Services, Trust) và cấu hình BigQuery Dashboard đo lường W2A Conversion.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BMC Media (Inbound) x Web Platform Team x Data Team</td>
    </tr>
  </tbody>
</table>

---

## 7. Khung Phân Định Trách Nhiệm Chỉ Số Đo Lường (Single Ownership Framework)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm Chỉ Số</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng Mục Đo Lường Chi Tiết</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đơn Vị Chịu Trách Nhiệm 100% (Single Ownership)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nhận Diện Truyền Thông (SoV & Ranking)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Share of Voice (SoV), Tỷ lệ thứ hạng từ khóa (Search Keyword Ranking), Tỷ lệ trích dẫn AI Search (GEO Citation), Out-App Brand Reach.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>100% Thuộc Phía BMC Media (Inbound)</strong><br/><i>(Web Platform KHÔNG chịu trách nhiệm về chỉ số SoV hay Ranking này).</i></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Top-of-Funnel Web Metrics & Hạ Tầng Kỹ Thuật</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic tổng ngang website (Visitor/Pageview), Tỷ lệ nhấp CTA %, Agent ID Login App, Onelink, Edge Cookie Sync, Automated Guardrails. *Lưu ý: Không tính In-App Traffic vào Web KPI.*</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>100% Thuộc Phía Web Platform Team</strong><br/><i>(Web Platform KHÔNG chịu trách nhiệm về chỉ số chuyển đổi giao dịch sâu cuối phễu của BU).</i></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hiệu Quả Chuyển Đổi Kinh Doanh (Business Value)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số lượng hợp đồng giải ngân, số lượng giao dịch, MEU & doanh số In-App cho Financial Services / Trust Project.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>100% Thuộc Phía Các Business Units (BUs)</strong><br/><i>(Đo lường qua BigQuery Single Source of Truth).</i></td>
    </tr>
  </tbody>
</table>

---

## 8. Nhật Ký Thay Đổi (Change Log)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phiên Bản</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngày</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội Dung Thay Đổi</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tác Giả / Phê Duyệt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>v1.0 - v3.0</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-08-13</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khởi tạo, định hình khoảng trống Alignment VP/Head và đồng bộ biên bản họp tái cấu trúc ngày 13/08/2026.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead, Web Platform</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>v3.1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-08-13</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bổ sung định hướng chỉ đạo từ <strong>Executive Leadership (anh Công)</strong> và <strong>Senior Web Manager</strong>: (1) Traffic In-App KHÔNG được tính vào KPI của Web Platform; (2) Web Platform chỉ sở hữu Top-of-Funnel metrics (Traffic, Click, App Login), không gánh KPI chuyển đổi sâu cuối phễu của BU; (3) Khẳng định <strong>BMC Inbound bắt buộc phải giữ vai trò điều phối và chịu trách nhiệm 100% chất lượng phê duyệt xuất bản</strong> (không thả floating cho BU tự làm gây "nát hết"); (4) Thiết kế bài T&C Webview tự động theo chuẩn TLDR.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead, Web Platform</td>
    </tr>
  </tbody>
</table>

*Tài liệu được quản trị bởi Web Product Lead & Web Platform Team | Cập nhật lần cuối: 2026-08-13*
