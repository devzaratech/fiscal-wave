# Estándares de ingeniería — Español

**FW-022 · Estado: propuesto, no instalado.** Los controles se hacen exigibles al implementar código en M1/M2. Consultar [English](../en/engineering-standards.md), [catálogo de patrones](../architecture/pattern-catalog.md), [idempotencia](../architecture/idempotency-contract.md) y [ADR-0006](../adr/0006-engineering-standards.md).

## Principios de diseño
- **SOLID:** SRP (una responsabilidad coherente), OCP (extender comportamientos mediante contratos cuando haya variantes reales), LSP (los adaptadores respetan contratos y semántica de errores), ISP (interfaces pequeñas para consumidores) y DIP (dominio desacoplado de SDK AWS, SQL y HTTP SII).
- **DRY:** eliminar duplicación de *conocimiento*, no confundir dos reglas parecidas pero con evolución distinta.
- **KISS:** preferir implementaciones directas; justificar cada patrón utilizado.
- **YAGNI:** no construir frameworks, fábricas, repositorios, microservicios, cachés o blockchain especulativos en el flujo tributario.
- **Clean Code:** nombres técnicos precisos en INGLÉS, funciones cohesionadas, errores explícitos, objetos inmutables cuando conviene, nulabilidad clara, sin estado global oculto, sin capturar errores silenciosamente y sin secretos en logs. UI y documentación bilingües.
- **Seguridad desde el diseño:** validar entradas, permisos mínimos, aislamiento de tenant en backend, redacción de PII, XML seguro y trazabilidad.

## Java / Spring
- Java 21 como base y pruebas de compatibilidad Java 25 si se verifican; Maven Wrapper y compilaciones reproducibles.
- Invariantes fiscales en Java de dominio; preferir puertos sin dependencia Spring. Adaptadores PostgreSQL/SII/AWS implementan puertos.
- Controladores adaptan HTTP, casos de uso coordinan procesos y entidades JPA no se usan directamente como DTO de API.
- Usar `java.time`, instantes UTC en persistencia y zonas explícitas al mostrar; dinero con `BigDecimal`, precisión/redondeo documentados, nunca `double`.
- Folios protegidos por transacción y restricción única (emisor, tipo DTE, folio), con reglas SII verificadas antes de declarar corrección legal.
- Idempotencia HTTP y deduplicación de eventos según [contrato explícito](../architecture/idempotency-contract.md), con pruebas negativas, concurrencia y timeout.

## React / TypeScript
- TypeScript estricto, clientes de API tipados, evitar `any` sin razón, componentes por dominio y acoplamiento mínimo entre MFEs.
- Shell controla navegación, identidad, idioma y tenant; cada MFE administra sus rutas, carga y errores. El backend decide permisos.
- Accesibilidad: teclado, etiquetas, foco, anuncios de errores. Catálogos `en` y `es-CL` equivalentes.
- Frontend no es autoridad de cálculos tributarios; solo presenta información validada por backend.

## Matriz de verificación (propuesta; instalar con código)
| Capa | Herramientas a evaluar | Evidencia exigida |
|---|---|---|
| Formato Java | Spotless/formateador y Checkstyle | Comando reproducible |
| Errores/análisis | SpotBugs, PMD; SonarQube si es viable | Hallazgos y excepciones justificadas |
| Arquitectura | ArchUnit | Pruebas que fallen al violar límites |
| Seguridad | Revisión de dependencias / OSV/OWASP y secretos | Reportes y clasificación |
| Java | JUnit 5, Mockito, Testcontainers, JaCoCo | Unitarias, DB, concurrencia, contratos y tendencia de cobertura |
| TypeScript | ESLint, Prettier, `tsc --noEmit` | Lint, formato y tipos |
| UI | Vitest, React Testing Library, Playwright | Accesibilidad, idiomas, errores y E2E |
| Entrega | GitHub Actions u otro CI | Resultados reales, artefactos y sin claves cloud fijas |

No añadir todas las herramientas de golpe. Verificar versiones compatibles de Java/Node/Spring, incorporar controles progresivos. Un porcentaje de cobertura aislado no reemplaza casos límites y pruebas negativas.

## Criterio de revisión de PR
Issue, motivo del patrón y alternativas, pruebas *realmente ejecutadas*, contratos/ADR, seguridad/privacidad, traducciones, costo y reversión. Las pruebas no realizadas no se reportan como aprobadas.

## Preparación profesional
Explicar en inglés y español decisiones sobre Strategy/Adapter/State/Outbox, complejidad, concurrencia, fallas, tests y compensaciones, mostrando código verificable.
