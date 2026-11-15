# Khung Báo Cáo Định Kỳ Web Platform (Web Platform Reporting Framework)

> **Mục tiêu:** Bộ quy chuẩn toàn diện về phương pháp luận, cấu trúc slide, công thức hành văn (copywriting/texting) và mẫu báo cáo định kỳ dành cho Web Platform.
> **Đối tượng báo cáo:** 
> - **Weekly Report:** Báo cáo tuần gửi Executive Leadership (anh Công) - tập trung vào tiến độ thực thi, tháo gỡ điểm nghẽn và đo lường tác động nhanh.
> - **Monthly Report:** Báo cáo tháng gửi Ban Giám Đốc / Hội đồng Quản trị (anh Tường, anh Công) - tập trung vào sức khỏe động cơ tăng trưởng, danh mục 4 Zone, phân tích Cohort và tác động chiến lược vĩ mô.

---

## 1. NGUYÊN TẮC BẮT BUỘC (CORE COMPLIANCE RULES)

Theo chỉ dẫn tại `AGENTS.md`, mọi báo cáo của Web Platform bắt buộc tuân thủ:

1. **Tuyệt đối không sử dụng Emoji / Icon:** Không dùng bất kỳ biểu tượng cảm xúc hay icon trang trí nào trong toàn bộ tiêu đề, bảng biểu và danh sách của bài báo cáo.
2. **Không đề cập tên riêng cá nhân / PIC:** Thay thế toàn bộ tên riêng bằng tên đội ngũ chuyên môn tương ứng (`Web Dev`, `Backend Team`, `Content Team`, `SEO Vendor`, `Media Team`, `Risk Team`, `AI/ML Team`, `CX Team`, `BU Movies`, `VTTI BU`, `FS Team`...).
3. **Cấu trúc 3 khối chuẩn mực** (áp dụng cho báo cáo Tuần, và cho phần thân báo cáo Tháng):
   - Khối 1: `Điểm nổi bật & Tác động kinh doanh`
   - Khối 2: `Phối hợp liên phòng ban & Việc cần hỗ trợ`
   - Khối 3: `Ưu tiên 7/30 ngày tới`
   - Riêng slide `Executive Summary` của báo cáo Tháng dùng cấu trúc 2 khối theo quy chuẩn công ty: `Điểm nổi bật` và `Vấn đề cần cải thiện`. Khối thứ hai bắt buộc có nội dung; một báo cáo chỉ có tin tốt là lỗi về độ tin cậy.
4. **Hệ thống 2 tầng chỉ số song song:** Luôn đo lường đồng thời **Tầng Web Metrics** (Pageviews, Sessions, MEU, CTR) và **Tầng App Business Impact** (Login App, New Installs, Transactions, Saved Profiles).
5. **Định dạng biểu diễn trực quan:**
   - Luồng người dùng / Hành trình trải nghiệm: Bắt buộc dùng sơ đồ Mermaid (`graph TD` hoặc `graph LR`) kèm theo Bảng phân tích chi tiết các bước (Step Breakdown Table).
   - Lộ trình và Cột mốc: Bắt buộc dùng Bảng Markdown (`Table`).

---

## 2. PHÂN ĐỊNH BÁO CÁO WEEKLY (ANH CÔNG) VS. MONTHLY (ANH TƯỜNG)

| Tiêu Chí So Sánh | Báo Cáo Tuần (Weekly - Anh Công) | Báo Cáo Tháng (Monthly - Anh Tường) |
| :--- | :--- | :--- |
| **Nhịp độ & Khung thời gian** | 7 ngày (Tuần hiện tại & 7 ngày tới) | 30 ngày (Tháng hiện tại & 30-90 ngày tới) |
| **Trọng tâm quản trị** | Vận hành thực thi, tiến độ tính năng, tháo gỡ điểm nghẽn kỹ thuật, quản trị ngân sách và A/B testing. | Sức khỏe động cơ tăng trưởng, danh mục 4 Zone, phân tích Cohort giữ chân, thị phần và chiến lược điểm đến Web Destination. |
| **Mức độ chi tiết số liệu** | Biến động tuần (WoW), số lượng ticket CS, tốc độ tải P90, CVR từng biến thể A/B, tiến độ rollout tính năng. | Chuỗi thời gian 6-12 tháng, Cohort Retention (M0-M11), cơ cấu First-service 15+ dịch vụ, tiến độ 3 kịch bản Traffic (4M-5M-6M). |
| **Cấu trúc Ưu tiên (Priorities)** | 1. Sửa lỗi & Phát hành (Hotfix & Delivery)<br/>2. Đánh giá A/B Testing<br/>3. Phối hợp liên đội ngũ (Sync) | 1. Vùng Hiệu suất (Performance Scaling)<br/>2. Vùng Chuyển đổi & Ươm tạo (Transformation/Incubation)<br/>3. Nền tảng & AI (Platform & AI Adoption) |

---

## 3. CÔNG THỨC HÀNH VĂN & MÔ TẢ (TEXTING & COPYWRITING FORMULA)

### 3.1. Công thức viết khối "Key Highlights & Business Impact"
**Giới hạn bắt buộc:** tối đa 5 ý, mỗi ý 1 dòng, mở đầu bằng con số (PV, % target, Install, ngày go-live) và kết bằng chỉ dẫn mục chi tiết ("Chi tiết mục III.2"). Khối này là bản tóm tắt cho cấp quản lý, không lặp lại phần mô tả của mục II-IV.
- Không đưa chi tiết build (tên tính năng con, URL, kiến trúc, quy trình nội bộ) vào đây; các chi tiết đó nằm ở mục Hub/Platform tương ứng.
- Nhiều việc go-live trong tuần gom chung vào một ý "Lên Production".
- Không kết luận vượt quá số liệu (ví dụ: tỷ trọng Non-Paid cao không có nghĩa "độc lập hoàn toàn với Paid").

Áp dụng công thức 4 thành tố liên kết:
$$\text{Số liệu đạt được (Biên độ WoW/MoM)} \longrightarrow \text{Nguyên nhân cốt lõi (Driver)} \longrightarrow \text{Tác động hệ sinh thái (Impact)} \longrightarrow \text{Hành động tiếp theo (Next Action)}$$

*Mẫu câu chuẩn cho Web Traffic & SEO/GEO:*
- "Lưu lượng truy cập đạt [Số] Pageviews ([+/-]% MoM) và [Số] MEU. Tỷ lệ Pageviews/MEU đạt [Số], phản ánh tệp người dùng có nhu cầu tìm kiếm thực (Intent Search) ổn định. Kênh Organic Search bứt phá (+[Số]% MoM) bù đắp cho phần sụt giảm của Paid Search sau khi chiến dịch Mega kết thúc."
- "Go-live [Số] trang nội dung chuẩn SEO/GEO; 100% đối tác xuất hiện trong Top 3-5 Google Search đối với cụm từ khóa thương hiệu; ghi nhận [Số] trích dẫn trên các công cụ AI Search (GEO đạt [Số]% Share of Authority)."

*Mẫu câu chuẩn cho Phễu Web-to-App & New User:*
- "Lượt cài đặt ứng dụng mới (New Install) duy trì đà tăng trưởng 3 tháng liên tiếp ([Số] $\rightarrow$ [Số] $\rightarrow$ [Số] installs), chứng minh nhóm người dùng mới được thu hút hiệu quả ngoài Web độc lập với biến động của tệp người dùng hiện hữu."
- "Tỷ lệ chuyển đổi MEU sang New Install cải thiện lên [Số]% (từ [Số]% tháng trước); gói quà chào mừng CHAOMOMO đóng góp [Số]% tổng lượt cài đặt nhờ giảm thiểu rào cản dùng thử."

*Mẫu câu chuẩn cho Năng lực Nền tảng & Công nghệ (MoSpark & GenAI):*
- "Tối ưu hóa luồng gọi API và tinh giản giao diện giúp cải thiện tốc độ tải trang P90 giảm [Số]%, thời gian đến khi nhấp chuột (Time to Click P90) giảm [Số]%, nâng điểm CSAT lên [Số]/5."
- "Triển khai GenAI Content Pipeline giúp rút ngắn thời gian sản xuất bài viết từ 1-2 ngày xuống còn 4-5 phút/bài, chi phí sản xuất giảm xuống 7.000 - 20.000 VNĐ/bài, giải phóng 90% thời gian vận hành thủ công."

---

### 3.2. Công thức viết khối "Cross-team Collaboration & Support Needed"
Bóc tách chi tiết rõ ràng theo từng đội ngũ đối tác kèm yêu cầu định lượng:

- **Đội ngũ Business Units (Cinema, VTTI, FS, SPS, Student Pass):**
  - "Phối hợp với BU tương ứng để chốt bộ quy tắc nghiệp vụ (Domain Knowledge), tích hợp API sản phẩm và thống nhất ngân sách truyền thông Off-page."
- **Đội ngũ Media & Marketing:**
  - "Phối hợp phân bổ ngân sách Paid Search/Paid Social tập trung vào các cụm từ khóa có tỷ lệ chuyển đổi cao (High-intent KWs) cho gói quà chào mừng người dùng mới."
- **Đội ngũ Risk, Security & Compliance:**
  - "Thiết lập bộ lọc giám sát chất lượng tự động (Guardrails) trên MoSpark CMS để ngăn chặn xuất bản nội dung vi phạm tiêu chuẩn SEO/Compliance; hoàn thiện cơ chế phân quyền Admin Panel."
- **Đội ngũ App Platform & Analytics:**
  - "Chuẩn hóa hạ tầng tracking Full Funnel qua Onelink để bóc tách chính xác toàn bộ hành trình từ Web Pageviews sang App Install, Mapbank và First Transaction."
- **Đội ngũ AI/ML & Big Data:**
  - "Mở rộng thuật toán gợi ý dịch vụ thông minh (Service Recommendation) ngoài Web dựa trên phân tích hành vi tìm kiếm của người dùng."

---

### 3.3. Công thức viết khối "Priorities"

**Đối với Báo cáo Tuần (7 Days):**
- **Sửa lỗi & Tối ưu Giao diện (Hotfix & Delivery):** Hoàn thành phát hành bản vá [Tên tính năng], tối ưu hóa tốc độ tải trang trên thiết bị di động.
- **Thử nghiệm A/B (A/B Test Validation):** Đánh giá số liệu biến thể [Treatment] so với [Control] trên quy mô [Số] người dùng để quyết định mở rộng toàn phần (Roll mass).
- **Phối hợp liên đội ngũ (Cross-team Sync):** Tổ chức họp chuyên sâu chốt giải pháp tự phục vụ (Self-service) cho các BU.

**Đối với Báo cáo Tháng (30 Days):**
- **Vùng Hiệu suất (Performance Scaling):** Mở rộng quy mô các dịch vụ mang lại dòng tiền ổn định (như luồng đặt vé xem phim toàn quốc, thanh toán QR trực tiếp).
- **Vùng Chuyển đổi & Ươm tạo (Transformation & Incubation):** Đưa Master Page Tiện Ích Giao Thông và Financial Hub vào vận hành chính thức; mở rộng độ phủ Student Pass tại các cụm trường đại học.
- **Nền tảng & AI (Platform & AI Adoption):** Nâng cấp công suất GenAI Content Pipeline đạt mục tiêu [Số] bài/tháng; mở rộng công cụ Landing Page Builder cho các Cell Teams.

---

## 4. MẪU BÁO CÁO TUẦN CHUẨN ĐIỀU HÀNH DÀNH CHO ANH CÔNG (WEEKLY REPORT ARCHITECTURE)

> **Cập nhật quy chuẩn (Đúc kết từ Báo Cáo Tuần 46):** Áp dụng nguyên mẫu kiến trúc từ `[InsurTech] Web 2026 Performance.pptx` kết hợp cẩm nang `03_SKILLS/executive-presentation-playbook.md`:
> 1. **Mục I.1 Overview:** Giới hạn đúng 4 chỉ số trọng tâm (PageViews vs Target, Non-Paid Traffic, AI Traffic / GEO, Phễu W2A trọn vẹn Install -> MAU).
> 2. **Mục I.3 Hub Targets:** Hiệu chỉnh mục tiêu sát thực tế vận hành và run-rate MTD.
> 3. **Mục I.4 Funnel Progression:** Bảng theo dõi tiến trình phễu W2A đa tháng (từ Tháng 7 đến MTD hiện tại).
> 4. **Mục II Tiêu đề Action Titles:** Bắt buộc thuần số liệu (PageViews, chuyển đổi, CVR), **tuyệt đối KHÔNG đưa tên tính năng hay công cụ vào tiêu đề** (tên tính năng và chi tiết kỹ thuật nằm ở thân bài).
> 5. **Mục II Thân bài chuẩn 3 khối:** (a) Highlights & Business Impact (phễu 4 bước + mốc kỹ thuật + Lowlights trung thực), (b) Phối hợp liên đội ngũ (BU đối tác + ngân sách cụ thể), (c) Kế hoạch hành động 7 ngày tới (không gắn nhãn ưu tiên P-zero đến P-three).
> 6. **Mục III Kết luận & Đề xuất hành động:** Bảng 3 cột khép kín: BÀI HỌC THỰC TẾ | BẰNG CHỨNG ĐỐI SOÁT | KẾ HOẠCH HÀNH ĐỘNG 7 NGÀY TỚI.
> 7. **Quy chuẩn văn phong:** Dùng `PageViews` (không dùng từ ngữ dịch thô), dùng `Nghiệm thu kỹ thuật` / `UAT` / `test`, dùng `Gói Quà tự chọn cho người dùng mới`, không ký tự En Dash / Em Dash, không gắn nhãn P-zero đến P-three.

```markdown
# BÁO CÁO TIẾN ĐỘ TUẦN [Số tuần] ([Từ ngày] - [Đến ngày]): WEB PLATFORM

> **Kỳ báo cáo:** Tuần [Số tuần] ([Từ ngày] - [Đến ngày]) | **Cập nhật:** [Ngày/Tháng/Năm]
> **Đội ngũ thực hiện:** Web Platform
> **Nguồn dữ liệu:** GA4 Data API (Property 270743103), BigQuery Data Warehouse, AppsFlyer GPD Attribution Engine, MoSpark CMS.

---

## I. TỔNG QUAN HIỆU SUẤT TUẦN & TÁC ĐỘNG KINH DOANH

### 1. Tổng quan hiệu suất (Overview)
- **Tổng lưu lượng so với mục tiêu (Total PageViews vs. Target):** Đạt **[Số] PageViews** MTD [Số] ngày, hoàn thành **[X]%** kế hoạch tháng ([Số] PageViews); nhịp MTD đạt **[Số] PageViews/ngày**, riêng 7 ngày gần nhất ([Từ ngày] - [Đến ngày]) đạt **[Số] PageViews/ngày**, tăng/giảm **[+/-]%** so với tuần trước. Tiến độ so với thời gian trôi qua; nhịp dự báo cuối tháng và số PageViews/ngày cần thiết để về đích.
- **Lưu lượng tự nhiên (Non-Paid Traffic):** Chiếm **[X]%** toàn Website (**[Số] PageViews**), tiếp tục là trụ cột dẫn dắt với Organic Search đóng góp **[Số] PageViews** ([X]%) và Direct đạt **[Số] PageViews** ([X]%).
- **Tìm kiếm AI (AI Traffic / GEO):** Ghi nhận **[Số] PageViews** từ các công cụ AI (ChatGPT, Perplexity, Gemini); nhịp bình quân đạt **[Số] PageViews/ngày** nhờ tối ưu cấu trúc dữ liệu Schema và trích dẫn chuyên môn.
- **Phễu chuyển đổi Web-to-App (Install ➔ MAU, AppsFlyer MTD):** Ghi nhận **[Số] lượt cài đặt mới (App Installs)**, chuyển đổi thành **[Số] tài khoản đăng ký (New Reg)**, **[Số] liên kết ngân hàng (Map Bank)** và **[Số] người dùng kích hoạt (Active MAU)**; tỷ lệ chuyển đổi trọn phễu (End-to-End CVR) đạt **[X]%**.

### 2. Cơ cấu kênh lưu lượng qua các tháng (Tháng [X] đến MTD [Ngày/Tháng])

| Kênh lưu lượng (Nguồn dữ liệu chuẩn) | Tháng N-4 | Tháng N-3 | Tháng N-2 | Tháng N-1 | Tháng N (MTD) | Tỷ Trọng Kỳ Này (%) | Nhận định Xu Hướng & Tín Hiệu Điều Hành |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **KÊNH TỰ NHIÊN (NON-PAID)** | **[Số]** | **[Số]** | **[Số]** | **[Số]** | **[Số]** | **[Tỷ trọng]%** | **Trụ cột tăng trưởng bền vững, luôn giữ vị thế đầu tàu (70 - 88% quy mô)** |
| - Organic Search | [Số] | [Số] | [Số] | [Số] | [Số] | [Tỷ trọng]% | Lưu lượng tìm kiếm tự nhiên chủ lực |
| - Direct Traffic | [Số] | [Số] | [Số] | [Số] | [Số] | [Tỷ trọng]% | Thói quen truy cập tiện ích trực tiếp |
| - Referral | [Số] | [Số] | [Số] | [Số] | [Số] | [Tỷ trọng]% | Đóng góp từ đối tác, in-app và mạng xã hội |
| - AI Search (GEO) | [Số] | [Số] | [Số] | [Số] | [Số] | [Tỷ trọng]% | Lưu lượng trích dẫn từ ChatGPT, Gemini, Copilot |
| **KÊNH TRẢ PHÍ (PAID ADS)** | **[Số]** | **[Số]** | **[Số]** | **[Số]** | **[Số]** | **[Tỷ trọng]%** | Ngân sách quảng cáo có chọn lọc dẫn dòng chuyển đổi |
| **TỔNG LƯỢNG TRUY CẬP** | **[Số]** | **[Số]** | **[Số]** | **[Số]** | **[Số]** | **100,0%** | Nhịp ngày bình quân toàn Website đạt [Số] PageViews/ngày |

### 3. Tiến độ mục tiêu các Hub (Hub Targets & Actual MTD)

| Danh mục Hub / Dự án | Target Tháng | MTD Thực Tế | Tiến Độ (%) | Tỷ Trọng Toàn Web (%) | Trạng Thái Vận Hành & Đánh Giá Nhịp Chạy |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Cinema Hub** | [Target] | [Actual] | [Pacing]% | [Share]% | [Đánh giá nhịp chạy, nguyên nhân tăng/chậm] |
| **Financial Hub** | [Target] | [Actual] | [Pacing]% | [Share]% | [Đánh giá nhịp chạy, đóng góp từ công cụ tiện ích] |
| **Vehicle Hub** | [Target] | [Actual] | [Pacing]% | [Share]% | [Đánh giá nhịp chạy tra cứu phạt nguội 0-CAPTCHA] |
| **Dự án New User** | [Target] | [Actual] | [Pacing]% | [Share]% | [Đánh giá cổng /tai-app và chiến dịch kích hoạt] |

### 4. Tiến trình chuyển đổi Web-to-App qua các tháng (AppsFlyer GPD Funnel)

| Kỳ dữ liệu | Installs | New Reg | Tỷ lệ Reg / Install | Map Bank | Tỷ lệ Map / Install | Active MAU | End-to-End CVR (MAU / Install) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Tháng N-3 | [Số] | [Số] | [%] | [Số] | [%] | [Số] | [%] |
| Tháng N-2 | [Số] | [Số] | [%] | [Số] | [%] | [Số] | [%] |
| Tháng N-1 | [Số] | [Số] | [%] | [Số] | [%] | [Số] | [%] |
| Tháng N (MTD) | [Số] | [Số] | [%] | [Số] | [%] | [Số] | [%] |

---

## II. TIẾN ĐỘ THỰC TẾ CÁC DỰ ÁN CHIẾN LƯỢC (HUBS DEEP-DIVE)

### 1. Cinema Hub [R]: Web mang về [Số] PageViews, kéo về [Số] lượt cài app mới và đạt tỷ lệ chuyển đổi sang MAU [X]%
> **Hoàn thành [X]% kế hoạch tháng; tỷ lệ chuyển đổi sang MAU dẫn đầu toàn bộ hệ thống Web.**

#### a. Key Highlights & Business Impact
- **Phễu chuyển đổi (GA4 & AppsFlyer):**
  - *Bước 1 (Traffic Web):* **[Số] PageViews** | Chiếm [X]% lưu lượng toàn Hub; cụm rạp đối tác đóng góp [X]%.
  - *Bước 2 (Trang Lịch Chiếu / Cụm Rạp):* **[Số] PageViews** | Tỷ lệ đi tiếp vào phễu đặt vé đạt [X]%.
  - *Bước 3 (Click Mở App / Đặt Vé):* **[Số] Clicks** | Tỷ lệ nhấp CTA đạt [X]% trên trang lịch chiếu.
  - *Bước 4 (Chuyển Đổi App Thực Tế):* **[Số] Installs**, **[Số] New Reg**, **[Số] Active MAU**; CVR Install ➔ MAU đạt **[X]%**.
- **Tiến độ kỹ thuật:** Hoàn tất nghiệm thu kỹ thuật và đưa vào vận hành [Tính năng/Trang] trên Production.
- **Điểm nghẽn (Lowlights):** [Nêu thẳng thắn sự cạnh tranh thứ hạng từ khóa, tỷ lệ rơi rớt, hoặc độ hụt so với kỳ vọng kèm nguyên nhân gốc rễ].

#### b. Phối hợp liên đội ngũ (Collaboration)
- **BU Movies:** [Nội dung làm việc, thống nhất ngân sách hoặc tài trợ].
- **Dự án đầu tư / Ngân sách:** Triển khai gói Pilot Off-Page SEO [Số tiền] triệu VNĐ (BU Movies tài trợ [X]%).

#### c. Kế hoạch hành động 7 ngày tới
- [Hành động cụ thể 1: Ký hợp đồng, triển khai kỹ thuật, rà soát SEO].
- [Hành động cụ thể 2: Tối ưu trang nội dung, liên kết nội bộ].
- [Hành động cụ thể 3: Đo lường và đối soát tỷ lệ chuyển đổi].

---

### 2. Financial Hub [R]: Web mang về [Số] PageViews và kích hoạt [Số] lượt chuyển đổi về app (Điểm Tín Dụng dẫn đầu [Số] clicks)
> **Hoàn thành [X]% kế hoạch tháng; các công cụ tiện ích tương tác chiếm [X]% tổng lượng chuyển đổi.**

#### a. Key Highlights & Business Impact
- **Phễu chuyển đổi công cụ tiện ích:**
  - *Bước 1 (Traffic Hub):* **[Số] PageViews** | Tỷ trọng Non-Paid đạt [X]%.
  - *Bước 2 (Tương Tác Công Cụ):* Công cụ Tính Lương đạt CTR tương tác **[X]%**; bài viết cẩm nang tĩnh đạt **[X]% CTR**.
  - *Bước 3 (Click Chuyển Tiếp OneLink về App):* **[Số] clicks** (Trích xuất từ dữ liệu kiểm toán BRD: CIC [Số], TTTC [Số], VTS [Số], Vay Nhanh [Số] clicks); tỷ lệ W2A CVR đạt **[X]%**.
  - *Bước 4 (Chuyển Đổi App):* **[Số] Installs**, **[Số] New Reg**, **[Số] Active MAU**.
- **Tiến độ kỹ thuật:** Ra mắt bộ đôi công cụ Tính Thuế TNCN & Hộ Kinh Doanh; hoàn tất nghiệm thu kỹ thuật Production.
- **Điểm nghẽn (Lowlights):** [Phân tích điểm rơi rớt giữa các bước hoặc rào cản thao tác].

#### b. Phối hợp liên đội ngũ (Collaboration)
- **BU Financial Services & BU Bank:** Phối hợp nghiệm thu kỹ thuật 15 trang chi tiết ngân hàng; chốt quy tắc tính điểm CIC.
- **Media Team:** [Kế hoạch phân bổ ngân sách thử nghiệm].

#### c. Kế hoạch hành động 7 ngày tới
- [Hành động cụ thể 1: Đẩy mạnh liên kết nội bộ sang các công cụ tính thuế].
- [Hành động cụ thể 2: Hoàn tất nghiệm thu kỹ thuật (UAT) 15 trang chi tiết ngân hàng cùng BU Bank].
- [Hành động cụ thể 3: Triển khai kịch bản Gamification tương tác].

---

### 3. Vehicle Hub [R]: Đạt [Số] PageViews ([X]% target), phễu tra cứu ghi nhận [Số] lượt tra cứu và [Số] lượt mở app in-app
> **Tiện ích tra cứu phạt nguội 0-CAPTCHA tạo động lực tăng trưởng; tỷ lệ chuyển tiếp mở app đạt [X]%.**

#### a. Key Highlights & Business Impact
- **Phễu tra cứu (GA4):**
  - *Bước 1 (Traffic trang tra cứu):* **[Số] PageViews** | PageViews của 2 trang xe máy và ô tô.
  - *Bước 2 (Thao Tác Hoàn Tất Tra Cứu):* **[Số] lượt form_submit** | Tỷ lệ tra cứu trên PageViews đạt [X]%.
  - *Bước 3 (Chuyển Tiếp Mở App In-App):* **[Số] click_to_app** | Tỷ lệ chuyển tiếp đạt [X]% trên lượt tra cứu.
- **Tốc độ tăng trưởng:** Nhịp bình quân [Số] PageViews/ngày; tiến độ vượt nhịp thời gian.
- **Điểm nghẽn (Lowlights):** Tỷ lệ chuyển đổi sang thanh toán còn thấp; cần bổ sung cảnh báo thời hạn xử lý.

#### b. Phối hợp liên đội ngũ (Collaboration)
- **Khối CSGT / VTTI:** Duy trì luồng kết nối API ổn định, mở rộng kênh thông báo vi phạm.

#### c. Kế hoạch hành động 7 ngày tới
- [Hành động cụ thể 1: Tối ưu giao diện hiển thị kết quả và khối cảnh báo nộp phạt].
- [Hành động cụ thể 2: Thử nghiệm biến thể CTA nộp phạt trực tiếp trên Mobile].

---

### 4. Dự án New User [R]: Web mang về [Số] lượt cài app mới, tạo ra [Số] tài khoản đăng ký và [Số] người dùng liên kết ngân hàng
> **Đóng góp [X]% tổng lượng cài đặt mới toàn Website; cổng tải app tập trung cải thiện trải nghiệm chuyển đổi.**

#### a. Key Highlights & Business Impact
- **So sánh cổng tải app (`/tai-app` vs `/download`):**
  - Cổng `/tai-app` đạt **[Số] PageViews**, tỷ lệ người dùng mới lần đầu (First Visits) đạt **[X]%**, thời gian trên trang **[Số]s** (so với 0,5s của `/download`).
  - Giao diện máy tính (Desktop) chiếm **[X]%** lượng truy cập, kích hoạt quét mã Dynamic QR trực tiếp.
  - Từ khóa tìm kiếm tải file APK đạt thứ hạng Top [X] trên Google Search.
- **Điểm nghẽn (Lowlights):** Tỷ lệ chuyển đổi từ cài đặt sang đăng ký (Install ➔ Reg) bị suy giảm [X] điểm %; cần gói ưu đãi đủ mạnh để kích hoạt.

#### b. Phối hợp liên đội ngũ (Collaboration)
- **Growth & Media Team:** Phối hợp triển khai chiến dịch "Gói Quà tự chọn cho người dùng mới" với ngân sách [Số] triệu VNĐ.

#### c. Kế hoạch hành động 7 ngày tới
- [Hành động cụ thể 1: Cấu hình chuyển hướng từ `/download` sang `/tai-app` trên toàn bộ Header, Footer và Banner].
- [Hành động cụ thể 2: Tối ưu khối hướng dẫn cài đặt file APK trên trang `/tai-app`].
- [Hành động cụ thể 3: Hoàn tất nghiệm thu kỹ thuật và chuẩn bị kích hoạt Minigame kéo tệp người dùng đăng ký mới].

---

## III. KẾT LUẬN & ĐỀ XUẤT HÀNH ĐỘNG TOÀN KÊNH WEB [D]

Kế hoạch hành động 7 ngày tới bám sát 3 bài học từ dữ liệu tuần:

| Bài học thực tế | Bằng chứng đối soát | Kế hoạch hành động 7 ngày tới |
| :--- | :--- | :--- |
| **1. Công cụ tiện ích (PLG) tạo chuyển đổi vượt trội so với bài viết tĩnh** | [Con số chứng minh chênh lệch CTR hoặc lượng clicks giữa công cụ tương tác và bài viết cẩm nang tĩnh]. | **[Hành động trọng tâm: Đẩy mạnh liên kết nội bộ, mở rộng công cụ tính toán].** |
| **2. Kênh tự nhiên giữ vững quy mô, tạo nền tảng vững chắc cho đợt cao điểm** | [Con số chứng minh tỷ trọng Non-Paid và nhịp ngày tăng trưởng ổn định]. | **[Hành động trọng tâm: Tối ưu hóa tỷ lệ chuyển đổi từng trang đích, gom phễu về /tai-app].** |
| **3. Cạnh tranh từ khóa mùa cao điểm đe dọa thứ hạng Top 3** | [Dữ liệu thứ hạng từ khóa bị đe dọa và tỷ trọng đóng góp của mảng liên quan]. | **[Hành động trọng tâm: Ký kết và triển khai các gói Off-Page thẩm quyền kịp thời].** |

---

- **Ghi chú nguồn số liệu:** GA4 (PageViews, kênh, Hub) là MTD [Số] ngày [Từ ngày] - [Đến ngày]; phễu W2A AppsFlyer là MTD [Số] ngày [Từ ngày] - [Đến ngày] do trễ đối soát attribution.
- **Ngân sách Media:** Duy trì gói [Số] triệu VNĐ cho chiến dịch Gói Quà tự chọn New User.
```

---

## 5. MẪU BÁO CÁO THÁNG DÀNH CHO ANH TƯỜNG (MONTHLY TEMPLATE)

```markdown
# BÁO CÁO TỔNG QUAN THÁNG - WEB PLATFORM
**Tháng:** [Tháng/Năm] | **Khung Mục Tiêu Năm 2026:** Kịch bản Cơ sở 5M MUV - Kịch bản Bùng nổ 6M MUV

## 1. SỨC KHỎE PHỄU TOÀN DIỆN (FULL-FUNNEL TRACKING - 6 MONTHS)

| Chỉ Số Đo Lường | Tháng 03 | Tháng 04 | Tháng 05 | Tháng 06 | Tháng 07 | MoM (%) | YoY (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TẦNG WEB METRICS** | | | | | | | |
| Page Views (Attention) | 3.221.705 | 2.699.883 | 3.273.707 | 3.311.429 | 3.167.821 | -4.3% | +18.5% |
| Sessions (Attention) | 2.347.190 | 1.859.048 | 2.330.499 | 2.451.799 | 2.617.774 | +6.7% | +24.1% |
| MEU (Interest) | 1.686.392 | 1.427.165 | 1.706.739 | 1.675.301 | 1.728.912 | +3.2% | +21.0% |
| Click-to-App (Desire) | -- | -- | 964.893 | 824.309 | 713.318 | -13.4% | -- |
| **TẦNG APP IMPACT** | | | | | | | |
| Login App (W2A Users) | -- | -- | 180.148 | 248.468 | 224.162 | -9.8% | +35.2% |
| New Install (Appsflyer) | -- | -- | 1.737 | 4.486 | 5.242 | +16.9% | +180.0% |
| CVR (MEU -> New Install) | -- | -- | 0.10% | 0.27% | 0.30% | +0.03pp | +0.20pp |

> **Observation:** 
> 1. Sessions tăng +6.7% và MEU tăng +3.2% chứng minh chất lượng lưu lượng truy cập cải thiện dù Pageviews giảm nhẹ; Organic Search tăng trưởng +14.5% bù đắp hiệu quả cho Paid Search.
> 2. Lượng cài đặt mới (New Install) tăng trưởng liên tục 3 tháng, đạt 5.242 lượt (+16.9% MoM) nhờ tối ưu hóa các điểm chạm dẫn dắt gói quà người dùng mới.
> 
> **Problem Statement:** 
> 1. Làm thế nào để mở rộng CVR từ MEU sang New Install từ mốc 0.30% lên mốc 1.00% (tương đương ~17.000 New Installs/tháng) thông qua mô hình "Trải nghiệm trước, Cài đặt sau"?
> 2. Làm thế nào để duy trì đà tăng trưởng tự nhiên (Organic) trong bối cảnh các công cụ tìm kiếm AI (AI Overview) làm sụt giảm CTR chung của thị trường?

---

## 2. TIẾN ĐỘ 5 DỰ ÁN CHIẾN LƯỢC THEO MÔ HÌNH 4 ZONE

| Phân Vùng | Dự Án Chiến Lược | Mục Tiêu Kênh Web | Mục Tiêu Tác Động App | Tình Trạng Thực Thi & Kết Quả |
| :--- | :--- | :--- | :--- | :--- |
| **Performance** | Cinema Hub | 8.0M Pageviews<br/>1.7M Clicks | 76K Login App<br/>214K Vé bán | Đang tái cấu trúc sang MoSpark; thử nghiệm luồng thanh toán QR trực tiếp ngoài Web. |
| **Transformation**| Vehicle Hub | 500K Traffic<br/>50% W2A CR | 250K Login App<br/>100K Hồ sơ xe | Phạt Nguội đạt 267K views; chuẩn bị ra mắt Master Page `/tien-ich-giao-thong` và Spoke Giá Xăng. |
| **Transformation**| Financial Hub | 1.0M Traffic<br/>50% W2A CR | 500K MEU In-App<br/>Đón sóng 8M CIC | Hoàn tất đóng gói 4 công cụ (CIC, Vay Nhanh, VTS, Bảo hiểm); chuẩn bị chiến dịch CIC toàn dân. |
| **Incubator** | Student Pass Hub | 500K Traffic (Peak) | 15K Sinh viên định danh | Xây dựng cổng cẩm nang trường đại học; triển khai thử nghiệm tại 5 trường trọng điểm TP.HCM. |
| **Incubator** | New User Hub | TBU | 30K New Installs/tháng | Vận hành mô hình Utility Store; kết hợp gói quà CHAOMOMO giảm rào cản chuyển đổi. |

---

## 3. NĂNG LỰC NỀN TẢNG MOSPARK & TỰ ĐỘNG HÓA VẬN HÀNH

- **GenAI Content Pipeline:** Sản xuất [Số] bài viết/tháng; thời gian sản xuất 4-5 phút/bài; chi phí 7.000 - 20.000 VNĐ/bài; giải phóng 90% thời gian vận hành thủ công so với trước đây.
- **Landing Page Builder & Self-serve:** Triển khai mô hình tự phục vụ cho các BU; chuẩn hóa [Số] mẫu template có sẵn (chiếm 37% nhu cầu); rút ngắn thời gian khởi tạo trang từ 1-2 tuần xuống còn 1-2 ngày.
- **Hệ Thống Kiểm Soát Chất Lượng (Guardrails):** Tích hợp bộ lọc tự động kiểm tra tiêu chuẩn SEO/Compliance trước khi cho phép xuất bản trang, bảo vệ uy tín tên miền `momo.vn`.

---

## 4. PHỐI HỢP LIÊN PHÒNG BAN & HỖ TRỢ CHIẾN LƯỢC (CROSS-TEAM COLLABORATION)

- **Executive Leadership / Ban Giám Đốc:** Định hướng phê duyệt chủ trương liên kết dữ liệu với C08 và Cổng Dịch vụ công Quốc gia để xử lý luồng nộp phạt vi phạm giao thông và xuất biên lai điện tử.
- **Inbound Team (BMC):** Tiếp nhận vai trò điều phối và chịu trách nhiệm toàn diện về chất lượng nội dung, phê duyệt xuất bản theo mô hình Agency nội bộ.
- **Các Business Units (BUs):** Đăng ký chỉ tiêu kinh doanh cụ thể (Single Ownership KPI) trước khi yêu cầu triển khai các dự án Custom Landing Page.

---

## 5. KẾ HOẠCH HÀNH ĐỘNG 30 NGÀY TỚI (PRIORITIES FOR NEXT 30 DAYS)

| Nhóm Dự Án | Thời Gian | Tên Hạng Mục | Chi Tiết Triển Khai & Mục Tiêu |
| :--- | :--- | :--- | :--- |
| **Performance** | Tháng 08/2026 | Tối ưu Cinema Booking | Mở rộng thanh toán QR Web trực tiếp; tích hợp Deep Linking cho lịch chiếu phim. |
| **Transformation** | Tháng 08/2026 | Ra mắt Master Giao Thông | Go-live `/tien-ich-giao-thong` và Spoke Giá Xăng; tích hợp khối bán chéo Bảo hiểm Ô tô/Xe máy. |
| **Transformation** | Tháng 08/2026 | Hoàn thiện Financial Hub | Tích hợp bộ giả lập tài chính vào các bài viết cẩm nang; thử nghiệm luồng tính điểm CIC. |
| **Incubator** | Tháng 08/2026 | Thử nghiệm Student Pass | Ra mắt chuyên trang Review Trường Học; kích hoạt mạng lưới đại sứ sinh viên. |
| **Platform & AI** | Tháng 08/2026 | Nâng cấp MoSpark Engine | Nâng công suất GenAI lên 150 bài/tháng; mở rộng phân quyền Self-serve cho Cell Teams. |
```

---

## 7. BỘ FRAMEWORK QUẢN TRỊ KỊCH BẢN 4M PAGE VIEWS & BỘ CHỈ SỐ QUẢN TRỊ

> **Mục tiêu North Star:** Kịch bản bứt phá tổng lưu lượng Web Platform về mốc **4.000.000 Page Views vào Tháng 12/2026**.
> **Mẫu bảng tính tham khảo:** [full_month_performance_template.csv](../07_REPORTS/templates/sheets/full_month_performance_template.csv). Workbook framework cũ đã được loại bỏ, không còn là nguồn bắt buộc.

Mọi bài báo cáo Weekly cho Executive Leadership và Monthly cho Ban Giám Đốc **BẮT BUỘC phải áp dụng bộ chỉ số phễu 3 tầng hoàn chỉnh**:

### 7.1. Bộ Chỉ Số Phễu 3 Tầng Chuẩn (Full-Funnel Metric Framework)

| Tầng Phễu | Tên Chỉ Số (Key Metrics) | Công Thức / Nguồn GA4 & AppsFlyer | Ý Nghĩa Quản Trị & Đánh Giá |
| :--- | :--- | :--- | :--- |
| **Đầu Phễu (Traffic & Audience)** | **1. Tổng PageViews** | Tổng PageViews từ TẤT CẢ các nguồn. | Quy mô lưu lượng toàn Website. |
| | **2. Total Users (Unique Visitors)** | Số người dùng duy nhất (`totalUsers` từ GA4). | Quy mô khách thực tế tiếp cận được (tránh ảo số do 1 người F5 tải lại nhiều lần). |
| | **3. PV / User (Độ Sâu Tương Tác)** | `= Tổng Page Views / Total Users` | Mức độ tương tác trung bình (healthy: 1.5 - 2.5 trang/người). |
| | **4. Net Add (Lưu Lượng Mới)** | `Current Month PV - Previous Month PV` | Chỉ báo nỗ lực tạo ra giá trị tăng trưởng mới. |
| | **5. Growth Rate (%)** | `Net Add / Previous Month PV` | Tốc độ tăng trưởng MoM/WoW. |
| | **6. Phân Bổ Kênh (Source Breakdown)** | Tỷ trọng các nhóm kênh: Non-Paid (Organic Search, Direct, Referral, AI Traffic) và Paid Ads. | Phân định kênh sức mạnh chủ lực và kênh suy giảm. |
| | **7. Cơ Cấu Theo Dự Án / Use Case** | Phân bổ theo Cinema Hub, Financial Hub, Vehicle Hub, Home Page, TikTok... | Xác định use case tạo lực đẩy và use case cần tối ưu. |
| **Giữa Phễu (Intent & CTA)** | **8. Click-to-App** | Tổng lượt nhấp vào các nút CTA mở App MoMo. | Đo lường ý định chuyển đổi sang ứng dụng. |
| | **9. Tỷ Lệ %CTR** | `= Click-to-App / Tổng Page Views` | Hiệu quả của thông điệp và vị trí nút bấm CTA. |
| **Cuối Phễu (App Conversion & Growth)** | **10. Login App (Khách Cũ)** | Sự kiện xác thực mở App thành công từ Web. | Mức độ tái kích hoạt người dùng hiện hữu. |
| | **11. Install App** | Lượt tải và cài đặt ứng dụng mới từ Web. | Năng lực kéo người dùng mới ngoài App. |
| | **12. New Registered Users (Mới Tinh)** | Tracking qua AppsFlyer / BigQuery (`first_open` + eKYC). | **KPI Cốt Lõi:** Số người dùng mới hoàn tất đăng ký MoMo lần đầu từ nguồn Web. |
| | **13. Re-install Users (Cài Lại)** | `= Install App - New Registered Users` | Khách cũ từng xóa App nay cài đặt lại. |

### 7.2. Phương Pháp Luận So Sánh Đối Soát (Benchmark Methods)

* **SPLM (Same Period Last Month):** So sánh tuần/tháng hiện tại với cùng kỳ tháng trước (`Vs. SPLM`) để triệt tiêu yếu tố mùa vụ (Seasonal factors), tránh đưa ra nhận định sai lầm do biến động thị trường.
* **FULL MONTH:** Đánh giá bức tranh toàn cảnh cả tháng, đối soát song song giữa số liệu tích lũy lũy kế MTD, số chạy dự báo (Run-rate Forecast) và Target cam kết với BU.

---

## 8. DANH MỤC KIỂM TRA CHẤT LƯỢNG BÁO CÁO (QUALITY CHECKLIST)

Trước khi gửi báo cáo Weekly cho Executive Leadership hoặc Monthly cho Ban Giám Đốc, bắt buộc rà soát hai nhóm.

### Nhóm A: Quy chuẩn công ty (theo [`03_SKILLS/momo-reporting-guidelines.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-guidelines.md))

1. **Mục đích:** Mỗi slide/mục có dòng `Mục đích` nói được trong một câu slide này giúp ai hiểu hoặc quyết định điều gì chưa?
2. **Title:** Chỉ đọc lần lượt các tiêu đề có nắm được toàn bộ câu chuyện báo cáo chưa? Tiêu đề là kết luận kèm số, không phải tên chủ đề, và viết sentence case?
3. **Số ý chính:** Mỗi slide 1-2 ý, tối đa 3 ý chưa? Nhiều hơn thì đã tách slide chưa?
4. **Tag:** Đã gắn `[R]` / `[D]` / `[F]` cho mọi slide chưa? Slide `[D]` có thật sự cần quyết định không?
5. **Độ tin cậy:** Mỗi số liệu có mốc so sánh (Target, kỳ trước), có việc tiếp theo, có nguồn và owner chưa?
6. **Thứ tự deck:** Discussion Topics đứng đầu, có slide Follow-up, Executive Summary có khối `Vấn đề cần cải thiện` chưa?
7. **Ngôn ngữ và cỡ chữ:** Toàn bộ báo cáo một ngôn ngữ, mọi tiêu đề cùng cỡ, mọi nội dung chính cùng cỡ chưa?
8. **Màu số liệu:** Đã tô theo mức đạt Target (xanh >= 100%, cam 90-99%, đỏ < 90%) chứ không tô theo biến động MoM chưa?

### Nhóm B: Đặc thù Web Platform

1. Đã xóa bỏ 100% Emoji / Icon trong toàn bộ tiêu đề, bảng biểu và danh sách chưa?
2. Đã thay thế toàn bộ tên riêng cá nhân/PIC bằng tên đội ngũ chuyên môn chưa?
3. Đã có đầy đủ 3 khối chuẩn: `Key Highlights & Business Impact`, `Collaboration`, `Priority` chưa?
4. Đã áp dụng Bộ Chỉ Số Phễu 3 Tầng (`Total PV`, `Total Users`, `PV/User`, `Click-to-App`, `Login`, `Install`, `New Registered Users`) chưa?
5. Đã tuân thủ chuẩn 4 kênh Non-Paid (Organic Search, Direct, Referral, AI Traffic) và gộp toàn bộ nguồn vãng lai vào Referral mà không tách dòng `Others` chưa?
6. Đã đối chiếu số liệu theo 2 tầng: Kênh Web và Tác động App chưa?
7. Các bảng số liệu lớn đã có 2 khối `Observation` và `Problem Statement` ở chân trang chưa?
8. Kế hoạch hành động đã được phân loại theo đúng nhóm phân vùng (Performance / Transformation / Incubator) chưa?

