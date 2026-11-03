# Threat model / Modelo de amenazas (draft / borrador)

**Assets / Activos:** issuer identity, tax documents, folios, CAF/certificates, personal data, tenant data, event queue, invoices, cloud account and costs.

| Threat / Amenaza | Controls to design / Controles a diseñar | Test / Prueba |
|---|---|---|
| Cross-tenant access / Lectura entre empresas | JWT/OIDC claims plus server-side tenant ownership and DB isolation | Attempt wrong-tenant fetch and mutation |
| Duplicate folios / Folios duplicados | Unique DB constraint, transactional allocator, idempotency key | Concurrent submissions under load |
| Forged document / Documento alterado | Verified XML schema, signing and immutable storage | Mutate document and verify signature failure |
| XXE and XML abuse / XML malicioso | Disable external entities, size limits, safe parsers | Synthetic XML attack fixture |
| Leaked CAF/certificate / Fuga de CAF/certificado | Encrypted storage, least privilege, rotation, never log values | Secret scanning and negative access tests |
| Replay or lost delivery / Reenvío o pérdida | Outbox/inbox, dedupe, audit; reconcile unknown SII outcomes | Simulate timeout and replay |
| Cost amplification / Abuso de costos | API rate limiting, bounded scaling, IAM permissions, budget alerts, teardown | Artificial traffic + resource inventory |
| Corrupt audit / Auditoría manipulada | Append-only events, authorization and structured redacted logs | Tamper and missing-event checks |
| Compromised CI runner / CI comprometida | OIDC short-lived federation, scoped workflow token, pin dependencies | Attempt unauthorized deploy in lab |

**EN:** Threats are hypotheses until tests and review. **ES:** riesgos propuestos; no declarar mitigación efectiva sin pruebas. No live secrets, taxpayer data or production simulations with unapproved AWS.
