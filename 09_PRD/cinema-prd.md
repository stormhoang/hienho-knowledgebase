# Product Requirements Document (PRD): Web Cinema H2/2026

*Lưu ý: Tài liệu này được tách ra từ BRD để làm input chi tiết cho quá trình xây dựng Product Backlog và Sprint Planning của team Web Platform.*

---

## 1. Product Context & Guardrails

### 1.1 Product Job Cốt Lõi (JTBD)

User tìm phim đang chiếu hoặc lịch chiếu theo rạp - tìm thấy thông tin realtime chính xác trên momo.vn - mua vé ngay trong 1 flow mà không cần rời trang tìm kiếm.

**PLG Hook:** Booking flow là PLG hook tự nhiên - user đến với commercial intent cao, product chỉ cần serve đúng intent thì tự convert, không cần campaign hay push. "Nhắc tôi khi mở bán" (Phase 1) là PLG hook bổ sung tạo repeat engagement khi phim chưa ra rạp.

3 kết quả kinh doanh đạt được khi Product Job được giải quyết tốt:
- **Doanh thu Giao dịch (Transaction revenue):** Hoa hồng từ vé bán ra - Mục tiêu kinh doanh cốt lõi của dự án.
- **Độ phủ Thị phần Tìm kiếm (Market Share):** Bao phủ toàn bộ các từ khóa tìm kiếm về rạp và lịch chiếu tại từng địa phương.
- **Bảo vệ Vị thế Dài hạn:** Chuẩn hóa cấu trúc dữ liệu để luôn xuất hiện nổi bật khi người dùng sử dụng AI Overview của Google để tìm kiếm phim.

### 1.2 Dự Án Này KHÔNG Phải (Anti-Goals)

- Không build mobile app - scope của Mobile/MDS team
- Không xây platform streaming hay video-on-demand
- Không bao gồm SEO cho MoMo blog general - chỉ `/cinema/*`
- Không cover performance marketing hay paid media
- Không bao gồm backend partner API negotiation

**Target user:**
- User đi xem phim cuối tuần (18-35, đô thị, mobile payment habit) - search "lịch chiếu + rạp", "phim đang chiếu"
- User discover phim - search "top phim hay", "review phim"
- User lookup thông tin rạp cụ thể - search "CGV Aeon Canary lịch chiếu"

---

## 2. Dữ liệu Vận hành & Phân tích Hiện trạng

### 2.1 Dữ liệu Lịch sử Vận hành & Thanh toán

**A. Chỉ số Người dùng Web in App (MAU & MEU)**
*Ghi chú: MEU đo lường số lượng User có hành vi click từ trang Web dẫn sâu sang In-App hoặc quét QR thanh toán.*
- MAU Web in App dao động mạnh theo mùa vụ (Tết, Hè), chạm mốc kỷ lục 16.5K (2025).
- MEU duy trì gấp 2-3 lần MAU, cho thấy hành vi chuyển đổi deep-link diễn ra liên tục.

**B. Chỉ số Giao dịch Cổng Thanh Toán (Payment Gateway)**
- PG Web/App Đối tác: H1/2026 chạm mức cao nhất ~303K giao dịch/tháng.
- PG Offline tại quầy: H1/2026 trung bình ~3.7K/tháng (tăng so với 2025).

### 2.2 Keyword Ranking Hiện Tại

**Gap lớn nhất:** "Phim chiếu rạp" (102,820/tháng), "Rạp chiếu phim" (74,000/tháng), "Galaxy Cinema" (100,030/tháng) - tổng ~280K/tháng ngoài Top 50. Đây là discovery queries có volume cao nhất thị trường chưa được capture.

### 2.3 Cảnh báo Rủi ro SEO & Bảo mật Nội dung (SEO Spam Attack Warning)

> [!CAUTION]
> **Phát hiện lỗ hổng SEO Spam nghiêm trọng trong dữ liệu GSC:**
> Lượng search query chứa các từ khóa nhạy cảm người lớn lọt vào Top 3 lượng clicks của mục Cinema, đổ bộ trực tiếp vào 3 bài viết blog informational.
> **Rủi ro:** Google Penalty/Sandbox.
> **Giải pháp:** Rà soát mã độc cloaking, noindex/cleanup các trang blog vệ tinh nhiễm bẩn.

---

## 3. Chiến Lược Triển Khai (Roadmap)

### Giai đoạn 1 - Q3/2026 (Tháng 7 → 9): Nền tảng & Quick Win

Ưu tiên tuyệt đối là làm nền tảng kỹ thuật để hệ thống có thể scale.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Việc cần làm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trụ cột</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Triển khai luồng thanh toán trực tiếp trên Web</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Payment Flow</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">W2A CR phục hồi về ≥ 4.5%</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Triển khai URL Lifecycle System (nightly cron)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic + Ranking</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phase 1→4 tự động theo lịch chiếu</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Deploy Schema Movie + ScreeningEvent đầy đủ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Authority + Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AIO eligibility, rich result</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xây dựng Film Series Hub pages (10+ franchise lớn)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic + Ranking</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Capture Series cluster, cross-link Film pages</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuẩn hóa CTA "Đặt vé ngay" sticky</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Payment Flow</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tăng booking click rate</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xử lý SEO Spam: noindex / cleanup 3 blog</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Authority</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo vệ domain trust</td>
    </tr>
  </tbody>
</table>

### Giai đoạn 2 - Q4/2026 (Tháng 10 → 12): Scale & Authority

Sau khi nền tảng ổn định, tập trung mở rộng content và mở luồng OTT để bứt tốc cuối năm.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Việc cần làm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trụ cột</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">OTT Flow: tích hợp CTA mua gói OTT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic + Payment</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Revenue OTT bổ sung; giữ link equity phim hết rạp</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xây top-phim/{topic-slug} evergreen pages</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Authority + Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ranking cho genre queries volume lớn</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Scale Film Series Hub lên 50+ franchise</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic + Ranking</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Long-tail Series cluster phủ rộng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog /cinema/blog/ depth content theo thể loại</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Authority</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hạ tầng content cho AIO & long-tail</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review system: rating phim từ user</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Authority</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tăng trust signal, UGC content</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQPage schema per series + film</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Authority</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xuất hiện trong AIO Q&A format</td>
    </tr>
  </tbody>
</table>

---

## 4. Đề xuất Tăng trưởng & Sáng kiến (Growth Backlog)

### 4.1 Tăng Organic Traffic
1. **Chiến dịch Off-page SEO & Link Building:** Ngân sách 600 triệu VNĐ từ BU Movies. Đi bài PR báo chí, booking Social/KOL trỏ backlink.
2. **Trang "Phim chiếu hôm nay tại [Thành phố]":** Capture search demand theo địa điểm.
3. **Trang Actor & Director Hub:** Capture từ khóa tên đạo diễn, diễn viên. (Lưu ý từ PO: Được phép dùng GenAI tổng hợp tiểu sử, nhưng BẮT BUỘC có dòng disclaimer "thông tin tổng hợp có thể sai sót" & ghi rõ nguồn. Danh sách phim tham gia sẽ lấy từ API TMDb hoặc tự crawl).
4. **Cluster "Phim sắp chiếu [Năm]":** Giữ traffic dài và chuyển sang Phase 2 khi phim mở bán.
5. **Mở rộng Blog theo hướng "Xem ở đâu":** Kéo traffic từ user đã bỏ lỡ phim rạp sang OTT.

### 4.2 Tăng W2A Conversion Rate
1. **Mở App đúng màn hình đặt vé:** Thay vì mở màn hình chủ, giảm friction rớt phễu 20-30%.
2. **Trải nghiệm cho user chưa cài App:** Giữ nguyên ngữ cảnh (phim + rạp) sau khi cài App thành công.
3. **Social proof trên trang lịch chiếu:** Hiển thị "X người đã đặt vé suất này" tạo FOMO.

### 4.3 Tăng Transactions & Tickets Sold
1. **Thanh toán Trực tiếp trên Web (Guest Checkout):** Hỗ trợ QR đa năng và Ví MoMo để khách hàng Non-App có thể mua.
2. **"Nhắc tôi khi mở bán":** Thông báo khi phim chuyển Phase 2.
3. **Hiển thị ưu đãi combo (Vé + Bắp nước):** Tăng AOV.
4. **OTT Upsell:** Chuyển traffic phim Phase 3-4 sang giao dịch mua gói OTT.
5. **Gợi ý phim tương tự đang chiếu:** Giữ khách hàng trong phễu mua vé khi họ xem nhầm phim hết rạp.

### 4.4 Data & Tracking (Cập nhật từ PO)
- **Dữ liệu Doanh thu & Market Share:** Có thể sync trực tiếp dữ liệu doanh thu và tính toán thị phần (Market Share) từ hệ thống dữ liệu nội bộ (sắp ra mắt).

## 5. JTBD Analysis (Detailed)

### Job #1: Transact - "Tôi cần đặt vé ngay"

> "Khi tôi đã chọn được phim + rạp + suất chiếu, tôi cần mua vé nhanh gọn với giá tốt nhất có thể."

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xem lịch chiếu theo rạp/ngày, chọn suất, thanh toán trong 1 flow</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không mất thời gian, không lo hết chỗ đẹp, an tâm về giá</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Anh đặt vé CGV tối thứ 7 rồi, em chọn ghế đi" - chủ động với bạn bè/gia đình</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cuối tuần, bộ phim vừa ra, thấy trailer hot trên social</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"lịch chiếu phim CGV hôm nay" → /cinema/rap/cgv/{slug} → "Đặt vé ngay" (sticky deeplink) → App MoMo → Transaction confirmed</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** /cinema/lich-chieu, /cinema/rap/{chain}/{theater-slug}, /cinema/{movie-slug} Phase 2 (Showing). CTA "Đặt vé ngay" sticky dẫn vào luồng Thanh toán Web.

---

### Job #2: Plan - "Tôi muốn tìm phim hay để xem"

> "Khi tôi rảnh và muốn có gợi ý, tôi cần xem top phim hay đang chiếu và review đáng tin."

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xem list phim theo thể loại, đọc review, xem điểm rating</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tự tin chọn đúng phim hay, không phí 2 tiếng cuộc đời</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trở thành người "biết tuốt" về phim ảnh để gợi ý cho group bạn</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tối rảnh rỗi, cần giải trí</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"top phim kinh dị hay nhất" → /cinema/blog/{slug} → Click link phim → /cinema/{movie-slug} Phase 2 → Đặt vé</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** /cinema/blog/*, /cinema/{movie-slug} Phase 1 (Sắp chiếu) & Phase 2 (Đang chiếu). Review system + FAQ Schema.

---

### Job #3: Navigate - "Tôi cần thông tin về rạp cụ thể"

> "Tôi thường xem ở rạp gần nhà, tôi chỉ muốn biết rạp đó hôm nay chiếu gì, giá vé ra sao."

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xem địa chỉ, bảng giá vé, tiện ích, và lịch chiếu của 1 rạp duy nhất</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">An tâm không đi nhầm rạp, tính toán được chi phí</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">N/A</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đã chốt địa điểm gặp mặt (VD: Đi ăn ở Aeon Mall)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"giá vé cgv aeon canary" → /cinema/rap/cgv/{theater-slug} → Chọn suất → Đặt vé</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** /cinema/rap/{chain}/{theater-slug}. Thông tin bảng giá, map, tiện ích + Lịch chiếu rạp đó.

---

### Job #4: Archive - "Tôi muốn xem lại phim cũ / tìm phim đã hết rạp"

> "Phim này ngày xưa hot lắm, giờ muốn xem lại thì xem ở đâu?"

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đọc lại thông tin phim cũ, tìm link xem trên OTT</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hoài niệm, thỏa mãn trí tò mài</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chia sẻ link phim cho bạn bè</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nghe nhạc phim, thấy ảnh chế meme trên mạng</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"mắt biếc" → /cinema/{movie-slug} Phase 3 (Archive) → Click OTT Link → Mua gói Galaxy Play qua MoMo</td>
    </tr>
  </tbody>
</table>

**Giải pháp:** /cinema/{movie-slug} Phase 3 (Archive) & Phase 4 (TV Series). Tích hợp affiliate link OTT.

---

## 6. Trải Nghiệm Khách Hàng (Customer Experience)

### 6.1 Cấu trúc Hệ Sinh Thái Nội Dung (Site Structure)

#### A. Cấu trúc Hiện tại (H1/2026)
- **/cinema/lich-chieu:** Trang chủ tổng hợp lịch chiếu.
- **/cinema/phim-dang-chieu, /cinema/phim-sap-chieu:** Danh sách phim theo trạng thái.
- **/cinema/rap:** Danh sách cụm rạp.
- **/cinema/{movie-slug}:** Trang chi tiết phim (chỉ có phim rạp).
- **/cinema/rap/{chain-slug}:** Trang chuỗi rạp (VD: CGV).
- **/cinema/rap/{chain-slug}/{theater-slug}:** Trang rạp cụ thể.
- **/cinema/blog:** Bài viết tin tức/review.

#### B. Cấu trúc Đề xuất (H2/2026)
- Bổ sung **/cinema/phim-bo/{series-slug}:** Hub chuyên biệt cho Phim Bộ (TV Series).
- Bổ sung **/cinema/nguoi-noi-tieng/{actor-slug}:** (Growth Sáng kiến) Hub tổng hợp phim theo diễn viên/đạo diễn.
- Chuyển đổi **/cinema/{movie-slug}** thành mô hình Lifecycle (có thể phục vụ cả phim đã hết rạp).

### 6.2 Quản Lý Vòng Đời Phim Tự Động

**Yêu cầu:** Triển khai Cronjob (Chạy ngầm hàng đêm) để tự động cập nhật trạng thái phim trên toàn bộ hệ thống Web dựa vào dữ liệu API từ hệ thống CMS lõi.
- Chuyển tự động từ "Sắp chiếu" ➔ "Đang chiếu" dựa vào .
- Chuyển tự động từ "Đang chiếu" ➔ "Ngừng chiếu" khi  trong 7 ngày liên tiếp.

### 6.3 Phạm vi Tính năng (Functional Scope)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Feature / Page</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phase 1 (Sắp chiếu)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phase 2 (Đang chiếu)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phase 3 (Hết rạp/Archive)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phase 4 (TV Series)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Lịch chiếu</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không hiển thị</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hiển thị đầy đủ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không hiển thị</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không hiển thị</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nút Hành động (CTA)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Nhắc tôi khi mở bán"</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>"Đặt vé ngay"</strong> (sticky)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Xem trên [OTT]" (nếu có)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Xem trên [OTT]"</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Schema Markup</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Movie</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Movie + ScreeningEvent</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Movie</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TVSeries</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nội dung chính</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trailer, Nội dung, Diễn viên</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lịch chiếu, Review, Giá vé</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Review, Info, Nền tảng OTT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Danh sách tập, Nền tảng OTT</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Khối Gợi ý</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phim sắp chiếu khác</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phim đang chiếu cùng thể loại</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phim đang chiếu cùng thể loại</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phim bộ cùng thể loại</td>
    </tr>
  </tbody>
</table>

### 6.4 Mở Rộng Thị Trường Phim Bộ (TV Series)

#### Mục tiêu
Capture lượng search traffic khổng lồ của các TV Series đình đám (VD: *Queen of Tears*, *Squid Game*).

#### Nguồn dữ liệu & Tích hợp
- Nguồn data chính: **TMDb (The Movie Database) API** (Do data CMS nội bộ không có dữ liệu phim bộ).
- Web Platform xây dựng service tự động fetch metadata (Poster, Synopsis, Cast, Episodes) từ TMDb dựa trên IMDB ID.

#### Kết nối Đối tác OTT tại Việt Nam
- Ánh xạ dữ liệu TMDb (API có trả Provider) với các nền tảng OTT hợp pháp tại VN (Netflix, FPT Play, Galaxy Play, VieON).
- **Policy & Hạn chế (Theo confirm từ PO):**
  - **Trên Web Platform:** Được phép gắn link promote/affiliate cho các nền tảng OTT. Nếu đối tác có tích hợp thanh toán MoMo thì đẩy thẳng vào luồng mua gói.
  - **Trên Mini App:** KHÔNG được phép promote các nền tảng OTT. (Tính năng này hoàn toàn dành riêng cho Web để capture traffic).

#### Trải nghiệm Khách hàng trên Trang Phim Bộ
- Tối ưu hóa SEO cho từ khóa: .
- Hiển thị widget: "Phim này đang chiếu trên [Logo OTT]".

#### Yêu cầu Phối hợp (Dependencies)
- BU Movies cung cấp danh sách Top 50 TV Series cần ưu tiên làm nội dung trong Q3/2026.
- Team Content tối ưu hóa tay (manual optimization) nội dung (Review/Tóm tắt) cho Top 50 này sau khi Web đã auto-generate sườn bài bằng GenAI.
