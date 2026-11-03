# Product backlog / Backlog de producto

**Ordered by immediate value and risk.** Use GitHub issues for day-to-day execution after tasks are approved. The list below is the seed, not evidence of implementation. / Ordenado por valor y riesgo; las tareas no están ejecutadas.

| ID | Priority | Slice / Entregable | Acceptance criteria (EN / ES) | Status |
|---|---|---|---|---|
| FW-001 | P0 | Product boundaries / Límites de dominio | ADR for folio owner, 6 service contexts and MFE ownership / ADR de propiedad fiscal y MFE | TODO |
| FW-002 | P0 | Repo & CI / Monorepo y CI | Java Maven, TypeScript build and docs checks on PR; no cloud credentials | TODO |
| FW-003 | P0 | Tenant + fiscal APIs / API de empresas y DTE | Two isolated Java deployments, synthetic create/read contract, authorization checks | TODO |
| FW-004 | P0 | Shell + invoices MFE / Shell y facturas | English/Spanish switch, tenant selection, draft screen, accessible validation | TODO |
| FW-005 | P0 | Local integration / Integración local | Compose starts DB + APIs + UI, smoke test and rollback/cleanup instructions | TODO |
| FW-006 | P0 | DTE calculations / Cálculos DTE | Versioned verified SII rules; unit tests for 33/34, exempt/tax cases, rounding | TODO |
| FW-007 | P0 | Folio reservation / Reserva de folios | Unique (issuer, type, folio), concurrent tests, retry idempotency | TODO |
| FW-008 | P0 | XML & signing / XML y firma | Valid official schemas with synthetic keys/CAF; tamper tests, no live secrets | TODO |
| FW-009 | P0 | SII connector simulator / Simulador SII | Outbox -> inbox, accepted/rejected/timeout flows, reconciliation, contract tests | TODO |
| FW-010 | P1 | Observability / Observabilidad | Trace ID through UI/API/event; alerts without sensitive payloads | TODO |
| FW-011 | P1 | AWS cost lab / Laboratorio AWS | Estimate + owner approval + AWS IAM/S3/Lambda/SQS; Terraform destroy + cost review | TODO |
| FW-012 | P1 | ECS/ALB reliability / Balanceo | Two targets, health-check failure demo, traffic rerouting, no persistent resources | TODO |
| FW-013 | P1 | Partner + operations MFEs / MFEs de terceros y operaciones | Independently deployable routes, shell contract, accessibility and E2E | TODO |
| FW-014 | P1 | Admin + reporting / Administración y reportes | Isolation and query contracts; independent deployment only if justified | TODO |
| FW-015 | P1 | Official SII readiness / Preparación oficial SII | Requirements matrix + test authorization + accepted official test evidence | TODO |
| FW-016 | P1 | Backup and disaster recovery / Respaldo y DR | Restore exercise with target RPO/RTO and runbook | TODO |
| FW-017 | P2 | Second-cloud spike / Prueba Azure | Same container boots and tests without domain code changes | TODO |
| FW-018 | P2 | Second jurisdiction discovery / Otro país | Legal discovery, adapter ADR; no implementation by assumption | TODO |
| FW-019 | P0 | Interview practice / Práctica técnica | Original Java/SQL/React/system design drills, timed self-evaluation, evidence logs | TODO |
| FW-020 | P0 | Portfolio proof / Evidencia laboral | Short EN/ES architecture walkthrough + reproducible installation + honest status | TODO |
| [FW-021](https://github.com/devzaratech/fiscal-wave/issues/6) | P1 local / P2 optional anchoring | Verifiable audit / Auditoría criptográfica verificable | SHA-256 digest, event hash chain and tamper tests (M5); optional Merkle root, signed checkpoint or blockchain anchoring PoC (M7), with privacy/cost approval. Not required for DTE issuance / No requerido para DTE | TODO |
| [FW-022](https://github.com/devzaratech/fiscal-wave/issues/7) | P0 | Engineering standards / Estándares de ingeniería | EN/ES SOLID + Clean Code + justified patterns, idempotency contract, agent/DoD standards, progressive quality gates and reproducible tests (M1 baseline, M2 idempotency verification) / Calidad y pruebas documentadas | TODO |
| [FW-023](https://github.com/devzaratech/fiscal-wave/issues/8) | P0 M1 / P1 later | CI/CD per component / Integración y entrega continua | Always-run required PR gate; selective Maven/React checks; security + contract tests; digest-tagged artifacts; environment approvals, OIDC, rollback and zero unapproved AWS costs / Entrega gradual con pruebas y costos autorizados | TODO |

| [FW-024](https://github.com/devzaratech/fiscal-wave/issues/9) | P1 Redis / P2 Mongo | Polyglot / Redis y MongoDB | PostgreSQL fiscal authority; Redis non-authoritative cache, Mongo optional projection vs JSONB / Datos opcionales | TODO |
| [FW-025](https://github.com/devzaratech/fiscal-wave/issues/10) | P0 | PFX and CAF custody / Custodia de claves | Authorized PKCS#12 signer separate from CAF private timbre key; encryption, expiry, tenant ACL, audit / Bóveda y seguridad | TODO |
| [FW-026](https://github.com/devzaratech/fiscal-wave/issues/11) | P0 | SII XML/XSD, XMLDSig and TED / Esquemas y timbre | Verified official versioned schemas and separate PFX vs CAF crypto; XXE and tamper tests / XSD oficiales y firmas | TODO |
| [FW-027](https://github.com/devzaratech/fiscal-wave/issues/12) | P0 | XML-to-PDF/PDF417 / Representación gráfica | Derive printable PDF and machine-readable TED PDF417 from immutable signed XML / Pruebas de escaneo e impresión | TODO |
| [FW-028](https://github.com/devzaratech/fiscal-wave/issues/13) | P1 | Provider feature map / Comparativa LibreDTE | Source-backed SII + LibreDTE + SimpleFactura benchmark, not assumed implementation / Prioridades por hito | TODO |

| [FW-029](https://github.com/devzaratech/fiscal-wave/issues/14) | P0 | Multi-agent governance / Gobernanza IA | Canonical AGENTS.md, Claude/OpenCode wrappers, isolated worktrees, task contracts and PR scope CI; manual cross-PR coordination / Worktrees y checker | IN_PROGRESS |
| [FW-030](https://github.com/devzaratech/fiscal-wave/issues/15) | P0 | Chile Law 21.719 privacy readiness / Privacidad | Controller/processor inventory, lawful basis, rights, retention exceptions, EIPD risk screen, breach response and transfer review / Derechos y seguridad | IN_PROGRESS |
| [FW-031](https://github.com/devzaratech/fiscal-wave/issues/16) | P0 architecture / P2 split | Country repository decision / Repositorios por país | ADR monorepo per-jurisdiction now, criteria for splitting later; data/IAM isolation independent of Git / ADR y límites reales | IN_PROGRESS |

## Next executable sprint candidate / Próximo sprint sugerido
**Goal:** reviewed repository foundation + runnable local invoice draft vertical slice (not six empty apps). Candidate scope: FW-001, FW-002 and a minimum vertical subset of FW-003/004/005. Re-scope after refinement. / Objetivo: base revisada y flujo local de borrador, sin seis apps vacías.

## Blocked until prerequisites / Bloqueos
Official SII operations require genuine issuer enrollment/authorization, appropriate certificates/CAF, tax sources and legal review. AWS deployment requires explicit owner approval and a quantified cost plan. / SII real y nube con autorización previa.
