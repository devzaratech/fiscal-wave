# Immediate TODOs / Pendientes inmediatos

Tasks begin **unchecked** and are checked only with linked evidence. Completed M0 tasks are marked below; other activities remain pending. / Las tareas comienzan pendientes y solo se marcan completadas con evidencia. M0 está cerrado; las demás siguen pendientes.

## M0 foundation completed / Fundamentos M0 completados
- [x] Review, approve and merge [foundation PR #1](https://github.com/devzaratech/fiscal-wave/pull/1); verify merge SHA [2548b614](https://github.com/devzaratech/fiscal-wave/commit/2548b61465c8a39790ed3cffecf910bc623b6078) / Revisión, aprobación e integración.
- [x] Validate all six architecture PlantUML diagrams with real rendering / Diagramas validados. [CI evidence](https://github.com/devzaratech/fiscal-wave/actions/runs/41601171335).
- [x] Review the M0 source, scope and legal/security disclaimers; keep unimplemented features as TODO / Alcance documental revisado. [Release review](M0-REVIEW.md).

## Next work / Siguiente trabajo M1
- [ ] Adopt [FW-032 AI selection](AI-AGENT-STRATEGY.md) and choose **one** active coding agent using evidence, cost and safety; preserve task handoff / Un solo escritor.
- [ ] Approve [M1 stack](STACK-BASELINE.md) and pin actual versions when Maven and npm manifests are created / Versiones reales.
- [ ] Execute [FW-002 first small PR](M1-KICKOFF.md) only after an approved foundation base; Java 21 tenant health/test/CI; no AWS/SII/real PII / Empezar con código funcional.

## Before public release / Antes de publicar o abrir el proyecto
- [ ] Confirm brand, initial MVP boundaries and future Apache-2.0/open-core strategy; **the existing Apache-2.0 LICENSE has not changed** / Confirmar marca, alcance y futura licencia comercial.
- [ ] Enable GitHub branch protection for this private repo if/when plan supports it. Until then require human PR review, CI and no direct main edits / Proteger main cuando sea posible (no protegida hoy).

- [ ] Main branch protection when GitHub private-repository plan supports it; never claim it is enforced while disabled / Proteger main cuando sea posible.

## Agent coordination, Chile privacy and country boundaries / Agentes, privacidad y países (FW-029–031)
- [ ] Review and merge [multi-agent protocol](MULTI_AGENT.md), verify Claude/OpenCode/Codex instructions are loaded and use separate worktrees / Verificar instrucciones y worktrees.
- [ ] Declare branch/base SHA/allowed paths per task; review other open PRs for collisions; forbid overwrites and auto-merges / Contratos y revisión humana.
- [ ] Execute agent manifest unit tests and PR ownership check; understand that this is **not** a global PR lock / Probar control sin prometer mutex.
- [ ] Verify current Law 21.719 effective date and bill 18.623-07 status before release / Verificar vigencia real.
- [ ] Complete personal data inventory, processing role and lawful basis mapping, processors, transfers, notices and retention schedule / Inventario y contratos.
- [ ] Design/verify rights (access, rectify, suppress when lawful, oppose, block, portability when applicable) and exceptions for signed DTE / Derechos y conservación fiscal.
- [ ] Establish incident/breach process, risk-based EIPD screening, per-tenant security negative tests and counsel review / Seguridad y revisión jurídica.
- [ ] Validate [country strategy ADR](../adr/0010-country-repository-strategy.md) before implementing additional jurisdictions / No dividir repos sin caso de negocio.

[FW-029](https://github.com/devzaratech/fiscal-wave/issues/14) · [FW-030](https://github.com/devzaratech/fiscal-wave/issues/15) · [FW-031](https://github.com/devzaratech/fiscal-wave/issues/16) · [Privacy](../privacy/README.md)

## Engineering standards / Estándares de ingeniería (FW-022, M1/M2)
- [ ] Review EN/ES SOLID, DRY/KISS/YAGNI, clean naming, pattern catalog, and ADR-0006 / Revisar guías y decisión.
- [ ] M1: configure compatible formatter, lint, unit tests, typecheck and CI for the **code that exists**, with real outputs / Configurar controles progresivos.
- [ ] M1: create ArchUnit rule for forbidden cross-boundary dependencies when Java modules exist / Reglas arquitectónicas.
- [ ] M2: implement HTTP idempotency key/fingerprint/conflict semantics and durable uniqueness / Idempotencia HTTP.
- [ ] M2: implement consumer inbox dedupe, event replay and unknown SII response reconciliation tests / Deduplicación de eventos y conciliación.
- [ ] Add unit/DB integration/contract/security negative tests and track results, not fabricated coverage / Pruebas con evidencia.

[FW-022](https://github.com/devzaratech/fiscal-wave/issues/7) · [EN](../en/engineering-standards.md) · [ES](../es/engineering-standards.md)

## CI/CD / Integración y entrega continua (FW-023)
- [ ] M1: Always-run PR quality gate plus selective Java Maven and React/TS jobs; do not block merges with skipped required workflows / Gate obligatorio siempre ejecutado.
- [ ] M1: Configure actual build, test, format/lint/typecheck and dependency scans as modules appear; publish redacted results / Compilar y probar código existente.
- [ ] M2: Add contract/integration/Testcontainers, idempotency/concurrency and MFE end-to-end tests / Pruebas de contrato e integración.
- [ ] M3: Build OCI images and MFE static artifacts by immutable commit/digest; prove local deployment and rollback / Artefactos inmutables.
- [ ] M3: Optional AWS lab deploy only with OIDC, approval, cost estimate, TTL, teardown and monitoring / AWS sujeto a presupuesto y permiso.
- [ ] M5: Approved production-like promotions, smoke tests, forward-only migration planning, rollback and audit / Promoción protegida.

[FW-023 issue](https://github.com/devzaratech/fiscal-wave/issues/8) · [CI/CD specification](CICD.md) · [ADR-0007](../adr/0007-cicd-delivery.md)

## First vertical increment / Primer incremento (M1)
- [ ] Scaffold Maven Java service `fiscal-document` plus `tenant` API with health endpoints / Crear dos APIs Java.
- [ ] Define OpenAPI contract, fake issuer/recipient and negative authorization test / Contrato y pruebas.
- [ ] Add PostgreSQL/Flyway and independent ownership/credentials / Datos aislados.
- [ ] Scaffold React shell + invoices MFE with `es-CL` and `en` catalogs / UI bilingüe.
- [ ] Add Docker Compose and smoke test for draft create/read / Prueba local completa.
- [ ] Add CI build/test for Java and TypeScript with no paid cloud resource / CI sin AWS.

## Redis, MongoDB and Chilean fiscal documents / Datos y ciclo DTE (FW-024–028)
- [ ] Evaluate optional Redis cache/rate limits; outages must not change folios or DTE status / Redis no autoritativo.
- [ ] Compare Mongo read projection with PostgreSQL JSONB and test rebuild and isolation / Mongo opcional.
- [ ] Design encrypted signer PFX/P12 vault, separate password, tenant permissions, expiration and rotation / Certificado firmante.
- [ ] Independently protect CAF and its private RSASK timbre key; verify authorized issuer/type/range / CAF distinto del PFX.
- [ ] Verify official SII XSD bundle, version and checksum; offline safe parser without XXE / Esquemas.
- [ ] Sign TED with CAF key; sign whole DTE using authorized signer, test invalid XML, signature and key / Timbre y firma separados.
- [ ] Render PDF/PDF417 from immutable signed XML with print and barcode-decoding tests / PDF.
- [ ] Track LibreDTE and other providers' public capabilities with realistic milestone scope / Comparativa.

[Data platforms](DATA-PLATFORMS.md) · [SII lifecycle](SII-DTE-LIFECYCLE.md) · [Provider matrix](PROVIDER-CAPABILITIES.md)

## Fiscal correctness / Correctitud fiscal (M2)
- [ ] Verify current SII DTE 33/34, CAF, XML, signature and certification specifications with dated sources.
- [ ] Implement unique folio and idempotency under concurrent load using synthetic fixtures.
- [ ] Model timeout, rejection and reconciliation before a real SII integration.

## Verifiable cryptographic audit / Auditoría criptográfica verificable (FW-021, M5/M7)
- [ ] M5: Define versioned SHA-256 hashes of the exact signed XML bytes and ordered audit events / Definir hashes versionados.
- [ ] M5: Implement append-only hash chain and tests detecting changed, deleted and reordered synthetic events / Verificar integridad.
- [ ] M5: Review tenant isolation, restricted audit access, retention and administrator rewrite threat / Revisar privacidad, retención y límites.
- [ ] M7 optional: Compare signed independent checkpoints, Merkle roots, WORM and blockchain costs and trust / Comparar alternativas.
- [ ] M7 optional: Design AuditAnchoringProvider with local stub; enable external provider only after approval / Adaptador opcional sin costos no autorizados.
- [ ] Never publish DTE, RUT, PII, CAF or certificates on-chain; blockchain does not replace SII certification / Sin datos reales ni sustitución del SII.

[FW-021 issue / Historia](https://github.com/devzaratech/fiscal-wave/issues/6) · [ADR-0005 / Decisión arquitectónica](../adr/0005-cryptographic-audit.md)

## Career skills / Competencias laborales (parallel / paralelo)
- [ ] Complete original challenge EX-01 and record Big-O + edge cases.
- [ ] Complete SQL EX-04 with window functions, EX-05 with unique constraint discussion.
- [ ] Explain in English and Spanish the diagram, ALB failover and Outbox tradeoffs.
- [ ] Publish an honest demo and test evidence in the project before using it as a portfolio claim.

## AWS money protection / Protección económica AWS
- [ ] Establish sandbox account, billing view and budgets; validate Spend limits eligibility.
- [ ] Obtain explicit cost/risk approval for any paid resource before `terraform apply`.
- [ ] Verify terraform destroy and residual resource review after every experiment.

**Next sprint candidate:** document review + synthetic draft end-to-end, not payments, international taxes or six empty services. / El siguiente sprint prioriza una experiencia vertical real.
