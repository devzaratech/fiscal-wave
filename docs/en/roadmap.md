# FiscalWave roadmap (EN)

**Planning horizon:** milestone gates, not promised calendar dates. Shipping a working, documented vertical slice takes precedence over deploying every service. [Product backlog](../planning/BACKLOG.md) and [milestones](../planning/MILESTONES.md) are the planning sources.

## Milestone sequence
| Gate | Goal | Evidence required |
|---|---|---|
| M0 - Foundation | Bilingual repo, architecture maps, scope, agent guardrails, Scrum backlog | Docs merged; review checklists; no unsupported status claims |
| M1 - Runnable distributed skeleton + quality baseline | Two Java services + shell/invoices MFE, local Docker, Postgres; FW-022 design standards | CI builds, smoke/contracts, selected formatter/linter/architecture tests with real evidence; demo |
| M2 - Offline fiscal domain | Synthetic DTE 33/34, signed artifacts, folio and idempotent command processing | Request replay/conflict + event dedupe/concurrency tests; verified SII XML/XSD sources |
| M3 - AWS competence lab | Cost-approved, temporary IAM/S3/Lambda/SQS and ECS/ALB routing demo | IaC plan, budget, logs, failover evidence, terraform destroy and cost review |
| M4 - Official Chile integration | SII testing and certification workflow by properly authorized issuer | Official test artifacts/receipts, traceable evidence; never claim certification prematurely |
| M5 - Customer-ready pilot + audit integrity | Security, tenant isolation, restore tests, SHA-256 event chain and tamper detection | Synthetic verification tests, authorized pilot and an operational runbook |
| M6 - Expansion | Additional jurisdiction or billing/payments only after discovery | New ADR, research, jurisdiction-specific validation |
| M7 - Optional cryptographic anchoring | Evaluate signed checkpoints, WORM, Merkle roots and blockchain adapter | Synthetic PoC, privacy and cost review; independent of DTE issuance |

## First delivery objective
A user creates a synthetic draft from a bilingual UI, issues it to a mock gateway, sees a stable status, and can explain the audit trail. The next increment strengthens document correctness. Never spend months creating empty microservices before this flow exists.

## Career evidence track (parallel, not blocker)
Weekly original coding drills in Java/SQL/TypeScript; one documented architecture explanation; one reproducible cloud lab when budget permits; regular job applications can continue before M4/M5.

**Release gates:** requirements linked -> test evidence -> security/cost review -> bilingual docs -> reviewed PR. Official SII certification is a separate external prerequisite.
