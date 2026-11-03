# Milestones and outcome gates / Hitos y metas

M0 is **completed as a reviewed documentation and governance foundation**; M1–M7 remain proposed. / M0 completado como base documental; M1–M7 siguen pendientes. No fixed due dates / Sin fechas obligatorias.

| ID | Outcome (EN) / Resultado (ES) | Acceptance evidence / Evidencia de aceptación | Status |
|---|---|---|---|
| M0 | Reviewed bilingual foundation + sequential AI governance / Base revisada y selección de IA | [PR #1 merged](https://github.com/devzaratech/fiscal-wave/pull/1) at [`2548b614`](https://github.com/devzaratech/fiscal-wave/commit/2548b61465c8a39790ed3cffecf910bc623b6078), docs/agent checks and actual PlantUML renders; [release review](M0-REVIEW.md) / Alcance documental auditado | DONE (documentation only) |
| M1 | Local runnable distributed slice + quality CI / Flujo local y CI | Two APIs + shell/invoice MFE + Compose, FW-022 engineering rules and FW-023 Java/React PR build/test gate (no cloud), reproducible evidence / CI sin recursos AWS | TODO |
| M2 | Validated signed XML and PDF / XML firmado y PDF verificables | DTE 33/34, synthetic PFX/CAF secret controls, official XSD, TED/XMLDSig, PDF417 print scan tests (FW-025–027), idempotency/folio/concurrency evidence / Validación offline sin certificación | TODO |
| M3 | Cost-limited AWS CI/CD lab / Laboratorio AWS y despliegue controlado | IAM/S3/Lambda/SQS, temporary ECS/ALB, FW-023 manual approved deploy and rollback, Terraform destroy evidence and actual cost review / Aprobar costos y verificar destrucción | TODO |
| M4 | Official SII test path / Pruebas oficiales SII | Authorized issuer and signer, validated DTE, PDF417 print samples, exchange, test/certification receipts; no invented approvals / Habilitación real del SII requerida | TODO |
| M5 | Privacy-reviewed authorized pilot / Piloto con revisión jurídica | Tenant isolation, cryptographic audit, protected release and FW-030 lawful processing, DSAR/retention, breach/transfer, EIPD screening, backup/restore and legal sign-off; authorized SII only / No asumir conformidad automática | TODO |
| M6 | Expansion and data decision / Expansión y persistencia | FW-024 optional Mongo vs JSONB; FW-028 research for boletas, guides, notes, books, factoring and payments, only with SII and market evidence / Expansión validada | TODO |
| M7 (optional / opcional) | Independent audit proof / Prueba independiente de auditoría | FW-021: compare signed checkpoints, WORM and Merkle anchoring; optional blockchain adapter design and synthetic PoC with approved privacy/cost review; no real DTE on-chain / Blockchain no obligatorio | TODO |

## Mandatory gate / Puerta obligatoria
A milestone is DONE only when its acceptance evidence exists, is reviewed and accessible, and all open blockers are explicitly reported. / Un hito es DONE únicamente con pruebas revisadas y bloqueos transparentes.

## Employment-friendly evidence / Evidencia para entrevistas
For each technical milestone, save architecture ADR, code diff, automated test logs, troubleshooting notes, CI URL and 5-minute demo. Do not claim professional production experience when the result is a sandbox exercise.
