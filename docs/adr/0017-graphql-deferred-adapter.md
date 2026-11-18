# ADR-0017 — Optional GraphQL Adapter (Deferred) / Adaptador GraphQL opcional (diferido)

**Status / Estado:** Deferred / Diferido · 2026-11-18 · [FW-035](https://github.com/devzaratech/fiscal-wave/issues/23)

## Context / Contexto
REST with JSON/XML and multilingual public contracts already adds a significant verification matrix. GraphQL is a **query language and API layer**, not another data serialization format equivalent to XML or JSON. It can help clients request tailored and aggregated reads, but also introduces schema maintenance, cost/security controls, versioning and authorization complexity. FiscalWave has no demonstrated workload requiring GraphQL yet. / Priorizar el motor DTE y REST, sin zoológico de frameworks.

## Decision / Decisión
1. **Do not implement in MVP / No implementar en MVP:** continue REST/OpenAPI and async webhooks/events where justified. No Spring for GraphQL dependency, endpoint, mock server or schema until a measured use case exists. / YAGNI.
2. **Future adapter only / Solo adaptador:** if approved later, GraphQL calls the same application use cases and authoritative data owners; it must not duplicate tax calculation, folio allocation, signing, status transitions or authorization. / Un motor de negocio.
3. **Prefer read use cases first / Lecturas primero:** candidate dashboard/portal queries with measured REST overfetch, underfetch or composition complexity. Evaluate DataLoader/N+1, pagination, complexity/depth limits, timeouts, query rate quotas, tenant field-level authorization and observable cost. / Seguridad de consultas.
4. **Mutations not exempt / Mutaciones:** any eventual issuance mutation needs the same idempotency, unique fiscal state, policy, audit, human/automated approvals and unknown SII-outcome reconciliation as REST. No direct arbitrary database mutation. / Misma seguridad.
5. **Schema language / Idioma:** if implemented, first consider English-first schema. Do **not** assume GraphQL inherits REST's `en`/`es-CL`/`sii-cl` six-mode matrix; assess multilingual schema cost with real clients and separate decision. / No triplicar automáticamente GraphQL.

## Adoption trigger / Condición para reabrir
A documented consumer demonstrates: (a) an important query/use case; (b) measured REST complexity/latency/round trips; (c) comparative prototype showing benefit; (d) field-level authorization and abuse-budget tests; (e) sustainable maintenance/security cost. Human owner approves a separate implementation issue and ADR status change. / Evidencia antes de tecnología.

## Alternatives / Alternativas
REST projections, compound endpoints, BFF or read models: preferred now due to lower maintenance. GraphQL for all writes/reads from day one: rejected for premature complexity. / REST primero.

## Acceptance / Aceptación
No code or dependency changes in this ADR. The deferred decision is recorded, easily reversible and compatible with domain/application separation in [ADR-0001](0001-repo-and-service-boundaries.md). / Diferido, no compromiso de implementación.
