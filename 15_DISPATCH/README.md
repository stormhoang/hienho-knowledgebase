# 15_DISPATCH: Lệnh giao việc từ Hub /agent

Nơi lưu các lệnh Hiến ra qua khung chat trên Hub `/agent`. Đây là SSOT của việc giao trực tiếp, tách khỏi báo cáo tuần.

## Luồng

1. Hiến gõ lệnh trên Hub `/agent`.
2. Hub ghi lệnh vào hàng chờ `15_DISPATCH/.queue/<id>.json` (không vào git). Phiên Claude trong desktop app nhận lệnh, soạn bảng phân công theo mục "Quy trình cho phiên Claude" bên dưới. Mỗi người có: việc cần làm, những gì cần Hiến cung cấp, timeline theo mốc ngày, phụ thuộc, rủi ro.
3. Hiến bấm "Chốt giao việc". Route của Hub ghi 2 file vào thư mục này:
   - `<ngày>-<slug>.json`: dữ liệu máy đọc, `scripts/sync_agent_tasks.py` dùng file này.
   - `<ngày>-<slug>.md`: bản đọc cho người.
4. Hub chạy `scripts/sync_agent_tasks.py`. Script gộp các phân công chưa hoàn thành vào `agent-tasks.json` bên Hub.
5. Người được giao bấm "Xác nhận" trên Hub. Trạng thái của người đó trong file JSON đổi từ `cho-xac-nhan` sang `da-xac-nhan`, file `.md` được ghi lại.

## Quy trình cho phiên Claude

Công cụ: `node scripts/agent-queue.mjs` trong repo Hub (`react-web-momo`).

1. Canh hàng chờ bằng Monitor, lệnh `node scripts/agent-queue.mjs watch`, timeout 30 phút. Hết hạn thì bật lại. Mỗi dòng `LENH_MOI <id>` là một lệnh mới.
2. `list` để xem lệnh và lịch sử cùng luồng. Lệnh nhắn tiếp trong một luồng là yêu cầu chỉnh: đọc bảng phân công đã trả của luồng đó, trả lại toàn bộ bảng đã cập nhật.
3. `claim <id>`, rồi ghi `progress <id> "<bước>"` mỗi khi đọc một file, để Hub hiện tiến độ.
4. Bắt buộc đọc `00_HARNESS_CORE/team_scope_of_work.md`. Cần thêm bối cảnh dự án thì đọc theo `00_HARNESS_CORE/KNOWLEDGE_ROUTING.md`, chỉ file liên quan.
5. Soạn bảng phân công:
   - Chỉ giao cho: Bảo, Hoài Anh, Hiếu, Duy, Lộc, Hùng, Nhật, Thuận, Trọng, Hoan, Tữ. Không giao cho Hiến. Giao ít người nhất đủ để làm xong, không giao việc nằm trong mục "Không phụ trách" của người đó.
   - **Luồng sản phẩm trực tiếp (không thông qua Product Design · Tữ sắp vào):** Định tuyến đi thẳng đến Key Owner tương ứng:
     * Thuận: Vehicle Hub, công cụ xe (định giá xe, tra cứu phạt nguội, chi phí xe...).
     * Hùng: Cinema Hub, lịch chiếu phim, minigame tương tác.
     * Nhật: Financial Hub, công cụ tiện ích tài chính (tính thuế, lãi vay, tỷ giá...).
     * Trọng: GenAI Pipeline, MoSpark nodes, PLG Dashboard, Chatbot KB parser.
   - **Điều kiện tiên quyết để Go-Live đầy đủ lên Production:**
     * Trừ Trọng, các sản phẩm công khai của Thuận, Hùng, Nhật để Go-Live bắt buộc phải có phân công phối hợp: Meta Data, SEO Keywords, Long Content từ Hoan, và ký duyệt Product Sign-off từ Hiến.
     * Sản phẩm của Trọng là công cụ vận hành nội bộ, được miễn trừ yêu cầu Meta Data, SEO Keywords và Long Content từ Hoan; chỉ cần hoàn thành kiểm thử tính năng và nhận Product Sign-off từ Hiến.
   - Đóng vai từng người: việc cụ thể, những gì người đó cần Hiến cung cấp, timeline có mốc và ngày YYYY-MM-DD (tính từ hôm nay, bỏ thứ Bảy, Chủ nhật), phụ thuộc, rủi ro.
   - Mốc của người cần đầu ra của người khác phải nằm sau mốc giao của người đó.
   - Lệnh mơ hồ ở điểm ảnh hưởng phân công thì ghi vào `cauHoiChoHien`, vẫn đưa phương án tốt nhất với giả định hợp lý.
   - Tiếng Việt, câu ngắn, không dấu gạch ngang dài, không bịa số liệu.
6. Ghi bảng ra file tạm trong scratchpad, cấu trúc `dispatchPlanSchema` (`lib/agent/dispatch-types.ts` của Hub), rồi `answer <id> <file>`. Script kiểm cấu trúc, sai thì sửa và nộp lại. Không xử lý được thì `fail <id> "<lý do>"`.
7. Không tự ghi vào `15_DISPATCH/*.json`. Việc đó chỉ diễn ra khi Hiến bấm "Chốt giao việc" trên Hub.

## Trạng thái một phân công

| Giá trị | Nghĩa |
|---|---|
| `cho-xac-nhan` | AI đã soạn thay theo vai, người thật chưa xác nhận |
| `da-xac-nhan` | Người được giao đã xác nhận việc, input và timeline |
| `hoan-thanh` | Đã xong, không còn hiện trên Hub |

## Quy tắc

- Agent lập kế hoạch chỉ đọc KB và ghi vào `.queue`. Mọi thao tác ghi lệnh do route của Hub làm, sau khi Hiến bấm chốt.
- Không sửa tay file `.json` khi Hub đang chạy. Sửa trạng thái qua Hub, hoặc sửa xong thì chạy lại `scripts/sync_agent_tasks.py`.
