#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KNOWLEDGE GRAPH - build + query do thi tri thuc repo (Phase 3).

Nodes : file .md (knowledge dirs), scripts .py, skills SKILL.md, data artifacts
        duoc reference, registry entries.
Edges :
  links_to    - link markdown (file:/// hoac relative .md) giua cac docs
  routes_to   - FAST_ROUTING_INDEX row -> target file
  generates   - registry generator_script -> artifact path
  cross_check - registry entry <-> cross_check_with ids
  references  - bat ky file nao -> path literal repo ton tai
  io_write    - script -> artifact (heuristic: path literal tren dong co open 'w'/json.dump/write_text)
  io_read     - script -> artifact (heuristic: json.load/open 'r'/read_text/glob)

Output : 00_HARNESS_CORE/knowledge_graph.json

Cach dung:
    ./.venv/bin/python scripts/build_knowledge_graph.py                 # build graph
    ./.venv/bin/python scripts/build_knowledge_graph.py --stats         # thong ke
    ./.venv/bin/python scripts/build_knowledge_graph.py --node page_mtd # node + neighbors
    ./.venv/bin/python scripts/build_knowledge_graph.py --produces page_mtd.json
    ./.venv/bin/python scripts/build_knowledge_graph.py --consumes ingest_gsc
    ./.venv/bin/python scripts/build_knowledge_graph.py --path A B      # shortest path
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).resolve().parents[1]
GRAPH_PATH = BASE_DIR / "00_HARNESS_CORE" / "knowledge_graph.json"
REGISTRY_PATH = BASE_DIR / "00_HARNESS_CORE" / "knowledge_registry.yaml"
ROUTING_PATH = BASE_DIR / "00_HARNESS_CORE" / "FAST_ROUTING_INDEX.md"

MD_DIRS = ["00_HARNESS_CORE", "03_SKILLS", "05_HUBS", "06_USE_CASE_MOMO",
           "07_REPORTS/docs", "14_ROADMAP"]
SKIP_PARTS = {".git", "node_modules", "archive", "scratch", "__pycache__", ".venv"}

PATH_LITERAL_RE = re.compile(
    r"(?<![\w/.-])((?:scripts|00_HARNESS_CORE|03_SKILLS|04_MOSPARK_PLATFORM|05_HUBS|"
    r"06_USE_CASE_MOMO|07_REPORTS|14_ROADMAP|\.agents|graphify-out)/[^\s\"'`,)\]}]+)"
)
KNOWN_TOP = ("scripts", "00_HARNESS_CORE", "03_SKILLS", "04_MOSPARK_PLATFORM", "05_HUBS",
             "06_USE_CASE_MOMO", "07_REPORTS", "14_ROADMAP", ".agents", "graphify-out")
JOIN_RE = re.compile(r"os\.path\.join\(([^)]*)\)")
DIVCHAIN_RE = re.compile(r"((?:BASE_DIR|HUBS_REPO|REPO_ROOT|KB_REPO|HUB_REPO|\w*DIR\w*|\w*REPO\w*)\s*(?:/\s*[\"'][^\"']+[\"']\s*)+)")
VAR_ASSIGN_RE = re.compile(r"^\s*(\w+)\s*=\s*(.+?)\s*$")
OPEN_VAR_RE = re.compile(r"open\(\s*(\w+)((?:\s*,\s*[^)]*)?)\)")
ABS_PATH_RE = re.compile(r"[\"'](/[^\"']*(?:react-web-momo|Hienho_MoMo-Base)/[^\"']+)[\"']")
LOAD_RE = re.compile(r"(?:json\.load|json\.loads|pd\.read_csv|read_text|read_excel|glob|os\.path\.exists|Path\([^)]*\)\.exists)\s*\(?\s*(\w+)?")
WRITE_TOKENS = ("json.dump", "write_text", "to_csv", "to_excel", "shutil.copy", ".write(")
FILE_URI_RE = re.compile(r"\((file:///[^)\s]+)\)")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+\.md[^)\s]*)\)")
WRITE_LINE_RE = re.compile(r"json\.dump|write_text|to_csv|to_excel|open\([^)]*['\"][wa]|shutil\.copy|\.write\(")
READ_LINE_RE = re.compile(r"json\.load|read_text|open\([^)]*['\"]r|glob|os\.path\.exists|Path\([^)]*\)\.exists")


def is_skipped(path: Path) -> bool:
    return any(part in SKIP_PARTS for part in path.parts)


def collect_md_files():
    files = []
    for d in MD_DIRS:
        root = BASE_DIR / d
        if not root.exists():
            continue
        for p in root.rglob("*.md"):
            if not is_skipped(p):
                files.append(p)
    for p in BASE_DIR.glob("*.md"):
        files.append(p)
    return sorted(set(files))


def collect_scripts():
    files = []
    for p in (BASE_DIR / "scripts").rglob("*.py"):
        if not is_skipped(p):
            files.append(p)
    for p in (BASE_DIR / ".agents" / "skills").rglob("SKILL.md"):
        files.append(p)
    return sorted(set(files))


def rel(p: Path) -> str:
    return str(p.relative_to(BASE_DIR))


def norm_node_id(path_str: str) -> str:
    return path_str.rstrip("/.")


def _join_args_to_path(argstr):
    """os.path.join(BASE_DIR, '07_REPORTS', 'data', 'x.json') -> '07_REPORTS/data/x.json'."""
    segs = re.findall(r"[\"']([^\"']+)[\"']", argstr)
    segs = [s for s in segs if s not in (".", "..") and "/" not in s or s.startswith(("07_", "00_", "scripts", "data", "lib", "app"))]
    if not segs:
        return None
    joined = "/".join(segs)
    if joined.startswith(KNOWN_TOP):
        return joined
    # thuong hop: '07_REPORTS','data','x.json' -> '07_REPORTS/data/x.json'
    if segs[0] in KNOWN_TOP or segs[0].startswith(("07_", "00_", "03_", "04_", "05_", "06_", "14_")):
        return joined
    return None


def _divchain_to_paths(expr, var_paths=None):
    """Resolve bieu thuc `VAR / 'seg' / 'seg'` thanh tap path repo.

    - VAR la BASE_DIR/HUBS_REPO/const: segs noi tiep, loc theo KNOWN_TOP.
    - VAR da co base path trong var_paths (vd KB_DATA_DIR='07_REPORTS/data'):
      ghep de quy -> '07_REPORTS/data/analytics/page_mtd.json'.
    - HUBS_REPO/... -> 'react-web-momo/...'.
    """
    var = expr.split("/")[0].strip()
    segs = re.findall(r"[\"']([^\"']+)[\"']", expr)
    if not segs:
        return set()
    joined = "/".join(segs)
    out = set()
    var_up = var.upper()
    if "HUB" in var_up or ("REPO" in var_up and "BASE" not in var_up):
        out.add("react-web-momo/" + joined)
    elif var_paths and var in var_paths:
        for base in var_paths[var]:
            cand = base.rstrip("/") + "/" + joined
            if cand.startswith(KNOWN_TOP):
                out.add(cand)
    if joined.startswith(KNOWN_TOP) or segs[0] in KNOWN_TOP or segs[0].startswith(
            ("07_", "00_", "03_", "04_", "05_", "06_", "14_")):
        out.add(joined)
    return out


def _norm_raw(raw):
    """Chuan hoa path: absolute -> relative repo; .../react-web-momo/x -> react-web-momo/x."""
    raw = raw.rstrip("/.")
    if raw.startswith("/"):
        if "react-web-momo/" in raw:
            return "react-web-momo/" + raw.split("react-web-momo/", 1)[1]
        try:
            return str(Path(raw).resolve().relative_to(BASE_DIR))
        except (ValueError, OSError):
            return raw
    return raw


def extract_script_io(text):
    """Tra ve (refs, reads, writes): set path literal repo.

    Xu ly 3 dang: literal lien tuc, os.path.join(...), var / 'seg' chains.
    Phan loai read/write dua tren bien trung gian: VAR = <path>; open(VAR,..'w') -> write.
    """
    refs, reads, writes = set(), set(), set()

    # 0. absolute path literals -> react-web-momo/... hoac relative repo
    for m in ABS_PATH_RE.finditer(text):
        refs.add(_norm_raw(m.group(1)))

    # 1. literal lien tuc (doc + ref)
    for m in PATH_LITERAL_RE.finditer(text):
        refs.add(_norm_raw(m.group(1)))

    # 2. os.path.join(...) -> path
    for m in JOIN_RE.finditer(text):
        p = _join_args_to_path(m.group(1))
        if p:
            refs.add(_norm_raw(p))

    # 3. var->paths map + div chains gan truc tiep
    var_paths = defaultdict(set)
    for line in text.splitlines():
        # VAR = os.path.join(...) hoac VAR = BASE_DIR / 'a' / 'b' hoac VAR = 'path'
        am = VAR_ASSIGN_RE.match(line)
        if not am:
            continue
        var, rhs = am.groups()
        for jm in JOIN_RE.finditer(rhs):
            p = _join_args_to_path(jm.group(1))
            if p:
                var_paths[var].add(_norm_raw(p))
                refs.add(_norm_raw(p))
        for dm in DIVCHAIN_RE.finditer(rhs):
            for p in _divchain_to_paths(dm.group(1), var_paths):
                var_paths[var].add(_norm_raw(p))
                refs.add(_norm_raw(p))
        lm = PATH_LITERAL_RE.search(rhs)
        if lm:
            var_paths[var].add(_norm_raw(lm.group(1)))
            refs.add(_norm_raw(lm.group(1)))

    # 4. io classification: open(VAR, mode), json.load/dump, read_*, write calls
    # open(VAR, 'w'/'a') -> write ; open(VAR) / open(VAR,'r') -> read
    for m in OPEN_VAR_RE.finditer(text):
        var, args = m.group(1), m.group(2) or ""
        is_write = bool(re.search(r"['\"][wa]\+?['\"]", args))
        for p in var_paths.get(var, ()):
            (writes if is_write else reads).add(_norm_raw(p))
    # literal open("path", "w")
    for m in re.finditer(r"open\(\s*[\"']([^\"']+)[\"']\s*,\s*['\"]([wa])", text):
        raw = m.group(1)
        if raw.startswith(KNOWN_TOP) or raw.startswith("react-web-momo"):
            writes.add(_norm_raw(raw))
            refs.add(_norm_raw(raw))
    for m in re.finditer(r"(?:json\.load|json\.loads)\s*\(\s*open\(\s*[\"']([^\"']+)[\"']", text):
        raw = m.group(1)
        if raw.startswith(KNOWN_TOP):
            reads.add(_norm_raw(raw))
            refs.add(_norm_raw(raw))
    # VAR.write_text / VAR.to_csv / shutil.copy*(.., VAR)
    for var, paths in var_paths.items():
        for p in paths:
            if re.search(rf"{re.escape(var)}\.(write_text|to_csv|to_excel)\b", text):
                writes.add(_norm_raw(p))
            if re.search(rf"(?:json\.load|read_text|read_csv|glob|exists)\s*\(?\s*{re.escape(var)}\b", text):
                reads.add(_norm_raw(p))
            if re.search(rf"json\.dump\([^)]*?{re.escape(var)}", text, re.S):
                writes.add(_norm_raw(p))

    return refs, reads, writes


def build_graph():
    nodes = {}   # id -> {type, path}
    edges = []   # {src, dst, kind}
    edge_set = set()

    def add_node(nid, ntype, path=None):
        if nid not in nodes:
            nodes[nid] = {"id": nid, "type": ntype, "path": path or nid}
        return nid

    def add_edge(src, dst, kind):
        if src == dst or not src or not dst:
            return
        key = (src, dst, kind)
        if key in edge_set:
            return
        edge_set.add(key)
        edges.append({"src": src, "dst": dst, "kind": kind})

    # 1. MD files -> nodes
    md_files = collect_md_files()
    for p in md_files:
        add_node(rel(p), "doc")

    # 2. Scripts + SKILL.md -> nodes
    script_files = collect_scripts()
    for p in script_files:
        ntype = "skill" if p.name == "SKILL.md" else "script"
        add_node(rel(p), ntype)

    # 3. Registry -> nodes registry:<id> + edges generates/cross_check
    registry = {}
    if REGISTRY_PATH.exists():
        try:
            registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8")) or {}
        except Exception as e:
            print(f"[warn] doc registry loi: {e}", file=sys.stderr)
    reg_entries = registry.get("knowledge", registry.get("entries", []))
    if isinstance(reg_entries, dict):
        reg_entries = list(reg_entries.values())
    id_to_path = {}
    for e in reg_entries or []:
        if not isinstance(e, dict) or "id" not in e:
            continue
        rid = e["id"]
        rnode = add_node(f"registry:{rid}", "registry_entry")
        id_to_path[rid] = e.get("path")
        if e.get("path"):
            tgt = norm_node_id(str(e["path"]))
            add_node(tgt, "artifact")
            add_edge(rnode, tgt, "registers")
        gen = e.get("generator_script")
        if gen and gen != "manual_authoring" and (BASE_DIR / gen).exists():
            add_node(gen, "script")
            if e.get("path"):
                add_edge(gen, norm_node_id(str(e["path"])), "generates")
        for cc in e.get("cross_check_with") or []:
            cc_node = f"registry:{cc}"
            add_node(cc_node, "registry_entry")
            add_edge(rnode, cc_node, "cross_check")

    # 4. FAST_ROUTING_INDEX -> routes_to edges (reuse parser cua route.py)
    sys.path.insert(0, str(BASE_DIR / "scripts"))
    try:
        import route as route_mod
        for r in route_mod.parse_routes():
            intent_node = add_node(f"intent:{r['intent'][:80]}", "intent")
            for t in r["targets"]:
                tnorm = t.replace("skill:", "")
                if t.startswith("skill:"):
                    cand = BASE_DIR / ".agents" / "skills" / tnorm / "SKILL.md"
                    dst = rel(cand) if cand.exists() else f"skill:{tnorm}"
                else:
                    dst = norm_node_id(t.split("://")[-1])
                    if not (BASE_DIR / dst).exists() and not dst.startswith(("http", "/")):
                        dst = t  # giu nguyen dang text
                add_edge(intent_node, dst, "routes_to")
    except Exception as e:
        print(f"[warn] parse routing loi: {e}", file=sys.stderr)

    # 5. Markdown links: doc -> doc/artifact
    for p in md_files:
        src = rel(p)
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for m in FILE_URI_RE.finditer(text):
            tgt = m.group(1).replace("file://", "")
            if "<" in tgt or "*" in tgt:
                continue
            # file:/// tra ve absolute path -> chuan hoa ve relative trong repo
            try:
                tgt = str(Path(tgt).resolve().relative_to(BASE_DIR))
            except (ValueError, OSError):
                continue
            tnorm = norm_node_id(tgt)
            if (BASE_DIR / tnorm).exists():
                add_node(tnorm, "doc" if tnorm.endswith(".md") else "artifact")
                add_edge(src, tnorm, "links_to")
        for m in MD_LINK_RE.finditer(text):
            href = m.group(1)
            if href.startswith(("http", "#", "mailto")):
                continue
            target = (p.parent / href.split("#")[0]).resolve()
            try:
                tnorm = str(target.relative_to(BASE_DIR))
            except ValueError:
                continue
            if target.exists() and target.suffix == ".md":
                add_edge(src, tnorm, "links_to")

    # 6. Path literals: scripts -> extract_script_io (refs+reads+writes);
    #    docs -> chi references don gian
    for p in script_files:
        src = rel(p)
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        refs, reads, writes = extract_script_io(text)
        for raw in refs | reads | writes:
            ntype = "artifact"
            if raw.endswith(".md"):
                ntype = "doc"
            elif raw.endswith(".py"):
                ntype = "script"
            add_node(raw, ntype)
            add_edge(src, raw, "references")
        for raw in reads:
            add_edge(src, raw, "io_read")
        for raw in writes:
            add_edge(src, raw, "io_write")

    for p in md_files:
        src = rel(p)
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for m in PATH_LITERAL_RE.finditer(text):
            raw = m.group(1).rstrip("/.")
            if any(ch in raw for ch in "<*()"):
                continue
            if (BASE_DIR / raw).exists():
                add_node(raw, "doc" if raw.endswith(".md") else "artifact")
                add_edge(src, raw, "references")

    graph = {
        "schema_version": 1,
        "generated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "meta": {
            "note": "io_read/io_write la heuristic line-level; generates la SSOT tu registry",
            "node_count": len(nodes),
            "edge_count": len(edges),
        },
        "nodes": sorted(nodes.values(), key=lambda n: n["id"]),
        "edges": edges,
    }
    return graph


def load_graph():
    if not GRAPH_PATH.exists():
        sys.exit(f"Chua co graph - chay: ./.venv/bin/python scripts/build_knowledge_graph.py")
    return json.loads(GRAPH_PATH.read_text(encoding="utf-8"))


def neighbors(graph, node_id, direction="both"):
    out = []
    for e in graph["edges"]:
        if direction in ("both", "out") and e["src"] == node_id:
            out.append((e["kind"], e["dst"]))
        if direction in ("both", "in") and e["dst"] == node_id:
            out.append(("<-" + e["kind"], e["src"]))
    return out


def find_nodes(graph, query):
    q = query.lower()
    return [n["id"] for n in graph["nodes"] if q in n["id"].lower()]


def bfs(graph, src, dst):
    adj = defaultdict(list)
    for e in graph["edges"]:
        adj[e["src"]].append((e["dst"], e["kind"]))
        adj[e["dst"]].append((e["src"], "<" + e["kind"]))
    prev = {src: None}
    dq = deque([src])
    while dq:
        cur = dq.popleft()
        if cur == dst:
            break
        for nxt, kind in adj.get(cur, []):
            if nxt not in prev:
                prev[nxt] = (cur, kind)
                dq.append(nxt)
    if dst not in prev:
        return None
    path = []
    cur = dst
    while cur is not None:
        path.append(cur)
        cur = prev[cur][0] if prev[cur] else None
    return list(reversed(path))


def main():
    ap = argparse.ArgumentParser(description="Build/query knowledge graph")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--node", help="Node id (substring match)")
    ap.add_argument("--produces", help="Ai generate/write X (in-edges generates/io_write)")
    ap.add_argument("--consumes", help="X doc/ghi gi (out-edges io_read/io_write/references)")
    ap.add_argument("--path", nargs=2, metavar=("A", "B"), help="Shortest path A -> B")
    ap.add_argument("--rebuild", action="store_true", help="Build lai graph truoc khi query")
    args = ap.parse_args()

    if args.rebuild or not GRAPH_PATH.exists() or args.stats:
        graph = build_graph()
        GRAPH_PATH.parent.mkdir(parents=True, exist_ok=True)
        GRAPH_PATH.write_text(json.dumps(graph, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"Da ghi {GRAPH_PATH}: {graph['meta']['node_count']} nodes, {graph['meta']['edge_count']} edges")
        if args.stats or not (args.node or args.produces or args.consumes or args.path):
            from collections import Counter
            kinds = Counter(e["kind"] for e in graph["edges"])
            types = Counter(n["type"] for n in graph["nodes"])
            print("Edge kinds:", dict(kinds))
            print("Node types:", dict(types))
            return
    else:
        graph = load_graph()

    if args.node:
        matches = find_nodes(graph, args.node)
        if not matches:
            sys.exit(f"Khong tim thay node nao match {args.node!r}")
        nid = matches[0]
        if len(matches) > 1:
            print(f"Nhieu match, lay dau tien: {nid} ({len(matches)} matches)")
        n = next(x for x in graph["nodes"] if x["id"] == nid)
        print(f"NODE {n['id']}  [{n['type']}]")
        for kind, other in neighbors(graph, nid):
            print(f"  {kind:>14}  {other}")
        return

    if args.produces:
        matches = [n["id"] for n in graph["nodes"] if args.produces.lower() in n["id"].lower()]
        targets = set(matches)
        hits = [(e["kind"], e["src"]) for e in graph["edges"]
                if e["dst"] in targets and e["kind"] in ("generates", "io_write", "registers")]
        if not hits:
            print(f"Khong ai produces {args.produces!r}")
        for kind, src in sorted(set(hits)):
            print(f"  {kind:>10}  {src}")
        return

    if args.consumes:
        matches = [n["id"] for n in graph["nodes"] if args.consumes.lower() in n["id"].lower()]
        sources = set(matches)
        hits = [(e["kind"], e["dst"]) for e in graph["edges"]
                if e["src"] in sources and e["kind"] in ("io_read", "io_write", "references", "routes_to")]
        if not hits:
            print(f"Khong co consume nao tu {args.consumes!r}")
        for kind, dst in sorted(set(hits))[:60]:
            print(f"  {kind:>10}  {dst}")
        return

    if args.path:
        a, b = args.path
        ma, mb = find_nodes(graph, a), find_nodes(graph, b)
        if not ma or not mb:
            sys.exit(f"Khong tim thay node: {a if not ma else b}")
        path = bfs(graph, ma[0], mb[0])
        if not path:
            print(f"Khong co duong di {ma[0]} -> {mb[0]}")
        else:
            print(f"Path ({len(path)-1} hops):")
            for i, n in enumerate(path):
                print(f"  {'->' if i else '  '}{n}")
        return


if __name__ == "__main__":
    main()
