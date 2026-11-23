---
name: web-platform-engineer-weekly-report
description: Quy chuẩn và hướng dẫn tự động tạo Báo cáo Tuần cấp Kỹ sư (Engineer Weekly Report) cho Web Platform MoMo. Hướng dẫn AI Agent phân tích git log, git diff, commit và PR để tự động biên soạn báo cáo 5 phần chuẩn mực W46, tuân thủ 100% Glossary MoMo, không bịa số liệu và đính kèm đầy đủ link môi trường thực tế.
---

# SKILL: HƯỚNG DẪN VIẾT BÁO CÁO TUẦN CHUẨN TECH LEAD CHO KỸ SƯ WEB PLATFORM (CHUẨN W46)

> **Mục đích:** Tài liệu này là **Skill duy nhất** dùng để hướng dẫn Kỹ sư hoặc cấp trực tiếp cho các Trợ lý AI (Cursor, Claude Code, Antigravity, ChatGPT, Gemini CLI...) tự động trích xuất thông tin từ công việc tuần qua và biên soạn thành **Báo cáo Tuần chuẩn mực cấp Tech Lead / Product Lead**, sẵn sàng nộp vào thư mục báo cáo tuần của Web Platform mà không cần biên tập lại.

---

## 1. HƯỚNG DẪN NHANH DÀNH CHO KỸ SƯ (QUICK START FOR ENGINEERS)

Kỹ sư chỉ cần sao chép toàn bộ tài liệu này, đưa vào AI Agent đang làm việc cùng mình (hoặc thêm vào file luật `.cursorrules`, `CLAUDE.md`, `.agents/skills/`), rồi chạy câu lệnh mẫu sau:

### Câu Lệnh Mẫu Cho Kỹ Sư (Prompt to Agent):
```text
Đọc kỹ file SKILL này. Dựa trên git log tuần qua, git diff, danh sách commit và các đầu việc tôi đã làm trong tuần này, hãy tự động viết Báo cáo Tuần của tôi theo đúng cấu trúc chuẩn W46 trong tài liệu này.

Thông tin của tôi:
- Tên đăng nhập: <username> (ví dụ: hung.nguyen9, thuan.vo, duy.tran2, anh.dang, loc.le4, nhat.bui1, hieu.nguyen8, hoan.tran2, trong.tran2)
- Tuần báo cáo: Tuần <Số tuần> (<Ngày bắt đầu> - <Ngày kết thúc>)
- Mảng / Dự án phụ trách: <Tên dự án, Hub hoặc Module>

Yêu cầu Agent:
1. Đọc git log/diff để lấy đúng các file đã sửa, logic đã làm, test cases đã pass.
2. Tuân thủ nghiêm ngặt cấu trúc 5 khối và bảng tổng hợp đầu việc.
3. Tuân thủ 100% quy chuẩn từ ngữ Glossary MoMo (không dùng từ cấm, không emoji, không en/em dash, không nhãn P0-P3).
4. Đính kèm đầy đủ link Staging, Production và tài liệu thực tế.
```

---

## 2. QUY TRÌNH 4 BƯỚC DÀNH CHO AI AGENT (AGENT WORKFLOW)

Khi nhận được yêu cầu viết báo cáo tuần từ Kỹ sư, AI Agent phải thực hiện tuần tự 4 bước sau:

### Bước 1: Thu thập dữ liệu thực tế từ hệ thống (Zero Hallucination)
- Chạy `git log --since="7 days ago" --oneline` để xem danh sách commit trong 7 ngày qua.
- Chạy `git status` và `git diff HEAD~5` để nắm các file, component, API, migration hoặc script đã tạo/chỉnh sửa.
- Thu thập các đường link thực tế từ code hoặc config: link Staging (`momo-stg.mservice.io/...`), link Production (`momo.vn/...` hoặc `mospark.mservice.io/...`), link Admin (`adminweb.momocdn.net/...`).
- Thu thập bằng chứng số liệu: số test cases đã pass, số bản ghi database, độ trễ tối ưu được, số lượt click/tương tác đo được từ Umami hoặc GA4 nếu có.

### Bước 2: Phân bổ vào Cấu Trúc 5 Khối Chuẩn W46
Mỗi dự án/module kỹ thuật phụ trách bắt buộc phải có đầy đủ 5 khối thông tin:
1. **Tiêu đề Module & Key Owner & Liên kết thực tế (Demo & Docs)**
2. **Mục tiêu & Bối cảnh kinh doanh (Objectives & Business Context)**
3. **Tiến độ thực tế & Giải pháp kỹ thuật trong tuần (Discuss & Tasks)**
4. **Kế hoạch 7 ngày tới (Next Actions)**
5. **Phối hợp liên đội ngũ (Cross-team Collaboration)**

### Bước 3: Tổng hợp Bảng đầu việc kỹ thuật tuần (Task Summary Table)
Cuối báo cáo bắt buộc có bảng tổng hợp 4 cột:
`Mô-đun / Hạng mục | Đầu việc kỹ thuật | Trạng thái (Done/Next) | Kết quả cụ thể`.

### Bước 4: Kiểm duyệt chuẩn mực từ ngữ (Glossary & Formatting Guard)
- Kiểm tra toàn bộ bài viết không vi phạm bảng từ ngữ cấm kỵ ở Mục 4.
- Đảm bảo không có bất kỳ ký tự En Dash (`–`, U+2013) hoặc Em Dash (`—`, U+2014); chỉ dùng Hyphen `-` (U+002D) cho khoảng số.
- Đảm bảo không có nhãn ưu tiên `P0`, `P1`, `P2`, `P3`.
- Đảm bảo không có emoji / icon trang trí.

---

## 3. CẤU TRÚC CHI TIẾT 5 KHỐI BÁO CÁO CHUẨN W46

### Khối 1: Tiêu Đề & Thông Tin Định Danh
```markdown
### [Số thứ tự]. [Tên Dự Án Kỹ Thuật / Tính Năng / Hub]: [Tiêu Đề Hành Động Phản Ánh Trọng Tâm]
- **Key Owner:** <username> | **Phối hợp:** <Tên BU / Đội ngũ phối hợp>
- **Liên kết Demo & Tài liệu:** (Bắt buộc đính kèm link thật để đối soát, không để trống)
  - *Môi trường Staging/Dev:* [Đường dẫn link staging]
  - *Môi trường Production:* [Đường dẫn link production]
  - *Tài liệu kỹ thuật / PRD:* [Đường dẫn file tài liệu hoặc PR]
```

### Khối 2: Mục Tiêu & Bối Cảnh Nghiệp Vụ (Objectives & Business Context)
- **Mục tiêu định lượng:** Nêu rõ giải quyết bài toán gì, giảm tải bao nhiêu %, tăng CVR bao nhiêu, response time tối ưu thế nào, tỷ lệ chính xác > bao nhiêu %.
- **Bối cảnh kinh doanh (Problem Statement):** Nêu rõ trước đây người dùng hoặc nội bộ gặp trở ngại gì, điểm nghẽn nằm ở đâu, tại sao phải ưu tiên làm tính năng này.

### Khối 3: Tiến Độ Thực Tế & Giải Pháp Kỹ Thuật (Discuss & Tasks)
- **Những việc ĐÃ HOÀN TẤT trong tuần:** Nêu rõ ngày hoàn thành (ví dụ: 10/11, 14/11).
- **Giải pháp kỹ thuật đã chọn:** Nêu cụ thể kiến trúc, cơ chế xử lý (ví dụ: State Machine, RPC bypass PostgREST, Schema ScreeningEvent cho Googlebot, Caching, Token cascading resolution, BFF role `mini_web_server`...).
- **Số liệu kỹ thuật thực chứng:** Số bản ghi đã xử lý, số tình huống test đã đạt (ví dụ: 63/63 test cases đạt 100%), số lượng bài viết, số lượt nhấp (clicks) đo được.
- **Điểm nghẽn kỹ thuật (Lowlights / Blockers):** Nêu trung thực các khó khăn, lỗi phát sinh, sự cố API bên thứ ba hoặc điểm nghẽn đang chờ đội ngũ khác phối hợp.

### Khối 4: Kế Hoạch 7 Ngày Tới (Next Actions)
- Liệt kê các đầu việc cụ thể sẽ thực hiện trong tuần tiếp theo.
- Trình bày theo thứ tự triển khai logic, gạch đầu dòng tự nhiên (tuyệt đối không gắn nhãn P0, P1, P2, P3).
- Mỗi đầu việc nêu rõ kết quả đầu ra dự kiến (Deliverable).

### Khối 5: Phối Hợp Liên Đội Ngũ (Cross-team Collaboration)
- Ghi rõ tên đội ngũ phối hợp kèm vai trò cụ thể:
  - `BU Movies`: phối hợp dữ liệu suất chiếu, cụm rạp đối tác.
  - `Insurtech BU`: phối hợp luồng báo giá và bảo lãnh gara.
  - `Financial Services (FS Team)`: phối hợp API tỷ giá, chứng chỉ quỹ.
  - `ITC Security Team`: phối hợp đánh giá an toàn thông tin, rà soát Pentest.
  - `DevOps Team`: phối hợp hạ tầng, tài nguyên server, CI/CD pipeline.
  - `Content Team / SEO Team`: phối hợp từ khóa, bài viết, xử lý liên kết hỏng.
  - `Legal & Compliance`: phối hợp thẩm định pháp lý và quy chuẩn YMYL.

---

## 4. TỪ ĐIỂN CHUẨN MỰC & QUY TẮC CẤM KỴ (MOMO MASTER GLOSSARY)

Để báo cáo đạt chuẩn C-Suite và Tech Lead, AI Agent BẮT BUỘC tuân thủ bảng đối soát sau:

| Thuật ngữ CẤM dùng ❌ | Thuật ngữ BẮT BUỘC dùng ✅ | Giải thích & Quy chuẩn MoMo |
| :--- | :--- | :--- |
| **Sàn, Sàn Web, Sàn MoMo, Toàn sàn, Toàn site, Toàn trang** | **Nền tảng Web, Kênh Web, Web Platform, toàn Website, momo.vn** | MoMo là ứng dụng tài chính và hệ sinh thái số, không phải sàn thương mại điện tử. |
| **Hoàn, Hoàn Trần (khi nói về nhân sự hoan.tran2)** | **Hoan** hoặc **Hoan Trần** (`hoan.tran2`) | Tên chính xác của nhân sự là **Hoan** (không có dấu huyền). |
| **Bấm nút, Bấm, Nhấp chuột cộc lốc** | **1 click, thao tác một chạm, chạm gọi trực tiếp** | Chuẩn hóa trải nghiệm người dùng số hiện đại. |
| **Phát hành tính năng, Phát hành web** | **Chính thức Go-live, Triển khai lên Production, Ra mắt, Xuất bản** | Từ 'phát hành' là thuật ngữ ngành in ấn/vé số/tài chính. Phần mềm dùng Go-live/Triển khai; bài viết/báo cáo dùng Xuất bản. |
| **Kiểm thử, Kiểm thử thâm nhập** | **Nghiệm thu kỹ thuật (UAT), Đánh giá chất lượng, Chạy test, Pentest** | Bỏ từ dịch thô hành chính cũ; giữ nguyên thuật ngữ kỹ thuật quốc tế chuẩn. |
| **Lượt xem, View cộc lốc** | **PageViews (PV)** | Chuẩn hóa danh từ chỉ số quốc tế trong toàn bộ báo cáo Web Platform. |
| **Động cơ tăng trưởng** | **Đầu tàu tăng trưởng, Cơ chế tăng trưởng (Growth Engine)** | Bỏ từ cơ khí, thay bằng thuật ngữ kinh doanh chuẩn. |
| **Bùng nổ** | **Bứt phá, Tăng trưởng ấn tượng (+X%)** | Tránh từ giật gân, thiếu khách quan. |
| **Phân hệ** | **Mô-đun, Khu vực chức năng, Mảng sản phẩm (Hub)** | Từ 'phân hệ' mang phong cách phần mềm bao cấp thập niên 2000. |
| **Phân rã** | **Cơ cấu, Phân bổ, Bóc tách chi tiết** | 'Phân rã' mang nghĩa phân rã hạt nhân; trong báo cáo dùng cơ cấu/bóc tách. |
| **Nỗi đau, Nỗi đau người dùng** | **Rào cản thao tác, Điểm nghẽn trải nghiệm, Khó khăn của người dùng** | Bỏ lối dịch sến súa, bi kịch hóa. |
| **Thâu tóm, Hứng trọn, Mồi câu** | **Bao phủ thị trường, Đón nhận và tối ưu chuyển đổi, Tiện ích thu hút** | Bỏ từ ngữ quân sự, bẫy khách hàng; dùng thuật ngữ tăng trưởng chuẩn mực. |
| **Chủ trì** | **Điều phối, Đầu mối thực hiện, Chịu trách nhiệm (Owner/Lead)** | Bỏ từ ngữ hành chính bao cấp; dùng ngôn ngữ công nghệ hiện đại. |
| **Dự phóng** | **Dự báo kết tháng (Forecast), Ước tính theo nhịp chạy (Run-rate)** | Bỏ từ Hán-Việt cổ, dùng từ ngữ dự báo kinh doanh chuẩn. |
| **Link generic** | **Đường dẫn dùng chung (Generic link)** | Bổ sung nghĩa tiếng Việt chuẩn mực, tránh chắp vá tiếng Anh cụt lủn. |
| **Feedback** | **Ý kiến phản hồi, Góp ý từ đối tác/BU** | Dùng tiếng Việt hoàn chỉnh trong báo cáo quản trị. |
| **Ký tự En Dash (–) hoặc Em Dash (—)** | **Dấu gạch ngang chuẩn Hyphen (-)** | Quy tắc bàn phím chuẩn; cấm 100% unicode dashes (U+2013, U+2014). |
| **Nhãn ưu tiên P0, P1, P2, P3** | **Danh sách triển khai tự nhiên theo thứ tự logic** | Báo cáo tuần của Kỹ sư trình bày các task mạch lạc, không gán nhãn P0-P3. |
| **Emoji / Icon (🚀, 🔥, ⚠️, ❌, ✅)** | **Văn bản thuần túy, Thẻ trạng thái Markdown `Done`, `In Progress`** | Cấm 100% biểu tượng cảm xúc trong báo cáo kỹ thuật chuyên nghiệp. |

---

## 5. VÍ DỤ MẪU ĐẠT CHUẨN W46 (GOLDEN REFERENCES)

### Ví Dụ 1: Báo Cáo Dự Án Nền Tảng (Platform / Infrastructure)
```markdown
### 1. Security & Hạ Tầng MoMo API (BFF): Kiểm Soát Giới Hạn Record & Triển Khai BFF Đóng Cổng Public Supabase
- **Key Owner:** loc.le4 | **Phối hợp:** hieu.nguyen8, thuan.vo, ITC Security Team, DevOps Team
- **Liên kết Demo & Tài liệu:**
  - *Dịch vụ BFF Node.js:* `momo-web-node-function`
  - *Thư viện dùng chung:* `momo-fe-share-lib` (`lib/bff/`)
  - *Dự án triển khai:* `momo-web-train` và toàn bộ các dự án Mini Web
- **Mục tiêu & Tác động:** Triệt tiêu nguy cơ rò rỉ dữ liệu hàng loạt và lộ cấu trúc cơ sở dữ liệu khi client gọi trực tiếp Supabase qua `anon key` (khóa ẩn danh); chuẩn hóa toàn bộ truy vấn qua tầng trung gian Backend for Frontend (BFF) với role riêng `mini_web_server` để đóng hoàn toàn cổng Supabase public theo tiêu chuẩn an ninh thông tin.
- **Tiến độ thực tế trong tuần (loc.le4):**
  - **Kiểm Soát Trần Dữ Liệu & Vị Trí Bắt Đầu Truy Vấn:** Thiết lập trần số dòng mỗi truy vấn tối đa 100 dòng áp dụng đồng bộ cho bảng, view và RPC; khống chế vị trí bắt đầu (`offset`) mặc định tối đa 300 dòng (vượt quá trả lỗi 400 `OFFSET_TOO_LARGE` ngắt sớm truy vấn nặng); kiểm chứng hàm RPC trả về 1 JSON chạy nhanh gấp 2 lần so với `jsonb`.
  - **Triển Khai & Chuẩn Hóa Kiến Trúc BFF:** Tự động kẹp trần truy vấn vào mọi route BFF mà lập trình viên không cần gọi thêm bước bổ sung; ẩn 100% lỗi từ Supabase khỏi client (chỉ nhận mã lỗi 500 kèm `requestId`, log chi tiết lưu ở server); áp dụng quy tắc ESLint bắt buộc bọc `withApi`.
  - **Đo lường hiệu năng:** Lớp bảo vệ chuẩn hóa chỉ tiêu tốn xấp xỉ 3 micro-giây mỗi truy vấn, hoàn toàn không gây ảnh hưởng đến hiệu năng mạng.
  - **Dọn dẹp mã nguồn:** Gỡ bỏ 11 packages dependencies và 11 packages devDependencies không sử dụng; cập nhật Hotline 028.8888.5555 cho toàn bộ Mini Web; build và triển khai dịch vụ `momo-web-train`.
- **Kế hoạch 7 ngày tới:**
  - Tiếp tục hoàn thiện chuyển đổi các route còn lại sang BFF; rà soát nâng cấp điều kiện bắt buộc bọc `withApi` vào quy trình build.
  - Phối hợp DevOps Team và ITC Security đánh giá an toàn thông tin để chuẩn bị đóng hoàn toàn cổng truy cập public của Supabase trên Production.
- **Phối hợp liên đội ngũ:**
  - **ITC Security Team:** Rà soát kiểm tra an ninh thông tin trước khi đóng cổng public.
  - **DevOps Team:** Giám sát tài nguyên máy chủ và hệ thống log lỗi.
```

### Ví Dụ 2: Báo Cáo Tính Năng Nghiệp Vụ / Hub Sản Phẩm
```markdown
### 2. Vehicle Hub: Bản Đồ Gara Bảo Lãnh & Thẻ Dẫn Nộp Phạt CSGT
- **Key Owner:** thuan.vo | **Phối hợp:** hoan.tran2, VTTI BU, Insurtech BU
- **Liên kết Demo & Tài liệu:**
  - *Cổng Giao thông Production:* https://www.momo.vn/tien-ich-giao-thong
  - *Tra cứu phạt nguội Production:* https://www.momo.vn/phat-nguoi
  - *Bản đồ Garage Production:* https://www.momo.vn/tien-ich-giao-thong/garage
- **Mục tiêu & Tác động:** Giải quyết điểm nghẽn danh sách gara bị rỗng khi khách chọn mua bảo hiểm ô tô thân vỏ; dẫn dắt người dùng tra cứu có lỗi vi phạm sang luồng nộp phạt CSGT để tạo chuyển đổi số trực tiếp.
- **Tiến độ thực tế trong tuần (thuan.vo):**
  - **Sửa Lỗi Danh Sách Gara Bảo Lãnh (10/11):** Xử lý triệt để lỗi so khớp chữ hoa/thường tên hãng xe, ưu tiên xếp gara đối tác bảo lãnh lên đầu danh sách tại `/bao-hiem-o-to/than-vo/xem-bao-gia`.
  - **Nâng Cấp Bản Đồ Gara Tỉnh Thành:** Bản đồ tự động định vị theo tỉnh thành đang chọn, hiển thị ghim nhận diện gara chính hãng và gara thường đồng bộ cho cả cây xăng và trạm sạc.
  - **Thẻ Dẫn Nộp Phạt CSGT Golive Production:** Thẻ "Hướng dẫn nộp phạt CSGT" tại kết quả tra cứu phạt nguội ghi nhận **158 lượt nhấp (clicks)** dẫn sang luồng nộp phạt trong 7 ngày (Ô tô 108, Xe máy 50; tra cứu ô tô 92, tra cứu xe máy 40, trang chính 25).
  - **Tự Tạo Trang Con CMS (12/11):** BU có thể tự tạo trang mới dưới `/tien-ich-giao-thong/*` trên trang quản trị mà không cần kỹ sư dựng trang.
- **Kế hoạch 7 ngày tới:**
  - Đưa vào hoạt động giải pháp giảm ô xác minh captcha (chỉ xác minh 1 lần ở form tra cứu).
  - Đối chiếu 158 lượt nhấp thẻ dẫn nộp phạt với PageViews và tỷ lệ chuyển đổi thanh toán trên trang nộp phạt CSGT.
  - Rà soát tọa độ gara hiển thị sai trên Production.
- **Phối hợp liên đội ngũ:**
  - **Insurtech BU:** Thử nghiệm nhúng tiện ích bảo hiểm TNDS bắt buộc tại trang kết quả tra cứu không có lỗi.
  - **Backend Team:** Phối hợp kết nối API tra phạt nguội tại thẻ Liên kết xe.
```

---

## 6. MẪU KHUNG BÁO CÁO HOÀN CHỈNH ĐỂ AGENT TỰ ĐỘNG ĐIỀN

```markdown
# BÁO CÁO CÔNG VIỆC TUẦN [Số tuần] ([Ngày/Tháng] - [Ngày/Tháng/Năm])

**Key Owner:** [username]  
**Phạm vi phụ trách:** [Tên Dự Án / Hub / Module Kỹ Thuật]  
**Trọng tâm tuần:** [Tóm tắt 1 câu về kết quả kỹ thuật và giá trị đạt được lớn nhất trong tuần]

---

## I. CHI TIẾT TIẾN ĐỘ THEO TỪNG DỰ ÁN / MODULE

### 1. [Tên Dự Án / Module 1]: [Tiêu Đề Hành Động]
- **Key Owner:** [username] | **Phối hợp:** [Tên Team / BU phối hợp]
- **Liên kết Demo & Tài liệu:**
  - *Môi trường Staging:* [URL staging]
  - *Môi trường Production:* [URL production]
  - *Tài liệu / PR:* [URL tài liệu hoặc mã PR]
- **Mục tiêu & Tác động:** [Mô tả mục tiêu định lượng và bối cảnh giải quyết bài toán]
- **Tiến độ thực tế trong tuần ([username]):**
  - **[Tính năng / Module A] ([Ngày hoàn thành]):** [Mô tả chi tiết giải pháp kỹ thuật, cơ chế xử lý và bằng chứng số liệu đạt được].
  - **[Tính năng / Module B]:** [Mô tả chi tiết giải pháp kỹ thuật, cơ chế xử lý và bằng chứng số liệu đạt được].
  - **Điểm nghẽn kỹ thuật (Lowlights):** [Các khó khăn, điểm nghẽn hoặc sự cố đã ghi nhận và phương án xử lý].
- **Kế hoạch 7 ngày tới:**
  - [Đầu việc 1 cần làm ngay kèm kết quả đầu ra].
  - [Đầu việc 2 cần làm tiếp theo].
- **Phối hợp liên đội ngũ:**
  - **[Tên Team/BU 1]:** [Nội dung phối hợp cụ thể].
  - **[Tên Team/BU 2]:** [Nội dung phối hợp cụ thể].

---

## II. BẢNG TỔNG HỢP ĐẦU VIỆC TUẦN

| Mô-đun / Hạng mục | Đầu việc kỹ thuật | Trạng thái | Kết quả cụ thể |
| :--- | :--- | :---: | :--- |
| **[Tên Module 1]** | [Tên đầu việc kèm mã task nếu có] | `Done` | [Kết quả lượng hóa / Đã lên Production ngày DD/MM] |
| **[Tên Module 1]** | [Tên đầu việc 2] | `Done` | [Kết quả lượng hóa / Đã hoàn tất UAT] |
| **[Tên Module 2]** | [Tên đầu việc 3] | `In Progress` | [Đạt X% tiến độ, đang chờ API đối tác] |
| **[Tên Module 2]** | [Tên đầu việc 4] | `Next` | [Kế hoạch tuần tới] |
```
