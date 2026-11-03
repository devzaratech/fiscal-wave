# FiscalWave roadmap (EN)

**Planning horizon:** milestone gates, not promised calendar dates. Shipping a working, documented vertical slice takes precedence over deploying every service. [Product backlog](../planning/BACKLOG.md) and [milestones](../planning/MILESTONES.md) are the planning sources.

## Milestone sequence
| Gate | Goal | Evidence required |
|---|---|---|
| M0 - Foundation | Bilingual repo, architecture maps, scope, agent guardrails, Scrum backlog | Docs merged; review checklists; no unsupported status claims |
| M1 - Runnable distributed skeleton + quality CI | Two Java services + shell/invoices MFE, local Docker, Postgres, FW-022/FW-023 | Always-run PR gate, selective Java/React builds and verified tests, no AWS deployment, demo |
| M2 - Offline Chilean DTE XML/PDF | Synthetic DTE 33/34, protected synthetic PFX/CAF, TED, XMLDSig, PDF417 | FW-025–027, official XSD version, hash/signature and printable barcode tests; idempotency |
| M3 - AWS competence and delivery lab | Cost-approved, temporary IAM/S3/Lambda/SQS and ECS/ALB + FW-023 release rehearsal | Protected OIDC deploy, smoke/failover, rollback, destroy and cost evidence |
| M4 - Official Chile integration | Authorized issuer's SII certification route with XML, PDF417 print samples and exchange | Official signed receipts, status, interoperability and print evidence; no premature certification claim |
| M5 - Customer-ready pilot + audit integrity | Security, tenant isolation, restore tests, SHA-256 event chain and tamper detection | Synthetic verification tests, authorized pilot and an operational runbook |
| M6 - Expansion | Optional MongoDB/JSONB choice, other DTE types/features and jurisdictions after discovery | FW-024/028 matrix, legal review, business tests and architecture decision |
| M7 - Optional cryptographic anchoring | Evaluate signed checkpoints, WORM, Merkle roots and blockchain adapter | Synthetic PoC, privacy and cost review; independent of DTE issuance |

## First delivery objective
A user creates a synthetic draft from a bilingual UI, issues it to a mock gateway, sees a stable status, and can explain the audit trail. The next increment strengthens document correctness. Never spend months creating empty microservices before this flow exists.

## Career evidence track (parallel, not blocker)
Weekly original coding drills in Java/SQL/TypeScript; one documented architecture explanation; one reproducible cloud lab when budget permits; regular job applications can continue before M4/M5.

**Release gates:** requirements linked -> test evidence -> security/cost review -> bilingual docs -> reviewed PR. Official SII certification is a separate external prerequisite.
