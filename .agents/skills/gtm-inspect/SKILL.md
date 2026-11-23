---
name: gtm-inspect
description: Tra cứu nhanh GTM container (live version, tags, triggers, variables, folders) bằng CLI dùng chung, không tạo script ad-hoc check_gtm_*.py.
---

# SKILL: GTM INSPECT (/gtm-inspect)

## 1. MỤC TIÊU & TRIGGER
Kích hoạt khi user hỏi về trạng thái GTM:
- *"GTM đang live version mấy"*, *"check GTM"*, *"tag X trong GTM chưa"*
- *"Trigger cho event Y tồn tại không"*, *"biến GTM Z config thế nào"*
- *"GTM in-app có tag gì"*

## 2. NGUYÊN TẮC CỨNG

1. **CẤM viết file script mới** để inspect GTM. Dùng CLI `scripts/gtm_inspect.py` hoặc lib `scripts/lib/gtm_client.py`.
2. **READ-ONLY mặc định.** CLI chỉ đọc. Mọi thao tác ghi (tạo tag/trigger, publish version) phải qua quy trình riêng có xác nhận của user - không tự ý publish.
3. Credentials SSOT: service account `07_REPORTS/data/credentials/gsc-credentials.json` (đã có scope tagmanager). OAuth user token `gtm-token.json` chỉ dùng cho `scripts/auth_gtm.js`.

## 3. CÁCH DÙNG

```bash
# Tổng quan container web (GTM-P9JDDJZ)
./.venv/bin/python scripts/gtm_inspect.py

# Liệt kê + lọc (filter match cả name lẫn event value trong config)
./.venv/bin/python scripts/gtm_inspect.py --list tags --filter utility
./.venv/bin/python scripts/gtm_inspect.py --list triggers --filter click_to_app
./.venv/bin/python scripts/gtm_inspect.py --list variables --filter user_id
./.venv/bin/python scripts/gtm_inspect.py --list versions --limit 10
./.venv/bin/python scripts/gtm_inspect.py --list folders

# In-app container
./.venv/bin/python scripts/gtm_inspect.py --container inapp --list tags

# Raw JSON khi cần full config
./.venv/bin/python scripts/gtm_inspect.py --list tags --filter utility --json
```

`--list` options: `overview` (mặc định), `tags`, `triggers`, `variables`, `folders`, `versions`.
`--no-live`: đọc từ Default Workspace thay vì live version (xem thay đổi chưa publish).

## 4. LIB API (khi cần logic phức tạp hơn CLI)

```python
import sys; sys.path.insert(0, ".")
from scripts.lib.gtm_client import get_client

c = get_client("web")          # hoặc "inapp"
c.latest_version()             # header live version
c.list_tags(live=True)         # tags trong live version
c.list_triggers(live=False)    # triggers trong workspace (chưa publish)
c.list_variables()
c.list_folders()
c.version_detail(224)          # full config 1 version
c.list_versions()
```

Containers:
- `web` = `accounts/4262611053/containers/10104547` (GTM-P9JDDJZ, web momo.vn)
- `inapp` = `accounts/4262611053/containers/57119568` (GTM-5TCGRPX - in-app, cần verify nếu API báo lỗi)

## 5. TRẢ LỜI USER

- Luôn nêu rõ đang xem **live version** hay **workspace** (draft) - 2 trạng thái khác nhau.
- Khi check "event X đã setup chưa": query cả `tags` (tìm GA4 event tag) lẫn `triggers` (tìm custom event trigger) - event cần cả 2 mới bắn được.
- Đối chiếu với SSOT tracking: `04_MOSPARK_PLATFORM/WEB_EVENT_TRACKING_DICTIONARY.md` (web) trước khi kết luận thiếu/thừa.

## 6. LIÊN QUAN

- `scripts/auth_gtm.js`: OAuth user flow khi cần scope ngoài service account (hiếm).
- `04_MOSPARK_PLATFORM/WEB_EVENT_TRACKING_DICTIONARY.md`: SSOT event schema GA4/GTM.
- Scratch cũ `check_gtm_*`, `review_gtm_*` đã được thay thế bởi skill này - không tái tạo.
- GA4 event data (đã bắn thật chưa): dùng skill `ad-hoc-ga4-query`.
- Publish version: KHÔNG tự làm - cần user xác nhận, dùng GTM UI hoặc API `versions().create` + `publish` có chủ đích.

## 7. LƯU Ý DEPRECATED

- `scripts/catalog_gtm_events.py`: script cũ generate catalog - kiểm tra còn dùng không trước khi tham khảo.
- Service account scopes hiện tại rộng (edit + publish) vì kế thừa từ scratch scripts - nếu siết quyền thì chỉ giữ `tagmanager.readonly` cho inspect.
