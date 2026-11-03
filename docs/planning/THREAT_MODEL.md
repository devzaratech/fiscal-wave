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
| Corrupt audit / Auditoría manipulada | Versioned SHA-256 hash chain, restricted append-only event records, independent signed checkpoints where justified | Mutation/deletion/reordering tests, privileged rewrite threat |
| Public blockchain privacy leak / Filtración por blockchain | Publish only privacy-reviewed aggregate commitments (e.g., Merkle root), never DTE, RUT, PII, CAF or keys | Inspect public payloads and analyze correlation risks |
| Agent overwrites another PR / IA sobrescribe otra | One task/worktree/PR, versioned task allowlist, human cross-PR collision review; no automatic merge | Concurrent test branches with overlapping contracts, manual conflict check |
| Data subject rights denied / Derechos negados | DSAR flow, identity checks, applicable exceptions for legally retained DTE, privacy officer/legal review | Synthetic access/rectification/blocking/erasure cases |
| Cross-border PII leaks / Transferencia no controlada | Processor register, hosting region/access inventory, transfer safeguards, minimised logs and no real PII in AI prompts | Unauthorized vendor/AI export simulation |
| Privacy breach without response / Incidente sin respuesta | Legal notification triggers, incident ledger, tenant isolation, redacted evidence and backup runbook | Tabletop breach drill |
| Compromised CI runner / CI comprometida | OIDC short-lived federation, scoped workflow token, pin dependencies | Attempt unauthorized deploy in lab |

**EN:** Threats are hypotheses until tests and review. **ES:** riesgos propuestos; no declarar mitigación efectiva sin pruebas. No live secrets, taxpayer data or production simulations with unapproved AWS.
