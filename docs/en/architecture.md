# Architecture decisions (EN)

## Principles
1. **Multiple deployable services, one coherent fiscal owner.** Target bounded contexts: tenant, catalog, fiscal-document, chile-sii-connector, notification, reporting. Only instantiate the first necessary services for a vertical user flow.
2. **Microfrontends:** shell owns auth navigation, locale and tenant selection; invoice/partners/operations/admin MFEs own routes. Prove React/TypeScript composition (e.g., Module Federation) in an isolated spike before adopting it.
3. **Strong consistency:** issuer + document type + folio must be unique; allocate under DB transaction with unique constraint and concurrency tests. Signed artifacts immutable. Fiscal-document alone owns legal document state; connector owns delivery attempts.
4. **Integration:** OpenAPI HTTP for synchronous commands/queries; AsyncAPI event contracts, transactional outbox + inbox/deduplication for async work. No exactly-once assumption; reconcile unknown SII responses before retrying.
5. **Storage:** Postgres per-service ownership (separate database/schema and credentials), object store for immutable artifacts, S3-compatible adapter locally; no cross-service DB writes.
6. **Security:** OIDC user identity, backend authorization per tenant, role least privilege, certificates/CAF outside source control, secrets manager when legitimately deployed.
7. **Cloud:** Docker Compose by default; lab-only AWS ALB + ECS for load-balancing, IAM/S3/Lambda/SQS for application features; Terraform with cleanup; Azure adapter only after a validated need.
8. **I18N:** UI strings en/es-CL; locale formatting separate from fiscal calculations and signed XML.
9. **Evidence:** no certification or production maturity status before official validation.

## Decision record
ADR-001: multi-service monorepo now, independent builds and deploys later. ADR-002: AWS-first learning but cloud-portable domain. ADR-003: one transactional fiscal-document owner. ADR-004: single frontend shell, domain MFEs. ADRs proposed; validate in first milestone.

## SII cryptographic workflow and storage / Flujo criptográfico y datos
FW-024 proposes optional Redis cache and MongoDB projections only after comparison with PostgreSQL JSONB; Postgres remains authority for folios and durable idempotency. FW-025 protects signer PKCS#12 separately from SII CAF/RSASK. FW-026 covers versioned official XSD, TED and XMLDSig; FW-027 renders PDF/PDF417 from immutable XML; FW-028 defines public-provider feature benchmark. See [data](../planning/DATA-PLATFORMS.md), [SII lifecycle](../planning/SII-DTE-LIFECYCLE.md), [vendor matrix](../planning/PROVIDER-CAPABILITIES.md), [ADR-0008](../adr/0008-polyglot-persistence.md), [ADR-0009](../adr/0009-credential-custody-and-signing.md), [PlantUML](../architecture/sii-signing-and-pdf.puml). **None are implemented yet.**

## AI collaboration, country boundaries and Chile personal data / Agentes y privacidad
[FW-029](../planning/MULTI_AGENT.md) defines one write owner/branch/worktree/PR, validated path manifests and independent read-only reviews; cross-PR collisions still require human intervention. [FW-031 / ADR-0010](../adr/0010-country-repository-strategy.md) prefers monorepo + `jurisdictions/cl` boundary until a real reason to split country repositories. This choice cannot substitute independent data/credential/hosting access. [FW-030](../privacy/CHILE-21719.md) makes Law 21.719 privacy by design cross-cutting; inventory, DSAR, retention, contracts, incident response, EIPD risk and international transfers remain TODO, not a legal certificate. [Privacy map](../architecture/privacy-boundaries.puml).

## Engineering quality / Calidad de ingeniería
FW-022 establishes [SOLID and coding standards](engineering-standards.md), [pattern selection](../architecture/pattern-catalog.md), [idempotency semantics](../architecture/idempotency-contract.md) and [ADR-0006](../adr/0006-engineering-standards.md). These are proposed controls, not proof of implementation. Apply a pattern only with a concrete problem and tested tradeoff. Format, lint, architecture and test gates join CI progressively with code.

## Nonfunctional acceptance targets (proposals, not results)
- Contract tests for every boundary; synthetic data; zero cross-tenant reads in authorization tests.
- A duplicate request yields one fiscal intent and at most one allocated folio.
- Controlled SII outage leads to observable retry/reconciliation, never silent duplicate submission.
- Resource tags, budget alerts, explicit cost approval and teardown for every cloud lab.
- Audit events exclude secrets, full certificates and sensitive payloads.

[System map](../architecture/system-map.puml) · [Lifecycle](../architecture/dte-lifecycle.puml) · [AWS lab](../architecture/aws-lab.puml)
