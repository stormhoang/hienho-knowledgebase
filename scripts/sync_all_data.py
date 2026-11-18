#!/usr/bin/env python3
"""
MASTER SYNCHRONIZATION PIPELINE - WEB PLATFORM (momo.vn)
Tập hợp toàn bộ các luồng sync dữ liệu thành 1 lệnh điều phối duy nhất:
1. Web Performance Tracking (Excel MTD, Target vs Actual, Hubs Sync)
2. Microsoft Clarity Data Export (Traffic, Kênh AiPlatform, AI Sessions, 5 Frustration metrics)
3. Google Trends Validation (Rolling top themes, Geo-intent, Rising queries)
4. Bing AI Performance Ingest (Copilot citations)
5. Inventory & Clusters Sync to Web Hubs (react-web-momo)
6. SEO News (SEO/GEO/AI Search) -> data/seo-news.json (react-web-momo)
"""

import os
import sys
import subprocess
import argparse
import concurrent.futures
import time
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = BASE_DIR / "scripts"
sys.path.insert(0, str(BASE_DIR))
from scripts.lib.hub_sync_lock import hub_sync_lock

def run_step(step_name, command_args, continue_on_error=True):
    """Thực thi 1 bước đồng bộ với logging rõ ràng."""
    print(f"\n{'='*70}")
    print(f"▶ [SYNC STEP] {step_name.upper()}")
    print(f"{'='*70}")
    start_time = time.time()
    
    cmd = [sys.executable] + command_args
    try:
        res = subprocess.run(cmd, cwd=str(BASE_DIR), capture_output=False, text=True)
        elapsed = time.time() - start_time
        if res.returncode == 0:
            print(f"✓ [{step_name}] Hoàn thành thành công ({elapsed:.1f}s)")
            return True, elapsed
        else:
            print(f"✗ [{step_name}] Thất bại với exit code {res.returncode} ({elapsed:.1f}s)")
            if not continue_on_error:
                sys.exit(res.returncode)
            return False, elapsed
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"✗ [{step_name}] Lỗi ngoại lệ: {e} ({elapsed:.1f}s)")
        if not continue_on_error:
            sys.exit(1)
        return False, elapsed

def run_step_capture(step_name, command_args):
    """Chạy step song song: capture output thay vì stream trực tiếp.
    Trả về (success, elapsed, combined_output) để caller tự in sau khi xong."""
    start_time = time.time()
    cmd = [sys.executable] + command_args
    try:
        res = subprocess.run(cmd, cwd=str(BASE_DIR), capture_output=True, text=True)
        elapsed = time.time() - start_time
        output = (res.stdout or "") + (res.stderr or "")
        return res.returncode == 0, elapsed, output
    except Exception as e:
        return False, time.time() - start_time, str(e)

def main():
    parser = argparse.ArgumentParser(description="Master Data & API Sync Runner for MoMo Web Platform")
    parser.add_argument("--skip-clarity", action="store_true", help="Bỏ qua kéo dữ liệu Microsoft Clarity")
    parser.add_argument("--reprocess-clarity", action="store_true", help="Chỉ reprocess Clarity từ raw data có sẵn (tiết kiệm quota)")
    parser.add_argument("--skip-tracking", action="store_true", help="Bỏ qua sync Web Performance Tracking")
    parser.add_argument("--skip-trends", action="store_true", help="Bỏ qua Google Trends validation")
    parser.add_argument("--skip-hubs", action="store_true", help="Bỏ qua sync sang Web Hubs (react-web-momo)")
    parser.add_argument("--skip-seo-news", action="store_true", help="Bỏ qua sync tin SEO/GEO News")
    parser.add_argument("--skip-ga4", action="store_true", help="Bỏ qua sync GA4 thực tế sang Web Hubs")
    parser.add_argument("--skip-funnel", action="store_true", help="Bỏ qua bóc tách ma trận phễu GSC + GA4")
    parser.add_argument("--push-hubs", action="store_true", help="Tự động đẩy commit lên GitHub Hubs qua REST API (vượt qua firewall)")
    args = parser.parse_args()

    overall_start = time.time()
    results = {}

    print("\n" + "#"*70)
    print(f"# KHỞI CHẠY TỔNG ĐỒNG BỘ NỀN TẢNG WEB PLATFORM (MASTER SYNC)")
    print(f"# Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("#"*70)

    # 1. Luồng Web Performance Tracking
    if not args.skip_tracking:
        tracking_script = SCRIPTS_DIR / "sync_tracking_report.py"
        if tracking_script.exists():
            success, elapsed = run_step("Web Performance Tracking MTD", [str(tracking_script)])
            results["Web Tracking (MTD)"] = ("SUCCESS" if success else "FAILED", elapsed)
        else:
            results["Web Tracking (MTD)"] = ("SKIPPED (File not found)", 0)
    else:
        results["Web Tracking (MTD)"] = ("SKIPPED (User flag)", 0)

    # 2-4. Nhóm step ĐỘC LẬP (không ghi react-web-momo/hubs-momo) chạy SONG SONG:
    # Clarity Data Export, Google Trends Validation, Bing Copilot Ingest.
    # Các step ghi Hub (Tracking, Inventory, SEO News, GA4, Funnel, Push) vẫn chạy tuần tự bên dưới.
    parallel_tasks = []  # (step_name, command_args, result_key)

    # 2. Microsoft Clarity Data Export API
    if not args.skip_clarity:
        clarity_script = SCRIPTS_DIR / "fetch_clarity.py"
        if clarity_script.exists():
            clarity_args = [str(clarity_script)]
            if args.reprocess_clarity:
                clarity_args.append("--reprocess")
            parallel_tasks.append(("Microsoft Clarity API (AI & Frustration)", clarity_args, "Clarity Data Export"))
        else:
            results["Clarity Data Export"] = ("SKIPPED (File not found)", 0)
    else:
        results["Clarity Data Export"] = ("SKIPPED (User flag)", 0)

    # 3. Google Trends Validation (Top Financial Themes Rolling)
    if not args.skip_trends:
        trends_script = SCRIPTS_DIR / "cron_google_trends_validation.py"
        if trends_script.exists():
            parallel_tasks.append(("Google Trends Demand Validation", [
                str(trends_script),
                "--sector", "Financial",
                "--themes", "gia-vang,ty-gia,vay-tin-chap,vi-tra-sau,gui-tiet-kiem",
                "--kws-per-theme", "2"
            ], "Google Trends Validation"))
        else:
            results["Google Trends Validation"] = ("SKIPPED (File not found)", 0)
    else:
        results["Google Trends Validation"] = ("SKIPPED (User flag)", 0)

    # 4. Bing Webmaster / Copilot AI Ingest (Nếu có file export mới)
    bing_script = SCRIPTS_DIR / "ingest_bing_ai.py"
    if bing_script.exists():
        parallel_tasks.append(("Bing AI Copilot Performance Ingest", [str(bing_script)], "Bing Copilot Ingest"))

    if parallel_tasks:
        print(f"\n{'='*70}")
        print(f"▶ [PARALLEL GROUP] Chạy song song {len(parallel_tasks)} luồng độc lập")
        print(f"{'='*70}")
        par_start = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(parallel_tasks)) as ex:
            futures = {
                ex.submit(run_step_capture, name, cargs): (name, key)
                for name, cargs, key in parallel_tasks
            }
            for fut in concurrent.futures.as_completed(futures):
                name, key = futures[fut]
                success, elapsed, output = fut.result()
                print(f"\n{'='*70}")
                print(f"▶ [SYNC STEP] {name.upper()} (chạy song song, {elapsed:.1f}s)")
                print(f"{'='*70}")
                tail = output[-3000:] if len(output) > 3000 else output
                if tail.strip():
                    print(tail)
                status = "SUCCESS" if success else "FAILED"
                print(f"{'✓' if success else '✗'} [{name}] {status} ({elapsed:.1f}s)")
                results[key] = (status, elapsed)
        print(f"\n[PARALLEL GROUP] Hoàn thành {len(parallel_tasks)} luồng trong {time.time() - par_start:.1f}s")

    # 5. Luồng Sync Inventory & Clusters sang Web Hubs
    if not args.skip_hubs:
        hubs_script = SCRIPTS_DIR / "sync_inventory_to_hubs.py"
        if hubs_script.exists():
            success, elapsed = run_step("Sync Inventory & Clusters to Web Hubs", [str(hubs_script)])
            results["Web Hubs Distribution"] = ("SUCCESS" if success else "FAILED", elapsed)
        else:
            results["Web Hubs Distribution"] = ("SKIPPED (File not found)", 0)
    else:
        results["Web Hubs Distribution"] = ("SKIPPED (User flag)", 0)

    # 6. Luồng SEO/GEO News -> data/seo-news.json
    if not args.skip_seo_news:
        seo_news_script = SCRIPTS_DIR / "sync_seo_news.py"
        if seo_news_script.exists():
            success, elapsed = run_step("SEO/GEO News Feed -> Web Hubs", [str(seo_news_script)])
            results["SEO/GEO News Feed"] = ("SUCCESS" if success else "FAILED", elapsed)
        else:
            results["SEO/GEO News Feed"] = ("SKIPPED (File not found)", 0)
    else:
        results["SEO/GEO News Feed"] = ("SKIPPED (User flag)", 0)

    # 7. Luồng GA4 Real Performance & W2A Sync -> data/ga4/landing-pages.json
    if not args.skip_ga4:
        fetch_ga4_script = SCRIPTS_DIR / "fetch_ga4.js"
        if fetch_ga4_script.exists():
            print(f"\n{'='*70}")
            print(f"▶ [SYNC STEP] GA4 DATA API DIRECT FETCH")
            print(f"{'='*70}")
            t_ga4 = time.time()
            try:
                res_ga4 = subprocess.run(["node", str(fetch_ga4_script), "--days", "30"], cwd=str(BASE_DIR), capture_output=False, text=True)
                elap_ga4 = time.time() - t_ga4
                results["GA4 API Direct Fetch"] = ("SUCCESS" if res_ga4.returncode == 0 else "FAILED", elap_ga4)
            except Exception as e:
                elap_ga4 = time.time() - t_ga4
                results["GA4 API Direct Fetch"] = (f"FAILED ({e})", elap_ga4)

        ga4_script = SCRIPTS_DIR / "sync_ga4_to_hubs.py"
        if ga4_script.exists():
            success, elapsed = run_step("GA4 Real Data & W2A -> Web Hubs", [str(ga4_script)])
            results["GA4 Real Data (Hubs)"] = ("SUCCESS" if success else "FAILED", elapsed)
        else:
            results["GA4 Real Data (Hubs)"] = ("SKIPPED (File not found)", 0)
    else:
        results["GA4 API Direct Fetch"] = ("SKIPPED (User flag)", 0)
        results["GA4 Real Data (Hubs)"] = ("SKIPPED (User flag)", 0)

    # 8. Luồng Bóc tách Ma trận Phễu Hợp nhất (GSC + GA4 Full-Funnel)
    if not args.skip_funnel:
        funnel_script = SCRIPTS_DIR / "build_full_funnel_matrix.py"
        if funnel_script.exists():
            success, elapsed = run_step("Full-Funnel Matrix (GSC + GA4)", [str(funnel_script)])
            results["Full-Funnel Matrix"] = ("SUCCESS" if success else "FAILED", elapsed)
        else:
            results["Full-Funnel Matrix"] = ("SKIPPED (File not found)", 0)
    else:
        results["Full-Funnel Matrix"] = ("SKIPPED (User flag)", 0)

    # 9. Luồng Đẩy Commit sang GitHub (GitHub REST API Firewall Bypass)
    if args.push_hubs:
        push_script = SCRIPTS_DIR / "push_to_hubs_api.py"
        if push_script.exists():
            success, elapsed = run_step("Push to Hubs (GitHub REST API)", [str(push_script)])
            results["Push to GitHub Hubs"] = ("SUCCESS" if success else "FAILED", elapsed)
        else:
            results["Push to GitHub Hubs"] = ("SKIPPED (File not found)", 0)

    # Báo cáo tổng kết Master Sync
    total_elapsed = time.time() - overall_start
    print("\n" + "="*70)
    print("BÁO CÁO TỔNG KẾT TIẾN TRÌNH MASTER SYNC HOÀN TẤT")
    print("="*70)
    print(f"Tổng thời gian thực thi: {total_elapsed:.1f} giây\n")
    print(f"{'Luồng đồng bộ':<35} | {'Trạng thái':<15} | {'Thời gian'}")
    print("-" * 70)
    for name, (status, elap) in results.items():
        print(f"{name:<35} | {status:<15} | {elap:.1f}s")
    print("="*70 + "\n")

if __name__ == "__main__":
    with hub_sync_lock("sync_all_data"):
        main()
