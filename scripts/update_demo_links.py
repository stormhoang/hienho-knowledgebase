import os

path = '07_REPORTS/docs/weekly-report-2026-10-26-11-01.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Lottery Hub
old_lottery = '''### 6. Lottery Hub: Sẵn Sàng Công Cụ MoSpark Trên Staging
- **Key Owner:** duy.tran2
- **Bối cảnh & Bài toán:'''

new_lottery = '''### 6. Lottery Hub: Sẵn Sàng Công Cụ MoSpark Trên Staging
- **Key Owner:** duy.tran2
- **Liên kết Demo & Tài liệu:**
  - *Môi trường UAT/Demo:* [momovn-dev.mservice.io/ve-so](https://momovn-dev.mservice.io/ve-so)
  - *Tài liệu nghiệp vụ:* [Tài liệu nghiệp vụ Vé số MoMo](https://docs.google.com/document/d/1Ec8momzGi4_H_K5Uk-MH4Ios3ayrxYXC_TlztwiGnHY/edit?tab=t.0)
  - *Bảng góp ý & phản hồi (Feedback):* [Lottery Feedback Sheet](https://docs.google.com/spreadsheets/d/1BvqWMe6QcZ94rkzqioOfBHW2Wtb-rijHNWSVBWsi_kU/edit?gid=2057949935#gid=2057949935)
- **Bối cảnh & Bài toán:'''

assert old_lottery in text, 'old_lottery not found'
text = text.replace(old_lottery, new_lottery)

# 2. Update Chatbot AI
old_chatbot = '''### 1. Chatbot AI & Hệ Thống Cơ Sở Tri Thức (Knowledge Base)
- **Key Owner:** duy.tran2
- **Objectives:'''

new_chatbot = '''### 1. Chatbot AI & Hệ Thống Cơ Sở Tri Thức (Knowledge Base)
- **Key Owner:** duy.tran2
- **Liên kết Hệ thống & Demo:**
  - *Môi trường Production:* [adminweb.momocdn.net/chatbot-admin/grounding_document](https://adminweb.momocdn.net/chatbot-admin/grounding_document)
  - *Môi trường UAT:* [momovn-dev.mservice.io/chatbot-admin/grounding_document](https://momovn-dev.mservice.io/chatbot-admin/grounding_document)
- **Objectives:'''

assert old_chatbot in text, 'old_chatbot not found'
text = text.replace(old_chatbot, new_chatbot)

# 3. Update Admin Panel Phase 2
old_admin = '''### 2. Admin Panel: All-in-One Editor, Khối Nội Dung In-App & Quản Trị Menu (Build Prod Phase 2)
- **Key Owner:** hieu.nguyen8, duy.tran2
- **Objectives:'''

new_admin = '''### 2. Admin Panel: All-in-One Editor, Khối Nội Dung In-App & Quản Trị Menu (Build Prod Phase 2)
- **Key Owner:** hieu.nguyen8, duy.tran2
- **Liên kết Hệ thống & Tài liệu:**
  - *Môi trường Production:* [adminweb.momocdn.net/cell-team/inbound/inapp-article](https://adminweb.momocdn.net/cell-team/inbound/inapp-article)
  - *Môi trường UAT:* [momovn-dev.mservice.io/admin/cell-team/inbound/inapp-article](https://momovn-dev.mservice.io/admin/cell-team/inbound/inapp-article)
  - *Tài liệu đề xuất cải tiến Phase 2 từ BU:* [Slide Đề xuất cải tiến Phase 2 (Google Slides)](https://docs.google.com/presentation/d/1Ncpvg7CD9VblXga8vVo3bzIfaMxdPt_oPZB5VjmBIkM/edit?slide=id.h1b2dddbaad68927b_0_0#slide=id.h1b2dddbaad68927b_0_0)
- **Objectives:'''

assert old_admin in text, 'old_admin not found'
text = text.replace(old_admin, new_admin)

# 4. Update Vehicle Hub
old_vehicle = '''### 3. Vehicle Hub: Danh Sách Gara Mới, Tool Maps & Menu Bảo Hiểm Xe Máy
- **Key Owner:** Thuận Võ (thuan.vo)'''

new_vehicle = '''### 3. Vehicle Hub: Danh Sách Gara Mới, Tool Maps & Menu Bảo Hiểm Xe Máy
- **Key Owner:** Thuận Võ (thuan.vo)
- **Liên kết Môi trường:**
  - *Môi trường Production:* [momo.vn/tien-ich-giao-thong](https://www.momo.vn/tien-ich-giao-thong) · Gara: [momo.vn/tien-ich-giao-thong/garage](https://www.momo.vn/tien-ich-giao-thong/garage) · Bảo hiểm xe máy: [momo.vn/bao-hiem-xe-may](https://www.momo.vn/bao-hiem-xe-may)
  - *Môi trường Staging:* [momo-stg.mservice.io/tien-ich-giao-thong](https://momo-stg.mservice.io/tien-ich-giao-thong)'''

assert old_vehicle in text, 'old_vehicle not found'
text = text.replace(old_vehicle, new_vehicle)

# 5. Update Minigame Bo Sua Bay
old_bsb = '''  - **Xử lý Minigame Bò Sữa Bay ([momo.vn/cinema/bo-sua-bay-25058](https://www.momo.vn/cinema/bo-sua-bay-25058)):**
    - Phim khởi chiếu ngày 06/11. Game gắn trên trang phim, phát cùng video tại các cụm rạp kèm mã QR để khán giả quét chơi.'''

new_bsb = '''  - **Xử lý Minigame Bò Sữa Bay ([momo.vn/cinema/bo-sua-bay-25058](https://www.momo.vn/cinema/bo-sua-bay-25058)):**
    - *Link xem trước:* Staging Game Preview: [momo-stg.mservice.io/cinema/bo-sua-bay-25058?bsb-preview](https://momo-stg.mservice.io/cinema/bo-sua-bay-25058?bsb-preview) (trên Production [momo.vn/cinema/bo-sua-bay-25058](https://www.momo.vn/cinema/bo-sua-bay-25058) tạm ẩn game chờ Legal duyệt).
    - Phim khởi chiếu ngày 06/11. Game gắn trên trang phim, phát cùng video tại các cụm rạp kèm mã QR để khán giả quét chơi.'''

assert old_bsb in text, 'old_bsb not found'
text = text.replace(old_bsb, new_bsb)

# 6. Update Security RPC Fuel API
old_rpc = '''    - *Khóa đọc trực tiếp (Anonymous read) trên 19 trang web:* Chuyển toàn bộ luồng dữ liệu quảng cáo, giá xăng và địa điểm sang gọi qua Server-side Proxy / Public RPC API của [momo.vn](https://www.momo.vn) *(thuan.vo)*.'''

new_rpc = '''    - *Khóa đọc trực tiếp (Anonymous read) trên 19 trang web:* Chuyển toàn bộ luồng dữ liệu quảng cáo, giá xăng và địa điểm sang gọi qua Server-side Proxy / Public RPC API của [momo.vn](https://www.momo.vn) *(thuan.vo)* (Kiểm thử UAT API Giá Xăng sạch: [momovn-dev.mservice.io/api/fuel_prices_latest](https://momovn-dev.mservice.io/api/fuel_prices_latest)).'''

assert old_rpc in text, 'old_rpc not found'
text = text.replace(old_rpc, new_rpc)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated demo links successfully!')
