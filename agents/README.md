# Agent roles / Roles de agentes

Agent documents are **role instructions**, not runnable autonomous processes. The root [AGENTS.md](../AGENTS.md) always wins. / Son instrucciones, no agentes ejecutándose.

| Role / Rol | Purpose / Propósito |
|---|---|
| [Product & compliance](product-compliance.md) | SII evidence, requirements, market/scope / Evidencia normativa y alcance |
| [Architecture](architect.md) | Boundaries, ADRs, API/event contracts / Límites, ADR y contratos |
| [Backend](backend.md) | Java/Spring, transactions, XML, tests / Dominio fiscal y pruebas |
| [Frontend](frontend.md) | Shell, MFEs, i18n, UX / Microfrontends bilingües |
| [QA & interview coach](qa-interview.md) | Original drills, verification, test design / Ejercicios y pruebas |
| [Cloud & security](cloud-security.md) | IAM, cost approval, IaC, observability / AWS, FinOps y seguridad |

## Agent isolation / Aislamiento de agentes
The roles in this directory are **instructions**, not automatically running cross-tool agents. See [FW-029](../docs/planning/MULTI_AGENT.md) for branch/worktree/ownership rules. Claude Code loads [CLAUDE.md](../CLAUDE.md) which imports root AGENTS.md; OpenCode has a read-only [reviewer](../.opencode/agents/fiscalwave-reviewer.md) and Claude an independent [reviewer](../.claude/agents/fiscalwave-reviewer.md). Codex reads root AGENTS.md. Do not run several write agents on the same directory/branch. / No editar en paralelo los mismos archivos.
All agents must read [Chile privacy program](../docs/privacy/README.md) before handling personal data, and [country ADR](../docs/adr/0010-country-repository-strategy.md) before proposing other jurisdictions.
 
## Suggested handoff / Traspaso
Product gives source-backed acceptance -> Architect states boundaries -> Backend/Frontend implement -> QA tests independently -> Cloud/Security reviews cost & threat model -> human owner reviews PR. Agents must **never auto-merge**. / El propietario humano aprueba.

## Prompt contract / Contrato de entrega
Every agent response must contain: objective / objetivo, scope / alcance, files / archivos, tests executed / pruebas ejecutadas, unverified work / pendientes, SII/legal risk / riesgo, AWS cost impact / costo, next acceptance gate / siguiente criterio.
