# Milestones and outcome gates / Hitos y metas

All milestones are **proposed, not complete** / Todos los hitos están **propuestos, no completados**. No fixed due dates / Sin fechas obligatorias.

| ID | Outcome (EN) / Resultado (ES) | Acceptance evidence / Evidencia de aceptación | Status |
|---|---|---|---|
| M0 | Reviewed bilingual foundation / Base documental bilingüe revisada | Docs + diagrams + agent rules + backlog merged after review / docs fusionados tras revisión | IN_PROGRESS |
| M1 | Local runnable distributed slice + quality CI / Flujo local y CI | Two APIs + shell/invoice MFE + Compose, FW-022 engineering rules and FW-023 Java/React PR build/test gate (no cloud), reproducible evidence / CI sin recursos AWS | TODO |
| M2 | Correct offline DTE flow / Flujo DTE offline correcto | DTE 33/34, signed artifacts, official schema sources, FW-022 HTTP/event idempotency with replay/conflict/timeout and concurrency/folio tests / Pruebas de idempotencia y concurrencia | TODO |
| M3 | Cost-limited AWS CI/CD lab / Laboratorio AWS y despliegue controlado | IAM/S3/Lambda/SQS, temporary ECS/ALB, FW-023 manual approved deploy and rollback, Terraform destroy evidence and actual cost review / Aprobar costos y verificar destrucción | TODO |
| M4 | Chilean official test path / Ruta oficial Chile | Authorized test issuer, SII test/certification evidence and documented outcome; no invented approvals | TODO |
| M5 | Pilot operational readiness + verifiable audit / Piloto y auditoría verificable | Tenant isolation, FW-021 cryptographic audit, FW-023 protected release/rollback, restore drills, monitoring and authorized pilot / Entrega segura con aprobaciones | TODO |
| M6 | Expansion decision / Decisión de expansión | Research and validated need before payments or additional country | TODO |
| M7 (optional / opcional) | Independent audit proof / Prueba independiente de auditoría | FW-021: compare signed checkpoints, WORM and Merkle anchoring; optional blockchain adapter design and synthetic PoC with approved privacy/cost review; no real DTE on-chain / Blockchain no obligatorio | TODO |

## Mandatory gate / Puerta obligatoria
A milestone is DONE only when its acceptance evidence exists, is reviewed and accessible, and all open blockers are explicitly reported. / Un hito es DONE únicamente con pruebas revisadas y bloqueos transparentes.

## Employment-friendly evidence / Evidencia para entrevistas
For each technical milestone, save architecture ADR, code diff, automated test logs, troubleshooting notes, CI URL and 5-minute demo. Do not claim professional production experience when the result is a sandbox exercise.
