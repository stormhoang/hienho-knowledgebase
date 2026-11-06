import sys

with open('07_REPORTS/docs/weekly-report-2026-10-26-11-01.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Cinema Hub
old_cinema = """- **Công việc thực tế đã làm trong tuần:**
  - **Lên Production trang danh sách diễn viên tổng (`/cinema/person`):**"""
new_cinema = """- **Bối cảnh & Bài toán:**
  - Dữ liệu nghệ sĩ/diễn viên trước đây chỉ nằm rải rác ở từng trang chi tiết phim, thiếu trang Hub tập trung làm hạn chế SEO liên kết nội bộ `Phim ↔ Nghệ sĩ` và người xem không có nơi tra cứu danh sách phim theo thần tượng.
  - Các suất chiếu Cinetour (giao lưu đoàn làm phim) là "nam châm" hút khách nhưng trước đây bị lẫn vào suất thường, khán giả không biết suất nào có nghệ sĩ. Backend vừa ra mắt API Suất chiếu mới thời gian thực cần tích hợp gấp.
  - Minigame tương tác Bò Sữa Bay cần chạy đua tiến độ để kịp chiến dịch công chiếu toàn quốc ngày 06/11.
- **Công việc thực tế đã làm trong tuần:**
  - **Lên Production trang danh sách diễn viên tổng (`/cinema/person`):**"""
if old_cinema in text:
    text = text.replace(old_cinema, new_cinema, 1)
    print("1. Cinema Hub: OK")
else:
    print("1. Cinema Hub: FAILED")

# 2. Financial Hub
old_fin = """- **Công việc thực tế đã làm trong tuần:**
  - **Trang Chứng Chỉ Quỹ (`/tai-chinh/chung-chi-quy` - Staging):**"""
new_fin = """- **Bối cảnh & Bài toán:**
  - *Chứng Chỉ Quỹ:* Thuộc trụ cột Đầu Tư & Tích Sản (Quick Win P0), đóng vai trò phễu chuyển đổi dẫn người dùng ngại rủi ro sang tích sản định kỳ từ 10.000đ; do API NAV realtime từ đối tác chưa sẵn sàng nên team chốt triển khai Phase 1 với dữ liệu bán tự động để kịp tiến độ.
  - *Thuế TNCN:* Cụm nhu cầu lớn (~1,16 triệu lượt tìm kiếm) giải quyết bài toán tự tính và chuẩn bị quyết toán thuế cho người có thu nhập đa nguồn (lương, freelance, vãng lai 10%) mà không cần đăng nhập.
  - *Thuế Hộ Kinh Doanh:* Đón đầu Thông tư 40 và ngưỡng doanh thu mới 200 triệu cho hơn 5,2 triệu hộ kinh doanh cá thể và người bán hàng online (Shopee, TikTok Shop), đồng thời là tệp khách hàng tiềm năng mở QR/Soundbox MoMo.
- **Công việc thực tế đã làm trong tuần:**
  - **Trang Chứng Chỉ Quỹ (`/tai-chinh/chung-chi-quy` - Staging):**"""
if old_fin in text:
    text = text.replace(old_fin, new_fin, 1)
    print("2. Financial Hub: OK")
else:
    print("2. Financial Hub: FAILED")

# 3. Vehicle Hub
old_veh = """- **Công việc thực tế đã làm trong tuần:**
  - **Danh sách gara mới ([momo.vn/tien-ich-giao-thong/garage](https://www.momo.vn/tien-ich-giao-thong/garage)):**"""
new_veh = """- **Bối cảnh & Bài toán:**
  - Chủ xe hiện phải dùng nhiều trang/ứng dụng rời rạc để tra phạt nguội, tìm cây xăng, gara và mua bảo hiểm. Vehicle Hub gom các tiện ích này lên momo.vn để đón người dùng từ Google, tạo hồ sơ xe rồi dẫn sang ứng dụng MoMo (Mục tiêu Phase 1: 500K PV, 250K đăng nhập, 100K hồ sơ xe).
  - Khách mua bảo hiểm ô tô cần xem danh sách gara chính hãng có liên kết bảo lãnh bồi thường gần vị trí hiện tại nhất để an tâm ra quyết định.
- **Công việc thực tế đã làm trong tuần:**
  - **Danh sách gara mới ([momo.vn/tien-ich-giao-thong/garage](https://www.momo.vn/tien-ich-giao-thong/garage)):**"""
if old_veh in text:
    text = text.replace(old_veh, new_veh, 1)
    print("3. Vehicle Hub: OK")
else:
    print("3. Vehicle Hub: FAILED")

# 4. Insurtech Hub
old_ins = """- **Kỹ sư thực hiện:** thuan.vo
- **Công việc thực tế đã làm trong tuần:**"""
new_ins = """- **Kỹ sư thực hiện:** thuan.vo
- **Bối cảnh & Bài toán:** Trang chủ Bảo hiểm đóng vai trò cửa ngõ gom 9 nhóm sản phẩm bảo hiểm số và các tiện ích tính toán (BHYT, BHXH, báo giá xe). Người mua bảo hiểm vật chất ô tô thường băn khoăn về mức khấu trừ (miễn thường) ảnh hưởng thế nào đến phí mua hàng năm, cần công cụ trực quan để tự chọn gói phù hợp.
- **Công việc thực tế đã làm trong tuần:**"""
if old_ins in text:
    text = text.replace(old_ins, new_ins, 1)
    print("4. Insurtech Hub: OK")
else:
    print("4. Insurtech Hub: FAILED")

# 5. New User Hub
old_nu = """- **Kỹ sư thực hiện:** thuan.vo
- **Công việc thực tế đã làm trong tuần:**"""
new_nu = """- **Kỹ sư thực hiện:** thuan.vo
- **Bối cảnh & Bài toán:** Kênh Web cần một trang đích chính thức (/tai-app) đồng bộ nhận diện thương hiệu, tối ưu trải nghiệm đa thiết bị (mobile tự điều hướng vào kho ứng dụng, desktop hiển thị mã QR sắc nét) để thu hút và chuyển đổi người dùng mới (New User) từ nguồn tìm kiếm và chiến dịch truyền thông ngoài.
- **Công việc thực tế đã làm trong tuần:**"""
if old_nu in text:
    text = text.replace(old_nu, new_nu, 1)
    print("5. New User Hub: OK")
else:
    print("5. New User Hub: FAILED")

# 6. Lottery Hub
old_lot = """- **Kỹ sư thực hiện:** duy.tran2
- **Công việc thực tế đã làm trong tuần:**"""
new_lot = """- **Kỹ sư thực hiện:** duy.tran2
- **Bối cảnh & Bài toán:** Nhóm dịch vụ Vé số có lượng truy cập tăng vọt cục bộ vào khung giờ mở thưởng hàng ngày (18h00 - 18h30); đồng thời ngành hàng (PO) cần công cụ CMS để tự chủ động thay đổi nội dung banner, khuyến mãi mà không phải phụ thuộc kỹ sư can thiệp code.
- **Công việc thực tế đã làm trong tuần:**"""
if old_lot in text:
    text = text.replace(old_lot, new_lot, 1)
    print("6. Lottery Hub: OK")
else:
    print("6. Lottery Hub: FAILED")

# 7. Chatbot AI & KB
old_chat = """- **Kỹ sư chủ trì:** duy.tran2
- **Công việc thực tế đã làm trong tuần:**"""
new_chat = """- **Kỹ sư chủ trì:** duy.tran2
- **Bối cảnh & Bài toán:** Trước đây tài liệu tri thức quản lý phân tán theo từng màn hình riêng lẻ, người quản trị không nắm được tổng thể dự án nào thiếu/đủ tài liệu khiến AI trả lời thiếu chính xác; việc kiểm tra bài viết mới từ sitemap bằng tay rất tốn công; nếu nạp cả bài nháp hoặc trang toàn ảnh quảng cáo sẽ gây hiện tượng "ảo giác" (hallucination) cho Chatbot.
- **Công việc thực tế đã làm trong tuần:**"""
if old_chat in text:
    text = text.replace(old_chat, new_chat, 1)
    print("7. Chatbot AI: OK")
else:
    print("7. Chatbot AI: FAILED")

# 8. Admin Panel
old_adm = """- **Kỹ sư chủ trì:** hieu.nguyen8, duy.tran2
- **Công việc thực tế đã làm trong tuần:**"""
new_adm = """- **Kỹ sư chủ trì:** hieu.nguyen8, duy.tran2
- **Bối cảnh & Bài toán:** Biên tập viên gặp khó khăn khi phải chuyển qua lại giữa nhiều màn hình soạn thảo, danh sách bài và xem trước; các nút mở app thường xuyên bị lỗi mất điều hướng do quên nhập mã tính năng (`featureCode`); hệ thống chuẩn bị nghiệm thu Phase 2 để bàn giao cho khối BMC quản trị nội dung in-app toàn diện.
- **Công việc thực tế đã làm trong tuần:**"""
if old_adm in text:
    text = text.replace(old_adm, new_adm, 1)
    print("8. Admin Panel: OK")
else:
    print("8. Admin Panel: FAILED")

# 9. Search
old_search = """- **Kỹ sư chủ trì:** hieu.nguyen8
- **Công việc thực tế đã làm trong tuần:**"""
new_search = """- **Kỹ sư chủ trì:** hieu.nguyen8
- **Bối cảnh & Bài toán:** Người dùng có thói quen gõ thẳng số điện thoại người nhận vào ô tìm kiếm trên website momo.vn, nhưng trước đây hệ thống chỉ trả về trang trắng không có kết quả, gây đứt gãy luồng chuyển tiền và lãng phí lượng truy cập tự nhiên.
- **Công việc thực tế đã làm trong tuần:**"""
if old_search in text:
    text = text.replace(old_search, new_search, 1)
    print("9. Search: OK")
else:
    print("9. Search: FAILED")

# 10. URL Catalog
old_url = """- **Kỹ sư chủ trì:** hieu.nguyen8
- **Công việc thực tế đã làm trong tuần:**"""
new_url = """- **Kỹ sư chủ trì:** hieu.nguyen8
- **Bối cảnh & Bài toán:** Dữ liệu đường dẫn URL của website đang phân tán ở nhiều nguồn, thiếu một kho dữ liệu trung tâm chuẩn (Single Source of Truth) để phục vụ đồng thời Cổng tìm kiếm, tạo sơ đồ website (Sitemap SEO) theo dự án và cung cấp danh mục URL sạch cho đội AI xây dựng Cơ sở tri thức.
- **Công việc thực tế đã làm trong tuần:**"""
if old_url in text:
    text = text.replace(old_url, new_url, 1)
    print("10. URL Catalog: OK")
else:
    print("10. URL Catalog: FAILED")

# 11. Security & BFF
old_sec = """- **Kỹ sư thực hiện:** hieu.nguyen8, loc.le4, thuan.vo
- **Công việc thực tế đã làm trong tuần:**"""
new_sec = """- **Kỹ sư thực hiện:** hieu.nguyen8, loc.le4, thuan.vo
- **Bối cảnh & Bài toán:** Lúc 15:11 ngày 27/10, ITC thông báo kết quả Pentest phát hiện role `anon` có thể đọc được 218.243 bản ghi đối tác qua mã nguồn công khai của website (tính năng tra cứu cửa hàng làm gấp cho chiến dịch Mega Hoàn tiền 50%); hệ thống cần lập tức khoanh vùng bảo mật, làm sạch dữ liệu nhạy cảm và chuyển đổi toàn diện sang kiến trúc máy chủ trung gian (BFF) để đóng cổng truy cập công khai.
- **Công việc thực tế đã làm trong tuần:**"""
if old_sec in text:
    text = text.replace(old_sec, new_sec, 1)
    print("11. Security & BFF: OK")
else:
    print("11. Security & BFF: FAILED")

# 12. MoBase Design System
old_mob = """- **Kỹ sư thực hiện:** hung.nguyen9
- **Công việc thực tế đã làm trong tuần:**"""
new_mob = """- **Kỹ sư thực hiện:** hung.nguyen9
- **Bối cảnh & Bài toán:** Header hiện tại trên trang chủ momo.vn là phiên bản cũ, cấu trúc đơn tầng, thiếu tính linh hoạt khi cần hiển thị đồng thời nhiều dịch vụ, chương trình ưu đãi hoặc chiến dịch lớn; cần nâng cấp lên component Header Advance (Navigation 2 tầng) chuẩn MoBase Design System.
- **Công việc thực tế đã làm trong tuần:**"""
if old_mob in text:
    text = text.replace(old_mob, new_mob, 1)
    print("12. MoBase: OK")
else:
    print("12. MoBase: FAILED")

# 13. Web Performance
old_perf = """- **Kỹ sư thực hiện:** thuan.vo
- **Công việc thực tế đã làm trong tuần:**"""
new_perf = """- **Kỹ sư thực hiện:** thuan.vo
- **Bối cảnh & Bài toán:** Đội ngũ sản phẩm (PM) và các BU cần chủ động theo dõi hiệu suất GA4 và Google Search Console trực tiếp trong MoSpark Admin để kịp thời điều chỉnh nội dung, nhưng cần đảm bảo phân quyền an toàn dữ liệu và kết nối máy chủ độc lập.
- **Công việc thực tế đã làm trong tuần:**"""
if old_perf in text:
    text = text.replace(old_perf, new_perf, 1)
    print("13. Web Performance: OK")
else:
    print("13. Web Performance: FAILED")

# 14. Quiz Blog
old_quiz = """- **Kỹ sư thực hiện:** thuan.vo
- **Công việc thực tế đã làm trong tuần:**"""
new_quiz = """- **Kỹ sư thực hiện:** thuan.vo
- **Bối cảnh & Bài toán:** Các bài viết blog kiến thức tài chính thuần văn bản thường có tỷ lệ thoát trang cao, người đọc khó tự đánh giá nhu cầu cá nhân; cần công cụ trắc nghiệm (Interactive Quiz/Calculator) nhúng trực tiếp vào thân bài để tăng thời gian lưu trang và dẫn phễu mở thẻ/kiểm tra điểm tín dụng.
- **Công việc thực tế đã làm trong tuần:**"""
if old_quiz in text:
    text = text.replace(old_quiz, new_quiz, 1)
    print("14. Quiz Blog: OK")
else:
    print("14. Quiz Blog: FAILED")

with open('07_REPORTS/docs/weekly-report-2026-10-26-11-01.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved cleanly!")
