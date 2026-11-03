#!/usr/bin/env bash
# Render actual Mermaid diagrams in Chromium; a Python text check is not enough.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
: "${MERMAID_CLI:?Set MERMAID_CLI to the installed mmdc executable}"
: "${MERMAID_PUPPETEER_CONFIG:?Set MERMAID_PUPPETEER_CONFIG to a safe browser config}"
OUT_DIR="${MERMAID_OUTPUT_DIR:-${RUNNER_TEMP:-/tmp}/fiscalwave-mermaid-validated}"
mkdir -p "$OUT_DIR"
shopt -s nullglob
files=(docs/architecture/mermaid/*.mmd)
if (( ${#files[@]} == 0 )); then
  echo "No Mermaid sources" >&2
  exit 1
fi
for src in "${files[@]}"; do
  name="$(basename "$src" .mmd)"
  echo "Validating Mermaid: $name"
  "$MERMAID_CLI" -i "$src" -o "$OUT_DIR/$name.svg" -b white -p "$MERMAID_PUPPETEER_CONFIG"
  test -s "$OUT_DIR/$name.svg"
  # Explicit white canvas: don't rely on CSS/theme selection inside GitHub.
  # Record the input digest so CI can detect stale tracked Mermaid SVG previews.
  python3 - "$src" "$OUT_DIR/$name.svg" <<'PY'
import hashlib
import re
import sys
from pathlib import Path
source, output = map(Path, sys.argv[1:])
digest = hashlib.sha256(source.read_bytes()).hexdigest()
svg = output.read_text(encoding="utf-8")
root = re.search(r"<svg\b[^>]*>", svg)
if not root:
    raise SystemExit(f"Missing SVG root in {output}")
canvas = '<rect x="0" y="0" width="100%" height="100%" fill="#FFFFFF"/>'
marker = f"<!-- fiscalwave-mermaid-sha256:{digest} -->"
svg = svg[:root.end()] + canvas + marker + svg[root.end():]
output.write_text(svg, encoding="utf-8")
PY
done
echo "Rendered ${#files[@]} Mermaid diagrams using real Chromium."
