# 📝 NHẬT KÝ BIÊN BẢN HỌP & RECAP CHIẾN LƯỢC (MEETING RECAPS)
> **File hiện hành: MEETING RECAPS Q4/2026 (10/2026 - nay).**
> Archive các quý trước: `MEETING_RECAPS_2026-Q3.md` (và các file `MEETING_RECAPS_<year>-Q<quarter>.md` khi được tách).
> Khi cần chiến lược cũ hơn Q4, đọc đúng file archive theo quý thay vì file này.

---


Tài liệu này lưu trữ toàn bộ thông tin quan trọng từ các buổi thảo luận, họp chiến lược và định hướng sản phẩm của **Web Platform**.
AI Agent (Antigravity) sẽ **luôn đọc file này** trước khi thực hiện các tác vụ phân tích, lập kế hoạch, viết PRD hoặc chuẩn bị báo cáo.

---

## DANH SÁCH BẢN GHI RECAPS

### Bản ghi ngày 11/11/2026: Chuẩn Hóa Cấu Trúc Kênh Lưu Lượng Sheet Overall Performance & Hệ Thống Báo Cáo
> **Thành phần:** Web Product Lead x Senior Engineering Lead x AI Agent (Antigravity)
> **Mục tiêu:** Thống nhất chuẩn hóa cấu trúc bóc tách kênh lưu lượng (Rows 9-22) trên Google Sheets SSOT (`Overall Performance`), file Excel nội bộ (`web_performance_tracking.xlsx`) và toàn bộ tài liệu báo cáo điều hành.

#### 1. Bối Cảnh & Quyết Định Tái Cấu Trúc Kênh
* **Hiện trạng cũ:** Kênh Paid bị kẹp giữa Organic và Direct ở dòng 10; dòng 20 chỉ tính tỷ trọng Non-Paid mà không có khối lượng; kênh truy cập từ các công cụ AI (GEO) bị gom lẫn trong nhóm Others.
* **Quyết định chuẩn hóa mới:**
  * **Tách riêng 2 khối độc lập:** **Paid** (Lưu lượng trả phí Marketing) và **Non-Paid** (Lưu lượng tự nhiên cốt lõi).
  * **Nhóm Non-Paid gồm 4 kênh chính:**
    1. **Organic:** Tìm kiếm tự nhiên Google / Cốc Cốc.
    2. **Direct:** Người dùng gõ trực tiếp URL / Bookmark / quay lại trực tiếp.
    3. **AI Traffic:** Khai mở kênh lưu lượng tìm kiếm AI (ChatGPT, Perplexity, Gemini, Claude, Copilot) trích xuất trực tiếp từ GA4 API.
    4. **Referral:** Gộp toàn bộ "Phần còn lại" (đối tác PR, liên kết ngoài, mạng xã hội tự nhiên, Unassigned) vào Referral để bảng gọn gàng, mạch lạc.
  * **Cân bằng toán học 100.0%:**
    * Dòng 5 (`Total page views Actual`) tính bằng `=Paid + Non-Paid` (`=K9+K10`, `=L9+L10`, `=U9+U10`...), tuyệt đối không cộng trùng.
    * Tổng `%Paid + %Non-Paid = 100.0%`; tổng 4 kênh con Non-Paid khớp 100% với dòng Non-Paid.

#### 2. Dữ Liệu Thực Tế Sau Khi Chuẩn Hóa (Tháng 10 Full & Tháng 11 MTD 10 Ngày)
* **Tháng 10/2026 (Full 31 Ngày - 3.602.023 PVs):**
  * **Paid:** 473.481 PVs (13.1%)
  * **Non-Paid:** 3.128.542 PVs (86.9%)
    * Organic: 1.715.771 PVs (47.6%)
    * Direct: 931.731 PVs (25.9%)
    * AI Traffic: 18.164 PVs (0.5%)
    * Referral *(gộp Phần còn lại)*: 462.876 PVs (12.9%)
* **Tháng 11/2026 (MTD 10 Ngày - 1.189.033 PVs):**
  * **Paid:** 210.398 PVs (17.7%)
  * **Non-Paid:** 978.635 PVs (82.3%)
    * Organic: 566.163 PVs (47.6%)
    * Direct: 298.140 PVs (25.1%)
    * AI Traffic: 9.212 PVs (0.8%)
    * Referral *(gộp Phần còn lại)*: 105.120 PVs (8.8%)

#### 3. Trạng Thái Triển Khai & Kiểm Tra An Toàn
* **Google Sheets SSOT:** Sheet `Overall Performance` đã cập nhật cấu trúc dòng 9-22, dòng Notes chuyển về dòng 23. Quét tự động dải cột B-V: **0 lỗi `#REF!`, `#VALUE!`, `#NAME?`, `#DIV/0!`**.
* **Excel SSOT:** Tệp [`07_REPORTS/web_performance_tracking.xlsx`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/web_performance_tracking.xlsx) đã đồng bộ 100% công thức và dữ liệu.
* **Tài liệu điều hành:** Đã cập nhật snapshot tại [`07_REPORTS/docs/PERFORMANCE_SNAPSHOT_LATEST.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/PERFORMANCE_SNAPSHOT_LATEST.md) và [`07_REPORTS/docs/report-thang-11-2026-board.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/report-thang-11-2026-board.md).
### Bản ghi ngày 30/10/2026: Cập Nhật Vận Hành Đa Dự Án - Staging Game Bò Sữa Bay & Legal TnC, Thuế TNCN & Content Financial, Tool Khấu Trừ & Quiz BH Thân Vỏ, Xử Lý Sự Cố Bảo Mật Merchant Page
> **Thành phần:** Web Product Lead x Strategic Project Teams (Cinema, Financial, Vehicle) x Platform Security Team  
> **Mục tiêu:** Cập nhật tiến độ Staging và yêu cầu pháp lý (Legal TnC) cho Game Bò Sữa Bay, tiến độ triển khai trang Thuế TNCN và nhịp Always-on Content mảng Tài chính, nghiên cứu Quiz và Tool Khấu Trừ cho Xe / Bảo hiểm Thân vỏ, cùng phương án ứng phó sự cố rò rỉ dữ liệu Merchant.

#### 1. Strategic Projects
- **Cinema Hub:**
  - **Game Bò Sữa Bay:** Đã chính thức đẩy lên môi trường Staging; hoàn tất tích hợp API từ `m.momo.vn/cinema` phụ trách việc quản lý Gmail và tự động cấp mã code định danh cho người chơi để phục vụ xuất danh sách Leaderboard.
  - **Rà Soát Pháp Lý (Legal & Compliance):** Điều khoản và Điều kiện (TnC) cần được Legal review gấp, làm rõ mục đích thu thập và sử dụng Gmail (Data User) nhằm phục vụ các hoạt động hợp lệ: xác thực người chơi, đối soát trao thưởng, gửi mã ưu đãi/vé xem phim và truyền thông hợp lệ.
  - **Go-Live Chính Thức Cụm Trang Diễn Viên (`/cinema/person`):** Đã chính thức Go-live Production trang danh mục Diễn Viên & Đạo Diễn tại URL `/cinema/person` (kèm các trang hồ sơ chi tiết `/cinema/person/[slug]`). Cấu trúc trang hỗ trợ bộ lọc Diễn viên / Đạo diễn, liên kết mạng lưới phim tham gia, tiểu sử và tối ưu Schema thực thể `Person` chuẩn E-E-A-T để đón đầu các đợt tìm kiếm dàn cast phim chiếu rạp.
- **Financial Hub:**
  - **Công Cụ & Trang Tính Thuế Thu Nhập Cá Nhân (`/tai-chinh/thue-thu-nhap-ca-nhan`):**
    - Quy chuẩn URL: **Tuyệt đối không viết tắt URL**, chuẩn hóa thành `/tai-chinh/thue-thu-nhap-ca-nhan` (thay vì `/tai-chinh/thue-tncn`, đồng bộ đối xứng với `/tai-chinh/thue-ho-kinh-doanh`).
    - Tiến độ: Kỹ sư Frontend đang hoàn thiện giao diện trang và tiện ích tính toán theo biểu lũy tiến hiện hành và đề xuất luật mới. Cần cấu hình redirect 301 từ URL cũ nếu đã từng phát sinh link.
  - **Cỗ Máy Nội Dung (Content Engine):** Duy trì nhịp sản xuất và xuất bản Blog Content đều đặn với tốc độ 5 bài/ngày chuẩn E-E-A-T.
- **Vehicle Hub (Bảo Hiểm & Tiện Ích Xe):**
  - **Tool Khấu Trừ Bảo Hiểm:** Bắt đầu khởi động xây dựng công cụ tính mức khấu trừ và khấu hao vật chất xe.
  - **Nghiên Cứu Quiz Bảo Hiểm Thân Vỏ Ô Tô (VCX):**
    - Nghiên cứu mô hình Gamification Quiz tương tự mô hình CIC theo tài liệu thiết kế prototype `/Users/hienhv/Downloads/Bước Khó Nhất BH Thân Vỏ.html`.
    - Concept: "Thử thách dự đoán bước ngốn thời gian nhất khi mua bảo hiểm thân vỏ" (3 câu hỏi ngắn gọn, định vị kim đồng hồ xe hơi sang trọng, so sánh trực diện quy trình Ngoài kia vs. Trên MoMo, kết quả dự báo thời gian hoàn tất cá nhân hóa và mở khóa Voucher ưu đãi lần đầu dẫn deeplink về app).

#### 2. Platform & Core Operations
- **Go-Live Chính Thức Trang Tải Ứng Dụng (`/tai-app`):**
  - Kỹ sư Thuận đã hoàn thành nghiệm thu và chính thức đưa trang `/tai-app` lên Production.
  - Vận hành trọn vẹn cơ chế Smart Device Routing: tự động nhận diện thiết bị (iOS mở trực tiếp Apple App Store, Android mở Google Play Store, Desktop hiển thị QR Code động để quét tải app ngay lập tức) kèm Smart Fallback và gắn attribution OneLink AppsFlyer chuẩn xác.
  - Đây là cổng chuyển đổi tập trung Web-to-App tối quan trọng hỗ trợ trực tiếp cho mục tiêu **30.000 install trong Quý 4/2026** từ kênh Web theo chỉ đạo của CEO anh Tường.
- **Xử Lý Sự Cố An Toàn Thông Tin (Security Vulnerability):**
  - Đội ngũ Kỹ sư Nền tảng (Platform Security) đang khẩn trương điều tra và xử lý triệt để lỗ hổng rò rỉ dữ liệu tên Merchant trên hệ thống trang Đối tác/Merchant Page.
  - Hướng xử lý: Thu hồi API public bộc lộ thông tin nhạy cảm, thiết lập lại phân quyền và che chắn dữ liệu (masking/BFF proxy) để ngăn chặn hành vi scraping hàng loạt từ bên ngoài.

---

### Bản ghi ngày 29/10/2026: Họp Định Kỳ Bi-Weekly Với Lãnh Đạo - Chuẩn Hóa Tư Duy Trình Bày Số Liệu (Pyramid Principle), Phê Duyệt Pilot Off-Page Cinema & Định Hướng Năng Lực Đội Ngũ
> **Thành phần:** Ban Giám Đốc x Web Product Lead x Web Engineering Team  
> **Mục tiêu:** Rút kinh nghiệm phương pháp báo cáo và tư duy dữ liệu theo chuẩn Minto Pyramid; định nghĩa rõ ràng mục tiêu thành công (Definition of Success) cho dự án Pilot Off-Page; phê duyệt cơ chế triển khai thử nghiệm Cinema Hub và Financial Hub.

#### 1. Chuẩn Hóa Tư Duy Lập Luận Dữ Liệu & Báo Cáo Cấp Quản Lý (Minto Pyramid Principle)
- **Tư Duy Báo Cáo Hướng Tác Động (Impact-Driven & Action Title):**
  - Mạch suy nghĩ của người làm kỹ thuật thường đi xuôi: Bối cảnh -> Vấn đề -> Giải pháp -> Kết quả. Mạch tiếp nhận của Lãnh đạo đi ngược lại: **Tác động (Impact) là gì? -> Làm cái gì để ra được tác động đó? -> Bước tiếp theo (Next Steps) là gì?**
  - Tiêu đề từng slide (Action Title) phải là kết luận chốt chặn mang tính đóng khung (Frame the mindset), ví dụ: *"Financial Hub: Đã bắt đầu triển khai, ghi nhận tín hiệu ban đầu tích cực, traffic organic x4 lần đạt 27.000 clicks"*. Phần thân slide chỉ đóng vai trò làm bằng chứng (Evidence) đối soát.
  - Tránh tuyệt đối việc đẩy người nghe vào quá trình tự phán đoán hay giải quyết vấn đề khi chưa đưa ra kết luận.
- **Kỷ Luật Ngôn Ngữ & Độ Chính Xác Của Số Liệu:**
  - Tuyệt đối không dùng các từ cảm tính, mơ hồ vô giá trị trong báo cáo: *"tăng trưởng tốt"*, *"ổn định"*, *"bình thường"*.
  - Định lượng rõ ràng: Tăng 1% là đi ngang; tăng 10% là bình thường; tăng từ 20% trở lên mới được xem là tốt.
  - Phân định rõ bản chất tăng trưởng: Khi base ban đầu bằng 0 hoặc chưa triển khai gì (như Financial Hub giai đoạn đầu), việc đạt 27.000 traffic là do *"bắt đầu đầu tư và ghi nhận kết quả ban đầu"*, không dùng từ *"tăng trưởng"* để tránh ngộ nhận.
- **Đo Lường Giá Trị Biên (Counterfactual & Marginal Impact):**
  - Mọi sáng kiến triển khai phải trả lời được bài toán phản thực tế: *"Nếu không làm gì thì chỉ số sẽ tụt bao nhiêu?"* và *"Hành động này đóng góp thêm chính xác bao nhiêu kết quả so với mức cơ sở (baseline)?"*.
  - Chấm dứt thói quen làm theo trực giác (gut feeling). Mọi nỗ lực giải quyết vấn đề của người dùng phải quy đổi được ra giá trị kinh doanh cụ thể.

#### 2. Phê Duyệt Dự Án Pilot Off-Page SEO (Cinema Hub & Financial Hub)
- **Khung Dự Án:** Thử nghiệm trong 3 tháng (đến hết tháng 01/2027) với ngân sách 125 triệu VNĐ cho Cinema Hub; tiếp nối mở rộng cho mảng Financial Services (Thẻ tín dụng / CAC) với ngân sách BU tài trợ dự kiến 80 - 100 triệu VNĐ.
- **Định Nghĩa Thành Công (Definition of Success):**
  - **Mục Tiêu Cốt Lõi (Primary Target - Theo Tiêu Chí Của BU):** Tập trung vào **Thứ hạng Từ khóa (Search Ranking)** đưa các trang cụm phim chiếu rạp đạt mức trung bình Top 5.5 trên Google Search và tối đa hóa hiện diện trên Generative Engine Optimization (GEO / AI Overview). Đây là tiêu chí BU ưu tiên vì năng lực traffic in-app của BU đã rất lớn và nhu cầu chính là xây dựng thương hiệu (Branding) ngoài app.
  - **Mục Tiêu Nền Tảng (Secondary / Platform Target):** Đóng vai trò là chỉ số vệ sinh (Hygiene metric) theo dõi độ uy tín (Authority / Trust) và lưu lượng Organic Traffic của toàn Website.
- **Hiệu Quả Kinh Tế So Với Thuê Ngoài (In-House Direct vs. Agency):**
  - Triển khai trực tiếp với mạng lưới đối tác giúp tiết kiệm chi phí trung gian (agency thường đội giá từ 175 - 200 triệu VNĐ cho cùng khối lượng).
  - Khác với Paid Ads (ngừng chi tiền là mất toàn bộ traffic), giá trị của Off-Page xây dựng uy tín bền vững (Evergreen Authority) cho các trang trụ cột, duy trì giá trị tích lũy dài hạn.

#### 3. Phát Triển Năng Lực Đội Ngũ & Kế Hoạch Tuyển Dụng
- **Phê Duyệt Tuyển Dụng:** Đồng ý tuyển dụng Cộng tác viên / Nhân sự triển khai Off-Page trong 2 - 3 tháng. Yêu cầu tuyển nhanh để kịp nhịp phim bom tấn và mùa phim Tết.
- **Nguyên Tắc Trực Tiếp Làm Chủ Năng Lực (Skin In The Game):**
  - Đội ngũ Web Platform không được có tâm lý né tránh hoặc tự giới hạn đây không phải năng lực cốt lõi (Core Competency) để đẩy việc cho người khác.
  - Phải trực tiếp tham gia cùng nhân sự mới: tự học quy trình, trực tiếp thẩm định bài viết, kiểm soát tiêu chuẩn chất lượng và chịu trách nhiệm đến cùng về kết quả kinh doanh.
  - Coi khoản ngân sách thử nghiệm là chi phí đầu tư mở rộng vùng năng lực, rèn luyện sự tự tin và tư duy làm chủ (Ownership) cho đội ngũ.

---

### Bản ghi ngày 29/10/2026: Hoàn Tất Đồng Bộ GA4 & GSC Về MoSpark Datamart - Nền Tảng Cho Chuỗi Tasks Phân Tích & AI
> **Thành phần:** Fullstack/Data Engineering Team x Web Product Lead  
> **Mục tiêu:** Ghi nhận mốc hoàn tất việc kết nối và đồng bộ tự động dữ liệu Google Analytics 4 (GA4) và Google Search Console (GSC) về MoSpark Datamart; chuẩn bị triển khai chuỗi nhiệm vụ khai thác dữ liệu, Growth Dashboard và AI.

#### 1. Hiện Trạng Hạ Tầng Dữ Liệu Đã Hoàn Thành
- Toàn bộ pipeline kỹ thuật đồng bộ dữ liệu GA4 (Sessions, Non-Paid vs. Paid, Engagement, OneLink W2A) và GSC (Impressions, Clicks, Average Position, CTR, Search Queries) đã được tích hợp thành công vào MoSpark Datamart.
- MoSpark chính thức trở thành Single Source of Truth (SSOT) cho toàn bộ bức tranh tăng trưởng Web Platform, chấm dứt việc đối soát và kéo số thủ công.

#### 2. Định Hướng Chuỗi Nhiệm Vụ Tiếp Theo (Upcoming Tasks Pipeline)
- **Tích Hợp LLM Nội Bộ (Qwen 3.5):**
  - Cắm trực tiếp Qwen 3.5 vào MoSpark Datamart để chạy tính năng tự động phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA Engine) cho các báo cáo WBR/MBR.
  - Tự động sinh báo cáo điều hành (Executive Summary) định kỳ.
- **Hệ Thống Cảnh Báo Dị Biệt (Automated Anomaly Detection):**
  - Xây dựng module tự động phát hiện sớm đứt gãy phễu chuyển đổi Web-to-App, sụt giảm traffic đột biến hoặc hiện tượng ăn thịt từ khóa (Cannibalization).
- **Phát Triển MoSpark Growth Dashboard Cho PM/PO:**
  - Thiết kế các widget trực quan hóa dữ liệu hiệu suất MTD theo từng Hub/Theme.
  - Xây dựng tính năng Self-Service cho PM/PO tra cứu Quick Wins (Impressions cao, CTR thấp) và cơ cấu nguồn lưu lượng.
- **Tối Ưu Hóa Content Studio:**
  - Đẩy dữ liệu search query thực tế từ GSC vào gợi ý dàn ý bài viết và tự động đề xuất tối ưu Title/Meta Description cho các bài viết chuẩn SEO/GEO.

---

### Bản ghi ngày 28/10/2026: Định Hướng Trọng Tâm Hành Động Tuần 44 - Cinema (Bò Sữa Bay TVC & Trang Diễn Viên), Financial (Thuế, CCQ Phase 1, CIC Duolingo), Vehicle (Nộp Phạt CSGT) & Platform (Security API Public, PLG UI/UX Viết Bài)
> **Thành phần:** Web Product Lead x Cell Team Leads x Web Engineering Team  
> **Mục tiêu:** Chốt danh mục hành động cần làm trước cho Tuần 44 trên các mặt trận Cinema, Financial, Vehicle và Nền tảng Platform (Security, PLG).

#### 1. Cinema Hub
- **Game Bò Sữa Bay (`/cinema/bo-sua-bay-25058`):** Yêu cầu kỹ thuật cao nhất: game phải tuyệt đối ổn định, zero-crash, tối ưu bundle và chịu tải cao vì có kế hoạch phát sóng TVC tại các cụm rạp đối tác kèm mã QR Code cho khán giả quét chơi trực tiếp trên mobile.
- **Chiến dịch Seeding:** Đẩy mạnh seeding đa kênh trên mạng xã hội và cộng đồng yêu phim.
- **Go-Live Trang Diễn Viên:** Đưa cụm trang hồ sơ Diễn Viên (`/cinema/dien-vien/...`) lên Production chuẩn E-E-A-T.
- **Thúc đẩy Ranking Phim Hot Tháng 11:** Sản xuất nội dung và tối ưu SEO đón đầu loạt phim bom tấn chiếu rạp tháng 11/2026.

#### 2. Financial Hub
- **Xây dựng 2 Trang Cụm Thuế:** Tập trung hoàn thiện và đưa lên Production trang Tính Thuế TNCN (`/tai-chinh/thue-tncn`) và Thuế Hộ Kinh Doanh (`/tai-chinh/thue-ho-kinh-doanh`).
- **Chốt Trang Chứng Chỉ Quỹ (SIP) & Go-Live Phase 1:** Do hiện tại chưa có kết nối API NAV thời gian thực từ các Quỹ mở đối tác, chốt giải pháp Go-live Phase 1 sử dụng dữ liệu tĩnh/bán tự động (danh mục quỹ, tỷ suất sinh lời quá khứ, cơ chế đầu tư từ 10.000đ) kết nối phễu mở tài khoản in-app.
- **Build Blog Content (Always-on):** Duy trì và đẩy mạnh cỗ máy sản xuất bài viết tài chính E-E-A-T theo nhịp Always-on hàng tuần.
- **Nghiên Cứu UI Education Gamification Về CIC (Mô hình Duolingo):** Thiết kế ý tưởng/giao diện Gamification giáo dục tài chính về điểm tín dụng CIC dạng bài học tương tác mini (chia lộ trình từng cấp độ, câu hỏi tình huống trắc nghiệm, giữ chuỗi streak học tập hàng ngày, nhận huy hiệu/voucher), biến kiến thức tín dụng khô khan thành hành trình học tập lôi cuốn.

#### 3. Vehicle Hub
- **Go-Live Trang Nộp Phạt CSGT:** Đưa trang Nộp Phạt Giao Thông / CSGT lên Production kết nối trực tiếp từ cổng tra cứu phạt nguội (`/phat-nguoi`) sang thanh toán MoMo.

#### 4. Dự Án Platform (Security & PLG)
- **Security (An Toàn & Bảo Mật Nền Tảng):**
  - Rà soát toàn bộ các API Public của Web Platform.
  - Chuẩn hóa các sản phẩm/tiện ích đang dùng API Public trả dữ liệu về Client-Side: đánh giá rủi ro lộ dữ liệu, triển khai rate-limiting, xác thực CORS nghiêm ngặt hoặc chuyển đổi các dữ liệu nhạy cảm sang Server-Side API Proxy (BFF).
- **PLG (Product-Led Growth):**
  - Tái thiết kế toàn diện UI/UX giao diện Viết bài (Blog Editor / Content Creation Interface) trên MoSpark CMS: tinh gọn không gian viết, bố cục trực quan thanh công cụ, các khối SEO metadata, keyword cluster, hình ảnh và khối Key Takeaway, hỗ trợ xem trước đa thiết bị.

---

### Bản ghi ngày 28/10/2026: Hoàn Tất Đóng Gói API Công Ty (Model Qwen 3.5) Dùng Chung Đa Dự Án - Tích Hợp MoMo AI & MoSpark Growth Dashboard (GA4 & GSC Ingestion)
> **Thành phần:** AI Platform Team x Web Product Lead x Web Engineering Team x Data Team  
> **Mục tiêu:** Đồng bộ tiến độ đóng gói thư viện API nội bộ công ty (Company LLM Gateway SDK) với mô hình chủ lực Qwen 3.5; thống nhất kiến trúc tích hợp đa dự án Web Platform gồm MoMo AI (Proposal Engine) và MoSpark Growth Dashboard (kết nối dữ liệu GA4/GSC được đồng bộ tự động để phân tích RCA).

#### 1. Đóng Gói API Nội Bộ Công Ty (Company LLM Gateway SDK - Model Qwen 3.5)
- **Hạ Tầng & Xác Thực:**
  - Hoàn tất đóng gói SDK client (`@momo/llm-gateway-client`) kết nối trực tiếp vào cụm máy chủ LLM nội bộ của MoMo.
  - Chuẩn xác thực: Bearer JWT bảo mật cao, phân quyền theo mã dự án (`X-Project-Id`).
  - Lợi thế vượt trội: Không phát sinh chi phí token bên ngoài (zero commercial cost), bảo mật thông tin nội bộ 100%, kiểm soát độ trễ và không bị phụ thuộc vào hạn ngạch (rate limit) của các nhà cung cấp ngoại.
- **Mô Hình Chủ Lực:** Triển khai chính thức model **Qwen 3.5** (Instruct & Reasoning) tối ưu cho việc hiểu tiếng Việt, trích xuất dữ liệu có cấu trúc và lập luận logic.

#### 2. Kế Hoạch Tích Hợp Đa Dự Án Trên Web Platform
- **Dự Án 1: MoMo AI / Proposal Engine (Financial Hub & Công Cụ Tính Toán):**
  - Chuyển dịch từ mô hình thuần Rule-based sang **Kiến trúc Lai Đa Tầng (Hybrid Dual-Engine Architecture)**.
  - Tầng 1 (Client-Side Instant Heuristics, <10ms): Xử lý phản hồi tức thì khi người dùng kéo thanh trượt (slider) hoặc nhập số liệu cơ bản, hiển thị ngay nhận xét hóm hỉnh (Gentle / Roast Mode) và CTA tương ứng.
  - Tầng 2 (Deep Contextual Reasoning qua Qwen 3.5): Kích hoạt bất đồng bộ khi người dùng yêu cầu phân tích sâu hoặc đặt câu hỏi phức tạp. Qwen 3.5 phân tích cơ cấu tài chính, đối chiếu thu nhập - nợ và đưa ra phương án tối ưu hóa dòng tiền.
  - Cơ chế Graceful Fallback: Nếu API phản hồi chậm quá 2.5s hoặc mất kết nối, UI tự động giữ nguyên kết quả Tầng 1, không gián đoạn trải nghiệm.
- **Dự Án 2: MoSpark Growth Dashboard (Tiêu Thụ Dữ Liệu GA4 & GSC Đã Đồng Bộ):**
  - Khai thác nguồn dữ liệu hiệu suất Google Analytics 4 và Google Search Console đã được pipeline kỹ thuật đồng bộ tự động về MoSpark Datamart.
  - Qwen 3.5 được kết nối để tự động:
    1. Sinh bản tin tóm tắt điều hành định kỳ (Executive Summaries) cho WBR/MBR.
    2. Chẩn đoán nguyên nhân gốc rễ (Root Cause Analysis - RCA) khi phát hiện biến động traffic hoặc sụt giảm kênh Non-Paid / Paid.
    3. Tự động cảnh báo dị biệt (Anomaly Detection) về đứt gãy luồng chuyển đổi Onelink Web-to-App.
    4. Tự động đề xuất danh mục hành động theo thứ tự triển khai cho các Squad chuyên môn.
- **Dự Án 3: MoSpark Content Studio (Sinh Nội Dung Theo Cấu Trúc):**
  - Cung cấp tiêu đề H1/H2/H3 và ngữ cảnh thực tế của sản phẩm cho Qwen 3.5 để tạo dàn ý và bài viết E-E-A-T chuẩn SEO/GEO.

#### 3. Action Items & Kế Hoạch Bàn Giao
- **AI Platform Team:** Triển khai API gateway endpoint và cấp phát JWT token môi trường Staging/Production cho nhánh Web Platform trước ngày 30/10/2026.
- **Web Frontend Team:** Tích hợp module `@momo/llm-gateway-client` vào component MoMo AI trên Financial Hub; gắn đầy đủ 6 sự kiện Umami tracking.
- **Data & Web Engineering Team:** Hoàn thiện pipeline cấp dữ liệu GA4/GSC từ MoSpark Datamart vào prompt template của Qwen 3.5 trên Growth Dashboard.
- **Legal Team:** Hoàn thiện văn bản rà soát tuân thủ và bộ lọc an toàn thông tin (Safety Guardrails) cho nội dung tài chính tự động.

---

### Bản ghi ngày 28/10/2026: Chiến Dịch Game Bò Sữa Bay (Cinema Hub) - Kế Hoạch Seeding, TVC Rạp & Điều Chỉnh Game Rules
> **Thành phần:** Web Product Lead x Cinema Team x Web Dev Team  
> **Mục tiêu:** Đồng bộ yêu cầu chiến dịch phát hành Game Bò Sữa Bay trên Cinema Hub, kế hoạch quảng bá đa kênh (Seeding, TVC rạp, Video diễn viên trải nghiệm) và quy chuẩn bộ Game Rules mới để kịp tiến độ bàn giao testing trước thứ Sáu (31/10/2026).

#### 1. Kế Hoạch Go-live & Chiến Dịch Truyền Thông (Marketing & Media)
- **Tiến Độ Bắt Buộc:** Phải hoàn thành và đẩy game lên môi trường Testing trước thứ Sáu (31/10/2026).
- **Kênh Quảng Bá & Phân Phối:**
  - Triển khai seeding trên các cộng đồng mạng xã hội.
  - Video Game sẽ được chiếu TVC tại các cụm rạp chiếu phim đối tác.
  - Sản xuất clip diễn viên/KOLs chơi thử game để tạo hiệu ứng lan tỏa (viral).

#### 2. Quy Chuẩn Bộ Game Rules Mới (Product & Logic Specs)
- **Cơ Chế Sinh Tồn (Survival / Endless Mode):**
  - **Máu (Lives):** Giảm số lượng máu xuống còn **2 mạng** (tối đa 2 lần va chạm chướng ngại vật).
  - **Thời Gian Chơi:** Bỏ giới hạn thời gian (Endless mode). Người dùng chơi liên tục cho đến khi hết 2 mạng thì Game Over.
  - **Cơ Chế Điểm Số:** Mỗi bình sữa thu thập được tính **1 điểm**.
  - **Độ Khó Thích Ứng (Dynamic Difficulty):** Càng chơi lâu, tốc độ di chuyển càng gia tăng và mật độ chướng ngại vật xuất hiện càng dày đặc để khống chế thời gian trung bình 1 session (khoảng 60 - 90 giây).
- **Cơ Chế Người Dùng & Bảng Xếp Hạng (Leaderboard):**
  - Cho phép người dùng chơi lại (Replay) không giới hạn số lần.
  - Mỗi người dùng được định danh bằng một mã code cố định hoặc Email/Gmail.
  - Bảng xếp hạng (Leaderboard) ghi nhận **Điểm số cao nhất (High Score)** của người dùng thay vì ghi đè điểm lần chơi cuối.
  - **Cơ chế trao quà:** Backend sẽ trực tiếp tổng hợp dữ liệu và xuất danh sách (Export Report) thứ hạng điểm cao nhất theo Gmail để team vận hành/Marketing tiến hành trao giải; Frontend không bắt buộc phải dựng giao diện Leaderboard công khai phức tạp.

#### 3. Điều Chỉnh Giao Diện & Vị Trí Hiển Thị (UI / Placements)
- **Vị Trí Nhúng Game:** Đặt trực tiếp ngay dưới Hero Section của trang bài viết/landing page `https://www.momo.vn/cinema/bo-sua-bay-25058`.
- **Kênh Kéo Traffic Nội Bộ:** Gắn Balloon Ads (Banner bóng bay nổi) trên trang chủ Cinema Hub (`/cinema`) trỏ thẳng về URL chơi game.
- **Chuẩn Hóa Nhãn Giao Diện (Copywriting):**
  - Màn hình kết quả: Đổi nhãn "Cỡ Bò" thành **"Điểm"** (hoặc "Số Điểm").
  - Màn hình thông tin/xác nhận: Đổi trường nhập "Tên Bò Của Bạn" thành **"Gmail / Email"** để phục vụ định danh và trao thưởng.

#### 4. Kế Hoạch Triển Khai Tiện Ích Financial Hub
- **Trang Quỹ Nhóm (`/tai-chinh/quy` - Phase 1):**
  - Triển khai Phase 1 tích hợp **Content chuẩn hóa** (nguyên tắc vận hành, minh bạch thu chi, E-E-A-T) kết hợp **Simulator Quỹ Nhóm** (công cụ mô phỏng phân bổ chi phí, tính tiền nộp định kỳ theo số lượng thành viên).
  - Phễu chuyển đổi Web-to-App: Dẫn luồng người dùng mở tính năng Quỹ Nhóm in-app trên MoMo (quản lý số dư, tự động nhắc nợ thành viên, sao kê minh bạch).
- **Phân Tách 2 URL Độc Lập Cho Cụm Công Cụ Tính Thuế:**
  - **Trang Tính Thuế TNCN (`/tai-chinh/thue-tncn`):** Phục vụ quyết toán thuế thu nhập cá nhân đa nguồn (lương công ty, vãng lai 10%, freelance), cập nhật biểu thuế lũy tiến hiện hành và đề xuất luật mới.
  - **Trang Tính Thuế Hộ Kinh Doanh (`/tai-chinh/thue-ho-kinh-doanh`):** Phục vụ hộ kinh doanh, cá nhân bán hàng online sàn TMĐT (Shopee, TikTok Shop), cho thuê tài sản theo Thông tư 40/2021 và Luật Thuế GTGT mới (ngưỡng 200 triệu đồng).
  - Định hướng kiến trúc: Tách biệt hoàn toàn 2 URL để tối ưu SEO Intent, chống cannibalization từ khóa, liên kết chéo qua thanh điều hướng chuyên biệt `TaxHubNav`.

---

### Bản ghi ngày 22/10/2026: GPD Monthly BOM Review Với CEO Anh Tường - Chiến Lược Web Platform, Target 30k Install Q4, Định Hướng Financial Hub, Micro Journey & Signal
> **Thời gian:** 22/10/2026 (95 phút)  
> **Thành phần tham dự:** Anh Tường (CEO/BOM), Anh Công, Chị Yên, Anh Bảo, Huy Lê, Tín, Tuyền.  
> **Mục tiêu:** Đánh giá kết quả Tháng 9/2026 các nhánh (Web Platform, Gamification, Tab Me, User Growth), đồng bộ mục tiêu Q4/2026 và định hướng chiến lược 2026 - 2027 từ CEO.

#### 1. Định Hướng & Mục Tiêu Trọng Yếu Dành Cho Web Platform
- **Vị Thế Kênh Web & Mục Tiêu New User (BOM Mandate):**
  - **Mục tiêu Q4/2026:** Nâng chỉ tiêu từ 20.000 lên **30.000 install ứng dụng từ nguồn Web**.
  - **Tầm nhìn 2026 - 2027:** Tiếp tục xây nền cho mốc **4.000.000 traffic/tháng** và kiểm soát nguồn traffic từ Internet.
  - **Trọng trách dài hạn:** Hiện kênh Web đóng góp chưa tới 10% tổng New User của MoMo. Khi đạt tỷ trọng tối thiểu 10% trên base ~500.000 New User/tháng (tương đương **30.000 - 50.000 New User/tháng**), Web sẽ chính thức trở thành một trục tăng trưởng độc lập, thuộc sở hữu bền vững (owned media), giảm phụ thuộc vào Paid Ads.
  - **Action Item:** Lập kế hoạch Web cho năm sau (kết hợp Traffic từ đội Web và Conversion từ thử nghiệm nhánh New User); bám sát mục tiêu 30.000 install Q4 (Phụ trách: Anh Bảo + Huy Lê; Thời hạn: Cuối năm 2026).
- **Chiến Lược 2 Dự Án Trọng Điểm:**
  - **Cinema Hub:** Khai thác tối đa lưu lượng theo mùa vụ phim chiếu rạp, trọng tâm chiến dịch phim Tết 2027 để kéo đỉnh traffic.
  - **Financial Hub (Xây dựng Financial Authority & Trust):**
    - Nhận định: Traffic hiện tại của Web phần lớn đến từ mảng giải trí, trong khi mảng tài chính còn mỏng cả về nội dung và lượng truy cập.
    - Hành động: Web Team phối hợp cùng BU Dịch vụ Tài chính xây dựng đồng bộ nội dung chuẩn chuyên gia và các tiện ích tính toán (utility tools), định hình lại navigation tổng thể để tạo dựng uy tín tài chính trên Web.
    - Cơ chế chuyển đổi: Nhúng trực tiếp các tiện ích tính toán (utility) vào sâu trong bài viết content để tăng tương tác và chuyển đổi người dùng sang ứng dụng MoMo.
- **Tiến Độ Kỹ Thuật Đang Triển Khai Tại Web Platform:**
  - **Trang Tải App (`/tai-app`):** Đã hoàn thành Staging cơ chế Smart Fallback và nhận diện thiết bị (iOS/Android/Desktop QR). Đang chuẩn bị nghiệm thu tracking và test cross-browser.
  - **Luồng Tìm Kiếm (`/tim-kiem`):** Đang hoàn tất Phase 1 (UI/UX thanh tìm kiếm, Instant Search Dropdown, Trending Keywords, Empty State).
  - **Hợp Tác Ngân Sách Off-page (Cinema & CIC):** Cinema Hub tài trợ tối đa 100 triệu VNĐ, Web Platform đồng tài trợ phần còn lại cùng SEO Vendor.
  - **Retargeting Onsite Bảo Hiểm Ô Tô (`/bao-hiem-o-to`):** Nhận diện người dùng quay lại đã xem báo giá để kích hoạt widget phục hồi giỏ hàng.
  - **Hạ Tầng LLM API Nội Bộ:** Kỹ sư Backend phối hợp thử nghiệm API LLM công ty tự huấn luyện + Qwen 3.5 thay thế dần API bên thứ ba.

#### 2. Các Chủ Đề Thảo Luận Chiến Lược Cấp Khối (Liên Đới Web Platform)
- **Financial Health Score (FHS):**
  - BOM định hướng FHS là sản phẩm của nền tảng (Platform), là cầu nối giữa Quản lý chi tiêu và Đầu tư.
  - Chuẩn hóa theo các trụ cột hành vi: **Spend Smart (Chi tiêu thông minh), Earn More (Gia tăng thu nhập), Invest Wisely (Đầu tư khôn ngoan)** và tích lũy/trả nợ.
  - Nguyên tắc cốt lõi: Đánh giá dựa trên hành vi thực tế thay vì con số tĩnh. Web Platform cần ứng dụng logic này vào các công cụ tính toán tài chính và bộ câu hỏi đánh giá nhanh (Quiz/Simulator) trên Web để phân loại nhu cầu và dẫn luồng vào app.
- **Signal Intelligence (Tư Duy Định Hướng Dữ Liệu Mới):**
  - Nguyên tắc từ CEO: Đi từ bài toán cần giải (Use Case kinh doanh) rồi mới truy ngược xem cần signal nào, tuyệt đối không đi từ dữ liệu đang có.
  - Web Platform là điểm chạm đầu tiên tiếp cận người dùng chưa định danh; dữ liệu tìm kiếm và hành vi dùng utility trên Web là signal giá trị cao để dự đoán nhu cầu tài chính trước khi người dùng tải app.
- **Micro Journey & Bài Toán Retention 93%:**
  - Lạm dụng Push Notification là triệu chứng của việc thiếu năng lực tạo thói quen (Habit). Nền tảng chỉ đạt Habit thực sự khi duy trì tăng trưởng mà không phụ thuộc vào việc đẩy Push liên tục.
  - Trọng tâm là tìm và tháo gỡ điểm nghẽn (bottleneck) tại các điểm rơi (drop-off points) trong hành trình người dùng (Connect -> Check -> Do).
- **Ứng Dụng AI (AI Adoption):**
  - Điểm nghẽn không nằm ở công nghệ mà ở thói quen sử dụng (xu hướng quay lại prompt rời rạc thay vì đi theo Agentic workflow).
  - Yêu cầu xây dựng Context Engineering bài bản và duy trì cơ chế Human-in-the-loop để kiểm duyệt chất lượng.
---

#### 3. Định Hướng Hạ Tầng LLM API Nội Bộ (Free Tier)
- **Tiến Độ:** Kỹ sư Backend và SEO Vendor đang phối hợp đồng bộ và test API LLM nội bộ (Mô hình công ty tự huấn luyện + Qwen 3.5).
- **Mục Tiêu:** Thay thế dần các API thương mại có tính phí (OpenAI, Gemini) cho các tính năng AI trên Web Platform nhằm tối ưu chi phí vận hành.
- **Phạm Vi Ứng Dụng:** MoMo AI gợi ý trên Utility Tools, RAG Knowledge Base, Tự động sinh Quiz cho bài viết Blog, cùng các tác vụ tối ưu SEO / GEO Direct Answers quy mô lớn.

---

### Bản ghi ngày 20/10/2026: Cập Nhật Shipment Financial Hub - Go-Live 4 Cặp Ngoại Tệ, On Demo CCQ, MoMo AI & Umami Tracking
> **Thành phần:** Web Product Lead x Web Platform Team x FS Team  
> **Mục tiêu:** Cập nhật các hạng mục đã hoàn thành và triển khai thực tế trên cụm sản phẩm Financial Hub.

#### 1. Các Sản Phẩm Đã Go-Live Chính Thức
- **Cụm Sub-page 4 Cặp Tiền Tệ Chủ Lực (AUD, EUR, USD, GBP sang VND):** Đã chính thức Go-live cụm trang chi tiết tỷ giá 4 cặp tiền tệ phổ biến nhất quy đổi sang VND, tích hợp công cụ quy đổi hai chiều, biểu đồ biến động và bảng so sánh tỷ giá đa ngân hàng theo thời gian thực.
- **Bảng Lãi Suất 40 Ngân Hàng & Tool Tính Tiền Lãi (`/tai-chinh/lai-suat`):** Đã Go-live phục vụ so sánh và tính toán lãi gửi tiết kiệm/tiền vay tối ưu.
- **Phân Bổ Lương 50/30/20 & Hũ Tài Chính (`/tai-chinh/phan-bo-luong`):** Đã Go-live, kết nối trực tiếp tính năng Hũ Chi Tiêu in-app.

#### 2. Các Sản Phẩm Đang On Demo / On UAT
- **Trang Chứng Chỉ Quỹ (`/tai-chinh/chung-chi-quy`):** Đã hoàn thiện và đưa lên môi trường Demo (On Demo), tích hợp bảng giá NAV các quỹ mở và simulator tích sản SIP.
- **Mega Menu Header Financial Hub (`/tai-chinh`):** Đang hoàn tất giai đoạn test UX co giãn thông minh sang Top Menu cố định khi điều hướng trang con.

#### 3. Năng Lực Nền Tảng & Trải Nghiệm Mới
- **Tích Hợp MoMo AI Gợi Ý Cho Utility Tools:** Đã tích hợp trợ lý MoMo AI với 2 chế độ (Mode): **Hài Hước** và **Nghiêm Túc**, đưa ra các lời khuyên tài chính cá nhân hóa và dí dỏm/chuyên nghiệp dựa trên kết quả tính toán của người dùng trên từng tiện ích.
- **Chuẩn Hóa & Hoàn Tất Tích Hợp Umami Tracking:** Đã tự động hóa việc gắn tracking Umami chi tiết cho từng Tool/Widget tài chính theo đúng chuẩn schema SSOT, bắt trọn toàn bộ hành vi nhập liệu, tính toán và tỷ lệ nhấp CTA chuyển đổi sang app.

---

### Bản ghi ngày 13/10/2026: Cập Nhật Tiến Độ Go-Live & On UAT Các Dự Án Financial Hub
> **Thành phần:** Web Product Lead x Web Development Team x FS Team  
> **Mục tiêu:** Cập nhật trạng thái Go-live, On UAT và thẩm định API kỹ thuật của hệ thống công cụ và tiện ích Financial Hub.

#### 1. Các Sản Phẩm Đã Go-Live Chính Thức
- **Bảng Lãi Suất 40 Ngân Hàng & Tool Tính Tiền Lãi (`/tai-chinh/lai-suat`):** Đã chính thức Go-live với 2 cấu phần cốt lõi: Bảng so sánh lãi suất tiền gửi/vay 40 ngân hàng thương mại và Tool tính tiền lãi gửi tiết kiệm theo số tiền người dùng tự nhập, tự động tính toán và hiển thị ngân hàng có lãi suất tối ưu nhất.
- **Phân Bổ Lương 50/30/20 & Hũ Tài Chính (`/tai-chinh/phan-bo-luong`):** Đã chính thức Go-live, hỗ trợ chia ngân sách tự động theo quy tắc 50/30/20 và mô hình 6 Hũ tài chính, kết nối tính năng Hũ Chi Tiêu in-app.

#### 2. Các Sản Phẩm Đang On UAT (Dự Kiến Go-Live Trong Tuần Này)
- **Hệ Thống Sub-page Tỷ Giá (5 Cặp Tiền Tệ Phổ Biến):** Đã on UAT các trang chi tiết cặp ngoại tệ lưu lượng lớn nhất (USD, EUR, JPY, GBP, CNY...) tích hợp công cụ quy đổi hai chiều, bảng tỷ giá đa ngân hàng và biểu đồ biến động; chốt kế hoạch Go-live trong tuần này.
- **Mega Menu Header Mới Trên Financial Hub (`/tai-chinh`):** Đã on UAT kiến trúc Mega Menu 4 trụ cột tài chính. Cơ chế điều hướng UX: Khi người dùng nhấp sang các trang con có menu chức năng riêng, Mega Menu chính sẽ tự động co lại thành Top Menu toàn cục cố định, đảm bảo trải nghiệm liền mạch không bị xung đột điều hướng. Chốt Go-live trong tuần này.

#### 3. Tiến Độ Kỹ Thuật Đang Thẩm Định (In Review)
- **API Lãi Suất Tiền Gửi Trên MoMo (`/tai-chinh/gui-tiet-kiem`):** Đang trong giai đoạn review kỹ thuật API lãi suất tiền gửi của các đối tác liên kết (Bản Việt, VPBank) với chính sách ưu đãi cộng thêm tới +0.2% lãi suất để chuẩn bị phát hành.
- **API Dữ Liệu Chứng Chỉ Quỹ (`/tai-chinh/chung-chi-quy`):** Đang review kết nối API dữ liệu giá NAV và tỷ suất sinh lời của các quỹ mở đối tác từ BU CVS, chuẩn bị dựng giao diện bảng giá và bộ giả lập tích sản SIP.

---

### Bản ghi ngày 10/10/2026: Tổng Hợp Đánh Giá Run-rate Target Tháng 10, Crawl Budget & Backlink Profile
> **Thành phần:** Web Product Lead x Web Analytics x GSC Data Export (10/10/2026)
> **Mục tiêu:** Tổng hợp 3 nguồn dữ liệu - Tracking MTD Tháng 10, GSC Crawl Stats, GSC Top Linking Sites - thành một đánh giá khả năng đạt Target tháng 10 và rủi ro chuyển tiếp cho Quý 4/2026.

#### 1. Run-rate Đạt Target Tháng 10 (MTD 9 Ngày: 01/10 - 09/10)

| Chỉ số | Giá trị |
| :--- | :---: |
| Target Tháng 10 | 3.665.607 PV |
| Lũy kế MTD 9 ngày | 903.977 PV (24,66% Target / 29,03% thời gian) |
| Daily pace hiện tại | 100.442 PV/ngày |
| Dự báo 31 ngày | 3.113.699 PV = **84,94% Target** (thiếu ~552K PV) |
| Pace yêu cầu 22 ngày còn lại | **125.529 PV/ngày (+25% so với pace hiện tại)** |
| So với pace Tháng 9 (131.692/ngày) | Thấp hơn 23,7% |

- **Nguyên nhân Gap là 2 kênh:** Paid co về 89,9% (39.903 -> 4.037 PV/ngày so với T9) và Referral -26%. Organic ngược lại **tăng +20,4%** (54.127 -> 65.181 PV/ngày), chiếm 64,89% traffic MTD.
- **Gap tập trung ở Hub:** Financial dự báo chỉ 33% Target (-301K), New User 25,5% (-223K), Student 1,6% (-98K), Vehicle 33,4% (-67K). Chỉ Cinema vượt (+232K).
- **3 Kịch bản:** Base (giữ pace) 84,9% / Target hit ~102% (cần Paid về 18-20K PV/ngày + Financial utilities bứt tốc) / Best ~110% (Paid full mức T9 + campaign 20/10, 11.11).

#### 2. Crawl Budget (GSC Crawl Stats: 12/07 - 06/10/2026 - 1.810.416 requests, Host "No problems")

| Tháng | Req/ngày | Download/ngày | KB/req | Resp time |
| :--- | ---: | ---: | ---: | ---: |
| T7 (12 ngày) | 20.008 | 799 MB | 40,9 | 1.008ms |
| T8 | 22.186 | 2.043 MB | 94,3 | 839ms |
| T9 | 21.114 | 2.031 MB | 98,5 | 789ms |
| **T10 (6 ngày)** | **14.850** | **564 MB** | **38,9** | 852ms |

- **2 điểm gãy cấu trúc:** 05/08 (KB/req x2,3 lần) và **01/10** (Req -29,7% vs T9, Download -72%, KB/req quay ngược về đúng mức trước 05/08). Sự đối xứng này cho thấy thay đổi cấu trúc (robots.txt / deploy / template weight), không phải mùa vụ.
- **Chất lượng crawl:** 200 OK 94,11% / **404 = 4,14% (~860 request/ngày bị đốt)** / 301 1,71%.
- **Cơ cấu purpose:** Refresh 95,97% / **Discovery chỉ 4,03%** - content mới tranh phần crawl rất nhỏ.
- **File type:** HTML 73,68% / JS 19,94% / Image chỉ 0,09%.
- **Bot:** Smartphone 51,2% - Desktop 12,54% / AdsBot 15,3% / Page resource load 20,14%.
- **Cảnh báo leading indicator:** Crawl T10 sụp 29,7% nhưng Organic MTD T10 vẫn +20,4% - traffic đang chạy trên nền crawl của T9. Lag 2-6 tuần nghĩa là tác động thật sẽ lộ ra cuối T10 / đầu T11, đúng lúc Q4 cần giữ nhịp 4M PV.

#### 3. Backlink Profile (GSC Top Linking Sites: 1.000 site / 118.757 linking pages)

| Bucket | Số site | Linking pages | Tỷ trọng |
| :--- | ---: | ---: | ---: |
| ≥1.000 pages | 5 | 103.773 | **87,4%** |
| 100-999 pages | 32 | 10.229 | 8,6% |
| 10-99 pages | 105 | 2.625 | 2,2% |
| 1-9 pages | 858 | 2.130 | **1,8%** |

- **Tập trung cực đoan:** topcv.vn 70.100 pages -> 7 target (59,0%) + cvs.vn 24.825 -> 11 (20,9%) = **2 site giữ 79,9%**; Top 5 = 87,4%; Top 20 = 93,3%.
- **9 site pattern site-wide** (≥500 pages, tỷ lệ pages/target >20x) giữ **85,6%** toàn bộ linking pages - xác nhận hiện trạng Task 5.17 (~96K backlinks/domain).
- **Authority bị bẫy trên trang tuyển dụng:** topcv + cvs chỉ trỏ vào 7-11 URL careers, không rò rỉ sang trang thương mại. Đây là lý do cấu trúc giải thích nghịch lý: backlink đồ sộ nhưng SoV Vay Nhanh 6%, BH ô tô 0%.
- **Khối editorial chính thống chỉ ~5%:** congly.vn, thuonghieucongluan.com.vn, baophapluat.vn, baolangson.vn, baodanang.vn, phunuvietnam.vn, baodongthap.vn, nghean24h.vn - phần tài sản duy nhất nên nhân rộng.
- **Cờ đỏ review disavow:** ai-hay.vn (5.511 pages -> **1.430 target pages** - footprint bất thường), c99.nl (384/1), aeroleads.com (227/1), clashofclansviet.com (528/1), zegashop.com, ideashop.vn, cadoco.vn.
- **[Audit link bẩn hoàn tất 10/10/2026]** - phân loại toàn bộ 1.000 site, kết quả 147 domain candidate / 353 linking pages (0,30% profile):
  - A1 Gambling strong (bet/casino/slot trong domain): 67 site / 109 pg
  - A2 Gambling pattern (digit + win/vip/club/88/789): 36 site / 45 pg
  - B Link networks (5 domain `*digitalbank` DNS chung name-services.com + multi-TLD): 18 site / 28 pg
  - C Spam directory/affiliate: 26 site / 171 pg
  - VERIFY tay (chưa disavow): c99.nl (384 pg), 2game.vn (16 pg)
  - Output: `07_REPORTS/backlink_disavow_candidates_2026-10-10.txt` (draft GSC format) + `backlink_audit_detail_2026-10-10.csv`
  - Kết luận: **105+ domain gambling = chiến dịch link spam/negative SEO nhắm vào momo.vn**; volume toxic chỉ 0,30% nên Google nhiều khả năng đã ignore, disavow là bảo hiểm cho YMYL. Vấn đề cấu trúc thật vẫn là 85,6% site-wide job board - không disavow được, phải sửa bằng cách đưa link về trang thương mại.

#### 4. Nhận Định Kết Hợp (3 nguồn dữ liệu)

- **Cùng chỉ về một điểm:** quyền lực xếp hạng của momo.vn đang tập trung nơi không tạo doanh thu (trang tuyển dụng + template footer), crawl budget đang co lại đúng lúc cần đẩy content mới, và Discovery chỉ 4%.
- **Rủi ro Quý 4:** Organic T10 đangneo được nhờ đà crawl T9 - đà đó đang hết. Base case 84,9% Target T10 khó đổi nếu không xử lý break 01/10 và không trả lại ngân sách Paid.
- **Mâu thuẫn logic cần chốt mid-month:** Target T10 (3,67M) cao hơn T9 (3,51M) trong khi T9 vượt nhờ cú bùng Paid cuối tháng, còn T10 Paid đang co 90%. Giả định tăng target mà giữ nguyên cấu trúc spend là chưa validate.

#### 5. Recommendations & Action Items

| # | Action | Mục tiêu / KPI | Ưu tiên | Owner |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Điều tra break 01/10: soi robots.txt hiện tại vs trước 01/10, đối chiếu deploy log | Khôi phục crawl về ~21K req/ngày | Cao nhất | Web Dev |
| 2 | Scale lại Paid T10 (campaign 20/10, 11.11, ngân sách BH Ô tô 550 triệu) | Về 18-20K PV/ngày để chạm pace 118K | Cao nhất | Growth/Ads |
| 3 | Đẩy Financial Hub utilities go-live nửa đầu tháng (Phân Bổ Lương, Chứng Chỉ Quỹ Phase 2) | Financial từ 9,6% lên >= run-rate 24,6% | Cao | Web Platform x FinHub Cell |
| 4 | Chuyển URL chết sang **410 Gone** + gỡ khỏi sitemap (thay vì để 404) | Tiết kiệm ~860 req/ngày crawl budget | Cao | Web Dev theo Zero-Traffic Audit |
| 5 | Review + disavow đợt 1: ai-hay.vn, c99.nl, aeroleads.com, clashofclansviet.com | Chặn toxic footprint, hoàn tất SOP disavow T10 | Trung bình | Media Team, audit lại trước khi submit |
| 6 | Xuất thêm GSC Top Linked Pages (bản hiện tại chỉ có count, thiếu URL đích) | Biết authority rơi vào careers hay trang thương mại | Trung bình | SEO execute |
| 7 | Chuyển KPI off-page từ tổng backlink sang: referring domains đến trang thương mại + editorial link ratio | Loại vanity metric | Trung bình | Đưa vào BRD Off-Page v2 revision |
| 8 | Internal link + sitemap ping ngay khi URL mới go-live (Cinema, Financial) | Nâng Discovery trên 4,03% | Trung bình | Web Platform |
| 9 | Nhân rộng 8 domain tin tức đang cho kết quả, mở scope list 15 domains outreach | Tăng khối editorial từ ~5% | Dài hạn | Inbound/Media |

---

