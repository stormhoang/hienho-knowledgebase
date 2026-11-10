# MoMo Game Hub - PRD Luồng Điều HƯớng Web MoMo Sang Web NaptheNgay.vn

## 1. PHẠM VI VÀ BỐI CẢNH

* **Phạm Vi Đặc Tả:** Luồng tương tác và chuyển tiếp dữ liệu tham số từ trang Web MoMo (`momo.vn/nap-the-game/{tên-nph}`) sang trang Web NaptheNgay (`napthengay.vn`).
* **URL Trang NPH Trên Web MoMo:** `momo.vn/nap-the-game/funtap`, `momo.vn/nap-the-game/sohagame`, `momo.vn/nap-the-game/gosu`, `momo.vn/nap-the-game/vtc-game`, `momo.vn/nap-the-game/gamota`...
* **Nguyên Tắc Phân Định Trách Nhiệm Kỹ Thuật:**
  * **Phía NaptheNgay:** Định nghĩa và ban hành Bộ Quy Chuẩn Tham Số (Parameter Contract Spec) bao gồm định danh đối tác, mã loại thẻ, mốc mệnh giá và dữ liệu đầu vào người dùng.
  * **Phía Web MoMo:** Tiếp nhận quy chuẩn, bắt sự kiện thao tác của người dùng trên trang `/nap-the-game/{tên-nph}`, đóng gói đúng các tham số đó và bắn (forward) sang URL target của `napthengay.vn`.

---

## 2. LUỒNG ĐIỀU HƯỚNG WEB MOMO ➔ WEB NAPTHENGAY

### 2.1 Bảng Tóm Tắt Trình Tự Luồng Điều Hướng

| Thứ Tự | Giai Đoạn | Trách Nhiệm Hệ Thống | Mô Tả Chi Tiết Hành Vi |
| :--- | :--- | :--- | :--- |
| **1** | Tra cứu mệnh giá | **Web MoMo** | Game thủ xem bảng niêm yết mệnh giá và tỷ giá quy đổi tại trang `/nap-the-game/{tên-nph}`. |
| **2** | Thao tác chọn | **Web MoMo** | Game thủ nhấp vào nút `[ Mua Thẻ 100k Trên NaptheNgay ]` tại mốc mệnh giá tương ứng. |
| **3** | Đóng gói & Bắn Param | **Web MoMo** | Web MoMo đóng gói dữ liệu theo đúng Param Spec của NaptheNgay (`partner`, `card`, `amount`, `email`...) và bắn URL target. |
| **4** | Mở Tab Chuyển Hướng | **Trình Duyệt** | Mở tab mới với liên kết HTML `target="_blank" rel="noopener noreferrer nofollow"`. |
| **5** | Parse Parameter | **NaptheNgay** | Website `napthengay.vn` trích xuất các tham số từ URL ngay khi DOM Ready. |
| **6** | Auto-Select UI | **NaptheNgay** | Website `napthengay.vn` tự động chọn ô loại thẻ, tự động chọn mệnh giá và điền sẵn thông tin user (nếu có). |
| **7** | Quét QR Thanh Toán | **NaptheNgay & MoMo** | Game thủ xác nhận thông tin và quét mã QR MoMo để nhận mã PIN tức thì. |

### 2.2 Bảng Phân Tích Chi Tiết Các Bước (Step Breakdown Table)

| Bước | Tên Giai Đoạn | Trải Nghiệm Người Dùng (UX) | Hạ Tầng / Cơ Chế Kỹ Thuật | Nền Tảng |
| :--- | :--- | :--- | :--- | :--- |
| **Bước 1** | Chọn Mệnh Giá Trên MoMo | Tra cứu bảng giá và nhấp vào nút `[ Mua Thẻ 100k Trên NaptheNgay ]` tại trang `/nap-the-game/{tên-nph}`. | Event Listener bắt sự kiện Click, trích xuất mã NPH và mốc mệnh giá. | Web MoMo |
| **Bước 2** | Ghép & Bắn Params | Hệ thống Web MoMo ghép các tham số do NaptheNgay quy định vào đường dẫn target. | Dynamic Target URL Builder Engine (MoMo Web). | Web MoMo |
| **Bước 3** | Chuyển Hướng Tab Mới | Trình duyệt mở tab mới dẫn sang địa chỉ website `napthengay.vn` kèm tham số. | Link HTML `target="_blank" rel="noopener noreferrer nofollow"`. | Trình duyệt Web |
| **Bước 4** | Tiếp Nhận Param Spec | Trang `napthengay.vn` tải giao diện và trích xuất các tham số `partner`, `card`, `amount`, `email`. | Client-side URL SearchParams Parser (DOM Ready). | Napthengay.vn |
| **Bước 5** | Auto-Select Giao Diện | Trang `napthengay.vn` tự động chọn ô loại thẻ tương ứng, mốc mệnh giá và pre-fill dữ liệu user. | State Selector & Auto-focus Form UI. | Napthengay.vn |

---

## 3. DANH MỤC QUY CHUẨN THAM SỐ DO NAPTHENGAY QUY ĐỊNH (PARAMETER CONTRACT SPEC)

### 3.1 Cấu Trúc URL Target Chuyển Tiếp Sang Napthengay.vn

```text
https://napthengay.vn/?partner={partner_code}&card={card_code}&amount={denomination}&email={user_email}&quantity={qty}
```

### 3.2 Bảng Phân Loại Các Nhóm Tham Số (Parameter Contract Table)

| Nhóm Tham Số | Tham Số (Key) | Kiểu Dữ Liệu | Giá Trị Mẫu | Mô Tả & Trách Nhiệm Xử Lý |
| :--- | :--- | :--- | :--- | :--- |
| **1. Định danh Đối tác** | `partner` | String | `momo` | **Bắt buộc** (Do NaptheNgay quy định). Định danh nguồn traffic và đối soát doanh thu thuộc về MoMo. |
| **2. Sản phẩm Thẻ** | `card` | String | `funcard`, `sohacoin`, `gosu`, `vcoin`, `appota` | **Bắt buộc** (Do NaptheNgay quy định). Mã loại thẻ cào NPH. Web Napthengay tự động chọn (Active) thẻ này. |
| **3. Mệnh giá Thẻ** | `amount` | Integer | `20000`, `50000`, `100000`, `200000`, `500000` | **Bắt buộc** (Do NaptheNgay quy định). Mệnh giá thẻ (VND). Web Napthengay tự động chọn mốc mệnh giá này. |
| **4. Số lượng Mua** | `quantity` | Integer | `1` | **Không bắt buộc** (Mặc định = 1). Số lượng mã thẻ mua. |
| **5. Dữ liệu User Input** | `email` | String | `gamer@gmail.com` | **Không bắt buộc** (Optional Prefill). Nếu Web MoMo có sẵn Email user đã đăng nhập, bắn sang để NaptheNgay tự điền sẵn. |

### 3.3 Bảng Mapping Tham Số Web MoMo Bắn Sang NaptheNgay Theo NPH

| Nhà Phát Hành | URL Trang NPH Trên Web MoMo | Tham Số `partner` | Tham Số `card` | Tham Số `amount` | Ví Dụ URL Web MoMo Bắn Sang NaptheNgay |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Funtap** | `/nap-the-game/funtap` | `momo` | `funcard` | `100000` | `https://napthengay.vn/?partner=momo&card=funcard&amount=100000` |
| **SohaGame** | `/nap-the-game/sohagame` | `momo` | `sohacoin` | `500000` | `https://napthengay.vn/?partner=momo&card=sohacoin&amount=500000` |
| **Gosu** | `/nap-the-game/gosu` | `momo` | `gosu` | `200000` | `https://napthengay.vn/?partner=momo&card=gosu&amount=200000` |
| **VTC Game** | `/nap-the-game/vtc-game` | `momo` | `vcoin` | `100000` | `https://napthengay.vn/?partner=momo&card=vcoin&amount=100000` |
| **Gamota** | `/nap-the-game/gamota` | `momo` | `appota` | `50000` | `https://napthengay.vn/?partner=momo&card=appota&amount=50000` |

---

## 4. YÊU CẦU PHỐI HỢP KỸ THUẬT VÀ XỬ LÝ NGOẠI LỆ

### 4.1 Trách Nhiệm Phía Web MoMo
* Đọc đúng file Spec tham số do NaptheNgay cung cấp.
* Khi người dùng click nút CTA tại trang `/nap-the-game/{tên-nph}`, trích xuất mệnh giá `amount` và mã thẻ `card` tương ứng, ghép tham số `partner=momo` và bắn URL target sang tab mới.
* Gắn thuộc tính `target="_blank" rel="noopener noreferrer nofollow"` cho liên kết chuyển tiếp.

### 4.2 Trách Nhiệm Phía Website NaptheNgay
* Tiếp nhận và trích xuất danh mục tham số (`partner`, `card`, `amount`, `email`, `quantity`) ngay khi trang load (DOM Ready).
* Auto-select ô loại thẻ tương ứng với `card` và mốc mệnh giá tương ứng với `amount`.
* Điền sẵn (Pre-fill) địa chỉ Email vào ô nhận mã nếu có tham số `email`.
* **Xử lý Ngoại lệ (Fallback):** Nếu mốc mệnh giá `amount` tạm thời hết hàng trong kho, giữ nguyên loại thẻ `card`, bỏ chọn `amount` và hiển thị thông báo nhẹ (Toast): *"Mệnh giá chọn tạm thời hết hàng, vui lòng chọn mệnh giá khác"*.
