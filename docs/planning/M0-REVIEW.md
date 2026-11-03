# M0 release review / Revisión de cierre de M0

**Reviewed on / Revisado:** 2026-11-03. **Scope:** architecture-and-governance foundation only, not implemented application features. / Base documental, sin aplicación construida.

## Evidence / Evidencia verificable
- [Foundation PR #1](https://github.com/devzaratech/fiscal-wave/pull/1): bilingual architecture, ADR-0001–0011 (proposed), Scrum/backlog, SII lifecycle, privacy plan, multi-agent and sequential AI strategy, CI design, local cost restrictions. / Arquitectura y políticas.
- [Documentation checks](https://github.com/devzaratech/fiscal-wave/actions/runs/41600280153): local links/document structure, six real PlantUML syntax checks and SVG rendering passed on reviewed head before final fixes. / Comprobación ejecutada; volver a ejecutar en último SHA.
- [Agent scope checks](https://github.com/devzaratech/fiscal-wave/actions/runs/41600280187): Python tests, manifest scope and GitHub PR file overlap check passed before final fixes. / Revalidar último SHA.
- [Chile privacy plan](../privacy/CHILE-21719.md): legal role mapping, individual rights, official sources and retention/incident framework, **all operating controls TODO**. [Official Law 21.719](https://www.bcn.cl/leychile/navegar?i=1209272) and bill 18.623-07 still under congressional consideration on the review date. / No afirmar certificación legal.
- [Country repository strategy](../adr/0010-country-repository-strategy.md): monorepo with isolated jurisdiction modules initially; repo separation is not data isolation. / Decisión reversible.
- [FW-032 selection and handoff](AI-AGENT-STRATEGY.md): one active write agent per issue, decisions and tests in Git, independent read-only review after writer finishes. / Sin dependencia de memoria de agente.

## Reviewed architecture choices / Decisiones examinadas
- One consistent `fiscal-document` authority for folios/DTE, transactional PostgreSQL, CAF and signer PFX **independent**, SII connector owns submission only. / Integridad fiscal.
- Local Compose and synthetic data first; no real SII credentials or production tax issuance, no billable AWS. / Sin gastos ni claves reales.
- Only the minimal `tenant` Spring Boot service is first FW-002 slice. Full Java/React/DB CI remains M1; no false claims about working services. / Primer incremento pequeño.

## License / Licencia
- Root `LICENSE` in `main` already states **Apache-2.0**. M0 leaves it unchanged; no claim that proprietary or open-core module licensing has been decided. / No alterar licencia.
- Any later proprietary modules, third-party SII schemas, generated code and externally contributed source require explicit per-artifact license/attribution review **before redistribution**, and human approval for any license change. / Estrategia comercial futura pendiente.
- Private repository stays private; this merge neither publishes it nor authorizes public release. / Sin publicación automática.

## Safety corrections during M0 review / Correcciones
- OpenCode review profile uses stable documented `permission` keys; actual installed version MUST verify effective read-only permissions, especially if using OpenCode V2. / Verificación local requerida.
- Task owner tool name accepts safe slugs (including Antigravity/other providers), avoiding provider lock-in; scope tests cover accepted and rejected names. / Agnóstico de proveedor.
- SII signing diagram now expresses an isolated **CAF signature operation**, not exporting CAF private signing key to the fiscal service. / Firma sin exponer clave privada.

## Explicit limits / Límites que NO bloquean M0 documental
- `main` is **unprotected** in the private repository. GitHub's current plan restrictions prevent rulesets; manual PR review remains necessary. Later enable PR/check enforcement when supported. / Control de integración pendiente.
- No actual local OpenCode/Claude/Codex configuration execution demonstrated; files are instructions, not an enforced sandbox. / Validación con herramienta real antes de asignar.
- No implementation or legal review of Chile data-protection compliance, no SII certification, no Java/React builds, no cloud resources, and no runtime privacy tests. / Producción no autorizada.
- The detailed architecture, frontend composition and Apache-2.0 vs future business model choices remain *proposed or deferred*, not production-ready sign-off. / Hitos posteriores.

## Closure checklist / Lista de cierre
- [x] Review source and scope against M0, including safety and privacy claims / Alcance y riesgos revisados.
- [x] Review license status without modifications / Licencia existente revisada.
- [x] Identify prior diagram rendering CI evidence / Diagramas previos validados.
- [ ] Both mandatory documentation + agent CI workflows green on **final** PR head / CI verde último SHA.
- [ ] Owner authorizes review completion and PR merge / Propietario autoriza merge.
- [ ] Verify `main` contains reviewed files and record merge SHA / Verificar integración.
- [ ] Start FW-002 **only after** successful merge and fresh base SHA / Nuevo desarrollo posterior.

**M0 completion rule:** marked complete only after all release checks pass and GitHub confirms a merge to `main`; document review is not a substitute for source control evidence. / No cerrar por mera documentación.
