#!/usr/bin/env bash
# Thin wrapper so device benchmark PRs use the same flags.
# Requires llama-cli on PATH.

set -euo pipefail

MODEL="${1:-}"
if [ -z "$MODEL" ]; then
  echo "Usage: $0 /path/to/model.gguf"
  exit 1
fi

if ! command -v llama-cli >/dev/null 2>&1; then
  echo "llama-cli not on PATH. Install llama.cpp first."
  exit 1
fi

echo "device : $(uname -a)"
echo "model  : $MODEL"
echo

llama-cli -m "$MODEL" -p "Say only: ready" -n 16 -ngl 0 --no-display-prompt
