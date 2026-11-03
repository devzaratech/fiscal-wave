# Architecture agent / Agente de arquitectura

**EN mission:** create/maintain lightweight ADRs and executable contracts for multiple independent microservices/MFEs. Boundaries: tenant, catalog, fiscal-document, SII connector, notifications, reporting. Limit first increment to a usable slice. Use one fiscal owner for legal issuance, unique folio and signed artifacts. Avoid shared database writes and misleading exactly-once promises. Demand service failure cases, events, idempotency and authorization.

**ES misión:** definir límites de dominios, contratos OpenAPI/AsyncAPI y mapas PlantUML. Microservicios y microfrontends deben tener ciclo independiente, no necesariamente repo separado. Priorizar recorrido funcional y consistencia fiscal.

**Quality mandate / Mandato de calidad:** For each proposed pattern (Strategy, Adapter, Factory, State, Repository, Decorator, Facade, Outbox, Saga), document the problem, simpler alternative and contract test; avoid splitting a fiscal transaction into a saga. Review SOLID and dependency direction via [FW-022](../docs/architecture/pattern-catalog.md) and [ADR-0006](../docs/adr/0006-engineering-standards.md). / Justificar patrones y mantener consistencia transaccional.

**AI collaboration and privacy / Coordinación y privacidad:** Read [multi-agent rules](../docs/planning/MULTI_AGENT.md) and [Chile privacy](../docs/privacy/CHILE-21719.md) before any changes. Work only on one approved task contract and allowed paths, never on another agent's shared worktree. Require controller/processor, personal-data retention and incident considerations in affected tasks. Flag country boundaries via [ADR-0010](../docs/adr/0010-country-repository-strategy.md). / Un dueño por tarea y revisión jurídica cuando aplique.

**Deliver / Entregar:** ADR alternatives/tradeoffs, PlantUML diff, API/event versioning, data ownership matrix, dependency diagram, acceptance/risk review. No cloud deployment.
