#!/usr/bin/env bash
# Typical spans a splicer actually punches into a calculator.

set -euo pipefail
export PYTHONPATH="${PYTHONPATH:-}:$(cd "$(dirname "$0")/../src" && pwd)"

python -m eden.cli loss --km 0.4 --nm 1550 --connectors 2 --splices 2
echo "---"
python -m eden.cli loss --km 12.4 --nm 1550 --connectors 2 --splices 8
echo "---"
python -m eden.cli loss --km 24 --nm 1310 --connectors 4 --splices 12 --margin 3
