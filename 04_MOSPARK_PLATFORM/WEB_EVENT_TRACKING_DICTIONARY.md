# SỔ TAY TỪ ĐIỂN SỰ KIỆN WEB PLATFORM (DATA ANALYST EVENT DICTIONARY)
**Phiên bản:** 2.0 (Đồng bộ theo GTM Container Version 222 & GA4 Property 270743103)  
**Tài liệu dành cho:** Data Analyst (DA), Business Intelligence (BI), Product Lead, Engineering Team  
**Phạm vi:** Toàn bộ website MoMo (`momo.vn`, `m.momo.vn`)

---

## I. THÔNG TIN HỆ THỐNG & NGUỒN DỮ LIỆU GỐC TRÊN BIGQUERY

| Thuộc tính | Giá trị chuẩn xác | Ghi chú cho DA |
| :--- | :--- | :--- |
| **BigQuery Project** | `momovn-prod` | Project chứa kho dữ liệu production của MoMo |
| **GA4 Raw Export Dataset** | `momovn-prod.analytics_270743103` | Dataset xuất thô hàng ngày từ GA4 Web |
| **Bảng chốt ngày (Daily Batch)** | `analytics_270743103.events_YYYYMMDD` | Chốt sau 12:00 trưa hàng ngày (dữ liệu sạch) |
| **Bảng trong ngày (Intraday Streaming)** | `analytics_270743103.events_intraday_YYYYMMDD` | Đổ realtime sau 15-30 phút (dùng check nhanh) |
| **GA4 Property ID** | `270743103` (Stream: `G-02G70QKZ26`) | Web MoMo Out-App Traffic |
| **GTM Container ID** | `GTM-P9JDDJZ` (Container ID: `10104547`) | M_Service `[out_app] - momo.vn` |
| **Umami Analytics** | `https://analytics.momo.vn` | Hệ thống đo lường hành vi UI / InView |

---

## II. TOP SỰ KIỆN QUAN TRỌNG NHẤT (CORE W2A & FUNNEL EVENTS)

Đội ngũ DA cần tập trung vào các sự kiện lõi sau để đo lường Traffic, Chuyển đổi Web-to-App (W2A) và Tương tác CTA:

| Event Name (Chuẩn xác) | Nghiệp vụ / Ý nghĩa | Khi nào sự kiện bắn ra? | Bộ Parameter quan trọng nhất đính kèm |
| :--- | :--- | :--- | :--- |
| **`click_to_app`** | **Mở App / Web-to-App Chuyển đổi chính** | User click vào bất kỳ nút mở App nào (CTA Hero, Banner, WebAds, hoặc Utility Tools). | `click_url`, `link_url`, `tool_id`, `onelink_id`, `placement`, `click_to_app: 1`, `device_type`, `page_path` |
| **`click_link_url`** | **Click liên kết chuyển trang / OneLink ngoài** | User click vào thẻ liên kết `<a>` trỏ tới OneLink, Deep link hoặc URL ngoài. | `link_url`, `click_text`, `page_path`, `device_type` |
| **`click_cta`** | **Click nút hành động chung (CTA Button)** | User click vào các nút CTA (Button) trên toàn bộ Landing Page / Hubs. | `click_text`, `click_url`, `page_path`, `component_name` |
| **`component_view`** | **Lượt xem khối nội dung (In-View)** | Một khối giao diện (Widget, Form, Carousel, Banner) hiển thị vào khung nhìn màn hình. | `component_category1`, `component_category2`, `component_name`, `page_location` |
| **`component_click_cta`** | **Click tương tác trong component** | User click nút hành động nằm bên trong một component cụ thể. | `component_name`, `click_text`, `click_url`, `page_location` |
| **`page_view`** | **Lượt xem trang tiêu chuẩn** | Trang được tải thành công trên trình duyệt. | `page_location`, `page_title`, `page_referrer`, `device_type` |

---

## III. BỘ ĐO LƯỜNG TIỆN ÍCH NHÚNG (UTILITIES TOOL & LOGIN ATTRIBUTION)

Đây là hệ thống mới được chuẩn hóa qua **Folder `[Platform] - UTILITIES TOOL` (GTM Version 222)** và mã frontend:

### 1. Sự kiện GTM / GA4 bắn ra
* **Event Name:** **`click_to_app`**
* **Trigger kích hoạt:** Custom Event `utility_track` khi người dùng click CTA mở App hoặc mở Popup QR của Tool.
* **Các tham số đính kèm (Query qua `event_params`):**
  * **`tool_id`**: Mã định danh công cụ (ví dụ: `cic_calc`, `salary_calc`, `bhxh_calc`, `saving_calc`).
  * **`onelink_id`**: Mã OneLink tương ứng (ví dụ: `6OKONic9`, `EoWoWJ1G`, `J3hhwGSR`).
  * **`placement`**: Vị trí nhúng công cụ (ví dụ: `mot-mua-quyt`, `inline_widget`, `blog_body`).
  * **`click_url`**: Full OneLink URL đã được tự động trang trí (Decorated URL).
  * **`click_to_app`**: Giá trị cố định `'1'`.

### 2. Danh mục 8 Master Utility Tools & Mã OneLink SSOT
DA dùng bảng này để map mã công cụ hoặc OneLink ID với tên nghiệp vụ:

| Tên Công Cụ Tiện Ích | `tool_id` | `onelink_id` | Tham số OneLink URL chứa | Trang nhúng điển hình |
| :--- | :--- | :--- | :--- | :--- |
| **Tính Điểm Tín Dụng & Nợ Xấu CIC** | `cic_calc` | `6OKONic9` | `af_sub1=cic_calc` | `/diem-tin-dung`, `/game/mot-mua-quyt` |
| **Tính BHXH Tự Nguyện** | `bhxh_calc` | `J3hhwGSR` | `af_sub1=bhxh_calc` | `/game/mot-mua-quyt`, Blog Tài chính |
| **Tính Lương Gross Sang Net** | `salary_calc` | `EoWoWJ1G` | `af_sub1=salary_calc` | `/tai-chinh/tinh-luong`, `/game/mot-mua-quyt` |
| **Tính Lãi Tiết Kiệm Ngân Hàng** | `saving_calc` | `EoWoWJ1G` | `af_sub1=saving_calc` | `/tai-chinh/gui-tiet-kiem`, `/game/mot-mua-quyt` |
| **Chọn Ngân Hàng Tiết Kiệm Tốt Nhất** | `best_bank_saving` | `EowWdqm6` | `af_sub1=best_bank_saving` | `/tai-chinh/lai-suat`, `/game/mot-mua-quyt` |
| **Tỷ Giá & Quy Đổi Ngoại Tệ FX** | `exchange_rate` | `gmfyvcnA` | `af_sub1=exchange_rate` | `/tai-chinh/ty-gia`, `/game/mot-mua-quyt` |
| **Chứng Chỉ Quỹ Đầu Tư** | `fund_certificate` | `aiAQInWp` | `af_sub1=fund_certificate` | `/tai-chinh`, `/game/mot-mua-quyt` |
| **Ví Trả Sau (PayLater)** | `pay_later` | `68rtnbrt` | `af_sub1=pay_later` | `/vi-tra-sau`, `/game/mot-mua-quyt` |

### 3. Quy chuẩn URL OneLink để Join với Dữ Liệu App Login
Mọi link OneLink khi user click đều có cấu trúc:
```text
https://momoapp.onelink.me/7UUy/<onelink_id>?ref=website&af_sub1=<tool_id>&af_sub2=<page_path>&c=embed_utility
```
* **Để xác định User Login App từ Tool nào:** DA join bảng `USER_LOGIN` / `APPSFLYER_INSTALLS` với điều kiện:
  * `af_sub1 = '<tool_id>'` (hoặc `c = 'embed_utility'`).
  * `af_sub2` là slug trang web dẫn nguồn (ví dụ `/game/mot-mua-quyt`).

---

## IV. BỘ ĐO LƯỜNG QUẢNG CÁO NỘI BỘ (WEBADS TRACKING)

Dành cho định dạng Popup và Balloon góc màn hình:

| Event Name | Định dạng quảng cáo | Tham số đính kèm | Ghi chú bóc tách cho DA |
| :--- | :--- | :--- | :--- |
| **`webads_balloon`** | Balloon Popup góc phải màn hình | `webads_campaign`, `ad_project`, `ad_format`, `ad_position`, `ad_creative`, `click_url`, `action_type`, `device_type`, `page_path` | Bắt cả lượt xem và click. **Để lọc Click mở app:** Lọc điều kiện `click_url LIKE 'http%'`. |
| **`webads_popup`** | Modal Popup trung tâm màn hình | Tương tự như Balloon | Bắn khi có chiến dịch Popup trung tâm. |
| **`floatads_view`** | Lượt hiển thị Float Icon | `campaign_name`, `placement` | Nút Zalo/Hỗ trợ góc màn hình. |
| **`floatads_cta_click`**| Lượt click Float Icon | `campaign_name`, `click_url` | Click vào nút nổi. |

---

## V. DANH MỤC SỰ KIỆN THEO TỪNG HUB NGHIỆP VỤ

### 1. Vehicle Hub (Giao Thông & Bảo Hiểm Xe)
* **`web_vehicle_hub_view`**: Xem trang tổng quan Vehicle Hub (`/tien-ich-giao-thong`).
* **`web_traffic_fine_lookup_form_submit`**: Người dùng bấm tra cứu phạt nguội giao thông trên form.
* **`web_fuel_price_lookup_btn_click`**: Người dùng click tra cứu giá xăng dầu hôm nay.
* **`web_car_insur_cta_click`**: Click CTA bảo hiểm thân vỏ ô tô.
* **`bhxm_form_view` / `bhxm_form_submit` / `bhxm_payment_click`**: Phễu đăng ký và thanh toán bảo hiểm xe máy.
* **`checkout_started` / `purchase`**: Phễu thanh toán bảo hiểm ô tô (BHOTO Ver 3).

### 2. Gamification (Game Zone / Một Mùa Quýt)
* **`quyt_screen_view`**: Lượt xem từng màn hình câu hỏi / kết quả trong game Một Mùa Quýt.
* **`gmc_1vuquyt_clickplay`**: Lượt click nút "Bắt đầu chơi / Trồng quýt".
* **`gmc_1vuquyt_install`**: Lượt click tải App / tham gia sự kiện trong game.
* **`quyt_share_click`**: Lượt click chia sẻ kết quả loại quýt của người chơi.

### 3. Dịch Vụ Số & Khác
* **Bảo hiểm Y Tế (BHYT):**
  * `bhyt_form_view`: Xem form tra cứu BHYT.
  * `bhyt_form_submit`: Gửi tra cứu BHYT.
  * `bhyt_payment_click`: Bấm thanh toán / nộp BHYT.
  * `bhyt_renew_click`: Bấm gia hạn thẻ BHYT.
  * `bhyt_app_download`: Bấm tải App từ trang BHYT.
* **Vé Xe Khách (OTA BUS):**
  * `bus_searchroute_submit`: Tìm chuyến xe.
  * `bus_operator_select`: Chọn nhà xe.
  * `bus_seatmap_select`: Chọn ghế trên sơ đồ xe.
  * `bus_click_to_buy`: Bấm tiến hành mua vé xe.
  * `bus_transaction_result`: Màn hình kết quả giao dịch vé.
* **SIM Số / Gói Cước Data:**
  * `sim_listing_view`: Xem danh sách sim/gói cước.
  * `sim_search_submit`: Tìm kiếm số đẹp.
  * `sim_plan_select`: Chọn gói cước.
  * `sim_click_to_buy`: Bấm mua sim / gói cước.
* **Ví Trả Sau (PayLater):**
  * `vts_cta_h1`: Click CTA mở Ví Trả Sau trên đầu trang (Hero).
  * `vts_cta_topnavi`: Click CTA trên menu điều hướng.
  * `vts_cta_footer`: Click CTA ở chân trang.
  * `vts_click_viewguide`: Bấm xem hướng dẫn đăng ký Ví Trả Sau.
  * `tragop_vts_click_thamkhao`: Bấm tham khảo tính năng trả góp qua Ví Trả Sau.

---

## VI. SQL CHEAT SHEET DÀNH CHO DATA ANALYST (BIGQUERY READY)

DA có thể copy các mẫu truy vấn bên dưới để lấy số liệu nhanh chóng:

### Mẫu 1: Kéo số Click Mở App theo từng Công Cụ Tiện Ích (`tool_id`)
```sql
SELECT
  PARSE_DATE('%Y%m%d', event_date) AS log_date,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'tool_id') AS tool_id,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'onelink_id') AS onelink_id,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'placement') AS placement,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'click_url') AS click_url,
  COUNT(1) AS click_to_app_events,
  COUNT(DISTINCT user_pseudo_id) AS unique_web_users
FROM
  `momovn-prod.analytics_270743103.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY))
                    AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
  AND event_name = 'click_to_app'
  AND (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'tool_id') IS NOT NULL
GROUP BY
  log_date, tool_id, onelink_id, placement, click_url
ORDER BY
  click_to_app_events DESC;
```

---

### Mẫu 2: Phân Tích WebAds Balloon (Lượt Hiển Thị vs. Lượt Click Mở App)
```sql
SELECT
  PARSE_DATE('%Y%m%d', event_date) AS log_date,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'webads_campaign') AS webads_campaign,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'ad_project') AS ad_project,
  -- Lượt tương tác tổng (View + Close + Click)
  COUNT(1) AS total_balloon_events,
  -- Lượt click CTA thực tế mở App (có gắn OneLink)
  COUNTIF(
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'click_url') LIKE 'http%'
  ) AS actual_cta_clicks,
  COUNT(DISTINCT user_pseudo_id) AS total_users
FROM
  `momovn-prod.analytics_270743103.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
                    AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
  AND event_name = 'webads_balloon'
GROUP BY
  log_date, webads_campaign, ad_project
ORDER BY
  actual_cta_clicks DESC;
```

---

### Mẫu 3: Join Web CTA Click với In-App Login (Web-to-App Closed Loop Attribution)
```sql
WITH web_utility_clicks AS (
  SELECT
    user_pseudo_id,
    TIMESTAMP_MICROS(event_timestamp) AS click_time,
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'tool_id') AS tool_id,
    REGEXP_EXTRACT(
      (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'click_url'),
      r'[?&]wui=([^&]+)'
    ) AS web_user_id
  FROM
    `momovn-prod.analytics_270743103.events_*`
  WHERE
    _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
    AND event_name = 'click_to_app'
)
SELECT
  w.tool_id,
  COUNT(w.user_pseudo_id) AS web_clicks,
  -- Đếm số user mở app có ghi nhận af_sub1 khớp tool_id trong bảng AppsFlyer
  COUNT(a.appsflyer_id) AS app_installs_or_opens
FROM
  web_utility_clicks w
LEFT JOIN
  `momovn-prod.APPSFLYER.installs` a
  ON a.af_sub1 = w.tool_id
  AND a.event_time >= w.click_time
  AND a.event_time <= TIMESTAMP_ADD(w.click_time, INTERVAL 24 HOUR)
GROUP BY
  w.tool_id;
```
