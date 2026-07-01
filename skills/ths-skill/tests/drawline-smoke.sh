#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHILD="$ROOT/skills/ths-drawline-annotation"

python3 -m py_compile \
  "$CHILD/scripts/write_drawline_annotation.py" \
  "$CHILD/scripts/manage_drawline_annotations.py"

"$CHILD/scripts/write_drawline_annotation.py" \
  --kind text \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384 \
  --date 20251028 \
  --price 40.22 \
  --open-price 31.20 \
  --text "SMOKE_TEXT" >/dev/null

"$CHILD/scripts/write_drawline_annotation.py" \
  --kind rect \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384 \
  --date 20260212 \
  --price 32.16 \
  --open-price 32.00 \
  --end-date 20260427 \
  --end-price 51.91 \
  --end-open-price 47.83 \
  --end-xdata 45 >/dev/null

set +e
"$CHILD/scripts/write_drawline_annotation.py" \
  --kind note \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384 \
  --anchor-date 20260622 \
  --anchor-price 195.55 \
  --anchor-open-price 195.55 \
  --box-date 20260526 \
  --box-price 193.99 \
  --box-open-price 92.00 \
  --text "MISSING_XDATA_SHOULD_FAIL" >/tmp/ths-drawline-smoke.err 2>&1
status=$?
set -e

if [[ "$status" -eq 0 ]]; then
  echo "expected missing box-xdata failure"
  exit 1
fi

grep -q "second_xdata_required_for_cross_date_shape" /tmp/ths-drawline-smoke.err
echo "drawline smoke ok"
