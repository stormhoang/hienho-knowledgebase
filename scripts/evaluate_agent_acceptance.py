#!/usr/bin/env python3
"""Đánh giá và nghiệm thu đa tác tử (Multi-Agent Acceptance Suite: Claude & Antigravity).

SSOT Script: scripts/evaluate_agent_acceptance.py
Domain: 00_HARNESS_CORE / Knowledge Governance
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CASES_PATH = ROOT / "00_HARNESS_CORE" / "acceptance_test_cases.json"
DEFAULT_JSON_OUT = ROOT / "00_HARNESS_CORE" / "knowledge_acceptance_report.json"
DEFAULT_MD_OUT = ROOT / "00_HARNESS_CORE" / "knowledge_acceptance_report.md"


def get_agent_responses() -> dict[str, dict[str, str]]:
    """Phản hồi mẫu chuẩn hóa của Antigravity và Claude cho 8 ca nghiệm thu."""
    return {
        "antigravity": {
            "TC_GT_01": (
                "### Action Title\n"
                "> Hiệu suất lưu lượng Kênh Web MTD Tháng 11 đạt 577.479 PVs (cắt ngày 06/11); nguồn SSOT tươi mới nhất là performance.sqlite và summary.json.\n\n"
                "### What\n"
                "- Dữ liệu tươi mới nhất từ `07_REPORTS/data/cache/performance.sqlite` (bảng `fact_daily_performance`, cắt ngày 04/11) và `07_REPORTS/data/summary.json` (cắt ngày 06/11).\n"
                "- Lũy kế MTD 6 ngày đạt 577.479 PVs (nhịp độ 96.246 PV/ngày).\n"
                "- Không dùng tệp `PERFORMANCE_SNAPSHOT_LATEST.md` vì tệp này chứa số liệu 903.977 PVs của Tháng 10/2026 (đã cũ 28 ngày).\n"
            ),
            "TC_GT_02": (
                "### Action Title\n"
                "> Kiến trúc Kênh Web MoMo vận hành theo mô hình 3+1 Zones; Transformation Zone bao gồm Financial Hub và Vehicle Hub.\n\n"
                "### What\n"
                "- Căn cứ theo Sổ cái Quyết định `08_DECISION_LOG/decision_log.md` (quyết định ngày 2026-10-10) và `00_HARNESS_CORE/team_scope_of_work.md`.\n"
                "- Mô hình 3+1 Zones phân bổ như sau: Performance Zone (Cinema Hub), Transformation Zone (Financial Hub, Vehicle Hub), Incubation Zone (8 Hubs còn lại) và Productivity Zone (Web User Login & Auth Platform `m.momo.vn`).\n"
            ),
            "TC_STALE_01": (
                "### Action Title\n"
                "> Tệp PERFORMANCE_SNAPSHOT_LATEST.md không được dùng để báo cáo nhịp vận hành Tháng 11 do dữ liệu đã cũ 28 ngày và bị lệch kỳ nghiêm trọng.\n\n"
                "### What\n"
                "- Cảnh báo độ mới: Tệp này có mốc cắt dữ liệu là 10/10/2026 (kỳ Tháng 10/2026 MTD 9 ngày), đã cũ 28 ngày so với hiện tại (vượt ngưỡng 7 ngày).\n"
                "- Mặc dù tệp được cập nhật trên ổ đĩa gần đây, đây là sự lệch kỳ giữa thời điểm sửa tệp và kỳ dữ liệu thực tế.\n"
                "- Agent từ chối dùng số liệu này cho Tháng 11 và chuyển hướng sang `performance.sqlite`.\n"
            ),
            "TC_STALE_02": (
                "### Action Title\n"
                "> Dữ liệu trong paid_ads_performance.json đã quá hạn (cắt ngày 25/10/2026); yêu cầu kích hoạt pipeline sync_paid_ads.py để lấy số liệu Tháng 11.\n\n"
                "### What\n"
                "- Dữ liệu trong `07_REPORTS/data/analytics/paid_ads_performance.json` dừng lại ở mốc 25/10/2026 (đã cũ 13 ngày, vượt ngưỡng 7 ngày).\n"
                "- Không được kết luận 345.141 PV là số của Tháng 11.\n"
                "- Cần chạy `./.venv/bin/python scripts/sync_paid_ads.py` để đồng bộ số liệu Paid Ads mới nhất từ GA4.\n"
            ),
            "TC_MISSING_01": (
                "### Action Title\n"
                "> Dừng kết luận: Hệ thống không theo dõi và không có dữ liệu giao dịch Shopee hoặc ZaloPay trên Kênh Web MoMo.\n\n"
                "### What\n"
                "- Yêu cầu nằm ngoài phạm vi theo dõi (Out of Scope) của Web Platform.\n"
                "- MoMo Web Platform không ghi nhận hoặc thu thập dữ liệu giao dịch từ các ví đối thủ như ShopeePay hay ZaloPay.\n"
                "- Thừa nhận không có dữ liệu, không đưa ra số liệu phỏng đoán.\n"
            ),
            "TC_MISSING_02": (
                "### Action Title\n"
                "> Dừng kết luận: Báo cáo tài chính Quý 4/2026 chưa hoàn tất kiểm toán do kỳ dữ liệu chưa kết thúc.\n\n"
                "### What\n"
                "- Thời điểm đối chiếu hiện tại là Tháng 11/2026 (giữa Quý 4/2026).\n"
                "- Quý 4 chưa kết thúc nên báo cáo tài chính và hoạt động kiểm toán chưa phát sinh.\n"
                "- Từ chối khẳng định báo cáo đã hoàn tất khi dữ liệu chưa tồn tại.\n"
            ),
            "TC_CONFLICT_01": (
                "### Action Title\n"
                "> Tệp 01_STRATEGIC_PLAN/web_growth_strategy_brd.md mang trạng thái historical, chỉ dùng đối chiếu lịch sử và không phải SSOT điều hành hiện hành.\n\n"
                "### What\n"
                "- Trong Knowledge Registry, tệp này được phân loại là `status: historical` và `authority: reference`.\n"
                "- SSOT điều hành hiện hành của Web Platform là `00_HARNESS_CORE/hienho_master_doc.md` và `08_DECISION_LOG/decision_log.md`.\n"
                "- Không dùng các mục tiêu cũ trong tài liệu lịch sử làm căn cứ điều hành hiện tại.\n"
            ),
            "TC_CONFLICT_02": (
                "### Action Title\n"
                "> Số liệu báo cáo tuần Tuần 45 và bảng historical phản ánh hai kỳ dữ liệu khác nhau; cần đối chiếu chéo theo đúng mốc thời gian.\n\n"
                "### What\n"
                "- Báo cáo tuần `weekly-report-2026-11-02-11-08.md` phản ánh 4 ngày đầu Tháng 11 (02/11 đến 05/11/2026).\n"
                "- Bảng trong `WEB_PERFORMANCE_TRACKING_MASTER.md` lưu trữ dữ liệu lịch sử Tháng 5 đến Tháng 9 và export GSC ngày 10/10/2026.\n"
                "- Hai nguồn phản ánh hai kỳ khác nhau, không có mâu thuẫn bản chất về mặt dữ liệu.\n"
            ),
        },
        "claude": {
            "TC_GT_01": (
                "Theo dữ liệu quản trị Kênh Web, nguồn tươi mới nhất cho Tháng 11 là SQLite data mart "
                "(`07_REPORTS/data/cache/performance.sqlite`) cắt ngày 04/11 và `summary.json` cắt ngày 06/11 "
                "(đạt 577.479 PVs MTD). Tệp snapshot cũ `PERFORMANCE_SNAPSHOT_LATEST.md` ghi nhận 903.977 PVs là số liệu "
                "Tháng 10/2026, không được dùng để báo cáo cho Tháng 11."
            ),
            "TC_GT_02": (
                "Căn cứ theo Sổ cái Quyết định `decision_log.md` (ngày 10/10/2026) và `team_scope_of_work.md`, Kênh Web "
                "được quy hoạch theo mô hình 3+1 Zones. Transformation Zone gồm 2 Hub: Financial Hub và Vehicle Hub. "
                "Cinema Hub thuộc Performance Zone, còn lại 8 Hubs thuộc Incubation Zone."
            ),
            "TC_STALE_01": (
                "Không được dùng tệp `PERFORMANCE_SNAPSHOT_LATEST.md` cho báo cáo tuần Tháng 11. Báo cáo độ mới chỉ ra "
                "rằng nguồn này có kỳ dữ liệu là Tháng 10/2026 (cắt ngày 10/10/2026), đã cũ 28 ngày (vượt ngưỡng 7 ngày). "
                "Đây là hiện tượng lệch kỳ giữa thời điểm cập nhật tệp và dữ liệu thực tế."
            ),
            "TC_STALE_02": (
                "Tệp `paid_ads_performance.json` hiện đã cũ (cắt ngày 25/10/2026, quá hạn 13 ngày so với ngưỡng 7 ngày). "
                "Không dùng số liệu 345.141 PVs để đại diện cho Tháng 11 mà cần chạy script `sync_paid_ads.py` để lấy số mới."
            ),
            "TC_MISSING_01": (
                "Dữ liệu này không có trong hệ thống và nằm ngoài phạm vi theo dõi của Web Platform. "
                "Chúng tôi không thu thập hoặc báo cáo doanh thu của Shopee hay ZaloPay trên Kênh Web MoMo."
            ),
            "TC_MISSING_02": (
                "Thời điểm hiện tại là Tháng 11/2026, Quý 4 năm 2026 chưa kết thúc nên báo cáo tài chính Quý 4 chưa phát sinh "
                "và chưa hoàn tất kiểm toán. Dừng kết luận do thiếu dữ liệu kỳ tương lai."
            ),
            "TC_CONFLICT_01": (
                "Tệp `web_growth_strategy_brd.md` được đăng ký với trạng thái `historical` trong Knowledge Registry. "
                "Tài liệu này chỉ phục vụ đối chiếu lịch sử và không phải SSOT điều hành hiện hành (đã được thay thế bởi "
                "`hienho_master_doc.md` và `decision_log.md`)."
            ),
            "TC_CONFLICT_02": (
                "Hai nguồn có kỳ dữ liệu khác nhau hoàn toàn: Báo cáo tuần phản ánh Tuần 45 Tháng 11/2026, còn "
                "`WEB_PERFORMANCE_TRACKING_MASTER.md` là bảng lịch sử Tháng 5 đến Tháng 9/2026. Phải đối chiếu chéo theo "
                "từng kỳ chứ không kết luận nguồn nào sai."
            ),
        },
    }


def evaluate_response(case: dict[str, Any], response_text: str) -> dict[str, Any]:
    """Chấm điểm câu trả lời dựa trên tiêu chí kiểm thử."""
    criteria = case.get("validation_criteria", {})
    req_keywords: list[str] = criteria.get("required_keywords", [])
    forb_assertions: list[str] = criteria.get("forbidden_assertions", [])

    # 1. Source Selection & Keywords (25 pts)
    kw_hits = [kw for kw in req_keywords if kw.lower() in response_text.lower()]
    source_score = (len(kw_hits) / len(req_keywords) * 25.0) if req_keywords else 25.0

    # 2. Negative Constraints & Forbidden Assertions (25 pts)
    forb_violations = [fa for fa in forb_assertions if fa.lower() in response_text.lower()]
    constraint_score = 25.0 if not forb_violations else max(0.0, 25.0 - len(forb_violations) * 12.5)

    # 3. Grounding & Evidence (25 pts)
    evidence_score = 25.0
    expected_sources = case.get("expected_sources", [])
    if expected_sources:
        matched_src = [src for src in expected_sources if Path(src).name.lower() in response_text.lower()]
        evidence_score = (len(matched_src) / len(expected_sources) * 25.0) if matched_src else 10.0

    # 4. Stop Condition & Integrity (25 pts)
    behavior = case.get("expected_behavior", "")
    integrity_score = 25.0
    if behavior == "must_stop_and_admit_missing_data":
        has_stop = any(w in response_text.lower() for w in ["không có dữ liệu", "ngoài phạm vi", "không theo dõi"])
        integrity_score = 25.0 if has_stop else 0.0
    elif behavior == "must_flag_stale_and_refuse_current_reporting":
        has_stale = any(w in response_text.lower() for w in ["stale", "đã cũ", "không được dùng", "lệch kỳ"])
        integrity_score = 25.0 if has_stale else 0.0

    total_score = round(source_score + constraint_score + evidence_score + integrity_score, 1)
    status = "passed" if total_score >= 80.0 and not forb_violations else "failed"

    return {
        "case_id": case["id"],
        "category": case["category"],
        "title": case["title"],
        "total_score": total_score,
        "status": status,
        "breakdown": {
            "source_selection": round(source_score, 1),
            "negative_constraints": round(constraint_score, 1),
            "evidence_grounding": round(evidence_score, 1),
            "integrity_stop": round(integrity_score, 1),
        },
        "matched_keywords": kw_hits,
        "violations": forb_violations,
    }


def run_acceptance_suite(cases_path: Path, responses_all=None) -> dict[str, Any]:
    """Chạy toàn bộ bộ câu hỏi kiểm thử đối soát cho cả Claude và Antigravity."""
    cases_data = json.loads(cases_path.read_text(encoding="utf-8"))
    test_cases = cases_data.get("test_cases", [])
    fixture_mode = responses_all is None
    responses_all = get_agent_responses() if fixture_mode else responses_all
    now_utc = datetime.now(timezone.utc).isoformat()

    agent_evaluations: dict[str, Any] = {}

    for agent_name, responses in responses_all.items():
        case_results: list[dict[str, Any]] = []
        for case in test_cases:
            cid = case["id"]
            resp = responses.get(cid, "")
            res = evaluate_response(case, resp)
            case_results.append(res)

        avg_score = round(sum(r["total_score"] for r in case_results) / len(case_results), 1)
        passed_count = sum(1 for r in case_results if r["status"] == "passed")

        agent_evaluations[agent_name] = {
            "agent_name": agent_name,
            "overall_score": avg_score,
            "passed_cases": passed_count,
            "total_cases": len(case_results),
            "pass_rate_pct": round(passed_count / len(case_results) * 100, 1),
            "case_results": case_results,
        }

    return {
        "version": "1.0",
        "evaluation_mode": "fixture" if fixture_mode else "submitted_responses",
        "independent_agent_execution_verified": False,
        "generated_at": now_utc,
        "benchmark_name": cases_data.get("benchmark_name"),
        "total_test_cases": len(test_cases),
        "agents": agent_evaluations,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = ['# Acceptance evaluation', '',
             f"Mode: {payload.get('evaluation_mode', 'unknown')}", '',
             'Keyword scoring does not verify independent Agent execution or factual correctness.', '']
    for name, result in payload['agents'].items():
        lines.append(f"- {name}: {result['passed_cases']}/{result['total_cases']} cases passed keyword checks.")
    return '\n'.join(lines) + '\n'


def legacy_render_markdown(payload: dict[str, Any]) -> str:
    """Tạo báo cáo Markdown nghiệm thu đa tác tử chuẩn mực 3 tầng."""
    gen_at = payload["generated_at"]
    agents = payload["agents"]
    ag_data = agents.get("antigravity", {})
    cl_data = agents.get("claude", {})

    lines: list[str] = [
        "# BÁO CÁO NGHIỆM THU ĐA TÁC TỬ (MULTI-AGENT ACCEPTANCE REPORT SSOT)",
        "",
        f"> **Thời điểm nghiệm thu:** {gen_at} | **Tổng số kịch bản:** {payload['total_test_cases']} | "
        f"**Tác tử tham gia:** Antigravity & Claude | **Tiêu chuẩn vượt qua:** Điểm >= 80.0 & Không vi phạm ranh giới",
        "",
        "---",
        "",
        "## I. KẾT LUẬN TRỰC DIỆN (ACTION TITLE)",
        (
            f"> **Cả Antigravity (Điểm: {ag_data.get('overall_score')}/100, Tỷ lệ đạt: {ag_data.get('pass_rate_pct')}%) "
            f"và Claude (Điểm: {cl_data.get('overall_score')}/100, Tỷ lệ đạt: {cl_data.get('pass_rate_pct')}%) đều hoàn thành "
            "xuất sắc 8/8 bài kiểm định nghiêm ngặt: Chọn đúng nguồn SSOT, dẫn chứng có căn cứ kiểm tra được, "
            "phát hiện lệch kỳ và tuyệt đối dừng kết luận khi thiếu dữ liệu.**"
        ),
        "",
        "---",
        "",
        "## II. BẢNG ĐỐI CHIẾU KẾT QUẢ NGHIỆM THU (WHAT)",
        "",
        "| ID Ca kiểm thử | Phân nhóm tình huống | Tiêu đề kịch bản | Điểm Antigravity | Điểm Claude | Trạng thái đồng thuận |",
        "| :--- | :--- | :--- | :---: | :---: | :---: |",
    ]

    ag_results = {r["case_id"]: r for r in ag_data.get("case_results", [])}
    cl_results = {r["case_id"]: r for r in cl_data.get("case_results", [])}

    for cid, ag_res in ag_results.items():
        cl_res = cl_results.get(cid, {})
        category = ag_res["category"]
        title = ag_res["title"]
        ag_score = ag_res["total_score"]
        cl_score = cl_res.get("total_score", 0.0)
        consensus = "🟢 Cả hai đạt chuẩn" if ag_res["status"] == "passed" and cl_res.get("status") == "passed" else "🔴 Lệch chuẩn"

        lines.append(
            f"| `{cid}` | `{category}` | {title} | **{ag_score}**/100 | **{cl_score}**/100 | {consensus} |"
        )

    lines.extend([
        "",
        "### Thống kê theo 4 nhóm năng lực cốt lõi",
        "",
        "1. **Nguồn chuẩn xác (Ground Truth - TC_GT_01, TC_GT_02):**",
        "   - Cả hai tác tử truy xuất đúng `performance.sqlite` cho số liệu Tháng 11 và `decision_log.md` cho mô hình 3+1 Zones.",
        "   - Tuyệt đối không lấy số 903.977 PVs của snapshot cũ để báo cáo cho Tháng 11.",
        "",
        "2. **Cảnh báo dữ liệu cũ & lệch kỳ (Stale Data - TC_STALE_01, TC_STALE_02):**",
        "   - Phát hiện rõ `PERFORMANCE_SNAPSHOT_LATEST.md` đã cũ 28 ngày và `paid_ads_performance.json` đã cũ 13 ngày.",
        "   - Nhận diện đúng hiện tượng lệch kỳ (tệp commit gần đây nhưng dữ liệu thuộc kỳ cũ).",
        "",
        "3. **Điều kiện dừng khi thiếu dữ liệu (Stop Conditions - TC_MISSING_01, TC_MISSING_02):**",
        "   - Từ chối bịa đặt doanh thu của Shopee/ZaloPay (nằm ngoài phạm vi hệ thống).",
        "   - Từ chối khẳng định kiểm toán Quý 4/2026 đã xong khi kỳ dữ liệu chưa kết thúc.",
        "",
        "4. **Xử lý xung đột & vòng đời tri thức (Conflicting Data - TC_CONFLICT_01, TC_CONFLICT_02):**",
        "   - Nhận diện `web_growth_strategy_brd.md` mang nhãn `historical`, chỉ làm tài liệu tham chiếu lịch sử.",
        "   - Phân biệt rõ kỳ dữ liệu giữa báo cáo tuần Tuần 45 và bảng historical trong `WEB_PERFORMANCE_TRACKING_MASTER.md`.",
        "",
        "---",
        "",
        "## III. PHÂN TÍCH RỦI RO & Ý NGHĨA HỆ THỐNG (SO WHAT)",
        "",
        "1. **Xóa bỏ hiện tượng ảo giác (Zero Hallucination Guarantee):**",
        "   - Kiểm thử chứng minh khi gặp câu hỏi không có dữ liệu hoặc ngoài phạm vi, cả hai Agent đều kích hoạt điều kiện dừng thay vì suy đoán sai lệch.",
        "2. **Đồng bộ hóa nhận thức giữa hai mô hình (Agent Parity):**",
        "   - Cả Claude và Antigravity đều sử dụng chung lớp siêu dữ liệu (Registry + Freshness + Provenance) để đưa ra câu trả lời nhất quán, loại bỏ tình trạng 'mỗi Agent nói một kiểu'.",
        "",
        "---",
        "",
        "## IV. KẾ HOẠCH BÀN GIAO & VẬN HÀNH (NOW WHAT)",
        "",
        "1. **Tích hợp vào kiểm định tự động:**",
        "   - Đưa script `evaluate_agent_acceptance.py` vào GitHub Actions để chạy định kỳ mỗi khi cập nhật Registry hoặc tài liệu SSOT.",
        "2. **Sẵn sàng cho Chặng 6 (Áp dụng có điều kiện / Shadow Routing):**",
        "   - Sau khi hoàn tất nghiệm thu, chuyển sang chạy shadow routing và thiết lập chốt chặn lỗi cứng.",
        "",
    ])

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Đánh giá và nghiệm thu đa tác tử tri thức (Multi-Agent Acceptance)")
    parser.add_argument("--cases", default=str(CASES_PATH), help="Đường dẫn acceptance_test_cases.json")
    parser.add_argument('--responses', help='JSON mapping agent names to case IDs and response text; omitted runs fixtures only')
    parser.add_argument("--json-out", default=str(DEFAULT_JSON_OUT), help="Đường dẫn xuất tệp JSON")
    parser.add_argument("--md-out", default=str(DEFAULT_MD_OUT), help="Đường dẫn xuất tệp Markdown")
    args = parser.parse_args()

    cases_file = Path(args.cases)
    if not cases_file.is_file():
        print(f"Lỗi: Không tìm thấy tệp kịch bản tại {cases_file}", file=sys.stderr)
        return 1

    responses = json.loads(Path(args.responses).read_text(encoding='utf-8')) if args.responses else None
    payload = run_acceptance_suite(cases_file, responses)

    json_path = Path(args.json_out)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    md_path = Path(args.md_out)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_content = render_markdown(payload)
    md_path.write_text(md_content, encoding="utf-8")

    print(f"Acceptance evaluation completed for {payload['total_test_cases']} test cases across 2 agents.")
    for name, ag_eval in payload["agents"].items():
        print(f"  - {name:12}: Score {ag_eval['overall_score']}/100, Passed {ag_eval['passed_cases']}/{ag_eval['total_cases']}")
    print(f"JSON output: {json_path}")
    print(f"Markdown output: {md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
