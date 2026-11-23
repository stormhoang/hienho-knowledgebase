# BÁO CÁO TOÀN DIỆN: REVIEW KẾT QUẢ TÁI CẤU TRÚC PIPELINE CONTENT PLAN

Dữ liệu kiểm toán và rà soát từ kho SSOT `05_HUBS/inventory/` chuẩn bị đồng bộ cho Web Platform.
Đáp ứng đầy đủ 5 tiêu chí:
1. Phân loại từ khóa sai theme (Entity-based reallocation).
2. Gộp biến thể chính tả (Max volume, không cộng dồn, lưu variants).
3. Triệt tiêu khung 6 slot cố định, sinh URL từ sub-cluster thực tế theo ngưỡng $\ge 500$/tháng.
4. Thuộc tính Priority, Funnel, Format tính toán hoàn toàn từ dữ liệu.
5. Loại bỏ câu fallback chung, ánh xạ chính xác tính năng MoMo thực tế kèm Deeplink & Event đo lường (hoặc null).

---

## 1. TỔNG QUAN CHỈ SỐ KIỂM TOÁN

| Chỉ Số Đo Lường | Giá Trị Thực Tế | Ghi Chú Kỹ Thuật |
| :--- | :---: | :--- |
| **Tổng số Use Cases (Themes)** | **190** | Sau khi merge cic -> diem-tin-dung |
| **Từ khóa chuyển sai theme** | **1,353** | Lottery: Vietlott <-> XSKT; Bank đối thủ; BHYT <-> BHXH; VETC <-> ePass |
| **Nhóm biến thể chính tả đã gộp** | **15,235** | Lấy Max Volume, loại trừ trùng lặp chính tả/khoảng trắng |
| **Cụm Sub-cluster bị loại (< 500)** | **605** | Dưới ngưỡng $\ge 500$/tháng, gộp vào section Pillar, không tách URL |
| **Use Case có CTA Hook cụ thể** | **58 / 190 (30.5%)** | Ánh xạ tính năng thực tế MoMo; 100% theme còn lại trả về `null` |

---

## 2. A. DANH SÁCH KEYWORD ĐÃ CHUYỂN THEME (TOP ĐIỂN HÌNH)

Tổng cộng **1,353 từ khóa** được chuyển về đúng thực thể chủ quản. Dưới đây là bảng trích xuất các từ khóa có volume lớn nhất:

| STT | Từ Khóa | Volume/Tháng | Chuyển Từ Theme | Chuyển Đến Theme | Lý Do Kỹ Thuật |
| :---: | :--- | :---: | :--- | :--- | :--- |
| 1 | `xsmb` | 83,100,000 | `vietlott` | `xo-so` | Từ khóa XSKT truyền thống nằm trong Vietlott |
| 2 | `agribank` | 368,000 | `vrb` | `agribank` | Chứa thương hiệu ngân hàng đối thủ (agribank) |
| 3 | `mbbank` | 301,000 | `scb` | `mbbank` | Chứa thương hiệu ngân hàng đối thủ (mbbank) |
| 4 | `mbbank` | 301,000 | `ab-bank` | `mbbank` | Chứa thương hiệu ngân hàng đối thủ (mbbank) |
| 5 | `mbbank` | 301,000 | `ocb` | `mbbank` | Chứa thương hiệu ngân hàng đối thủ (mbbank) |
| 6 | `mb bank` | 301,000 | `MSB` | `mbbank` | Chứa thương hiệu ngân hàng đối thủ (mb bank) |
| 7 | `xổ số vietlott` | 201,000 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 8 | `xs vietlott` | 165,000 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 9 | `xổ số power` | 110,000 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 10 | `vietlott sms` | 110,000 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 11 | `mb bank atm` | 90,500 | `seabank` | `mbbank` | Chứa thương hiệu ngân hàng đối thủ (mb bank) |
| 12 | `xổ số mega` | 90,500 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 13 | `vietlott 6 45` | 90,500 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 14 | `vietlott 6 55` | 90,500 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 15 | `bảo hiểm y tế` | 74,000 | `bhxh` | `bhyt` | Từ khóa thuần Bảo Hiểm Y Tế nằm trong BHXH |
| 16 | `xsmega` | 74,000 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 17 | `kết quả vietlott` | 60,500 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 18 | `mega645` | 49,500 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 19 | `xổ số vietlott hôm nay` | 40,500 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 20 | `truc tiep keno` | 40,500 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 21 | `trực tiếp keno` | 40,500 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 22 | `kết quả xổ số vietlott` | 33,100 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 23 | `max3d` | 33,100 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 24 | `vietinbank ipay` | 27,100 | `vietbank` | `VietinBank` | Chứa thương hiệu ngân hàng đối thủ (vietinbank) |
| 25 | `seabank` | 27,100 | `nam-a-bank` | `seabank` | Chứa thương hiệu ngân hàng đối thủ (seabank) |
| 26 | `xổ số điện toán` | 27,100 | `vietlott` | `xo-so` | Từ khóa XSKT truyền thống nằm trong Vietlott |
| 27 | `xổ số keno` | 27,100 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 28 | `keno trực tiếp` | 27,100 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 29 | `acb bank` | 22,200 | `ncb` | `ACB` | Chứa thương hiệu ngân hàng đối thủ (acb bank) |
| 30 | `tỷ giá vietinbank` | 22,200 | `vietbank` | `VietinBank` | Chứa thương hiệu ngân hàng đối thủ (vietinbank) |
| 31 | `acb bank` | 22,200 | `ocb` | `ACB` | Chứa thương hiệu ngân hàng đối thủ (acb bank) |
| 32 | `ket qua vietlott` | 22,200 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 33 | `kq vietlott` | 22,200 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 34 | `kqxs vietlott` | 22,200 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 35 | `kết quả các kỳ quay vietlott 6 55` | 22,200 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 36 | `vietlott 655` | 22,200 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 37 | `bidv i bank` | 18,100 | `nam-a-bank` | `BIDV` | Chứa thương hiệu ngân hàng đối thủ (bidv) |
| 38 | `xổ số hàng tuần` | 18,100 | `vietlott` | `xo-so` | Từ khóa XSKT truyền thống nằm trong Vietlott |
| 39 | `xổ số vietlott 6 55` | 18,100 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 40 | `keno vietlott` | 18,100 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 41 | `kết quả keno` | 18,100 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 42 | `xs vietlott hôm nay` | 18,100 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 43 | `mbbank đăng nhập` | 14,800 | `ab-bank` | `mbbank` | Chứa thương hiệu ngân hàng đối thủ (mbbank) |
| 44 | `mbbank đăng nhập` | 14,800 | `ocb` | `mbbank` | Chứa thương hiệu ngân hàng đối thủ (mbbank) |
| 45 | `ngan hàng bản việt` | 14,800 | `VietinBank` | `ban-viet` | Chứa thương hiệu ngân hàng đối thủ (bản việt) |
| 46 | `keno minh chinh` | 14,800 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 47 | `keno minh chính` | 14,800 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 48 | `vietlott vn` | 14,800 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 49 | `xskeno` | 14,800 | `xo-so` | `vietlott` | Từ khóa sản phẩm Vietlott nằm trong XSKT/Vé số |
| 50 | `mbbank online` | 12,100 | `ab-bank` | `mbbank` | Chứa thương hiệu ngân hàng đối thủ (mbbank) |

---

## 3. B. DANH SÁCH NHÓM BIẾN THỂ ĐÃ GỘP (MAX VOLUME)

Tổng cộng **15,235 nhóm biến thể** được làm sạch. Volume lấy MAX (không cộng dồn) để tránh phóng đại dung lượng thị trường:

| STT | Theme | Từ Khóa Chính (Canonical) | Max Volume | Danh Sách Biến Thể Đã Gộp (`variants[]`) |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `xo-so` | **`xsmb`** | 83,100,000 |  |
| 2 | `xo-so` | **`xổ so miền bắc`** | 83,100,000 | `xô sô miên băc`, `xo số mien bac`, `xổ số miền bắc`, `xo số miền bắc` (+13 khác) |
| 3 | `xo-so` | **`xổ số miền nam`** | 68,000,000 | `xo số mien nam`, `xo số miền nam`, `xô số miền nam`, `xổ sô miền nam` (+10 khác) |
| 4 | `xo-so` | **`xổ số miền trung`** | 20,400,000 | `xo so mien trung`, `xo so miên trung`, `xo so miền trung` |
| 5 | `xo-so` | **`xổ số miền nam hôm nay`** | 11,100,000 | `xo số miền nam hôm nay`, `xo so mien nam hom nay`, `xo so miền nam hôm nay` |
| 6 | `gia-vang` | **`giá vàng hôm nay`** | 9,140,000 | `giâ vàng hôm nay`, `gia vang hom nay`, `giá vang hom nay`, `giá vàng hômnay` (+6 khác) |
| 7 | `xo-so` | **`kq xsmb`** | 9,140,000 | `kqxsmb`, `kqxs mb` |
| 8 | `xo-so` | **`xổ số hôm nay`** | 7,480,000 | `xô số hôm nay`, `xo so hom nay`, `xo số hôm nay`, `xo so hôm nay` (+1 khác) |
| 9 | `xo-so` | **`xổ số miền bắc hôm nay`** | 7,480,000 | `xo số miền bắc hôm nay`, `xổ số miên bắc hôm nay`, `xo so mien bac hom nay`, `xo so miền bắc hôm nay` (+2 khác) |
| 10 | `xo-so` | **`xổ số minh ngọc`** | 5,000,000 | `xổ số mình ngọc`, `xo so minhngoc`, `xôsominhngoc` |
| 11 | `xo-so` | **`kết quả xổ số miền bắc`** | 5,000,000 | `ket qua xo so mien bac`, `kết qua xo so mien bac`, `ket qua xổ số miền bắc`, `ket quả xổ số miền bắc` (+4 khác) |
| 12 | `gia-vang` | **`giá vàng thế giới`** | 4,090,000 | `gia vang the gioi`, `giá vàng the giới`, `giá vàng the giới` |
| 13 | `xo-so` | **`xổ số miền trung hôm nay`** | 4,090,000 | `xo so mien trung hom nay`, `xổ số miền trung hom nay`, `xo so miền trung hôm nay`, `xosomientrunghomnay` |
| 14 | `xo-so` | **`xs mb hôm nay`** | 3,350,000 | `xsmb hôm nay` |
| 15 | `lich-am` | **`lịch âm`** | 2,740,000 | `lich am`, `lịch ám`, `lịcham`, `lịchâm` |
| 16 | `nap-game` | **`nạp thẻ x5`** | 2,740,000 | `napthex5` |
| 17 | `xo-so` | **`kq xsmn`** | 2,740,000 | `kqxs mn` |
| 18 | `xo-so` | **`xổ số`** | 2,240,000 | `xo so`, `xô số` |
| 19 | `xo-so` | **`kêt quả xổ số miền bắc hôm nay`** | 2,240,000 | `ket qua xo so mien bac hom nay`, `kết quả xô sô miên bắc hôm nay` |
| 20 | `xo-so` | **`kết quả xổ số miền nam`** | 2,240,000 | `ket qua xo so mien nam`, `ket quả xổ số miền nam` |
| 21 | `xo-so` | **`số xo`** | 2,240,000 | `so xo`, `số xổ` |
| 22 | `gia-vang` | **`giá vàng`** | 1,830,000 | `gia vàng`, `giâ vàng`, `gia vang`, `gía vàng` (+1 khác) |
| 23 | `xo-so` | **`xs kt`** | 1,830,000 | `xskt` |
| 24 | `xo-so` | **`xổ số hà nội`** | 1,830,000 | `xổ số ha noi`, `xo so ha noi` |
| 25 | `xo-so` | **`xổ số minh ngọc miền nam`** | 1,830,000 | `xo so minh ngoc mien nam`, `xosominhngoc miennam` |
| 26 | `xo-so` | **`mình ngoc`** | 1,830,000 | `minhngoc` |
| 27 | `xo-so` | **`xsmn hôm nay`** | 1,830,000 | `xs mn hom nay` |
| 28 | `gia-vang` | **`giá vàng thế giới hôm nay`** | 1,500,000 | `gia vang thê giơi hôm nay`, `giá vàng thê giới hôm nay`, `gia vang the gioi hom nay`, `giá vàng the giới hôm nay` (+2 khác) |
| 29 | `lich-am` | **`lịch âm hôm nay`** | 1,500,000 | `lich am hom nay`, `lich am hôm nay`, `lich am homnay`, `lich âm hom nay` (+1 khác) |
| 30 | `xo-so` | **`xổ số khánh hòa`** | 1,500,000 | `xo so khanh hoa` |
| 31 | `xo-so` | **`số xo mien nam`** | 1,500,000 | `so xo mien nam`, `sổ xô miên nam`, `sô xo miên nam`, `so xo miên nam` (+5 khác) |
| 32 | `xo-so` | **`số miền nam`** | 1,500,000 | `so mien nam`, `sỗ mien nam` |
| 33 | `gia-xang` | **`xăng`** | 1,220,000 | `xang` |
| 34 | `gia-dau` | **`xăng`** | 1,220,000 | `xang` |
| 35 | `xo-so` | **`xổ số minh ngọc miền bắc`** | 1,220,000 | `xo so minh ngoc mien bac`, `xosominhngoc mienbac` |
| 36 | `xo-so` | **`xổ số 66`** | 1,220,000 | `xoso66` |
| 37 | `xo-so` | **`kết quả xổ số`** | 1,220,000 | `kêt quả xổ số`, `ket qua xo so`, `ket qua xổ số`, `ketqua xo so` (+1 khác) |
| 38 | `xo-so` | **`xs hom nay`** | 1,220,000 | `xshom nay` |
| 39 | `lich-am` | **`âm lịch hôm nay`** | 1,000,000 | `am lich hom nay`, `am lịch hôm nay`, `âm lich hôm nay`, `am lich hôm nay` (+4 khác) |
| 40 | `gia-xang` | **`gia xăng hôm nay`** | 1,000,000 | `giá xăng hôm nay`, `gia xăng hom nay`, `gia xang hom nay`, `gia xang hôm nay` (+2 khác) |
| 41 | `gia-dau` | **`gia xăng hôm nay`** | 1,000,000 | `giá xăng hôm nay`, `gia xăng hom nay`, `gia xang hom nay`, `gia xang hôm nay` (+1 khác) |
| 42 | `tram-sac` | **`trạm sạc vinfast`** | 1,000,000 | `tram sac vinfast`, `tram sạc vinfast` |
| 43 | `xo-so` | **`xổ số ba miền`** | 1,000,000 | `xo so ba mien` |
| 44 | `xo-so` | **`xổ số kiến thiết miền nam`** | 1,000,000 | `xo so kien thiet mien nam` |
| 45 | `xo-so` | **`số xo hôm nay`** | 1,000,000 | `so xo hom nay`, `số xổ hôm nay` |
| 46 | `xo-so` | **`số miền bắc`** | 1,000,000 | `so mien bac`, `sốmienbac`, `sỗ mien bac` |
| 47 | `Vietcombank` | **`vietcombank`** | 823,000 | `việtcombank`, `việt combank`, `việt com bank` |
| 48 | `internet-banking` | **`vietcombanking`** | 823,000 | `vietcom banking` |
| 49 | `xo-so` | **`xskt mièn bắc`** | 823,000 | `xskt miên bac`, `xskt miên bắc`, `xskt miền bac`, `xskt miền băc` (+4 khác) |
| 50 | `xo-so` | **`xổ số kiến thiết miền bắc`** | 823,000 | `xo so kien thiet mien bac` |
| 51 | `xo-so` | **`xổ số phú yên`** | 823,000 | `xổ số phú yen` |
| 52 | `xo-so` | **`sô kết qua`** | 823,000 | `so ket qua`, `sổ kết quả`, `sổ kêt quả`, `so kêt quả` (+6 khác) |
| 53 | `xo-so` | **`sổ xô miên bắc`** | 823,000 | `so xo mien bac`, `sô xo miên bac`, `so xo mien băc`, `so xo miền bắc` (+7 khác) |
| 54 | `xo-so` | **`dự đoán xsmb`** | 823,000 | `du đoán xsmb` |
| 55 | `gia-xang` | **`giá xăng dầu hôm nay`** | 673,000 | `gia xang dầu hôm nay`, `gia xăng dâu hôm nay`, `gia xăng dầu hôm nay`, `gia xang dau hom nay` (+7 khác) |
| 56 | `phat-nguoi` | **`tra cứu phạt nguội`** | 673,000 | `tra cuu phat nguoi`, `tra cuu phat nguội`, `tra cuu phat nguôi`, `tra cuu phạt nguoi` (+1 khác) |
| 57 | `gia-dau` | **`giá xăng dầu hôm nay`** | 673,000 | `gia xang dầu hôm nay`, `gia xăng dâu hôm nay`, `gia xăng dầu hôm nay`, `gia xang dau hom nay` (+5 khác) |
| 58 | `xo-so` | **`xô sô mn`** | 673,000 | `xo so mn`, `xổ số mn`, `xo số mn`, `xoso mn` |
| 59 | `xo-so` | **`xô sô mb`** | 673,000 | `xo so mb`, `xo sô mb`, `xô số mb`, `xổ số mb` (+1 khác) |
| 60 | `xo-so` | **`trực tiếp xổ số miền nam`** | 673,000 | `truc tiep xo so mien nam` |

---

## 4. C. SILO MỚI THEO TỪNG USE CASE (MẪU CÁC DỰ ÁN TRỌNG ĐIỂM)

Số trang mỗi Use Case thay đổi linh hoạt theo Search Demand thực tế (từ 1 đến 6 trang). Không còn slug cố định.

### Theme: `vietlott` (2,905,960 volume/tháng, 10 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/vietlott/` | Cẩm Nang & Bảng Tra Cứu Vietlott Mega & Power Toàn Diện | `vietlott` | 550,000 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Đặt Vé Số Vietlott Online Qua MoMo -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 2 | `/vietlott/mega-6-45/` | Mega 6/45 Vietlott Mega & Power: Hướng Dẫn & Tra Cứu Chi Tiết | `xổ số mega` | 357,400 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Đặt Vé Số Vietlott Online Qua MoMo -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 3 | `/vietlott/power-6-55/` | Power 6/55 Vietlott Mega & Power: Hướng Dẫn & Tra Cứu Chi Tiết | `xổ số power` | 288,370 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Đặt Vé Số Vietlott Online Qua MoMo -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 4 | `/vietlott/keno/` | Keno Vietlott Mega & Power: Hướng Dẫn & Tra Cứu Chi Tiết | `trực tiếp keno` | 208,030 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Đặt Vé Số Vietlott Online Qua MoMo -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 5 | `/vietlott/dai-ly-mua-ve/` | Đại lý & Mua vé online Vietlott Mega & Power: Hướng Dẫn & Tra Cứu Chi Tiết | `vietlott sms` | 132,040 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Đặt Vé Số Vietlott Online Qua MoMo -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 6 | `/vietlott/max-3d/` | Max 3D Vietlott Mega & Power: Hướng Dẫn & Tra Cứu Chi Tiết | `max3d` | 53,970 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Đặt Vé Số Vietlott Online Qua MoMo -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 7 | `/vietlott/bingo-18/` | Bingo 18 Vietlott Mega & Power: Hướng Dẫn & Tra Cứu Chi Tiết | `bingo18` | 2,230 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Đặt Vé Số Vietlott Online Qua MoMo -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 8 | `/vietlott/co-cau-trung-thuong/` | Cơ cấu & Trúng thưởng Vietlott Mega & Power: Hướng Dẫn & Tra Cứu Chi Tiết | `dò vé số vietlott` | 1,310 | `Đợt 2` | `TOFU` | Educational Guide & FAQ | `Đặt Vé Số Vietlott Online Qua MoMo -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 9 | `/vietlott/thu-tuc/` | Đăng ký & Hướng dẫn thủ tục Vietlott Mega & Power: Hướng Dẫn & Tra Cứu Chi Tiết | `muavietlott com` | 890 | `Đợt 1` | `BOFU` | Step-by-step How-to & Action Form | `Đặt Vé Số Vietlott Online Qua MoMo -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 10 | `/vietlott/lien-he/` | Cổng dịch vụ & Liên hệ Vietlott Mega & Power: Hướng Dẫn & Tra Cứu Chi Tiết | `tổng đài vietlott` | 540 | `Đợt 3` | `TOFU` | Directory & Service Portal | `Đặt Vé Số Vietlott Online Qua MoMo -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |

### Theme: `xo-so` (714,678,250 volume/tháng, 8 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/xo-so/` | Cẩm Nang & Bảng Tra Cứu Xổ Số Kiến Thiết 3 Miền Toàn Diện | `xsmn` | 101,000,000 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Dò Kết Quả & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 2 | `/xo-so/mien-bac/` | Xổ số Miền Bắc Xổ Số Kiến Thiết 3 Miền: Hướng Dẫn & Tra Cứu Chi Tiết | `xsmb` | 231,967,000 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Dò Kết Quả & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 3 | `/xo-so/quay-thu-truc-tiep/` | Quay thử & Trực tiếp Xổ Số Kiến Thiết 3 Miền: Hướng Dẫn & Tra Cứu Chi Tiết | `sxttmn` | 103,082,530 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Dò Kết Quả & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 4 | `/xo-so/cam-nang/` | Cẩm nang & Hỏi đáp Xổ Số Kiến Thiết 3 Miền: Hướng Dẫn & Tra Cứu Chi Tiết | `xổ số hôm nay` | 95,589,270 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Dò Kết Quả & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 5 | `/xo-so/mien-trung/` | Xổ số Miền Trung Xổ Số Kiến Thiết 3 Miền: Hướng Dẫn & Tra Cứu Chi Tiết | `xổ số miền trung` | 53,886,040 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Dò Kết Quả & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 6 | `/xo-so/thong-ke-soi-cau/` | Thống kê & Soi cầu Xổ Số Kiến Thiết 3 Miền: Hướng Dẫn & Tra Cứu Chi Tiết | `lô gan` | 5,262,420 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Dò Kết Quả & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 7 | `/xo-so/tra-cuu/` | Công cụ & Tra cứu Xổ Số Kiến Thiết 3 Miền: Hướng Dẫn & Tra Cứu Chi Tiết | `tra cứu kết quả xổ số` | 35,250 | `Đợt 1` | `BOFU` | Interactive Calculator / Lookup Tool | `Dò Kết Quả & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 8 | `/xo-so/co-cau-doi-thuong/` | Cơ cấu & Đổi thưởng Xổ Số Kiến Thiết 3 Miền: Hướng Dẫn & Tra Cứu Chi Tiết | `dự đoán trúng thưởng` | 22,720 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Dò Kết Quả & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |

### Theme: `ve-so` (399,360 volume/tháng, 6 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/ve-so/` | Cẩm Nang & Bảng Tra Cứu Dò Vé Số Trực Tuyến Toàn Diện | `dò vé số` | 74,000 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Dò Vé Số & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 2 | `/ve-so/cam-nang/` | Cẩm nang & Hỏi đáp Dò Vé Số Trực Tuyến: Hướng Dẫn & Tra Cứu Chi Tiết | `vé số` | 167,330 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Dò Vé Số & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 3 | `/ve-so/co-cau-giai-thuong/` | Cơ cấu giải thưởng vé số Dò Vé Số Trực Tuyến: Hướng Dẫn & Tra Cứu Chi Tiết | `vé số cào` | 7,730 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Dò Vé Số & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 4 | `/ve-so/thu-tuc/` | Đăng ký & Hướng dẫn thủ tục Dò Vé Số Trực Tuyến: Hướng Dẫn & Tra Cứu Chi Tiết | `mua vé số online` | 5,690 | `Đợt 1` | `BOFU` | Step-by-step How-to & Action Form | `Dò Vé Số & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 5 | `/ve-so/dai-ly-doi-ve/` | Đại lý & Điểm đổi vé Dò Vé Số Trực Tuyến: Hướng Dẫn & Tra Cứu Chi Tiết | `đại lý vé số đại phát` | 3,880 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Dò Vé Số & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |
| 6 | `/ve-so/tra-cuu/` | Công cụ & Tra cứu Dò Vé Số Trực Tuyến: Hướng Dẫn & Tra Cứu Chi Tiết | `vé số giải 4 bao nhiêu tiền` | 1,040 | `Đợt 1` | `BOFU` | Interactive Calculator / Lookup Tool | `Dò Vé Số & Đặt Vé Số Trực Tuyến -> Deeplink: momo://lottery -> Event: web_lottery_btn_click` |

### Theme: `gia-vang` (32,885,840 volume/tháng, 7 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/gia-vang/` | Cẩm Nang & Bảng Tra Cứu Giá Vàng Toàn Diện | `giá vàng hôm nay` | 9,140,000 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Mua Vàng Tích Lũy / Túi Thần Tài -> Deeplink: momo://gold-accumulation -> Event: web_gold_price_lookup_btn_click` |
| 2 | `/gia-vang/bieu-do-du-bao/` | Biểu đồ & Dự báo giá vàng Giá Vàng: Hướng Dẫn & Tra Cứu Chi Tiết | `giá vàng thế giới` | 7,046,260 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Mua Vàng Tích Lũy / Túi Thần Tài -> Deeplink: momo://gold-accumulation -> Event: web_gold_price_lookup_btn_click` |
| 3 | `/gia-vang/vang-doji-pnj/` | Giá vàng DOJI & PNJ Giá Vàng: Hướng Dẫn & Tra Cứu Chi Tiết | `giá vàng pnj` | 2,887,710 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Mua Vàng Tích Lũy / Túi Thần Tài -> Deeplink: momo://gold-accumulation -> Event: web_gold_price_lookup_btn_click` |
| 4 | `/gia-vang/gia-vang-sjc/` | Giá vàng SJC Giá Vàng: Hướng Dẫn & Tra Cứu Chi Tiết | `giá vàng sjc` | 1,402,950 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Mua Vàng Tích Lũy / Túi Thần Tài -> Deeplink: momo://gold-accumulation -> Event: web_gold_price_lookup_btn_click` |
| 5 | `/gia-vang/vang-nhan-9999/` | Vàng nhẫn 9999 & Vàng 24K Giá Vàng: Hướng Dẫn & Tra Cứu Chi Tiết | `giá vàng 9999 hôm nay` | 1,288,420 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Mua Vàng Tích Lũy / Túi Thần Tài -> Deeplink: momo://gold-accumulation -> Event: web_gold_price_lookup_btn_click` |
| 6 | `/gia-vang/thu-tuc/` | Đăng ký & Hướng dẫn thủ tục Giá Vàng: Hướng Dẫn & Tra Cứu Chi Tiết | `giá vàng mua vào hôm nay` | 3,280 | `Đợt 1` | `BOFU` | Step-by-step How-to & Action Form | `Mua Vàng Tích Lũy / Túi Thần Tài -> Deeplink: momo://gold-accumulation -> Event: web_gold_price_lookup_btn_click` |
| 7 | `/gia-vang/tra-cuu/` | Công cụ & Tra cứu Giá Vàng: Hướng Dẫn & Tra Cứu Chi Tiết | `tra cứu giá vàng` | 1,560 | `Đợt 1` | `BOFU` | Interactive Calculator / Lookup Tool | `Mua Vàng Tích Lũy / Túi Thần Tài -> Deeplink: momo://gold-accumulation -> Event: web_gold_price_lookup_btn_click` |

### Theme: `diem-tin-dung` (73,670 volume/tháng, 2 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/diem-tin-dung/` | Cẩm Nang & Bảng Tra Cứu Điểm Tín Dụng & Tra Cứu CIC Toàn Diện | `cic` | 60,500 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Tra cứu Điểm Tín Dụng & Hồ Sơ CIC -> Deeplink: momo://credit-score -> Event: web_cic_lookup_btn_click` |
| 2 | `/diem-tin-dung/xoa-no-xau/` | Xóa nợ xấu & Cải thiện điểm Điểm Tín Dụng & Tra Cứu CIC: Hướng Dẫn & Tra Cứu Chi Tiết | `điểm tín dụng cic` | 8,850 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Tra cứu Điểm Tín Dụng & Hồ Sơ CIC -> Deeplink: momo://credit-score -> Event: web_cic_lookup_btn_click` |

### Theme: `phat-nguoi` (1,588,890 volume/tháng, 3 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/phat-nguoi/` | Cẩm Nang & Bảng Tra Cứu Tra Cứu Phạt Nguội Toàn Quốc Toàn Diện | `tra cứu phạt nguội` | 673,000 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Nộp Phạt Nguội Giao Thông Toàn Quốc -> Deeplink: momo://traffic-fine -> Event: web_traffic_fine_lookup_btn_click` |
| 2 | `/phat-nguoi/cam-nang/` | Cẩm nang & Hỏi đáp Tra Cứu Phạt Nguội Toàn Quốc: Hướng Dẫn & Tra Cứu Chi Tiết | `kiểm tra phạt nguôi oto` | 29,200 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Nộp Phạt Nguội Giao Thông Toàn Quốc -> Deeplink: momo://traffic-fine -> Event: web_traffic_fine_lookup_btn_click` |
| 3 | `/phat-nguoi/tra-cuu/` | Công cụ & Tra cứu Tra Cứu Phạt Nguội Toàn Quốc: Hướng Dẫn & Tra Cứu Chi Tiết | `tra cứu phạt` | 1,680 | `Đợt 1` | `BOFU` | Interactive Calculator / Lookup Tool | `Nộp Phạt Nguội Giao Thông Toàn Quốc -> Deeplink: momo://traffic-fine -> Event: web_traffic_fine_lookup_btn_click` |

### Theme: `gui-tiet-kiem` (247,140 volume/tháng, 7 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/gui-tiet-kiem/` | Cẩm Nang & Bảng Tra Cứu Gửi Tiết Kiệm Toàn Diện | `tiết kiệm` | 27,100 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Mở Sổ Tiết Kiệm Online / Túi Thần Tài -> Deeplink: momo://saving-partner -> Event: web_saving_interest_calculator_btn_click` |
| 2 | `/gui-tiet-kiem/lai-suat-ngan-hang/` | Lãi suất ngân hàng Gửi Tiết Kiệm: Hướng Dẫn & Tra Cứu Chi Tiết | `lãi suất gửi tiết kiệm ngân hàng` | 120,470 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Mở Sổ Tiết Kiệm Online / Túi Thần Tài -> Deeplink: momo://saving-partner -> Event: web_saving_interest_calculator_btn_click` |
| 3 | `/gui-tiet-kiem/ky-han-hinh-thuc/` | Kỳ hạn & Hình thức gửi Gửi Tiết Kiệm: Hướng Dẫn & Tra Cứu Chi Tiết | `gửi tiết kiệm online có an toàn ko` | 18,520 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Mở Sổ Tiết Kiệm Online / Túi Thần Tài -> Deeplink: momo://saving-partner -> Event: web_saving_interest_calculator_btn_click` |
| 4 | `/gui-tiet-kiem/thu-tuc-mo-so/` | Thủ tục mở sổ & Rút tiền Gửi Tiết Kiệm: Hướng Dẫn & Tra Cứu Chi Tiết | `sổ tiết kiệm` | 17,370 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Mở Sổ Tiết Kiệm Online / Túi Thần Tài -> Deeplink: momo://saving-partner -> Event: web_saving_interest_calculator_btn_click` |
| 5 | `/gui-tiet-kiem/so-sanh-tiet-kiem/` | So sánh giải pháp tiết kiệm Gửi Tiết Kiệm: Hướng Dẫn & Tra Cứu Chi Tiết | `nên gửi tiết kiệm ngân hàng nào` | 3,430 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Mở Sổ Tiết Kiệm Online / Túi Thần Tài -> Deeplink: momo://saving-partner -> Event: web_saving_interest_calculator_btn_click` |
| 6 | `/gui-tiet-kiem/tra-cuu/` | Công cụ & Tra cứu Gửi Tiết Kiệm: Hướng Dẫn & Tra Cứu Chi Tiết | `gửi tiết kiệm 1 triệu 1 tháng lãi bao nhiêu vietcombank` | 2,650 | `Đợt 1` | `BOFU` | Interactive Calculator / Lookup Tool | `Mở Sổ Tiết Kiệm Online / Túi Thần Tài -> Deeplink: momo://saving-partner -> Event: web_saving_interest_calculator_btn_click` |
| 7 | `/gui-tiet-kiem/tinh-lai/` | Công cụ tính lãi Gửi Tiết Kiệm: Hướng Dẫn & Tra Cứu Chi Tiết | `gửi tiết kiệm 100 triệu 1 năm lãi bao nhiêu` | 1,510 | `Đợt 2` | `TOFU` | Educational Guide & FAQ | `Mở Sổ Tiết Kiệm Online / Túi Thần Tài -> Deeplink: momo://saving-partner -> Event: web_saving_interest_calculator_btn_click` |

### Theme: `tinh-luong` (145,060 volume/tháng, 4 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/tinh-luong/` | Cẩm Nang & Bảng Tra Cứu Tính Lương Gross Sang Net Toàn Diện | `lương gross la gi` | 9,900 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Tính Lương Gross Sang Net & Quản Lý Chi Tiêu -> Deeplink: momo://financial-management -> Event: web_gross_net_calculator_btn_click` |
| 2 | `/tinh-luong/bieu-phi-thu-tuc/` | Biểu phí & Thủ tục Tính Lương Gross Sang Net: Hướng Dẫn & Tra Cứu Chi Tiết | `cách tính lương hưu` | 48,210 | `Đợt 1` | `BOFU` | Interactive Calculator / Lookup Tool | `Tính Lương Gross Sang Net & Quản Lý Chi Tiêu -> Deeplink: momo://financial-management -> Event: web_gross_net_calculator_btn_click` |
| 3 | `/tinh-luong/tra-cuu/` | Công cụ & Tra cứu Tính Lương Gross Sang Net: Hướng Dẫn & Tra Cứu Chi Tiết | `tính lương gross sang net` | 44,350 | `Đợt 1` | `BOFU` | Interactive Calculator / Lookup Tool | `Tính Lương Gross Sang Net & Quản Lý Chi Tiêu -> Deeplink: momo://financial-management -> Event: web_gross_net_calculator_btn_click` |
| 4 | `/tinh-luong/thu-tuc/` | Đăng ký & Hướng dẫn thủ tục Tính Lương Gross Sang Net: Hướng Dẫn & Tra Cứu Chi Tiết | `các khoản phụ cấp không phải đóng bhxh` | 1,800 | `Đợt 1` | `BOFU` | Step-by-step How-to & Action Form | `Tính Lương Gross Sang Net & Quản Lý Chi Tiêu -> Deeplink: momo://financial-management -> Event: web_gross_net_calculator_btn_click` |

### Theme: `nap-game` (6,154,770 volume/tháng, 5 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/nap-game/` | Cẩm Nang & Bảng Tra Cứu Nạp Thẻ Game Toàn Diện | `nạp thẻ x5` | 2,740,000 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Nạp Thẻ Game Trực Tuyến Chiết Khấu Cao -> Deeplink: momo://game-topup -> Event: web_game_card_topup_btn_click` |
| 2 | `/nap-game/cam-nang/` | Cẩm nang & Hỏi đáp Nạp Thẻ Game: Hướng Dẫn & Tra Cứu Chi Tiết | `vltkm` | 14,040 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Nạp Thẻ Game Trực Tuyến Chiết Khấu Cao -> Deeplink: momo://game-topup -> Event: web_game_card_topup_btn_click` |
| 3 | `/nap-game/thu-tuc/` | Đăng ký & Hướng dẫn thủ tục Nạp Thẻ Game: Hướng Dẫn & Tra Cứu Chi Tiết | `mua card dien thoai` | 2,150 | `Đợt 1` | `BOFU` | Step-by-step How-to & Action Form | `Nạp Thẻ Game Trực Tuyến Chiết Khấu Cao -> Deeplink: momo://game-topup -> Event: web_game_card_topup_btn_click` |
| 4 | `/nap-game/tai-khoan-huong-dan/` | Tài khoản & Hướng dẫn Nạp Thẻ Game: Hướng Dẫn & Tra Cứu Chi Tiết | `scoin vtc` | 1,550 | `Đợt 2` | `TOFU` | Educational Guide & FAQ | `Nạp Thẻ Game Trực Tuyến Chiết Khấu Cao -> Deeplink: momo://game-topup -> Event: web_game_card_topup_btn_click` |
| 5 | `/nap-game/tua-game-su-kien/` | Tựa game & Sự kiện Nạp Thẻ Game: Hướng Dẫn & Tra Cứu Chi Tiết | `mua quân huy liên quân` | 1,020 | `Đợt 2` | `TOFU` | Educational Guide & FAQ | `Nạp Thẻ Game Trực Tuyến Chiết Khấu Cao -> Deeplink: momo://game-topup -> Event: web_game_card_topup_btn_click` |

### Theme: `dat-phim` (13,390 volume/tháng, 2 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/dat-phim/` | Cẩm Nang & Bảng Tra Cứu Đặt Vé Phim Online Toàn Diện | `đặt vé cgv` | 1,600 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Đặt Vé Phim & Chọn Ghế Rạp Rẻ Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click` |
| 2 | `/dat-phim/gia-ve-khuyen-mai/` | Giá vé & Khuyến mãi Đặt Vé Phim Online: Hướng Dẫn & Tra Cứu Chi Tiết | `combo bắp nước cgv` | 1,700 | `Đợt 2` | `TOFU` | Educational Guide & FAQ | `Đặt Vé Phim & Chọn Ghế Rạp Rẻ Nhất -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click` |

### Theme: `bhyt` (302,860 volume/tháng, 7 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/bhyt/` | Cẩm Nang & Bảng Tra Cứu Bảo Hiểm Y Tế (BHYT) Toàn Diện | `bảo hiểm y tế` | 74,000 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Gia Hạn Thẻ Bảo Hiểm Y Tế (BHYT) Online -> Deeplink: momo://bhyt-renew -> Event: web_bhyt_lookup_btn_click` |
| 2 | `/bhyt/bieu-phi-mua-online/` | Biểu phí & Mua bảo hiểm Bảo Hiểm Y Tế (BHYT): Hướng Dẫn & Tra Cứu Chi Tiết | `mua bảo hiểm y tế online` | 65,320 | `Đợt 1` | `BOFU` | Step-by-step How-to & Action Form | `Gia Hạn Thẻ Bảo Hiểm Y Tế (BHYT) Online -> Deeplink: momo://bhyt-renew -> Event: web_bhyt_lookup_btn_click` |
| 3 | `/bhyt/tra-cuu-han-dung/` | Tra cứu & Hạn sử dụng Bảo Hiểm Y Tế (BHYT): Hướng Dẫn & Tra Cứu Chi Tiết | `bhyt tra cứu` | 32,580 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Gia Hạn Thẻ Bảo Hiểm Y Tế (BHYT) Online -> Deeplink: momo://bhyt-renew -> Event: web_bhyt_lookup_btn_click` |
| 4 | `/bhyt/boi-thuong-quy-dinh/` | Quy định & Bồi thường Bảo Hiểm Y Tế (BHYT): Hướng Dẫn & Tra Cứu Chi Tiết | `luật bhyt 2024` | 3,200 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Gia Hạn Thẻ Bảo Hiểm Y Tế (BHYT) Online -> Deeplink: momo://bhyt-renew -> Event: web_bhyt_lookup_btn_click` |
| 5 | `/bhyt/quyen-loi-che-do/` | Quyền lợi & Chế độ Bảo Hiểm Y Tế (BHYT): Hướng Dẫn & Tra Cứu Chi Tiết | `mã bhyt ak được hưởng như thế nào` | 2,680 | `Đợt 1` | `TOFU` | Educational Guide & FAQ | `Gia Hạn Thẻ Bảo Hiểm Y Tế (BHYT) Online -> Deeplink: momo://bhyt-renew -> Event: web_bhyt_lookup_btn_click` |
| 6 | `/bhyt/thu-tuc/` | Đăng ký & Hướng dẫn thủ tục Bảo Hiểm Y Tế (BHYT): Hướng Dẫn & Tra Cứu Chi Tiết | `đăng ký bảo hiểm y tế` | 2,260 | `Đợt 1` | `BOFU` | Step-by-step How-to & Action Form | `Gia Hạn Thẻ Bảo Hiểm Y Tế (BHYT) Online -> Deeplink: momo://bhyt-renew -> Event: web_bhyt_lookup_btn_click` |
| 7 | `/bhyt/lien-he/` | Cổng dịch vụ & Liên hệ Bảo Hiểm Y Tế (BHYT): Hướng Dẫn & Tra Cứu Chi Tiết | `tổng đài bảo hiểm y tế` | 1,890 | `Đợt 2` | `TOFU` | Directory & Service Portal | `Gia Hạn Thẻ Bảo Hiểm Y Tế (BHYT) Online -> Deeplink: momo://bhyt-renew -> Event: web_bhyt_lookup_btn_click` |

### Theme: `vetc` (70,700 volume/tháng, 2 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/vetc/` | Cẩm Nang & Bảng Tra Cứu Thu Phí Tự Động VETC Toàn Diện | `vetc` | 40,500 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | `Nạp Tiền Thu Phí Tự Động VETC Không Dừng -> Deeplink: momo://etc-topup -> Event: web_etc_topup_btn_click` |
| 2 | `/vetc/cam-nang/` | Cẩm nang & Hỏi đáp Thu Phí Tự Động VETC: Hướng Dẫn & Tra Cứu Chi Tiết | `thu phí tự động` | 580 | `Đợt 3` | `TOFU` | Educational Guide & FAQ | `Nạp Tiền Thu Phí Tự Động VETC Không Dừng -> Deeplink: momo://etc-topup -> Event: web_etc_topup_btn_click` |

### Theme: `gdp` (32,510 volume/tháng, 1 trang được quy hoạch)

| STT | URL Slug | Tiêu Đề Trang Đích | Primary Keyword | Volume | Đợt Sản Xuất | Funnel | Format | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| 1 | `/gdp/` | Cẩm Nang & Bảng Tra Cứu Tổng Sản Phẩm Quốc Nội (GDP) Toàn Diện | `gdp` | 14,800 | `Đợt 1` | `TOFU` | Pillar Hub Page + Interactive Widget | *null (Không có tính năng MoMo)* |

---

## 5. D. DANH SÁCH CỤM BỊ LOẠI DO DƯỚI NGƯỠNG VOLUME (< 500/THÁNG)

Tổng cộng **605 cụm** có volume dưới ngưỡng 500/tháng bị loại bỏ khỏi danh mục trang độc lập và được tích hợp thành Section trong Pillar Page:

| STT | Theme | Phân Khối Ngành | Tên Cụm Bị Loại | Primary Keyword | Volume Cụm | Xử Lý Kiến Trúc |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| 1 | `Eximbank` | `Financial` | Giá vàng & Kim loại quý | `eximbank giá vàng` | 490 | Tích hợp thành Section trong Pillar Hub |
| 2 | `bao-hiem-nhan-tho` | `insurtech` | So sánh & Đánh giá | `so sánh các loại bảo hiểm nhân thọ` | 490 | Tích hợp thành Section trong Pillar Hub |
| 3 | `doi-pin` | `vehicle-hub` | Cổng dịch vụ & Liên hệ | `đổi mã pin vietcombank trên app` | 490 | Tích hợp thành Section trong Pillar Hub |
| 4 | `tram-sac` | `vehicle-hub` | Đăng ký & Hướng dẫn thủ tục | `đăng ký trạm sạc vinfast` | 490 | Tích hợp thành Section trong Pillar Hub |
| 5 | `agribank` | `Financial` | Công cụ & Tra cứu | `agribank 1 ngày chuyển được bao nhiêu tiền` | 470 | Tích hợp thành Section trong Pillar Hub |
| 6 | `chuyen-khoan` | `Financial` | Lãi suất & Tiền gửi | `gửi tiền qua viettel` | 460 | Tích hợp thành Section trong Pillar Hub |
| 7 | `gui-tiet-kiem` | `Financial` | Đăng ký & Hướng dẫn thủ tục | `mở tiết kiệm vietcombank` | 460 | Tích hợp thành Section trong Pillar Hub |
| 8 | `tinh-luong` | `Financial` | So sánh & Đánh giá | `gross to net topcv` | 460 | Tích hợp thành Section trong Pillar Hub |
| 9 | `tra-gop` | `Financial` | Tra cứu & Chi nhánh | `hd saison tổng đài` | 460 | Tích hợp thành Section trong Pillar Hub |
| 10 | `Shinhan Bank` | `Financial` | Vay vốn & Tín chấp | `shinhan bank vay tín chấp` | 450 | Tích hợp thành Section trong Pillar Hub |
| 11 | `co-phieu` | `Financial` | Thẻ & Tài khoản | `tài khoản chứng khoán` | 450 | Tích hợp thành Section trong Pillar Hub |
| 12 | `lai-suat` | `Financial` | Tỷ giá & Ngoại tệ | `lãi suất usd` | 450 | Tích hợp thành Section trong Pillar Hub |
| 13 | `phi-bao-hiem` | `insurtech` | Tra cứu & Hạn sử dụng | `phí bảo hiểm thẻ tín dụng vpbank` | 450 | Tích hợp thành Section trong Pillar Hub |
| 14 | `Techcombank` | `Financial` | So sánh & Đánh giá | `ưu đãi techcombank` | 440 | Tích hợp thành Section trong Pillar Hub |
| 15 | `nam-a-bank` | `Financial` | Tra cứu & Chi nhánh | `nam á bank hotline` | 440 | Tích hợp thành Section trong Pillar Hub |
| 16 | `thau-chi` | `Financial` | Biểu phí & Thủ tục | `cách tính lãi thấu chi` | 440 | Tích hợp thành Section trong Pillar Hub |
| 17 | `ACB` | `Financial` | Tra cứu & Chi nhánh | `địa chỉ ngân hàng acb` | 430 | Tích hợp thành Section trong Pillar Hub |
| 18 | `Shinhan Bank` | `Financial` | Biểu phí & Thủ tục | `tổng đài shinhan bank miễn phí` | 430 | Tích hợp thành Section trong Pillar Hub |
| 19 | `bac-a-bank` | `Financial` | Lãi suất & Tiền gửi | `bắc a bank lãi suất` | 430 | Tích hợp thành Section trong Pillar Hub |
| 20 | `gui-tiet-kiem` | `Financial` | Cổng dịch vụ & Liên hệ | `gửi tiết kiệm chi nhánh này rút chi nhánh khác được không` | 430 | Tích hợp thành Section trong Pillar Hub |
| 21 | `mua-truoc-tra-sau` | `Financial` | Vay vốn & Tín chấp | `vay kredivo có an toàn không` | 430 | Tích hợp thành Section trong Pillar Hub |
| 22 | `phi-bao-hiem` | `insurtech` | Quy định & Bồi thường | `bảo hiểm bắt buộc ô to 5 chỗ` | 430 | Tích hợp thành Section trong Pillar Hub |
| 23 | `ACB` | `Financial` | Cổng dịch vụ & Liên hệ | `acb login` | 420 | Tích hợp thành Section trong Pillar Hub |
| 24 | `mbbank` | `Financial` | Biểu phí & Thủ tục | `mbbank thu phí thường niên` | 420 | Tích hợp thành Section trong Pillar Hub |
| 25 | `tpbank` | `Financial` | Lãi suất & Tiền gửi | `tpbank lãi suất` | 420 | Tích hợp thành Section trong Pillar Hub |
| 26 | `tra-gop` | `Financial` | Đăng ký & Hướng dẫn thủ tục | `mua góp điện thoại` | 420 | Tích hợp thành Section trong Pillar Hub |
| 27 | `phan-mem-mo-phong` | `vehicle-hub` | Phạt nguội & Luật giao thông | `mô phỏng bằng lái xe` | 420 | Tích hợp thành Section trong Pillar Hub |
| 28 | `sacombank` | `Financial` | Cổng dịch vụ & Liên hệ | `website sacombank` | 410 | Tích hợp thành Section trong Pillar Hub |
| 29 | `nap-data` | `telco` | Cẩm nang & Hỏi đáp | `12mdt50` | 410 | Tích hợp thành Section trong Pillar Hub |
| 30 | `bhxh` | `insurtech` | Đăng ký & Hướng dẫn thủ tục | `thủ tục làm bảo hiểm xã hội` | 400 | Tích hợp thành Section trong Pillar Hub |
| 31 | `vpbank` | `Financial` | Biểu phí & Thủ tục | `điều kiện mở the tín dụng vpbank online` | 390 | Tích hợp thành Section trong Pillar Hub |
| 32 | `phim` | `cinema` | So sánh & Đánh giá | `heartstopper vietsub` | 390 | Tích hợp thành Section trong Pillar Hub |
| 33 | `bien-so-xe` | `vehicle-hub` | Bảo dưỡng & Nuôi xe | `thông tin đăng kiểm` | 390 | Tích hợp thành Section trong Pillar Hub |
| 34 | `ma-chung-khoan` | `Financial` | Đăng ký & Hướng dẫn thủ tục | `nên mua mã chứng khoán nào hôm nay` | 380 | Tích hợp thành Section trong Pillar Hub |
| 35 | `tien-so` | `Financial` | Thẻ & Tài khoản | `số tiền phong tỏa trong thẻ tín dụng là gì` | 380 | Tích hợp thành Section trong Pillar Hub |
| 36 | `vi-tra-sau` | `Financial` | Lãi suất & Tiền gửi | `lãi suất ví trả sau momo` | 380 | Tích hợp thành Section trong Pillar Hub |
| 37 | `ma-so-thue` | `other` | Cổng dịch vụ & Liên hệ | `đăng nhập thuế cá nhân` | 380 | Tích hợp thành Section trong Pillar Hub |
| 38 | `voucher` | `other` | So sánh & Đánh giá | `voucher khuyến mãi` | 380 | Tích hợp thành Section trong Pillar Hub |
| 39 | `Eximbank` | `Financial` | Thẻ & Tài khoản | `eximbank thẻ tín dụng` | 370 | Tích hợp thành Section trong Pillar Hub |
| 40 | `vib` | `Financial` | So sánh & Đánh giá | `ưu đãi vib` | 370 | Tích hợp thành Section trong Pillar Hub |
| 41 | `crypto` | `Financial` | So sánh & Đánh giá | `cryptopanic` | 360 | Tích hợp thành Section trong Pillar Hub |
| 42 | `kien-long-bank` | `Financial` | Tra cứu & Chi nhánh | `tổng đài kienlongbank` | 360 | Tích hợp thành Section trong Pillar Hub |
| 43 | `tai-san` | `Financial` | Biểu phí & Thủ tục | `thủ tục từ chối tài sản` | 360 | Tích hợp thành Section trong Pillar Hub |
| 44 | `vietlott` | `Lottery` | Công cụ & Tra cứu | `vietlott bao nhiêu tiền` | 360 | Tích hợp thành Section trong Pillar Hub |
| 45 | `lam-phat` | `Financial` | Lãi suất & Tiền gửi | `lạm phát tăng thì lãi suất tăng hay giảm` | 350 | Tích hợp thành Section trong Pillar Hub |
| 46 | `rap` | `cinema` | Review & Đánh giá phim | `phim hay rap` | 350 | Tích hợp thành Section trong Pillar Hub |
| 47 | `du-lich-singapore` | `ota` | Cẩm nang & Hỏi đáp | `chi phí đi singapore` | 350 | Tích hợp thành Section trong Pillar Hub |
| 48 | `co-tuc` | `Financial` | Đăng ký & Hướng dẫn thủ tục | `mua cổ phiếu có được trả cổ tức không` | 340 | Tích hợp thành Section trong Pillar Hub |
| 49 | `tien-so` | `Financial` | Lãi suất & Tiền gửi | `rút tiền từ số dư tk shopee` | 330 | Tích hợp thành Section trong Pillar Hub |
| 50 | `tien-so` | `Financial` | Đăng ký & Hướng dẫn thủ tục | `số tiền đã nạp valorant` | 320 | Tích hợp thành Section trong Pillar Hub |

---

## 6. E. THỐNG KÊ MAPPING ĐIỂM CHẠM WEB-TO-APP (CTA HOOK)

- **Tổng số Use Cases:** 190
- **Số Use Case có CTA Hook cụ thể:** **58** (30.5%)
- **Số Use Case trả về `null`:** **132** (69.5%)
- **Nguyên tắc kỹ thuật:** Đã xóa bỏ hoàn toàn câu fallback chung *"Tích hợp Widget tương tác trên Web -> Deeplink mở MoMo App kích hoạt dịch vụ"*. Chỉ điền khi map được tính năng MoMo cụ thể gồm: `Tên Tính Năng -> Deeplink Đích -> Event Đo Lường`.
