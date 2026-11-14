#!/bin/bash
# Render every src/*.dot to img/*.png (slides, 200 dpi) and img/*.svg.
# The line //COMMON in each .dot is replaced with the shared style in src/common.inc.
set -e
cd "$(dirname "$0")"
for f in src/*.dot; do
  b=$(basename "$f" .dot)
  sed -e "/\/\/COMMON/r src/common.inc" -e "/\/\/COMMON/d" "$f" | dot -Tpng -Gdpi=200 -o "img/$b.png"
  sed -e "/\/\/COMMON/r src/common.inc" -e "/\/\/COMMON/d" "$f" | dot -Tsvg -o "img/$b.svg"
done
