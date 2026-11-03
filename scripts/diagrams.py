#!/usr/bin/env python3
"""Generate a GitHub gallery of canonical PlantUML sources and rendered SVGs.

There is intentionally no diagram-language conversion: edit .puml and regenerate
its .svg. The SVGs are checked into Git for normal GitHub previews.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "architecture"
GALLERY = SOURCE / "diagrams.md"
LABELS = {
    "system-map": "System map / Mapa del sistema",
    "dte-lifecycle": "DTE lifecycle / Ciclo de vida DTE",
    "idempotency-sequence": "Idempotent issuance / Emisión idempotente",
    "aws-lab": "Temporary AWS lab / Laboratorio AWS temporal",
    "sii-signing-and-pdf": "SII signing and PDF / Firma SII y PDF",
    "privacy-boundaries": "Personal-data boundaries / Límites de datos personales",
}


def gallery(stems: list[str]) -> str:
    parts = [
        "# FiscalWave diagrams / Diagramas",
        "",
        "**EN:** Architecture proposals only, not running services or SII authorization. "
        "PlantUML (`.puml`) is the sole source of truth; the SVG images are generated from it.",
        "",
        "**ES:** Solo propuestas de arquitectura, no servicios operativos ni autorización del SII. "
        "PlantUML (`.puml`) es la única fuente de verdad; los SVG se generan desde esos archivos.",
        "",
        "To regenerate / Para regenerar: `bash scripts/render-diagrams.sh` "
        "(PlantUML + Graphviz required). CI validates syntax and checks the generated images.",
        "",
        "All SVGs have an opaque white background and dark labels for reliable viewing "
        "in light and dark GitHub themes. / Los SVG usan fondo blanco opaco y texto oscuro.",
        "",
    ]
    for stem in stems:
        title = LABELS.get(stem, stem)
        parts += [
            f"## {title}",
            "",
            f"[PlantUML source / Código PlantUML]({stem}.puml) · "
            f"[SVG](rendered/{stem}.svg)",
            "",
            f"![{title}](rendered/{stem}.svg)",
            "",
        ]
    return "\n".join(parts).rstrip() + "\n"


def run(check: bool) -> int:
    sources = sorted(SOURCE.glob("*.puml"))
    if not sources:
        raise ValueError("No PlantUML diagrams found")
    text = gallery([p.stem for p in sources])
    if check:
        if not GALLERY.is_file() or GALLERY.read_text(encoding="utf-8") != text:
            print(f"Stale or missing gallery: {GALLERY.relative_to(ROOT)}", file=sys.stderr)
            return 1
    else:
        GALLERY.write_text(text, encoding="utf-8")
    print(f"{'Verified' if check else 'Generated'} SVG gallery for {len(sources)} PlantUML diagrams")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    options = parser.parse_args()
    try:
        sys.exit(run(check=options.check))
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
