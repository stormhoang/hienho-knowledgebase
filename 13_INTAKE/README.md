# 13_INTAKE: INTAKE AGENT (Drop file -> hubs-momo)

Diem tiep nhan trung tam cho intake agent. File drop vao `~/Downloads/intake/`, agent tu xu ly va push sang hubs-momo (`/dashboard`). (Lưu ý: Luồng `/board` và `/roadmap` bên Hub đã xóa, không còn đẩy sang).

---

## 1. LUONG VAN HANH

```
Drop file vao ~/Downloads/intake/
        |
        v
python3 scripts/intake.py --scan --push
  1. SCAN      - quet file moi, bo qua da xu ly (sha256 idempotency)
  2. DETECT    - nhan dien format theo signature registry
  3. PARSE     - parser tuong ung -> ghi SSOT local
  4. VALIDATE  - sanity bound (PV tracking, days_elapsed)
  5. ROUTE     - map format -> dich push
  6. PUSH      - goi build-dashboard-data.py cua hubs-momo
  7. LOG       - ghi 07_REPORTS/data/push_log.jsonl
```

---

## 2. FORMAT HO TRO (Signature Registry)

| Format | Dinh dang file | Parser | Dich push |
|---|---|---|---|
| Tracking | xlsx co sheet "MTD Pivot" + "Full month Pivot" | parse_tracking | dashboard |
| Crawl stats | zip/csv GSC Crawl Stats export | parse_crawl | dashboard |
| Backlink | csv `Site,Linking pages,Target pages` | parse_backlink | dashboard |
| Unknown | bat ky | - | quarantine (13_INTAKE/quarantine/) |

---

## 3. CAC LENH

Wrapper `intake` da cai tai `~/.local/bin/intake` (dung truc tiep, khong can `python3 scripts/...`):

```bash
# Health check pipeline
intake verify

# Dry-run: xu ly moi file, khong push (mac dinh)
intake

# Xu ly + push sang hubs-momo
intake push

# Xu ly 1 file cu the
intake file <duong_dan_file> [--push]

# Chay watcher nen (poll intake folder)
intake-watch            # chay thuong
intake-watch --install  # cai launchd, chay suot doi
```

Lenh goc (neu can goi truc tiep):
`./.venv/bin/python scripts/intake.py --scan [--push|--verify|--file ...]`

---

## 4. QUY DINH AN TOAN

- **Dry-run la mac dinh:** chi `--push` moi thuc te ghi sang hubs-momo.
- **Idempotency:** moi file da xu ly luu sha256 vao `07_REPORTS/data/processed_hashes.json`, file trung se bi SKIP.
- **Validation gate:** tracking xlsx bi reject neu PV MTD ngoai [50k, 20M] hoac days_elapsed ngoai [1, 31] - khong push bira.
- **Quarantine:** file khong nhan dien duoc format -> copy sang `13_INTAKE/quarantine/`, khong crash.
- **Audit trail:** moi lan xu ly ghi `07_REPORTS/data/push_log.jsonl` (file, hash, status, push_msg, timestamp).
- **Notification:** macOS notification khi push fail/thanh cong.

---

## 5. HUBS-MOMO ENDPOINT

| Dich | File trong hubs-momo | Script |
|---|---|---|
| /dashboard | `lib/dashboard/web-data.json` | `scripts/build-dashboard-data.py` |

Hubs repo: `/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo`

---

## 6. LICH SU THAY DOI

- 2026-11-05: Loai bo tasklist va weekly rollover khoi intake pipeline. Trang thai shipment duoc theo doi qua roadmap va release data.
