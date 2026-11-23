# 🧠 Critical Thinking - The MoMo Gatekeeper

## 🎯 Mục tiêu
Đảm bảo mọi hành động trong hệ thống **Harness** đều dựa trên sự thật (Truth), dữ liệu (Data) và logic chặt chẽ. Ngăn chặn việc copy-cat mù quáng hoặc thực thi dựa trên các giả định sai lầm (false assumptions).

---

## 🧭 4 Trụ Cột Truy Vấn (The 4 Pillars of Interrogation)

### 1. Search Truth (Sự thật về Intent)
*Thách thức các giả định về SEO/GEO.*
- "Chúng ta target keyword này vì volume cao, hay vì nó thực sự dẫn tới conversion (Hire the Job)?"
- "Content này đang phục vụ Googlebot (Old SEO) hay đang phục vụ Answer Engine (New GEO)?"
- "Tại sao chúng ta nghĩ user muốn đọc bài blog dài 2000 chữ thay vì một cái tool tra cứu (Utility)?"
- **Red Flag:** "Đối thủ rank top bài này nên mình cũng phải viết bài tương tự." ➔ *Hỏi: MoMo có thể làm gì tốt hơn/khác đi để 'steal' citation từ AI Overview không?*

### 2. Data Truth (Sự thật về Con số)
*Thách thức các báo cáo và metrics.*
- "Baseline này lấy từ GSC (Clicks) hay GA4 (Sessions)? Tại sao có sự chênh lệch?"
- "W2A rate tăng là do landing page tốt hơn, hay do segment user từ social/paid đổ vào thay đổi?"
- "Dữ liệu này là Tương quan (Correlation) hay Nhân quả (Causation)?"
- **Red Flag:** "Traffic tăng 50% là thành công." ➔ *Hỏi: Bao nhiêu trong số đó là New User? Bao nhiêu người Register/KYC thành công?*

### 3. Product Truth (Sự thật về Chuyển đổi)
*Thách thức luồng Web-to-App.*
- "Tại sao user phải click vào CTA này? Họ nhận được giá trị gì ngay lập tức (Instant Gratification)?"
- "Deep-link này dẫn vào trang chủ App hay dẫn thẳng vào đúng flow trong App? (Friction check)"
- "Chúng ta đang tối ưu cho Desktop hay Mobile-first (90% traffic MoMo)?"
- **Red Flag:** "Thêm thật nhiều banner để tăng conversion." ➔ *Hỏi: Banner có làm loãng JTBD chính của trang không?*

### 4. Resource Truth (Sự thật về Nguồn lực)
*Thách thức tính khả thi và ROI.*
- "Feature này tốn 2 Sprint của Dev. Có cách nào làm 'Quick Win' bằng HTML/No-code trên MoSpark để validate trước không?"
- "Chúng ta đang giải quyết vấn đề 80/20 (Impact lớn nhất) hay đang sa đà vào các tiểu tiết?"
- "Nếu dự án này thất bại, chúng ta mất bao nhiêu tiền/công sức? (Risk check)"

---

## 🕵️ Chế độ "Hallucination Hunting" (Dành cho AI Content)
Khi review nội dung do AI tạo ra (Claude/Gemini), luôn kiểm tra:
- **Dữ liệu tài chính:** Lãi suất, hạn mức, quy định pháp lý có đúng với [[mospark_genai_content#7. Business Context - Các trường bắt buộc|mospark_business_context]] không?
- **Logic vòng vo:** AI có đang viết filler (văn mẫu) thay vì đi thẳng vào câu trả lời cho User không?
- **Brand Voice:** Giọng văn có bị quá "robot" hay sai lệch với Core Mantra của MoMo không?

---

## 🛠 Thực thi: The Interrogation Log (Mẫu output)
Khi được yêu cầu "Critical Thinking" cho một dự án, Agent hãy output theo format:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giả định (Assumption)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lỗ hổng / Nghi vấn (Challenge)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cần Verify gì?</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đợt Triển Khai</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"User cần đọc hướng dẫn vay"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"User có thể chỉ muốn biết lãi suất thực tế ngay"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">A/B test Simulation tool vs Long-form content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Traffic tăng sẽ tăng MAU"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Traffic từ keyword 'là gì' thường có bounce rate cao"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Filter intent 'Buy/Do' trong keyword map</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Copy layout của Wise.com"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Context người dùng Việt Nam khác người dùng Wise"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Check JTBD local: User cần tin tưởng hay cần tốc độ?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đợt 2</td>
    </tr>
  </tbody>
</table>

---

## 🚦 Gate Check (Sign-off)
Trước khi chuyển sang [[orchestrator_engine]], hãy chắc chắn:
- [ ] Đã hỏi "Tại sao" ít nhất 3 lần cho mục tiêu của dự án.
- [ ] Đã xác định được "Single Source of Truth" cho dữ liệu.
- [ ] Đã đề xuất được một phương án đơn giản hơn (MVP) để đạt 80% kết quả.

## Liên kết
- Skill này dùng trước: [[brainstorming]], [[First-Principles]]
- Skill dùng kèm: [[jtbd-analysis]], [[Seo-Geo-audit]]
- Xem tổng thể: [[skill_registry]]
