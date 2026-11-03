# Chilean fiscal readiness / Preparación tributaria Chile

**No certification is claimed. / No se afirma certificación.** This document is a research/verification plan, not tax or legal advice. / Es plan de verificación, no asesoría tributaria.

## Official source of truth / Fuente oficial
- [SII Chile](https://www.sii.cl/)
- [SII facturación electrónica](https://www.sii.cl/factura_electronica/)
- [SII XML/XSD catalogue](https://www.sii.cl/servicios_online/1039-formato_xml-1184.html)
- [SII technical instructive 2021](https://www.sii.cl/factura_electronica/factura_mercado/instructivo_emision.pdf)
- [SII certification stages](https://www.sii.cl/servicios_online/1039-proceso_certificacion-1184.html)
- [DTE signing/PDF plan](SII-DTE-LIFECYCLE.md)

## Traceability matrix template / Matriz de trazabilidad
| Requirement / Requisito | Source + version/date / Fuente y fecha | Owner / Dueño | Test / Prueba | Evidence / Evidencia |
|---|---|---|---|---|
| DTE 33/34 calculations / Cálculos | TODO official source | fiscal-document | synthetic tax cases | TODO |
| CAF / folio uniqueness / Folios | TODO official source | fiscal-document | concurrent DB test | TODO |
| PKCS#12 signer/PFX / Firma del emisor | SII technical instructive 2021; reverify current | credential vault | expiry/tenant/signature tests | TODO |
| CAF RSASK + TED / Llave timbre SII | SII technical instructive 2021; reverify current | fiscal-document | key separation/CAF/timbre tests | TODO |
| Official XSD / Schemas SII | [SII XML index](https://www.sii.cl/servicios_online/1039-formato_xml-1184.html) checked 2026-11-03 | fiscal-document | versioned offline validation, XXE tests | TODO |
| XMLDSig and PDF417 representation / Firma y timbre impreso | [SII certification](https://www.sii.cl/servicios_online/1039-proceso_certificacion-1184.html) checked 2026-11-03 | fiscal-document + PDF renderer | signature, print and barcode decode | TODO |
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

## Personal-data law separate from SII certification / Protección de datos independiente del SII
- [Law 21.719 readiness / Programa Ley 21.719](../privacy/CHILE-21719.md) is a separate compliance gate for personal data, including taxpayer identifiers and signed XML/PDF; [source](https://www.bcn.cl/leychile/navegar?i=1209272). / La certificación tributaria no certifica privacidad.
- [Data inventory](../privacy/DATA-INVENTORY.md), [DSAR and retention](../privacy/DSAR-RETENTION.md), [incident response](../privacy/INCIDENT-RUNBOOK.md), [privacy release gates](../privacy/RELEASE-GATES.md) all require actual implementation and legal review before production. / Controles con evidencia.
- Bill 18.623-07 may modify effective date; as reviewed 2026-11-03 the **published law still states 2026-12-01**; never assume proposed 2027 date is enacted. / No adelantar postergación.

## Milestone exit / Salida de hito
M4 only after legitimate issuer eligibility, official test evidence, legal review and operational runbook. / M4 depende de autorización, evidencia y revisión.
