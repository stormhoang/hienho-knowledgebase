# **WEB PLATFORM - ĐỀ XUẤT CẤP QUYỀN GOOGLE CLOUD CONSOLE & GOOGLE API (GSC & GA4)**

## **1. Bối cảnh**

Trong định hướng chiến lược của Web Platform, hệ thống đang chuyển dịch thành nền tảng AI-Powered Web Engine. Để vận hành mô hình này, dữ liệu từ các hệ thống đo lường và công trị tìm kiếm không chỉ dừng lại ở việc xem báo cáo mà phải trở thành "nhiên liệu" đầu vào trực tiếp cho các **AI Workflows (AI Agents & Automation Systems)** nhằm tự động hóa tối ưu nội dung, thứ hạng và bảo vệ sức khỏe website theo thời gian thực.

Hiện tại, việc khai thác dữ liệu GA4 và GSC đối mặt với hai rào cản chính:

* **Thiếu đường ống đồng bộ báo cáo High-Level**: Chưa có cơ chế Auto-sync trực tiếp dữ liệu thô từ BigQuery lên Google Sheets cho Ban Giám Đốc và các Quản lý theo dõi chỉ số MTD mà không phụ thuộc vào thao tác trích xuất thủ công.
* **Chưa kích hoạt API phục vụ AI Workflows**: Chưa kết nối API của Google Search Console (GSC) và Google Analytics 4 (GA4) với hệ thống AI Agent để tự động phát hiện suy giảm thứ hạng (Query Positioning), phân tích hiệu suất trang (URL Performance), kiểm tra biến động liên kết (Backlinks) và tự động đề xuất/thực thi giải pháp tối ưu.

Đề xuất này xin cấp quyền quản trị và khởi tạo tài khoản dịch vụ (Service Account) trên Google Cloud Console (GCP) nhằm giải quyết dứt điểm hai nhu cầu trên.

---

## **2. Nguyên tắc đề xuất**

Đề xuất được xây dựng dựa trên 4 nguyên tắc cốt lõi:

### **Automate High-Level Reporting**

Đảm bảo khả năng:

* Kết nối trực tiếp BigQuery với Google Sheets qua Service Account theo lịch trình cố định.
* Cung cấp bức tranh toàn cảnh MTD (Active Users, Pageviews, Net Add, Web-to-App Conversions) cho Ban Giám Đốc chuẩn Single Source of Truth (SSOT).

### **AI-Powered Optimization Workflows**

Đảm bảo khả năng:

* Cung cấp dữ liệu chi tiết qua GSC & GA4 APIs cho AI Workflows tự động phân tích thứ hạng từ khóa (Query Positioning) và CTR của từng URL.
* Kích hoạt AI Agent tự động phát hiện sụt giảm vị trí, nhận diện xu hướng GEO/Search Intent mới và đề xuất hướng điều chỉnh nội dung/kỹ thuật.

### **Proactive Website Safeguard**

Đảm bảo khả năng:

* Thiết lập hệ thống AI Safeguard tự động quét và cảnh báo các bất thường về cấu trúc liên kết (Backlinks decay/spam).
* Giám sát trạng thái thu thập dữ liệu (Crawl/Indexation) và biến động traffic bất thường nhằm bảo vệ an toàn toàn diện cho website.

### **Secure & Governance-Compliant**

Đảm bảo khả năng:

* Áp dụng nguyên tắc quyền tối thiểu (Least Privilege) cho Service Account và API Keys.
* Quản lý tập trung Credential trên Google Cloud Console của doanh nghiệp với hệ thống Audit Log minh bạch.

---

## **3. Chuẩn cấp quyền & Tài khoản Google Cloud Console (GCP)**

### **Đặc tả Service Account & IAM Roles**

Khởi tạo **01 Dedicated Service Account** phục vụ Web Data & AI Automation Engine với các vai trò IAM sau:

| Loại phân quyền | Vai trò IAM (IAM Role) | Phạm vi áp dụng (Scope) | Mục đích sử dụng |
| ----- | ----- | ----- | ----- |
| BigQuery Access | BigQuery Data Viewer / BigQuery Job User | Project / Dataset GA4 & GSC Export | Truy vấn dữ liệu thô phục vụ Auto-sync High-Level Sheets |
| Search Console API | Webmaster Read-Only (`webmasters.readonly`) | Google Search Console Properties | Cung cấp dữ liệu Query, URL & Backlinks cho AI Workflows |
| Analytics API | Google Analytics Read-Only (`analytics.readonly`) | GA4 Property | Cung cấp dữ liệu User Journey & Conversion cho AI Engine |
| Google Drive / Sheets | Google Sheets API & Drive API Scope | Target Master Google Sheets | Tự động đồng bộ báo cáo quản trị |

### **API Services Cần Kích Hoạt (Enabled APIs)**

* **Google Search Console API**: Truy xuất thứ hạng từ khóa, trang đích, chỉ số CTR và liên kết trỏ về.
* **Google Analytics Data API (v1beta)**: Truy xuất chỉ số tương tác, sự kiện tùy chỉnh và phễu chuyển đổi.
* **BigQuery API & BigQuery Storage API**: Tối ưu tốc độ trích xuất dữ liệu tập trung lớn.
* **Google Sheets API v4**: Ghi và cập nhật dữ liệu tự động lên bảng tính báo cáo Executive.

---

## **4. Luồng Xử lý Dữ liệu & Vận hành AI Workflows**

Hệ thống hạ tầng dữ liệu và AI Workflows được chia thành 4 bước vận hành tiêu chuẩn:

| Bước | Giai đoạn | Trải nghiệm & Luồng dữ liệu | Cơ chế kỹ thuật | Hạ tầng / Công cụ |
| ----- | ----- | ----- | ----- | ----- |
| 1 | Data Ingestion | Tự động kích hoạt job theo lịch trình, gọi API lấy dữ liệu thô từ GSC, GA4 và truy vấn BigQuery | Service Account thực hiện Authentication và lấy dữ liệu định kỳ (Daily/Hourly) | GCP Service Account, GSC/GA4 APIs, BigQuery |
| 2 | Executive Auto-Sync | Số liệu kinh doanh MTD tự động tổng hợp và ghi trực tiếp vào file báo cáo quản trị | Gọi Google Sheets API v4 ghi dữ liệu vào các ô/tab quy định | BigQuery, Google Sheets API v4 |
| 3 | AI Optimization Workflows | AI Agent phân tích biến động thứ hạng từ khóa, hiệu suất URL và intent tìm kiếm để đề xuất tối ưu | AI Model xử lý dữ liệu GSC/GA4 API, so sánh baseline và tạo báo cáo đề xuất tối ưu nội dung | Python Automation Engine, AI Agent Workflow |
| 4 | AI Safeguard & Alerting | AI Agent tự động rà soát độc hại, mất backlink, lỗi crawl/indexation và cảnh báo tức thì | Rule-based & ML Anomaly Detection kiểm tra ngưỡng biến động tiêu cực | Health DB, Automated Alerting Channel |

---

## **5. Đặc tả Chi tiết Các AI Workflows & Hạng mục Triển khai**

### **Hạng mục 1: Auto-sync Báo cáo High-Level (BigQuery ➔ Google Sheets)**

* **Chỉ số tự động đồng bộ**: Total Pageviews, Active Users, Net Add Users, Web-to-App Conversions, MTD Target vs Actual.
* **Tần suất**: Hàng ngày (Daily Auto-sync lúc 06:00 AM).
* **Mục tiêu**: Loại bỏ hoàn toàn công đoạn làm báo cáo thủ công, đảm bảo tính nhất quán dữ liệu cho Ban Giám Đốc.

### **Hạng mục 2: Các AI Workflows Tối ưu hóa (Proactive Optimization)**

#### **AI Query Positioning & Intent Analyzer**

* Phân tích biến động vị trí từ khóa (Query Positioning), lượt nhấp (Clicks) và lượt hiển thị (Impressions).
* Tự động phát hiện hiện tượng ăn thịt từ khóa (Keyword Cannibalization) và nhóm từ khóa bị trượt thứ hạng.
* AI Agent đề xuất kế hoạch cập nhật nội dung (Content Refresh) và tối ưu hóa cấu trúc Heading/Meta.

#### **AI URL Performance & CTR Optimizer**

* Giám sát hiệu suất từng URL theo chuyên mục (Cinema, Financial, Vehicle, Student...).
* Lọc danh sách URL có lượt hiển thị cao nhưng CTR thấp hơn trung bình ngành.
* AI Agent tạo gợi ý thay đổi tiêu đề (Title) và mô tả (Meta Description) để tăng tỷ lệ nhấp.

### **Hạng mục 3: Các AI Workflows Bảo vệ Website (Website Safeguard)**

#### **AI Backlink Health & Anomaly Detector**

* Theo dõi danh sách Referring Domains và các liên kết trỏ về từ GSC API.
* AI Agent phát hiện kịp thời tình trạng sụt giảm liên kết chất lượng (Lost Backlinks) hoặc bị tấn công bằng liên kết bẩn (Spam Backlinks).

#### **AI Technical Health & Indexing Safeguard**

* Tự động kiểm tra trạng thái lập chỉ mục (Indexing Status) và phát hiện các lỗi thu thập dữ liệu (Crawl Errors, 4xx/5xx).
* Cảnh báo ngay lập tức khi xuất hiện sụt giảm lưu lượng truy cập bất thường do Google tung ra các bản cập nhật thuật toán (Core Search Updates).

---

## **6. Lộ trình Triển khai & Cột mốc**

| Giai đoạn | Thời gian | Tên Giai Đoạn | Chi Tiết Triển Khai & Mục Tiêu |
| ----- | ----- | ----- | ----- |
| Giai đoạn 1 | Tuần 1 | Khởi tạo & Cấp quyền GCP | Tạo Project trên GCP, kích hoạt các API (GSC, GA4, BigQuery, Google Sheets), khởi tạo Service Account và phân quyền IAM |
| Giai đoạn 2 | Tuần 2 | Auto-sync High-Level Sheets | Xây dựng pipeline kết nối BigQuery ➔ Google Sheets phục vụ báo cáo quản trị MTD |
| Giai đoạn 3 | Tuần 3 | Triển khai AI Optimization Workflows | Xây dựng AI Agent kết nối GSC/GA4 APIs để tự động phân tích Query Positioning và URL Performance |
| Giai đoạn 4 | Tuần 4 | Triển khai AI Safeguard & Alerting | Đóng gói AI Workflow tự động theo dõi Backlinks, lỗi Indexation và kích hoạt hệ thống cảnh báo sự cố |

---

## **7. Kỳ vọng & Giá trị Mang lại**

* **Tự động hóa 100% báo cáo High-Level**: Giúp Ban Giám Đốc và Quản lý theo dõi dữ liệu kinh doanh liên tục mà không cần thao tác trích xuất thủ công.
* **Chuyển dịch sang AI-Driven Optimization**: Chuyển từ việc phân tích thủ công sang sử dụng AI Workflows tự động phát hiện cơ hội tăng trưởng thứ hạng và tối ưu CTR.
* **Bảo vệ sức khỏe Website chủ động**: AI Safeguard liên tục rà soát dữ liệu GSC/GA4 API để phát hiện và xử lý sự cố rớt thứ hạng, mất backlink hoặc lỗi kỹ thuật trong vòng 24h.
* **Xây dựng hạ tầng AI bền vững**: Tạo nền tảng chuẩn hóa dữ liệu để phát triển các AI Agent phức tạp hơn trong tương lai cho Web Platform.
