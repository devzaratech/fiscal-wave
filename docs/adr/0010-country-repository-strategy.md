# ADR-0010 — Country boundaries before country repositories / Límites fiscales antes de separar repositorios

**Status / Estado:** Proposed / Propuesto, to validate at M0/M6 · 2026-11-03 · [FW-031](https://github.com/devzaratech/fiscal-wave/issues/16)

## Problem / Problema
Country tax law, XML/certification rules, personal-data privacy and operational access may differ. Split repositories can reduce access scope, **but cannot alone isolate databases, backups, deployments, credentials or legal processing responsibility**. / Separar repositorios no basta para evitar multas.

## Options / Alternativas
| Approach / Enfoque | Benefit / Ventaja | Cost/risk / Costo y riesgo | Choice / Decisión |
|---|---|---|---|
| **One monorepo + isolated jurisdiction modules** | Shared Spring/React/CI/infra/security fixes; consistent contracts; economical now | Enforce module ownership and tests; risk of shared CI visibility | **Preferred for initial Chile MVP** |
| Shared core + repo per country | Independent access, reviews, regulatory release; can restrict contractor code visibility | SDK/contracts duplicated or versioned, CI pipelines, release/security drift, integration complexity | Later when country-specific team/legal ownership exists |
| Separate product/repo and infra per country | Strongest potential operational segregation if *data/IAM/cloud* truly separated | More cost, duplicated compliance/security engineering, harder patch coordination | Only after verified regulatory/commercial case |

## Proposed code layout / Estructura
```text
fiscal-wave/
  services/                 # shared domain interfaces and deployable services
  apps/                     # shell + MFEs
  contracts/                # versioned API/events; no country-specific legal constants
  jurisdictions/
    cl/
      README.md             # Chile owner, applicable laws and approved versions
      schemas/              # verified SII XSD with provenance/license review
      rules/                # DTE 33/34, CAF/TED, XMLDSig
      adapters/             # SII operations, signature/PDF417
      tests/                # verified synthetic fixtures and negative tests
      privacy/              # Chile data flows, notice, retention, legal hold
  infrastructure/
    environments/           # separated accounts/regions/roles when justified
```
**Illustration only: these directories are not deployed or created as runtime components yet.** / Estructura objetivo.

## Mandatory separation independent of Git / Separación real
Per-tenant and jurisdiction scoped database roles; separate PFX/CAF vault access, IAM principals and encryption keys; backups and DTE XML/PDF by retention rules; controller/processor agreements, access approvals, data-flow inventory and cross-border transfer assessment. Geographical hosting is not universally mandated merely because a country has privacy law; assess each concrete data flow and transfer mechanism. / Aislamiento técnico y jurídico real.

## Triggers to extract a country repo / Cuándo separar
- Local company/partner/team with distinct legal controller or different contracted access; independent SII vs SAT/SUNAT certification responsibilities.
- Country-only confidential integration/crypto material or licensing restrictions requiring repo-level access isolation.
- Country release cadence, security policy and dependency risk diverge enough that monorepo permission controls cannot safely satisfy them.
- Independent operations, budgets, residency/transfer decisions and actual client demand justify duplicate CI/security patch process.
- Migration plan exists for versioned contracts, shared core dependencies, DTE histories, access and tenant data. / Migrar sin pérdida de trazabilidad.

## Decision gates / Puertas
M0/M1: document ownership and enforce country package boundary; only implement Chile initially. M6: evaluate each split through architecture ADR, security, Chile law review and actual evidence. Never claim code repository choice ensures compliance or eliminates fines. / Separación con evidencia, no promesas jurídicas.
