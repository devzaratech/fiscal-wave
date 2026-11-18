# ADR-0015 — Versioned Agent Skills and Verification Contracts / Skills de agentes y contratos verificables

**Status / Estado:** Proposed / Propuesto · 2026-11-18 · [FW-035](https://github.com/devzaratech/fiscal-wave/issues/23)

## Context / Contexto
FiscalWave already has role prompts in [agents/](../../agents/README.md) and root [AGENTS.md](../../AGENTS.md). Those documents describe responsibilities; they are **not** independently executable, automatically installed tools or effective security permissions. Specialized repeatable procedures are useful for XML/XSD, cryptographic signing, folio concurrency, provenance and security checks. / Se necesitan procedimientos reproducibles, no solo personajes de IA.

## Decision / Decisión
1. **Version skills in Git / Versionar:** proposed future directory `skills/fiscalwave-<capability>/SKILL.md` with companion examples, test scripts and synthetic fixtures as needed. Each skill documents purpose, inputs, prerequisites, authoritative references, allowed tools, human approval points, stop conditions, commands, expected outputs and evidence. / Skill como contrato de procedimiento.
2. **Tool compatibility verified / Compatibilidad:** portability across Codex/Claude/OpenCode is a goal, **not an assumed fact**. Validate discovery conventions, frontmatter, tool permissions and read-only behavior in the actual installed runtime/version; write thin provider adapters if needed. / No prometer carga automática.
3. **Root policy precedence / Prioridad:** `AGENTS.md` and applicable ADR/issue restrictions override any skill; skills cannot self-grant cloud access, merge rights, secrets, write paths or permission to issue DTE. / Una skill no autoriza operaciones riesgosas.
4. **Skills propose, checks prove / Evidencia:** each skill must link deterministic tests and expected failure modes. A model's assertion that XML is valid or a signature passed is never proof. Store executed commands, versions and redacted results in PR/CI. / Verificación real.
5. **Supply chain and injections / Cadena de suministro:** review all skill text/scripts, lock third-party versions and inspect executable commands before adoption. Treat copied skills and tool output as untrusted; do not automatically install or execute arbitrary downloaded scripts. / Skills externas sujetas a revisión.
6. **Privacy and fiscal scope / Privacidad:** only synthetic XML, fictional identifiers and nonproduction keys by default. Prohibit PFX/CAF real material, taxpayer PII and production SII traffic in agent prompts; evaluate any exception separately with owner and legal/security controls. / Datos sintéticos exclusivamente.
7. **Small catalog first / YAGNI:** no skill framework or marketplace dependency is required for FW-002. Start with one useful reviewed skill only after a demonstrated manual procedure; do not generate dozens of unused skills. / Catálogo incremental.

## First candidates (not implemented) / Primeras candidatas
| Proposed skill | Inputs | Expected verifiable output |
|---|---|---|
| `fiscalwave-sii-schema-validation` | Pinned official XSD, synthetic XML | XSD version/hash report and pass/fail cases incl. XXE |
| `fiscalwave-dte-cryptography` | Test CAF/PFX, synthetic XML | TED/XMLDSig verification and tamper detection |
| `fiscalwave-folio-consistency` | Local PostgreSQL, concurrent synthetic commands | Unique folios, conflict and rollback tests |
| `fiscalwave-security-review` | Scoped PR, dependency manifest | Findings, severity and negative authorization evidence |
| `fiscalwave-legacy-provenance` | Private legacy inventory summary, license metadata | Reuse/attribution blockers without copying secrets |

## Required SKILL.md contents / Contenido mínimo
- Identity/version, scope, owner and trigger; explicit non-goals. / Identidad y límites.
- Preflight: FW issue, read-only/write role, baseline SHA, dependencies, source date/hash and allowed paths. / Precondiciones.
- Steps and commands with safe defaults, real permission checks and expected negative cases. / Procedimiento.
- Evidence manifest: tests actually run, artifacts/checksums, known failures, exit criteria and owner approval. / Pruebas.
- Change and rollback policy, upstream citations and license provenance. / Mantenimiento.

## Alternatives / Alternativas
Only free-form prompts: too little reproducibility; rejected as sole mechanism. Vendor-specific hidden skills: easier initially but too much lock-in; allowed only as a tested adapter. Full custom skill runtime now: deferred until an implementation need exists. / Reutilización pragmática.

## Acceptance / Aceptación
- First pilot skill demonstrated in one tool with enforced permissions, synthetic fixtures, redacted logs, intentional failure test and clear version.
- Run the same pilot in another tool **only after** compatibility verification; document differences instead of claiming portability.
- No skill installation or runtime enforcement is claimed by approval of this ADR; follow [ADR-0013](0013-agent-harness-and-human-oversight.md).

**Non-goal / Fuera de alcance:** shipping `SKILL.md` executables or selecting a permanent AI vendor within this documentation PR.
