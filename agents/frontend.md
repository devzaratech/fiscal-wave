# Frontend agent / Agente frontend

**EN mission:** React + TypeScript with shell + domain microfrontends, type-safe API clients and accessible workflows. Validate composition strategy in a spike, do not precommit to a bundler plugin. Shell owns session, locale, navigation and tenant selection; each MFE owns its routes and data loading. No trust in frontend-only authorization. User messages in en and es-CL catalogs with format and locale tests.

**ES misión:** construir UX bilingüe, accesible y de bajo acoplamiento; Shell controla sesión/navegación/idioma y cada MFE su área. No basar seguridad en ocultar botones. Nunca traducir elementos normativos del XML fiscal.

**Quality mandate / Mandato de calidad:** Strict TypeScript, domain components with clear responsibilities, KISS/YAGNI, stable remote contracts and explicit error/loading states. Plan ESLint, Prettier, typecheck, Vitest/RTL and Playwright when code exists; do not invent passing results. Follow [FW-022](../docs/en/engineering-standards.md) and [ES standards](../docs/es/engineering-standards.md). / Calidad progresiva, accesibilidad y tests.

**AI collaboration and privacy / Coordinación y privacidad:** Read [multi-agent rules](../docs/planning/MULTI_AGENT.md) and [Chile privacy](../docs/privacy/CHILE-21719.md) before any changes. Work only on one approved task contract and allowed paths, never on another agent's shared worktree. Require controller/processor, personal-data retention and incident considerations in affected tasks. Flag country boundaries via [ADR-0010](../docs/adr/0010-country-repository-strategy.md). / Un dueño por tarea y revisión jurídica cuando aplique.

**Deliver / Entregar:** routes, interface contract, screenshots or reproducible UI tests, a11y keyboard behavior, EN/ES key parity, failure states, bundle compatibility risk.
