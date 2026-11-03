# Agent task contracts / Contratos de trabajo de agentes

**One issue = one independent worktree and PR.** The owning agent creates `coordination/tasks/FW-XXX.json` with a base SHA, branch, agent, allowed_paths and handoff notes **before modifying application directories**. Start from [example](examples/FW-000.example.json). Keep one active task contract in a feature PR. Never modify another agent's contract.

The CI checker validates syntax and whether modified application paths fall within the declared allowlist. Shared contracts and security/privacy policies always require human review. **A task contract is NOT a GitHub lock; inspect concurrent open PRs manually.**

**Un issue = un worktree y PR.** Registrar rutas exclusivas, SHA y pruebas reales. No sobrescribir otro agente. Ver [MULTI_AGENT](../docs/planning/MULTI_AGENT.md).
