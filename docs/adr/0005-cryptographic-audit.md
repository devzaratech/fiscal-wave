# ADR-0005 — Verifiable audit trail / Auditoría verificable

**Status / Estado:** Proposed / Propuesto — 2026-11-03 — [FW-021](https://github.com/devzaratech/fiscal-wave/issues/6)

## Context / Contexto
**EN:** A fiscal system needs integrity and event traceability. Local audit logs are vulnerable to privileged rewrites. Blockchain does not confer Chilean tax validity or replace SII authorization or XML signatures.
**ES:** La plataforma necesita integridad y trazabilidad; un administrador privilegiado puede reescribir registros locales. Blockchain no reemplaza la firma XML ni la habilitación ante el SII.

## Decision / Decisión
1. **M5:** Hash exact signed XML bytes with SHA-256. Hash versioned, ordered audit events with unambiguous encoding and previous-event hashes; verify with synthetic tampering, deletion and reordering tests. / Hashes versionados, cadena local y pruebas.
2. **M5:** Restrict proof access by tenant, minimize sensitive metadata, plan retention and protect signing/checkpoint keys. / Privacidad, control de acceso y retención.
3. **M7 optional:** Compare independently signed checkpoints, Merkle-root commitments and immutable/WORM storage. Define an AuditAnchoringProvider interface with a local stub before any external adapter. / Comparar checkpoints, Merkle, WORM y un adaptador opcional.
4. If an external blockchain is justified, only publish a privacy-reviewed aggregate commitment, never DTE, RUT, PII, CAF, private keys, personal invoices or secrets. / No publicar datos tributarios ni personales.
5. Audit anchoring is **out of band** and cannot block valid issuance if the provider fails. No live transactions, cloud costs or irreversible retention settings without explicit owner approval. / El anclaje no bloquea emisión y requiere aprobación.

## Tradeoffs / Consecuencias
**Benefits / Ventajas:** testable integrity, audit provenance, Java security practice, optional third-party verification.
**Risks / Riesgos:** privileged rewrite of an entirely local hash chain, leaked public metadata, key compromise, irreversible storage, cloud/on-chain fees and extra operational complexity.

## Exit evidence / Evidencia
- [ ] Deterministic SHA-256 vectors and integrity verification using synthetic artifacts.
- [ ] Tests for changed/deleted/reordered events and cross-tenant access.
- [ ] Independent checkpoint threat model and privacy assessment.
- [ ] Optional anchoring PoC costed and approved, with all cloud resources removed after testing.
- [ ] No claim of SII certification or legal non-repudiation on the basis of blockchain.

**Implementation / Implementación:** TODO, not yet coded / pendiente, todavía sin código.
