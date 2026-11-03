# ADR-0007 — Independent and cost-controlled CI/CD / CI/CD independiente y controlado

**Status / Estado:** Proposed / Propuesto · 2026-11-03 · [FW-023](https://github.com/devzaratech/fiscal-wave/issues/8)

## Context / Contexto
Multiple Java microservices and React MFEs must build, test and release independently while sharing API/event contracts. Required branch checks cannot remain skipped; AWS infrastructure is financially sensitive. / Varios servicios autónomos, contratos comunes y recursos limitados.

## Decision / Decisión
- GitHub Actions as default source-controlled CI; reusable jobs per Java service and React MFE; one **always-run aggregate required job**. / CI selectivo con gate siempre ejecutado.
- Build/tests before packaging, scanning and contract compatibility. Artifacts identified by immutable commit or digest. / Probar antes de empaquetar, artefactos inmutables.
- Explicit environment approvals for deployment; AWS GitHub OIDC role with least privilege (no static AWS keys); no deployment from untrusted PRs. / OIDC y entornos protegidos.
- No paid AWS CI/CD deployments until owner authorizes cost/region/TTL and teardown. / No crear cargos automáticamente.
- Compatibility-first migrations, health/smoke/observability and manual rollback plan for protected releases. / Migraciones compatibles y reversión controlada.

## Alternatives / Alternativas
Jenkins self-hosted may offer learning value but introduces operation/patching burden; AWS CodePipeline can be reconsidered when real cloud traffic/teams justify it. Many independent repos introduce versioning coordination overhead at present. / Jenkins y CodePipeline son opciones, no requisitos iniciales.

## Consequences / Consecuencias
Reusable CI templates and dependency-aware change detection require maintenance; required status aggregator must reflect failed jobs reliably. Deployments require IAM, billing and SII legal readiness checks. / Mantener pruebas, compatibilidad y seguridad.

**Implementation evidence / Evidencia:** current doc-only `docs-check.yml` exists; all app and deployment pipelines TODO. [Full specification](../planning/CICD.md).
