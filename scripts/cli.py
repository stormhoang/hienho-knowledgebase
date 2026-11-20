#!/usr/bin/env python3
"""Unified CLI runner for Web Platform codebase scripts and tools.

Usage:
    python3 scripts/cli.py ads [args...]          # ingest_paid_ads.py (GA4 Explore CSV -> paid_ads_performance.json)
    python3 scripts/cli.py ga4 [args...]          # ingest_ga4_daily.py (GA4 Explore CSV -> ga4_daily/)
    python3 scripts/cli.py ingest-gsc [args...]   # ingest_gsc_mtd.py (GSC Sheet/ZIP -> page_mtd.json)
    python3 scripts/cli.py sync [args...]
    python3 scripts/cli.py report-html [args...]
    python3 scripts/cli.py report-pptx [args...]
    python3 scripts/cli.py md-process [dir_path]
    python3 scripts/cli.py info
"""
import sys
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT_DIR / "scripts" / "tools"
LIB_DIR = ROOT_DIR / "scripts" / "lib"

def run_tool(script_path: Path, args: list):
    if not script_path.exists():
        print(f"Error: Tool script not found at {script_path}", file=sys.stderr)
        sys.exit(1)
    cmd = [sys.executable, str(script_path)] + args
    return subprocess.call(cmd)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        sys.exit(0)

    command = sys.argv[1]
    extra_args = sys.argv[2:]

    if command == "report-html":
        sys.exit(run_tool(TOOLS_DIR / "generate_report_html.py", extra_args))
    elif command == "report-pptx":
        sys.exit(run_tool(TOOLS_DIR / "generate_pptx.py", extra_args))
    elif command in ("md-process", "compress-md"):
        from scripts.lib.md_utils import process_markdown_directory
        target_dir = extra_args[0] if extra_args else str(ROOT_DIR)
        print(f"Processing markdown files in {target_dir}...")
        process_markdown_directory(target_dir, compress=True, remove_yaml=False)
    elif command in ("sync", "sync-all"):
        sys.exit(subprocess.call([sys.executable, str(ROOT_DIR / "scripts" / "sync_all_data.py")] + extra_args))
    elif command in ("ads", "sync-ads", "paid", "ingest-paid"):
        sys.exit(subprocess.call([sys.executable, str(ROOT_DIR / "scripts" / "ingest_paid_ads.py")] + extra_args))
    elif command in ("ga4", "fetch-ga4", "ingest-ga4"):
        sys.exit(subprocess.call([sys.executable, str(ROOT_DIR / "scripts" / "ingest_ga4_daily.py")] + extra_args))
    elif command in ("ingest-gsc", "gsc-mtd"):
        sys.exit(subprocess.call([sys.executable, str(ROOT_DIR / "scripts" / "ingest_gsc_mtd.py")] + extra_args))
    elif command == "info":
        print(f"Web Platform Unified CLI Engine")
        print(f"Root Directory: {ROOT_DIR}")
        print(f"Active Tools:")
        for tool in TOOLS_DIR.glob("*.py"):
            print(f"  - {tool.name}")
        print("  - ads / sync-ads / paid / ingest-paid (Paid Ads ingest tu GA4 Explore CSV)")
        print("  - ga4 / fetch-ga4 / ingest-ga4 (GA4 Explore CSV -> ga4_daily/)")
        print("  - ingest-gsc / gsc-mtd (GSC Sheet/ZIP -> page_mtd.json)")
        print("  - sync / sync-all (Master Data Sync Runner)")
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        print("Available commands: ads, ga4, ingest-gsc, sync, report-html, report-pptx, md-process, info")
        sys.exit(1)

if __name__ == "__main__":
    main()
