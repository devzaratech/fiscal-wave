# ADR-0009 — Secure PFX/CAF custody and SII signing / Custodia y firma SII

**Status / Estado:** Proposed / Propuesto · 2026-11-03 · [FW-025](https://github.com/devzaratech/fiscal-wave/issues/10) · [FW-026](https://github.com/devzaratech/fiscal-wave/issues/11) · [FW-027](https://github.com/devzaratech/fiscal-wave/issues/12)

**Context / Contexto:** The authorized signer certificate and the SII-issued CAF timbre key are **different** cryptographic materials. PDF is a derived representation, while tax-authoritative content must satisfy official XML/XSD and official authorization. / Firmante, CAF y PDF son roles distintos.

**Decision / Decisión:**
1. A per-tenant, per-issuer credential port manages encrypted PKCS#12 and separate protected CAF private key, with expiry/revocation, audit, least privilege and rotation. / Bóveda con aislamiento.
2. Only fiscal-document owns CAF range/folio transaction, TED generation and signed XML. SII connector sends signed immutable document, never allocates folios. / Un dueño fiscal transaccional.
3. Official versioned XSD bundles validated offline with hardened XML parser; cryptographic algorithms and canonicalization follow **current** SII source, even if legacy algorithms require isolated compatibility. / Esquemas y firma bajo norma vigente.
4. PDF rendering is read-only from immutable signed XML, includes correct PDF417 TED and is tested against SII print requirements; no PDF modifies XML. / PDF derivado y validable.
5. Production credential imports, SII submissions, and cloud storage require legal eligibility and explicit human approval. / Autorización previa.

**Consequences / Consecuencias:** More security engineering and SII-specific testing but avoids conflating timbre/private certificate or falsifying DTE validity. / Mayor seguridad y complejidad justificada. No active implementation yet.
