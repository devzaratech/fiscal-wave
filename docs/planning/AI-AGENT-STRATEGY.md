# FW-032 — AI-assisted engineering / Ingeniería asistida por IA

**Status / Estado: documented operating policy, not evidence of model quality or employer-certified skill.** [Issue FW-032](https://github.com/devzaratech/fiscal-wave/issues/17). This extends [FW-029](MULTI_AGENT.md) with a **sequential** provider-selection model.

## Golden rule / Regla principal
**One active write agent, one FW story, one branch/worktree, one PR at a time. / Un único agente escritor activo por historia.** You may later ask another tool for a *read-only, independent* review. Never run concurrent write agents in the same or separate branches unless the human changes the policy explicitly. All agents read [AGENTS.md](../../AGENTS.md); project knowledge stays in Git, never only in a private AI chat.

## Choose per task, not per milestone / Selección por tarea
1. Describe the task, acceptance tests, allowed paths, dependency and privacy/SII/cost risk **before choosing a vendor**. / Definir primero el problema.
2. Check the last **verified** outcomes for similar tasks (build, tests, reviewer findings, rework, cost and time); use a neutral baseline when no comparable evidence exists. / Evaluar historial verificable.
3. Score from 0–5, weighted: **correctness/tests 35%**, context/design 20%, **cost & availability 20%**, safety/permissions 15%, reproducibility/Git integration 10%. Formula = sum(score/5 × weight). / Puntuación de 0 a 100.
4. A tool with an unacceptable secrecy, permission or data-transfer risk is **ineligible regardless of score**. / Seguridad es condición excluyente.
5. Choose one agent, record decision, exact model/version when visible, price/usage assumptions, issue and accepted alternative. Do **not** manufacture benchmarks or claim any provider is best universally. / Decisión justificable y documentada.
6. Run a small comparison only when a new provider is introduced, a task is high-risk, a model changes significantly, or the current tool repeatedly fails. Never pay for four complete parallel implementations by default. / Evitar costos innecesarios.

## Execution phases / Fases
**Plan → implement → local tests → CI → review → accept or handoff.** Protect human approval for PR merge, real SII operations, live PFX/CAF, real personal data, privacy rights decisions, cloud resources or spending. If provider is blocked by quota/cost/error, **stop the current session** and version the handoff before switching; do not secretly run two writers. / Cambio solo tras traspaso.

## Required handoff / Traspaso verificable
Use [handoff template](../../coordination/examples/AGENT-HANDOFF.example.md) and task manifest:
- FW issue, chosen agent/tool/model, reason, approved base SHA, latest commit SHA, branch, worktree, allowed paths and open PR.
- Completed code with factual evidence vs suggested/unverified work; commands **actually run**, CI URL, errors and reviewer findings.
- Updated ADR/API/events/DB migration, security/SII/legal assumptions, privacy classification, costs, pending tests and next *single* action.
- New agent independently validates `git status`, `git diff`, branch SHA, ownership manifest and test commands before touching code. / No confiar ciegamente en el informe anterior.
- An agent switch is **not** an authorization to force push, reset, merge, use billable resources or copy private data. / Sin acciones destructivas.

## Evidence ledger / Registro de decisiones
For each meaningful task, track:
| Issue | Tool/model | Task type | Tests passed (source URL) | Review findings/rework | Time & cost measured | Decision |
|---|---|---|---|---|---|---|
| TODO | not selected | FW-002 local CI | not run | not reviewed | unknown | pending |

**Never fill unmeasured cells with guessed values.** / No inventar métricas.

## Interview explanation / Entrevistas
**EN:** “I use coding assistants as proposed-change tools. I define acceptance tests and architecture constraints, choose one provider using evidence and cost/safety criteria, maintain Git handoffs, verify with CI and review, and keep deployment and legal decisions human-owned.”

**ES:** “Uso asistentes de código bajo contratos de trabajo y evidencia. Selecciono un proveedor según calidad, contexto, riesgo y costo; guardo el traspaso en Git y verifico CI antes de aprobar. Nunca afirmo que la IA reemplaza la revisión humana.”

### Privacy boundary / Límites de privacidad
Never paste real taxpayer XML/PDF, natural-person RUT, personal information, production logs, live PFX/CAF keys or secrets into models or connectors without separate legal/security assessment and explicit authorization. Only synthetic fiscal fixtures by default. / No PII tributaria real en prompts.
