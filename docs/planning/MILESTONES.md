# Milestones and outcome gates / Hitos y metas

All milestones are **proposed, not complete** / Todos los hitos están **propuestos, no completados**. No fixed due dates / Sin fechas obligatorias.

| ID | Outcome (EN) / Resultado (ES) | Acceptance evidence / Evidencia de aceptación | Status |
|---|---|---|---|
| M0 | Reviewed bilingual foundation / Base documental bilingüe revisada | Docs + diagrams + agent rules + backlog merged after review / docs fusionados tras revisión | IN_PROGRESS |
| M1 | Local runnable distributed slice / Flujo distribuido local | Two APIs + shell/invoice MFE + PostgreSQL + Compose + CI + synthetic flow | TODO |
| M2 | Correct offline DTE flow / Flujo DTE offline correcto | DTE 33/34 rules + signed artifacts model + concurrency/idempotency tests + official schema references | TODO |
| M3 | Cost-limited AWS lab / Laboratorio AWS con control de costos | IAM/S3/Lambda/SQS; temporary ECS + ALB failover; terraform destroy evidence; actual cost checked | TODO |
| M4 | Chilean official test path / Ruta oficial Chile | Authorized test issuer, SII test/certification evidence and documented outcome; no invented approvals | TODO |
| M5 | Pilot operational readiness + verifiable audit / Piloto y auditoría verificable | Tenant isolation, FW-021 local SHA-256 hash chain and tamper tests, restore drills, monitoring, support, customer approval / Cadena de hashes, pruebas de alteración y operación | TODO |
| M6 | Expansion decision / Decisión de expansión | Research and validated need before payments or additional country | TODO |
| M7 (optional / opcional) | Independent audit proof / Prueba independiente de auditoría | FW-021: compare signed checkpoints, WORM and Merkle anchoring; optional blockchain adapter design and synthetic PoC with approved privacy/cost review; no real DTE on-chain / Blockchain no obligatorio | TODO |

## Mandatory gate / Puerta obligatoria
A milestone is DONE only when its acceptance evidence exists, is reviewed and accessible, and all open blockers are explicitly reported. / Un hito es DONE únicamente con pruebas revisadas y bloqueos transparentes.

## Employment-friendly evidence / Evidencia para entrevistas
For each technical milestone, save architecture ADR, code diff, automated test logs, troubleshooting notes, CI URL and 5-minute demo. Do not claim professional production experience when the result is a sandbox exercise.
