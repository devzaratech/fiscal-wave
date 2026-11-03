# FW-024 — Redis, MongoDB and PostgreSQL / Plataformas de datos

**Status / Estado: TODO, design only / solo diseño.** [Issue FW-024](https://github.com/devzaratech/fiscal-wave/issues/9). **EN:** Choose storage by domain invariants, not resume keyword count. **ES:** Elegir motor según necesidad, no por acumular tecnologías.

| Platform / Plataforma | Planned owner/use / Dueño y uso | Source of truth / Fuente de verdad | Milestone |
|---|---|---|---|
| PostgreSQL | Tenant, invoices, folios, idempotency, Outbox/Inbox; ACID and unique constraints | **Yes / Sí**, authoritative for fiscal states | M1–M2 |
| Redis | Ephemeral non-sensitive cache, TTL, API rate limiting, optional derived state | **No / No**: never sole folio/idempotency owner | M1/M2 learning spike |
| MongoDB | Optional read projections, variable integration metadata, provider payloads only if justified; compare with PostgreSQL JSONB | **No / No** for legal DTE; projections must be rebuildable | M3/M6 optional |
| S3-compatible object storage | Immutable signed XML, PDFs, redacted evidence; per-tenant access | Signed XML artifact source, metadata indexed in PostgreSQL | M2 |
| Secret vault (NOT Redis/Mongo) | PFX/P12, passphrases, CAF signing keys; separate crypto and authorization boundaries | Credential custody | M2/M4 |

## Redis — implement as an optional adapter / Redis — adaptador opcional
- Start with local Redis + Spring Data Redis/Testcontainers **only after an observable use case**. / Comenzar local con pruebas, solo por necesidad real.
- Candidate exercise: tenant-scoped, non-sensitive catalog cache and API rate limit with TTL, safe key names, cache stampede considerations and invalidation on change. / Caché e invalidación.
- Cache loss, eviction, restart or staleness must **not** cause duplicate folios, repeated issuance, missing audit records or leaked tenant data. / La pérdida de caché no puede alterar la emisión.
- Do not store raw DTE payloads, credentials, certificate passwords, CAF keys, PII or tokens with unbounded lifetime. / Sin secretos en Redis.
- Redis distributed locks are not a substitute for PostgreSQL transaction/unique constraints. / No usar locks Redis como único garante fiscal.

## MongoDB — compare before adoption / MongoDB — comparar antes
- Build a local spike using synthetic integration metadata and a projection in Spring Data MongoDB, then compare with PostgreSQL JSONB for performance, query shape, indexing, consistency and operating cost. / Prueba MongoDB contra JSONB.
- No cross-service database writes; events include version/IDs, replay and projection rebuild logic. / Propiedad de datos y proyecciones reconstruibles.
- MongoDB can support ACID transactions, but introducing it does not improve fiscal correctness automatically. / MongoDB tiene transacciones; no justifica uso por sí solo.
- Test stale read models, duplicate/reordered events, tenant boundaries, backup and restore. / Probar proyecciones retrasadas y segregación.

## Cloud/career gates / Costos y empleabilidad
- Practice local Docker, Spring Data, indexes, query plan and Testcontainers for interviews. / Práctica laboral sin gasto cloud.
- AWS ElastiCache/DocumentDB and managed MongoDB/Redis may incur ongoing infrastructure costs; only with explicit owner approval and actual use case. / Servicios administrados solo con aprobación.
- Evaluate retention, monitoring, encryption and restore before production. / Retención y recuperación obligatorias.

## Acceptance / Criterios
- [ ] Redis cache/expiry and failure fallback tests executed.
- [ ] MongoDB vs JSONB reproducible benchmark with stated assumptions (optional).
- [ ] Per-tenant ownership, privacy, backup and cost rationale documented.
- [ ] Fiscal operations work with Redis and MongoDB entirely disabled.
