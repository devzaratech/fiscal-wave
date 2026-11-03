# ADR-0001: Multi-service monorepo / Monorepo multiservicio

**Status / Estado:** Proposed / Propuesto · 2026-11-03

**Context / Contexto:** Product vision has 6 backend domains, 4 MFEs and a shell; team size and costs are small. / Plataforma de varios servicios, recursos limitados.

**Decision / Decisión:** Start with one Git repo, independent service module boundaries and deploy pipelines, owning their respective data. Enable only the first vertical flow. A microservice is defined by ownership and deployability, not repository count. / Monorepo con límites y despliegue autónomos; incremento vertical inicial.

**Consequences / Consecuencias:** Easier refactoring and cross-contract tests; requires selective CI, versioned contracts and directory ownership. Splitting a repository is allowed later if release, security or team boundaries require it. / CI selectivo y contratos claros; repos separados solo por necesidad.

**Alternatives / Alternativas:** Many repos now (more management overhead); modular monolith only (less deployment practice). / Multirepo inmediato o monolito modular.
