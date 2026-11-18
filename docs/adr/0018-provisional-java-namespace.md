# ADR-0018 — Provisional Java/Maven Namespace and Migration Safety / Namespace Java/Maven provisional y migración segura

**Status / Estado:** Proposed / Propuesto · 2026-11-18 · [FW-036](https://github.com/devzaratech/fiscal-wave/issues/25)

## Context / Contexto
FiscalWave is being developed before AxiomSur Technologies owns a verified corporate internet domain. The GitHub organization `axiomsur` exists, but the project may still be hosted under a different repository owner while it is transferred. Purchasing a domain is not an MVP prerequisite. The owner explicitly declares `io.github.axiomsur` **provisional**, rather than a permanent corporate namespace. / FiscalWave comienza sin dominio corporativo propio; el namespace ligado a GitHub es **provisional** y no obliga a comprar un dominio.

Renaming Java packages is generally manageable early, but can become a breaking binary/API change after SDK publication or when class names leak into persisted data, security policies or wire contracts. Maven `groupId` is not the same thing as a Java `package`, nor is a GitHub repository URL. / Separar esas tres identidades evita migraciones innecesarias y cambios incompatibles.

## Decision / Decisión

1. **Provisional identity / Identidad provisional.** Use `io.github.axiomsur.fiscalwave` as the root for FiscalWave-owned Java code, with descriptive lower-case domain/module subpackages; avoid the personal account name. Use `io.github.axiomsur` as the **provisional Maven groupId** for project-owned modules unless a later artifact-specific decision justifies otherwise. Example: `io.github.axiomsur.fiscalwave.fiscaldocument.domain`. The organization slug is not the legal business name. / Paquetes por dominio, no por titular personal.

2. **Not a forever commitment / No es definitivo.** A future, controlled corporate domain may justify `com.axiomsur.fiscalwave` or `cl.axiomsur.fiscalwave` **only after its registration/control and namespace verification as applicable**. This ADR neither approves purchasing a domain nor mandates a later rename. Domain registration, code packages, GitHub organization and Maven Central namespace verification are distinct processes; a GitHub Organization does **not** automatically grant publishing rights for `io.github.axiomsur` on Maven Central. / No suponer verificación ni cambio automático.

3. **Keep names internal / No filtrar FQCN.** Never make Java fully qualified class/package names, Maven coordinates, or GitHub owner strings authoritative identifiers for fiscal documents, folios, tenants, business records, security principals, HTTP paths, OpenAPI/AsyncAPI schemas, events, queues/topics, webhooks, public error codes, audit event types or idempotency keys. Use stable, versioned business identifiers and contract schemas. Framework diagnostics/stack traces may naturally contain class names but cannot be treated as public contracts. / La identidad técnica no debe formar parte de contratos ni claves de negocio.

4. **Persistence and serialization / Persistencia y serialización.** Persist domain facts and stable schema/type identifiers, **not** `Class.getName()` / FQCN, framework-specific Java polymorphic type names, implementation classes or enum class names. Audit ORM discriminator values, Jackson type metadata, reflection strings, JPA/entity scans, class-based job serialization and message type headers before adopting a library or format. Keep DB migrations and DTE history independent from package renames. / Evitar referencias de implementación en datos durables.

5. **Boundaries and configuration / Límites y configuración.** Keep a cohesive root package per Spring Boot executable; prefer normal component scanning from that root or explicit narrowly scoped configuration. Track required explicit references (`@ComponentScan`, `@EntityScan`, `@EnableJpaRepositories`, MyBatis aliases/mappers, security rules, `module-info.java`, reflection/native-image configuration, generated sources, manifests, tests, static-analysis rules, build/deployment scripts). Do not derive external service IDs, telemetry names or configuration keys from package paths. / El cambio debe ser mecánico y auditable.

6. **External compliance independence / Independencia normativa.** Package refactoring must not rewrite signed Chile SII XML, change XML namespaces/XSD versions, re-sign existing DTE or change legally meaningful persisted artifacts. DTE wire formats and signatures remain governed by official SII requirements, not by the Java namespace. / Los XML firmados se mantienen inmutables.

7. **Publishing and compatibility / Publicación y compatibilidad.** Before publishing a reusable Java library/SDK, verify the Maven Central namespace separately. Once artifacts are consumed externally, package migration can break Java imports, reflection and binary compatibility; a `groupId` change affects dependency resolution separately. Assess a **major version**, migration guide, temporary compatibility adapters where feasible, and Maven relocation POMs for changed coordinates. Never promise a transparent rename, and never rewrite published artifacts in place. / Versionar y comunicar cualquier cambio incompatible.

8. **Independent repository relocation / Repositorio independiente.** Transferring `devzaratech/fiscal-wave` to `axiomsur/fiscal-wave` (if/when approved) is **not** a technical trigger to rename packages or Maven coordinates. Git remotes, issue/CI references, permissions and secrets need their own transfer checklist. / Mover el repositorio no obliga a migrar Java.

## Example / Ejemplo

```xml
<groupId>io.github.axiomsur</groupId>
<artifactId>fiscalwave-api</artifactId>
<version>0.1.0-SNAPSHOT</version>
```

```java
package io.github.axiomsur.fiscalwave.fiscaldocument.domain;
```

These are naming conventions for future implementation, **not a statement that code or Maven Central publications already exist**. / Son referencias objetivo, no despliegues realizados.

## Migration trigger and runbook / Condición y procedimiento de migración
**Trigger / Condición:** the organization controls and has verified (where necessary) a corporate domain/namespace, and a documented cost–benefit assessment justifies changing the existing identity. Prefer deciding before any public Java SDK release. A separate reviewed PR must approve the actual migration. / Solo migrar cuando exista un beneficio y una identidad demostrable.

1. **Inventory / Inventario:** search source, tests, configuration, Maven parent/child POMs, SBOMs, generated code, reflection, metadata, docs, CI, Docker/Helm, consumers and persisted fields for old FQCN/groupId and repository owner references; classify public vs private usages.
2. **Compatibility plan / Compatibilidad:** list affected published coordinates and binary APIs; decide version/relocation/adapter and notification strategy; inventory serialization and database histories.
3. **Mechanical refactor / Refactor:** use IDE-aware package moves; update groupIds independently, only where explicitly planned; preserve module responsibilities, endpoint schemas, message contract types and SII XML.
4. **Verification / Pruebas:** build/test every Java module; execute unit, integration, ArchUnit, serialization round-trip, DB migration, application context startup, OpenAPI/AsyncAPI contract, event consumer and deployment smoke tests as applicable. Scan for obsolete prefixes and compare externally visible contracts and signed-artifact hashes.
5. **Release gate / Aprobación:** review the diff and compatibility report, evidence, rollback path and consumer migration notes. No merge, production deploy or artifact publication without owner approval. / Evidencia antes de liberar.

## Alternatives and consequences / Alternativas y consecuencias
- **Buy a domain now / Comprar ya:** avoids a future rename but adds unnecessary MVP cost; not required.
- **Use personal GitHub username / Usar usuario personal:** rejected as a brand dependency.
- **Invent `com.axiomsur` without control / Inventar namespace:** rejected as an assertion of an identity the project does not yet control.
- **Rename immediately on GitHub transfer / Renombrar por transferencia:** rejected; different concern.

**Trade-off / Costo:** a clear temporary namespace now in exchange for a potentially breaking, but planned, migration later. The most effective mitigation is preventing namespace leakage into durable/public contracts. / Migración potencial futura, sin acoplamiento accidental.

## Acceptance and scope / Aceptación y alcance
This ADR only proposes naming and migration guardrails. It does **not** change existing packages, Maven artifacts, SII integrations, billing resources, licenses, domain ownership or deployment. Verification of rules is **pending implementation**; document-only review is not a substitute for Java test execution. / Se registra la decisión; no se declara implementación realizada.

**Related / Relacionados:** [ADR-0001](0001-repo-and-service-boundaries.md), [ADR-0006](0006-engineering-standards.md), [ADR-0010](0010-country-repository-strategy.md), [ADR-0016](0016-multilingual-public-contracts-and-sii-native.md), [AGENTS.md](../../AGENTS.md).
