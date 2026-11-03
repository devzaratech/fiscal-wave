# ADR-0008 — PostgreSQL authority, Redis/Mongo optional / Persistencia políglota

**Status / Estado:** Proposed / Propuesto · 2026-11-03 · [FW-024](https://github.com/devzaratech/fiscal-wave/issues/9)

**Context / Contexto:** Fiscal correctness requires strongly consistent folio allocation and durable idempotency while job profiles value Redis/NoSQL skills. / Consistencia y empleabilidad sin sobrecarga operacional.

**Decision / Decisión:** PostgreSQL remains the legal fiscal and transactional source of truth. Redis is a replaceable, non-sensitive ephemeral cache/rate limiter; no folio authority, persistent idempotency source or private keys. MongoDB is optional for variable metadata/read projections only after a measured comparison with JSONB and an explicit owner. / PostgreSQL autoridad; Redis y MongoDB optativos.

**Tradeoffs / Compensaciones:** Extra databases increase backups, observability, privacy and cost. Local Compose/Testcontainers labs before paid managed services. / Costos y riesgos adicionales.

**Exit criteria / Aceptación:** Cache loss cannot change issuance; Mongo projections rebuild from events; query comparison and tenant isolation tested; absence of Redis/Mongo does not block DTE. / Pruebas y recuperación sin dependencia.
