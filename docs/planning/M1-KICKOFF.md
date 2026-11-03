# First executable increment — FW-002 / Primer incremento ejecutable

**Status / Estado: READY TO ASSIGN after reviewed M0 merge; NOT IMPLEMENTED.** [FW-002 issue](https://github.com/devzaratech/fiscal-wave/issues/3). Read [stack baseline](STACK-BASELINE.md) and [AI selection](AI-AGENT-STRATEGY.md).

## Non-negotiable prerequisites / Prerrequisitos
- Human owner reviews and explicitly approves merging [foundation PR #1](https://github.com/devzaratech/fiscal-wave/pull/1). Its `main` base currently has only README/LICENSE; **never create a detached FW-002 PR from unmerged docs unless owner approves a dependency**.
- Select one write agent (not multiple) and inspect current `main` SHA. Create `feat/FW-002-local-ci` worktree and `coordination/tasks/FW-002.json` from the example; list exact paths that the agent may touch. Shared `.github/` edits are reviewed by owner.
- Verify tool availability JDK21/Node24/Docker and compatible Spring Boot patch; choose with version-aware docs. Zero real taxpayers/CAF/PFX and no external SII calls or cloud expenses.

## First short PR scope / Primer PR pequeño
**Goal / Objetivo:** a reproducible Java 21 + Spring Boot 3.5 Maven project builds and exposes `/actuator/health`, with JUnit tests and a GitHub Actions build job. Start with the **tenant** service only; do not create 6 empty microservices or an elaborate full country platform. / Primer servicio pequeño y verificable.

**Write scope example / Alcance ejemplo** (change only with approved task manifest):
```text
pom.xml
.mvn/
mvnw
mvnw.cmd
services/tenant/
.github/workflows/java-ci.yml
coordination/tasks/FW-002.json
README.md
README.es.md
```
Do not commit custom generated binaries unless appropriate; use standard, reviewed Maven wrapper components. Ensure third-party Actions pinned to vetted commit SHA (or document deviation). / Revisar cadena de suministro.

**Acceptance / Criterios:**
1. Java 21 compile and `mvn -B -ntp test` (or documented wrapper equivalent) pass with actual logs.
2. `/actuator/health` reports healthy in a documented local run; one test detects a deliberate regression. No real PII.
3. CI checks Maven build/tests on every relevant PR; failure propagates to a stable required status (or report the protection limitation).
4. No AWS deployment, no real DTE, no secret and no production claims.
5. PR details issue, SHA, tests run/not run, security/privacy/cost impact, README EN/ES, rollback and next step; request human review.

## Subsequent FW-002 slices / Próximos incrementos
**Second:** independent `fiscal-document` skeleton and PostgreSQL/Flyway boundaries, contract and synthetic draft + tenant isolation tests (FW-003). **Third:** React shell/invoices MFE with Node 24, React 19.3.1, TS and i18n (FW-004). **Fourth:** Compose wiring and synthetic end-to-end create/read smoke (FW-005). No SII signing/certification until M2/M4. / Incrementos pequeños, con CI y demos.

## Stop criteria / Detener si
Unknown file modifications; scope or PR conflicts; tests fail; unverified SII rule; real sensitive data in fixtures; unexpected paid resource request. Record handoff and escalate rather than inventing success. / Detener y documentar.
