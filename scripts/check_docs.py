#!/usr/bin/env python3
"""Minimal offline documentation structure checks (not PlantUML rendering)."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
required = [
    "README.md", "README.es.md", "AGENTS.md", "CONTRIBUTING.md",
    "docs/en/vision.md", "docs/es/vision.md",
    "docs/en/architecture.md", "docs/es/architecture.md",
    "docs/en/roadmap.md", "docs/es/roadmap.md",
    "docs/en/engineering-standards.md", "docs/es/engineering-standards.md",
    "docs/architecture/pattern-catalog.md",
    "docs/architecture/idempotency-contract.md",
    "CLAUDE.md", "docs/planning/MULTI_AGENT.md",
    "docs/privacy/README.md", "docs/privacy/CHILE-21719.md",
    "docs/privacy/DATA-INVENTORY.md", "docs/privacy/DSAR-RETENTION.md",
    "docs/privacy/INCIDENT-RUNBOOK.md", "docs/privacy/RELEASE-GATES.md",
    "docs/adr/0010-country-repository-strategy.md",
    "docs/adr/0011-privacy-by-design.md",
    "coordination/README.md", "coordination/examples/FW-000.example.json",
    "scripts/check_task_manifest.py", "scripts/tests/test_task_manifest.py",
    ".claude/agents/fiscalwave-reviewer.md",
    ".opencode/agents/fiscalwave-reviewer.md",
    "docs/planning/DATA-PLATFORMS.md",
    "docs/planning/SII-DTE-LIFECYCLE.md",
    "docs/planning/PROVIDER-CAPABILITIES.md",
    "docs/adr/0008-polyglot-persistence.md",
    "docs/adr/0009-credential-custody-and-signing.md",
    "docs/adr/0006-engineering-standards.md",
    "docs/planning/README.md", "docs/planning/BACKLOG.md",
    "docs/planning/MILESTONES.md", "docs/planning/SCRUM.md",
    "docs/planning/QUALITY.md", "docs/planning/INTERVIEWS.md",
    "docs/planning/FINOPS.md", "docs/planning/COMPLIANCE.md",
    "docs/planning/I18N.md", "docs/planning/EMPLOYABILITY.md",
    "agents/README.md", "practice/README.md",
    "docs/planning/TODO.md", "docs/planning/THREAT_MODEL.md",
    "docs/architecture/system-map.puml",
    "docs/architecture/dte-lifecycle.puml", "docs/architecture/aws-lab.puml",
    "docs/architecture/idempotency-sequence.puml",
    "docs/architecture/sii-signing-and-pdf.puml",
]
errors = []
for name in required:
    if not (root / name).is_file():
        errors.append(f"Missing required file: {name}")
for path in root.rglob("*.puml"):
    text = path.read_text(encoding="utf-8")
    if text.count("@startuml") != 1 or text.count("@enduml") != 1:
        errors.append(f"Unbalanced PlantUML markers: {path.relative_to(root)}")
    if re.search(r"!include\s+https?://", text):
        errors.append(f"Remote includes not permitted: {path.relative_to(root)}")
for path in root.rglob("*.md"):
    if ".git" in path.parts:
        continue
    source = path.read_text(encoding="utf-8")
    for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^\)]+)\)", source):
        target = target.strip().split(" ")[0].strip("<>")
        if target.startswith(("http:", "https:", "mailto:", "#")):
            continue
        if not target:
            continue
        dest = unquote(target.split("#")[0])
        if not dest:
            continue
        if not (path.parent / dest).exists():
            errors.append(f"Broken local link in {path.relative_to(root)}: {target}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("Documentation structure checks passed / Estructura documental OK")
