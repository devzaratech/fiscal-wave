# Engineering standards — English

**FW-022 · Status: proposed, not installed.** These rules become enforceable with implementation during M1/M2. See [Spanish](../es/engineering-standards.md), [patterns](../architecture/pattern-catalog.md), [idempotency](../architecture/idempotency-contract.md) and [ADR-0006](../adr/0006-engineering-standards.md).

## Design principles
- **SOLID:** SRP (one cohesive reason to change); OCP (extend behavior behind stable contracts when variation exists); LSP (adapters honor preconditions, postconditions and error semantics); ISP (small consumer-focused interfaces); DIP (domain uses ports, never AWS SDK, SQL or SII HTTP directly).
- **DRY:** unify shared *knowledge*, not superficially similar code that changes for different reasons.
- **KISS:** prefer direct domain logic; pattern use requires a reason and an example of actual variation.
- **YAGNI:** no speculative repositories, services, factories, framework wrappers, caching or blockchain in critical issuance.
- **Clean Code:** precise ENGLISH code names (public identifiers), small cohesive functions, explicit errors, immutable value objects where suitable, explicit nullability, no hidden global state, no silent catch, no secrets in logs. Product copy and documentation in both English and Spanish.
- **Security by default:** untrusted input validation, least privilege, tenancy on server, redact PII, safe XML parser, threat model and auditable errors.

## Java / Spring
- Java 21 baseline with Java 25 compatibility only when validated; Maven wrapper, dependency management and reproducible build.
- Domain invariants in pure Java; avoid framework annotations in domain when possible. Adapters for Postgres, SII and AWS implement domain ports.
- Spring controllers adapt transport only; services/use cases own business workflow; repositories do not leak JPA entities as API contracts.
- Time: use `java.time`, UTC instants in persistence, explicit locale/timezone at display; currency with `BigDecimal` and documented precision/rounding, never floating-point money.
- Concurrent folio assignment protected by database transaction and unique (issuer, DTE type, folio) constraint. Validate actual SII rule before claiming legal correctness.
- HTTP idempotency and event deduplication obey [the explicit contract](../architecture/idempotency-contract.md), with negative, concurrent and timeout tests.

## React / TypeScript
- Strict TypeScript, narrow types, typed API clients, no unsafe `any` without rationale; reusable components by domain, avoid global MFE state coupling.
- Shell owns navigation/identity/locale/tenant selection; per-MFE routes and loading/errors; backend enforces every permission.
- Accessibility: keyboard navigation, meaningful labels, focus management, error announcements. EN and es-CL keys stay in parity.
- Components do not contain hidden fiscal authority; values returned from backend may be displayed, never recalculated as tax source of truth.

## Verification matrix (planned; add to CI when code exists)
| Layer | Tools to evaluate | Required proof |
|---|---|---|
| Java formatting | Spotless or formatter + Checkstyle | Reproducible format/check command |
| Java lint/bugs | SpotBugs, PMD; SonarQube if affordable | Tracked findings and justified suppressions |
| Architecture | ArchUnit | Forbidden dependency tests fail when deliberately violated |
| Security | Dependency review / OSV/OWASP scanner, secret scanning | Reports with severity triage; no hidden baseline |
| Java behavior | JUnit 5, Mockito, Testcontainers, JaCoCo | Unit, DB integration, transaction, API contract and coverage trend |
| TypeScript | ESLint, Prettier, `tsc --noEmit` | Lint/style/typecheck pass |
| UI | Vitest + React Testing Library; Playwright smoke/E2E | A11y, locale, failure, integration tests |
| Delivery | GitHub Actions or equivalent | PR check results, immutable artifacts, no production cloud keys |

Do not install all tools as a dependency bomb. Select compatible versions with supported JDK/Node/Spring; start small and add CI gates as code emerges. No arbitrary coverage score alone proves quality; critical branch/negative tests matter more.

## Pull request quality bar
An issue ID, rationale for chosen patterns and discarded alternatives, tests *actually executed*, changed contract/ADR, security/privacy review, EN/ES text review, cost effect and rollback instructions. Never claim unexecuted checks as passing. Missing evidence means TODO, not DONE.

## Professional interview competency
For each key decision, explain **why** Strategy/Adapter/State/Outbox was appropriate, complexity, DB concurrency guarantees, failure mode, tests and tradeoffs in both EN/ES. Demonstrate working code, not pattern vocabulary.
