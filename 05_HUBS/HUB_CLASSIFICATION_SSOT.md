# QUY CHUẨN ĐỒNG BỘ PHÂN LOẠI HUBS & PROJECTS TRÊN TOÀN NỀN TẢNG (HUB CLASSIFICATION SSOT)

> **Tài liệu nguồn chuẩn hóa (Single Source of Truth - SSOT)**  
> **Dành cho:** AI Agents, Đội ngũ Kỹ thuật Web Platform và Đội ngũ Phát triển Web Hubs (`react-web-momo`)  
> **Phiên bản:** v2.0 - Cập nhật ngày 14/11/2026  
> **Nguồn dữ liệu gốc:** [`07_REPORTS/data/web_dim_page_url.csv`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/web_dim_page_url.csv) (3.354 rules | 84 projects) và [`07_REPORTS/data/url_project_mapping.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/url_project_mapping.json) (28.270 URLs live, độ phủ 99.94%)

---

## 1. NGUYÊN TẮC KIẾN TRÚC PHÂN TẦNG (2-TIER ARCHITECTURE)

Hệ thống Web Platform quy định rạch ròi 2 tầng danh mục để chấm dứt tình trạng "lạm phát Hub" và làm loãng trọng tâm quản trị:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        TỔNG THỂ NỀN TẢNG WEB PLATFORM (momo.vn)                        │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
           ┌────────────────────────────────┴────────────────────────────────┐
           ▼                                                                 ▼
┌───────────────────────────────────────┐         ┌───────────────────────────────────────┐
│     TẦNG 1: 6 STRATEGIC HUBS          │         │    TẦNG 2: 14 UTILITY & PLATFORM HUBS │
│ (Có Target KPI, Thuộc 4 Zones,        │         │ (Tiện ích giao dịch, Hỗ trợ phễu W2A, │
│  Được xếp hạng Rank 1-6 trên City)    │         │  Không giao Target KPI độc lập)       │
├───────────────────────────────────────┤         ├───────────────────────────────────────┤
│ 1. Cinema Hub (Performance)           │         │ 7.  Travel Hub (OTA, Vé Xe)           │
│ 2. Financial Hub (Transformation)     │         │ 8.  Payment Hub (QR, Cross Border...) │
│ 3. Vehicle Hub (Transformation)       │         │ 9.  Billpay Hub (Điện, Nước, Net...)  │
│ 4. New User Hub (Transformation)      │         │ 10. Telco Hub (Data, Sim, Esim...)    │
│ 5. Insurance Hub (Incubator)          │         │ 11. Game Hub (Game, Nạp thẻ...)       │
│ 6. Student Hub (Incubator)            │         │ 12. Lottery Hub (Vé số, Vietlott)     │
│                                       │         │ 13. Merchant Hub (Đối tác, /page)     │
│                                       │         │ 14. Soundbox Hub (Loa thông báo)      │
│                                       │         │ 15. Download Hub (Trang tải ứng dụng) │
│                                       │         │ 16. Support Hub (Hỏi đáp, TnC, Trust) │
│                                       │         │ 17. Search Hub (Tìm kiếm nội bộ)      │
│                                       │         │ 18. Home MoMo (Trang chủ chính)       │
│                                       │         │ 19. News Hub (Tin tức, Khuyến mãi)    │
│                                       │         │ 20. Blog Hub (Blog bài viết chuyên sâu)│
│                                       │         │ 21. Campaign Hub (Chiến dịch sự kiện) │
│                                       │         │ 22. Donation Hub (Trái tim MoMo, CSR) │
│                                       │         │ 23. Others (Lưu lượng kỹ thuật khác)  │
└───────────────────────────────────────┘         └───────────────────────────────────────┘
```

---

## 2. SÁU ĐIỂM SỬA ĐỔI BẮT BUỘC ĐỐI VỚI BỘ MÃ HUB (`react-web-momo`)

Để triệt tiêu toàn bộ lỗi hiển thị và đồng bộ 100% với Knowledge Base, bộ mã Hubs Dashboard cần áp dụng ngay 6 chuẩn hóa sau:

1. **Tách biệt Download thành dự án và Hub độc lập:**
   - **Quy chuẩn SSOT:** Toàn bộ trang tải ứng dụng (`/download*`, `/tai-app*`) được quy về dự án và Hub riêng mang tên `Download` (`download`), đạt 128.5K PV MTD. `New User Hub` (`new_user`) chuyên trách các chiến dịch thu hút khách hàng mới, liên kết tài khoản ngân hàng, giới thiệu bạn bè, quà tặng onboarding và chiến dịch gamification kích hoạt bạn mới Một Mùa Quýt (`/gioi-thieu-momo*`, `/lienkettaikhoan*`, `/hellomomo*`, `/chaomomo*`, `/chao-ban-moi*`, `/qua-tang-ban-moi*`, `/game/mot-mua-quyt*`), đạt 192.2K PV MTD. Cụm `/game*` được loại khỏi Game Hub để trả về đúng dự án New User.
2. **Chuyển `Cross Border` từ `Travel Hub` sang `Payment Hub`:**
   - **Thực trạng sai lệch:** Hub đang xếp `Cross Border` vào `Travel Hub`.
   - **Quy chuẩn SSOT:** Các trang `/thanh-toan-quoc-te`, `/vi-vu-quoc-te-cung-momo-x-alipay`, thanh toán Napas/Alipay+ là tính năng thanh toán quét mã quốc tế, bản chất nghiệp vụ 100% thuộc `Payment Hub`. `Travel Hub` chỉ quản lý cẩm nang du lịch và đặt vé di chuyển liên tỉnh (`OTA`, `Vé Xe`).
3. **Chuẩn hóa chữ hoa/thường đồng nhất với bảng DIM SSOT:**
   - Tuyệt đối không để tồn tại các biến thể hoa/thường gây phân mảnh dữ liệu thành 2 dòng (dòng lịch sử và dòng tháng chạy).
   - Áp dụng các tên chính thức: `Cây xăng`, `Giá xăng`, `Trạm sạc`, `Dịch vụ liên kết`, `Phạt Nguội`, `Quản Lý Chi Tiêu`, `TnC`, `Trung Tâm Tài Chính`, `Vay Nhanh`.
4. **Bóc tách Cinema Hub thành 6 Sub-projects chi tiết:**
   - Không dùng một nhãn `Cinema` gộp chung 160 rules.
   - Bắt buộc bóc tách chi tiết thành 6 Sub-projects: `Cinema_Cineplex Page` (Rạp chiếu), `Cinema_Page` (Chi tiết phim), `Cinema_Home Page` (Trang chủ), `Cinema_Blog` (Bài viết blog review), `Cinema_News` (Khuyến mãi phim), `Cinema_Landing Page` (Landing page sự kiện).
5. **Thu gọn Home MoMo, tách riêng News Hub và Donation Hub:**
   - **Thực trạng sai lệch:** `Home MoMo` bị gộp quá nhiều mảng không đồng nhất (`Tin Tức`, `Donation`, `Blog`, `Khuyến mãi`, `TnC`, `Trust`...), làm toà nhà Home trên CityScene phình to lên hơn 463K PV và làm loãng số liệu thực chất của trang chủ.
   - **Quy chuẩn SSOT:**
     * `Home MoMo` (`home`): Thu gọn duy nhất về Trang chủ nền tảng (`Home MoMo` - URL `/`), đạt 288.7K PV MTD 13 ngày.
     * `News Hub` (`news`): Tách thành Hub riêng quản lý toàn bộ mảng nội dung truyền thông, tin tức, bài viết biên tập và khuyến mãi (`Tin Tức`, `Khuyến mãi`, `Blog`, `Campaign`), đạt 159.3K PV MTD.
     * `Donation Hub` (`donation`): Tách thành Hub riêng quản lý mảng thiện nguyện xã hội / CSR của MoMo (`Donation` - các trang `/trai-tim-momo*`, `/vi-nhan-ai*`), đạt 6.5K PV MTD.
     * `Support Hub` (`support`): Tiếp nhận các trang `TnC` (Điều khoản điều kiện), `Trust` (Thông báo bảo mật), `Tìm Kiếm` và `Tuyển Dụng` để tập trung thành cổng hỗ trợ người dùng và pháp lý toàn diện (đạt 225.6K PV MTD).
6. **Tách biệt hoàn toàn Soundbox Hub khỏi Merchant Hub:**
   - **Thực trạng sai lệch:** `Merchant Hub` bị gộp cả thiết bị phần cứng Loa thông báo (`Soundbox`), khiến quy mô Merchant bị che lấp bởi 69.5K PV của mảng Loa; đồng thời quy tắc phân loại trước đây bị gán nhầm 127 trang đối tác `/thanh-toan-momo-*` sang Game.
   - **Quy chuẩn SSOT:**
     * `Merchant Hub` (`merchant`): Quản lý toàn bộ hệ sinh thái đối tác doanh nghiệp gồm các trang cha `/doi-tac*`, 173 trang đối tác con thương hiệu dạng `/thanh-toan-momo-*` (Bách Hóa Xanh, Grab, Phúc Long, CGV, Dookki, Uniqlo...) và hệ thống landing page điểm bán `/page*`, đạt 59.4K PV MTD trên 2.950 URLs.
     * `Soundbox Hub` (`soundbox`): Tách thành Hub riêng quản lý toàn bộ thiết bị phần cứng Loa thông báo và các nội dung liên quan (các slug chứa `loa-thong-bao*`, `/loa-momo*`), đạt 69.5K PV MTD (+1208.0% MoM).

---

## 3. BẢNG QUY HOẠCH CHI TIẾT 19 HUBS VÀ 84 PROJECTS (CANONICAL MAPPING)

### Nhóm A: 5 Strategic Hubs Cấp Công Ty (Có Target KPI Tháng)

| Hub ID | Tên Hub Hiển Thị | Phân Loại Zone | Target T11 (PV) | Danh Sách Sub-projects Chuẩn Hóa | Quy Tắc URL Tiêu Biểu |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`cinema`** | Cinema Hub | **Performance** | 1.294.630 | `Cinema_Cineplex Page`<br>`Cinema_Page`<br>`Cinema_Home Page`<br>`Cinema_Blog`<br>`Cinema_News`<br>`Cinema_Landing Page` | `/cinema/rap/*`<br>`/cinema/*`<br>`/cinema`<br>`/cinema/blog/*`<br>`/cinema/khuyen-mai`<br>`/cinema/lp/*` |
| **`financial`** | Financial Hub | **Transformation** | 700.000 | `Vay Nhanh`<br>`Ví Trả Sau`<br>`Điểm Tín Dụng`<br>`Túi Thần Tài`<br>`Trung Tâm Tài Chính`<br>`Mở Thẻ Tín Dụng`<br>`Tiết Kiệm Online`<br>`Chứng Khoán`<br>`Chứng Chỉ Quỹ`<br>`Quản Lý Chi Tiêu`<br>`Mở tài khoản ngân hàng`<br>`Trả Góp Apple`<br>`Thanh Toán Khoản Vay`<br>`Thanh Toán Thẻ Tín Dụng`<br>`Sàn Đầu Tư`<br>`Tiệm Vàng Online`<br>`Tỷ Giá`<br>`Giá Vàng`<br>`Quỹ`<br>`Lãi Suất`<br>`Nhận Tiền Quốc Tế`<br>`Quỹ Nhóm` | `/vay-nhanh*`<br>`/vi-tra-sau*`<br>`/diem-tin-dung*`<br>`/tui-than-tai*`<br>`/trung-tam-tai-chinh*`<br>`/mo-the-tin-dung*`<br>`/tiet-kiem-online*`<br>`/chung-khoan*`<br>`/chung-chi-quy*`<br>`/quan-ly-chi-tieu*`<br>`/tra-gop-apple*`<br>`/gia-vang*`<br>`/ty-gia*` |
| **`vehicle`** | Vehicle Hub | **Transformation** | 100.000 | `Phạt Nguội`<br>`Nộp Phạt CSGT`<br>`Tiện Ích Giao Thông`<br>`Phí Không Dừng`<br>`Bảo Hiểm Ô Tô`<br>`Bảo Hiểm Xe Máy`<br>`Cây xăng`<br>`Giá xăng`<br>`Trạm sạc`<br>`Garage`<br>`Hãng Xe` | `/phat-nguoi*`<br>`/tien-ich-giao-thong/nop-phat-csgt*`<br>`/tien-ich-giao-thong*`<br>`/phi-khong-dung*`<br>`/bao-hiem-o-to*`<br>`/bao-hiem-xe-may*`<br>`/cay-xang*`<br>`/gia-xang*`<br>`/tram-sac*` |
| **`new_user** | New User Hub | **Transformation** | 300.000 | `New User` | `/gioi-thieu-momo*`<br>`/lienkettaikhoan*`<br>`/hellomomo*`<br>`/chaomomo*`<br>`/chao-ban-moi*`<br>`/qua-tang-ban-moi*`<br>`/game/mot-mua-quyt*` |
| **`insurance`** | Insurance Hub | **Incubator** | 50.000 | `Bảo Hiểm Y Tế`<br>`Bảo Hiểm Sức Khỏe`<br>`Bảo Hiểm Xã Hội`<br>`Bảo Hiểm` | `/bao-hiem-y-te*`<br>`/bao-hiem-suc-khoe*`<br>`/bao-hiem-xa-hoi*`<br>`/bao-hiem*` |

---

### Nhóm B: 15 Utility & Platform Hubs (Tiện Ích Giao Dịch & Nền Tảng Dùng Chung)

| Hub ID | Tên Hub Hiển Thị | Vai Trò Nghiệp Vụ | Danh Sách Projects Trực Thuộc | Quy Tắc URL Tiêu Biểu |
| :--- | :--- | :--- | :--- | :--- |
| **`student`** | Student Hub | Cổng thông tin, tiện ích sinh viên & Student Pass | `Student Pass`<br>`Student Hub` | `/sinh-vien*`, `/student*`, `/student-pass*` |
| **`travel`** | Travel Hub | Cẩm nang du lịch & Đặt vé di chuyển | `OTA`<br>`Vé Xe` | `/ve-may-bay*`, `/khach-san*`<br>`/ve-xe*`, `/ve-xe-khach*`, `/ve-tau*` |
| **`payment`** | Payment Hub | Cổng thanh toán, dịch vụ liên kết & chuyển tiền | `Tiktok`<br>`P2P`<br>`Hoàn Tiền Mua Sắm`<br>`Application Store`<br>`Dịch vụ liên kết`<br>`XU`<br>`Cross Border` *(Thanh toán quốc tế)* | `/thanh-toan-quoc-te*`<br>`/chuyen-tien*`<br>`/dich-vu-lien-ket*`<br>`/tiktok*`<br>`/app-store*` |
| **`billpay`** | Billpay Hub | Thanh toán hóa đơn sinh hoạt | `Billpay`<br>`Điện`<br>`Nước`<br>`Internet`<br>`Truyền Hình`<br>`Chung Cư`<br>`Học Phí`<br>`Phí Xét Tuyển` | `/thanh-toan-hoa-don*`<br>`/dien*`<br>`/nuoc*`<br>`/internet*`<br>`/truyen-hinh*`<br>`/chung-cu*`<br>`/phi-xet-tuyen*`<br>`/thanh-toan-momo-the-hoc-duong-ssc` |
| **`telco`** | Telco Hub | Viễn thông, SIM, Data 4G/5G | `Data`<br>`Sim`<br>`Esim`<br>`Airtime`<br>`Nạp tiền điện thoại` | `/nap-data*`<br>`/sim*`<br>`/esim*`<br>`/nap-tien-dien-thoai*` |
| **`game`** | Game Hub | Dịch vụ Nạp thẻ game & Cổng trò chơi | `Game`<br>`Nạp thẻ Game` | `/nap-the-game*` |
| **`lottery`** | Lottery Hub | Dịch vụ vé số điện toán & truyền thống | `Vé số` | `/ve-so*`, `/vietlott*`, `/xskt*` |
| **`merchant`** | Merchant Hub | Trang đối tác doanh nghiệp & Landing page điểm bán | `Merchant` | `/doi-tac*` *(trang cha)*, `/thanh-toan-momo-*` *(173 trang đối tác con)*, `/page*` *(landing page điểm bán)* |
| **`soundbox`** | Soundbox Hub | Thiết bị Loa thông báo chuyển khoản & Phần cứng POS | `Soundbox` | Các slug chứa `loa-thong-bao*`, `/loa-momo*`, các bài viết về loa thông báo |
| **`download`** | Download | Trang tải ứng dụng MoMo chính thức | `Download` | `/download*`, `/tai-app*` |
| **`support`** | Support Hub | Trung tâm trợ giúp, Hỏi đáp & Pháp lý điều khoản | `Hỏi đáp`<br>`Guide`<br>`TnC`<br>`Trust`<br>`Tuyển Dụng` | `/hoi-dap*` (995 URLs)<br>`/huong-dan*`<br>`/dieu-khoan-dieu-kien*`<br>`/chinh-sach-quyen-rieng-tu*`<br>`/an-toan-bao-mat*` |
| **`search`** | Tìm Kiếm | Công cụ tìm kiếm nội bộ nền tảng MoMo | `Tìm Kiếm` | `/tim-kiem*` |
| **`home`** | Home MoMo | Trang chủ chính duy nhất của nền tảng | `Home MoMo` | `https://www.momo.vn/` |
| **`news`** | News Hub | Cổng thông tin, tin tức & khuyến mãi | `Tin Tức`<br>`Khuyến mãi` | `/tin-tuc/*`<br>`/khuyen-mai/*` |
| **`blog`** | Blog Hub | Blog bài viết chuyên sâu & kiến thức tài chính đời sống | `Blog` | `/blog/*` |
| **`campaign`** | Campaign Hub | Các trang chiến dịch, sự kiện & landing page tiếp thị | `Campaign` | `/campaign/*`<br>`/tro-thu-tai-chinh*`<br>`/tet/*` |
| **`donation`** | Donation Hub | Nền tảng thiện nguyện & CSR cộng đồng | `Donation` | `/trai-tim-momo*`<br>`/vi-nhan-ai*`<br>`/donation*` |
| **`others`** | Khác | Lưu lượng kỹ thuật & dữ liệu lịch sử | `Toàn Website (Tổng hợp T1-T4)`<br>`Others` | Các URL không xác định |

---

## 4. TỆP CẤU HÌNH MẪU CHO HUB (`hub-map.json`)

Đội ngũ phát triển Hub (`react-web-momo`) sử dụng khối JSON chuẩn hóa dưới đây để thay thế toàn bộ nội dung của file `lib/dashboard/hub-map.json`:

```json
{
  "hubs": [
    {
      "id": "cinema",
      "name": "Cinema Hub",
      "zone": "Performance",
      "isStrategic": true,
      "projects": [
        "Cinema_Cineplex Page",
        "Cinema_Page",
        "Cinema_Home Page",
        "Cinema_Blog",
        "Cinema_News",
        "Cinema_Landing Page"
      ]
    },
    {
      "id": "financial",
      "name": "Financial Hub",
      "zone": "Transformation",
      "isStrategic": true,
      "projects": [
        "Vay Nhanh",
        "Ví Trả Sau",
        "Điểm Tín Dụng",
        "Trung Tâm Tài Chính",
        "Túi Thần Tài",
        "Mở Thẻ Tín Dụng",
        "Trả Góp Apple",
        "Quản Lý Chi Tiêu",
        "Thanh Toán Khoản Vay",
        "Tiết Kiệm Online",
        "Chứng Khoán",
        "Chứng Chỉ Quỹ",
        "Sàn Đầu Tư",
        "Thanh Toán Thẻ Tín Dụng",
        "Mở tài khoản ngân hàng",
        "Tiệm Vàng Online",
        "Tỷ Giá",
        "Giá Vàng",
        "Quỹ",
        "Lãi Suất",
        "Nhận Tiền Quốc Tế",
        "Quỹ Nhóm"
      ]
    },
    {
      "id": "vehicle",
      "name": "Vehicle Hub",
      "zone": "Transformation",
      "isStrategic": true,
      "projects": [
        "Phạt Nguội",
        "Nộp Phạt CSGT",
        "Tiện Ích Giao Thông",
        "Phí Không Dừng",
        "Bảo Hiểm Ô Tô",
        "Bảo Hiểm Xe Máy",
        "Cây xăng",
        "Giá xăng",
        "Trạm sạc",
        "Garage",
        "Hãng Xe"
      ]
    },
    {
      "id": "new_user",
      "name": "New User Hub",
      "zone": "Transformation",
      "isStrategic": true,
      "district": "transformation",
      "url": "momo.vn/chao-ban-moi",
      "projects": [
        "New User"
      ]
    },
    {
      "id": "download",
      "name": "Download",
      "zone": "Platform",
      "isStrategic": false,
      "district": "center",
      "url": "momo.vn/download",
      "projects": [
        "Download"
      ]
    },
    {
      "id": "insurance",
      "name": "Insurance Hub",
      "zone": "Incubator",
      "isStrategic": true,
      "projects": [
        "Bảo Hiểm",
        "Bảo Hiểm Y Tế",
        "Bảo Hiểm Sức Khỏe",
        "Bảo Hiểm Xã Hội"
      ]
    },
    {
      "id": "student",
      "name": "Student Hub",
      "zone": "Incubator",
      "isStrategic": false,
      "projects": [
        "Student Hub",
        "Student Pass"
      ]
    },
    {
      "id": "travel",
      "name": "Travel Hub",
      "zone": "Utility",
      "isStrategic": false,
      "projects": [
        "OTA",
        "Vé Xe"
      ]
    },
    {
      "id": "payment",
      "name": "Payment Hub",
      "zone": "Utility",
      "isStrategic": false,
      "projects": [
        "Tiktok",
        "P2P",
        "Hoàn Tiền Mua Sắm",
        "Application Store",
        "Dịch vụ liên kết",
        "XU",
        "Cross Border"
      ]
    },
    {
      "id": "billpay",
      "name": "Billpay Hub",
      "zone": "Utility",
      "isStrategic": false,
      "projects": [
        "Billpay",
        "Điện",
        "Nước",
        "Internet",
        "Truyền Hình",
        "Chung Cư",
        "Học Phí",
        "Phí Xét Tuyển"
      ]
    },
    {
      "id": "telco",
      "name": "Telco Hub",
      "zone": "Utility",
      "isStrategic": false,
      "projects": [
        "Data",
        "Sim",
        "Esim",
        "Airtime",
        "Nạp tiền điện thoại"
      ]
    },
    {
      "id": "game",
      "name": "Game Hub",
      "zone": "Utility",
      "isStrategic": false,
      "projects": [
        "Game",
        "Nạp thẻ Game",
        "Game Hub"
      ]
    },
    {
      "id": "lottery",
      "name": "Lottery Hub",
      "zone": "Utility",
      "isStrategic": false,
      "projects": [
        "Vé số"
      ]
    },
    {
      "id": "merchant",
      "name": "Merchant Hub",
      "zone": "Utility",
      "isStrategic": false,
      "district": "center",
      "url": "momo.vn/doi-tac",
      "projects": [
        "Merchant"
      ]
    },
    {
      "id": "soundbox",
      "name": "Soundbox Hub",
      "zone": "Utility",
      "isStrategic": false,
      "district": "center",
      "url": "momo.vn/loa-thong-bao-chuyen-khoan",
      "projects": [
        "Soundbox"
      ]
    },
    {
      "id": "support",
      "name": "Support Hub",
      "zone": "Platform",
      "isStrategic": false,
      "district": "center",
      "url": "momo.vn/hoi-dap",
      "projects": [
        "Hỏi đáp",
        "Guide",
        "TnC",
        "Trust",
        "Tuyển Dụng"
      ]
    },
    {
      "id": "search",
      "name": "Tìm Kiếm",
      "zone": "Platform",
      "isStrategic": false,
      "district": "center",
      "url": "momo.vn/tim-kiem",
      "projects": [
        "Tìm Kiếm"
      ]
    },
    {
      "id": "home",
      "name": "Home MoMo",
      "zone": "Platform",
      "isStrategic": false,
      "district": "center",
      "url": "momo.vn",
      "projects": [
        "Home MoMo"
      ]
    },
    {
      "id": "news",
      "name": "News Hub",
      "zone": "Platform",
      "isStrategic": false,
      "district": "center",
      "url": "momo.vn/tin-tuc",
      "projects": [
        "Tin Tức",
        "Khuyến mãi"
      ]
    },
    {
      "id": "blog",
      "name": "Blog Hub",
      "zone": "Platform",
      "isStrategic": false,
      "district": "center",
      "url": "momo.vn/blog",
      "projects": [
        "Blog"
      ]
    },
    {
      "id": "campaign",
      "name": "Campaign Hub",
      "zone": "Platform",
      "isStrategic": false,
      "district": "center",
      "url": "momo.vn/campaign",
      "projects": [
        "Campaign"
      ]
    },
    {
      "id": "donation",
      "name": "Donation Hub",
      "zone": "Platform",
      "isStrategic": false,
      "district": "center",
      "url": "momo.vn/trai-tim-momo",
      "projects": [
        "Donation"
      ]
    },
    {
      "id": "others",
      "name": "Others",
      "zone": "Platform",
      "isStrategic": false,
      "projects": [
        "Toàn Website (Tổng hợp T1-T4)",
        "Others"
      ]
    }
  ]
}
```

---

## 5. QUY CHUẨN HIỂN THỊ GIAO DIỆN TRÊN CITYSCENE DASHBOARD

Nhằm đảm bảo trải nghiệm trực quan cho Ban Lãnh đạo khi theo dõi giao diện đồ họa **CityScene** (`components/dashboard/CityScene.tsx`):

1. **Phân biệt rạch ròi Tháp Chiến Lược (Strategic Towers) và Toà Nhà Tiện Ích (Utility Buildings):**
   - Chỉ có **5 Strategic Hubs** (`cinema`, `financial`, `vehicle`, `new_user`, `insurance`) mới được gắn:
     + Chóp tháp đèn pha phát sáng.
     + Huy hiệu số thứ hạng **Rank 1 đến Rank 5** theo % hoàn thành Target tháng.
     + Cột đo tiến độ Target % và nhãn trạng thái vận hành: **Đủ nhịp** (Xanh lá), **Sát nhịp** (Vàng cam), hoặc **Chậm nhịp** (Đỏ).
   - `Student Hub` tạm thời đưa ra khỏi Nhóm A về Nhóm B (Incubator/Tiện ích), hiển thị dưới dạng toà nhà thông thường, không xếp Rank và không gắn cảnh báo trễ hạn target.
   - Các Hub còn lại thuộc Nhóm Tiện ích & Nền tảng hiển thị dưới dạng toà nhà màu pastel nhạt, không có huy hiệu Rank và **tuyệt đối không gắn nhãn cảnh báo "chưa giao target tháng"** gây hiểu lầm là trễ tiến độ.
2. **Hiển thị độc lập Toà nhà Download và Tháp New User Hub:**
   - Toà tháp chiến lược `New User Hub` (95.1K PV, tăng trưởng +81.5% MoM) tập trung đo lường các chương trình giới thiệu, chào bạn mới và kích hoạt tài khoản.
   - Toà nhà `Download` (128.5K PV, màu tím `#722ED1`) xuất hiện độc lập đo lường trực tiếp lưu lượng người dùng tải ứng dụng qua `/download` và `/tai-app`.
4. **Hiển thị tách bạch Home MoMo, News Hub và Donation Hub:**
   - Toà nhà `Home MoMo` thu gọn về đúng quy mô thực tế của trang chủ (288.7K PV), không còn bị phình to bất thường do gộp tin tức, bài viết và các trang vệ tinh.
   - Toà nhà `News Hub` (159.3K PV) và `Donation Hub` (6.5K PV) hiển thị độc lập như các toà nhà nền tảng dùng chung, phản ánh chính xác cấu trúc kênh nội dung và hoạt động thiện nguyện của công ty.
5. **Hiển thị độc lập Toà nhà Soundbox và Toà nhà Merchant:**
   - Toà nhà `Merchant Hub` (56.2K PV) phản ánh đúng hoạt động thu hút đối tác doanh nghiệp và mạng lưới điểm bán (`/doi-tac*`, `/page*`).
   - Toà nhà `Soundbox Hub` (69.5K PV, tăng trưởng +1208.0% MoM) hiển thị riêng biệt đại diện cho dòng sản phẩm phần cứng Loa thông báo chuyển khoản đang bùng nổ của MoMo.
