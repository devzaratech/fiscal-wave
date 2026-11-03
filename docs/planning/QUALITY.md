# Quality gates and Definition of Done / Calidad y Definición de Terminado

**Done** only when the implemented increment is usable, integrated and demonstrably verified. / `Done` solo con software utilizable, integrado y evidencia real.

## Definition of Done / Definición de terminado
- [ ] The story's acceptance criteria pass / Criterios de aceptación cumplidos.
- [ ] Unit tests and relevant integration/contract tests executed and recorded / Pruebas ejecutadas y reportadas.
- [ ] SOLID/domain boundaries, KISS/YAGNI, naming, typed errors and pattern choice reviewed; exceptions justified / SOLID, límites y patrones revisados sin sobreingeniería.
- [ ] Available format/lint/static-security/typecheck/architecture gates pass with actual logs; missing tooling explicitly TODO / Gates disponibles con evidencia, los ausentes pendientes.
- [ ] Side-effect operations verify idempotency and DB uniqueness; concurrent/replay/conflict cases tested where applicable / Idempotencia y pruebas negativas, de reintentos y concurrencia.
- [ ] No unaddressed high/critical security finding; secrets never printed / Sin hallazgos graves no resueltos ni secretos expuestos.
- [ ] Tenant access verified when applicable; negative authorization tests included / Aislamiento probado.
- [ ] Bilingual end-user strings & docs reviewed, and locale/catalog parity tested / Traducciones revisadas.
- [ ] API/events/versioning and architecture diagrams updated if changed / Contratos actualizados.
- [ ] Metrics, tracing, failure modes, idempotency and rollback documented where relevant / Observabilidad y recuperación.
- [ ] Any cloud cost quantified, approved, monitored and teardown verified / Costos y destrucción comprobados.
- [ ] Tax-related rules trace to dated official sources and synthetic fixtures / Fuentes oficiales fechadas.
- [ ] Required CI gate always runs on PR; Maven/TS checks, security and contract jobs executed or explicitly marked not applicable / Gate CI siempre ejecutado, resultados o N/A.
- [ ] Release artifacts immutable (commit/digest), deployment approval/rollback and schema compatibility checked when applicable / Artefactos, aprobación y rollback.
- [ ] PR reviewed and no unresolved blockers; implemented status distinguished from future work / PR revisado.

## Suggested test pyramid / Pirámide de pruebas
Pure-domain unit tests -> contract and DB integration tests (Testcontainers) -> one end-to-end invoice happy path and rejection path -> cloud lab smoke/failover tests only when approved.

## Nonnegotiable / No negociable
No “certified” label until external SII requirements are actually met. No false CI claims, no real taxpayer data, no fabricated job credentials.
