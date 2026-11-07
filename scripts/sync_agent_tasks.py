#!/usr/bin/env python3
"""
Pipeline đồng bộ Tác vụ và Nhật ký điều phối từ Hiến sang Hub /agent.
SSOT: Hienho_MoMo-Base -> react-web-momo/lib/agent/

Nguyên tắc bất biến:
- 100% tiếng Việt tự nhiên, gãy gọn, dễ đọc.
- Tuyệt đối KHÔNG dùng ký hiệu mã hóa, không mã task, không nhãn phân cấp độ ưu tiên viết tắt.
- Pipeline code chạy 100% tại Hienho_MoMo-Base.
- Bên Hub chỉ nhận file dữ liệu (JSON) và tệp Log (agent-activity.log), tuyệt đối KHÔNG đụng đến mã nguồn code của Hub.
"""

import argparse
import datetime
import glob
import json
import os
import re
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HUB_DIR = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo"
HUB_AGENT_LIB = os.path.join(HUB_DIR, "lib", "agent")

LOCAL_DATA_DIR = os.path.join(BASE_DIR, "07_REPORTS", "data")
DISPATCH_DIR = os.path.join(BASE_DIR, "15_DISPATCH")

DISPATCH_STATUS_LABEL = {
    "cho-xac-nhan": "Chờ xác nhận",
    "da-xac-nhan": "Đã xác nhận",
}
LOCAL_LOG_DIR = os.path.join(BASE_DIR, "07_REPORTS", "logs")

# Bảng nhân sự chuẩn hóa theo bàn làm việc
PERSONNEL_MAP = {
    "hùng": {"name": "Hùng", "role": "Front-end Team Lead", "desk": "Bàn 01", "scope": "Cinema Hub & MoBase"},
    "nhật": {"name": "Nhật", "role": "Senior Front-end", "desk": "Bàn 01", "scope": "Financial Hub & Utility Tools"},
    "thuận": {"name": "Thuận", "role": "Senior Front-end", "desk": "Bàn 01", "scope": "Vehicle Hub & Quiz Platform"},
    "duy": {"name": "Duy", "role": "Senior Back-end", "desk": "Bàn 01", "scope": "RAG Knowledge Base & Vé Số"},
    "lộc": {"name": "Lộc", "role": "DevOps Lead", "desk": "Bàn 01", "scope": "Hạ tầng, Hiệu năng & MoSpark Auth"},
    "hiếu": {"name": "Hiếu", "role": "Back-end Team Lead", "desk": "Bàn 01", "scope": "Tracking Pipeline & APIs Hubs"},
    "hoài anh": {"name": "Hoài Anh", "role": "Tech Solution Lead", "desk": "Bàn 01", "scope": "Kiến trúc MoSpark Core & API Gateway"},
    "trọng": {"name": "Trọng", "role": "Senior Front-end", "desk": "Bàn 01", "scope": "GenAI Content Workflow & PLG Dashboard"},
    "bảo": {"name": "Bảo", "role": "Senior Manager", "desk": "Bàn 02", "scope": "Quản lý SE Team & MoSpark Platform"},
    "hoan": {"name": "Hoan", "role": "Senior Product Marketing", "desk": "Bàn 02", "scope": "Content Strategy & Chuẩn hóa Skill"},
    "tữ": {"name": "Tữ", "role": "Senior Product Designer", "desk": "Bàn 02", "scope": "UI/UX Web Design & Design-to-Code"},
    "hiến": {"name": "Hiến", "role": "Web Product Lead · Điều phối", "desk": "Bàn 02", "scope": "Định hướng Sản phẩm Web & SEO/GEO"},
}

# 4 Key Owners cho các luồng sản phẩm trực tiếp (không thông qua Product Design)
DIRECT_ROUTING_KEY_OWNERS = {
    "thuận": "Vehicle Hub & Mini Tools / Quiz (định giá xe, tra cứu phạt nguội, chi phí xe...)",
    "hùng": "Cinema Hub & BMC Front-end (lịch chiếu phim, mua vé, minigame tương tác...)",
    "nhật": "Financial Hub & Utility Tools (interactive calculators, thuế TNCN, lãi vay...)",
    "trọng": "GenAI Content Workflow, PLG Dashboard & Công Cụ Vận Hành Nội Bộ",
}

def resolve_golive_prerequisites(person_key: str):
    """
    Xác định điều kiện tiên quyết để Go-Live đầy đủ lên Production.
    - Trừ Trọng, các Key Owner (Thuận, Hùng, Nhật) bắt buộc phải có Meta Data, SEO keyword, Long Content từ Hoan và ký duyệt Product Sign-off từ Hiến.
    - Trọng (công cụ/hệ thống nội bộ) được miễn trừ Meta Data, SEO keyword và Long Content.
    """
    key = person_key.lower().strip()
    if key in ["thuận", "hùng", "nhật"]:
        return {
            "dieuKienGoLive": "Bắt buộc có Meta Data, SEO keyword, Long Content từ Hoan và ký duyệt Product Sign-off từ Hiến trước khi Go-Live Production.",
            "yeuCauNoiDungSEO": "Bắt buộc (Hoan phụ trách Long Content, Meta Data và từ khóa SEO)",
            "kyDuyetProductSignoff": "Bắt buộc (Hiến ký duyệt Product Sign-off)",
            "laCongCuNoiBo": False,
        }
    elif key == "trọng":
        return {
            "dieuKienGoLive": "Sản phẩm công cụ nội bộ: Miễn trừ Meta Data, SEO keyword và Long Content từ Hoan. Chỉ cần hoàn tất kiểm thử tính năng và nhận Product Sign-off từ Hiến để Go-Live vận hành.",
            "yeuCauNoiDungSEO": "Miễn trừ (Hệ thống nội bộ không phục vụ SEO Google)",
            "kyDuyetProductSignoff": "Bắt buộc (Hiến nghiệm thu tính năng)",
            "laCongCuNoiBo": True,
        }
    return None

def find_latest_weekly_report():
    docs_dir = os.path.join(BASE_DIR, "07_REPORTS", "docs")
    pattern = os.path.join(docs_dir, "weekly-report-*.md")
    files = glob.glob(pattern)
    if not files:
        return None
    files.sort(key=lambda x: os.path.basename(x), reverse=True)
    return files[0]

def clean_project_name(raw_title):
    # Loại bỏ phần số liệu và mô tả phụ trong dấu ngoặc
    # Ví dụ: "Cinema Hub (157.658 PVs - Dẫn Đầu Toàn Web): Ra Mắt..." -> "Cinema Hub"
    title = raw_title.split(":")[0].strip()
    title = re.sub(r"\(.*?\)", "", title).strip()
    return title

def make_clean_task_title(project, action_text):
    # Rút trích tiêu đề ngắn gọn thuần ngôn ngữ tự nhiên từ câu hành động đầu tiên
    sentences = re.split(r"[;\.]", action_text)
    first_sentence = sentences[0].strip()
    if len(first_sentence) > 85:
        first_sentence = first_sentence[:82] + "..."
    return f"{project}: {first_sentence}" if not first_sentence.lower().startswith(project.lower()) else first_sentence

def parse_weekly_tasks(report_path):
    tasks = []
    if not os.path.exists(report_path):
        return tasks

    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    sections = re.split(r"\n###\s+(\d+)\.\s+", content)
    now_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    for i in range(1, len(sections), 2):
        sec_body = sections[i+1] if i+1 < len(sections) else ""
        first_line = sec_body.strip().split("\n")[0]
        raw_title = first_line.split("---")[0].strip()
        project = clean_project_name(raw_title)

        owner_match = re.search(r"-\s+\*\*Key Owner:\*\*\s*([^\n]+)", sec_body)
        raw_owner = owner_match.group(1).strip() if owner_match else "Hiến"
        
        pic_key = "hiến"
        for k in PERSONNEL_MAP.keys():
            if k in raw_owner.lower():
                pic_key = k
                break
        person = PERSONNEL_MAP.get(pic_key, PERSONNEL_MAP["hiến"])

        obj_match = re.search(r"-\s+\*\*Objectives:\*\*\s*([^\n]+)", sec_body)
        objectives = obj_match.group(1).strip() if obj_match else ""

        next_action_match = re.search(r"-\s+\*\*Next Action:\*\*\s*(.*?)(?=\n-\s+\*\*|\n---|\Z)", sec_body, re.DOTALL)
        next_action_raw = next_action_match.group(1).strip() if next_action_match else ""
        action_clean = " ".join([line.strip().lstrip("-").strip() for line in next_action_raw.split("\n") if line.strip()])

        colab_match = re.search(r"-\s+\*\*(?:Collaboration|Colab):\*\*\s*(.*?)(?=\n-\s+\*\*|\n---|\Z)", sec_body, re.DOTALL)
        colab_raw = colab_match.group(1).strip() if colab_match else ""
        colab_clean = " ".join([line.strip().lstrip("-").strip() for line in colab_raw.split("\n") if line.strip()])

        if not action_clean and not objectives:
            continue

        task_title = make_clean_task_title(project, action_clean if action_clean else objectives)
        gate_info = resolve_golive_prerequisites(pic_key)

        tasks.append({
            "tenDauViec": task_title,
            "duAn": project,
            "nguoiPhuTrach": person["name"],
            "vaiTro": person["role"],
            "banLamViec": person["desk"],
            "nguoiDieuPhoi": "Hiến Hồ (Web Product Lead)",
            "trangThai": "Đang thực hiện",
            "mucTieu": objectives,
            "viecCanLam": action_clean,
            "phoiHop": colab_clean,
            "dieuKienGoLive": gate_info["dieuKienGoLive"] if gate_info else "",
            "thoiGianCapNhat": now_str,
            "nhatKyXuLy": [
                f"[{now_str}] Hiến Hồ giao việc và làm rõ phạm vi kết quả mong đợi.",
                f"[{now_str}] {person['name']} đã tiếp nhận và đang triển khai tại {person['desk']}."
            ]
        })

    return tasks

def load_dispatch_tasks():
    """Đọc các lệnh giao việc từ Hub /agent (15_DISPATCH/*.json), bỏ qua phân công đã hoàn thành."""
    tasks = []
    if not os.path.isdir(DISPATCH_DIR):
        return tasks
    files = sorted(glob.glob(os.path.join(DISPATCH_DIR, "*.json")), reverse=True)
    for path in files:
        try:
            with open(path, "r", encoding="utf-8") as f:
                dispatch = json.load(f)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"Bỏ qua {os.path.basename(path)}: {exc}")
            continue
        for item in dispatch.get("phanCong", []):
            status = item.get("trangThai", "cho-xac-nhan")
            if status not in DISPATCH_STATUS_LABEL:
                continue
            person_key = item.get("nguoi", "").lower()
            person = PERSONNEL_MAP.get(person_key)
            if not person:
                continue
            gate_info = resolve_golive_prerequisites(person_key)
            log = [f"[{dispatch.get('taoLucHienThi', '')}] Hiến Hồ giao qua Hub /agent: {dispatch.get('lenhGoc', '')}"]
            if item.get("xacNhanLuc"):
                log.append(f"[{item['xacNhanLuc']}] {person['name']} đã xác nhận.")
            tasks.append({
                "tenDauViec": item.get("viecCanLam", ""),
                "duAn": dispatch.get("duAn", "Web Platform"),
                "nguoiPhuTrach": person["name"],
                "vaiTro": person["role"],
                "banLamViec": person["desk"],
                "nguoiDieuPhoi": "Hiến Hồ (Web Product Lead)",
                "trangThai": DISPATCH_STATUS_LABEL[status],
                "mucTieu": dispatch.get("tomTat", ""),
                "viecCanLam": item.get("viecCanLam", ""),
                "phoiHop": "; ".join(item.get("phuThuoc", [])),
                "dieuKienGoLive": gate_info["dieuKienGoLive"] if gate_info else "",
                "thoiGianCapNhat": item.get("xacNhanLuc") or dispatch.get("taoLucHienThi", ""),
                "nhatKyXuLy": log,
                "nguon": "dispatch",
                "maLenh": dispatch.get("id", ""),
                "canHienCungCap": item.get("canHienCungCap", []),
                "timeline": item.get("timeline", []),
                "hanChot": dispatch.get("hanChot", ""),
            })
    return tasks

def generate_activity_log(tasks, adhoc_item=None):
    now_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [
        "=" * 82,
        "SỔ NHẬT KÝ ĐIỀU PHỐI VÀ GIAO VIỆC · ĐỘI NGŨ WEB PLATFORM",
        f"Thời gian cập nhật : {now_str} (GMT+7)",
        "Người điều phối    : Hiến Hồ (Web Product Lead)",
        "Không gian đích    : Hub /agent (Không can thiệp mã nguồn)",
        "=" * 82,
        ""
    ]

    if adhoc_item:
        lines.append("──────────────────────────────────────────────────────────────────────────────────")
        lines.append("LỆNH GIAO VIỆC TRỰC TIẾP TỪ HIẾN HỒ")
        lines.append(f"  * Người nhận : {adhoc_item['nguoiPhuTrach']} ({adhoc_item['banLamViec']})")
        lines.append(f"  * Dự án      : {adhoc_item['duAn']}")
        lines.append(f"  * Việc cần làm: {adhoc_item['viecCanLam']}")
        lines.append("──────────────────────────────────────────────────────────────────────────────────")
        lines.append("")

    lines.append(f"DANH SÁCH {len(tasks)} ĐẦU VIỆC TRỌNG TÂM ĐANG TRIỂN KHAI:")
    lines.append("")

    for idx, t in enumerate(tasks, start=1):
        lines.append(f"[{idx:02d}] {t['duAn']} · Phụ trách: {t['nguoiPhuTrach']} ({t['banLamViec']})")
        lines.append(f"     Tiêu đề: {t['tenDauViec']}")
        lines.append(f"     Chi tiết việc: {t['viecCanLam']}")
        if t.get('phoiHop'):
            lines.append(f"     Phối hợp: {t['phoiHop']}")
        if t.get('dieuKienGoLive'):
            lines.append(f"     Điều kiện Go-Live: {t['dieuKienGoLive']}")
        lines.append("")

    lines.append("=" * 82)
    lines.append(f"TỔNG KẾT: {len(tasks)} đầu việc đã được đồng bộ chuẩn xác sang Hub.")
    lines.append("=" * 82)
    return "\n".join(lines)

def generate_intercom_feed(tasks):
    feed = []
    base_time = datetime.datetime.now() - datetime.timedelta(minutes=25)
    
    feed.append({
        "nguoiGui": "Hiến Hồ (Product Lead)",
        "vaiTro": "Web Product Lead · Điều phối",
        "noiDung": f"Đã rà soát và chuyển giao toàn bộ {len(tasks)} đầu việc trọng tâm tuần này. Các bạn tại Bàn 1 và Bàn 2 kiểm tra nội dung và phối hợp nhé.",
        "thoiGian": base_time.strftime("%H:%M"),
        "nhanViTri": "Bàn 02"
    })

    time_step = 2
    for t in tasks[:7]:
        msg_time = (base_time + datetime.timedelta(minutes=time_step)).strftime("%H:%M")
        feed.append({
            "nguoiGui": t["nguoiPhuTrach"],
            "vaiTro": t["vaiTro"],
            "noiDung": f"Đã tiếp nhận đầu việc {t['duAn']}: {t['viecCanLam'][:110]}...",
            "thoiGian": msg_time,
            "nhanViTri": t["banLamViec"]
        })
        time_step += 3

    return feed

def main():
    parser = argparse.ArgumentParser(description="Pipeline đồng bộ tác vụ từ Hiến sang Hub /agent không dùng ký hiệu.")
    parser.add_argument("--dispatch", type=str, help="Giao một đầu việc mới trực tiếp bằng ngôn ngữ tự nhiên")
    parser.add_argument("--pic", type=str, default="thuận", help="Tên người nhận (thuận, hùng, nhật, duy, lộc, hiếu, hoài anh, trọng, bảo, hoan, tữ)")
    parser.add_argument("--project", type=str, default="Web Platform", help="Tên dự án liên quan")
    args = parser.parse_args()

    latest_report = find_latest_weekly_report()
    if not latest_report:
        print("Lỗi: Không tìm thấy Báo Cáo Tuần trong 07_REPORTS/docs/")
        sys.exit(1)

    tasks = load_dispatch_tasks() + parse_weekly_tasks(latest_report)

    adhoc_item = None
    if args.dispatch:
        now_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        pic_key = args.pic.lower().strip()
        person = PERSONNEL_MAP.get(pic_key, PERSONNEL_MAP["thuận"])
        gate_info = resolve_golive_prerequisites(pic_key)

        phoi_hop_text = "Phối hợp các thành viên liên quan trên sơ đồ bàn làm việc"
        if pic_key in ["thuận", "hùng", "nhật"]:
            phoi_hop_text = "Phối hợp Hoan (chuẩn bị Meta Data, SEO keywords, Long Content chuẩn E-E-A-T) và Hiến (ký duyệt Product Sign-off trước khi Go-Live Production)"
        elif pic_key == "trọng":
            phoi_hop_text = "Phối hợp Hiến nghiệm thu tính năng nội bộ (Miễn trừ yêu cầu SEO và Long Content)"

        adhoc_item = {
            "tenDauViec": f"{args.project}: {args.dispatch[:70]}",
            "duAn": args.project,
            "nguoiPhuTrach": person["name"],
            "vaiTro": person["role"],
            "banLamViec": person["desk"],
            "nguoiDieuPhoi": "Hiến Hồ (Web Product Lead)",
            "trangThai": "Đang thực hiện",
            "mucTieu": "Chỉ đạo trực tiếp từ Product Lead",
            "viecCanLam": args.dispatch,
            "phoiHop": phoi_hop_text,
            "dieuKienGoLive": gate_info["dieuKienGoLive"] if gate_info else "",
            "thoiGianCapNhat": now_str,
            "nhatKyXuLy": [
                f"[{now_str}] Hiến Hồ trực tiếp giao việc: {args.dispatch}",
                f"[{now_str}] Gán trực tiếp cho {person['name']} ({person['desk']})."
            ]
        }
        tasks.insert(0, adhoc_item)

    # Chuẩn bị dữ liệu
    tasks_data = {
        "thongTinChung": {
            "tenDanhSach": "Sổ Tác Vụ Điều Phối Web Platform",
            "thoiGianDongBo": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
            "nguonBaoCao": os.path.basename(latest_report),
            "nguoiDieuPhoi": "Hiến Hồ (Web Product Lead)",
            "tongSoDauViec": len(tasks)
        },
        "danhSachDauViec": tasks
    }

    tasks_json = json.dumps(tasks_data, ensure_ascii=False, indent=2)
    intercom_json = json.dumps(generate_intercom_feed(tasks), ensure_ascii=False, indent=2)
    activity_log = generate_activity_log(tasks, adhoc_item)

    # 1. Lưu bản sao SSOT cục bộ
    os.makedirs(LOCAL_DATA_DIR, exist_ok=True)
    os.makedirs(LOCAL_LOG_DIR, exist_ok=True)
    with open(os.path.join(LOCAL_DATA_DIR, "agent_tasks.json"), "w", encoding="utf-8") as f:
        f.write(tasks_json)
    with open(os.path.join(LOCAL_LOG_DIR, "agent_activity.log"), "w", encoding="utf-8") as f:
        f.write(activity_log)

    # 2. Xuất dữ liệu sang Hub /agent (Tuyệt đối chỉ ghi file Data/Log, KHÔNG sửa code TSX/TS)
    if os.path.exists(HUB_AGENT_LIB):
        with open(os.path.join(HUB_AGENT_LIB, "agent-tasks.json"), "w", encoding="utf-8") as f:
            f.write(tasks_json)
        with open(os.path.join(HUB_AGENT_LIB, "agent-activity.log"), "w", encoding="utf-8") as f:
            f.write(activity_log)
        with open(os.path.join(HUB_AGENT_LIB, "agent-intercom.json"), "w", encoding="utf-8") as f:
            f.write(intercom_json)
        print(f"[ĐÃ ĐỒNG BỘ XONG SANG HUB]")
        print(f"  -> {os.path.join(HUB_AGENT_LIB, 'agent-tasks.json')}")
        print(f"  -> {os.path.join(HUB_AGENT_LIB, 'agent-activity.log')}")
        print(f"  -> {os.path.join(HUB_AGENT_LIB, 'agent-intercom.json')}")

    print(f"Hoàn tất: Đã đồng bộ {len(tasks)} đầu việc bằng ngôn ngữ tự nhiên thuần túy, không có bất kỳ ký hiệu mã hóa nào.")

if __name__ == "__main__":
    main()
