#!/data/data/com.termux/files/usr/bin/bash
# Project Eden — Termux bootstrap
# Safe to re-run. Does not download model weights.

set -euo pipefail

echo "== Project Eden Termux bootstrap =="

pkg update -y
pkg install -y git python clang make cmake wget

python -m pip install --upgrade pip

ROOT="$(cd "$(dirname "$0")/.." 2>/dev/null && pwd || pwd)"
if [ -f "$ROOT/pyproject.toml" ]; then
  python -m pip install -e "$ROOT"
else
  echo "Clone the repo first, then rerun this script from inside it."
fi

mkdir -p "$HOME/models"
echo
echo "Next:"
echo "  1. Put a Q4_K_M GGUF in ~/models"
echo "  2. Build or install llama.cpp for your device"
echo "  3. eden stack --preset phone-8gb"
echo
echo "Weights are not bundled. See docs/models.md"
