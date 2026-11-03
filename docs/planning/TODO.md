# Immediate TODOs / Pendientes inmediatos

Every box is **unchecked by default** and must be backed by evidence before it can be ticked. / Ninguna tarea se considera hecha sin evidencia. These are proposed next actions, not completed work.

## Foundation / Fundamentos (M0)
- [ ] Review and merge bilingual foundation PR / Revisar y fusionar PR documental.
- [ ] Confirm brand, MVP boundaries and Apache-2.0/open-core strategy before publishing / Confirmar marca, alcance y licencias.
- [ ] Validate architecture PlantUML with an actual renderer (marker checks alone are insufficient) / Validar los diagramas con PlantUML real.
- [ ] Set GitHub branch protections, review flow and issues/milestones as desired / Configurar protección de rama y tablero.

## First vertical increment / Primer incremento (M1)
- [ ] Scaffold Maven Java service `fiscal-document` plus `tenant` API with health endpoints / Crear dos APIs Java.
- [ ] Define OpenAPI contract, fake issuer/recipient and negative authorization test / Contrato y pruebas.
- [ ] Add PostgreSQL/Flyway and independent ownership/credentials / Datos aislados.
- [ ] Scaffold React shell + invoices MFE with `es-CL` and `en` catalogs / UI bilingüe.
- [ ] Add Docker Compose and smoke test for draft create/read / Prueba local completa.
- [ ] Add CI build/test for Java and TypeScript with no paid cloud resource / CI sin AWS.

## Fiscal correctness / Correctitud fiscal (M2)
- [ ] Verify current SII DTE 33/34, CAF, XML, signature and certification specifications with dated sources.
- [ ] Implement unique folio and idempotency under concurrent load using synthetic fixtures.
- [ ] Model timeout, rejection and reconciliation before a real SII integration.

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
