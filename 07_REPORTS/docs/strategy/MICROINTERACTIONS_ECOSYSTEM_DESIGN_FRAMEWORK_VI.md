# KHUNG THIẾT KẾ HỆ SINH THÁI VÀ HÀNH TRÌNH VI MÔ (MICROJOURNEYS)
**Tài liệu gốc:** `Microinteractions_Ecosystem_Design_vFf.pptx.pdf`  
**Đơn vị:** MoMo Platform & Strategy Planning  
**Phiên bản:** Bản dịch tiếng Việt hoàn chỉnh và chuẩn hóa nội bộ  

---

## PHẦN 1: TỔNG QUAN KHUNG HỆ SINH THÁI (FRAMEWORK AT A GLANCE)

Hệ sinh thái được tổ chức thành 4 tầng nghiệp vụ chính (cùng 1 tầng mở rộng), mỗi tầng đảm nhiệm một vai trò duy nhất:

| Tầng (Layer) | Vai trò trong hệ thống | Hiệu quả kinh tế (Economics) | Chỉ số cốt lõi (Core Metrics) |
| :--- | :--- | :--- | :--- |
| **1. Mỏ neo (Anchors)**<br>*(Tần suất cao)* | Thu hút người dùng mới và xây dựng thói quen sử dụng thường xuyên. | Hòa vốn hoặc chấp nhận bù lỗ; được xem là chi phí thu nạp người dùng (CAC). | MAU, DAU, Tần suất giao dịch trên mỗi người dùng, Tỷ lệ giữ chân A30, CAC. |
| **2. Kết nối (Connective Layer)**<br>*(Dữ liệu người dùng sở hữu: ID, Ví, Điểm, FinHub, PromoHub, Rewards)* | Giúp mọi dịch vụ mới ra mắt rẻ hơn và khiến người dùng khó rời bỏ hơn (tăng chi phí chuyển đổi). | Chi phí hạ tầng dùng chung, không trực tiếp tạo ra doanh thu. | Số dịch vụ sử dụng trên mỗi người dùng, Tỷ lệ bán chéo (Cross-sell), Tỷ lệ đổi điểm thưởng, Độ phủ dữ liệu. |
| **3. Cận biên (Adjacent Services)**<br>*(Hành vi người dùng: Vé xem phim, Dịch vụ nhúng)* | Khai thác sâu hơn nhu cầu bên trong các hành trình mà người dùng đã và đang hoàn tất. | Biên lợi nhuận mỏng nhưng dương. | Tỷ lệ đính kèm dịch vụ trên mỗi giao dịch (Attach rate). |
| **4. Sinh lời (Monetization)**<br>*(Tín dụng, Quản lý tài sản, Bảo hiểm, Quảng cáo, Merchant SaaS)* | Tận dụng kênh phân phối chi phí thấp từ các tầng trên để tạo ra lợi nhuận cao. | Biên lợi nhuận cao, chịu sự quản lý pháp lý chặt chẽ và chịu rủi ro tín dụng/thị trường. | Doanh thu trên mỗi người dùng (ARPU), Tỷ lệ thu phí (Take rate), Tỷ lệ nợ xấu/thất thoát, Tỷ lệ phê duyệt và chuyển đổi. |
| **5. Nền tảng mở (Open Layer)**<br>*(Tạm gác lại đánh giá sâu: Mini-apps đối tác, APIs, Marketplace)* | Mở rộng quy mô danh mục dịch vụ mà không cần MoMo phải tự tay xây dựng tất cả. | Phí nền tảng, hoặc giá trị gián tiếp từ việc dẫn dắt lưu lượng. | Số đối tác đang hoạt động, GMV bên thứ ba, Tỷ lệ giữ chân nhà phát triển. |

---

## PHẦN 2: CƠ CHẾ VẬN HÀNH BÁNH ĐÀ HỆ SINH THÁI (THE ECOSYSTEM FLYWHEEL)

```
        ┌────────────────────────────────────────────────────────┐
        │                 1. MỎ NEO (ANCHORS)                    │
        │       Thu hút người dùng với chi phí được trợ giá      │
        └───────────────────────────┬────────────────────────────┘
                     ▲              │
                     │              ▼
        ┌────────────┴──────────────┐     ┌──────────────────────┐
        │       VÒNG LẶP HỖ TRỢ     │ ◄───┤ 2. KẾT NỐI           │
        │  Lợi nhuận từ Tầng 4      │     │ Thu thập ID & Dữ liệu│
        │  tài trợ cho chi phí trợ  │     │ qua từng giao dịch   │
        │  giá của Tầng 1           │     └──────────┬───────────┘
        └────────────▲──────────────┘                │
                     │                               ▼
        ┌────────────┴──────────────┐     ┌──────────────────────┐
        │   4. SINH LỜI             │ ◄───┤ 3. CẬN BIÊN          │
        │ Ưu đãi đích danh, quản trị│     │ Tăng tần suất & số dư│
        │ rủi ro và lựa chọn tốt hơn│     │ MẮT XÍCH YẾU CẦN TỐI │
        └───────────────────────────┘     │ ƯU: CHUYỂN ĐỔI SP    │
                                          └──────────────────────┘
```

*   **Vòng lặp tương hỗ (The Reinforcing Link):** Lợi nhuận biên cao từ Tầng 4 (Tài chính, Tín dụng) quay lại tài trợ cho ngân sách khuyến mãi và chi phí vận hành miễn phí của Tầng 1 (Chuyển tiền, Thanh toán).
*   **Mắt xích yếu phổ biến (Common Weak Link):** Tỷ lệ chuyển đổi sản phẩm (Product Conversion). Khoảng cách giữa việc người dùng hoàn tất một dịch vụ cận biên (Tầng 3) hoặc dịch vụ mỏ neo sang việc chấp nhận dùng sản phẩm sinh lời (Tầng 4) thường là điểm rơi rụng lớn nhất của toàn hệ thống.

---

## PHẦN 3: VÍ DỤ THỰC TẾ VỀ QUẢN TRỊ SỐ DƯ TÀI KHOẢN (WALLET BALANCE EXAMPLE)

Ví dụ thực tế triển khai tại MoMo:

*   **1. Mỏ neo (Anchors):** Đưa người dùng vào với chi phí trợ giá -> Thúc đẩy giao dịch thanh toán và tỷ lệ giữ chân tăng từ 28 lên 30 giao dịch.
*   **2. Kết nối (Connective Layer):** Thu thập danh tính và dữ liệu trên mỗi giao dịch:
    *   Chia sẻ số dư ngân hàng liên kết: Đã đạt 6,6 triệu người dùng hiện hữu.
    *   Quản lý giao dịch định kỳ (hóa đơn sắp đến hạn).
    *   Tối ưu hóa chi tiêu và tiết kiệm (Quản lý tài chính cá nhân - PFM).
*   **3. Cận biên (Adjacent Services):** Tăng tần suất và số dư ví:
    *   Chuyển đổi người dùng có số dư ngân hàng cao (từ 500.000đ trở lên) sang mở Túi Thần Tài (TTT) với tỷ lệ chuyển đổi mục tiêu x%.
    *   Đề xuất mở Ví Trả Sau (VTS) cho nhóm người dùng có dòng tiền thấp hoặc âm.
*   **4. Sinh lời (Monetization):** Đưa ra ưu đãi trúng đích, chọn lọc rủi ro tốt hơn:
    *   Chuyển đổi người dùng đang có Túi Thần Tài sang các sản phẩm đầu tư, chứng chỉ quỹ, tích lũy dài hạn.
    *   Chuyển đổi người dùng đang dùng Ví Trả Sau sang các gói vay tiền mặt / vay tiêu dùng (Lending).

---

## PHẦN 4: GIẢI PHÁP HÀNH TRÌNH VI MÔ (THE SOLUTION: MICROJOURNEYS)

**Hành trình vi mô (Microjourneys) giúp mọi tầng có thể kết nối trực tiếp đến bất kỳ tầng nào khác:**

*   **Không phải vòng lặp một chiều:** Hành trình vi mô là một bước ngắn nhúng ngay bên trong luồng chính của một tầng, đưa người dùng bước sang một tầng khác một cách tự nhiên.
*   **Bất kỳ tầng nào sang bất kỳ tầng nào:** Bất kỳ tầng nào cũng có thể đóng vai trò kích hoạt (trigger) một hành trình vi mô, và bất kỳ tầng nào cũng có thể tiếp nhận nó.
*   **Tác động tối đa:** Những hành trình vi mô tốt nhất là những hành trình kết nối được số lượng người dùng đông đảo nhất đến nhiều tầng cùng một lúc.

**Ví dụ: Một tín hiệu dữ liệu nuôi dưỡng hai tầng cùng lúc:**
*   *Tín hiệu xuất phát từ Tầng 2 (Kết nối):* Người dùng chia sẻ số dư ngân hàng liên kết.
*   *Tác động đồng thời sang Tầng 1 (Mỏ neo):* Nhắc nhở thanh toán hóa đơn / chi tiêu định kỳ để nâng tần suất giao dịch.
*   *Tác động đồng thời sang Tầng 4 (Sinh lời):* Đề xuất chuyển đổi số dư nhàn rỗi (ví dụ: số dư tài khoản trên 1.000.000đ) vào Túi Thần Tài để sinh lời hàng ngày.

---

## PHẦN 5: 4 BỘ KIỂM TRA ĐỊNH VỊ DỊCH VỤ (DECISION RULES: FOUR TESTS)

Để quyết định một tính năng hoặc dịch vụ thuộc về tầng nào trong hệ sinh thái, áp dụng 4 bài kiểm tra tuần tự:

*   **Bài kiểm tra 1: Mỏ neo (Anchor Test)**
    *   *Câu hỏi:* Người dùng có chủ động mở dịch vụ này ít nhất hàng tuần hoặc hàng tháng mà không cần khuyến mãi hay không?
    *   *NẾU CÓ:* Xem đây là Dịch vụ Mỏ neo (Tầng 1); sẵn sàng cấp ngân sách trợ giá như một khoản chi phí thu nạp người dùng (CAC).
    *   *NẾU KHÔNG:* Đây chỉ là một tính năng chứ không phải một dịch vụ độc lập: Chuyển sang Tầng 2 (Kết nối) hoặc Tầng 3 (Cận biên).
*   **Bài kiểm tra 2: Kết nối (Connective Test)**
    *   *Câu hỏi:* Có từ 3 dịch vụ trở lên sẽ sử dụng dữ liệu hoặc tính năng này không, và nó có tăng thêm giá trị khi càng có nhiều người dùng hay không?
    *   *NẾU CÓ:* Xây dựng tập trung thành hạ tầng dùng chung (Tầng 2).
    *   *NẾU KHÔNG:* Giữ nguyên dưới dạng tính năng độc lập nằm bên trong một dịch vụ cụ thể (Ví dụ: chương trình tích điểm riêng cho thanh toán hóa đơn).
*   **Bài kiểm tra 3: Cận biên (Adjacency Test)**
    *   *Câu hỏi:* Dịch vụ này có nằm tự nhiên bên trong một hành trình mà người dùng vốn đã hoàn tất trong ứng dụng hay không?
    *   *NẾU CÓ:* Đưa vào Tầng 3 và gắn chặt vào hành trình sẵn có đó.
    *   *NẾU KHÔNG:* Không bổ sung; việc đưa thêm một sản phẩm ngẫu nhiên không liên quan sẽ làm loãng và rối loạn trải nghiệm người dùng.
*   **Bài kiểm tra 4: Nền tảng mở (Open Layer Test)**
    *   *Câu hỏi:* Đối tác bên ngoài có mang lại tệp người dùng hoặc nội dung mà MoMo không thể tự xây dựng một cách hiệu quả về mặt kinh tế hay không?
    *   *NẾU CÓ:* Mở cổng kết nối API hoặc tạo vị trí Mini-app cho đối tác (Tầng 5).
    *   *NẾU KHÔNG:* Chờ đợi đánh giá thêm, hoặc tự phát triển nội bộ.

---

## PHẦN 6: PHÂN BỔ DANH MỤC DỊCH VỤ HIỆN TẠI VÀ CÁC CÂU HỎI MỞ (SERVICE ALLOCATION)

| Tầng (Layer) | Dịch vụ và Tính năng hiện hữu | Câu hỏi chiến lược còn để ngỏ (Open Questions) |
| :--- | :--- | :--- |
| **1. Mỏ neo (Anchors)** | - Chuyển tiền (P2P, VietQR)<br>- Giải pháp Định chế tài chính (ngoại trừ Tìm kiếm khách hàng tiềm năng)<br>- Giao dịch Online (Thương mại điện tử, Giao vận, Cửa hàng ứng dụng)<br>- Giao dịch Offline (Thanh toán tại quầy - EPS)<br>- Tiện ích đời sống (Nạp tiền điện thoại, Thanh toán hóa đơn, Dịch vụ công) | Đối với VietQR và chuyển khoản giữa các tài khoản ngân hàng: Làm thế nào để MoMo trở thành một lớp nhúng mượt mà trong hệ sinh thái chuyển tiền của các ngân hàng (OTT)? |
| **2. Kết nối (Connective)** | - FinHub (Số dư ngân hàng, Điểm tín dụng CIC, Thông báo biến động OTT)<br>- Quản lý tài chính cá nhân (PFM)<br>- Hệ thống Điểm thưởng (Reward)<br>- Trung tâm Khuyến mãi (Promotion Hub)<br>- Hubs chuyên đề (Gói dịch vụ đăng ký định kỳ)<br>- Quỹ nhóm, Quyên góp từ thiện, Điểm tin cậy, Tính năng xã hội | Những Hubs nào là trọng tâm cốt lõi? Làm thế nào để kết nối các Hubs này sang các tầng khác và đo lường chính xác tác động đóng góp? |
| **3. Cận biên (Adjacent)** | - Vé xem phim (bao gồm cả sản phẩm nhượng quyền IP)<br>- Gói cước Data viễn thông<br>- Nội dung số<br>- Bảo hiểm nhúng<br>- Ví Trả Sau (PayLater)<br>- Quản lý tài sản (Wealth Management) | Các dịch vụ này thực sự đóng vai trò cận biên (thúc đẩy mỏ neo hoặc sinh lời), hay chỉ đang vận hành như các dịch vụ đơn lẻ quy mô nhỏ? |
| **4. Sinh lời (Monetization)** | - Vay tiền mặt (Cash Loan)<br>- Du lịch và Đi lại (OTA)<br>- Giải pháp cho Đơn vị chấp nhận thanh toán (Merchant Solutions)<br>- Hoàn tiền (Cashback)<br>- Tìm kiếm khách hàng tiềm năng (Lead Gen)<br>- Chấm điểm tín dụng (Credit Score) | Ngưỡng doanh thu hoặc quy mô kinh doanh ở mức nào thì được chính thức tính là một mảng sinh lời độc lập? |
| **5. Nền tảng mở (Open Layer)** | - Cộng đồng (Community)<br>- Trang doanh nghiệp (Business Pages)<br>- Mini-apps đối tác | Chưa có khung đánh giá và lượng hóa cụ thể. |

---

## PHẦN 7: 4 LOẠI MÓC NỐI TRONG HÀNH TRÌNH VI MÔ (HOOK TYPES)

Bốn loại móc nối chịu trách nhiệm dẫn dắt người dùng chuyển dịch mượt mà từ tầng này sang tầng khác:

### 1. Bước tiếp theo - JTBD (Next Step Hook)
*   **Bản chất:** Dự đoán chính xác việc người dùng sẽ cần làm tiếp theo sau khi vừa hoàn tất thao tác hiện tại.
*   **Ví dụ:** Sau khi thanh toán xong hóa đơn tiền điện -> Đưa ra gợi ý: "Cài đặt thanh toán tự động hàng tháng từ nguồn tiền ví".
*   **Mối liên kết:** Dẫn từ Tầng Mỏ neo hoặc Cận biên sang Tầng Cận biên, Kết nối hoặc Sinh lời.

### 2. Bảo vệ rủi ro (Protective Hook)
*   **Bản chất:** Giảm thiểu hoặc triệt tiêu một rủi ro phát sinh từ chính hành động ban đầu của người dùng.
*   **Ví dụ:** Khi chuyển khoản P2P -> Hiển thị bước kiểm tra tên người nhận kèm cảnh báo tài khoản có dấu hiệu bất thường; Khi mua vé máy bay/vé xem phim -> Đưa ra tùy chọn mua bảo hiểm hủy vé.
*   **Mối liên kết:** Dẫn từ Tầng Mỏ neo hoặc Cận biên sang Tầng Kết nối (xác thực người dùng) hoặc Tầng Sinh lời (bán bảo hiểm).

### 3. Mở khóa năng lực (Enabling Hook)
*   **Bản chất:** Gỡ bỏ rào cản cản trở người dùng hoàn tất tác vụ chính (thường là rào cản về thanh khoản hoặc thủ tục).
*   **Ví dụ:** Khi số dư ví không đủ tại bước thanh toán -> Cho phép nạp tiền nhanh nội dòng từ ngân hàng liên kết; Khi giỏ hàng mua sắm có giá trị lớn -> Đưa ra tùy chọn "Chia nhỏ khoản thanh toán này qua Ví Trả Sau".
*   **Mối liên kết:** Dẫn từ Tầng Mỏ neo hoặc Cận biên sang Tầng Kết nối (nạp tiền, dùng điểm) hoặc Tầng Sinh lời (tín dụng, trả góp).

### 4. Phần thưởng và Ghi nhận (Reward Hook)
*   **Bản chất:** Gắn điểm thưởng, cơ chế trò chơi hóa (gamification) hoặc hành động đóng góp xã hội vào luồng giao dịch.
*   **Ví dụ:** Thanh toán quét mã QR thành công -> Hiển thị ngay số điểm thưởng vừa tích lũy trên biên lai điện tử.
*   **Mối liên kết:** Dẫn từ bất kỳ tầng nào sang Tầng Kết nối (tích lũy và sử dụng điểm thưởng).

---

## PHẦN 8: 6 QUY TẮC UX CHO LỜI MỜI NHÚNG (SIX UX RULES FOR EMBEDDED OFFERS)

Sáu quy tắc bảo đảm các đề xuất dịch vụ nhúng giữ đúng vị trí hỗ trợ, không gây phản cảm cho người dùng:

1.  **Không bắt nhập lại thông tin (Zero-data entry):** Kế thừa toàn bộ ngữ cảnh sẵn có; người dùng không bao giờ phải gõ lại những thông tin họ đã cung cấp ở bước trước.
2.  **Đặt đúng thời điểm ý định cao nhất (Peak-intent placement):** Chỉ đưa ra lời mời khi nhu cầu lên mức cao nhất: sau khi quyết định chính đã được chốt, trước bước xác nhận thanh toán cuối cùng. Luôn luôn có thể bỏ qua dễ dàng (Always skippable).
3.  **Lựa chọn có thể đảo ngược nhẹ nhàng (Reversible choices):** Cơ chế đồng ý tham gia đơn giản bằng 1 chạm (checkbox hoặc nút gạt toggle) với các giá trị mặc định thông minh.
4.  **Đặt tên hướng hành động (Action-oriented framing):** Lời kêu gọi hành động phải bám sát mục tiêu của luồng chính: Sử dụng *"Chia nhỏ khoản thanh toán này"*, tuyệt đối không dùng *"Đăng ký mở hạn mức tín dụng"*.
5.  **Thứ bậc thị giác chìm (Visual subordination):** Sản phẩm nhúng phải được thiết kế như một thành phần con tự nhiên của giao diện (native child component), không được hiển thị dưới dạng banner quảng cáo cắt ngang luồng.
6.  **Mỗi luồng tối đa một lời mời (One offer per flow):** Một hành trình chính chỉ được mang tối đa một ưu đãi nhúng tại một thời điểm, tránh gây quá tải nhận thức cho người dùng.

---

## PHẦN 9: MA TRẬN KẾT HỢP HÀNH TRÌNH VI MÔ (COMBINATION MAP)

Bảng phân bổ các loại Móc nối (Hooks) giữa Tầng kích hoạt (Trigger) và Tầng được nhúng (Embedded):

| Tầng kích hoạt (Trigger) ↓ \ Tầng nhúng (Embedded) → | 1. Mỏ neo (Anchors) | 2. Kết nối (Connective) | 3. Cận biên (Adjacent) | 4. Sinh lời (Monetization) | 5. Nền tảng mở (Open) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Mỏ neo (Anchors)** | - | - Reward<br>- Protective<br>- Enabling | - Next step<br>- Protective | - Enabling<br>- Next step | - |
| **2. Kết nối (Connective)** | - | - | - Reward | - Enabling | - |
| **3. Cận biên (Adjacent)** | - Next step | - Next step<br>- Enabling | - | - Protective<br>- Enabling | - |
| **4. Sinh lời (Monetization)** | - | - Reward | - | - | - |
| **5. Nền tảng mở (Open Layer)**| - | - | - | - Protective | - |

*Quy luật tổng quát:* Phần lớn các tổ hợp đều có đích đến là Tầng Kết nối hoặc Tầng Sinh lời; các ô trống biểu thị chưa có ví dụ thực tế phù hợp.

---

## PHẦN 10: CÁC VÍ DỤ TỔ HỢP CỤ THỂ (COMBINATION EXAMPLES)

### Nhóm 1: Các hành trình vi mô kích hoạt từ Tầng Mỏ neo (Anchors)
*Quy luật 1: Các móc nối dạng Phần thưởng (Reward) trên tầng Mỏ neo cần xuất hiện đầu tiên để xây dựng thói quen tích điểm và thu thập dữ liệu phục vụ các móc nối sau này.*

| Luồng chuyển tiếp (Trigger ➔ Embedded) | Loại Móc nối (Hook) | Kịch bản hành trình vi mô cụ thể |
| :--- | :--- | :--- |
| **Mỏ neo ➔ Kết nối** | Phần thưởng (Reward) | Thanh toán QR -> Hiển thị điểm thưởng trên biên lai kèm lời nhắc đổi quà. |
| **Mỏ neo ➔ Kết nối** | Phần thưởng (Reward) | Chuyển tiền P2P hoặc thanh toán QR -> Nút gạt làm tròn số tiền dư để quyên góp từ thiện. |
| **Mỏ neo ➔ Kết nối** | Bảo vệ (Protective) | Chuyển tiền P2P -> Hiển thị tên người nhận trước khi chuyển, kèm cảnh báo lừa đảo với giao dịch bất thường. |
| **Mỏ neo ➔ Kết nối** | Mở khóa (Enabling) | Số dư ví không đủ khi thanh toán -> Nạp tiền nhanh nội dòng từ ngân hàng, hoặc dùng điểm bù phần thiếu. |
| **Mỏ neo ➔ Cận biên** | Bước tiếp theo (Next step) | Vừa nhận được tiền chuyển khoản P2P -> Gợi ý thanh toán hóa đơn điện thoại/điện nước sắp tới hạn. |
| **Mỏ neo ➔ Cận biên** | Bảo vệ (Protective) | Thanh toán đơn hàng thương mại điện tử -> Đính kèm bảo hiểm bảo vệ mua sắm hoặc bảo hiểm giao hàng. |
| **Mỏ neo ➔ Sinh lời** | Mở khóa (Enabling) | Thanh toán giỏ hàng giá trị cao -> Gợi ý tùy chọn "Chia nhỏ khoản thanh toán này" (Ví Trả Sau). |
| **Mỏ neo ➔ Sinh lời** | Bước tiếp theo (Next step) | Có số dư nhàn rỗi sau khi nhận tiền chuyển khoản -> Gợi ý chuyển vào Túi Thần Tài để sinh lời. |
| **Mỏ neo ➔ Sinh lời** | Mở khóa (Enabling) | Tiểu thương nhận nhiều tiền thanh toán qua mã QR -> Đề xuất gói vay vốn lưu động hoặc phần mềm quản lý bán hàng. |

### Nhóm 2: Các hành trình vi mô kích hoạt từ các Tầng khác
*Quy luật 2: Các mũi tên đảo ngược (ví dụ: vé xem phim -> gợi ý đặt xe; trả nợ đúng hạn -> cộng điểm thưởng) giúp khép kín vòng tròn bánh đà hệ sinh thái.*

| Luồng chuyển tiếp (Trigger ➔ Embedded) | Loại Móc nối (Hook) | Kịch bản hành trình vi mô cụ thể |
| :--- | :--- | :--- |
| **Cận biên ➔ Kết nối** | Bước tiếp theo (Next step) | Thanh toán xong hóa đơn -> Gợi ý cài đặt thanh toán tự động định kỳ từ ví. |
| **Cận biên ➔ Kết nối** | Mở khóa (Enabling) | Số tiền hóa đơn lớn hơn số dư ví hiện có -> Nạp tiền nhanh trực tiếp từ tài khoản ngân hàng liên kết. |
| **Cận biên ➔ Mỏ neo** | Bước tiếp theo (Next step) | Vừa mua vé xem phim xong -> Gợi ý đặt xe di chuyển đến rạp hoặc đặt trước bắp nước. |
| **Cận biên ➔ Sinh lời** | Bảo vệ (Protective) | Mua vé xem phim / vé máy bay -> Đưa ra tùy chọn mua bảo hiểm hủy vé. |
| **Cận biên ➔ Sinh lời** | Mở khóa (Enabling) | Hóa đơn điện nước tháng này tăng cao bất thường -> Đề xuất chia nhỏ kỳ hạn thanh toán qua trả góp. |
| **Kết nối ➔ Cận biên** | Phần thưởng (Reward) | Điểm thưởng sắp hết hạn -> Nhắc nhở người dùng đổi vé xem phim hoặc nạp thẻ cào. |
| **Kết nối ➔ Sinh lời** | Mở khóa (Enabling) | Dựa trên lịch sử giao dịch tốt -> Hiển thị hạn mức vay phê duyệt trước ngay trong luồng, không bắt làm hồ sơ. |
| **Sinh lời ➔ Kết nối** | Phần thưởng (Reward) | Trả nợ tín dụng đúng hạn -> Thưởng điểm thành viên hoặc tự động nâng hạn mức chi tiêu. |
| **Nền tảng mở ➔ Sinh lời** | Bảo vệ (Protective) | Đặt tour trên Mini-app du lịch của đối tác -> Đính kèm bảo hiểm du lịch tích hợp. |

---

## PHẦN 11: TĂNG TRƯỞNG GIỮ CHÂN NHỜ HÀNH VI ĐẦU TƯ (INVESTMENT-DRIVEN RETENTION)

Dữ liệu thực chứng chứng minh mức độ đầu tư của người dùng vào Nền tảng Đáng tin cậy (Trusted Platform) tạo ra bước nhảy vọt về tỷ lệ giữ chân (Cohort Retention):

| Phân nhóm người dùng | Tần suất thấp (< 4 ngày) | Tần suất cao (≥ 4 ngày) | Mức độ chênh lệch giữ chân |
| :--- | :---: | :---: | :---: |
| **Nhóm CÓ hành vi Đầu tư (Investment)** | **45%** *(chiếm 35,8% user)* | **84%** *(chiếm 18,6% user)* | **+9 đến +12 điểm %** |
| **Nhóm KHÔNG có hành vi Đầu tư** | **36%** *(chiếm 36,0% user)* | **72%** *(chiếm 9,6% user)* | Cơ sở so sánh |

### 3 hình thức đầu tư giá trị (Example Investments):
1.  **Đầu tư Dữ liệu (Data Investment):** Người dùng chủ động bật nhận thông báo, chia sẻ số dư ngân hàng liên kết, liên kết ứng dụng ngân hàng, kiểm tra điểm tín dụng CIC trên FinHub.
2.  **Đầu tư Tiền bạc (Money Investment):** Duy trì số dư ví tối thiểu từ 10.000đ vào cuối tháng, số dư Túi Thần Tài trên 10.000đ, có lịch sử thanh toán hóa đơn viễn thông và tiện ích định kỳ.
3.  **Đầu tư Mối quan hệ (Relationship Investment):** Thực hiện chuyển tiền qua lại thường xuyên (Chuyển giữa các ví MoMo - W2W, hoặc Chuyển từ ví về tài khoản ngân hàng - W2B).

---

## PHẦN 12: KẾ HOẠCH HÀNH ĐỘNG TIẾP THEO (WHAT'S NEXT)

1.  **Tích hợp khung hệ sinh thái vào công tác lập kế hoạch chiến lược:** Đưa toàn bộ cấu trúc 4 tầng và nguyên tắc phân bổ dịch vụ vào bản kế hoạch năm của các nhóm sản phẩm.
2.  **Lập danh mục chi tiết các hành trình vi mô:** Từng dịch vụ rà soát và định nghĩa các điểm chạm kết nối chéo với các tầng khác trong hệ sinh thái MoMo.
3.  **Làm việc với FinanceBP:** Lượng hóa tác động tài chính, dự tính chi phí trợ giá cho Tầng 1 và doanh thu kỳ vọng từ Tầng 4 để thiết lập chỉ số mục tiêu kinh doanh.
4.  **Trình duyệt Ban Giám đốc (BOM):** Hoàn thiện hồ sơ thông qua FinanceBP trong vòng 2 tuần để phục vụ kỳ họp đánh giá kế hoạch chiến lược với Ban Điều hành.
