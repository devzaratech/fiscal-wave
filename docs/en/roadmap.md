# FiscalWave roadmap (EN)

**Planning horizon:** milestone gates, not promised calendar dates. Shipping a working, documented vertical slice takes precedence over deploying every service. [Product backlog](../planning/BACKLOG.md) and [milestones](../planning/MILESTONES.md) are the planning sources.

## Milestone sequence
| Gate | Goal | Evidence required |
|---|---|---|
| M0 - Foundation + multi-agent governance | Bilingual repo, agent worktree/ownership rules, privacy role review, country ADR | Docs and diagrams reviewed, CI scope test, owner merge pending |
| M1 - Runnable local slice with privacy-by-design | Two Java services + shell/invoices MFE, Docker, Postgres, FW-022/023/029/030 | Real Java/React tests, tenancy negative tests, task scope checks, personal-data inventory and lawful-basis review |
| M2 - Offline Chilean DTE XML/PDF | Synthetic DTE 33/34, protected synthetic PFX/CAF, TED, XMLDSig, PDF417 | FW-025–027, official XSD version, hash/signature and printable barcode tests; idempotency |
| M3 - AWS competence and delivery lab | Cost-approved, temporary IAM/S3/Lambda/SQS and ECS/ALB + FW-023 release rehearsal | Protected OIDC deploy, smoke/failover, rollback, destroy and cost evidence |
| M4 - Official Chile integration | Authorized issuer's SII certification route with XML, PDF417 print samples and exchange | Official signed receipts, status, interoperability and print evidence; no premature certification claim |
| M5 - Privacy-reviewed customer pilot | Security, tenant isolation, audit, incident/rights procedures, retention, transfer and backup controls | External legal review, privacy evidence, signed agreements, approved SII pilot and runbook |
| M6 - Expansion | Optional MongoDB/JSONB choice, other DTE types/features and jurisdictions after discovery | FW-024/028 matrix, legal review, business tests and architecture decision |
| M7 - Optional cryptographic anchoring | Evaluate signed checkpoints, WORM, Merkle roots and blockchain adapter | Synthetic PoC, privacy and cost review; independent of DTE issuance |

## First delivery objective
A user creates a synthetic draft from a bilingual UI, issues it to a mock gateway, sees a stable status, and can explain the audit trail. The next increment strengthens document correctness. Never spend months creating empty microservices before this flow exists.

## Career evidence track (parallel, not blocker)
Weekly original coding drills in Java/SQL/TypeScript; one documented architecture explanation; one reproducible cloud lab when budget permits; regular job applications can continue before M4/M5.

**Release gates:** requirements linked -> test evidence -> security/cost review -> bilingual docs -> reviewed PR. Official SII certification is a separate external prerequisite.
