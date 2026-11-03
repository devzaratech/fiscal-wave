# Initial application stack / Stack inicial — FiscalWave

**FW-002 planning decision / Decisión para M1 (2026-11-03). NOT YET INSTALLED.** Real dependency versions must be locked in Maven/package manifests with reproducible tests; avoid floating ranges in releases. / Son versiones objetivo, no software instalado.

| Component / Componente | M1 baseline / Base | Compatibility & verification / Validación |
|---|---|---|
| Java / JDK | **21 LTS** (OpenJDK/Temurin or appropriately licensed distribution) | Build/test on 21; optional 25 LTS matrix after dependency support verified |
| Spring Boot | **3.5.x**, latest reviewed patch at implementation | Pin explicit patch in parent POM and verify Java 21, plugins, CVEs and SII XML libs |
| Maven | Wrapper, supported compatible release | Lock wrapper checksum/version and plugins |
| Node.js | **24 LTS**, supported major | Pin `24` for local CI baseline; evaluate Node 26 Active LTS after Vite, package-manager and MFE compatibility |
| React & React DOM | **19.3.1** target, TypeScript strict | Lock exact versions + dependencies via package lock; validate i18n and MFE composition before Module Federation |
| TypeScript / Vite | Latest mutually compatible stable versions chosen on implementation | Pin exact versions in lockfile, check Node engine requirements |
| Database | PostgreSQL (supported release selected with actual Docker images) | Transaction/unique constraint and Testcontainers proof; no Redis/Mongo required for first slice |
| Local deployment | Docker Compose, no cloud | Synthetic data only, explicit health and cleanup |
| CI | GitHub Actions | Java/React checks only once modules exist; docs/agent CI already runs |

**Why 21 instead of 25 right now / Por qué Java 21:** stable financial-enterprise baseline while showing Java 25 compatibility as evidence, not risking unexpected library/support issues in SII signing. **Why Node 24 vs 26 / Por qué Node 24:** smaller compatibility gamble for tooling in the first vertical slice; Node 26 is also LTS and can be tested later. / Decisiones reversibles, sujetas a resultados.

**No paid deployment / Sin despliegues pagados.** Dokploy is an *optional* self-hosted demo target after tests, not a build dependency or required career credential. AWS IAM/ECS/ALB/Terraform remains a separate, approved cost-controlled lab.

References / Referencias:
- [Node LTS schedule](https://github.com/nodejs/Release)
- [React releases](https://github.com/facebook/react/releases)
- [Official Spring Boot reference](https://docs.spring.io/spring-boot/)
