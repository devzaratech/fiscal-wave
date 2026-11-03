# FW-029 — Multi-agent collaboration / Colaboración entre agentes

**Status / Estado: policy and local checks implemented in this documentation branch; NOT a global GitHub lock.** [Issue FW-029](https://github.com/devzaratech/fiscal-wave/issues/14).

## Current execution model / Modo vigente
**Sequential, NOT parallel writers / Secuencial, no escritores simultáneos.** [FW-032](AI-AGENT-STRATEGY.md) supersedes any suggestion in this document that more than one writer should work at once. Separate worktrees still protect history, enable migration and allow a read-only reviewer. Cross-PR checks remain defense in depth, not a reason to enable simultaneous writes. / Un agente escritor a la vez.

## Source of truth / Fuente única
- `AGENTS.md` is canonical for **Codex, OpenCode and Claude Code**. `CLAUDE.md` imports it; OpenCode reads root `AGENTS.md`. Tool-specific reviewer profiles are **short wrappers**, not competing policies. / Las reglas no deben divergir.
- Read the current `AGENTS.md`, relevant role in `agents/`, FW issue, acceptance criteria, ADR, privacy/SII requirements, and the latest base SHA before coding. / Validar SHA y alcance.
- **Main is currently unprotected**, and GitHub reported branch rulesets unavailable for this private repository configuration as of 2026-11-03. No technical guarantee of blocked direct pushes: owner must enforce review and merges. / Restricción real, no garantía de bloqueo.

## Agent version and effective permission checks / Verificación de permisos reales
The project OpenCode reviewer uses the **stable** `permission:` map (not the distinct OpenCode V2 `permissions:` list). Before using an updated/experimental OpenCode version, confirm the loaded agent configuration and the **effective** denial of edit, shell and subagents; documentation alone is not a sandbox. Claude reviewer tool allowlist must likewise be verified in the actual installed version. For any tool without a verified read-only profile, perform the review manually from GitHub. / Verificar la versión y permisos de cada agente.


**One task / one write owner / one worktree / one branch / one PR.** / Una historia, un dueño de escritura, un worktree, una rama y un PR.

- Example branches: `feat/FW-025-pfx-vault`, `feat/FW-027-pdf417`. Start from an **approved base SHA**; do not start concurrent agent work from an unreviewed PR unless the owner explicitly approves and records dependency. / Base aprobada.
- Agents declare exact allowed directories/files in `coordination/tasks/FW-XXX.json`; a task contract must exist for PRs changing `services/`, `apps/`, `jurisdictions/`, `contracts/` or `infrastructure/`. / Declarar rutas antes de implementar.
- `contracts/`, `AGENTS.md`, `CLAUDE.md`, `.github/`, `docs/adr/`, `docs/privacy/` and other shared files require **human coordination and review**. An agent cannot infer ownership merely by touching a file. / Compartidos reservados.
- Before starting, inspect **all open PRs**, task contracts, and changed paths for overlap. GitHub Actions also queries other open PR changed files, but simultaneous drafts can race and no GitHub API check can replace a protected merge policy. / Revisar PRs concurrentes.
- If two tasks need the same contract/API, one owner edits it in a separate contract-first PR; the other rebases after approval. / Primero contrato común, luego consumidores.
- Do not `git reset --hard`, `git push --force`, `git checkout --` or clean another agent's changes; never switch a shared working directory used by another process. / Sin comandos destructivos sobre trabajo ajeno.
- If unexpected unstaged changes or unknown ownership are detected, **stop writing** and ask the human owner to reconcile. / Detener escritura ante conflicto.

## Git worktrees / Worktrees de Git
```bash
git fetch origin
git worktree add ../fw-025-pfx -b feat/FW-025-pfx-vault origin/main
git worktree add ../fw-027-pdf -b feat/FW-027-pdf417 origin/main
git worktree list
```
These are examples only. Replace with currently approved base and branch names; do not execute automatically. Claude's `claude --worktree` and Codex Worktree mode may create isolated worktrees. OpenCode should be launched from a separately created worktree. / Ejemplos, no ejecución.

## Handoff / Traspaso obligatorio
Provide the following in the issue/PR and structured task contract:
1. FW issue, assigned human coordinator, write agent, exact branch and **base commit SHA**.
2. Allowed paths and shared contracts touched; rationale for any dependency and privacy/SII implications.
3. Tests **run**, command/output, tests not run, known failures, pending decisions and review findings.
4. PR commit SHA and artifacts, security/cost impact, rollback and next concrete step.
5. No claims of finished work before CI and independent review. / No confundir plan con entrega.

## Independent review and integration / Revisión independiente e integración
- A different agent may review in **read-only mode**. Reviewers never push to author branches. / Revisor sin escritura.
- Human coordinator checks changed files of **every concurrent PR** before merging. If overlap, sequence/resolve; never accept automatic conflict resolution for fiscal or privacy-critical files. / Revisión cruzada.
- Merge one PR at a time; rebase/update remaining branches against latest approved main and rerun checks. Verify compatibility of OpenAPI, event schemas, XSD/CAF, migration and i18n. / Integración secuencial.
- No autopush to main, auto-merges, cloud deployments, SII submissions or real secrets. / Acciones sensibles requieren autorización.

## Executable validation / Validación ejecutable
- `python3 -m unittest discover -s scripts/tests -v`
- `python3 scripts/check_task_manifest.py --changed-files-file /tmp/changed.txt`
- CI computes the PR changed paths, requires a task JSON for application changes, and checks declared ownership. It also compares changed filenames against other open PRs on the same base branch through a read-only GitHub API call. This catches many collisions but **does not create a global lock or protect direct pushes**. / Validación de alcance local, no mutex entre ramas.

## Quality and legal constraints / Calidad y normativa
- Read [Definition of Done](QUALITY.md), [CI/CD](CICD.md), [Chile 21.719](../privacy/CHILE-21719.md) and [country isolation decision](../adr/0010-country-repository-strategy.md).
- Do not place live taxpayer XML, RUT, PFX, CAF, passports, personal logs or secrets in prompts, online evaluation tools, issues or unapproved AI connectors. Use synthetic fixtures. / Solo datos ficticios.
- In case of ambiguous legal rules, add a blocker and an official-source citation; never invent deadlines or jurisdiction-specific requirements. / No inventar plazos.
