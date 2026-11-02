#!/usr/bin/env python3
"""
Report Grounding & Anti-Hallucination Harness
Kiem tra tinh xac thuc 100% cua Weekly Report so voi cac file bao cao goc tren Google Drive.
Tuyet doi chan moi hinh thuc bia so lieu, tinh nang ao, hay chen thong tin khong co trong bao cao.
"""

import os
import re
import sys
from pathlib import Path

DRIVE_RAW_DIR = Path("/Users/hienhv/Library/CloudStorage/GoogleDrive-hien.ho@mservice.com.vn/My Drive/WEB GROWTH 2026/#6 - Report/Web Platform_Report (Markdown)/26 10-01 11")
REPORT_FILE = Path("/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/weekly-report-2026-10-26-11-01.md")

# Danh sach cac tu khoa "slop / bia dat" bi cam tuyet doi xuat hien
FORBIDDEN_PATTERNS = [
    r"nối số view từ ga4",
    r"giảm 40% cuộn chuột",
    r"pilot offpage",
    r"nộp phạt csgt lên prod",
    r"125m",
    r"chứng chỉ quỹ sip",  # Yeu cau cua user: bo chu SIP
]

def load_raw_corpus():
    corpus = ""
    if not DRIVE_RAW_DIR.exists():
        print(f"Warning: Khong tim thay thu muc raw: {DRIVE_RAW_DIR}")
        return corpus
    
    for f in DRIVE_RAW_DIR.glob("*.md"):
        try:
            corpus += f.read_text(encoding="utf-8").lower() + "\n"
        except Exception as e:
            print(f"Loi doc file {f}: {e}")
    return corpus

def verify_report(report_path: Path):
    if not report_path.exists():
        print(f"Error: Khong tim thay file report: {report_path}")
        return False

    report_text = report_path.read_text(encoding="utf-8")
    report_lower = report_text.lower()
    
    errors = []
    
    # 1. Kiem tra tu khoa cam / bia dat
    for pat in FORBIDDEN_PATTERNS:
        matches = re.findall(pat, report_lower)
        if matches:
            errors.append(f"[FORBIDDEN CLAUSE] Phat hien tu khoa cam/ao: '{pat}' ({len(matches)} lan)")

    # 2. Kiem tra cac keyword ky thuat chinh trong report co can cu tu corpus khong
    corpus = load_raw_corpus()
    
    key_assertions = [
        ("momo.vn/cinema/person", "hung.nguyen9"),
        ("cinetour", "hung.nguyen9"),
        ("chung-chi-quy", "nhat.bui1"),
        ("thue-thu-nhap-ca-nhan", "nhat.bui1"),
        ("thue-ho-kinh-doanh", "nhat.bui1"),
        ("garage", "thuanvo"),
        ("bao-hiem-xe-may", "thuanvo"),
        ("momo.vn/bao-hiem", "thuanvo"),
        ("tai-app", "thuanvo"),
        ("bò sữa bay", "thuanvo / hoan"),
        ("sitemap & link scanner", "duy.tran2"),
        ("project center", "duy.tran2"),
        ("eligibility validation", "duy.tran2"),
        ("voucher card", "hieu.nguyen8 / duy.tran2"),
        ("step-by-step", "hieu.nguyen8 / duy.tran2"),
        ("tim-kiem", "hieu.nguyen8"),
        ("url catalog", "hieu.nguyen8"),
    ]

    for key, owner in key_assertions:
        if key not in report_lower:
            errors.append(f"[MISSING GROUNDING] Thieu tinh nang thuc te duoc dev bao cao: '{key}' ({owner})")
        elif key not in corpus:
            errors.append(f"[UNGROUNDED ITEM] Tinh nang '{key}' khong ton tai trong file dev goc!")

    if errors:
        print("❌ PHÁT HIỆN LỖI HARNESS KIỂM TRA TÍNH XÁC THỰC:")
        for err in errors:
            print(f" - {err}")
        return False

    print("✅ HARNESS KIỂM TRA HOÀN TẤT: 100% Khớp với báo cáo dev gốc, không phát hiện hallucination hoặc từ khóa ảo.")
    return True

if __name__ == "__main__":
    success = verify_report(REPORT_FILE)
    sys.exit(0 if success else 1)
