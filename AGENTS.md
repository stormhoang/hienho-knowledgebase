# AGENTS.MD - WORKSPACE INSTRUCTIONS & RULES

## 🎯 CHẾ ĐỘ VẬN HÀNH: PROBLEM → OPTIMAL ANSWER (KHÔNG PHẢI AGENT TỰ ĐỘNG)

- **Không tự ý triển khai, không chạy tác vụ dài hơi khi chưa được yêu cầu.** Đây không phải chế độ autonomous agent.
- **🔒 PHẠM VI GIT & PHÂN ĐỊNH REPOSITORY (STRICT SINGLE-REPO BOUNDARY SSOT):**
  - Mọi thao tác git (`git status`, `git add`, `git commit`, `git push`, `git diff`, v.v.) khi người dùng gõ "push" hoặc các lệnh git thông thường **CHỈ ĐƯỢC PHÉP thực hiện duy nhất trong repository hiện tại (`Hienho_MoMo-Base`)**.
  - Tuyệt đối KHÔNG tự ý quét, đọc, commit hoặc push sang repository khác (như `Web-Idea/react-web-momo` hay bất kỳ repo nào khác ngoài workspace).
  - **Cơ chế mở quyền truy cập (Intent-Gated Access):** Chỉ khi người dùng **đề cập rõ ràng tên "Hub", "Hubs" hoặc "React"** trong câu lệnh thì mới được phép sang bên đó đọc dữ liệu hoặc làm việc. Mọi trường hợp khác: Không đọc, không chạm, không push.
- **Khi người dùng đặt vấn đề:** Trả lời trực tiếp, sắc sảo, đúng trọng tâm - là câu trả lời tối ưu nhất dựa trên toàn bộ knowledge base, không cần người dùng phải hỏi đi hỏi lại.
- **Quy trình trả lời một vấn đề (Lazy & Intent-Based Routing):**
  1. **Định tuyến nhanh (Fast Routing):** Phân loại ý định theo bảng Fast Routing Index bên dưới. Tuyệt đối KHÔNG tự ý đọc các file lớn (`MEETING_RECAPS.md`, `hienho_master_doc.md`, `WEB_PERFORMANCE_TRACKING_MASTER.md`) cho các câu hỏi kỹ thuật, code review, trao đổi logic hoặc tra cứu thông thường. Cần mảng nào chỉ đọc đúng 1 file SSOT của mảng đó.
  2. **Phân tích với Chain of Thought:** reasoning trước, kết luận sau. Chỉ ra lỗi logic, điểm mâu thuẫn, giả định chưa validate nếu phát hiện.
  3. **Gắn vào business metric (khi phù hợp):** New User / MAU / Traffic / Revenue và framework hiện có (JTBD, 4 Zones, PLG, Web-to-App).
  4. **Đề xuất tối ưu kèm Action Items cụ thể**, có ưu tiên rõ ràng.
- **🌟 NGUYÊN TẮC TƯ DUY & PHẢN HỒI TOÀN DIỆN (UNIVERSAL EXECUTIVE & STORYTELLING SSOT - BẮT BUỘC TRONG MỌI TRƯỜNG HỢP):**
  Áp dụng xuyên suốt cho **MỌI câu trả lời, thảo luận thông thường, soạn thảo document/PRD, phân tích kỹ thuật/sản phẩm, review hội thoại hay đồng bộ dữ liệu (sync)**, không chỉ giới hạn trong việc làm report:
  - **Tư duy No Naked Facts / Numbers:** Tuyệt đối không quăng thông tin/số liệu thô, bảng tĩnh hay mô tả rời rạc không lời bình. Mọi dữ kiện phải có điểm quy chiếu (Target, Benchmark, Baseline, hoặc kỳ trước), bóc tách nguyên nhân gốc rễ và gắn vào tác động thực chất (Kinh doanh, Kỹ thuật, Trải nghiệm).
  - **Format tư duy 3 tầng bắt buộc (What? ➔ So What? ➔ Now What?):**
    1. **Action Title (Tiêu đề hành động / Kết luận trực diện):** 1 câu kết luận gồm [Chủ đề/Chỉ số chính] + [Hiện trạng/Xu hướng] + [Bản chất/Nguyên nhân cốt lõi].
    2. **What (Hiện tượng, Bằng chứng & Dữ kiện sạch):** Bằng chứng thực tế, số liệu sạch kèm điểm so sánh (Target, Baseline, %A/B, MoM); nêu rõ nguồn và bối cảnh.
    3. **So What (Phân tích thực chất, Tác động & Rủi ro):** Tác động đến bài toán lớn (New User, MAU, Traffic, CVR, Doanh thu, Kiến trúc); chỉ ra điểm nghẽn, rủi ro đánh đổi và Lowlights khách quan (tuyệt đối không nói chung chung hay tô hồng).
    4. **Now What (Hành động, Giải pháp & Quyết định):** Việc cần làm ngay, phương án giải quyết cụ thể, hoặc đề xuất cần phê duyệt/thống nhất (kèm deadline, owner và hệ quả nếu trễ).
  - **Quy chuẩn Tag [D], [R], [F] (CHỈ DÙNG KHI LÀM BÁO CÁO - STRICT REPORT ONLY):** Các tag định vị nội dung `[D]` (thảo luận/quyết định), `[R]` (kết quả/báo cáo số), `[F]` (tham khảo) **CHỈ ĐƯỢC DÙNG KHI LÀM BÁO CÁO** (Weekly/Monthly Report, slide báo cáo ban lãnh đạo). Tuyệt đối **KHÔNG** tự ý gắn các tag `[D]`, `[R]`, `[F]` vào câu trả lời thông thường, tài liệu kỹ thuật, PRD, tài liệu kiến trúc hay các đoạn văn trao đổi/thảo luận.
  - **🚫 CẤM DÙNG EN DASH & EM DASH (STRICT NO EN DASH / NO EM DASH):** Tuyệt đối KHÔNG sử dụng ký tự En Dash (`–`, U+2013) hoặc Em Dash (`—`, U+2014) trong bất kỳ câu trả lời, tài liệu hay phân tích nào. Chỉ dùng dấu gạch ngang bàn phím chuẩn Hyphen (`-`, U+002D) cho khoảng số (ví dụ: `80-90%`, `5-10 ngày`), hoặc dùng dấu hai chấm `:`, dấu ngoặc đơn `(...)`, hoặc tách câu trực tiếp.
  - **🚫 CẤM GẮN NHÃN PRIORITY (STRICT NO P0, P1, P2, P3):** Tuyệt đối KHÔNG gắn nhãn, phân loại mức độ ưu tiên hay tạo cột dạng `P0`, `P1`, `P2`, `P3` (hoặc Priority 0/1/2/3) cho các task, hành động, giải pháp hay kế hoạch trong bất kỳ câu trả lời, tài liệu, bảng biểu hay báo cáo nào. Trình bày các đầu việc một cách tự nhiên theo thứ tự triển khai logic, nhóm chuyên môn hoặc danh sách gạch đầu dòng thuần túy.
  - **🛡️ BỘ LỌC TỪ NGỮ CHUẨN MỰC & KHỬ TỪ AI (STRICT VOCABULARY GUARD - BẮT BUỘC TRÊN TOÀN BỘ FILE MỚI & CẬP NHẬT):**
    Khi soạn thảo file mới hoặc cập nhật bất kỳ tài liệu nào (BRD, PRD, Architecture, Strategy, Report, Markdown), AI Agent **BẮT BUỘC tuân thủ SSOT từ điển [`03_SKILLS/momo-reporting-glossary.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-glossary.md)**. Từ điển này quy định 2 tầng chuẩn hóa:
    1. **Tầng Dùng Chung (Cho 100% tài liệu):** Khử sạch văn mẫu AI, từ ngữ bạo lực/quân sự, chợ búa hoặc dịch thô:
       - *Bạo lực / Thâu tóm:* `thâu tóm` (thay bằng `bao phủ` / `thu hút lưu lượng`), `đánh/tấn công bất đối xứng` (thay bằng `tiếp cận khác biệt`).
       - *Chợ búa / Bẫy người dùng:* `mồi câu / phễu mồi câu` (thay bằng `tiện ích thu hút` / `Engagement Hooks`), `hứng trọn` (thay bằng `đón nhận trọn vẹn` / `hấp thu`), `mù internet` (thay bằng `mất kết nối mạng`), `shock bill` (thay bằng `phát sinh cước ngoài ý muốn`).
       - *Cơ khí / Dịch thô:* `phân hệ` (thay bằng `module` / `hub`), `phân rã / bảng phân rã` (thay bằng `cơ cấu` / `phân bổ` / `bóc tách chi tiết`), `phân khối phụ trách` (thay bằng `khối phụ trách`), `triệt tiêu ma sát / không ma sát` (thay bằng `giảm rào cản thao tác`), `hào nước dữ liệu` (thay bằng `lợi thế phòng thủ dữ liệu`), `đơn thuốc hành động` (thay bằng `kế hoạch xử lý`), `nỗi đau` (thay bằng `rào cản thao tác / điểm nghẽn`), `chi tiêu trả thù` (thay bằng `chi tiêu bù đắp quá độ`), `tạ thế` (thay bằng `kết thúc sớm`), `phát hành tính năng/trang/tool` (phát hành là từ của ngành in ấn/xuất bản/tài chính, trong Product thay bằng `ra mắt` / `chính thức Go-live` / `triển khai lên Production` / `xuất bản` đối với nội dung, bài viết, báo cáo / `đưa vào hoạt động`).
       - *Thổi phồng / Cổ kính:* `đỉnh cao` (thay bằng `hiệu suất cao nhất`), `đạt đỉnh` (thay bằng `chạm mốc kỷ lục`), `chủ trì` (thay bằng `điều phối` / `lead`), `dự phóng` (thay bằng `dự báo` / `ước tính`), `trạm tải app` (thay bằng `Trang Tải Ứng Dụng`), `vùng trũng` (thay bằng `lưu lượng còn thấp`), `mục tiêu tối thượng` (thay bằng `mục tiêu cốt lõi`).
       - *Khẩu ngữ / Cá nhân:* `bấm nút` (thay bằng `nhấp vào nút` / `kích hoạt`), `bữa tối gia đình test` (thay bằng `tiêu chuẩn trải nghiệm đột phá`), `văn hiến sign-off` (thay bằng `Web Platform phê duyệt`).
    2. **Tầng C-Suite / Executive Reporting (Dành riêng cho Báo cáo Ban Giám Đốc - anh Tường, anh Công):** Giữ nguyên các thuật ngữ kỹ thuật chuyên ngành chuẩn mực (`Pentest`, `môi trường Staging`, `Production`, `BFF`, `API`, `OneLink`, `Schema`...), tuyệt đối không gượng ép dịch thô làm méo mó bản chất hệ thống. Chỉ chuẩn hóa cách diễn đạt: tránh nói tắt cộc lốc như `On Prod` (thay bằng `Triển khai lên Production` / `Chính thức Go-live` / `Chính thức vận hành`); thuật ngữ chuyên ngành viết tắt có chú giải ngữ cảnh kinh doanh ở lần đầu xuất hiện.
    Tất cả các commit và stage git đều được tự động bảo vệ qua script kiểm duyệt `./.venv/bin/python scripts/guard_vocabulary.py --staged`.
- **Chỉ build/render file (HTML, script, PRD, report) khi người dùng yêu cầu rõ** - hoặc khi câu trả lời "tối ưu nhất" bắt buộc cần artifact để chứng minh, và phải nêu lý do.
- Khi thấy phương án người dùng chọn có rủi ro hoặc có phương án tốt hơn đáng kể: nêu thẳng, không xuôi theo.

### 🗺️ BẢNG ĐỊNH TUYẾN NHANH (FAST ROUTING INDEX SSOT)

| Nghiệp vụ / Chủ đề người dùng hỏi | File SSOT đích duy nhất (Target File) | Hành vi nạp file (Loading Policy) |
| :--- | :--- | :--- |
| **Tổng quan Codebase, Cách thức hoạt động, Onboarding** | [`CODEBASE_MANIFEST.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/CODEBASE_MANIFEST.md) | **Bắt buộc quét file này** khi tìm hiểu cách hoạt động tổng thể của repo. |
| **Hỏi nhanh, Kỹ thuật, Code, Review, Debug** | File code hoặc file văn bản liên quan trực tiếp | **Zero context file load**. Trả lời ngay, không đọc file bối cảnh. |
| **Tracking Umami, Event Name, Schema Params** | [`04_MOSPARK_PLATFORM/umami_utility_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/umami_utility_tracking.md) | Chỉ đọc file này khi hỏi về tracking/sự kiện. |
| **Tra cứu Keyword Inventory Use Case** | [`05_HUBS/inventory/<hub-name>/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/inventory/) | Chỉ đọc đúng file CSV của Hub tương ứng. |
| **Chẩn đoán hiệu suất, Root Cause, Tại sao tăng/giảm** | [`scripts/diagnose_performance.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/diagnose_performance.py) | Chạy `./.venv/bin/python scripts/diagnose_performance.py`. |
| **Cảnh báo Dị biệt, Anomaly Detection, Đứt gãy W2A** | [`scripts/detect_anomalies.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/detect_anomalies.py) | Chạy `./.venv/bin/python scripts/detect_anomalies.py`. |
| **Xếp hạng Ưu tiên RICE, Sáng kiến Tăng trưởng** | [`scripts/prioritize_initiatives.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/prioritize_initiatives.py) | Chạy `./.venv/bin/python scripts/prioritize_initiatives.py`. |
| **Thống kê A/B Test, P-Value, Cỡ mẫu MDE** | [`scripts/lib/ab_test_evaluator.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/lib/ab_test_evaluator.py) | Chạy `./.venv/bin/python scripts/lib/ab_test_evaluator.py`. |
| **Hiệu suất 7 ngày SERP, Biến động Tăng/Giảm, Đồng bộ /report** | [`scripts/sync_7d_performance_report.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_7d_performance_report.py) | Chạy `./.venv/bin/python scripts/sync_7d_performance_report.py`. |
| **Sổ cái Quyết định, Đối soát Closed-Loop** | [`scripts/track_decisions.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/track_decisions.py) | Chạy `./.venv/bin/python scripts/track_decisions.py`. |
| **Truy vấn Dữ liệu Đa chiều, Quick Wins, W2A, SQL** | [`scripts/query_analytics.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/query_analytics.py) | Chạy `./.venv/bin/python scripts/query_analytics.py`. |
| **Mô phỏng Kịch bản What-If, Cắt giảm Ads, CTR Lift** | [`scripts/lib/scenario_simulator.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/lib/scenario_simulator.py) | Chạy `./.venv/bin/python scripts/lib/scenario_simulator.py`. |
| **Dự báo Mùa vụ, Ngoại suy Đa kịch bản** | [`scripts/lib/forecast_engine.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/lib/forecast_engine.py) | Chạy `./.venv/bin/python scripts/lib/forecast_engine.py`. |
| **Paid Ads, Kênh Media, UTM Campaigns** | [`07_REPORTS/data/analytics/paid_ads_performance.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/analytics/paid_ads_performance.json) | Đọc file JSON SSOT hoặc chạy `./.venv/bin/python scripts/sync_paid_ads.py`. |
| **Lịch mùa vụ, Phân tích Google Trends** | [`07_REPORTS/data/theme_seasonality.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/theme_seasonality.json) | Đọc file JSON đã xuất bản hoặc chạy script cron. |
| **Báo cáo Tuần/Tháng, Hiệu suất MTD, Target** | [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md) | Chỉ đọc khi người dùng yêu cầu làm báo cáo/phân tích số liệu. |
| **Tiêu chuẩn Báo cáo Tháng (Executive 6 Streams SSOT)** | [`.agents/skills/web-platform-reporting/SKILL.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/.agents/skills/web-platform-reporting/SKILL.md) | Đọc khi soạn thảo, review hoặc đồng bộ báo cáo tháng cấp Ban Giám Đốc. |
| **Quy chuẩn trình bày báo cáo, slide, agenda, tag R/D/F** | [`03_SKILLS/momo-reporting-guidelines.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-guidelines.md) | Đọc bắt buộc trước khi dựng hoặc review bất kỳ báo cáo/slide nào. Hiệu lực cao hơn mọi quy chuẩn nội bộ. |
| **Glossary Báo cáo, Chuẩn hóa Thuật ngữ, Tránh viết tùm lum** | [`03_SKILLS/momo-reporting-glossary.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-glossary.md) | Tra cứu từ điển thuật ngữ, chỉ số, cấm kỵ và quy chuẩn hành văn báo cáo. |
| **Strict Vocabulary Guard, Linter Kiểm tra BRD/PRD/Report** | [`scripts/guard_vocabulary.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/guard_vocabulary.py) | Chạy `./.venv/bin/python scripts/guard_vocabulary.py --changed` hoặc `--staged`. |
| **Tra cứu Báo cáo Lịch sử (T1 -> T10, Hubs)** | [`07_REPORTS/docs/INDEX.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/INDEX.md) | Đọc index để mở đúng file báo cáo tháng hoặc chuyên đề cần tìm. |
| **Chỉ đạo Lãnh đạo, Quyết định chiến lược** | [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md) | Chỉ đọc section gần nhất khi lập kế hoạch chiến lược mới. |
| **Cinema Hub Roadmap, BU Movies Collab, Minigames** | [`scripts/sync_cinema_roadmap_sheet.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_cinema_roadmap_sheet.py) | Chạy `./.venv/bin/python scripts/sync_cinema_roadmap_sheet.py`. SSOT Sheet ID: `1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg`. |
| **Pipeline Tác vụ Agent, Giao việc Hiến sang Hub /agent** | [`scripts/sync_agent_tasks.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_agent_tasks.py) | Chạy `./.venv/bin/python scripts/sync_agent_tasks.py`. |
| **Kiến trúc Codebase, Phụ thuộc Module/Hàm, Luồng Call Flow, Tác động thay đổi** | [`graphify-out/graph.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/graphify-out/graph.json) | **Tự động kích hoạt Graphify**: Tự chạy `graphify explain / path / query` thay vì đọc file thô hoặc grep mù. |
| **Quy chuẩn viết, Văn phong, Format** | Trực tiếp trong `AGENTS.md` | Có sẵn trong bộ nhớ hệ thống, không đọc thêm file. |

---

## 🧠 MANDATORY CONTEXT MEMORY: ALWAYS READ MEETING RECAPS & PERFORMANCE SSOT

- **Memory Source Files:** 
  1. [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md)
  2. [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md)
- **Python Runtime & Environment SSOT Rule:** Toàn bộ pipeline và script Python trong repo (`scripts/*.py`) được quản lý tập trung qua môi trường ảo [`./.venv`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/.venv) (Python 3.12) và định nghĩa SSOT tại [`scripts/requirements.txt`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/requirements.txt). Khi AI Agent hoặc hệ thống chạy bất kỳ script Python nào, **BẮT BUỘC gọi trực tiếp `./.venv/bin/python <script_path>`** (ví dụ: `./.venv/bin/python scripts/sync_tracking_report.py`). Tuyệt đối không dùng lệnh `python3` trần để tránh việc macOS tự động fallback về Python 3.9 hệ thống gây thiếu thư viện (`underthesea`, `pytrends`).
- **Automated Tracking Report Trigger Rule:** Khi người dùng yêu cầu *"đọc tracking report mới nhất"* (hoặc bất kỳ câu lệnh tương tự về việc cập nhật/lấy số tracking), AI Agent **BẮT BUỘC tự động chạy script `./.venv/bin/python scripts/sync_tracking_report.py`** để:
  1. Quét tự động file `*Web Performance Tracking*.xlsx` mới nhất trong thư mục `/Users/hienhv/Downloads/`.
  2. Trích xuất chính xác số ngày lũy kế MTD (MTD Days), lưu bản ghi sạch vào SSOT [web_performance_tracking.xlsx](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/web_performance_tracking.xlsx) và tạo JSON snapshot.
  3. Đồng bộ báo cáo master và trình bày kết quả ngay lập tức theo phong cách Product Lead / Tech Lead.
- **Automated Hybrid Report Sync & Cross-Reconciliation Rule (Tự Động Đối Soát & Hợp Nhất 2 Nguồn):** Khi người dùng yêu cầu *"sync report"*, *"đồng bộ report"*, *"sync và đối chiếu report"*, AI Agent **BẮT BUỘC gọi ngay `./.venv/bin/python scripts/sync_hybrid_report.py`**. Script tự động:
  1. Quét file Excel BigQuery mới nhất và truy vấn GA4 Data API song song.
  2. Tự động đối chiếu chéo (Cross-Reconcile): Xác nhận độ khớp số cùng kỳ (100% Match) và tính toán phần bù tăng trưởng ngày mới (+Net Add) nếu Excel có độ trễ ngày so với GA4 API.
  3. Tự động làm giàu (Enrichment): Gắn thêm W2A OneLink Clicks, URL Retention Matrix vào cơ cấu Hubs/Projects của Excel.
  4. Tự động đồng bộ hiệu suất biến động 7 ngày SERP (Gainers & Losers) vào `/report` và `/dashboard` qua `scripts/sync_7d_performance_report.py --no-push`.
  5. Cập nhật đồng bộ vào Hubs `/dashboard` ([`web-data.json`](file:///Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/web-data.json) & [`summary.json`](file:///Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/summary.json)), Excel SSOT, Markdown SSOT và đẩy lên GitHub `main` qua REST API trong 8-10 giây.
  6. Xuất bản bảng Báo cáo Đối Soát & Hợp Nhất hoàn chỉnh trong 1 lượt trả lời duy nhất.
- **Automated GA4 MTD Master Sync Rule (Trọn Gói 1 Lệnh - Fast Path):** Khi người dùng yêu cầu *"cập nhật số GA4"*, *"cập nhật GA4 MTD"*, *"lấy số GA4"*, AI Agent **BẮT BUỘC gọi ngay `./.venv/bin/python scripts/sync_ga4_master.py` (kèm `--mtd <ngày>` nếu có)**. Script chạy trọn gói trong 6-10 giây:
  1. Truy vấn trực tiếp GA4 Data API (Property 270743103) lấy số tổng thể, kênh Non-Paid vs. Paid, W2A OneLink clicks và bóc tách cơ cấu các Hub.
  2. Tự động tính toán Target Pacing, Forecast 31 ngày và tiến độ về đích.
  3. Tự động ghi đồng bộ vào: Snapshot JSON, Hubs `/dashboard` ([`web-data.json`](file:///Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/web-data.json) & [`summary.json`](file:///Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/dashboard/summary.json)), Excel SSOT và Markdown SSOT.
  4. Tự động đẩy lên Google Sheets Native SSOT qua Cloud Sheets API (Spreadsheet ID: `1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU`), đồng bộ tệp Excel dự phòng trên Google Drive Desktop.
  5. Tự động đồng bộ hiệu suất biến động 7 ngày SERP (Gainers & Losers, Clicks & Root Causes) vào Báo cáo Tuần (`/report`) và Dashboard (`/dashboard`) qua `scripts/sync_7d_performance_report.py --no-push`.
  6. Tự động đẩy toàn bộ thay đổi lên GitHub Hubs (`main`) qua REST API.
  7. Trả về bảng kết quả hoàn chỉnh ngay lập tức trong 1 lượt trả lời duy nhất, tuyệt đối không chạy phân mảnh hay hỏi đi hỏi lại từng bước.
- **Google Sheets Cloud-Native SSOT Rule (Spreadsheet ID `1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU`):** Mọi thao tác cập nhật/đồng bộ số liệu hiệu suất Web Platform lên Google Sheets **BẮT BUỘC** trỏ trực tiếp qua Google Sheets API vào Spreadsheet ID **`1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU`** (đường dẫn mở trên trình duyệt: [https://docs.google.com/spreadsheets/d/1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU/edit?gid=1273714888#gid=1273714888](https://docs.google.com/spreadsheets/d/1JaaYv2MnDy-dfBdC3P-GMB6SFgjez2VowdjX9PjmPYU/edit?gid=1273714888#gid=1273714888)). Ghi trực tiếp Cloud-to-Cloud đảm bảo:
  1. Tự động lưu 100% lịch sử sửa đổi trong **Google Sheets Version History** (Tệp ➔ Lịch sử phiên bản).
  2. Google Sheets tự động tính toán lại các công thức `SUM`, `INDEX MATCH`, `ARRAYFORMULA`.
  3. Hoạt động độc lập hoàn toàn, không phụ thuộc vào trạng thái ứng dụng `Google Drive for Desktop` trên máy Mac. Đồng thời vẫn duy trì bản sao Excel `.xlsx` offline tại thư mục `WEB GROWTH 2026/#4 - Tracking & Performance` (File ID `1H_1RNCA1NBdZ9vJH5VLSw7D9aaYhx3XI`).
- **Google Sheets Cinema Roadmap SSOT Rule (Spreadsheet ID `1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg`):** Mọi thao tác đồng bộ / tra cứu kế hoạch hợp tác Web Platform x BU Movies, Roadmap, Minigames và Content Plan của Cinema Hub **BẮT BUỘC** trỏ qua Google Sheets API vào Spreadsheet ID **`1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg`** (đường dẫn mở trên trình duyệt: [https://docs.google.com/spreadsheets/d/1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg/edit?gid=113654251#gid=113654251](https://docs.google.com/spreadsheets/d/1YT2sdU-O4smoy6TUKBic6PTFBxUXNUVkd_S-tmjiplg/edit?gid=113654251#gid=113654251)). Đồng bộ cục bộ và hai chiều qua script `./.venv/bin/python scripts/sync_cinema_roadmap_sheet.py`. Tệp liên kết Google Drive Desktop lưu tại: `/Users/hienhv/Library/CloudStorage/GoogleDrive-hien.ho@mservice.com.vn/My Drive/WEB GROWTH 2026/#1 - Use Case/[MDS] - Movies/[WP] Web Cinema | Roadmap.gsheet`. Bản sao Excel SSOT lưu tại: [`05_HUBS/cinema/cinema_hub_roadmap_drive_sync.xlsx`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/cinema/cinema_hub_roadmap_drive_sync.xlsx).
- **Automated Paid Ads & UTM Trigger Rule:** Khi người dùng yêu cầu *"kiểm tra ads"*, *"web đang chạy ads gì"*, *"kênh media nào đang chạy ads"*, *"hiệu suất paid ads/UTM"*, AI Agent **BẮT BUỘC tự động chạy script `./.venv/bin/python scripts/sync_paid_ads.py`** để:
  1. Truy vấn trực tiếp GA4 Data API (Property 270743103) cho chu kỳ MTD.
  2. Tự động bóc tách landing pages, kênh media (`sessionSourceMedium`), chiến dịch và chuyển đổi Web-to-App.
  3. Xuất dữ liệu sạch sang SSOT [`07_REPORTS/data/analytics/paid_ads_performance.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/analytics/paid_ads_performance.json), cập nhật báo cáo [`07_REPORTS/docs/PAID_ADS_TRACKING_LATEST.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/PAID_ADS_TRACKING_LATEST.md) và trình bày báo cáo trực diện.
- **Automated Performance Diagnostic & Root Cause Rule (RCA Trigger):** Khi người dùng yêu cầu *"chẩn đoán hiệu suất"*, *"tại sao traffic tụt"*, *"tìm nguyên nhân gốc rễ"*, *"phân tích gap/laggard"*, AI Agent **BẮT BUỘC tự động chạy script `./.venv/bin/python scripts/diagnose_performance.py`** để:
  1. Đo lường độ lệch tiến độ MTD thực tế so với mục tiêu và nhịp độ cần đạt.
  2. Phân rã đa chiều: Non-Paid vs Paid -> Cơ cấu Hubs -> Phễu Sessions vs W2A CVR.
  3. Phát hiện từ khóa Quick Wins (>50K impressions, CTR thấp) và đưa ra danh mục hành động cụ thể kèm ROI kỳ vọng (không gắn nhãn P0/P1/P2).
- **Automated Anomaly Detection Trigger Rule:** Khi người dùng yêu cầu *"quét dị biệt"*, *"kiểm tra bất thường"*, *"có trang nào rớt traffic không"*, *"hỏng tracking/OneLink"*, AI Agent **BẮT BUỘC gọi ngay `./.venv/bin/python scripts/detect_anomalies.py`** để phát hiện các URL bị đứt gãy W2A, rớt thứ hạng hoặc sụt giảm tương tác.
- **Automated Scenario Modeling Trigger Rule:** Khi người dùng yêu cầu *"mô phỏng kịch bản"*, *"nếu cắt giảm paid ads"*, *"tối ưu CTR được gì"*, *"nâng CVR W2A"*, AI Agent **BẮT BUỘC gọi ngay `./.venv/bin/python scripts/lib/scenario_simulator.py`** để định lượng tác động kinh doanh cụ thể.
- **Automated Strategy & What-If Simulation Trigger Rule:** Khi người dùng yêu cầu *"dự báo mùa vụ"*, *"mô phỏng dịch chuyển nguồn lực"*, *"kịch bản what-if"*, AI Agent **BẮT BUỘC gọi ngay `./.venv/bin/python scripts/lib/forecast_engine.py`** để định lượng tác động chuyển đổi ròng (Net W2A Lift) và 3 kịch bản kết tháng.
- **Automated Multi-Dimensional Analytics Query Rule:** Khi người dùng yêu cầu *"tra cứu từ khóa quick wins"*, *"xếp hạng W2A"*, *"phân tích ăn thịt từ khóa (cannibalization)"* hoặc chạy truy vấn SQL tùy ý trên Data Mart, AI Agent **BẮT BUỘC gọi ngay `./.venv/bin/python scripts/query_analytics.py`**.
- **Weekly Report Drive Folder Lifecycle & Color Rule (Quy Chuẩn Thư Mục & Màu Sắc Báo Cáo Tuần):**
  - Mọi thư mục báo cáo tuần trên Google Drive (`.../#6 - Report/Web Platform_Report (Markdown)/`) bắt buộc đặt tên chuẩn: `Tuần <XX> (dd.mm - dd.mm.yyyy)`.
  - **Quy tắc đổi màu thư mục (Visual Color Tagging):** Thư mục của **tuần hiện tại đang thu thập báo cáo (Active Week)** bắt buộc được đổi sang **Màu Đỏ (Red / Tomato)** (trên macOS Finder set `label index to 2` và trên Google Drive Web UI chọn màu Đỏ) để toàn bộ đội ngũ kỹ sư nhận diện tức thì, upload đúng thư mục. Khi tuần kết thúc, chuyển thư mục tuần đó về màu xám/mặc định (`label index to 0`) và kích hoạt màu Đỏ cho tuần mới kế tiếp.
- **Strategic Context Trigger Rule:** Khi người dùng yêu cầu **lập kế hoạch chiến lược cấp cao, viết PRD mới, chuẩn bị báo cáo tuần/tháng (WBR/MBR) hoặc phân tích số liệu hiệu suất Web Platform**, AI Agent mới chủ động tham chiếu số liệu thực tế từ file [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md) và mục recaps gần nhất từ [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md). Với các câu hỏi nghiệp vụ thông thường, hỏi kỹ thuật, tra cứu tiện ích hay review trao đổi, **TUYỆT ĐỐI KHÔNG tự ý đọc các file này** để tối ưu tốc độ phản hồi.
- **Automated Graphify Architecture & Navigation Rule (Tự Động Phán Đoán & Kích Hoạt Đồ Thị Kiến Trúc):** Khi người dùng đặt bất kỳ câu hỏi nào liên quan đến kiến trúc codebase, phụ thuộc giữa các module/hàm, đường dẫn luồng xử lý (call path/flow), kiểm tra tác động thay đổi (impact analysis), tìm kiếm cấu trúc code hoặc cách các file kết nối nhau:
  1. AI Agent **BẮT BUỘC tự động phán đoán và gọi Graphify ngầm** (`graphify explain "<concept>"`, `graphify path "<A>" "<B>"`, `graphify query "<câu hỏi>"`) dựa trên `graphify-out/graph.json` đã được dựng sẵn trong workspace tương ứng.
  2. **Tuyệt đối không yêu cầu người dùng phải gõ lệnh Graphify thủ công**, và không chạy `grep` phân mảnh hay đọc tuần tự nhiều file source khi chưa tra cứu qua đồ thị.
  3. Sau khi thực hiện chỉnh sửa hoặc tạo code mới trong session, Agent tự động chạy `graphify update .` ngầm để bảo đảm đồ thị luôn phản ánh mã nguồn thực tế.
- **Utility Tracking SSOT Rule:** Khi Kỹ sư (Dev) hoặc người dùng hỏi về: gắn tracking, đo lường công cụ, sự kiện Umami, Event Name cho tool/widget/calculator, schema tham số (`provider`, `amount`) hoặc cách track cho bất kỳ tiện ích nào, AI Agent **BẮT BUỘC chỉ định và trích xuất trực tiếp từ file SSOT [`04_MOSPARK_PLATFORM/umami_utility_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/umami_utility_tracking.md)**.
- **Use Case Keyword Inventory SSOT Rule:** Khi người dùng yêu cầu *"tra cứu Inventory của 1 use case"* (hoặc bất kỳ câu lệnh liên quan đến kiểm tra dataset từ khóa, keyword clusters, market volume thô của một ngành/use case), AI Agent **BẮT BUỘC chỉ định và đọc trực tiếp từ thư mục SSOT [`05_HUBS/inventory/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/inventory/)** (gồm các phân khối: `Financial/`, `vehicle-hub/`, `insurtech/`, `ota/`, `telco/`, `hospital/`, `Lottery/`, `trust/`, `cinema/`, `student/`, `Entertainment/`, `other/`). Tuyệt đối không tự suy diễn số liệu từ khóa khi chưa quét các file CSV tương ứng trong thư mục này.
- **Seasonality & Google Trends Intelligence SSOT Rule:** Khi người dùng hoặc hệ thống yêu cầu tính toán, cập nhật lịch mùa vụ (Seasonality), phân tích xu hướng thị trường hoặc chuẩn bị dữ liệu xuất sang Web Hubs (`react-web-momo`):
  1. AI Agent **BẮT BUỘC chỉ định và sử dụng script [`scripts/cron_theme_seasonality.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/cron_theme_seasonality.py)** (chạy bằng `./.venv/bin/python`) để xuất bản file dữ liệu SSOT [`07_REPORTS/data/theme_seasonality.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/theme_seasonality.json).
  2. **Quy tắc Khung thời gian (Timeframe):** Tuyệt đối **KHÔNG dùng dữ liệu 12 tháng** của `theme_trends` để tính mùa vụ (vì 12 tháng chỉ là 1 năm đơn lẻ, dễ bị nhiễu bởi các biến động ngẫu nhiên). BẮT BUỘC phải lấy dữ liệu 5 năm (`timeframe="today 5-y"`) và tính trung bình theo từng tháng dương lịch (T1..T12) qua 5 năm.
  3. **Quy tắc Bắt buộc của Contract (theo schema `lib/content-plan/seasonality.ts`):**
     - Mảng `monthly` gồm đúng 12 số nguyên, theo thứ tự từ T1 đến T12, đã chuẩn hóa sao cho tháng cao nhất bằng 100.
     - `theme_id` phải trùng khớp chính xác `id` trong file cluster (`data/seo-clusters/*/*.json`).
     - Mỗi payload truy vấn chỉ chứa **duy nhất 1 keyword (pillar)**; không gộp nhiều keyword để tránh bị chuẩn hóa chéo làm méo dạng mùa vụ của keyword yếu hơn.
     - Cơ chế vận hành: Tích hợp Resume cache (không crawl lại các theme đã hoàn tất) và Exponential Backoff tự động khi gặp mã lỗi HTTP 429.
- **Vietnamese NLP SSOT Rule:** Mọi tác vụ tách từ / word segmentation / trích xuất n-gram tiếng Việt trong pipeline **BẮT BUỘC gọi qua gateway [`scripts/lib/vi_nlp.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/lib/vi_nlp.py)** (`segment()`, `segment_text()`) - KHÔNG import trực tiếp `underthesea`/`pyvi` rải rác trong script khác. Backend: underthesea 9.5+ (đã tích hợp trong `./.venv`), tự fallback pyvi rồi naive split khi thiếu lib (không crash). Chuẩn hóa teencode / lỗi dấu dùng `TELEX_FIXES` + `normalize_text()` trong `scripts/lib/keyword_intelligence.py` - KHÔNG dùng `text_normalize()` của underthesea (yếu với teencode). Entity/brand dùng `ENTITY_LEXICON` + `flashtext` trong `scripts/lib/keyword_extractor.py` - KHÔNG dùng NER của underthesea cho keyword fragment. Khi đọc CSV inventory trực tiếp, LUÔN bóc artifact Excel `="..."` bằng `clean_val()` trước khi xử lý.
- **Traffic Source Classification SSOT Rule (Non-Paid vs. Paid Dichotomy):** Khi phân tích, đo lường hoặc trình bày bất kỳ báo cáo nào (Weekly, Monthly, Ad-hoc) về nguồn lưu lượng (Traffic Source / Channels) của Web Platform:
  1. **BẮT BUỘC phân chia thành 2 nhóm lớn rõ rệt:**
     - **Kênh Tự Nhiên (Non-Paid Traffic):** Là động cơ tăng trưởng tự nhiên bền vững, thể hiện chất lượng thực chất, giá trị SEO/GEO, sức mạnh thương hiệu và độ tin cậy của toàn Website. **BẮT BUỘC chỉ gồm đúng 4 kênh con chuẩn hóa (đồng bộ chuẩn Monthly Report):**
       - **Organic:** Lưu lượng tìm kiếm tự nhiên qua công cụ tìm kiếm truyền thống.
       - **Direct:** Người dùng chủ động gõ URL hoặc truy cập trực tiếp momo.vn.
       - **AI Traffic (GEO):** Lưu lượng được trích dẫn và dẫn nguồn từ các công cụ AI (ChatGPT, Bing Copilot, Perplexity).
       - **Referral:** Toàn bộ lưu lượng giới thiệu từ đối tác rạp chiếu, liên kết ngân hàng và toàn bộ phần còn lại (tuyệt đối không tách thêm dòng "Others" rời rạc).
     - **Kênh Trả Phí (Paid Traffic / Paid Ads):** Bao gồm Paid Search, Google Ads, Campaign Ads...
  2. **Quy tắc hiển thị bảng biểu:** Phân cấp rõ 2 dòng tổng **KÊNH TỰ NHIÊN (NON-PAID)** vs. **KÊNH TRẢ PHÍ (PAID ADS)** (kèm tỷ trọng % tương ứng) và **TỔNG LƯỢNG TRUY CẬP (ACTUAL)**. Đúng 4 kênh con (`Organic`, `Direct`, `AI Traffic (GEO)`, `Referral`) phải được đặt thụt dòng bên dưới nhóm **Non-Paid**. Tuyệt đối không để Paid nằm xen kẽ ngang hàng giữa các kênh tự nhiên.
- **Mục đích:** Đảm bảo toàn bộ bối cảnh chiến lược của Ban Giám Đốc, định hướng của các Hubs và dữ liệu hiệu suất Single Source of Truth (SSOT) chuẩn xác luôn được đưa vào context xử lý tự động trước khi xuất bản bất kỳ báo cáo nào.

---

## ✍️ QUY TẮC VĂN PHONG VÀ VIẾT TÀI LIỆU (WRITING STYLE RULE)

- **Phong cách:** Thực tế, cô đọng, ngắn gọn, tự nhiên chuẩn Product Lead / Tech Lead. Đi thẳng vào bản chất vấn đề, số liệu và gạch đầu dòng.
- **TUYỆT ĐỐI KHÔNG:** 
  - **TUYỆT ĐỐI KHÔNG dùng các từ "sàn", "sàn Web", "toàn sàn":** Bắt buộc chỉ dùng **"toàn Website"**, **"nền tảng Web"**, **"Kênh Web"**, **"Web Platform"** hoặc **"Web"**.
  - **Không dùng bất kỳ Emoji / Icon nào** trong nội dung tiêu đề, bảng biểu và danh sách của bài báo cáo (Report).
  - **Không đề cập tên riêng của cá nhân / PIC** (như `[Hiến]`, `[Thuận]`, `[Trọng]`, `[Nhật]`, `Hiếu`...) trong bài báo cáo. Thay thế bằng tên đội ngũ chuyên môn (như `Web Dev`, `Backend Team`, `Content Team`, `SEO Vendor`...). **"Web Platform" là tên team (đội ngũ), không phải vị trí chức danh; luôn ghi đúng là "Web Platform" (không ghi "Web Platform Lead", không ghi "Web Growth Team").**
  - **Cấm dùng các từ ngữ hành chính, sáo rỗng hoặc dịch thô:** Tuyệt đối không dùng *"Chủ trì"* (thay bằng *Web Platform điều phối / phối hợp*), *"Dự phóng"* (thay bằng *Dự báo kết tháng (Forecast) / Ước tính theo nhịp chạy (Run-rate)*), *"Trạm tải app"* (thay bằng *Trang Tải Ứng Dụng /tai-app*), *"Đỉnh cao"*, *"Đạt đỉnh"*, *"Vùng trũng"*, *"Bấm nút"*.
  - Không viết dài dòng lê thê, không lặp lại ý.
- **Chuẩn hóa Thuật ngữ Kiến trúc Thông tin (Information Architecture Terminology):**
  - **Hub:** Bắt buộc dùng thay cho "Phân Khối Ngành", "Phân ngành", "Sector" (ví dụ: Cinema Hub, Financial Hub, Vehicle Hub, Insurtech Hub, OTA Hub, Lottery Hub...).
  - **Theme:** Bắt buộc dùng thay cho "Use Case", "Use case" (ví dụ: trong Financial Hub có các Themes: Tỷ giá, Giá vàng, Tiết kiệm ngân hàng, Vay tín chấp...).
  - Cấu trúc phân cấp 3 tầng chuẩn mực: **Hub ➔ Theme ➔ Cluster/Article**.
- **Cấu trúc viết:** Nhìn vào hiểu ngay ➔ Nêu rõ Context ➔ Action Items ➔ KPIs / Số liệu thực tế.

---

## 📐 QUY TẮC TRÌNH BÀY SƠ ĐỒ & CẤU TRÚC TÀI LIỆU (DOCUMENTATION & DIAGRAM FORMATTING)

- **Biểu diễn Luồng Người dùng (User Flow / Onboarding / Conversion Flow):**
  - **BẮT BUỘC** sử dụng **Sơ đồ Trực quan Mermaid (`mermaid`)** dạng `graph TD` hoặc `graph LR` cho toàn bộ các luồng User Flow trong BRD/PRD.
  - **TUYỆT ĐỐI KHÔNG** dùng sơ đồ mã ASCII thô (văn bản vẽ tay dạng `[1] ──► [2]`).
  - Bổ sung ngay bên dưới sơ đồ Mermaid một **Bảng Phân Tích Chi Tiết Các Bước (Step Breakdown Table)** gồm các cột: `Bước`, `Tên Giai Đoạn`, `Trải Nghiệm Người Dùng (UX)`, `Hạ Tầng / Cơ Chế Kỹ Thuật`, `Nền Tảng`.
- **Biểu diễn Lộ trình & Cột mốc (Roadmap & Milestones):**
  - **BẮT BUỘC** trình bày dưới dạng **Bảng Markdown (`Table`)** (gồm: `Giai đoạn`, `Thời gian`, `Tên Giai Đoạn`, `Chi Tiết Triển Khai & Mục Tiêu`).
- **Metadata & Chuẩn hóa Tài liệu:**
  - **Bỏ thuộc tính `Platform:`** trong blockquote Metadata ở đầu tất cả các file BRD.
  - **Không dùng Emoji / Icon** trong tất cả các bài báo cáo (Report) và tiêu đề / bảng biểu.

---

## 🚫 QUY TẮC HẠN CHẾ VẼ ẢNH & SƠ ĐỒ (MINIMAL VISUALS RULE)

- **TUYỆT ĐỐI KHÔNG tự ý sinh/vẽ ảnh:** Không dùng công cụ sinh ảnh, không tạo hình ảnh minh họa trừ khi có yêu cầu rõ ràng từ người dùng.
- **Hạn chế tối đa sơ đồ (Diagrams) trong câu trả lời thông thường:** Không chèn sơ đồ luồng/quy trình rườm rà vào các câu trả lời phân tích trao đổi hàng ngày. Ưu tiên **Bảng biểu Markdown (Tables)** và **Gạch đầu dòng phân tích trực diện, sắc sảo**.
- **Phạm vi duy nhất cho phép dùng Mermaid:** Chỉ sử dụng Mermaid `graph TD` / `graph LR` khi viết tài liệu đặc tả luồng người dùng (User Flow) trong các file BRD/PRD chính thức.

---

## 📊 QUY CHUẨN AGENDA BÁO CÁO THÁNG WEB PLATFORM (MONTHLY BUSINESS REVIEW STANDARD)

Khi người dùng yêu cầu viết **Monthly Report cho Web Platform**, AI Agent **BẮT BUỘC** đọc trước [`03_SKILLS/momo-reporting-guidelines.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-guidelines.md) (quy chuẩn cấp công ty, hiệu lực cao hơn mục này) rồi áp dụng agenda sau:

1. **Nguyên tắc vận hành:** *Report để cung cấp thông tin, Meeting để thảo luận và ra quyết định.* Phục vụ CEO và BOM nhận diện nhanh rủi ro trọng yếu và ra quyết định điều hành.
2. **Dòng Mục đích:** Mỗi slide/mục mở đầu bằng một dòng `Mục đích:` nêu slide này giúp ai hiểu điều gì hoặc quyết định điều gì. Không viết được thành một câu thì gộp hoặc bỏ slide.
3. **Action title:** Tiêu đề nêu kết luận kèm chỉ số và lý do, không ghi tên chủ đề. Viết sentence case. Đọc lần lượt các tiêu đề phải nắm được toàn bộ câu chuyện báo cáo.
4. **Tối đa 3 ý chính dưới mỗi tiêu đề:** Tốt nhất 1-2 ý. Nhiều hơn 3 thì tách slide. Phần còn lại là bằng chứng.
5. **Mỗi số liệu có so sánh và việc tiếp theo:** Con số luôn kèm mốc so sánh (Target, kỳ trước) và hành động cần làm. Số đứng trần là lỗi.
6. **Gắn nhãn phân loại:** 
   - `[R] - Reporting`: Cung cấp thông tin & kết quả hoạt động; dùng cho pre-read, không trình bày lại trong cuộc họp.
   - `[D] - Discussion`: Nội dung có vấn đề cần thảo luận, xin ý kiến alignment, cần hỗ trợ hoặc ra quyết định (trọng tâm cuộc họp).
   - `[F] - FYI`: Thông tin tham khảo, không thảo luận.
7. **Thứ tự deck chuẩn (Discussion Topics đứng ĐẦU, không phải cuối):**
   ```
   Bìa -> Agenda -> [D] Discussion Topics -> [D] Deep-dive từng chủ đề -> [R] Follow-up
    -> [R] Executive Summary -> [R] Product & Business Performance -> [R] Key Projects -> [R] New User
   ```
8. **Phần Follow-up `[R]` là bắt buộc:** Bảng theo dõi action từ meeting minutes kỳ trước (`Action` | `Owner` | `Hạn` | `Trạng thái` | `Cập nhật mới nhất`). Action còn mở mà cần quyết định thì đưa lên Discussion Topics.
9. **Nội dung các phần `[R]` của Web Platform:**
   - **Executive Summary `[R]`:** Hai khối `Điểm nổi bật` và `Vấn đề cần cải thiện`. Khối thứ hai là bắt buộc; deck chỉ có tin tốt là lỗi về độ tin cậy.
   - **Product & Business Performance `[R]`:** 
     - Bảng theo dõi mục tiêu và thực tế (Target vs. Actual) chuẩn 6 dòng chỉ số: `Total page views (target)`, `% Growth Rate (target)`, `Total page views (Actual)`, `Net add`, `% Growth Rate`, `% Target Rate`.
     - **Nguyên tắc "So What?" (Không đọc lại số liệu):** Tuyệt đối không diễn giải lại các con số người đọc đã nhìn thấy trong bảng. Phần phân tích bắt buộc tập trung vào kết quả thực chất: bản chất sự dịch chuyển lưu lượng, nguyên nhân cốt lõi đằng sau sự tăng/giảm, rủi ro đánh đổi và hành động điều chỉnh chiến lược.
   - **Key Projects `[R]`:** 
     - Chi tiết hiệu suất của 2 dự án trọng điểm lớn nhất (Cinema Hub và Financial Hub).
     - Với từng dự án: Chi tiết số liệu hiệu suất, điểm nổi bật đạt được trong tháng, việc trọng tâm tháng tới, và việc cần hỗ trợ.
     - `Financial Hub` ở đây là một hub sản phẩm (tỷ giá, giá vàng, CIC, Ví Trả Sau), không phải slide `Financial` theo nghĩa kết quả tài chính do Finance cung cấp.
   - **New User `[R]`:** 
     - Mô tả luồng Ads (Paid Search, Ads Campaigns) và phễu Web-to-App.
     - Số lượng Installs, New Registered Users (New Reg), Mapbank, MAU bóc tách theo từng chiến dịch (dữ liệu AppsFlyer GPD).
10. **Discussion Topics `[D]`:** 
    - Slide tổng: bảng một dòng mỗi chủ đề, 8 cột `#` | `Chủ đề` | `Loại` (Discuss/Approve) | `Cần CEO/BOM quyết định hoặc hỗ trợ gì` | `Tác động` (lượng hóa) | `Hạn` | `Ưu tiên` | `Chi tiết`. Tối đa 3-5 chủ đề.
    - Slide deep-dive cho từng chủ đề: `Problem Statement` -> `Bối cảnh` -> `Tác động` (lượng hóa) -> bảng `Phương án` tối thiểu 2 lựa chọn -> `Đề nghị với CEO/BOM` -> `Khuyến nghị của BU` -> `Nếu không quyết định` (hệ quả lượng hóa kèm mốc ngày).
11. **Quy định trình bày:**
   - Tuyệt đối không dùng Emoji/Icon; không dùng tên riêng cá nhân/PIC (thay bằng tên đội ngũ chuyên môn).
   - Không đưa phần CX, không đưa chỉ số kỹ thuật sâu (CWV, P90, 4xx/5xx), không đưa Ticket tồn đọng.
   - **Định vị kênh cốt lõi:** **Organic là kênh chủ lực và mang lại giá trị thực chất nhất của Web Platform**. Tuyệt đối **không tô điểm cho Paid**, không xem việc đốt tiền Paid là thành tích tăng trưởng. Paid tăng mà Organic giảm là tín hiệu cảnh báo rủi ro về độ lành mạnh của nền tảng Web.
   - **Thống nhất ngôn ngữ:** Toàn bộ báo cáo dùng một ngôn ngữ. Tiêu đề khối, nhãn cột và tiêu đề gạch đầu dòng viết tiếng Việt ngắn gọn (`Vượt target:`, `Lưu lượng trực tiếp & sức mạnh thương hiệu:`, `Chuyển dịch SEO sang GEO:`, `Điểm nổi bật:`, `Việc tiếp theo:`). Chỉ giữ nguyên thuật ngữ chỉ số đã quen thuộc: Target, Budget, Actual, MAU, MEU, CVR, EBITDA, Map Bank, OneLink, Installs, New Reg.
   - **Màu số liệu:** Tô màu cột mức đạt so với Target hoặc Budget: xanh khi từ 100% trở lên, cam khi 90-99%, đỏ khi dưới 90%. Quy tắc này áp dụng cho mức đạt Target, không áp dụng cho biến động MoM. Chỉ số giảm MoM nhưng vẫn đạt Target thì không tô đỏ.
   - **Đồng bộ cỡ chữ:** Mọi tiêu đề cùng một cỡ, mọi nội dung chính cùng một cỡ, mọi chú thích cùng một cỡ, xuyên suốt tất cả slide.
   - **Chân slide:** Mỗi slide ghi `Nguồn | Owner | Chốt số liệu (dd/mm/yyyy)`.
   - **Tháng báo cáo:** Xác định theo kỳ dữ liệu được báo cáo, không phải thời điểm gửi hay tháng diễn ra cuộc họp.
   - Không lặp lại số liệu thô; tập trung diễn giải ý nghĩa kinh doanh, bài học và quyết định vận hành.
   - Đảm bảo quyền truy cập cho Ban Giám Đốc và các đầu mối tổng hợp (`tuong.nguyen`, `tram.phan1`, `nga.nguyen1`).



---

## 📑 QUY CHUẨN TỔNG HỢP BÁO CÁO TUẦN WEB PLATFORM (WEEKLY REPORT RULES)

Khi người dùng ra lệnh tổng hợp Báo cáo Tuần (Weekly Report) từ thư mục thành viên trên Google Drive:

1. **Quy trình vận hành:**
   - Đọc toàn bộ các file báo cáo cá nhân của member trong thư mục tuần tương ứng (tại `/Users/hienhv/Library/CloudStorage/GoogleDrive-hien.ho@mservice.com.vn/My Drive/WEB GROWTH 2026/#6 - Report/Web Platform_Report (Markdown)/<tuần>/`).
   - Đối chiếu và tổng hợp đầy đủ các hạng mục vào file báo cáo tổng hợp tuần của Web Platform (đồng bộ cả local repo và Google Drive Desktop).

2. **Quy tắc Biên tập & Tinh chỉnh (Editing & Fine-tuning Rules):**
   - **Không AI Slop:** Câu từ tự nhiên, gãy gọn, chuẩn văn phong Product/Tech thực chiến. Tuyệt đối không dùng từ sáo rỗng, hoa mỹ, văn mẫu AI (như *bứt phá ngoạn mục*, *bệ phóng*, *khẳng định vị thế*, *hành trình chuyển đổi*...).
   - **Không ghi đội ngũ phụ trách:** Tuyệt đối không liệt kê cột hay thông tin đội ngũ phụ trách (không ghi Web Dev, Backend Team, Content Team, SEO Vendor, BU...).
   - **Thuần text, không dùng Table hay Chart (trừ Report Số):** Ngoại trừ bảng số liệu hiệu suất đo lường (Report Số), toàn bộ các phần tóm tắt tổng quan, phối hợp liên phòng ban và kế hoạch hành động tiếp theo **bắt buộc trình bày dạng gạch đầu dòng (bullet points) thuần text**, không vẽ bảng (`Table`) hay biểu đồ.
   - **Không đề xuất Priority:** Tuyệt đối không gắn nhãn độ ưu tiên dạng `[P0]`, `[P1]`, `[P2]`. Trình bày các đầu việc kế hoạch tuần tới tự nhiên dưới dạng danh sách gạch đầu dòng.
   - **Loại bỏ các từ ngữ khó hiểu / cản trở người đọc:** Tuyệt đối không dùng các từ như "Phân hệ", "Động cơ", "Phân khối ngành", "Ươm tạo", "Vùng hiệu suất"... Thay bằng từ ngữ trực diện, dễ hiểu như "Mảng", "Nhóm tính năng", "Hệ thống", "Dịch vụ" hoặc gọi thẳng tên dự án/Hub.
   - **Phân tách rõ ràng 2 Loại Dự Án:**
     - **Nhóm Dự Án Dịch Vụ (Use Case / Hubs):** Cinema Hub, Financial Hub, Vehicle Hub, Insurtech Hub, New User & Web-to-App, Lottery Hub, Dịch Vụ Mới & Nạp Game.
     - **Nhóm Dự Án Nền Tảng (Platform Enablers):** Hệ thống AI & MoSpark Core, Hệ thống Giao diện MoBase, CMS & Trình Soạn Thảo, Tìm Kiếm Website, Dữ Liệu Đo Lường & Tự Động Hóa Vận Hành.
   - **Cấu trúc 3 thành tố trong từng dự án:**
     - `Kết quả nổi bật`
     - `Phối hợp`
     - `Kế hoạch tuần tới`
