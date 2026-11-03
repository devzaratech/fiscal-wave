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
done
echo "Rendered ${#files[@]} Mermaid diagrams using real Chromium."
