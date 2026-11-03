# Personal data security incident / Incidentes de seguridad de datos personales

**Proposed, not rehearsed / Propuesto, no ensayado.** [FW-030](https://github.com/devzaratech/fiscal-wave/issues/15).

1. **Detect / Detectar:** authorized logs, alerts, customer/vendor reports, suspected PFX/CAF exposure, lost XML/PDF, wrong-tenant retrieval, malicious data access or AI prompt leak.
2. **Contain / Contener:** isolate impacted tenant, revoke tokens/sessions/certificates/roles as justified, halt leaking endpoint, retain forensic evidence; don't destroy signed DTE or tamper with logs.
3. **Assess / Evaluar:** determine who is controller and processor, categories/number of affected subjects, dates, jurisdictions, impact and risk to people, onward transfers and SII document consequences.
4. **Escalate / Escalar:** notify internal incident/security owner and legal counsel immediately; engage contractual processors and authorized customer contacts.
5. **Notify / Notificar:** apply **Chile-specific legal triggers and timelines verified from current law and Agency instructions**; notify authority and subjects when required. Do NOT assume a universal 72-hour GDPR deadline.
6. **Recover / Recuperar:** rotate keys, patch root cause, restore from tested backups without re-exposing deleted optional data, verify idempotent DTE state and tenant boundaries.
7. **Review / Revisar:** preserve redacted chronology, evidence, decisions, remediation, customer communications, independent audit and follow-up.

## Incident record template / Registro
- Ticket, detected_at, affected tenants/jurisdictions, owner, controller/processor, categories, risk assessment, impacted services, legal determination, notification recipients/times, mitigations, tests, open actions.
- No real PII or keys in shared issue/PR/AI prompt. / Tickets sin secretos.

## Rehearsal tests / Simulacros
- [ ] Cross-tenant invoice exposure drill (synthetic).
- [ ] Simulated stolen signing key: revoke and rotate without corrupting history.
- [ ] Credential leak in CI/AI attempt: scanner/redaction and escalation.
- [ ] Restore drills with privacy-erasure tombstone handling.
- [ ] Tabletop review of notification trigger, roles and evidence.

All exercises require human approval if they affect real infrastructure or data. / Ensayos solo autorizados.
