# HƯỚNG DẪN THIẾT LẬP TRACKING GOOGLE TAG MANAGER CHO TRANG TẢI ỨNG DỤNG (/tai-app)

> **Mã Container:** `GTM-P9JDDJZ` (Container ID: `10104547`)  
> **Tài khoản GTM:** M_Service `[out_app] - momo.vn` (`4262611053`)  
> **Trang áp dụng:** `https://www.momo.vn/tai-app`  
> **Sự kiện mục tiêu:** `click_to_app` (Chuyển đổi Web-to-App chính thức)  
> **Tệp cấu hình Import tự động:** [`04_MOSPARK_PLATFORM/gtm_export/gtm_tai_app_import_package.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/gtm_export/gtm_tai_app_import_package.json)

---

## I. BỐI CẢNH & ĐIỂM NGHẼN KỸ THUẬT HIỆN TẠI

* **Thực trạng phát hiện từ dữ liệu GA4:**
  - Trang `/tai-app` đạt **Top 1,91 trên Google Search** và mang về hàng nghìn lượt truy cập tự nhiên.
  - Tuy nhiên, trong báo cáo sự kiện GA4, `/tai-app` hiện ghi nhận **0 sự kiện `click_to_app`**.
  - **Nguyên nhân:** Khi người dùng click nút "Tải trên App Store", "Tải trên Google Play" hoặc "Tải APK", GTM hiện tại chỉ kích hoạt sự kiện mặc định `click_link_url` và `click_outbound_link` chứ chưa có thẻ gắn sự kiện chuẩn `click_to_app`.
  - **Hệ quả:** Tỷ lệ chuyển đổi Web-to-App (W2A CVR) của `/tai-app` bị hiển thị bằng 0%, làm sai lệch báo cáo hiệu suất của New User Hub.

---

## II. PHƯƠNG ÁN 1: IMPORT FILE CẤU HÌNH TỰ ĐỘNG VÀO GTM (KHUYẾN NGHỊ - 30 GIÂY)

Hệ thống đã chuẩn bị sẵn gói cấu hình chuẩn JSON theo đúng định dạng xuất bản của Google Tag Manager:

1. Đăng nhập vào [Google Tag Manager](https://tagmanager.google.com).
2. Chọn Container **`GTM-P9JDDJZ`** (Account: `4262611053`).
3. Vào tab **Quản trị (Admin)** ở thanh trên cùng.
4. Ở cột Container bên phải, chọn **Nhập Vùng chứa (Import Container)**.
5. Thiết lập các bước như sau:
   - **Chọn tệp để nhập:** Tải lên tệp [`04_MOSPARK_PLATFORM/gtm_export/gtm_tai_app_import_package.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/gtm_export/gtm_tai_app_import_package.json).
   - **Chọn không gian làm việc (Workspace):** Chọn **Hiện tại (Default Workspace)**.
   - **Chọn phương án nhập (Options):** **HỢP NHẤT (MERGE)** -> Chọn **Ghi đè xung đột (Overwrite)**. *(Tuyệt đối không chọn Overwrite toàn bộ container)*.
6. GTM sẽ hiển thị bản tóm tắt:
   - Thêm mới 1 Thẻ: `[New User] - GA4 - Tai App - Click To App`.
   - Thêm mới 2 Trình kích hoạt: `Click - Tai App - Store and App Download Buttons` và `CE - tai_app_click_action`.
7. Bấm **Xác nhận (Confirm)** -> Bấm **Gửi (Submit)** để Xuất bản (Publish) phiên bản mới.

---

## III. PHƯƠNG ÁN 2: THIẾT LẬP THỦ CÔNG QUA GIAO DIỆN GTM (CLICK-BY-CLICK)

Nếu bạn muốn tự tay cấu hình từng bước trên giao diện GTM Web:

### Bước 1: Tạo Trình kích hoạt (Trigger)
1. Vào mục **Trình kích hoạt (Triggers)** -> Bấm **Mới (New)**.
2. Đặt tên: `Click - Tai App - Store and App Download Buttons`.
3. Loại trình kích hoạt: **Chỉ liên kết (Just Links)** (trong mục Nhấp chuột).
4. Thiết lập điều kiện kích hoạt: Chọn **Một số nhấp chuột vào liên kết (Some Link Clicks)**:
   - Điều kiện 1: `Page Path` | **bắt đầu bằng (starts with)** | `/tai-app`
   - Điều kiện 2: `Click URL` | **khớp với biểu thức chính quy (matches RegEx)**:
     ```text
     (apps\.apple\.com|play\.google\.com|\.apk|momoapp\.onelink\.me|momoapp\.onelink\.la|momo:\/\/|af_dp=momo)
     ```
5. Bấm **Lưu (Save)**.

### Bước 2: Tạo Thẻ Sự kiện GA4 (Tag)
1. Vào mục **Thẻ (Tags)** -> Bấm **Mới (New)**.
2. Đặt tên: `[New User] - GA4 - Tai App - Click To App`.
3. Loại thẻ: **Google Analytics: Sự kiện GA4 (Google Analytics: GA4 Event)**.
4. Thẻ cấu hình: Chọn thẻ cấu hình GA4 có sẵn trong container (hoặc điền Measurement ID `G-02G70QKZ26`).
5. Tên sự kiện (Event Name): `click_to_app`
6. Mục **Thông số sự kiện (Event Parameters)** -> Bấm **Thêm hàng (Add Row)** để nhập các cặp Key-Value sau:

| Tên thông số (Parameter Name) | Giá trị (Value) | Ghi chú nghiệp vụ |
| :--- | :--- | :--- |
| **`click_to_app`** | `1` | Bắt buộc để nhận diện sự kiện chuyển đổi W2A |
| **`hub_name`** | `New User` | Định danh thuộc New User Hub |
| **`use_case`** | `tai-app` | Định danh trang đích tải app |
| **`tool_id`** | `tai_app` | Mã tiện ích dùng chung |
| **`onelink_id`** | `tai_app_portal` | Mã nguồn điều hướng |
| **`placement`** | `tai_app_store_btn` | Vị trí nút bấm |
| **`click_url`** | `{{Click URL}}` | Bắt link đích người dùng bấm vào |
| **`link_url`** | `{{Click URL}}` | Đồng bộ trường liên kết |
| **`click_text`** | `{{Click Text}}` | Bắt text hiển thị trên nút (Tải App Store/Google Play...) |
| **`page_path`** | `{{Page Path}}` | Đường dẫn trang hiện tại |
| **`traffic_type`** | `organic_direct` | Phân loại luồng lưu lượng tự nhiên |

7. Mục **Kích hoạt (Triggering)**: Chọn Trình kích hoạt vừa tạo ở Bước 1: `Click - Tai App - Store and App Download Buttons`.
8. Bấm **Lưu (Save)**.

---

## IV. PHƯƠNG ÁN 3: ĐOẠN MÃ DATALAYER CHO FRONTEND (DÀNH CHO KỸ SƯ NEXT.JS)

Để bảo đảm 100% không bao giờ bị phụ thuộc vào URL ngoài hay class giao diện, kỹ sư Frontend có thể gắn trực tiếp hàm gọi `window.dataLayer.push` khi người dùng nhấp vào nút:

```typescript
// Gọi khi người dùng click nút Tải App Store / Google Play / Direct APK / Mở App
export const trackTaiAppClick = (storeName: 'app_store' | 'google_play' | 'direct_apk' | 'open_app', targetUrl: string) => {
  if (typeof window !== 'undefined' && window.dataLayer) {
    window.dataLayer.push({
      event: 'tai_app_click_action',
      click_to_app: 1,
      hub_name: 'New User',
      use_case: 'tai-app',
      tool_id: 'tai_app',
      onelink_id: 'tai_app_portal',
      placement: 'hero_store_button',
      store_type: storeName,
      click_url: targetUrl,
      link_url: targetUrl
    });
  }
};
```

---

## V. NGHIỆM THU KỸ THUẬT & XÁC NHẬN (DEBUGGING & QA)

1. Trên giao diện GTM, bấm **Xem trước (Preview)** -> Nhập URL `https://www.momo.vn/tai-app`.
2. Trên tab mới mở ra, thử click vào:
   - Nút "Tải trên App Store" (hoặc "Tải trên Google Play").
   - Nút "Tải trực tiếp file APK".
3. Quay lại cửa sổ **Tag Assistant**:
   - Kiểm tra cột bên trái xuất hiện sự kiện `Link Click` hoặc `tai_app_click_action`.
   - Kiểm tra thẻ `[New User] - GA4 - Tai App - Click To App` nằm trong mục **Tags Fired**.
4. Vào **GA4 DebugView** (Property `270743103`):
   - Xác nhận sự kiện `click_to_app` xuất hiện trên timeline với đầy đủ tham số `hub_name = New User` và `use_case = tai-app`.
