#!/usr/bin/env python3
"""
Pre-commit guard: quet staged diff tim secret/credential bi lo vao git.

Usage:
    ./.venv/bin/python scripts/guard_secrets.py          # quet git diff --cached
    ./.venv/bin/python scripts/guard_secrets.py --staged # tuong duong (mac dinh)

Exit 1 neu phat hien pattern credential that (private key, OAuth token,
API key). Khong quet file binary. Bo qua file trong .gitignore van an toan
vi chung khong bao gio vao staged diff.
"""

import re
import subprocess
import sys

# (ten, regex) - chi bat credential vat ly, tranh false positive tren docs
PATTERNS = [
    ("RSA/EC/OPENSSH PRIVATE KEY", re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----")),
    ("Google OAuth access token", re.compile(r"ya29\.[A-Za-z0-9_\-]{20,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z_\-]{35}")),
    ("Slack token", re.compile(r"xox[baprs]-[0-9A-Za-z\-]{10,}")),
    ("refresh_token value", re.compile(r'"refresh_token"\s*:\s*"[0-9A-Za-z_\-\.]{20,}"')),
    ("client_secret value", re.compile(r'"client_secret"\s*:\s*"[0-9A-Za-z_\-\.]{20,}"')),
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("GitHub token", re.compile(r"gh[pousr]_[0-9A-Za-z]{36,}")),
]

# Cho phep nhung chuoi nay (placeholder/example trong docs)
ALLOWLIST = [
    "YOUR_", "your-", "example", "xxx", "<", "REDACTED", "placeholder",
]


def get_staged_diff() -> str:
    res = subprocess.run(
        ["git", "diff", "--cached", "-U0", "--diff-filter=ACMR"],
        capture_output=True, text=True,
    )
    return res.stdout or ""


def scan(diff_text: str):
    findings = []
    current_file = None
    for line in diff_text.splitlines():
        if line.startswith("+++ b/"):
            current_file = line[6:]
            continue
        if not line.startswith("+") or line.startswith("+++"):
            continue
        content = line[1:]
        if any(a in content for a in ALLOWLIST):
            continue
        for name, pat in PATTERNS:
            if pat.search(content):
                # mask gia tri trong log, khong in secret ra output
                masked = pat.sub(lambda m: m.group(0)[:6] + "...***", content.strip())
                findings.append((current_file, name, masked[:120]))
                break
    return findings


def main() -> int:
    findings = scan(get_staged_diff())
    if not findings:
        return 0
    print("[GUARD-SECRETS] Phat hien credential/secret trong staged diff:")
    seen = set()
    for f, name, snippet in findings:
        key = (f, name)
        if key in seen:
            continue
        seen.add(key)
        print(f"  - {f}: {name} -> {snippet}")
    print("\nBo sung file vao .gitignore hoac go secret khoi diff truoc khi commit.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
