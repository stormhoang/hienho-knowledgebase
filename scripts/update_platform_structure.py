import os

path = '07_REPORTS/docs/weekly-report-2026-10-26-11-01.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Find Section III
s3_marker = '## III. TIẾN ĐỘ THỰC TẾ CÁC DỰ ÁN NỀN TẢNG (PLATFORM PROJECTS)'
p_s3 = text.find(s3_marker)
assert p_s3 != -1, 'Section III not found'

s3_new_content = """## III. TIẾN ĐỘ THỰC TẾ CÁC DỰ ÁN NỀN TẢNG (PLATFORM PROJECTS)

### 1. Chatbot AI & Hệ Thống Cơ Sở Tri Thức (Knowledge Base)
- **Key Owner:** duy.tran2
- **Objectives:** Tự động hóa quét và nạp dữ liệu tri thức toàn website đạt độ bao phủ >95%; thẩm định và chặn 100% bài viết thiếu nội dung hoặc bài rác để Chatbot không bị ảo giác (hallucination) hay trả lời sai lệch thông tin sản phẩm MoMo.
- **Business Context:** Trước đây tài liệu tri thức quản lý phân tán theo từng màn hình riêng lẻ, người quản trị không nắm được tổng thể dự án nào thiếu/đủ tài liệu khiến AI trả lời thiếu chính xác; việc kiểm tra bài viết mới từ sitemap bằng tay rất tốn công; nếu nạp cả bài nháp hoặc trang toàn ảnh quảng cáo sẽ gây hiện tượng "ảo giác" (hallucination) cho Chatbot.
- **Discuss & Tasks:**
  - **Project Center:** Bảng điều khiển trung tâm theo dõi số lượng tài liệu đã đồng bộ, số cụm chủ đề, trạng thái đồng bộ và thời gian cập nhật gần nhất cho từng dự án Chatbot.
  - **Sitemap & Link Scanner:** Tự động đọc `sitemap.xml`, so khớp với kho tài liệu tri thức, phân loại tài liệu thiếu (*Missing*) vs đã đồng bộ (*Synced*), tính tỷ lệ bao phủ tri thức (% Coverage).
  - **Eligibility Validation:** Tự động kiểm tra chất lượng bài viết trước khi nạp vào AI (chỉ nhận bài blog đã xuất bản chính thức; trang web phải có ít nhất 1 khối văn bản dài hoặc khối FAQ thực tế; gắn nhãn cảnh báo lý do không đủ điều kiện).
  - **Web Pages Tree:** Đồng bộ tri thức trực tiếp từ cây danh mục trang web (1-chạm hoặc theo link tùy chọn).
  - **Chuẩn hóa trích xuất:** Lọc bỏ banner, nút bấm trang trí; chỉ lấy phần chữ giàu tri thức (tiêu đề, tóm tắt, từ khóa, H2, nội dung chi tiết, FAQ) cho LLM.
- **Next Action:** Thử nghiệm độ chính xác của câu trả lời Chatbot trên Staging với tập dữ liệu tri thức mới; bổ sung bộ lọc và phân loại tài liệu tri thức theo chuyên đề.
- **Colab:** Phối hợp **Đội ngũ Quản trị Nội dung (Content Team)** bổ sung khối FAQ hoặc bài viết nội dung dài cho các trang web chưa đạt chuẩn để tăng độ bao phủ tri thức của AI.
---

### 2. Admin Panel: All-in-One Editor, Khối Nội Dung In-App & Quản Trị Menu (Build Prod Phase 2)
- **Key Owner:** hieu.nguyen8, duy.tran2
- **Objectives:** Nghiệm thu và phát hành Phase 2 lên Production đúng hạn (02/11/2026); rút ngắn 50% thời gian biên tập cho khối BMC nhờ hợp nhất màn hình soạn thảo; loại bỏ triệt để lỗi mất nút mở app do quên gắn mã `featureCode` / deeplink.
- **Business Context:** Biên tập viên gặp khó khăn khi phải chuyển qua lại giữa nhiều màn hình soạn thảo, danh sách bài và xem trước; các nút mở app thường xuyên bị lỗi mất điều hướng do quên nhập mã tính năng (`featureCode`); hệ thống chuẩn bị nghiệm thu Phase 2 để bàn giao cho khối BMC quản trị nội dung in-app toàn diện.
- **Discuss & Tasks:**
  - **All-in-One Editor:** Hợp nhất công cụ soạn thảo cho các trang chuyên biệt, gom chỉnh sửa nội dung, danh sách bài, banner và xem trước lên cùng 1 màn hình.
  - **Phân quyền tài khoản:** Tách bạch rõ quyền giữa người tạo bài viết và người duyệt bài; bổ sung nút chuyển nhanh sang danh sách bài chờ duyệt.
  - **Đóng gói khối nội dung In-App nâng cao:**
    - *Khối Voucher:* Nhập tiêu đề, quyền lợi, mã voucher, hạn dùng; tự sinh thẻ ưu đãi chuẩn MoMo kèm nút sao chép mã.
    - *Khối Hướng dẫn từng bước (Step-by-step Guide):* Hộp thoại soạn thảo 2 cột (Zero-Scroll Split-View); tự động co giãn hiển thị theo số bước (1 ảnh giữa, 2 ảnh đối xứng, từ 3 ảnh xếp lớp); bắt buộc ảnh tải từ CDN MoMo để bảo mật.
    - *Live Mobile Preview:* Khung xem trước trực tiếp ngay trong màn hình chỉnh sửa in-app.
  - **Chuẩn hóa Deeplink tự động cho các nút CTA:** Tự động nhận diện và đồng bộ tham số mã tính năng (`featureCode` tương ứng `refId`) trên cả bài viết Website và bài viết In-App (Deeplink 1 & Deeplink 2), đảm bảo nút mở app luôn dẫn đúng màn hình đích, loại bỏ lỗi mất định hướng.
  - **Nâng cấp độ ổn định trình quản lý Menu Header & Footer:** Cho phép lưu mượt mà 100% các mục menu không bị chặn kiểm duyệt; tối ưu công cụ kéo thả (Drag & Drop) sắp xếp phân cấp các nhánh menu chính và menu con.
  - **Chuẩn bị hoàn tất nghiệm thu Phase 2:** Phía BMC đã hoàn tất kiểm thử và gửi email xác nhận đồng thuận (confirm) vào ngày 29/10; chốt ngày build production Phase 2 vào ngày **02/11/2026** cùng nhánh BMC.
- **Next Action:** Tiến hành build Production Phase 2 vào ngày 02/11/2026; theo dõi vận hành sau phát hành và giám sát độ ổn định của All-in-One Editor.
- **Colab:** Phối hợp **Khối BMC (Brand & Marketing Communications)** và các **Cell Team** nghiệm thu thực tế, hướng dẫn sử dụng các khối nội dung In-App mới và tiếp nhận phản hồi cải tiến.
---

### 3. User Engagement: Cổng Tìm Kiếm Website ([momo.vn/tim-kiem](https://www.momo.vn/tim-kiem))
- **Key Owner:** hieu.nguyen8
- **Objectives:** Chuyển đổi trang tìm kiếm từ trang hiển thị kết quả tĩnh thành cửa ngõ kích hoạt giao dịch P2P; thúc đẩy tỷ lệ mở app MoMo từ các truy vấn số điện thoại và tăng chuyển đổi kéo người dùng mới qua banner ưu đãi tân thủ.
- **Business Context:** Người dùng có thói quen gõ thẳng số điện thoại người nhận vào ô tìm kiếm trên website momo.vn, nhưng trước đây hệ thống chỉ trả về trang trắng không có kết quả, gây đứt gãy luồng chuyển tiền và lãng phí lượng truy cập tự nhiên.
- **Discuss & Tasks:**
  - **Thẻ chuyển tiền nhanh qua số điện thoại:** Nhập số điện thoại hợp lệ vào ô tìm kiếm thì web tự hiện thẻ chuyển tiền dẫn vào app MoMo (nhận diện số điện thoại hoàn toàn phía trình duyệt, không gửi lên server để bảo mật).
  - **Banner người dùng mới:** Gắn banner hướng dẫn nhận quà và tải app cho khách lần đầu vào trang tìm kiếm hoặc khi tìm kiếm không có kết quả phù hợp.
- **Next Action:** Theo dõi số liệu sử dụng thẻ chuyển tiền nhanh qua số điện thoại và tỷ lệ click banner người dùng mới trên [momo.vn/tim-kiem](https://www.momo.vn/tim-kiem) môi trường Production.
- **Colab:** Phối hợp **Data / Analytics Team** bóc tách tỷ lệ chuyển đổi từ ô tìm kiếm website dẫn vào app MoMo thực hiện giao dịch chuyển tiền.
---

### 4. Hồ Danh Mục URL Toàn Website (URL Catalog)
- **Key Owner:** hieu.nguyen8
- **Objectives:** Thiết lập kho dữ liệu chuẩn trung tâm (Single Source of Truth) quản trị tập trung 100% đường dẫn URL toàn website; tự động hóa việc xuất bản Dynamic Sitemap theo từng phân khối và cấp danh mục link sạch cho Cổng tìm kiếm lẫn Chatbot AI.
- **Business Context:** Dữ liệu đường dẫn URL của website đang phân tán ở nhiều nguồn, thiếu một kho dữ liệu trung tâm chuẩn (Single Source of Truth) để phục vụ đồng thời Cổng tìm kiếm, tạo sơ đồ website (Sitemap SEO) theo dự án và cung cấp danh mục URL sạch cho đội AI xây dựng Cơ sở tri thức.
- **Discuss & Tasks:**
  - **Thiết kế kiến trúc kho dữ liệu tập trung:** Rà soát tài liệu kiến trúc so với thực tế vận hành để quản lý toàn bộ đường dẫn website phục vụ đồng thời Tìm kiếm, Sitemap/SEO và Cơ sở tri thức AI.
  - **Chốt 4 quyết định thiết kế cốt lõi:**
    1. Vị trí lưu trữ theo chuẩn chung của hệ thống.
    2. Bổ sung định danh rút gọn theo từng dự án để sinh Sitemap riêng biệt.
    3. Bộ lọc theo dự án luôn bao gồm các dự án con.
    4. Đồng bộ tự động trước mắt áp dụng cho Bài viết, Blog và Trang dịch vụ.
  - **Lộ trình triển khai 4 giai đoạn:** (1) Tạo bảng nạp 51 trang tìm kiếm ưu tiên; (2) Lớp đọc dữ liệu dùng chung có cache; (3) Chuyển Tìm kiếm sang đọc từ Hồ danh mục có cơ chế dự phòng; (4) Đồng bộ tự động từ CMS/MoSpark và sinh Sitemap theo dự án.
- **Next Action:** Triển khai Giai đoạn 1 của Hồ danh mục URL: tạo bảng cơ sở dữ liệu trên môi trường dev và nạp danh mục 51 trang tìm kiếm ưu tiên để đối chiếu dữ liệu.
- **Colab:** Phối hợp **Đội ngũ AI / Chatbot** và **SEO Team** thống nhất cấu trúc metadata và taxonomy phân cấp dự án trước khi mở rộng ra toàn bộ URL website.
---

### 5. Security: Bảo Mật Dữ Liệu Web, BFF & Hạ Tầng MoMo API
- **Key Owner:** hieu.nguyen8, loc.le4, thuan.vo
- **Objectives:** Khắc phục triệt để lỗ hổng Pentest; đóng hoàn toàn cổng đọc trực tiếp từ trình duyệt (`anon read`); chuyển đổi toàn bộ 19 trang web sang gọi qua máy chủ trung gian (BFF) bảo mật nhiều lớp; tự động hóa 100% cảnh báo lỗi CronJob về Google Chat.
- **Business Context:** Lúc 15:11 ngày 27/10, ITC thông báo kết quả Pentest phát hiện role `anon` có thể đọc được 218.243 bản ghi đối tác qua mã nguồn công khai của website (tính năng tra cứu cửa hàng làm gấp cho chiến dịch Mega Hoàn tiền 50%); hệ thống cần lập tức khoanh vùng bảo mật, làm sạch dữ liệu nhạy cảm và chuyển đổi toàn diện sang kiến trúc máy chủ trung gian (BFF) để đóng cổng truy cập công khai.
- **Discuss & Tasks:**
  - **Ứng phó sự cố Pentest & Khoanh vùng bảo mật Merchant (hieu.nguyen8, loc.le4):**
    - *Khoanh vùng cấp tốc trong 1 giờ:* Nhận cảnh báo Pentest lúc 15:11 ngày 27/10 (lỗ hổng role `anon` đọc được 218.243 bản ghi đối tác qua mã nguồn công khai), hoàn tất đóng toàn bộ API public Merchant và tạm ẩn tính năng tra cứu cửa hàng lúc 16:00 cùng ngày; không có rủi ro can thiệp hay sửa đổi dữ liệu.
    - *Làm sạch dữ liệu nhạy cảm trong cơ sở dữ liệu:* Xóa triệt để các cột dữ liệu nhạy cảm của chủ hộ kinh doanh (`merchant_codes`, `official_account_id`, `official_account_rating`, `merchant_name`, `merchant_info`) khỏi 5 bảng dữ liệu (`merchants`, `merchants_feed`, `merchants_oa`, `merchants_store`, `merchants_update`), ngăn chặn nguy cơ mạo danh lừa đảo.
    - *Hoàn thiện sơ đồ kiến trúc AS-IS / TO-BE & Incident Report:* Bóc tách 4 điểm rủi ro gốc và đề xuất giải pháp TO-BE; xây dựng bảng kế hoạch 48 đầu việc theo lộ trình P0 - P3; hoàn tất báo cáo sự cố trình ban quản lý kèm các đề xuất cải tiến quy trình phát hành (bắt buộc Security duyệt trước khi mở kết nối mới).
  - **Triển khai kiến trúc BFF (Backend for Frontend) & Kiểm soát truy cập (loc.le4, thuan.vo):**
    - *Kiểm thử 7 RPC public:* Xác nhận 7 hàm RPC hiện tại chỉ trả cột cố định, không bị embed sang bảng khác và không chọn thêm cột ngoài hàm.
    - *Kiến trúc BFF máy chủ riêng:* Chuyển luồng đọc dữ liệu từ trình duyệt sang gọi qua BFF với câu truy vấn cố định, kẹp giới hạn `limit/offset`, ẩn hoàn toàn lỗi hệ thống; BFF kết nối cơ sở dữ liệu qua role riêng an toàn `mini_web_server`.
    - *Đóng cổng dữ liệu công khai:* Đặt `PGRST_DB_MAX_ROWS=50` và chuẩn bị đóng hoàn toàn cổng truy cập công khai sau khi chuyển đổi xong 7 hàm RPC sang BFF.
    - *Khóa đọc trực tiếp (Anonymous read) trên 19 trang web:* Chuyển toàn bộ luồng dữ liệu quảng cáo, giá xăng và địa điểm sang gọi qua Server-side Proxy / Public RPC API của [momo.vn](https://www.momo.vn) *(thuan.vo)*.
  - **Hạ tầng Cron Job tự động & Vận hành API (loc.le4, hieu.nguyen8):**
    - *Hạ tầng tác vụ định kỳ (loc.le4):* Dựng xong Helm chart chạy tác vụ tự động bằng **Kubernetes CronJob** (cấu hình linh hoạt qua `values.yaml` không cần build lại code); tích hợp cơ chế tự thử lại 2 lần khi lỗi và **tự động gửi cảnh báo về Google Chat khi thất bại**.
    - *Vận hành MoMo API (hieu.nguyen8):* Mở cấu hình cho phép môi trường phát triển nội bộ gọi API kiểm thử và API chính; bổ sung cấu hình kết nối trung tâm dữ liệu ổn định; cập nhật thư viện dùng chung lên phiên bản mới nhất.
- **Next Action:** Trình duyệt giải pháp nâng cấp dữ liệu; triển khai Giai đoạn P1 (thu hồi quyền đọc public anon, dựng máy chủ BFF qua role mini_web_server, chuyển đổi 19 trang gọi qua BFF); đưa Cron Job lên môi trường dev nội bộ.
- **Colab:** Phối hợp **ITC Security Team** đặt lịch Pentest lại (Giai đoạn P3) và thẩm định các API public mới; phối hợp **DevOps Team** cấu hình cổng API, tường lửa và chuẩn bị đóng hoàn toàn cổng public Supabase.
---

### 6. MoBase Design System: Header Advance (Navigation 2 Tầng)
- **Key Owner:** hung.nguyen9
- **Objectives:** Nâng cấp thanh điều hướng trang chủ momo.vn lên chuẩn Navigation 2 tầng mới của MoBase Design System; cho phép cấu hình linh hoạt menu chính, menu phụ, icon dịch vụ và banner chiến dịch từ MoSpark CMS mà không cần can thiệp code.
- **Business Context:** Header hiện tại trên trang chủ momo.vn là phiên bản cũ, cấu trúc đơn tầng, thiếu tính linh hoạt khi cần hiển thị đồng thời nhiều dịch vụ, chương trình ưu đãi hoặc chiến dịch lớn; cần nâng cấp lên component Header Advance (Navigation 2 tầng) chuẩn MoBase Design System.
- **Discuss & Tasks:**
  - Đưa component **Header Advance (Navigation 2 tầng)** lên môi trường Staging trang chủ ([momo-stg.mservice.io](https://momo-stg.mservice.io/)), cho phép cấu hình linh hoạt menu chính, menu phụ, icon và nút CTA từ MoSpark CMS; kiểm tra responsive trên mobile, tablet và desktop.
- **Next Action:** Kiểm tra tính tương thích, responsive và hiệu năng trên môi trường Staging ([momo-stg.mservice.io](https://momo-stg.mservice.io/)); chuẩn bị kế hoạch phát hành lên trang chủ chính thức.
- **Colab:** Phối hợp **Web Platform Lead** và **Design System Team (MoBase)** review giao diện và trải nghiệm điều hướng trước khi On Production.

---

### 7. Web Performance GA4 & GSC (Admin MoSpark)
- **Key Owner:** thuan.vo
- **Objectives:** Đưa bảng số liệu truy cập GA4 và từ khóa Google Search Console vào thẳng MoSpark Admin để PM và các BU tự theo dõi hiệu suất dịch vụ của mình, vận hành trên máy chủ riêng cách ly an toàn dữ liệu nội bộ.
- **Business Context:** Đội ngũ sản phẩm (PM) và các BU cần chủ động theo dõi hiệu suất GA4 và Google Search Console trực tiếp trong MoSpark Admin để kịp thời điều chỉnh nội dung, nhưng cần đảm bảo phân quyền an toàn dữ liệu và kết nối máy chủ độc lập.
- **Discuss & Tasks:**
  - Chuyển kết nối Google Search Console và GA4 sang máy chủ riêng để mở rộng cho PM/BU xem số liệu an toàn trong MoSpark Admin (Analytics › Web Performance); hiện code xong, đang chờ DevOps dựng máy chủ riêng.
- **Next Action:** Kết nối bảng hiển thị số liệu GA4 & Google Search Console vào MoSpark Admin ngay khi máy chủ riêng sẵn sàng; kiểm thử phân quyền xem theo từng BU/PM.
- **Colab:** Phối hợp **DevOps Team** dựng máy chủ riêng, cấu hình mở quyền truy cập và gỡ bỏ các API key cũ để bảo đảm an toàn dữ liệu.
---

### 8. Utility Tool & Quiz: MoSpark Quiz
- **Key Owner:** thuan.vo
- **Objectives:** Nhúng công cụ trắc nghiệm tương tác vào thân bài viết blog để kéo dài thời gian lưu trang (Time on Page); tạo phễu chuyển đổi dẫn dắt người đọc bấm mở app đăng ký mở thẻ tín dụng hoặc kiểm tra điểm tín dụng CIC.
- **Business Context:** Các bài viết blog kiến thức tài chính thuần văn bản thường có tỷ lệ thoát trang cao, người đọc khó tự đánh giá nhu cầu cá nhân; cần công cụ trắc nghiệm (Interactive Quiz/Calculator) nhúng trực tiếp vào thân bài để tăng thời gian lưu trang và dẫn phễu mở thẻ/kiểm tra điểm tín dụng.
- **Discuss & Tasks:**
  - Đang làm thử nghiệm gắn quiz tương tác điểm tín dụng vào bài blog ([momo.vn/tai-chinh/blog/co-nen-mo-the-tin-dung-5138](https://www.momo.vn/tai-chinh/blog/co-nen-mo-the-tin-dung-5138)).
  - Chuẩn bị hạ tầng widget trắc nghiệm tương tác nhằm tăng thời gian lưu trang (Time on Page) và dẫn phễu mở thẻ tín dụng / tra cứu điểm tín dụng.
- **Next Action:** Chạy thử nghiệm widget Quiz trên bài blog thật; hoàn tất bộ kiểm thử 13 trường hợp (test cases) đa thiết bị trước khi phát hành chính thức.
- **Colab:** Phối hợp **Financial BU / Growth Team** đối soát tỷ lệ tương tác (Time on Page) và tỷ lệ nhấp vào CTA mở thẻ tín dụng / tra cứu điểm tín dụng sau khi hoàn thành quiz.
"""

clean_text = text[:p_s3] + s3_new_content
with open(path, 'w', encoding='utf-8') as f:
    f.write(clean_text)

print('Updated Section III successfully!')
