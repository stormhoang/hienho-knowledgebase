#!/usr/bin/env bash
# Cai dat git hooks cho repo. Chay 1 lan: bash scripts/git-hooks/install.sh
set -e
HOOK_DIR="$(git rev-parse --git-path hooks)"
cp "$(dirname "$0")/pre-commit" "$HOOK_DIR/pre-commit"
chmod +x "$HOOK_DIR/pre-commit"
echo "Da cai dat pre-commit hook vao $HOOK_DIR/pre-commit"
