import sys
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
from scripts.build_full_funnel_matrix import build_theme_matcher, normalize_path

def run():
    matcher = build_theme_matcher()
    data_path = BASE_DIR / "07_REPORTS" / "data" / "ga4" / "landing-pages.json"
    if not data_path.exists():
        return

    with open(data_path, "r", encoding="utf-8") as f:
        ga4_data = json.load(f)

    rows = ga4_data.get("rows", [])
    project_stats = {}
    total_sessions = 0
    total_w2a = 0
    channel_stats = {}

    for r in rows:
        p = normalize_path(r.get("landing_page", ""))
        s = r.get("sessions", 0)
        w = r.get("onelink_clicks_track1", 0) + r.get("onelink_clicks_track2", 0)
        cg = r.get("channel_group", "Other")
        total_sessions += s
        total_w2a += w

        if cg not in channel_stats:
            channel_stats[cg] = {"sessions": 0, "w2a": 0, "pages": set()}
        channel_stats[cg]["sessions"] += s
        channel_stats[cg]["w2a"] += w
        channel_stats[cg]["pages"].add(p)

        tid, tname, sec, mvol, proj, ptype = matcher(p)
        if proj not in project_stats:
            project_stats[proj] = {
                "sessions": 0, "w2a": 0, "pages": set(),
                "channels": {}
            }
        project_stats[proj]["sessions"] += s
        project_stats[proj]["w2a"] += w
        project_stats[proj]["pages"].add(p)
        if cg not in project_stats[proj]["channels"]:
            project_stats[proj]["channels"][cg] = {"sessions": 0, "w2a": 0}
        project_stats[proj]["channels"][cg]["sessions"] += s
        project_stats[proj]["channels"][cg]["w2a"] += w

    cr = (total_w2a / total_sessions * 100) if total_sessions > 0 else 0.0
    print(f"Total rows: {len(rows):,}")
    print(f"Total sessions: {total_sessions:,}")
    print(f"Total W2A Clicks: {total_w2a:,} (Overall CR: {cr:.2f}%)")

if __name__ == "__main__":
    run()
