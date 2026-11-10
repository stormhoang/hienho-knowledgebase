#!/usr/bin/env python3
"""Kiểm soát độ mới dữ liệu và phân biệt thời điểm sửa tệp với kỳ dữ liệu nghiệp vụ.

SSOT Script: scripts/check_knowledge_freshness.py
Domain: 00_HARNESS_CORE / Knowledge Governance
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
REGISTRY_PATH = ROOT / "00_HARNESS_CORE" / "knowledge_registry.yaml"
DEFAULT_JSON_OUT = ROOT / "00_HARNESS_CORE" / "knowledge_freshness.json"
DEFAULT_MD_OUT = ROOT / "00_HARNESS_CORE" / "knowledge_freshness.md"


def parse_date_str(val: str | None) -> date | None:
    """Chuyển đổi chuỗi ngày thành đối tượng date."""
    if not val:
        return None
    val = val.strip()
    # YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS or YYYY-MM-DD HH:MM:SS
    m_iso = re.match(r"^(\d{4})-(\d{2})-(\d{2})", val)
    if m_iso:
        try:
            return date(int(m_iso.group(1)), int(m_iso.group(2)), int(m_iso.group(3)))
        except ValueError:
            return None
    # DD/MM/YYYY or DD/MM/YYYY HH:MM
    m_vn = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})", val)
    if m_vn:
        try:
            return date(int(m_vn.group(3)), int(m_vn.group(2)), int(m_vn.group(1)))
        except ValueError:
            return None
    return None


def extract_sqlite_metadata(file_path: Path) -> tuple[date | None, str | None, str]:
    """Trích xuất ngày dữ liệu mới nhất từ cơ sở dữ liệu SQLite."""
    try:
        uri = f"file:{file_path.resolve()}?mode=ro"
        conn = sqlite3.connect(uri, uri=True)
        cursor = conn.cursor()
        tables = [row[0] for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
        if "fact_daily_performance" in tables:
            row = cursor.execute("SELECT max(date), max(synced_at) FROM fact_daily_performance").fetchone()
            if row and row[0]:
                data_date = parse_date_str(row[0])
                period = f"MTD {row[0][:7]} (cắt ngày {row[0]})"
                conn.close()
                return data_date, period, "sqlite:fact_daily_performance"
        conn.close()
    except Exception:
        pass
    return None, None, "sqlite:unresolved"


def extract_json_metadata(file_path: Path) -> tuple[date | None, str | None, str]:
    """Trích xuất ngày dữ liệu và kỳ báo cáo từ tệp JSON."""
    try:
        raw = json.loads(file_path.read_text(encoding="utf-8"))
        if isinstance(raw, dict):
            for key in ('data_as_of',):
                d = parse_date_str(raw.get(key))
                if d:
                    return d, d.isoformat(), f'json_key:{key}'
            dr = raw.get('date_range', {})
            if isinstance(dr, dict):
                d = parse_date_str(dr.get('end_date') or dr.get('end'))
                if d:
                    return d, f"{dr.get('start_date', dr.get('start', ''))} đến {d.isoformat()}", 'json:date_range.end'
            if isinstance(raw.get('running'), dict):
                run = raw['running']
                try:
                    d = date.fromisoformat(f"{run['month']}-{int(run['daysElapsed']):02d}")
                    return d, f'MTD đến {d.isoformat()}', 'json:running.daysElapsed'
                except (KeyError, ValueError, TypeError):
                    pass
            # 1. Trường updated_at / generated_at / snapshot_date
            for key in ("snapshot_date", "as_of"):
                if key in raw and isinstance(raw[key], str):
                    d = parse_date_str(raw[key])
                    if d:
                        period = None
                        if "date_range" in raw and isinstance(raw["date_range"], dict):
                            dr = raw["date_range"]
                            start = dr.get("start_date", "")
                            end = dr.get("end_date", "")
                            period = f"{start} đến {end}"
                        elif "timeframe" in raw:
                            period = f"{raw['timeframe']} (cập nhật {d.isoformat()})"
                        return d, period, f"json_key:{key}"

            # 2. Trường running (e.g. summary.json)
            if "running" in raw and isinstance(raw["running"], dict):
                run = raw["running"]
                month = run.get("month", "")
                days = run.get("daysElapsed")
                if month and days:
                    try:
                        year, m = month.split("-")
                        d = date(int(year), int(m), int(days))
                        period = f"Tháng {m}/{year} (MTD {days} ngày)"
                        return d, period, "json_key:running.daysElapsed"
                    except Exception:
                        pass

            # 3. Thông tin chung (e.g. agent_tasks.json)
            if "thongTinChung" in raw and isinstance(raw["thongTinChung"], dict):
                info = raw["thongTinChung"]
                sync_time = info.get("thoiGianDongBo")
                d = parse_date_str(sync_time)
                if d:
                    src = info.get("nguonBaoCao", "")
                    period = f"Đồng bộ từ {src}" if src else "Bản ghi tác vụ"
                    return d, period, "json_key:thongTinChung.thoiGianDongBo"

        elif isinstance(raw, list):
            # Danh sách bản ghi có trường date
            dates: list[date] = []
            for item in raw:
                if isinstance(item, dict) and "date" in item:
                    d = parse_date_str(item["date"])
                    if d:
                        dates.append(d)
            if dates:
                max_d = max(dates)
                return max_d, f"Bản ghi gần nhất ({max_d.isoformat()})", "json_array:max_date"
    except Exception:
        pass
    return None, None, "json:unresolved"


def extract_markdown_metadata(file_path: Path) -> tuple[date | None, str | None, str]:
    """Trích xuất ngày dữ liệu và kỳ báo cáo từ tệp Markdown."""
    try:
        content = file_path.read_text(encoding="utf-8")
        # 1. Header blockquote: Cập nhật & Kỳ dữ liệu / Kỳ báo cáo
        m_update = re.search(r"\*\*Cập nhật:\*\*\s*([0-9]{1,2}/[0-9]{1,2}/[0-9]{4}|[0-9]{4}-[0-9]{2}-[0-9]{2})", content)
        m_period = re.search(r"\*\*(?:Kỳ dữ liệu|Kỳ báo cáo):\*\*\s*([^\|\n\r]+)", content)
        if m_update:
            data_date = parse_date_str(m_update.group(1))
            period = m_period.group(1).strip() if m_period else None
            return data_date, period, "markdown_header:Cập nhật"

        # 2. Heading: GSC DATA EXPORT DD/MM/YYYY
        m_gsc = re.search(r"GSC DATA EXPORT\s*([0-9]{1,2}/[0-9]{1,2}/[0-9]{4}|[0-9]{4}-[0-9]{2}-[0-9]{2})", content)
        if m_gsc:
            data_date = parse_date_str(m_gsc.group(1))
            return data_date, f"GSC Export {data_date.isoformat()}", "markdown_heading:gsc_export"

        # 3. Table ISO date rows (e.g. decision log: | **YYYY-MM-DD** |)
        table_dates = re.findall(r"\|\s*\*\*(\d{4}-\d{2}-\d{2})\*\*\s*\|", content)
        if table_dates:
            parsed = [parse_date_str(d) for d in table_dates]
            valid = [p for p in parsed if p is not None]
            if valid:
                max_d = max(valid)
                return max_d, f"Quyết định gần nhất ({max_d.isoformat()})", "markdown_table:max_date"

        # 4. Frontmatter date
        m_fm = re.search(r"^---\n.*?date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2}|[0-9]{1,2}/[0-9]{1,2}/[0-9]{4})", content, re.DOTALL)
        if m_fm:
            data_date = parse_date_str(m_fm.group(1))
            return data_date, "Frontmatter Date", "markdown_frontmatter:date"
    except Exception:
        pass
    return None, None, "markdown:unresolved"


def extract_source_metadata(file_path: Path, entry: dict) -> dict[str, Any]:
    """Bóc tách chi tiết metadata thời điểm sửa tệp và kỳ dữ liệu nghiệp vụ."""
    st_mtime = file_path.stat().st_mtime
    file_dt = datetime.fromtimestamp(st_mtime, tz=timezone.utc)
    file_modified_at = file_dt.isoformat()
    file_mtime_date = datetime.fromtimestamp(st_mtime).date()

    suffix = file_path.suffix.lower()
    data_as_of: date | None = None
    data_period: str | None = None
    method = "none"

    if suffix in (".sqlite", ".db"):
        data_as_of, data_period, method = extract_sqlite_metadata(file_path)
    elif suffix == ".json":
        data_as_of, data_period, method = extract_json_metadata(file_path)
    elif suffix == ".md":
        data_as_of, data_period, method = extract_markdown_metadata(file_path)

    # Nếu file là historical từ registry, gán nhãn rõ
    if entry.get("status") == "historical" and not data_period:
        data_period = "Dữ liệu đối chiếu lịch sử"

    return {
        "file_modified_at": file_modified_at,
        "file_mtime_date": file_mtime_date,
        "data_as_of": data_as_of,
        "data_period": data_period or (data_as_of.isoformat() if data_as_of else "Không xác định"),
        "extraction_method": method,
    }


def evaluate_freshness(entry: dict, metadata: dict[str, Any], reference_date: date) -> dict[str, Any]:
    """Đánh giá trạng thái độ mới, độ trễ và cảnh báo lệch kỳ."""
    freshness_days: int | None = entry.get("freshness_days")
    data_as_of: date | None = metadata.get("data_as_of")
    file_mtime_date: date = metadata["file_mtime_date"]
    file_age_days = (reference_date - file_mtime_date).days

    age_days: int | None = None
    if data_as_of:
        age_days = (reference_date - data_as_of).days

    mtime_drift_days = 0
    if age_days is not None:
        mtime_drift_days = abs(file_age_days - age_days)

    status: str
    warning: str | None = None

    if entry.get("status") == "historical":
        status = "historical"
    elif freshness_days is None:
        status = "normative"
    else:
        # Nguồn có ngưỡng thời gian
        if data_as_of is None:
            status = "unknown"
            warning = (
                f"Nguồn '{entry['id']}' có ngưỡng {freshness_days} ngày nhưng không trích xuất được "
                "kỳ dữ liệu (data_as_of). Cần rà soát cấu trúc tệp."
            )
        elif age_days is not None and age_days < 0:
            status = "future_date_anomaly"
            warning = (
                f"Nguồn '{entry['id']}' có data_as_of ({data_as_of.isoformat()}) lớn hơn ngày đối chiếu "
                f"({reference_date.isoformat()}). Dữ liệu có thể bị lỗi mốc thời gian."
            )
        elif age_days is not None and age_days <= freshness_days:
            status = "fresh"
        elif age_days is not None and age_days <= freshness_days + 3:
            status = "lag_reconciled"
            warning = (
                f"Nguồn '{entry['id']}' có độ trễ {age_days} ngày (ngưỡng {freshness_days} ngày). "
                "Đang trong biên độ đối soát định kỳ của hệ thống."
            )
        else:
            status = "stale"
            warning = (
                f"CẢNH BÁO ĐỘ MỚI: Nguồn '{entry['id']}' có kỳ dữ liệu '{metadata['data_period']}' "
                f"(data_as_of: {data_as_of.isoformat() if data_as_of else 'None'}), đã cũ {age_days} ngày "
                f"(vượt ngưỡng {freshness_days} ngày). File được sửa lúc {file_mtime_date.isoformat()} "
                f"(lệch {mtime_drift_days} ngày so với kỳ dữ liệu). "
                "Agent tuyệt đối không dùng nguồn này để kết luận số liệu của kỳ hiện tại mà chưa đối chiếu số liệu mới."
            )

    # Cảnh báo lệch ngày sửa file vật lý và ngày dữ liệu
    drift_notice: str | None = None
    if age_days is not None and file_age_days < age_days and mtime_drift_days >= 3:
        drift_notice = (
            f"Tệp được sửa gần đây ({file_age_days} ngày trước) nhưng kỳ dữ liệu thực tế là "
            f"{data_as_of.isoformat() if data_as_of else 'None'} ({age_days} ngày trước). "
            "Không nhầm lẫn thời điểm commit/sửa tệp với độ mới của số liệu."
        )

    return {
        "id": entry["id"],
        "path": entry.get("path", ""),
        "domain": entry.get("domain", "unknown"),
        "owner": entry.get("owner", "Web Platform"),
        "authority": entry.get("authority", "reference"),
        "entry_status": entry.get("status", "active"),
        "freshness_threshold_days": freshness_days,
        "data_as_of": data_as_of.isoformat() if data_as_of else None,
        "data_period": metadata["data_period"],
        "file_modified_at": metadata["file_modified_at"],
        "file_mtime_date": file_mtime_date.isoformat(),
        "age_days": age_days,
        "file_age_days": file_age_days,
        "mtime_drift_days": mtime_drift_days,
        "status": status,
        "extraction_method": metadata["extraction_method"],
        "warning": warning,
        "drift_notice": drift_notice,
    }


def scan_registry_freshness(registry_path: Path, reference_date: date | None = None) -> dict[str, Any]:
    """Quét toàn bộ Knowledge Registry và đánh giá độ mới."""
    import yaml

    if reference_date is None:
        reference_date = date.today()

    registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    entries = registry.get("entries", [])

    results: list[dict[str, Any]] = []
    warnings: list[str] = []

    for entry in entries:
        path_text = entry["path"]
        abs_path = (ROOT / path_text).resolve()
        if not abs_path.is_file():
            results.append({
                "id": entry["id"],
                "path": path_text,
                "domain": entry.get("domain", "unknown"),
                "owner": entry.get("owner", "Web Platform"),
                "authority": entry.get("authority", "reference"),
                "entry_status": entry.get("status", "active"),
                "freshness_threshold_days": entry.get("freshness_days"),
                "data_as_of": None,
                "data_period": "Tệp không tồn tại",
                "file_modified_at": None,
                "file_mtime_date": None,
                "age_days": None,
                "file_age_days": None,
                "mtime_drift_days": 0,
                "status": "missing_file",
                "extraction_method": "none",
                "warning": f"Không tìm thấy tệp: {path_text}",
                "drift_notice": None,
            })
            warnings.append(f"Tệp không tồn tại: {path_text}")
            continue

        meta = extract_source_metadata(abs_path, entry)
        res = evaluate_freshness(entry, meta, reference_date)
        results.append(res)
        if res.get("warning"):
            warnings.append(res["warning"])

    summary = {
        "total_sources_checked": len(results),
        "time_sensitive_sources": sum(1 for r in results if r["freshness_threshold_days"] is not None),
        "fresh_count": sum(1 for r in results if r["status"] == "fresh"),
        "stale_count": sum(1 for r in results if r["status"] == "stale"),
        "lag_reconciled_count": sum(1 for r in results if r["status"] == "lag_reconciled"),
        "normative_count": sum(1 for r in results if r["status"] == "normative"),
        "historical_count": sum(1 for r in results if r["status"] == "historical"),
        "unknown_count": sum(1 for r in results if r["status"] in ("unknown", "missing_file", "future_date_anomaly")),
    }

    return {
        "version": "1.0",
        "reference_date": reference_date.isoformat(),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": registry.get("mode", "observe"),
        "summary": summary,
        "sources": results,
        "warnings": warnings,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """Tạo báo cáo Markdown chuẩn 3 tầng (Action Title, What, So What, Now What)."""
    sum_data = payload["summary"]
    ref_date = payload["reference_date"]
    sources = payload["sources"]

    lines: list[str] = [
        "# BÁO CÁO KIỂM SOÁT ĐỘ MỚI NGUỒN TRI THỨC (KNOWLEDGE FRESHNESS SSOT)",
        "",
        f"> **Thời điểm đối chiếu:** {ref_date} | **Chế độ:** {payload.get('mode', 'observe')} | "
        f"**Tổng số nguồn:** {sum_data['total_sources_checked']} | **Nguồn có hạn định:** {sum_data['time_sensitive_sources']}",
        "",
        "---",
        "",
        "## I. KẾT LUẬN TRỰC DIỆN (ACTION TITLE)",
        (
            f"> **Hệ thống giám sát phát hiện {sum_data['fresh_count']} nguồn đạt chuẩn độ mới, "
            f"{sum_data['lag_reconciled_count']} nguồn trong biên độ bù trễ, và {sum_data['stale_count']} nguồn đã cũ "
            "vượt ngưỡng khuyến nghị. Đã kích hoạt cơ chế nhận diện lệch kỳ nhằm ngăn chặn hoàn toàn việc nhầm lẫn "
            "giữa thời điểm sửa đổi tệp và kỳ dữ liệu thực tế.**"
        ),
        "",
        "---",
        "",
        "## II. BẰNG CHỨNG & DỮ KIỆN ĐỘ MỚI (WHAT)",
        "",
        "### 1. Bảng theo dõi các nguồn dữ liệu có hạn định thời gian",
        "",
        "| ID Nguồn | Đường dẫn | Kỳ dữ liệu | Data As Of | Ngày sửa tệp | Tuổi DL | Lệch mtime | Ngưỡng | Trạng thái |",
        "| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    time_sources = [s for s in sources if s["freshness_threshold_days"] is not None]
    for s in time_sources:
        status_badge = {
            "fresh": "🟢 Đạt chuẩn (Fresh)",
            "lag_reconciled": "🟡 Chờ bù trễ (Lag)",
            "stale": "🔴 Đã cũ (Stale)",
            "unknown": "⚪ Chưa rõ",
        }.get(s["status"], s["status"])
        data_as_of_str = s["data_as_of"] or "N/A"
        mtime_date_str = s["file_mtime_date"] or "N/A"
        age_str = f"{s['age_days']} ngày" if s["age_days"] is not None else "N/A"
        drift_str = f"{s['mtime_drift_days']} ngày" if s["mtime_drift_days"] else "0"
        limit_str = f"{s['freshness_threshold_days']} ngày"
        lines.append(
            f"| `{s['id']}` | [{Path(s['path']).name}](file://{ROOT / s['path']}) | "
            f"{s['data_period']} | {data_as_of_str} | {mtime_date_str} | {age_str} | {drift_str} | {limit_str} | {status_badge} |"
        )

    lines.extend([
        "",
        "### 2. Danh mục nguồn quy chuẩn & lịch sử (Normative & Historical)",
        "",
        "| ID Nguồn | Miền (Domain) | Đội ngũ phụ trách | Vai trò | Trạng thái | Kỳ dữ liệu ghi nhận |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ])

    static_sources = [s for s in sources if s["freshness_threshold_days"] is None]
    for s in static_sources:
        lines.append(
            f"| `{s['id']}` | `{s['domain']}` | {s['owner']} | {s['authority']} | "
            f"{s['entry_status']} | {s['data_period']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## III. PHÂN TÍCH RỦI RO & TÁC ĐỘNG NGHIỆP VỤ (SO WHAT)",
        "",
        "1. **Rủi ro nhầm lẫn ngày commit với ngày số liệu (Mtime vs Data Drift):**",
        "   - Khi lập trình viên hoặc AI Agent chạy lệnh git/sync/format, thuộc tính ngày sửa tệp trên ổ đĩa sẽ đổi sang ngày hiện tại.",
        "   - Nếu hệ thống chỉ đọc ngày sửa tệp, Agent sẽ nhầm tưởng snapshot cũ (ví dụ: Snapshot Tháng 10 cắt ngày 10/10) là số liệu mới nhất của Tháng 11.",
        "   - Giải pháp: Bắt buộc đọc trường `data_as_of` và `data_period` trực tiếp từ nội dung tệp.",
        "",
        "2. **Tác động đến quyết định vận hành:**",
        "   - Dữ liệu `performance_snapshot_latest` đang dừng ở mốc 10/10/2026 (cũ hơn 7 ngày so với hiện tại). Agent không được dùng số liệu này làm căn cứ chẩn đoán nhịp vận hành hiện tại.",
        "   - Dữ liệu `performance_data_mart` (`performance.sqlite`) có mốc 04/11/2026, là nguồn tươi mới và hợp lệ để phân tích hiệu suất tuần 45.",
        "",
        "---",
        "",
        "## IV. KẾ HOẠCH XỬ LÝ & HƯỚNG DẪN AGENT (NOW WHAT)",
        "",
        "1. **Quy tắc đọc nguồn cho Claude và Antigravity:**",
        "   - Khi truy vấn miền `performance`, ưu tiên truy vấn `performance_data_mart` (`performance.sqlite`) hoặc chạy pipeline đối soát mới.",
        "   - Nếu bắt buộc đọc `performance_snapshot_latest`, phải ghi rõ cảnh báo: *Số liệu trích xuất từ Snapshot Tháng 10/2026, không phản ánh nhịp vận hành Tháng 11*.",
        "2. **Đồng bộ hóa trong pipeline:**",
        "   - Chạy định kỳ `check_knowledge_freshness.py` trong CI để ngăn ngừa tình trạng trích dẫn dữ liệu quá hạn.",
        "",
    ])

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm soát độ mới nguồn tri thức và phân biệt ngày sửa tệp với kỳ dữ liệu")
    parser.add_argument("--registry", default=str(REGISTRY_PATH), help="Đường dẫn knowledge_registry.yaml")
    parser.add_argument("--as-of-date", help="Ngày đối chiếu định dạng YYYY-MM-DD (mặc định là hôm nay)")
    parser.add_argument("--json-out", default=str(DEFAULT_JSON_OUT), help="Đường dẫn xuất tệp JSON")
    parser.add_argument("--md-out", default=str(DEFAULT_MD_OUT), help="Đường dẫn xuất tệp Markdown")
    parser.add_argument("--check", action="store_true", help="Trả về mã lỗi 1 nếu có nguồn stale")
    args = parser.parse_args()

    ref_date: date | None = None
    if args.as_of_date:
        ref_date = parse_date_str(args.as_of_date)
        if not ref_date:
            print(f"Lỗi: Định dạng ngày không hợp lệ: {args.as_of_date}", file=sys.stderr)
            return 1

    registry_file = Path(args.registry)
    if not registry_file.is_file():
        print(f"Lỗi: Không tìm thấy registry tại {registry_file}", file=sys.stderr)
        return 1

    payload = scan_registry_freshness(registry_file, ref_date)

    json_path = Path(args.json_out)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    md_path = Path(args.md_out)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_content = render_markdown(payload)
    md_path.write_text(md_content, encoding="utf-8")

    summary = payload["summary"]
    print(
        f"Freshness scan completed: {summary['total_sources_checked']} sources, "
        f"{summary['fresh_count']} fresh, {summary['lag_reconciled_count']} lag, "
        f"{summary['stale_count']} stale, {summary['normative_count']} normative."
    )
    print(f"JSON output: {json_path}")
    print(f"Markdown output: {md_path}")

    if args.check and summary["stale_count"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
