# BRD: Merchant Hub - Cổng Thông Tin & Nền Tảng Đối Tác Merchant MoMo

> - **Dự án:** Merchant Hub (Web Platform & Merchant Profile Identity)
> - **Khối phụ trách:** Growth Platform Division (GPD)
> - **Owner:** Web Platform Team (GPD)

## I. Executive Summary

### 1.1 Core Problems & Objectives
* **Vấn đề thực tế (Problem Statement):** Hàng triệu hộ kinh doanh cá thể, cửa hàng offline và chuỗi SME tại Việt Nam đang thiếu sự hiện diện số hóa chuẩn SEO trên Open Web (Google Search, Google Maps, AI Search). Họ đối mặt với chi phí quảng cáo đắt đỏ, khó tiếp cận khách hàng tiềm năng xung quanh khu vực (Local GEO), đồng thời gặp rào cản trong việc quản lý doanh thu, phòng tránh thất thoát khi nhận chuyển khoản và tiếp cận các giải pháp tài chính linh hoạt.
* **Mục tiêu định lượng:** Hợp nhất toàn bộ nhu cầu tìm kiếm địa điểm mua sắm, ăn uống O2O và kéo **>1.500.000 - 2.500.000 Organic Visits/tháng** về `momo.vn/merchant`, chuyển đổi lượng truy cập tự nhiên này thành giao dịch tại cửa hàng offline và tạo nguồn leads tư vấn thiết bị Loa báo chuyển tiền Soundbox.
* **Triết lý cốt lõi:** **"Một Cửa Hàng - Một Trang Định Danh Số"**, biến địa chỉ/thương hiệu của merchant thành trung tâm kết nối Online-to-Offline (O2O) tự động:
  1. **Một lần khai báo, số hóa chuẩn SEO trọn đời:** Đưa thông tin cửa hàng, menu/sản phẩm, địa chỉ Google Maps, giờ mở cửa và phương thức thanh toán MoMo lên Open Web chuẩn SEO chỉ trong 3 phút.
  2. **Chủ động thu hút, tự động chuyển đổi:** Tự động phát hành Voucher O2O 1-click trên Web, dẫn dắt khách hàng ghé shop quét mã MoMo / Ví Trả Sau, và giới thiệu giải pháp Loa báo chuyển tiền Soundbox chống thất thoát.
  3. **Một hệ sinh thái cho mọi hộ kinh doanh:** Kết nối chủ shop với toàn bộ tiện ích tài chính & tăng trưởng của MoMo (Ví Trả Sau, Loa Soundbox, QR Cửa hàng, MoMo Rewards).

### 1.2 Situation - Complication - Resolution
* **Situation (Bối cảnh & Vai trò Website):** Khi phát sinh nhu cầu ăn uống, mua sắm, tìm tiệm làm đẹp, dịch vụ sửa chữa hay siêu thị tiện lợi gần nhất, phản xạ tự nhiên của người dùng là tra cứu trên Google hoặc các công cụ AI Search (ChatGPT, Gemini, Perplexity). Website `momo.vn` đóng vai trò là **"cửa ngõ hứng nhu cầu O2O và cổng định danh Merchant"**. Bằng các tiện ích tra cứu địa điểm, menu, bảng giá và kho voucher O2O trực tuyến, Website giải quyết tức thời nhu cầu của người dùng, từ đó thu thập dữ liệu vị trí và thiết lập Hồ sơ Cửa hàng (Merchant Profile).
* **Complication (Khó khăn & Thách thức):** Nếu thông tin merchant chỉ nằm sâu trong ứng dụng di động đóng (App-only ecosystem), MoMo sẽ hoàn toàn vô hình trước hàng chục triệu lượt tìm kiếm tự nhiên ngoài Open Web. Hậu quả là lượng Traffic có ý định mua sắm cao (High purchase intent) sẽ chảy sang các nền tảng bên thứ ba (ShopeeFood, Grab, Foody), đồng thời việc ép người dùng tải App ngay lần đầu tìm kiếm địa điểm sẽ tạo ra rào cản đứt gãy lớn.
* **Resolution (Giải pháp):** Xây dựng **Merchant Hub** hoạt động theo mô hình Product-Led Growth (PLG) & Hub-and-Spoke: Hứng traffic tự nhiên từ Open Web qua các Utility Category Spoke Pages (Đồ ăn, Đồ uống, Bách hoá, Làm đẹp, Mua sắm...)  ➔  Khởi tạo Hồ sơ Cửa hàng (Merchant Profile)  ➔  Điều hướng Web-to-App (W2A) để thu thập Voucher O2O & thực hiện giao dịch quét QR thanh toán tại shop.

### 1.3 Product-Led Growth (PLG) Strategy
Cơ chế PLG của Merchant Hub dựa trên 5 "Phễu Tiện Ích Thu Hút" (Acquisition & Engagement Hooks) giải quyết nhu cầu tìm kiếm tức thì ngoài Open Web để dẫn dắt người dùng tự nguyện khám phá cửa hàng và chuyển đổi sang App (Web-to-Merchant-to-App Flywheel):

1. **Phễu Tra Cứu Địa Điểm & Menu (Acquisition Gate):** Xem vị trí Google Maps, menu/bản giá sản phẩm và đánh giá cửa hàng gần đây không cần đăng nhập  ➔  Bấm "Thu thập Voucher O2O"  ➔  Dẫn dắt kích hoạt App MoMo.
2. **Phễu Săn Voucher O2O (Conversion Hook):** Nhận voucher giảm giá trực tiếp trên Web với 1-click  ➔  Thúc đẩy người dùng di chuyển đến cửa hàng offline quét mã MoMo / Ví Trả Sau để sử dụng voucher.
3. **Phễu Đăng Ký Loa Soundbox (B2B Merchant Lead Gen Hook):** Landing page & Widget giới thiệu thiết bị Loa báo chuyển tiền Soundbox cho chủ cửa hàng  ➔  Điền form tư vấn nhận cuộc gọi từ bộ phận kinh doanh M4B.
4. **Phễu Cửa Hàng Hỗ Trợ Ví Trả Sau (High-Value Intent Hook):** Tra cứu danh sách cửa hàng/chuỗi mua sắm chấp nhận thanh toán Ví Trả Sau 0% lãi suất  ➔  Dẫn dắt kích hoạt Ví Trả Sau và mua sắm đơn hàng giá trị cao.
5. **Phễu Đánh Giá & MoMo Rewards (Retention Hook):** Người dùng quét QR thanh toán tại merchant được tích điểm đổi quà MoMo Rewards  ➔  Khuyến khích người dùng quay lại đánh giá cửa hàng trên Web Platform.

### 1.4 Key Metrics & Targets

#### Dual North Star Metrics

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Platform Layer</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">North Star Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Definition</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Strategic Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Platform</strong> <em>(Primary Goal)</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Total Organic Web Traffic</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổng lượt truy cập tự nhiên từ Google Search và AI Search vào các trang Merchant Pages & Category Hubs mỗi tháng.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>1.5M - 2.5M Visits/tháng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mục tiêu cốt lõi: Hứng tối đa nhu cầu tìm kiếm địa điểm, ăn uống, mua sắm O2O ngoài Open Web (~15M+ volume/tháng).</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>In-App & Merchant Layer</strong> <em>(Secondary Layer)</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Voucher Redemption Rate & Soundbox Leads</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tỷ lệ đổi Voucher O2O thành công tại shop & Tổng số Leads tư vấn mua thiết bị Soundbox từ chủ shop.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Voucher Redemption >35%</strong><br><strong>Soundbox Leads ≥ 15.000/tháng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đo lường hiệu quả O2O chuyển đổi traffic Web thành giao dịch thực tế tại cửa hàng & doanh thu phần cứng/dịch vụ M4B.</td>
    </tr>
  </tbody>
</table>

#### Web Platform Metric Tree

1. **Organic Traffic & Search Reach**
   * **Đồ Ăn & Nhà Hàng:** Top 1-3 Organic Search Google cụm từ khóa tìm kiếm địa điểm ăn uống, đạt **>600.000 visits/tháng**.
   * **Đồ Uống & Quán Cà Phê:** Hứng **>500.000 visits/tháng** nhu cầu tìm quán cà phê, trà sữa gần đây.
   * **Bách Hoá & Siêu Thị Mini:** Hứng **>350.000 visits/tháng** tìm tạp hoá, chợ truyền thống, cửa hàng tiện lợi.
   * **Làm Đẹp - Sức Khỏe & Mua Sắm:** Hứng **>400.000 visits/tháng** tìm spa, hair salon, cửa hàng thời trang, điện máy.

2. **Web Engagement & Identification**
   * **Tỷ Lệ Thu Thập Voucher (Claim Rate):** Đạt **15% - 20%** lượt truy cập trang Merchant thực hiện 1-click thu thập Voucher O2O.
   * **Tỷ Lệ Điều Hướng Web-to-App (W2A CVR):** Đạt **>30%** người dùng thu thập voucher thực hiện mở App MoMo để lưu voucher/thanh toán.
   * **Tỷ Lệ Đăng Ký Tư Vấn Soundbox:** Đạt **3% - 5%** chủ shop truy cập trang Soundbox điền thông tin tư vấn thành công.

3. **Commercial Conversion**
   * **O2O Transactions:** Đạt **>250.000 giao dịch QR thành công/tháng** tại merchant xuất phát từ các chiến dịch O2O Voucher trên Web.
   * **Ví Trả Sau Activation:** Đạt **>10.000 lượt kích hoạt/sử dụng Ví Trả Sau** tại các merchant thuộc danh mục Mua sắm & Điện máy.

#### Phase 1 Pilot Targets (Cell Team Alignment T9 - T12/2026)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">STT</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chỉ Số (Key Metric)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Baseline (H1/2026)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Target Phase 1 Pilot (T9 - T12/2026)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi Chú Thực Thi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phase 1 Organic Traffic</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">450K/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>1.500.000 Visits</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mở rộng SEO Hub theo 14 nhóm ngành nghề chính & 53 ngành nghề phụ</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web-to-App Conversion Rate (W2A CVR)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">18%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>>= 30% CVR</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tỷ lệ từ xem Web Merchant Page sang Thu thập Voucher / Mở App MoMo</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>O2O Voucher Redemptions</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">35.000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>120.000 Redemptions</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số lượt sử dụng voucher thành công khi quét QR thanh toán tại shop</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Soundbox Qualified Leads</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2.100/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>8.500 Leads/tháng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Leads chủ cửa hàng đăng ký tư vấn mua thiết bị Loa Soundbox từ Web</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>SEO Ranking (Merchant & Category Keywords)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Top 15-30</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>Top 1 - Top 10 Keywords</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đưa các cụm từ khóa địa điểm (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">quán ăn gần đây</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">tiệm cà phê mo mo</code>...) lọt Top 1-10</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Merchant Profile Verified Rate</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">5%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>>25% Verified</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tỷ lệ chủ cửa hàng thực hiện xác minh quyền sở hữu trang Merchant Page</td>
    </tr>
  </tbody>
</table>

## II. Market Context & Strategy

### 2.1 Market Sizing & Opportunity
* **Quy mô thị trường Hộ kinh doanh & SME tại Việt Nam:**
  * **Hộ kinh doanh cá thể:** Hơn 5,2 triệu hộ kinh doanh cá thể đang hoạt động trên toàn quốc.
  * **Doanh nghiệp SME:** Hơn 900.000 doanh nghiệp vừa và nhỏ, trong đó nhóm bán lẻ và F&B chiếm hơn 45%.
* **Cơ hội O2O từ M4B & GPD:** Việc MoMo sở hữu mạng lưới hàng trăm ngàn merchant chấp nhận thanh toán QR kết hợp với năng lực thu hút traffic tự nhiên trên Web tạo ra vòng lặp O2O hoàn chỉnh: Tìm kiếm trên Google  ➔  Xem Merchant Page  ➔  Thu thập Voucher O2O  ➔  Ghé cửa hàng quét QR MoMo / Ví Trả Sau  ➔  Đăng ký Loa Soundbox chống thất thoát.

### 2.2 Cross-BU Synergy & Data Consolidation
MoMo sở hữu lợi thế cạnh tranh tuyệt đối khi kết hợp sức mạnh giữa **Web Platform (GPD)**, **M4B (Merchant Platform)**, **Ví Trả Sau (FS)** và **Loa Soundbox (VTTI/Hardware)**:
1. **Quy mô kho dữ liệu Merchant:** MoMo đang quản lý tệp dữ liệu hơn **500.000+ điểm chấp nhận thanh toán**, tạo tiền đề số hóa thành 500.000+ Merchant Pages chuẩn SEO trên Open Web mà không tốn chi phí khởi tạo nội dung ban đầu.
2. **Cơ chế Bán Chéo Dịch Vụ Tài Chính (Cross-sell Synergy):** Khách hàng tra cứu cửa hàng mua sắm/điện máy sẽ được gợi ý nhãn nhúng *"Hỗ trợ Ví Trả Sau - Mua trước trả sau 0%"*, thúc đẩy tăng trưởng nợ vay lành mạnh cho mảng FS. Đồng thời, chủ shop xem trang Merchant Page của chính mình sẽ được hệ thống gợi ý trang bị Loa Soundbox để tự động hóa việc nhận tiền chuyển khoản.
3. **Cá nhân hóa trải nghiệm theo Ngành nghề:** Dựa trên bộ danh mục 14 ngành nghề chính & 53 ngành nghề phụ để đề xuất chương trình khuyến mãi và giao diện Merchant Page tối ưu cho từng loại hình kinh doanh (Ví dụ: Ngành F&B hiển thị Menu/Bảng giá; Ngành Làm đẹp hiển thị Bảng giá dịch vụ & Đặt lịch; Ngành Bách hoá hiển thị danh mục ưu đãi O2O).

### 2.3 Search Demand Analysis
Theo phân tích dữ liệu thực tế trên Open Web tại Việt Nam, tổng nhu cầu tìm kiếm địa điểm ăn uống, mua sắm, dịch vụ local và giải pháp kinh doanh vượt **15.8 triệu lượt/tháng**. Đây là hệ thống nhu cầu cốt lõi mà Merchant Hub tập trung đón nhận trọn vẹn qua mô hình Hub-and-Spoke:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">STT</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhu Cầu / Use Case / Ngành Nghề</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Volume Search / Tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đặc Điểm Ý Định Tìm Kiếm (Search Intent) & Vai Trò Trong Merchant Hub</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đồ Ăn (Nhà hàng, Quán ăn, Fastfood)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>5.200.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhu cầu F&B lớn nhất thị trường. Hứng từ khóa tìm quán ăn gần đây, tiệm bánh, nhà hàng buffet.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đồ Uống (Cà phê, Trà sữa, Sinh tố)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>3.800.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic có tần suất lặp lại cao hàng ngày. Phễu kéo người dùng trẻ săn Voucher O2O 1-click.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>3</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bách Hoá & Siêu Thị (Tạp hoá, Tiện lợi)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>2.500.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tìm siêu thị tiện lợi, tạp hoá gần đây, chợ truyền thống. Phễu đẩy thanh toán QR quét mã nhanh.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>4</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Làm Đẹp - Sức Khỏe (Spa, Hair, Nail, Gym)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>1.600.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhu cầu dịch vụ chăm sóc cá nhân có ARPU cao. Phễu tư vấn ưu đãi Ví Trả Sau & Đặt lịch.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>5</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Mua Sắm (Thời trang, Điện máy, Mẹ & bé)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>1.200.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhu cầu mua sắm sản phẩm giá trị lớn. Phễu chuyển đổi chính cho dịch vụ Ví Trả Sau 0%.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>6</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Dịch Vụ Xe & Nhà Cửa (Rửa xe, Giặt ủi)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>850.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tìm tiệm sửa xe, rửa xe, giặt ủi, dọn dẹp nhà cửa tại địa phương (Local GEO intent).</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>7</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Loa Báo Chuyển Tiền / Soundbox</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>150.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhu cầu của chủ shop tìm giải pháp loa thông báo chuyển tiền tự động. Phễu B2B Lead Gen trực tiếp.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>8</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Điểm Chấp Nhận Thanh Toán MoMo</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>280.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khách hàng chủ động tra cứu địa điểm dùng Ví MoMo, Ví Trả Sau và săn khuyến mãi MoMo Rewards.</td>
    </tr>
  </tbody>
</table>

## III. Product Strategy & Core Flows

### 3.1 Multi-sided Value Proposition
* **Cho Chủ Cửa Hàng / Merchant (B2B):** Sở hữu một trang thông tin doanh nghiệp chuẩn SEO chuyên nghiệp hoàn toàn miễn phí trên `momo.vn/merchant`, tiếp cận hàng triệu khách hàng tiềm năng xung quanh, tăng lượt ghé shop offline nhờ voucher O2O, và tiếp cận giải pháp phần cứng Loa Soundbox chống thất thoát doanh thu.
* **Cho Khách Hàng Tiêu Dùng (Consumers):** Tra cứu địa điểm ăn uống, mua sắm uy tín gần nhất; xem trước menu, bảng giá, giờ mở cửa và đánh giá thực tế; săn voucher giảm giá O2O 1-click và linh hoạt chọn phương thức thanh toán (Ví MoMo, Ví Trả Sau).
* **Cho Nền Tảng MoMo (Acquisition & Monetization Engine):** Thu hút dòng traffic tự nhiên giá rẻ khổng lồ từ Open Web (Zero-ad cost), mở rộng tệp Merchant M4B active, tạo dòng doanh thu từ bán thiết bị Loa Soundbox và kích hoạt hạn mức Ví Trả Sau.

### 3.2 Web Onboarding Flow
```
[1. Tìm trên Google "Quán ăn X / Cửa hàng Y gần đây"] ──► [2. Xem Merchant Page trên Web momo.vn]
                                                                        │
                                                                        ▼
[4. Quét QR Thanh toán MoMo / Ví Trả Sau tại Shop] ◄─── [3. Thu thập Voucher O2O 1-Click trên Web]
```

### 3.3 Kick-off Alignment Rules & Web Compliance
1. **Quy tắc Bảo mật & Tuân thủ Thông tin trên Web (Web Compliance Rule):** Khi hiển thị trang Merchant Page công khai trên Web, **chỉ hiển thị các thông tin doanh nghiệp/cửa hàng công khai** (Họ tên thương hiệu, Địa chỉ Google Maps, Giờ mở cửa, Menu/Sản phẩm public, Ưu đãi voucher công khai). Tuyệt đối **không hiển thị doanh thu cửa hàng, thông tin cá nhân chủ shop (CCCD, Số điện thoại riêng, Tài khoản ngân hàng liên kết)** trừ khi chủ shop đã đăng nhập và xác thực chính chủ.
2. **Nguyên tắc Chuyển đổi Thanh toán (NHNN Compliance):** Mọi thao tác thu thập voucher có giá trị quy đổi tiền mặt và giao dịch thanh toán bắt buộc được xử lý chuyển tiếp qua App MoMo đã KYC chính chủ. Web Platform đóng vai trò hiển thị thông tin, tối ưu SEO và thu thập leads.
3. **Mô hình tiếp cận theo Ngành nghề (Category-first Approach):** Tối ưu SEO Hub theo 14 nhóm ngành nghề chính trước, sau đó phát triển 53 trang ngành nghề phụ để phủ trọn toàn bộ cụm từ khóa tìm kiếm địa điểm local.

### 3.4 Core Use Cases & KPIs Matrix

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Use Case (Hệ Sinh Thái Merchant)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Search Volume</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả Chức Năng & Luồng Trải Nghiệm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KPIs Cam Kết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Merchant Page chuẩn SEO</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>~5.2M</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang thông tin chi tiết cửa hàng (Địa chỉ Maps, Hotline, Giờ mở cửa, Menu, Đánh giá).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Top 1-3 Organic Search; Time-on-page >1.5 phút.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>O2O Voucher Claim Engine</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>~3.8M</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thu thập voucher giảm giá O2O trên Web với 1-click để sử dụng khi quét QR thanh toán tại shop.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tỷ lệ Claim Voucher >15%; Tỷ lệ sử dụng tại shop >35%.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Soundbox Lead Gen</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>~150K</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chủ shop xem tính năng Loa báo chuyển tiền Soundbox và điền form đăng ký tư vấn giải pháp.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">>8.500 Leads tư vấn/tháng; Tỷ lệ chốt đơn >20%.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Local GEO Merchant Search</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>~2.5M</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ tra cứu điểm bán chấp nhận MoMo theo bán kính GPS (500m, 1km, 3km) và theo Tỉnh thành/Quận huyện.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hứng tệp tìm kiếm local; >300k lượt chỉ đường/tháng.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Ví Trả Sau Merchant Locator</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>~280K</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bộ lọc chuyên biệt danh sách cửa hàng/chuỗi siêu thị cho phép thanh toán qua Ví Trả Sau 0% lãi suất.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">>10.000 giao dịch Ví Trả Sau được kích hoạt/tháng.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Menu & Product Explorer</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>~1.2M</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khách hàng xem thực đơn, hình ảnh món ăn, bảng giá dịch vụ trước khi quyết định đến cửa hàng.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tỷ lệ xem Menu >45% tổng lượt truy cập trang Merchant.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Review & Rating Platform</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>~850K</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xem đánh giá từ cộng đồng người dùng MoMo đã thực hiện giao dịch thực tế tại merchant.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">>50.000 lượt đánh giá mới được gửi mỗi tháng.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Merchant Verification (Claim Store)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>Internal</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chủ cửa hàng xác minh quyền sở hữu trang Merchant Page để tự cập nhật Menu & phát hành Voucher.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">>25% Merchant Active hoàn tất xác minh trang.</td>
    </tr>
  </tbody>
</table>

## IV. Target Personas & JTBD

### 4.1 Target Personas
* **Persona 1: Chủ hộ kinh doanh cá thể & Chuỗi SME (Merchant B2B):** Sở hữu cửa hàng ăn uống, tạp hoá, tiệm làm đẹp hoặc chuỗi cửa hàng bán lẻ. Bận rộn, ít kiến thức kỹ thuật, muốn tăng lượng khách ghé shop nhưng không có ngân sách chạy quảng cáo đắt đỏ; cần giải pháp nhận tiền chuyển khoản minh bạch, không lo bị lừa đảo giả mạo biên lai.
* **Persona 2: Khách hàng tiêu dùng O2O (Consumer End-User):** Người dùng trẻ di chuyển thường xuyên, thích khám phá quán ăn, tiệm cà phê mới; có thói quen gõ Google tra cứu địa điểm trước khi đi; muốn săn voucher ưu đãi và thích thanh toán không dùng tiền mặt (MoMo, Ví Trả Sau).
* **Persona 3: Chủ chuỗi thương hiệu lớn / Doanh nghiệp đối tác (Enterprise Partner):** Các chuỗi F&B, chuỗi siêu thị tiện lợi (KFC, Highlands, Circle K, WinMart). Nhu cầu: phủ sóng thương hiệu số lượng lớn, đẩy các chiến dịch Marketing O2O quy mô toàn quốc.

### 4.2 Consumer Journey (4 Stages)
1. **Giai đoạn 1 (Trigger):** Phát sinh nhu cầu ăn uống, mua sắm hoặc tìm dịch vụ gần vị trí hiện tại ("tìm quán cà phê đẹp gần đây", "tiệm giặt ủi quận 1").
2. **Giai đoạn 2 (Search & Discovery):** Tìm kiếm trên Google / AI Search  ➔  Truyc cập trang Category Hub hoặc Merchant Page trên `momo.vn/merchant` không cần đăng nhập.
3. **Giai đoạn 3 (Utility & Identification):** Xem menu, địa chỉ Google Maps, đánh giá  ➔  Bấm 1-click "Thu thập Voucher O2O"  ➔  Khởi tạo liên kết định danh trên Web.
4. **Giai đoạn 4 (App Automation & Retention):** Chuyển đổi Web-to-App (W2A) mở App MoMo  ➔  Đến shop quét QR thanh toán sử dụng voucher  ➔  Tích điểm MoMo Rewards & Đánh giá cửa hàng.

### 4.3 Multi-sided JTBD Matrix

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đối tượng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Job-To-Be-Done chính (Job Statement)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pain Points cần giải quyết</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thay đổi sau khi dùng Merchant Hub</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Chủ cửa hàng (Merchants)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>"Giúp cửa hàng của tôi xuất hiện chuyên nghiệp trên Google, thu hút thêm nhiều khách hàng quanh khu vực ghé shop và tự động hóa việc nhận tiền chuyển khoản để tôi yên tâm kinh doanh."</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Không có website riêng, chi phí làm SEO quá đắt.<br>- Khó thu hút khách mới xung quanh.<br>- Lo bị lãng quên hoặc bị lừa chuyển khoản giả.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Có trang Merchant Page chuẩn SEO miễn phí.<br>- Tiếp cận tệp khách MoMo qua Voucher O2O.<br>- Trang bị Loa Soundbox đọc tiền tự động.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Khách hàng (Consumers)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>"Giúp tôi nhanh chóng tìm được địa điểm ăn uống, mua sắm uy tín gần nhất với đầy đủ thông tin menu, bảng giá và voucher giảm giá để tiết kiệm thời gian và chi phí."</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Thông tin cửa hàng trên mạng thiếu chính xác.<br>- Không biết cửa hàng có nhận thanh toán MoMo/Ví Trả Sau không.<br>- Bỏ lỡ các ưu đãi giảm giá tại shop.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Tra cứu chuẩn xác menu/địa chỉ trên Web.<br>- Biết rõ điểm nhận MoMo & Ví Trả Sau.<br>- Săn Voucher O2O 1-click tiện lợi.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nền tảng (MoMo Platform)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>"Giúp MoMo đón nhận trọn vẹn lượng traffic tìm kiếm địa điểm O2O khổng lồ từ Open Web, chuyển đổi người dùng Web thành giao dịch tại shop và bán chéo giải pháp Soundbox/Ví Trả Sau."</em></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Chi phí thu hút người dùng mới (CAC) ngày càng cao.<br>- Merchant M4B thiếu công cụ kéo traffic O2O.<br>- Nguồn leads bán phần cứng Soundbox bị hạn chế.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Hứng traffic tự nhiên từ SEO Hub (Zero-ad cost).<br>- Tăng sản lượng giao dịch QR O2O In-App.<br>- Tạo nguồn leads bán Loa Soundbox liên tục.</td>
    </tr>
  </tbody>
</table>

## V. Site Structure & SEO/GEO Strategy

### 5.1 Hub-and-Spoke Sitemap Architecture

Tích hợp trọn vẹn bộ danh mục **14 Ngành nghề chính** và **53 Ngành nghề phụ** từ dữ liệu chuẩn ngành nghề MoMo:

#### A. Nhóm Trang Category Hubs & Spoke Pages (`/merchant/*`)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngành nghề chính (Level 1)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Category Canonical</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Danh sách Ngành nghề phụ (Level 2) & URL Mở Rộng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục Tiêu SEO & Intent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>1. Đồ ăn</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/do-an</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khu ẩm thực (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/do-an/khu-am-thuc</code>)<br>Nhà hàng (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/do-an/nha-hang</code>)<br>Quán ăn đường phố (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/do-an/quan-an-duong-pho</code>)<br>Quán ăn nhanh (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/do-an/quan-an-nhanh</code>)<br>Tiệm ăn (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/do-an/tiem-an</code>)<br>Tiệm bánh kẹo (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/do-an/tiem-banh-keo</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hứng <strong>~5.2M volume/tháng</strong>. SEO các từ khóa địa điểm ăn uống, nhà hàng, quán ăn gần đây.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>2. Đồ uống</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/do-uong</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cà phê (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/do-uong/ca-phe</code>)<br>Sinh tố (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/do-uong/sinh-to</code>)<br>Trà sữa (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/do-uong/tra-sua</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hứng <strong>~3.8M volume/tháng</strong>. SEO từ khóa tiệm cà phê, trà sữa, sinh tố gần bạn.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>3. Bách hoá</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/bach-hoa</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chợ truyền thống (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bach-hoa/cho-truyen-thong</code>)<br>Cửa hàng thực phẩm (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bach-hoa/cua-hang-thuc-pham</code>)<br>Cửa hàng tiện lợi (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bach-hoa/cua-hang-tien-loi</code>)<br>Máy bán hàng tự động (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bach-hoa/may-ban-hang-tu-dong</code>)<br>Siêu thị (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bach-hoa/sieu-thi</code>)<br>Tạp hóa (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bach-hoa/tap-hoa</code>)<br>Trung tâm thương mại (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bach-hoa/trung-tam-thuong-mai</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hứng <strong>~2.5M volume/tháng</strong>. SEO từ khóa siêu thị mini, tiệm tạp hoá, cửa hàng tiện lợi 24/7.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>4. Làm đẹp - Sức khỏe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/lam-dep-suc-khoe</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dịch vụ làm móng (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/lam-dep-suc-khoe/nail</code>)<br>Dịch vụ làm tóc (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/lam-dep-suc-khoe/lam-toc</code>)<br>Dịch vụ massage, spa (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/lam-dep-suc-khoe/massage-spa</code>)<br>Dịch vụ thẩm mỹ (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/lam-dep-suc-khoe/tham-my</code>)<br>Gym & Fitness (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/lam-dep-suc-khoe/gym-fitness</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hứng <strong>~1.6M volume/tháng</strong>. SEO các cụm từ khóa làm đẹp, spa, thẩm mỹ viện, phòng gym.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>5. Mua sắm</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/mua-sam</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cửa hàng mẹ và bé (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/me-va-be</code>)<br>Cửa hàng thể thao (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/the-thao</code>)<br>Điện thoại/Máy tính (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/dien-thoai-may-tinh</code>)<br>Đồ lót (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/do-lot</code>)<br>Gia dụng khác (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/gia-dung</code>)<br>Giày dép (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/giay-dep</code>)<br>Hạt giống/cây kiểng (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/cay-kieng</code>)<br>Nhà sách/Đồ chơi (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/nha-sach-do-choi</code>)<br>Nội thất (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/noi-that</code>)<br>Phụ kiện thời trang (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/phu-kien-thoi-trang</code>)<br>Quần áo (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/quan-ao</code>)<br>Siêu thị điện máy (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/sieu-thi-dien-may</code>)<br>Thiết bị điện (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/thiet-bi-dien</code>)<br>Thiết bị y tế (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/thiet-bi-y-te</code>)<br>Trang sức (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/trang-suc</code>)<br>Văn phòng phẩm (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/van-phong-pham</code>)<br>Vật liệu xây dựng (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/mua-sam/vat-lieu-xay-dung</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hứng <strong>~1.2M volume/tháng</strong>. Phễu chính tư vấn thanh toán Ví Trả Sau 0% lãi suất.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>6. Dịch vụ ô tô/xe máy</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/dich-vu-o-to-xe-may</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rửa xe (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-o-to-xe-may/rua-xe</code>)<br>Sửa chữa ô tô/xe máy (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-o-to-xe-may/sua-xe</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hứng <strong>~550K volume/tháng</strong>. Kết nối hệ sinh thái Vehicle Hub & M4B Garage.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>7. Đặt dịch vụ & Vận chuyển</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/dat-dich-vu-van-chuyen</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đại lý du lịch (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dat-dich-vu-van-chuyen/dai-ly-du-lich</code>)<br>Taxi/Xe máy (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dat-dich-vu-van-chuyen/taxi-xe-may</code>)<br>Vé máy bay (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dat-dich-vu-van-chuyen/ve-may-bay</code>)<br>Vé tàu hỏa (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dat-dich-vu-van-chuyen/ve-tau-hoa</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO dịch vụ du lịch, đại lý vé và vận tải liên kết MoMo.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>8. Giải trí</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/giai-tri</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bar Club (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/giai-tri/bar-club</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO dịch vụ giải trí về đêm, bar club chấp nhận MoMo.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>9. Giáo dục</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/giao-duc</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giáo dục khác (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/giao-duc/trung-tam-hoc-tap</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO các trung tâm đào tạo, trường học đóng học phí MoMo.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>10. Hoạt động thể thao, vui chơi</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/hoat-dong-the-thao</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hoạt động thể thao (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/hoat-dong-the-thao/san-tap</code>)<br>Khu vui chơi giải trí (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/hoat-dong-the-thao/khu-vui-choi</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO các địa điểm vui chơi giải trí gia đình, sân tập thể thao.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>11. Nhà cửa & Bảo trì</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/nha-cua-bao-tri</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dịch vụ dọn dẹp (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/nha-cua-bao-tri/don-dep</code>)<br>Giặt ủi (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/nha-cua-bao-tri/giat-ui</code>)<br>Sửa chữa thiết bị, nội thất (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/nha-cua-bao-tri/sua-chua-noi-that</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hứng <strong>~300K volume/tháng</strong>. SEO tiệm giặt ủi, sửa đồ gia dụng tại địa phương.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>12. Dịch vụ thú y</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/dich-vu-thu-y</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chăm sóc thú cưng (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-thu-y/pet-shop</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO tiệm thú y, spa thú cưng, pet shop chấp nhận MoMo.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>13. Bán lẻ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/ban-le</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua sắm/Bán hàng khác (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/ban-le/khac</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang tổng hợp ngành bán lẻ chung.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>14. Viễn thông</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/vien-thong</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua thẻ cào điện thoại (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/vien-thong/the-cao</code>)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO điểm nạp tiền & đại lý viễn thông.</td>
    </tr>
  </tbody>
</table>

#### B. Nhóm Trang Landing Pages Use Case Độc Lập

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Trang / Use Case Page</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Canonical</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cấu Trúc URL Mở Rộng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mục Tiêu SEO & Intent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trang Chủ Merchant Hub</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cổng tổng hợp tra cứu địa điểm & cửa hàng MoMo toàn quốc.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Loa Soundbox MoMo</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/soundbox</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/soundbox/dang-ky</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing page giới thiệu Loa báo chuyển tiền Soundbox & Form tư vấn B2B.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Ví Trả Sau Merchant Directory</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/vi-tra-sau</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/vi-tra-sau/{category-slug}</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Danh mục cửa hàng chấp nhận thanh toán Ví Trả Sau 0%.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Kho Voucher O2O</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/voucher-o2o</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/voucher-o2o/{tinh-thanh}</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổng hợp mã giảm giá & voucher O2O claim 1-click trên Web.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Merchant Detail Page</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/{store-slug}</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/merchant/{tinh-thanh}/{store-slug}</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang thông tin chi tiết từng cửa hàng chuẩn SEO JSON-LD.</td>
    </tr>
  </tbody>
</table>

### 5.2 SEO & GEO Strategy & Schema Matrix
1. **Cấu trúc URL Địa lý Phân cấp (Local GEO pSEO):** Kết hợp Cấu trúc Ngành nghề + Tỉnh thành/Quận huyện để phủ trọn các cụm từ khóa tìm kiếm local:
   * `momo.vn/merchant/do-an/nha-hang/tp-ho-chi-minh`
   * `momo.vn/merchant/do-uong/ca-phe/ha-noi/cau-giay`
2. **Chuẩn hóa Dữ liệu Thực thể Schema.org Matrix (Structured Data):**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngành nghề chính</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Schema.org <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">@type</code> tương ứng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đã khai báo thuộc tính JSON-LD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đồ ăn / Đồ uống</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">FoodEstablishment</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Restaurant</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">CafeOrCoffeeShop</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Bakery</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">name</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">image</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">address</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">geo</code> (latitude, longitude), <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">telephone</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">priceRange</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">openingHoursSpecification</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">menu</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">acceptsReservations</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Làm đẹp - Sức khỏe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">BeautySalon</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">HairSalon</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">HealthClub</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">DaySpa</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">name</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">address</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">geo</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">telephone</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">priceRange</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">openingHoursSpecification</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bách hoá / Mua sắm</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">Store</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">ConvenienceStore</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">DepartmentStore</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">GroceryStore</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">name</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">address</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">geo</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">telephone</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">priceRange</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">paymentAccepted</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Dịch vụ ô tô/xe máy</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">AutomotiveBusiness</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">AutoRepair</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">AutoWash</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">name</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">address</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">geo</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">telephone</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">priceRange</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cửa hàng chung</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">LocalBusiness</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">name</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">address</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">geo</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">telephone</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">sameAs</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">hasMap</code></td>
    </tr>
  </tbody>
</table>

3. **Tối ưu hóa Tìm kiếm AI (Generative Engine Optimization - GEO):** Xây dựng mục FAQ chuẩn hóa câu trả lời tự nhiên (Ví dụ: *"Quán cà phê ABC có nhận thanh toán MoMo và Ví Trả Sau không?"*) giúp các công cụ AI Search (ChatGPT, Gemini, Perplexity) trích dẫn nguồn `momo.vn/merchant` khi trả lời người dùng.

## VI. Gamification & Promotions

* **Tích Điểm Merchant (MoMo Rewards Integration):** Người dùng quét QR thanh toán tại merchant được tích điểm đổi quà trên MoMo Rewards  ➔  Hiển thị tiến trình tích điểm trực tiếp trên Merchant Page để khuyến khích người dùng quay lại shop.
* **Gói Quà Tặng Mở Cửa Hàng (Merchant Onboarding Package):** Tài trợ 100.000đ Voucher O2O cho 1.000 chủ shop mới tạo và xác minh trang Merchant Page đầu tiên.
* **Vòng Quay May Mắn Soundbox (Soundbox Lucky Spin):** Chủ cửa hàng đăng ký tư vấn Loa Soundbox trên Web có cơ hội trúng 100% voucher miễn phí phí thuê loa 3 tháng.

## VII. Compliance & Risk Governance

### 7.1 Security & PDPD Compliance
* **Nghị định 13/2023/NĐ-CP (PDPD):** Tuân thủ nghiêm ngặt quy định bảo vệ dữ liệu cá nhân. Trên Web public, tuyệt đối không công khai số điện thoại cá nhân của chủ shop, tài khoản ngân hàng cá nhân hay doanh thu cửa hàng. Thông tin chủ shop chỉ được chỉnh sửa trong cổng quản trị App M4B đã xác thực.
* **Quy định Ngân hàng Nhà nước (NHNN):** Mọi voucher quy đổi giá trị tiền mặt và giao dịch quét QR thanh toán bắt buộc được thực hiện trên ứng dụng MoMo đã hoàn tất xác thực KYC. Web Platform đóng vai trò hiển thị thông tin và thu thập leads.

### 7.2 Risk Management Matrix

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Rủi ro tiềm tàng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Mức độ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phương án xử lý</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đơn vị chịu trách nhiệm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Thông tin cửa hàng bị sai lệch</strong> (Địa chỉ, Giờ mở cửa) do chủ shop thay đổi không báo.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tích hợp nút <em>"Báo sai thông tin"</em> trên Web; cho phép cộng đồng người dùng đóng góp chỉnh sửa & tự động nhắc chủ shop qua App M4B.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Operations Team & M4B</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Spam / Leads ảo đăng ký tư vấn Soundbox</strong> từ form công khai trên Web.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tích hợp reCAPTCHA v3, OTP xác thực số điện thoại chủ shop trước khi gửi Lead về CRM.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Technical Team & Sales M4B</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Merchant lạm dụng phát hành Voucher O2O</strong> để trục lợi gian lận.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thiết lập hạn mức phát hành voucher tối đa/ngày; kiểm soát tự động qua hệ thống Fraud Detection của MoMo.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Risk Management & Financial Services</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Quá tải truy cập trang Merchant</strong> trong các chiến dịch khuyến mãi lớn.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tối ưu Caching CDN (Cloudflare/Akamai), Server-side Rendering (SSR) nhẹ giúp tốc độ tải trang di động <1.5s.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform Team</td>
    </tr>
  </tbody>
</table>

## VIII. Growth Roadmap & Changelog

### 8.1 5-Phase Growth Roadmap
* **Phase 1: Merchant Acquisition & Web Hub Launch (T9 - T12/2026):** Mở rộng `momo.vn/merchant` theo 14 nhóm ngành nghề chính & 53 ngành nghề phụ; kích hoạt luồng Web-to-App Claim Voucher O2O; chuẩn hóa 500.000 Merchant Pages.
* **Phase 2: Soundbox & FS Monetization Engine (Q1/2027):** Đẩy mạnh Landing Page Loa Soundbox; hiển thị nhãn Ví Trả Sau badge trên Merchant Pages; triển khai luồng Merchant Verification (Claim Store).
* **Phase 3: Merchant Commerce & Engagement Engine (Q2/2027):** Ra mắt tính năng Đánh giá & Review từ người dùng MoMo; tích hợp Booking/Menu order trước; mở Cổng phát hành Voucher O2O cho chủ shop trên App M4B.
* **Phase 4: AI Merchant Assistant & Hyper-Local GEO (Q3/2027):** Trợ lý AI gợi ý chương trình khuyến mãi cho chủ shop dựa trên dữ liệu ngành nghề; cá nhân hóa vị trí hiển thị cửa hàng theo hành vi người dùng.
* **Phase 5: Merchant Financial Ecosystem (Q4/2027):** Mở rộng hệ sinh thái tài chính cho Merchant: Gói vay hộ kinh doanh, Bảo hiểm cửa hàng, B2B Procurement Marketplace mua hàng giá sỉ.

### 8.2 Change Log

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phiên bản</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ngày cập nhật</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Người thực hiện</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung thay đổi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>v2.1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-08-07</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Software Engineering Team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>MoSpark CMS Merchant Feature Upgrades:</strong> Cập nhật tính năng quản trị Merchant List View (50 rows/page), hệ thống Quản lý Tags & Import CSV hàng loạt, công cụ Bulk Actions (Add/Remove Tag, Index/No-index, Bulk Remove), tính năng tự động trích xuất tọa độ Lat/Long từ Google Maps share link, và nâng cấp GenAI Options kèm bộ Prompt Long Content mới.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>v2.0</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-07-31</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Product Lead (GPD)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Master BRD Upgrade:</strong> Đại tu toàn bộ Merchant Hub BRD theo chuẩn cấu trúc <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">vehicle-hub-brd.md</code>. Bổ sung SCR Framework, PLG 5 Phễu Tiện Ích Thu Hút, Dual North Star Metrics, Bảng Phân Tích Nhu Cầu Tìm Kiếm (Search Demand Analysis), Tích hợp Bộ Taxonomy 14 Ngành nghề chính & 53 Ngành nghề phụ từ CSV, Schema.org Matrix, PDPD Compliance và Risk Management Matrix.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>v1.0</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2026-07-15</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform Team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khởi tạo tài liệu BRD ban đầu cho dự án Merchant Hub (MoMo Merchant Page cho SME).</td>
    </tr>
  </tbody>
</table>
