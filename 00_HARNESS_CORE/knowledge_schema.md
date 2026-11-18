# Knowledge Registry Schema

## Mục đích

Schema này là lớp metadata dùng chung cho Claude, Antigravity và các Agent khác. Registry không thay thế tài liệu gốc và không cấp quyền ưu tiên tuyệt đối cho bất kỳ Agent nào.

## Trường bắt buộc

- `id`: định danh ổn định, không chứa path.
- `path`: đường dẫn tương đối trong repository.
- `domain`: miền tri thức.
- `type`: loại nguồn.
- `authority`: mức sử dụng gồm `primary`, `secondary`, `reference`, `generated`.
- `status`: `active`, `legacy`, `deprecated`, `draft`, `historical` hoặc `retired`.
- `owner`: đội ngũ hoặc vai trò chuyên môn phụ trách nguồn (ví dụ: `Web Product Lead`, `Cinema Hub Team`, `Vehicle Hub Team`, `Financial Hub Team`, `DevOps Team`).
- `used_for`: các mục đích được phép dùng.

## Trường kiểm soát

- `freshness_days`: số ngày khuyến nghị trước khi cảnh báo cũ.
- `schema_version`: phiên bản cấu trúc dữ liệu nếu là JSON hoặc dữ liệu máy đọc.
- `supersedes`: danh sách nguồn cũ hơn.
- `cross_check_with`: nguồn cần đối chiếu.
- `notes`: giả định hoặc giới hạn sử dụng.

## Quản trị nguồn gốc dữ liệu (Provenance Governance SSOT)

Để đảm bảo hai hoặc nhiều Agent độc lập (Claude, Antigravity) xác thực được tính toàn vẹn và chắc chắn đang đọc cùng một phiên bản nguồn, Registry và Manifest hỗ trợ các trường provenance:
- `system_of_record`: Nguồn hệ thống gốc sinh ra dữ liệu hoặc tài liệu (ví dụ: `GA4 Data API (Property 270743103)`, `Google Sheets Cloud SSOT`, `Antigravity Harness Governance`).
- `generator_script`: Script hoặc quy trình tạo ra tệp (đường dẫn tương đối như `scripts/sync_ga4_master.py` hoặc `manual_authoring`).
- `checksum`: Mã băm SHA-256 tính toán từ nội dung tệp thực tế trên đĩa tại thời điểm kiểm tra.
- `content_length_bytes`: Dung lượng tệp tính bằng byte.
- `verified_at`: Thời điểm kiểm tra tính toàn vẹn của tệp.

## Quản trị độ mới dữ liệu (Freshness Governance SSOT)

Hệ thống phân biệt rõ hai khái niệm thời gian:
1. `file_modified_at` (Thời điểm sửa tệp vật lý): Ngày giờ tệp được commit hoặc ghi trên ổ đĩa. Giá trị này thường bị làm mới khi chạy git pull, reformat hoặc chỉnh sửa cú pháp.
2. `data_as_of` / `data_period` (Mốc cắt dữ liệu nghiệp vụ): Ngày chốt số liệu hoặc kỳ báo cáo thực tế được bóc tách từ nội dung tệp (ví dụ: Snapshot MTD, báo cáo tuần, log quyết định).

Các trạng thái độ mới được quy chuẩn:
- `fresh`: Số ngày kể từ `data_as_of` nằm trong ngưỡng `freshness_days`.
- `lag_reconciled`: Dữ liệu trễ từ 1 đến 3 ngày so với ngưỡng, phản ánh biên độ đối soát định kỳ của hệ thống ETL / BigQuery / GA4.
- `stale`: Dữ liệu đã cũ vượt ngưỡng khuyến nghị cộng biên độ đối soát. Agent bắt buộc phát cảnh báo và không được dùng để kết luận kỳ hiện tại.
- `normative`: Tài liệu quy chuẩn, hợp đồng, kiến trúc hoặc tiêu chuẩn kỹ thuật không phụ thuộc mốc thời gian ngày.
- `historical`: Tài liệu đối chiếu lịch sử (Historical SSOT).

Khi phát hiện `mtime_drift_days >= 3` (tệp được sửa gần đây nhưng số liệu bên trong là từ kỳ cũ), hệ thống sẽ kích hoạt cảnh báo lệch kỳ (`drift_notice`) để Agent không ngộ nhận.

## Nguyên tắc tương thích

1. Agent vẫn đọc trực tiếp file gốc.
2. Registry chỉ mô tả và kiểm tra, không tự sửa nội dung.
3. `primary` không có nghĩa là luôn đúng nếu validator phát hiện conflict.
4. Conflict phải được báo cáo, không được tự động hợp nhất.
5. Mọi thay đổi Registry phải kiểm tra lại bằng validator.
