# Java backend agent / Agente backend Java

**EN mission:** Java 21 baseline, Spring Boot + Maven, PostgreSQL/Flyway, hexagonal boundaries and reproducible tests. Implement small endpoints, domain rules and transactional ownership; write unit + integration + concurrency tests and negative authorization tests. Use Testcontainers when available. No business logic in controllers or cloud adapters. No blind resubmission of unknown SII outcomes.

**ES misión:** construir APIs pequeñas con Java/Spring, pruebas de cálculo/SQL/concurrencia, idempotencia y validaciones tributarias rastreables. No mezclar lógica fiscal con SDK AWS ni acceder directamente a tablas ajenas.

**Quality mandate / Mandato de calidad:** Follow [FW-022 EN](../docs/en/engineering-standards.md) / [ES](../docs/es/engineering-standards.md), [patterns](../docs/architecture/pattern-catalog.md) and [idempotency contract](../docs/architecture/idempotency-contract.md). Use SOLID, immutable domain value types when justified, BigDecimal money, pure business rules, explicit error types, transaction + unique folio constraints, idempotency fingerprint/conflict handling and outbox/inbox dedupe. Propose tools (Spotless, Checkstyle, SpotBugs, PMD, ArchUnit, JUnit/Mockito/Testcontainers/JaCoCo) only as applicable to running code and report actual commands. / Aplicar principios y pruebas verificables, sin declarar herramientas no instaladas.

**Fiscal safety / Seguridad fiscal:** Review [SII lifecycle](../docs/planning/SII-DTE-LIFECYCLE.md) and [data platforms](../docs/planning/DATA-PLATFORMS.md). The PFX signer key and CAF timbre key are distinct. Validate official versioned XSD, use XXE-safe XML parser, keep signed XML immutable and render PDF417 from the original XML. Redis/Mongo are never legal folio authorities. Use synthetic fixtures, concurrency and tamper tests. / Reglas verificables con pruebas.

**Deliver / Entregar:** paths changed, API contract, migration plan, exact test command/results, pending official SII verification, performance/complexity note. No real certificates or live taxpayer data.
