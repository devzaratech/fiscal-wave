#!/usr/bin/env bash
# Rebuild tracked SVG and Mermaid views; never writes to Git or network.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
python3 scripts/diagrams.py --write
if ! command -v plantuml >/dev/null 2>&1; then
  echo 'Install PlantUML + Graphviz before rendering SVG (on Ubuntu: apt install plantuml graphviz).' >&2
  exit 1
fi
mkdir -p docs/architecture/rendered
# This directory contains generated assets only; drop stale files on rename/removal.
find docs/architecture/rendered -maxdepth 1 -type f -name "*.svg" -delete
shopt -s nullglob
sources=(docs/architecture/*.puml)
if (( ${#sources[@]} == 0 )); then
  echo 'No PlantUML sources found' >&2; exit 1
fi
for source in "${sources[@]}"; do
  plantuml -checkonly "$source"
done
plantuml -tsvg -o "$ROOT/docs/architecture/rendered" "${sources[@]}"
for source in "${sources[@]}"; do
  stem="$(basename "$source" .puml)"
  test -s "docs/architecture/rendered/$stem.svg" || { echo "Missing SVG: $stem" >&2; exit 1; }
done
echo "Rendered ${#sources[@]} SVG diagrams / Diagramas SVG generados"
