# MÔ HÌNH VẬN HÀNH QUẢN LÝ ĐẦU VIỆC (TASK OPERATING MODEL)

Tài liệu này xác lập quy chuẩn vận hành, quản trị danh mục công việc (Tasklists) và cơ chế phân phối giá trị liên tục (Continuous Delivery) hàng tuần cho toàn bộ các dự án thuộc nền tảng Web Platform.

---

## 1. NGUYÊN TẮC VẬN HÀNH: WEEKLY SHIPPING CADENCE

Mô hình quản lý không vận hành theo cấu trúc giai đoạn truyền thống (không chia tuần theo kiểu Tuần 1 Kick-off, Tuần 2 Code, Tuần 3 Test, Tuần 4 Go-live cuối tháng). 

Thay vào đó, Web Platform áp dụng nguyên tắc **Ship Mỗi Tuần (Weekly Shipping Cadence)**:
- **Mỗi tuần là một chu kỳ hoàn chỉnh:** Từng tuần (Tuần 1, Tuần 2, Tuần 3, Tuần 4) các dự án đều phải có các đầu việc cụ thể được **SHIP** (Release tính năng, Go Live trang, Publish nội dung, Tích hợp API live, Gắn tracking, hoặc Đo kiểm hiệu năng thực tế).
- **Không dồn việc cuối tháng:** Tránh dồn rủi ro kiểm thử và bàn giao vào tuần cuối. Mọi tính năng lớn đều được bóc tách thành các đầu việc có thể ship và nghiệm thu độc lập ngay trong tuần.
- **Tiêu chí Hoàn thành (AC - Acceptance Criteria) rõ ràng:** Mỗi task phải có mô tả đầu ra cụ thể, đo lường được trên môi trường thực tế (Production / Staging / CMS live).
- **Chu kỳ vận hành tuần:**
  - Đầu tuần: Chốt danh sách task cam kết ship trong tuần (trạng thái `To Do` / `In Progress`).
  - Trong tuần: Kỹ sư và nhân sự chuyên môn tập trung thực thi, phối hợp liên ngành.
  - Cuối tuần: Rà soát đầu việc đã ship. Task hoàn thành chuyển sang `Done`.
- **Quy tắc Carry-Forward (Bắt buộc):** Bất kỳ task nào ở tuần hiện tại **chưa chuyển sang `Done`** (vẫn ở `To Do` / `In Progress` / `Blocked`) sẽ **tự động được chuyển tiếp (carry-forward) sang tuần kế tiếp** khi chạy rollover. Task carry-forward được đánh dấu rõ trong cột Mô tả/AC (chèn suffix `[carry từ Tuần N]`) để phân biệt với task mới lên kế hoạch trong tuần đó. Task không được phép "mất" giữa các tuần - chỉ Done mới kết thúc vòng đời.

---

## 2. PHÂN NHÓM DỰ ÁN VÀ PHÂN VAI TRÁCH NHIỆM

### Phân nhóm 2 khối dự án cốt lõi:
1. **Strategic Projects (Dự án Chiến lược):** Cinema, Financial, Vehicle, New User.
2. **Platform - MoSpark (Nền tảng):** Puck Editor, Blog Editor, PLG Project, MoBase.

### Phân vai trách nhiệm:
- **Lead Quản trị chung (Hiến):** Nắm overall toàn bộ các dự án, định hướng chiến lược, gỡ vướng blocker và tham gia phối hợp linh hoạt; trực tiếp chủ trì các đầu việc chiến lược trọng điểm (như cải tiến trang Bonbon, chuẩn hóa tracking SSOT), không gán task dev chi tiết.
- **PIC Chuyên môn (Kỹ sư / Content):** Từng đầu việc được gán trực tiếp cho đúng nhân sự chịu trách nhiệm chính (Hùng, Hoan, Nhật, Hiếu, Thuận, Hoài Anh, Trọng, Duy...). 

---

## 3. CẤU TRÚC THƯ MỤC VÀ DỮ LIỆU

Mỗi tháng được gom gọn trong đúng **4 file đại diện cho 4 tuần**. Không tạo thêm file lẻ theo từng dự án nhằm giữ dữ liệu tập trung, dễ theo dõi.

```
12_TASK_MANAGEMENT/
├── TASK_OPERATING_MODEL.md             # Quy chuẩn mô hình vận hành (File này)
├── templates/
│   └── weekly_task_template.md         # File mẫu chuẩn cho từng tuần
└── 2026-10/                            # Thư mục dữ liệu Tháng 10/2026 (4 files tuần)
    ├── week_01.md                      # Tuần 1 (01/10 – 07/10/2026): Các hạng mục đã ship đợt 1
    ├── week_02.md                      # Tuần 2 (08/10 – 14/10/2026): Các hạng mục cam kết ship đợt 2 (Tuần hiện tại)
    ├── week_03.md                      # Tuần 3 (15/10 – 21/10/2026): Các hạng mục cam kết ship đợt 3
    └── week_04.md                      # Tuần 4 (22/10 – 31/10/2026): Các hạng mục cam kết ship đợt 4
```

---

## 4. QUY CHUẨN TRÌNH BÀY BẢNG TASKLIST

Mọi file tuần tuân thủ nghiêm ngặt bảng chuẩn 5 cột tinh gọn:

`| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |`

- **Phạm vi đầu việc (Bắt buộc):** Bảng tuần chỉ theo dõi đầu việc **product-side**: content, đo lường/đánh giá, audit, nghiệm thu/UAT, chuẩn hóa (EventName, Topic Cluster), nghiên cứu khả thi. **Không đưa đầu việc dev/code thuần** (Build, Code, Golive, Release, Tích hợp API, Migration, Nâng cấp UI...) vào bảng tuần - SE Team tự track các đầu việc này trên ticket board riêng.
- **Không sử dụng cột Mã Task:** Giữ tài liệu trực quan, dễ đọc, không phát sinh mã hóa cồng kềnh.
- **Không sử dụng cột Priority / nhãn P0-P1-P2:** Mọi việc đã đưa vào bảng tuần đều là việc bắt buộc ship trong tuần đó, không phân cấp độ ưu tiên trong bảng.
- **Quy định trạng thái:**
  - `To Do`: Đầu việc đã lên kế hoạch, chuẩn bị thực hiện trong tuần.
  - `In Progress`: Đầu việc đang trong quá trình phát triển/sản xuất.
  - `Done`: Đầu việc đã ship thành công ra môi trường thực tế và đạt tiêu chí AC.
  - `Blocked`: Đầu việc bị tắc nghẽn do phụ thuộc bên ngoài (kèm ghi chú rõ nguyên nhân).

---

## 5. DANH MỤC DỰ ÁN TRỌNG ĐIỂM THÁNG 10/2026

### I. Strategic Projects
1. **Cinema (Hùng, Hoan, Hoài Anh, Hiến):**
   - Content plan từ Blog, Diễn Viên, Film Detail.
   - Sản xuất 100 bài blog điện ảnh/review/phim chiếu rạp qua MoSpark GenAI Pipeline chuẩn SEO/GEO.
   - Tối ưu Core Web Vitals (LCP < 2.0s) trên MoSpark.
   - Xây dựng Sitemap chuyên biệt cho cụm Cinema.
   - Thiết kế Mini Game Tìm Hidden Puzzle và hiển thị mass.
   - Migration hệ thống rạp đối tác qua MoSpark.
   - Đồng bộ API View Comment Review và hiển thị Viewcount cho User Review trong Film Detail.
   - Nghiên cứu và xây dựng cấu trúc trang Community hiển thị toàn bộ bài Post Review của người dùng theo từng phim.

2. **Financial (Nhật, Hiếu, Thuận, Hoan, Hiến, Hùng):**
   - Phối hợp BU Bank lên Content Structure trang Bank Detail và hoàn thiện UI.
   - Xây dựng Content Plan cho cụm trang Tỷ Giá và Chứng Chỉ Quỹ.
   - Go Live trang Tỷ Giá theo từng cặp tiền tệ.
   - Triển khai và Go Live Mega Menu điều hướng cho toàn bộ cụm trang Tài Chính.
   - Đồng bộ API Chứng Chỉ Quỹ và Lãi tiết kiệm.
   - Định nghĩa Umami EventName cho toàn bộ Utilities trên Knowledgebase SSOT.
   - Tự động hóa gắn tracking Umami cho từng Tool/Widget.
   - Sản xuất 30 bài blog chất lượng cao cho Financial.

3. **Vehicle (Thuận, Hoan, Hoài Anh, Hiến):**
   - Go Live trang Hãng xe và Model Xe (ưu tiên cụm Vinfast).
   - Triển khai trang Phong Thủy theo đúng Prototype.
   - Nghiên cứu kết nối API Database Garage của Cell Team.
   - Review và khôi phục API Phạt Nguội 0-CAPTCHA trên Production.
   - Rà soát danh mục lỗi vi phạm trên MoSpark để Cell Team đối soát và chuẩn hóa lại mức phạt.
   - Xây dựng trang Nộp Phạt vi phạm giao thông trực tuyến.
   - Xây dựng trang Tra cứu mức phạt giao thông theo hành vi và loại phương tiện.
   - Nghiên cứu và triển khai cụm trang Phạt Nguội + Địa Điểm (tỉnh thành, vị trí camera).

4. **New User (Thuận, Hiếu, Hiến):**
   - Go Live Quýt Game (phiên bản 2D và 3D).
   - Đề xuất và triển khai giải pháp update tối ưu trang Download (`/download`) hiện hữu.
   - Xây dựng trang mới Tải App (`/tai-app`, tách biệt trang Download) chuẩn Utility Download Center nhằm acquire nhóm search intent cài đặt ví/app, tiếp nhận điều hướng từ `/download` và xây dựng luồng OneLink thông minh (mặc định fallback về `/tai-app` kèm Dynamic QR Code quét tức thì thay vì văng về homepage trên desktop).
   - Cải tiến giao diện và tỷ lệ chuyển đổi trang Bonbon.

5. **Game/App (Thuận, Hiếu):**
   - Follow tiếp các dự án Nạp thẻ Game theo provider (Zing, Garena, VTC, Soha...) và đồng bộ mệnh giá live.
   - Triển khai trang ChatGPT (giao diện và luồng thanh toán mua gói tài khoản ChatGPT trên Web MoMo).

### II. Platform (MoSpark)
1. **Puck Editor (Duy, Nhật):**
   - Nghiên cứu giải pháp và tích hợp Blog Section.
   - Bổ sung Template Menu Header dùng chung cho các Hubs.

2. **Blog Editor (Trọng, Duy):**
   - Nâng cấp giao diện người dùng bộ chấm điểm SEO/GEO Scoring.
   - Bổ sung kích thước 1200x630 và cơ chế chỉnh sửa/làm mờ Watermark logo MoMo trên Image Template.
   - Hiển thị số lượt View đo lường từ Umami và Search Volume cạnh mỗi bài viết trên Microsite Blog Management.

3. **PLG Project & MoBase (Trọng, Hoan, Hùng, Nhật):**
   - Quản trị Topic Cluster và đồng bộ 1-1 với CMS Editor.
   - Xây dựng PLG Project cho Blog Common và kết nối vào các bài Blog.
   - Xây dựng Dashboard trực quan theo dõi pipeline bài viết PLG (Outline, Draft, Đang Chờ Duyệt, Published và Tổng bài).
   - Chuẩn hóa Design Token V2 và đồng bộ thư viện component dùng chung.

4. **Tìm Kiếm /tim-kiem (Duy, Hoài Anh):**
   - Xây dựng Knowledge Base để phản hồi chính xác kết quả tìm kiếm trên trang `/tim-kiem`.

5. **Blog Common (Duy, Hùng):**
   - Migration toàn bộ bài viết blog từ hệ thống Admin Tool cũ sang nền tảng MoSpark.

6. **Dashboard Tracking (Hiến, Thuận):**
   - Nghiên cứu giải pháp sử dụng crawl data từ hạ tầng Datasef của công ty phục vụ Dashboard Web Tracking.

7. **Quiz Platform (Thuận):**
   - Tích hợp component Quiz tương tác trong bài Blog (đặt ngay bên trên phần Author) nhằm thúc đẩy mức độ tương tác và time-on-page.

