# -*- coding: utf-8 -*-
from pathlib import Path

report_path = Path("07_REPORTS/docs/weekly-report-2026-10-26-11-01.md")
with open(report_path) as f:
    text = f.read()

# Replacement for Section III
old_sec_iii = text[text.find("## III. TIẾN ĐỘ CÁC NỀN TẢNG KỸ THUẬT"):text.find("## IV. ĐIỂM NGHẼN & VIỆC CẦN PHỐI HỢP")]

new_sec_iii = """## III. TIẾN ĐỘ CÁC NỀN TẢNG KỸ THUẬT (PLATFORM PROJECTS)
*(Trích xuất chính xác theo báo cáo công việc của duy.tran2 và hieu.nguyen8 trên Google Drive)*

### 1. Chatbot AI & Hệ Thống Cơ Sở Tri Thức (Knowledge Base)
- **Đội ngũ phụ trách:** AI Platform Engineering (Chủ trì: duy.tran2)
- **Tiến độ & Kết quả tuần qua:**
  - **Trung tâm quản trị đối soát tri thức (Project Center):** Xây dựng bảng điều khiển trung tâm theo dõi số lượng tài liệu đã đồng bộ, số cụm chủ đề, trạng thái đồng bộ và mốc thời gian cập nhật gần nhất cho từng dự án Chatbot.
  - **Quét & đối soát tự động từ Sitemap (Sitemap & Link Scanner):** Tự động đọc sitemap.xml, so khớp với kho tài liệu tri thức hiện có, phân loại thành 2 nhóm rõ ràng: tài liệu còn thiếu (*Missing*) và tài liệu đã đồng bộ (*Synced*), tính toán chính xác tỷ lệ bao phủ tri thức (% Coverage).
  - **Bộ tiêu chuẩn thẩm định điều kiện nạp tài liệu (Eligibility Validation):**
    - *Bài viết Blog:* Tự động xác thực bài viết có tồn tại và đã ở trạng thái xuất bản chính thức hay chưa (chặn hoàn toàn bài nháp hoặc bài đã xóa đưa vào tri thức AI).
    - *Trang Web / Trang con:* Kiểm tra trạng thái xuất bản và bắt buộc nội dung phải chứa ít nhất một khối văn bản dài hoặc khối câu hỏi thường gặp (FAQ) có thông tin thực tế.
    - *Gắn nhãn lý do không đủ điều kiện:* Đưa ra cảnh báo cụ thể (Chưa xuất bản, Không có nội dung dài/FAQ, Không tìm thấy trong hệ thống) để quản trị viên dễ dàng rà soát và bổ sung trên CMS.
  - **Đồng bộ tri thức từ Cây phân cấp trang Web (Web Pages Tree):** Quản lý và đối chiếu trực tiếp từ sơ đồ cây trang web, hỗ trợ thao tác đồng bộ 1-chạm hoặc đồng bộ nhanh theo link URL tùy chọn.
  - **Chuẩn hóa trích xuất nội dung chuyên sâu:** Lọc bỏ banner, hình ảnh trang trí và nút bấm; chỉ trích xuất các phần chữ giàu tri thức (tiêu đề, tóm tắt, từ khóa, H2, nội dung chi tiết và FAQ) để cung cấp ngữ cảnh chính xác cho mô hình ngôn ngữ lớn (LLM).
  - **Tối ưu trải nghiệm quản trị:** Mở trực tiếp tài liệu trong tab mới; căn chỉnh hiển thị thẻ số liệu thống kê cân đối và dễ quan sát.
- **Kế hoạch tiếp theo:** Tiếp tục hoàn thiện bộ tiêu chí đánh giá chất lượng câu trả lời của Chatbot và theo dõi tỷ lệ bao phủ tri thức trên các trang dịch vụ trọng điểm.

---

### 2. Admin Panel: All-in-One Editor & Khối Nội Dung In-App (Chuẩn Bị Build Prod Phase 2)
- **Đội ngũ phụ trách:** Web-in-App & CMS Engineering (Chủ trì: hieu.nguyen8, phối hợp duy.tran2)
- **Tiến độ & Kết quả tuần qua:**
  - **Hoàn thành All-in-One Editor:** Hợp nhất công cụ soạn thảo cho các trang chuyên biệt, gom chỉnh sửa nội dung, danh sách bài viết, banner và khung xem trước lên cùng một màn hình (giảm thao tác chuyển đổi giữa 3-4 trang riêng lẻ).
  - **Phân định quyền tài khoản & Luồng duyệt bài:** Tách bạch rõ quyền giữa người tạo bài viết và người duyệt bài; bổ sung nút chuyển nhanh sang danh sách các bài viết đang chờ duyệt.
  - **Đóng gói các khối nội dung In-App nâng cao:**
    - *Khối Mã khuyến mãi (Voucher):* Biểu mẫu nhập tiêu đề, quyền lợi, mã voucher và hạn dùng; hệ thống tự sinh thẻ ưu đãi chuẩn giao diện MoMo kèm nút sao chép mã.
    - *Khối Hướng dẫn từng bước:* Thêm và sắp xếp các bước có hình ảnh minh họa, tiêu đề, mô tả; tự sinh khối trình chiếu dạng thẻ mô phỏng giao diện điện thoại.
    - *Xem trước giao diện điện thoại (Live Mobile Preview):* Bổ sung khung xem trước trực tiếp ngay trong màn hình chỉnh sửa, hiển thị đúng định dạng các khối nội dung như khi người dùng đọc trên ứng dụng MoMo.
  - **Chuẩn bị hoàn tất nghiệm thu Phase 2:** Rà soát và chạy kiểm thử tự động (Unit Test), làm sạch mã nguồn, chốt ngày build production Phase 2 vào ngày 02/11/2026 cùng nhánh BMC.
- **Kế hoạch tiếp theo:** Hỗ trợ theo dõi vận hành sau đợt build prod Phase 2 vào ngày 02/11 và tiếp nhận phản hồi từ các Cell Teams khi sử dụng các khối nội dung mới.

---

### 3. Cổng Tìm Kiếm Website (`/tim-kiem`) & Hồ Danh Mục URL Toàn Website (URL Catalog)
- **Đội ngũ phụ trách:** Search & Portal Engineering (Chủ trì: hieu.nguyen8)
- **Tiến độ & Kết quả tuần qua:**
  - **Thẻ chuyển tiền nhanh qua số điện thoại:** Khi người dùng nhập số điện thoại hợp lệ vào ô tìm kiếm, web tự nhận diện và hiển thị ngay thẻ chuyển tiền dẫn thẳng vào app MoMo (xử lý nhận diện số điện thoại hoàn toàn ở phía trình duyệt, không gửi số điện thoại lên máy chủ để bảo mật thông tin người dùng).
  - **Banner người dùng mới (New User):** Gắn banner hướng dẫn nhận quà và tải app cho khách truy cập lần đầu vào trang tìm kiếm.
  - **Hoàn thiện thiết kế Hồ danh mục URL toàn website (URL Catalog):**
    - *Bối cảnh:* Dữ liệu link web đang phân tán ở nhiều nơi, chưa có một nguồn chuẩn duy nhất (SSOT) phục vụ đồng thời cho Tìm kiếm, tạo Sitemap theo dự án và cung cấp danh mục URL cho đội AI xây dựng Cơ sở tri thức.
    - *Chốt 4 quyết định thiết kế:* Vị trí lưu trữ theo chuẩn chung hệ thống; bổ sung định danh rút gọn cho từng dự án để sinh Sitemap riêng; khi lọc theo dự án luôn bao gồm các dự án con; giai đoạn đồng bộ tự động trước mắt áp dụng cho Bài viết, Blog và Trang dịch vụ.
    - *Lộ trình triển khai 4 giai đoạn:* (1) Tạo bảng dữ liệu và nạp 51 trang tìm kiếm ưu tiên; (2) Xây dựng lớp đọc dữ liệu dùng chung có cache; (3) Chuyển trang Tìm kiếm sang đọc từ Hồ danh mục; (4) Đồng bộ tự động từ CMS và MoSpark, cung cấp danh mục URL cho đội AI và sinh Sitemap theo dự án.
- **Kế hoạch tiếp theo:** Theo dõi số liệu sử dụng thẻ chuyển tiền và banner bạn mới trên bản chính thức; bắt đầu triển khai giai đoạn 1 của Hồ danh mục URL (tạo bảng dữ liệu trên môi trường phát triển và nạp dữ liệu ban đầu).

---

### 4. Hạ Tầng & Vận Hành MoMo API
- **Đội ngũ phụ trách:** Backend & API Operations (Chủ trì: hieu.nguyen8)
- **Tiến độ & Kết quả tuần qua:**
  - **Mở kết nối cho môi trường phát triển nội bộ:** Bổ sung cấu hình cho phép môi trường dev nội bộ gọi tới hệ thống API trên cả môi trường kiểm thử và môi trường chính, giúp lập trình viên kiểm thử tính năng thuận tiện hơn.
  - **Cập nhật thư viện dùng chung:** Đồng bộ phiên bản mới nhất của các thư viện dùng chung giữa các dự án.
  - **Cấu hình kết nối trung tâm dữ liệu:** Bổ sung cấu hình đảm bảo hệ thống API kết nối ổn định tới các dịch vụ nội bộ của MoMo sau khi triển khai.
  - **Bảo mật & Server-side Proxy:** Tiếp tục rà soát kiểm soát CORS, giới hạn tần suất gọi API (Rate Limiting) và chuẩn bị chuyển đổi lớp máy chủ trung gian cho luồng dữ liệu Merchant.
- **Kế hoạch tiếp theo:** Tiếp tục theo dõi độ ổn định của hệ thống API sau khi cập nhật cấu hình và hỗ trợ triển khai lớp máy chủ trung gian (Server-side Proxy) cho dữ liệu Merchant.

---

### 5. Trang Dịch Vụ Vé Số Trên Website (Lottery Hub)
- **Đội ngũ phụ trách:** Utility Web Engineering (Chủ trì: duy.tran2)
- **Tiến độ & Kết quả tuần qua:**
  - **Sẵn sàng công cụ MoSpark trên Staging:** Đã chuẩn bị sẵn công cụ cấu hình trên môi trường Staging, sẵn sàng hướng dẫn PO vé số tự chỉnh sửa các khối nội dung tĩnh khi PO vào làm quen hệ thống.
  - **Duy trì hiển thị và cache giờ cao điểm:** Đảm bảo kết quả 8 trò chơi Vietlott và bảng kết quả XSKT 3 miền hiển thị ổn định, tải trang nhanh dưới 1,5 giây lúc 18h00 - 18h30 hàng ngày.
- **Kế hoạch tiếp theo:** Hỗ trợ PO vé số thao tác thực tế trên Staging và giám sát tải hệ thống trong khung giờ mở thưởng.

---

"""

text = text[:text.find("## III. TIẾN ĐỘ CÁC NỀN TẢNG KỸ THUẬT")] + new_sec_iii + text[text.find("## IV. ĐIỂM NGHẼN & VIỆC CẦN PHỐI HỢP"):]

with open(report_path, "w") as f:
    f.write(text)

hubs_path = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/reports/weekly-report-2026-10-26-11-01.md")
with open(hubs_path, "w") as f:
    f.write(text)

print("Updated Section III in both files successfully.")
