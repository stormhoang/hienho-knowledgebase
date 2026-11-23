# INTERACTIVE QUIZ CARD FRAMEWORK & PRODUCT SPECIFICATIONS
## KHUNG THIẾT KẾ & TỔNG HỢP KỊCH BẢN QUIZ CHUYỂN ĐỔI WEB-TO-APP TOÀN DIỆN

- **Mã tài liệu:** `MOSP-SPEC-QUIZ-01`
- **Phân loại:** Product Specification & Behavioral Growth Framework
- **Trạng thái:** Active / Production-Ready
- **Phiên bản:** 1.0
- **Dự án áp dụng:** MoMo Web Platform (Landing Pages, Microsites, PLG Blog Injection)

---

## 1. TỔNG QUAN & NGUYÊN TẮC TÂM LÝ HỌC HÀNH VI (BEHAVIORAL FOUNDATION)

### 1.1. Bối cảnh & Mục tiêu Chuyển đổi
Bên cạnh công cụ tính toán thụ động (Utility Simulator), **Interactive Quiz Card (2-4 câu hỏi phân nhánh)** được triển khai như một phễu dẫn dắt và sàng lọc sơ bộ (Pre-qualification & Advisory Funnel) nhằm:
1. **Educate người dùng** một cách tự nhiên thông qua các tình huống đời thường.
2. **Kích hoạt hiệu ứng tâm lý (Sunk Cost + Zeigarnik Effect):** Khi người dùng đã bỏ ra 30-45 giây tương tác, họ có thôi thúc mạnh mẽ muốn xem kết quả cuối cùng.
3. **Cơ chế Gating 60% Reveal / 40% Locked:** Trả ra 60% kết quả chẩn đoán và khoảng giá/hạn mức ước tính trên Web để tạo sự tin tưởng tuyệt đối (Aha! Moment), đồng thời giữ lại 40% giá trị cốt lõi (Báo giá chi tiết từng đối tác, Hạn mức chính xác, Voucher ưu đãi độc quyền) phía sau nút bấm Web-to-App Deeplink.

### 1.2. Bằng chứng Thực nghiệm (Validation Proof từ Trang Điểm Tín Dụng)
Dữ liệu đo lường thực tế từ Umami Analytics cho trang `momo.vn/diem-tin-dung`:
- **Completion Rate (`quiz_complete` / `quiz_start`):** Đạt **62,5%** (Cứ 10 người bắt đầu thì hơn 6 người đi hết bộ câu hỏi).
- **CTA Conversion from Complete (`quiz_click_cta` / `quiz_complete`):** Đạt **84,3%** (Cơ chế 60% Reveal kích thích mở App vượt trội).
- **End-to-End Action Rate (`quiz_click_cta` / `quiz_start`):** Đạt **52,7%**.
- **Hiệu quả so với Banner Ads:** Tạo ra lượng click mở App gấp **1,77 lần** toàn bộ banner quảng cáo tĩnh, dù lượt hiển thị chỉ bằng 1/3.

### 1.3. Bốn Nguyên tắc Thiết kế Bắt buộc (Core UX Rules)
1. **Zero-Click Entry:** Bỏ nút "Bắt đầu". Hiển thị ngay Câu hỏi 1 ra màn hình chính; người dùng chạm vào đáp án là tự động kích hoạt câu tiếp theo.
2. **Ngôn ngữ đời thường, đúng Anxiety:** Tuyệt đối không dùng thuật ngữ tài chính/bảo hiểm sách vở. Đánh thẳng vào nỗi sợ mất tiền, sợ thủ tục hành xác, sợ bị từ chối hồ sơ.
3. **Cấu trúc Đồ thị Phân nhánh Linh hoạt (Non-Linear Dynamic Graph Engine):**
   - Tuyệt đối **không ép luồng tuyến tính cố định ($1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow \text{Result}$)**.
   - Luồng câu hỏi vận hành theo dạng cây quyết định sâu (Nested Drill-down & Fast Exit):
     - **Đường tắt (Fast-path / Early Exit):** Nếu hồ sơ rõ ràng (ví dụ: chưa từng trễ hạn nợ, hoặc xe đỗ hầm không có nhu cầu đặc thù), luồng chỉ cần qua 2 câu là trả kết quả ngay ($1 \rightarrow 2 \rightarrow \text{Result}$).
     - **Đào sâu theo ngữ cảnh (Contextual Drill-down):** Khi người dùng chọn một đáp án phức tạp (ví dụ: từng có nợ xấu hoặc xe chạy dịch vụ), hệ thống tự động bung các câu hỏi nhánh con ($1 \rightarrow 2 \rightarrow 2.1 / 2.2 \rightarrow 3.1 / 3.2 \rightarrow \text{Result}$) để bắt đúng bệnh.
   - Số lượng câu hỏi dao động linh hoạt từ **1 đến 4 câu** tuỳ theo hành vi trả lời thực tế.
4. **Không dùng phán xét nhị phân YES/NO:** Tránh gây hụt hẫng (churn) và phòng ngừa rủi ro pháp lý/cam kết ảo. Thay vào đó dùng **"Tỷ lệ phê duyệt dự kiến"** kèm **"Giải pháp khả thi thay thế"**.

---

## 1.4. KIẾN TRÚC DỮ LIỆU ĐỒ THỊ CÂU HỎI (GRAPH-BASED JSON SCHEMA)

Để hỗ trợ cơ chế nhảy câu hỏi linh hoạt ($1 \rightarrow 2 \rightarrow 2.1 / 2.2 \rightarrow 3.x \rightarrow \text{Result}$), cấu trúc cấu hình Quiz được định nghĩa dưới dạng Đồ thị hữu hướng (Directed Graph) thay vì mảng phẳng:

```json
{
  "quiz_id": "car_insurance_diagnostic",
  "root_question_id": "q1",
  "nodes": {
    "q1": {
      "question": "Chiếc xe của bạn hiện đang thuộc trường hợp nào dưới đây?",
      "options": [
        { "label": "Xe mới lăn bánh dưới 3 năm (Gia đình)", "next_node": "q2_new_car" },
        { "label": "Xe đi trên 3 năm (Hết bảo hành hãng)", "next_node": "q2_old_car" },
        { "label": "Xe có chạy dịch vụ / Chạy khách", "next_node": "q2_commercial" }
      ]
    },
    "q2_new_car": {
      "question": "Chỗ đỗ xe qua đêm của bạn thường ở đâu?",
      "options": [
        { "label": "Gửi hầm chung cư an toàn", "next_node": "q3_repair_pref" },
        { "label": "Khu vực cứ mưa to là ngập đường", "next_node": "q2_1_flood_risk" }
      ]
    },
    "q2_1_flood_risk": {
      "question": "Đoạn ngập thường sâu đến mức nào khi bạn phải lái qua?",
      "options": [
        { "label": "Nước ngập nửa bánh xe", "next_node": "result_flood_special" },
        { "label": "Chỉ mấp mé mép bánh xe", "next_node": "q3_repair_pref" }
      ]
    },
    "result_flood_special": {
      "type": "result",
      "tier": "flood_comprehensive_pack"
    }
  }
}
```

Mỗi lựa chọn (`option`) quyết định trực tiếp node tiếp theo (`next_node`), cho phép:
- Nhảy sang câu hỏi đào sâu chuyên biệt (`q2.1`, `q2.2`).
- Nhảy cóc qua các câu hỏi không liên quan.
- Kết thúc sớm và hiển thị màn hình kết quả ngay lập tức khi đã đủ dữ liệu chẩn đoán (`result_*`).

---

## 2. TỔNG HỢP KỊCH BẢN QUIZ THEO TỪNG DÒNG SẢN PHẨM

---

### SẢN PHẨM 1: BẢO HIỂM THÂN VỎ Ô TÔ (CAR PHYSICAL DAMAGE INSURANCE)

- **Định vị:** Chuyên gia tư vấn "Bắt bệnh" gói bảo hiểm - Mua đúng, không bị "hành", không bị "hớ".
- **JTBD của chủ xe:** Muốn biết xe của mình mua hết bao nhiêu tiền, nên mua điều khoản nào, có thể bỏ bớt điều khoản thừa nào để tiết kiệm tiền, và hãng nào bồi thường nhanh nhất.

#### Cây Rẽ Nhánh (Decision Tree Flow)

```
[Câu 1 - Root]: Chiếc xe của bạn thuộc trường hợp nào dưới đây?
  │
  ├──► [Nhánh 1]: Xe mới mua hoặc lăn bánh dưới 3 năm (Đi gia đình/cá nhân)
  │      ├──► Câu 1.1: Chỗ đỗ xe qua đêm của bạn thường ở đâu?
  │      └──► Câu 1.2: Nếu chẳng may xe bị móp xước cản, bạn muốn sửa ở đâu?
  │             └──► KẾT QUẢ: Gói "Toàn diện giữ Zin xe"
  │
  ├──► [Nhánh 2]: Xe đã đi trên 3 năm (Đã hết thời gian bảo hành hãng)
  │      ├──► Câu 2.1: Trong 1 năm vừa qua, bạn có từng gọi bảo hiểm làm vụ nào không?
  │      └──► Câu 2.2: Sẵn sàng tự trả 500k vết xước nhỏ để giảm 20% phí cả năm không?
  │             └──► KẾT QUẢ: Gói "Tiết kiệm thông minh - Cắt giảm phí thừa"
  │
  └──► [Nhánh 3]: Xe có chạy dịch vụ, Grab/Be hoặc cho thuê tự lái
         ├──► Câu 3.1: Xe đang đăng ký biển số màu gì?
         └──► Câu 3.2: Khi xe vào xưởng làm bảo hiểm, điều gì khiến bạn đau đầu nhất?
                └──► KẾT QUẢ: Gói "Bảo vệ xe kinh doanh - Bồi thường siêu tốc"
```

#### Chi tiết Câu hỏi & Phương án Lựa chọn

##### Câu 1 (Root - Câu Gốc)
**Chiếc xe của bạn hiện đang thuộc trường hợp nào dưới đây?**
- A. Xe mới mua hoặc lăn bánh dưới 3 năm (Chủ yếu đi gia đình/cá nhân) *(Rẽ sang Nhánh 1)*
- B. Xe đã đi trên 3 năm, đã hết thời gian bảo hành hãng *(Rẽ sang Nhánh 2)*
- C. Xe có chạy dịch vụ, Grab/Be hoặc cho thuê tự lái *(Rẽ sang Nhánh 3)*

##### Nhánh 1: Xe mới / Xe lướt (Dưới 3 năm)
- **Câu 1.1 (Tuỳ câu trả lời): Chỗ đỗ xe qua đêm của bạn thường ở đâu?**
  - A. Hầm chung cư hoặc bãi có mái che, bảo vệ *(An toàn, không lo vặt gương)*
  - B. Đỗ ngoài vỉa hè, trước cửa nhà lộ thiên *(Nguy cơ cao: Vặt gương, quẹt trộm ban đêm)*
  - C. Khu vực cứ mưa to là ngập đường *(Cảnh báo đỏ: Nguy cơ thủy kích)*
- **Câu 1.2 (Tuỳ câu trả lời): Nếu chẳng may xe bị móp méo trầy xước, bạn muốn sửa ở đâu?**
  - A. Nhất định phải vào đúng Xưởng chính hãng *(Ưu tiên: Phụ tùng zin, sơn chuẩn màu hãng)*
  - B. Gara ngoài uy tín cũng được, miễn gần nhà và lấy xe nhanh

##### Nhánh 2: Xe gia đình đã đi lâu năm (Trên 3 năm)
- **Câu 2.1 (Tuỳ câu trả lời): Trong 1 năm vừa qua, bạn có từng gọi bảo hiểm làm vụ nào không?**
  - A. Không lần nào, tay lái cẩn thận chỉ đi làm hàng ngày
  - B. Có vài vết xước nhẹ nhưng tự bỏ tiền ra sơn ngoài cho nhanh
  - C. Đã từng va chạm nặng hoặc ngập nước phải làm bảo hiểm lớn
- **Câu 2.2 (Tuỳ câu trả lời): Bạn có sẵn sàng tự trả 500k cho mỗi lần xước xát nhỏ để đổi lại giảm ngay 20% - 30% tiền mua bảo hiểm cả năm không?**
  - A. Rất sẵn sàng, vì cả năm hiếm khi quẹt, chỉ cần bảo hiểm đền khi có va chạm lớn hoặc ngập nước
  - B. Không, xe xước dù nhỏ nhất mình cũng muốn bảo hiểm lo hết từ A-Z

##### Nhánh 3: Xe chạy dịch vụ / Kinh doanh
- **Câu 3.1 (Tuỳ câu trả lời): Chiếc xe của bạn đang đăng ký biển màu gì?**
  - A. Biển số vàng *(Đăng ký kinh doanh vận tải chính thức)*
  - B. Biển số trắng nhưng có chạy khách ngoài / Chở tour kiếm thêm *(Cảnh báo: Không mua đúng điều khoản kinh doanh sẽ bị từ chối đền 100%)*
- **Câu 3.2 (Tuỳ câu trả lời): Khi xe phải vào xưởng làm bảo hiểm, điều gì khiến bạn đau đầu nhất?**
  - A. Bị giam xe quá lâu, mỗi ngày nằm xưởng là mất đứt 500k - 1 triệu tiền chạy xe
  - B. Thủ tục giấy tờ hành xác, bắt tài xế đi lại nhiều lần bổ sung biên bản hiện trường

#### Thiết kế Màn hình Kết quả (60% Reveal / 40% Gated)
- **60% Public trên Web:**
  1. *Khung giá thị trường:* Biểu phí chuẩn ngoài đại lý: 8.500.000đ - 9.800.000đ/năm.
  2. *Gói bảo hiểm nên mua & nên bỏ:* Bắt buộc có Thủy kích + Gara chính hãng; Cắt bỏ gói mất cắp gương nếu đỗ hầm (tiết kiệm 1.200.000đ); Chọn mức khấu trừ 500k (tiết kiệm thêm 15%-20%).
  3. *So sánh sơ bộ 4 hãng lớn:* PVI (bồi thường nhanh nhất), Bảo Việt (gara chính hãng phủ kín), PTI (cứu hộ 24/7), MIC (phí cạnh tranh nhất).
- **40% Khóa để chuyển đổi sang App:**
  - Bảng giá chính xác từng đồng của 4 hãng (`6.xxx.000đ`).
  - Voucher hoàn tiền đến 1.500.000đ vào Ví MoMo hoặc Voucher quà tặng xăng xe.
  - Luồng bồi thường va quẹt nhỏ bằng chụp ảnh trên App không cần chờ giám định viên.
- **Nút CTA Web-to-App:** `Mở App MoMo để mở khóa bảng giá 4 hãng & Ưu đãi` (Cam kết: *Không gọi điện làm phiền - Tự chủ 100% online*).

---

### SẢN PHẨM 2: VAY NHANH (FAST CONSUMER LOAN)

- **Định vị:** Đánh giá độ phù hợp hồ sơ giải ngân tức thì 100% online, loại bỏ nỗi sợ bị từ chối (Rejection Anxiety).
- **JTBD của người vay:** Đang cần tiền gấp giải quyết việc phát sinh, muốn biết mình có cơ hội vay được không, trả góp mỗi tháng bao nhiêu, thủ tục mất bao lâu.

#### Bộ 4 Câu hỏi Zero-Click Entry
- **Câu 1: Số tiền bạn đang muốn hỗ trợ tài chính là bao nhiêu?**
  - A. 2.000.000đ - 5.000.000đ *(Nhu cầu vi mô, cấp bách)*
  - B. 6.000.000đ - 15.000.000đ *(Khoảng phổ biến nhất)*
  - C. 16.000.000đ - 30.000.000đ *(Mức trần giải ngân nhanh)*
  - D. Trên 30.000.000đ *(Nhu cầu vay tiêu dùng lớn)*
- **Câu 2: Bạn đang cần khoản tiền này gấp trong bao lâu?**
  - A. Cần gấp trong ngày hôm nay *(Đánh mạnh vào tính năng giải ngân sau 1 phút)*
  - B. Trong vài ngày tới
  - C. Đang khảo sát để chuẩn bị tài chính dự phòng
- **Câu 3: Thu nhập hàng tháng của bạn đến từ hình thức nào?**
  - A. Nhận lương qua chuyển khoản ngân hàng *(Điểm tín nhiệm: +2)*
  - B. Kinh doanh tự do / Bán hàng / Làm nghề tự do *(Điểm tín nhiệm: +1)*
  - C. Lương tiền mặt / Thu nhập khác *(Điểm tín nhiệm: 0)*
- **Câu 4: Lịch sử trả nợ thẻ tín dụng hoặc các khoản vay trước đây?**
  - A. Chưa từng vay ai hoặc luôn trả đúng hạn *(Điểm tín nhiệm: +2)*
  - B. Thỉnh thoảng trễ hạn 1-3 ngày nhưng đã thanh toán đầy đủ *(Điểm tín nhiệm: +1)*
  - C. Đang có khoản vay ở ngân hàng/ứng dụng khác *(Điểm tín nhiệm: 0)*

#### Ma trận Trả Kết quả (Scoring Matrix)
- **Hồ sơ Loại A (Tổng điểm 3-4):**
  - *Kết quả:* Khả năng duyệt đạt **95%**. Đủ điều kiện nhận gói đúng số tiền mong muốn.
  - *Ước tính trả góp:* Chỉ từ ~350.000đ/tháng (chia nhỏ 6-12 tháng). Tốc độ giải ngân 1 phút.
  - *CTA:* `Nhận khoản vay trên App MoMo`.
- **Hồ sơ Loại B (Tổng điểm 1-2 hoặc Nhu cầu >15tr):**
  - *Kết quả:* Gói [Số tiền chọn] cần thêm hồ sơ chứng minh thu nhập. Đề xuất phương án tối ưu: Nhận trước gói giải ngân tức thì 100% online **5.000.000đ - 10.000.000đ** không cần giấy tờ.
  - *CTA:* `Xem gói vay khả thi trên App MoMo`.
- **Hồ sơ Loại C (Tổng điểm 0):**
  - *Kết quả:* Hướng sang giải pháp Chi tiêu trước - Trả sau (Ví Trả Sau miễn lãi 45 ngày) hoặc gói vay siêu nhỏ 2 triệu để xây dựng lại lịch sử tín dụng.
  - *CTA:* `Kích hoạt giải pháp thay thế trên App MoMo`.

---

### SẢN PHẨM 3: VÍ TRẢ SAU (BUY NOW PAY LATER - BNPL)

- **Định vị:** Tự kiểm tra điều kiện cấp hạn mức chi tiêu trước - trả tiền sau.
- **JTBD của người dùng:** Tò mò xem mình có được cấp tiền chi tiêu mua sắm/đi chợ/thanh toán hóa đơn không, có tốn lãi phí không.

#### Bộ 3 Câu hỏi
- **Câu 1: Bạn thường chi tiêu nhiều nhất cho nhu cầu nào hàng tháng?**
  - A. Đi siêu thị, cửa hàng tiện lợi, mua thực phẩm
  - B. Nạp tiền điện thoại, thanh toán hóa đơn điện/nước/internet
  - C. Mua sắm online, đặt đồ ăn công nghệ
  - D. Đi ăn uống, cafe, xem phim cuối tuần
- **Câu 2: Trung bình mỗi tháng bạn chi tiêu không dùng tiền mặt khoảng bao nhiêu?**
  - A. Dưới 1 triệu
  - B. Từ 1-3 triệu
  - C. Từ 3-5 triệu
  - D. Trên 5 triệu
- **Câu 3: Bạn đã có tài khoản MoMo và liên kết ngân hàng chưa?**
  - A. Đã có và dùng thường xuyên
  - B. Có tài khoản nhưng ít khi dùng
  - C. Chưa có tài khoản MoMo

#### Màn hình Kết quả (60% Reveal / 40% Gated)
- **60% Public trên Web:**
  - *Tỷ lệ mở thành công sơ bộ:* 92% (Hồ sơ rất tiềm năng).
  - *Khoảng hạn mức đề xuất kích hoạt lần đầu:* 1.000.000đ - 3.000.000đ (có thể tăng lên đến 10.000.000đ sau vài tháng chi tiêu).
  - *Quyền lợi:* 0% lãi suất lên đến 45 ngày, thanh toán tại hơn 50.000 điểm đối tác.
- **40% Khóa để chuyển đổi sang App:**
  - Hạn mức chính xác được cấp riêng cho số điện thoại của bạn.
  - Bộ thẻ quà tặng giảm giá 50.000đ - 100.000đ áp dụng cho lần thanh toán đầu tiên bằng Ví Trả Sau.
- **Nút CTA Web-to-App:** `Kích hoạt hạn mức trên App MoMo`.

---

### SẢN PHẨM 4: TIẾT KIỆM & TÍCH LŨY (WEALTH / SAVINGS)

- **Định vị:** Lập kế hoạch "Tiền đẻ ra tiền" - Tối ưu tiền nhàn rỗi hàng tháng.
- **JTBD của người dùng:** Có một khoản tiền nhàn rỗi (vài triệu đến vài chục triệu) để trong tài khoản thanh toán không có lãi, muốn tìm chỗ gửi an toàn, sinh lời mỗi ngày và rút ra linh hoạt khi cần.

#### Bộ 3 Câu hỏi
- **Câu 1: Bạn thường có khoản tiền nhàn rỗi hàng tháng khoảng bao nhiêu?**
  - A. Từ 500.000đ - 3.000.000đ *(Tiền tiêu vặt dư ra cuối tháng)*
  - B. Từ 5.000.000đ - 20.000.000đ *(Tiền dự phòng công việc/gia đình)*
  - C. Trên 20.000.000đ *(Khoản tích lũy lớn chờ cơ hội đầu tư)*
- **Câu 2: Bạn cần rút khoản tiền này ra sử dụng khi nào?**
  - A. Bất cứ lúc nào cần là phải rút được ngay, không bị mất lãi
  - B. Có thể gửi cố định từ 1-3 tháng
  - C. Gửi dài hạn từ 6 tháng đến 1 năm trở lên
- **Câu 3: Nỗi lo lớn nhất của bạn khi đem tiền đi gửi tích lũy?**
  - A. Lãi suất tài khoản ngân hàng thông thường quá thấp (gần như bằng 0%)
  - B. Rút trước hạn bị mất hết toàn bộ tiền lãi
  - C. Thủ tục mở sổ tiết kiệm tại quầy rườm rà

#### Màn hình Kết quả (60% Reveal / 40% Gated)
- **60% Public trên Web:**
  - *Chẩn đoán sản phẩm tối ưu:* 
    - Nếu cần rút linh hoạt: Đề xuất **Túi Thần Tài (Sinh lời mỗi ngày đến ~5%/năm, rút tiền tức thì về ví vẫn giữ nguyên tiền lãi)**.
    - Nếu gửi có kỳ hạn: Đề xuất **Tiết kiệm Ngân hàng đối tác trên MoMo (Lãi suất cạnh tranh hơn quầy đến 0,5%)**.
  - *Bảng tính tiền lời ước tính:* Nhập số tiền nhàn rỗi -> Hiển thị số tiền lãi nhận được mỗi ngày/mỗi tháng.
- **40% Khóa để chuyển đổi sang App:**
  - Kích hoạt tính năng "Tự động sinh lời mỗi ngày" từ số dư ví.
  - Quà tặng 20.000đ - 50.000đ nạp đầu vào Túi Thần Tài.
- **Nút CTA Web-to-App:** `Mở Túi Thần Tài nhận tiền lời mỗi ngày trên MoMo`.

---

## 3. KIẾN TRÚC TÍCH HỢP HỆ THỐNG (INTEGRATION ARCHITECTURE)

```
[CMS / Content Repository]
  │
  ├──► Strategy 1: Manual Embed (Frontmatter Override)
  │      └── Bài viết chỉ định: `quiz_id: "car_damage_advisor"`
  │
  └──► Strategy 2: Dynamic Taxonomy Mapping (Auto Injection)
         └── Bài viết có `theme_id: "bao-hiem-xe"`
               └── Tự động mount Component `<QuizWidget theme="car_insurance" />`
```

### 3.1. Kế hoạch Ngắn hạn (Manual Embed)
- Đóng gói Quiz thành một Shared UI Component chuẩn trong Design System: `<QuizWidget quizId="..." />`.
- Nhúng cố định vào chân bài viết (hoặc đặt xen kẽ giữa bài viết tại Zone 3/Zone 4) trên Top 20 bài viết có lượng truy cập tự nhiên (Organic Traffic) cao nhất thuộc các Theme tương ứng.

### 3.2. Kế hoạch Dài hạn (Dynamic Taxonomy Engine vs. Bẫy Dynamic AI)
- **Cảnh báo về Dynamic AI runtime:** Tuyệt đối không để AI tự đọc bài viết và tự sinh câu hỏi lúc người dùng đang duyệt trang (vì gây độ trễ LCP, chi phí token cao và nguy cơ sinh ra câu hỏi kiểm tra đọc hiểu ngô nghê thay vì câu hỏi phễu bán hàng).
- **Giải pháp chuẩn hóa (Taxonomy-driven Auto Injection):**
  - Mỗi bài blog đều được gắn nhãn `theme_id` (ví dụ: `theme_vay_nhanh`, `theme_vi_tra_sau`, `theme_bao_hiem_oto`).
  - Hệ thống CMS tự động map `theme_id` của bài viết với `Master Quiz Template` tương ứng. Nếu Content Editor không cấu hình đè (override), hệ thống tự động chèn Quiz chuẩn của Theme đó vào chân bài viết.
  - **Ứng dụng AI chuẩn mực (Offline Human-in-the-loop):** Sử dụng AI trong pipeline CMS lúc Content Editor viết bài: AI đọc bài viết -> gợi ý Theme phù hợp -> tự động điền mã Quiz tương ứng.

---

## 4. QUY CHUẨN ĐO LƯỜNG & TRACKING UMAMI (TRACKING SSOT)

Toàn bộ các Quiz áp dụng bộ Event Schema chuẩn mực đồng nhất để theo dõi phễu chuyển đổi:

| Tên Sự kiện (Event Name) | Điều kiện kích hoạt (Trigger) | Schema Tham số (Event Data) | Ý nghĩa phân tích |
| :--- | :--- | :--- | :--- |
| `quiz_view` | Quiz xuất hiện trong Viewport | `quiz_id`, `theme`, `placement` (`standalone`, `blog_bottom`, `blog_inline`) | Đo lường độ phủ hiển thị (Reach Rate) |
| `quiz_start` | Chạm vào đáp án Câu hỏi 1 | `quiz_id`, `theme`, `first_choice` | Đo lường tỷ lệ bắt đầu (Start Rate) |
| `quiz_step` | Hoàn thành mỗi câu hỏi | `quiz_id`, `step_index` (1, 2, 3), `question_key`, `selected_option` | Đo lường tỷ lệ rơi rụng (Drop-off Rate) qua từng bước |
| `quiz_complete` | Màn hình kết quả 60% hiển thị | `quiz_id`, `result_tier`, `persona_id` | Đo lường tỷ lệ hoàn tất (Completion Rate) |
| `quiz_click_cta` | Nhấp vào nút mở App MoMo | `quiz_id`, `result_tier`, `destination_deeplink` | Đo lường tỷ lệ chuyển đổi cuối cùng (Web-to-App Conversion) |

---

## 5. LỘ TRÌNH TRIỂN KHAI (IMPLEMENTATION ROADMAP)

| Giai đoạn | Thời gian | Hạng mục thực hiện | Mục tiêu & Output |
| :--- | :--- | :--- | :--- |
| **Đợt 1: Vay Nhanh** | Tuần 1 | Triển khai Quiz Vay Nhanh trên Landing Page chuyên biệt | Validate Start Rate (>25%) và CTA Conversion (>80%) |
| **Đợt 2: Bảo hiểm Thân vỏ** | Tuần 2 | Dựng luồng rẽ nhánh 3 Persona cho Bảo hiểm Thân vỏ Ô tô | Đạt tỷ lệ hoàn tất >60% cho sản phẩm High-Ticket |
| **Đợt 3: Ví Trả Sau & Wealth** | Tuần 3 | Đóng gói Quiz Ví Trả Sau và Túi Thần Tài | Hoàn thiện bộ 5 Master Quiz trụ cột |
| **Đợt 4: Blog Auto-Injection** | Tuần 4 | Tích hợp cơ chế tự động gắn Quiz theo `theme_id` vào toàn bộ hệ thống Blog | Mở rộng quy mô tiếp cận toàn bộ traffic Web Platform |
