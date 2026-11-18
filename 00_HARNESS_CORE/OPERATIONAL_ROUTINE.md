# 📅 Operational Routine
perational Routine (Web Product Lead)

> **Vision**: Vận hành MoSpark như một Growth Engine tự động hóa, đảm bảo 100% nội dung đạt chuẩn E-E-A-T và tối ưu tỷ lệ Web-to-App.

---

## 0. AI Interaction Protocol (Bắt buộc)
Trước khi xử lý bất kỳ câu hỏi hoặc yêu cầu nào (đặc biệt là lập báo cáo, rà soát hiệu suất các dự án Hubs), AI phải tuân thủ [[momo-thinking-protocol]] theo cấu trúc 3 bước:
1.  **ĐỌC**: Nạp bối cảnh từ `MEETING_RECAPS.md` và **BẮT BUỘC tham chiếu hiệu suất thực tế từ `07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`** làm Single Source of Truth (SSOT).
2.  **DÙNG**: Chọn Framework và Skill phù hợp.
3.  **TRẢ**: Cấu trúc câu trả lời Actionable & Strategic.

---
---

## 1. Daily Health Check (15-30 phút)
*Mục tiêu: Đảm bảo "mạch máu" dữ liệu và hệ thống luôn thông suốt.*

*   **Audit Real-time**: Kiểm tra nhanh các nội dung mới xuất bản qua biến `Project` trên MoSpark.
*   **Gatekeeper Alert**: Tiếp nhận các yêu cầu Review từ team Media Team / Agency thông qua SEO/GEO Scoring.
*   **Critical Monitoring**: Observe tình trạng Indexing và Search Console của các dự án trọng điểm (Phạt Nguội, Vay Nhanh).
*   **AI Crawler Check**: Spot-check server logs cho OAI-SearchBot, Claude-SearchBot, PerplexityBot trên các page mới golive.

---

## 2. Weekly Orchestration (Vòng lặp 7 ngày)
*Mục tiêu: Điều phối nguồn lực và xử lý các nút thắt cổ chai.*

### Thứ 2: Planning & Alignment
*   Review **Project Orchestrator**: Cập nhật trạng thái Step 01-09 cho các dự án đang chạy.
*   Check-in với **Anh Bảo (Lead)**: Align về Roadmap tính năng mới của MoSpark (Simulation, API integration).

### Thứ 4: Quality Audit
*   Audit chuyên sâu 1 Use Case cụ thể (Ví dụ: Tuần 1: Cinema, Tuần 2: Vay Nhanh...).
*   Check lỗi Tech debt: Schema, Redirect 301, CWV (LCP < 2.5s).
*   Verify robots.txt đang allow đúng các AI search crawlers (OAI-SearchBot, Claude-SearchBot, PerplexityBot).

### Thứ 6: Governance & Support
*   Review bộ **GenAI Prompts**: Hiệu chỉnh Outline/Writer prompts dựa trên kết quả Ranking thực tế.
*   Support team **DA (Hải)**: Kiểm tra tính đúng đắn của Tracking Plan cho các Landing Page mới.
*   Check **llms.txt** các use case đang live: URLs có còn 200 OK không, có product mới cần add không.

---

## 3. Monthly Strategic Review (Vòng lặp 30 ngày)
*Mục tiêu: Đánh giá hiệu quả đầu tư và tối ưu hóa hệ thống.*

*   **SEO Inventory Audit**: Cập nhật SoV (Share of Voice) của MoMo so với đối thủ (Ví dụ: Vay Nhanh 6% ➔ Mục tiêu 10%).
*   **Migration Cleanup**: Rà soát các URLs cũ đã chuyển sang MoSpark, đảm bảo 100% Link Integrity.
*   **Standard Update**: Cập nhật **momo-seo-geo-guideline** và **YMYL Guideline** dựa trên các thuật toán mới của Google/AI Search.
*   **AI Citation Audit**: Test monthly - hỏi ChatGPT/Perplexity/Claude về các sản phẩm MoMo, kiểm tra AI đang describe đúng chưa. Nếu sai lệch → review llms.txt + Long Content nguồn.
*   **llms.txt Quarterly Review**: Verify toàn bộ URLs trong llms.txt trả về 200 OK. Update nếu có product mới hoặc URL thay đổi.

---

## 4. Workflow theo Dự án (Project-based Variable Logic)

Mỗi khi có một Use Case mới (Ví dụ: `Dịch vụ công`), Routine thực thi tuân thủ chặt chẽ theo Framework **[[seo-execution-sop]]** (Quy trình 8 bước triển khai). Dưới đây là tóm tắt các điểm chốt chặn (Gate Checks) quan trọng:

1.  **Define Project**: Khởi tạo biến `Project: Dịch vụ công` trên MoSpark.
2.  **Mapping Hierarchy**: Phân bổ URL cho các cụm trang (Blog, News, Help, Guides...).
3.  **Prompt Setup**: Chọn bộ Skill/Prompt phù hợp cho Use Case đó (Finance vs Lifestyle).
4.  **Gate Check**: Chỉ Sign-off xuất bản khi điểm **SEO Score > 80** và **Foundation Checklist** đạt 100%.
5.  **Tracking Handoff**: Gửi Event Spec cho team DA và Observe kết quả.

---

## 5. Các "Nút bấm" Quyết định (Decision Gates)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tình huống</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Quyết định của Hiến</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content Score < 80</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Reject</strong>: Yêu cầu Media Team / Agency sửa lại theo Guideline.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Use Case không có Search Demand</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Deprioritize</strong>: Chuyển xuống hàng chờ, không đầu tư Resource.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lỗi Tech/Platform</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Request</strong>: Gửi yêu cầu cho Anh Bảo xử lý trong Roadmap.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sai lệch Tracking</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Consult</strong>: Support team DA tìm ra "Truth of Source".</td>
    </tr>
  </tbody>
</table>

---

## 6. Framework Usage (Hệ thống tư duy)

Khi thực hiện các tác vụ phân tích và ra quyết định, hãy tham chiếu các Framework chuẩn trong folder `02_FRAMEWORKS`:

*   **Phân tích tăng trưởng**: Sử dụng [[80-20-growth]] để xác định 20% Use Cases mang lại 80% traffic.
*   **Giải quyết vấn đề**: Áp dụng [[First-Principles]] và [[critical-thinking]] để tìm root cause của traffic leak.
*   **Xây dựng nội dung**: Luôn bắt đầu bằng [[jtbd-analysis]] để hiểu điểm nghẽn của user trước khi viết Brief.
*   **Trình bày & Báo cáo**: Tuân thủ [[pyramid-principle]] để cấu trúc thông tin mạch lạc cho Lãnh đạo.
*   **Ra quyết định**: Sử dụng [[decision-framework]] cho các Fork Points chiến lược (ghi nhận vào Decision Log).

---
*Last Updated: 05/05/20
---

## Change Log
- **Tháng 5/2026:** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.

