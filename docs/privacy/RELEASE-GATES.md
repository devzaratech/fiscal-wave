# Privacy release gates / Puertas de entrega de privacidad

Each checkbox is **TODO** until evidenced; this is not an assertion of compliance. / Pendientes, no certificación.

## M0–M1: design before personal data / Diseño previo
- [ ] [FW-030](https://github.com/devzaratech/fiscal-wave/issues/15): counsel-approved legal inventory, controller/processor allocation, lawful purpose map and privacy notices EN/ES.
- [ ] Minimize collected fields; tenant isolation, access roles, vault separation and private logs documented.
- [ ] [FW-031](https://github.com/devzaratech/fiscal-wave/issues/16): national adapter boundaries and cross-border data flows mapped, with no assumption that Git repo separation meets legal transfer requirements.
- [ ] Shared AI agent prompts and CI use synthetic data only, no original taxpayers' XML, RUT or PFX/CAF keys.
- [ ] Review actual effective date of Law 21.719 and bill 18.623-07 before any launch.

## M2–M4: testing and authorized SII / Pruebas y SII
- [ ] Access-denied tests across tenants and jurisdiction-scoped roles.
- [ ] Record real source and retention obligations for XML/PDF, audit events, logs and backups.
- [ ] Simulated rights requests: access, rectify, suppress, oppose, block, portability eligibility, exceptions and audit.
- [ ] Document EIPD/DPIA screening and risk-mitigation decisions for any high-risk processing before operations.
- [ ] Test unauthorized PFX/CAF read, expiration, SII XML/PDF transport and vulnerability controls.
- [ ] Incident response tabletop, processor contracts and subprocessors/transfers reviewed.

## M5: pilot gate / Puerta piloto
- [ ] Actual source-backed law and SII review and signed contractual privacy roles/terms.
- [ ] Operational privacy requests and breach handling with authorized owner and legal review.
- [ ] Tested backups, purge/retention and logs excluding private data.
- [ ] Lawful issuer authorization, valid certificate and SII test evidence as necessary.
- [ ] Independent review records: risk owner, go/no-go decision, tests executed and unresolved blockers.

**No automatic “compliant” banner in product UI. / Sin sello automático de cumplimiento.**
