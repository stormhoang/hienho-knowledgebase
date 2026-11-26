# 2026 REFLECTION & 2027 DIRECTION - WEB PLATFORM

## 1. EXECUTIVE SUMMARY

**Năm 2026, Web đạt 36,91 triệu PageView, trong đó Non-Paid 29,09 triệu (78,8%) và tăng 53% từ T1 đến T10, cùng 44.684 lượt cài App từ T7 đến T11. Năm 2027, Web là entry point từ out-app cho user chưa có App: Nurture user từ nhu cầu tìm kiếm trên Google và AI, chuyển đổi (Conversion) sang cài App và điều hướng đến các Service của MoMo theo định hướng Product-Led Growth. KPI 2027 là 40,00 triệu PageView Non-Paid (+22,1% so với Forecast 2026) và 30.000 Install mỗi tháng (+169% so với T10/2026), khoảng 360.000 Install cả năm.**

**Kết quả 2026**

1. **Non-Paid là động lực tăng trưởng.** Từ T1 đến T10, tổng PageView tăng 39% và Non-Paid tăng 53% trong khi Paid giảm; T11 vượt mục tiêu tháng.
2. **AI Traffic nhỏ nhưng chất lượng cao.** Traffic từ AI tăng 177% mỗi ngày từ T5 đến T11. Tỷ lệ Click-to-App của AI (5,24%) cao hơn Organic (2,96%) và ngang Direct, dù AI mới chiếm khoảng 0,5% tổng PageView.
3. **Utility chứng minh hiệu quả chuyển đổi.** Utility đạt CTR 33,7-43,8%, nội dung tĩnh gần như 0%. Sau khi tái cấu trúc Financial Hub theo hướng Utility, Non-Paid của hub này tăng 105%.
4. **Web có năng lực tạo GMV.** Cinema đạt 16,01 tỷ đ GMV; Bảo hiểm y tế 2,67 tỷ đ GMV với chi phí SEO 150 triệu đ; Bảo hiểm ô tô khoảng 462 triệu đ (ước tính từ 71 giao dịch) và Bảo hiểm xe máy 289 triệu đ. Vé xe (1,51 tỷ đ, ước tính) và eSIM du lịch (160,4 triệu đ) cũng đã ghi nhận GMV.
5. **Web tạo user mới cho App.** 44.684 Install, 14.735 đăng ký và 5.093 MAU từ T7 đến T11.
6. **MoSpark vận hành từ Q2.** Web Platform hợp nhất thành Growth Unit và đưa vào vận hành MoSpark gồm Landing Page Builder, GenAI Content Pipeline (tự động khoảng 80% quy trình nội dung SEO/GEO), PLG Project Engine, Ads Manager và Chatbot. Thời gian dựng Landing Page giảm từ 1-2 tuần xuống 1-2 ngày; 16 Cell Teams được hỗ trợ, 6 đội tự xuất bản.
7. **Chuẩn hóa kỹ thuật.** GA4 và GTM vào BigQuery, 100% liên kết chuẩn hóa OneLink, Dashboard Web Performance live từ T5, Identity Platform nối hành vi từ Web sang App, và chuyển 100% từ AWS sang FPT Cloud không gián đoạn.

**Điểm cải thiện 2027**

- **Cải tiến Utility theo từng Microjourney** để đóng góp Traffic vào App cho các Service liên quan. Utility đạt CTR 33,7-43,8% nhưng Click to App chênh lệch giữa các Service (T11: Điểm Tín Dụng 80,4%, Trung Tâm Tài Chính 5,4%).
- **Cải tiến GEO/AEO.** AI Traffic mới chiếm 0,6% Non-Paid (T10) dù Click to App đạt 5,24% trên phiên, ngang Direct.
- **Web to App Tracking cho từng Service.** Mỗi Microjourney cần OneLink riêng để đo Click to App và giao dịch theo Service trong App.
- **Hiệu suất Web.** Uptime từ 99,9% và Core Web Vitals đạt ngưỡng cho mọi sản phẩm trên momo.vn, kể cả sản phẩm do Cell Team sở hữu.

**Đề xuất 2027**

| Chỉ số | Baseline 2026 | KPI 2027 |
| :--- | :--- | :--- |
| PageView Non-Paid | 32,77M (Forecast cả năm) | 40,00M (+22,1% YoY) |
| Tổng PageView Web | 40,69M (Forecast cả năm) | 47,92M (+17,8%) |
| W2A CTR | 3,36% (T10) | 4,0-4,5% (+19% đến +34%) |
| Install mỗi tháng | 11.143 (T10) | 30.000 (+169%) |

---

**Tầm nhìn 2027-2030 (Từ Human Web sang Agentic Web):**
- **2027 (Utility-Led + GEO/AEO + Microjourney):** Trước làn sóng Zero-Click Search (khi AI trả lời trực tiếp trên trang kết quả), nội dung thông tin thuần túy sẽ mất dần lượt nhấp; Web MoMo giữ chân user bằng **công cụ tương tác thực tế (Utility)** mà AI không tự làm thay được, chuẩn hóa Schema.org và llms.txt để AI ưu tiên trích dẫn, đồng thời **thiết kế mọi điểm chạm theo Microinteraction và Microjourney của hệ sinh thái MoMo** (giữ ngữ cảnh, một Offer đúng lúc trong luồng) để chuyển đổi thành Install và giao dịch ngay trong năm 2027.
- **2028-2030 (Agent-ready / B2A):** Chuẩn hóa hạ tầng dữ liệu và endpoint để các trợ lý AI bên ngoài (AI Agents) có thể truy vấn trực tiếp công cụ tra cứu và khởi tạo dịch vụ của MoMo, biến Web thành lớp thu thập tín hiệu nhu cầu (Intent Signal Layer) nuôi hệ sinh thái App.

**Luận cứ cho hướng đi này:**

- **Hành vi tìm kiếm đã chuyển sang AI.** ChatGPT có 1,2 tỷ user mỗi tuần trên toàn cầu (OpenAI, DevDay 9/2026). Tại Việt Nam, 78% user online đã dùng AI trong 3 tháng, 33% dùng hằng ngày (Decision Lab 2025, 600 người), và 62% người mua dùng AI tìm hiểu trước khi mua, trong khi Google vẫn ở mức 86% (Q&Me 10/2026, 200 người ở HCM và Hà Nội).
- **Nội dung thông tin mất lượt nhấp.** CTR vị trí 1 giảm 58% khi truy vấn có AI Overview (Ahrefs, 12/2025 so với 12/2023). Tại MoMo, Organic tăng 5,7% so với T9 (T10), chậm hơn Non-Paid tổng (+13,5%).
- **Traffic từ AI nhỏ nhưng chất lượng và tăng nhanh.** AI Traffic tăng 177% mỗi ngày từ T5 đến T11, Click to App đạt 5,24% trên phiên, ngang Direct (5,52%) và cao hơn Organic (2,96%). Đây là kênh mà user đã có ý định rõ khi sang Web, nên giá trị nằm ở Utility và dữ liệu có cấu trúc mà AI trích dẫn được.
- **Rủi ro phụ thuộc một nền tảng.** ChatGPT chiếm 96,8% AI Traffic của MoMo (Gemini 2,3%, Perplexity 1,0%), nên hạ tầng dữ liệu và endpoint cần chuẩn hóa để dùng được với nhiều AI Agent, không gắn với một nền tảng.

## 2. 2026 REFLECTION

### 2.1. Năng lực nền tảng

Năm 2026, Web Platform xây năm năng lực làm nền cho 2027: MoSpark, GenAI Content, Utility-Led SEO, Tracking Full Funnel, Payment và OneLink. MoSpark là công cụ sản xuất và quản trị nội dung cho các Cell Team, bốn năng lực còn lại phục vụ nội dung, Utility, đo lường và giao dịch.

| Năng lực | Đã áp dụng trong 2026 | Tiếp nối trong 2027 |
| :--- | :--- | :--- |
| MoSpark (công cụ sản xuất, quản trị nội dung cho Cell Team) | 16 Cell Teams, 6 tự vận hành; Landing Page 1-2 ngày (trước: 1-2 tuần); CMS live trên Production; Payment Component, Lead Form, JSON Form Builder; 100% sang FPT Cloud, không downtime; Mobase V2 | 20 Cell Teams; BMC, HR, L&D tự xuất bản; CMS duy nhất cho nội dung, quảng cáo, analytics; uptime từ 99,9%; chuẩn hóa toàn bộ sản phẩm theo Design System **MoBase V2**, áp dụng quy trình **Design-to-Code** và **Code-to-Design** |
| GenAI Content | Tự động khoảng 80% quy trình SEO, GEO; từ nhiều ngày xuống vài giờ | Mở rộng cho Cell Teams, còn vài phút; AI Quality Gate quản trị Content Strategy trước khi xuất bản |
| Utility-Led SEO | Phạt Nguội, CIC, Ước tính khoản vay, Tính lương; CTR Utility 33,7-43,8% (T10) | Mỗi Hub có Microjourney, nối kết quả sang bước tiếp theo |
| Tracking Full Funnel | GA4, GTM, GSC vào BigQuery; 100% OneLink chuẩn hóa; Dashboard live từ T5 | Identity Platform nối hành vi Web sang App; đo hoàn tất theo hành trình |
| Payment và OneLink | Payment Component; GMV Cinema 16,01 tỷ đ | Cinema: QR hoặc OneLink mở App đúng bước thanh toán, giữ lựa chọn |

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

Giá trị kinh tế: thay vì mỗi Cell Team duy trì đội kỹ thuật Web và tên miền riêng, tất cả kết nối vào momo.vn để thừa hưởng uy tín thương hiệu, Domain Authority và hạ tầng đã chuẩn hóa. Web Platform đảm bảo hiệu suất, hạ tầng, kỹ thuật và công nghệ ổn định cho mọi sản phẩm trên momo.vn, kể cả sản phẩm do Cell Team tự sở hữu.

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

**Tổng quan Traffic Web 2026 và Forecast cả năm**

Web đạt 32,97M PV trong 10 tháng và lũy kế **36,91M PV** đến 24/11/2026 (gồm **29,09M Non-Paid** chiếm 78,8%, trong đó Organic 18,20M chiếm 62,6% Non-Paid; và **7,82M Paid**). Forecast cả năm 2026 đạt **40,69M PV** (Non-Paid 32,77M, Paid 7,92M). Tỷ trọng Non-Paid tăng dần khi Paid được tối ưu: 77-80% trong Q1-Q3, 86,9% trong T10 và Forecast đạt ~80,5% cả năm (40,69M tổng = 32,77M Non-Paid + 7,92M Paid).

| Tháng | PageView Web (triệu) |
| :--- | :---: |
| T1/2026 | 2,59 |
| T2/2026 | 3,46 |
| T3/2026 | 3,21 |
| T4/2026 | 2,69 |
| T5/2026 | 3,27 |
| T6/2026 | 3,41 |
| T7/2026 | 3,17 |
| T8/2026 | 3,47 |
| T9/2026 | 3,95 |
| T10/2026 | 3,60 |
| T11/2026 (MTD 1-24/11) | 3,94 |
| T12/2026 (Forecast) | 4,00 |
| **Forecast cả năm 2026** | **40,69** |

- **Non-Paid là động lực tăng trưởng.** T10 đạt 3,60M PV (-8,9% so với T9) do cắt 723.612 PV Paid kém hiệu quả, trong khi Non-Paid tăng 13,5% lên 3,13M: Organic Search 1,72M (+5,7%), Direct 0,93M (+23,3%), Referral và nguồn khác 0,48M (+27,9%), AI 18.547 PV (+36,4%).
- **Cinema và Financial Hub dẫn đầu Traffic.** T10, Cinema đạt 1,13M PV (khoảng 31% tổng), Financial Hub đạt 273.705 PV (+9,6% so với T9).

**Kết luận:** Non-Paid là nguồn tăng trưởng chính của Web (29,09M PV, 79% tổng PV), nhưng Organic đi ngang quanh 1,6-1,9M PV mỗi tháng từ T5 vì AI trả lời trực tiếp các câu hỏi kiến thức chung, trong khi Direct, Referral và AI tăng. Vì vậy 2027 Web đầu tư song song SEO và GEO/AEO, và dùng Utility để user có lý do ở lại và sang App.

### 2.3. AI Search

- **AI Traffic còn nhỏ nhưng chuyển đổi cao.** Lũy kế 93.652 PV đến 24/11 (70.758 PV T1-T10), trung bình ngày tăng 177% từ T5 đến T11; T11 Forecast 32,4 nghìn PV (thực tế 28,8 nghìn PV 1-24/11). ChatGPT chiếm 96,8%, Gemini 2,3%, Perplexity 1,0%. Click to App đạt 5,24% trên phiên (T10 đến 08/11), ngang Direct (5,52%) và cao hơn Organic (2,96%).
- **Tìm kiếm chuyển từ từ khóa sang khám phá bằng AI theo ý định.** Nội dung tĩnh, thiếu chiều sâu mất lượt nhấp; công cụ tương tác và dữ liệu thời gian thực được Google lẫn AI engine ưu tiên trích dẫn.

**Xu hướng 1-2 năm: tìm kiếm theo mục tiêu và hành trình**

- Google AI Mode tách một câu hỏi thành nhiều câu hỏi phụ, mỗi câu một ý định riêng (query fan-out, theo Aleyda Solis).
- Theo SEOClarity, nguồn AI trích dẫn có thể không trùng kết quả đứng đầu. Web cần phủ nhiều câu hỏi phụ của một chủ đề, cùng logic với việc thiết kế hành trình nhiều bước thay vì một trang đơn lẻ.

### 2.4. Install và MAU

**New Users: phễu cài đặt và đăng ký từ Web**

Lũy kế từ T7 đến 24/11/2026: **44.684 lượt cài đặt (Install)** (T7: 5.239; T8: 10.041; T9: 10.501; T10: 11.143; T11 MTD 1-24/11: 7.760) → **14.735 đăng ký (33,0%; T10 đạt 35,0%)** → **8.934 liên kết ngân hàng (60,6% trên đăng ký; 20,0% trên Install)** → **5.093 MAU (57,0% trên liên kết ngân hàng; 11,4% trên Install)**. T11 MTD ghi nhận đăng ký 30,3%, liên kết ngân hàng 63,9% và MAU 11,8% trên Install.

- Banner Chào MoMo toàn Web mang về 8.517 lượt, chiếm 76% cài đặt T10. Cinema Hub đóng góp 1.931 lượt (17%), tỷ lệ đăng ký sang liên kết ngân hàng 25,1%. Tăng trưởng cài đặt phụ thuộc lớn vào một cơ chế.
- Phễu T10: cài đặt sang đăng ký 3.902 (35,0%), bước rớt lớn nhất; đăng ký sang liên kết ngân hàng 2.389 (61,2%), cao nhất từ đầu năm; liên kết ngân hàng sang MAU 1.284 (khoảng 54%). Tổng từ cài đặt đến MAU 11,5%.
- iOS chiếm 51% lượt cài đặt nhưng 57% người liên kết ngân hàng và 59% MAU T10.
- **Kết luận:** người cài từ banner (76% Install T10) chưa dùng Utility nào nên vào App không có lý do để đăng ký (35,0% Install đăng ký). Người đến từ Utility đã có việc cần làm tiếp; đây là nhóm cần đo riêng và ưu tiên.

### 2.5. Cinema

**Cinema Hub.** Baseline Traffic lớn nhất (9,10M PV, T1-T10), và là dự án có vấn đề chuyển đổi cần xử lý sớm nhất (hơn 90% bỏ dở ở bước thanh toán).

| Tháng | Impression (Google Search) | PV Cinema Hub | Vé | Giao dịch | GMV (tỷ đ) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| T1/2026 | 10.988.973 | 581.349 | 12.643 | 5.889 | 1,21 |
| T2/2026 (Tết) | 14.875.825 | 1.044.429 | 28.379 | 12.432 | 2,55 |
| T3/2026 | 11.505.959 | 759.142 | 20.600 | 9.881 | 2,03 |
| T4/2026 | 11.164.473 | 851.919 | 18.730 | 8.221 | 1,69 |
| T5/2026 | 12.779.934 | 994.719 | 12.561 | 5.777 | 1,18 |
| T6/2026 | 12.659.436 | 859.183 | 19.444 | 9.055 | 1,86 |
| T7/2026 | 13.009.013 | 822.859 | 5.211 | 2.425 | 0,50 |
| T8/2026 | 12.784.452 | 832.460 | 8.754 | 4.016 | 0,82 |
| T9/2026 | 11.288.422 | 1.220.075 | 20.983 | 9.807 | 2,01 |
| T10/2026 | 10.951.659 | 1.132.721 | 26.789 | 12.547 | 2,57 |
| **Lũy kế 10 tháng (cộng từng tháng)** | **122.008.146** | **9.098.856** | **174.094** | **80.050** | **16,01 (AOV 200k) / 16,41 (thực tế)** |

- Lũy kế T1-T10: 174.094 vé và 80.050 giao dịch. GMV chuẩn 16,01 tỷ đ theo AOV quy chuẩn 200.000 đ/giao dịch; GMV thực tế đối soát 16,41 tỷ đ (AOV khoảng 205.000 đ). T11 đạt thêm 1,01M PV (1-24/11), mục tiêu T1,29M; mục tiêu T12 là 1,50M.
- Tỷ lệ quy đổi chuẩn dùng cho kế hoạch 2027: **8,8 giao dịch trên 1.000 PV** (tỷ lệ PV sang giao dịch 0,88%), AOV quy chuẩn **200.000 đ/giao dịch** (~2,17 vé/giao dịch).
- T9 đạt 1.220.075 PV, cao hơn mục tiêu 1,12M khoảng 9%.
- **Kết luận:** người xem lịch chiếu đã có ý định cao nhất, nhưng khi chuyển sang App để thanh toán thì mất suất chiếu và ghế đã chọn, phải làm lại từ đầu, và hơn 90% bỏ dở. Đây là điểm rơi có giá trị lớn nhất của toàn Web.

### 2.6. Financial

**Financial Hub.** Dự án chiến lược cốt lõi với bộ Utility tài chính. Utility có CTR 33,7-43,8% là yếu tố thu hút user, trong khi nhóm Tích lũy và Đầu tư còn thiếu Utility (Tiết kiệm 1,5K PV, Chứng chỉ quỹ 458 PV).

- **Traffic T10:** 273.705 PV (+9,6% so với T9), đạt 109,5% mục tiêu 250.000 PV. Trung Tâm Tài Chính và Tiện ích Tỷ giá đạt 43.495 PV (+442,0%), Ví Trả Sau đạt 58.268 PV (+38,2%), bù mức giảm 47.814 PV của Vay Nhanh (-43,5%).
- **Utility tạo tương tác:** CTR T10 của Ước tính khoản vay là 43,8%, Tra cứu CIC 38,6%, Tính lương Gross-Net 33,7%; ba Utility này chiếm 87,4% lượt tương tác của Hub (7.100 trên 8.120 lượt). Bảng tĩnh giá vàng, tỷ giá, lãi suất đạt 0% CTR.
- **Utility đã triển khai:** Tính lương Gross-Net, Tỷ giá, Giá vàng (từ T9), Chứng chỉ quỹ, Ước tính khoản vay, Tra cứu điểm CIC, Trả góp Ví Trả Sau, Lãi tiết kiệm, Chuyển đổi ngoại tệ, BHXH và lương hưu. Đang triển khai: Phân bổ lương 50/30/20, Tính thuế TNCN và Thuế Hộ Kinh Doanh, Gamification Điểm Tín Dụng CIC (T11).
- **Phục hồi T11 sau tái cấu trúc PLG từ T8:** PageView Non-Paid 1-19/11 đạt 294,5 nghìn, tăng 105% so với cùng kỳ T10 (143,4 nghìn). Trong 1-20/11, Financial đạt 4,36M Impression trên Google Search (21,3% tổng momo.vn) và 5,77M Impression trên AI Overview (18/5-20/11, 25,7% toàn Website). Click to App theo user T11: Điểm Tín Dụng 80,4%, Vay Nhanh 65,0%, Ví Trả Sau 29,0%, Trung Tâm Tài Chính 5,4%.
- **Hướng 2027:** đạt 1M PV mỗi tháng cần gấp khoảng 3,7 lần T10. Năm 2027 chuẩn hóa UX Framework và Microjourney cho từng Utility tài chính.

### 2.7. Vehicle Hub

**Vehicle Hub.** Phạt Nguội là Pioneer Project đã xác nhận trong H1/2026, làm nền để khởi động Vehicle Hub cùng VTTI và Insurtech. Thị trường 23,2 triệu lượt tìm kiếm mỗi tháng (Giá xăng 10,52 triệu, Phạt Nguội 6,58 triệu, ETC 1,31 triệu, Trạm sạc EV 1,24 triệu).

- **Phạt Nguội phục hồi:** CTR 24,3% và 660 trích dẫn từ AI trong 28 ngày đầu; 1-15/11 đạt 88.160 PVs, tỷ lệ mở App 69,5% (run rate khoảng 176 nghìn PVs/tháng). T9 giảm do API Phạt Nguội gián đoạn 01/09-20/09.
- **Cụm liên quan tăng:** Bảo hiểm ô tô từ 11.885 PV (T5) lên 25.502 PV (T10); Tiện ích giao thông từ 5 PV (T8) lên 20.425 PV (T10).
- **Kết luận:** người tra Phạt Nguội là chủ xe, nhóm có nhu cầu bảo hiểm xe, nhưng năm 2026 hai cụm chạy tách nhau và chưa có Offer nối từ trang tra cứu sang báo giá.

### 2.8. Potential Intent Search

**InsurTech (bảo hiểm), 01/01-12/11/2026.** Web mang về 136.819 user bảo hiểm, tăng 32% so với cả năm 2025. 44-51% người mua bảo hiểm trên Web chưa có ví MoMo.

| Sản phẩm | Traffic Web | So với 2025 | Kết quả từ Web | Đầu tư SEO + SEM |
| :--- | :---: | :---: | :---: | :---: |
| Bảo hiểm ô tô (thân vỏ) | 162.304 | +46% | 2.118 leads, 71 giao dịch (khoảng 462 triệu đ GMV) | 1,05 tỷ đ |
| Bảo hiểm xe máy | 90.522 | -52% | 1.750 người mua (289 triệu đ GMV, -11% YoY); 1.948 giao dịch về App | 350 triệu đ |
| BHYT | 196.198 | Gấp 4,4 lần | 2.643 người mua, **2,67 tỷ đ GMV (+65% YoY)** | 150 triệu đ |

- Bảo hiểm ô tô: lead sang giao dịch 3,3%, thấp hơn mục tiêu 7-10%.
- Bảo hiểm xe máy: traffic năm nay bằng 48% cả năm 2025 dù 10/10 từ khóa mục tiêu trong top 10.
- **Kết luận:** BHYT có chi phí SEO và SEM thấp nhất (khoảng 57.000 đ mỗi người mua từ Web), nhưng sau khi mua chưa có bước tiếp theo đưa nhóm 44-51% chưa có ví vào App.

**Sản phẩm khác đóng góp GMV trên Web, T1-T10/2026 (đang thả tự nhiên, chưa có sự đầu tư của BU)**

| Sản phẩm | Chỉ số đến T10 | GMV | Ghi chú |
| :--- | :---: | :---: | :--- |
| Vé xe | 3.787 MAU giao dịch | 1,51 tỷ đ (ước tính) | Tính theo 3.787 MAU x AOV 400.000 đ |
| eSIM du lịch | 824 giao dịch | 160,4 triệu đ | Tỷ lệ chuyển đổi 3,18%; không có chi phí quảng cáo |

### 2.9. Điểm rơi 2026 và nguyên tắc 2027

Năm 2026 cho thấy giá trị bị mất ở bảy điểm, từ Traffic đến đăng ký trong App:

| Điểm rơi | Số liệu | Nguyên nhân |
| :--- | :--- | :--- |
| Organic tăng chậm | +5,7% so với T9 (T10), thấp hơn Non-Paid tổng (+13,5%) | AI Search trả lời trực tiếp nội dung kiến thức chung |
| Bảng tĩnh không điều hướng user đi tiếp | Giá vàng, tỷ giá, lãi suất: CTR 0% | Trang chỉ hiển thị số, không có Utility hay bước tiếp theo |
| Nhóm Tích lũy thiếu Utility | Tiết kiệm 1,5K PV, Chứng chỉ quỹ 458 PV | Chưa đủ Utility cho nhóm này |
| Các cụm sản phẩm chạy riêng | Phạt Nguội và Bảo hiểm xe | Chưa có Offer nối giữa các cụm |
| Cinema bỏ dở ở bước thanh toán | Trên 90% | Sang App thanh toán làm mất suất chiếu và ghế đã chọn trên Web |
| Bảo hiểm ô tô: lead không thành giao dịch | 3,3% (71 trên 2.118 lead), mục tiêu 7-10% | Luồng báo giá chưa tối ưu |
| Install không đăng ký | 35,0% đăng ký (T10), 65% không đăng ký | 76% Install từ một banner, user chưa có việc cần làm tiếp trong App |

**Nguyên tắc 2027**

- **Utility trước, nội dung sau, mỗi Utility có một Microjourney.** Utility điều hướng user sang việc kế tiếp, còn bảng tĩnh giá vàng, tỷ giá, lãi suất không có bước tiếp theo nên CTR là 0%. Mỗi Utility có một Offer gắn với ngữ cảnh của user.
- **Đầu tư SEO và GEO/AEO song song.** Organic tăng chậm hơn Non-Paid tổng khi AI trả lời trực tiếp, trong khi AI Traffic nhỏ nhưng chuyển đổi cao. Phạt Nguội là mẫu: 28 ngày theo đúng chiến lược từ khóa tạo Organic bền vững và 660 trích dẫn từ AI. llms.txt, Schema và Topical Authority áp dụng cho mọi cụm.
- **KPI theo vai trò.** Web Platform được đo bằng chất lượng lưu lượng Non-Paid từ Search & AI, đóng góp Install cho App và kết quả kinh doanh đồng sở hữu (Shared-KPI) với từng BU, thay vì số lượng tính năng đã giao.

---

## 3. 2027 DIRECTION

### 3.1. Objectives

| Cấp | Chỉ số | Baseline 2026 | KPI 2027 |
| :--- | :--- | :--- | :--- |
| **North Star Metric** | PageView Non-Paid | 32,77M (Forecast cả năm) | 40,00M (+22,1% YoY) |
| **Success Metric** (cùng BU) | GMV, DAU, MAU, MEU | Cinema 16,01 tỷ đ GMV (T1-T10); Bảo hiểm 2,67 tỷ đ GMV (BHYT) | BU và FinanceBP xác nhận |
| **Success Metric** | W2A CTR | 3,36% (T10) | 4,0-4,5% |
| **KPI** | Install mỗi tháng | 11.143 (T10) | 30.000 |

### 3.2. Overview

Năm 2027, Web làm bốn việc: thu hút đúng nhu cầu từ Google và AI, nối từng bước sang đúng Service trong App, đo đến kết quả, và đảm bảo vận hành ổn định cho mọi sản phẩm trên momo.vn.

**Nhu cầu tìm kiếm**

Nhu cầu đến từ Search Engine và AI Agent (Google, ChatGPT, Gemini, Perplexity), nơi user đã có ý định rõ. Utility và nội dung trả lời đúng nhu cầu đó là động cơ chính tạo ra Non-Paid Traffic bền vững mà không phụ thuộc ngân sách Paid; một số Utility tần suất cao như giá vàng, giá xăng dầu, tỷ giá còn giúp user chủ động quay lại Web.

**Bước nối sang App**

Web thu hút user, để user tự xử lý việc cần làm bằng Utility, rồi chuyển sang App bằng một Offer, giữ đúng ngữ cảnh từ Out-App đến In-App. App đảm nhận xác minh hoặc thanh toán. Bước nối giữa các Service được thiết kế theo bốn nhóm:

| Nhóm Service | Service | Bước nối 2027 |
| :--- | :--- | :--- |
| Anchors (kéo user, tạo thói quen sử dụng) | Phạt Nguội, Vé Số, Chứng Khoán, Chứng Chỉ Quỹ | Phạt Nguội sang báo giá Bảo hiểm xe |
| Connective (dữ liệu user sở hữu, tăng mức độ gắn bó) | Tra cứu CIC | Điểm CIC tốt sang hạn mức Ví Trả Sau; Ước tính khoản vay sang Vay Nhanh với số tiền đã nhập |
| Adjacent (đi sâu hành trình user đã làm) | Cinema, Bảo hiểm, Ví Trả Sau, Tích lũy | Cinema mở App đúng bước thanh toán, giữ suất chiếu và ghế; Tính lương, lãi suất sang Túi Thần Tài |
| Monetization (biến phân phối rẻ thành lợi nhuận) | Vé xe, eSIM du lịch, Vay Nhanh | eSIM, Vé xe: Offer cài App cho chuyến sau |

Các bước nối 2027 được xây sau khi BU xác nhận khả thi về sản phẩm, dữ liệu và pháp lý.

Bốn nguyên tắc thiết kế mỗi bước nối:

- **Mỗi Microjourney chỉ có một Offer,** đặt đúng lúc user vừa có kết quả và gọi đúng việc đang làm, ví dụ "Kiểm tra hạn mức với điểm CIC này" thay cho "Tải App".
- **Điều hướng bắt đầu từ việc user vừa làm,** không bắt đầu từ sản phẩm MoMo muốn bán.
- **Mỗi trang có ba khối:** trả lời câu hỏi (đủ rõ để Google và AI trích dẫn), Utility để user tự kiểm tra trường hợp của mình, và một Offer duy nhất. Trang chỉ có khối đầu, như bảng tĩnh giá vàng, tỷ giá, lãi suất (CTR 0%), không chuyển được user nào.
- **Tối ưu Conversion giữa các bước, không chỉ tăng Traffic.** Install sang đăng ký đạt 33,0% (T7-T11), và hơn 90% người chọn ghế Cinema bỏ dở ở bước thanh toán.

**Trust đi xuyên suốt từng sản phẩm trên Web:** Đây là điều kiện tiên quyết để AI Agent trích dẫn và để user yên tâm chuyển sang App. Tùy theo đặc thù từng nhóm sản phẩm (như Tài chính/Tín dụng cần minh bạch pháp lý YMYL và giấy phép đối tác; Bảo hiểm, Vé và Thanh toán cần chứng nhận an toàn thông tin và bảo vệ giao dịch), Web chuẩn hóa giấy phép theo từng Service, chứng nhận an toàn thông tin và kênh Báo cáo lừa đảo ẩn danh. Kênh Báo cáo lừa đảo đã có; trang tổng hợp giấy phép và pháp lý triển khai theo từng Service cùng Legal.

**Kết quả đo lường**

Web chịu trách nhiệm PageView Non-Paid, Click to App và Install; các chỉ số sau cài đặt và doanh thu (GMV, DAU, MAU, MEU) cùng chịu trách nhiệm với BU. Mọi điểm chạm trên Web đều gắn OneLink riêng theo từng Utility và Service để đo đóng góp thực tế cho từng BU:

| BU | Service | Giá trị Web mang lại |
| :--- | :--- | :--- |
| Movies | Cinema | Traffic và GMV |
| Financial Services | Ví Trả Sau, Vay Nhanh, Túi Thần Tài, Tiết kiệm, Chứng chỉ quỹ và các sản phẩm của FinHub | Traffic và Click to App |
| InsurTech | Bảo hiểm xe, bảo hiểm y tế | Traffic và GMV |
| User Growth (New User) | Cài App, đăng ký | Install và đăng ký |

**Vận hành ổn định**

Web Platform chịu trách nhiệm hiệu suất, hạ tầng, kỹ thuật và công nghệ của mọi sản phẩm trên momo.vn, kể cả sản phẩm do Cell Team tự sở hữu. Mục tiêu 2027: uptime từ 99,9%, Core Web Vitals đạt ngưỡng (LCP dưới 2,5 giây, INP dưới 200ms, CLS dưới 0,1), 20 Cell Teams được hỗ trợ trong đó 15 trở lên tự vận hành.

**Các sản phẩm tự nhiên (Potential Market) và nhóm Anchor mở rộng**

Ngoài các sản phẩm, dịch vụ đã được xây dựng, Web theo dõi thêm các thị trường có quy mô tìm kiếm lớn (potential sizing) đóng vai trò **Anchor** nhờ tần suất sử dụng cao để thu hút user mới, tạo thói quen quay lại và dẫn sang dịch vụ liền kề (**Anchor -> Adjacent**): gồm nhóm đang có GMV tự nhiên trên Web (chưa cam kết chỉ tiêu) và nhóm Anchor mới mở rộng trong năm 2027.

| Nhóm | Vai trò | Search Demand | Hướng 2027 hoặc kết quả Web 2026 |
| :--- | :--- | :--- | :--- |
| Bảo hiểm y tế | Anchor -> Adjacent | 1,42 triệu, SoV MoMo 0% | 2,67 tỷ đ GMV (+65% YoY) |
| Vé xe khách | Anchor -> Adjacent | 2,12 triệu | 1,51 tỷ đ GMV (ước tính) |
| Bảo hiểm xe máy | Anchor -> Adjacent | 58.810, SoV MoMo 38% | 289 triệu đ GMV (-11% YoY) |
| eSIM | Anchor -> Adjacent | 1,87 triệu (SIM số đẹp và eSIM) | 160,4 triệu đ GMV, 824 giao dịch |
| Bảo hiểm ô tô | Anchor -> Adjacent | 74.000 (vật chất), SoV MoMo 0% | 2.118 lead, 71 giao dịch |
| Bảo hiểm xã hội | Anchor -> Adjacent | 938.090 | Sắp ra mắt |
| Mua vé Tàu | Anchor -> Adjacent | - | Sắp ra mắt |
| Vé Số | Anchor | 1,54 tỷ lượt tìm kiếm | Cổng Vé Số tại momo.vn/ve-so theo mô hình Utility-Led: tra cứu kết quả, dò vé, rồi điều hướng sang App |
| Chứng Khoán | Anchor | 2,66 triệu, SoV MoMo 0% | Chuyên trang Chứng Khoán và 30 trang mã VN30; Utility giả lập tích sản cổ phiếu, CTA mở App |
| Chứng Chỉ Quỹ | Anchor | 19,2 nghìn | Trang Chứng Chỉ Quỹ với 30 quỹ mở đối tác, đầu tư định kỳ từ 10.000đ/ngày; cấp OneLink riêng theo Utility để đo Click to App (hiện dưới 15 Click to App mỗi dự án) |


### 3.3. Strategic

**Tổng thể, Web là kênh điều hướng (Navigation) đưa user đến các Anchor, và từ Anchor dẫn dắt user tải hoặc mở App.** Năm 2027, Web là kênh Nurture user chưa có App từ nhu cầu tìm kiếm: thu hút Non-Paid Traffic từ Search Engine và AI Agent, thiết kế Microjourney trên Utility để điều hướng user sang đúng Service trong App, giữ đúng ngữ cảnh từ Out-App đến In-App. Chiến lược này đi qua năm trụ cột: SEO / GEO / AEO, MoSpark 2.0, New User Acquisition, Security và Shared Product.

**Tiêu chí lựa chọn bài toán triển khai năm 2027:** Không chỉ ưu tiên các nhu cầu có **dung lượng tìm kiếm lớn (High Volume)** để mở rộng độ phủ, Web lựa chọn song song theo **khung Microjourney** nhằm dẫn lưu lượng **đúng chất lượng và đúng nhu cầu (qualified & relevant)** về đúng Service trong App hoặc chuyển đổi thành **Install**, tránh chạy theo lượng truy cập lớn nhưng không tạo giá trị cho hệ sinh thái.

### 3.4. Portfolio

Danh mục đầu tư năm 2027 tập trung vào ba nhóm dự án trọng tâm có bước nối trực tiếp vào doanh thu App (Cinema, CIC & Tín dụng, Tích lũy & Đầu tư), kết hợp mở rộng các điểm chạm chuyển đổi Install mới trên luồng Utility.

**Ngoài phạm vi trọng tâm 2027.** Ví Trả Sau và Vay Nhanh không nằm trong ba dự án trọng tâm vì hai dự án này thuộc Inbound do BMC chịu trách nhiệm, Web Platform không can thiệp.

**Khoảng trống điều hướng user.** Giữ nguyên nhịp T10/2026 (11.143 lượt/tháng), cả năm 2027 chỉ đạt khoảng 134 nghìn Install. Để đạt 30.000/tháng, bên cạnh nguồn banner hiện có, Web cần mở rộng thêm nguồn Install mới từ các luồng Utility thông qua Ads Manager (đặt Offer đúng lúc trong luồng) và Deferred Deep Linking.

**Thị trường và trọng tâm đầu tư:**

- **Quy mô thị trường:** 214,4 triệu lượt/tháng ở 5 nhóm ngành (Google Keyword Planner, Semrush); Tài chính 122,97 triệu.
- **Ngân sách 2027 tập trung vào CIC, vay và tích lũy (khoảng 9,4 triệu lượt/tháng)** thay vì giá vàng và tỷ giá, vì các nhóm này có bước tiếp theo điều hướng thẳng vào sản phẩm tạo doanh thu. Giá vàng và tỷ giá là lựa chọn có chủ đích: cụm Tỷ giá đang triển khai theo mô hình pSEO từ 2026 và nằm trong phần tăng trưởng không ngân sách.

**Điều kiện từ BU:**

- Movies BU và Financial Services BU chia sẻ lịch phim, lộ trình sản phẩm và thay đổi chính sách trước 2-4 tuần.
- Financial Services BU cung cấp chỉ số trên App (GMV, MAU, MEU) và đối soát qua Dashboard dùng chung.

### 3.5. Allocation

**Bảng phân bổ mục tiêu 40,00M PVs Non-Paid 2027 theo 3 dự án trọng tâm và phần nền:**

| Nhóm dự án / Nguồn | Mục tiêu 2027 (M PVs) | Tỷ trọng trên 40,00M | Ghi chú |
| :--- | :---: | :---: | :--- |
| **Cinema Hub** | **12,6 - 14,0M** | 31,5 - 35,0% | Hub có GMV vé; BU Movies |
| **CIC & Tín dụng** | **2,2 - 2,5M** | 5,5 - 6,3% | Tín dụng; BU Financial Services |
| **Financial: Tích lũy & Đầu tư** | **1,0 - 1,5M** | 2,5 - 3,8% | Túi Thần Tài, Tiết kiệm, CCQ; BU Financial Services |
| **Dự án khác & nội dung nền** | **22,0 - 24,2M** | 55,0 - 60,5% | Giữ ổn định trên nền ~23,0M năm 2026 (Vehicle Hub, New User, Tỷ giá, eSIM, Cell Teams, Bảo hiểm) |
| **Tổng Non-Paid 2027** | **40,00M** | **100%** | Tổng Web gồm Paid 7,92M (giữ như 2026 do BU quyết định) = **47,92M PVs** |

Mục tiêu PV giả định Paid giữ nguyên mức 2026 (7,92M, khoảng 0,66M mỗi tháng); toàn bộ mức tăng còn lại đến từ Non-Paid. Lộ trình từng tháng:

| Tháng | Tổng PV 2026 (triệu) | Tổng PV 2027 (triệu) | Chênh lệch YoY | Paid 2027 (triệu) | Non-Paid 2027 (triệu) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| T1 | 2,59 | 3,66 | +1,07 (+41,3%) | 0,66 | 3,00 |
| T2 | 3,46 | 3,71 | +0,25 (+7,2%) | 0,66 | 3,05 |
| T3 | 3,21 | 3,76 | +0,55 (+17,1%) | 0,66 | 3,10 |
| T4 | 2,69 | 3,81 | +1,12 (+41,6%) | 0,66 | 3,15 |
| T5 | 3,27 | 3,88 | +0,61 (+18,7%) | 0,66 | 3,22 |
| T6 | 3,41 | 3,96 | +0,55 (+16,1%) | 0,66 | 3,30 |
| T7 | 3,17 | 4,01 | +0,84 (+26,5%) | 0,66 | 3,35 |
| T8 | 3,47 | 4,08 | +0,61 (+17,6%) | 0,66 | 3,42 |
| T9 | 3,95 | 4,16 | +0,21 (+5,3%) | 0,66 | 3,50 |
| T10 | 3,60 | 4,24 | +0,64 (+17,8%) | 0,66 | 3,58 |
| T11 | 3,94 *(MTD 1-24/11)* | 4,29 | +0,35 (+8,9%) | 0,66 | 3,63 |
| T12 | 4,00 *(Forecast)* | 4,36 | +0,36 (+9,0%) | 0,66 | 3,70 |
| **Cả năm** | **40,69** *(Forecast)* | **47,92** | **+7,23 (+17,8%)** | **7,92** | **40,00** |

- So với 2026 (Forecast cả năm: tổng 40,69M, Paid 7,92M, Non-Paid 32,77M), KPI 2027 giúp tổng PVs tăng +17,8% (47,92M) và Non-Paid tăng +7,23M (+22,1% YoY).
- Non-Paid đặt theo tốc độ tăng trưởng, không theo tỷ trọng, vì Paid do BU quyết định và không thuộc cam kết của Web Platform.

**Sáu chỉ số hỗ trợ KPI chính.** Ngoài PageView Non-Paid và Install, Web theo dõi sáu chỉ số cho biết từng khâu trong hành trình đang ở đâu và cần đạt gì vào năm 2027.

| Chỉ số | Hiện tại | KPI 2027 | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| Install sang đăng ký | 33,0% (T7-T11); 35,0% (T10) | 40-45% | User cài App mà chưa đăng ký thì chưa dùng được Service; cần tách nguồn banner và nguồn Utility để đo riêng |
| Install từ nguồn ngoài banner (Utility & Offer) | 2.626 (T10) | 15.000-20.000/tháng | Mở rộng nguồn Install mới bên cạnh banner hiện có thông qua Ads Manager và Offer theo ngữ cảnh |
| PageView từ AI mỗi tháng | 18.547 (T10); 28,8 nghìn (1-24/11) | 46.000 bình quân mỗi tháng (khoảng 551 nghìn cả năm) | AI Traffic còn nhỏ nhưng Click to App ngang Direct |
| PageView CIC và Tích lũy | 0,63M (T1-T10, gồm CIC 0,42M và Tích lũy, Đầu tư 0,21M) | 3,2-4,0M cả năm | Hai nhóm có ngân sách đầu tư riêng; Web cam kết Traffic và Click to App, MAU do BU xác nhận khi có dữ liệu |
| Cell Teams được hỗ trợ | 16 (6 tự vận hành) | 20 (15 trở lên tự vận hành) | Số Cell Teams tự xuất bản trên MoSpark mà không cần Dev |
| Strategic Hubs đang hoạt động | 3 (Cinema, Vehicle, Financial) | 5 trở lên | Mở rộng Vé số, Chứng khoán, Chứng chỉ quỹ theo điều kiện |

**Cơ sở tăng trưởng có ngân sách: 100% mức tăng Non-Paid đến từ các dự án trọng tâm**

Ba dự án có ngân sách đóng góp thêm 6,1-8,3M PV, khớp trọn vẹn với mức tăng +7,23M PV Non-Paid của năm 2027 (32,77M lên 40,00M); phần nội dung nền (~23,0M PV) chỉ cần giữ ổn định như 2026. Các dự án Anchor mới (Vé số, Chứng khoán, Chứng chỉ quỹ) nếu mở rộng thành công sẽ tạo dư địa vượt mục tiêu.

- **Phụ trách:** Web Platform và Out-App Traffic, rà soát hằng tuần.

### 3.6. Pillar Objectives

#### Pillar 1: SEO / GEO / AEO cho các Strategic Project
*Objective:* mở rộng lưu lượng Non-Paid chất lượng cao (qualified & relevant) cho các Strategic Project thông qua kết hợp Utility-Led SEO và GEO/AEO (On-page lẫn Off-page), giữ vững đà tăng trưởng tự nhiên trước xu hướng Zero-Click Search.

**Dự án trọng tâm.** SEO và GEO/AEO tập trung vào ba dự án:

| Dự án | PVs 2027 | Tỷ trọng Non-Paid 2027 | Mục tiêu thứ hạng |
| :--- | :--- | :--- | :--- |
| Cinema Hub | 12,6-14,0M | 31,5-35,0% | Top 1-3 cụm mua vé, rạp, phim mới |
| CIC và Tín dụng | 2,2-2,5M | 5,5-6,3% | Top 3-5 cụm CIC, nợ xấu, điểm tín dụng |
| Tích lũy và Đầu tư | 1,0-1,5M | 2,5-3,8% | Top 3-5 cụm lãi suất, tiết kiệm, CCQ, tích sản |

**Dự án Anchor (chưa cam kết thứ hạng Top 1).** Phạt Nguội (tham chiếu 2,1-2,5M PVs; team chủ động chọn vì vai trò **Anchor** thu hút nhóm chủ xe và dẫn sang bảo hiểm xe, chưa cam kết Top 1), cùng Vé Số, Chứng Khoán và Chứng Chỉ Quỹ (triển khai sau khi BU xác nhận khả thi về sản phẩm và pháp lý).

**Bảo hiểm.** Giữ luồng mua BHYT và tối ưu báo giá Bảo hiểm ô tô, nâng tỷ lệ lead sang giao dịch từ 3,3% lên 7-10%, chờ định hướng chung của công ty.

**Phần nền ngoài dự án trọng tâm.** 22,0-24,2M PV, chiếm 55,0-60,5% Non-Paid 2027, giữ ổn định trên nền khoảng 23,0M của 2026; đến từ Vehicle Hub, New User, Tỷ giá, eSIM, Cell Teams và Bảo hiểm. Phần này cần được duy trì thứ hạng, không để Traffic giảm khi AI Search trả lời trực tiếp.

Các đòn bẩy tăng trưởng của hạng mục này:

1. **Phủ cụm từ khóa theo Search Demand và SoV.** Mỗi dự án có bản đồ cụm từ khóa ưu tiên theo Search Demand và SoV của MoMo. Ngưỡng SoV: trên 40% là Market Leader, 20-40% trung bình, dưới 20% là khoảng trống lớn cần đầu tư.
2. **Xử lý các URL kém hiệu quả.** Rà soát định kỳ và xử lý theo bốn mức: Nofollow và gỡ khỏi Sitemap, 308 Redirect, 410 Gone, cập nhật nội dung.
3. **Chất lượng kỹ thuật là điều kiện xuất bản.** Core Web Vitals đạt ngưỡng (LCP dưới 2,5 giây, INP dưới 200ms, CLS dưới 0,1) và mục tiêu index 80% sau 30 ngày.
4. **E-E-A-T cho nội dung tài chính (YMYL).** Foundation Checklist là điều kiện bắt buộc trước khi xuất bản, kể cả nội dung của Inbound và Agency; chính sách tác giả có tên cho nội dung tài chính.
5. **GEO/AEO cho mọi dự án (kết hợp On-page và chủ động Off-page).** Chuẩn hóa Schema.org, llms.txt và trang minh bạch pháp lý YMYL, đồng thời **chủ động triển khai Off-page** (Digital PR, xây dựng Entity và mở rộng trích dẫn từ báo chí, nguồn uy tín bên ngoài) để cả Google Search và AI Agent ưu tiên trích dẫn momo.vn. Mục tiêu: AI Traffic 46.000 PV bình quân mỗi tháng. Mỗi hạng mục pilot một quý với KPI rõ: đạt ngưỡng thì mở rộng, không đạt thì dừng.

**Đo bằng:** PV Non-Paid theo dự án, thứ hạng cụm từ khóa mục tiêu, AI Traffic 46.000 PV mỗi tháng, tỷ lệ index sau 30 ngày.

#### Pillar 2: MoSpark 2.0
MoSpark cung cấp công cụ sản xuất và quản trị nội dung cho các Cell Team.

*Objective:* Cell Teams tự dựng Landing Page cho Utility và chiến dịch trong 1-2 ngày; mở rộng nguồn Install mới từ Offer trong luồng qua Ads Manager; W2A CTR trên các trang Utility từ 4,5%, cao hơn mức toàn Web; GenAI Content tự phục vụ trong vài phút cho Cell Teams.

1. **GenAI Content Pipeline và AI Quality Gate.** Mở rộng cho toàn bộ Cell Teams tự phục vụ trong vài phút. AI Quality Gate chấm điểm độ chính xác thông tin, E-E-A-T và chống trùng lặp trước khi xuất bản. Ngoài viết mới, pipeline có năng lực Content Refreshness: phát hiện bài cũ, đề xuất và tự cập nhật số liệu, nội dung theo mùa để giữ Organic.
2. **Product-Led Growth (PLG).** Nâng số Hub chiến lược từ 3 lên 5 trở lên trên PLG Project Engine của MoSpark; scale Hub có Traffic tốt, thử tiếp phần còn lại. Ngoài quản lý Content Strategy cho từng Hub, PLG Project Engine đo performance nội dung theo bài (PV, CTR, Click to App) và đề xuất chỉnh sửa bài kém hiệu quả.
3. **Utility-Led SEO.** Xây bộ mẫu pSEO (calculator, comparison, tra cứu theo ngân hàng, quận, phương tiện) trên MoSpark, thay các bảng tĩnh có CTR 0% bằng Utility. Mỗi Utility điều hướng user sang use case tiếp theo theo Microjourney, ví dụ Tra cứu CIC sang Ví Trả Sau, Ước tính khoản vay sang Vay Nhanh.
4. **Landing Page Builder (Scale và Integrate).** Mở rộng thư viện template cho Utility và chiến dịch, cho phép nhúng Utility và quiz vào trang, AI-assisted generation, A/B Testing ngay trên Builder, Variant fan-out và Multi-tenant để nhiều Cell Teams cùng dùng. Mỗi trang gắn một KPI rõ ràng. Success metrics: Time-to-launch dưới 1-2 ngày, Self-serve rate, tỷ lệ trang gắn KPI.
5. **Auto Internal Link.** Nền tảng tự đề xuất và chèn liên kết nội bộ giữa các trang cùng cụm, và từ trang Utility sang nội dung liên quan, để Cell Teams không phải gắn tay. Ưu tiên cụm Phạt Nguội, vốn cần liên kết nội bộ để phục hồi Traffic.
6. **Ads Manager.** Quản lý Offer ngay trong MoSpark: mỗi luồng tối đa một Offer, đặt sau khi user có kết quả, luôn bỏ qua được, giữ đúng ngữ cảnh từ Out-App đến In-App qua OneLink để tăng thêm nguồn Install mới bên cạnh banner. Tách chiến dịch theo ba trạng thái: chưa cài App, đã cài chưa đăng ký, đã đăng ký chưa liên kết ngân hàng. Ads Manager đa dạng định dạng quảng cáo (Balloon Ads, banner, thẻ quà theo intent) và có tính năng retargeting ads.
7. **Utility Tracking và Chatbot.** Chuẩn hóa tham số cho 100% liên kết OneLink vào BigQuery, cấp OneLink riêng cho từng Microjourney để đo Web to App theo từng Service trong App, mở rộng Umami cho toàn bộ Mini Web và đối soát với GA4 hằng tháng. Chatbot và RAG Knowledge Base mở rộng trợ lý tư vấn Service trên Web.
8. **Identify (SSO): Gamification và New User Nurturing.** Gamification kế thừa chiến dịch Game Một Mùa Quýt, triển khai Gamification Điểm Tín Dụng CIC sau khi Pháp lý xác nhận khung giấy phép. New User Nurturing dựa trên Identity Platform đã chạy Production.

#### Pillar 3: New User Acquisition
*Objective:* tăng Install từ Web lên 30.000 mỗi tháng và tối ưu funnel từ Install đến đăng ký, liên kết ngân hàng và MAU, cùng New User (User Growth).

1. **Mở rộng điểm chạm Install trên các luồng Utility.** Cộng thêm nguồn Install mới bên cạnh banner bằng Offer theo Microjourney (đặt đúng lúc user có kết quả) và Ads Balloon hiển thị thẻ quà đúng intent từng trang.
2. **Mở App đúng kết quả.** Deferred Deep Linking qua OneLink mở App vào đúng kết quả user vừa tra trên Web (CIC, Ước tính khoản vay), không bắt nhập lại.
3. **Tối ưu Install sang đăng ký.** Nâng từ 33,0% lên 40-45%; thử Gamification hoặc quà tự chọn để giữ người cài; tách nguồn banner và nguồn Utility để đo riêng.
4. **Đo funnel đến MAU theo nguồn.** Identity Platform nối hành vi Web sang App, đo Install, đăng ký, liên kết ngân hàng và MAU theo từng nguồn và Utility. New User chịu trách nhiệm chính với tỷ lệ liên kết ngân hàng trên Install.

#### Pillar 4: Security
*Objective:* đóng cổng truy cập public vào dữ liệu và không còn lỗ hổng mức CRITICAL được xác nhận độc lập, đạt chuẩn ITC Security trước mỗi lần Go-live.

1. **Truy vấn dữ liệu qua BFF.** Toàn bộ Web chuyển sang lớp BFF, đóng cổng public Supabase sau khi ITC Security Team duyệt Pentest API.
2. **Vá lỗ hổng còn mở.** Kế hoạch vá 68 lỗ hổng của MoMo API theo ba đợt, ưu tiên các route public; quét lại độc lập để xác nhận kết quả, vì số liệu hiện tại dựa trên đọc mã nguồn.
3. **Quản lý khóa bí mật.** Chuyển các khóa bí mật khỏi mã nguồn sang K8s Secret kèm đổi khóa.
4. **Security duyệt trước Go-live.** Mọi kết nối và Utility mới có Security duyệt trước khi mở, rút ra từ sự cố Pentest ngày 27/10.
5. **Zero-PII.** Utility và Offer không thu thập thông tin định danh cá nhân; BotID chặn bot spam trên Lead Form.

#### Pillar 5: Shared Product
*Objective:* cung cấp nền tảng dùng chung cho **20 Cell Teams** (15+ đội tự xuất bản trên MoSpark), rút ngắn thời gian Go-to-Market ra end-user xuống 1-2 ngày, chuẩn hóa **Branding và Design System MoBase V2** trên toàn Web, duy trì uptime từ 99,9%.

1. **Nền tảng dùng chung giúp Cell Teams Go-to-Market nhanh ra end-user.** Cung cấp hạ tầng sẵn sàng, thừa hưởng Domain Authority của `momo.vn`, tích hợp sẵn Tracking Full Funnel và OneLink để 20 Cell Teams (HR với MoMo Talent `momo.career`, L&D, BMC, GMC, MDS, CVS News duy trì 100% Smoke Test chuẩn ITC) tự xuất bản Webview In/Out App và Landing Page ra người dùng cuối mà không cần Dev thủ công.
2. **Công cụ quản lý chuẩn Branding và Design System (MoBase V2).** BMC quản trị tập trung Brand Guideline ngay trên nền tảng; chuẩn hóa toàn bộ giao diện theo **MoBase V2** kết hợp quy trình **Design-to-Code** và **Code-to-Design**, đảm bảo mọi sản phẩm trên Web đồng bộ nhận diện thương hiệu, trải nghiệm người dùng và đạt chuẩn Core Web Vitals trước khi Go-live.
3. **Bộ thành phần kỹ thuật dùng chung (Shared Components).** Payment Component, Lead Form (gắn BotID), JSON Form Builder và lớp bảo mật BFF tích hợp sẵn, giúp mọi đội tái sử dụng ngay và tuân thủ 100% chuẩn ITC Security.

### 3.7. Budget

**Ngân sách:** 1.995.800.000 đ, khoảng 166,3 triệu đ mỗi tháng, gồm 1,95 tỷ đ cho 3 dự án và 45,8 triệu đ bản quyền công cụ. Không đề xuất ngân sách Paid. Ngân sách Cinema và Financial có phần đồng tài trợ từ BU, tỷ lệ thống nhất với từng BU trước khi giải ngân.

| Dự án | Ngân sách | PV 2026 (T1-T10) | PV 2027 | PV tăng thêm | Thứ hạng mục tiêu |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Cinema Hub** | 620 triệu đ | 9,10M | 12,6 - 14,0M | 3,5 - 4,9M | Top 1-3 cụm mua vé, rạp, phim mới |
| **Financial - CIC & Tín dụng** | 480 triệu đ | 0,42M | 2,2 - 2,5M | 1,8 - 2,1M | Top 3-5 cụm CIC, nợ xấu, điểm tín dụng |
| **Financial - Tích lũy & Đầu tư** | 850 triệu đ | 0,21M | 1,0 - 1,5M | 0,8 - 1,3M | Top 3-5 cụm lãi suất, tiết kiệm, CCQ, tích sản |
| **Bản quyền công cụ** (Figma Pro 9,8 triệu đ, 2 users; Semrush Pro 36 triệu đ, 1 user) | 45,8 triệu đ |  |  |  |  |
| **Tổng** | **1.995,8 triệu đ (~1,996 tỷ đ)** | **9,73M** | **15,8 - 18,0M** | **6,1 - 8,3M** |  |

Chuyển đổi cuối phễu khác nhau theo use case: Cinema đo bằng giao dịch và GMV; Financial đo bằng lượt click App, MAU/MEU và chỉ số sản phẩm do BU định nghĩa. Đây là chỉ số chất lượng traffic, đồng chịu trách nhiệm với BU.

---

## 4. CONCLUSION

Năm 2026, Web Platform xây xong nền tảng gồm MoSpark, GenAI Content, Utility-Led SEO, Tracking Full Funnel, Payment và OneLink, và đưa Non-Paid lên 29,09M PV, 79% Traffic Web. Điểm nghẽn nằm ở chuyển đổi: 76% Install đến từ một banner, chỉ 35,0% Install đăng ký (T10), và hơn 90% người chọn ghế Cinema bỏ dở ở bước thanh toán.

Năm 2027, Web là kênh Nurture user chưa có App từ nhu cầu tìm kiếm. KPI 2027 là 40,00M PageView Non-Paid (+22,1% YoY), W2A CTR 4,0-4,5% và 30.000 Install mỗi tháng; GMV, DAU, MAU, MEU cùng chịu trách nhiệm với BU.

Để đạt KPI này, Web cần:

- **Đầu tư song song SEO và GEO/AEO,** xây Utility cho mỗi Hub với một Microjourney và một Offer.
- **Triển khai năm Pillar:** SEO / GEO / AEO, MoSpark 2.0, New User Acquisition, Security và Shared Product.
- **Giữ vận hành ổn định** cho mọi sản phẩm trên momo.vn, kể cả sản phẩm do Cell Team tự sở hữu: uptime từ 99,9%, Core Web Vitals đạt ngưỡng.
- **Ngân sách 1,996 tỷ đ** cho ba dự án Cinema, CIC và Tín dụng, Tích lũy và Đầu tư, cùng việc BU xác nhận bước nối và chỉ số kinh doanh trước khi xây.
