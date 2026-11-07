#!/usr/bin/env python3
"""
scripts/detect_knowledge_conflicts.py
--------------------------------------
Phát hiện các xung đột đường dẫn, liên kết không tồn tại hoặc tham chiếu ngoại vi
trong toàn bộ kho tri thức Knowledge Base mà không tự ý sửa đổi tệp nguồn.
Vận hành ở chế độ quan sát (mode: observe).
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "00_HARNESS_CORE" / "knowledge_conflicts.json"
DEFAULT_MD_OUT = ROOT / "00_HARNESS_CORE" / "knowledge_conflicts.md"

SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    "graphify-out",
    ".claude",
    ".kilo",
}

TEXT_EXTENSIONS = {
    ".md",
    ".yaml",
    ".yml",
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".mts",
}

GENERATED_FILES = {
    "knowledge_conflicts.md",
    "knowledge_conflicts.json",
    "knowledge_inventory.md",
    "knowledge_inventory.json",
    "knowledge_conflict_triage.yaml",
    "knowledge_conflict_triage.json",
}

# Các thư mục hoặc tệp mẫu bên thứ ba không thuộc phạm vi kiểm tra liên kết nội bộ
IGNORED_PACKAGE_SUBSTRINGS = {
    "bold-template-pack",
}

# Các biến giữ chỗ trong tài liệu mẫu hoặc biểu thức regex/CLI
TEMPLATE_PLACEHOLDER_TOKENS = (
    "XX",
    "YYYY",
    "MM_",
    "{",
    "}",
    "<slug>",
    "<date>",
    "<id>",
    "<token>",
    "<account>",
    "<hub-name>",
    "<target>",
    "<file>",
    "<checkpoint>",
    "<conversation-id>",
    "<day>",
    "<metric>",
    "<name>",
    "<YYYY-MM-DD>",
    "...",
)


def is_template_placeholder(ref: str) -> bool:
    """Kiểm tra xem chuỗi có phải là biến giữ chỗ (placeholder) trong tài liệu mẫu hay không."""
    if any(token in ref for token in TEMPLATE_PLACEHOLDER_TOKENS):
        return True
    if ref.startswith("<") or ref.endswith(">"):
        return True
    if ref.startswith("[") or ref.endswith("]"):
        return True
    return False


def determine_conflict_details(ref: str, raw: str, source_path: Path, root: Path, line_text: str) -> tuple[str, str, str]:
    """
    Phân loại chi tiết và xác định lý do cho tham chiếu không giải quyết được.
    Trả về: (kind, reason, message)
    """
    relative_source = source_path.relative_to(root)
    is_code = source_path.suffix != ".md"

    # 1. Tham chiếu ngoại vi (External References)
    if "Web-Idea/" in ref or "react-web-momo/" in ref:
        return (
            "external_reference",
            "cross_repository_reference",
            "Tham chiếu liên kết sang repository Front-end Hub (react-web-momo)."
        )
    if "/Users/hienhv/Downloads/" in ref or "/Downloads/" in ref:
        return (
            "external_reference",
            "external_downloads_artifact",
            "Tham chiếu tệp tin tạm hoặc báo cáo xuất trong thư mục Downloads máy cục bộ."
        )
    if "Obsidian_Vault" in ref or "/Documents/Obsidian" in ref:
        return (
            "external_reference",
            "historical_vault_reference",
            "Tham chiếu lịch sử từ kho ghi chép cá nhân cũ (Obsidian Vault)."
        )
    if ref.startswith("../") and not (source_path.parent / ref).resolve().is_relative_to(root.resolve()):
        return (
            "external_reference",
            "outside_repository",
            "Đường dẫn tương đối trỏ ra ngoài phạm vi thư mục repository."
        )
    if Path(ref).is_absolute() and not Path(ref).resolve().is_relative_to(root.resolve()):
        return (
            "external_reference",
            "outside_repository",
            "Đường dẫn tuyệt đối trỏ ra ngoài phạm vi repository."
        )

    # 2. Tham chiếu trong Agent Skills
    if relative_source.parts and relative_source.parts[0] == ".agents":
        return (
            "skill_asset_reference",
            "skill_package_reference",
            "Tham chiếu tài nguyên cục bộ bên trong gói agent skill."
        )

    # 3. Tham chiếu trong mã nguồn hoặc tệp sinh runtime
    if is_code or any(token in line_text for token in ('"sync:', "cp ../", "cache/performance.sqlite", "output =")):
        return (
            "code_path_reference",
            "code_runtime_or_generated_path",
            "Đường dẫn trong mã nguồn kỹ thuật; có thể là tệp sinh ra khi chạy (runtime output)."
        )

    # 4. Liên kết nội bộ không tìm thấy tệp đích
    return (
        "broken_reference",
        "unresolved_internal_path",
        "Đường dẫn nội bộ không tìm thấy tệp đích trong repository."
    )


def scan(root: Path = ROOT) -> list[dict]:
    """Quét toàn bộ kho tri thức để tìm các tham chiếu lỗi hoặc cần kiểm tra."""
    findings = []
    pattern = re.compile(
        r"file://[^\s)\]>]+|(?<![\w/])(?:\.{1,2}/)*(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+\.(?:md|yaml|yml|json|sqlite|csv)"
    )

    for source in sorted(root.rglob("*")):
        if not source.is_file() or source.suffix not in TEXT_EXTENSIONS:
            continue
        relative = source.relative_to(root)
        rel_posix = relative.as_posix()

        # Bỏ qua các thư mục hệ thống, tệp tự sinh hoặc thư mục kiểm thử
        if any(part in SKIP_DIRS for part in relative.parts) or source.name in GENERATED_FILES:
            continue
        if relative.parts[:2] == ("scripts", "tests"):
            continue
        if any(ignored in rel_posix for ignored in IGNORED_PACKAGE_SUBSTRINGS):
            continue

        try:
            content = source.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        for number, line in enumerate(content.splitlines(), 1):
            for match in pattern.finditer(line):
                raw = match.group().rstrip("`\"'.,;")
                prefix = line[:match.start()]
                if "https://" in prefix or "http://" in prefix:
                    continue

                ref = unquote(raw.removeprefix("file://")).split("#")[0]
                if not raw.startswith("file://") and match.end() < len(line) and line[match.end()].isalnum():
                    continue

                # Bỏ qua các mẫu placeholder hoặc biến mẫu
                if is_template_placeholder(ref):
                    continue

                # Bỏ qua tệp thuộc gói template đã loại trừ
                if any(ignored in ref for ignored in IGNORED_PACKAGE_SUBSTRINGS):
                    continue

                # Xác định các đường dẫn khả dĩ
                targets = [Path(ref)] if Path(ref).is_absolute() else [source.parent / ref, root / ref.removeprefix("Base/")]
                internal_targets = []
                for target in targets:
                    try:
                        resolved = target.resolve()
                        if resolved.is_relative_to(root.resolve()):
                            internal_targets.append(resolved)
                    except (ValueError, OSError):
                        pass

                # Nếu tệp đích tồn tại thực tế trong repo -> Hợp lệ, bỏ qua
                if any(target.exists() for target in internal_targets):
                    continue

                kind, reason, message = determine_conflict_details(ref, raw, source, root, line)

                findings.append({
                    "kind": kind,
                    "reference": ref,
                    "raw_reference": raw,
                    "source": rel_posix,
                    "sources": [rel_posix],
                    "line": number,
                    "reason": reason,
                    "message": message,
                })

    return findings


def render_markdown(payload: dict) -> str:
    """Xuất báo cáo xung đột dưới dạng Markdown cấu trúc chuẩn mực."""
    counts = Counter(item["kind"] for item in payload["conflicts"])
    lines = [
        "# Báo Cáo Xung Đột & Kiểm Tra Đường Dẫn Kho Tri Thức (Knowledge Conflict Report)",
        "",
        f"- Thời điểm xuất bản: {payload['generated_at']}",
        f"- Chế độ vận hành: {payload['mode']} (Không tự ý sửa đổi mã nguồn)",
        f"- Tổng số điểm phát hiện: {payload['conflict_count']}",
        "",
        "## 1. Bảng Tổng Hợp Phân Loại",
        "",
        "| Phân loại | Số lượng | Ý nghĩa & Mô tả |",
        "| :--- | ---: | :--- |",
        f"| `broken_reference` | {counts.get('broken_reference', 0)} | Đường dẫn nội bộ không tìm thấy tệp đích |",
        f"| `external_reference` | {counts.get('external_reference', 0)} | Tham chiếu sang repo khác, thư mục Downloads hoặc Obsidian |",
        f"| `code_path_reference` | {counts.get('code_path_reference', 0)} | Đường dẫn trong mã nguồn; có thể là tệp sinh runtime |",
        f"| `skill_asset_reference` | {counts.get('skill_asset_reference', 0)} | Tài nguyên thuộc các gói Agent Skill |",
        "",
        "## 2. Nguyên Tắc Xử Lý",
        "",
        "- Báo cáo này hoàn toàn mang tính chất kiểm kê và phân loại (observe).",
        "- Tuyệt đối không tự động xóa, đổi tên hoặc hợp nhất nguồn khi chưa có phê duyệt từ Web Product Lead.",
        "",
        "## 3. Danh Sách Chi Tiết Theo Tệp Tin Nguồn",
        "",
    ]

    # Gom nhóm theo nguồn
    by_source = defaultdict(list)
    for item in payload["conflicts"]:
        src = item.get("source") or (item.get("sources", ["unknown"])[0])
        by_source[src].append(item)

    for src in sorted(by_source.keys()):
        lines.append(f"### `{src}`")
        lines.append("")
        for item in by_source[src]:
            line_no = item.get("line", "?")
            ref = item.get("reference", "unknown")
            kind = item.get("kind", "unknown")
            reason = item.get("reason", "requires_review")
            msg = item.get("message", "")
            lines.append(f"- **Dòng {line_no}:** `{ref}`")
            lines.append(f"  * Phân loại: `{kind}` | Mã lý do: `{reason}`")
            lines.append(f"  * Chi tiết: {msg}")
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Phát hiện và phân loại các xung đột đường dẫn trong Knowledge Base")
    parser.add_argument("--output", default=str(DEFAULT_OUT), help="Đường dẫn xuất tệp JSON")
    parser.add_argument("--markdown-output", default=str(DEFAULT_MD_OUT), help="Đường dẫn xuất tệp Markdown")
    args = parser.parse_args()

    conflicts = scan()
    payload = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "observe",
        "resolved": False,
        "conflict_count": len(conflicts),
        "conflicts": conflicts,
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md_out_path = Path(args.markdown_output)
    md_out_path.parent.mkdir(parents=True, exist_ok=True)
    md_out_path.write_text(render_markdown(payload), encoding="utf-8")

    print(f"Hoàn tất quét: Phát hiện {len(conflicts)} điểm cần rà soát (Đã khử sạch false positives từ template bên thứ ba).")
    counts = Counter(c["kind"] for c in conflicts)
    for k, v in sorted(counts.items()):
        print(f"  * {k}: {v}")
    print(f"  -> JSON: {out_path}")
    print(f"  -> Markdown: {md_out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
