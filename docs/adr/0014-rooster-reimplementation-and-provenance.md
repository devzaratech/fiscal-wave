# ADR-0014 — ROOSTER Reimplementation and Provenance / Reimplementación de ROOSTER y procedencia

**Status / Estado:** Proposed / Propuesto · 2026-11-18 · [FW-035](https://github.com/devzaratech/fiscal-wave/issues/23)

## Context / Contexto
ROOSTER (2015–2017) is recovered legacy code, not the FiscalWave production foundation. A prior static review inspected **189 Java files** including adapted `cl.nic.dte` material, Java 7, Spring Boot 1.2.5 and historical JSON→XML, CAF timbre, PKCS#12 signer, signed envelope, PDF and SII certification-path code. The static inspection **did not** compile/run the service, certify with SII or establish full third-party copyright ownership. Legacy security findings include credential logging/plaintext PFX passwords, unsafe SQL construction, SSL bypass, unbounded retries and encoding/signature hazards. / El código histórico sirve para estudiar comportamiento, no para trasladar dependencias obsoletas.

## Decision / Decisión
1. **New platform, not an in-place upgrade / Plataforma nueva:** implement FiscalWave with current supported Java/Spring stack, owned domain boundaries and versioned contracts. Do not import `cl.nic.dte` wholesale, keep a runtime reliance on archived NicLabs code, or claim its intellectual property is owned exclusively by FiscalWave. / Reimplementación independiente.
2. **Preserve evidence / Preservar:** archive original ZIPs, Git history and checksums privately without modifying originals; audit license notices, author provenance, bundled dependencies, credentials and customer data before any publication. Never push raw legacy source or real secrets to the public repository. / Archivo histórico privado.
3. **Characterize and verify / Caracterizar:** obtain synthetic fixtures for supported legacy behavior, starting with DTE type **52** (the best-supported historical code path). Test XML/XSD, TED, signer signature, envelope, PDF and fault cases in an isolated/offline laboratory with test credentials. Treat historical outputs as clues; **current official SII specifications are authoritative**. / Pruebas de caracterización, no homologación automática.
4. **Implementation boundary / Límite de implementación:** establish independent FiscalWave canonical domain and interfaces for schema registry, folio allocation, CAF/TED, signing, validation, transport and rendering. Prefer maintained libraries for generic cryptography/XML; do not rewrite standards implementations merely to claim zero dependencies. / Motor propio con dependencias mantenidas.
5. **Schema provenance / Esquemas:** source official SII XSD bundles, record URLs/retrieval dates, hashes, dependencies and supported document types. Harden XML parser against XXE; test encoding, namespaces, canonicalization and verification on the exact signed representation. Regulatory files and third-party libraries retain any applicable rights/notices. / XSD oficiales versionados.
6. **Clear ownership / Titularidad:** inventory third-party and adapted sections; legal review determines whether any reused source can be distributed under PolyForm and a separate commercial agreement. Similar behavior/functionality does not itself establish a copyright-clean implementation; preserve provenance of generated or adapted code. / No declarar independencia legal sin análisis.
7. **Controlled progression / Alcance:** start with a small demonstrable vertical slice, not a rewrite of every ROOSTER subsystem or every DTE type. Maintain separately testable adapters for Chile; no production SII or real issuers until official eligibility and certification gates are met. / Entregas incrementales.

## Alternatives / Alternativas
- Upgrade ROOSTER in place: rejected for tight legacy coupling and security/maintenance debt. / Refactorización directa descartada como producto.
- Copy NicLabs engine into FiscalWave: rejected pending rights and security review; defeats independence. / No copiar motor heredado.
- Reimplement XMLDSig cryptography from primitives: rejected as default; prefer established reviewed implementations with independent verification. / Evitar criptografía artesanal.

## Traceable migration map / Mapa verificable
| Legacy behavior | New boundary | Required proof |
|---|---|---|
| JSON/XML transformation | Request adapters + canonical domain + Chile mapper | Contract equivalence and official XSD |
| CAF/timbre | Fiscal owner + protected key port | Range, tenant and TED signature tests |
| PFX/DTE/envelope signature | Key custody and signer port | Independent signature verification and tamper tests |
| SII upload/TrackId | Chile SII connector | Fake server, retry bounds and uncertain-outcome reconciliation |
| XSL/PDF | Read-only document renderer | Immutable XML source, PDF417 decodability |

## Acceptance / Aceptación
- A reviewed SBOM/license provenance inventory for any code actually introduced, with links to third-party notices and legal review blockers.
- Historical reference fixtures synthetically recreated where possible; immutable signed XML, nonduplicated folios and recoverable SII-outcome tests before functional claims.
- No bundled ROOSTER/NicLabs source or live credential copied to the public product merely for convenience.
- Compliance source version/date recorded when each fiscal rule is implemented, referencing [COMPLIANCE](../planning/COMPLIANCE.md) and [SII lifecycle](../planning/SII-DTE-LIFECYCLE.md).

**Non-goal / Fuera de alcance:** certify SII, migrate real customer data, declare clean-room legal status, or adopt a complete microservice platform in this documentation task.
