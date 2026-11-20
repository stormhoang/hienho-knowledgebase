#!/usr/bin/env python3
"""
MoMo Web Platform Report Generator
JSON data -> HTML slide deck (brand MoMo, Be Vietnam Pro)

Usage:
    python3 07_REPORTS/scripts/generate_report_html.py 07_REPORTS/data/monthly/monthly_08_2026.json -o 07_REPORTS/dashboards/monthly_THÁNG082026.html
    python3 07_REPORTS/scripts/generate_report_html.py 07_REPORTS/data/weekly_w33_2026.json -o 07_REPORTS/dashboards/weekly_w33.html
"""

import argparse
import json
import os
import sys

# ── Brand tokens ──
MAGENTA = "#A50064"
DARK_MAGENTA = "#6B0042"
PINK_HEADER = "#E5007D"
SOFT_PINK = "#FCE4EC"
ACCENTS = {
    "magenta": "#A50064",
    "teal": "#00838F",
    "blue": "#1565C0",
    "green": "#2E7D32",
    "amber": "#D97706",
    "gold": "#B8860B",
}
INK_DARK = "#1E1E24"
INK_SOFT = "#5A5A68"
BORDER = "#E2E8F0"
STAGE_BG = "#F4F5F9"

ZONE_COLORS = {
    "Performance": "green",
    "Transformation": "blue",
    "Incubation": "amber",
    "Productivity": "teal",
}
ZONE_EMOJI = ""


def esc(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def slide_wrap(idx, inner):
    return f'<div class="slide" data-idx="{idx:02d}">{inner}</div>'


def header(title, subtitle=""):
    sub = f"<p>{esc(subtitle)}</p>" if subtitle else ""
    return f"""
    <div class="slide-header">
      <div class="brand-logo">mo<br>mo</div>
      <div class="slide-title-wrap">
        <h1>{esc(title)}</h1>
        {sub}
      </div>
    </div>"""


def card(title, items, accent="magenta", kind="list"):
    color = ACCENTS.get(accent, MAGENTA)
    if kind == "list":
        lis = "".join(f"<li>{i}</li>" for i in items)
        body = f'<ul class="b-list">{lis}</ul>'
    else:
        body = items
    return f"""
    <div class="card" style="border-top:4px solid {color};">
      <div class="card-header"><h2>{esc(title)}</h2></div>
      <div class="card-body">{body}</div>
    </div>"""


def kpi_grid(kpis):
    cells = ""
    for k in kpis:
        color = ACCENTS.get(k.get("color", "magenta"), MAGENTA)
        delta = f'<div class="kpi-delta">{esc(k["delta"])}</div>' if k.get("delta") else ""
        target = f'<div class="kpi-target">Target: {esc(k["target"])}</div>' if k.get("target") and k["target"] != "-" else ""
        cells += f"""
        <div class="kpi">
          <div class="kpi-value" style="color:{color};">{esc(k["value"])}</div>
          {delta}
          <div class="kpi-label">{esc(k["label"])}</div>
          {target}
        </div>"""
    return f'<div class="kpi-grid">{cells}</div>'


def table_block(title, columns, rows, highlight_col=None, first_col_bold=True):
    ths = "".join(
        ('<th class="cur">' if c.get("current") else "<th>") + esc(c["label"]) + "</th>"
        for c in columns
    )
    trs = ""
    for r in rows:
        tds = ""
        for i, c in enumerate(columns):
            val = r.get(c["key"], "")
            cls = ""
            if c.get("current"):
                cls += " cur"
            if first_col_bold and i == 0:
                cls += " strong"
            tds += f'<td class="{cls.strip()}">{esc(val)}</td>'
        trs += f"<tr>{tds}</tr>"
    return f"""
    <div class="table-wrap">
      <div class="table-title">{esc(title)}</div>
      <table class="matrix-table">
        <thead><tr>{ths}</tr></thead>
        <tbody>{trs}</tbody>
      </table>
    </div>"""


def bullet(items, prefix=""):
    return "".join(f"<li><b>{prefix}</b>{esc(i)}</li>" if prefix else f"<li>{esc(i)}</li>" for i in items)


def build_monthly(data):
    slides = []
    meta = data["meta"]
    idx = 1

    # SLIDE 1 - Cover
    cover = f"""
    <div class="cover-bg"></div>
    <div class="cover-inner">
      <div class="cover-brand">MOMO · GROWTH PLATFORM DIVISION</div>
      <h1>{esc(meta["title"])}</h1>
      <div class="cover-period">{esc(meta["period"])}</div>
      <div class="cover-sub">{esc(meta["subtitle"])}</div>
      <div class="cover-meta">{esc(meta["team"])} · {esc(meta["date"])}</div>
    </div>"""
    slides.append(slide_wrap(idx, cover))
    idx += 1

    # SLIDE 2 - Executive Summary (KPIs)
    exec_inner = header("Executive Summary", "Tổng quan hiệu suất tháng")
    exec_inner += kpi_grid(data["kpis"])
    slides.append(slide_wrap(idx, exec_inner))
    idx += 1

    # SLIDE 3 - Key Highlights
    cols = []
    for i, h in enumerate(data["highlights"]):
        accent = ["magenta", "teal", "blue", "green"][i % 4]
        cols.append(card(h["title"], [h["body"]], accent=accent))
    highlights = header("Key Highlights & Định Hướng Chiến Lược", "Trọng tâm tháng")
    highlights += f'<div class="grid-2">{ "".join(cols) }</div>'
    slides.append(slide_wrap(idx, highlights))
    idx += 1

    # SLIDE 4 - Funnel
    fun = header(data["funnel"]["title"])
    fun += table_block(data["funnel"]["title"], data["funnel"]["columns"], data["funnel"]["rows"])
    slides.append(slide_wrap(idx, fun))
    idx += 1

    # SLIDE 5 - Channels
    ch = header(data["channels"]["title"])
    ch += table_block(data["channels"]["title"], data["channels"]["columns"], data["channels"]["rows"])
    slides.append(slide_wrap(idx, ch))
    idx += 1

    # SLIDES - Hubs (1 hub per slide, 2 columns: results/issues + actions)
    for hub in data["hubs"]:
        zone_key = hub.get("zone", "")
        zone_color = "blue"
        for z, c in ZONE_COLORS.items():
            if z in zone_key:
                zone_color = c
        hub_inner = header(hub["name"], hub.get("tagline", ""))
        hub_inner += f'<div class="zone-badge" style="border-left:4px solid {ACCENTS[zone_color]}; color:{ACCENTS[zone_color]};">{esc(zone_key)}</div>'
        if hub.get("kpis"):
            hub_inner += kpi_grid(hub["kpis"])
        hub_inner += f"""
        <div class="grid-2">
          {card("Kết Quả Triển Khai", hub.get("results", []), accent="green")}
          {card("Điểm Nghẽn & Vấn Đề", hub.get("issues", []), accent="amber")}
        </div>
        <div class="grid-1">
          {card("Action Items & Hướng Xử Lý", hub.get("actions", []), accent="magenta")}
        </div>"""
        slides.append(slide_wrap(idx, hub_inner))
        idx += 1

    # SLIDE - 30 days forward
    n30 = header("Phối Hợp Liên Phòng Ban & Trọng Tâm 30 Ngày Tới")
    n30 += f"""
    <div class="grid-1">
      {card("Trọng Tâm 30 Ngày Tới", data.get("next30days", []), accent="blue")}
    </div>"""
    slides.append(slide_wrap(idx, n30))
    idx += 1

    # SLIDE - Roadmap
    rm = header(data["roadmap"]["title"])
    rm += table_block(data["roadmap"]["title"], data["roadmap"]["columns"], data["roadmap"]["rows"], first_col_bold=True)
    slides.append(slide_wrap(idx, rm))
    idx += 1

    # SLIDE - Closing
    close = f"""
    <div class="cover-bg"></div>
    <div class="cover-inner">
      <h1 style="font-size:3rem;">Thank You</h1>
      <div class="cover-sub">Growth Platform Division (GPD) · Web Platform Team</div>
      <div class="cover-meta">{esc(meta["date"])} · {esc(meta["author"])}</div>
    </div>"""
    slides.append(slide_wrap(idx, close))

    return slides


def build_weekly(data):
    slides = []
    meta = data["meta"]
    idx = 1

    # SLIDE 1 - Cover
    cover = f"""
    <div class="cover-bg"></div>
    <div class="cover-inner">
      <div class="cover-brand">MOMO · GROWTH PLATFORM DIVISION</div>
      <h1>{esc(meta["title"])}</h1>
      <div class="cover-period">{esc(meta["period"])}</div>
      <div class="cover-sub">{esc(meta["subtitle"])}</div>
      <div class="cover-meta">{esc(meta["team"])} · {esc(meta["date"])}</div>
    </div>"""
    slides.append(slide_wrap(idx, cover))
    idx += 1

    # SLIDE 2 - Executive Summary
    exec_inner = header("Executive Summary", "Tổng quan hiệu suất tuần")
    exec_inner += kpi_grid(data["kpis"])
    slides.append(slide_wrap(idx, exec_inner))
    idx += 1

    # SLIDE 3 - Highlights
    cols = []
    for i, h in enumerate(data["highlights"]):
        accent = ["magenta", "teal", "blue", "green"][i % 4]
        cols.append(card(h["title"], [h["body"]], accent=accent))
    highlights = header("Điểm Nổi Bật Tuần")
    highlights += f'<div class="grid-2">{ "".join(cols) }</div>'
    slides.append(slide_wrap(idx, highlights))
    idx += 1

    # SLIDE 4 - Weekly progress table
    wp = data["weeklyProgress"]
    prog = header(wp["title"])
    prog += table_block(wp["title"], wp["columns"], wp["rows"], first_col_bold=False)
    slides.append(slide_wrap(idx, prog))
    idx += 1

    # SLIDES - Hub blocks
    for hub in data.get("hubBlocks", []):
        zone_key = hub.get("zone", "")
        zone_color = "blue"
        for z, c in ZONE_COLORS.items():
            if z in zone_key:
                zone_color = c
        hub_inner = header(hub["name"], f"{zone_key} · Weekly Update")
        hub_inner += f"""
        <div class="grid-2">
          {card("Kết Quả Tuần", hub.get("results", []), accent="green")}
          {card("Hành Động Tuần Sau", hub.get("actions", []), accent="magenta")}
        </div>"""
        slides.append(slide_wrap(idx, hub_inner))
        idx += 1

    # SLIDE - Next 30 days
    n30 = header("Trọng Tâm 30 Ngày Tới")
    n30 += f'<div class="grid-1">{card("Next Actions", data.get("next30days", []), accent="blue")}</div>'
    slides.append(slide_wrap(idx, n30))
    idx += 1

    # SLIDE - Closing
    close = f"""
    <div class="cover-bg"></div>
    <div class="cover-inner">
      <h1 style="font-size:3rem;">Thank You</h1>
      <div class="cover-sub">Growth Platform Division (GPD) · Web Platform Team</div>
      <div class="cover-meta">{esc(meta["date"])} · {esc(meta["author"])}</div>
    </div>"""
    slides.append(slide_wrap(idx, close))

    return slides


CSS = """
:root{
  --momo-magenta:#A50064; --momo-dark-magenta:#6B0042; --momo-pink-header:#E5007D;
  --momo-soft-pink:#FCE4EC; --accent-gold:#E8A820; --accent-teal:#00838F;
  --accent-blue:#1565C0; --accent-green:#2E7D32; --accent-amber:#D97706;
  --ink-dark:#1E1E24; --ink-soft:#5A5A68; --paper:#FFFFFF; --border-line:#E2E8F0;
}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;font-family:'Be Vietnam Pro',sans-serif;background:#0E0A14;color:var(--ink-dark);-webkit-font-smoothing:antialiased;overflow:hidden;}
.deck{position:relative;width:100vw;height:100vh;display:flex;align-items:center;justify-content:center;padding:16px;}
.stage{width:100%;height:100%;max-width:1440px;max-height:860px;position:relative;box-shadow:0 30px 90px -20px rgba(0,0,0,.6);border-radius:20px;overflow:hidden;background:var(--paper);display:flex;flex-direction:column;}
.slide{position:absolute;inset:0;display:none;flex-direction:column;opacity:0;transform:translateY(6px);transition:opacity .3s ease,transform .3s ease;padding:32px 40px;background:var(--paper);overflow-y:auto;}
.slide.active{display:flex;opacity:1;transform:translateY(0);}
.slide-header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:16px;border-bottom:2px solid var(--border-line);padding-bottom:12px;}
.brand-logo{font-size:2.2rem;font-weight:900;color:var(--momo-magenta);line-height:.9;letter-spacing:-.04em;}
.slide-title-wrap{flex:1;margin-left:24px;}
.slide-title-wrap h1{font-size:1.7rem;font-weight:800;color:var(--momo-magenta);line-height:1.2;letter-spacing:-.01em;}
.slide-title-wrap p{font-size:.85rem;color:var(--ink-soft);font-weight:600;line-height:1.45;margin-top:4px;}
.grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;flex:1;}
.grid-1{display:grid;grid-template-columns:1fr;gap:20px;}
.card{background:#FAFBFD;border:1px solid var(--border-line);border-radius:16px;padding:20px;display:flex;flex-direction:column;gap:12px;box-shadow:0 4px 16px rgba(0,0,0,.02);}
.card-header{display:flex;align-items:center;gap:10px;padding-bottom:8px;border-bottom:2px solid var(--border-line);}
.card-header h2{font-size:1.02rem;font-weight:800;color:var(--ink-dark);}
.card-body{font-size:.84rem;line-height:1.55;color:var(--ink-dark);display:flex;flex-direction:column;gap:10px;flex:1;}
.b-list{list-style:none;display:flex;flex-direction:column;gap:8px;}
.b-list li{position:relative;padding-left:18px;font-size:.84rem;line-height:1.55;}
.b-list li::before{content:"";position:absolute;left:0;top:8px;width:6px;height:6px;border-radius:50%;background:var(--momo-magenta);}
.b-list li b{font-weight:700;color:var(--ink-dark);}
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin-bottom:20px;}
.kpi{background:var(--paper);border:1px solid var(--border-line);border-radius:14px;padding:18px;text-align:center;box-shadow:0 4px 16px rgba(0,0,0,.03);}
.kpi-value{font-size:1.9rem;font-weight:900;letter-spacing:-.02em;font-family:'Be Vietnam Pro',sans-serif;}
.kpi-delta{font-size:.78rem;font-weight:800;color:var(--accent-green);margin-top:2px;}
.kpi-label{font-size:.78rem;font-weight:700;color:var(--ink-soft);margin-top:6px;}
.kpi-target{font-size:.7rem;color:#9AA3B2;margin-top:4px;}
.table-wrap{overflow-x:auto;border:1px solid var(--border-line);border-radius:12px;background:var(--paper);flex:1;}
.table-title{font-size:.9rem;font-weight:800;color:var(--ink-dark);padding:14px 16px;border-bottom:1px solid var(--border-line);}
.matrix-table{width:100%;border-collapse:collapse;text-align:left;font-size:.8rem;}
.matrix-table th{background:var(--momo-pink-header);color:#fff;padding:11px 14px;font-weight:700;text-transform:uppercase;font-size:.7rem;letter-spacing:.04em;border-bottom:2px solid var(--momo-magenta);white-space:nowrap;}
.matrix-table td{padding:11px 14px;border-bottom:1px solid var(--border-line);vertical-align:top;line-height:1.45;color:var(--ink-dark);}
.matrix-table tr:nth-child(even){background:#FAFBFD;}
.matrix-table td.cur{background:#FFF5F9;font-weight:700;color:var(--momo-magenta);}
.matrix-table th.cur{background:var(--momo-magenta);}
.matrix-table td.strong{font-weight:700;}
.zone-badge{display:inline-block;padding:6px 14px;border-radius:8px;background:#F8FAFC;font-size:.78rem;font-weight:800;margin-bottom:14px;}
.cover-bg{position:absolute;inset:0;background:linear-gradient(135deg,#6B0042 0%,#A50064 55%,#E5007D 100%);}
.cover-inner{position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;text-align:center;color:#fff;padding:40px;}
.cover-brand{font-size:.85rem;font-weight:800;letter-spacing:.22em;color:#FFCCE5;margin-bottom:28px;}
.cover-inner h1{font-size:2.6rem;font-weight:900;line-height:1.25;letter-spacing:-.01em;max-width:1000px;}
.cover-period{font-size:1.4rem;font-weight:800;color:#FFCCE5;margin-top:20px;}
.cover-sub{font-size:1rem;font-weight:600;color:#FFD9EB;margin-top:16px;max-width:800px;line-height:1.6;}
.cover-meta{font-size:.82rem;font-weight:600;color:#BB88A0;margin-top:36px;}
.nav{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:14px;background:rgba(15,10,20,.9);backdrop-filter:blur(8px);padding:8px 20px;border-radius:100px;z-index:99;border:1px solid rgba(255,255,255,.18);box-shadow:0 10px 30px rgba(0,0,0,.5);}
.nav button{width:32px;height:32px;border-radius:50%;border:none;background:rgba(255,255,255,.15);color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1.1rem;transition:all .2s;}
.nav button:hover{background:var(--momo-magenta);}
.nav button:disabled{opacity:.3;cursor:default;}
.nav .dots{display:flex;gap:6px;}
.nav .dots span{width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,.3);cursor:pointer;transition:all .2s;}
.nav .dots span.on{background:var(--accent-gold);transform:scale(1.4);}
.nav .counter{font-family:'JetBrains Mono',monospace;font-size:.75rem;color:rgba(255,255,255,.85);min-width:45px;text-align:center;}
@media print{.deck{height:auto;padding:0;}.stage{box-shadow:none;border-radius:0;max-height:none;overflow:visible;}.slide{position:relative;display:flex!important;opacity:1;transform:none;page-break-after:always;height:100vh;}.nav{display:none;}}
"""

JS = """
<script>
(function(){
  const slides=[].slice.call(document.querySelectorAll('.slide'));
  const dotsWrap=document.getElementById('dots');
  const counter=document.getElementById('counter');
  let cur=0;
  slides.forEach((s,i)=>{
    const d=document.createElement('span');
    d.addEventListener('click',()=>goto(i));
    dotsWrap.appendChild(d);
  });
  const dots=dotsWrap.children;
  function goto(i){
    if(i<0||i>=slides.length)return;
    slides[cur].classList.remove('active');
    dots[cur].classList.remove('on');
    cur=i;
    slides[cur].classList.add('active');
    dots[cur].classList.add('on');
    counter.textContent=(cur+1)+' / '+slides.length;
    slides[cur].scrollTop=0;
  }
  document.getElementById('prev').addEventListener('click',()=>goto(cur-1));
  document.getElementById('next').addEventListener('click',()=>goto(cur+1));
  document.addEventListener('keydown',e=>{
    if(e.key==='ArrowRight'||e.key==='ArrowDown'||e.key==='PageDown')goto(cur+1);
    if(e.key==='ArrowLeft'||e.key==='ArrowUp'||e.key==='PageUp')goto(cur-1);
    if(e.key==='Home')goto(0);
    if(e.key==='End')goto(slides.length-1);
  });
  goto(0);
})();
</script>
"""


def build_html(data):
    meta = data["meta"]
    report_type = meta.get("type", "monthly")
    slides = build_monthly(data) if report_type == "monthly" else build_weekly(data)
    slides_html = "\n".join(slides)
    title = f'{meta.get("title")} - {meta.get("period")} | MoMo Web Platform'
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>{esc(title)}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="deck">
  <div class="stage" id="stage">
    {slides_html}
  </div>
</div>
<div class="nav">
  <button id="prev" aria-label="Previous">‹</button>
  <div class="dots" id="dots"></div>
  <span class="counter" id="counter">1 / 1</span>
  <button id="next" aria-label="Next">›</button>
</div>
{JS}
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Generate MoMo branded HTML slide deck from JSON data")
    parser.add_argument("data", help="Path to report JSON file")
    parser.add_argument("-o", "--output", help="Output HTML path (default: 07_REPORTS/<type>_<period>.html)")
    args = parser.parse_args()

    data_path = args.data
    if not os.path.exists(data_path):
        print(f"Error: file not found: {data_path}")
        sys.exit(1)

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    meta = data["meta"]
    output = args.output
    if not output:
        safe_period = "".join(c for c in meta.get("period", "report") if c.isalnum() or c in "-_")
        fname = f'{meta.get("type", "report")}_{safe_period}.html'
        output = os.path.join("07_REPORTS", fname)

    html = build_html(data)
    os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"OK: generated {output} ({len(html)//1024} KB, {len(json.dumps(data))//1024} KB data)")


if __name__ == "__main__":
    main()
