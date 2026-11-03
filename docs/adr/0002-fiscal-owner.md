# ADR-0002: One legal fiscal owner / Único dueño del documento tributario

**Status / Estado:** Proposed / Propuesto · 2026-11-03

**Context / Contexto:** Splitting folio allocation, signing and state ownership across services could create inconsistent or duplicated documents. / La emisión tributaria exige integridad.

**Decision / Decisión:** `fiscal-document` owns issuer/type/folio uniqueness, CAF state, signed XML immutable artifacts and legal status. PostgreSQL transaction, unique constraint and idempotency control. `chile-sii-connector` owns communication attempts, never folio assignment. Remote unknown outcome requires status reconciliation before any resubmission. / Un servicio es autoridad fiscal; el conector no emite folios.

**Acceptance / Aceptación:** concurrent duplicate tests, cross-tenant negative tests, outbox replay tests, SII timeout simulation, source-backed XML checks. / Pruebas de concurrencia, aislamiento, reintentos y fuente normativa.

**Tradeoff / Costo:** Less independent scaling of issuance steps, but legally safer consistency. / Menos fragmentación, mayor integridad.
