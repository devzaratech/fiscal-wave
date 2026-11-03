# FiscalWave — AI agent policy / Política de agentes IA

Applies to Codex, Copilot and any code assistants. **Instructions are guidance; role documents do not launch autonomous agents.**

## Mandatory / Obligatorio
1. **Never touch BSK or other repositories** unless the owner explicitly requests it. / **Nunca modificar BSK ni otros repositorios** sin autorización.
2. Prefer a feature branch + reviewed PR; do not merge into main, deploy to cloud, create billable resources, change licenses or publish data without explicit owner approval. / Usar rama y PR; sin despliegues, costos, cambios de licencia ni publicaciones sin autorización.
3. Before coding, read README, architecture, backlog, acceptance criteria and applicable SII source. Confirm source/version/date for legal or tax claims. / Consultar fuentes SII vigentes antes de implementar reglas.
4. Never claim certification, production readiness, test results, cloud costs or compliance without verifiable evidence. / No inventar certificaciones ni resultados.
5. Preserve strong consistency within the fiscal-document boundary for CAF, folio allocation, signed XML and versioned tax rules. The connector sends but never allocates folios. / Mantener consistencia fiscal; el conector no asigna folios.
6. No secrets, customer PII, live certificates, real CAF, taxpayer identifiers or production DTE in tests/prompts. Use explicitly synthetic fixtures. / Solo datos sintéticos.
7. Protect tenant isolation, least privilege, idempotency and auditable state changes. Document retries and uncertain remote outcomes before implementation.
8. English and Spanish parity is required for end-user text and key user documentation. Tax XML and machine contracts follow authoritative specifications, not user locale.
9. Do not introduce microservices/microfrontends without defining boundary, owner, API/events, security, lifecycle and test strategy.
10. Run available checks and report **executed**, **not executed**, **failed**, **pending** separately. Never mark TODOs done without evidence.

## Engineering standards / Estándares de ingeniería
All code agents MUST follow [EN engineering standards](docs/en/engineering-standards.md), [ES estándares](docs/es/engineering-standards.md), [pattern catalog](docs/architecture/pattern-catalog.md), [idempotency contract](docs/architecture/idempotency-contract.md) and [ADR-0006](docs/adr/0006-engineering-standards.md). Apply SOLID, DRY/KISS/YAGNI without pattern cargo cult; document chosen pattern and simpler alternative. Require transaction-level idempotency + event dedupe and SII reconciliation on affected flows. Add tooling progressively as code exists; do not claim absent checks passed. / Aplicar SOLID y patrones justificados, pruebas reales y calidad progresiva.

## Work routine / Flujo de trabajo
- Select one backlog ID; define objective, non-goals, accepted dependencies and acceptance criteria (EN/ES).
- Propose plan + touched files + risk and estimated recurring cloud cost.
- Implement narrowly; unit, integration and contract tests as appropriate.
- Update diagrams, docs, examples and bilingual copy together.
- Publish PR description with evidence, risks, security/cost impact and rollback steps.

## Agent roles / Roles de agentes
Role prompts are in [agents/README.md](agents/README.md): product/compliance, architect, backend, frontend, quality/interviews and cloud/security. **No role may override these root constraints.**

## High-risk actions requiring explicit approval / Acciones con autorización explícita
AWS/Azure real resources or `terraform apply`; live SII submissions, taxpayer CAF/certificates, payments or financial transfers; changing IAM/secret permissions; data migrations/destruction; production release; merging PRs; modifying other repos.
