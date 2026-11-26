# 2026 REFLECTION & 2027 DIRECTION - WEB PLATFORM

---

## 1. EXECUTIVE SUMMARY

**Năm 2026, Web đạt 36,91 triệu PageView (Non-Paid 29,09 triệu, 78,8%) và 44.684 lượt cài App từ Jul đến Nov. Năm 2027, Web là entry point từ out-app cho user chưa có App: Nurture nhu cầu từ Google và AI, chuyển đổi (Conversion) sang cài App và điều hướng đến các Service của MoMo theo hướng Product-Led Growth. Web cam kết 38,9-41,1 triệu PageView Non-Paid (Base case; Best case 55,57 triệu) và đặt KPI 2027 là 30.000 Install mỗi tháng (khoảng 360.000 Install cả năm).**

**Kết quả 2026**

1. **Non-Paid là động lực tăng trưởng.** Tổng PageView tăng 39% và Non-Paid tăng 53% trong khi Paid giảm; Nov vượt mục tiêu tháng.
2. **AI Traffic nhỏ nhưng chất lượng cao.** Traffic từ AI tăng 177% mỗi ngày từ May đến Nov. Tỷ lệ Click-to-App của AI (5,24%) cao hơn Organic (2,96%) và ngang Direct, dù AI mới chiếm khoảng 0,5% tổng PageView.
3. **Utility chứng minh hiệu quả chuyển đổi.** Utility đạt CTR 33,7-43,8%, nội dung tĩnh gần như 0%. Sau khi tái cấu trúc Financial Hub theo hướng Utility, Non-Paid của hub này tăng 105%.
4. **Web có năng lực tạo GMV.** Cinema đạt 16,01 tỷ đ GMV, Bảo hiểm y tế đạt 2,67 tỷ đ GMV với chi phí SEO 150 triệu đ. Vé xe và eSIM du lịch cũng đã ghi nhận GMV.
5. **Web tạo user mới cho App.** 44.684 Install, 14.735 đăng ký và 5.093 MAU từ Jul đến Nov.
6. **MoSpark vận hành từ Q2.** Web Platform hợp nhất thành Growth Unit và đưa vào vận hành MoSpark gồm Landing Page Builder, GenAI Content Pipeline (tự động khoảng 80% quy trình nội dung SEO/GEO), PLG Project Engine, Ads Manager và Chatbot. Thời gian dựng Landing Page giảm từ 1-2 tuần xuống 1-2 ngày; 16 Cell Teams được hỗ trợ, 6 đội tự xuất bản.
7. **Chuẩn hóa kỹ thuật.** GA4 và GTM vào BigQuery, 100% liên kết chuẩn hóa OneLink, Dashboard Web Performance live từ May, Identity Platform nối hành vi từ Web sang App, và chuyển 100% từ AWS sang FPT Cloud không gián đoạn.

**Điểm cải thiện 2027**

- **Thiết kế Microjourney cho các Utility.** 76% Install hiện đến từ một banner toàn trang. Mỗi Utility cần một Microjourney riêng: kết quả tra cứu mở thẳng đúng Service trong App qua OneLink, giữ đúng ngữ cảnh từ Out-App đến In-App. Mục tiêu giảm tỷ trọng banner xuống dưới 50%, quản lý bằng Ads Manager trên MoSpark.
- **Giữ ngữ cảnh khi chuyển sang App.** Hơn 90% người chọn ghế Cinema bỏ dở ở bước thanh toán trong App; Bảo hiểm ô tô chỉ chốt 71 trên 2.118 lead. Microjourney cần mở App đúng bước và giữ nguyên lựa chọn đã có.
- **Mở rộng GEO/AEO.** AI Overview và AI Assistant trả lời trực tiếp, Organic tăng chậm hơn Non-Paid tổng. GEO/AEO bổ sung cho SEO để giữ lưu lượng từ nhu cầu tìm kiếm.

**Đề xuất 2027**

| Chỉ số | Baseline 2026 | Base case 2027 (cam kết) | Best case 2027 |
| :--- | :--- | :--- | :--- |
| PageView Non-Paid | 32,77M (ước cả năm) | 38,9-41,1M (+19% đến +25%) | 55,57M (+70%) |
| Tổng PageView Web | 40,69M (ước cả năm) | 46,8-49,0M (+15% đến +20%) | 63,49M (+56%) |
| W2A CTR | 3,36% (Oct) | Không thấp hơn 3,36% (0%) | 4,0-4,5% (+19% đến +34%) |
| KPI: Install mỗi tháng | 11.143 (Oct) | 30.000 (+169%) | 30.000 (+169%) |

---

## 2. ROLE OF WEB

Web là kênh thu hút user từ ngoài App cho hệ sinh thái MoMo. Khi ai đó hỏi Google hay ChatGPT về một việc cần làm và momo.vn trả lời đúng, họ vào Web, làm xong phần việc đầu tiên rồi được chuyển sang đúng dịch vụ trong App, từ Anchors đến Adjacent và Monetization, giữ đúng ngữ cảnh từ Out-App đến In-App. Với user chưa có App, đây là cơ hội New User Acquisition: họ đi tiếp đến Install và đăng ký.

Nhu cầu không do Web tạo ra. Nó đến từ Search Engine và AI Agent như Google, ChatGPT, Gemini, Perplexity, nơi user đã có ý định rõ (high-intent). Utility và nội dung trả lời đúng nhu cầu đó tạo ra Non-Paid Traffic, còn Microjourney đưa Traffic sang App. Một số Utility như giá vàng, giá xăng dầu, tỷ giá còn khiến user quay lại Web (retain).

Vì vậy Web cần cả quy mô lẫn chất lượng: đủ Traffic để có user, đủ qualified và relevant để họ sang App. Hiệu suất đo bằng Non-Paid Traffic, Click to App, Install và Shared-KPI với BU.

### 2.1. Web đứng ở đâu trong User Journey

**Web đảm nhận hai bước Tiếp cận và Kiểm tra: thu hút Traffic từ Search Engine và AI Agent, rồi để user tự xử lý việc cần làm bằng Utility. Ở bước Hành động, Web chuyển user sang App bằng một Offer, và App đảm nhận xác minh hoặc thanh toán.** Web chịu trách nhiệm PageView, Click to App và Install; GMV, DAU, MAU, MEU là chỉ số cùng BU. Mỗi Journey được thiết kế theo JTBD của user, với một Microjourney liền mạch từ Web sang App.

**Bốn bước Microjourney mà Web đảm nhận**

| Bước | User đang làm gì | Web làm gì | Web chịu trách nhiệm | Cùng BU |
| :--- | :--- | :--- | :--- | :--- |
| **Tiếp cận** | Hỏi Google hoặc AI | Trả lời để được tìm thấy và được AI trích dẫn | PageView, Impression, AI citation | - |
| **Kiểm tra** | Tự xem tình huống của mình | Công cụ tương tác: CIC, ước tính khoản vay, Phạt Nguội, tính lương, lịch chiếu | Lượt dùng công cụ, CTR công cụ | - |
| **Hành động** | Sang App để xác minh hoặc thanh toán | Một Offer, giữ đúng ngữ cảnh từ Out-App đến In-App | W2A CTR, Install | GMV |
| **Quay lại** | Đăng ký, liên kết ngân hàng, dùng tiếp | Identity Platform, cá nhân hóa theo trạng thái | Install đến đăng ký | DAU, MAU, MEU |

**Giá trị Web mang lại cho từng BU**

| BU | Service | Giá trị Web mang lại |
| :--- | :--- | :--- |
| Movies | Cinema | Traffic và GMV |
| Financial Services | Ví Trả Sau, Vay Nhanh, Túi Thần Tài, Tiết kiệm, Chứng chỉ quỹ | Traffic và Click to App |
| InsurTech | Bảo hiểm xe, bảo hiểm y tế | Traffic và GMV |
| User Growth (New User) | Cài App, đăng ký | Install và đăng ký |

### 2.2. Năm nguyên tắc thiết kế Microjourney trên Web

1. **Tối ưu Conversion giữa các bước, không chỉ tăng Traffic.** Điểm rơi lớn nhất nằm giữa Service user vừa dùng trên Web và Service tiếp theo trong App: Install sang đăng ký đạt 33,0% (Jul-Nov; Nov MTD: 30,3%), và hơn 90% người chọn ghế Cinema bỏ dở ở bước thanh toán.
2. **Mỗi Microjourney chỉ có một Offer.** Offer đặt đúng lúc user vừa có kết quả, giữ đúng ngữ cảnh từ Out-App đến In-App, và gọi đúng việc đang làm ("Kiểm tra hạn mức với điểm CIC này" thay cho "Tải App"). Nguyên tắc rút từ khung Microjourneys: zero-data entry, peak-intent placement, action-oriented framing, one offer per flow.
3. **Một tín hiệu trên Web phục vụ nhiều Service.** Kết quả tra CIC cho thấy khả năng phù hợp với Ví Trả Sau, Vay Nhanh hoặc Tích lũy; tra Phạt Nguội cho thấy nhu cầu bảo hiểm xe. Tín hiệu nào được dùng phải xuất phát từ bài toán kinh doanh của từng BU.
4. **Web có năng lực Product Educate, không capture được dữ liệu user.** Theo khung Microjourneys, user có hành vi Investment (Data, Money, Relationship) giữ chân cao hơn 9-12 điểm phần trăm so với user chưa Investment, nhưng Investment chỉ xảy ra trong App. Việc của Web là Educate: giúp user hiểu Service và biết bước tiếp theo, để họ sẵn sàng Investment ngay khi vào App.
5. **Thiết kế từ User Journey tổng thể, không cross-sell rời rạc.** Vẽ hành trình của user trước, sau đó mới đặt các touchpoint của Web vào đúng vị trí.

### 2.3. Cách Web điều hướng user sang Service khác

Mọi hành trình Web đề xuất trong tài liệu này viết theo một công thức:

> Khi user **vừa làm X trên Web**, Web dẫn sang **dịch vụ Y** bằng **Offer Z, giữ đúng ngữ cảnh từ Out-App đến In-App**, đo bằng **chỉ số W**.

| User vừa làm | Điều hướng sang | Bằng cách | Đo bằng |
| :--- | :--- | :--- | :--- |
| Tra điểm CIC | Ví Trả Sau | "Kiểm tra hạn mức với điểm này", giữ đúng ngữ cảnh từ Out-App đến In-App | Click to App |
| Ước tính khoản vay | Vay Nhanh | Mở App với số tiền đã nhập | Click to App, Install |
| Chọn suất chiếu, ghế | Thanh toán Cinema | QR hoặc OneLink giữ nguyên lựa chọn | Giao dịch, Install |
| Tính lương | Túi Thần Tài | Gợi ý để riêng phần tích lũy | Click to App, MAU |
| Tra Phạt Nguội | Bảo hiểm xe | Báo giá theo loại xe đã nhập | Click to App, GMV Bảo hiểm |

Mỗi dòng bắt đầu từ việc user đang làm, không bắt đầu từ sản phẩm MoMo muốn bán. Đây là điểm khác giữa dẫn đường và bán chéo.

**Cấu trúc trang để điều hướng được user.** Mỗi trang trên momo.vn có 3 khối, theo thứ tự:

1. **Trả lời câu hỏi** của user, đủ rõ để Google và AI trích dẫn (GEO).
2. **Công cụ để user tự kiểm tra trường hợp của mình.** Đây là bước tạo tín hiệu cho dịch vụ tiếp theo.
3. **Một lời mời duy nhất**, gọi đúng việc tiếp theo và giữ đúng ngữ cảnh từ Out-App đến In-App, không phải banner chung.

Trang chỉ có khối 1 dễ bị AI lấy mất lượt nhấp và không dẫn được ai. Bảng tĩnh giá vàng, tỷ giá, lãi suất năm 2026 (CTR 0%) là ví dụ. Trang có đủ 3 khối mới tạo được lượt chuyển sang dịch vụ.


**Trust đi xuyên suốt từ Search Engine đến Web và App.** Trust là điều kiện để AI Agent trích dẫn (AI ưu tiên nguồn có giấy phép, biểu phí công khai, kênh khiếu nại, tác giả có tên) và để user yên tâm sang App. Web cần ba thành phần: giấy phép hoạt động theo từng Service tài chính, bảo hiểm; chứng nhận an toàn thông tin; kênh Báo cáo lừa đảo ẩn danh. Hiện Web đã có kênh Báo cáo lừa đảo ẩn danh, còn trang tổng hợp giấy phép và pháp lý chưa có, sẽ pilot trên cụm CIC từ Jan/2027.


---

## 3. REFLECTION 2026

### 3.1. Vai trò và mô hình phục vụ

Web Platform được hình thành trong Growth Platform Division từ tháng 3/2026; tháng 4/2026 Out-App Traffic thành lập mới trong User Engagement và sáp nhập vào Web Platform từ tháng 5/2026. Đơn vị phụ trách nền tảng công nghệ dùng chung cho Web MoMo, phối hợp ITC cung cấp hạ tầng, thư viện, công cụ và quy trình cho các Mini Web trên momo.vn của Cell Teams, BUs và Division. Giá trị tạo ra ở 3 tầng:

- **Tầng MoMo:** xây Content Authority cho các Theme theo hành trình user, để Google Search và AI Chatbot (ChatGPT, Gemini, Perplexity) trích dẫn MoMo là nguồn uy tín.
- **Tầng User:** xây Utility Tools giải quyết nhu cầu cụ thể ngay trong lúc tìm kiếm, thay cho nội dung tĩnh.
- **Tầng BUs:** Platform-as-a-Service nội bộ: tư vấn giải pháp, cung cấp nền tảng, đồng hành dự án chiến lược theo Product-Led Growth.

**Hai mô hình phục vụ:**

- **CMS tự phục vụ (BUs Self-serve):** phối hợp BMC xây Admin Panel để BU tự tạo, chỉnh sửa và xuất bản trang.
- **Phát triển trực tiếp (Dedicated Build):** đồng hành Cell Teams xây Web Product có UI/UX và nghiệp vụ riêng theo Mobase Design System, ở 3 mức: tư vấn, đồng hành phát triển, chuyển giao tự vận hành. Điển hình: Cinema Hub, Vehicle Hub, Financial Hub, Student Hub.

**Giá trị kinh tế:** thay vì mỗi Cell Team duy trì đội kỹ thuật Web và tên miền riêng, tất cả kết nối vào momo.vn để thừa hưởng uy tín thương hiệu, Domain Authority và hạ tầng đã chuẩn hóa.

**Objectives 2026:**

| Objective | Hoạt động | Kết quả chính đến 10/2026 |
| :--- | :--- | :--- |
| Objective 1: Phát triển Strategic Themes theo PLG | Tăng trưởng | Rà soát hơn 30 Theme; triển khai PLG cho Cinema, Financial, Vehicle và Student. Cinema 9,1M PV trong 10 tháng; Financial 273.705 PV tháng 10. |
| Objective 2: CMS tự phục vụ bằng AI | Nền tảng | MoSpark vận hành từ Q2. 16 Cell Teams được hỗ trợ, 6 tự vận hành. Landing page rút từ 1-2 tuần xuống 1-2 ngày. |
| Objective 3: Đo lường Full Funnel Web-to-App | Nền tảng | GA4 và OneLink đầy đủ, Dashboard live từ May. Tháng 10 có 11.143 lượt cài đặt từ Web. |
| Objective 4: Hạ tầng & Bảo mật ổn định | Nền tảng | AWS sang FPT Cloud: 36/36 FE, 11/11 BE, 3/3 DB không downtime; đóng cổng public DB qua BFF; hoàn tất Pentest API cùng ITC Security; vá 45 CVE; tích hợp BotID chống spam form. |

### 3.2. Tiếp cận: Traffic và AI Search

**Tổng quan lưu lượng Web, Jan-Oct/2026**

Web đạt 32,97M PV trong 10 tháng và lũy kế **36,91M PV** trong năm 2026 (gồm **29,09M Non-Paid** chiếm 78,8%, trong đó Organic 18,20M chiếm 62,6% Non-Paid; và **7,82M Paid**). Tỷ trọng Non-Paid tăng dần khi Paid được tối ưu: 77-80% trong Q1-Q3, 86,9% trong tháng 10 và ước đạt ~80,5% cả năm (40,69M tổng = 32,77M Non-Paid + 7,92M Paid).

| Tháng | PageView Web (triệu) |
| :--- | :---: |
| May/2026 | 3,27 |
| Jun/2026 | 3,41 |
| Jul/2026 | 3,17 |
| Aug/2026 | 3,47 |
| Sep/2026 | 3,95 |
| Oct/2026 | 3,60 |
| Nov/2026 (MTD `1-24/11`) | 3,94 |

- Tháng 10: 3,60M PV, giảm 8,9% so với tháng 9 sau khi cắt 723.612 PV Paid kém hiệu quả. Non-Paid đạt 3,13M (+13,5%): Organic Search 1,72M (+5,7%), Direct 0,93M (+23,3%), Referral và nguồn khác 0,48M (+27,9%), AI 18.547 PV (+36,4%).
- Lưu lượng từ AI (kênh AI Assistant/Referrals trên GA4): 70.758 PV từ Jan đến Oct và lũy kế **93.652 PV** (`1/1-24/11`), mức trung bình ngày tăng **+177%** từ May đến Nov. Tháng 11 dự kiến đạt 32,4 nghìn PV (28,8 nghìn thực tế `1-24/11`). ChatGPT chiếm **96,8%** (Oct-Nov; Gemini 2,3%, Perplexity 1,0%). Chất lượng chuyển đổi vượt trội: tỷ lệ **Click-to-App đạt 5,24%/phiên** (Oct-08/11), ngang bằng Direct (5,52%) và cao hơn hẳn Organic (2,96%).
- Hub lớn nhất tháng 10 là Cinema (1,13M PV, khoảng 31% tổng), tiếp theo là Financial Hub (273.705 PV, +9,6% MoM).

**Đọc theo hành trình:** bước Tiếp cận vẫn rộng (Cinema 122M Impression Google Search trong 10 tháng), nhưng Organic tăng chậm và AI trả lời thay cho trang kiến thức chung. Lưu lượng chỉ còn giá trị khi dẫn được sang bước Kiểm tra.

### 3.3. Kiểm tra: Utility

**Financial Hub.** Dự án chiến lược cốt lõi, gồm bộ công cụ tài chính tương tác.

- Tháng 10: 273.705 PV (+9,6% MoM, đạt 109,5% mục tiêu tháng 250.000 PV; nếu theo bảng Excel 450.000 PV thì đạt 60,8%). Trung Tâm Tài Chính và Tiện ích Tỷ giá 43.495 PV (+442,0%), Ví Trả Sau 58.268 PV (+38,2%), bù mức giảm 47.814 PV của Vay Nhanh (-43,5%).
- **Hiệu suất công cụ (tháng 10):** Ước tính khoản vay CTR 43,8%, Tra cứu CIC 38,6%, Tính lương Gross-Net 33,7%. Bảng tĩnh (giá vàng, tỷ giá, lãi suất) đạt 0% CTR. Ba công cụ trên chiếm 87,4% lượt tương tác công cụ của Hub (7.100 trên 8.120 lượt).
- **Utility đã triển khai:** Tính lương Gross-Net, Tỷ giá, Giá vàng (từ Sep), Chứng chỉ quỹ, Ước tính khoản vay, Tra cứu điểm CIC, Trả góp Ví Trả Sau, Lãi tiết kiệm, Chuyển đổi ngoại tệ, BHXH và lương hưu. Đang triển khai: Phân bổ lương 50/30/20, Tính thuế TNCN và Thuế Hộ Kinh Doanh, gamification Điểm Tín Dụng CIC (tháng 11).
- **Điểm yếu:** Tiết kiệm (1,5K PV) và Chứng chỉ quỹ (458 PV) còn lưu lượng tự nhiên thấp; bước Kiểm tra cho nhóm Tích lũy chưa đủ công cụ.
- **Tín hiệu phục hồi Nov (sau tái cấu trúc PLG từ Aug):** PVs Non-Paid `1-19/11` đạt **294,5 nghìn**, tăng **+105%** so với cùng kỳ Oct (143,4 nghìn). Về mức độ phủ tìm kiếm (`1-20/11`), Financial đạt **4,36M Impression** trên Google Search (21,3% tổng momo.vn) và **5,77M Impression** trên AI Overview (`18/5-20/11`, chiếm 25,7% toàn Website). Tỷ lệ Click-to-App theo user (Nov/2026) đạt **80,4%** ở Điểm Tín Dụng, **65,0%** ở Vay Nhanh, **29,0%** ở Ví Trả Sau và **5,4%** ở Trung Tâm Tài Chính.
- **Khoảng cách mục tiêu:** Đạt 1M PV mỗi tháng vào cuối 2026 cần tăng khoảng 3,7 lần so với Oct; năm 2027 tập trung chuẩn hóa UX Framework và Microjourney cho từng công cụ tài chính.

**Vehicle Hub.** Phạt Nguội là Pioneer Project đã xác nhận trong H1/2026, làm nền để khởi động Vehicle Hub cùng VTTI và Insurtech. Thị trường 23,2 triệu lượt tìm kiếm mỗi tháng (Giá xăng 10,52 triệu, Phạt Nguội 6,58 triệu, ETC 1,31 triệu, Trạm sạc EV 1,24 triệu).

| Tháng | Impression (Google Search) | Tổng | Phạt Nguội | Bảo hiểm ô tô | Bảo hiểm xe máy | Tiện ích giao thông |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| May/2026 | 629.463 | 308.552 | 295.186 | 11.885 | 1.481 | - |
| Jun/2026 | 692.775 | 610.152 | 597.471 | 11.112 | 1.569 | - |
| Jul/2026 | 851.569 | 170.572 | 155.070 | 12.525 | 2.977 | - |
| Aug/2026 | 1.002.150 | 230.333 | 213.946 | 13.105 | 3.277 | 5 |
| Sep/2026 | 1.571.740 | 63.677 | 39.452 | 19.013 | 2.552 | 2.660 |
| Oct/2026 | 1.973.851 | 72.954 | 24.195 | 25.502 | 2.832 | 20.425 |

- Jun cao nhất nhờ SEM. Sep giảm do API Phạt Nguội gián đoạn 01/09-20/09. Oct Phạt Nguội cần SEO On-Page và liên kết nội bộ để phục hồi. Phạt Nguội đạt CTR 24,3% và 660 trích dẫn từ AI trong 28 ngày đầu; nửa đầu Nov (`1-15/11`) phục hồi mạnh đạt **88.160 PVs** với tỷ lệ mở App **69,5%** (tương đương run rate ~176 nghìn PVs/tháng).
- **Đọc theo hành trình:** người tra Phạt Nguội là chủ xe, nhóm có nhu cầu bảo hiểm xe. Năm 2026 hai cụm này vẫn chạy tách nhau; lưu lượng bảo hiểm ô tô tăng đều (11.885 lên 25.502 PV) nhưng chưa có lời mời nối từ trang tra cứu sang báo giá.

### 3.4. Hành động: giao dịch, Install và Conversion

**Cinema Hub.** Baseline lưu lượng lớn nhất, và là dự án có vấn đề chuyển đổi cần xử lý sớm nhất.

| Tháng | Impression (Google Search) | PV Cinema Hub | Vé | Giao dịch | GMV (tỷ đ) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Jan/2026 | 10.988.973 | 581.349 | 12.643 | 5.889 | 1,21 |
| Feb/2026 (Tết) | 14.875.825 | 1.044.429 | 28.379 | 12.432 | 2,55 |
| Mar/2026 | 11.505.959 | 759.142 | 20.600 | 9.881 | 2,03 |
| Apr/2026 | 11.164.473 | 851.919 | 18.730 | 8.221 | 1,69 |
| May/2026 | 12.779.934 | 994.719 | 12.561 | 5.777 | 1,18 |
| Jun/2026 | 12.659.436 | 859.183 | 19.444 | 9.055 | 1,86 |
| Jul/2026 | 13.009.013 | 822.859 | 5.211 | 2.425 | 0,50 |
| Aug/2026 | 12.784.452 | 832.460 | 8.754 | 4.016 | 0,82 |
| Sep/2026 | 11.288.422 | 1.220.075 | 20.983 | 9.807 | 2,01 |
| Oct/2026 | 10.951.659 | 1.132.721 | 26.789 | 12.547 | 2,57 |
| **Lũy kế 10 tháng (cộng từng tháng)** | **122.008.146** | **9.098.856** | **174.094** | **80.050** | **16,01 (AOV 200k) / 16,41 (thực tế)** |

- **Thống nhất số liệu giữa Slide và Tài liệu:** Tổng cộng từng tháng cho kết quả **174.094 vé** và **80.050 giao dịch** (lưu ý: truy vấn Dashboard theo dải ngày từng báo hụt đúng phần Jul ra 168.884 vé / 77.625 giao dịch / 15,91 tỷ đ, đã kiểm tra bổ sung). Trên Slide (8, 13, 14, 20) dùng mức AOV quy chuẩn thận trọng là **200.000 đ/giao dịch**, cho GMV chuẩn là **16,01 tỷ đ** (`80.050 x 200.000 đ`); giá trị thực tế ghi nhận trên đối soát tháng là **16,41 tỷ đ** (AOV thực tế `~205.000 đ`). Tháng 11 (Nov/2026) ghi nhận thêm 1,01M PVs (MTD `1-24/11`) (mục tiêu tháng 1,29M; tháng 12 mục tiêu 1,50M).
- Tỷ lệ quy đổi chuẩn dùng cho kế hoạch 2027: **8,8 giao dịch trên 1.000 PV** (tỷ lệ PV sang giao dịch 0,88%), AOV quy chuẩn **200.000 đ/giao dịch** (~2,17 vé/giao dịch).
- Sep đạt 1.220.075 PV, cao hơn mục tiêu 1,12M khoảng 9%.
- **Đọc theo hành trình:** người xem lịch chiếu đã có ý định cao nhất, nhưng khi chuyển sang App để thanh toán thì mất suất chiếu và ghế đã chọn, phải làm lại từ đầu, và hơn 90% bỏ dở. Đây là điểm rơi có giá trị lớn nhất của toàn Web.

**InsurTech (bảo hiểm), 01/01-12/11/2026.** Web mang về 136.819 user bảo hiểm, tăng 32% so với cả năm 2025. 44-51% người mua bảo hiểm trên Web chưa có ví MoMo.

| Sản phẩm | Traffic Web | So với 2025 | Kết quả từ Web | Đầu tư SEO + SEM |
| :--- | :---: | :---: | :---: | :---: |
| BH thân vỏ (VCX) | 162.304 | +46% | 2.118 leads, 71 đơn (khoảng 462 triệu đ GMV) | 1,05 tỷ đ |
| BH xe máy (XMBB) | 90.522 | -52% | 1.750 người mua (289 triệu đ GMV, -11% YoY); 1.948 đơn về App | 350 triệu đ |
| BHYT | 196.198 | Gấp 4,4 lần | 2.643 người mua, **2,67 tỷ đ GMV (+65% YoY)**, 86% chốt trên Web | 150 triệu đ |

- VCX: lead sang đơn 3,3%, thấp hơn mục tiêu 7-10%.
- XMBB: traffic năm nay bằng 48% cả năm 2025 dù 10/10 từ khóa mục tiêu trong top 10. Chưa xác định nguyên nhân.
- BHYT: chi phí SEO và SEM khoảng 57.000 đ mỗi người mua từ Web, thấp nhất trong ba sản phẩm.
- **Đọc theo hành trình:** BHYT chứng minh khi bước Hành động hoàn tất ngay trên Web thì chuyển đổi cao. Nhưng sau khi mua, chưa có bước tiếp theo đưa nhóm 44-51% chưa có ví vào App.

**Sản phẩm khác đóng góp GMV trên Web, Jan-Oct/2026**

| Sản phẩm | Chỉ số đến tháng 10 | GMV | Ghi chú |
| :--- | :---: | :---: | :--- |
| Vé xe | 3.787 MAU giao dịch | 1,51 tỷ đ (ước tính) | Tính theo 3.787 MAU x AOV 400.000 đ |
| eSIM du lịch | 824 giao dịch | 160,4 triệu đ | Tỷ lệ chuyển đổi 3,18%; không có chi phí quảng cáo |

**New Users: phễu cài đặt và đăng ký từ Web**

Lũy kế từ Jul đến `24/11/2026`: **44.684 lượt cài đặt (Install)** (Jul: 5.239; Aug: 10.041; Sep: 10.501; Oct: 11.143; Nov MTD `1-24/11`: 7.760) → **14.735 đăng ký (33,0%; Oct đạt 35,0%)** → **8.934 liên kết ngân hàng (60,6% trên đăng ký; 20,0% trên Install)** → **5.093 MAU (57,0% trên LKNH; 11,4% trên Install)**. Nov MTD ghi nhận đăng ký 30,3%, liên kết ngân hàng 63,9% và MAU 11,8% trên Install, so với kênh Media trả phí 11,0% (kỳ của số Media chưa được xác nhận, cần verify). Số đăng ký Nov trong file AppsFlyer đến `24/11` trùng với file đến `22/11`, nên tỷ lệ đăng ký Nov có thể chưa đủ.

- Banner Chào MoMo toàn Web mang về 8.517 lượt, chiếm 76% cài đặt tháng 10. Cinema Hub đóng góp 1.931 lượt (17%), tỷ lệ đăng ký sang liên kết ngân hàng 25,1%. Tăng trưởng cài đặt phụ thuộc lớn vào một cơ chế.
- Phễu tháng 10: cài đặt sang đăng ký 3.902 (35,0%), bước rớt lớn nhất; đăng ký sang liên kết ngân hàng 2.389 (61,2%), cao nhất từ đầu năm; liên kết ngân hàng sang MAU 1.284 (khoảng 54%). Tổng từ cài đặt đến MAU 11,5%.
- iOS chiếm 51% lượt cài đặt nhưng 57% người liên kết ngân hàng và 59% MAU tháng 10.
- **Đọc theo hành trình:** người cài từ banner chưa trải qua bước Kiểm tra nào, nên vào App không mang theo lý do để đăng ký. Người đến từ công cụ đã có việc cần làm tiếp; đây là nhóm cần đo riêng và ưu tiên.

### 3.5. Nền tảng: MoSpark và hạ tầng dùng chung

**MoSpark (Objective 2).** Vận hành từ Q2/2026 với Landing Page Builder, GenAI Content Pipeline, PLG Project Engine, Ads Manager, Chatbot và Knowledge Base.

- Landing Page Builder rút thời gian từ 1-2 tuần xuống 1-2 ngày, Cell Team tự xuất bản không cần Dev. Đang thử với GMC, BMC, MDS.
- GenAI Content Pipeline tự động khoảng 80% quy trình nội dung SEO/GEO, rút từ nhiều ngày xuống vài giờ.
- 16 Cell Teams được hỗ trợ, 6 tự vận hành. MoSpark cũng phục vụ momo.career và L&D.
- BMC phụ trách Brand Guideline và duyệt Creative/Legal; Web Platform cung cấp MoSpark và hạ tầng.

**Full Funnel Tracking (Objective 3).** GA4 và GTM vào BigQuery; GSC vào BigQuery theo URL; 100% liên kết chuẩn hóa OneLink; Identity Platform (Edge Cookie) nối hành vi từ Web sang App; Dashboard Web Performance live từ May/2026. Từ May Web Platform có baseline theo dõi toàn hành trình từ điểm chạm đầu tiên đến hành động trong App, làm căn cứ đặt mục tiêu theo tuần, tháng và tìm điểm nghẽn.

**Hạ tầng ổn định (Objective 4).**

- AWS sang FPT Cloud hoàn tất 100%: 36/36 Frontend, 11/11 Backend, 3/3 Database, 137 endpoint, không rollback, không downtime (21-22/07/2026).
- Mobase V2 là Design System chuẩn thương hiệu, Single Source of Truth cho Web Product; đang mở rộng sang AI-Legible Design System.
- **Bảo mật hạ tầng & ứng dụng (Security 2026):** Quản lý 69 dự án GitLab theo chuẩn ITC; đóng toàn bộ cổng public cơ sở dữ liệu Supabase thông qua tầng trung gian **Backend-for-Frontend (BFF)** xác thực JWT (loại bỏ truy xuất DB trực tiếp từ trình duyệt); hoàn tất đánh giá an toàn thông tin **Pentest API cùng ITC Security Team** trước khi đưa lên Production; rà soát và vá dứt điểm **45 mã lỗ hổng bảo mật (CVE)** trên các thư viện dùng chung (`MoMo.CommonLib`) và hoàn thiện bản vá Clickjacking; tích hợp **BotID** chống tấn công spam và thu thập dữ liệu trái phép trên các biểu mẫu Lead Form; thiết lập sao lưu dữ liệu tự động hàng ngày cho cụm `momovn` và `mospark` trên FPT Cloud.
- Technical SEO: xử lý khoảng 8.600 URL giá trị thấp, tối ưu Crawl Budget, bổ sung sameAs Schema cho Organization.

### 3.6. Đánh giá 8 sáng kiến

| Initiative | Nhóm | Bước hành trình hỗ trợ | Kết quả 2026 | Yếu tố thành công / thất bại | Khuyến nghị |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Cloud Migration (AWS sang FPT Cloud) | Productivity | Nền tảng | Go-Live 21-22/07; 36/36 FE, 11/11 BE, 3/3 DB; 137 endpoint; 0 rollback | Kế hoạch cutover chi tiết, Smoke Test trước và sau, cutover ban đêm | Chuyển sang vận hành ổn định |
| MoSpark / Admin Panel | Transformation | Tiếp cận, Kiểm tra | Live trên Production; GenAI sinh nội dung theo chuẩn brand | Next.js, Supabase, Refine; nhu cầu tự tạo Landing Page rõ | Scale thành CMS duy nhất cho nội dung, quảng cáo, analytics |
| Identity Platform | Transformation | Hành động, Quay lại | Hoàn thiện spec; core định danh đa nền tảng lên Production | Phụ thuộc phối hợp User Growth và ITC | Tiếp tục: là nền cho tín hiệu Web sang App |
| Umami Internal Tracking | Productivity | Đo lường | Chạy song song GA4; dashboard theo Project | Chủ động dữ liệu, real-time; cần vận hành hạ tầng | Mở rộng cho toàn bộ Mini Web |
| Utility Tools và Boilerplate | Productivity | Kiểm tra | Payment Component, Lead Form, JSON Form Builder, UI Kit cho hàng chục Mini Web | Đồng bộ Tech Stack ITC; JTBD trước khi xây | Mở rộng thư viện theo nhu cầu Cell Team |
| Hub mới (Phạt Nguội, Merchant, Cinema, Financial, Vehicle, Student) | Incubator | Tiếp cận, Kiểm tra | Ra mắt nhiều Mini Web ngách | Bám nhu cầu tìm kiếm của người chưa dùng MoMo | Scale Hub có lưu lượng tốt; thử tiếp phần còn lại |
| Chatbot AI và RAG Knowledge Base | Incubator | Kiểm tra | Triển khai giới hạn trên Production | Chất lượng dữ liệu từ nội dung Web | Thử tiếp, đánh giá mở rộng 2027 |
| Vận hành Mini Web hiện hữu (Vé máy bay, Vay nhanh, BHOT, Bus, Travel, Sim, CVS, Soundbox...) | Performance | Hành động | 100% Smoke Test đạt trên Production | Bảo trì định kỳ, SLA rõ | Tiếp tục hỗ trợ theo chuẩn ITC |

### 3.7. Điểm rơi 2026 và nguyên tắc 2027

| Bước | Điểm rơi | Số liệu | Nguyên nhân |
| :--- | :--- | :--- | :--- |
| Tiếp cận | Organic tăng chậm | +5,7% MoM (Oct), thấp hơn Non-Paid tổng (+13,5%) | AI Search trả lời thay nội dung kiến thức chung |
| Tiếp cận → Kiểm tra | Bảng tĩnh không dẫn sang đâu | Giá vàng, tỷ giá, lãi suất: 0% CTR | Trang chỉ hiển thị số, không có công cụ hay bước tiếp theo |
| Kiểm tra | Tích lũy thiếu công cụ | Tiết kiệm 1,5K PV, CCQ 458 PV | Chưa có công cụ tính toán cho nhóm tích lũy |
| Kiểm tra → Hành động | Công cụ tách khỏi sản phẩm liên quan | Phạt Nguội và bảo hiểm xe chạy riêng | Chưa thiết kế bước tiếp theo giữa các cụm |
| Hành động | Bỏ dở ở bước mua vé | Trên 90% (Cinema) | Chuyển sang App để thanh toán làm mất ngữ cảnh đã chọn trên Web |
| Hành động | Lead không thành đơn | VCX 3,3% so với mục tiêu 7-10% | Luồng báo giá chưa tối ưu |
| Hành động → Quay lại | Cài đặt không đăng ký | 35,0% (65% rớt) | 76% cài đặt từ banner, user chưa có việc cần làm tiếp trong App |

**Nguyên tắc 2027**

- **Utility trước, nội dung sau, mỗi Utility có một Microjourney.** Utility thắng nội dung tĩnh vì dẫn user sang việc kế tiếp; bảng giá vàng, tỷ giá, lãi suất không có bước tiếp theo nên CTR là 0%. Mỗi cụm ưu tiên Utility, và mỗi Utility có một Offer gắn với ngữ cảnh của user.
- **SEO và GEO/AEO đầu tư song song.** Organic tăng chậm hơn Non-Paid tổng khi AI trả lời trực tiếp, còn AI Traffic nhỏ nhưng chất lượng cao. Phạt Nguội là playbook: 28 ngày đúng chiến lược từ khóa tạo Organic bền vững và 660 trích dẫn AI. llms.txt, Schema và Topical Authority là hạng mục xuyên suốt.
- **KPI đi theo vai trò.** Web Platform được đo bằng Traffic, Install và Shared-KPI với BU, thay vì số tính năng đã giao.

---

## 4. MARKET

- **Tìm kiếm chuyển từ từ khóa sang khám phá bằng AI theo ý định.** Nội dung tĩnh, thiếu chiều sâu mất lượt nhấp; công cụ tương tác và dữ liệu thời gian thực được Google lẫn AI engine ưu tiên trích dẫn.
- **Quy mô thị trường (một nguồn):** 214,4 triệu lượt/tháng ở 5 nhóm ngành (Google Keyword Planner, Semrush); Tài chính 122,97 triệu.

**Độ phủ của MoMo theo nhóm (tập từ khóa theo dõi, Impression Google Search Oct)**

| Nhóm | Lượt tìm kiếm mỗi tháng | Impression MoMo (Oct) | SoV (Impression / lượt tìm kiếm) |
| :--- | :---: | :---: | :---: |
| Giá vàng và đầu tư | 65,8 triệu | 20.053 | 0,03% |
| Tỷ giá và ngoại tệ | 11 triệu | 791.963 | 7,2% |
| Vay tiêu dùng và tín dụng | Hơn 3 triệu | 1.087.671 | Tối đa 36% |
| Giao thông và phương tiện | 23,2 triệu | 1.973.851 | 8,5% |
| Điện ảnh và giải trí | Hơn 9 triệu | 10.951.659 | Trên 100% |

- Lượt tìm kiếm theo tập từ khóa đang theo dõi, khác phạm vi quy mô thị trường ở trên; Impression có thể vượt 100% vì một lượt tìm kiếm hiển thị nhiều trang.
- **Ngân sách 2027 tập trung vào CIC, vay và tích lũy (khoảng 9,4 triệu lượt/tháng)** thay vì giá vàng và tỷ giá, vì các nhóm này có bước tiếp theo dẫn thẳng vào sản phẩm tạo doanh thu. Giá vàng và tỷ giá là lựa chọn có chủ đích: cụm Tỷ giá đang triển khai theo mô hình pSEO từ 2026 và nằm trong phần tăng trưởng không ngân sách.

**Xu hướng 1-2 năm: tìm kiếm theo mục tiêu và hành trình**

- Google AI Mode tách một câu hỏi thành nhiều câu hỏi phụ, mỗi câu một ý định riêng (query fan-out, theo Aleyda Solis).
- Intent graph (mục tiêu gốc, mục tiêu phụ, điều kiện) mới là hướng nghiên cứu, chưa phải hệ thống chính thức của Google, chưa dùng làm căn cứ kế hoạch.
- Theo SEOClarity, nguồn AI trích dẫn có thể không trùng kết quả đứng đầu. Web cần phủ nhiều câu hỏi phụ của một chủ đề, cùng logic với việc thiết kế hành trình nhiều bước thay vì một trang đơn lẻ.
- Thử nghiệm 2027: chọn một cụm (CIC), đo tỷ lệ được trích dẫn trên các câu hỏi phụ, tách khỏi thứ hạng; báo cáo go/no-go cuối mỗi quý.

### 4.1. Benchmark fintech toàn cầu

- **pSEO (Wise):** phần lớn lưu lượng organic đến từ trang sinh từ template, mỗi trang trả lời một ý định giao dịch. Bài học: xây template library trên MoSpark thay vì làm từng trang lẻ. Cụm Tỷ giá (Sep-Oct/2026) là trường hợp đầu tiên trong nội bộ.
- **SEO là bề mặt sản phẩm (Revolut):** trang traffic cao nhất là utility pages (converter, giá crypto, trang quốc gia), không phải blog. Mọi tính năng sản phẩm đều có URL index được.
- **Neobank so với ngân hàng truyền thống:** help center làm tài sản SEO, pSEO trang phí và sản phẩm, web index được dù app-first, CWV dưới 2 giây, review schema, nội dung pháp lý làm lợi thế tin cậy. MoMo đã có CWV gates và E-E-A-T; còn thiếu review schema và trang minh bạch phí, giấy phép.
- **GEO cho fintech (YMYL):** AI engine ưu tiên nguồn có giấy phép, biểu phí công khai, kênh khiếu nại, tác giả có tên. MoMo đã có quy trình GEO qua Phạt Nguội nhưng chưa có trang tổng hợp giấy phép và pháp lý.

---

## 5. DIRECTION 2027

### 5.1. Introduce

Năm 2027, Web là kênh Nurture user chưa có App từ nhu cầu tìm kiếm. Web thu hút Non-Paid Traffic từ Search Engine và AI Agent, thiết kế Microjourney trên Utility để điều hướng user sang đúng Service trong App, giữ đúng ngữ cảnh từ Out-App đến In-App. Hướng này đi qua bốn trụ cột: SEO / GEO / AEO, MoSpark 2.0, Security và Shared Product.

### 5.2. Objectives

| Cấp | Chỉ số | Baseline 2026 | Base case 2027 | Best case 2027 |
| :--- | :--- | :--- | :--- | :--- |
| **North Star Metric** | PageView Non-Paid | 32,77M (ước cả năm) | 38,9-41,1M | 55,57M |
| **Success Metric** (cùng BU) | GMV, DAU, MAU, MEU | Cinema 16,01 tỷ đ GMV (Jan-Oct); Bảo hiểm 2,67 tỷ đ GMV (BHYT) | BU và FinanceBP xác nhận | BU và FinanceBP xác nhận |
| **Success Metric** | W2A CTR | 3,36% (Oct) | Không thấp hơn 3,36% | 4,0-4,5% |
| **KPI** | Install mỗi tháng | 11.143 (Oct) | 30.000 | 30.000 |

### 5.3. Pillar Objectives

#### Pillar 1: SEO / GEO / AEO
*Objective:* tăng PageView Non-Paid bằng Utility và AI Search.

1. **GenAI Content Pipeline và AI Quality Gate.** Nâng pipeline từ tự động khoảng 80% (vài giờ) lên tự phục vụ trong vài phút cho toàn bộ Cell Teams. AI Quality Gate chấm điểm độ chính xác thông tin, E-E-A-T và chống trùng lặp trước khi xuất bản.
2. **Product-Led Growth (PLG).** Nâng số Hub chiến lược từ 3 lên 5 trở lên, tập trung vào bốn dự án: Phạt Nguội (2,1-2,5M PVs), Cinema Hub (12,6-14,0M PVs), CIC và Tín dụng (2,2-2,5M PVs), Tích lũy và Đầu tư (1,0-1,5M PVs). Bảo hiểm giữ luồng mua BHYT và tối ưu báo giá VCX, chờ định hướng chung của công ty. Mở rộng sang Vé số, Chứng khoán và Chứng chỉ quỹ sau khi BU xác nhận khả thi về sản phẩm và pháp lý.
3. **Utility-Led SEO và GEO/AEO.** Xây bộ mẫu pSEO (calculator, comparison, tra cứu theo ngân hàng, quận, phương tiện) trên MoSpark, thay các bảng tĩnh có CTR 0% bằng Utility. Chuẩn hóa Schema.org, llms.txt và trang minh bạch pháp lý YMYL để AI Agent ưu tiên trích dẫn momo.vn. Mỗi hạng mục pilot một quý với KPI rõ: đạt ngưỡng thì mở rộng, không đạt thì dừng.

#### Pillar 2: MoSpark 2.0
*Objective:* Cell Teams tự dựng Landing Page cho Utility và chiến dịch trong 1-2 ngày; giảm tỷ trọng Install từ banner toàn trang từ 76% xuống dưới 50%; W2A CTR từ 4,5% trên các trang Utility.

1. **Landing Page Builder (Scale và Integrate).** Mở rộng kho template cho Utility và chiến dịch, AI-assisted generation, A/B Testing ngay trên Builder, Variant fan-out và Multi-tenant để nhiều Cell Teams cùng dùng. Mỗi trang gắn một KPI rõ ràng. Success metrics: Time-to-launch dưới 1-2 ngày, Self-serve rate, tỷ lệ trang gắn KPI.
2. **Ads Manager.** Quản lý Offer ngay trong MoSpark: mỗi luồng tối đa một Offer, đặt sau khi user có kết quả, luôn bỏ qua được, giữ đúng ngữ cảnh từ Out-App đến In-App qua OneLink. Tách chiến dịch theo ba trạng thái: chưa cài App, đã cài chưa đăng ký, đã đăng ký chưa liên kết ngân hàng.
3. **Utility Tracking và Chatbot.** Chuẩn hóa tham số cho 100% liên kết OneLink vào BigQuery, mở rộng Umami cho toàn bộ Mini Web và đối soát với GA4 hằng tháng. Chatbot và RAG Knowledge Base mở rộng trợ lý tư vấn Service trên Web.
4. **Identify (SSO): Gamification và New User Nurturing.** Gamification kế thừa chiến dịch Game Một Mùa Quýt (7.097 người chơi, 3.454 click OneLink, 1.230 người cài hoặc mở App), triển khai Gamification Điểm Tín Dụng CIC sau khi Pháp lý xác nhận khung giấy phép. New User Nurturing dựa trên Identity Platform đã chạy Production; Q1/2027 thử nghiệm đăng nhập nhẹ (Soft SSO) trên hai Utility (CIC, Ước tính khoản vay) và đo tỷ lệ đồng ý trước khi quyết định đầu tư lớn.

#### Pillar 3: Security
*Objective:* đóng cổng truy cập public vào dữ liệu và không còn lỗ hổng mức CRITICAL được xác nhận độc lập, đạt chuẩn ITC Security trước mỗi lần Go-live.

1. **Truy vấn dữ liệu qua BFF.** Toàn bộ Web chuyển sang lớp BFF, đóng cổng public Supabase sau khi ITC Security Team duyệt Pentest API.
2. **Vá lỗ hổng còn mở.** Kế hoạch vá 68 lỗ hổng của MoMo API theo ba đợt, ưu tiên các route public; quét lại độc lập để xác nhận kết quả, vì số liệu hiện tại dựa trên đọc mã nguồn.
3. **Quản lý khóa bí mật.** Chuyển các khóa bí mật khỏi mã nguồn sang K8s Secret kèm đổi khóa.
4. **Security duyệt trước Go-live.** Mọi kết nối và Utility mới có Security duyệt trước khi mở, rút ra từ sự cố Pentest ngày 27/10.
5. **Zero-PII.** Utility và Offer không thu thập thông tin định danh cá nhân; BotID chặn bot spam trên Lead Form.

#### Pillar 4: Shared Product
*Objective:* nâng số Cell Teams được hỗ trợ từ 16 lên 20, số Cell Teams tự xuất bản trên MoSpark từ 6 lên 15 trở lên, duy trì uptime từ 99,9%.

1. **Tự phục vụ cho các mảng nội bộ.** HR tự vận hành MoMo Talent (momo.career); L&D tự xuất bản trên MoSpark kèm AI Quality Gate; BMC quản lý Brand Guideline và tự xuất bản Webview In/Out App (đã thử Landing Page Builder với GMC, BMC, MDS); CVS (News) duy trì 100% Smoke Test trên Production theo chuẩn ITC.
2. **Bốn thành phần dùng chung.** Payment Component, Lead Form (gắn BotID), JSON Form Builder và MoBase UI Kit, để mọi đội dùng chung hạ tầng và thừa hưởng Domain Authority của momo.vn.

## 6. INVESTMENT 2027

**Ngân sách:** 1.995.800.000 đ, khoảng 166,3 triệu đ mỗi tháng, gồm 1,95 tỷ đ cho 3 dự án và 45,8 triệu đ bản quyền công cụ. Không đề xuất ngân sách Paid. Ngân sách Cinema và Financial có phần đồng tài trợ từ BU, tỷ lệ thống nhất với từng BU trước khi giải ngân.

| Dự án | Vai trò trong hành trình | Ngân sách | PV 2026 (Jan-Oct) | PV 2027 | PV tăng thêm | Thứ hạng mục tiêu | Chuyển đổi tham chiếu | Chi phí đơn vị |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| **Cinema Hub** | Nguồn lưu lượng và Install lớn nhất; dịch vụ theo mùa, đã có GMV | 620 triệu đ | 9,10M | 12,6 - 14,0M | 3,5 - 4,9M | Top 1-3 cụm mua vé, rạp, phim mới | **31 - 43 nghìn giao dịch; 6,2 - 8,6 tỷ đ GMV** (6,3-8,8B ở AOV 205k) | 130 - 180 đ/PV; 1 đ chi phí tạo 10,0 - 13,9 đ GMV |
| **Financial - CIC & Tín dụng** | Bước kiểm tra, dẫn sang Ví Trả Sau và Vay Nhanh | 480 triệu đ | 0,42M | 2,2 - 2,5M | 1,8 - 2,1M | Top 3-5 cụm CIC, nợ xấu, điểm tín dụng | 52 - 61 nghìn lượt click App (CIC, Ví Trả Sau, Vay Nhanh) | 230 - 270 đ/PV; 7.900 - 9.200 đ/lượt click App |
| **Financial - Tích lũy & Đầu tư** | Dẫn sang Túi Thần Tài, rồi đến Tiết kiệm, CCQ | 850 triệu đ | 0,21M | 1,0 - 1,5M | 0,8 - 1,3M | Top 3-5 cụm lãi suất, tiết kiệm, CCQ, tích sản | 32 - 52 nghìn lượt click App (Túi Thần Tài, Tiết kiệm, CCQ) | 650 - 1.060 đ/PV; 16.300 - 26.600 đ/lượt click App |
| **Bản quyền công cụ** | Vận hành | 45,8 triệu đ | | | | | Figma Pro 9,8 triệu đ (2 users); Semrush Pro 36 triệu đ (1 user) | Vận hành |
| **Tổng** | | **1.995,8 triệu đ (~1,996 tỷ đ)** | **9,73M** | **15,8 - 18,0M** | **6,1 - 8,3M** | | **6,2 - 8,6 tỷ đ GMV Cinema; 84 - 113 nghìn lượt click App Financial** | **240 - 330 đ/PV** |

**Chi phí đơn vị dùng để đánh giá:** đ/giao dịch với Cinema (khoảng 14.800-20.700 đ/giao dịch tăng thêm) và đ/lượt click App với Financial. Chi phí đ/PV chỉ là chỉ số đầu vào, dùng để so với SEM.

Chuyển đổi cuối phễu khác nhau theo use case: Cinema đo bằng giao dịch và GMV; Financial đo bằng lượt click App, MAU/MEU và chỉ số sản phẩm do BU định nghĩa. Đây là chỉ số chất lượng traffic, đồng chịu trách nhiệm với BU.

**Vì sao ba dự án này:** mỗi dự án điều hướng user vào một phễu đã được chứng minh trong App. Cinema mang lưu lượng lớn nhất và đóng góp 17% Install từ Web (Oct). CIC dẫn vào Ví Trả Sau, phễu lớn nhất sang Vay Nhanh và trả góp. Tích lũy dẫn vào Túi Thần Tài, cửa vào của các sản phẩm đầu tư. Web không cần tự xây phễu sinh lời; Web đưa người chưa có App vào đúng đầu phễu.

### 6.1. Cơ sở tính toán

- **Cinema:** baseline Jan-Oct là `9.098.856 PV`, `174.094 vé`, `80.050 giao dịch`, GMV quy chuẩn AOV 200.000 đ là `16,01 tỷ đ` (thực tế đối soát bảng tháng `16,41 tỷ đ`, AOV `~205.000 đ`). Tỷ lệ chuẩn tính cho 2027: **8,8 giao dịch trên 1.000 PV** và **AOV 200.000 đ/giao dịch** (~1,76 triệu đ GMV trên 1.000 PV). Không đầu tư: giữ quanh ~80 nghìn giao dịch, 16,0 tỷ đ. Có đầu tư (12,6-14,0M PV): 111-123 nghìn giao dịch, 22,2-24,6 tỷ đ GMV (phần tăng thêm: `31-43 nghìn giao dịch`, `6,2-8,6 tỷ đ`). Chưa tính phần tăng nếu rút ngắn bước thanh toán QR trong H1/2027.
- **Financial:** baseline GA4 Jan-Oct cấp trang. CIC & Tín dụng khoảng 417 nghìn PV (trang Tra cứu điểm tín dụng và nội dung tín dụng, không gồm Vay Nhanh và Ví Trả Sau). Tích lũy & Đầu tư khoảng 210 nghìn PV (tiết kiệm, chứng khoán, CCQ, quản lý chi tiêu, nội dung đầu tư). Tỷ lệ click App thực tế 2026: CIC & Tín dụng 2,9%, Tích lũy & Đầu tư 4,0%.
- **So sánh kênh:** cùng 6,1-8,3M PV (3,8-5,1M phiên ở 1,62 PV/phiên), Paid SEM tốn 7,5-10,2 tỷ đ/năm ở giá thầu thấp nhất 2.000 đ (giá thầu thực nhóm tài chính có thể 5.000-20.000 đ) và mất ngay khi dừng chi. Content 1,95 tỷ đ để lại tài sản lưu lượng nhiều năm.

**Mức tăng khi có đầu tư:**

| Chỉ số | Mức 2026 (Jan-Oct) | Tăng thêm khi có đầu tư |
| :--- | :---: | :---: |
| PV (3 dự án) | 9,7M | +63-86% |
| Giao dịch Cinema | 80,05 nghìn | +39-54% |
| GMV Cinema | 16,01 tỷ đ (16,41 tỷ đ thực tế) | +39-54% |
| Lượt click App từ Financial | khoảng 21 nghìn | +400-540% |

Kịch bản không đầu tư giả định 3 cụm giữ nguyên lưu lượng 2026. Thực tế lưu lượng dễ giảm do AI Search, nên chênh lệch thực có thể lớn hơn.

### 6.2. Giải ngân Financial hai đợt

- **Đợt 1 (Q1-Q2/2027), 540 triệu đ:** CIC & Tín dụng 240 triệu đ; Tích lũy & Đầu tư 300 triệu đ. Mục tiêu: chứng minh chuyển đổi trước khi mở rộng.
- **Đợt 2 (Q3-Q4/2027), 790 triệu đ:** chỉ giải ngân khi cuối Q2 đạt đủ 3 ngưỡng: PV đạt ít nhất 80% KPI 2 quý; tỷ lệ click App không thấp hơn 2026 (2,9% và 4,0%); Financial Services BU đã cung cấp GMV, MAU và MEU theo use case từ lượt click App.
- **Không đạt ngưỡng:** dừng đợt 2 của dự án không đạt, chuyển sang Cinema Hub hoặc hoàn lại.

### 6.3. Các phương án đã cân nhắc

- **Scale Paid SEM:** chi phí gấp 3,8-5,1 lần content cho cùng lượng truy cập; mất khi dừng chi; không xây được tài sản.
- **Dàn trải nhiều Hub nhỏ:** nguồn lực mỏng; Hub nhỏ không đủ công cụ và nội dung tối thiểu để thắng SoV, và không nối được thành hành trình.
- **Chỉ làm in-app, bỏ Web:** Web là kênh acquisition rẻ nhất có Domain Authority; in-app không chạm được người chưa biết MoMo.
- **Status quo:** Organic chỉ tăng 5,7% MoM và vẫn chịu áp lực từ AI Search; không đầu tư là chấp nhận mất share cho đối thủ và AI engine.
- **Đổ toàn bộ vào giá vàng, tỷ giá:** search volume lớn nhất nhưng chưa có bước tiếp theo dẫn vào sản phẩm doanh thu.

### 6.4. Kịch bản đạt 50% mục tiêu

- **Cinema 50%:** +1,8-2,5M PV; khoảng 15-21 nghìn giao dịch, 3,1-4,3 tỷ đ GMV.
- **Financial 50%:** khoảng 42-57 nghìn lượt click App; chi phí trên PV và trên lượt click App tăng khoảng 2 lần, vẫn thấp hơn Paid cho cùng ý định.
- **Organic mất đà (tăng từ 0% trở xuống mỗi tháng):** mục tiêu 63,49M PV không đạt; đây là rủi ro lớn nhất, ngân sách không giải quyết được, cần kế hoạch riêng.
- **Cả 3 cùng chỉ đạt 50%:** tổng chi khoảng 1,95 tỷ đ, thu về chủ yếu là tài sản nội dung, dữ liệu và GEO citation đếm được; đánh giá lại mô hình sau Q2.

---

## 7. TARGETS 2027

Mục tiêu được phân thành 2 tầng lưu lượng rõ ràng: **Base case, cam kết (38,9-41,1M PVs Non-Paid)** trên phần nguồn lực tự chủ được; và **Best case (55,57M PVs Non-Paid, tổng Web 63,49M PVs)** khi đủ kế hoạch cho phần nội dung nền và giải ngân trọn vẹn 2 đợt. Về **Install**, KPI 2027 là **30.000/tháng** (khoảng 360.000 cả năm), gấp khoảng 2,7 lần Oct/2026 (11.143).

**Khoảng trống điều hướng user.** Giữ nguyên nhịp Oct/2026 (`11.143 lượt/tháng`), cả năm 2027 chỉ đạt khoảng `134 nghìn` Install. Để đạt `30.000/tháng`, tỷ trọng cài đặt từ banner toàn trang phải giảm từ 76% xuống dưới 50%, nguồn ngoài banner tăng lên nhờ Ads Manager (Cược 2) và Deferred Deep Linking (Cược 3).

**Bảng phân bổ mục tiêu 55,57M PVs Non-Paid 2027 theo 4 dự án và phần nền:**

| Nhóm dự án / Nguồn | Mục tiêu 2027 (M PVs) | Tỷ trọng trên 55,57M | Ghi chú kiểm chứng |
| :--- | :---: | :---: | :--- |
| **Cinema Hub** | **12,6 - 14,0M** | 23 - 25% | Hub có GMV vé; BU Movies (cần xác nhận thêm phần Paid tách riêng nếu có) |
| **Phạt Nguội** | **2,1 - 2,5M** | 4% | Run rate Nov đạt ~176K PVs/tháng, tăng tới 20% |
| **CIC & Tín dụng** | **2,2 - 2,5M** | 4% | Tín dụng; BU Financial Services |
| **Financial: Tích lũy & Đầu tư** | **1,0 - 1,5M** | 2 - 3% | Túi Thần Tài, Tiết kiệm, CCQ; BU Financial Services |
| **Dự án khác & nội dung nền** | **35,1 - 37,7M** | 63 - 68% | Vehicle Hub, New User, Tỷ giá, eSIM, Cell Teams, Bảo hiểm (phép trừ phần còn lại) |
| **Tổng Non-Paid 2027 (Mở rộng)** | **55,57M** | **100%** | Tổng Web gồm Paid 7,92M (giữ như 2026 do BU quyết định) = **63,49M PVs** |

Mục tiêu PV giả định Paid giữ nguyên mức 2026 (`7,92M`, khoảng `0,66M` mỗi tháng); toàn bộ mức tăng còn lại đến từ Non-Paid. Lộ trình từng tháng cho Best case:

| Tháng | Tổng PV (triệu) | Paid (triệu) | Non-Paid (triệu) |
| :--- | :---: | :---: | :---: |
| Jan/2027 | 4,12 | 0,66 | 3,46 |
| Feb/2027 | 4,45 | 0,66 | 3,79 |
| Mar/2027 | 4,35 | 0,66 | 3,69 |
| Apr/2027 | 4,52 | 0,66 | 3,86 |
| May/2027 | 4,80 | 0,66 | 4,14 |
| Jun/2027 | 5,10 | 0,66 | 4,44 |
| Jul/2027 | 5,25 | 0,66 | 4,59 |
| Aug/2027 | 5,45 | 0,66 | 4,79 |
| Sep/2027 | 5,75 | 0,66 | 5,09 |
| Oct/2027 | 6,15 | 0,66 | 5,49 |
| Nov/2027 | 6,55 | 0,66 | 5,89 |
| Dec/2027 | 7,00 | 0,66 | 6,34 |
| **Cả năm (Mở rộng)** | **63,49** | **7,92** | **55,57** |

- **Base case, cam kết (38,9-41,1M Non-Paid + 7,92M Paid = 46,8-49,0M tổng PVs):** Tương đương `3,90-4,09M PVs/tháng`.
- So với 2026 (ước cả năm: tổng 40,69M, Paid 7,92M, Non-Paid 32,77M), Best case giúp tổng PVs tăng `+56%` (`63,49M`) và Non-Paid tăng `+22,80M (+70%)`, bình quân khoảng 5,7% mỗi tháng.
- Non-Paid đặt theo tốc độ tăng trưởng, không theo tỷ trọng, vì Paid do BU quyết định và không thuộc cam kết của Web Platform.

| Chỉ số | 2026 | Mục tiêu 2027 Cam kết | Mục tiêu 2027 Mở rộng | Ghi chú |
| :--- | :---: | :---: | :---: | :--- |
| Lượt cài đặt mới mỗi tháng (KPI) | 11.143 (Oct) | **30.000** | **30.000** | KPI 2027, khoảng 360.000 cả năm |
| Tỷ lệ cài đặt sang đăng ký | 33,0% (Jul-Nov); 35,0% (Oct) | Đo riêng từng nguồn | Cải thiện lên 40-45% | Tách nguồn banner và nguồn công cụ |
| Tỷ trọng cài đặt từ banner toàn trang | 76% (Oct); 81% (Nov MTD) | **Dưới 50%** | **Dưới 50%** | Thay dần bằng Ads Manager trong luồng |
| PV từ AI mỗi tháng | 18.547 (Oct); 28,8k (`1-24/11`) | 50.000 vào Dec | **46.000 bình quân; 100.000 vào Dec** | Kênh AI Assistant trên GA4 (~551k cả năm) |
| Lưu lượng CIC và Tích lũy | 0,63M (Jan-Oct) | 3,2 - 4,0M cả năm | 3,2 - 4,0M cả năm | Có ngân sách đầu tư riêng |
| Cell Teams được hỗ trợ | 16 (6 tự vận hành) | 20 (15+ tự vận hành) | 20 (15+ tự vận hành) | Self-serve trên MoSpark |
| Strategic Hubs đang hoạt động | 3 (Cinema, Vehicle, Financial) | 5 trở lên | 5 trở lên | Mở rộng Vé số, Chứng khoán, CCQ theo điều kiện |

**Phần tăng trưởng không ngân sách: 64-73% mức tăng Non-Paid**

Ba dự án có ngân sách đóng góp 6,1-8,3M PV. Phần còn lại, 14,5-16,7M PV Non-Paid, nằm ngoài các dự án được cấp vốn. Đây là giả định lớn nhất của toàn bộ mục tiêu.

- **Phụ trách:** Web Platform và Out-App Traffic, rà soát hằng tuần cùng hội đồng lưu lượng.
- **Cơ chế:** MoSpark self-serve (mục tiêu 15+ Cell Teams tự vận hành), seasonal content, pSEO cụm Tỷ giá, carry-over thứ hạng từ 8.600 URL đã xử lý, user quay lại (Direct) nhờ các Microjourney đã đề xuất.
- **Điều kiện kích hoạt:** nếu Q1/2027 phần không ngân sách tăng dưới 15% so với baseline, mục tiêu 63,49M PV được rà soát lại và báo Ban Giám đốc trước khi giải ngân đợt 2.

**Điều kiện từ BU:**

- Movies BU và Financial Services BU chia sẻ lịch phim, lộ trình sản phẩm và thay đổi chính sách trước 2-4 tuần.
- Financial Services BU cung cấp chỉ số trên App (GMV, MAU, MEU) và đối soát qua Dashboard dùng chung.
- Movies BU thống nhất lộ trình rút ngắn bước thanh toán (QR hoặc deep link mở App giữ suất chiếu và ghế) trong 6 tháng đầu 2027.
