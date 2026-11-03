#!/usr/bin/env python3
"""Validate a changed-files allowlist for one FW task. Not a cross-PR lock.

Use: python3 scripts/check_task_manifest.py --changed-files-file /tmp/changed.txt
The file lists one path per line from a PR diff, relative to repository root.
"""
import argparse
import json
from pathlib import Path
import re
import sys

PREFIXES_REQUIRING_CONTRACT = ("services/", "apps/", "jurisdictions/", "contracts/", "infrastructure/")
TASK_PREFIX = "coordination/tasks/"
BRANCH_RE = re.compile(r"^(?:feat|fix|docs|chore)/FW-[0-9]{3}-[a-z0-9][a-z0-9-]*$")
SHA_RE = re.compile(r"^[a-f0-9]{40}$")
ISSUE_RE = re.compile(r"^FW-[0-9]{3}$")
AGENT_ID_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


def relative_path(path):
    """Return validated POSIX repo path or raise ValueError."""
    if not isinstance(path, str) or not path or "\\" in path or path.startswith("/"):
        raise ValueError("invalid path / ruta inválida")
    parts = path.split("/")
    if any(x in ("", ".", "..") for x in (parts[:-1] if path.endswith("/") else parts)):
        raise ValueError("invalid path traversal / ruta insegura")
    if path.endswith("/") and not path[:-1]:
        raise ValueError("empty directory / carpeta vacía")
    return path


def allows(allowed, changed):
    return any(changed == p or (p.endswith("/") and changed.startswith(p)) for p in allowed)


def validate_task(task, paths):
    errors = []
    issue, agent, branch, base = (task.get(k) for k in ("issue", "agent", "branch", "base_sha"))
    if not isinstance(issue, str) or not ISSUE_RE.fullmatch(issue):
        errors.append("issue must be FW-XXX / ID inválido")
    if not isinstance(agent, str) or len(agent) > 64 or not AGENT_ID_RE.fullmatch(agent):
        errors.append("agent must be a safe provider slug / identificador de agente inválido")
    if not isinstance(branch, str) or not BRANCH_RE.fullmatch(branch):
        errors.append("branch naming invalid / rama inválida")
    if isinstance(issue, str) and isinstance(branch, str) and issue not in branch:
        errors.append("branch not linked to issue / rama sin ID")
    if not isinstance(base, str) or not SHA_RE.fullmatch(base) or base == "0"*40:
        errors.append("base_sha must be real 40-char SHA / SHA real requerido")
    allowed = task.get("allowed_paths")
    if not isinstance(allowed, list) or not allowed or not all(isinstance(p, str) for p in allowed):
        errors.append("nonempty allowed_paths required / rutas requeridas")
        allowed = []
    for p in allowed:
        try:
            relative_path(p)
        except ValueError:
            errors.append("unsafe allowed path: " + p)
    if len(set(allowed)) != len(allowed):
        errors.append("duplicated allowed paths / rutas duplicadas")
    for changed in paths:
        try:
            relative_path(changed)
        except ValueError:
            errors.append("unsafe changed path: " + changed)
            continue
        if changed.startswith(TASK_PREFIX) and changed == TASK_PREFIX + str(issue) + ".json":
            continue
        if not allows(allowed, changed):
            errors.append("undeclared changed path / ruta no autorizada: " + changed)
    return errors


def check_paths(paths, root):
    app_changed = any(p.startswith(PREFIXES_REQUIRING_CONTRACT) for p in paths)
    manifest_paths = [p for p in paths if p.startswith(TASK_PREFIX) and p.endswith(".json")]
    if not app_changed and not manifest_paths:
        return []
    if len(manifest_paths) != 1:
        return ["exactly one modified FW task manifest required for application changes"]
    name = manifest_paths[0]
    if not ISSUE_RE.fullmatch(Path(name).stem):
        return ["invalid FW task filename: " + name]
    f = root / name
    try:
        task = json.loads(f.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"manifest unreadable / JSON inválido: {exc}"]
    if not isinstance(task, dict):
        return ["manifest must be an object / objeto JSON requerido"]
    if task.get("issue") != f.stem:
        return ["manifest filename/issue mismatch / ID no coincide"]
    return validate_task(task, paths)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--changed-files-file", required=True)
    p.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[1]))
    args = p.parse_args()
    root = Path(args.repo_root)
    paths = [x.strip() for x in Path(args.changed_files_file).read_text(encoding="utf-8").splitlines() if x.strip()]
    errors = check_paths(paths, root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Task scope validation passed / Alcance de tarea validado")
    return 0


if __name__ == "__main__":
    sys.exit(main())
