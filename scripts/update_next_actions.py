import os

path = '07_REPORTS/docs/weekly-report-2026-10-26-11-01.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace project 1
old_p1 = '''- **Điểm nghẽn:** Chờ Legal phê duyệt luật chơi và BU Movies duyệt kịch bản TVC minigame tại rạp trước ngày chiếu 06/11.
---'''
new_p1 = '''- **Next Action:** Hoàn thiện render giao diện gắn Badge Cinetour và luồng CTA đặt vé nhanh; phối hợp BU Movies và Legal chốt phương án minigame Bò Sữa Bay trước ngày chiếu 06/11; làm việc với Procurement để chọn đối tác SEO Off-page cho Cinema Hub.
- **Collaboration:** Phối hợp **Bình, Thức (BU Movies)** duyệt kịch bản TVC minigame; **Pháp chế (Legal)** duyệt thể lệ minigame; **Phòng Mua hàng (Procurement)** thống nhất tiêu chí chọn Vendor SEO Off-page.
---'''

assert old_p1 in text, "old_p1 not found"
text = text.replace(old_p1, new_p1)

# Find old_p2 accurately
old_p2_needle = "- **Kế hoạch tuần tới:**\n  - Nghiên cứu và dựng tiếp công cụ"
assert old_p2_needle in text, "old_p2_needle not found"

# Let's inspect the exact lines around old_p2
p2_start = text.find("- **Kế hoạch tuần tới:**\n  - Nghiên cứu và dựng tiếp công cụ")
p2_end = text.find("---\n\n### 3. Vehicle Hub:", p2_start)
old_p2 = text[p2_start:p2_end]

new_p2 = '''- **Next Action:** Research nhu cầu và dựng công cụ Chia hóa đơn & Quỹ nhóm (`/tai-chinh/cong-cu/chia-tien-du-lich`) kèm Simulator và CTA in-app; nghiên cứu cấu trúc trang Hub Công Cụ (`/tai-chinh/cong-cu`); mở rộng các trang tỷ giá đảo VND sang ngoại tệ.
- **Collaboration:** Phối hợp **BU Tài chính (Financial Services)** duyệt nội dung trang Chứng Chỉ Quỹ để đưa lên Production và review công thức 2 trang tính thuế (TNCN, Hộ kinh doanh).
'''
text = text[:p2_start] + new_p2 + text[p2_end:]

# Replace project 3
old_p3 = '''- **Điểm nghẽn & Việc tiếp theo:** Gỡ nút thử nghiệm để phát hành trang Gara; chạy lại 28 gara đối tác báo lỗi và rà soát 10 nhóm gara trùng để trình BU phương án gộp.
---'''
new_p3 = '''- **Next Action:** Gỡ nút thử nghiệm để phát hành chính thức trang Gara (`/tien-ich-giao-thong/garage`); chạy lại 28 gara đối tác báo lỗi và rà soát 10 nhóm gara trùng tên/địa chỉ.
- **Collaboration:** Phối hợp **BU Phụ trách Dịch vụ Xe / Giao thông** duyệt phương án gộp các gara trùng lặp và gắn công cụ danh sách gara vào luồng mua bảo hiểm ô tô.
---'''

assert old_p3 in text, "old_p3 not found"
text = text.replace(old_p3, new_p3)

# Replace project 4
old_p4 = '''- **Điểm nghẽn:** Chờ BU Bảo hiểm duyệt nội dung trang [momo.vn/bao-hiem](https://www.momo.vn/bao-hiem) và xếp lịch phát hành công cụ khấu trừ.
---'''
new_p4 = '''- **Next Action:** Phát hành chính thức công cụ mức khấu trừ lên trang `/bao-hiem-o-to/vat-chat-xe`; hoàn thiện nội dung text các khối trên trang chủ Bảo hiểm.
- **Collaboration:** Phối hợp **BU Bảo hiểm (Insurtech)** duyệt nội dung text trang chủ [momo.vn/bao-hiem](https://www.momo.vn/bao-hiem) và xác nhận mức % giảm phí của từng nấc khấu trừ.
---'''

assert old_p4 in text, "old_p4 not found"
text = text.replace(old_p4, new_p4)

# Replace project 5
old_p5 = '''- **Kế hoạch tiếp theo:** Hoàn thành khối đánh giá người dùng và phối hợp Growth Team theo dõi số lượt tải app thực tế.
---'''
new_p5 = '''- **Next Action:** Hoàn thiện khối hiển thị đánh giá của người dùng (Social Proof) và chính sách quà tặng tân thủ trên trang `/tai-app`; theo dõi lưu lượng chuyển đổi W2A và CTR cài app.
- **Collaboration:** Phối hợp **Growth Team / Media Team** đối soát lượng click OneLink từ các chiến dịch Paid Ads và tối ưu thông điệp mở app sau cài đặt để giảm tỷ lệ rơi rụng.
---'''

assert old_p5 in text, "old_p5 not found"
text = text.replace(old_p5, new_p5)

# Replace project 6
old_p6 = '''- **Kế hoạch tiếp theo:** Hướng dẫn PO vé số thao tác trên Staging khi PO bắt đầu làm quen.

### 7. Hiệu Suất Biến Động 7 Ngày Qua Trên Google SERP'''
new_p6 = '''- **Next Action:** Tiến hành build và kiểm thử toàn diện trên Staging; giám sát tốc độ tải trang dưới 1,5 giây giờ quay số mở thưởng 18h00 - 18h30.
- **Collaboration:** Phối hợp **PO Vé số (Lottery)** hướng dẫn sử dụng MoSpark CMS để chủ động thay đổi nội dung chữ, banner khuyến mãi mà không phụ thuộc dev can thiệp code.

### 7. Hiệu Suất Biến Động 7 Ngày Qua Trên Google SERP'''

assert old_p6 in text, "old_p6 not found"
text = text.replace(old_p6, new_p6)

# Section III:
# Project 1 Chatbot
old_p1_3 = '''- **Kế hoạch tuần sau:** Hoàn thiện bộ tiêu chí đánh giá chất lượng câu trả lời của Chatbot và theo dõi tỷ lệ bao phủ tri thức trên các trang dịch vụ trọng điểm.
---'''
new_p1_3 = '''- **Next Action:** Thử nghiệm độ chính xác của câu trả lời Chatbot trên Staging với tập dữ liệu tri thức mới; bổ sung bộ lọc và phân loại tài liệu tri thức theo chuyên đề.
- **Collaboration:** Phối hợp **Đội ngũ Quản trị Nội dung (Content Team)** bổ sung khối FAQ hoặc bài viết nội dung dài cho các trang web chưa đạt chuẩn để tăng độ bao phủ tri thức của AI.
---'''

assert old_p1_3 in text, "old_p1_3 not found"
text = text.replace(old_p1_3, new_p1_3)

# Project 2 Admin Panel
old_p2_3 = '''- **Chuẩn bị hoàn tất nghiệm thu Phase 2:** Phía BMC đã hoàn tất kiểm thử và gửi email xác nhận đồng thuận (confirm) vào ngày 29/10; chốt ngày build production Phase 2 vào ngày **02/11/2026** cùng nhánh BMC.
---'''
new_p2_3 = '''- **Next Action:** Tiến hành build Production Phase 2 vào ngày 02/11/2026; theo dõi vận hành sau phát hành và giám sát độ ổn định của All-in-One Editor.
- **Collaboration:** Phối hợp **Khối BMC (Brand & Marketing Communications)** và các **Cell Team** nghiệm thu thực tế, hướng dẫn sử dụng các khối nội dung In-App mới và tiếp nhận phản hồi cải tiến.
---'''

assert old_p2_3 in text, "old_p2_3 not found"
text = text.replace(old_p2_3, new_p2_3)

# Project 3 Search
old_p3_3 = '''- **Kế hoạch tuần sau:** Theo dõi số liệu tương tác thực tế của thẻ chuyển tiền và banner bạn mới trên môi trường chính thức.
---'''
new_p3_3 = '''- **Next Action:** Theo dõi số liệu sử dụng thẻ chuyển tiền nhanh qua số điện thoại và tỷ lệ click banner người dùng mới trên [momo.vn/tim-kiem](https://www.momo.vn/tim-kiem) môi trường Production.
- **Collaboration:** Phối hợp **Data / Analytics Team** bóc tách tỷ lệ chuyển đổi từ ô tìm kiếm website dẫn vào app MoMo thực hiện giao dịch chuyển tiền.
---'''

assert old_p3_3 in text, "old_p3_3 not found"
text = text.replace(old_p3_3, new_p3_3)

# Project 4 URL Catalog
old_p4_3 = '''- **Kế hoạch tuần sau:** Bắt đầu tạo bảng dữ liệu trên môi trường phát triển và nạp 51 trang tìm kiếm ban đầu để đối chiếu.
---'''
new_p4_3 = '''- **Next Action:** Triển khai Giai đoạn 1 của Hồ danh mục URL: tạo bảng cơ sở dữ liệu trên môi trường dev và nạp danh mục 51 trang tìm kiếm ưu tiên để đối chiếu dữ liệu.
- **Collaboration:** Phối hợp **Đội ngũ AI / Chatbot** và **SEO Team** thống nhất cấu trúc metadata và taxonomy phân cấp dự án trước khi mở rộng ra toàn bộ URL website.
---'''

assert old_p4_3 in text, "old_p4_3 not found"
text = text.replace(old_p4_3, new_p4_3)

# Project 5 Security
old_p5_3 = '''- **Kế hoạch tuần sau:** Hoàn tất chuyển đổi các trang dùng 7 RPC sang BFF; đóng hoàn toàn cổng truy cập công khai; đưa module Cron Job lên môi trường dev nội bộ.
---'''
new_p5_3 = '''- **Next Action:** Trình duyệt giải pháp nâng cấp dữ liệu; triển khai Giai đoạn P1 (thu hồi quyền đọc public anon, dựng máy chủ BFF qua role mini_web_server, chuyển đổi 19 trang gọi qua BFF); đưa Cron Job lên môi trường dev nội bộ.
- **Collaboration:** Phối hợp **ITC Security Team** đặt lịch Pentest lại (Giai đoạn P3) và thẩm định các API public mới; phối hợp **DevOps Team** cấu hình cổng API, tường lửa và chuẩn bị đóng hoàn toàn cổng public Supabase.
---'''

assert old_p5_3 in text, "old_p5_3 not found"
text = text.replace(old_p5_3, new_p5_3)

# Project 6 MoBase
old_p6_3 = '''- **Kế hoạch tuần sau:** Kiểm tra tương thích và chuẩn bị đưa Header Advance lên trang chủ bản chính thức.

---'''
new_p6_3 = '''- **Next Action:** Kiểm tra tính tương thích, responsive và hiệu năng trên môi trường Staging ([momo-stg.mservice.io](https://momo-stg.mservice.io/)); chuẩn bị kế hoạch phát hành lên trang chủ chính thức.
- **Collaboration:** Phối hợp **Web Platform Lead** và **Design System Team (MoBase)** review giao diện và trải nghiệm điều hướng trước khi On Production.

---'''

assert old_p6_3 in text, "old_p6_3 not found"
text = text.replace(old_p6_3, new_p6_3)

# Project 7 Web Performance
old_p7_3 = '''- **Kế hoạch tuần sau:** DevOps mở quyền truy cập máy chủ để kết nối bảng số liệu.
---'''
new_p7_3 = '''- **Next Action:** Kết nối bảng hiển thị số liệu GA4 & Google Search Console vào MoSpark Admin ngay khi máy chủ riêng sẵn sàng; kiểm thử phân quyền xem theo từng BU/PM.
- **Collaboration:** Phối hợp **DevOps Team** dựng máy chủ riêng, cấu hình mở quyền truy cập và gỡ bỏ các API key cũ để bảo đảm an toàn dữ liệu.
---'''

assert old_p7_3 in text, "old_p7_3 not found"
text = text.replace(old_p7_3, new_p7_3)

# Project 8 MoSpark Quiz
old_p8_3 = '''- **Kế hoạch tuần sau:** Tiếp tục chạy thử quiz trên trình duyệt thật và theo dõi phản hồi người dùng.'''
new_p8_3 = '''- **Next Action:** Chạy thử nghiệm widget Quiz trên bài blog thật; hoàn tất bộ kiểm thử 13 trường hợp (test cases) đa thiết bị trước khi phát hành chính thức.
- **Collaboration:** Phối hợp **Financial BU / Growth Team** đối soát tỷ lệ tương tác (Time on Page) và tỷ lệ nhấp vào CTA mở thẻ tín dụng / tra cứu điểm tín dụng sau khi hoàn thành quiz.'''

assert old_p8_3 in text, "old_p8_3 not found"
text = text.replace(old_p8_3, new_p8_3)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Update successful!')
