#!/usr/bin/env python3
"""Derive Mermaid views and GitHub gallery from supported canonical PlantUML.

Strict fail-closed conversion: unsupported source constructs are rejected rather
than silently omitted. Visual/layout equivalence still needs human review.
"""
from __future__ import annotations
import argparse
import re
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
DECL = re.compile(
    r'^(actor|participant|cloud|node|rectangle|component|database|queue|folder|package)'
    r'(?:\s+"((?:[^"\\]|\\.)*)"(?:\s+as\s+(\w+))?|\s+(\w+))'
    r'(\s*\{)?$')
EDGE = re.compile(r'^(\w+)\s+(-->|->|\.\.)\s+(\w+)(?:\s*:\s*(.*))?$')
NOTE = re.compile(r'^note\s+(bottom|right|left|top|over)(?:\s+of\s+(\w+)|\s+(\w+))?$')
IGNORED = ("skinparam ", "title ")
# Mermaid theming must be explicit: GitHub dark mode otherwise blends diagrams
# with its dark canvas even when PlantUML exports have an opaque white SVG.
MERMAID_LIGHT = '%%{init: {"theme":"base","themeVariables":{"background":"#FFFFFF","darkMode":false,"primaryColor":"#FFFFFF","primaryTextColor":"#111111","primaryBorderColor":"#334155","secondaryColor":"#F1F5F9","tertiaryColor":"#FFFFFF","lineColor":"#475569","textColor":"#111111","actorBkg":"#FFFFFF","actorTextColor":"#111111"},"themeCSS":"svg { background-color: #FFFFFF !important; }"}}%%'

class DiagramError(ValueError):
    pass

def clean(text: str) -> str:
    return (text.replace("\\n", "<br/>").replace('"', "&quot;")
            .replace("|", "&#124;").replace("[", "&#91;").replace("]", "&#93;"))

def sequence_text(text: str) -> str:
    # Mermaid sequence grammar treats semicolons as statement separators.
    # Escape *before* adding HTML entity references in clean().
    return clean(text.replace(";", "#59;"))

def source_lines(path: Path) -> list[tuple[int, str]]:
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    if not lines or lines[0] != "@startuml" or lines[-1] != "@enduml":
        raise DiagramError(f"{path.name}: expected one complete PlantUML block")
    return [(i, line) for i, line in enumerate(lines[1:-1], 2) if line]

def convert(path: Path) -> str:
    lines = source_lines(path)
    is_sequence = any(line.startswith("participant ") or line == "autonumber" for _, line in lines)
    output = [f"%% Generated from {path.name}; edit the PlantUML source, not this file.",
              MERMAID_LIGHT,
              "sequenceDiagram" if is_sequence else ("flowchart LR" if any(line == "left to right direction" for _, line in lines) else "flowchart TD")]
    group_stack: list[str] = []
    i = note_count = group_count = 0
    while i < len(lines):
        line_number, line = lines[i]
        i += 1
        if line.startswith(IGNORED) or line == "left to right direction":
            continue
        if line == "autonumber" and is_sequence:
            output.append("    autonumber")
            continue
        if line == "}" and not is_sequence:
            if not group_stack:
                raise DiagramError(f"{path.name}:{line_number}: unexpected group close")
            group_stack.pop()
            output.append("    end")
            continue
        match = DECL.fullmatch(line)
        if match:
            kind, quoted, alias, unquoted, opens = match.groups()
            name = alias or unquoted
            label = quoted if quoted is not None else unquoted
            if is_sequence:
                if opens:
                    raise DiagramError(f"{path.name}:{line_number}: sequence group unsupported")
                prefix = "actor" if kind == "actor" else "participant"
                if name is None:
                    raise DiagramError(f"{path.name}:{line_number}: missing sequence alias")
                output.append(f"    {prefix} {name} as {clean(label)}")
            else:
                if opens:
                    group_count += 1
                    group_name = f"group_{group_count}"
                    output.append(f'    subgraph {group_name}["{clean(label)}"]')
                    group_stack.append(group_name)
                    if name:
                        output.append(f'        {name}["{clean(label)}"]')
                else:
                    if not name:
                        raise DiagramError(f"{path.name}:{line_number}: missing flowchart alias")
                    shape = f'{name}[("{clean(label)}")]' if kind == "database" else f'{name}["{clean(label)}"]'
                    output.append("    " + shape)
            continue
        note_match = NOTE.fullmatch(line)
        if note_match:
            side, target1, target2 = note_match.groups()
            target = target1 or target2
            note_lines = []
            while i < len(lines) and lines[i][1] != "end note":
                note_lines.append(lines[i][1])
                i += 1
            if i == len(lines):
                raise DiagramError(f"{path.name}:{line_number}: unclosed note")
            i += 1
            message = clean(" ".join(note_lines))
            if is_sequence:
                if not target:
                    raise DiagramError(f"{path.name}:{line_number}: unanchored sequence note")
                location = "over" if side == "over" else "left of" if side == "left" else "right of"
                output.append(f"    Note {location} {target}: {sequence_text(' '.join(note_lines))}")
            else:
                note_count += 1
                note_id = f"note_{note_count}"
                output.append(f'    {note_id}["Note: {message}"]')
                if target:
                    output.append(f"    {target} -.-> {note_id}")
            continue
        if is_sequence and (line.startswith("alt ") or line.startswith("else ") or line == "end"):
            if line != "end":
                keyword, caption = line.split(" ", 1)
                output.append(f"    {keyword} {sequence_text(caption)}")
            else:
                output.append("    end")
            continue
        edge = EDGE.fullmatch(line)
        if edge:
            start, arrow, end, label = edge.groups()
            if is_sequence:
                if arrow == "..":
                    raise DiagramError(f"{path.name}:{line_number}: dotted sequence edge unsupported")
                output.append(f"    {start}{'-->>' if arrow == '-->' else '->>'}{end}: {sequence_text(label or '')}")
            else:
                arrow = "-.-" if arrow == ".." else "-->"
                output.append(f"    {start} {arrow}{'|' + clean(label) + '|' if label else ''} {end}")
            continue
        raise DiagramError(f"{path.name}:{line_number}: unsupported PlantUML: {line}")
    if group_stack:
        raise DiagramError(f"{path.name}: unclosed group")
    return "\n".join(output) + "\n"

def gallery(diagrams: dict[str, str]) -> str:
    parts = [
        "# FiscalWave diagrams / Diagramas", "",
        "**EN:** Proposed architecture only, not implemented services or SII authorization. "
        "PlantUML (`.puml`) is the source of truth. SVGs and supported Mermaid views are derived.", "",
        "**ES:** Arquitectura propuesta, no servicios implementados ni autorización del SII. "
        "PlantUML (`.puml`) es la fuente de verdad. SVG y Mermaid son vistas derivadas.", "",
        "Generate / Generar from the repository root: `bash scripts/render-diagrams.sh`. "
        "CI validates both rendered SVG and deterministic Mermaid output.", "",
        "Conversion is strict and limited to the PlantUML constructs in this repository. "
        "Unsupported syntax fails CI rather than producing an incomplete diagram. "
        "Mermaid may use simplified shapes/layout, and visual equivalence still requires human review. "
        "Native previews request an explicit light palette and white background; GitHub still controls its embedded viewer. "
        "CI renders every Mermaid in Chromium to catch parser and render errors.", "",
    ]
    for stem, mermaid in diagrams.items():
        title = LABELS.get(stem, stem)
        parts += [
            f"## {title}", "",
            f"[PlantUML source]({stem}.puml) · [Mermaid source](mermaid/{stem}.mmd) · "
            f"[PlantUML SVG](rendered/{stem}.svg) · [Mermaid SVG](rendered/mermaid/{stem}.svg)", "",
            f"![{title}](rendered/{stem}.svg)", "",
            "<details>", "<summary>Mermaid — white SVG preview and editable source / vista clara y código</summary>", "",
            f"![{title} — Mermaid](rendered/mermaid/{stem}.svg)", "",
            "```mermaid", mermaid.rstrip(), "```", "", "</details>", "",
        ]
    return "\n".join(parts).rstrip() + "\n"

def run(check: bool) -> int:
    paths = sorted(SOURCE.glob("*.puml"))
    if not paths:
        raise DiagramError("No PlantUML sources")
    diagrams = {p.stem: convert(p) for p in paths}
    outputs = {SOURCE / "mermaid" / f"{stem}.mmd": content for stem, content in diagrams.items()}
    outputs[GALLERY] = gallery(diagrams)
    stale = []
    for dest, contents in outputs.items():
        if check:
            if not dest.exists() or dest.read_text(encoding="utf-8") != contents:
                stale.append(dest.relative_to(ROOT).as_posix())
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(contents, encoding="utf-8")
    extra = set((SOURCE / "mermaid").glob("*.mmd")) - set(outputs)
    if extra and check:
        stale += [p.relative_to(ROOT).as_posix() for p in sorted(extra)]
    elif extra:
        for p in sorted(extra):
            p.unlink()
    if stale:
        print("Stale/extra generated documents: " + ", ".join(stale), file=sys.stderr)
        return 1
    print(f"{'Verified' if check else 'Generated'} {len(diagrams)} Mermaid diagrams and gallery")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        sys.exit(run(args.check))
    except (DiagramError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
