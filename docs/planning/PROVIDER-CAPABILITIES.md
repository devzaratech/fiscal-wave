# FW-028 — Functional benchmark / Comparativa funcional

**Status / Estado:** research backlog, not delivered. Updated / Revisado: **2026-11-03**. **Objective / Objetivo:** build a compliant and commercially meaningful fiscal product, **not** clone a competitor or copy copyrighted code. / Referencia funcional, no copia de software.

## Sources / Fuentes documentales
- [LibreDTE Core supported document types](https://core.libredte.cl/docs/lib/documentos-tributarios) (updated 20 Oct 2026); [LibreDTE Pro API](https://pro.libredte.cl/docs/api) (API inventory 2026-09-30); [LibreDTE manual](https://www.libredte.cl/docs/manual/facturacion).
- [LibreDTE public API](https://www.libredte.cl/docs/api) (exchange, folio/CAF and PDF capabilities).
- [SimpleFactura public API](https://documentacion.simplefactura.cl/) (PDF/XML, timbre and issued DTE details, 2026).
- [SII certification](https://www.sii.cl/servicios_online/1039-proceso_certificacion-1184.html) and [SII XML schemas](https://www.sii.cl/servicios_online/1039-formato_xml-1184.html). SII requirements take precedence over vendors.

## Capability matrix / Matriz de capacidades
| Capability / Capacidad | Public vendor reference / Referencia pública | FiscalWave target / Objetivo | Milestone | Owner / Dueño | Status |
|---|---|---|---|---|---|
| DTE 33/34 issue, XML and XSD | LibreDTE Core, SimpleFactura | **MVP**, verify SII | M2 | fiscal-document | TODO |
| Authorized PFX certificate + CAF private key | SII instructive; LibreDTE certificate/folio API | **MVP prerequisite**, secret custody | M2/M4 | fiscal-document/credential port | TODO |
| TED/XMLDSig, PDF417 PDF | SII + LibreDTE, SimpleFactura API | **MVP**, PDF derived from immutable XML | M2/M4 | fiscal-document + PDF adapter | TODO |
| SII send, Track ID, document status/reconciliation | LibreDTE Pro SII endpoints, SimpleFactura DTE status | **MVP integration** after authorization | M4 | sii-connector | TODO |
| Receiver XML exchange, acknowledgements/rejection | LibreDTE exchange/RCV endpoints, SII certification | **Certification-critical**, test as required | M4 | sii-connector/exchange | TODO |
| Email XML + PDF to customer | LibreDTE FAQ | Phase after accepted state, privacy checked | M4/M5 | notification | TODO |
| DTE 39/41 boletas | LibreDTE Core | Later type-specific specs, no generic reuse assumptions | M6 | dedicated adapter | TODO |
| Credit/debit notes 56/61 and invoice purchase 46 | LibreDTE Core | Later source-backed rules and references | M6 | fiscal-document rules | TODO |
| Dispatch guide 52 | LibreDTE Core, SimpleFactura API | Later, separate format and legal workflow | M6 | fiscal-document/connector | TODO |
| Exports 110/111/112 | LibreDTE Core | Later, jurisdiction-specific research | M6 | fiscal-document | TODO |
| Books, RCV, received DTE and daily summary | LibreDTE Pro API/manual | Later, distinguish local reports vs official submissions | M6 | reporting/exchange | TODO |
| Assignment/factoring (AEC), cedible PDF | LibreDTE Pro, SimpleFactura cedible | Later, independent legal and partner approval | M6 | future ownership-transfer context | TODO |
| Multi-tenant API, observability, audit | FiscalWave design, vendor APIs for comparison | Cross-cutting development | M1–M5 | tenant/reporting | TODO |
| Redis/MongoDB | Technology learning/optional query & cache | Optional, never fiscal authority | M1–M6 | selected adapters | TODO |

**Not a parity claim / No afirmar paridad:** LibreDTE and others offer more functionality than the first FiscalWave release; each extension requires SII source, acceptance cases, real evidence and business validation. Product support differs by service/version; verify before marketing claims. / Soporte por producto y versión.

## Feature prioritization / Priorización
- **Must for first Chilean product slice:** DTE 33/34 synthetic → validated XML/folio/sign/timbre → PDF output → SII test/status/exchange path when eligible. / Primero completar emisión segura.
- **Next for real operations:** credential lifecycle, alerts, backups, incident recovery, SII status reconciliation and exchange. / Operación y soporte.
- **Later by validated demand:** other DTE types, factoring, books/RCV, integrations, payments and regional tax adapters. / Expansión.
- Compare API design quality, error transparency, user ergonomics, price and security without copying competitors' proprietary code or data. / Diferenciación legítima.

## Benchmark policy / Política de comparación
Every capability should include: regulation source/date, vendor public documentation/date, API/UX owner, test evidence, acceptance and honest status; avoid claims of certification until official. Consult dependency licenses before reuse. / Registrar fuentes, licencias y evidencias.
