#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/guard_vocabulary.py
---------------------------
Bộ lọc và bảo vệ từ ngữ chuẩn mực (Strict Vocabulary Guard SSOT) cho MoMo Web Platform.
Ngăn chặn và cảnh báo các từ ngữ sượng, AI buzzwords, En-dash/Em-dash, Priority tags (P0-P3),
và các thuật ngữ không chuẩn mực trong tài liệu PRD, BRD, Report và Markdown mới hoặc đang cập nhật.

Sử dụng:
    ./.venv/bin/python scripts/guard_vocabulary.py --staged          # Quét các file đang stage git
    ./.venv/bin/python scripts/guard_vocabulary.py --changed         # Quét các file mới/sửa đổi
    ./.venv/bin/python scripts/guard_vocabulary.py --check [files]   # Quét file/thư mục cụ thể
    ./.venv/bin/python scripts/guard_vocabulary.py --all             # Quét toàn bộ .md được git theo dõi
    ./.venv/bin/python scripts/guard_vocabulary.py --all --rule EN_EM_DASH  # Chỉ một rule
    ./.venv/bin/python scripts/guard_vocabulary.py --install-hook    # Cài đặt git pre-commit hook
    ./.venv/bin/python scripts/guard_vocabulary.py --fix [files]     # Tự động thay thế các từ cấm
"""

import sys
import os
import re
import argparse
import subprocess
from pathlib import Path
from typing import List, Tuple, Dict, Any, Optional

# Danh sách file / thư mục ngoại lệ (chứa danh mục từ điển để tra cứu hoặc mã nguồn hệ thống)
IGNORE_FILES = {
    "momo-reporting-glossary.md",
    "guard_vocabulary.py",
    "AGENTS.md",
}

IGNORE_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    ".gemini",
    "graphify-out",
    "archive",
    "scratch",
    "_archive",
    "frontend-slides",  # skill bên thứ ba (vendored, có LICENSE riêng)
}

# Định nghĩa các quy tắc kiểm tra (Rules)
# Mỗi rule gồm: (ID, Regex Pattern, Flag, Mô tả, Khuyến nghị thay thế, Có thể tự động fix)
RULES = [
    {
        "id": "EN_EM_DASH",
        "pattern": r"[\u2013\u2014]",
        "flags": 0,
        "desc": "Ký tự En Dash (–) hoặc Em Dash (—) bị cấm",
        "replacement": "Dùng dấu gạch ngang chuẩn Hyphen (-) cho khoảng số hoặc tách câu bằng dấu hai chấm (:), ngoặc đơn",
        "auto_fix": None, # Không auto fix mù quáng vì ngữ cảnh En/Em dash có thể là gạch nối hoặc tách câu
    },
    {
        "id": "PRIORITY_TAG",
        # "Priority 0.9" (sitemap priority) không phải nhãn ưu tiên -> loại bằng (?![.,]\d)
        "pattern": r"(?i)\b(P0|P1|P2|P3|Priority\s*[0-3](?![.,]\d))\b",
        "flags": 0,
        "desc": "Nhãn mức độ ưu tiên P0/P1/P2/P3 bị cấm",
        "replacement": "Trình bày theo thứ tự triển khai logic, gạch đầu dòng tự nhiên hoặc nhóm chuyên môn",
        "auto_fix": None,
    },
    {
        "id": "PHAN_HE",
        "pattern": r"(?i)\bphân\s+hệ\b",
        "flags": 0,
        "desc": "Từ 'phân hệ' mang phong cách phần mềm bao cấp",
        "replacement": "Module, Khu vực chức năng, hoặc Mảng sản phẩm (Hub)",
        "auto_fix": "module",
    },
    {
        "id": "PHAN_RA",
        "pattern": r"(?i)\b(bảng\s+)?phân\s+rã(\s+(lưu\s+lượng|kênh|số\s+liệu|dữ\s+liệu|hub|phễu))?\b",
        "flags": 0,
        "desc": "Từ 'phân rã' dịch thô từ Breakdown, mang hàm ý hạt nhân/phân hủy",
        "replacement": "cơ cấu lưu lượng, phân bổ, hoặc bóc tách chi tiết",
        "auto_fix": "cơ cấu",
    },
    {
        "id": "PHAT_HANH_FEATURE",
        "pattern": r"(?i)\b(phát\s+hành(\s+chính\s+thức)?\s+(lên\s+production|trên\s+production|trang|công\s+cụ|tính\s+năng|phase|giao\s+diện|tiện\s+ích|web)|kế\s+hoạch\s+phát\s+hành|sau\s+khi\s+phát\s+hành|sau\s+phát\s+hành)\b",
        "flags": 0,
        "desc": "Từ 'phát hành' là từ ngành báo chí/in ấn/vé số, không phải thuật ngữ Product",
        "replacement": "Ra mắt (Launch), Chính thức Go-live, Triển khai lên Production (Deploy), hoặc Đưa vào hoạt động",
        "auto_fix": "Go-live",
    },
    {
        "id": "TRAM_TAI_APP",
        "pattern": r"(?i)\btrạm\s+(tải\s+app|chuyển\s+đổi)\b",
        "flags": 0,
        "desc": "Từ 'trạm tải app / trạm chuyển đổi' nghe như trạm xăng/bến xe",
        "replacement": "Trang Tải Ứng Dụng (App Download Page / momo.vn/tai-app) hoặc Cổng chuyển đổi tập trung",
        "auto_fix": "Trang Tải Ứng Dụng",
    },
    {
        "id": "DINH_CAO",
        "pattern": r"(?i)\bđỉnh\s+cao\b",
        "flags": 0,
        "desc": "Từ 'đỉnh cao' là văn PR thổi phồng, thiếu khách quan",
        "replacement": "hiệu suất cao nhất, chất lượng tối ưu, hoặc khung giờ cao điểm",
        "auto_fix": "hiệu suất cao nhất",
    },
    {
        "id": "DAT_DINH",
        "pattern": r"(?i)\bđạt\s+đỉnh(\s+mới)?\b",
        "flags": 0,
        "desc": "Từ 'đạt đỉnh' mang hàm ý sau đó sẽ rơi dốc",
        "replacement": "thiết lập mức kỷ lục mới, chạm mốc cao nhất từ đầu năm, hoặc ghi nhận mức cao nhất",
        "auto_fix": "chạm mốc kỷ lục",
    },
    {
        "id": "CHU_TRI",
        "pattern": r"(?i)\bchủ\s+trì\b",
        "flags": 0,
        "desc": "Từ 'chủ trì' mang nặng văn phong hành chính bao cấp",
        "replacement": "điều phối, đầu mối thực hiện, hoặc chịu trách nhiệm (Owner/Lead)",
        "auto_fix": "điều phối",
    },
    {
        "id": "DU_PHONG",
        "pattern": r"(?i)\bdự\s+phóng\b",
        "flags": 0,
        "desc": "Từ 'dự phóng' là từ Hán-Việt cổ, trịnh trọng thái quá",
        "replacement": "dự báo kết tháng (Forecast) hoặc ước tính theo nhịp chạy (Run-rate)",
        "auto_fix": "dự báo",
    },
    {
        "id": "THAU_TOM",
        "pattern": r"(?i)\bthâu\s+tóm\b",
        "flags": 0,
        "desc": "Từ 'thâu tóm' mang tính quân sự, bạo lực hoặc M&A thù địch",
        "replacement": "bao phủ thị trường (cover), chiếm lĩnh thị phần tìm kiếm, hoặc thu hút lưu lượng",
        "auto_fix": "bao phủ",
    },
    {
        "id": "BAT_DOI_XUNG",
        "pattern": r"(?i)\b(đánh|tấn\s+công)\s+bất\s+đối\s+xứng\b",
        "flags": 0,
        "desc": "Cụm từ quân sự hóa",
        "replacement": "chiến lược cạnh tranh khác biệt, hoặc tiếp cận ngách giá trị cao",
        "auto_fix": "tiếp cận khác biệt",
    },
    {
        "id": "MOI_CAU",
        "pattern": r"(?i)\b(phễu\s+)?mồi\s+câu\b",
        "flags": 0,
        "desc": "Từ 'mồi câu' mang cảm giác bẫy người dùng",
        "replacement": "tiện ích thu hút, điểm chạm kích hoạt (Engagement Hooks)",
        "auto_fix": "tiện ích thu hút",
    },
    {
        "id": "HUNG_TRON",
        "pattern": r"(?i)\bhứng\s+trọn\b",
        "flags": 0,
        "desc": "Khẩu ngữ đời thường, thiếu tính chuyên nghiệp",
        "replacement": "đón nhận trọn vẹn, khai thác toàn bộ, hoặc hấp thu lưu lượng",
        "auto_fix": "đón nhận trọn vẹn",
    },
    {
        "id": "MU_INTERNET",
        "pattern": r"(?i)\bmù\s+internet\b",
        "flags": 0,
        "desc": "Khẩu ngữ giật gân, thiếu chuyên nghiệp",
        "replacement": "mất kết nối mạng khi hạ cánh",
        "auto_fix": "mất kết nối mạng",
    },
    {
        "id": "SHOCK_BILL",
        "pattern": r"(?i)\bshock\s+bill\b",
        "flags": 0,
        "desc": "Từ ngữ lóng, không trang trọng",
        "replacement": "phát sinh cước chuyển vùng ngoài ý muốn",
        "auto_fix": "phát sinh cước ngoài ý muốn",
    },
    {
        "id": "PHAN_KHOI_PHU_TRACH",
        "pattern": r"(?i)\bphân\s+khối\s+phụ\s+trách\b",
        "flags": 0,
        "desc": "Dịch sai từ Division",
        "replacement": "Khối phụ trách, hoặc Đơn vị phụ trách",
        "auto_fix": "Khối phụ trách",
    },
    {
        "id": "BUA_TOI_GIA_DINH",
        "pattern": r"(?i)\bbữa\s+tối\s+gia\s+đình\s+test\b",
        "flags": 0,
        "desc": "Khẩu ngữ nội bộ đặt sai văn cảnh tài liệu",
        "replacement": "Tiêu chuẩn trải nghiệm đột phá (Aha Moment) hoặc Tiêu chuẩn đại chúng",
        "auto_fix": "Tiêu chuẩn trải nghiệm đột phá (Aha Moment)",
    },
    {
        "id": "VAN_HIEN_SIGN_OFF",
        "pattern": r"(?i)\b(văn\s+hiến\s+sign-?off|chủ\s+trì:\s*văn\s+hiến)\b",
        "flags": 0,
        "desc": "Ghi đích danh cá nhân vi phạm nguyên tắc tài liệu tổ chức",
        "replacement": "Web Platform phê duyệt / Web Platform sign-off",
        "auto_fix": "Web Platform sign-off",
    },
    {
        "id": "BAM_NUT",
        "pattern": r"(?i)\bbấm\s+nút(\s+cta|\s+publish)?\b",
        "flags": 0,
        "desc": "Từ ngữ khẩu ngữ văn nói bình dân",
        "replacement": "nhấp vào nút / CTA, kích hoạt triển khai, hoặc thực hiện xuất bản (Publish)",
        "auto_fix": "nhấp vào nút",
    },
    {
        "id": "TRIET_TIEU_MA_SAT",
        "pattern": r"(?i)\b(triệt\s+tiêu\s+ma\s+sát|giảm\s+ma\s+sát|không\s+ma\s+sát)\b",
        "flags": 0,
        "desc": "Dịch cơ học từ user friction",
        "replacement": "giảm rào cản thao tác, xóa bỏ điểm nghẽn, hoặc luồng thao tác liền mạch",
        "auto_fix": "giảm rào cản thao tác",
    },
    {
        "id": "VUNG_TRUNG",
        "pattern": r"(?i)\bvùng\s+trũng(\s+traffic)?\b",
        "flags": 0,
        "desc": "Từ ngữ sáo rỗng giống dự báo thời tiết lũ lụt",
        "replacement": "lưu lượng còn thấp, chưa có lưu lượng tự nhiên, hoặc đóng góp khiêm tốn",
        "auto_fix": "lưu lượng còn thấp",
    },
    {
        "id": "DON_THUOC",
        "pattern": r"(?i)\bđơn\s+thuốc\s+hành\s+động\b",
        "flags": 0,
        "desc": "Văn phong AI sáo rỗng",
        "replacement": "kế hoạch xử lý, giải pháp khắc phục, hoặc hành động trọng tâm",
        "auto_fix": "kế hoạch xử lý",
    },
    {
        "id": "HAO_NUOC",
        "pattern": r"(?i)\bhào\s+nước(\s+dữ\s+liệu)?\b",
        "flags": 0,
        "desc": "Dịch thô từ moat / data moat",
        "replacement": "lợi thế phòng thủ dữ liệu, rào cản cạnh tranh, hoặc Data Moat",
        "auto_fix": "lợi thế phòng thủ dữ liệu",
    },
    {
        "id": "NOI_DAU",
        "pattern": r"(?i)\bnỗi\s+đau(\s+(của\s+)?(người\s+dùng|khách\s+hàng|sinh\s+viên|lớn\s+nhất))?\b",
        "flags": 0,
        "desc": "Dịch thô từ pain points, sến súa và thiếu tính kỹ thuật",
        "replacement": "rào cản thao tác, điểm nghẽn trải nghiệm, hoặc khó khăn của người dùng",
        "auto_fix": "rào cản người dùng",
    },
    {
        "id": "CHI_TIEU_TRA_THU",
        "pattern": r"(?i)\bchi\s+tiêu\s+trả\s+thù\b",
        "flags": 0,
        "desc": "Dịch thô từ Revenge Spending",
        "replacement": "chi tiêu bù đắp quá độ, hoặc mua sắm giải tỏa tâm lý",
        "auto_fix": "chi tiêu bù đắp quá độ",
    },
    {
        "id": "MUC_TIEU_TOI_THUONG",
        "pattern": r"(?i)\bmục\s+tiêu\s+tối\s+thượng\b",
        "flags": 0,
        "desc": "Văn phong triết lý, thổi phồng",
        "replacement": "mục tiêu kinh doanh cốt lõi (Primary Business Objective)",
        "auto_fix": "mục tiêu cốt lõi",
    },
    {
        "id": "BAY_KIET_SUC",
        "pattern": r"(?i)\bbẫy\s+kiệt\s+sức\b",
        "flags": 0,
        "desc": "Dịch thô từ Burnout trap",
        "replacement": "ngưỡng áp lực tài chính, hoặc kiệt quệ tâm lý do tiết kiệm quá mức",
        "auto_fix": "ngưỡng áp lực tài chính",
    },
    {
        "id": "TA_THE",
        "pattern": r"(?i)\btạ\s+thế(\s+sớm)?\b",
        "flags": 0,
        "desc": "Văn phong cáo phó cổ trang phong kiến",
        "replacement": "kịch bản kết thúc sớm, hoặc mô phỏng rủi ro đột ngột",
        "auto_fix": "kịch bản kết thúc sớm",
    },
    {
        "id": "SAN_LUONG_TRAFFIC",
        "pattern": r"(?i)\bsản\s+lượng\s+(truy\s+cập|thất\s+thoát|chuyển\s+đổi|traffic|pv|pageview|người\s+dùng|khách\s+hàng)\b",
        "flags": 0,
        "desc": "Dùng từ sản lượng cho traffic / chuyển đổi web (thuật ngữ cơ khí / sản xuất công nghiệp)",
        "replacement": "lưu lượng truy cập, lượt truy cập (Pageviews/Sessions), hoặc mục tiêu chuyển đổi Web-to-App",
        "auto_fix": "lưu lượng",
    },
    {
        "id": "GOI_QUA_TAN_THU",
        "pattern": r"(?i)\b((gói\s+)?quà\s+(tặng\s+)?tân\s+thủ|tân\s+thủ)\b",
        "flags": 0,
        "desc": "Từ 'gói quà tân thủ / quà tân thủ / tân thủ' bị cấm (từ lóng game), thay bằng 'Gói quà CHAOMOMO' hoặc 'người dùng mới'",
        "replacement": "Gói quà CHAOMOMO (cho gói quà) hoặc người dùng mới (cho user)",
        "auto_fix": "Gói quà CHAOMOMO",
    },
    {
        "id": "MA_TRAN_LAM_DUNG",
        "pattern": r"(?i)\b((bảng\s+)?ma\s+trận\s+(tóm\s+tắt|chi\s+tiết|liên\s+kết|phân\s+bổ|kế\s+hoạch|kpis?|ngân\s+sách|quy\s+hoạch|hành\s+động)|bảng\s+ma\s+trận)\b",
        "flags": 0,
        "desc": "Lạm dụng chữ 'ma trận' cho bảng biểu, kế hoạch thông thường (AI buzzword sáo rỗng)",
        "replacement": "bảng tổng hợp, bảng phân bổ, bảng liên kết, khung kế hoạch, hoặc bảng chi tiết",
        "auto_fix": "bảng tổng hợp",
    },
    {
        "id": "THI_CONG_LAM_DUNG",
        "pattern": r"(?i)\b((nguyên\s+tắc\s+)?thi\s+công(\s+(dự\s+án|tính\s+năng|web|hub|ui|frontend|backend|hệ\s+thống|ban\s+đêm|kỹ\s+thuật|nền\s+tảng))?)\b",
        "flags": 0,
        "desc": "Dùng từ 'thi công' (ngành xây dựng, công trình) cho phần mềm / sản phẩm số; thay bằng 'triển khai', 'thực thi' hoặc 'phát triển'",
        "replacement": "nguyên tắc triển khai, phương thức thực thi, phát triển, hoặc triển khai kỹ thuật",
        "auto_fix": "triển khai",
    },
    {
        "id": "KIEM_THU_LAM_DUNG",
        "pattern": r"(?i)\bkiểm\s+thử(\s+(kỹ\s+thuật|chức\s+năng|toàn\s+diện|hệ\s+thống|production|staging|uat))?\b",
        "flags": 0,
        "desc": "Từ 'kiểm thử' mang tính giáo trình sách vở/hành chính cũ; trong báo cáo và văn bản quản trị thay bằng 'nghiệm thu kỹ thuật', 'đánh giá chất lượng', hoặc giữ nguyên 'test', 'test cases', 'UAT'",
        "replacement": "nghiệm thu kỹ thuật, đánh giá chất lượng, hoàn tất UAT, hoặc chạy test",
        "auto_fix": "nghiệm thu kỹ thuật",
    },
]


# Các file dùng P1-P4 làm mã trụ cột MoSpark (P1 Tài chính & Tín dụng, P2 Bảo hiểm, P3 Dịch vụ Công & Tiện ích,
# P4 Đời sống & Merchant). Đây là định danh Pillar, không phải nhãn ưu tiên.
PILLAR_CODE_FILES = {
    "01_STRATEGIC_PLAN/product-lead.md",
    "03_SKILLS/mospark-glossary.md",
    "04_MOSPARK_PLATFORM/mospark_master.md",
    "04_MOSPARK_PLATFORM/mospark_microsite_management.md",
}

class VocabularyGuard:
    def __init__(self, workspace_root: Optional[Path] = None):
        if workspace_root is None:
            workspace_root = Path(__file__).resolve().parent.parent
        self.workspace_root = workspace_root

    rule_filter: Optional[set] = None

    def get_all_tracked_files(self) -> List[Path]:
        """Toàn bộ file markdown đang được git theo dõi (quét cả vi phạm cũ, không chỉ file đang sửa)."""
        try:
            out = subprocess.run(["git", "ls-files", "-z", "*.md"], cwd=self.workspace_root,
                                 capture_output=True, text=True, check=True).stdout
        except Exception:
            return []
        return [self.workspace_root / f for f in out.split("\0") if f and not self.is_ignored(self.workspace_root / f)]

    def is_ignored(self, file_path: Path) -> bool:
        """Kiểm tra file hoặc đường dẫn có nằm trong danh sách bỏ qua không."""
        if file_path.name in IGNORE_FILES:
            return True
        for part in file_path.parts:
            if part in IGNORE_DIRS:
                return True
        return False

    def check_file(self, file_path: Path) -> List[Dict[str, Any]]:
        """Quét 1 file cụ thể và trả về danh sách các vi phạm."""
        violations = []
        if self.is_ignored(file_path):
            return violations

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
        except Exception as e:
            return violations

        rel_path = file_path.relative_to(self.workspace_root).as_posix() if file_path.is_relative_to(self.workspace_root) else str(file_path)
        active_rules = [r for r in RULES if not self.rule_filter or r["id"] in self.rule_filter]
        in_fence = False
        for line_num, line in enumerate(lines, start=1):
            if line.lstrip().startswith(("```", "~~~")):
                in_fence = not in_fence
            for rule in active_rules:
                # P0-P3 trong code fence (Mermaid node/subgraph ID, sơ đồ ASCII) là định danh, không phải nhãn ưu tiên
                if rule["id"] == "PRIORITY_TAG" and in_fence:
                    continue
                pattern = rule["pattern"]
                matches = list(re.finditer(pattern, line, flags=rule["flags"]))
                for match in matches:
                    matched_text = match.group(0)
                    # Ngoại lệ hợp lý: ký tự được trích dẫn trong backtick (`–`) để định nghĩa luật,
                    # hoặc nằm bên trong một URL. Không bỏ qua cả dòng chỉ vì dòng có chứa link.
                    if rule["id"] == "PRIORITY_TAG":
                        # Mã giai đoạn / điều kiện / Pillar (P1-P4 trụ cột MoSpark) là định danh, không phải nhãn ưu tiên
                        if re.search(r"(?i)(giai\s+đoạn|phase|pre-condition|pillar|trụ\s+cột)\s*$", line[: match.start()]):
                            continue
                        # File MoSpark dùng P1-P4 làm mã 4 trụ cột (Pillar). P0 vẫn bị chặn vì không phải mã Pillar.
                        if rel_path in PILLAR_CODE_FILES and matched_text.upper() in ("P1", "P2", "P3"):
                            continue
                    if rule["id"] == "EN_EM_DASH":
                        st, en = match.start(), match.end()
                        if st > 0 and en < len(line) and line[st - 1] == "`" and line[en] == "`":
                            continue
                        if any(u.start() <= st < u.end() for u in re.finditer(r"(?:https?|file)://\S+", line)):
                            continue

                    violations.append({
                        "file": str(file_path.relative_to(self.workspace_root) if file_path.is_relative_to(self.workspace_root) else file_path),
                        "abs_path": file_path,
                        "line": line_num,
                        "col": match.start() + 1,
                        "rule_id": rule["id"],
                        "matched": matched_text,
                        "desc": rule["desc"],
                        "replacement": rule["replacement"],
                        "line_content": line.strip(),
                        "auto_fix": rule["auto_fix"],
                    })

        return violations

    def get_staged_files(self) -> List[Path]:
        """Lấy danh sách các file markdown đang staged trong git."""
        try:
            res = subprocess.run(
                ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
                cwd=str(self.workspace_root),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            files = []
            for line in res.stdout.strip().split("\n"):
                line = line.strip()
                if line and (line.endswith(".md") or line.endswith(".txt")):
                    p = self.workspace_root / line
                    if p.is_file():
                        files.append(p)
            return files
        except Exception:
            return []

    def get_changed_files(self) -> List[Path]:
        """Lấy danh sách các file markdown mới hoặc bị thay đổi trong git working tree."""
        try:
            res = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=str(self.workspace_root),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            files = []
            for line in res.stdout.strip().split("\n"):
                if not line.strip():
                    continue
                # Format: XY PATH
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    file_str = parts[1]
                    if file_str.endswith(".md") or file_str.endswith(".txt"):
                        p = self.workspace_root / file_str
                        if p.is_file():
                            files.append(p)
            return files
        except Exception:
            return []

    def scan_directories(self, target_dirs: List[str]) -> List[Path]:
        """Quét toàn bộ file markdown trong các thư mục chỉ định."""
        files = []
        for d in target_dirs:
            dp = self.workspace_root / d
            if dp.is_dir():
                for p in dp.rglob("*.md"):
                    if not self.is_ignored(p):
                        files.append(p)
        return files

    def install_git_hook(self) -> bool:
        """Cài đặt pre-commit hook vào .git/hooks/pre-commit."""
        hook_path = self.workspace_root / ".git" / "hooks" / "pre-commit"
        hook_content = """#!/usr/bin/env bash
# MoMo Web Platform - Pre-commit Strict Vocabulary Guard Hook
PYTHON="./.venv/bin/python"
if [ ! -f "$PYTHON" ]; then
    PYTHON="python3"
fi

$PYTHON scripts/guard_vocabulary.py --staged
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo "❌ [STRICT GUARD BLOCKED] Phát hiện từ ngữ bị cấm hoặc vi phạm quy chuẩn văn phong!"
    echo "💡 Xem hướng dẫn sửa ở trên hoặc chạy: ./.venv/bin/python scripts/guard_vocabulary.py --staged"
    exit 1
fi
exit 0
"""
        try:
            hook_path.parent.mkdir(parents=True, exist_ok=True)
            with open(hook_path, "w", encoding="utf-8") as f:
                f.write(hook_content)
            # Gán quyền thực thi
            os.chmod(hook_path, 0o755)
            print(f"✅ Đã cài đặt git pre-commit hook thành công tại: {hook_path}")
            return True
        except Exception as e:
            print(f"❌ Không thể cài đặt hook: {e}")
            return False

    def auto_fix_files(self, files: List[Path]) -> int:
        """Tự động sửa các từ ngữ vi phạm có thể fix an toàn."""
        total_fixed = 0
        for fp in files:
            if self.is_ignored(fp):
                continue
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    content = f.read()

                orig_content = content
                for rule in RULES:
                    if rule["auto_fix"]:
                        pattern = rule["pattern"]
                        # Thực hiện thay thế
                        content = re.sub(pattern, rule["auto_fix"], content, flags=rule["flags"])

                if content != orig_content:
                    with open(fp, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"🛠️ Đã tự động cập nhật: {fp.relative_to(self.workspace_root)}")
                    total_fixed += 1
            except Exception as e:
                print(f"❌ Lỗi khi sửa file {fp}: {e}")
        return total_fixed

def main():
    parser = argparse.ArgumentParser(description="Strict Vocabulary Guard for MoMo Web Platform")
    parser.add_argument("--staged", action="store_true", help="Kiểm tra các file đang staged trong git")
    parser.add_argument("--changed", action="store_true", help="Kiểm tra các file đang sửa đổi trong git")
    parser.add_argument("--install-hook", action="store_true", help="Cài đặt git pre-commit hook")
    parser.add_argument("--fix", action="store_true", help="Tự động sửa các lỗi từ ngữ an toàn")
    parser.add_argument("--check", nargs="*", help="Kiểm tra các file hoặc thư mục chỉ định")
    parser.add_argument("--all", action="store_true", help="Kiểm tra toàn bộ file markdown được git theo dõi (bắt cả vi phạm cũ)")
    parser.add_argument("--rule", action="append", help="Chỉ áp dụng rule ID chỉ định (lặp lại được), ví dụ --rule EN_EM_DASH")

    args = parser.parse_args()
    guard = VocabularyGuard()
    if args.rule:
        guard.rule_filter = set(args.rule)

    if args.install_hook:
        guard.install_git_hook()
        sys.exit(0)

    files_to_check = []
    if args.all:
        files_to_check = guard.get_all_tracked_files()
    elif args.staged:
        files_to_check = guard.get_staged_files()
        if not files_to_check:
            print("ℹ️ Không có file markdown nào đang staged trong git.")
            sys.exit(0)
    elif args.changed:
        files_to_check = guard.get_changed_files()
        if not files_to_check:
            print("ℹ️ Không có file markdown nào bị sửa đổi trong git working tree.")
            sys.exit(0)
    elif args.check:
        for c in args.check:
            cp = Path(c).resolve()
            if cp.is_file():
                files_to_check.append(cp)
            elif cp.is_dir():
                for p in cp.rglob("*.md"):
                    if not guard.is_ignored(p):
                        files_to_check.append(p)
    else:
        # Mặc định quét các thư mục trọng yếu nếu không truyền tham số: 05_HUBS, 06_USE_CASE_MOMO, 07_REPORTS, 09_PRD
        target_dirs = ["05_HUBS", "06_USE_CASE_MOMO", "07_REPORTS", "09_PRD", "01_STRATEGIC_PLAN"]
        files_to_check = guard.scan_directories(target_dirs)

    if args.fix:
        print(f"🚀 Bắt đầu tự động sửa {len(files_to_check)} files...")
        fixed_count = guard.auto_fix_files(files_to_check)
        print(f"✅ Hoàn tất sửa {fixed_count} files.")
        sys.exit(0)

    # Tiến hành kiểm tra
    total_violations = 0
    violations_by_file: Dict[str, List[Dict[str, Any]]] = {}

    for fp in files_to_check:
        v_list = guard.check_file(fp)
        if v_list:
            violations_by_file[str(fp)] = v_list
            total_violations += len(v_list)

    if total_violations == 0:
        print(f"✅ [VOCABULARY GUARD PASSED] Toàn bộ {len(files_to_check)} files đã kiểm tra hoàn toàn sạch, đạt chuẩn mực!")
        sys.exit(0)

    print("=" * 80)
    print(f"❌ [VOCABULARY GUARD FAILED] Phát hiện {total_violations} vi phạm từ ngữ trong {len(violations_by_file)} files:")
    print("=" * 80)

    for f_path, v_list in violations_by_file.items():
        rel_path = Path(f_path).relative_to(guard.workspace_root) if Path(f_path).is_relative_to(guard.workspace_root) else f_path
        print(f"\n📄 {rel_path} ({len(v_list)} lỗi):")
        for v in v_list:
            print(f"  • Dòng {v['line']}:{v['col']} [{v['rule_id']}] Từ vi phạm: \"{v['matched']}\"")
            print(f"    ↳ Lý do: {v['desc']}")
            print(f"    ↳ Đề xuất: {v['replacement']}")
            print(f"    ↳ Trích dẫn: {v['line_content'][:100]}...")

    print("\n" + "=" * 80)
    print("💡 Hướng xử lý:")
    print("1. Chỉnh sửa thủ công theo đề xuất ở trên.")
    print("2. Hoặc chạy tự động thay thế an toàn: ./.venv/bin/python scripts/guard_vocabulary.py --fix [files]")
    print("=" * 80)
    sys.exit(1)

if __name__ == "__main__":
    main()
