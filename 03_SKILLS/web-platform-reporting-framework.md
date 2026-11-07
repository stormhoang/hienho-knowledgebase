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

## 4. MẪU BÁO CÁO TUẦN DÀNH CHO ANH CÔNG (WEEKLY TEMPLATE)

```markdown
# BÁO CÁO TIẾN ĐỘ TUẦN - WEB PLATFORM
**Tuần:** [Số tuần] | **Thời gian:** [Từ ngày] - [Đến ngày]

## 1. BẢNG CHỈ SỐ VẬN HÀNH TUẦN (WEEKLY PERFORMANCE)

| Nhóm Chỉ Số | Tuần Trước | Tuần Này | Biến Động (WoW) | Mục Tiêu Tuần | Trạng Thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Page Views (Lượt xem) | 750.000 | 820.000 | +9.3% | 800.000 | Đạt |
| Sessions (Phiên truy cập) | 580.000 | 630.000 | +8.6% | 600.000 | Đạt |
| MEU (Người dùng Web) | 410.000 | 445.000 | +8.5% | 420.000 | Đạt |
| Tỷ lệ nhấp CTA (% CTR) | 12.4% | 14.1% | +1.7pp | 13.0% | Đạt |
| Login App từ Web (W2A) | 52.000 | 58.500 | +12.5% | 55.000 | Đạt |
| Lượt cài đặt mới (Install) | 1.100 | 1.350 | +22.7% | 1.200 | Đạt |

## 2. TIẾN ĐỘ & TÁC ĐỘNG KINH DOANH (KEY HIGHLIGHTS & BUSINESS IMPACT)

- **Phễu Chuyển Đổi Web-to-App:** Lượt cài đặt mới tăng trưởng +22.7% WoW nhờ triển khai tối ưu nội dung banner gói quà CHAOMOMO trên các trang có lưu lượng cao. Tỷ lệ chuyển đổi CTA sang Login App duy trì ở mức 14.1%.
- **Vận Hành MoSpark Platform:** Phát hành thành công [Số] bài viết chuẩn SEO/GEO qua GenAI Pipeline, kiểm duyệt hoàn tất trong 20 phút/bài; ghi nhận [Số] từ khóa lọt Top 5 Google Search.
- **Tối Ưu Trải Nghiệm Kỹ Thuật:** Triển khai cơ chế 0-CAPTCHA cho công cụ Tra cứu Phạt nguội, nâng tỷ lệ hoàn tất tra cứu từ 75.0% lên 78.2%, giảm 45% thời gian phản hồi máy chủ.

## 3. PHỐI HỢP LIÊN ĐỘI NGŨ (CROSS-TEAM COLLABORATION & SUPPORT NEEDED)

- **VTTI BU:** Cần thống nhất luồng liên kết đối tác ePass/Đăng kiểm trước ngày [Ngày/Tháng] để kịp tích hợp vào Master Page Tiện Ích Giao Thông.
- **Risk Team:** Cần phê duyệt bộ tiêu chí Guardrails tự động cho module CMS trước khi mở rộng phân quyền Self-service cho BU.
- **Media Team:** Đề xuất bổ sung ngân sách Paid Search cho nhóm từ khóa vé xem phim dịp cuối tuần.

## 4. KẾ HOẠCH TRỌNG TÂM 7 NGÀY TỚI (PRIORITIES FOR NEXT 7 DAYS)

- **Hotfix & Delivery:** Bàn giao giao diện Master Page `/tien-ich-giao-thong` cho đội phát triển Front-end; hoàn thành kiểm thử trên môi trường Staging.
- **A/B Testing:** Chạy thử nghiệm 2 biến thể nút CTA (Đặt vé ngay vs. Nhận ưu đãi vé) trên Cinema Hub để đo lường CVR.
- **Cross-team Alignment:** Họp chi tiết với Inbound Team (BMC) để chuyển giao quy trình kiểm duyệt nội dung tự động.
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
| **Đầu Phễu (Traffic & Audience)** | **1. Tổng Page Views** | Tổng lượt xem trang từ TẤT CẢ các nguồn. | Quy mô lưu lượng toàn sàn. |
| | **2. Total Users (Unique Visitors)** | Số người dùng duy nhất (`totalUsers` từ GA4). | Quy mô khách thực tế tiếp cận được (tránh ảo số do 1 người F5 tải lại nhiều lần). |
| | **3. PV / User (Độ Sâu Tương Tác)** | `= Tổng Page Views / Total Users` | Mức độ tương tác trung bình (healthy: 1.5 - 2.5 trang/người). |
| | **4. Net Add (Lưu Lượng Mới)** | `Current Month PV - Previous Month PV` | Chỉ báo nỗ lực tạo ra giá trị tăng trưởng mới. |
| | **5. Growth Rate (%)** | `Net Add / Previous Month PV` | Tốc độ tăng trưởng MoM/WoW. |
| | **6. Phân Bổ Kênh (Source Breakdown)** | Tỷ trọng 6 nhóm kênh: Organic, Paid, Direct, Cross, Referral Domain, Others. | Phân định kênh sức mạnh chủ lực và kênh suy giảm. |
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
5. Đã bóc tách rõ kênh `Referral Domain` (Báo chí PR & Đối tác) khỏi nhóm `Others` chưa?
6. Đã đối chiếu số liệu theo 2 tầng: Kênh Web và Tác động App chưa?
7. Các bảng số liệu lớn đã có 2 khối `Observation` và `Problem Statement` ở chân trang chưa?
8. Kế hoạch hành động đã được phân loại theo đúng nhóm phân vùng (Performance / Transformation / Incubator) chưa?

