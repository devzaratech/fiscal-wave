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

## Suggested handoff / Traspaso
Product gives source-backed acceptance -> Architect states boundaries -> Backend/Frontend implement -> QA tests independently -> Cloud/Security reviews cost & threat model -> human owner reviews PR. Agents must **never auto-merge**. / El propietario humano aprueba.

## Prompt contract / Contrato de entrega
Every agent response must contain: objective / objetivo, scope / alcance, files / archivos, tests executed / pruebas ejecutadas, unverified work / pendientes, SII/legal risk / riesgo, AWS cost impact / costo, next acceptance gate / siguiente criterio.
