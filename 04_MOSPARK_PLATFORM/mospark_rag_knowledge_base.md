# MoSpark - RAG Knowledge Base Architecture
Hệ thống Quản trị Tri thức Tập trung & Truy xuất Cơ sở Dữ liệu MoMo

> - **Project:** MoSpark Web Platform
> - **Division:** GPD (Growth Product Division)
> - **Product:** Web Growth Platform
> - **Governance:** Văn Hiến (Web Product Lead)
> - **Version:** 1.0 · June 2026
> - **Status:** Proposal - Core Knowledge Engine

---

## 1. Executive Summary

### 1.1. Tầm nhìn & Mục tiêu (Vision & Objectives)
Để các bài viết và trang nội dung do GenAI hoặc biên tập viên tạo ra trên MoSpark luôn đạt độ chính xác tối đa, không bị ảo giác thông tin (Hallucination), và đồng nhất với các chính sách của MoMo, hệ thống cần một **Cơ sở Tri thức Tập trung (RAG Knowledge Base)**.

Thay vì quản lý ngữ cảnh phân mảnh ở từng dự án, RAG Knowledge Base hoạt động như một lớp hạ tầng độc lập. Nó lưu trữ toàn bộ dữ liệu sản phẩm, dịch vụ của MoMo, các quy chuẩn thương hiệu, và cả những nội dung lịch sử do GenAI tạo ra. Khi cần thiết, hệ thống sẽ sử dụng cơ chế **Truy xuất Thông tin tăng cường (Retrieval-Augmented Generation)** để cung cấp ngữ cảnh chuẩn xác nhất cho các tác vụ sinh nội dung hoặc giải đáp người dùng.

### 1.2. Mối quan hệ trong Hệ sinh thái MoSpark
RAG Knowledge Base đóng vai trò là "Kho tri thức gốc" (Source of Truth), liên kết trực tiếp với các cấu phần khác của MoSpark:
*   **GenAI Content Engine (Factory):** Truy xuất các quy chuẩn viết bài và thông tin sản phẩm để nhúng vào Prompt trước khi gọi LLM.
*   **Microsite / CMS Page Editor:** Đọc dữ liệu từ RAG để điền thông tin tự động (Auto-fill) hoặc gợi ý chèn liên kết chéo (Cross-linking).
*   **Chatbot & Assistant:** Sử dụng RAG để trả lời các câu hỏi thực tế của khách hàng về sản phẩm/dịch vụ trên các trang đối tác (Merchant) hoặc trang tiện ích.

---

## 2. Nguồn Dữ Liệu Nạp Vào (Knowledge Sources)

Hệ thống RAG được thiết kế để bao phủ toàn bộ tài sản dữ liệu tĩnh và động của MoMo, bao gồm 4 nhóm tài nguyên lớn:

```
+-------------------------------------------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">RAG KNOWLEDGE SOURCES</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
+-------------------------------------------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1. Quy chuẩn toàn cục (Global Standards):</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Brand Guideline (Tone of Voice, Xưng hô)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Design System (MoBase UI/UX Rules, Headings)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- SEO & Content Principles (E-E-A-T, YMYL)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2. Dữ liệu sản phẩm & dịch vụ (MoMo Product Catalogue):</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Tài chính (Vay Nhanh, Ví Trả Sau, CIC, Tiết Kiệm)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Tiện ích (Thanh toán hóa đơn, Vé xem phim, Mua sắm)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- API Docs & Vận hành từ các Cell Teams</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3. Dữ liệu đối tác (Merchant Project):</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Địa chỉ, Giờ mở cửa, Tiện ích, Quy định thanh toán</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4. Dữ liệu sinh ra bởi GenAI (Historical Outputs):</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">- Bài viết Blog, Landing Pages, FAQs đã được xuất bản</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
  </tbody>
</table>
+-------------------------------------------------------------------------+
```

---

## 3. Kiến Trúc Kỹ Thuật & Luồng Xử Lý (RAG Processing Pipeline)

Hệ thống RAG được triển khai dưới sự phụ trách của **Duy (Senior BE Developer)** với kiến trúc 4 bước tiêu chuẩn:

```
[Ingestion] (Markdown/PDF/APIs)
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
     v
[Chunking] (Semantic/Recursive, size: 512 tokens)
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
     v
[Embedding] (text-embedding-3-small)
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
     v
[Vector Database] (Supabase pgvector)
```

### 3.1. Phân mảnh Tài liệu (Semantic Chunking)
Hệ thống sử dụng giải thuật phân mảnh đệ quy (Recursive Character Text Splitter) kết hợp phân mảnh theo ngữ nghĩa (Semantic Chunking) để đảm bảo các khối dữ liệu (chunks) không bị mất ngữ cảnh gốc.
*   *Chunk Size tối ưu:* 512 tokens.
*   *Overlap Size:* 64 tokens (để nối ngữ cảnh giữa các đoạn liền kề).

### 3.2. Vector hóa & Lưu trữ (Embeddings & Database)
*   **Embedding Model:** Sử dụng model `text-embedding-3-small` (hoặc `cohere-embed-multilingual-v3`) để tối ưu hóa khả năng hiểu ngữ nghĩa tiếng Việt đa ngành hàng.
*   **Vector Database:** pgvector tích hợp trực tiếp trên Supabase database hiện tại của MoSpark để tối ưu hóa chi phí vận hành và đồng bộ dữ liệu nhanh với CMS.

---

## 4. Cơ Chế Truy Xuất Động (Retrieval & Query Orchestration)

Khi một tác vụ sinh nội dung (Outline/Detail Generator) hoặc một câu hỏi từ Chatbot được kích hoạt, hệ thống sẽ thực hiện quy trình truy xuất 3 lớp:

```
                  +-----------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tác vụ sinh bài viết / Câu hỏi User</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
                  +-----------------------------------------+
                                       | (Trích xuất Keyword & Embedding)
                                       v
                  +-----------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tìm kiếm độ tương đồng (RAG)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">(Supabase pgvector)</td>
    </tr>
  </tbody>
</table>
                  +-----------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
                   +-------------------+-------------------+
                   | (Độ khớp > 0.75)                      | (Độ khớp < 0.75)
                   v                                       v
+-------------------------------------+  +-------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lọc theo Metadata của Project</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Fallback về Google Search</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">(Lấy Brand + Product Chunks)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">(Grounding Search)</td>
    </tr>
  </tbody>
</table>
+-------------------------------------+  +-------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;"></th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
                   +-------------------+-------------------+
                                       v
                  +-----------------------------------------+
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Bơm vào Context Layer gửi đến LLM</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
                  +-----------------------------------------+
```

### 4.1. Thuật toán tìm kiếm tương đồng (Similarity Search)
Hệ thống tính toán khoảng cách Cosine Similarity giữa Vector câu truy vấn và cơ sở dữ liệu Vector DB.
*   **Ngưỡng lọc (Threshold):** Đặt ở mức $0.75$. Các đoạn có điểm tương đồng dưới $0.75 sẽ bị loại bỏ để tránh nạp dữ liệu rác.
*   **Giới hạn truy xuất (Top-K):** Lấy tối đa $Top-5 chunks liên quan nhất cho mỗi lượt sinh nội dung.

### 4.2. Bơm Ngữ Cảnh Tự Động (Inference Context Injection)
Hệ thống biên dịch prompt động bằng cách gộp các chunks tìm được vào Prompt gửi sang LLM:
$$Final System Prompt= Project-Specific System Prompt+ RAG Brand Guideline Chunks$
$$Final User Prompt= Business Context+ RAG Product Specs Chunks+ Primary Keyword$

### 4.3. Gợi ý Chèn Liên Kết Chéo (RAG Cross-linking Recommendation)
Khi viết một bài mới (ví dụ: *Cách đăng ký phạt nguội qua momo*), RAG Engine sẽ quét cơ sở dữ liệu các bài viết hiện hữu:
*   Phát hiện các bài liên quan (ví dụ: *Quy định nộp phạt nguội xe máy*, *Cách đăng ký Ví Trả Sau*).
*   Tự động xuất danh sách các URL gợi ý chèn Internal Link vào CMS Editor để PM phê duyệt. Điều này ngăn chặn việc bỏ sót link juice và tối ưu hóa SEO Silo Structure.

---

## 5. Yêu Cầu Giao Diện Quản Trị RAG trên Web (UI/UX Specification)

Nằm trong khu vực cấu hình nâng cao của Admin Panel MoSpark:

### 5.1. Màn hình Quản lý Nguồn Tri thức (Knowledge Center Dashboard)
*   **Trình tải lên tài liệu (Ingestion Panel):**
    *   Hỗ trợ kéo thả các file định dạng `.md`, `.pdf`, `.docx`.
    *   Ô nhập URL để crawl dữ liệu tự động từ các trang hướng dẫn của MoMo (ví dụ: `momo.vn/huong-dan-thanh-toan`).
*   **Trình kết nối API (API Connectors):** Nơi cấu hình để đồng bộ dữ liệu thời gian thực từ các Cell Teams.
*   **Bảng giám sát Chỉ mục (Vector Indexing Dashboard):**
    *   Hiển thị danh sách tài liệu đã index.
    *   Số lượng chunks được sinh ra từ mỗi tài liệu.
    *   Trạng thái index (Success / Pending / Error).

### 5.2. RAG Playground (Khu vực thử nghiệm)
*   Giao diện hộp chat giả lập để PM hoặc Developer gõ thử câu hỏi/từ khóa.
*   Hệ thống sẽ hiển thị danh sách các Chunks được truy xuất kèm theo điểm số tương đồng (Similarity Score) và nguồn gốc tài liệu (Source file/URL).
*   Giúp tối ưu hóa các tham số cắt đoạn (Chunk size) và ngưỡng lọc (Threshold) trước khi chạy thực tế.

---

## 6. Quy Tắc Kỹ Thuật & Bảo Mật Dữ Liệu (Technical & Security Constraints)

### 6.1. Quản lý Quyền Truy cập (RBAC Matrix)
*   **System Admin / Tech Lead (Duy/Bảo):** Quyền CRUD đối với tất cả Knowledge Sources, điều chỉnh cấu hình Chunking và Embedding.
*   **Product Manager (PM):** Xem danh sách tài liệu, chạy RAG Playground, upload tài liệu bổ sung cho dự án của mình (Project-level Knowledge).
*   **Content Writer:** Quyền đọc dữ liệu thông qua các prompt tự động, không có quyền upload trực tiếp tài liệu hệ thống.

### 6.2. Bảo Mật Thông Tin & Loại Bỏ Dữ Liệu Nhạy Cảm (Data Scrubbing)
*   **Nguyên tắc Zero PII (Personally Identifiable Information):** RAG Knowledge Base chỉ được lưu trữ thông tin sản phẩm, chính sách và cẩm nang thương hiệu. Tuyệt đối không lưu trữ thông tin khách hàng, số điện thoại, số tài khoản hoặc lịch sử giao dịch cá nhân.
*   **Hậu kiểm tự động:** Hệ thống chạy bộ lọc regex và các model NER (Named Entity Recognition) để tự động bóc tách/mã hóa các chuỗi ký tự nghi ngờ là thông tin cá nhân trước khi thực hiện vector hóa.

### 6.3. Cơ chế Quản lý Vòng đời & Tự động Dọn dẹp Dữ liệu Hết hạn (Data Lifecycle & Decay Management)
Để tránh hiện tượng phình dữ liệu (Data Bloat), tiết kiệm dung lượng Vector DB và tối ưu hóa context window (tránh tốn tokens khi truy xuất), RAG Engine áp dụng các quy chuẩn quản lý vòng đời tri thức chặt chẽ:

1.  **Thiết lập Expiration Tag (TTL - Time To Live):**
    *   Mỗi tài liệu hoặc bài viết lịch sử GenAI khi nạp vào hệ thống bắt buộc phải được gắn kèm thẻ thời gian hết hạn (`expire_at`).
    *   *Quy tắc mặc định:* Các tài liệu tĩnh (Brand Guideline, Design System) có TTL vô hạn; thông tin khuyến mãi/mã ưu đãi ngắn hạn có TTL mặc định 30 ngày; các phiên bản nháp GenAI nháp có TTL mặc định 15 ngày.
2.  **Cơ chế Tự động Dọn dẹp (Auto-purge Cron Job):**
    *   Hệ thống Vector DB (do Duy thiết lập backend) chạy một cron job định kỳ quét hàng tuần để tự động xóa các vector và chunks đã quá thời hạn `expire_at`.
3.  **Lớp Lưu trữ Đệm & Xử lý Dữ liệu Hết hạn (Archive & Fallback Gate):**
    *   Đối với các tài liệu về sản phẩm/dịch vụ quan trọng sắp hết hạn, hệ thống sẽ gửi thông báo cảnh báo đến màn hình Admin. PM có quyền chọn `Gia hạn` (Extend TTL) hoặc `Xác nhận xóa` (Approve Purge).
    *   Nếu PM không phản hồi sau 7 ngày, các chunks của tài liệu này sẽ tự động được chuyển sang đĩa lạnh (Cold Storage - lưu trữ dạng nén không index vector) và loại bỏ khỏi Vector DB hoạt động để giải phóng bộ nhớ RAM cho hệ thống index.
4.  **Tối ưu hóa Token khi Inference:**
    *   Khi RAG Engine thực hiện truy xuất thông tin, các chunks cũ có điểm tương đồng (Similarity score) thấp hoặc có nhãn thời gian cũ hơn sẽ bị hạ mức ưu tiên hoặc lọc bỏ hoàn toàn, tránh việc nhúng thông tin thừa thãi làm phình to payload gửi tới LLM.

---

## 7. Tài liệu Liên kết (Related Documents)
*   **Platform Master:** [MoSpark Master Doc](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_master.md)
*   **PLG Project Hub:** [MoSpark PLG Project Hub](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_plg_project.md)
*   **GenAI Production Lab:** [MoSpark GenAI Content Engine](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_genai_content.md)

---
*Maintained by: Văn Hiến (Web Product Lead) | Technical Lead: Duy (Senior BE Developer)*
