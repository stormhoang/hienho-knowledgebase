# BRD: Bảo Hiểm Ô Tô

> - **Dự án:** Bảo Hiểm Ô Tô (Vật Chất Xe - VCX & TNDS)
> - **URL chính:** momo.vn/bao-hiem-o-to
> - **Khối phụ trách:** FS (Financial Services)
> - **Use Case:** InsurTech
> - **Owner:** Web Platform
> - **Phê duyệt:** Web Product Lead (Văn Hiến)
> - **Phiên bản:** 1.0 - Draft (12/07/2026)
> - **Trạng thái:** Draft - cần review với BU, Web Platform, Media Team

---

## 1. Executive Summary

### 1.1 Elegant Problem Framing
- **Vấn đề cốt lõi:** Người dùng có nhu cầu tìm hiểu về bảo hiểm ô tô (đặc biệt là Vật Chất Xe) qua công cụ tìm kiếm, tuy nhiên từ vựng bảo hiểm thường phức tạp, nhiều điều khoản, người dùng sợ "mua sai" hoặc bị hớ. Việc chỉ tập trung bán qua In-app đang bỏ lỡ hoàn toàn hành vi nghiên cứu và so sánh tự nhiên này.
- **Giải pháp (The "What"):** Xây dựng Mini-web BHOTO thanh toán end-to-end với 9 trang đối tác bảo hiểm minh bạch (review thực, biểu phí). Biến MoMo từ một "cổng thanh toán" thành một "aggregator minh bạch và tiện lợi".

### 1.2 Situation
Thị trường Việt Nam hiện có ~2 triệu xe ô tô, với 60% chưa trang bị bảo hiểm. 75% người dùng Việt bắt đầu hành trình mua sắm phương tiện thông qua Search Engine. Tuy nhiên, MoMo hiện tại chủ yếu tiếp cận qua In-app, lượng leads chững lại quanh 3-4K/tháng và không nhắm đúng đối tượng (chủ yếu từ touchpoint VETC - xe không kinh doanh).

### Complication
**Vấn đề cốt lõi: Traffic organic Web sụt giảm mạnh và rank yếu.**
Organic traffic năm 2025 giảm ~80% từ tháng 1 (44.968 views) đến tháng 12 (9.203 views). Các trang thương mại chủ lực (main page `/bao-hiem-o-to`, `/than-vo`) đang rank ngoài top 10 với 0 click. MoMo không xuất hiện trong Google AI Overview cho các core keyword, để đối thủ và các aggregator khác chiếm sóng.

### Resolution
Triển khai chiến lược revamp toàn bộ Mini-web để hỗ trợ thanh toán end-to-end với đa phương thức (AIO QR) và direct discount. Song song chạy SEM quick win. Mục tiêu: Thu hút 9.800 traffic (VCX) và 6.000 traffic (TNDS), kéo theo hàng trăm đơn hàng mới thông qua Web.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Keyword Data & Opportunity
- **Total Market Pool:** 75.080 search/tháng (Toàn bộ automotive universe).
- **VCX (Tự nguyện):** 199.190 search/năm (2025). Top-3 VCX volume: 74.680 (AOV ~7.1M VNĐ).
- **TNDS (Bắt buộc):** 212.070 search/năm (2025). Top-3 TNDS volume: 45.840 (AOV ~561K VNĐ).
> **[CẦN VERIFY]** Total Market Pool 75.080/tháng không khớp scope với volume VCX+TNDS năm. Cần chuẩn hóa 1 nguồn keyword universe duy nhất.

### 2.2 Content Inventory Hiện Tại
- **Số lượng:** 72-80 bài viết (cần audit lại số lượng chính xác).
- **Content Decay (Tình trạng rác nội dung):** Dữ liệu cho thấy 84% traffic chỉ đến từ 30 bài cốt lõi. Khoảng 40-50 bài viết còn lại đang là "dead weight" kéo tụt sức khỏe toàn trang.
- **Hiệu năng:** Top traffic nằm ở các bài TOFU/SUPPORT (vd: "Mức phạt nồng độ cồn" - 20K traffic) nhưng CTR cực thấp (0.3 - 0.7%).
- **Trang cha (Main page):** Đang có sự chuyển dịch lớn. Cụm từ khóa "vật chất" (bảo hiểm vật chất xe ô tô) đã mất hút hoàn toàn trên bảng xếp hạng (hạng 27 rớt xuống 0). Ngược lại, cụm từ khóa "thân vỏ" đang có đà tăng trưởng cực mạnh trong T7/2026: "Bảo hiểm thân vỏ ô tô" leo từ hạng 56 lên hạng 17, đặc biệt keyword "mua bảo hiểm thân vỏ ô tô" đã **lọt top #2**.
- **AI Overview:** Đã bắt đầu xuất hiện và trigger thành công cho từ khóa intent giá cả là "giá bảo hiểm thân vỏ ô tô".
- **Điểm sáng:** Bài "Mua Bảo hiểm Ô tô Bắt buộc" có CTR tốt (41.2%), có thể dùng làm template tham chiếu.

---

## 3. Định Hướng Dự Án

### 3.1 Dự án này phục vụ điều gì? (In-Scope)
- **Revamp Mini-web BHOTO:** Tối ưu UI/UX, tích hợp Direct discount pricing và Multi-payment method (AIO QR).
- **Insurer Sub-pages:** Đã Go Live 9 trang đối tác bảo hiểm (PVI, Bảo Việt, PJICO, DBV, MIC, PTI, Liberty, Bảo Long, GIC) với nội dung E-E-A-T chuẩn. Cấu trúc URL được sử dụng: `/bao-hiem-o-to/doi-tac/{tên đối tác}`.
- **URL Migration & Redirect:** Gộp các URL rời rạc về đúng chuẩn cấu trúc `/bao-hiem-o-to/doi-tac/`.
- **Off-page & SEM:** Triển khai backlink, PR article để build authority (hướng tới AI Overview) và chạy test SEM campaign.

### 3.2 Dự án này KHÔNG phải (Out of Scope)
- Không bao gồm Bảo hiểm xe máy.
- Không bao gồm các module bảo hiểm khác ngoài VCX và TNDS (như bảo hiểm người ngồi trên xe).
- Không mở rộng ra thị trường quốc tế ở giai đoạn này.

---

## 4. JTBD Analysis

### Job #1: So sánh phí và quyền lợi giữa các nhà bảo hiểm
> "Phí bảo hiểm hãng nào rẻ nhất? Quyền lợi bồi thường của Bảo Việt có hơn PVI không?"
- **Functional:** Xem báo giá nhanh, so sánh điều khoản mở rộng và điều khoản loại trừ của 9 nhà BH.
- **Emotional:** Không bị hớ, cảm giác thông minh khi chọn được gói hời nhất.
- **Giải pháp:** Insurer Sub-page cho 9 hãng với cấu trúc minh bạch: USP, Điều khoản, Review thực từ user.

### Job #2: Mua bảo hiểm phù hợp theo Dòng xe cụ thể
> "Tôi đi VinFast VF8, nên mua gói nào? Phí bao nhiêu?"
- **Functional:** Biết chính xác chi phí cho dòng xe của mình.
- **Emotional:** Cảm giác cá nhân hóa, chắc chắn gói bảo hiểm cover đúng rủi ro của dòng xe đó.
- **Giải pháp:** (Đã loại bỏ khỏi scope dự án Bảo Hiểm) ➔ Chuyển giao về luồng quản lý Vehicle Profile của dự án Vehicle Hub mẹ để xử lý.

### Job #3: Nhanh chóng nhận GCN Điện tử hợp lệ
> "Tôi cần mua ngay để đi đường không bị phạt."
- **Functional:** Thanh toán 1-chạm (AIO QR), cấp GCN ngay lập tức.
- **Emotional:** An tâm, tiện lợi, tiết kiệm thời gian chờ đợi.
- **Giải pháp:** Revamp luồng thanh toán trên Mini-web.

---

## 5. Kiến Trúc Web & Chiến lược GEO

### 5.1 Sitemap Hub & Spoke
```text
momo.vn/bao-hiem-o-to [Hub]
│
├── TRANG SẢN PHẨM (SPOKE)
│   ├── /bao-hiem-o-to/than-vo           - Vật chất xe (VCX)
│   ├── /bao-hiem-o-to/bat-buoc          - TNDS
│
├── LANDING PAGE 9 NHÀ BẢO HIỂM (INSURERS)
│   ├── /bao-hiem-o-to/doi-tac/pvi
│   ├── /bao-hiem-o-to/doi-tac/bao-viet
│   └── ... (PJICO, DBV, MIC, PTI, Liberty, Bao Long, GIC)
│
└── BLOG CẨM NANG (TOFU/SUPPORT)
    └── Các bài viết tư vấn, review (optimize cross-sell block)
```

### 5.2 Content Structure - Insurer Sub-page
Các trang đối tác được cấu trúc chuẩn E-E-A-T với 14 block chính:
- META (Title, Desc, Schema).
- HERO (Tagline, Rating placeholder, CTA).
- STATS (4 chỉ số tin cậy).
- BENEFITS (4 USP riêng từng hãng).
- ACCORDION (Bồi thường / Điều khoản mở rộng / Loại trừ).
- WHY MOMO (Tự so sánh vs Chuyên gia tư vấn).
- SHOWCASE CLAIM (Hồ sơ bồi thường thực tế).
- REVIEWS (3 review thực: Tên, Tỉnh, Rating).
- STEPS (4 bước mua).
- WHO (Phù hợp vs Cân nhắc thêm).
- FAQ (6 câu hỏi cố định).
- LONG TEXT (E-E-A-T intro).
- CTA & Order Value (Social proof về số đơn lịch sử).
> **[CẦN VERIFY]** Tránh fake rating (hiện tại tất cả đều 4.9/5). Fix lỗi trùng block "WHY MOMO" của Liberty và MIC.

### 5.3 GEO/AEO Strategy
- **Mục tiêu:** Top 10 cho 3 core keywords + Hiện diện trên Google AI Overview (hiện tại: False).
- **Cam kết Từ khóa (Agency Midas):** Nhóm từ khóa thương mại chủ lực (đặc biệt là cụm "thân vỏ") đang được Cell Team thuê agency Midas cam kết thứ hạng. Thực tế T7/2026 cho thấy Midas đang vượt KPI mảng "thân vỏ" (lọt top 2) nhưng fail mảng "vật chất" (do chuyển dịch URL).
- **Checklist:** Đoạn mở đầu (<50 từ) trả lời trực tiếp intent, Schema (Product/Service, FAQPage, BreadcrumbList), Internal Link chặt chẽ.
- **Off-page (Ngân sách 500 Triệu VNĐ):** Triển khai mạnh từ Tháng 4 đến Tháng 12 (đỉnh điểm Q3 với 60-80 triệu/tháng). Thực thi 25-35 bài Guest Post, 25-35 bài PR Báo tỉnh, và Textlink để build authority cực mạnh.

---

## 6. Success Metrics (KPI 2026)

### 6.1 Funnel Targets & North Star Metric
**North Star Metric:** Số hợp đồng mua qua kênh Web.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Sản phẩm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target Traffic</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target Leads</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">CR (Web-to-Purchase)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Business Target (Best Case)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>VCX</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">9.800</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1.400</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3.4%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">335 đơn (tăng từ 3 đơn năm 2025)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>TNDS</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6.000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">459</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">20.0%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">707 đơn</td>
    </tr>
  </tbody>
</table>

> **[CẦN VERIFY]** Mô hình Funnel (Marketing vs Business objective) đang có sự chênh lệch (1.400 leads x 3.4% = 48 đơn, khác với 335 đơn). Cần BU và Media Team chốt 1 model duy nhất.

### 6.2 Traffic Targets (Theo quý)
- **Q1/2026:** ~28.024 views.
- **Q2/2026:** ~30.021 - 34.170 views.
- **Q3/2026:** ~32.941 - 48.229 views.
- **Q4/2026:** ~40.037 - 89.889 views.

---

## 7. Dependencies & Constraints

### 7.1 Stakeholders & RACI
<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Người/Team</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trách nhiệm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Product Lead</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Văn Hiến</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Consult chiến lược SEO/GEO, audit, chuẩn hóa framework</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Media Team Web Product Lead</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Media Team / Ngọc Hạnh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content optimization, execution content plan</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>SEO Agency</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Midas</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cam kết thứ hạng từ khóa (Ranking KPI) và triển khai Off-page theo ngân sách</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Platform</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Anh Thuận, Bảo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Build mini-web, component (discount, payment)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>BU (Insurance)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">INS incharge</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Product objective, đối tác, pricing, direct discount</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>PR / Backlink</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Anh Đặng.Lê</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">PR article, đối tác PR & media mention</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Ads / SEM</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Team Ads, chị Tường</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search volume verify, campaign setup, budget</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>VP GPD</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Công</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Approve scope & budget</td>
    </tr>
  </tbody>
</table>

### 7.2 Constraints & Operational Blockers
- **Giải ngân Offpage Budget:** Ngân sách 500 triệu VNĐ phân bổ dồn dập vào Q3 (Tháng 7-9). Cần đảm bảo năng lực sản xuất content (Guest post, PR) của team Media Team theo kịp tiến độ giải ngân để không bị miss plan.
- **SEM Budget:** Ngân sách test (50 triệu) khá mỏng, rủi ro không đủ data để optimize CPA. Cần check kỹ volume.
- **Lộ trình (Q3-Q4):** File Action Plan hiện tại chỉ chi tiết Q2, cần break down các task cụ thể cho Q3 và Q4.

---

## 8. Risk Assessment

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Rủi ro</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mức độ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khả năng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hướng xử lý (Mitigation)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web đang bị Content Decay nặng (84% traffic chỉ từ 30 bài), làm giảm sức mạnh của toàn cụm chủ đề bảo hiểm.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bắt buộc triển khai chiến dịch Pruning (Xóa) hoặc Consolidate (Gộp) 40-50 bài kém chất lượng trước khi triển khai Off-page.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Biến động thứ hạng trong quá trình chuyển dịch (Migration) từ keyword "vật chất" sang "thân vỏ" có thể làm hụt traffic ngắn hạn.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tiếp tục dồn lực tối ưu On-page và Off-page cho cụm "thân vỏ" vì tín hiệu T7/2026 đang rất tốt (lên top 2).</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số liệu Funnel mâu thuẫn (MKT vs Business).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thống nhất 1 model với BU trước khi report KPI lên VP.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Fake rating/Review trên Insurer sub-page.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chỉ implement AggregateRating Schema nếu có review thực tế.</td>
    </tr>
  </tbody>
</table>

---

## 9. Change Log

- **Tháng 7/2026 (v1.0):** Khởi tạo BRD phiên bản chuẩn hóa, gộp nội dung từ 4 files rời rạc. Áp dụng chuẩn Product-led SEO/GEO framework.
