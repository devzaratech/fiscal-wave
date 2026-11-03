# EX-08 — Reliable fiscal submission / Envío fiscal confiable

**EN:** Design a system with one fiscal-document service and a separate external connector. The issuer may retry the same HTTP request, the broker may deliver messages twice, and the simulated SII may time out **after** accepting an XML. Explain how your design prevents duplicate folios and avoids blind submission retries. Draw a sequence in PlantUML.

**ES:** Diseñar sistema con dueño fiscal y conector externo. El emisor puede repetir HTTP, la cola puede redeliverar y el SII simulado puede cortar conexión **después de aceptar**. Explicar unicidad de folios y conciliación de resultados inciertos. Dibujar secuencia PlantUML.

## Acceptance / Criterios
- Unique DB constraint + idempotency key / Restricción única y clave de idempotencia.
- Transactional outbox + consumer dedupe / Outbox y deduplicación.
- State diagram for pending, accepted, rejected and unknown / Estados.
- Retries use jitter/backoff, DLQ and reconciliation / Reintentos y conciliación.
- Tenant isolation, redacted logs, trace ID / Seguridad y trazabilidad.
- Discussion of availability vs. consistency, latency and recovery / Tradeoffs.

**No live SII use / Sin envío real SII.** Compare your work with [reference design](../../docs/architecture/dte-lifecycle.puml), not an official certification receipt.
