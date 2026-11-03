# FW-023 — CI/CD for microservices and microfrontends / CI/CD multiservicio y microfrontends

**Status / Estado:** proposed design, not yet implemented beyond the existing `docs-check.yml` workflow / diseño propuesto; hoy solo opera CI documental. [GitHub issue](https://github.com/devzaratech/fiscal-wave/issues/8) · [ADR-0007](../adr/0007-cicd-delivery.md).

## Operating principle / Principio operativo
**EN:** One monorepo, independently buildable and deployable Java services and React/TypeScript MFEs, coherent cross-component contracts and gradual promotion. Build and test code only where it exists. **ES:** monorepo con builds/despliegues independientes, contratos compatibles y promoción controlada; no fingir pipelines instalados.

## Pipeline stages / Etapas
| Stage / Etapa | Scope / Alcance | Trigger / Disparador | Evidence / Evidencia |
|---|---|---|---|
| PR quality gate / Gate PR | Required overall status, changed-file detector, branch protection | Every pull request to main (no workflow path filter for required check) | A stable `ci-required` job result, even if a component has no changes |
| Java CI | Maven wrapper, JDK 21, format/lint, unit, integration, ArchUnit, API contracts, security scanning | Changes to Java services or shared Java contracts | Test reports, failure evidence, coverage trend, static findings |
| Frontend CI | Node LTS, lockfile + `npm ci`, `tsc`, ESLint/Prettier, Vitest/RTL, build, optional Playwright | Changes to apps/packages or frontend contracts | Typed build, unit/E2E and i18n results |
| Contract validation | OpenAPI/AsyncAPI schemas and backward-compatibility checks | Contract changes or changed consumers/producers | Contract diff and tests |
| Package | OCI container image per service; static versioned MFE package/manifest, commit SHA or digest | Protected merge or release tag, after CI | SBOM/provenance where feasible; immutable digest |
| Dev/staging promotion | Use tested artifacts, smoke/health/telemetry, deployment logs | Explicit release workflow or environment-approved trigger | Deployment URL, version, health and rollback evidence |
| Production | Protected environment, manual approval, compatibility and tax readiness gate | Authorized owner initiates release | Signed-off checklist, release notes and rollback runbook |

## Monorepo strategy / Estrategia de monorepo
- Implement an **always-triggered** PR workflow and a **required aggregator job** (e.g. `ci-required`) that checks all applicable child jobs. / Gate requerido siempre visible.
- Detect changed paths in a job; conditionally execute service/MFE builds and dependent consumers. When shared contracts change, run all affected components. / Solo construir los afectados, con dependencias.
- **Do not mark an entirely skipped workflow as a required check.** GitHub path-filtered skipped workflows can leave required checks Pending; conditional jobs plus an always-running aggregator are safer. / Evitar gates bloqueados por filtros.
- Reusable workflows may implement per-component templates. Avoid giving every service full-repo deploy permissions. / Workflows reutilizables y mínimos permisos.

## Multi-agent scope gate / Control de agentes
The [FW-029](MULTI_AGENT.md) policy adds an unfiltered [agent-scope workflow](../../.github/workflows/agent-scope.yml) running Python unit tests and a changed-files/task-manifest allowlist for application code. This validates one PR's scope, **not concurrent PR global ownership**. `main` is currently unprotected in the private GitHub repository; human review is required. / Control local sin bloqueo global.

## Security and supply chain / Seguridad y cadena de suministro
- Default `permissions: contents: read`; grant `packages: write` only to packaging job, `id-token: write` only to approved cloud deployment job. / Token mínimo por job.
- Prefer pinned, reviewed GitHub Action **commit SHAs**; update deliberately (Dependabot/Renovate if approved). / Versiones verificadas de Actions.
- On untrusted PRs: no deploy secrets, untrusted script injection or elevated token, and no cloud role assumption. / PR externos sin credenciales de despliegue.
- For AWS: use GitHub OIDC → restricted AWS IAM role scoped to repository, environment and refs; temporary credentials, **no long-lived keys**. Keep review approval on protected environments. / AWS OIDC y autorización.
- Generate artifact digest and optional attestation/SBOM once justified, scan dependencies and images, guard against compromised third-party actions. / Identidad de artefactos y análisis de dependencias.
- Prohibit real CAF, keys, certificates, customer DTE and taxpayer PII in CI fixtures, logs and artifacts. / Solo datos sintéticos.

## Packaging and rollout / Empaquetado y despliegue
- Each backend service has separate image tag/digest and deployment configuration; frontends publish immutable versioned assets and a Shell-compatible MFE manifest. / Entregables por servicio y MFE.
- Deploy contracts before consumers when backward compatible; prefer **expand/contract** schema migrations. A rollback of code does not magically reverse database mutations. / Compatibilidad y migraciones seguras.
- For ECS/ALB lab, health checks + two target tasks, fault injection, rolling/blue-green tradeoff analysis, rollback to previous image digest. / Balanceo y reversión comprobada.
- For production fiscal services, issuing DTE requires authorized SII pathway, certificates and operational review; automated infrastructure deployment never grants regulatory authorization. / CI/CD no otorga habilitación SII.

## Financial protection / Protección de costos
- **M1/M2:** GitHub-hosted CI (check quotas/plan) + Docker Compose/Testcontainers; no AWS resources created. / Pruebas locales sin AWS.
- **M3:** temporary AWS sandbox only with owner approval, specific region/resources, Pricing Calculator estimate, IAM restrictions, alerts, bounded runtime/task count, explicit `terraform destroy` and residual billing review. / AWS autorizado y destruido.
- **M5:** never automatically destroy production services; production deployments and migration require review and incident rollback procedures. / Producción con control humano.
- Budget notifications can lag and **are not hard cost caps**; account-specific Spend limits eligibility must be verified. / Alertas no son topes garantizados.

## Acceptance by milestone / Criterios por hito
- **M1:** actual Java+React modules build/test and a required gate succeeds/fails predictably; docs-only PR does not require nonexistent app components.
- **M2:** integration/contract, tenancy and idempotency tests; replay/failure scenarios in CI.
- **M3:** cost-approved lab deployment, 2-task ALB failover, smoke, digest rollback, teardown and actual cost review.
- **M5:** protected staging/production-like release, manual approval, runbook, monitoring and database migration compatibility, only when lawful and ready.

## External references / Referencias oficiales
- [GitHub Actions security](https://docs.github.com/en/actions/how-tos/secure-your-work)
- [Required checks and skipped workflows](https://docs.github.com/en/enterprise-cloud@latest/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)
- [AWS OIDC federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html)
- [AWS GitHub OIDC trust restrictions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html)

**No deployment has been performed / No se efectuó despliegue.** All components beyond `docs-check.yml` are planned. / El resto es planificación.
