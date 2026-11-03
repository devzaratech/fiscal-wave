# ADR-0011 — Privacy by design, fiscal retention and responsible AI / Privacidad y retención tributaria

**Status / Estado:** Proposed / Propuesto · 2026-11-03 · [FW-030](https://github.com/devzaratech/fiscal-wave/issues/15)

## Context / Contexto
FiscalWave's Chile DTE includes identifiers of natural persons, signed XML/PDF, recipients and signing credentials. The new Law 21.719 may apply differently by operation, contractual controller/processor roles and future scope. Signed tax artifacts have retention constraints. / Datos personales y tributarios con deberes concurrentes.

## Decision / Decisión
- Privacy-by-design as a **cross-cutting constraint** of each service, jurisdiction and MFE; no isolated “compliance magic” microservice. / Privacidad transversal.
- Map controller/processor roles and real lawful basis per data flow; minimize defaults; per-tenant and country access, separate vault for PFX/CAF, security logs redacted, private encryption, incident response. / Bases de licitud, aislamiento y seguridad.
- Document and test data-subject rights, retention exceptions, international transfer safeguards, backup/restore and processor instructions; signed XML stays immutable until lawful retention policy says otherwise. / Derechos y preservación justificada.
- Use only synthetic data in AI prompts, model tools and CI; block automatic submission of real certificates or tax PDFs to external LLM providers. / Gobierno de IA.
- Screen high-risk data flows for EIPD and obtain local counsel review before processing real data; preserve evidence without fabricating regulator approvals. / Evaluación de impacto.
- The published law effective date is **2026-12-01** as of 2026-11-03; bill 18.623-07 postponement remains pending. Revalidate before release. / Fecha sujeta a cambio legislativo aún no aprobado.

## Alternatives / Alternativas
Treat privacy as a future add-on (too late), store all data in an immutable ledger (conflicts with rights/retention), or separate each jurisdiction Git repo as legal guarantee (does not isolate actual operations). / Alternativas rechazadas.

## Acceptance / Evidencia
Privacy data inventory, secure DSAR/incident runbooks, synthetic negative tests, audited legal basis and retention, independently reviewed release gate and original law source links. / Revisión jurídica y pruebas, no promesa de evitar multas.
