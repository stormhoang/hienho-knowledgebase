# 2026 REFLECTION & 2027 DIRECTION - WEB PLATFORM

## 1. EXECUTIVE SUMMARY

**Năm 2026, Web đạt 36,91 triệu PageView (Non-Paid 29,09 triệu, 78,8%) và 44.684 lượt cài App từ Jul đến Nov. Năm 2027, Web là entry point từ out-app cho user chưa có App: Nurture nhu cầu từ Google và AI, chuyển đổi (Conversion) sang cài App và điều hướng đến các Service của MoMo theo hướng Product-Led Growth. Web đặt KPI 2027 là 55,57 triệu PageView Non-Paid và 30.000 Install mỗi tháng (khoảng 360.000 Install cả năm).**

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
- **Mở rộng GEO/AEO.** AI Overview và AI Assistant trả lời trực tiếp, Organic tăng chậm hơn Non-Paid tổng. GEO/AEO bổ sung cho SEO để giữ Traffic từ nhu cầu tìm kiếm.

**Đề xuất 2027**

| Chỉ số | Baseline 2026 | KPI 2027 |
| :--- | :--- | :--- |
| PageView Non-Paid | 32,77M (Forecast cả năm) | 55,57M (+70%) |
| Tổng PageView Web | 40,69M (Forecast cả năm) | 63,49M (+56%) |
| W2A CTR | 3,36% (Oct) | 4,0-4,5% (+19% đến +34%) |
| Install mỗi tháng | 11.143 (Oct) | 30.000 (+169%) |

---

## 2. 2026 REFLECTION

### 2.1. Năng lực nền tảng

Năm 2026, Web Platform xây năm năng lực làm nền cho 2027: MoSpark, GenAI Content, Utility-Led SEO, Tracking Full Funnel, Payment và OneLink. MoSpark là nền kỹ thuật dùng chung, bốn năng lực còn lại phục vụ nội dung, Utility, đo lường và giao dịch.

| Năng lực | Đã áp dụng trong 2026 | Tiếp nối trong 2027 |
| :--- | :--- | :--- |
| MoSpark (nền kỹ thuật dùng chung) | 16 Cell Teams, 6 tự vận hành; Landing Page 1-2 ngày (trước: 1-2 tuần); CMS live trên Production; Payment Component, Lead Form, JSON Form Builder; 100% sang FPT Cloud, không downtime; Mobase V2 | 20 Cell Teams; BMC, HR, L&D tự xuất bản; CMS duy nhất cho nội dung, quảng cáo, analytics; uptime từ 99,9% |
| GenAI Content | Tự động khoảng 80% quy trình SEO, GEO; từ nhiều ngày xuống vài giờ | Mở rộng cho Cell Teams, còn vài phút; AI Quality Gate quản trị Content Strategy trước khi xuất bản |
| Utility-Led SEO | Phạt Nguội, CIC, Ước tính khoản vay, Tính lương; CTR Utility 33,7-43,8% (Oct) | Mỗi Hub có Microjourney, nối kết quả sang bước tiếp theo |
| Tracking Full Funnel | GA4, GTM, GSC vào BigQuery; 100% OneLink chuẩn hóa; Dashboard live từ May | Identity Platform nối hành vi Web sang App; đo hoàn tất theo hành trình |
| Payment và OneLink | Payment Component; GMV Cinema 16,01 tỷ đ; BHYT 86% người mua chốt trên Web | Cinema: QR hoặc OneLink mở App đúng bước thanh toán, giữ lựa chọn |

**Bảo mật và Technical SEO**

- **Bảo mật:** truy vấn dữ liệu chuyển qua tầng BFF xác thực JWT; Pentest API cùng ITC Security Team, cổng public Supabase đóng sau khi ITC duyệt; vá 45 mã lỗ hổng (CVE) trên momo.api và các thư viện dùng chung; BotID chống spam Lead Form; sao lưu tự động hàng ngày trên FPT Cloud; 69 dự án GitLab theo chuẩn ITC.
- **Technical SEO:** xử lý khoảng 8.600 URL giá trị thấp, tối ưu Crawl Budget, bổ sung sameAs Schema cho Organization.

**Vai trò và mô hình phục vụ**

Web Platform phụ trách nền tảng công nghệ dùng chung cho Web MoMo, phối hợp ITC cung cấp hạ tầng, thư viện, công cụ và quy trình cho các Mini Web trên momo.vn của Cell Teams, BUs và Division. Giá trị tạo ra ở ba tầng:

- **Tầng MoMo:** xây Content Authority cho các Theme theo hành trình user, để Google Search và AI Chatbot (ChatGPT, Gemini, Perplexity) trích dẫn MoMo là nguồn uy tín.
- **Tầng User:** xây Utility giải quyết nhu cầu cụ thể ngay trong lúc tìm kiếm, thay cho nội dung tĩnh.
- **Tầng BUs:** Platform-as-a-Service nội bộ: tư vấn giải pháp, cung cấp nền tảng, đồng hành dự án chiến lược theo Product-Led Growth.

Hai mô hình phục vụ:

- **CMS tự phục vụ (BUs Self-serve):** phối hợp BMC xây Admin Panel để BU tự tạo, chỉnh sửa và xuất bản trang.
- **Phát triển trực tiếp (Dedicated Build):** đồng hành Cell Teams xây Web Product có UI/UX và nghiệp vụ riêng theo Mobase Design System, ở ba mức: tư vấn, đồng hành phát triển, chuyển giao tự vận hành. Điển hình: Cinema Hub, Vehicle Hub, Financial Hub, Student Hub.

Giá trị kinh tế: thay vì mỗi Cell Team duy trì đội kỹ thuật Web và tên miền riêng, tất cả kết nối vào momo.vn để thừa hưởng uy tín thương hiệu, Domain Authority và hạ tầng đã chuẩn hóa.

**Đánh giá 8 sáng kiến**

| Initiative | Kết quả 2026 | Yếu tố thành công hoặc thất bại | Khuyến nghị |
| :--- | :--- | :--- | :--- |
| Cloud Migration (AWS sang FPT Cloud) | Go-Live 21-22/07; 36/36 FE, 11/11 BE, 3/3 DB; 137 endpoint; 0 rollback | Kế hoạch cutover chi tiết, Smoke Test trước và sau, cutover ban đêm | Chuyển sang vận hành ổn định |
| MoSpark / Admin Panel | Live trên Production; GenAI sinh nội dung theo chuẩn brand | Next.js, Supabase, Refine; nhu cầu tự tạo Landing Page rõ | Scale thành CMS duy nhất cho nội dung, quảng cáo, analytics |
| Identity Platform | Hoàn thiện spec; core định danh đa nền tảng lên Production | Phụ thuộc phối hợp User Growth và ITC | Tiếp tục: là nền cho tín hiệu Web sang App |
| Umami Internal Tracking | Chạy song song GA4; dashboard theo Project | Chủ động dữ liệu, real-time; cần vận hành hạ tầng | Mở rộng cho toàn bộ Mini Web |
| Utility Tools và Boilerplate | Payment Component, Lead Form, JSON Form Builder, UI Kit cho hàng chục Mini Web | Đồng bộ Tech Stack ITC; JTBD trước khi xây | Mở rộng thư viện theo nhu cầu Cell Team |
| Hub mới (Phạt Nguội, Merchant, Cinema, Financial, Vehicle, Student) | Ra mắt nhiều Mini Web ngách | Bám nhu cầu tìm kiếm của người chưa dùng MoMo | Scale Hub có Traffic tốt; thử tiếp phần còn lại |
| Chatbot AI và RAG Knowledge Base | Triển khai giới hạn trên Production | Chất lượng dữ liệu từ nội dung Web | Thử tiếp, đánh giá mở rộng 2027 |
| Vận hành Mini Web hiện hữu (Vé máy bay, Vay nhanh, BHOT, Bus, Travel, Sim, CVS, Soundbox...) | 100% Smoke Test đạt trên Production | Bảo trì định kỳ, SLA rõ | Tiếp tục hỗ trợ theo chuẩn ITC |

### 2.2. Traffic Web: Non-Paid và Paid

**Tổng quan Traffic Web, Jan-24/Nov/2026 và Forecast cả năm**

Web đạt 32,97M PV trong 10 tháng và lũy kế **36,91M PV** đến 24/11/2026 (gồm **29,09M Non-Paid** chiếm 78,8%, trong đó Organic 18,20M chiếm 62,6% Non-Paid; và **7,82M Paid**). Forecast cả năm 2026 đạt **40,69M PV** (Non-Paid 32,77M, Paid 7,92M). Tỷ trọng Non-Paid tăng dần khi Paid được tối ưu: 77-80% trong Q1-Q3, 86,9% trong tháng 10 và Forecast đạt ~80,5% cả năm (40,69M tổng = 32,77M Non-Paid + 7,92M Paid).

| Tháng | PageView Web (triệu) |
| :--- | :---: |
| Jan/2026 | 2,59 |
| Feb/2026 | 3,46 |
| Mar/2026 | 3,21 |
| Apr/2026 | 2,69 |
| May/2026 | 3,27 |
| Jun/2026 | 3,41 |
| Jul/2026 | 3,17 |
| Aug/2026 | 3,47 |
| Sep/2026 | 3,95 |
| Oct/2026 | 3,60 |
| Nov/2026 (MTD 1-24/11) | 3,94 |
| Dec/2026 (Forecast) | 4,00 |
| **Forecast cả năm 2026** | **40,69** |

- **Non-Paid là động lực tăng trưởng.** Tháng 10 đạt 3,60M PV (-8,9% so với Sep) do cắt 723.612 PV Paid kém hiệu quả, trong khi Non-Paid tăng 13,5% lên 3,13M: Organic Search 1,72M (+5,7%), Direct 0,93M (+23,3%), Referral và nguồn khác 0,48M (+27,9%), AI 18.547 PV (+36,4%).
- **Cinema và Financial Hub dẫn đầu Traffic.** Tháng 10, Cinema đạt 1,13M PV (khoảng 31% tổng), Financial Hub đạt 273.705 PV (+9,6% so với Sep).

**Kết luận:** Non-Paid là nguồn tăng trưởng chính của Web (29,09M PV, 79% tổng PV), nhưng Organic đi ngang quanh 1,6-1,9M PV mỗi tháng từ May vì AI trả lời trực tiếp các câu hỏi kiến thức chung, trong khi Direct, Referral và AI tăng. Vì vậy 2027 Web đầu tư song song SEO và GEO/AEO, và dùng Utility để user có lý do ở lại và sang App.

### 2.3. AI Search

- **AI Traffic còn nhỏ nhưng chuyển đổi cao.** Lũy kế 93.652 PV đến 24/11 (70.758 PV Jan-Oct), trung bình ngày tăng 177% từ May đến Nov; Nov dự kiến 32,4 nghìn PV (thực tế 28,8 nghìn PV 1-24/11). ChatGPT chiếm 96,8%, Gemini 2,3%, Perplexity 1,0%. Click to App đạt 5,24% trên phiên (Oct đến 08/11), ngang Direct (5,52%) và cao hơn Organic (2,96%).
- **Tìm kiếm chuyển từ từ khóa sang khám phá bằng AI theo ý định.** Nội dung tĩnh, thiếu chiều sâu mất lượt nhấp; công cụ tương tác và dữ liệu thời gian thực được Google lẫn AI engine ưu tiên trích dẫn.

**Xu hướng 1-2 năm: tìm kiếm theo mục tiêu và hành trình**

- Google AI Mode tách một câu hỏi thành nhiều câu hỏi phụ, mỗi câu một ý định riêng (query fan-out, theo Aleyda Solis).
- Intent graph (mục tiêu gốc, mục tiêu phụ, điều kiện) mới là hướng nghiên cứu, chưa phải hệ thống chính thức của Google, chưa dùng làm căn cứ kế hoạch.
- Theo SEOClarity, nguồn AI trích dẫn có thể không trùng kết quả đứng đầu. Web cần phủ nhiều câu hỏi phụ của một chủ đề, cùng logic với việc thiết kế hành trình nhiều bước thay vì một trang đơn lẻ.
- Thử nghiệm 2027: chọn một cụm (CIC), đo tỷ lệ được trích dẫn trên các câu hỏi phụ, tách khỏi thứ hạng; báo cáo go/no-go cuối mỗi quý.

### 2.4. Install và MAU

**New Users: phễu cài đặt và đăng ký từ Web**

Lũy kế từ Jul đến 24/11/2026: **44.684 lượt cài đặt (Install)** (Jul: 5.239; Aug: 10.041; Sep: 10.501; Oct: 11.143; Nov MTD 1-24/11: 7.760) → **14.735 đăng ký (33,0%; Oct đạt 35,0%)** → **8.934 liên kết ngân hàng (60,6% trên đăng ký; 20,0% trên Install)** → **5.093 MAU (57,0% trên liên kết ngân hàng; 11,4% trên Install)**. Nov MTD ghi nhận đăng ký 30,3%, liên kết ngân hàng 63,9% và MAU 11,8% trên Install, so với kênh Media trả phí 11,0% (kỳ của số Media chưa được xác nhận, cần verify). Số đăng ký Nov trong file AppsFlyer đến 24/11 trùng với file đến 22/11, nên tỷ lệ đăng ký Nov có thể chưa đủ.

- Banner Chào MoMo toàn Web mang về 8.517 lượt, chiếm 76% cài đặt tháng 10. Cinema Hub đóng góp 1.931 lượt (17%), tỷ lệ đăng ký sang liên kết ngân hàng 25,1%. Tăng trưởng cài đặt phụ thuộc lớn vào một cơ chế.
- Phễu tháng 10: cài đặt sang đăng ký 3.902 (35,0%), bước rớt lớn nhất; đăng ký sang liên kết ngân hàng 2.389 (61,2%), cao nhất từ đầu năm; liên kết ngân hàng sang MAU 1.284 (khoảng 54%). Tổng từ cài đặt đến MAU 11,5%.
- iOS chiếm 51% lượt cài đặt nhưng 57% người liên kết ngân hàng và 59% MAU tháng 10.
- **Kết luận:** người cài từ banner chưa dùng Utility nào nên vào App không có lý do để đăng ký. Người đến từ Utility đã có việc cần làm tiếp; đây là nhóm cần đo riêng và ưu tiên.

### 2.5. Cinema

**Cinema Hub.** Baseline Traffic lớn nhất, và là dự án có vấn đề chuyển đổi cần xử lý sớm nhất.

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

- **Thống nhất số liệu giữa Slide và Tài liệu:** Tổng cộng từng tháng cho kết quả **174.094 vé** và **80.050 giao dịch** (lưu ý: truy vấn Dashboard theo dải ngày từng báo hụt đúng phần Jul ra 168.884 vé / 77.625 giao dịch / 15,91 tỷ đ, đã kiểm tra bổ sung). Trên Slide (8, 13, 14, 20) dùng mức AOV quy chuẩn thận trọng là **200.000 đ/giao dịch**, cho GMV chuẩn là **16,01 tỷ đ** (80.050 x 200.000 đ); giá trị thực tế ghi nhận trên đối soát tháng là **16,41 tỷ đ** (AOV thực tế ~205.000 đ). Tháng 11 (Nov/2026) ghi nhận thêm 1,01M PVs (MTD 1-24/11) (mục tiêu tháng 1,29M; tháng 12 mục tiêu 1,50M).
- Tỷ lệ quy đổi chuẩn dùng cho kế hoạch 2027: **8,8 giao dịch trên 1.000 PV** (tỷ lệ PV sang giao dịch 0,88%), AOV quy chuẩn **200.000 đ/giao dịch** (~2,17 vé/giao dịch).
- Sep đạt 1.220.075 PV, cao hơn mục tiêu 1,12M khoảng 9%.
- **Kết luận:** người xem lịch chiếu đã có ý định cao nhất, nhưng khi chuyển sang App để thanh toán thì mất suất chiếu và ghế đã chọn, phải làm lại từ đầu, và hơn 90% bỏ dở. Đây là điểm rơi có giá trị lớn nhất của toàn Web.

### 2.6. Financial

**Financial Hub.** Dự án chiến lược cốt lõi với bộ Utility tài chính. Utility có CTR cao là yếu tố thu hút user, trong khi nhóm Tích lũy và Đầu tư còn thiếu Utility.

- **Traffic tháng 10:** 273.705 PV (+9,6% so với Sep), đạt 109,5% mục tiêu 250.000 PV. Trung Tâm Tài Chính và Tiện ích Tỷ giá đạt 43.495 PV (+442,0%), Ví Trả Sau đạt 58.268 PV (+38,2%), bù mức giảm 47.814 PV của Vay Nhanh (-43,5%).
- **Utility tạo tương tác:** CTR tháng 10 của Ước tính khoản vay là 43,8%, Tra cứu CIC 38,6%, Tính lương Gross-Net 33,7%; ba Utility này chiếm 87,4% lượt tương tác của Hub (7.100 trên 8.120 lượt). Bảng tĩnh giá vàng, tỷ giá, lãi suất đạt 0% CTR.
- **Utility đã triển khai:** Tính lương Gross-Net, Tỷ giá, Giá vàng (từ Sep), Chứng chỉ quỹ, Ước tính khoản vay, Tra cứu điểm CIC, Trả góp Ví Trả Sau, Lãi tiết kiệm, Chuyển đổi ngoại tệ, BHXH và lương hưu. Đang triển khai: Phân bổ lương 50/30/20, Tính thuế TNCN và Thuế Hộ Kinh Doanh, Gamification Điểm Tín Dụng CIC (tháng 11).
- **Điểm cần cải thiện:** Tiết kiệm (1,5K PV) và Chứng chỉ quỹ (458 PV) còn Traffic tự nhiên thấp, nhóm Tích lũy chưa đủ Utility.
- **Phục hồi tháng 11 sau tái cấu trúc PLG từ Aug:** PageView Non-Paid 1-19/11 đạt 294,5 nghìn, tăng 105% so với cùng kỳ Oct (143,4 nghìn). Trong 1-20/11, Financial đạt 4,36M Impression trên Google Search (21,3% tổng momo.vn) và 5,77M Impression trên AI Overview (18/5-20/11, 25,7% toàn Website). Click to App theo user tháng 11: Điểm Tín Dụng 80,4%, Vay Nhanh 65,0%, Ví Trả Sau 29,0%, Trung Tâm Tài Chính 5,4%.
- **Hướng 2027:** đạt 1M PV mỗi tháng cần gấp khoảng 3,7 lần Oct. Năm 2027 chuẩn hóa UX Framework và Microjourney cho từng Utility tài chính.

### 2.7. Vehicle Hub

**Vehicle Hub.** Phạt Nguội là Pioneer Project đã xác nhận trong H1/2026, làm nền để khởi động Vehicle Hub cùng VTTI và Insurtech. Thị trường 23,2 triệu lượt tìm kiếm mỗi tháng (Giá xăng 10,52 triệu, Phạt Nguội 6,58 triệu, ETC 1,31 triệu, Trạm sạc EV 1,24 triệu).

- **Phạt Nguội phục hồi:** CTR 24,3% và 660 trích dẫn từ AI trong 28 ngày đầu; 1-15/11 đạt 88.160 PVs, tỷ lệ mở App 69,5% (run rate khoảng 176 nghìn PVs/tháng). Tháng 9 giảm do API Phạt Nguội gián đoạn 01/09-20/09.
- **Cụm liên quan tăng:** Bảo hiểm ô tô từ 11.885 PV (May) lên 25.502 PV (Oct); Tiện ích giao thông từ 5 PV (Aug) lên 20.425 PV (Oct).
- **Kết luận:** người tra Phạt Nguội là chủ xe, nhóm có nhu cầu bảo hiểm xe, nhưng năm 2026 hai cụm chạy tách nhau và chưa có Offer nối từ trang tra cứu sang báo giá.

### 2.8. Potential Intent Search

**InsurTech (bảo hiểm), 01/01-12/11/2026.** Web mang về 136.819 user bảo hiểm, tăng 32% so với cả năm 2025. 44-51% người mua bảo hiểm trên Web chưa có ví MoMo.

| Sản phẩm | Traffic Web | So với 2025 | Kết quả từ Web | Đầu tư SEO + SEM |
| :--- | :---: | :---: | :---: | :---: |
| Bảo hiểm ô tô (thân vỏ) | 162.304 | +46% | 2.118 leads, 71 giao dịch (khoảng 462 triệu đ GMV) | 1,05 tỷ đ |
| Bảo hiểm xe máy | 90.522 | -52% | 1.750 người mua (289 triệu đ GMV, -11% YoY); 1.948 giao dịch về App | 350 triệu đ |
| BHYT | 196.198 | Gấp 4,4 lần | 2.643 người mua, **2,67 tỷ đ GMV (+65% YoY)**, 86% chốt trên Web | 150 triệu đ |

- Bảo hiểm ô tô: lead sang giao dịch 3,3%, thấp hơn mục tiêu 7-10%.
- Bảo hiểm xe máy: traffic năm nay bằng 48% cả năm 2025 dù 10/10 từ khóa mục tiêu trong top 10. Chưa xác định nguyên nhân.
- BHYT: chi phí SEO và SEM khoảng 57.000 đ mỗi người mua từ Web, thấp nhất trong ba sản phẩm.
- **Kết luận:** BHYT chứng minh khi giao dịch hoàn tất ngay trên Web thì chuyển đổi cao. Nhưng sau khi mua, chưa có bước tiếp theo đưa nhóm 44-51% chưa có ví vào App.

**Sản phẩm khác đóng góp GMV trên Web, Jan-Oct/2026**

| Sản phẩm | Chỉ số đến tháng 10 | GMV | Ghi chú |
| :--- | :---: | :---: | :--- |
| Vé xe | 3.787 MAU giao dịch | 1,51 tỷ đ (ước tính) | Tính theo 3.787 MAU x AOV 400.000 đ |
| eSIM du lịch | 824 giao dịch | 160,4 triệu đ | Tỷ lệ chuyển đổi 3,18%; không có chi phí quảng cáo |

### 2.9. Điểm rơi 2026 và nguyên tắc 2027

Năm 2026 cho thấy giá trị bị mất ở bảy điểm, từ Traffic đến đăng ký trong App:

| Điểm rơi | Số liệu | Nguyên nhân |
| :--- | :--- | :--- |
| Organic tăng chậm | +5,7% so với Sep (Oct), thấp hơn Non-Paid tổng (+13,5%) | AI Search trả lời trực tiếp nội dung kiến thức chung |
| Bảng tĩnh không điều hướng user đi tiếp | Giá vàng, tỷ giá, lãi suất: CTR 0% | Trang chỉ hiển thị số, không có Utility hay bước tiếp theo |
| Nhóm Tích lũy thiếu Utility | Tiết kiệm 1,5K PV, Chứng chỉ quỹ 458 PV | Chưa đủ Utility cho nhóm này |
| Các cụm sản phẩm chạy riêng | Phạt Nguội và Bảo hiểm xe | Chưa có Offer nối giữa các cụm |
| Cinema bỏ dở ở bước thanh toán | Trên 90% | Sang App thanh toán làm mất suất chiếu và ghế đã chọn trên Web |
| Bảo hiểm ô tô: lead không thành giao dịch | 3,3% (71 trên 2.118 lead), mục tiêu 7-10% | Luồng báo giá chưa tối ưu |
| Install không đăng ký | 35,0% đăng ký (Oct), 65% không đăng ký | 76% Install từ một banner, user chưa có việc cần làm tiếp trong App |

**Nguyên tắc 2027**

- **Utility trước, nội dung sau, mỗi Utility có một Microjourney.** Utility điều hướng user sang việc kế tiếp, còn bảng tĩnh giá vàng, tỷ giá, lãi suất không có bước tiếp theo nên CTR là 0%. Mỗi Utility có một Offer gắn với ngữ cảnh của user.
- **Đầu tư SEO và GEO/AEO song song.** Organic tăng chậm hơn Non-Paid tổng khi AI trả lời trực tiếp, trong khi AI Traffic nhỏ nhưng chuyển đổi cao. Phạt Nguội là mẫu: 28 ngày theo đúng chiến lược từ khóa tạo Organic bền vững và 660 trích dẫn từ AI. llms.txt, Schema và Topical Authority áp dụng cho mọi cụm.
- **KPI theo vai trò.** Web Platform được đo bằng Traffic, Install và Shared-KPI với BU, thay vì số tính năng đã giao.

---

## 3. 2027 DIRECTION

### 3.1. Objectives

| Cấp | Chỉ số | Baseline 2026 | KPI 2027 |
| :--- | :--- | :--- | :--- |
| **North Star Metric** | PageView Non-Paid | 32,77M (Forecast cả năm) | 55,57M |
| **Success Metric** (cùng BU) | GMV, DAU, MAU, MEU | Cinema 16,01 tỷ đ GMV (Jan-Oct); Bảo hiểm 2,67 tỷ đ GMV (BHYT) | BU và FinanceBP xác nhận |
| **Success Metric** | W2A CTR | 3,36% (Oct) | 4,0-4,5% |
| **KPI** | Install mỗi tháng | 11.143 (Oct) | 30.000 |

### 3.2. Overview

Năm 2027, Web làm ba việc theo thứ tự: thu hút đúng nhu cầu từ Google và AI, nối từng bước sang đúng Service trong App, và đo đến kết quả.

**Nhu cầu tìm kiếm**

Nhu cầu đến từ Search Engine và AI Agent (Google, ChatGPT, Gemini, Perplexity), nơi user đã có ý định rõ. Utility và nội dung trả lời đúng nhu cầu đó tạo ra Non-Paid Traffic. Mục tiêu 2027 là 63,49M PVs toàn Web, gồm Non-Paid 55,57M. Một số Utility như giá vàng, giá xăng dầu, tỷ giá còn giúp user quay lại Web.

**Bước nối sang App**

Web thu hút user, để user tự xử lý việc cần làm bằng Utility, rồi chuyển sang App bằng một Offer, giữ đúng ngữ cảnh từ Out-App đến In-App. App đảm nhận xác minh hoặc thanh toán. Bước nối giữa các Service được thiết kế theo bốn nhóm:

| Nhóm Service | Service | Bước nối 2027 |
| :--- | :--- | :--- |
| Anchors (thu hút, tạo thói quen) | Phạt Nguội, Vé Số, Chứng Khoán, Chứng Chỉ Quỹ | Phạt Nguội sang báo giá Bảo hiểm xe |
| Connective (thu thập ID, dữ liệu) | Tra cứu CIC | Điểm CIC tốt sang hạn mức Ví Trả Sau; Ước tính khoản vay sang Vay Nhanh với số tiền đã nhập |
| Adjacent (tăng tần suất, số dư ví) | Cinema, Bảo hiểm, Ví Trả Sau, Tích lũy | Cinema mở App đúng bước thanh toán, giữ suất chiếu và ghế; Tính lương, lãi suất sang Túi Thần Tài |
| Monetization (ưu đãi trúng đích) | Vé xe, eSIM du lịch, Vay Nhanh | eSIM, Vé xe: Offer cài App cho chuyến sau |

Bước nối 2027 là giả thuyết, cần BU xác nhận khả thi về sản phẩm, dữ liệu và pháp lý trước khi xây.

Bốn nguyên tắc thiết kế mỗi bước nối:

- **Mỗi Microjourney chỉ có một Offer,** đặt đúng lúc user vừa có kết quả và gọi đúng việc đang làm, ví dụ "Kiểm tra hạn mức với điểm CIC này" thay cho "Tải App".
- **Điều hướng bắt đầu từ việc user vừa làm,** không bắt đầu từ sản phẩm MoMo muốn bán.
- **Mỗi trang có ba khối:** trả lời câu hỏi (đủ rõ để Google và AI trích dẫn), Utility để user tự kiểm tra trường hợp của mình, và một Offer duy nhất. Trang chỉ có khối đầu, như bảng tĩnh giá vàng, tỷ giá, lãi suất (CTR 0%), không chuyển được user nào.
- **Tối ưu Conversion giữa các bước, không chỉ tăng Traffic.** Install sang đăng ký đạt 33,0% (Jul-Nov), và hơn 90% người chọn ghế Cinema bỏ dở ở bước thanh toán.

Trust đi xuyên suốt: đây là điều kiện để AI Agent trích dẫn và để user yên tâm sang App. Web cần giấy phép theo từng Service, chứng nhận an toàn thông tin và kênh Báo cáo lừa đảo ẩn danh. Kênh Báo cáo lừa đảo đã có; phần tổng hợp giấy phép và pháp lý cần phối hợp với Legal để xác nhận và triển khai theo từng Service.

**Kết quả đo lường**

Web chịu trách nhiệm PageView, Click to App và Install; GMV, DAU, MAU, MEU cùng chịu trách nhiệm với BU. KPI Install 2027 là 30.000/tháng (Oct/2026: 11.143). Giá trị Web mang lại cho từng BU:

| BU | Service | Giá trị Web mang lại |
| :--- | :--- | :--- |
| Movies | Cinema | Traffic và GMV |
| Financial Services | Ví Trả Sau, Vay Nhanh, Túi Thần Tài, Tiết kiệm, Chứng chỉ quỹ và các sản phẩm của FinHub | Traffic và Click to App |
| InsurTech | Bảo hiểm xe, bảo hiểm y tế | Traffic và GMV |
| User Growth (New User) | Cài App, đăng ký | Install và đăng ký |

**Anchor và Potential Market**

Ngoài các Service đã có bước nối, Web mở rộng theo Search Demand sang hai nhóm. Anchor là Service tần suất cao, thu hút user mới và tạo thói quen quay lại; Web xây Utility cho nhóm này trong 2027. Potential Market có nhu cầu tìm kiếm lớn nhưng Web chưa cam kết chỉ tiêu.

| Nhóm | Vai trò | Search Demand | Hướng 2027 hoặc kết quả Web 2026 |
| :--- | :--- | :--- | :--- |
| Bảo hiểm y tế | Potential | 1,42 triệu, SoV MoMo 0% | 2,67 tỷ đ GMV (+65% YoY) |
| Vé xe khách | Potential | 2,12 triệu | 1,51 tỷ đ GMV (ước tính) |
| Bảo hiểm xe máy | Potential | 58.810, SoV MoMo 38% | 289 triệu đ GMV (-11% YoY) |
| eSIM | Potential | 1,87 triệu (SIM số đẹp và eSIM) | 160,4 triệu đ GMV, 824 giao dịch |
| Bảo hiểm ô tô | Potential | 74.000 (vật chất), SoV MoMo 0% | 2.118 lead, 71 giao dịch |
| Bảo hiểm xã hội | Potential | 938.090 | Sắp ra mắt |
| Vé Số | Anchor | 1,54 tỷ lượt tìm kiếm | Cổng Vé Số tại momo.vn/ve-so theo mô hình Utility-Led: tra cứu kết quả, dò vé, rồi điều hướng sang App |
| Chứng Khoán | Anchor | 2,66 triệu, SoV MoMo 0% | Chuyên trang Chứng Khoán và 30 trang mã VN30; Utility giả lập tích sản cổ phiếu, CTA mở App |
| Chứng Chỉ Quỹ | Anchor | 19,2 nghìn | Trang Chứng Chỉ Quỹ với 30 quỹ mở đối tác, đầu tư định kỳ từ 10.000đ/ngày; cấp OneLink riêng theo Utility để đo Click to App (hiện dưới 15 Click to App mỗi dự án) |

Với Potential Market, Web giữ Traffic Non-Paid và Utility hiện có, đầu tư thêm theo định hướng của công ty.

### 3.3. Strategic

Năm 2027, Web là kênh Nurture user chưa có App từ nhu cầu tìm kiếm. Web thu hút Non-Paid Traffic từ Search Engine và AI Agent, thiết kế Microjourney trên Utility để điều hướng user sang đúng Service trong App, giữ đúng ngữ cảnh từ Out-App đến In-App. Hướng này đi qua bốn trụ cột: SEO / GEO / AEO, MoSpark 2.0, Security và Shared Product.

### 3.4. Portfolio

KPI 2027 là **55,57M PVs Non-Paid** (tổng Web 63,49M PVs), đạt được khi đủ kế hoạch cho phần nội dung nền và giải ngân trọn vẹn 2 đợt. Về **Install**, KPI 2027 là **30.000/tháng** (khoảng 360.000 cả năm), gấp khoảng 2,7 lần Oct/2026 (11.143).

**Khoảng trống điều hướng user.** Giữ nguyên nhịp Oct/2026 (11.143 lượt/tháng), cả năm 2027 chỉ đạt khoảng 134 nghìn Install. Để đạt 30.000/tháng mà vẫn giữ chất lượng người dùng mới, cần đáp ứng đồng thời 3 điều kiện bắt buộc:
- **Giảm phụ thuộc banner:** Tỷ trọng cài đặt từ banner toàn trang giảm từ 76% xuống dưới 50%; nguồn ngoài banner tăng lên nhờ Ads Manager (đặt lời mời đúng lúc trong luồng công cụ) và Deferred Deep Linking.
- **Giữ sàn chất lượng:** Duy trì tỷ lệ **Register/Install >= 35%** và **MAU/Install >= 11,4%**, không ép tải App bằng banner đại trà.
- **Điều kiện giải ngân:** Mục tiêu `55,57M PVs Non-Paid` phụ thuộc vào việc giải ngân đủ 2 đợt; nếu đợt 2 không được duyệt, ưu tiên giữ ngân sách cho Top 3 Hub (Cinema, CIC, Tích lũy) và điều chỉnh giảm phần nội dung nền.

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
- **Ngân sách 2027 tập trung vào CIC, vay và tích lũy (khoảng 9,4 triệu lượt/tháng)** thay vì giá vàng và tỷ giá, vì các nhóm này có bước tiếp theo điều hướng thẳng vào sản phẩm tạo doanh thu. Giá vàng và tỷ giá là lựa chọn có chủ đích: cụm Tỷ giá đang triển khai theo mô hình pSEO từ 2026 và nằm trong phần tăng trưởng không ngân sách.

**Điều kiện từ BU:**

- Movies BU và Financial Services BU chia sẻ lịch phim, lộ trình sản phẩm và thay đổi chính sách trước 2-4 tuần.
- Financial Services BU cung cấp chỉ số trên App (GMV, MAU, MEU) và đối soát qua Dashboard dùng chung.
- Movies BU thống nhất lộ trình rút ngắn bước thanh toán (QR hoặc deep link mở App giữ suất chiếu và ghế) trong 6 tháng đầu 2027.

### 3.5. Allocation

**Bảng phân bổ mục tiêu 55,57M PVs Non-Paid 2027 theo 4 dự án và phần nền:**

| Nhóm dự án / Nguồn | Mục tiêu 2027 (M PVs) | Tỷ trọng trên 55,57M | Ghi chú kiểm chứng |
| :--- | :---: | :---: | :--- |
| **Cinema Hub** | **12,6 - 14,0M** | 23 - 25% | Hub có GMV vé; BU Movies (cần xác nhận thêm phần Paid tách riêng nếu có) |
| **Phạt Nguội** | **2,1 - 2,5M** | 4% | Run rate Nov đạt ~176K PVs/tháng, tăng tới 20% |
| **CIC & Tín dụng** | **2,2 - 2,5M** | 4% | Tín dụng; BU Financial Services |
| **Financial: Tích lũy & Đầu tư** | **1,0 - 1,5M** | 2 - 3% | Túi Thần Tài, Tiết kiệm, CCQ; BU Financial Services |
| **Dự án khác & nội dung nền** | **35,1 - 37,7M** | 63 - 68% | Vehicle Hub, New User, Tỷ giá, eSIM, Cell Teams, Bảo hiểm (phép trừ phần còn lại) |
| **Tổng Non-Paid 2027** | **55,57M** | **100%** | Tổng Web gồm Paid 7,92M (giữ như 2026 do BU quyết định) = **63,49M PVs** |

Mục tiêu PV giả định Paid giữ nguyên mức 2026 (7,92M, khoảng 0,66M mỗi tháng); toàn bộ mức tăng còn lại đến từ Non-Paid. Lộ trình từng tháng:

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
| **Cả năm** | **63,49** | **7,92** | **55,57** |

- So với 2026 (Forecast cả năm: tổng 40,69M, Paid 7,92M, Non-Paid 32,77M), KPI 2027 giúp tổng PVs tăng +56% (63,49M) và Non-Paid tăng +22,80M (+70%), bình quân khoảng 5,7% mỗi tháng.
- Non-Paid đặt theo tốc độ tăng trưởng, không theo tỷ trọng, vì Paid do BU quyết định và không thuộc cam kết của Web Platform.

**Sáu chỉ số hỗ trợ KPI chính.** Ngoài PageView Non-Paid và Install, Web theo dõi sáu chỉ số cho biết từng khâu trong hành trình đang ở đâu và cần đạt gì vào năm 2027.

| Chỉ số | Hiện tại | KPI 2027 | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| Install sang đăng ký | 33,0% (Jul-Nov); 35,0% (Oct) | 40-45% | User cài App mà chưa đăng ký thì chưa dùng được Service; cần tách nguồn banner và nguồn Utility để đo riêng |
| Tỷ trọng Install từ banner toàn trang | 76% (Oct); 81% (Nov MTD) | Dưới 50% | Cài App từ banner nghĩa là user chưa dùng Utility nào trước đó; thay dần bằng Offer trong luồng qua Ads Manager |
| PageView từ AI mỗi tháng | 18.547 (Oct); 28,8 nghìn (1-24/11) | 46.000 bình quân mỗi tháng (khoảng 551 nghìn cả năm) | AI Traffic còn nhỏ nhưng Click to App ngang Direct |
| PageView CIC và Tích lũy | 0,63M (Jan-Oct, gồm CIC 0,42M và Tích lũy, Đầu tư 0,21M) | 3,2-4,0M cả năm | Hai nhóm có ngân sách đầu tư riêng; Web cam kết Traffic và Click to App, MAU do BU xác nhận khi có dữ liệu |
| Cell Teams được hỗ trợ | 16 (6 tự vận hành) | 20 (15 trở lên tự vận hành) | Số Cell Teams tự xuất bản trên MoSpark mà không cần Dev |
| Strategic Hubs đang hoạt động | 3 (Cinema, Vehicle, Financial) | 5 trở lên | Mở rộng Vé số, Chứng khoán, Chứng chỉ quỹ theo điều kiện |

**Phần tăng trưởng không ngân sách: 64-73% mức tăng Non-Paid**

Ba dự án có ngân sách đóng góp 6,1-8,3M PV. Phần còn lại, 14,5-16,7M PV Non-Paid, nằm ngoài các dự án được cấp vốn. Đây là giả định lớn nhất của toàn bộ mục tiêu.

- **Phụ trách:** Web Platform và Out-App Traffic, rà soát hằng tuần.

### 3.6. Pillar Objectives

#### Pillar 1: SEO / GEO / AEO
*Objective:* tăng PageView Non-Paid cho các Strategic Project bằng SEO và GEO/AEO, hướng tới 55,57M PageView Non-Paid năm 2027.

**Dự án trọng tâm.** SEO và GEO/AEO tập trung vào ba dự án:

| Dự án | PVs 2027 | Mục tiêu thứ hạng |
| :--- | :--- | :--- |
| Cinema Hub | 12,6-14,0M | Top 1-3 cụm mua vé, rạp, phim mới |
| CIC và Tín dụng | 2,2-2,5M | Top 3-5 cụm CIC, nợ xấu, điểm tín dụng |
| Tích lũy và Đầu tư | 1,0-1,5M | Top 3-5 cụm lãi suất, tiết kiệm, CCQ, tích sản |

**Dự án Anchor tiềm năng (chưa cam kết).** Phạt Nguội (tham chiếu 2,1-2,5M PVs, Top 1 cụm phạt nguội), Vé Số, Chứng Khoán và Chứng Chỉ Quỹ, triển khai sau khi BU xác nhận khả thi về sản phẩm và pháp lý.

**Bảo hiểm.** Giữ luồng mua BHYT và tối ưu báo giá Bảo hiểm ô tô, chờ định hướng chung của công ty.

**GEO/AEO cho mọi dự án.** Chuẩn hóa Schema.org, llms.txt và trang minh bạch pháp lý YMYL để AI Agent ưu tiên trích dẫn momo.vn. Mỗi hạng mục pilot một quý với KPI rõ: đạt ngưỡng thì mở rộng, không đạt thì dừng.

#### Pillar 2: MoSpark 2.0
*Objective:* Cell Teams tự dựng Landing Page cho Utility và chiến dịch trong 1-2 ngày; giảm tỷ trọng Install từ banner toàn trang từ 76% xuống dưới 50%; W2A CTR từ 4,5% trên các trang Utility; GenAI Content tự phục vụ trong vài phút cho Cell Teams.

1. **Landing Page Builder (Scale và Integrate).** Mở rộng kho template cho Utility và chiến dịch, AI-assisted generation, A/B Testing ngay trên Builder, Variant fan-out và Multi-tenant để nhiều Cell Teams cùng dùng. Mỗi trang gắn một KPI rõ ràng. Success metrics: Time-to-launch dưới 1-2 ngày, Self-serve rate, tỷ lệ trang gắn KPI.
2. **GenAI Content Pipeline và AI Quality Gate.** Nâng pipeline từ tự động khoảng 80% (vài giờ) lên tự phục vụ trong vài phút cho toàn bộ Cell Teams. AI Quality Gate chấm điểm độ chính xác thông tin, E-E-A-T và chống trùng lặp trước khi xuất bản.
3. **Product-Led Growth (PLG).** Nâng số Hub chiến lược từ 3 lên 5 trở lên trên PLG Project Engine của MoSpark; scale Hub có Traffic tốt, thử tiếp phần còn lại.
4. **Utility-Led SEO.** Xây bộ mẫu pSEO (calculator, comparison, tra cứu theo ngân hàng, quận, phương tiện) trên MoSpark, thay các bảng tĩnh có CTR 0% bằng Utility.
5. **Ads Manager.** Quản lý Offer ngay trong MoSpark: mỗi luồng tối đa một Offer, đặt sau khi user có kết quả, luôn bỏ qua được, giữ đúng ngữ cảnh từ Out-App đến In-App qua OneLink. Tách chiến dịch theo ba trạng thái: chưa cài App, đã cài chưa đăng ký, đã đăng ký chưa liên kết ngân hàng.
6. **Utility Tracking và Chatbot.** Chuẩn hóa tham số cho 100% liên kết OneLink vào BigQuery, mở rộng Umami cho toàn bộ Mini Web và đối soát với GA4 hằng tháng. Chatbot và RAG Knowledge Base mở rộng trợ lý tư vấn Service trên Web.
7. **Identify (SSO): Gamification và New User Nurturing.** Gamification kế thừa chiến dịch Game Một Mùa Quýt (7.097 người chơi, 3.454 click OneLink, 1.230 người cài hoặc mở App), triển khai Gamification Điểm Tín Dụng CIC sau khi Pháp lý xác nhận khung giấy phép. New User Nurturing dựa trên Identity Platform đã chạy Production; Q1/2027 thử nghiệm đăng nhập nhẹ (Soft SSO) trên hai Utility (CIC, Ước tính khoản vay) và đo tỷ lệ đồng ý trước khi quyết định đầu tư lớn.

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

### 3.7. Budget

**Ngân sách:** 1.995.800.000 đ, khoảng 166,3 triệu đ mỗi tháng, gồm 1,95 tỷ đ cho 3 dự án và 45,8 triệu đ bản quyền công cụ. Không đề xuất ngân sách Paid. Ngân sách Cinema và Financial có phần đồng tài trợ từ BU, tỷ lệ thống nhất với từng BU trước khi giải ngân.

| Dự án | Ngân sách | PV 2026 (Jan-Oct) | PV 2027 | PV tăng thêm | Thứ hạng mục tiêu |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Cinema Hub** | 620 triệu đ | 9,10M | 12,6 - 14,0M | 3,5 - 4,9M | Top 1-3 cụm mua vé, rạp, phim mới |
| **Financial - CIC & Tín dụng** | 480 triệu đ | 0,42M | 2,2 - 2,5M | 1,8 - 2,1M | Top 3-5 cụm CIC, nợ xấu, điểm tín dụng |
| **Financial - Tích lũy & Đầu tư** | 850 triệu đ | 0,21M | 1,0 - 1,5M | 0,8 - 1,3M | Top 3-5 cụm lãi suất, tiết kiệm, CCQ, tích sản |
| **Bản quyền công cụ** (Figma Pro 9,8 triệu đ, 2 users; Semrush Pro 36 triệu đ, 1 user) | 45,8 triệu đ |  |  |  |  |
| **Tổng** | **1.995,8 triệu đ (~1,996 tỷ đ)** | **9,73M** | **15,8 - 18,0M** | **6,1 - 8,3M** |  |

Chuyển đổi cuối phễu khác nhau theo use case: Cinema đo bằng giao dịch và GMV; Financial đo bằng lượt click App, MAU/MEU và chỉ số sản phẩm do BU định nghĩa. Đây là chỉ số chất lượng traffic, đồng chịu trách nhiệm với BU.

**Vì sao ba dự án này:** mỗi dự án điều hướng user vào một phễu đã được chứng minh trong App. Cinema mang Traffic lớn nhất và đóng góp 17% Install từ Web (Oct). CIC điều hướng vào Ví Trả Sau, phễu lớn nhất sang Vay Nhanh và trả góp. Tích lũy điều hướng vào Túi Thần Tài, cửa vào của các sản phẩm đầu tư. Web không cần tự xây phễu sinh lời; Web đưa người chưa có App vào đúng đầu phễu.

---

## 4. CONCLUSION

Năm 2026, Web Platform xây xong nền tảng gồm MoSpark, GenAI Content, Utility-Led SEO, Tracking Full Funnel, Payment và OneLink, và đưa Non-Paid lên 29,09M PV, 79% Traffic Web. Điểm nghẽn nằm ở chuyển đổi: 76% Install đến từ một banner, chỉ 35,0% Install đăng ký (Oct), và hơn 90% người chọn ghế Cinema bỏ dở ở bước thanh toán.

Năm 2027, Web là kênh Nurture user chưa có App từ nhu cầu tìm kiếm. KPI 2027 là 55,57M PageView Non-Paid, W2A CTR 4,0-4,5% và 30.000 Install mỗi tháng; GMV, DAU, MAU, MEU cùng chịu trách nhiệm với BU.

Để đạt KPI này, Web cần:

- **Đầu tư song song SEO và GEO/AEO,** xây Utility cho mỗi Hub với một Microjourney và một Offer.
- **Triển khai bốn Pillar:** SEO / GEO / AEO, MoSpark 2.0, Security và Shared Product.
- **Ngân sách 1,996 tỷ đ** cho ba dự án Cinema, CIC và Tín dụng, Tích lũy và Đầu tư, cùng việc BU xác nhận bước nối và chỉ số kinh doanh trước khi xây.
