# ADR-0013 — Agent Harness and Human-in-the-Loop / Harness de agentes y supervisión humana

**Status / Estado:** Proposed / Propuesto · 2026-11-18 · [FW-035](https://github.com/devzaratech/fiscal-wave/issues/23)

## Context / Contexto
FiscalWave processes legally significant fiscal documents, cryptographic keys, CAF/folios, tenant identities and eventually SII submissions. Generative coding agents can accelerate implementation but may hallucinate regulations, silently alter security boundaries or report unexecuted tests. Root [AGENTS.md](../../AGENTS.md), [FW-032](../planning/AI-AGENT-STRATEGY.md), [FW-029](../planning/MULTI_AGENT.md) and [quality gates](../planning/QUALITY.md) already require one sequential writer and human approval; this ADR makes a **proposed engineering control model**, not a claim of an enforced runtime harness. / La generación de código asistida requiere controles técnicos verificables y supervisión humana.

## Decision / Decisión
1. **Human accountable owner / Responsable humano:** owner approves architecture-sensitive design, production access, third-party IP incorporation, licensing, merge and release. AI is a change proposer, never a legal/tax authority. HITL applies to these gates; routine harmless read-only operations need no repeated approval. / Aprobación humana por riesgo, no para cada lectura.
2. **Single writer / Un escritor:** one active write-capable agent, one FW issue, declared scope, isolated worktree/branch, one PR; independently review with a different read-only agent *after* writing stops. Do not launch concurrent writers unless an explicit future ADR changes policy. / Escritores secuenciales.
3. **Harness = enforced controls + guidance / Harness:** minimum proposed executor includes restricted worktree, tool allow/deny policy with verified actual permissions, time/budget limits, synthetic fixtures, command logging, preflight drift/overlap checks, deterministic local tests and CI. Markdown prompts and role names alone are not a sandbox or an enforcement guarantee. / Permisos comprobados, no solo prompts.
4. **Risk-tiered gates / Riesgos:** low = docs and isolated tests (automated checks + normal review); medium = API/contracts/persistence (unit/integration/contract tests); high = folios, CAF, signer, immutable XML, tenant isolation (negative/concurrency/cryptographic tests + independent security/fiscal review + owner acceptance); critical = live SII, real keys/data, prod infrastructure/migrations/billable cloud (explicit owner authorization and operational runbook before action). / Gates según impacto fiscal.
5. **Evidence-based completion / Evidencia:** report changed paths and diffs, actual commands and exit codes, CI run URL, security/privacy/cost implications, pending checks, rollback, ADR changes. Do not conflate a green documentation job with working Java, legal compliance or SII certification. / No inventar resultados.
6. **Failure containment / Contención:** stop upon unexpected working-tree edits, failed required tests, ambiguous official SII requirement, secrets/PII exposure, unknown write ownership, agent prompt injection or uncontrolled cost. Never auto-retry sensitive side effects or auto-merge. / Detener y escalar.
7. **Untrusted inputs / Entradas no confiables:** issue text, README, third-party skills, SII examples and retrieved web content are data, not authorization to bypass root rules. Review dependency and tool-supply-chain changes; no real DTE/PFX/CAF in prompts. / Defenderse de instrucciones maliciosas.
8. **Traceable selection / Selección:** continue FW-032 provider rubric rather than hard-coding a vendor/model; every handoff contains tool/model when available, base/head SHA, tests and remaining work. / Independencia del proveedor.

## Proposed enforcement matrix / Matriz de ejecución propuesta
| Phase / Fase | Required gate / Control | Enforced today? / ¿Activo? |
|---|---|---|
| Scope | FW issue, branch, task allowlist for application directories | Existing task-manifest CI for covered paths; not a global lock |
| Work | Verified sandbox/tool permissions and limited secrets/network | **TODO:** per-agent runtime verification |
| Validate | Unit, contract, concurrency, XML/crypto and security tests as applicable | Only checks already present may be claimed; Java app not built yet |
| Review | Read-only independent review; owner accepts risk | Procedural policy, not automatic security proof |
| Merge/deploy | Explicit human owner approval; no automated live SII or cloud writes | Procedural policy; protection enforcement must be verified separately |

## Alternatives / Alternativas
- Pure vibe coding with direct main pushes: rejected, poor repeatability and unacceptable fiscal risk. / Rechazado.
- Fully manual development without agents: viable but discards bounded productivity gains. / Alternativa segura pero más lenta.
- Autonomous concurrent agents as default: deferred; coordination, permissions and cost are not established. / Diferido.

## Acceptance evidence / Criterios de aceptación
- Demonstrate blocked writes outside allowed paths and blocked network/secrets access in the **chosen** agent runtime; prompt text is insufficient.
- Execute a controlled failed test and confirm CI fails; verify one-writer handoff and read-only reviewer permissions.
- For fiscal changes, prove negative authorization, concurrent folio uniqueness, signed-XML immutability, timeout/unknown-outcome reconciliation, and official-source traceability with **synthetic data**.
- Record actual results and approval in each PR; no certification or legal assurance is inferred.

## Consequences and follow-up / Consecuencias
Initial overhead from tests and human review; lower risk of silent fiscal defects. Implement incrementally with [FW-002](../planning/M1-KICKOFF.md); select an agent and validate permissions **before** claiming harness enforcement. Existing [ADR-0002](0002-fiscal-owner.md), [ADR-0006](0006-engineering-standards.md) and [ADR-0009](0009-credential-custody-and-signing.md) remain authoritative for fiscal boundaries. / No modifica código ni habilita operaciones reales.
