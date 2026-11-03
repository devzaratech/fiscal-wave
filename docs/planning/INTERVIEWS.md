# Interview training / Preparación de entrevistas

**Purpose / Propósito:** prepare independently for platform-style assessments and explainable engineering work. Original training tasks only, not copied answer keys or assistance in a live restricted test. Employer-specific assignments vary; no platform guarantees a universal syllabus. / Ejercicios originales; cada evaluación depende del empleador.

## Platform mapping / Plataformas
| Platform | Officially described formats / Formatos descritos | Study route / Ruta |
|---|---|---|
| [HackerRank](https://www.hackerrank.com/skills-directory) | Coding, SQL/database, Spring Boot, front/back end, Linux, system design and cloud depending on assessment | Java DSA + SQL + API + explanation |
| [LeetCode](https://support.leetcode.com/hc/en-us/articles/360013578114-How-to-use-Explore) | Topic-based data structures and algorithms practice | Pattern repetition + Big-O + edge cases |
| [CoderPad (verify whether your employer's “CodePad” refers to this product)](https://coderpad.io/resources/docs/for-candidates/interview-preparation-guide/) | Live collaborative coding/IDE, debugging and communication | Solve aloud + tests + refactoring |
| [Evalart](https://evalart.com/pruebas-programacion) | Practical coding, SQL, reasoning, theoretical technical and QA questions | Timed coding + SQL + explanation |

Exercises with original prompts and a synthetic SQL fixture: [practice kit](../../practice/README.md). / Guía práctica y fixture SQL: [kit](../../practice/README.md).

## Weekly rotation / Rotación semanal
- **Day A (30–45 min):** Java DSA (arrays, hash maps, strings, stacks/queues, two pointers, sliding window, sorting/binary search, recursion/trees, complexity). / Algoritmos.
- **Day B (30 min):** SQL joins, GROUP BY/HAVING, subqueries/CTE, windows, indexes, transactions/isolation, query plan. / SQL real.
- **Day C (45 min):** Java core: generics, equals/hashCode, streams, Optional, exceptions, immutable types, collections, concurrency, thread safety. / Java profesional.
- **Day D (45 min):** Spring Boot REST, validation, security, JWT/OIDC, JPA pitfalls, tests, migration, API design. / Backend.
- **Day E (45 min):** React/TypeScript, component state, async errors, accessibility, API integration; or Linux/AWS/architecture. / Frontend y cloud.
- **Review (15 min):** record tests, time, confidence, complexity, bugs and a short explanation in English and Spanish. / Registrar evidencia.

## Original mini-challenges / Retos originales
| ID | Problem / Problema | Skill / Competencia | Done when / Terminado cuando |
|---|---|---|---|
| EX-01 | Detect duplicate invoice requests by (tenant, externalId) / Detectar solicitudes repetidas | HashMap, composite keys, O(n) | Handles empty input, case policy and duplicates / Casos límite |
| EX-02 | Find longest run of invoices below an alert threshold / Tramo más largo bajo umbral | Sliding window / dos punteros | Explains assumptions for positive/negative amounts |
| EX-03 | Merge ordered event streams without losing timestamp ties / Unir eventos ordenados | Sorting, priority queue | Stable order and O(n log k) analysis |
| EX-04 | SQL: top 3 customers by paid total per month / SQL: tres mejores clientes por mes | JOIN, CTE, window functions | Correct ties, NULLs, zero invoices |
| EX-05 | SQL: identify duplicate folios within each issuer/type / Encontrar folios repetidos | GROUP BY, indexes, unique constraints | Explains why query + constraint are both needed |
| EX-06 | Build POST /drafts with validation and idempotency / Endpoint de borradores | Spring REST, JUnit | Repeat requests produce one draft, invalid data returns 4xx |
| EX-07 | React form in es-CL/en with loading, error and keyboard flow / Formulario bilingüe | React, TypeScript, a11y | Tests success, error, keyboard and locale |
| EX-08 | Design resilient message delivery to fake SII / Diseñar entrega confiable | Outbox, retry, DLQ, circuit breaker | Draws timeout/unknown/reconciliation state |
| EX-09 | Balance two APIs with Nginx; kill one / Balancear dos APIs y detener una | HTTP networking, health checks | Demonstrated failover + no lost state |
| EX-10 | Secure Lambda writing only one S3 prefix / Asegurar Lambda a prefijo S3 | IAM, S3, policy design | Deny cross-bucket writes, no static keys |

## Design and quality practice / Práctica de diseño y calidad (FW-022)
- Explain SOLID with an actual FiscalWave class that violates and then satisfies SRP/DIP; justify why fewer abstractions may be safer / Ejemplo de refactor SOLID sin sobreingeniería.
- Refactor one API to Strategy or Adapter **only** when real variation exists; explain Big-O, alternative and tests / Justificar patrón, complejidad y pruebas.
- Exercise idempotency: duplicate request, changed payload with same key, concurrent calls, restart and unknown SII result / Repetición, conflicto, concurrencia y reconciliación.
- Practice identifying fragile controller/domain coupling and test behavior with JUnit and integration fixtures / Detectar acoplamiento y probar.
See [EN engineering standards](../en/engineering-standards.md) · [ES estándares](../es/engineering-standards.md).

## Mock evaluation rubric / Rúbrica
Score each dimension 0–2: (1) correct output, (2) tests/edge cases, (3) time/space complexity, (4) clarity and communication, (5) code readability. Maximum 10; improvement matters more than one score. / Puntuar corrección, pruebas, complejidad, claridad y legibilidad.

**Evidence / Evidencia:** preserve original problem description, your own solution, test run, complexity note and a 60-second bilingual explanation, never confidential employer assessments. For hard problems, log approach and learn; don't treat a failed session as an employment verdict.
