---
trigger: "Whenever running git commands or inspecting projects/directories"
---
# STRICT SINGLE-REPO BOUNDARY & INTENT-GATED ACCESS

1. **Phạm vi Git duy nhất (Strict Single-Repo Push):**
   - Mọi thao tác git (`git status`, `git add`, `git commit`, `git push`, `git diff`) khi người dùng yêu cầu "push" hoặc các thao tác git thông thường **CHỈ ĐƯỢC PHÉP thực hiện duy nhất trong repository hiện tại (`Hienho_MoMo-Base`)**.
   - Tuyệt đối KHÔNG tự ý quét, đọc, commit hoặc push sang repository khác (như `Web-Idea/react-web-momo` hay bất kỳ repo nào khác ngoài workspace).

2. **Cơ chế mở quyền truy cập (Intent-Gated Access):**
   - Chỉ khi người dùng **đề cập rõ ràng tên "Hub", "Hubs" hoặc "React"** trong câu lệnh thì mới được phép tương tác, đọc hoặc làm việc với repo React (`Web-Idea/react-web-momo`).
   - Mọi trường hợp khác: Không đọc, không chạm, không push sang repo React.
