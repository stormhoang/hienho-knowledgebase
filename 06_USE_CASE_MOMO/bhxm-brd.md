# BRD: Bảo Hiểm Xe Máy

> - **Dự án:** Bảo Hiểm Xe Máy Web Growth
> - **URL chính:** momo.vn/bao-hiem-xe-may
> - **Khối phụ trách:** FS (Financial Services)
> - **Use Case:** InsurTech
> - **Owner:** Web Platform
> - **Phê duyệt:** Web Product Lead (Hiến)
> - **Phiên bản:** 1.2 - Tháng 7/2026
> - **Trạng thái:** Draft (Updated Media Team Plan)
> - **SEO Score:** 65/100 | **Traffic:** 15K sessions/tháng | **W2A:** 8.5%

---

## 1. Executive Summary

### 1.1 Elegant Problem Framing
- **Vấn đề cốt lõi:** Chủ xe máy thường quên mua hoặc không biết bảo hiểm của mình khi nào hết hạn, đến khi bị vẫy vào chốt CSGT thì bị phạt nặng. Đọc luật thì dài, mua thì sợ mua nhầm thẻ bảo hiểm giả.
- **Giải pháp (The "What"):** Biến MoMo thành "Cứu tinh 1-chạm". Cung cấp PLG tool nhập biển số xe để tra cứu thời hạn, tính phí và đóng tiền gia hạn ngay lập tức, cấp Giấy chứng nhận điện tử hợp lệ trình CSGT.

### 1.2 Situation
MoMo là một trong những kênh phân phối bảo hiểm xe máy trực tuyến lớn tại Việt Nam, đã phân phối hơn 2.3 triệu hợp đồng với đối tác là các nhà bảo hiểm uy tín (Bảo Việt, PVI, PTI, MIC, GIC, Liberty). Thị trường có nền tảng cầu tự nhiên rất cao: 72 triệu xe máy đang lưu hành, bảo hiểm TNDS bắt buộc theo pháp luật.

Dữ liệu keyword nội bộ ghi nhận 519 từ khoá, tổng volume ~67,540/tháng và chạm mức cao nhất ~76,460 vào tháng 3/2025. Nhu cầu tìm kiếm trải rộng 7 cluster khác nhau từ transactional, informational đến utility.

### Complication

**Vấn đề cốt lõi: Traffic sụt 95% sau mỗi spike đầu năm.**

Dữ liệu internal cho thấy: Tháng 1 đạt 79K → Tháng 2: 16K → Tháng 3: 6.4K → Tháng 4: 5.1K → Tháng 5: 4K. Pattern này lặp lại mỗi năm, cho thấy MoMo chỉ đang tận dụng được spike theo mùa từ cluster "Phạt/Pháp lý" mà không xây được baseline traffic quanh năm.

6 trong 7 keyword cluster lớn (Giá, Tra cứu, Địa điểm, Nhà BH, Kiến thức, Xe máy điện) chưa có trang đích tương ứng trên momo.vn. Cụ thể:

- Cluster "Giá" (~8,500 vol/tháng): chưa có trang bảng giá theo phân khối với calculator
- Cluster "Tra cứu" (~2,500 vol/tháng): chưa có widget tra cứu biển số/số khung
- Cluster "Địa điểm" (~4,000 vol/tháng): user tìm kênh offline nhưng không được redirect sang online MoMo
- Cluster "Xe máy điện" (+40% YoY): whitespace ít cạnh tranh, MoMo chưa có trang riêng

Các đối thủ không bán hàng (royalhelmet.com.vn, ibaohiem.vn) đang chiếm Top 3-5 cluster Kiến thức và Giá. Các nhà BH trực tiếp (MIC, PVI, PTI) chiếm branded cluster của chính họ. Trang cha `/bao-hiem-xe-may` chỉ có content TOFU cơ bản, thiếu khoảng 15-20 trang so với sitemap mục tiêu.

### Resolution

Xây dựng cluster Bảo Hiểm Xe Máy theo kiến trúc Hub & Spoke đầy đủ: 1 trang cha đóng vai Hub, các spoke gồm trang sản phẩm, trang theo nhà BH, trang theo loại xe (bao gồm pSEO), và blog content hub. Song song, tối ưu GEO/AEO để MoMo được trích dẫn trong Google AI Overview, Gemini, và các AI assistant khi user hỏi về bảo hiểm xe máy. Mục tiêu: xây baseline 15-25K sessions/tháng quanh năm, spike 70-90K tháng 1 hàng năm.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Hiện Trạng Trang Cha `/bao-hiem-xe-may`

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khía cạnh</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">URL</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">momo.vn/bao-hiem-xe-may</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trạng thái</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang hoạt động - có hero form mua BH, so sánh CÓ/KHÔNG BH, hướng dẫn bồi thường 4 bước</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content hiện có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TOFU cơ bản: hero + trust bar + so sánh + hướng dẫn quy trình</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thiếu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảng giá theo phân khối, widget tra cứu, cluster nhà BH, cluster loại xe, blog hub, FAQ schema, AggregateRating schema</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4-79K sessions/tháng (biến động theo mùa, đỉnh tháng 1 do Nghị định 168)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vấn đề cốt lõi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không có evergreen content cluster - traffic sụt 95% sau spike tháng 1</td>
    </tr>
  </tbody>
</table>

### 2.2 Keyword Data - 7 Pillar Clusters

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vol ước tính</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trang đích hiện tại</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khoảng trống</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua / Giao dịch Online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~15,000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/bao-hiem-xe-may (hiện có)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tối ưu UX/copy, thêm trust signals</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phạt / Bắt buộc / Pháp lý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~12,000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có blog mức phạt cũ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Update 2026, thêm biến thể FOMO</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giá / Chi phí</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~8,500/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần /bao-hiem-xe-may/bang-gia + calculator</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Địa điểm / Kênh mua offline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~4,000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bridge content chuyển offline sang online intent</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Kiến thức / Giải thích</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~4,000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rải rác, không có hub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog hub + FAQ schema</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu / Kiểm tra hạn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~2,500/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/bao-hiem-xe-may/tra-cuu + widget biển số</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhà BH Branded</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~2,000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Landing page per nhà BH</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xe máy điện</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">+40% YoY</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/bao-hiem-xe-may/xe-may-dien - whitespace ít cạnh tranh</td>
    </tr>
  </tbody>
</table>

**Insight quan trọng:** Cluster "Phạt" có CPC = 0đ vào tháng 10/2025 - không ai bid, organic gần như free. ~60 biến thể keyword, tổng ~12,000 vol/tháng. Đây là nhóm FOMO conversion cao nhất, ranking dễ nhất - nên publish đầu tiên.

### 2.3 Phân Tích Cạnh Tranh

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đối thủ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster đang chiếm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Điểm yếu</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cơ hội MoMo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">royalhelmet.com.vn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phạt - Giá - Kiến thức (Top 3-5)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không có sản phẩm - zero conversion</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cùng content depth + inline form. Thắng bằng trust 2.3M hợp đồng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ibaohiem.vn / tasco.vn / opes.com.vn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Kiến thức - Tra cứu (DA tốt)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">UX kém, không mobile-first, không có widget tra cứu thực</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Beat Core Web Vitals + widget tra cứu biển số thực tế</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Điện Máy Xanh / TGDĐ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua + Địa điểm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH chỉ là phụ trợ, không có cluster giá hay tra cứu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo chuyên sâu hơn - tra cứu, tái tục, cluster giá 2/3 năm</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MIC / PVI / PTI trực tiếp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Branded cluster của chính họ (~260-390/brand)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chỉ push 1 nhà BH, không có trang so sánh đa bên</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo = trung lập đa nhà BH - trang so sánh capture toàn cluster branded</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ZaloPay / ViettelMoney</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Branded search nhỏ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web SEO rất yếu, không có content cluster</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Duy trì lợi thế content depth - tấn công thay vì phòng thủ</td>
    </tr>
  </tbody>
</table>

### 2.4 Seasonality & Trend

**Spike định kỳ hàng năm:**
- Tháng 11-12: Cuối năm, nhiều người biết BH sắp hết hạn - "gia hạn bảo hiểm xe máy" tăng mạnh
- Tháng 1: Nghị định mới có hiệu lực, CSGT tăng cường - cluster Phạt/Mức phạt đỉnh điểm
- Tháng 4-5: Mùa mưa bắt đầu - cluster bồi thường, tai nạn tăng
- Tháng 6-7: Mùa học mới, học sinh/sinh viên mua xe - cluster 50cc/xe điện học sinh

**Emerging trends:**
- Xe máy điện: +40% YoY. VinFast, Yamaha Neo, Yadea tạo cluster keyword mới "xe máy điện có cần bảo hiểm không" - whitespace ít cạnh tranh, nên chiếm trước.
- GCN điện tử: Sau Nghị định 03/2021, hợp pháp 100% nhưng user vẫn search "giấy chứng nhận điện tử có hợp lệ không" - cần content trust-building.
- Mobile-first purchase: Search query ngày càng conversational hơn, MoMo là Super App có lợi thế tự nhiên.

---

## 3. Định Hướng Dự Án

### 3.1 Dự Án Này Phục Vụ Điều Gì?

**Xây dựng cluster Bảo Hiểm Xe Máy như một Organic Growth Engine phục vụ 3 mục tiêu:**

**Acquisition - Capture toàn bộ funnel bảo hiểm xe máy**

User đang search từ nhiều entry point (mua, giá, tra cứu, địa điểm, pháp lý) nhưng MoMo chỉ có 1 trang cha phủ được cluster transactional. Cần xây đủ 7 cluster để không để traffic rơi vào tay đối thủ không có conversion value.

**Retention & Renewal - Tra cứu và Gia hạn như utility**

User đã mua BH trên MoMo cần tra cứu hạn, gia hạn hàng năm. Xây `/bao-hiem-xe-may/tra-cuu` và `/bao-hiem-xe-may/gia-han` như utility tools - vừa phục vụ user hiện tại, vừa capture organic traffic từ user chưa mua trên MoMo.

**GEO/AI Visibility - Trở thành nguồn trích dẫn cho AI engines**

FAQ + HowTo + AggregateRating Schema trên trang cha và trang sản phẩm inject câu trả lời vào Google AI Overview, Gemini, Perplexity khi user hỏi "mua bảo hiểm xe máy ở đâu uy tín?" hay "bảo hiểm xe máy MoMo có tốt không?". Đây là GEO moat dài hạn vì cần entity authority mạnh (số hợp đồng, đối tác nhà BH, dữ liệu thực).

### 3.2 Dự Án Này KHÔNG Phải

- Không phải xây lại trang marketing campaign - đây là evergreen content cluster phục vụ organic traffic
- Không phải CMS cho nhà BH tự quản lý content
- Không phải store locator hay agent directory
- Không phải thay thế Deep Link / App flow - web chỉ là entry point, conversion vẫn xảy ra trong App

---

## 4. JTBD Analysis

### Job #1: Xác Nhận Nghĩa Vụ Pháp Lý

> "Tôi cần biết xe mình có bắt buộc mua bảo hiểm không, và không mua thì bị phạt bao nhiêu."

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xác nhận xe loại mình có bắt buộc mua BH không. Biết chính xác mức phạt hiện hành theo Nghị định mới nhất</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tránh bị phạt bất ngờ, bị giữ xe. Cảm giác tuân thủ pháp luật, an tâm lưu thông</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không muốn bị cảnh sát giao thông "làm khó" trước mặt người khác</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấy bạn bè bị phạt - Nghe tin mức phạt mới - CSGT đang kiểm tra đường mình đi</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** Blog cluster Phạt/Pháp lý - Bảng mức phạt 2026 cập nhật (Nghị định 168) - CTA mua ngay.

---

### Job #2: So Sánh Giá Và Lựa Chọn Nhà BH Phù Hợp

> "Bảo hiểm xe máy giá bao nhiêu? Mua Bảo Việt hay PVI hay MIC thì tốt hơn?"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Biết chính xác phí bảo hiểm theo phân khối xe. So sánh giữa các nhà BH. Tìm gói tự nguyện phù hợp</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cảm giác mua đúng giá, không bị "chặt chém". Thông minh tài chính</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chia sẻ thông tin BH tốt với gia đình, bạn bè có xe</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuẩn bị mua xe mới - BH sắp hết hạn - Đang so sánh trên điện thoại</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** /bao-hiem-xe-may/bang-gia + price calculator + landing page per nhà BH với điểm khác biệt.

---

### Job #3: Tra Cứu Hạn BH Và Gia Hạn Nhanh

> "Xe mình còn BH không? Hết hạn rồi thì gia hạn ở đâu nhanh nhất?"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhập biển số - biết ngay xe còn hạn không. Gia hạn ngay trong 1-2 click nếu hết hạn</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tránh lo lắng, không chắc xe còn hạn không trước khi lên đường. Tự tin khi ra đường</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trách nhiệm với gia đình - không để xe hết BH mà không biết</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuẩn bị đi xa - CSGT đang kiểm tra - Nhớ ra BH có thể hết hạn rồi</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** /bao-hiem-xe-may/tra-cuu (widget biển số, kết quả contextual: Còn hạn → "Gia hạn", Hết hạn → "Mua ngay").

---

### Job #4: Mua BH Nhanh, Không Cần Ra Ngoài

> "Tôi biết cần mua rồi - làm sao mua online nhanh nhất, nhận GCN ngay?"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua xong trong dưới 3 phút, trên điện thoại. Nhận GCN điện tử hợp lệ ngay sau thanh toán</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không mất thời gian ra bưu điện, đại lý. Cảm giác hiệu quả, tiện lợi</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo là Super App - mua BH ở đây như các việc khác: nhanh và tin</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang cầm điện thoại, sắp đi ra đường - Bạn bị phạt vừa nhắc nhở</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** Trang cha /bao-hiem-xe-may (hero form) + Blog "Không cần ra bưu điện" bridge content.

---

### Job #5: Được Bồi Thường Đúng Khi Xảy Ra Tai Nạn

> "Bị tai nạn rồi - làm thế nào để được nhà BH bồi thường? Cần giấy tờ gì?"

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dimension</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Functional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Biết chính xác quy trình bồi thường step-by-step. Biết cần giấy tờ gì, nộp ở đâu</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giảm stress trong lúc hoảng loạn sau tai nạn. Cảm giác được hỗ trợ, không bị bỏ mặc</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chứng minh BH mua trên MoMo "là thật", được bồi thường đàng hoàng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vừa xảy ra tai nạn - Người thân bị tai nạn - Tìm hiểu trước khi mua</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** /bao-hiem-xe-may/boi-thuong (hướng dẫn 4 bước + schema) + blog bồi thường chi tiết.

---

## 5. Kiến Trúc Web

### 5.1 Sitemap Hub & Spoke

```
momo.vn/bao-hiem-xe-may [Hub]
│
├── TRANG SẢN PHẨM
│   ├── /bao-hiem-xe-may/bat-buoc           - BH TNDS bắt buộc
│   ├── /bao-hiem-xe-may/tu-nguyen          - BH tự nguyện/vật chất
│   ├── /bao-hiem-xe-may/gia-han            - Gia hạn / Tái tục
│   ├── /bao-hiem-xe-may/boi-thuong         - Hướng dẫn bồi thường
│   ├── **PLG Interactive Tool:** /bao-hiem-xe-may/tra-cuu - Widget tra cứu biển số (Tiêu chuẩn trải nghiệm đột phá)
│   └── **PLG Interactive Tool:** /bao-hiem-xe-may/bang-gia - Bảng giá + Calculator tính phí
│
├── LANDING PAGE THEO NHÀ BH
│   ├── /bao-hiem-xe-may/bao-viet
│   ├── /bao-hiem-xe-may/pvi
│   ├── /bao-hiem-xe-may/pti
│   ├── /bao-hiem-xe-may/mic
│   ├── /bao-hiem-xe-may/gic
│   └── /bao-hiem-xe-may/liberty
│
├── LANDING PAGE THEO LOẠI XE (pSEO)
│   ├── /bao-hiem-xe-may/xe-may-dien        - Trend +40% YoY
│   ├── /bao-hiem-xe-may/duoi-50cc
│   ├── /bao-hiem-xe-may/50-175cc
│   ├── /bao-hiem-xe-may/tren-175cc
│   ├── /bao-hiem-xe-may/honda-wave
│   └── /bao-hiem-xe-may/yamaha-exciter
│
└── BLOG & CẨM NANG HUB
    ├── /blog/muc-phat-khong-bao-hiem-2026  - Pillar FOMO
    ├── /blog/gcn-bao-hiem-dien-tu
    ├── /blog/huong-dan-mua-bao-hiem-xe-may
    ├── /blog/bao-hiem-xe-may-dien
    ├── /blog/bh-bat-buoc-vs-tu-nguyen
    ├── /blog/mua-bao-hiem-online-vs-offline - Bridge offline intent
    ├── /blog/huong-dan-boi-thuong-tai-nan
    ├── /blog/sinh-vien-mua-bao-hiem-lan-dau
    └── /blog/checklist-xe-truoc-tet         - Seasonal
```

**Nguyên tắc internal linking:**
- Hub ➔ Spoke: Trang cha link ra tất cả trang sản phẩm, nhà BH, loại xe
- Spoke ➔ Hub: Mỗi trang con có breadcrumb + CTA về trang cha
- Spoke ➔ Spoke: Trang xe điện link sang trang dưới 50cc; trang Bảo Việt link sang trang PVI (comparison)
- Không để trang nào bị orphan

### 5.2 Content Structure - Trang Cha `/bao-hiem-xe-may`

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Component</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hero Section</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">H1 + Form chọn phân khối - CTA "Mua ngay". Tối ưu UX copy</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trust Bar</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2.3M hợp đồng - các nhà BH uy tín - GCN điện tử hợp pháp - Nhắc gia hạn tự động</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">So sánh CÓ vs KHÔNG mua BH</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2 cột: FOMO + benefit</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Grid nhà BH</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Logo + tên 6 nhà BH + CTA link tới trang riêng</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hướng dẫn 3 bước (HowTo)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chọn phân khối - Chọn nhà BH - Thanh toán & nhận GCN điện tử. HowTo Schema</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hướng dẫn bồi thường 4 bước</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CTA link sang /bao-hiem-xe-may/boi-thuong</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog feed</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6 bài mới nhất</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQ 10+ câu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Accordion, FAQPage Schema bắt buộc</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">9</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review / Đánh giá</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tối thiểu 10 reviews thực. AggregateRating Schema (4.x/5 sao) - quan trọng cho E-E-A-T và GEO</td>
    </tr>
  </tbody>
</table>

**Schema bắt buộc trang cha:** FAQPage - HowTo - Product - AggregateRating - BreadcrumbList

### 5.3 GEO/AEO Strategy

Bảo hiểm xe máy là YMYL - Google yêu cầu E-E-A-T cao. Các AI engines (Google AI Overview, Gemini, Perplexity) ưu tiên cite nguồn có structured data, FAQ rõ ràng, và authority signals.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nền tảng AI</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Behavior</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chiến lược tối ưu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Google AI Overview (SGE)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổng hợp từ 3-5 nguồn, hiển thị trước organic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQPage Schema bắt buộc, câu trả lời direct dưới 50 từ, cấu trúc H2/H3 rõ</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gemini (Google)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Real-time web access, ưu tiên nguồn authority</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cập nhật content sau mỗi Nghị định mới, structured data đầy đủ</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ChatGPT / Copilot</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cite từ training data, volume content indexed nhiều</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog chất lượng cao, được index và share nhiều</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TikTok / YouTube Search</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gen Z tìm qua video</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Embed video guide ngắn trong trang hướng dẫn mua</td>
    </tr>
  </tbody>
</table>

**E-E-A-T & AEO signals cần có:**
- **AEO/GEO Standard (VP GPD):** `momo.vn/bao-hiem-xe-may/llms.txt` chứa dữ liệu sạch về biểu phí BH bắt buộc 2026. Bắt buộc để được trích dẫn chính xác.
- Author byline với chức danh chuyên môn
- Ngày cập nhật visible (dd/mm/yyyy), Last reviewed date
- Cite đúng số Nghị định (Nghị định 168/2024/NĐ-CP, Nghị định 67/2023)
- Link tới văn bản pháp luật chính thức
- Số liệu thực: 2.3M hợp đồng, tên đối tác BH cụ thể

---

## 6. Success Metrics

### 6.1 KPI Framework

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Baseline</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target (90 ngày post-launch)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic sessions /bao-hiem-xe-may cluster</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~4-5K/tháng (ngoài mùa)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">15K/tháng (quanh năm)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC + GA4</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic sessions spike tháng 1/2027</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">79K (tháng 1/2025)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">90K</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang mới trong Top 10 GSC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0 trang mới</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">10 trang mới</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Click-to-app từ cluster BH xe máy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang đo baseline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có baseline xác định</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 + Appsflyer</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog time on page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang đo baseline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2:30 phút</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AI Overview citations cho BH xe máy queries</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang audit</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5 queries được cite</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Manual monitoring</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AggregateRating Schema indexing</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xuất hiện Rich Results</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC Rich Results</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cross-sell CTR (post-purchase)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 events</td>
    </tr>
  </tbody>
</table>

### 6.1.2. Kế hoạch Thứ hạng Từ khóa (SEO Keyword Ranking Targets)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Từ khóa mục tiêu</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Baseline (T3/2026)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Target (T6/2026)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Target (T9/2026)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Target (T12/2026)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">mua bảo hiểm xe máy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">22</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">15</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">bảo hiểm xe máy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">53</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">30</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">15</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">5</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">bao hiem xe may</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">54</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">30</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">15</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">5</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">bán bảo hiểm xe máy</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">30</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">20</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">10</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">mua bảo hiểm xe online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">bảo hiểm xe máy online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">33</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">20</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">12</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">bảo hiểm xe bắt buộc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">69</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">40</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">20</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">10</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">mua bh xe máy online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
    </tr>
  </tbody>
</table>

### 6.2 North Star Metric

**Organic-attributed Insurance Purchases từ cluster /bao-hiem-xe-may** = số hợp đồng BH xe máy được attributed từ organic traffic web.

**Funnel:**

```
Organic session → Mua ngay click → App open → Purchase (via Appsflyer)
```

### 6.3 Mandatory Tracking & AB Test Hypothesis (MoSpark Standard)
- **Hypothesis:** Nếu đưa widget "Nhập biển số tra cứu hạn bảo hiểm" lên đầu trang thay vì các banner quảng cáo dài dòng, W2A Conversion sẽ tăng 45% do đánh trúng FOMO bị phạt.
- **Tracking Event Schema:** Bắt buộc track `bhxm_plate_input`, `bhxm_result_view`, `bhxm_buy_click` qua GA4 & Appsflyer.

---

## 7. Dependencies & Constraints

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dependency</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Owner</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Blocker?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Widget tra cứu biển số - API kết nối CSDL BH</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH Product team + BE</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần API để widget /tra-cuu hoạt động thực. Không có API - fallback hướng dẫn tra cứu thủ công</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có - cho /tra-cuu</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dữ liệu phí bảo hiểm chính xác per nhà BH</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH Product team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phí BH bắt buộc = quy định nhà nước. Phí tự nguyện khác nhau per nhà BH - cần data thực</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có - cho /bang-gia</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Deep Link per nhà BH và per phân khối xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">App team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CTA "Mua ngay" cần deep link đúng destination trong App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có - cho landing page nhà BH</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AggregateRating data (rating + số review thực)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH Product team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần số liệu rating thực từ hợp đồng đã mua. Không được dùng rating không có nguồn gốc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có - YMYL + legal</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review / Approve nội dung pháp lý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Legal team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mọi số liệu mức phạt, mức bồi thường, điều kiện bắt buộc phải có legal sign-off</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có - YMYL</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số liệu trust bar (số hợp đồng, đối tác BH)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BH Product team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần xác nhận số liệu chính xác nhất tính đến ngày publish</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không - có thể update sau</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content production</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEO team</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">9 blog posts + 15+ landing pages</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không - team tự build</td>
    </tr>
  </tbody>
</table>

### 7.1 Go-to-Market: SPA Framework (Service Productization)
- **reSearch / Strategy:** Phân tích nhu cầu 67.5K searches/tháng, 7 pillar clusters.
- **Pilot / Plan (T6/2026):** Launch Hub page + PLG Widget (Tra cứu biển số + Tính phí).
- **Action / Amplify (Q3/2026):** Scale pSEO cho các dòng xe máy điện và blog FOMO pháp lý để dominate organic SOV.

### 7.2 Operational Constraints
**Hard Constraints (VP GPD Standard):**
- **Không dùng Geo-URL:** Tuyệt đối KHÔNG tạo trang kiểu `/bao-hiem-xe-may-hcm` (pSEO rác). Quy định giao thông và giá BHXM áp dụng toàn quốc.
- Content pháp lý (mức phạt, điều kiện BH, mức bồi thường) PHẢI qua legal review trước khi publish - không auto-publish
- AggregateRating Schema chỉ được dùng khi có data review thực - không dùng fake rating
- Số liệu Nghị định phải cite đúng số hiệu và năm ban hành
- Widget tra cứu biển số không được lưu trữ biển số sau query - privacy constraint
- Khi có Nghị định mới về mức phạt hoặc phí BH - update content trong vòng 7 ngày

---

## 8. Risk Assessment

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Rủi ro</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khả năng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Impact</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mitigation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content pháp lý lỗi thời sau khi có Nghị định mới - Google penalize hoặc user complaint</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quy trình review định kỳ, alert khi có Nghị định mới, update trong 7 ngày</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">API tra cứu biển số không khả dụng hoặc delay - trang /tra-cuu không có giá trị thực</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Fallback: hướng dẫn 4 cách tra cứu thủ công thay thế. Không block launch trang cha</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rating/Review data không đủ hoặc chất lượng thấp - không implement được AggregateRating Schema đúng chuẩn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gate: chỉ implement schema khi có đủ 10+ reviews thực. Không dùng placeholder</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content production bottleneck - 15+ trang cần viết đồng thời gây delay launch</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phân giai đoạn: 3-4 trang cốt lõi launch trước, phần còn lại follow sau 4-6 tuần</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Keyword "xe máy điện" đang tăng - đối thủ build trang trước MoMo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Speed-to-market: /xe-may-dien là trang ưu tiên đầu tiên</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Deep link per nhà BH chưa sẵn sàng - landing page nhà BH không có CTA đúng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Fallback: CTA link về trang cha trong khi chờ deep link</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog posts YMYL không đạt E-E-A-T - không rank hoặc bị manual action</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Template strict: cite Nghị định, author byline, legal review bắt buộc</td>
    </tr>
  </tbody>
</table>

---

## Change Log

- **Tháng 7/2026 (v1.2):** Cập nhật kế hoạch Media SEO/GEO H1/H2 2026: Media Team tham gia phối hợp tối ưu hóa cùng Midas; cập nhật phương án khôi phục organic traffic sụt giảm; đề xuất 2 phương án đi backlink (Option 1: ngân sách 330 triệu đồng/năm để đạt Top 1-3 cho 4/10 từ khóa, Top 3-5 cho 5/10 từ khóa; Option 2: ngân sách 450 triệu đồng/năm để đạt Top 1-3 cho 5/10 từ khóa, Top 3-5 cho 7/10 từ khóa) bằng Guest Posts (15-20 bài), PR báo tỉnh (20-35 bài) và mua textlink.
- **Tháng 5/2026:** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.
