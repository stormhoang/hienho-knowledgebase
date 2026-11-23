# BRD: Student Pass - Thẻ Sinh Viên Số & Đặc Quyền Sinh Viên MoMo

> - **Dự án:** Student Pass (In-App Digital Identity & Privileges)
> - **Nền tảng:** MoMo App (Mini-app)
> - **Khối phụ trách:** Growth Platform Division (GPD)
> - **Owner:** Youth & Student Segment Team

---

## I. Business Context & Product Statement

### 1.1 Vấn đề & Cơ hội
Nhóm người dùng Gen Z (đặc biệt là Tân sinh viên 18 tuổi) là tệp khách hàng chiến lược, đại diện cho "cột mốc tài chính đầu đời". Tuy nhiên, trước đây MoMo thiếu một **định danh duy nhất** để nhận diện người dùng là sinh viên trên toàn hệ thống. Việc phân phát ưu đãi sinh viên thường bị phân tán, khó xác thực đúng đối tượng (chống gian lận) và khó giữ chân người dùng sau khi họ sử dụng xong voucher.

### 1.2 Định vị Sản phẩm
**Student Pass** không phải là một trang web cẩm nang (như Student Hub), mà là một **tính năng/Mini-app cốt lõi (In-App)** nằm bên trong ứng dụng MoMo. Nó đóng vai trò là chiếc **Thẻ Sinh Viên Số (Digital Student ID)** được xác thực định danh (eKYC) kết nối với cơ sở dữ liệu trường học.
Student Pass là chìa khóa (Identity Layer) để sinh viên mở khóa toàn bộ **hệ sinh thái Đặc Quyền Sinh Viên** và các sản phẩm tài chính chuyên biệt (Ví Trả Sau 0%, Vay Nhanh sinh viên, Túi Thần Tài).

### 1.3 Gen Z Target Insights & Behavior Breakdown (Nghiên Cứu Khách Hàng)

* **Bối cảnh phát triển & Đặc điểm thế hệ (Digital Natives):**
  * Gen Z dự kiến chiếm **1/3 lực lượng lao động** tại Việt Nam đến năm 2025. Sinh ra trong thời kỳ kinh tế bùng nổ, MXH ảnh hưởng sâu sắc đến xu hướng tiêu dùng, giải trí và tìm kiếm thông tin của họ.
  * **Hành vi cuộc sống (Life Behavior):** 79% lướt Facebook Newfeed xem thông tin (so với 42% đi cà phê ngoài). 51% thấy quan trọng khi được tương tác, kỳ vọng các trải nghiệm được **"cá nhân hóa"**.
  * **Nguồn thông tin tin cậy (Source of Awareness):** Ba mẹ, chuyên gia và bạn bè ("Word of Mouth") là nguồn thông tin đáng tin cậy hàng đầu thay vì các Influencers đơn thuần.
  * **Tâm lý tự hào & gia đình:** Lớn lên trong sự bao bọc của gia đình, Gen Z có xu hướng sống như "tâm điểm". Việc khiến cha mẹ tự hào là điều mang lại niềm vui lớn nhất cho giới trẻ.

* **Tiềm năng & Đặc điểm tiêu dùng (Buying Power & Consumption Behavior):**
  * **Cơ cấu chi tiêu:** Tập phần lớn chi tiêu vào **Mua sắm quần áo (53% thảo luận)** và các hoạt động vui chơi xã hội. 58% thảo luận về "tiết kiệm ngắn hạn" là để phục vụ mua sắm.
  * **Xu hướng tiêu dùng (Preferences):**
    * *Định hình bản thân:* >50% thảo luận ưu tiên thương hiệu ngoại/đồ hiệu để khẳng định bản thân. Quan tâm đến các vấn đề xã hội (bình đẳng giới, môi trường, trách nhiệm cộng đồng).
    * *Tư duy tài chính sớm:* 66.9% thảo luận xoay quanh chủ đề Kiếm tiền. Gen Z vượt trội hơn thế hệ Millennials trong việc xây dựng thói quen **tiết kiệm & đầu tư** từ sớm.
  * **Khát khao & An toàn tài chính (Approach & Financial Security):**
    * *Khao khát sở hữu (Top of mind):* Vé đại nhạc hội quốc tế (34%), đồ công nghệ giá trị cao (iPhone, máy ảnh...), du lịch & du học.
    * *Thực trạng tài chính:* Chỉ 25% thoải mái chi trả chi phí sinh hoạt hàng tháng, gần 50% chi tiêu hết tiền hàng tháng ➔ **Nhu cầu cấp thiết về giải pháp quản lý tài chính an toàn & dự phòng.**

---

## II. Core Features & Luồng Trải Nghiệm (User Flow)

### 2.1 eKYC & Định danh Thẻ Sinh Viên Số
* **Xác thực tự động (API Integration):** Liên kết API với hệ thống quản lý sinh viên của các trường Đại học/Cao đẳng trọng điểm (Phase 1: UEH, FTU, TDTU, HCMUT, VLU).
* **Xác thực thủ công (Manual eKYC):** Cho phép sinh viên upload ảnh chụp thẻ sinh viên cứng hoặc giấy báo trúng tuyển (dành cho tân sinh viên chưa có thẻ) để hệ thống AI/OCR OCR và nhân sự kiểm duyệt.
* **Giao diện Thẻ cá nhân hóa:** Thẻ Sinh Viên Số hiển thị tên, mã số sinh viên, logo trường ĐH và avatar của người dùng, có thể thiết kế theo màu sắc đặc trưng của trường (School Pride) để sinh viên tự hào chia sẻ lên Mạng xã hội.

### 2.2 Hệ sinh thái Đặc Quyền Sinh Viên (Tích hợp Chiến dịch "Bảo bối nhập học")
Một khi đã kích hoạt Student Pass thành công, sinh viên sẽ lập tức được cấp **Gói Đặc Quyền Sinh Viên (>1,386M/năm)**.
Đặc biệt trong mùa Back2School (Tháng 08-09), Student Pass tích hợp chiến dịch **"Bảo bối nhập học"** với các ưu đãi khủng:
* **Năng lượng & Tự tin (F&B, Mua sắm):** Voucher ăn uống thả ga (Katinat, Gong Cha, Highlands...), ưu đãi mua sắm (Giảm 50K Innisfree, 100K Routine), và trợ giá đồ công nghệ cho sinh viên (CellphoneS).
* **Di chuyển & Giải trí:** Mã giảm giá di chuyển (Vexere giảm 50K, Hải Vân giảm 10%, Vietnam Airlines giá sinh viên), đồng giá vé xem phim 50K tại Galaxy Cinema mỗi tuần.
* **Kết nối, An tâm & Học tập:** Voucher Data 3G/4G thả ga, bảo hiểm sinh viên toàn diện, đặc quyền sử dụng Trợ thủ AI Gemini để nâng cao học lực.

### 2.3 Gamification & Hệ thống Nhiệm Vụ (Missions)
Student Pass không chỉ tặng voucher thụ động mà xây dựng hệ thống nhiệm vụ để giữ chân (Retention) sinh viên tương tác hàng ngày:
* **Nhiệm vụ Onboarding:** Nhận thưởng lớn (+2.000 Xu) khi hoàn thành Mở/Liên kết ngân hàng nội địa.
* **Nhiệm vụ Daily/Tần suất:** +200 Xu khi thanh toán/quẹt thẻ bằng mã QR MoMo tại căn tin trường hoặc cửa hàng tiện lợi.
* **Chuỗi sự kiện Mùa vụ (Tháng 08):** Đua Top U18 săn deal đậm (10-15/08), Khởi động cuộc thi Đại sứ sinh viên, Ngày hội chào đón Tân Sinh Viên.

### 2.4 Cổng Cross-sell Sản Phẩm Tài Chính
Student Pass đóng vai trò bộ lọc rủi ro (Risk Filter). Sinh viên có Student Pass hợp lệ và điểm tín nhiệm tốt (Trust Score) sẽ được:
* Đề xuất mở **Ví Trả Sau** với đặc quyền **miễn phí duy trì tài khoản** (0đ phí hàng tháng) và hỗ trợ trả góp 0% mua Laptop/Thiết bị học tập.
* Kích hoạt tự động tính năng **Quản lý chi tiêu** và **Túi Thần Tài** với lãi suất ưu đãi cho số dư nhỏ.

---

## III. Jobs-to-be-Done (JTBD), Pain Points & Phân Tích Giải Pháp

Bảng phân tích chi tiết theo 03 nhóm hành vi/hành động chính của người dùng Sinh viên (User Behaviors):

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hành vi / Behavior</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Jobs-to-be-Done (JTBD)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Pain Points (Điểm đau của Sinh viên)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoMo Solution / Product Features (Giải pháp từ MoMo & Student Pass)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>1. Sử dụng Ngân hàng (Bank)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nơi giữ tiền và chuyển tiền an toàn, uy tín lâu đời, có bảo hộ của Nhà nước.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Thủ tục tại quầy phức tạp, nhiều yêu cầu phải ra trực tiếp quầy.<br>• Khó mở thẻ tín dụng do đòi hỏi chứng minh thu nhập/bảng lương/sổ tiết kiệm.<br>• Lịch sử giao dịch không rõ tên người nhận, khó kiểm tra/phân loại chi tiêu.<br>• Số tài khoản dài, khó nhớ, dễ chuyển nhầm người.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• <strong>100% Online:</strong> Thủ tục thực hiện online nhanh chóng, không cần ra quầy.<br>• <strong>Tín dụng Sinh viên (Ví Trả Sau):</strong> Cấp hạn mức tín dụng sinh viên không cần bảng lương với ưu đãi hạn mức riêng cho tệp Student Pass.<br>• <strong>Quản lý chi tiêu:</strong> Lịch sử giao dịch rõ ràng, tính năng Quản lý chi tiêu tự động phân loại giao dịch ngay khi thanh toán xong.<br>• <strong>Chuyển tiền bằng SĐT:</strong> Định danh người dùng dễ dàng, hạn chế sai sót.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>2. Sử dụng Ví MoMo</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trải nghiệm chuyển tiền và sử dụng dịch vụ nhanh chóng, không rườm rà (không phải ra quầy làm thủ tục giấy tờ như ngân hàng).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• Nhiều thông báo (notification) và pop-up gây khó chịu.<br>• Khó liên lạc CSKH so với ngân hàng.<br>• Vượt quá số lần chuyển tiền/tháng bị charge phí (khi ngân hàng đã free).<br>• App load chậm trên điện thoại cũ, một số giao dịch W2B gặp lỗi pending.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• <strong>Tối ưu trải nghiệm In-App:</strong> Thắt chặt chính sách giảm notification & pop-up trên app.<br>• <strong>CSKH Tự động:</strong> Cải thiện đội ngũ CSKH, phát triển thêm luồng xử lý ticket tự động qua tool.<br>• <strong>Tối ưu Luồng W2B:</strong> Có giải pháp cải thiện hạ tầng giảm pending giao dịch chuyển tiền.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>3. Tìm kiếm Tiết kiệm / Ưu đãi (Saving/Promotions)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chọn được khuyến mãi phù hợp (đúng nhu cầu, đúng thời điểm) để tiết kiệm tiền và sử dụng tiện lợi nhất (tiện đường, gần nhà, gần trường).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• <strong>Visibility & Navigation:</strong> Ưu đãi nằm rải rác nhiều chỗ gây rối, khó tìm kiếm và thu thập; Tâm lý lo lắng bỏ lỡ (FOMO) ưu đãi có hạn.<br>• <strong>Location:</strong> Khó kiếm ưu đãi gần vị trí của mình (recommend vị trí xa).<br>• <strong>Voucher Type:</strong> Thiếu các voucher nhu cầu thực tế ngoài FnB (đổ xăng, nạp game, đi xe công nghệ, logistics...).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">• <strong>Cá nhân hóa & Tinh gọn (Student Pass):</strong> Chọn lọc những voucher phù hợp nhất với nhu cầu sinh viên, không bắt người dùng phải "bơi" trong quá nhiều voucher rác.<br>• <strong>Mở rộng Hệ sinh thái Merchant:</strong> Kết nối sinh viên với các dịch vụ/merchants phù hợp đúng nhu cầu thực tế (Data, Vé xe, Công nghệ, AI...) thay vì chỉ tập trung voucher FnB.</td>
    </tr>
  </tbody>
</table>

---

## IV. Rủi Ro & Quản Trị (Risk Governance)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Rủi ro (Risk)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tác động</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phương án Xử lý & Quản trị (Mitigation)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Gian lận định danh (Fraud/Fake ID)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Người dùng mượn/chỉnh sửa thẻ sinh viên giả để trục lợi gói quà.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tích hợp OCR chống làm giả, đối chiếu chéo tên trên Thẻ sinh viên với tên thật đã eKYC trên MoMo. Xây dựng tool nội bộ để duyệt thẻ thủ công các trường hợp nghi ngờ.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bảo mật dữ liệu trường học</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lộ lọt thông tin mã số sinh viên.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mã hóa dữ liệu, không chia sẻ data định danh ngược lại cho bên thứ ba.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tốt nghiệp (Graduation Churn)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sinh viên ra trường, hết hạn Student Pass và từ bỏ MoMo.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thiết lập logic <strong>Ngày hết hạn (Expiry Date)</strong> dựa trên số năm đào tạo của trường. Trước khi thẻ hết hạn 1 tháng, tự động kích hoạt chiến dịch "Welcome to Adulthood", up-sell gói Tín dụng cá nhân cho người đi làm.</td>
    </tr>
  </tbody>
</table>
