# Chilean fiscal readiness / Preparación tributaria Chile

**No certification is claimed. / No se afirma certificación.** This document is a research/verification plan, not tax or legal advice. / Es plan de verificación, no asesoría tributaria.

## Official source of truth / Fuente oficial
- [SII Chile](https://www.sii.cl/)
- [SII facturación electrónica](https://www.sii.cl/factura_electronica/)

## Traceability matrix template / Matriz de trazabilidad
| Requirement / Requisito | Source + version/date / Fuente y fecha | Owner / Dueño | Test / Prueba | Evidence / Evidencia |
|---|---|---|---|---|
| DTE 33/34 calculations / Cálculos | TODO official source | fiscal-document | synthetic tax cases | TODO |
| CAF / folio uniqueness / Folios | TODO official source | fiscal-document | concurrent DB test | TODO |
| XML signature + PDF417 / Firma y timbre | TODO official source | fiscal-document | schema + tamper test | TODO |
| SII auth, submit and statuses / Envío | TODO official source | sii-connector | sandbox integration | TODO |
| Exchange + acknowledgments / Intercambio | TODO official source | sii-connector | contract test | TODO |
| Authorization/certification / Habilitación | TODO official SII procedure | owner + compliance | official process evidence | BLOCKED |

## Guardrails / Límites
- Real issuance only with authorized contributor, certificates and CAF. / Emisión real solo con emisor autorizado.
- Keep test/sandbox separate from production. / Separar pruebas de producción.
- Never generate or fake an official acceptance receipt. / No falsificar recepción SII.
- Signed XML remains immutable; tax corrections use the prescribed document workflow. / XML firmado inmutable.
- Boletas, RV daily summaries, guides, assignment/cesión and international rules require **separate** regulatory research. / Boletas y otros DTE requieren análisis propio.
- RCV is official; internal reporting does not replace it. / Reportes propios no reemplazan RCV.
- Personal-data, retention, accounting and business licensing obligations require jurisdiction-specific review.

## Milestone exit / Salida de hito
M4 only after legitimate issuer eligibility, official test evidence, legal review and operational runbook. / M4 depende de autorización, evidencia y revisión.
