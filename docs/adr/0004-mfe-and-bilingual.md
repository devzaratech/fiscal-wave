# ADR-0004: Domain microfrontends and bilingual UX / Microfrontends bilingües

**Status / Estado:** Proposed / Propuesto · 2026-11-03

**Decision / Decisión:** One React+TypeScript shell for navigation, tenant and locale; separate invoice/partners/operations/admin MFEs by business capability, not every widget. Prove module loading and shared dependency compatibility in a spike before choosing Module Federation implementation. Contracts and design system are versioned. Use en/es-CL locale catalogs, translation parity checks and locale-format tests. / Un shell y MFEs por dominio, con prueba de composición antes de adoptar tecnología.

**Risk / Riesgo:** runtime dependency drift, cross-MFE state coupling, bundle and accessibility regressions, localization gaps.

**Acceptance / Aceptación:** shell loads two independent MFEs, language switch, a11y keyboard navigation, valid tenant-scoped API calls, independent deploy/revert.
