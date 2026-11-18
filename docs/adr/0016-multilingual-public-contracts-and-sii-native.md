# ADR-0016 — Multilingual Public Contracts and SII-Native Mapping / Contratos públicos multilingües y mapeo SII

**Status / Estado:** Proposed / Propuesto · 2026-11-18 · [FW-035](https://github.com/devzaratech/fiscal-wave/issues/23)

## Context / Contexto
FiscalWave's first jurisdiction is Chile, while its public API should be accessible to international English-speaking and Chilean Spanish-speaking developers. The owner requests **three mutually exclusive structural vocabularies per request**: `en`, `es-CL` and `sii-cl` (actual Chile SII element nomenclature). Each should eventually accept JSON and XML while producing consistent operations and exact SII-authoritative wire documents. / Una solicitud, un vocabulario; ninguna traducción del XML regulatorio firmado.

## Decision / Decisión
1. **Public contract modes / Modos:** `en` (English names, default canonical public contract), `es-CL` (Spanish field names), `sii-cl` (Chile-only SII-native names/structure subject to supported official XSD versions). `sii-cl` is a **jurisdiction contract**, not a third natural language. No generic global promise for other countries. / Inglés, español y dialecto normativo chileno.
2. **One vocabulary per request / Un modo:** accept a single mode per request, including nested fields. Reject unknown, mixed, duplicate or conflicting aliases rather than silently selecting a value. Business **string values** can be any language; structural field names cannot mix. / Rechazo determinista de spanglish estructural.
3. **Negotiation proposal / Selección:** candidate request header `X-FiscalWave-Contract: en | es-CL | sii-cl`; explicitly declared for alternate modes; omitted header means `en` unless a future approved API version changes that contract. `Content-Type` selects `application/json` or `application/xml`, `Accept` negotiates response media type, and `Accept-Language` localizes human-facing messages, **not** structural fields. Version public contracts explicitly. Header name/default are proposals to validate in OpenAPI tests before acceptance. / Sin autodetección por IA.
4. **Canonical application model / Dominio único:** separate request DTO/schema per representation, normalize to a single English-first application command/domain model, then apply one set of authorization, tax, folio, validation and signing rules. The external mapping layer must never own tax-authoritative calculations. / Un núcleo sin alias.
5. **SII native fidelity / Fidelidad:** `sii-cl` should preserve documented official field semantics, nesting and type constraints, including versioned mapping rather than direct exposure of internal entities. Do not claim arbitrary JSON is itself a valid SII DTE. Exact official SII XML/XSD, names, order, namespaces, signature, canonicalization and required encoding are authoritative regardless of request language. / El contrato SII manda al emitir.
6. **Separate signed import / XML firmado:** a request to **prepare or emit** a new DTE differs from **import/validate/preserve** an already signed official SII XML. Use a separately authorized operation for signed XML; never deserialize and reserialize signed XML casually, nor automatically re-sign a supplied document. / XML firmado inmutable.
7. **Parity and schema publishing / Paridad:** six future request combinations (three vocabularies × JSON/XML) require individually published machine-readable schemas where possible and tests for semantic equivalence, errors, round trips and invalid/mixed fields. Roll out incrementally: first `en` + JSON for M1, then other representations with measured use cases. / La matriz es dirección futura, no implementación presente.
8. **Stable technical values / Valores:** `INVOICE`-like enums, ISO currency codes, error codes and identifiers remain stable; error messages and portal text are localized. Supported jurisdiction extensions are typed/versioned rather than a bag of arbitrary fields. / No traducir códigos de máquina.

## Logical flow / Flujo lógico
```text
REST + JSON/XML
  ├── en schema/DTO ─────┐
  ├── es-CL schema/DTO ──┼──> normalize/validate -> application command
  └── sii-cl schema/DTO ─┘            -> fiscal owner/domain
                                          -> Chile SII adapter
                                          -> official XSD/XML/signature
```

## Alternatives / Alternativas
- Only English: smallest contract surface but excludes requested domestic ergonomics. / Insuficiente.
- Alias any field in the same request: rejected for ambiguity, difficult SDK/schema generation and security bugs. / Rechazado.
- Rename the signed SII XML into English: invalidates regulatory compliance/signature; forbidden. / Prohibido.
- Separate domain per language: high duplication and inconsistent fiscal outcomes; rejected. / Un solo dominio.

## Verification and open questions / Verificación y pendientes
- Define explicit OpenAPI request/response schemas and XML schema strategy per mode; test enforcement, duplicate-key detection and unknown-field rejection **at every nesting level**.
- Contract tests for en/es-CL/sii-cl semantic equivalence where representation is possible, with precise exceptions for legally SII-specific fields. / Equivalencia sin perder semántica.
- Confirm error status codes, header name/default, canonical naming, response negotiation, enum representation and XSD bundle/version against dated official sources **before implementation**. / Decisiones pendientes.
- Verify XML parser against XXE, oversized payload and namespace attacks; protect signature byte fidelity and tax security invariants. / Seguridad XML.
- No new tax jurisdiction, GraphQL implementation or live SII issuance is approved by this ADR.

**Related / Relacionados:** [ADR-0002](0002-fiscal-owner.md), [ADR-0004](0004-mfe-and-bilingual.md), [ADR-0009](0009-credential-custody-and-signing.md), [COMPLIANCE](../planning/COMPLIANCE.md).
