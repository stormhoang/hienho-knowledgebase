---
name: web-platform-skill
description: Quy chuẩn và bộ mẫu báo cáo hoạt động kỹ thuật (Session, Weekly, Monthly) dành cho Đội ngũ Kỹ sư (Engineering Team) và AI Agent của Web Platform, tích hợp đầy đủ Executive, Hypothesis, Solution, Status theo định dạng văn bản Markdown và bảng biểu chuẩn Tech Lead.
---

# HƯỚNG DẪN VIẾT BÁO CÁO KỸ THUẬT & TỔNG KẾT HOẠT ĐỘNG (ENGINEERING ACTIVITY REPORTING SYSTEM)

> **Dành cho:** Đội ngũ Kỹ sư (Engineers) và các Trợ lý AI (AI Coding Assistants / AI Agents).  
> **Mục đích:** Chuẩn hóa quy trình chuyển đổi toàn bộ nhật ký mã nguồn, lịch sử làm việc, lệnh terminal và commit của kỹ sư thành Báo cáo Tổng kết (Session, Weekly, Monthly) đạt chuẩn Technical Lead / Product Lead.

---

## 0. HƯỚNG DẪN DÀNH CHO TRỢ LÝ AI (AI SYSTEM INSTRUCTIONS & CONTEXT INGESTION)

*Phần này dành riêng để AI Agent / AI Assistant đọc hiểu vai trò và tự động trích xuất thông tin khi Kỹ sư yêu cầu viết báo cáo:*

### A. Vai Trò Của AI (AI Persona)
Bạn là **Technical Lead AI Co-pilot**. Nhiệm vụ của bạn là phân tích toàn bộ công việc mà Kỹ sư vừa thực hiện (qua git log, diff, lịch sử tương tác, lệnh terminal, code changes) và tự động biên soạn thành báo cáo chuyên nghiệp, chính xác và có tính thuyết phục cao.

### B. Cơ Chế Thu Thập Dữ Liệu Của AI (How AI Ingests Context)
Khi được yêu cầu tạo báo cáo, AI cần chủ động kiểm tra các nguồn dữ liệu sau:
1. **Mã nguồn & Thay đổi Git:** Kiểm tra `git status`, `git diff`, `git log -n 10` để nắm rõ các file đã tạo, sửa, xóa và thông điệp commit.
2. **Lịch sử tương tác & Lệnh Terminal:** Đọc lại các câu lệnh build, test, lint, script chạy trong phiên và các lỗi runtime đã gỡ.
3. **Mục tiêu & Yêu cầu:** Bóc tách bài toán từ lời nhắc ban đầu của Kỹ sư hoặc mô tả ticket/task.

### C. Quy Tắc Sinh Báo Cáo Cốt Lõi Cho AI (AI Directives)
- **Bắt buộc đủ 4 Thành Tố:** Mọi báo cáo phải có **Executive Summary** (Tóm tắt điều hành), **Hypothesis** (Giả thuyết/Vấn đề), **Solution** (Giải pháp kỹ thuật) và **Status** (Trạng thái nghiệm thu & % hoàn thành).
- **Tuyệt đối không dùng Emoji / Icon:** Không chèn bất kỳ icon/emoji nào trong tiêu đề, bảng biểu và nội dung.
- **Không đề cập tên riêng cá nhân:** Thay bằng tên vai trò (`Frontend Engineer`, `Backend Engineer`, `Lead AI Agent`, `DevOps Team`, `QA Team`...).
- **Không dùng Graph/Chart/Mermaid:** Trình bày 100% bằng **Bảng biểu Markdown (`Table`)** và **Gạch đầu dòng súc tích**.
- **Không bịa số liệu (Zero Hallucination):** Chỉ đưa số liệu có thực từ code/logs; phần nào chưa có số liệu đo lường cụ thể thì để placeholder `[Kỹ sư bổ sung số liệu: ...]` để kỹ sư điền thêm.

---

## 1. HƯỚNG DẪN NHANH DÀNH CHO KỸ SƯ (QUICK START FOR ENGINEERS)

Kỹ sư có thể sao chép tài liệu này vào dự án của mình và sử dụng các câu lệnh (prompt) mẫu sau để AI tự động viết báo cáo:

- **Viết báo cáo sau một phiên làm việc / tính năng vừa code:**
  > *"Dựa trên các file anh vừa sửa và git diff/log hiện tại, hãy viết Báo cáo Phiên làm việc (Session Report) theo đúng chuẩn trong tài liệu này."*
- **Viết báo cáo tổng kết tuần:**
  > *"Dựa trên lịch sử commit tuần này và các task vừa hoàn thành, hãy viết Báo cáo Tuần (Weekly Report) theo Mẫu 2."*
- **Viết báo cáo tổng kết tháng:**
  > *"Hãy tổng hợp toàn bộ các tính năng, refactor và cải tiến trong tháng qua theo Khung 4 Zone để làm Báo cáo Tháng (Monthly Report) theo Mẫu 3."*

---

## 2. NGUYÊN TẮC BẮT BUỘC (NON-NEGOTIABLES)

1. **Tuyệt đối không sử dụng Emoji / Icon** trong bất kỳ phần nào của báo cáo.
2. **Không đề cập tên riêng cá nhân / PIC** (thay thế bằng tên đội ngũ chuyên môn hoặc vai trò kỹ thuật).
3. **Bộ 4 Thành Tố Bắt Buộc (Executive - Hypothesis - Solution - Status):**
   - **Executive (Tóm tắt điều hành):** Đánh giá tổng quan bài toán và tác động kỹ thuật/nghiệp vụ.
   - **Hypothesis (Giả thuyết):** Vấn đề tồn đọng và giả định cải thiện chỉ số/hiệu năng khi thực thi.
   - **Solution (Giải pháp):** Phương án kỹ thuật, cơ chế xử lý hoặc kiến trúc đã chọn.
   - **Status (Trạng thái):** Mức độ hoàn thiện cụ thể (Hoàn thành 100% / Đang test / Gặp điểm nghẽn).
4. **Hình thức trình bày tối giản:** 
   - Chỉ sử dụng **Bảng biểu Markdown** và **Gạch đầu dòng phân tích trực diện**.
   - **Không vẽ sơ đồ, graph hay chart**.
5. **Dữ liệu thực tế và có đối chứng:** Mọi kết luận phải dựa trên mã nguồn, số lượt gọi công cụ, tệp tin đã tạo/sửa, và các lỗi đã khắc phục.

---

## 3. CÔNG THỨC HÀNH VĂN CHUẨN TECH LEAD

### 3.1. Công thức liên kết Hypothesis $\rightarrow$ Solution $\rightarrow$ Status $\rightarrow$ Impact
$$\text{Hypothesis (Vấn đề & Giả định)} \longrightarrow \text{Solution (Giải pháp kỹ thuật)} \longrightarrow \text{Status (Trạng thái nghiệm thu)} \longrightarrow \text{Impact (Tác động đo lường)}$$

- *Ví dụ:* "Giả định việc chuẩn hóa cấu trúc dữ liệu và loại bỏ các truy vấn lặp sẽ giảm độ trễ (Hypothesis) $\rightarrow$ Đã tái cấu trúc 3 module tính toán cốt lõi (Solution) $\rightarrow$ Trạng thái: Đã hoàn tất test 100% (Status) $\rightarrow$ Thời gian xử lý phản hồi giảm 35% không phát sinh lỗi biên dịch (Impact)."

### 3.2. Khung phân loại 4 Zone cho Báo cáo Tổng thể
- **Performance Zone (Hiệu suất):** Duy trì, tối ưu và refactor hệ thống đang vận hành ổn định.
- **Transformation Zone (Chuyển đổi):** Phát triển tính năng cốt lõi mới, module bứt phá hiệu năng.
- **Incubator Zone (Ươm tạo):** Thử nghiệm công nghệ mới, prototype tính năng mới.
- **Productivity & Self-serve Zone (Năng suất):** Tự động hóa quy trình nội bộ, xây dựng công cụ hỗ trợ giúp tiết kiệm thời gian vận hành.

---

## 4. MẪU BÁO CÁO 1: PHIÊN LÀM VIỆC / TÁC VỤ CỤ THỂ (SESSION REPORT)

```markdown
# BÁO CÁO TỔNG KẾT PHIÊN LÀM VIỆC CỦA AGENT

> **Loại báo cáo:** Báo cáo Phân tích & Đánh giá Phiên làm việc (Session Audit Report)  
> **Phạm vi tác vụ:** [Tên tác vụ / Dự án]  
> **Thời gian thực hiện:** [YYYY-MM-DD HH:MM] - [YYYY-MM-DD HH:MM]  
> **Đơn vị thực thi:** [Tên vai trò Kỹ sư / AI Agent - ví dụ: Backend Engineer / Lead AI Agent]  
> **Trạng thái tổng thể (Overall Status):** [Hoàn thành 100% / Đang test / Gặp điểm nghẽn]  

---

## 1. TÓM TẮT ĐIỀU HÀNH (EXECUTIVE SUMMARY)

- **Tổng quan bài toán:** [Tóm tắt yêu cầu cốt lõi và bối cảnh kỹ thuật]
- **Tác động đạt được:** [Tóm tắt kết quả kỹ thuật/nghiệp vụ nổi bật nhất sau phiên làm việc]
- **Mức độ rủi ro & Ràng buộc:** [Đánh giá rủi ro còn lại, sự phụ thuộc hệ thống]

---

## 2. KHUNG GIẢ THUYẾT VÀ GIẢI PHÁP TRIỂN KHAI (HYPOTHESIS & SOLUTION)

| Hạng Mục | Nội Dung Chi Tiết |
| :--- | :--- |
| **Vấn Đề Tồn Đọng (Problem Statement)** | [Mô tả chi tiết điểm nghẽn, lỗi kỹ thuật hoặc hạn chế hiện tại] |
| **Giả Thuyết Đặt Ra (Hypothesis)** | [Giả định: Nếu thực hiện giải pháp X thì sẽ đạt kết quả Y, cải thiện chỉ số Z] |
| **Giải Pháp Kỹ Thuật (Technical Solution)** | [Chi tiết kiến trúc, thuật toán, module hoặc luồng dữ liệu được áp dụng] |
| **Tiêu Chuẩn Nghiệm Thu (Acceptance Criteria)** | [Danh sách các điều kiện cụ thể để xác nhận giải pháp thành công] |
| **Trạng Thái Thực Thi (Status)** | [Hoàn thành 100% / Đang test - kèm lý do nếu chưa hoàn tất] |

---

## 3. CHỈ SỐ KỸ THUẬT VÀ NĂNG SUẤT THỰC THI (EXECUTION METRICS)

| Chỉ Số | Giá Trị Thực Tế | Ghi Chú |
| :--- | :--- | :--- |
| Tổng số bước thực thi (Steps) | [Số bước] | Các bước suy luận và xử lý code |
| Số tệp tin tạo mới (New Files) | [Số file] | Mã nguồn, tài liệu, cấu hình |
| Số tệp tin chỉnh sửa (Modified Files) | [Số file] | Refactor, sửa lỗi |
| Số lệnh Terminal đã chạy (Commands) | [Số lệnh] | Build, test, lint, search |
| Số bài test đã pass (Tests Passed) | [Số bài / Tổng số] | Đạt 100% test cases |
| Số sự cố kỹ thuật gặp phải (Errors) | [Số lỗi] | Lỗi cú pháp, runtime đã khắc phục |

---

## 4. BẢNG PHÂN TÍCH TIẾN ĐỘ THỰC HIỆN CÁC BƯỚC (STEP BREAKDOWN)

| Bước | Giai Đoạn | Hành Động & Cơ Chế Xử Lý | Trạng Thái (Status) | Kết Quả Đạt Được |
| --- | --- | --- | --- | --- |
| 1 | Khảo sát & Đọc bối cảnh | Kiểm tra kiến trúc hiện tại, rà soát mã nguồn và lịch sử | Hoàn thành | Nắm rõ luồng nghiệp vụ và cấu trúc dữ liệu |
| 2 | Phân tích & Lập giải pháp | Bóc tách yêu cầu, kiểm chứng Hypothesis và chốt Solution | Hoàn thành | Chốt phương án triển khai tối ưu |
| 3 | Triển khai mã nguồn | Viết code, cập nhật tệp tin cấu hình và tài liệu đặc tả | Hoàn thành | Hoàn thiện mã nguồn mới |
| 4 | Test & Nghiệm thu | Chạy test, kiểm tra tính toàn vẹn và chuẩn format | Hoàn thành | Hệ thống hoạt động chính xác, 0 lỗi |
| 5 | Đóng gói & Bàn giao | Soạn tài liệu tổng kết và bàn giao sản phẩm | Hoàn thành | Bàn giao hoàn chỉnh cho đội ngũ liên quan |

---

## 5. DANH MỤC TỆP TIN VÀ SẢN PHẨM BÀN GIAO (DELIVERABLES)

### A. Tệp Tin Tạo Mới
- `[Đường dẫn tệp tin 1]`: [Mô tả chức năng] - *Trạng thái: Hoàn tất*
- `[Đường dẫn tệp tin 2]`: [Mô tả chức năng] - *Trạng thái: Hoàn tất*

### B. Tệp Tin Chỉnh Sửa / Refactor
- `[Đường dẫn tệp tin 1]`: [Mô tả nội dung thay đổi] - *Trạng thái: Hoàn tất*
- `[Đường dẫn tệp tin 2]`: [Mô tả nội dung thay đổi] - *Trạng thái: Hoàn tất*

---

## 6. NHẬT KÝ SỰ CỐ VÀ CÁCH KHẮC PHỤC (TROUBLESHOOTING LOG)

| STT | Sự Cố / Lỗi Kỹ Thuật | Nguyên Nhân Gốc Rễ | Giải Pháp Khắc Phục (Solution) | Trạng Thái (Status) |
| --- | --- | --- | --- | --- |
| 1 | [Mô tả sự cố 1] | [Nguyên nhân] | [Giải pháp khắc phục triệt để] | Đã xử lý |
| 2 | [Mô tả sự cố 2] | [Nguyên nhân] | [Giải pháp khắc phục triệt để] | Đã xử lý |

---

## 7. ĐÁNH GIÁ KẾT QUẢ VÀ KẾ HOẠCH TIẾP THEO (ACTION ITEMS)

### A. Đánh Giá Kết Luận
- **Mức độ hoàn thiện giải pháp:** Đạt [100% / Tỷ lệ %] so với Hypothesis ban đầu.
- **Chất lượng kỹ thuật:** Tuân thủ tiêu chuẩn kiến trúc, không hard-code, bảo đảm an toàn dữ liệu.

### B. Kế Hoạch Hành Động Tiếp Theo

| Thứ Tự Triển Khai | Hạng Mục Công Việc | Đội Ngũ Phụ Trách | Thời Hạn | Trạng Thái (Status) |
| --- | --- | --- | --- | --- |
| 1. Làm ngay | [Hành động cần làm ngay] | [Tên đội ngũ chuyên môn] | [Thời hạn] | Chưa bắt đầu |
| 2. Làm tiếp theo | [Hành động hoàn thiện/mở rộng] | [Tên đội ngũ chuyên môn] | [Thời hạn] | Chưa bắt đầu |
| 3. Tối ưu dài hạn | [Hành động tối ưu dài hạn] | [Tên đội ngũ chuyên môn] | [Thời hạn] | Chưa bắt đầu |
```

---

## 5. MẪU BÁO CÁO 2: BÁO CÁO TUẦN (WEEKLY REPORT)

```markdown
# BÁO CÁO TIẾN ĐỘ VÀ HIỆU SUẤT TUẦN CỦA ĐỘI NGŨ KỸ THUẬT

> **Khung thời gian:** Tuần [Số tuần] ([Từ ngày] - [Đến ngày])  
> **Đơn vị thực thi:** [Tên đội ngũ kỹ thuật - ví dụ: Core Engineering Team]  
> **Trạng thái tổng thể tuần:** [Đạt mục tiêu / Cần lưu ý / Chậm tiến độ]  

---

## 1. TÓM TẮT ĐIỀU HÀNH TUẦN (EXECUTIVE SUMMARY)

- **Đánh giá tổng quan:** [Tóm tắt 2-3 điểm mấu chốt về tiến độ và năng suất kỹ thuật trong 7 ngày qua]
- **Tác động kinh doanh & Kỹ thuật chính:** [Kết quả nổi bật đóng góp cho hệ thống]
- **Cảnh báo rủi ro (Risk Alert):** [Các điểm nghẽn kỹ thuật hoặc sự phụ thuộc đang cần can thiệp]

---

## 2. BẢNG THEO DÕI GIẢ THUYẾT & GIẢI PHÁP TUẦN (HYPOTHESIS, SOLUTION & STATUS)

| Hạng Mục / Dự Án | Giả Thuyết Ban Đầu (Hypothesis) | Giải Pháp Triển Khai (Solution) | Trạng Thái (Status) | Kết Quả Đo Lường / Impact |
| :--- | :--- | :--- | :--- | :--- |
| [Tên Dự Án 1] | [Giả định cải thiện chỉ số/tính năng] | [Chi tiết giải pháp kỹ thuật đã áp dụng] | Hoàn thành (100%) | [Chỉ số đạt được thực tế] |
| [Tên Dự Án 2] | [Giả định giảm tải thời gian/lỗi] | [Chi tiết giải pháp kỹ thuật đã áp dụng] | Đang test (80%) | [Kết quả test ban đầu] |
| [Tên Dự Án 3] | [Giả định tối ưu quy trình] | [Chi tiết giải pháp kỹ thuật đã áp dụng] | Gặp điểm nghẽn (40%) | [Vướng mắc cần hỗ trợ] |

---

## 3. BẢNG CHỈ SỐ NĂNG SUẤT TUẦN (WEEKLY PERFORMANCE METRICS)

| Nhóm Chỉ Số | Tuần Trước | Tuần Này | Biến Động (WoW) | Mục Tiêu Tuần | Trạng Thái (Status) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Số tác vụ hoàn tất (Tasks Completed) | [Số] | [Số] | [+/-]% | [Mục tiêu] | Đạt |
| Số tệp tin tạo mới (New Files) | [Số] | [Số] | [+/-]% | [Mục tiêu] | Đạt |
| Số tệp tin refactor (Modified) | [Số] | [Số] | [+/-]% | [Mục tiêu] | Đạt |
| Số PR / Commits đã merge | [Số] | [Số] | [+/-]% | [Mục tiêu] | Đạt |
| Tỷ lệ thành công test (Test Pass Rate) | [Số]% | [Số]% | [+/-]pp | [Mục tiêu]% | Đạt |

---

## 4. TRỌNG TÂM THỰC THI VÀ TÁC ĐỘNG KỸ THUẬT (KEY HIGHLIGHTS & IMPACT)

- **Phát Triển Mã Nguồn & Tiện Ích:** Hoàn thành [Số] tính năng cốt lõi; nâng cao độ chính xác xử lý logic; tối ưu [Số]% thời gian phản hồi.
- **Tự Động Hóa & Tối Ưu Quy Trình:** Chuẩn hóa quy trình xử lý dữ liệu; giảm [Số]% các thao tác thủ công lặp lại.
- **Xử Lý Lỗi & Ổn Định Hệ Thống:** Khắc phục triệt để [Số] lỗi runtime; 100% bài test trên môi trường staging vượt qua tiêu chuẩn nghiệm thu.

---

## 5. PHỐI HỢP LIÊN ĐỘI NGŨ & ĐIỂM NGHẼN (COLLABORATION & BLOCKERS)

- **Backend Team:** Thống nhất đặc tả API và định dạng dữ liệu cho module [Tên module] trước ngày [Ngày/Tháng] - *Trạng thái: Đang trao đổi*.
- **Data Analytics Team:** Chuẩn hóa cấu trúc trường dữ liệu log để phục vụ phân tích - *Trạng thái: Đã hoàn tất*.
- **QA Team:** Hoàn tất kịch bản test cho các trường hợp biên (Edge Cases) - *Trạng thái: Đang chờ bàn giao*.

---

## 6. KẾ HOẠCH TRỌNG TÂM 7 NGÀY TỚI (PRIORITIES FOR NEXT 7 DAYS)

| Thứ Tự Triển Khai | Hạng Mục Công Việc Cần Triển Khai | Đội Ngũ Phụ Trách | Mục Tiêu Đầu Ra | Trạng Thái (Status) |
| --- | --- | --- | --- | --- |
| 1. Làm ngay | [Nhiệm vụ trọng điểm 1 - Bugfix/Delivery] | [Tên đội ngũ chuyên môn] | [Deliverable cụ thể] | Đang chuẩn bị |
| 2. Làm tiếp theo | [Nhiệm vụ trọng điểm 2 - Feature/Testing] | [Tên đội ngũ chuyên môn] | [Deliverable cụ thể] | Chưa bắt đầu |
| 3. Tối ưu dài hạn | [Nhiệm vụ tối ưu hóa / Refactor kiến trúc] | [Tên đội ngũ chuyên môn] | [Deliverable cụ thể] | Chưa bắt đầu |
```

---

## 6. MẪU BÁO CÁO 3: BÁO CÁO THÁNG (MONTHLY REPORT)

```markdown
# BÁO CÁO TỔNG KẾT THÁNG CỦA ĐỘI NGŨ KỸ THUẬT

> **Khung thời gian:** Tháng [Số tháng]/[Năm]  
> **Đơn vị thực thi:** [Tên đội ngũ kỹ thuật]  
> **Đánh giá hiệu suất tháng:** [Xuất sắc / Đạt yêu cầu / Cần cải thiện]  

---

## 1. TÓM TẮT ĐIỀU HÀNH THÁNG (EXECUTIVE SUMMARY)

- **Tổng quan kết quả tháng:** [Tóm tắt quy mô thực thi: tổng số tính năng hoàn tất, số PRs merged và độ tin cậy hệ thống]
- **Tác động chiến lược vĩ mô:** [Đóng góp lớn nhất vào mục tiêu tăng trưởng, tối ưu chi phí vận hành và nâng cao chất lượng nền tảng]
- **Đánh giá năng lực tự động hóa:** [Mức độ giảm tải công việc thủ công nhờ công cụ và kịch bản tự động]

---

## 2. KHUNG GIẢ THUYẾT & GIẢI PHÁP THEO MÔ HÌNH 4 ZONE (4-ZONE HYPOTHESIS & SOLUTION MAPPING)

| Zone Quản Trị | Giả Thuyết Đặt Ra (Hypothesis) | Giải Pháp Thực Thi (Solution) | Trạng Thái (Status) | Tác Động Đo Lường (Impact) |
| :--- | :--- | :--- | :--- | :--- |
| **Performance Zone** (Hiệu suất) | [Giả định tối ưu hệ thống hiện hữu] | [Giải pháp refactor / caching / query] | Hoàn thành (100%) | Tăng độ ổn định, giảm [Số]% lỗi |
| **Transformation Zone** (Chuyển đổi) | [Giả định tăng trưởng đột phá x2-x5] | [Giải pháp phát triển tính năng cốt lõi mới] | Đang triển khai (75%) | Mở rộng năng lực xử lý gấp [Số] lần |
| **Incubator Zone** (Ươm tạo) | [Giả định kiểm chứng tính khả thi mới] | [Giải pháp prototype / PoC] | Hoàn thành PoC (100%) | Chứng minh tính khả thi kỹ thuật |
| **Productivity Zone** (Năng suất) | [Giả định tự động hóa tiết kiệm nguồn lực] | [Giải pháp xây dựng tool tự phục vụ] | Đã go-live (100%) | Tiết kiệm [Số] giờ làm việc thủ công |

---

## 3. TỔNG HỢP CHỈ SỐ KỸ THUẬT VÀ NĂNG SUẤT THÁNG (MONTHLY METRICS)

| Chỉ Số Đánh Giá | Tháng Trước | Tháng Này | Biến Động (MoM) | Đánh Giá Hiệu Suất | Trạng Thái (Status) |
| --- | --- | --- | --- | --- | --- |
| Tổng số tác vụ kỹ thuật hoàn tất | [Số] | [Số] | [+/-]% | Vượt kế hoạch | Đạt |
| Tổng tệp tin mã nguồn tạo mới & tối ưu | [Số] | [Số] | [+/-]% | Đạt tiêu chuẩn | Đạt |
| Tổng số PR / Commits đã merge | [Số] | [Số] | [+/-]% | Tương tác chuyên sâu | Đạt |
| Tỷ lệ thành công test (Test Pass Rate) | [Số]% | [Số]% | [+/-]pp | Chất lượng cao | Đạt |
| Thời gian trung bình hoàn tất tác vụ | [Số] giờ | [Số] giờ | [+/-]% | Tốc độ cải thiện | Đạt |

---

## 4. CÁC ĐỘT PHÁ KIẾN TRÚC VÀ GIẢI PHÁP NỀN TẢNG (KEY INNOVATIONS & SOLUTIONS)

- **Đột phá 1:** [Mô tả chi tiết giải pháp kỹ thuật, cơ chế tối ưu và giá trị đạt được] - *Trạng thái: Đã đưa vào vận hành chính thức*.
- **Đột phá 2:** [Mô tả chi tiết giải pháp kỹ thuật, cơ chế tối ưu và giá trị đạt được] - *Trạng thái: Đã đưa vào vận hành chính thức*.
- **Đột phá 3:** [Mô tả chi tiết giải pháp kỹ thuật, cơ chế tối ưu và giá trị đạt được] - *Trạng thái: Đang trong giai đoạn mở rộng*.

---

## 5. KẾ HOẠCH CHIẾN LƯỢC 30 NGÀY TỚI (30-DAY STRATEGIC PRIORITIES)

| Ưu Tiên | Hạng Mục Chiến Lược | Giải Pháp Đề Xuất (Solution) | Mục Tiêu Cụ Thể | Trạng Thái (Status) | Đội Ngũ Phối Hợp |
| --- | --- | --- | --- | --- | --- |
| Ưu tiên 1 | [Phát triển mã nguồn / Hệ thống] | [Giải pháp kỹ thuật] | [Metric cần đạt] | Kế hoạch mới | [Tên đội ngũ] |
| Ưu tiên 2 | [Tối ưu hóa / Tự động hóa quy trình] | [Giải pháp kỹ thuật] | [Metric cần đạt] | Kế hoạch mới | [Tên đội ngũ] |
| Ưu tiên 3 | [Củng cố bảo mật / Giám sát] | [Giải pháp kỹ thuật] | [Metric cần đạt] | Kế hoạch mới | [Tên đội ngũ] |
```

---

## 7. CHECKLIST KIỂM ĐỊNH TRƯỚC KHI XUẤT BẢN BÁO CÁO

- [ ] **Executive Summary Check:** Có phần tóm tắt điều hành súc tích ở đầu báo cáo dành cho cấp quản lý.
- [ ] **Hypothesis & Solution Check:** Mọi vấn đề kỹ thuật đều nêu rõ Giả thuyết đặt ra (Hypothesis) và Giải pháp thực thi (Solution).
- [ ] **Status Check:** Tất cả các hạng mục, tệp tin, bước xử lý và action items đều có gắn trạng thái cụ thể (Status / % hoàn thành).
- [ ] **Emoji Check:** Đã loại bỏ 100% emoji, biểu tượng cảm xúc trong tiêu đề và nội dung.
- [ ] **Anonymity Check:** Toàn bộ tên riêng cá nhân đã được thay bằng tên đội ngũ chuyên môn hoặc vai trò.
- [ ] **No Visuals Check:** Không có bất kỳ Mermaid, graph, chart nào; trình bày hoàn toàn bằng Bảng Markdown và Gạch đầu dòng.
