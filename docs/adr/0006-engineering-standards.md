# ADR-0006 — Engineering quality and pragmatic patterns / Calidad y patrones pragmáticos

**Status / Estado:** Proposed / Propuesto — 2026-11-03 · [FW-022](https://github.com/devzaratech/fiscal-wave/issues/7)

## Context / Contexto
Multiple Java microservices and React microfrontends increase the risk of coupling, inconsistent APIs and unreliable DTE operations. Interview preparation also demands explainable design decisions. / Varios servicios y MFEs pueden introducir acoplamiento y fallas tributarias.

## Decision / Decisión
- Adopt **SOLID, Clean Code, DRY/KISS/YAGNI and explicit design-pattern selection criteria**. Follow [EN](../en/engineering-standards.md), [ES](../es/engineering-standards.md), [catalog](../architecture/pattern-catalog.md).
- Define typed ports/adapters, domain invariants, clean service boundaries and independent deployment only where needed. / Puertos, invariantes y límites claros.
- Treat **HTTP idempotency + transaction uniqueness + event deduplication + SII reconciliation** as separate mandatory guarantees where appropriate. See [contract](../architecture/idempotency-contract.md). / Idempotencia en capas.
- Incrementally add compatible format, lint, tests, security scan, architecture tests and CI checks **as code appears**, not all upfront. / Calidad progresiva con herramientas compatibles.
- No arbitrary coverage target substitutes tests of fiscal invariants and negative paths; store evidence and require human review. / Cobertura no reemplaza pruebas importantes.
- Training exercises remain original and do not represent production expertise until proven. / Evidencia de aprendizaje honesta.

## Alternatives / Alternativas
No shared standards → drift; blanket use of every pattern or tool → complexity, maintenance and cost. / Sin estándares hay deriva, con exceso hay sobreingeniería.

## Consequences / Consecuencias
Every relevant feature PR must explain chosen pattern (or simpler approach), show idempotency/failure tests, EN/ES docs, CI results, security and cloud cost impact. / Cada PR necesita justificación y evidencia. No changes to AWS, BSK or SII.

## Verification / Verificación
M1: standards and selected checks configured when first code exists; M2: functional idempotency/folio negative tests. Document-only checks must not be mistaken for application tests. / M1 controles iniciales, M2 pruebas tributarias.
