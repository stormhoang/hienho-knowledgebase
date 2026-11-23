# BÁO CÁO TÓM TẮT ĐỊNH HƯỚNG DỰ ÁN: VEHICLE HUB (WEB PLATFORM)

> **Mục đích:** Báo cáo tóm tắt tổng thể chiến lược định hướng, quy hoạch sitemap, mục tiêu KPI và khung triển khai phối hợp giữa **Khối Web Platform** và các Cell Teams (**VTTI & Insurtech**) xây dựng hệ sinh thái **Vehicle Hub - Tiện Ích Giao Thông** trên Kênh Web MoMo.

---

## I. BỐI CẢNH & TẦM NHÌN CHIẾN LƯỢC

### 1. Vấn Đề Cốt Lõi
Hàng triệu chủ xe ô tô và xe máy tại Việt Nam đang bị phân mảnh thông tin, phải chuyển qua lại giữa nhiều website rời rạc để tra cứu phạt nguội, theo dõi hạn đăng kiểm, tìm cây xăng, trạm sạc, cứu hộ và mua bảo hiểm. Nếu chỉ tập trung dịch vụ trong ứng dụng di động (In-App), MoMo sẽ lãng phí hơn **12.6 triệu lượt tìm kiếm tự nhiên/tháng** ngoài Open Web.

### 2. Tầm Nhìn & Phễu Tăng Trưởng (Product-Led Growth Funnel)
Vehicle Hub trên Web đóng vai trò là kênh thu hút người dùng có nhu cầu chủ động ngoài Open Web, sau đó điều hướng trải nghiệm và giữ chân người dùng trong hệ sinh thái MoMo theo phễu 4 bước:

$$Search Demand (Google/AI)\longrightarrow Web Utility Page\longrightarrow Vehicle Hub In-App\longrightarrow Add Vehicle Profile / Transaction$

* **Kênh Web (Web Platform):** Thu hút Organic Traffic quy mô lớn, tạo điểm chạm đầu tiên và thu thập Biển số xe (Thẻ Xe Số Level 1).
* **In-App Vehicle Hub (VTTI):** Điểm đến trung tâm lưu trữ và tự động hóa quản lý phương tiện (Vehicle Profile Level 2).
* **Lớp Sản Phẩm Thương Mại (Insurtech & VTTI):** Tạo chuyển đổi doanh thu trực tiếp (Bảo hiểm Ô tô/Xe máy, Phí không dừng ePass/VETC, Phí nộp phạt DVC, Cứu hộ...).

---

## II. MỤC TIÊU KINH DOANH & BẢNG CHỈ TIÊU KPI

### 1. Bảng Chỉ Tiêu Proposal Của Mini App Vehicle Hub (Target Đến 31/12/2026)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KPI</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Target đề xuất (tính đến 31/12/2026)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Saved Vehicle User (Level 1)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có biển số xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>100.000 xe</strong> (bao gồm ô tô và xe máy)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Saved Vehicle User (Level 2)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có biển số, OCR cà vẹt xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>140.000 xe</strong> (bao gồm ô tô và xe máy)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Saved Vehicle User (Level 3) - ô tô</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có đầy đủ data xe (OCR cà vẹt, đăng kiểm)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>20.000 xe</strong> (bao gồm ô tô và xe máy)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Vehicle Hub 90-day Active Rate</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% user có xe quay lại/có hành động trong 90 ngày</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>20%</strong></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Service attach rate/vehicle</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trung bình số service active trên mỗi xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>1,2 service/xe</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trigger-to-action rate</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhắc hạn/phạt/ETC  ➔  user xử lý</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>15%</strong></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Data reuse rate</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">% flow được auto-fill từ Vehicle Profile</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>≥ 40% eligible sessions</strong></td>
    </tr>
  </tbody>
</table>

---

### 2. Bảng Bóc Tách Monthly Run-Rate Phase 1 Pilot (Tháng 9 - Tháng 12/2026)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tầng Đo Lường</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chỉ Số KPI Cốt Lõi</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Tháng 9/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Tháng 10/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Tháng 11/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Tháng 12/2026</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Target End Phase 1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Kênh Web</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Total Traffic</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>75,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>110,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>140,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>175,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>500,000</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>%CTR</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>0.30%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>0.40%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>0.50%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>0.55%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>0.50%</strong></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Kênh App</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>MAU</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>35,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>55,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>70,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>90,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>250,000</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>New Vehicle Profiles</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>15,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>22,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>28,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>35,000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>100,000</strong></td>
    </tr>
  </tbody>
</table>

---

## III. QUY HOẠCH SITEMAP VÀ CẤU TRÚC URL DỰ ÁN

Hệ sinh thái Kênh Web được chia làm **2 Nhóm Cấu Trúc Rõ Ràng**:

### Nhóm A: Trang Chủ & Các Spoke Pages Trực Thuộc Hub (`/tien-ich-giao-thong/*`)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">STT</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Trang</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Canonical</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Volume Search/Tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai Trò & Mô Tả Chức Năng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trang Chủ Vehicle Hub</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Master Hub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cổng định danh Thẻ Xe Số, tích hợp tra phạt nguội & điều hướng 360°</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Giá Xăng Dầu</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/gia-xang</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>10.100.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cập nhật giá xăng Petrolimex/PVOil, biến động giá chiều Thứ 5</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trạm Sạc Xe Điện</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/tram-sac</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>1.200.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ vị trí trạm sạc VinFast, V-Green toàn quốc</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cây Xăng Gần Đây</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/cay-xang</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>550.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ vị trí cây xăng Petrolimex/PVOil kết nối phễu thanh toán M4B</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Garage Sửa Xe & Bảo Dưỡng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/garage</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>272.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Danh sách garage, trung tâm chăm sóc ô tô uy tín theo địa phương</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đăng Kiểm Xe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/dang-kiem</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>180.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu hạn đăng kiểm, lịch hẹn trung tâm kiểm định</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hãng Xe & Dòng Xe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/hang-xe</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>150.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thông số kỹ thuật, giá niêm yết và chi phí lăn bánh ô tô</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bãi Đỗ Xe & Giữ Xe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/bai-do-xe</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>85.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bản đồ điểm trông giữ xe ô tô / xe máy</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">9</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cứu Hộ Đường Bộ 24/7</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/cuu-ho</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>45.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổng đài cứu hộ ô tô, cẩu xe, kích bình ắc quy khẩn cấp</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">10</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Định Giá Xe Cũ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/dinh-gia-xe</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>14.500</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Công cụ định giá xe ô tô/xe máy cũ, phễu Vay & Bảo hiểm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">11</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Blog Tiện Ích Giao Thông</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tien-ich-giao-thong/blog</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Long-tail SEO</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bài viết tư vấn luật giao thông, mẹo bảo dưỡng và kinh nghiệm lái xe</td>
    </tr>
  </tbody>
</table>

### Nhóm B: 4 Trang Use Case Độc Lập (Top-Level Standalone Canonical Pages)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">STT</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Use Case Standalone</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Canonical</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Volume Search/Tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai Trò & Điểm Khác Biệt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tra Cứu Phạt Nguội</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/phat-nguoi</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>6.100.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility độc lập Top 1 Google, tra cứu 0-CAPTCHA real-time</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bảo Hiểm Ô Tô</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-o-to</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>450.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang bán hàng độc lập cho Bảo hiểm TNDS & Thân vỏ ô tô</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bảo Hiểm Xe Máy</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/bao-hiem-xe-may</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>680.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang bán hàng độc lập cho Bảo hiểm TNDS xe máy online</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phí Không Dừng (ETC)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/phi-khong-dung</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;"><strong>320.000</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang tiện ích nạp tiền & kiểm tra số dư tài khoản ePass / VETC</td>
    </tr>
  </tbody>
</table>

---

## IV. KHUNG TRIỂN KHAI PHASE 1: BUILD FOUNDATION (THÁNG 8 - 9/2026)

Song song với kế hoạch go-live Tiện ích Giao thông In-App, 3 Cell Teams (**Web Platform, VTTI & Insurtech**) thống nhất tập trung toàn bộ nguồn lực Phase 1 vào **"Build Foundation"** với 3 Trụ cột cốt lõi:

```
                     ┌───────────────────────────────────────────────┐
                     │     PHASE 1: BUILD FOUNDATION (T8 - T9/2026)  │
                     └───────────────────────┬───────────────────────┘
                                             │
      ┌──────────────────────────────────────┼──────────────────────────────────────┐
      ▼                                      ▼                                      ▼
┌───────────────────────────┐  ┌───────────────────────────┐  ┌───────────────────────────┐
│ TRỤ CỘT 1: MOSPARK & GENAI│  │ TRỤ CỘT 2: MASTER HUB PAGE│  │ TRỤ CỘT 3: CORE PILLARS   │
│ Migration Bảo Hiểm Ô Tô/XM│  │ Landing /tien-ich-giao-thong│  │ Chuyên Trang Giá Xăng Dầu │
│ Kích hoạt GenAI Engine    │  │ Tích hợp Tra Phạt Nguội & │  │ Bản Đồ Cây Xăng Gần Đây   │
│ Phủ Keyword Thương Mại    │  │ Xoay quanh Biển Số Xe     │  │ (10.6M Search Volume)     │
└───────────────────────────┘  └───────────────────────────┘  └───────────────────────────┘
```

### 1. Trụ Cột 1: Chuyển Dịch Bảo Hiểm Ô Tô / Xe Máy Sang MoSpark & Kích Hoạt GenAI Engine
* Move 100% hệ thống trang Bảo hiểm Ô tô (`/bao-hiem-o-to`) và Bảo hiểm Xe máy (`/bao-hiem-xe-may`) sang hạ tầng **MoSpark**.
* Kích hoạt **GenAI Content Engine (MoSpark CMS + Claude 3.5)** để tự động sản xuất bài viết pSEO/AIO chuyên sâu, phủ các trang đối tác `/bao-hiem-o-to/doi-tac/{ten-doi-tac}` và bài viết chuẩn SEO/GEO.
* Nâng cao tốc độ nạp trang (<1.5s), chuẩn hóa Schema structured data và tích hợp luồng **Auto-fill dữ liệu từ Vehicle Profile** để tối ưu hóa tỷ lệ chuyển đổi mua bảo hiểm.

### 2. Trụ Cột 2: Master Landing Page `/tien-ich-giao-thong` Tích Hợp Phạt Nguội & Hiển Thị Xoay Quanh Biển Số Xe
* Phát triển Master Landing Page `/tien-ich-giao-thong` làm cổng điều hướng trung tâm.
* Tích hợp công cụ **Tra Cứu Phạt Nguội 0-CAPTCHA** trực tiếp tại Hero Section làm ô nhập liệu chính.
* Xây dựng giao diện **Hiển thị Tiện ích Phương tiện Xoay Quanh Biển Số Xe (Vehicle-Centric Service Promotion / Thẻ Xe Số)**: Ngay sau khi nhập Biển số xe, hệ thống vừa trả ra kết quả phạt nguội, vừa tự động hiển thị trạng thái các dịch vụ xung quanh xe (Bảo hiểm, Hạn đăng kiểm, Định giá xe, Số dư ETC) nhằm thúc đẩy người dùng mở App MoMo để **Thêm phương tiện (Add Vehicle Profile)**.

### 3. Trụ Cột 3: Xây Dựng Các Trang Traffic Pillar Cốt Lõi Chi Cụm Quanh Master Hub
* **Chuyên trang Giá Xăng Dầu (`/tien-ich-giao-thong/gia-xang`):** Hứng **10.1M search/tháng**, tạo thói quen quay lại định kỳ mỗi chiều Thứ 5 hàng tuần.
* **Local GEO Cây Xăng Gần Đây (`/tien-ich-giao-thong/cay-xang`):** Hứng **550K search/tháng**, kết nối trực tiếp phễu O2O quét mã thanh toán Petrolimex/PVOil qua MoMo.

---

## V. MÔ HÌNH PHỐI HỢP GIỮA CÁC CELL TEAMS

Dự án được vận hành theo mô hình phối hợp 3 bên chặt chẽ:

### 1. Business Owners (Cell Teams VTTI & Insurtech)
* **Business Ownership:** Nắm giữ quyền quyết định và chịu trách nhiệm toàn trình đối với kết quả kinh doanh (Doanh thu Bảo hiểm, GTV nạp ePass, Phí dịch vụ nộp phạt DVC, Số lượng đơn hàng).
* **Domain Strategy:** Hoạch định chiến lược kinh doanh dịch vụ giao thông & bảo hiểm, quản lý đối tác (PVI, Bảo Việt, MIC, ePass, VETC, Petrolimex, VinFast) và cung cấp Deeplink W2A tự động truyền tham số Biển số xe.

### 2. Web Platform (Product & Tech Partner)
* **Product & Growth Ownership:** Sở hữu, định hướng và vận hành Kênh Web (`/tien-ich-giao-thong`), Tỷ lệ Chuyển đổi (CR), Hạ tầng Kỹ thuật (MoSpark) và Tăng trưởng Organic Traffic.
* **Trọng tâm thực thi:**
  * **Product-Led Growth (PLG):** Xây dựng luồng Web-to-Vehicle-to-App (W2V2A) biến Traffic tự nhiên ngoài Open Web thành tệp Hồ sơ xe định danh.
  * **MoSpark Infrastructure Migration:** Chuyển đổi hệ thống Web sang MoSpark để chịu tải lớn và nâng cao tốc độ ra mắt tính năng.
  * **GenAI Automation Engine:** Ứng dụng AI tự động hóa sản xuất và tối ưu hóa nội dung pSEO/AIO theo Content Plan.
