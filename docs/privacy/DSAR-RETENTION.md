# Rights requests and retention / Derechos del titular y conservación

**Proposed runbook / Guía propuesta**, not operating automation or legal advice. [Law readiness](CHILE-21719.md).

## Intake / Recepción
1. Secure accessible request channel (EN/ES), contact and audit ticket; never expose other tenants' existence. / Canal accesible y ticket.
2. Confirm identity using proportionate verification; do not demand unnecessary sensitive documents. / Verificación proporcional.
3. Determine controller/processor relationship: platform-owned data versus customer-controlled tax content. Coordinate processor requests with controller per contract. / Rol y autoridad.
4. Classify requested right: access, rectification, suppression, opposition, blocking or portability **only under applicable statutory conditions**. / Derecho aplicable.
5. Determine data sources (PostgreSQL, XML, PDF, logs, object storage, optional Redis/Mongo, processors and backups), obligations, response windows and lawful exceptions based on current legal source. / Origen, plazos y excepción.
6. Execute eligible action across authoritative and derived stores; never rewrite signed XML to 'rectify' its fields; follow legally authorized correction documents/workflows instead. / No modificar XML firmado.
7. Record decision, legal basis, reply and evidence; minimize sensitive response contents. / Trazabilidad.

## Suppression vs mandatory retention / Supresión vs conservación
- User profile, optional analytics, duplicate contacts and disposable cache may be deleted when grounds exist. / Datos suprimibles.
- Signed fiscal XML, mandatory logs and SII evidence may require preservation; **document exception** with counsel rather than blanket denial or blanket deletion. / Retención tributaria.
- Pseudonymization/redaction is not automatically legal anonymization; evaluate re-identification risk. / Pseudonimización no equivale a anonimización.
- Backup lifecycle must prevent arbitrary restoration of erased optional PII and document retention limits. / Respaldo y restitución.
- No DSAR closure until response sent and evidence preserved / Cierre verificable.

## Proposed tests / Pruebas
- [ ] Cross-tenant access denial.
- [ ] Identify and export only eligible subject data without leaking other parties.
- [ ] Rectification updates profile but not immutable signed XML.
- [ ] Suppression propagates to optional derived stores; mandatory retention exception recorded.
- [ ] Blocking prevents applicable further processing while preserving required storage.
- [ ] Portability format and applicability validated.
- [ ] Notification and backup restoration practice with synthetic records.

No hard-coded SLA until dates and conditions verified. / Plazos pendientes de verificación legal.
