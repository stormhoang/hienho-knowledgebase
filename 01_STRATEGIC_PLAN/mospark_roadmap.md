# MOSPARK MASTER PRODUCT ROADMAP
## Lộ trình Năng lực Nền tảng Tăng trưởng (Growth OS) momo.vn

> **Owner:** Văn Hiến (Web Product Lead) & Anh Bảo (Head of Web Platform)
> **Tiến độ:** H1/2026 (Đã hoàn thành) - H2/2026 (Hiện tại) - 2027+ (Tầm nhìn)
> **Trạng thái:** Active
> **Phiên bản:** v3.6 (Cập nhật định hướng hạ tầng truyền thông và phân biệt dự án PLG)

---

## 1. Tầm nhìn Chiến lược & Mô hình Trưởng thành Nền tảng

MoSpark được định vị là **Growth OS (Hệ điều hành tăng trưởng)** của momo.vn. Bản lộ trình này tập trung vào việc phát triển năng lực của **12 Modules cốt lõi** qua các giai đoạn, từ khởi tạo công cụ (H1/2026) đến nâng cấp tính năng tối ưu chuyển đổi & tự động hóa (H2/2026) và tiến tới tự trị vận hành bằng AI (2027+).

Về mặt phạm vi sản phẩm hỗ trợ, MoSpark phân định rõ hai trụ cột hoạt động:
1. **Dự án Product-Led Growth (PLG):** Các dự án xây dựng công cụ, widget tương tác (như Tra cứu Phạt Nguội, Vay Nhanh, Trả Góp Simulator) có cam kết trực tiếp về chỉ số tăng trưởng số (W2A rate, Activation, Transactions).
2. **Mini Web & Landing Page Truyền thông:** Phối hợp cùng các Cell Teams triển khai các trang nội dung chuyên đề, chiến dịch PR thương hiệu (như Landing Page báo cáo lừa đảo dự án Trust, ATBM). Nhóm sản phẩm này tận dụng hạ tầng kéo thả và CMS của MoSpark để tối ưu vận hành nhưng **không gán các cam kết tăng trưởng số cứng**, tập trung vào tính toàn vẹn thông tin và giáo dục người dùng.

---

## 2. Chi tiết các Tính năng đã Hoàn thành trong H1/2026 (Completed Breakdown)
*Hạ tầng và các công cụ phục vụ sản xuất nội dung quy chuẩn, số hóa merchant, kéo thả giao diện và chatbot RAG đã hoàn thành trong nửa đầu năm:*

### 1. GenAI Content
*   **Tích hợp API Claude:** Vận hành luồng sinh bài viết tự động 2 tầng (Outline và chi tiết bài Blog/Long Content).
*   **Metrics & Cost Tracking:** Thu thập và hiển thị chính xác số lượng Input/Output Tokens sử dụng của từng bài viết.
*   **Minh bạch chi phí:** Hiển thị trực quan chi phí tài chính (USD/VND) tiêu tốn cho API tại mỗi giai đoạn sinh bài viết trên giao diện.

### 2. PLG Project
*   **Quản trị Dự án Growth (Phạt Nguội làm Pilot):** Khu vực quản lý tập trung các chiến dịch Product-Led Growth.
*   **Keywords Ingestion:** Hoàn thành tính năng upload trực tiếp tệp CSV Keyword Research để tự động tạo và phân loại các cụm Theme/Cluster.
*   **Cluster Sizing:** Quản lý dung lượng tìm kiếm (Volume Search) và kiểm soát số lượng Cluster bài viết cần GenAI sản xuất.
*   **Visual Status Board:** Hiển thị và theo dõi trạng thái thời gian thực của từng Cluster (Chưa viết, Đã viết Outline, Đã xuất bản).
*   **Mối quan hệ mật thiết 1-1:** Thiết lập liên kết logic 1-1 chặt chẽ giữa mỗi Cluster Keyword trong PLG Project và bài viết tương ứng trên Blog Editor.
*   **Quy tắc xóa bài viết từ gốc:** Ngăn chặn việc xóa bài viết trực tiếp từ Blog Editor. Bài viết bắt buộc phải được xóa từ gốc (Source-deleting) tại màn hình quản lý của PLG Project.
*   **Microsite Blog Editor Sync:** Luồng đồng bộ một chạm giúp PM dễ dàng đi thẳng tới Blog Editor nằm trong Microsite Phạt Nguội.

### 3. Merchant Page
*   **Đồng bộ đối tác Ví Trả Sau:** Nạp và lưu trữ dữ liệu của hơn **200K+ Merchant MoMo** có chấp nhận thanh toán qua Ví Trả Sau.
*   **Dữ liệu thực thể chi tiết:** Khai thác và đồng bộ các trường dữ liệu quan trọng gồm: Tên cửa hàng, Địa chỉ hành chính kèm tọa độ (Vĩ độ Lat / Kinh độ Long), Số điện thoại liên hệ, Tên chủ quán và Danh mục ngành hàng (Category).
*   **Đa dạng hóa Template theo Category:** Thiết lập sẵn hệ thống template đa dạng tối ưu hiển thị cho từng ngành hàng dịch vụ khác nhau (F&B, Beauty, Retail...).
*   **Thiết lập Umami Tracking:** Tích hợp mã theo dõi Umami tracking riêng cho từng merchant page để đo lường traffic và CTR.
*   **Luồng khởi tạo Merchant tự động:**
    *   Map mã M4B ID (MoMo for Business) của đối tác.
    *   Kiểm tra tài khoản chính thức (Official Account - OA), cào dữ liệu đánh giá (MoMo Review) và hình ảnh cửa hàng.
    *   Tự động cào dữ liệu Google Maps API để làm giàu context.
    *   GenAI tự động viết nội dung bài giới thiệu merchant và tạo hình ảnh cửa hàng theo template thương hiệu.
    *   Bàn giao sang Merchant Editor để sẵn sàng duyệt xuất bản.

### 4. Microsite
*   **Microsite Engine:** Bước khởi tạo đầu tiên khi xây dựng dự án PLG Project trên Web.
*   **Giao diện quản lý cấu trúc:** Cấu hình sơ đồ cây liên kết trang (site structure) và chỉnh sửa inline chi tiết từng trang bằng Puck Editor.
*   **Quản trị SEO & AI Search Policy:** Quản lý SEO metadata của trang, thiết lập robots.txt và bước đầu tạo file `llms.txt` của dự án.
*   **Performance Metrics:** Tích hợp trực tiếp mã theo dõi Umami tracking để hiển thị hiệu năng (Traffic, Views, Clicks) ngay trên dashboard của Microsite.
*   **Hạ tầng Đăng nhập & Phân quyền HRM (Access & Identity Sync):** Tích hợp cổng đăng nhập Gmail doanh nghiệp qua `ldp.mservice.io`. Hệ thống tự động đồng bộ API với HRM của công ty để lấy dữ liệu Email, Tên, Cấp bậc (Level/Role) và Bộ phận (Division) của User, sẵn sàng phân lập quyền truy cập và cấp quyền sử dụng tức thì khi User đăng nhập.

### 5. SEO Inventory
*   **Bản đồ thị trường (Market Cap):** Hiển thị tổng quan quy mô tìm kiếm của từng Division theo từng Use Case dịch vụ cụ thể.
*   **Ràng buộc logic khởi tạo (Integrity Guard):** Ràng buộc nghiệp vụ cứng trên CMS: khi tạo một PLG Project mới, bắt buộc phải chọn liên kết với một Microsite và một SEO Inventory tương ứng để tránh phân mảnh dữ liệu.

### 6. Blog Editor
*   **Blog CMS quản trị GenAI Content:** Quản lý và xuất bản các bài viết được tạo ra từ GenAI.
*   **Tiptap Editor Integration:** Bộ soạn thảo WYSIWYG Tiptap cho phép Editor chỉnh sửa format, chèn ảnh, viết thêm nội dung linh hoạt.
*   **Keyword & Metadata Auto-Sync:** Tự động đồng bộ các từ khóa chính (Primary), từ khóa phụ (Secondary) và dữ liệu meta từ PLG Project sang Editor khi kích hoạt gen bài bằng AI.
*   **Khóa chỉnh sửa từ khóa trên Editor:** Vô hiệu hóa hoàn toàn quyền chỉnh sửa các từ khóa chính (Primary Keyword) và từ khóa phụ (Secondary Keyword) trực tiếp tại giao diện Blog Editor để tránh sai lệch dữ liệu gốc.
*   **Thumbnail & Social Templates:** Tính năng upload ảnh chia sẻ mạng xã hội và ảnh đại diện bài viết (Thumbnail) sử dụng khung mẫu (template) thiết kế riêng.
*   **AI Performance Tracker:** Dashboard đo lường hiệu suất sinh bài của AI bao gồm chi phí API và thời gian hoàn thành.

### 7. Landing Page Builder
*   **LP Creation Flow:** Hỗ trợ 3 luồng tạo Landing Page gồm: Tạo bằng Prompt AI (Sử dụng Gemini để sinh layout tự động), tạo từ Template mẫu, hoặc tạo từ trang trắng (Blank slate).
*   **Mobase Drag-and-drop Builder:** Tích hợp Puck Editor để chỉnh sửa kéo thả trực tiếp các khối giao diện (Blocks) được thiết kế theo đúng chuẩn hệ thống Mobase Design System.
*   **Cell Teams Self-service Sharing:** Tính năng chia sẻ quyền truy cập cho PM/PO các Cell Teams tự vào kéo thả và chỉnh sửa độc lập.
*   **Umami Performance Check:** Tích hợp sẵn tracking Umami để đo lường hiệu suất chuyển đổi của Landing Page.

### 8. Chatbot & Knowledge Base
*   **Chatbot Customizer:** Hoàn thiện giao diện UI/UX Chatbot động (cho phép đổi màu sắc, theme theo nhận diện thương hiệu).
*   **RAG Knowledge Base Pipeline:** Tự động cào dữ liệu các bài viết của dự án PLG, thực hiện chuyển đổi (vectorization) và nạp vào Vector Database để chạy cơ chế RAG tư vấn tự động khi user chat.
*   **Typebot Integration:** Tích hợp Typebot để PM tự xây dựng kịch bản hội thoại và các bước điều hướng khách hàng.

### 9. Ads Manager
*   **Quản trị chiến dịch hiển thị:** Xây dựng luồng tạo và cấu hình Ads Campaign, Campaign Group và Ad Items.
*   **Đa định dạng Ads:** Hỗ trợ cấu hình 3 định dạng hiển thị quảng cáo W2A chính trên Web: Float (Banner nổi), Balloon (Bóng bay ở góc), và Popup.
*   **Umami Ads Attribution:** Tích hợp Umami tracking để đo lường click và CTR của từng Ad Item.

### 10. Utilities Tool
*   **Quản lý Tiện ích Tăng trưởng (Utilities Center):** Nơi quản lý tập trung toàn bộ các Utilities (tiện ích tương tác/giả lập) của MoMo do Cell Team yêu cầu hoặc do Platform chủ động xây dựng để thúc đẩy Product-Led Growth (PLG) trên Web.
*   **Cơ chế Tự động Gán & Thừa kế (Auto-mapping & Auto-inheritance):** Việc hiển thị tiện ích trên các trang Microsite/Blog được thực hiện tự động qua cơ chế gán 1-1 với Microsite tương ứng. Mọi trang con thuộc Microsite đó tự động thừa kế và hiển thị tiện ích tại đúng vị trí quy chuẩn, hoàn toàn không cần Cell Team phải nhúng mã Shortcode hay sử dụng editor kéo thả các block code tự build (chưa hỗ trợ kéo thả tiện ích tự build).
*   **Liên kết Bán chéo (Ads Manager Cross-sell):** Kết hợp chặt chẽ với module Ads Manager để thực hiện kịch bản bán chéo (cross-sell) các Utilities này bằng cách "khoét slot" quảng cáo hiển thị tương thích trên các trang/dự án khác có liên quan.

### 11. MoSpark Request
*   *Trạng thái H1:* Chưa triển khai (Được loại bỏ khỏi phạm vi thực thi H1 và chuyển sang kế hoạch H2).

### 12. Umami Tracking & User Identity (Identify User)
*   **Umami Base Tracking:** Tích hợp mã theo dõi cơ bản các lượt xem trang (PageView) và tương tác nút bấm (Clicks) cho các module Microsite, Landing Page, và Ads.
*   **User Identity Back-end:** Hoàn thành phát triển logic phân tích định danh và luồng dữ liệu stitch hành vi người dùng (Anonymous ➔ Logged-in ➔ chèn tham số `?wui=` vào link deep-link Onelink ➔ đối khớp chuyển đổi KYC/giao dịch trong App MoMo).

---

## 3. Lộ trình Nâng cấp Tính năng trong H2/2026 (Active)
*Giai đoạn đóng vòng lặp tối ưu hóa, tích hợp luồng thanh toán API GenAI, đo lường ROI Web-to-App và mở rộng năng lực tự vận hành cho Cell Teams.*

### 1. GenAI Content
*   **Enterprise Multi-Model Hub:** Tích hợp cổng API gateway tập trung của công ty hỗ trợ đa dạng model (Gemini, Claude, GPT) tùy theo nhu cầu và tính chất của từng dự án Cell Team.
*   **GenAI Billing & Chargeback System:** Tự động tổng hợp chi phí tạo bài viết từ GenAI (dựa trên token tiêu thụ thực tế) để xuất "hóa đơn ảo" khấu trừ trực tiếp vào ngân sách (Budgets) của từng Cell Team.
*   **Custom Use-Case Prompts (Content Writer Agent):** Cho phép cấu hình các Prompts chuyên biệt viết Outline/Detail cho từng Use Case cụ thể. Mỗi dự án được gán một "Content Writer" riêng biệt được tối ưu hóa để đảm bảo chất lượng văn phong, kiểm soát chi phí, và định hướng chính xác theo Business Context.
*   **Creative GenAI Suite (Image & Video):** Tự động tạo hình ảnh minh họa (theo template chuẩn Mobase) và video ngắn từ prompt trực tiếp trong luồng sản xuất content.
*   **Tự động hóa luồng viết lại (Rewrite Loop):** Nhận tín hiệu cảnh báo từ Content Decay để tự động tạo draft nâng cấp bài viết.

### 2. PLG Project
*   **Mô hình Agent tự vận hành (Autonomous Content Production Agent):** Định hình mỗi PLG Project như một thực thể độc lập tự vận hành gồm 3 cấu phần: một Business Context riêng, một Market Cap (SEO Inventory) riêng, và một GenAI (Content Writer) Agent riêng để tự động hóa toàn trình quy trình sản xuất nội dung.
*   **BigQuery Search Console Sync:** Đồng bộ dữ liệu GSC và GA4 từ BigQuery về MoSpark để hiển thị thứ hạng (Position) trung bình của từng từ khóa đối với mỗi Cluster.
*   **Google Ads Keyword Planner API:** Tự động kết nối API lấy dung lượng tìm kiếm (Volume Search) thực tế khi PM làm kế hoạch từ khóa (Keyword research/Content Plan).
*   **Cluster-level Quality Scoring Dashboard:** Hiển thị điểm SEO/GEO trung bình của toàn bộ Cluster để PM có cái nhìn tổng quan thay vì chỉ hiển thị ở mức bài viết đơn lẻ.
*   **Priority Scoring Engine:** Tính năng tự động tính toán điểm ưu tiên SEO-ICE trực tiếp trong danh sách keywords.

### 3. Merchant Page
*   **Merchant Listing & Category Hub Pages (Trang danh sách cửa hàng Ví Trả Sau):** Phát triển các trang danh sách (Listing Pages) và trang Hub cho phép tìm kiếm, lọc các địa điểm chấp nhận thanh toán Ví Trả Sau theo Khu vực địa lý (Tỉnh/Thành, Quận/Huyện), Category ngành hàng (F&B, Mua sắm, Làm đẹp...) và các Điều kiện ngữ cảnh đặc biệt (gần trường học, gần trung tâm thương mại/mall, mở cửa 24/7...).
*   **Automated Sitemap Splitting Engine:** Tự động phân tách và quản lý sitemap động cho hàng trăm nghìn trang merchant để tối ưu hóa crawl budget của Google.
*   **Local SEO Schema Auto-Generator:** Tự động sinh cấu trúc schema LocalBusiness (NAP data) chuẩn xác cho từng merchant page để đẩy mạnh tốc độ index của Google.
*   **Dynamic O2O Deep-linking Generator:** Tự động sinh Onelink deep-link gắn mã cửa hàng động phục vụ cho kịch bản quét QR Code/Soundbox tại quầy của merchant.
*   **Grabfood/Shopeefood Menu Crawling Engine:** Tích hợp tính năng tự động cào (crawl) danh sách thực đơn (Menu) và hình ảnh các món ăn của cửa hàng từ Grabfood/Shopeefood để hiển thị trực tiếp danh mục Món ăn (Dishes/Items) của Merchant trên trang.

### 4. Microsite
*   **Dynamic llms.txt Auto-Exporter:** Tự động xuất và quản lý file `llms.txt` (Master Index) và `llms-full.txt` (per-product) đồng bộ cho từng microsite phục vụ AI crawlers.
*   **Multi-tenant Access & RBAC (Phân quyền đa BU):** Nâng cấp hệ thống phân quyền để hỗ trợ nhiều Cell Teams của các Division quản trị Microsite độc lập trên cùng một hạ tầng.

### 5. SEO Inventory
*   **GSC Real-time Connector:** Kết nối API GSC để tự động tính toán và cập nhật thị phần tìm kiếm thực tế của MoMo (`SoV = Impression GSC / Total Search Volume`) trực tiếp trên hệ thống.
*   **Near Miss Keyword Recommender:** Thuật toán tự động phát hiện và gợi ý các từ khóa ở vị trí 4-15 có volume lớn để tối ưu hóa thứ hạng.

### 6. Blog Editor
*   **Tích hợp SEO/GEO Scoring Gate (Cải tiến H2):**
    *   *Tính năng:* Tích hợp bộ kiểm duyệt và chấm điểm chất lượng trực tiếp vào Editor.
    *   *Hard Block Gate:* Chặn nút Publish nếu điểm SEO/GEO < 60 hoặc vi phạm 1 trong 9 lỗi chặn cứng (Robots=noindex, thiếu canonical, LCP > 2.5s, CLS > 0.1, thiếu CTA...).
    *   *YMYL Compliance:* Tự động quét và chấm điểm E-E-A-T (Author Box hiển thị, link social thật của tác giả và Disclaimer).
*   **CTA Manager (Max 2 CTAs):** Giới hạn tối đa 2 CTA trên một bài blog. Hỗ trợ quản lý vị trí, thiết kế nút bấm và tự sinh deep-link Onelink chuẩn hóa.
*   **Các module cải tiến đề xuất tích hợp:**
    *   *Dynamic FAQ Accordion with Schema Markup:* Tự động sinh Schema FAQ structured data giúp hiển thị rich snippets nổi bật trên Google Search.
    *   *Interactive Table of Contents (TOC):* Sơ đồ điều hướng nhanh theo heading của bài viết, tự động tính toán tiến trình đọc (Reading Progress) của user.
    *   *Contextual Feedback Widget (EEAT trust builder):* Thu thập phản hồi nhanh của user (Like/Dislike hoặc đánh giá độ hữu ích) để gửi tín hiệu tương tác cho thuật toán tìm kiếm và AI Scoring.
*   **Semantic Internal Linking Engine:** Tính năng tự động phân tích ngữ nghĩa (vector embeddings) và gợi ý chèn liên kết nội bộ giữa các bài viết cùng chủ đề để tối ưu link equity.

### 7. Landing Page Builder
*   **Mở rộng Kho Templates:** Đa dạng hóa và bổ sung nhiều mẫu thiết kế Landing Page (Templates) chuẩn hóa sẵn cho các Cell Teams lựa chọn sử dụng nhanh chóng.
*   **Tiêu chuẩn hóa Giao diện & Tự động hóa nội dung (Standard & Auto-mapping):**
    *   *Giao diện mặc định:* Tự động tích hợp sẵn khối Header/Footer tiêu chuẩn khi tạo Landing Page mới (vẫn cho phép Editor chỉnh sửa hoặc ẩn đi nếu cần).
    *   *Auto-mapping Blog/News:* Hỗ trợ kết nối và tự động lấy danh sách bài viết Blog/Tin tức liên quan hiển thị lên Landing Page mà không cần cấu hình thủ công.
*   **Instant Live Preview (Xem Demo nhanh):** Cho phép người dùng xem trước bản Demo trực quan của Landing Page ngay trên hệ thống mà không cần tách source code hoặc build local.
*   **A/B Test Variant Customizer:** Tích hợp giao diện thiết lập các biến thể giao diện (Component swap hoặc URL routing) trực tiếp trên Puck Editor.
*   **Block-level W2A Conversion Tracker:** Đo lường và hiển thị hiệu năng chuyển đổi Web-to-App trực tiếp trên từng block kéo thả của Landing Page (giúp PM đánh giá block nào convert tốt nhất).

### 8. Chatbot & Knowledge Base
*   **Qualitative Data Ingestion Pipeline:** Khả năng nạp, phân tích và vector hóa dữ liệu Meeting Notes (Markdown) từ dự án khảo sát khách hàng (2H Customer) để làm phong phú context của RAG, giúp chatbot trả lời sát với insight thực tế.
*   **Scenario Mapping Engine (Typebot v2):** Nâng cấp kịch bản chatbot tự động điều hướng chuyên sâu theo hành vi người dùng đối với các dịch vụ tài chính phức tạp.

### 9. Ads Manager
*   **Ads Placement Registry & Conflict Resolution:** Bộ điều phối hiển thị quảng cáo tự động dựa trên ngữ cảnh Use Case của bài viết và enforce UX guardrails (Max 1 Popup, Max 2 Balloon).
*   **On-site Anonymous Retargeting Engine:** Tự động hóa việc ghi vết hành vi ẩn danh của người dùng (qua Local Storage) để phân phối ads cá nhân hóa khi họ truy cập các trang dùng chung mà không cần đăng nhập.

### 10. Utilities Tool (PLG Tool Builder)
*   **Low-code Drag-and-drop Tool Configurator:** Nâng cấp từ cấu hình bằng code sang trình kéo thả trực quan để PM tự cấu hình input fields, logic tính toán (Calculator) hoặc tra cứu API (Checker).
*   **Tool Data Pipeline (GEO Moat Generator):** Hệ thống tự động thu thập và tổng hợp dữ liệu tương tác ẩn danh của các công cụ tiện ích để làm nguồn viết bài báo cáo insight tự động, tạo hàng rào GEO Moat độc quyền.

### 11. MoSpark Request
*   **OAuth/SSO Google Integration:** Cho phép các Cell Teams đăng nhập bảo mật bằng tài khoản Gmail công ty vào hệ thống MoSpark.
*   **Instant UAT Sandbox Deployer:** Năng lực tự động tạo một URL chạy trực tiếp trên môi trường UAT để xem trực tiếp (Live Preview) các file HTML Prototype + Brief nghiệp vụ do Cell Teams upload (được tạo nhanh từ Claude) mà không cần tải về local.
*   **Dev Ticket Queue System:** Lưu trữ và quản lý các yêu cầu dưới dạng Ticket trong hàng đợi (Queue) để Dev tiến hành triển khai (hỗ trợ đính kèm brief công thức đối với các Utilities Tool tự gen bằng AI).

### 12. Umami Tracking & User Identity (Identify User)
*   **Hợp tác & Test Hạ tầng (SSO / Edge Cookie Deployment):** Do phần back-end bên dưới đã hoàn thiện trong H1, H2 sẽ tập trung vào việc căn chỉnh hạ tầng (aim lại), cấu hình các Edge Middleware để deploy HttpOnly Cookie an toàn và chạy tích hợp định danh thực tế trên production.
*   **GSC/GA4/BigQuery Integrated Dashboard:** Tích hợp dữ liệu từ Google Search Console, Google Analytics 4, BigQuery và Umami để hiển thị bức tranh toàn cảnh về traffic sources, engagement.
*   **End-to-End W2A Funnel Stitching:** Đo lường chi tiết hành trình người dùng từ Click Web ➔ Click to App ➔ Open App ➔ Login ➔ MAU thực tế trên ứng dụng MoMo.

---

## 4. Tầm nhìn Dài hạn 2027+ (Future Vision - Agentic)
*Giai đoạn AI chủ động vận hành vòng lặp tăng trưởng, cá nhân hóa sâu trải nghiệm người dùng và mở rộng tự động hóa.*

*   **GenAI Content:** *Real-time Content Adaptation* - Tự động thay đổi cấu trúc và văn phong bài viết theo thời gian thực dựa trên intent và nguồn traffic cụ thể của người đọc.
*   **PLG Project:** *Predictive Whitespace Discovery* - AI tự động quét thị trường và đề xuất tạo các PLG Projects mới dựa trên các khoảng trống từ khóa.
*   **Merchant Page:** *Contextual Merchant Personalization* - Tự động cá nhân hóa menu, chương trình khuyến mãi theo thời gian thực dựa trên vị trí địa lý và lịch sử tiêu dùng của user.
*   **Microsite:** *Autonomous Page Architecture* - AI tự động điều chỉnh cấu trúc trang, sơ đồ liên kết (sitemap) và đề xuất cập nhật.
*   **SEO Inventory:** *Predictive Demand Engine* - Hệ thống tự động dự báo sự dịch chuyển volume tìm kiếm của các dịch vụ tài chính trước 30 ngày.
*   **Blog Editor:** *Autonomous Linking Graph Manager* - AI tự động tối ưu hóa và liên kết chéo nội bộ mà không cần tác vụ thủ công.
*   **Landing Page Builder:** *Dynamic LP Layouts* - Năng lực tự động render layout và CTA thích ứng với phân khúc hành vi người dùng ẩn danh.
*   **Chatbot & Knowledge Base:** *Transactional AI Agent* - Trợ lý ảo kết nối trực tiếp với API giao dịch của MoMo App để giúp người dùng xử lý trực tiếp các tác vụ (tra cứu lỗi, hoàn tiền...) ngay trên Web Chatbot.
*   **Ads Manager:** *Autonomous Ad Optimization* - AI tự động phân tích CTR/W2A CR để tự thay đổi vị trí quảng cáo, thiết kế banner và nội dung CTA.
*   **Utilities Tool:** *AI-optimized Calculation Engine* - AI tự động tối ưu thuật toán tính toán và gợi ý API kết nối dựa trên phản hồi hành vi sử dụng của user.
*   **MoSpark Request:** *AI-to-Production Pipeline* - AI tự động kiểm tra bảo mật, sự tương thích Mobase CSS của HTML Prototype và tự động publish lên Production khi được phê duyệt.
*   **Umami Tracking & User Identity (Identify User):** *Predictive Attribution Modeling* - AI tự động phân bổ trọng số đóng góp của từng điểm chạm trên Web đối với chỉ số MAU mới.

---

## 5. Các Mốc Nghiệm thu Tính năng Chiến lược (Key Milestones)

*   **Milestone 1 (31/07/2026):** Hoàn tất robots.txt Layer 2+3 + Deploy Master llms.txt + Khởi chạy sitemap index cho 200K Merchant Pages.
*   **Milestone 2 (30/09/2026):** Hoàn thành Migration Phase 3 (Đóng hoàn toàn Admin Panel cũ) + Ra mắt SEO Inventory v2 (SoV & BQ Position Sync).
*   **Milestone 3 (31/10/2026):** Launching MoSpark Request (Gmail login & Sandbox UAT preview) + Ads Retargeting live.
*   **Milestone 4 (31/12/2026):** Launching PLG Low-code Tool Builder (M9) + Deploy 2 công cụ Calculator mới + Báo cáo Revenue Attribution ROI (W2A Funnel Stitching) trên BigQuery.
*   **Milestone 5 (Q2/2027):** Launching Autonomous Campaign Operation (AI tự vận hành chiến dịch) + Thử nghiệm Agentic Help Center cho các sản phẩm Tài chính.

---
*Owner: Web Product Lead & Head of Web Platform | Growth Platform Division (GPD)*
*Document updated: 2026-07-10 22:28 (Local time)*
