# Example agent handoff / Ejemplo de traspaso (no real work)

- **FW issue / Historia:** FW-002
- **Agent and model / Herramienta y modelo:** NOT SELECTED
- **Base branch and SHA / Base:** main, TODO actual SHA
- **Working branch / Rama:** feat/FW-002-local-ci (example)
- **Last commit / Último commit:** TODO
- **PR / Pull request:** not created
- **Write paths / Rutas autorizadas:** TODO before changing code
- **Status / Estado:** NOT STARTED

## Completed and verified / Completado y verificado
- None; no backend/frontend application code exists at this handoff. / Nada implementado.

## Tests / Pruebas
- Run: none / Ninguna.
- Not run: Java Maven, React TypeScript, Compose and application integration / Pendientes.

## Decisions / Decisiones
- Read [AI agent selection](../../docs/planning/AI-AGENT-STRATEGY.md), [stack](../../docs/planning/STACK-BASELINE.md), [M1 kickoff](../../docs/planning/M1-KICKOFF.md), root AGENTS.md and actual issue acceptance.

## Risks and blockers / Riesgos y bloqueos
- PR #1 foundation must be reviewed and merged **with human approval** before new work starts on main.
- The branch protection feature may require a GitHub plan upgrade for this private repository; check current plan/settings.
- No SII/certification or privacy runtime compliance is asserted; only synthetic data.
- No AWS, Dokploy or paid resources.

## Next single action / Próxima acción única
After owner approves merge and first agent selection: create FW-002 branch/worktree and corresponding `coordination/tasks/FW-002.json` with real base SHA and allowed paths, then implement the first narrow CI/backend slice. / Empezar por una tarea pequeña.
