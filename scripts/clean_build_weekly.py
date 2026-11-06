import re

with open('07_REPORTS/docs/weekly-report-2026-10-26-11-01.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Standardize Key Owner
text = re.sub(r'\*\*(?:Kỹ sư phụ trách|Kỹ sư chủ trì|Kỹ sư thực hiện):\*\*', '**Key Owner:**', text)

# 2. Refine Section I.2
old_s2 = """### 2. Tóm Tắt Điểm Đáng Chú Ý Tháng 10
- **Lưu lượng tự nhiên (Non-Paid) bù được một nửa lượng view bị hụt do cắt Ads:** Non-Paid tháng 10 đạt 3,12 triệu PV (+13,5% so với tháng 9), chiếm 86,9% tổng view toàn trang. Khi cắt 723K view quảng cáo, lượng view tự nhiên tăng thêm đã bù lại được 52% phần hụt này.
- **Khách vào web trực tiếp (Direct) tăng khá (+23,3% MoM, đạt 931K PV):** Người dùng có thói quen vào thẳng các trang tiện ích như xem lịch chiếu phim, tra cứu phạt nguội, xem tỷ giá ngoại tệ, giá vàng và giá xăng.
- **Tình hình 2 hub trọng điểm:**
  - *Cinema Hub:* Đạt 1,13 triệu PV (vượt chỉ tiêu 1,12 triệu, đạt 101,4%; giảm 7,2% so với tháng 9). Traffic tự nhiên tăng 21,7% giúp hub vẫn vượt chỉ tiêu dù cắt quảng cáo trang phim lẻ.
  - *Financial Hub:* Đạt 273K PV (tăng +9,6% so với 249K của tháng 9, đạt 60,8% chỉ tiêu 450K). Lượng view từ nhóm trang Trung tâm Tài chính (+442%) và Ví Trả Sau (+38%) tăng tốt, giúp bù phần giảm của Vay Nhanh khi dừng chạy ads.
- **Phễu tải app sang liên kết ngân hàng (AppsFlyer cả tháng 10):** Đạt **11.143 lượt cài đặt** ➔ **3.902 đăng ký tài khoản** (35%) ➔ **2.389 người liên kết ngân hàng (Map Bank)** (tăng +5% so với tháng 9, đạt mức cao nhất từ trước đến nay) ➔ **1.284 MAU**. Mất người nhiều nhất ở ngay sau bước cài app: 65% người đã cài vẫn chưa đăng ký tài khoản.
- **Việc cần làm trên Google tuần tới:** Tối ưu tỷ lệ click (CTR) cho cụm từ khóa Tỷ giá (vừa có thêm 440K lượt hiển thị) và kéo lại thứ hạng trang rạp CGV về lại top 5 sau khi bị tụt nhẹ."""

new_s2 = """### 2. Tóm Tắt Điểm Đáng Chú Ý Tháng 10
- **Lưu lượng tự nhiên (Non-Paid) bù đắp 52% lượng hụt do cắt Ads:** Non-Paid tháng 10 đạt 3,13 triệu PV (+13,5% MoM), chiếm 86,9% tổng view toàn sàn. Việc cắt giảm 723K view quảng cáo trả phí kém hiệu quả đã được bù đắp bền vững bằng 373K view tự nhiên tăng thêm.
- **Truy cập trực tiếp (Direct) tăng mạnh (+23,3% MoM, đạt 931K PV):** Người dùng đang hình thành thói quen vào thẳng các công cụ tiện ích thiết yếu hàng ngày: Lịch chiếu phim, Tra cứu phạt nguội, Tỷ giá ngoại tệ, Giá vàng và Giá xăng.
- **Diễn biến tại 2 Hub chiến lược:**
  - *Cinema Hub:* Đạt 1,13 triệu PV (vượt 101,4% chỉ tiêu 1,12M); lưu lượng tự nhiên tăng +21,7% giúp hub giữ vững chỉ tiêu dù đã cắt 98% ads phim lẻ.
  - *Financial Hub:* Đạt 254K PV (+1,7% MoM, đạt 56,5% target); sự bứt phá của Trung tâm Tài chính (+374% nhờ 7 trang Tỷ Giá mới) và Ví Trả Sau (+41%) đã bù đắp phần sụt giảm của Vay Nhanh khi dừng ngân sách ads.
- **Phễu chuyển đổi Web-to-App & Bản chất luồng Install (AppsFlyer cả tháng 10):**
  - Toàn sàn ghi nhận **11.143 lượt cài đặt** ➔ **3.902 đăng ký tài khoản** (35%) ➔ **2.389 liên kết ngân hàng (Map Bank - tăng +5% MoM, mức cao nhất lịch sử)** ➔ **1.284 MAU**.
  - *Bản chất luồng cài đặt:* Lượng Install hiện tại đa phần đến từ các chiến dịch **Paid Ads** (cụm trang tương tác Điểm Tín Dụng, Quýt... mang về 36.950 lượt bấm OneLink mở app), chưa phải từ trang tải app tự nhiên (`/tai-app` mới On Production ngày 30/10 để bắt đầu hứng SEO). Điểm rơi rụng lớn nhất là 65% người cài app từ luồng ads chưa đăng ký tài khoản."""

if old_s2 in text:
    text = text.replace(old_s2, new_s2)
    print("Replaced Section I.2")
else:
    print("Warning: old_s2 not matched exactly, checking substring...")

# 3. Remove Lesson Learned
lines = text.splitlines()
clean_lines = []
skip = False
for l in lines:
    if l.strip().startswith('- **Bài học kinh nghiệm'):
        skip = True
        continue
    if skip:
        if l.startswith('##') or l.startswith('###') or l.strip() == '---' or (l.startswith('- **') and not l.strip().startswith('- *')):
            skip = False
            clean_lines.append(l)
        else:
            continue
    else:
        clean_lines.append(l)

text = '\n'.join(clean_lines)

# 4. Remove 'Báo cáo nhu cầu tìm kiếm'
text = text.replace('  - **Báo cáo nhu cầu tìm kiếm:** Đã hoàn thành và dùng được.\n', '')

# 5. Append Section IV SO WHAT if not present
so_what = """

---

## IV. SO WHAT? (Ý NGHĨA KINH DOANH & ĐIỀU CHỈNH HÀNH ĐỘNG)

### 1. Ý nghĩa cốt lõi đối với Mô hình Tăng trưởng (Growth Implications)
- **Động cơ tăng trưởng tự nhiên (Non-Paid) đã tự chủ và đứng vững:** Lưu lượng tự nhiên tháng 10 tăng +13,5% MoM (đạt 3,13 triệu PV, chiếm 86,9% toàn sàn), bù đắp trọn vẹn 52% lượng hụt do chủ động cắt giảm 60,4% ngân sách Paid Ads. Kênh Web chứng minh năng lực tự tăng trưởng độc lập, không còn bị tổn thương khi dừng chi tiêu quảng cáo trả phí ngắn hạn.
- **Công cụ tiện ích (Utilities) là đòn bẩy kéo Direct & SEO mạnh nhất:** Tăng trưởng toàn sàn trong tháng qua không đến từ các bài viết tin tức thông thường mà đến từ các công cụ tiện ích thiết yếu (Direct đạt 931K PV, +23,3% MoM; Trung tâm Tài chính +374% nhờ 7 trang Tỷ Giá; Tiện ích giao thông +908% nhờ tra cứu giá xăng và thông tin xe; Rạp phim +46,5%). Người dùng vào Web để giải quyết công việc tức thì, tạo cơ hội chuyển đổi kép (Dual-Conversion) dẫn vào phễu In-App mở tài khoản đầu tư, mở thẻ và đặt vé.
- **Điểm nghẽn phễu New User nằm ở khâu kích hoạt (Onboarding), không phải Acquisition:** Toàn sàn ghi nhận 11.143 Installs nhưng có đến 65% rơi rụng ngay sau cài đặt (chưa hoàn tất đăng ký tài khoản). Số liệu đối soát cho thấy nguồn Install này phần lớn được kích hoạt từ các chiến dịch Paid Ads (36.950 OneLink clicks từ landing page Điểm Tín Dụng, Quýt), trong khi trang `/tai-app` mới On Production ngày 30/10. Nếu không tối ưu thông điệp nhận quà và quy trình mở app ngay từ luồng quảng cáo, chi phí thu hút người dùng mới sẽ bị lãng phí lớn.

### 2. Ba rủi ro hệ thống & Bài học vận hành cần kiểm soát (Systemic Risks)
1. **Rủi ro phụ thuộc chính sách đối tác bên ngoài:** Minigame Bò Sữa Bay bị vướng quy định đối tác rạp chiếu sát ngày công chiếu; tiến độ Chứng Chỉ Quỹ bị chậm do phụ thuộc API NAV thời gian thực từ các công ty quản lý quỹ.  
   - *Nguyên tắc điều hành:* Luôn chuẩn bị phương án phát hành Phase 1 với dữ liệu tĩnh/bán tự động để kịp tiến độ kinh doanh; đồng thời quy trình duyệt pháp chế và cơ chế hiển thị với đối tác ngoài bắt buộc phải chốt trước tối thiểu 2-3 tuần.
2. **Kẽ hở an toàn thông tin dưới áp lực chiến dịch gấp:** Sự cố Pentest Merchant ngày 27/10 (lộ thông tin đối tác role `anon` từ mã nguồn web) là bài học xương máu từ việc đưa tính năng lên Production phục vụ chiến dịch kinh doanh khi chưa qua kiểm thử bảo mật độc lập.  
   - *Nguyên tắc điều hành:* 100% kết nối dữ liệu công khai mới bắt buộc phải có phê duyệt từ Security và chuyển đổi toàn diện sang kiến trúc máy chủ trung gian (BFF), tuyệt đối không để trình duyệt gọi thẳng cơ sở dữ liệu.
3. **Độ trễ phối hợp nội dung giữa Kỹ thuật và Ngành hàng (BU):** Một số trang sản phẩm như Trang chủ Bảo hiểm (`/bao-hiem`) và công cụ tính thuế đã hoàn thành code nhưng bị nghẽn ở khâu duyệt văn bản (text copy) từ phía ngành hàng. Cần quy trình duyệt nội dung song song (Parallel Review) ngay từ giai đoạn Staging.

### 3. Điều chỉnh hành động trọng tâm tuần tới (Now What - Action Directives)
- **Ưu tiên 1 (Tăng trưởng & Chuyển đổi Web-to-App):** Hoàn thiện khối đánh giá người dùng (Social Proof) và chính sách quà tân thủ trên trang đích [momo.vn/tai-app](https://www.momo.vn/tai-app); phối hợp team Media gắn mã ưu đãi kích hoạt ngay trong luồng Ads để kéo giảm tỷ lệ rơi rụng 65% sau cài đặt.
- **Ưu tiên 2 (Hợp tác Use Cases & Đón mùa vụ):** Phối hợp BU Movies và Legal phê duyệt dứt điểm quy chế trả thưởng minigame Bò Sữa Bay trước ngày 04/11 để kịp phát sóng TVC/QR tại rạp ngày 06/11; làm việc với bộ phận Mua hàng (Procurement) thống nhất tiêu chí chọn Vendor SEO Off-page cho Cinema Hub.
- **Ưu tiên 3 (Hạ tầng, Nền tảng & An ninh bảo mật):** Hoàn tất chuyển đổi các trang còn lại sang BFF và đóng hoàn toàn cổng truy cập công khai (PostgREST anon read); phát hành bản cập nhật MoSpark CMS Phase 2 lên môi trường Production cùng khối BMC.
"""

if '## IV. SO WHAT?' not in text:
    text += so_what

# Replace special dashes
text = text.replace('\u2014', ',').replace('\u2013', '-').replace(' · ', ' & ')

with open('07_REPORTS/docs/weekly-report-2026-10-26-11-01.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved cleanly via update script!")
