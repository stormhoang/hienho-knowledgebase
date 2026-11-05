# AGENT OPERATING CONTRACT

## Mục đích

Codebase này là nguồn tri thức, công cụ phân tích và lớp kiểm soát cho các Agent làm việc với Web Platform MoMo. Agent bên ngoài chịu trách nhiệm hiểu yêu cầu tự nhiên. Codebase chịu trách nhiệm cung cấp nguồn đúng, công cụ đúng, bằng chứng và giới hạn hành động.

## Quy trình bắt buộc

1. Xác định loại vấn đề và phạm vi cần xử lý.
2. Đọc đúng SSOT theo `00_HARNESS_CORE/KNOWLEDGE_ROUTING.md`.
3. Chọn capability trong `00_HARNESS_CORE/AGENT_CAPABILITIES.yaml`.
4. Kiểm tra trạng thái worktree trước mọi thao tác ghi.
5. Chạy đúng runtime `./.venv/bin/python` khi gọi Python.
6. Phân biệt rõ dữ kiện, suy luận và đề xuất.
7. Với thao tác ghi hoặc đồng bộ bên ngoài, phải preview phạm vi và xin xác nhận trước khi thực thi.
8. Sau khi thực thi, kiểm tra đầu ra, đối soát số liệu và ghi audit trail nếu capability yêu cầu.

## Quy tắc không được vi phạm

- Không tự đọc các file lớn nếu routing không yêu cầu.
- Không dùng dữ liệu mẫu hoặc mock data để kết luận về thực tế.
- Không ghi đè file hoặc đẩy dữ liệu bên ngoài nếu chưa có yêu cầu rõ.
- Không trình bày số liệu mà không nêu kỳ dữ liệu và nguồn.
- Nếu có mâu thuẫn giữa các SSOT, phải dừng kết luận chắc chắn và nêu rõ điểm lệch.
- Không coi exit code thành công là bằng chứng pipeline đã cập nhật đúng.

## Hợp đồng đầu ra

Mọi kết quả phân tích cần có: kết luận trực diện, bằng chứng, tác động, hành động tiếp theo, nguồn dữ liệu, độ mới dữ liệu và giả định còn tồn tại.
