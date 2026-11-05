# KẾ HOẠCH & QUẢN LÝ ĐẦU VIỆC TUẦN 3 (15/10 – 21/10/2026)

> **Lead Quản trị chung:** Hiến (Nắm overall các dự án, tham gia linh hoạt, không gán task cụ thể)  
> **Tháng thực thi:** 10/2026  
> **Trạng thái tuần:** Đang thực thi (In Progress)  
> **Nguyên tắc kế thừa:** Kế thừa toàn bộ 32 đầu việc dở dang (Doing/Backlog) từ Tuần 2 theo dữ liệu Supabase, tích hợp các yêu cầu nghiệp vụ mới đã chỉ đạo. Tuyệt đối không chế task nghiệm thu/đo lường khi chưa triển khai.

---

## I. STRATEGIC PROJECTS

### 1. Cinema
- **Nhân sự phụ trách:** Hùng, Hoài Anh, Hiến

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Phát Triển Content Plan Cinema | Kế thừa W2: Tiếp tục hoàn thiện content plan cho cụm Blog, Diễn Viên và Film Detail | Hùng | Hiến (định hướng) | `In Progress` |
| Sản Xuất Blog Cinema (100 bài) | Kế thừa W2: Tiếp tục sản xuất và xuất bản đợt bài review điện ảnh qua MoSpark GenAI Pipeline | Hùng | Hiến (định hướng) | `In Progress` |
| Tối Ưu Core Web Vitals (LCP) | Kế thừa W2: Tối ưu LCP < 2.0s trên cụm trang rạp chiếu và trang phim chi tiết MoSpark | Hùng | Web Dev | `In Progress` |
| Build & Submit Sitemap Cinema | Kế thừa W2: Xây dựng cấu trúc sitemap chuyên biệt cho Cinema và submit lên Google Search Console | Hoài Anh | Hùng | `In Progress` |
| Migration Cụm Rạp Qua MoSpark | Kế thừa W2: Tiếp tục di chuyển các trang cụm rạp đối tác còn lại sang nền tảng MoSpark | Hùng | Web Dev | `In Progress` |
| Đồng Bộ API Lượt View Comment Review | Task mới W3: Kết nối và đồng bộ API theo dõi lượt View của từng Comment/Bài Review phim | Hoài Anh | Backend | `In Progress` |
| Build UI/UX Viewcount Cho User Review | Task mới W3: Thiết kế và hoàn thiện UI/UX hiển thị Viewcount cho từng User Review trong Film Detail | Hùng | Design | `In Progress` |
| Nghiên Cứu Trang Community Post Review | Task mới W3: Xây dựng cấu trúc trang Community hiển thị toàn bộ bài Post Review của user theo từng phim | Hiến | Hùng | `In Progress` |

---

### 2. Financial
- **Nhân sự phụ trách:** Nhật, Hiếu, Thuận, Hoan, Hiến, Hùng

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Go Live 4 Cặp Tiền Tệ Ngoại Tệ | Hoàn thiện và Go-live 4 cặp tiền tệ sang VND: AUD, EUR, USD, GBP tích hợp quy đổi 2 chiều và bảng giá | Nhật | Web Dev | `Done` |
| On Demo Trang Chứng Chỉ Quỹ | Hoàn thiện giao diện bảng giá NAV và simulator tích sản SIP, đưa lên môi trường Demo | Hiếu | Nhật | `Done (Demo)` |
| Tích Hợp MoMo AI Cho Utility | Tích hợp MoMo AI với 2 mode Hài Hước và Nghiêm Túc đưa ra lời khuyên tài chính trên từng Tool | Nhật | Backend | `Done` |
| Auto Gắn Tracking Umami Từng Tool | Tự động hóa và hoàn tất gắn tracking Umami chi tiết cho từng Tool/Widget tài chính theo SSOT | Thuận | Nhật | `Done` |
| Phối Hợp BU Bank Lên Content Structure | Kế thừa W2: Tiếp tục phối hợp với BU Bank chốt Content Structure chi tiết cho trang Bank Detail | Hiến | BU Bank | `In Progress` |
| Triển Khai UI Trang Bank | Kế thừa W2: Thiết kế và hoàn thiện giao diện người dùng cho trang Hub Ngân Hàng | Hiến | Nhật | `In Progress` |
| Content Plan Cho Tỷ Giá Và Quỹ | Kế thừa W2: Xây dựng Content Plan chi tiết cho cụm trang Tỷ Giá và Chứng Chỉ Quỹ | Hoan | Hiến | `In Progress` |
| Go Live Mega Menu Cho Trang Tài Chính | Kế thừa W2: Hoàn thiện và Go Live Mega Menu điều hướng cho toàn bộ cụm trang Tài Chính | Nhật | Hùng | `In Progress` |
| Đồng Bộ API CCQ & Lãi Tiết Kiệm | Kế thừa W2: Làm việc với Backend Team kết nối và đồng bộ dữ liệu API CCQ và Lãi tiết kiệm | Hiếu | Backend | `In Progress` |
| Sản Xuất Blog Financial (30 bài) | Kế thừa W2: Tiếp tục sản xuất và biên tập cho đủ số lượng 30 bài blog tài chính chuẩn SEO/GEO | Hoan | Hiến (định hướng) | `In Progress` |
| Re-Design UI/UX Tool Phân Bổ Lương | Kế thừa W2 (task Supabase): Tối ưu UI tool phân bổ lương, hướng user focus vào đầu tư và CTA dịch vụ | Nhật | Design | `In Progress` |
| Tạo LP Ngân Hàng Liên Kết | Kế thừa W2 (task Supabase): Thiết kế và xuất bản Landing Page cho nhóm đối tác Ngân hàng liên kết | Nhật | Growth | `In Progress` |

---

### 3. Vehicle
- **Nhân sự phụ trách:** Thuận, Hiến, Hoan, Hoài Anh

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Go Live Cụm Trang Hãng Xe & Model Xe | Kế thừa W2: Hoàn thiện việc xuất bản trang Hãng xe và Model xe (chủ lực Vinfast) | Thuận | Hoan | `In Progress` |
| Triển Khai Trang Phong Thủy | Kế thừa W2: Triển khai trang Phong Thủy xe theo đúng Prototype đã phê duyệt | Thuận | Design | `In Progress` |
| Review Lỗi Vi Phạm Trên MoSpark | Task mới W3: Rà soát danh mục lỗi vi phạm trên MoSpark để Cell Team đối soát và chuẩn hóa lại mức phạt | Thuận | Cell Team | `In Progress` |
| Xây Dựng Trang Nộp Phạt | Task mới W3: Thiết kế giao diện và luồng thanh toán nộp phạt vi phạm giao thông trực tuyến | Hiến | Thuận | `In Progress` |
| Xây Dựng Trang Tra Cứu Mức Phạt | Task mới W3: Xây dựng trang tra cứu mức phạt giao thông theo từ khóa, hành vi và phương tiện | Hiến | Thuận | `In Progress` |
| Triển Khai Phạt Nguội + Địa Điểm | Task mới W3: Nghiên cứu và triển khai cụm trang Phạt Nguội kết hợp Địa Điểm (tỉnh thành, camera) | Hiến | Thuận | `In Progress` |
| Giám Sát Hoạt Động API Phạt Nguội Live | Task mới W3: Kiểm tra tỷ lệ tra cứu thành công và độ ổn định của API CSGT sau khi khôi phục | Hoài Anh | Thuận | `In Progress` |
| Tối Ưu Liên Kết Model Xe Vinfast | Task mới W3: Bổ sung internal link từ trang Vinfast trỏ về các tiện ích đăng kiểm, trạm sạc | Thuận | Hoan | `In Progress` |

---

### 4. New User
- **Nhân sự phụ trách:** Thuận, Hiếu, Hiến, Hải

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Triển Khai Giải Pháp Update Trang Download | Kế thừa W2: Hiếu config trang `/download` để điều hướng Desktop sang `/tai-app` | Hiếu | Growth | `In Progress` |
| Cải Tiến Giao Diện Trang Bonbon | Kế thừa W2: Tối ưu hóa giao diện và trải nghiệm chuyển đổi người dùng mới trên trang Bonbon | Hiến | Web Dev | `In Progress` |
| Xây Dựng Trang Tải App Mới | Task mới W3: Tạo và đưa trang Tải App (`/tai-app`, tách `/download`) go-live trong tuần này, cấu hình OneLink fallback desktop về trang kèm QR Code; Mobile: Detect OS hiển thị đúng Store, nhận diện Mở app vs Tải app (Apple Smart App Banner iOS, getInstalledRelatedApps & Chrome Intent Android) | Hiến | Hiếu, Thuận | `In Progress` |
| Đo Lường Tỷ Lệ Chuyển Đổi Quýt Game | Task mới W3: Đánh giá tỷ lệ người chơi hoàn thành Quýt Game 2D/3D (đã Go Live ở W2) và tải App | Thuận | Hải | `In Progress` |

---

### 5. Game/App
- **Nhân sự phụ trách:** Thuận, Hùng

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Xây Dựng Trang ChatGPT | Kế thừa W2: Triển khai giao diện và luồng thanh toán mua gói tài khoản ChatGPT trên nền tảng Web | Hùng | Thuận | `In Progress` |
| UAT Deeplink Nạp Thẻ Game | Task mới W3: Kiểm thử toàn diện luồng chọn mệnh giá và deeplink thanh toán cho 4 provider game đã tích hợp ở W2 | Thuận | Backend | `In Progress` |

---

## II. PLATFORM (MOSPARK)

### 1. Blog Editor (Tiptap)
- **Nhân sự phụ trách:** Trọng, Hiến, Duy

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Cải Thiện UI SEO/GEO Scoring | Kế thừa W2: Cải thiện lại giao diện người dùng cho bộ chấm điểm SEO/GEO Scoring trên Editor | Trọng | Hiến | `In Progress` |
| Review Image Template & Watermark | Kế thừa W2: Bổ sung kích thước 1200x630 và cho phép tùy chỉnh Watermark logo MoMo | Trọng | Design | `In Progress` |
| Show Volume & Lượt View Blog Management | Kế thừa W2: Hiển thị số lượt View (Umami) và Volume bài viết bên cạnh danh sách quản lý Blog | Trọng | Duy | `In Progress` |
| Tối Ưu Quản Lý Hình Ảnh Trên Editor | Task mới W3: Tối ưu chèn và quản lý hình ảnh trên Editor, bổ sung kích thước 1200x630 và watermark logo MoMo | Trọng | Design | `In Progress` |
| Chỉnh Sửa Keyword Trực Tiếp | Task mới W3: Hỗ trợ người dùng chỉnh sửa keyword trực tiếp ngay trên giao diện soạn thảo bài viết | Trọng | Hoan | `In Progress` |
| Bổ Sung Tính Năng Unlink | Task mới W3: Thêm tính năng hủy liên kết (unlink) linh hoạt khi biên tập nội dung bài viết | Trọng | Hoan | `In Progress` |
| Tích Hợp Khối Key Takeaway Chuẩn Hóa | Task mới W3: Bổ sung component khối Key Takeaway chuẩn hóa phục vụ tóm tắt bài viết | Trọng | Design | `In Progress` |
| Khắc Phục Lỗi Giao Diện Biên Tập 1 | Task mới W3: Xử lý dứt điểm lỗi giao diện hiển thị và thao tác trên thanh công cụ soạn thảo | Trọng | Frontend | `In Progress` |
| Khắc Phục Lỗi Giao Diện Biên Tập 2 | Task mới W3: Sửa lỗi con trỏ và định dạng văn bản khi dán nội dung từ nguồn ngoài | Trọng | Frontend | `In Progress` |

---

### 2. PLG Project
- **Nhân sự phụ trách:** Trọng, Hoan

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Quản Trị Topic Cluster | Kế thừa W2: Chuẩn hóa việc phân loại Cluster từ khóa và đồng bộ với danh mục bài viết trên Blog CMS | Trọng | Hoan | `In Progress` |
| PLG Project Cho Blog Common | Kế thừa W2: Tạo PLG Project và nối vào các bài Blog trên nền tảng MoSpark | Trọng | Hoan | `In Progress` |
| Xây Dựng Dashboard Pipeline Bài Viết | Task mới W3: Tạo giao diện Dashboard trực quan thể hiện số bài Outline, Draft, Chờ Duyệt, Published, Tổng bài và theo dõi lượt xem (views) bài viết | Trọng | Hoan | `In Progress` |
| Quản Trị Cluster Trên MoSpark | Task mới W3: Xây dựng và chuẩn hóa tính năng quản lý Topic Cluster bài viết trực tiếp trên MoSpark | Trọng | Hoan | `In Progress` |
| Xây Dựng Landing Page Cho PLG | Task mới W3: Thiết kế và triển khai Landing Page phục vụ chiến dịch PLG trên nền tảng Web | Trọng | Design | `In Progress` |
| Tính Năng Tải Report Dữ Liệu | Task mới W3: Bổ sung tính năng xuất/tải báo cáo dữ liệu pipeline bài viết và hiệu suất nội dung | Trọng | Data | `In Progress` |
| Khắc Phục Lỗi UI Bảng 50 Dòng | Task mới W3: Sửa lỗi hiển thị giao diện bảng phân trang khi tải danh sách bài viết từ 50 dòng trở lên | Trọng | Frontend | `In Progress` |
| Sắp Xếp Bài Viết Theo Trạng Thái | Task mới W3: Tích hợp tính năng lọc và sắp xếp (sort) danh sách bài viết theo trạng thái (status: Outline, Draft, Published) | Trọng | Frontend | `In Progress` |

---

### 3. Puck Editor
- **Nhân sự phụ trách:** Duy, Nhật

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Nghiên Cứu Giải Pháp Blog Section | Kế thừa W2: Nghiên cứu giải pháp nhúng khối nội dung Blog vào Puck Editor; Duy hỗ trợ user tìm bài Blog khi tạo Blog section | Duy | Frontend | `In Progress` |
| Bổ Sung Template Menu Header Cho Hubs | Kế thừa W2: Bổ sung thêm Template cho Menu Header cho các dự án Hub trong Puck Editor | Nhật | Design | `In Progress` |

---

### 4. MoBase
- **Nhân sự phụ trách:** Hùng, Nhật

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Đồng Bộ Component & Token V2 | Kế thừa W2: Đảm bảo các component mới tuân thủ đúng chuẩn Design Token V2 của MoBase | Hùng | Nhật | `In Progress` |

---

### 5. Tìm Kiếm (/tim-kiem)
- **Nhân sự phụ trách:** Hiếu, Duy

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Xây Dựng & Cập Nhật Knowledge Base Tìm Kiếm | Kế thừa W2: Xây dựng và cập nhật dữ liệu Knowledge Base phản hồi chính xác kết quả trên trang `/tim-kiem` | Hiếu | Duy | `In Progress` |

---

### 6. Blog Common
- **Nhân sự phụ trách:** Duy, Hùng

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Migration Blog Admin Tool Qua MoSpark | Kế thừa W2: Tiếp tục migration toàn bộ blog ở Admin Tool cũ qua nền tảng MoSpark | Duy | Hùng | `In Progress` |

---

### 7. Quiz
- **Nhân sự phụ trách:** Thuận, Web Dev

| Hạng mục Công việc | Mô tả Chi tiết & Tiêu chí Hoàn thành (AC) | PIC Chính | Phối hợp | Trạng thái |
| :--- | :--- | :--- | :--- | :---: |
| Bổ Sung Quiz Trong Bài Blog | Task mới W3: Tích hợp component Quiz tương tác trong bài viết Blog, đặt vị trí ngay bên trên phần Author | Thuận | Web Dev | `In Progress` |
