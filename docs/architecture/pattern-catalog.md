# FiscalWave design pattern catalog / Catálogo de patrones

**FW-022 · Proposal / Propuesta.** Apply a pattern only where a tested variation or invariant justifies it. / Aplicar patrones solo por una necesidad concreta y comprobable.

| Pattern / Patrón | When to use / Cuándo usar | FiscalWave example / Ejemplo | Do NOT use / Evitar |
|---|---|---|---|
| Strategy | Several changing algorithms with same stable contract / Variantes reales | `TaxCalculationPolicy` per jurisdiction/document type | One rule and no variation / Una regla |
| Adapter | External provider APIs behind domain ports / SDK externos | `SiiDeliveryPort`, `ObjectStoragePort` (S3/local/Azure) | Trivial one-off mapping for no reason |
| Factory / Abstract Factory | Create families of collaborators with invariant configurations / Familias | Jurisdiction-specific document builder + validator after second jurisdiction exists | Guessing all future countries today |
| State / State machine | Legal transition graph with forbidden transitions / Transiciones DTE | Draft → signed → pending → accepted/rejected/unknown | Simple boolean flag |
| Repository | Persistence abstraction required by domain / Persistencia | `FiscalDocumentRepository` domain port, Postgres adapter | Wrapping every JPA method blindly |
| Facade | Simplify a cohesive cross-adapter workflow / Simplificar | `IssueDocumentUseCase` application coordinator | God object that owns all services |
| Chain of Responsibility | Independently composable validations with defined order / Validaciones | XML/domain validation pipeline, with complete error reporting | Hide validation errors or mutate signed XML |
| Decorator | Cross-cutting behavior on a narrow interface / Transversal | Trace/metrics decorator around a port | Duplicate framework middleware |
| Observer / Domain Events | Decouple reporting and notification from issuance | `FiscalDocumentIssued` domain event | Treat as exactly-once |
| Circuit Breaker + timeouts | Avoid cascading SII/external failures / Fallas externas | Connector calls with observability and half-open recovery | Replace reconciliation with blind retries |
| Retry + exponential backoff/jitter | Only safe retryable transient faults / Reintentos seguros | Broker publish, transient network handling | Reissue signed DTE when SII state is unknown |
| Transactional Outbox + Inbox | Atomic local business write and eventual delivery / Publicación confiable | Persist fiscal state + outbox, consumer dedupes event IDs | Claim end-to-end exactly-once |
| Saga | Long-running *reversible* cross-service business workflows / Procesos compensables | Future billing/payment workflows once defined | Split atomic folio/CAF/signing among services |
| CQRS (optional) | Read model proven to have different load / Lecturas distintas | Future reporting projection | Preemptive duplication for MVP |
| Bulkhead / Rate limiting | Bound resource exhaustion / Recursos | Tenant API limits and bounded connector concurrency | Arbitrary denial of valid work |

## Anti-patterns / Antipatrones
**EN:** Pattern obsession, premature microservice split of a fiscal transaction, distributed shared database, service-to-service JPA entity reuse, generic base repository everywhere, infinite retries, swallowing exceptions, magic constants for tax rates, excessive interface per class and frontend permission checks without backend enforcement.

**ES:** Sobreingeniería de patrones, fragmentar transacción fiscal, escribir BD ajena, reutilizar JPA entre servicios, repositorios genéricos indiscriminados, reintentos infinitos, ocultar errores, tasas impositivas mágicas, interfaces innecesarias y permisos solo frontend.

## Review evidence / Evidencia
Record the problem, selected pattern, simpler alternative, tests, runtime/maintenance cost and boundary ownership in PR or ADR. / Registrar necesidad, alternativa simple, pruebas y costos. See [EN standards](../en/engineering-standards.md) · [ES estándares](../es/engineering-standards.md).
