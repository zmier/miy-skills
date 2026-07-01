#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: render-mermaid-chrome.sh INPUT.mmd OUTPUT.png [width] [height] [scale]" >&2
  exit 2
fi

input="$1"
output="$2"
width="${3:-24000}"
height="${4:-1800}"
scale="${5:-2}"

npx --yes @mermaid-js/mermaid-cli \
  -i "$input" \
  -o "$output" \
  -b white \
  -w "$width" \
  -H "$height" \
  --scale "$scale"
