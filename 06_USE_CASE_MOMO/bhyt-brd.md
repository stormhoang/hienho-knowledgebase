# BRD: Bảo Hiểm Y Tế

> - **Dự án:** BHYT Web Growth - MiniWeb Expansion + Blog Production
> - **URL chính:** momo.vn/bao-hiem-y-te
> - **Khối phụ trách:** FS (Financial Services - InsurTech)
> - **Use Case:** Bảo Hiểm Y Tế
> - **Owner:** Web Platform
> - **Phê duyệt:** Web Product Lead (Hiến)
> - **Phiên bản:** 1.2 - Tháng 7/2026
> - **Trạng thái:** On Track (Updated Media Team Plan)

---

## 1. Executive Summary

### 1.1 Elegant Problem Framing
- **Vấn đề cốt lõi:** Người dân mua/gia hạn BHYT tự nguyện rất cực, phải ra phường hoặc đợi đại lý thu tiền. Các trang web hướng dẫn thì toàn văn bản luật khô khan, không cho phép thanh toán.
- **Giải pháp (The "What"):** Biến MoMo thành "Đại lý BHYT Online quốc dân". Cung cấp công cụ tra cứu số thẻ/ước tính mức đóng và nút thanh toán gia hạn trực tiếp ngay trên trang.

### 1.2 Situation
BHYT là vertical có tổng search market lớn nhất trong các vertical MoMo đang khai thác, với tổng search volume toàn category đạt trung bình ~525K searches/tháng (2024-2025). MoMo đang cung cấp dịch vụ mua và gia hạn BHYT tự nguyện online tại `momo.vn/bao-hiem-y-te`. Trang hiện tại có công cụ tra cứu, đóng phí 3-6-12 tháng.

### Complication

Hiệu suất organic hiện tại còn rất thấp so với tiềm năng thị trường. Traffic từ tháng 8/2025 chỉ ở mức ~10K views/tháng. Dự báo không can thiệp chỉ đạt ~72K views tổng cả năm 2026 - không tương xứng với thị trường 525K+ searches/tháng. Nguyên nhân cốt lõi:

1. MiniWeb thiếu các trang phủ intent cao nhất: tra cứu số thẻ bằng CCCD (~18,100/tháng), tra cứu mã số (~12,100/tháng), tra cứu thời hạn (~25,000/tháng) - đây là các cluster user đang tìm kiếm nhiều nhất nhưng MoMo không có trang đích.
2. Blog content chưa đủ volume để bao phủ market pool (hiện 14 bài vs thị trường ~525K searches).
3. Tracking organic vs paid chưa sạch nên không đo được hiệu quả thực sự.

### Resolution

Dự án 2026 triển khai 2 workstream song song: (1) MiniWeb Expansion - build 3 trang utility mới phủ intent tra cứu cao nhất, và (2) Blog Production Scale-Up - từ 14 bài lên 60-150 bài/năm để phủ 20-40% market pool.

- **Base case target:** 120,662 views toàn năm 2026 (tăng ~52% vs trajectory không can thiệp)
- **Best case target:** 452,294 views (nếu scale blog lên 120-150 bài/năm kèm backlink)

---

## 2. Bối Cảnh Thị Trường

### 2.1 Hiện Trạng Trang `momo.vn/bao-hiem-y-te`

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Yếu tố</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hiện trạng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chức năng trang</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu BHYT + Mua/gia hạn BHYT tự nguyện online</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đối tác</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo hiểm PVI (được BHXH VN ủy quyền thu)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thời hạn mua</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3 tháng / 6 tháng / 12 tháng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Điểm mạnh UX</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">93% khách nhận thẻ trong 4 ngày; xử lý hồ sơ online 5 phút</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~10,477 views/tháng (tháng 8/2025)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog hiện có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">14 bài published</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang utility bị thiếu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu bằng CCCD, tra cứu mã số, tra cứu thời hạn</td>
    </tr>
  </tbody>
</table>

### 2.2 Market Size & Search Demand

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Keyword đại diện</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Avg. Monthly Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu BHYT (core)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra cứu bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~90,500</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo hiểm y tế (brand)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~110,000</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu bằng CCCD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra cứu BHYT bằng CCCD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~33,100</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu thời hạn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra cứu thời hạn BHYT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~22,200</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu số thẻ bằng CMND</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra số thẻ BHYT bằng CMND</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~18,100</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua BHYT online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">mua bảo hiểm y tế online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~12,100</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu mã số</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra cứu mã số BHYT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~12,100</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gia hạn online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">gia hạn BHYT online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~5,400</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giá BHYT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">giá bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~5,400</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Clusters nhỏ hơn (50+ keywords)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">chi trả, trái tuyến, học sinh, hộ gia đình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~50,000+ tổng</td>
    </tr>
  </tbody>
</table>

**Tổng thị trường (2025):** ~525,260 searches/tháng

**Trend:** Tăng trưởng ~3.1x từ 2022 (~168K/tháng) lên 2025 (~525K/tháng). Các keyword mới xuất hiện sau 2024 liên quan CCCD và Luật BHYT mới (Nghị định 188, Thông tư 20, Luật 2025) đang tăng tốc.

**Seasonality:** Đỉnh tháng 8-9 (năm học mới, học sinh sinh viên), đỉnh tháng 12 (gia hạn cuối năm), spike tháng 7/2025 liên quan thông tuyến.

### 2.3 Competitive Landscape

Các đối thủ chính trên SERP: baohiemxahoi.gov.vn, vneid.gov.vn, VSSID app, các site tin tức/giải thích BHYT. MoMo có lợi thế unique là điểm đến transaction trực tiếp (mua được ngay) nhưng yếu ở content informational - là nơi user bắt đầu hành trình tìm kiếm.

---

## 3. Định Hướng Dự Án

### 3.1 Dự Án Này Phục Vụ Điều Gì?

Tăng organic traffic vào `momo.vn/bao-hiem-y-te` và blog BHYT, từ đó drive Web-to-App conversion (user mua/gia hạn BHYT trên MoMo). Mục tiêu trung hạn: MoMo trở thành điểm đến số 1 khi người Việt search bất kỳ thông tin gì về BHYT - từ tra cứu, tìm hiểu chính sách đến mua/gia hạn.

**Đối tượng phục vụ:**
- Người lao động tự do, freelancer chưa có BHYT hoặc cần gia hạn định kỳ (3-6 tháng)
- Người con mua BHYT cho cha/mẹ ở quê qua MoMo
- Học sinh/sinh viên cần tra cứu BHYT
- Người muốn tra cứu thông tin thẻ BHYT (số thẻ, mã số, thời hạn) bằng CCCD/CMND

### 3.2 Dự Án Này KHÔNG Phải

- Không build BHYT bắt buộc (đây là sản phẩm của BHXH, không phải MoMo)
- Không xây dựng tính năng mobile app
- Không cover BHYT thương mại (BH sức khỏe tư nhân)

---

## 4. JTBD Analysis

### 4.1 Keyword Clusters & Intent Map

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">JTBD</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster Keywords</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Volume đại diện</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Intent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">J1: Tra cứu thông tin thẻ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra cứu BHYT, tra cứu bằng CCCD, tra mã số, tra thời hạn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~170,000+/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Know - Go</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">J2: Hiểu chi phí / giá BHYT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">giá BHYT, BHYT bao nhiêu tiền, mức đóng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~25,000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Know - Buy</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">J3: Mua / Gia hạn online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">mua BHYT online, gia hạn BHYT online, đóng BHYT online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~25,000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Buy</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">J4: Hiểu quyền lợi & chính sách</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BHYT chi trả như thế nào, trái tuyến, 5 năm liên tục</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~15,000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Know</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">J5: Tìm kiếm cho nhóm đặc thù</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BHYT học sinh, hộ gia đình, cho cha mẹ, trẻ em</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~15,000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Know - Buy</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">J6: Tra cứu pháp lý & luật mới</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Luật BHYT 2025, Nghị định 188, thông tuyến trung ương</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~10,000/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Know</td>
    </tr>
  </tbody>
</table>

### 4.2 JTBD Priority Reasoning

**Cao nhất - J3 + J1:** Mua/Gia hạn Online và Tra cứu thông tin thẻ là lõi của MiniWeb Expansion. User đang trong hành trình sử dụng BHYT, MoMo intercept và convert sang giao dịch gia hạn. Đây là workstream có conversion path rõ ràng nhất.

**Trung bình - J2 + J4:** Chi phí và Quyền lợi phục vụ nhóm user đang cân nhắc. Blog content phủ rộng các cluster này, nuture user về sau. Quan trọng cho E-E-A-T và authority.

**Bổ trợ - J5 + J6:** Nhóm đặc thù và pháp lý. Conversion thấp hơn nhưng cần thiết để phủ toàn bộ funnel và xây dựng trust signal YMYL.

### 4.3 User Journey

**Flow 1 - Tra cứu để mua:**
User search "tra cứu BHYT bằng CCCD" ➔ Trang utility MoMo (Live API) ➔ Tra cứu được thông tin thẻ ➔ CTA "Gia hạn BHYT tại đây" ➔ Conversion mua/gia hạn.

**Flow 2 - Mua trực tiếp:**
User search "mua BHYT online 2026" ➔ Landing page momo.vn/bao-hiem-y-te ➔ Thấy form tra cứu + mua ➔ Conversion.

**Flow 3 - Informational sang transactional:**
User search "BHYT chi trả bao nhiêu phần trăm" ➔ Blog MoMo ➔ Đọc bài viết ➔ Thấy CTA mua BHYT ➔ Awareness ➔ Intent ➔ Conversion sau đó.

---

## 5. Kiến Trúc Web

### 5.1 Sitemap Hub & Spoke

```
momo.vn/bao-hiem-y-te [Hub - Transaction + Utility]
│
├── TRANG UTILITY (MiniWeb Expansion)
│   ├── /bao-hiem-y-te/tra-cuu-so-the-bhyt    - Tra cứu bằng CCCD (~18K+ vol/tháng)
│   ├── /bao-hiem-y-te/tra-cuu-ma-so-bhyt     - Tra cứu mã số (~12K+ vol/tháng)
│   ├── /bao-hiem-y-te/thoi-han-mua-bhyt      - Tra cứu thời hạn (~25K+ vol/tháng)
│   └── **PLG Interactive Tool:** /bao-hiem-y-te/tinh-phi-bhyt - Công cụ ước tính phí BHYT Hộ gia đình (Nhập số người → Ra giá tiền cần đóng, pass "Bữa tối test").
│
├── TRANG THÔNG TIN (Giai đoạn tiếp theo)
│   └── /bao-hiem-y-te/benh-vien              - Top list bệnh viện ~500 tuyến tỉnh (pSEO)
│
└── BLOG CLUSTER (/bao-hiem-y-te/blog/)
    ├── Chi trả BHYT theo thủ thuật/xét nghiệm
    ├── Tra cứu hướng dẫn (CCCD, CMND, online)
    ├── Mua BHYT cho nhóm đặc thù (cha mẹ, HSSV, trẻ em)
    ├── Quyền lợi & chính sách (trái tuyến, 5 năm liên tục)
    └── Luật & pháp lý (Luật BHYT 2025, Nghị định 188)
```

### 5.2 Content Architecture - Schema & AEO

**Schema bắt buộc:** FAQPage - HowTo - Product - BreadcrumbList trên trang cha và trang utility.

**AEO/GEO Standard (VP GPD):** Triển khai file `llms.txt` tại `momo.vn/bao-hiem-y-te/llms.txt` chứa dữ liệu sạch về luật và mức đóng. Bắt buộc để chiếm vị trí trích dẫn số 1 (Source of Truth) trên Perplexity, ChatGPT và Google AI Overviews.

### 5.3 Content Strategy - YMYL Standards

BHYT là YMYL (Your Money or Your Life). Google yêu cầu E-E-A-T cao. Toàn bộ nội dung bắt buộc phải có thông tin kiểm duyệt (Author/Reviewer Profile từ PVI hoặc chuyên gia luật) và trích dẫn trực tiếp nguồn chính phủ.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Topic Cluster</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Keywords</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Estimated Volume</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">YMYL & Compliance Rule</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chi trả BHYT theo thủ thuật</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">chụp CT/MRI/nội soi có BHYT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~10,000+/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trích dẫn danh mục chi trả của Bộ Y Tế</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu hướng dẫn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">cách tra cứu BHYT, BHYT bằng CCCD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~8,000+/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dùng screenshot UI/UX thực tế từ App/Web MoMo</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua BHYT cho nhóm đặc thù</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">cha mẹ, người nghỉ việc, bà bầu, trẻ em</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~15,000+/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trích dẫn định nghĩa nhóm đối tượng theo Luật BHYT</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quyền lợi & chính sách</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BHYT chi trả %, 5 năm liên tục, trái tuyến</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~15,000+/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Legal review bắt buộc trước khi publish</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Luật & pháp lý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Luật BHYT 2025, Nghị định 188, thông tuyến</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~10,000+/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Link-out bắt buộc tới chinhphu.vn hoặc thuvienphapluat</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giá & chi phí</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BHYT bao nhiêu tiền, bảng giá 2025-2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~15,000+/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">So sánh rõ ràng mức phí giữa HSSV và Hộ gia đình</td>
    </tr>
  </tbody>
</table>

---

## 6. Success Metrics

### 6.1 KPI Framework

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Baseline (Aug 2025)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Base Case Target (EOY 2026)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Best Case Target (EOY 2026)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Monthly Web Views (organic)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~10,477</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~16,064/tháng (Dec 2026)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Scale tuyến tính với blog volume</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Total Views 2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">-</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">120,662</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">452,294</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MiniWeb utility pages live</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">0</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3 trang</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3 trang + bệnh viện pSEO</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog articles published</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">14 bài</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">60 bài</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">120-150 bài</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Keyword coverage Top 10 GSC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang đo baseline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">+50 keywords mới Top 10</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">+150 keywords mới Top 10</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">W2A Conversion Rate</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang đo baseline</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có baseline xác định</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tối ưu từ baseline</td>
    </tr>
  </tbody>
</table>

**Rationale:** Base Case (+52% vs no-action trajectory) đạt được thông qua MiniWeb Expansion + 60 bài blog/năm. Best Case yêu cầu scale blog lên 120-150 bài/năm kèm backlink.

### 6.2 North Star Metric

**Organic Sessions từ cluster /bao-hiem-y-te** được attributed về transaction (mua/gia hạn BHYT).

**Funnel:**
```
Organic session ➔ Tra cứu/đọc blog ➔ Gia hạn / Mua ngay click ➔ App open ➔ Purchase
```

### 6.3 Mandatory Tracking & AB Test Hypothesis (MoSpark Standard)
- **Hypothesis:** Nếu đưa widget "Công cụ ước tính phí BHYT Hộ gia đình" lên màn hình đầu tiên (First fold), tỷ lệ W2A sẽ tăng 50% so với việc bắt user đọc một bài text về luật BHYT dài 2000 chữ.
- **Tracking Event Schema:** Gắn sự kiện `bhyt_calc_submit`, `bhyt_lookup_result`, `bhyt_gia_han_click` trên GA4 & Appsflyer.

---

## 7. Dependencies & Constraints

### 7.1 Go-to-Market: SPA Framework (Service Productization)
- **reSearch / Strategy:** Phân tích nhu cầu 525K searches/tháng, intent tra cứu thời hạn/CCCD là cao nhất.
- **Pilot / Plan (T6/2026):** Triển khai 3 trang Utility tra cứu + Công cụ tính phí BHYT hộ gia đình trên hạ tầng web hiện tại.
- **Action / Amplify (Q3/2026):** Scale blog lên 60-150 bài để thống trị organic SOV.

### 7.2 Operational Constraints

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dependency</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Blocker?</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MiniWeb 3 trang utility</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Build trang tra cứu CCCD, mã số, thời hạn - cần API từ BHXH VN hoặc PVI</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">API đã live, đang build UI</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">API tra cứu BHYT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">API để trang utility hoạt động thực tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Live</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog Production capacity</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5-15 bài/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang vận hành</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog Plan 2026 chi tiết</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Keyword plan và content calendar cho blog cluster</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang cập nhật</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 + GSC tracking sạch</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phân tách organic vs paid traffic trước khi đo KPI</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang chuẩn hóa</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Appsflyer W2A tracking</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Track conversion từ web sang app cho BHYT flow</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang đo baseline</td>
    </tr>
  </tbody>
</table>

**Hard Constraints (VP GPD Standard):**
- **Không dùng Geo-URL:** Tuyệt đối KHÔNG tạo các trang kiểu `/bao-hiem-y-te-ha-noi` hay `/bao-hiem-y-te-tphcm`. BHYT là chính sách quốc gia dùng chung 1 bảng giá trị, việc tạo pSEO theo tỉnh thành là tạo duplicate content rác.
- Trang phải comply với quy định bảo mật thông tin BHXH - user input CCCD/CMND phải xử lý đúng luật
- Content BHYT thuộc YMYL - cần review chính sách, không được thông tin sai về quyền lợi pháp lý
- Đối tác thu hộ hiện tại là PVI - mọi claim về dịch vụ phải align với scope PVI được ủy quyền
- Content về quyền lợi, mức đóng, chi trả bắt buộc có legal sign-off trước khi publish

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog production không đủ volume ➔ không đạt target</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content calendar rõ ràng, vendor đang vận hành</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MiniWeb utility không có API ➔ 3 trang quan trọng không launch được</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rất cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">API đã live; nếu unstable, làm trang hướng dẫn tĩnh làm fallback</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tracking organic vs paid chưa sạch ➔ KPI không đo được chính xác</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ưu tiên phân tách GA4 source/medium trước khi launch</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Gov site, news site outrank do domain authority cao hơn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Focus keyword long-tail trước, tích lũy content volume và backlink</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search intent shift sau khi Luật BHYT mới hiệu lực (thông tuyến)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đã xảy ra</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Refresh keyword research định kỳ; ưu tiên content về thông tuyến và chính sách mới</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">R6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content sai thông tin pháp lý ➔ vi phạm YMYL, Google penalty</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Rất cao</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Legal review bắt buộc cho mọi content về quyền lợi, mức đóng, chi trả</td>
    </tr>
  </tbody>
</table>

---

## Appendix A: Top 15 Keywords Theo Volume

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Keyword</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Avg. Monthly Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">110,000</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra cứu bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">90,500</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra cứu bảo hiểm y tế bằng cccd</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">33,100</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra cứu thời hạn bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">22,200</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra số thẻ bảo hiểm y tế bằng cmnd</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">18,100</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">14,800</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">mua bảo hiểm y tế online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">12,100</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra cứu mã số bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">12,100</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">kiểm tra bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">9,900</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">mua bảo hiểm y tế ở đâu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8,100</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">mua bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6,600</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">mã thẻ bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6,600</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">gia hạn bảo hiểm y tế online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5,400</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">giá bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5,400</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">tra mã bảo hiểm y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5,400</td>
    </tr>
  </tbody>
</table>

**Tổng thị trường addressable (sau khi loại keyword gov-only):** Ước tính 60-70% total, ~315-370K/tháng.

---

## Change Log

- **Tháng 7/2026 (v1.2):** Cập nhật định hướng kế hoạch Media SEO/GEO H1/H2 2026: Media Team tham gia phối hợp tối ưu hóa cùng Midas; cập nhật lộ trình MiniWeb Expansion chia làm 2 giai đoạn (Phase 1: tích hợp tra cứu CCCD, mã số BHYT, thời hạn đóng; Phase 2: xây dựng danh bạ 500 bệnh viện); thiết lập quy mô 60-150 blog/năm đạt KPI traffic Base Case (120k views) / Best Case (452k views) và ngân sách đi link (backlink budget) 300 triệu - 500 triệu đồng/năm.
- **Tháng 5/2026 (v1.1):** Cập nhật trạng thái API Tra cứu BHYT thành Live. Bổ sung tiêu chuẩn E-E-A-T (YMYL), chiến thuật AEO (llms.txt), và cập nhật cấu trúc Hub & Spoke.
