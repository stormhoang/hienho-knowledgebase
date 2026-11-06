# MoMo Student Hub - Product Requirements Document (PRD)

## I. DOCUMENT CONTROL & EXECUTIVE SUMMARY

### 1.1 Document Overview
* **Product Name:** MoMo Student Hub (Discovery Platform & Unified Student Gateway)
* **Target Platform:** Web Platform (`momo.vn/sinh-vien` - Unauthenticated Public Web Platform for SEO, AEO & Discovery). Hệ thống triển khai tập trung trên Web, không có trang Hub riêng trong App MoMo.
* **Document Version:** v1.0 Final (Production Ready - Strategic Alignment Version)
* **Product Ownership:** MoMo Web Platform & Student Acquisition Team
* **Platform Positioning:** Standing Platform vận hành dài hạn quanh năm, chuyển đổi từ trang Landing Page tĩnh "Student Pass" (lỗi thời từ 2024) thành **Hệ sinh thái Sản phẩm Product-Led Growth (PLG)** dành riêng cho Gen Z (lớp 12, tân sinh viên & sinh viên).

### 1.2 Strategic Context & Product Big Idea
* **Bối cảnh Chuyển đổi Chiến lược (Recap Alignment):** Thay thế Landing Page tĩnh "Student Pass" cũ kỹ từ năm 2024 thành một Hệ sinh thái Sản phẩm công nghệ dài hạn. Mục tiêu cốt lõi là dùng tiện ích thực tế thu hút lượng truy cập tự nhiên (Growth Hacking), giữ chân sinh viên và lồng ghép dịch vụ MoMo.
* **Product Vision:** Student Hub đóng vai trò là **lớp nội dung + điều hướng hợp nhất (Unified Content & Navigation Gateway)** cho toàn bộ tệp người dùng HSSV trên Web MoMo. Hệ thống kết nối từ thông tin trường học, kinh nghiệm sống xa nhà cho đến các dịch vụ tài chính sinh viên.
* **Big Idea Sản Phẩm:** *"Lần đầu tự lập, không phải tự lo"* - MoMo đồng hành cùng người trẻ qua từng cột mốc tài chính và học tập đầu đời.
* **Kiến trúc Không Authen trên Web & Chuyển Tiếp OneLink:**
  * Trang Web `momo.vn/sinh-vien` vận hành không yêu cầu đăng nhập (Unauthenticated Discovery).
  * Mọi nút bấm tương tác cá nhân hóa (Nộp học phí, Xác thực Thẻ Sinh Viên Số, Mở Ví Trả Sau, Vay Nhanh) sử dụng **OneLink điều hướng thẳng sang các màn hình/mini-app tương ứng sẵn có trong App MoMo**.

## II. 4 CORE STRATEGIC PILLARS (CHƯƠNG TRÌNH TRỌNG TÂM)

### 2.1 Trụ Cột 1: Xây Dựng Cổng Thông Tin Đại Học (Data & pSEO Engine)
* **File Dữ Liệu Đầu Vào Chính Thức (Official Data Matrix Input):** Toàn bộ cấu trúc nội dung 11 Section, Schema dữ liệu ngành học, học bổng, cổng đăng ký tín chỉ và bộ dữ liệu thực tế của 05 trường đại học thí điểm Phase 1 (UEH, FTU, TDTU, HCMUT, VLU) được đối soát và kế thừa trực tiếp từ file dữ liệu chuẩn: `/Users/hienhv/Downloads/Content Structure.xlsx`.
* **Thí điểm 05 Trường Đại học Trọng điểm Phase 1:** Bách Khoa TP.HCM (HCMUT), Kinh tế TP.HCM (UEH), Văn Lang (VLU), Ngoại thương (FTU), Tôn Đức Thắng (TDTU).
* **Cấu trúc Dữ liệu Chuẩn hóa (Schema Markup):** Thu thập và xác thực trực tiếp từ website chính thức của các trường ĐH:
  * Điểm chuẩn xét tuyển các năm (`22.8 - 27.7`).
  * Quy chế tuyển sinh & các phương thức xét tuyển.
  * Chi tiết ngành học, môn học tiêu biểu, lộ trình học theo học kỳ, chuẩn đầu ra & mức lương tốt nghiệp.
  * Điều kiện & giá trị các suất học bổng.
* **Ma trận Nội dung theo Search Volume (Google Trends VN 12 tháng):** Sắp xếp ưu tiên hiển thị nội dung theo nhu cầu tìm kiếm thực tế của sinh viên (Điểm chuẩn, Học phí, Xe buýt, Việc làm sinh viên).

### 2.2 Trụ Cột 2: Phát Triển Hệ Sinh Thái Tiện Ích (Utility Tools Ecosystem)
Tích hợp các công cụ giải quyết trực tiếp "nỗi đau" hàng ngày của sinh viên:
1. **Công cụ Tài chính Cá nhân (Tuition & Budget Calculator):**
   * *Utility Tính Học Phí Theo Tín Chỉ:* Công cụ giả lập tính tổng tiền học phí theo số lượng tín chỉ sinh viên chọn (12 - 30 tín chỉ), cơ cấu chi tiết học phí và kích hoạt CTA *"Nộp học phí ngay"* dẫn qua OneLink sang phễu thanh toán In-App.
   * *Công cụ Quản lý Ngân sách / Thu nhập:* Giúp sinh viên tính toán tiền sinh hoạt hàng tháng, điều hướng mở **Túi Thần Tài** (tích lũy sinh lời) hoặc **Ví Trả Sau 0%** (chi tiêu thiết bị học tập).
2. **Bản đồ Tiện ích Vị trí (Location-Based Amenities Map 5km):**
   * Bản đồ tương tác hiển thị Nhà trọ, Quán ăn, Cà phê, Xe buýt, Siêu thị quanh campus (cơ cấu *Bên trong Campus* & *Bên ngoài Campus* bán kính 500m, 1km, 2km, 5km).
   * **Ưu tiên hiển thị cửa hàng SME chấp nhận thanh toán MoMo** kèm mã giảm giá O2O.
   * Tích hợp API Tuyến xe buýt (Google Transit API & dữ liệu GTFS miễn phí từ Sở GTVT).
3. **Cổng Việc Làm & Thực Tập (Jobs & Internship Gateway):**
   * Kết nối sinh viên tìm việc làm part-time / thực tập (hiển thị mức lương, địa điểm, đánh giá, CTA Ứng tuyển).
   * Xử lý "nỗi đau" thiếu hụt nhân sự của các chuỗi nhà hàng, F&B, siêu thị đối tác thương mại của MoMo.
4. **Hệ thống Đánh giá UGC & Sự kiện (Review & Event Meetup Module):**
   * Đồng bộ API luồng đánh giá trường học 5 sao đa tiêu chí từ trong App ra ngoài Web.
   * Tính năng xem & đăng ký tham gia Webinar, AI talk, Workshop kỹ năng sinh viên (mô hình Meetup).

### 2.3 Trụ Cột 3: Số Hóa Chương Trình Đại Sứ Sinh Viên (Productized Ambassador Engine)
* **Sản phẩm hóa Ambassador (Tech-Enabled Ambassador System):** Chuyển đổi chiến dịch Social thủ công (TikTok, Threads) của 50 đại sứ hàng năm thành một **sản phẩm công nghệ độc lập**.
* **Tính năng Hệ thống Ambassador:**
  * Giao nhiệm vụ tự động (Daily/Weekly Quests).
  * Tích lũy điểm thưởng & Bảng xếp hạng Leaderboard.
  * Quản lý quyền lợi đại sứ: Mentorship 1-on-1, Workshop kỹ năng, Chứng nhận CV chính thức.
* **Tầm nhìn Mở rộng (Scale Roadmap):** Xây dựng hệ thống vững chắc để scale quy mô toàn quốc, kết nối trực tiếp nguồn nhân lực đại sứ sinh viên chất lượng cao vào chương trình **MoMo Talent Pipeline**.

### 2.4 Trụ Cột 4: Hành Động Thực Thi Ngắn Hạn (Landing Page Revamp & CMS Governance)
* **Xử lý Nội dung Lỗi thời:** Quét dọn và thay mới toàn bộ hình ảnh, video, voucher, CTAs cũ kỹ từ năm 2024 để chuẩn bị cho mùa Back to School.
* **Tối ưu UI/UX Mobile Webview:** Khắc phục triệt để lỗi font chữ quá nhỏ, hình ảnh bị vỡ/lệch khung hình khi hiển thị trên di động.
* **Bàn giao CMS Tự Chủ (MoSpark CMS / MS Park):** Thiết lập và bàn giao công cụ CMS cho đội ngũ Vận hành (Ops) tự chỉnh sửa nội dung, bật/tắt các khối UI Block trên Web mà không phụ thuộc vào lập trình viên.

## III. TARGET AUDIENCE & USER PERSONAS

### 3.1 Target User Base
* **Quy mô tệp sinh viên:** ~1,49 triệu sinh viên đại học/cao đẳng trên toàn quốc (~612.000 sinh viên đã xác thực trên App MoMo, chiếm ~41% thị phần).
* **Mục tiêu mở rộng:** Tiếp cận 100% tệp tân sinh viên nhập học hàng năm qua kênh Google Organic Search & mạng xã hội.

### 3.2 Core User Personas
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Persona</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả & Nhu cầu Đặc thù</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Touchpoint Ưu tiên trên Hub</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tân Sinh Viên (Freshmen)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mới lên thành phố, lo lắng về chọn trường, học phí, an toàn phòng trọ, phương tiện đi lại (xe buýt), chưa có kinh nghiệm quản lý chi tiêu.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hero Section Trường học, Bản đồ Tiện ích quanh trường 5km, FAQs Nhập học, Thẻ Sinh Viên Số.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Sinh Viên Đang Học (Sophomores/Seniors)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhu cầu nộp học phí hàng kỳ, tìm kiếm ưu đãi ăn uống, gia hạn Data 4G/5G, đăng ký công cụ AI (Gemini Student Offer), làm thêm & vay tiêu dùng ngắn hạn.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility Tính Học Phí Theo Tín Chỉ, Service Grid Icon, Top Ưu đãi Sinh viên, Cổng Việc làm Part-time.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phụ Huynh (Parents)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Muốn tra cứu độ uy tín của trường, minh bạch mức học phí trung bình, tìm hiểu môi trường sống an toàn cho con xa nhà.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thang điểm đánh giá uy tín (Parent Rating ⭐), Thông tin NAP, Bảng Học phí & Ngành học.</td>
    </tr>
  </tbody>
</table>

## IV. MASTER SITE STRUCTURE & URL HIERARCHY

### 4.1 Master Site Structure
* **Lộ Trình Triển Khai Kiến Trúc Trang (2-Phase Architecture Roadmap):**
  * **Phase 1 (Hiện tại - Single-Page + Modal Popups):** Hiện tại **chưa triển khai các trang con (Sub-pages)** cho Ngành đào tạo, Học bổng, Việc làm, Nhà trọ. Tất cả nội dung chi tiết được hiển thị trực tiếp trên một trang trường học duy nhất (`momo.vn/sinh-vien/[ten-truong-ma-truong]`) thông qua **Modal Popups / Drawers / Anchor Links (`#nganh-dao-tao`, `#hoc-bong`, `#viec-lam`, `#nha-tro`, `#review`)** nhằm tập trung sức mạnh SEO Domain Authority và tối ưu tốc độ tải trang.
  * **Phase 2 (Mở rộng Programmatic Sub-Pages):** Fast-track ra mắt Cổng Việc Làm Master (`/sinh-vien/viec-lam`) và trang Đại sứ (`/ambassador`) trong Phase 2 (Tháng 9/2026); các Cổng Master Nhà Trọ (`/nha-tro`) và Workshop (`/workshop`) mở rộng trong Phase 3.
 (`/sinh-vien`)
Cấu trúc đường dẫn URL chuẩn phân cấp Subdirectory cơ cấu từ gốc `/sinh-vien`:

```
momo.vn/sinh-vien (Trang chủ Student Hub / Discovery Hub)
├── /sinh-vien/viec-lam (Cổng Master Việc Làm Sinh Viên & AI Resume Builder)
├── /sinh-vien/nha-tro (Cổng Master Nhà Trọ & KTX Sinh Viên - Dynamic Query ?truong=[slug])
├── /sinh-vien/workshop (Cổng Master Webinar & Event Workshop Sinh Viên)
├── /sinh-vien/ambassador (Trang Showcase Đại sứ Sinh viên MoMo & Tuyển dụng Ambassador)
└── /sinh-vien/[ten-truong-ma-truong] (Trang chi tiết Trường ĐH - Ví dụ: /sinh-vien/ton-duc-thang-tdtu)
```

### 4.2 URL Routing Matrix
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Pattern</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Loại Trang (Page Type)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chức năng Chính & Trải nghiệm UX</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Primary CTA (OneLink Web-to-App)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/sinh-vien</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hub Homepage</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổng quan Thẻ Sinh Viên Số, Banner ưu đãi hot, Widget Bạn đồng hành MoMo, Top Review Trường.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Xác thực ngay / Nhận đặc quyền</em></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/sinh-vien/[ten-truong-ma-truong]</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>School Landing Page</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang trường chuyên biệt (VD: <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/sinh-vien/ton-duc-thang-tdtu</code>), thông tin học phí, môi trường học, review tổng quan (tích hợp Inline Block / Modal Drawer #review).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Review ngay (Mở App)</em></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/sinh-vien/[ten-truong-ma-truong]/nha-tro</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Sub-page Nhà trọ & KTX</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Danh sách phòng trọ an toàn, giá thuê KTX, bản đồ khoảng cách tới cơ sở trường ĐH.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Xem nhà trọ / Tính tiền trọ</em></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/sinh-vien/[ten-truong-ma-truong]/ambassador</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Sub-page Đại sứ Sinh viên (Ambassador)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chương trình tuyển dụng & hoạt động của Campus Ambassadors MoMo tại trường ĐH, cơ hội việc làm & đặc quyền thủ lĩnh.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Đăng ký làm Ambassador</em></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/sinh-vien/[ten-truong-ma-truong]/workshop</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Sub-page Workshop & Event</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuỗi bài viết & đăng ký tham gia Webinar "Career & AI Talk", sự kiện CLB trường ĐH.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Đăng ký tham gia Workshop</em></td>
    </tr>
  </tbody>
</table>

## V. DETAILED FEATURE SPECIFICATIONS & UI BLUEPRINT (FROM LIVE PROTOTYPE)

### 5.1 Top Strip & Site Navigation Bar
* **Top Announcement Strip:** Hiển thị thông báo khuyến mãi nổi bật: *"CHÀO MỪNG TÂN SINH VIÊN 2026 - MỞ THẺ SINH VIÊN SỐ NHẬN GÓI QUÀ 500K"*.
* **Header Components:**
  * Logo MoMo Student Hub + Dropdown danh sách trường ĐH (`nav-univ-dropdown`).
  * Khung tìm kiếm thông minh (`nav-search-inp`): Tìm kiếm trường ĐH, nhà trọ, ngành học.
  * **Kiến trúc Web:** Hệ thống Web `momo.vn/sinh-vien` vận hành không yêu cầu tài khoản đăng nhập hay xác thực (Unauthenticated Web Gateway). Người dùng truy cập nội dung tự do; các hành động cá nhân hóa hoặc giao dịch được điều hướng trực tiếp bằng OneLink sang màn hình/mini-app tính năng tương ứng trong App MoMo.

### 5.2 School Detail Hero Section (Airbnb-Style Layout)
Thiết kế theo bố cục Airbnb Mosaic hiện đại, tối ưu hiển thị thông tin trường học:
1. **Hero Header:**
   * Tên chính thức của trường ĐH kèm **nhãn xác thực (Verified)** đặt ngay bên cạnh tên trường.
   * Thông tin NAP (Name: Trường ĐH Tôn Đức Thắng, Address: 19 Nguyễn Hữu Thọ, Q.7, TP.HCM, Phone).
   * Thang điểm đánh giá uy tín (4.8★ Parent & Student Rating).
   * Chỉ số thống kê nhanh: Điểm chuẩn (`22.8 - 27.7`), Học phí TB (`30 - 60tr/năm`), Tỷ lệ có việc làm (`98.2%`).
2. **Campus Switcher Bar (Thanh Lọc Cơ Sở Chi Nhánh):**
   * Bộ lọc Tab chọn lọc theo từng chi nhánh cụ thể: `[Tất Cả Cơ Sở] | [Cơ Sở Tân Phong (Q7)] | [Cơ Sở Bảo Lộc] | [Cơ Sở Nha Trang]`.
   * Khi người dùng bấm chọn cơ sở, toàn bộ địa chỉ GPS, danh sách trọ và cửa hàng ăn uống sẽ tự động cập nhật theo cơ sở đó.
3. **Photo Mosaic Gallery:** Lưới hình ảnh khuôn viên trường, cơ sở vật chất, thư viện, canteen.
4. **Primary CTA:** Nút *"Đánh giá trường này"* kích hoạt OneLink mở phễu đánh giá trong App MoMo.

### 5.3 Service Icon Grid (6 Micro-Features)
Lưới 6 icon điều hướng 1-touch truy cập nhanh các dịch vụ trọng tâm:
1. **Đóng học phí:** Tra cứu mã sinh viên & thanh toán học phí trực tuyến.
2. **Đăng ký tín chỉ:** Mẹo săn tín chỉ & nhắc lịch nộp tiền tín chỉ.
3. **Vay nhanh:** Giả lập khoản vay tiêu dùng sinh viên (10M - 100M) lãi suất ưu đãi.
4. **Ví Trả Sau 0%:** Mở hạn mức tín dụng sinh viên mua sắm thiết bị học tập.
5. **Túi Thần Tài:** Tích lũy sinh lời hàng ngày cho tiền chi tiêu sinh viên.
6. **Student Pass:** Xác thực Thẻ Sinh Viên Số nhận đặc quyền.

### 5.4 Interactive Nearby Merchant Discovery Widget (Bản Đồ Cửa Hàng & Tuyến Xe Buýt 5km)
* **Bản đồ tương tác (Leaflet / Google Maps API):** Tích hợp bản đồ GPS quanh cơ sở trường ĐH.
* **Bộ lọc vị trí (Radius Filter):**
  * `Bên trong Campus` (Canteen, Tiệm photocopy, Máy bán nước tự động).
  * `Bên ngoài Campus` với bán kính tùy chọn: `500m | 1km | 2km | 5km`.
* **Danh mục địa điểm:** Ưu tiên hiển thị các cửa hàng SME chấp nhận MoMo (Nhà trọ & KTX, Quán ăn, Trà sữa, Xe buýt, Siêu thị, Trung tâm Tiếng Anh).
* **Tích hợp API Tuyến Xe Buýt (Public Transit Bus API):**
  * Hiển thị danh sách tuyến bus đi qua trường (VD: tuyến **139, 34, 38, 56...**), thời gian di chuyển (36 phút), trạm đón/trả và giá vé ước tính (6.000đ).
  * **Chiến lược Tối ưu Chi phí 0 VNĐ:** Phase 1 import dữ liệu GTFS miễn phí từ Sở GTVT vào Database nội bộ MoMo; Phase 2 mở rộng Google Maps Transit API với lớp Caching 24h.

### 5.5 Interactive Credit-Based Tuition Calculator (Utility Tính Học Phí Theo Tín Chỉ)
* **Thanh trượt tín chỉ linh hoạt (Credit Slider):** Sinh viên kéo chọn số lượng tín chỉ muốn học trong học kỳ (từ 12 đến 30 tín chỉ).
* **cơ cấu chi phí dự kiến:** Tự động tính tổng tiền học phí (`~12.600.000đ`), chi phí cơ sở vật chất và bảo hiểm.
* **CTA Chuyển đổi trực tiếp:** Nút *"Nộp học phí ngay"* dẫn dắt trực tiếp qua OneLink sang phễu Nộp học phí In-App.
* **Khối thông tin Học bổng:** Hiển thị danh sách học bổng của trường (Học bổng Xuất sắc 23.4 triệu, Học bổng Toàn phần 15.6 triệu) kèm điều kiện xét tuyển.

### 5.6 Cổng Việc Làm & AI Resume Master (`momo.vn/sinh-vien/viec-lam`)
* **Master Gateway URL:** `momo.vn/sinh-vien/viec-lam` (Cổng Master Việc Làm Sinh Viên & AI Resume Builder).
* **Bản đồ Việc làm 5km Campus:** Hiển thị danh sách vị trí việc làm part-time và thực tập sinh từ các chuỗi F&B, siêu thị, cửa hàng đối tác của MoMo (Highlands, Circle K, KFC, Co.opmart...) lọc theo bán kính 5km quanh campus.
* **AI Resume Builder & ATS Scoring:** Tạo & tải CV tự động chuẩn ATS trên Web, phân tích điểm tương thích CV với bản tả công việc (JD).
* **Luồng Chuyển Đổi 1-Tap Student Pass:** Ứng tuyển nhanh thông qua xác thực Thẻ Sinh Viên Số In-App qua OneLink, mở khóa gói voucher ưu đãi HSSV & Ví Trả Sau 0% (không yêu cầu nhận lương qua Ví).

### 5.7 Student Pass Digital Card Verification Flow
* **Quy trình xác thực 100% In-App (kích hoạt qua OneLink):**
  1. Nhập Họ tên & Mã số sinh viên (MSSV).
  2. Tải ảnh Thẻ sinh viên / Giấy xác nhận nhập học hoặc xác thực VNeID.
  3. Hệ thống AI OCR tự động đối soát trong 3 giây.
* **Hiển thị Thẻ Sinh Viên Số (Visual Digital Pass):**
  * Thẻ ảo thiết kế hiệu ứng kim loại sang trọng kèm MoMo Chip, mã Barcode và thông tin sinh viên.
  * Mở khóa chuỗi đặc quyền: Giảm 50% xem phim, Hoàn 10% vé xe buýt/Grab, Gói Data 4G giá rẻ.

### 5.8 Octalysis Gamification & Daily Quests (Thử Thách Hàng Ngày)
* **Daily Login Streak:** Điểm danh ngọn lửa Streak nhận Xu thưởng MoMo.
* **Cửa hàng Đổi Quà (Coins Reward Shop):** Đổi Xu lấy voucher ăn uống, vé xem phim, Data 4G.
* **Thử thách Sinh viên:** *"Xác thực thẻ SV"*, *"Thanh toán 1 đơn hàng quanh trường"*, *"Viết review trường"*.

### 5.9 Multi-Campus Review & Rating Engine (Phân Phối Nội Dung Review Đại Học Từ Student Pass)

* **Vai Trò Phân Phối Của Kênh Web (`momo.vn/sinh-vien/[ten-truong]`):**
  * **Cổng hiển thị công khai (Public Distribution Gateway):** Tiếp nhận dữ liệu review đã được xác thực từ Student Pass App, hiển thị công khai trên Web không cần đăng nhập nhằm đón lượng truy cập tìm kiếm tự nhiên từ Google Search và AI Search (GEO).
  * **Tối ưu SEO/GEO Schema Markup:** Khai báo cấu trúc dữ liệu chuẩn `AggregateRating` và `Review` theo Google Rich Snippets để hiển thị trực tiếp số sao trung bình, số lượng đánh giá trên trang kết quả tìm kiếm Google cho từ khóa `review trường [tên trường]`.
  * **Đòn bẩy lòng tin (Verified Student Trust Layer):** Hiển thị rõ nhãn "Sinh viên đã xác thực" (Verified Student Badge) kèm logo trường trên từng bài review để khẳng định tính khách quan, khác biệt hoàn toàn với các diễn đàn review không xác thực hiện nay.

* **cơ cấu 5 Tiêu Chí Đánh Giá Cốt Lõi (Multi-Criteria Rating):**
  1. Khuôn viên & Cảnh quan trường (Campus Environment)
  2. Thư viện & Thiết bị học tập (Academic Facilities)
  3. Canteen & Giá cả dịch vụ (Canteen & Service Pricing)
  4. An ninh & Bãi đỗ xe (Security & Parking)
  5. Vị trí & Khoảng cách Trọ/KTX (Location & Dorm Accessibility)

* **Vận Hành Luồng Hai Chiều (Dual-Loop Content Cycle):**
  * **Chiều đọc & Thu hút (Web Out-App):** Người dùng vãng lai / Tân sinh viên tìm kiếm thông tin trường trên Google ➔ Đọc bài review xác thực trên Web Hub ➔ Nhấp CTA OneLink "Viết review / Đánh giá trường".
  * **Chiều đóng góp & Xác thực (App In-App):** Mở App MoMo ➔ Sinh viên thực hiện eKYC Thẻ Sinh Viên Số trên Student Pass ➔ Viết review & chấm điểm ➔ Hệ thống kiểm duyệt tự động/bán tự động ➔ Đẩy dữ liệu ra hiển thị công khai trên Web Hub.

* **Nguồn Nội Dung & Đội Ngũ Đại Sứ (Student Pass Ambassador Network):**
  * **Đội ngũ nòng cốt Phase 1:** Khai thác mạng lưới Ambassador tại 22+ trường trọng điểm để tạo nguồn bài đánh giá chất lượng cao, đúng insight sinh viên, phủ đủ các cơ sở (Multi-Campus).
  * **Cơ chế mở rộng Phase 2:** Duy trì bài viết chất lượng qua các mùa Ambassador tiếp theo, kết hợp gamification tặng Xu thưởng MoMo khi sinh viên xác thực viết review.

### 5.10 Student Privileges & AI Tools
* Gợi ý gói **Google Gemini Student Offer**, voucher mua Laptop sinh viên, ưu đãi Data 4G/5G.
* Khối câu hỏi thường gặp **FAQs Sinh Viên** (Học vụ: *Nợ môn, Rớt môn, Điểm rèn luyện, Đăng ký tín chỉ, Thẻ SV*).

## VII. TECHNICAL ARCHITECTURE, ANALYTICS & CMS GOVERNANCE

### 7.1 Analytics & Attribution Tech Stack
* **Umami Analytics (Web Behavior Tracking):** Đo lường 100% hành vi trên Web (`momo.vn/sinh-vien`): lượt xem trang (Pageviews), luồng chuyển dịch (User Flow), độ sâu cuộn (Scroll Depth), click CTA, tương tác công cụ tính học phí và xem bài review.
* **OneLink / AppsFlyer (Web-to-App Attribution):** Xử lý luồng chuyển tiếp từ Web sang App MoMo, đo lường tỷ lệ Open App, Install App và Attribution lượt xác thực Thẻ Sinh Viên Số & giao dịch In-App.

### 7.2 CMS Governance (MoSpark CMS / MS Park)
* Bàn giao công cụ **MoSpark CMS** cho đội ngũ Operations (Vận hành):
  * Tự do quản lý bài viết, tạo mới trang trường học theo mẫu chuẩn pSEO Schema.
  * Chủ động bật/tắt các khối UI Block (Banner, Grid Icon, Widget Cửa hàng gần đây, Khối Việc làm) mà không cần can thiệp lập trình viên.

### 7.3 Regulatory Compliance & Risk Governance
* **Tuân thủ quy định NHNN (Thông tư 23 & 40/2024/TT-NHNN):** Mọi giao dịch tài chính, hoàn tiền, giải ngân Ví Trả Sau **100% thực hiện trong App MoMo đã KYC**. Web Platform (`momo.vn/sinh-vien`) đóng vai trò là kênh hiển thị nội dung công khai và điều hướng về App qua OneLink.
* **Quy Chuẩn Kỹ Thuật & Kiến Trúc API Xe Buýt 0 VNĐ (Public Transit GTFS & PostGIS Spec):**
  * **Phase 1 (MVP - Chi phí 0 VNĐ & Tốc độ < 50ms):**
    * Import dữ liệu chuẩn mở GTFS (`routes.txt`, `stops.txt`, `stop_times.txt`) từ Sở GTVT TP.HCM (`ebus.buyttphcm.com.vn`) & Hà Nội (`timbus.vn`) vào Database nội bộ MoMo (`PostgreSQL` + `PostGIS`).
    * Sử dụng truy vấn không gian PostGIS `ST_DWithin` để quét chính xác các trạm bus và tuyến bus chủ lực trong bán kính 500m - 1km quanh tọa độ GPS của từng cơ sở trường ĐH với **tốc độ phản hồi < 50ms và chi phí API 0 VNĐ**.
  * **Tích hợp Direct REST API Endpoints Nhà Nước:**
    * API Danh sách tuyến TP.HCM: `GET http://ebus.buyttphcm.com.vn/api/Route/GetAll`
    * API Trạm dừng theo tuyến: `GET http://ebus.buyttphcm.com.vn/api/Route/GetRouteDetail?routeId={route_id}`
    * API Trạm dừng quanh tọa độ: `GET http://ebus.buyttphcm.com.vn/api/Stop/GetStopsByBound`
    * AJAX Endpoints từ `timbus.vn` (Hà Nội).
  * **Phase 2 (Real-time Tracking & Dynamic Walking Directions):**
    * Tích hợp Google Maps Transit Directions API với lớp **Redis Cache 24h** tận dụng $200 credit miễn phí hàng tháng của Google Cloud giúp tiết kiệm 99% chi phí API phát sinh.
### 7.4 Data Integrity & Anti-Fake Metrics Policy (Quy Tắc Quản Trị Dữ Liệu Thực - Không Chế Số Trên Web Platform)
* **Nguyên Tắc Cốt Lõi (Zero Fake Data Guarantee):** Kênh Web Platform (`momo.vn/sinh-vien`) **TUYỆT ĐỐI KHÔNG** tự chế số, hardcode số liệu giả, tạo đánh giá ảo hoặc bịa đặt chỉ số xếp hạng trường học.
* **Cơ Chế Đồng Bộ Số Liệu Thực (Authentic Data Pipeline):**
  1. **Số liệu Review / Rating:** 100% điểm sao trung bình, lượt đánh giá và bài viết review hiển thị trên Web phải đồng bộ trực tiếp từ Database của Student Pass App (nơi dữ liệu đã được xác thực qua eKYC Thẻ Sinh Viên Số).
  2. **Số liệu Học phí & Điểm chuẩn:** 100% dữ liệu điểm chuẩn xét tuyển và khung học phí tín chỉ được đối soát chính xác theo đề án tuyển sinh chính thức của từng trường đại học (`/Users/hienhv/Downloads/Content Structure.xlsx`).
  3. **Số liệu Tuyến xe buýt & Tiện ích:** 100% thông tin trạm dừng xe buýt, khoảng cách GPS và địa điểm SME được truy vấn thực tế qua PostgreSQL/PostGIS và API của Sở GTVT.
  4. **Chỉ số đo lường Traffic & Conversion:** 100% báo cáo lưu lượng truy cập (Total Traffic, Organic Search, CTR) được đo lường thực tế qua Umami Analytics và AppsFlyer OneLink.

* **Hiệu năng kỹ thuật:** Thiết kế chuẩn **Mobile-First**, tốc độ tải trang dưới 1,5 giây.
