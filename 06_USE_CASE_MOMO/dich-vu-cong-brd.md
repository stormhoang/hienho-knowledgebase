# BRD: Dịch Vụ Công MoMo

> - **Dự án:** Dịch Vụ Công MoMo (DVC) - Governance Hub
> - **URL chính:** `momo.vn/dich-vu-cong` (Governance Hub) + kênh Web chiến lược (Phạt Nguội, ePass)
> - **Phiên bản:** 2.5 · Tháng 5/2026
> - **Trạng thái:** **DVC Chung:** (Info hub - đề án Bộ Công An) | **Phạt Nguội:** (BRD riêng, Phase 1 LIVE) | **ePass:** (Build Foundation)

---

> **Problem:** Hàng triệu người search thủ tục hành chính, phạt nguội, BHXH mỗi ngày - không fintech nào đang serve intent này trên web. MoMo xử lý 11.2% giao dịch DVCQG nhưng không có một trang web nào giúp user biết điều đó, biết thủ tục cần làm, hay dẫn họ vào App để thanh toán.
> **KPI Owned:** MEU Utility (Web) + MAU % New to services (App)
> **Conversion Flow:** Search "thủ tục [X]" / "phạt nguội" → `/dich-vu-cong/{service}` → Hướng dẫn + CTA → App open → Nộp phí/đóng phạt → Transaction

---

## 1. Executive Summary

### Situation

User cần làm thủ tục hành chính, tra phạt nguội, gia hạn BHYT - họ search Google đầu tiên. Experience hiện tại: tìm thấy VNExpress, Luatvietnam, blog cá nhân - không có fintech nào. MoMo đang xử lý 11.2% giao dịch trên Cổng DVCQG (~1.46M giao dịch/năm) nhưng không có một trang web nào giúp user biết MoMo hỗ trợ gì, biết thủ tục cần làm, hay dẫn họ vào App để thanh toán.

### Complication

Không có touchpoint web = không có acquisition funnel cho segment có purchase intent cao nhất. User đã quyết định nộp phí/phạt, đang search để biết cách - nhưng MoMo không xuất hiện. Với ~5M searches/tháng trên toàn cluster DVC, đây là kênh acquisition organic lớn nhất chưa được khai thác trong toàn bộ portfolio GPD. Mỗi lượt search bị bỏ lỡ là một user không biết MoMo hỗ trợ, một giao dịch không xảy ra trên MoMo.

### Resolution

`momo.vn/dich-vu-cong` là **Governance Hub** - điểm vào duy nhất cho toàn bộ DVC trên web. Product job: user search thủ tục hành chính, phạt nguội, gia hạn BHXH → tìm thấy MoMo → nhận hướng dẫn đủ để hành động → mở App → hoàn thành giao dịch. 3 kênh web chiến lược:

1. **Governance Hub** (`/dich-vu-cong`) - Thông tin & hướng dẫn DVC; align đề án Bộ Công An
2. **Phạt Nguội** (`/phat-nguoi`) - Utility tra cứu; quản lý độc lập tại BRD riêng
3. **ePass/ETC** - Build Foundation; lane Payment (xem Section 1.2)

**North Star:** **MEU Utility (Web)** + **MAU % New to services (App)**. Organic sessions & W2A là Tier B (leading/operational).

### 1.1 BU Portfolio - 8 dịch vụ

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dịch vụ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai trò MoMo</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Web priority</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Metro</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cân nhắc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Resources & strategy</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cổng DVC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Info / hướng dẫn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Chiến lược</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đề án Bộ Công An - đang triển khai</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bus (vé buýt công cộng)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cân nhắc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cân nhắc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BHXH</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cân nhắc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Overlap với BHYT</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giáo dục</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cân nhắc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">7</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dịch vụ Y tế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cân nhắc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ePass/ETC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Payment Gateway</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Chiến lược</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Section 1.2 - tách lane Payment</td>
    </tr>
  </tbody>
</table>

*Các sản phẩm ngoài 3 kênh chiến lược đang cân nhắc vì resources & strategy.*

### 1.2 ePass / ETC (Governance Strategic)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giai đoạn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô hình</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Before</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nạp qua provider ETC</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>After</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ePass liên kết Payment Gateway (MoMo) - 1 User ↔ 1 Payment Gateway</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phase Web</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Governance Strategic → Build Foundation (education/foundation; full payment flow trên Web khi BU chốt)</td>
    </tr>
  </tbody>
</table>

- **Lane đo lường:** Payment (MAU, % New to services) - khác Utility/Info của Cổng DVC.
- BRD chi tiết ePass: TBD (file riêng khi BU kick-off).

---

## 2. Bối Cảnh Thị Trường

### 2.1. Thị trường Dịch Vụ Công Số Việt Nam

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giá trị</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nguồn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổng giao dịch DVCQG (10 tháng 2025)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">15,725,239</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cổng DVCQG Overview</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổng giá trị giao dịch</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~10.4 nghìn tỷ VNĐ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cổng DVCQG Overview</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Số loại TTHC thanh toán qua Cổng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1,900+</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cổng DVCQG Overview</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo tổng giao dịch</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~1,462,714 (11.2% share)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tính từ Chi tiết TTHC</td>
    </tr>
  </tbody>
</table>

### 2.2. Competitive Landscape - Đơn vị thanh toán trên DVCQG

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Đơn vị</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vị thế</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">VNPT Pay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#1 volume</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chiếm ưu thế ở TTHC chứng thực, hộ tịch</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NAPAS</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#2 volume</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mạnh ở đất đai, doanh nghiệp</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>MoMo</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>#3 volume (~11.2%)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dẫn đầu ở Xét tuyển ĐH (39%), Đổi GPLX (25%)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AgriBank</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mạnh ở vùng nông thôn, đất đai</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ViettelPay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">#5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phủ rộng nhưng share thấp</td>
    </tr>
  </tbody>
</table>

**Gap chính:** Không đối thủ fintech nào có chiến lược web DVC nghiêm túc. VNExpress, Luatvietnam, blog cá nhân đang chiếm toàn bộ SERP - đây là cửa sổ cơ hội.

### 2.3. Search Market (Cập nhật T5/2026)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Volume/tháng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phạt Nguội</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~2,536,090</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cluster lớn nhất - quản lý tại BRD Phạt Nguội</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phương Tiện (Giao thông)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~510,910</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tra cứu biển số xe, đăng ký xe</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đổi GPLX</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~230,810</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thủ tục đổi bằng lái, gia hạn bằng lái</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hộ chiếu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~222,610</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Làm hộ chiếu online, gia hạn hộ chiếu</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tạm trú</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~154,540</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đăng ký tạm trú online</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CCCD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~145,690</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đổi CCCD online, cấp lại CCCD bị mất</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thủ tục hành chính (general)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~102,640</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dịch vụ công online</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đăng ký kết hôn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~89,420</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thủ tục đăng ký kết hôn online</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đăng kiểm xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~76,870</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thủ tục đăng kiểm online</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Các cluster khác</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~500,000+</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuế, khai sinh, định danh, chứng thực...</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tổng addressable</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>~5,000,000+</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nguồn: Ahrefs T5/2026</td>
    </tr>
  </tbody>
</table>

---

## 3. Định Hướng Dự Án

### 3.1 Product Job Cốt Lõi

User search thủ tục hành chính hoặc phạt nguội - tìm thấy MoMo - nhận đủ thông tin để hành động (checklist, hướng dẫn, deadline) - mở App để hoàn thành giao dịch. Không cần content dài. Không cần đọc nhiều. Product drives the funnel từ search intent đến in-app transaction.

3 outcome phát sinh:

**Acquisition:** MoMo xuất hiện trong SERP khi user có purchase intent cao nhất - cần nộp phí, đóng phạt, gia hạn. Organic traffic là kênh acquisition có cost thấp nhất và intent cao nhất trong DVC vertical.

**Education & Trust:** User biết MoMo hỗ trợ DVC trước khi ra quyết định. Web là touchpoint duy nhất capture được user chưa cài app - không có web, không có education, không có acquisition.

**MEU Foundation:** Governance Hub + Phạt Nguội Tool build MEU Utility baseline - chứng minh web DVC có business value trước khi commit mở rộng toàn bộ portfolio.

### Dự án này KHÔNG phải

- Không build app features mới - Web landing & content; App do Product Owner/Mobile team own
- Không thay thế Cổng DVCQG - không xử lý hồ sơ TTHC trên Web
- Không cam kết full payment journey trên Web cho Cổng DVC - CTA/policy TBD (Define sau với BU)
- Không cover toàn bộ 1,900+ TTHC - focus top demand + 3 kênh Web chiến lược

### 3.2 KPI Framework

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lane</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ý nghĩa</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">KPI cam kết</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ví dụ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Utility</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tương tác công cụ / tra cứu / info</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>MEU</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phạt nguội lookup, widget tra cứu</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Payment</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giao dịch / nạp / thanh toán</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>MAU + % New to services</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ePass PG, nộp phạt in-app</td>
    </tr>
  </tbody>
</table>

**Chiến lược triển khai:** Kế thừa pilot Phạt Nguội (test → amplify). Không all-in DVC content trước Pilot review T6/2026. Roadmap điều chỉnh theo kết quả pilot.

---

## 4. Search Intent & URL Strategy

### 4.1 Head Terms (Volume 500K+/tháng)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Keyword</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Volume</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Intent</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">dịch vụ công online</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">60,000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Keywords Phạt Nguội</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~2,536,090</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TOFU/MOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chi tiết tại BRD Phạt Nguội</td>
    </tr>
  </tbody>
</table>

### 4.2 High-Volume Clusters Chiến Lược (50K-500K/tháng)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Volume</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Intent</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đổi GPLX</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">230,810</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong/doi-bang-lai-xe</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hộ chiếu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">222,610</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong/ho-chieu</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tạm trú</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">154,540</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong/tam-tru</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CCCD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">145,690</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong/gia-han-cccd</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đăng ký kết hôn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">89,420</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong/ket-hon</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đăng kiểm xe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">76,870</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong/dang-kiem</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quyết toán thuế</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">50,570</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong/nop-thue</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khai sinh</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">44,490</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong/khai-sinh</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Định danh điện tử</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">29,170</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong/vneid-la-gi</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chứng thực</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">27,670</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BOFU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">/dich-vu-cong/chung-thuc</td>
    </tr>
  </tbody>
</table>

---

## 5. JTBD Analysis

### Job #1: Tra cứu & Xử lý Vi phạm Giao thông (Phạt Nguội)

> Nhu cầu tra cứu vi phạm giao thông và nộp phạt trực tuyến nhanh chóng, bảo mật.
>
> *Job này được phân tích chi tiết tại BRD Phạt Nguội.*

### Job #2: Hoàn thành Thủ tục Hành chính Online

> "Tôi cần biết thủ tục [X] cần những gì, nộp ở đâu, mất bao lâu - và nộp phí/lệ phí online cho nhanh."

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Biết checklist giấy tờ, quy trình từng bước, nơi nộp hồ sơ, thời gian xử lý, cách nộp phí online</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sợ thiếu giấy tờ phải đi lại nhiều lần, muốn tiết kiệm thời gian</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thủ tục cho sự kiện cuộc đời quan trọng (sinh con, kết hôn, mua nhà) - áp lực phải làm đúng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Con mới sinh cần khai sinh, bằng lái sắp hết hạn, CCCD hết hạn/bị mất, sắp kết hôn</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"thủ tục đổi GPLX" → Service page → Checklist → CTA nộp phí → App MoMo</td>
    </tr>
  </tbody>
</table>

### Job #3: Quản lý Nghĩa vụ Tài chính Cá nhân (Thuế, BHXH)

> "Tôi cần biết deadline, cách tính, và nộp thuế/BHXH online - không muốn bị phạt chậm nộp."

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tính thuế phải nộp, biết deadline, nộp tiền online, gia hạn BHYT</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sợ bị phạt chậm nộp, bối rối với quy định phức tạp</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nghĩa vụ pháp lý - không thể trì hoãn</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mùa quyết toán thuế (T3-T4), BHYT sắp hết hạn, nhận thông báo thuế</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"nộp thuế TNCN online" → Calculator → CTA nộp → App MoMo</td>
    </tr>
  </tbody>
</table>

### Job #4: Khám phá Toàn bộ DVC MoMo Hỗ trợ

> "MoMo làm được những dịch vụ công gì? Tôi muốn biết để dùng luôn thay vì ra UBND."

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tìm toàn bộ DVC MoMo hỗ trợ</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Emotional</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tò mò, muốn tiết kiệm thời gian, trust vào Super App quen thuộc</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trigger</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lần đầu biết MoMo có DVC, đang cần 1 DVC cụ thể và muốn xem có gì thêm</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search → App</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub /dich-vu-cong → Browse → Click service cần → App MoMo</td>
    </tr>
  </tbody>
</table>

---

## 6. Kiến Trúc Web

### 6.1. URL Architecture

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cluster</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Core Hubs</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Governance Hub</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/thu-tuc-hanh-chinh</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TTHC Hub</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phạt Nguội</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/phat-nguoi</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tool & Landing Page chính (BRD riêng)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Giấy tờ tùy thân</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/gia-han-cccd</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CCCD</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/ho-chieu</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hộ chiếu</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cư trú</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/tam-tru</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tạm trú</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/tam-vang</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tạm vắng</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hộ tịch</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/ket-hon</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đăng ký kết hôn</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/khai-sinh</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đăng ký khai sinh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Giấy tờ xe</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/doi-bang-lai-xe</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đổi GPLX</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Thuế</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/nop-thue</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thuế TNCN / Quyết toán</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Chứng thực</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/chung-thuc</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chứng thực / Sao y</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Kinh doanh</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/dang-ky-kinh-doanh</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hộ kinh doanh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đất đai</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/dat-dai</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sang tên, chuyển nhượng</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Knowledge Base</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/faq</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">FAQ Schema Hub</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/vneid-la-gi</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Định danh điện tử / VNeID</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>AEO/GEO Standard</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/dich-vu-cong/llms.txt</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tệp chuẩn hóa AI Indexing (Bắt buộc theo chuẩn VP GPD)</td>
    </tr>
  </tbody>
</table>

### 6.2. Governance Hub Anatomy (`/dich-vu-cong`)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Section</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thành phần</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hero</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Search bar auto-suggest + "Mọi dịch vụ công trong 1 ứng dụng" + trust counter</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LCP < 2.5s</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Quick Actions</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6 icon dịch vụ phổ biến nhất (Phạt nguội, Đổi bằng lái, CCCD, Thuế, BHXH, Khai sinh)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Personalize nếu logged in</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>PLG Interactive Tool</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Smart DVC Checklist Generator:</strong> Trả lời 3 câu hỏi nhanh (Loại dịch vụ, Tỉnh thành, Tình trạng) → Render ra ngay Checklist chuẩn bị hồ sơ 100% chính xác.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tạo "Aha Moment" (Utility-First của A.Công) & Passed "Tiêu chuẩn trải nghiệm đột phá" (của A.Tường)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Service Grid</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Map 8 dịch vụ BU: 3 kênh chiến lược nổi bật + các mảng cân nhắc</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Schema: Service + ItemList</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">App CTA</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sticky bottom banner + QR + deep link</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Firebase Dynamic Links</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Blog Preview</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3 bài mới nhất</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NewsArticle Schema</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Social Proof</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Counter lượt dùng + Rating App Store</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AggregateRating Schema</td>
    </tr>
  </tbody>
</table>

---

## 7. Success Metrics

**North Star:** **MEU Utility (Web)** + **MAU % New to services (App)** - hai metric này cam kết với BU + Web Platform. Organic sessions & W2A là Tier B (leading indicators).

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Lane</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Target</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tracking</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MEU Utility</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD post Pilot T6/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">DA + Appsflyer</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MAU % New to services</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Payment</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TBD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BU internal / Onelink</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic sessions EOY</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier B</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">500K/tháng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GSC → GA4</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Top 5 keywords DVC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier B</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">20 keywords</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ahrefs</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">W2A end-to-end</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tier B</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">15%</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GA4 + Appsflyer</td>
    </tr>
  </tbody>
</table>

### 7.1. Mandatory Tracking & AB Test Hypothesis (MoSpark Standard)
*Để đảm bảo quá trình xét duyệt và deploy trên MoSpark diễn ra nhanh chóng (Align với nền tảng User Growth):*
- **Hypothesis (Giả thuyết test):** Nếu đưa "Smart DVC Checklist Generator" (Interactive Tool) lên vị trí First Fold (thay vì bài viết Text), W2A Conversion Rate sẽ tăng ít nhất 30% so với trang thuần Text.
- **Tracking Event Schema:** Mọi lượt tương tác với Checklist (Click chọn dịch vụ, View kết quả) đều phải được gán event trên GA4 & Appsflyer để đo lường Funnel Drop-off.

---

## 8. Dependencies & Constraints

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform (MoSpark)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Build & deploy toàn bộ web pages</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">READY (v2 Live)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">GenAI Content Engine</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hệ thống sản xuất blog</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LIVE (Claude API)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Widget tra cứu phạt nguội</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">API tra cứu biển số (TTDK integration)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LIVE (BRD Phạt Nguội)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Analytics Stack</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Real-time traffic & attribution</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">LIVE (Umami + GA4)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Onelink/Appsflyer setup</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Config deeplink cho từng DVC page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ACTIVE</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEM Campaign</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">SEM cho Phạt Nguội</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">RUNNING</td>
    </tr>
  </tbody>
</table>

**Hard blockers (3):** Web Platform, Widget tra cứu, Onelink setup. Thiếu 1 trong 3 - không launch được.

### 8.1. Service Readiness (T5/2026)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Dịch vụ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Status</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phạt Nguội</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>LIVE</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Triển khai độc lập (BRD riêng)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Thủ tục Hành chính (TTHC)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>IN PROGRESS</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đang scale content</td>
    </tr>
  </tbody>
</table>

### 8.2. Go-to-Market: SPA Framework (Service Productization)
*Theo chỉ đạo "Đóng gói giải pháp Web" của VP GPD:*
1. **reSearch / Strategy (Hoàn thành):** Đã phân tích Demand (~5M searches) & Market Gap (Chưa có Fintech nào phủ).
2. **Pilot / Plan (Hiện tại):** Dùng **Phạt Nguội** làm Pilot Case Study. Triển khai Mini Web MVP trên MoSpark + GenAI Pipeline.
3. **Action / Amplifier (Next step T6/2026):** Sau khi Pilot Phạt Nguội chứng minh MEU/MAU thành công ➔ Pitch BU DVC để xin ngân sách Scale toàn bộ 1900+ TTHC.

---

## Appendix: Glossary

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thuật ngữ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định nghĩa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">DVC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dịch vụ công</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">DVCQG</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cổng Dịch vụ công Quốc gia (dichvucong.gov.vn)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">TTHC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thủ tục hành chính</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NĐ 168</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nghị định 168/2024/NĐ-CP về xử phạt vi phạm giao thông</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">W2A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web-to-App (conversion từ web visitor sang app user)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MEU</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Monthly Engagement User - tương tác Utility; metric commit Web Utility</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility lane</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đo bằng MEU - engagement công cụ/info</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Payment lane</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đo bằng MAU, % New to services - giao dịch in-app</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Governance Hub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang trung tâm tập hợp & điều hướng portfolio DVC</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">ePass</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trạm thu phí - liên kết Payment Gateway MoMo (1 User ↔ 1 PG)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">YMYL</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Your Money Your Life - tiêu chuẩn Google cho content tài chính/pháp luật</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoSpark</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web platform nội bộ MoMo</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">VNeID</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ứng dụng định danh điện tử quốc gia</td>
    </tr>
  </tbody>
</table>

---

## Change Log

- **Tháng 5/2026 (v2.5):** Xóa BHYT và BHXH khỏi Search Market, URL Architecture, Service Readiness - đã có BRD riêng (bhyt-brd.md, bhxm-brd.md).
- **Tháng 5/2026 (v2.4):** Rewrite theo chuẩn BRD - xóa Risk Assessment, Content Matrix, Appendix Cross-sell, Data Verification; trim keyword detail về Tier 1+2 only; thêm Problem Statement block + Product Job Cốt Lõi; rewrite Executive Summary theo Problem Framing.
- **Tháng 5/2026 (v2.3):** Chuẩn hóa tài liệu - loại bỏ liên kết nội bộ, thông tin vận hành, tên nhân sự.
- **Tháng 5/2026 (v2.2):** Portfolio 8 dịch vụ BU; 3 kênh Web chiến lược; ePass Build Foundation; KPI Utility (MEU) vs Payment (MAU).
- **Tháng 5/2026 (v2.1):** Tách biệt Phạt Nguội sang BRD riêng.
- **Tháng 5/2026:** Khởi tạo tài liệu.
