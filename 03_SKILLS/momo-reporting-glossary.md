# 📖 BẢNG TỪ ĐIỂN & QUY CHUẨN THUẬT NGỮ BÁO CÁO (MOMO REPORTING GLOSSARY)

> **Mục đích:** Bộ chuẩn hóa duy nhất (SSOT) về ngôn ngữ, thuật ngữ, từ viết tắt và chỉ số khi xây dựng slide, báo cáo tuần (Weekly - anh Công), báo cáo tháng (Monthly - anh Tường/BOM) và tài liệu nội bộ Web Platform.
> **Nguyên tắc cốt lõi:** Loại bỏ triệt để việc "viết tùm lum", dùng từ vô căn cứ, chắp vá Anh - Việt lộn xộn, gọi sai tên chỉ số hoặc nhầm lẫn bản chất kênh.
> **Hiệu lực:** Áp dụng song hành cùng [`03_SKILLS/momo-reporting-guidelines.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-guidelines.md) và [`03_SKILLS/web-platform-reporting-framework.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/web-platform-reporting-framework.md).

---

## 1. BẢNG CẤM KỴ & THAY THẾ BẮT BUỘC (STRICT DO'S & DON'TS)

Bảng này giải quyết trực diện các lỗi hành văn phổ biến gây mất tính chuyên nghiệp khi trình bày trước Ban Giám Đốc.

| Thành phần / Ngữ cảnh | Cấm viết (Viết tùm lum ❌) | Bắt buộc viết (Chuẩn mực ✅) | Lý do & Quy chuẩn |
| :--- | :--- | :--- | :--- |
| **Định danh Nền tảng** | Sàn Web, Sàn MoMo, Web con, Trang Web MoMo | **Nền tảng Web**, **Kênh Web**, **Web Platform**, **momo.vn** | MoMo là ứng dụng tài chính & hệ sinh thái số, không phải "sàn thương mại điện tử". |
| **Định danh Nhân sự** | Tên cá nhân / PIC (Hiến, Bảo, Trọng, Thuận, Duy, Nam...) | **Tên đội ngũ chuyên môn** (`Web Dev`, `Content Team`, `SEO Vendor`, `Media Team`, `Backend Team`...) | Báo cáo gửi Executive Leadership phản ánh năng lực và trách nhiệm của tổ chức, không quy về cá nhân. |
| **Trang trí / Biểu cảm** | Dùng Emoji, Icon (🚀, 🔥, ⚠️, ❌, ✅, 📈, 🎯, 💡) trong slide | **Văn bản thuần túy**, dùng nhãn phân loại `[R]`, `[D]`, `[F]` hoặc thẻ trạng thái `[Hoàn thành]`, `[Chậm tiến độ]` | Quy chuẩn công ty cấm 100% emoji trong slide báo cáo quản trị. |
| **Cơ cấu Kênh Traffic** | Đặt Paid ngang hàng hoặc xen kẽ với Organic, Direct | **Gom 2 khối lớn:**<br>1. **Non-Paid Traffic** (Chủ lực)<br>2. **Paid Traffic** (Hỗ trợ) | Phân định rõ chất lượng tăng trưởng hữu cơ (Organic) với tăng trưởng dùng tiền (Paid). |
| **Quy ước Chữ hoa (Title)** | Viết hoa chữ cái đầu từng từ (Title Case): *Báo Cáo Hiệu Suất Tháng 9* | **Sentence case (chỉ viết hoa chữ đầu câu):**<br>*Báo cáo hiệu suất tháng 9* | Trong văn bản tiếng Việt, Title Case làm giảm tốc độ đọc của người xem. |
| **Bullet Lead-ins** | Tiếng Anh chắp vá: *Key Highlights:*, *Lowlights:*, *Next Actions:* | **Tiếng Việt ngắn gọn:**<br>`Điểm nổi bật:`, `Vấn đề cần cải thiện:`, `Động lực chính:`, `Việc tiếp theo:` | Báo cáo tiếng Việt phải đồng nhất ngôn ngữ, chỉ giữ tiếng Anh cho tên chỉ số kỹ thuật. |
| **Định vị Kênh Paid** | "Paid tăng trưởng mạnh là điểm sáng", "Dùng Paid cứu target" | **Ghi nhận thực tế, cảnh báo rủi ro:**<br>"Paid tăng đột biến trong khi Organic chững lại phản ánh rủi ro phụ thuộc ngân sách ngắn hạn" | Organic là cốt lõi của Web Platform. Paid chỉ đóng vai trò kích mồi (seeding) và hỗ trợ chiến dịch. |
| **Báo cáo Tháng (Kỳ số liệu)** | "Báo cáo tháng 10" (khi họp vào tháng 10 nhưng số liệu là của tháng 9) | **"Báo cáo tháng 9/2026"** | Tháng báo cáo tính theo **kỳ dữ liệu phát sinh**, không tính theo ngày gửi hay ngày tổ chức họp. |
| **Chỉ số đứng trần** | Đưa số liệu không có so sánh: "Đạt 4.5M lượt xem" | **Luôn kèm mốc so sánh & việc tiếp theo:**<br>"Đạt 4.5M Pageviews (96% target tháng, +12% MoM), phần thiếu 4% đến từ biến động thuật toán Google, cần tập trung tối ưu 15 bài trụ cột" | Con số đứng một mình là con số chết. |

---

## 2. BẢNG KHỬ TỪ SÁO RỖNG & TIÊU CHUẨN HÓA VĂN PHONG AI (AI-ISMS & MACHINE-TRANSLATION CLEANUP)

Khi AI tham gia viết báo cáo, PRD hoặc slide, các mô hình ngôn ngữ (LLM) thường dịch thô (literal translation) các thuật ngữ tiếng Anh sang Hán-Việt cổ kính hoặc từ ngữ cơ khí, vật lý nghe rất ngô nghê, thiếu tính nghiệp vụ sản phẩm.

Bảng dưới đây chuẩn hóa triệt để các "tật" hành văn của AI:

| Từ ngữ AI tự viết (Dịch thô ❌) | Thuật ngữ gốc tiếng Anh | Chuẩn hóa MoMo Tech / Product Lead ✅ | Ngữ cảnh & Ví dụ chỉnh sửa thực tế |
| :--- | :--- | :--- | :--- |
| **Phân hệ** | Subsystem / Module / Sub-platform | **Module**, **Khu vực chức năng**, hoặc **Mảng sản phẩm** (Hub) | ❌ *"Phân hệ LDP và phân hệ GenAI"*<br>✅ *"Module LDP Builder (M1) và Module GenAI Content (M2)"*<br>*(Tuyệt đối không dùng "phân hệ", từ này mang phong cách phần mềm bao cấp thập niên 2000).* |
| **Động cơ** | Engine (Growth engine, Content engine, Search engine) | **Cơ chế tăng trưởng**, **Bộ máy vận hành**, **Công cụ** hoặc giữ nguyên **Growth Engine** | ❌ *"Động cơ tăng trưởng của Web đang gặp vấn đề"*<br>✅ *"Cơ chế tăng trưởng (Growth Engine) của Web đang chững lại"*<br>❌ *"Động cơ tìm kiếm"*<br>✅ *"Công cụ tìm kiếm"* (Google/Bing). |
| **Ma sát** | Friction / User friction / Drop-off | **Rào cản**, **Điểm nghẽn**, **Thao tác thừa**, **Điểm rơi rớt (Drop-off)** | ❌ *"Giảm thiểu ma sát cho khách hàng khi vào web"*<br>✅ *"Giảm rào cản thao tác (rút ngắn từ 4 bước xuống 2 bước) giúp giảm tỷ lệ rơi rớt người dùng"*<br>*(Ma sát là thuật ngữ vật lý cơ học, không dùng cho trải nghiệm người dùng).* |
| **Trải nghiệm không ma sát** | Frictionless experience | **Trải nghiệm mượt mà**, **Trải nghiệm thuận tiện**, **Luồng thao tác liền mạch** | ❌ *"Tạo trải nghiệm không ma sát"*<br>✅ *"Tối ưu luồng OneLink mở thẳng tính năng trên App giúp trải nghiệm mượt mà, không bị gián đoạn."* |
| **Tận dụng** *(Lạm dụng lặp lại)* | Leverage / Utilize / Tap into | **Khai thác**, **Ứng dụng**, **Tối ưu**, **Kế thừa** | ❌ *"Tận dụng sức mạnh của AI để tận dụng data"*<br>✅ *"Khai thác năng lực GenAI để chuẩn hóa dữ liệu từ khóa."* |
| **Bức tranh toàn cảnh / Mảnh ghép** | Big picture / Puzzle piece | **Báo cáo tổng quan**, **Bối cảnh tổng thể**, **Hạng mục chiến lược** | ❌ *"Mảnh ghép quan trọng trong bức tranh toàn cảnh"*<br>✅ *"Hạng mục trọng tâm đóng góp 25% vào mục tiêu MUA quý 4."* |
| **Hạ cánh / Trang hạ cánh** | Land / Landing page | **Điều hướng về trang đích**, **Trang đích (Landing Page / LDP)** | ❌ *"User hạ cánh vào trang"*<br>✅ *"Người dùng được điều hướng về trang đích (LDP)."* |
| **Hào nước / Hào nước dữ liệu** | Economic moat / Data moat | **Lợi thế phòng thủ dữ liệu**, **Rào cản cạnh tranh độc quyền**, hoặc giữ **Data Moat** | ❌ *"Tạo dựng hào nước bảo vệ web"*<br>✅ *"Xây dựng lợi thế phòng thủ dữ liệu (Data Moat) từ các tiện ích tra cứu độc quyền mà AI bên ngoài không thể cào được."* |
| **Rò rỉ phễu / Phễu dốc** | Funnel leakage / Steep funnel | **Tỷ lệ rơi rớt (Drop-off)**, **Đứt gãy luồng chuyển đổi** | ❌ *"Phễu chuyển đổi bị rò rỉ ở bước 3"*<br>✅ *"Ghi nhận tỷ lệ rơi rớt (Drop-off) 45% tại bước xác thực số điện thoại."* |
| **Đơn thuốc hành động** | Prescription / Prescriptive action | **Kế hoạch xử lý**, **Giải pháp khắc phục**, **Hành động trọng tâm** | ❌ *"Đơn thuốc hành động P0"*<br>✅ *"Kế hoạch xử lý khẩn cấp (P0) gồm 3 hành động cụ thể..."* |
| **Neo giữ / Neo móc** | Anchor / Retention | **Giữ chân người dùng (Retention)**, **Duy trì tương tác** | ❌ *"Neo giữ người dùng trên sàn web"*<br>✅ *"Nâng tỷ lệ giữ chân người dùng (Retention Rate) qua các tiện ích tài chính hàng ngày."* |
| **Kiến tạo / Thúc đẩy bùng nổ** | Foster / Boost / Skyrocket | **Tăng trưởng định lượng cụ thể (+X%)**, **Tối ưu hóa** | ❌ *"Kiến tạo giá trị bùng nổ cho dịch vụ"*<br>✅ *"Thúc đẩy tăng trưởng lượt cài đặt mới (+24% MoM) qua luồng CHAOMOMO."* |
| **Nút thắt cổ chai** | Bottleneck | **Điểm nghẽn kỹ thuật**, **Điểm nghẽn quy trình**, hoặc **Bottleneck** | ❌ *"Gặp nút thắt cổ chai ở backend"*<br>✅ *"Phát sinh điểm nghẽn kỹ thuật (Bottleneck) tại cổng API tra cứu phạt nguội do đối tác quá tải."* |
| **Chạm tới / Chạm mốc** *(Lạm dụng)* | Reach / Hit milestone | **Đạt**, **Ghi nhận**, **Cán mốc** | ❌ *"Traffic chạm tới ngưỡng bùng nổ"*<br>✅ *"Lưu lượng đạt 5,2M MUA, vượt 4% chỉ tiêu tháng."* |
| **Vùng trũng / Vùng trũng traffic** | Traffic trough / Low volume area | **Lưu lượng còn thấp**, **Chưa có lưu lượng tự nhiên**, **Đóng góp còn khiêm tốn** | ❌ *"Xóa vùng trũng traffic của CCQ"*<br>✅ *"Kích hoạt lưu lượng tự nhiên cho nhóm sản phẩm Đầu tư (hiện chỉ đạt 458 PVs) và mở rộng danh mục."*<br>*(Tuyệt đối không dùng "vùng trũng", từ ngữ sáo rỗng giống dự báo thời tiết lũ lụt).* |
| **Bấm nút / Bấm nút triển khai** | Kick-off / Push button | **Kích hoạt triển khai**, **Bắt đầu thực thi**, **Giải ngân gói thử nghiệm** | ❌ *"Bấm nút gói bài PR"*<br>✅ *"Triển khai dự án thử nghiệm Pilot Off-Page SEO 125M (BU Movies tài trợ 80%)."*<br>*(Bấm nút là từ khẩu ngữ, văn nói bình dân, cấm dùng trong slide BOM).* |
| **Gói bài PR** | PR articles / Guest posts | **Chiến dịch Off-Page SEO**, **Bài viết thẩm quyền (Authority Content)**, **Dự án Pilot Off-Page** | ❌ *"Chốt vendor mua gói bài PR"*<br>✅ *"Lựa chọn đối tác triển khai gói Pilot Off-Page SEO thẩm quyền."* |
| **Hứng trọn** | Capture / Absorb | **Đón nhận và tối ưu chuyển đổi**, **Hấp thu lưu lượng tìm kiếm** | ❌ *"Hứng trọn 22K volume tìm kiếm"*<br>✅ *"Tối ưu chuyển đổi từ 22.750 lượt tìm kiếm thương hiệu hàng tháng."* |
| **Kéo người chơi / Kéo lượng lớn** | Drive users / Acquire gamers | **Thu hút người dùng mới trải nghiệm**, **Thúc đẩy tương tác** | ❌ *"Kéo lượng lớn người chơi vào web"*<br>✅ *"Thu hút người dùng mới tham gia trải nghiệm minigame và mở rộng tệp tương tác."* |
| **Mức nền vận hành tiêu chuẩn** | Operating Baseline | **Mức nền vận hành tiêu chuẩn**, **Mức nền cơ sở** | ✅ *"Paid Traffic đạt 473.481 PVs (-60,4% MoM), quay về mức nền vận hành tiêu chuẩn tương đương Tháng 7 và Tháng 8 sau khi kết thúc các chiến dịch cao điểm mùa lễ và tựu trường."* |
| **Mức nền vận hành tiêu chuẩn** | Operating Baseline | **Mức nền vận hành tiêu chuẩn**, **Mức nền cơ sở** | ✅ *"Paid Traffic đạt 473.481 PVs (-60,4% MoM), quay về mức nền vận hành tiêu chuẩn tương đương Tháng 7 và Tháng 8 sau khi kết thúc các chiến dịch cao điểm mùa lễ và tựu trường."* |
| **Kênh tự nhiên gánh vác / Tự chủ quy mô** | Organic Self-Sufficiency | **Tự chủ quy mô**, **Kênh tự nhiên gánh vác** | ✅ *"Việc traffic tổng thể vẫn đạt 98,3% Target thể hiện sự tự chủ rất lớn khi hầu như toàn bộ quy mô truy cập tháng này đều do kênh tự nhiên gánh vác (chiếm 86,86%)."* |
| **Đảo chiều tăng trưởng** | Reversal / Rebound | **Đảo chiều tăng trở lại**, **Phục hồi tăng trưởng** | ✅ *"Điểm sáng là Organic Search đã đảo chiều tăng trở lại đạt 1,72M PVs (+5,7%), cho thấy nội lực từ nội dung và tiện ích trên trang đang giúp phục hồi tốt sau giai đoạn xây dựng nền tảng trong Q3."* |
| **Đà tăng liên tục qua các tháng** | Multi-Month Growth Momentum | **Duy trì đà tăng liên tục [n] tháng** | ✅ *"Direct Traffic đạt 931.731 PVs (chiếm 25,9% toàn trang) và duy trì đà tăng liên tục 4 tháng (từ 440K lên 932K, tăng +111,3% so với Tháng 7), chứng minh người dùng ngày càng có thói quen vào thẳng momo.vn."* |

---

## 3. HỆ THỐNG CHỈ SỐ BÁO CÁO (PERFORMANCE METRICS SSOT)

Tuyệt đối không dùng chung từ "khách hàng", "người dùng", "traffic" một cách mập mờ. Bắt buộc gọi đúng tầng chỉ số:

### 2.1. Tầng Web Traffic (Lưu lượng Web)

| Thuật ngữ | Ký hiệu | Định nghĩa chuẩn xác | Công thức / Đo lường | Ngữ cảnh sử dụng đúng |
| :--- | :--- | :--- | :--- | :--- |
| **Pageviews** | **PV** | Tổng số lượt trang web được tải hoặc tải lại trên trình duyệt. | GA4: `screenPageViews` | Đo lường dung lượng tiêu thụ nội dung tổng thể. 1 người xem 5 trang = 5 PV. |
| **Sessions** | **Sessions** | Tổng số phiên truy cập web (kết thúc sau 30 phút không hoạt động). | GA4: `sessions` | Đo lường số lượt ghé thăm của người dùng. |
| **MUA** | **MUA** | **Monthly Unique Audience** — Lượng độc giả/người dùng duy nhất truy cập Web trong tháng. | GA4: `totalUsers` (khung tháng) | Chỉ số North Star quy mô bao phủ thị trường của Web. |
| **MEU** | **MEU** | **Monthly Engaged Users** — Người dùng có phiên tương tác thực chất (trên 10s hoặc xem $\ge 2$ trang hoặc có tương tác). | GA4: `activeUsers` | Đo lường người dùng chất lượng thực, loại bỏ bot và click tặc. |
| **Engagement Rate** | **ER** | Tỷ lệ phiên tương tác trên tổng số phiên truy cập. | $\text{Engaged Sessions} / \text{Sessions}$ | Thay thế Bounce Rate cũ của Universal Analytics. Đo lường độ hấp dẫn của nội dung. |
| **Avg. Engagement Time** | **Duration** | Thời gian tương tác trung bình của người dùng trên trang. | GA4: `userEngagementDuration / activeUsers` | Đo lường độ sâu khi đọc bài viết hoặc thao tác tiện ích (Widget/Calculator). |

### 2.2. Tầng Chuyển đổi Web-to-App (W2A Funnel)

| Thuật ngữ | Ký hiệu | Định nghĩa chuẩn xác | Đo lường kỹ thuật | Ý nghĩa báo cáo |
| :--- | :--- | :--- | :--- | :--- |
| **OneLink Click** | **OneLink** | Lượt nhấp vào đường dẫn liên kết thông minh AppsFlyer để tải hoặc mở app MoMo. | Umami / GA4: `outbound_click` (domain: `app.momo.vn`) | Thể hiện ý định chuyển dịch từ Web sang App của người dùng. |
| **W2A CVR** | **W2A CVR** | Tỷ lệ chuyển đổi từ Web sang App. | $\frac{\text{OneLink Clicks}}{\text{Sessions}}$ hoặc $\frac{\text{OneLink Clicks}}{\text{MEU}}$ | Đo lường hiệu quả dẫn dòng và năng lực điều hướng người dùng vào App. |
| **App Open** | **Deeplink** | Lượt kích hoạt mở trực tiếp app MoMo (với user đã có sẵn app). | AppsFlyer: `af_app_opened` | Đo lường mức độ kích hoạt người dùng hiện hữu qua Web. |
| **App Install** | **Install** | Lượt tải mới và cài đặt ứng dụng MoMo từ liên kết trên Web. | AppsFlyer GPD: `install` (Non-organic Web) | Đóng góp trực tiếp vào tăng trưởng New User cho MoMo. |
| **New Registration** | **New Reg** | Người dùng mới hoàn tất đăng ký số điện thoại và kích hoạt tài khoản. | Backend MoMo: `account_created` | Đo lường chất lượng người dùng thực sự sau cài đặt. |
| **Map Bank** | **Map Bank** | Người dùng mới liên kết tài khoản ngân hàng thành công (hoàn tất KYC/KYB). | Backend MoMo: `bank_linked` | Điểm chuyển đổi vàng tạo ra người dùng kích hoạt tài chính thực thụ. |
| **First Transaction** | **FTX** | Giao dịch tài chính đầu tiên phát sinh trên ứng dụng MoMo. | Backend MoMo: `first_transaction` | Cột mốc hoàn tất phễu kích hoạt (Activation Funnel). |

### 2.3. Tầng Đánh giá Tiến độ & Tăng trưởng

| Thuật ngữ | Ký hiệu | Định nghĩa & Cách tính | Ý nghĩa trong slide |
| :--- | :--- | :--- | :--- |
| **Month-To-Date** | **MTD** | Lũy kế số liệu từ ngày 1 của tháng đến ngày chốt số liệu gần nhất. | So sánh cùng kỳ MTD của tháng trước để đánh giá đúng nhịp. |
| **Month-over-Month** | **MoM** | Tốc độ tăng trưởng so với tháng trước: $\frac{M_t - M_{t-1}}{M_{t-1}} \times 100\%$. | Phản ánh xu hướng ngắn hạn 30 ngày. |
| **Year-over-Year** | **YoY** | Tốc độ tăng trưởng so với cùng kỳ năm trước. | Loại bỏ yếu tố mùa vụ (Seasonality), đánh giá tăng trưởng cốt lõi. |
| **Week-over-Week** | **WoW** | Tốc độ tăng trưởng so với tuần trước. | Dùng riêng cho Báo cáo Tuần (Weekly Report). |
| **Day-over-Day** | **DoD** | Biến động so với ngày hôm trước. | Dùng khi chẩn đoán bất thường kỹ thuật hoặc đứt gãy tracking. |
| **Target Pacing** | **Pacing** | Tỷ lệ hoàn thành mục tiêu theo tiến độ thời gian thực:<br>$\text{Pacing} = \frac{\text{Actual MTD}}{\text{Target Tháng} \times (\text{Số ngày đã qua} / \text{Tổng ngày trong tháng})} \times 100\%$. | $\ge 100\%$: Vượt tiến độ;<br>$< 100\%$: Đang hụt nhịp (Lagging). |
| **Run-rate / Forecast** | **Forecast** | Dự báo kết quả cuối tháng nếu duy trì nhịp độ hiện tại:<br>$\text{Run-rate} = \frac{\text{Actual MTD}}{\text{Số ngày đã qua}} \times \text{Tổng số ngày của tháng}$. | Giúp Ban Giám Đốc biết kịch bản kết tháng để điều chỉnh kịp thời. |

---

## 4. PHÂN ĐỊNH KÊNH LƯU LƯỢNG (TRAFFIC SOURCE TAXONOMY)

Quy định cấu trúc phân loại bắt buộc trong mọi bảng số liệu và biểu đồ:

```
TỔNG LƯU LƯỢNG (TOTAL TRAFFIC)
├── 1. NON-PAID TRAFFIC (Chủ lực — Lưu lượng Tự nhiên & Thương hiệu)
│   ├── Organic Search (Tìm kiếm Google, Bing tự nhiên)
│   ├── Direct (Truy cập trực tiếp momo.vn, bookmark, thương hiệu)
│   ├── Referral (Giới thiệu từ báo chí, trang đối tác, blog uy tín)
│   ├── GEO / AI Citations (Trích dẫn từ Perplexity, ChatGPT, Gemini, Copilot)
│   └── Organic Social & Others (Mạng xã hội tự nhiên, lưu lượng nội bộ)
└── 2. PAID TRAFFIC (Bổ trợ — Ngân sách Tiếp thị trả tiền)
    ├── Paid Search (Google Ads Search)
    ├── Paid Social (TikTok Ads, Facebook Ads)
    ├── Display / Programmatic (Mạng quảng cáo hiển thị, Admicro, GDN)
    └── Paid Affiliate & Partner Ads
```

### Quy tắc bất di bất dịch khi báo cáo Kênh:
1. **Không gộp chung:** Tuyệt đối không để dòng `Paid` nằm xen kẽ giữa các kênh `Organic` và `Direct`.
2. **Nguyên tắc tỷ trọng:** Web Platform lấy `Non-Paid` làm gốc (mục tiêu $\ge 85-90\%$). Nếu `Paid` chiếm tỷ trọng tăng cao đột biến, bắt buộc phải giải trình nguyên nhân chiến dịch và lộ trình giảm dần sau khi kết thúc chiến dịch.
3. **Chất lượng W2A:** Luôn bóc tách CVR sang App của `Non-Paid` vs. `Paid`. Thông thường, `Non-Paid` có tỷ lệ giữ chân (Retention) và chuyển đổi ra giao dịch cao gấp 2-3 lần so với `Paid`.

---

## 5. DANH MỤC HUBS & NGÀNH HÀNG (HUBS & VERTICALS TAXONOMY)

Thống nhất tên gọi chuẩn cho các mảng sản phẩm/nội dung trên Web Platform:

| Tên Hub chuẩn | Tên tiếng Việt trong báo cáo | Phạm vi sản phẩm & Use Cases chính | URL Path SSOT |
| :--- | :--- | :--- | :--- |
| **Financial Hub** | Trung tâm Tài chính số | Tỷ giá ngoại tệ, Giá vàng, Điểm tín dụng CIC, Vay nhanh, Ví Trả Sau, Tiết kiệm Online, Chứng chỉ quỹ | `/tai-chinh/`, `/cong-cu/` |
| **Cinema Hub** | Trung tâm Điện ảnh & Vé phim | Lịch chiếu phim toàn quốc, Giá vé, Review phim, Cụm rạp đối tác (CGV, Lotte, Galaxy, BHD, Beta...) | `/cinema/` |
| **Vehicle Hub** | Trung tâm Giao thông & Xe | Tra cứu phạt nguội CSGT, Nạp phí không dừng VETC/ePass, Bảo hiểm bắt buộc TNDS xe máy/ô tô, Đăng kiểm xe | `/dich-vu-xe/` |
| **Insurtech Hub** | Trung tâm Bảo hiểm số | Bảo hiểm xe máy, Bảo hiểm viện phí, Bảo hiểm du lịch, Bảo hiểm tai nạn cá nhân | `/bao-hiem/` |
| **OTA / Travel Hub** | Trung tâm Du lịch & Đi lại | Vé máy bay nội địa/quốc tế, Vé tàu hỏa, Vé xe khách liên tỉnh, Đặt phòng khách sạn | `/du-lich/`, `/ve-xe/` |
| **Telco Hub** | Trung tâm Viễn thông | Nạp tiền điện thoại trả trước, Nạp Data 3G/4G/5G, Mua mã thẻ cào, Đổi điểm thưởng | `/nap-tien-dien-thoai/` |
| **Public Services (DVC)** | Dịch vụ công & Đời sống | Nộp phạt vi phạm giao thông, Tra cứu tiền điện, tiền nước, Phí học phí, Cổng DVC Quốc gia | `/dich-vu-cong/`, `/thanh-toan-hoa-don/` |
| **Entertainment Hub** | Trung tâm Giải trí & Gamification | Minigames, Lắc Xì, Sự kiện lễ hội, Vòng quay may mắn, Bảng xếp hạng nhận quà | `/giai-tri/` |

> [!WARNING]
> Không gọi tùy tiện: *Hub Phim* (phải là `Cinema Hub`), *Mảng Xe Cộ* (phải là `Vehicle Hub`), *Mảng Bank* (phải là `Financial Hub`).

---

## 6. BỘ TỪ VIẾT TẮT CHUẨN MỰC (ACRONYMS DICTIONARY A-Z)

Các từ viết tắt này được phép sử dụng trong deck báo cáo, với điều kiện dùng đúng ngữ cảnh:

| Từ viết tắt | Tên đầy đủ tiếng Anh | Ý nghĩa / Cách đọc chuẩn khi trình bày |
| :--- | :--- | :--- |
| **AEO** | Answer Engine Optimization | Tối ưu hóa để các công cụ trả lời trực tiếp trích dẫn nội dung MoMo. |
| **AIO** | AI Overviews | Khối tóm tắt thông tin bằng AI hiển thị trên đỉnh trang tìm kiếm Google. |
| **AOV** | Average Order Value | Giá trị trung bình trên một đơn hàng / giao dịch. |
| **ARPU** | Average Revenue Per User | Doanh thu bình quân trên một người dùng. |
| **BOM** | Board of Management | Ban Tổng Giám Đốc điều hành MoMo. |
| **BRD** | Business Requirements Document | Tài liệu yêu cầu nghiệp vụ kinh doanh. |
| **BU** | Business Unit | Đơn vị kinh doanh độc lập (ví dụ: BU Movies, BU Telco, BU FS). |
| **CAC** | Customer Acquisition Cost | Chi phí để thu hút được một khách hàng mới. |
| **CTR** | Click-Through Rate | Tỷ lệ nhấp chuột trên số lượt hiển thị ($\text{Clicks} / \text{Impressions}$). |
| **CVR** | Conversion Rate | Tỷ lệ chuyển đổi qua từng bước trong phễu hành vi. |
| **CX** | Customer Experience | Trải nghiệm khách hàng. |
| **E-E-A-T** | Experience, Expertise, Authoritativeness, Trustworthiness | Bộ tiêu chí đánh giá chất lượng nguồn tin của Google: Kinh nghiệm, Chuyên môn, Thẩm quyền, Đáng tin cậy. |
| **FTX** | First Transaction | Giao dịch tài chính đầu tiên của user mới trên ứng dụng. |
| **GA4** | Google Analytics 4 | Nền tảng đo lường dữ liệu truy cập web chuẩn của MoMo. |
| **GEO** | Generative Engine Optimization | Tối ưu hóa công cụ tìm kiếm tạo sinh (ChatGPT, Perplexity, Gemini). |
| **GPD** | Growth Product Division | Khối Sản phẩm Tăng trưởng. |
| **GSC** | Google Search Console | Công cụ đo lường hiệu suất tìm kiếm tự nhiên của Google. |
| **JTBD** | Jobs-To-Be-Done | Khung tư duy "Nhiệm vụ cần giải quyết" của khách hàng. |
| **KYC / KYB** | Know Your Customer / Know Your Business | Xác thực định danh khách hàng / đối tác doanh nghiệp. |
| **LTV** | Customer Lifetime Value | Giá trị vòng đời trọn đời của khách hàng. |
| **MAU** | Monthly Active Users | Người dùng hoạt động hàng tháng trên ứng dụng MoMo. |
| **MBR** | Monthly Business Review | Báo cáo & cuộc họp đánh giá kết quả kinh doanh hàng tháng. |
| **MDE** | Minimum Detectable Effect | Mức tác động tối thiểu có thể phát hiện được trong thử nghiệm A/B. |
| **MoM** | Month-over-Month | Biến động so với tháng trước liền kề. |
| **MTD** | Month-To-Date | Số liệu lũy kế từ đầu tháng đến thời điểm hiện tại. |
| **MUA** | Monthly Unique Audience | Tổng lượng người dùng duy nhất trên Web trong tháng. |
| **OKR** | Objectives and Key Results | Mục tiêu và kết quả then chốt của quý/năm. |
| **OneLink** | AppsFlyer OneLink | Công nghệ liên kết chuyển đổi từ Web sang mở/tải App. |
| **pSEO** | Programmatic SEO | Tự động hóa sản xuất hàng ngàn trang đích chuẩn SEO dựa trên cơ sở dữ liệu có cấu trúc. |
| **PLG** | Product-Led Growth | Chiến lược tăng trưởng lấy sản phẩm và tiện ích tương tác làm động cơ chính. |
| **PRD** | Product Requirements Document | Tài liệu đặc tả yêu cầu sản phẩm chi tiết cho kỹ thuật. |
| **RICE** | Reach - Impact - Confidence - Effort | Khung chấm điểm ưu tiên tính năng dựa trên Phạm vi, Tác động, Độ tin cậy và Công sức. |
| **SERP** | Search Engine Results Page | Trang hiển thị kết quả tìm kiếm của Google. |
| **SoV** | Share of Voice | Thị phần tiếng nói / tỷ lệ hiển thị thương hiệu so với toàn ngành. |
| **SSOT** | Single Source of Truth | Nguồn chân lý duy nhất — tệp dữ liệu được công nhận làm chuẩn đối soát. |
| **UIC** | Urgency - Impact - Confidence | Khung chấm điểm ưu tiên theo Độ cấp bách, Tác động và Độ tin cậy. |
| **UTM** | Urchin Tracking Module | Bộ tham số gắn vào URL để phân loại nguồn chiến dịch tiếp thị. |
| **W2A** | Web-to-App | Luồng điều hướng và chuyển đổi người dùng từ Website vào ứng dụng MoMo. |
| **WBR** | Weekly Business Review | Báo cáo & cuộc họp đánh giá tiến độ vận hành hàng tuần. |
| **WoW** | Week-over-Week | Biến động so với tuần trước. |
| **YMYL** | Your Money Your Life | Nhóm chủ đề liên quan đến Tiền bạc & Sức khỏe có tiêu chuẩn kiểm duyệt nội dung khắt khe nhất của Google. |
| **YoY** | Year-over-Year | Biến động so với cùng kỳ năm trước. |

---

## 7. QUY CHUẨN ĐỊNH DANH ĐỘI NGŨ (SQUADS / TEAMS / DIVISIONS)

Để loại bỏ hoàn toàn việc nhắc tên riêng cá nhân (`Hiến`, `Bảo`, `Trọng`...), bắt buộc dùng danh xưng chuẩn sau:

| Tên cá nhân / Gọi tắt (Cấm ❌) | Tên đội ngũ chuẩn mực (Dùng ✅) | Phạm vi chuyên môn |
| :--- | :--- | :--- |
| Team anh Hiến, Hiến | **Web Platform Lead** / **Web Growth Team** | Lãnh đạo định hướng sản phẩm, kiến trúc và chiến lược tăng trưởng Web. |
| Team dev, Bảo, Coder | **Web Dev** / **Frontend Team** | Đội ngũ kỹ sư phát triển giao diện Web và nền tảng MoSpark. |
| Team server, Trọng | **Backend Team** / **Data Platform Team** | Đội ngũ kỹ sư dịch vụ lõi, API tích hợp và cơ sở dữ liệu. |
| Team viết bài, CTV SEO | **Content Team** / **SEO Editorial Squad** | Đội ngũ biên tập, sản xuất nội dung bài viết và tối ưu cấu trúc từ khóa. |
| Agency SEO, Vendor | **SEO Vendor** / **SEO Agency Partner** | Đối tác bên ngoài phụ trách tối ưu kỹ thuật SEO chuyên sâu và backlink. |
| Team chạy ads, Media | **Media Team** / **Performance Marketing Team** | Đội ngũ phân bổ ngân sách và tối ưu hóa các chiến dịch quảng cáo trả phí. |
| Team rạp phim | **BU Movies** | Khối kinh doanh dịch vụ vé xem phim và giải trí điện ảnh. |
| Team bảo hiểm | **Insurtech BU** | Khối kinh doanh các sản phẩm bảo hiểm số. |
| Team tài chính, vay | **Financial Services Team (FS Team)** | Khối kinh doanh dịch vụ ngân hàng, tín dụng, đầu tư và thanh toán. |
| Team viễn thông, xe | **VTTI BU** (Viễn thông & Tiện ích) | Khối dịch vụ công, nạp tiền điện thoại, hóa đơn tiện ích và giao thông. |
| Team kiểm duyệt, Risk | **Risk & Compliance Team** | Đội ngũ quản trị rủi ro, tuân thủ pháp lý và an toàn thông tin. |
| Team AI, Bot | **AI/ML Team** | Đội ngũ nghiên cứu và triển khai mô hình học máy, GenAI pipeline. |

---

## 8. QUY CHUẨN TAGGING & MẪU CÂU HÀNH VĂN (REPORTING TEXTING RULES)

### 7.1. Hệ thống Tag phân loại Slide bắt buộc
Mỗi slide trong báo cáo bắt buộc phải mang đúng một trong 3 tag sau ở đầu tiêu đề:
- **`[R]` (Reporting):** Báo cáo tình hình, thông tin cập nhật (Pre-read). Người tham gia tự đọc trước cuộc họp, **không thuyết trình lại** trong buổi họp.
- **`[D]` (Discussion):** Nội dung trọng tâm cần thảo luận, căn chỉnh (align) hoặc xin ý kiến phê duyệt của Lãnh đạo. **Dành 80% thời lượng cuộc họp cho các slide này.**
- **`[F]` (FYI):** Thông tin tham khảo thêm, bảng số liệu chi tiết phụ lục, không thảo luận trong họp.

### 7.2. Nguyên tắc viết Action Title (Tiêu đề hành động)
- **Quy tắc:** Tiêu đề không được đặt tên chủ đề chung chung (như "Hiệu suất tháng 9" hay "Tình hình Cinema"). Tiêu đề phải là một câu hoàn chỉnh thể hiện: **Chỉ số đạt được + Xu hướng + Nguyên nhân cốt lõi**.
- **Cú pháp:** Sentence case (chỉ viết hoa chữ đầu).

*Ví dụ chuẩn mực:*
- ❌ *KPI Tháng 9*
- ✅ *Lưu lượng đạt 96% target tháng do kênh Paid cắt giảm sớm; Organic Search vẫn tăng trưởng +14% MoM bù đắp phần thiếu hụt*
- ❌ *Tình hình vé phim Cinema Hub*
- ✅ *Cinema Hub chạm mốc 420K MEU nhờ chiến dịch phim bom tấn quý 3; chuyển đổi Web-to-App tăng vọt lên 8,4%*

### 7.3. Bộ Bullet Lead-ins tiếng Việt chuẩn
Khi trình bày các gạch đầu dòng phân tích dưới Action Title, bắt buộc dùng các tiền tố tiếng Việt sau:
- `Vượt target:` hoặc `Chưa đạt target:` (Báo cáo kết quả so với kế hoạch)
- `Điểm nổi bật:` (Thành tựu và tác động kinh doanh lớn nhất)
- `Vấn đề cần cải thiện:` hoặc `Điểm nghẽn:` (Rủi ro, tồn đọng, sự cố kỹ thuật)
- `Động lực tăng trưởng:` hoặc `Nguyên nhân chính:` (Lý giải bản chất phía sau con số)
- `Tác động kinh doanh:` (Tác động tới New User, W2A, Doanh thu hoặc Chi phí)
- `Việc tiếp theo:` (Kế hoạch hành động cụ thể trong 7-30 ngày tới kèm thời hạn)
- `Đề xuất phê duyệt:` (Nội dung cần BOM/CEO quyết định phương án)

### 7.4. Cấu trúc Mẫu Slide Điều hành Kênh Lưu lượng (Executive Scorecard Pattern)
Khi xây dựng slide tổng quan hiệu suất kênh (`Scorecard` / `Executive Summary`), chuẩn hóa bố cục 2 khối đối xứng:
- **Khối bên trái (Chiếm 62% chiều rộng slide):**
  1. **Bảng phân rã 6 cột:** `Kênh lưu lượng | Tháng 7 | Tháng 8 | Tháng 9 | Tháng 10 | % MoM` (chia 2 tầng rành mạch `KÊNH TỰ NHIÊN (NON-PAID)` gồm Organic, AI Traffic (GEO), Direct, Referral và `KÊNH TRẢ PHÍ (PAID ADS)`, kèm các dòng tổng hợp `TỔNG LƯỢNG TRUY CẬP (ACTUAL)`, `MỤC TIÊU THÁNG (TARGET)`, `TỶ LỆ ĐẠT TARGET`).
  2. **Hộp Key Highlights (Chân bảng):** Phân tích 3 gạch đầu dòng cốt lõi:
     - *Kênh tự nhiên:* Đạt đỉnh, tỷ trọng chi phối (% share), đảo chiều tăng trở lại của Organic Search.
     - *Kênh trực tiếp & AI Search:* Tăng trưởng liên tục [n] tháng của Direct Traffic (thói quen vào thẳng momo.vn) và tốc độ bứt phá của AI Search (GEO).
     - *Kênh trả phí (Paid Ads):* Quay về mức nền vận hành tiêu chuẩn sau cao điểm mùa vụ; khẳng định sự tự chủ quy mô của kênh tự nhiên.
- **Khối bên phải (Chiếm 35% chiều rộng slide):**
  - **Hộp Priorities for the Next 30 Days (Toàn bộ chiều cao):** Xác lập ngay các mũi nhọn ưu tiên trong 30 ngày tới của từng Hub sản phẩm (Financial Hub, Cinema Hub, Platform) để người đọc thấy ngay lời giải và kế hoạch hành động.

---

## 9. BẢNG ĐỐI CHIẾU LỖI PHỔ BIẾN: VIẾT TÙM LUM ❌ VS. CHUẨN MOMO EXECUTIVE ✅

| Ngữ cảnh | Viết tùm lum (Kém chuyên nghiệp ❌) | Chuẩn mực MoMo Executive (Sắc sảo & Trúng đích ✅) |
| :--- | :--- | :--- |
| **Báo cáo kết quả Traffic** | "Tuần này sàn Web traffic tăng mạnh đạt 1.2M view, do chạy ads với lại team Bảo vừa update SEO mấy bài phim hay lắm 🚀" | `Điểm nổi bật:` Kênh Web ghi nhận 1,2M Pageviews (+18% WoW), trong đó Organic Search đóng góp 72% nhờ Web Dev tối ưu kiến trúc Schema cho cụm rạp Cinema Hub; lưu lượng Paid Search duy trì ổn định đúng ngân sách. |
| **Báo cáo Chuyển đổi sang App** | "User vào web bấm app nhiều hơn tháng trước, hình như được tầm vài nghìn install, bên media đang tính đẩy thêm tiền ads." | `Tác động Web-to-App:` Tỷ lệ chuyển đổi W2A CVR cải thiện lên 6,8% (+1,2 điểm % MoM); ghi nhận 12.500 lượt cài đặt ứng dụng mới (New Install), đóng góp 14% tổng lượng New User toàn MoMo với chi phí CAC thấp hơn 35% so với kênh Paid thuần túy. |
| **Giải trình nguyên nhân hụt Target** | "Tháng này target 5M mà chỉ được 4.6M vì Google update thuật toán làm rớt rank tùm lum với lại bên anh Trọng chưa nối xong API." | `Chưa đạt target:` Tổng MUA đạt 4,6M (đạt 92% target tháng). `Nguyên nhân chính:` Đợt cập nhật thuật toán Google Core Update làm biến động thứ hạng nhóm từ khóa tài chính vay tiêu dùng (-15% CTR); Backend Team đang hoàn tất đấu nối API tỷ giá để ra mắt tiện ích tra cứu bù đắp dung lượng trong tuần tới. |
| **Đề xuất trong cuộc họp BOM** | "Team em xin sếp duyệt thêm ít tiền ngân sách để chạy ads kéo lại mấy chỉ số bị rớt." | `Đề xuất phê duyệt [D]:` Đề xuất BOM phê duyệt gói ngân sách mồi 150 triệu VNĐ trong 14 ngày nhằm kích hoạt cụm tiện ích Lịch chiếu phim mới; kỳ vọng thu hút 180.000 MEU và hoàn vốn đầu tư (Break-even CAC) trong vòng 45 ngày qua dòng giao dịch vé rạp. |
| **Trình bày Kế hoạch tuần tới** | "Tuần sau Hiến với Bảo sẽ họp lại với bên vé phim để tính tiếp mấy trò minigame mới." | `Việc tiếp theo:` Web Growth Team chủ trì buổi đối soát kỹ thuật với BU Movies vào ngày 10/11 nhằm chốt danh mục 3 minigame tương tác cho mùa phim Tết, dự kiến hoàn tất tài liệu đặc tả PRD trước ngày 15/11. |

---

## 10. QUY TẮC CẬP NHẬT & BẢO TRÌ TỪ ĐIỂN

1. **Tính kế thừa:** Mọi thuật ngữ mới phát sinh từ các sáng kiến sản phẩm (như AI Agent, Auto-pSEO, GEO Tracking) phải được bổ sung ngay vào file này sau khi đã thống nhất định nghĩa với Product Lead.
2. **Kiểm tra trước khi xuất bản:** Bất kỳ văn bản báo cáo nào được sinh ra bởi AI Agent hoặc thành viên đội ngũ bắt buộc phải tự đối soát với Mục 1 (Cấm kỵ) và Mục 2 (Chỉ số) trước khi gửi đi.
