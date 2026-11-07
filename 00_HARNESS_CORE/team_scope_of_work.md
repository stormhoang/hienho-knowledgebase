# QUY CHUẨN PHẠM VI CÔNG VIỆC NHÂN SỰ WEB PLATFORM (SCOPE OF WORK SSOT)

Tài liệu này xác lập ranh giới trách nhiệm, phạm vi đảm nhiệm (In-scope), giới hạn không phụ trách (Out-of-scope) và luồng phối hợp bàn giao giữa 12 thành viên thuộc Đội ngũ Web Platform (MoMo).

---

## 1. TỔNG QUAN PHÂN BỔ BÀN LÀM VIỆC & NHÂN SỰ

*   **Quy mô:** 12 nhân sự (11 nhân sự đang làm việc + 1 nhân sự sắp gia nhập).
*   **Bàn 01 (8/8 ghế · Cụm Kỹ sư Lập trình & Vận hành Kỹ thuật):** Hoài Anh, Hiếu, Duy, Lộc, Hùng, Nhật, Thuận, Trọng.
*   **Bàn 02 (4/8 ghế có người · Bàn Điều phối, Quản lý & Tăng trưởng):** Hiến, Bảo (đối diện Hiến), Hoan (ngồi cạnh Hiến), Tữ (đối diện Hoan) và 4 ghế trống dự phòng.

---

## 2. MA TRẬN PHẠM VI CÔNG VIỆC CHI TIẾT (12 THÀNH VIÊN)

### 1. Bảo (Senior Manager)
*   **Vị trí bàn:** Bàn 02 (Đối diện Hiến)
*   **Dự án sở hữu:** MoSpark
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Quản lý toàn bộ SE Team và định hướng nền tảng MoSpark.
    *   Phê duyệt kiến trúc kỹ thuật cấp cao và phân bổ nguồn lực kỹ sư cho các dự án.
    *   Phối hợp trực tiếp cùng Web Product Lead (Hiến) thiết lập mục tiêu và tiến độ bàn giao.
*   **Không phụ trách (Out-of-scope):** Không trực tiếp viết code tính năng lẻ của từng Hub, không can thiệp nội dung biên tập hay chiến lược từ khóa SEO.
*   **Điểm bàn giao & Phối hợp:** Bàn giao mục tiêu cho các Team Lead (Hùng, Hiếu, Hoài Anh); phối hợp trực tiếp với Hiến trên trục Chiến lược - Kỹ thuật.

---

### 2. Đặng Hoài Anh (Tech Solution Lead)
*   **Vị trí bàn:** Bàn 01
*   **Dự án sở hữu:** MoSpark Core Backend & API, Web App
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Thiết kế kiến trúc tổng thể MoSpark, database Supabase và cổng YARP API Gateway.
    *   Xây dựng API tích hợp backend Web App và cơ chế đồng bộ dữ liệu M4B.
    *   Đảm bảo khả năng chịu tải và bảo mật cho toàn bộ hệ thống API trung gian.
*   **Không phụ trách (Out-of-scope):** Không trực tiếp làm giao diện UI/UX Front-end của các Hub, không quản trị chiến dịch nội dung.
*   **Điểm bàn giao & Phối hợp:** Bàn giao cổng API và schema cơ sở dữ liệu cho đội ngũ Front-end (Hùng, Nhật, Thuận) và Backend microsites (Duy).

---

### 3. Hiếu Nguyễn (Back-end Team Lead)
*   **Vị trí bàn:** Bàn 01
*   **Dự án sở hữu:** Tracking Pipeline & Cung ứng API
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Trưởng nhóm Backend; bảo đảm tính toàn vẹn của luồng tracking (OneLink, GA4, GTM, Umami).
    *   Đối soát dữ liệu truy cập và chuyển đổi với BigQuery SSOT; quản lý định danh người dùng đa nền tảng (Cross-platform Identity).
    *   Hỗ trợ kiến trúc API cho Payment Hub và Financial Hub.
*   **Không phụ trách (Out-of-scope):** Không viết component giao diện web, không chạy chiến dịch paid marketing.
*   **Điểm bàn giao & Phối hợp:** Bàn giao tiêu chuẩn tracking và API cho FE dev; phối hợp cùng Data Analyst (Hải Huỳnh) đối soát số liệu báo cáo tuần/tháng.

---

### 4. Duy Trần (Senior Back-end Developer)
*   **Vị trí bàn:** Bàn 01
*   **Dự án sở hữu:** RAG Knowledge Base, Vé Số, BMC Campaign
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Lập trình backend và API cho Vé Số và các chiến dịch BMC (Ví Trả Sau, Vay Nhanh).
    *   Xây dựng pipeline đồng bộ dữ liệu từ MoSpark sang hệ thống RAG Knowledge Base phục vụ tìm kiếm thông minh.
    *   Backend API cho các microsite vệ tinh.
*   **Không phụ trách (Out-of-scope):** Không quản lý hạ tầng máy chủ gốc (DevOps Lộc đảm nhiệm), không soạn thảo nội dung tri thức.
*   **Điểm bàn giao & Phối hợp:** Nhận nội dung chuẩn từ Hoan/Hiến để nạp vào RAG; bàn giao API cho Front-end tích hợp.

---

### 5. Lộc Lê (DevOps Lead)
*   **Vị trí bàn:** Bàn 01
*   **Dự án sở hữu:** Hạ tầng, Hiệu năng Website & Phân quyền
*   **Phạm vi đảm nhiệm (In-scope):**
    *   DevOps Lead: Chịu trách nhiệm toàn diện về hạ tầng máy chủ, độ sẵn sàng hệ thống (System Availability), tốc độ tải trang và hiệu năng website (Core Web Vitals).
    *   Quản trị hệ thống xác thực MoSpark Auth, phân quyền truy cập CMS (RBAC) và giám sát an toàn thông tin.
    *   Xử lý các sự cố kỹ thuật, rủi ro an ninh mạng, lỗi sập hệ thống hoặc nghẽn mạng trên môi trường Production/Staging; quản lý pipeline CI/CD và quy trình phát hành hạ tầng.
*   **Không phụ trách (Out-of-scope):** Không trực tiếp viết giao diện hay lập trình tính năng nghiệp vụ của từng Hub cụ thể.
*   **Điểm bàn giao & Phối hợp:** Thiết lập môi trường Staging/Production cho toàn bộ đội ngũ lập trình; hỗ trợ mở quyền truy cập an toàn cho PM và các BU; thẩm định hiệu năng và hạ tầng trước khi Go-Live.

---

### 6. Hùng Nguyễn (Front-End Team Lead)
*   **Vị trí bàn:** Bàn 01
*   **Dự án sở hữu:** Cinema Hub, MoBase Design System, BMC Campaign
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Trưởng nhóm Front-end; trực tiếp làm Key Owner toàn diện Cinema Hub (lịch chiếu, phim rạp, minigame tương tác).
    *   Triển khai kỹ thuật Front-end cho các chiến dịch BMC lớn trên website.
    *   Quản trị và phát triển thư viện MoBase Design System, bảo đảm tính nhất quán giao diện toàn web.
*   **Không phụ trách (Out-of-scope):** Không viết code backend API, không đàm phán hợp đồng thương mại với các cụm rạp đối tác.
*   **Điểm bàn giao & Phối hợp:** 
    *   Tiếp nhận luồng sản phẩm trực tiếp từ Hiến (khi không qua Product Design) hoặc bản thiết kế UI/UX từ Tữ.
    *   Chịu trách nhiệm hoàn thiện giao diện và tính năng trên môi trường Staging.
    *   Phối hợp cùng Hoan hoàn thiện đầy đủ Meta Data, bộ từ khóa SEO và Long Content chuẩn E-E-A-T trước khi phát hành lên Production.
    *   Bàn giao sản phẩm hoàn thiện cho Hiến ký duyệt Product Sign-off để chính thức Go-Live.

---

### 7. Nhật Bùi (Senior Front-end Developer)
*   **Vị trí bàn:** Bàn 01
*   **Dự án sở hữu:** Financial Hub & Utility Tools
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Key Owner Financial Hub toàn diện từ giao diện tới chức năng tương tác.
    *   Lập trình các công cụ tiện ích tài chính (Interactive Calculators: tính thuế TNCN, thuế hộ kinh doanh, lãi vay, tra cứu tỷ giá ngoại tệ, chứng chỉ quỹ).
    *   Tối ưu hóa Puck Editor phục vụ biên tập giao diện linh hoạt.
*   **Không phụ trách (Out-of-scope):** Không tự ý thay đổi công thức thuế hoặc lãi suất khi chưa có xác nhận từ BU Tài chính / Pháp chế.
*   **Điểm bàn giao & Phối hợp:** 
    *   Tiếp nhận luồng sản phẩm trực tiếp từ Hiến (khi không qua Product Design) hoặc BU Tài chính.
    *   Chịu trách nhiệm hoàn thiện giao diện tính toán và logic công cụ trên môi trường Staging.
    *   Phối hợp cùng Hoan bổ sung đầy đủ Meta Data, bộ từ khóa SEO và Long Content chuẩn E-E-A-T.
    *   Bàn giao sản phẩm hoàn thiện cho Hiến ký duyệt Product Sign-off để chính thức Go-Live lên Production.

---

### 8. Thuận Võ (Senior Front-end Developer)
*   **Vị trí bàn:** Bàn 01
*   **Dự án sở hữu:** Vehicle Hub, New User Quiz/Game, Tracking Umami
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Key Owner Vehicle Hub toàn diện: Tra cứu phạt nguội 0-CAPTCHA, định giá xe, danh bạ gara ô tô, tính chi phí xe, giá xăng dầu.
    *   Lập trình các mini tool, quiz trắc nghiệm tương tác cho New User nhằm tăng thời gian lưu trang.
    *   Triển khai và theo dõi sự kiện đo lường Umami trên toàn bộ các công cụ và tiện ích web.
    *   Hỗ trợ MoSpark Multimodal Studio (ComfyUI backend).
*   **Không phụ trách (Out-of-scope):** Không quản trị dữ liệu lớn BigQuery (Hiếu đảm nhiệm), không tự ý xuất bản sản phẩm nếu thiếu bài viết chuyên sâu bổ trợ.
*   **Điểm bàn giao & Phối hợp:** 
    *   Tiếp nhận luồng sản phẩm trực tiếp từ Hiến (khi không qua Product Design); không cần điều hướng qua Backend Lead hoặc Backend khi công cụ chạy thuần Front-end/Puck.
    *   Chịu trách nhiệm hoàn thiện công cụ tiện ích xe trên môi trường Staging.
    *   Phối hợp cùng Hoan chuẩn hóa đầy đủ Meta Data, bộ từ khóa SEO và Long Content chuẩn E-E-A-T.
    *   Bàn giao sản phẩm hoàn thiện cho Hiến ký duyệt Product Sign-off để chính thức Go-Live lên Production.

---

### 9. Trọng Trần (Senior Front-end Developer)
*   **Vị trí bàn:** Bàn 01
*   **Dự án sở hữu:** GenAI Content Workflow, PLG Dashboard & Công Cụ Nội Bộ
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Key Owner phụ trách hệ thống và công cụ vận hành nội bộ (Internal Tooling & Workflow Engine).
    *   Quản lý và lập trình GenAI Content Pipeline workflow (Text/Logic Nodes) trên MoSpark.
    *   Xây dựng Dashboard Điều Độ PLG: Quản trị vòng đời bài viết, SLA sản xuất và FSM Engine.
    *   Bóc tách cấu trúc dữ liệu cho Chatbot Knowledge Base.
*   **Không phụ trách (Out-of-scope):** Không trực tiếp sáng tạo nội dung chữ (Content Writing); không xây dựng trang đích công khai phục vụ Google Search.
*   **Điểm bàn giao & Phối hợp:** 
    *   Tiếp nhận luồng bài toán trực tiếp từ Hiến (khi không qua Product Design).
    *   Phối hợp cùng Hoan chuẩn hóa prompt và skill tự động hóa.
    *   Kiểm thử chức năng và bàn giao cho Hiến ký duyệt Product Sign-off để phát hành Go-Live vận hành nội bộ.
    *   **Ngoại lệ Go-Live:** Vì là sản phẩm công cụ nội bộ (không phục vụ người dùng tìm kiếm trên Google), sản phẩm của Trọng được miễn trừ yêu cầu Meta Data, SEO Keywords và Long Content từ Hoan.

---

### 10. Hoan Trần (Senior Product Marketing)
*   **Vị trí bàn:** Bàn 02 (Ngồi cạnh Hiến)
*   **Dự án sở hữu:** Content Strategy, SEO Content & Gamification
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Hoạch định Chiến lược Nội dung (Content Strategy) cho toàn bộ các Hub trên Web.
    *   Trực tiếp cung cấp Long Content chuẩn E-E-A-T, nghiên cứu bộ từ khóa SEO (SEO Keywords) và xây dựng cấu trúc Meta Data (Title, Meta Description, Schema) cho toàn bộ sản phẩm công khai chuẩn bị Go-Live (Vehicle Hub của Thuận, Cinema Hub của Hùng, Financial Hub của Nhật).
    *   Chuẩn hóa Context, Prompt và Skill phục vụ sản xuất bài viết qua GenAI Pipeline.
    *   Phối hợp cùng Trọng và ban biên tập vận hành nhịp độ sản xuất bài viết.
    *   Đề xuất kịch bản Gamification và Minigame tương tác (Cinema, New User).
*   **Không phụ trách (Out-of-scope):** Không can thiệp code kỹ thuật hệ thống, không tự ý thay đổi cấu trúc URL hoặc Canonical.
*   **Điểm bàn giao & Phối hợp:** Bàn giao dàn ý, Long Content, Meta Data và bộ từ khóa cho Key Owner (Thuận, Hùng, Nhật) tích hợp vào trang Staging; phối hợp Hiến kiểm duyệt nội dung trước khi ký duyệt Go-Live; phối hợp Hùng/Thuận lên kịch bản minigame.

---

### 11. Tữ (Senior Product Designer · Nhân sự sắp gia nhập)
*   **Vị trí bàn:** Bàn 02 (Đối diện Hoan)
*   **Dự án sở hữu:** UI/UX Web Design & MoBase Design System
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Thiết kế giao diện người dùng (UI) và trải nghiệm người dùng (UX) cho toàn bộ các trang trên `momo.vn`.
    *   Hiện thực hóa tư duy có hệ thống (System Thinking) và quy chuẩn Design-to-Code.
    *   Mở rộng bộ thư viện Design Tokens, icons, typography và component cho MoBase.
*   **Không phụ trách (Out-of-scope):** Không viết code backend API, không quản lý hạ tầng deployment.
*   **Điểm bàn giao & Phối hợp:** Nhận bài toán định hướng từ Hiến; bàn giao Figma UI/UX sạch và token thiết kế cho Hùng (Front-end Lead) và các kỹ sư Front-end.

---

### 12. Hiến Hồ (Web Product Lead · Điều phối trung tâm)
*   **Vị trí bàn:** Bàn 02
*   **Dự án sở hữu:** Danh mục Sản phẩm Web momo.vn & MoSpark
*   **Phạm vi đảm nhiệm (In-scope):**
    *   Chịu trách nhiệm tăng trưởng Pageviews (PV) và lưu lượng tự nhiên toàn trang thông qua việc khởi xướng, điều phối và thúc đẩy các dự án chiến lược (Strategic Projects: Cinema Hub, Vehicle Hub, Financial Hub, MoSpark CMS, RAG Knowledge Base, Interactive Calculators).
    *   Bảo đảm hiệu suất sản phẩm (Product Performance) và quản trị toàn diện danh mục Product Line trên Web: Giám sát vòng đời, thời gian tương tác (Engagement Time), tốc độ tải trang và tỷ lệ chuyển đổi Web-to-App (W2A).
    *   Định hướng chiến lược Product-Led Growth (PLG), quy hoạch danh mục sản phẩm và các Hub chiến lược.
    *   Thiết lập chuẩn mực Technical SEO/GEO, Entity Schema, Semantic Topic Clusters và hóa giải Zero-Click Search.
    *   Tư vấn giải pháp và làm việc với các BU / Cell Team đưa sản phẩm lên Web.
    *   Đóng vai trò Gatekeeper duy nhất: Ký duyệt xuất bản cuối cùng (Product Sign-off) về trải nghiệm người dùng, tính chính xác công cụ, luồng tracking OneLink/Umami và tiêu chuẩn SEO trước khi chuyển từ Staging lên Production (Go-Live).
*   **Không phụ trách (Out-of-scope):** Không trực tiếp viết mã nguồn chi tiết cho từng task (SE Team tự chủ thực thi); không làm thay việc của Cell Team.
*   **Điểm bàn giao & Phối hợp:** Giao Product Brief trực tiếp cho các Key Owner (Thuận, Hùng, Nhật, Trọng) hoặc SE Team (Bảo, Hùng, Hiếu) và Marketing (Hoan); kiểm duyệt và phê duyệt Go-Live; báo cáo trực tiếp với Ban Điều hành.

---

## 3. NGUYÊN TẮC PHỐI HỢP & CHUYỂN GIAO (OPERATING PRINCIPLES)

1.  **Một đầu việc - Một PIC duy nhất:** Mỗi task chỉ có một người chịu trách nhiệm chính (Accountable/Owner). Các thành viên khác tham gia với vai trò Hỗ trợ kỹ thuật hoặc Phối hợp (Consulted/Informed).
2.  **Trục Điều Phối (Bàn 02) ➔ Trục Sản Xuất (Bàn 01):** 
    *   Hiến & Hoan định hình bài toán sản phẩm và nội dung tại Bàn 02.
    *   Bảo điều phối năng lực kỹ thuật và giải pháp kiến trúc cùng Hoài Anh.
    *   Các kỹ sư tại Bàn 01 tập trung sản xuất, kiểm thử và bàn giao theo đúng tiêu chuẩn.
3.  **Quy chuẩn nghiệm thu (3 Quality Gates bắt buộc):**
    *   *Gate 1 (Kỹ thuật & Hiệu năng):* Lộc / Hùng / Hoài Anh duyệt code và Core Web Vitals.
    *   *Gate 2 (Tracking & Dữ liệu):* Hiếu / Thuận kiểm tra OneLink và sự kiện Umami.
    *   *Gate 3 (Nội dung & Sản phẩm):* Hoan hoàn thiện Long Content/SEO; Hiến ký duyệt Product Sign-off trước khi chuyển từ Staging lên Production.
4.  **Luồng Sản Phẩm Trực Tiếp (Direct Routing · Tuyến Bỏ Qua Product Design):**
    *   Đối với các luồng sản phẩm, tính năng hoặc công cụ tiện ích triển khai trực tiếp mà không thông qua Product Design (do Tữ sắp gia nhập hoặc các tính năng kế thừa Design System / Component có sẵn):
    *   Yêu cầu sản phẩm từ Hiến sẽ đi thẳng trực tiếp đến các Key Owner chính của dự án:
        *   **Thuận Võ**: Key Owner Vehicle Hub & Mini Tools / Quiz (công cụ định giá xe, tra cứu phạt nguội, chi phí xe, giá xăng dầu...).
        *   **Hùng Nguyễn**: Key Owner Cinema Hub & BMC Front-end (lịch chiếu phim, mua vé, minigame tương tác...).
        *   **Nhật Bùi**: Key Owner Financial Hub & Utility Tools (các bảng tính tài chính interactive calculators: thuế TNCN, lãi vay, tra cứu tỷ giá...).
        *   **Trọng Trần**: Key Owner GenAI Content Workflow, PLG Dashboard & Công Cụ Vận Hành Nội Bộ (MoSpark nodes, Chatbot KB parser...).
    *   Key Owner chịu trách nhiệm chính về toàn bộ giao diện, logic tính toán và triển khai kỹ thuật trên môi trường Staging.
5.  **Điều Kiện Tiên Quyết Để Go-Live Đầy Đủ Lên Production (Production Go-Live Gatekeeper Requirements):**
    *   Một sản phẩm/tính năng hoàn thiện trên Staging chỉ được phép chuyển trạng thái và chính thức phát hành lên môi trường Production (Go-Live đầy đủ) khi thỏa mãn trọn vẹn 4 điều kiện tiên quyết:
        1.  **Meta Data chuẩn mực**: Đầy đủ Title chuẩn Search Intent, Meta Description súc tích, Canonical URL, OpenGraph và Schema JSON-LD.
        2.  **Bộ từ khóa SEO (SEO Keywords)**: Xác định rõ ràng từ khóa chính, từ khóa phụ và bao phủ Search Intent.
        3.  **Long Content chuẩn E-E-A-T từ Hoan**: Bắt buộc có khối nội dung chuyên sâu từ chuyên gia/biên tập viên bao bọc xung quanh công cụ để giải thích phương pháp tính, hướng dẫn sử dụng và phân tích tình huống, triệt tiêu nguy cơ bị Google đánh giá là Thin Content hoặc Zero-Click.
        4.  **Ký duyệt Product Sign-off từ Hiến (Web Product Lead)**: Kiểm duyệt toàn diện về chất lượng trải nghiệm (UX), độ chính xác của logic/công thức, luồng chuyển đổi Web-to-App (OneLink) và tiêu chuẩn kỹ thuật trước khi chính thức mở truy cập cho người dùng.
    *   **Ngoại lệ duy nhất (Exemption Rule · Trọng Trần):**
        *   Trừ Trọng Trần, toàn bộ sản phẩm của 3 Key Owner trên (Thuận, Hùng, Nhật) bắt buộc phải đáp ứng đủ 4 điều kiện trên.
        *   Các sản phẩm do Trọng phụ trách là hệ thống/công cụ vận hành nội bộ (Internal Tooling & Workflow Engine: GenAI Pipeline, MoSpark CMS Dashboard, Chatbot KB Parser), không phải là trang đích công khai phục vụ Google Search.
        *   Do đó, sản phẩm của Trọng **được miễn trừ yêu cầu Meta Data, SEO Keywords và Long Content từ Hoan**. Trọng chỉ cần hoàn thành kiểm thử tính năng và nhận Product Sign-off kỹ thuật từ Hiến để chính thức Go-Live vận hành nội bộ.
