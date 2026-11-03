# FW-025/026/027 — Chilean DTE lifecycle / Ciclo documental de DTE Chile

**Status / Estado: proposed, NOT implemented, NOT SII-certified. / Diseño, sin implementación ni certificación.** [FW-025 credentials](https://github.com/devzaratech/fiscal-wave/issues/10) · [FW-026 schemas & signing](https://github.com/devzaratech/fiscal-wave/issues/11) · [FW-027 PDF](https://github.com/devzaratech/fiscal-wave/issues/12). [Sequence map / Diagrama](../architecture/sii-signing-and-pdf.puml).

## Critical separation of cryptographic credentials / Separación de credenciales
| Purpose / Propósito | Material / Material | Operation / Operación | Rule / Regla |
|---|---|---|---|
| Sign complete DTE / Firmar DTE completo | Authorized signer certificate + private key, often imported from PKCS#12 `.pfx/.p12` | XMLDSig over defined XML scope | Verify signer authorization, validity, revocation and current SII crypto specification |
| Electronic fiscal stamp / Timbre TED | SII-issued CAF for issuer, DTE type, authorized folio range **and its separate private timbre key** | Sign TED / `DD` using CAF key; include TED in XML and produce PDF417 graphic | Never treat PFX key as the CAF key; protect both separately |
| Print representation / Representación PDF | Existing immutable signed XML including TED | Render visible fields and PDF417 encoding TED | PDF does not replace official XML; PDF is not a substitute certificate |

Sources / Fuentes: [SII technical instructions, 28 Oct 2021](https://www.sii.cl/factura_electronica/factura_mercado/instructivo_emision.pdf), [SII current online technical instructions](https://www.sii.cl/factura_electronica/factura_mercado/instructivo.htm), [SII certification stages](https://www.sii.cl/servicios_online/1039-proceso_certificacion-1184.html). Historical SII formats name legacy signing algorithms: **do not replace or assume allowed algorithms without verifying the current version for each document and environment**. / Algoritmos bajo especificación vigente, nunca improvisados.

## PFX and CAF vault / Bóveda de PFX y CAF (FW-025, M2)
- Secure upload/import only from **authorized signer**; validate PKCS#12 format, key/certificate match, chain, serial/fingerprint, dates, issuer mapping and authorization. Never automatically trust uploader. / Importar y verificar firmante.
- Store encrypted artifacts with per-tenant and per-issuer ACL, separate passphrase from encrypted PFX, envelope-encrypted backup, no plaintext in repositories, Terraform, test artifacts, job logs, Redis or MongoDB. / Contraseñas y claves protegidas por separado.
- CAF archive has issuer, DTE type, authorized range, provenance and authenticity verification; private `RSASK` protected as secret. Strict audit of reads/sign operations. / CAF y llave privada en bóveda.
- Rotate, revoke and expire credentials with alerts and runbooks; determine policy for signed historical documents without rewriting XML. / Renovación y revocación sin reescribir DTE.
- Java PKCS12 provider/adapter is replaceable by approved external vault/HSM/key service. **AWS Secrets Manager can hold binary secrets up to 65,536 bytes**, but usage and per-secret charges must be reviewed; alternatives: private encrypted object storage + separate secrets manager, or HSM when justified. Avoid forcing certificate uploads into paid AWS. / Alternativas locales y costos.
- Negative tests: wrong password, malformed archive, tenant/issuer mismatch, expired/revoked cert, corrupted CAF, unauthorized private-key request, backup restore and secret leak scan. / Pruebas negativas.

## Official XML & XSD / XML y XSD oficiales (FW-026, M2)
- Source SII [official XML schema index](https://www.sii.cl/servicios_online/1039-formato_xml-1184.html) lists the classical DTE/EnvioDTE set: `EnvioDTE_v10.xsd`, `DTE_v10.xsd`, `SiiTypes_v10.xsd`, `xmldsignature_v10.xsd`. Includes other **separate** schemas for boletas, exports, exchange, books, responses, receipts, consumption. / Esquemas separados por familia.
- Download and verify **official** releases, source URL, retrieved date, document type, checksum, compatibility and redistribution terms before vendor into Git. Use a pinned, offline, versioned schema bundle in CI/tests; do not fetch arbitrary remote `schemaLocation` in a production XML parser. / Versiones verificadas y sin XXE.
- Validation layers: well-formed XML; offline XSD; business and mandatory fields; monetary and folio constraints; CAF authenticity; TED signature; XMLDSig and signer validity. No XSD test alone proves SII acceptance. / Validación en capas.
- Use secure XML parsing: disable XXE/external entities and network resolver, size/depth limits, known encodings, canonicalization and schema-specific signatures. / Parser seguro.
- Construct DTE with authorized folio and timbre, then sign whole XML per current SII source; immutable signed artifact, digest and audit. EnvioDTE/envelope and responses have separate tests and state machine. / Timbre, firma, envío y estados.
- Testing must include 33 (afecta) and 34 (exenta), synthetic CAF/PFX fixtures, malformed XML, altered signature, wrong folio, namespace errors, accents and independent validation. / Pruebas por tipo.

## PDF/PDF417 rendering / PDF y timbre impreso (FW-027, M2–M4)
- Input is **stored immutable signed XML**, never a mutated intermediate PDF-based fiscal source. Rendering is a derived, versioned artifact with checksum and documented source XML ID. / PDF derivado del XML.
- Produce legible invoice print layouts with header, issuer/receptor, type, folio, totals, line items and references and the **PDF417 of TED**, not a generic QR replacing it. / PDF417 tributario, no QR genérico.
- Consider Apache PDFBox for PDF and a PDF417-capable barcode renderer (e.g., ZXing) as candidates, subject to compatibility/license/quality review, not mandated upfront. / Evaluar bibliotecas.
- Test PDF417 decode, print/dpi, long strings and multi-page, Chilean characters, font embedding, differing locale only in UI—not in legal fields—and template fidelity versus official SII samples. / Validar impresión real.
- PDF attachments, download, exchange and customer email require access-control, redaction and delivery status. XML retained according to SII; no customer data in CI. / Control de acceso y retención.
- SII certification has **print samples** and **interchange tests** separate from XML schema validation. / Certificación incluye muestras e intercambio.

## Sequence of functional gates / Puertas de entrega
**M1:** DTE synthetic draft and schema discovery, adapter boundaries and threat model.  
**M2:** secure synthetic credential vault, CAF/folio and TED/XMLDSig behavior, schema tests, minimal XML-derived PDF/PDF417 with offline tests.  
**M4:** official SII certification/test sets, print samples, interchange/status, only for legally authorized issuer and document types.  
**M5:** production readiness: audit, backup/restore, credential rotation, operational monitoring, privacy and recovery.

### Authoritative sources / Fuentes
- [SII XML formats and schemas](https://www.sii.cl/servicios_online/1039-formato_xml-1184.html)
- [SII technical instructions](https://www.sii.cl/factura_electronica/factura_mercado/instructivo.htm)
- [SII emission instructive, version 28 Oct 2021](https://www.sii.cl/factura_electronica/factura_mercado/instructivo_emision.pdf)
- [SII certification stages](https://www.sii.cl/servicios_online/1039-proceso_certificacion-1184.html)
- [SII DTE retention FAQ, updated 26 Feb 2025](https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_1455.htm)
- [AWS Secrets Manager binary value quota](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_limits.html)

These references must be rechecked against current SII requirements at implementation time. / Verificar versiones actuales antes de codificar.
