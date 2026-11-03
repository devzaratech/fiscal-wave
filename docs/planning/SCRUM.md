# Scrum-compatible delivery / Entrega compatible con Scrum

Based on the [2020 official Scrum Guide](https://scrumguides.org/scrum-guide.html). **A single-person project can borrow Scrum practices; it is not a full multi-person Scrum Team.** / Un proyecto individual puede aplicar eventos y artefactos, sin afirmar que ya existe un equipo Scrum completo.

## Artifacts and commitments / Artefactos y compromisos
- Product Backlog + **Product Goal**: a safe first Chilean DTE workflow. / Backlog + objetivo de producto.
- Sprint Backlog + **Sprint Goal**: one testable vertical increment. / Backlog sprint + objetivo de sprint.
- Increment + **Definition of Done**: see [QUALITY.md](QUALITY.md). / Incremento + definición de terminado.
- Ordered backlog is refined continuously. / Refinamiento continuo.

## Lightweight cadence / Cadencia liviana
- **Sprint length:** up to 2 weeks, adjustable to personal capacity; don't promise release dates. / Hasta dos semanas, ajustables.
- **Sprint planning (30m):** Why this goal? What fits? How to verify? / ¿Por qué, qué y cómo?
- **Daily review (5–10m):** inspect progress and blockers; optional written log. / Revisar avance y bloqueos.
- **Sprint review (30m):** demonstrate working software and gather feedback. / Mostrar software, no solo PPT.
- **Retrospective (15m):** identify one improvement; reflect it in next sprint. / Una mejora accionable.
- WIP limit: at most **one main feature** and **one small interview exercise** concurrently, to preserve focus. / Límite de trabajo simultáneo.

## AI work ownership / Propiedad de trabajo IA
Each sprint task has one write owner (Codex/Claude/OpenCode/human), one branch/worktree and a versioned task contract. Separate agents review read-only. The maintainer reviews concurrent PRs for file/contract overlap and merges sequentially; no automatic conflict resolution for tax/privacy-critical changes. / Dueño único por tarea, traspaso y revisiones humanas. See [FW-029](MULTI_AGENT.md).

## Definition of Ready (team policy, not Scrum requirement) / Criterios de entrada
Objective, owner, acceptance tests, legal dependencies, EN/ES UI impact, threat/cost risk and rollback scope understood.

## Quality / Calidad
DoD is fixed for the increment; no partially done release. Pair story IDs with commits, PRs, tests, demos and decisions. Never mark planned agent work as delivered.

## Roles / Responsabilidades
Product direction, facilitation and implementation are distinct accountabilities; one solo maintainer can perform each explicitly. Agents are helpers, not accountable human owners.

## Example sprint / Ejemplo
Sprint Goal: “A synthetic invoice draft appears in Spanish/English through shell -> API -> own PostgreSQL, with automated tests.” / “Borrador sintético visible en ambos idiomas con pruebas automatizadas”.
