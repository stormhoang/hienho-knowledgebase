# MoSpark - A/B Testing & Personalization Engine
Nền tảng thử nghiệm A/B và cá nhân hóa nội dung động

> - **Project Name:** MoSpark Growth Platform - Phase 2
> - **Division:** GPD (Growth Platform Division)
> - **Owner:** Bảo
> - **PIC:** Thuận (Tech)
> - **Version:** 1.0 · June 2026

---

## 1. Executive Summary

### 1.1 Bối Cảnh
Hiện tại, MoSpark đã xây dựng thành công lớp **Acquisition** thông qua hệ thống CMS, SEO/GEO Builder và Programmatic SEO. Tuy nhiên, mọi trải nghiệm trên Web (từ Merchant Page đến các Landing Page chiến dịch) đều đang hoạt động theo dạng "One-size-fits-all" (Nội dung tĩnh, giống hệt nhau đối với mọi User).

Điều này hạn chế khả năng tối ưu hóa tỷ lệ chuyển đổi (CR) vì hệ thống không thể tự đánh giá xem thiết kế A hay B sẽ mang lại nhiều Click-to-App (CTA) hơn, hoặc không thể hiển thị ưu đãi cá nhân hóa theo từng nhóm người dùng cụ thể.

### 1.2 Giải Pháp
Bổ sung module **A/B Testing & Personalization Engine** vào lõi của MoSpark.
- **A/B Testing:** Công cụ cho phép Editor/PM triển khai song song nhiều biến thể (Variants) của một trang web (thay đổi Headline, Layout, CTA màu sắc) để đo lường và tự động dồn traffic vào phiên bản chiến thắng (Winning Variant).
- **Personalization:** Phân phối nội dung động (Dynamic Content) dựa trên ngữ cảnh người dùng. Ví dụ: User truy cập từ IP Hà Nội sẽ thấy các "Quán bún chả" thay vì "Cơm tấm", User đã Login MoMo sẽ thấy nút "Thanh toán ngay" thay vì "Đăng ký MoMo".

---

## 2. Nhu Cầu Người Dùng & JTBD

### 2.1 Đối với Growth Manager / PM (Người dùng nội bộ)
* **JTBD:** "Tôi muốn thử nghiệm 2 câu Headline khác nhau cho trang Landing Page Ví Trả Sau để xem câu nào đem lại tỷ lệ mở App cao hơn, mà không cần nhờ Dev deploy lại code."
* **Giải pháp:** Giao diện MoSpark Editor cho phép Duplicate Variant, chỉnh sửa trực quan (Visual Editor) và thiết lập tỷ lệ phân bổ traffic (Split Traffic 50/50).

### 2.2 Đối với End-User (Khách hàng)
* **JTBD:** "Tôi chỉ quan tâm đến các dịch vụ, hàng quán ở khu vực xung quanh tôi. Tôi không muốn đọc những thông tin chung chung không đúng nhu cầu."
* **Giải pháp:** Cung cấp trải nghiệm "Context-aware". Trang web tự nhận dạng vị trí, trạng thái đăng nhập để đưa ra các Recommendation chính xác nhất, rút ngắn hành trình từ Web đến App.

---

## 3. Tính Năng Cốt Lõi

### 3.1 A/B Testing (Split Testing)
1. **Visual Variant Builder:** Cho phép nhân bản (Duplicate) trang hiện tại để tạo Variant B. Editor có thể sửa nội dung Text, thay ảnh KV, đổi màu Nút CTA.
2. **Traffic Allocation:** Cho phép PM tùy chỉnh lượng Traffic đẩy vào mỗi biến thể (VD: 90% Original - 10% Variant B cho mục đích an toàn).
3. **MAB (Multi-Armed Bandit) Auto-Routing:** Tùy chọn nâng cao cho phép hệ thống tự động nhận diện Variant nào đang có CR cao hơn và tự động dồn traffic về Variant đó sau 48h, giúp tối ưu chuyển đổi mà không cần chờ kết thúc test.
4. **Bayesian Statistical Reporting:** Bảng báo cáo chỉ ra độ tin cậy thống kê (Statistical Significance), trả lời rõ ràng Variant B có thực sự tốt hơn Variant A hay không.

### 3.2 Personalization Engine (Dynamic Content)
Hệ thống sử dụng các Rule Engine dựa trên các biến (Variables) thu thập được qua Edge Middleware và Cookies:
1. **Geo-Location Rule:** Phân phối nội dung dựa trên Tỉnh/Thành phố.
   - *Use Case:* Trang "Thổ Địa" tự động hiển thị list nhà hàng gần User nhất.
2. **Identity/Login Rule:** Phân biệt User Anonymous và User đã Login.
   - *Use Case:* Nếu User đã login Web, Sticky CTA sẽ là "Mở App Thanh Toán Ngay". Nếu chưa Login, Sticky CTA là "Tải MoMo".
3. **UTM Context Rule:** Cá nhân hóa dựa trên nguồn Traffic.
   - *Use Case:* User bấm vào quảng cáo Facebook về "Thanh toán Cafe", trang Landing Page sẽ tự động đẩy Block Ưu Đãi Cafe lên đầu thay vì ưu đãi chung.

---

## 4. Kiến Trúc Kỹ Thuật

- **Edge Middleware:** Phân luồng Traffic (Routing) ngay tại tầng Edge (Cloudflare/CDN) để đảm bảo không bị giật/lag (Flicker Effect) khi đổi giao diện Variant. Điều này cực kỳ quan trọng đối với Core Web Vitals (CWV).
- **Identity Resolver:** Giao tiếp với API MoMo ID để kiểm tra trạng thái Token/Cookie mà không làm giảm tốc độ tải trang.
- **Tracking Integration:** Đồng bộ sự kiện Experiment (VD: `View_Variant_A`, `Click_CTA_Variant_A`) trực tiếp về **Umami** và **Appsflyer** để đo lường toàn phễu W2A.

---

## 5. Metrics Đo Lường
- **Testing Velocity:** Số lượng Experiment được tạo ra mỗi tháng trên nền tảng (Target: >20 exp/tháng).
- **Win Rate:** Tỷ lệ số lần thử nghiệm thành công (Tạo ra CR cao hơn bản gốc).
- **Lift in CR:** Phần trăm tăng trưởng Click-to-App trung bình từ các Winning Variants.
- **Personalization Engagement:** Tỷ lệ tương tác (Click-through) trên các Block nội dung cá nhân hóa so với nội dung tĩnh.

---

## 6. Phạm vi Tích hợp (Module Applicability Matrix)

Dự án A/B Testing & Personalization (M10) đóng vai trò là một "Core Engine". Tuy nhiên, cơ chế nội dung động này không được áp dụng tùy tiện trên toàn hệ thống mà bị giới hạn chặt chẽ để bảo vệ nền tảng SEO. Dưới đây là bảng phân bổ:

### 6.1. Chi tiết Ma trận Tích hợp

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Module được Tích hợp</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khả năng A/B Testing</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khả năng Personalization (Cá nhân hóa)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ghi chú & Rào cản (Guardrails)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M1 - Landing Page Builder</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Toàn diện:</strong> Cho phép Duplicate variant, test CTA, Hero Banner, Layout.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cao:</strong> Hỗ trợ thay đổi nội dung trang dựa theo Geo-Location và Login State.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phải tuân thủ Compliance Matrix (Khóa Scheme/TnC). Traffic Split tại Edge Router.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M3 - Ads Manager</strong> (Widget/Banner)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cao:</strong> Test các thông điệp Banner, màu sắc Widget.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tối đa:</strong> Target hiển thị Banner/Widget riêng biệt theo UTM Context hoặc User Cohort.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trải nghiệm Ads phải mượt, không làm rớt LCP.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M9 - PLG Tool Builder</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trung bình:</strong> Chỉ test UI nhập liệu hoặc vị trí đặt Tool trên trang.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trung bình:</strong> Tự động điền tham số mặc định (VD: Tự động chọn "TP.HCM" dựa vào Geo-Location).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không test công thức tính toán/API của Tool để đảm bảo tính chính xác của Data.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M2 - GenAI Content</strong> (Blog SEO)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Rất hạn chế:</strong> Tuyệt đối không test nội dung bài viết. Chốt phương án không test Title/H1 để bảo vệ thứ hạng.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Không áp dụng cho Nội dung:</strong> Bài SEO bắt buộc là trang tĩnh (Static) 100% để Googlebot index chính xác.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em>Ngoại lệ:</em> Có thể áp dụng Personalization cho <strong>các Ad slot nằm bên trong bài viết</strong>, không phải bản thân bài viết.</td>
    </tr>
  </tbody>
</table>

### 6.2. Lộ trình triển khai (Phase Rollout)
Vì việc áp dụng Personalization cho toàn hệ thống đòi hỏi khối lượng xử lý lớn tại Edge Router, hệ thống sẽ được mở khóa theo lộ trình:
- **Phase 1 (MVP):** Áp dụng độc quyền cho **M1 (Landing Page Builder)** để tối ưu tỷ lệ chuyển đổi các chiến dịch ngắn hạn.
- **Phase 2:** Mở rộng cho **M3 (Ads Manager)** để cá nhân hóa phân phối quảng cáo Widget/Banner trên toàn site.
- **Phase 3:** Áp dụng cho **M9 (PLG Tools)**.
