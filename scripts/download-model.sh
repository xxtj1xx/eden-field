#!/usr/bin/env bash
# Placeholder downloader. Fill in a URL you have rights to fetch.
# Eden will not vendor a specific host so the script does not rot
# when a mirror moves.

set -euo pipefail

DEST="${EDEN_MODEL_DIR:-$HOME/models}"
mkdir -p "$DEST"

if [ "${1:-}" = "" ]; then
  echo "Usage: $0 <url> [filename]"
  echo "Example:"
  echo "  $0 https://huggingface.co/.../model.Q4_K_M.gguf"
  exit 1
fi

URL="$1"
FILE="${2:-$(basename "${URL%%\?*}")}"
OUT="$DEST/$FILE"

echo "Downloading to $OUT"
if command -v wget >/dev/null 2>&1; then
  wget -O "$OUT" "$URL"
else
  curl -L --fail -o "$OUT" "$URL"
fi

echo "Done. Point llama.cpp at $OUT"
