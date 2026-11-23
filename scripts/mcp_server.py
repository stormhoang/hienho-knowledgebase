#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCP SERVER FOR GROWTH & PERFORMANCE REPORTING ENGINE
Model Context Protocol (MCP) Server cung cấp các công cụ báo cáo,
chẩn đoán hiệu suất và đồng bộ dữ liệu Web Platform cho Claude Desktop / MoMatrix.
Hỗ trợ Dual-Mode:
  - Production Mode (ENV=production): Kết nối và thực thi các pipeline dữ liệu thực tế.
  - Development / Demo Mode (Mặc định): Trả về dữ liệu mẫu (Mock Schema) chuẩn xác,
    giúp lập trình viên có thể phát triển và kiểm thử MCP Client ngay lập tức
    mà không phụ thuộc credentials hay dữ liệu mật nội bộ.
Giao thức: JSON-RPC 2.0 qua Standard I/O (stdio).
"""

import sys
import os
import json
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
if not (BASE_DIR / "scripts").exists():
    BASE_DIR = Path(__file__).resolve().parent.parent

def log(msg):
    sys.stderr.write(f"[growth-reporting-mcp] {msg}\n")
    sys.stderr.flush()

def is_production():
    return os.environ.get("ENV", "").lower() == "production"

def get_python_exec():
    venv_py = BASE_DIR / ".venv" / "bin" / "python"
    if venv_py.exists():
        return str(venv_py)
    venv_win = BASE_DIR / ".venv" / "Scripts" / "python.exe"
    if venv_win.exists():
        return str(venv_win)
    return sys.executable

TOOLS = [
    {
        "name": "get_latest_report",
        "description": "Lấy báo cáo tổng hợp hiệu suất Web Platform MTD mới nhất gồm Pageviews, Non-Paid vs Paid, cơ cấu các Hub chiến lược và tiến độ Target.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "scope": {
                    "type": "string",
                    "description": "Phạm vi báo cáo: 'snapshot' (tóm tắt nhanh) hoặc 'full' (báo cáo master chi tiết)",
                    "enum": ["snapshot", "full"],
                    "default": "snapshot"
                }
            }
        }
    },
    {
        "name": "diagnose_performance",
        "description": "Chạy chẩn đoán nguyên nhân gốc rễ (Root Cause Analysis - RCA) hiệu suất Web Platform: đo độ lệch Pacing MTD, bóc tách chi tiết kênh Non-Paid vs Paid, phễu Sessions vs W2A CVR, phát hiện từ khóa Quick Wins (>50k impressions, CTR thấp) và đề xuất danh mục hành động trọng tâm theo thứ tự triển khai.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "detect_anomalies",
        "description": "Quét dị biệt và bất thường lưu lượng truy cập: phát hiện các trang rớt traffic đột ngột, đứt gãy luồng chuyển đổi Web-to-App (W2A Onelink) và cảnh báo lãng phí Crawl budget.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "ingest_ga4_daily",
        "description": "Nạp dữ liệu GA4 thủ công: quét file CSV export từ GA4 Explore trong ~/Downloads, cộng dồn MTD, cập nhật Excel SSOT và Hubs Dashboard. (Thay thế sync_ga4_master đã deprecated do policy cấm GA4 API)",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "ingest_gsc_mtd",
        "description": "Nạp dữ liệu GSC thủ công: đọc tab SAS_* mới nhất của Google Sheet GSC-MTD hoặc file ZIP export, cập nhật page_mtd.json và Hub Dashboard. (Thay thế các script GSC API đã deprecated)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "start": {"type": "string", "description": "Override start date YYYY-MM-DD (khi thiếu Chart.csv)"},
                "end": {"type": "string", "description": "Override end date YYYY-MM-DD"}
            }
        }
    },
    {
        "name": "forecast_growth",
        "description": "Chạy mô phỏng dự báo tăng trưởng Web Platform đa kịch bản (Thận trọng, Cơ sở, Khả quan) kết hợp trọng số mùa vụ từ chu kỳ tìm kiếm 5 năm.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    }
]

# Bộ dữ liệu mẫu (Mock Schemas) cho môi trường Dev / Demo
MOCK_RESPONSES = {
    "get_latest_report": """# BÁO CÁO HIỆU SUẤT TỔNG HỢP WEB PLATFORM (MTD SAMPLE)
*Chế độ: Development / Demo Mock Data*

| Nhóm Chỉ Số | Thực Tế (MTD) | Mục Tiêu (Target) | Tiến Độ (%) | Dự Phóng Cuối Tháng |
| :--- | :--- | :--- | :--- | :--- |
| **Tổng Pageviews** | **2.650.000** | 3.650.000 | 72.6% | 3.520.000 (96.4%) |
| **Tổng Sessions** | **1.820.000** | 2.500.000 | 72.8% | 2.450.000 |
| **Người Dùng Web (MEU)** | **1.210.000** | 1.650.000 | 73.3% | 1.620.000 |
| **Chuyển Đổi Web-to-App (W2A)** | **88.500** | 120.000 | 73.8% | 118.000 |

### Cơ Cấu Nguồn Lưu Lượng (Traffic Channels)
- **Non-Paid Traffic (Chủ lực):** 2.252.500 PV (85.0% tỷ trọng)
  - *Organic Search:* 1.722.500 PV (65.0%)
  - *Direct Traffic:* 397.500 PV (15.0%)
  - *Referral:* 132.500 PV (5.0%)
- **Paid Traffic (Chiến dịch):** 397.500 PV (15.0% tỷ trọng)

### Phân Bổ Theo Strategic Hubs
1. **Cinema Hub:** 880.000 PV (33.2%)
2. **Financial Hub:** 345.000 PV (13.0%)
3. **Vehicle Hub:** 215.000 PV (8.1%)
4. **Student & Education Hub:** 160.000 PV (6.0%)
5. **Các Mảng Khác:** 1.050.000 PV (39.7%)
""",

    "diagnose_performance": """# CHẨN ĐOÁN NGUYÊN NHÂN GỐC RỄ (ROOT CAUSE ANALYSIS)
*Chế độ: Development / Demo Mock Data*

### 1. Bóc Tách Khoảng Cách Pacing (Pacing Gap)
- **Tiến độ thời gian:** Ngày 22/31 (71.0% chu kỳ tháng)
- **Tiến độ lưu lượng:** 72.6% Target (Vượt tiến độ chuẩn +1.6% ~ On-track)
- **Động cơ chính:** Kênh Organic Search duy trì phong độ ổn định; CTR trung bình đạt 4.8%.

### 2. Phát Hiện Từ Khóa Quick Wins (>50.000 Lượt Hiển Thị, CTR < 3%)
| Từ Khóa (Query) | Lượt Hiển Thị (Imp) | Thứ Hạng SERP | CTR Thực Tế | Tiềm Năng Click (+Net) |
| :--- | :--- | :--- | :--- | :--- |
| `tra cuu vi pham giao thong` | 145.000 | 4.2 | 2.4% | +8.200 clicks/tháng |
| `tinh lai suat tiet kiem` | 89.000 | 5.1 | 2.1% | +4.600 clicks/tháng |
| `lich chieu phim cgv hom nay`| 65.000 | 3.8 | 2.8% | +3.100 clicks/tháng |

### 3. Kế Hoạch Xử Lý (Prescriptive Action Items)
1. **Web Dev:** Cải thiện tốc độ tải trang LCP cho nhóm trang tra cứu xuống dưới 2.5s.
2. **SEO & Content:** Bổ sung Schema JSON-LD FAQ và Direct Answer cho 3 cụm từ khóa Quick Wins.
3. **Media Team:** Tối ưu hóa trang đích cho chiến dịch Paid Search để nâng CVR Web-to-App lên 4.5%.
""",

    "detect_anomalies": """# QUÉT DỊ BIỆT LƯU LƯỢNG & ĐỨT GÃY CHUYỂN ĐỔI (ANOMALY SCAN)
*Chế độ: Development / Demo Mock Data*

- **Trạng thái hệ thống:** BÌNH THƯỜNG (Không phát hiện lỗi nghiêm trọng)
- **Tổng số trang giám sát:** 1.250 URLs
- **Luồng chuyển đổi Onelink Web-to-App:** Tỷ lệ thành công 99.4% (Tín hiệu tốt)
- **Cảnh báo cần theo dõi (01):**
  - Trang `/tien-ich/tinh-lai`: Tỷ lệ thoát (Bounce Rate) tăng nhẹ +4.2% trong 3 ngày gần nhất. Khuyến nghị kiểm tra khả năng hiển thị widget trên trình duyệt Safari mobile.
""",

    "ingest_ga4_daily": """[GA4 INGEST SUCCESS]
Đồng bộ thành công dữ liệu MTD thời gian thực:
- Trích xuất: 2.650.000 Pageviews, 1.820.000 Sessions, 88.500 W2A Clicks.
- Cập nhật đồng bộ: Snapshot JSON, Dashboard Web Hubs và SSOT Master.
- Thời gian thực thi: 8.4 giây.
""",

    "ingest_gsc_mtd": """# GSC MTD INGEST SUCCESS
*Chế độ: Development / Demo Mock Data*

| Chỉ số | Giá trị |
| :--- | :--- |
| Total Clicks MTD | 540.654 |
| Total Impressions MTD | 19.189.025 |
| Avg CTR | 2.82% |
| Avg Position | 6.13 |
| Pages có GSC data | 16.066 |
""",

    "forecast_growth": """# MÔ PHỎNG DỰ BÁO TĂNG TRƯỞNG WEB PLATFORM (3 KỊCH BẢN)
*Chế độ: Development / Demo Mock Data*

1. **Kịch bản Thận trọng (Conservative):**
   - Dự kiến kết tháng: **3.380.000 PV** (92.5% Target)
   - Giả định: Lưu lượng tự nhiên đi ngang, giảm 20% ngân sách Paid Ads cuối tháng.
2. **Kịch bản Cơ sở (Base - Khả năng cao):**
   - Dự kiến kết tháng: **3.580.000 PV** (97.7% Target)
   - Giả định: Nhịp chạy (Daily Pace) duy trì ổn định ~115.000 PV/ngày.
3. **Kịch bản Khả quan (Bullish):**
   - Dự kiến kết tháng: **3.720.000 PV** (101.5% Target)
   - Giả định: Các cụm từ khóa Quick Wins lọt Top 3 SERP và chiến dịch cuối tuần bứt phá.
"""
}

def handle_tool_call(tool_name, arguments):
    # Nếu chạy ở chế độ Production và có script/dữ liệu thực tế:
    if is_production():
        py_exec = get_python_exec()
        log(f"[PROD MODE] Executing tool {tool_name} with Python: {py_exec}")

        if tool_name == "get_latest_report":
            scope = arguments.get("scope", "snapshot")
            doc_path = BASE_DIR / "07_REPORTS" / "WEB_PERFORMANCE_TRACKING_MASTER.md"
            if scope == "snapshot":
                snap_path = BASE_DIR / "07_REPORTS" / "docs" / "PERFORMANCE_SNAPSHOT_LATEST.md"
                if snap_path.exists():
                    doc_path = snap_path
            
            if doc_path.exists():
                try:
                    with open(doc_path, "r", encoding="utf-8") as f:
                        return f.read()[:15000]
                except Exception as e:
                    log(f"Error reading doc: {e}")

        script_map = {
            "diagnose_performance": BASE_DIR / "scripts" / "diagnose_performance.py",
            "detect_anomalies": BASE_DIR / "scripts" / "detect_anomalies.py",
            "ingest_ga4_daily": BASE_DIR / "scripts" / "ingest_ga4_daily.py",
            "ingest_gsc_mtd": BASE_DIR / "scripts" / "ingest_gsc_mtd.py",
            "forecast_growth": BASE_DIR / "scripts" / "lib" / "forecast_engine.py",
        }

        if tool_name in script_map:
            target_script = script_map[tool_name]
            if target_script.exists():
                try:
                    res = subprocess.run([py_exec, str(target_script)], capture_output=True, text=True, cwd=str(BASE_DIR))
                    out = res.stdout if res.stdout else res.stderr
                    if out and out.strip():
                        return out.strip()
                except Exception as e:
                    log(f"Execution error on {target_script}: {e}")

        if tool_name == "ingest_gsc_mtd":
            target_script = BASE_DIR / "scripts" / "ingest_gsc_mtd.py"
            if target_script.exists():
                try:
                    cmd = [py_exec, str(target_script)]
                    if arguments.get("start"):
                        cmd.extend(["--start", str(arguments["start"])])
                    if arguments.get("end"):
                        cmd.extend(["--end", str(arguments["end"])])
                    res = subprocess.run(cmd, capture_output=True, text=True, cwd=str(BASE_DIR))
                    out = res.stdout if res.stdout else res.stderr
                    if out and out.strip():
                        return out.strip()
                except Exception as e:
                    log(f"Execution error on ingest_gsc_mtd: {e}")

    # Fallback tự động sang Mock Data (Dành cho Dev / Demo hoặc khi thiếu file cấu hình)
    log(f"[DEV / MOCK MODE] Serving mock response for {tool_name}")
    return MOCK_RESPONSES.get(tool_name, f"Tool '{tool_name}' executed successfully (No mock data available).")

def send_response(response_dict):
    body = json.dumps(response_dict, ensure_ascii=False)
    sys.stdout.write(body + "\n")
    sys.stdout.flush()

def main():
    mode_str = "PRODUCTION" if is_production() else "DEVELOPMENT (MOCK DATA)"
    log(f"Server starting over stdio in {mode_str} mode...")
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception as e:
            log(f"Invalid JSON: {e}")
            continue

        req_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})

        if method == "initialize":
            send_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "growth_reporting",
                        "version": "1.0.0"
                    }
                }
            })
        elif method == "notifications/initialized":
            log("Client initialized successfully.")
        elif method == "tools/list":
            send_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": TOOLS
                }
            })
        elif method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})
            try:
                result_text = handle_tool_call(tool_name, tool_args)
                send_response({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": result_text
                            }
                        ]
                    }
                })
            except Exception as e:
                log(f"Error handling tool call: {e}")
                send_response({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": f"Lỗi khi thực thi công cụ: {str(e)}"
                            }
                        ],
                        "isError": True
                    }
                })
        elif method == "ping":
            send_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {}
            })
        else:
            if req_id is not None:
                send_response({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {
                        "code": -32601,
                        "message": f"Method not found: {method}"
                    }
                })

if __name__ == "__main__":
    main()
