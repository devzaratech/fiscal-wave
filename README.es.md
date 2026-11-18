# FiscalWave 🌊

**[English](README.md)** | **ES**

> **Estado: arquitectura y descubrimiento.** No se declara certificación del SII, emisión productiva, procesamiento de pagos ni servicios desplegados.

FiscalWave aspira a ser una plataforma fiscal **API-first, bilingüe y portable entre nubes**. La primera entrega funcional apunta a **documentos tributarios electrónicos (DTE) de Chile**. Los adaptadores de otros países, suscripciones, orquestación de pagos y libro contable son visión futura, **no compromisos del MVP**.

## Objetivos
1. Entregar un flujo chileno de DTE verificable, sin atribuirse autorizaciones del SII inexistentes.
2. Demostrar competencias laborales mediante código real: Java, Spring Boot, SQL, sistemas distribuidos, React/TypeScript, seguridad, pruebas, CI/CD y AWS.
3. Mantener experimentos cloud pequeños y sujetos a aprobación explícita de costos.

## Dirección tecnológica
- **Backend:** Java 21 como base (ensayos de compatibilidad con Java 25), Spring Boot, Maven y PostgreSQL; microservicios desplegables en forma independiente con propiedad de datos.
- **Frontend:** React + TypeScript; shell y microfrontends por dominio; composición a validar con una prueba de concepto.
- **Integración:** OpenAPI, AsyncAPI, patrón outbox, idempotencia, folios y DTE dentro de un dueño transaccional.
- **Infraestructura:** Docker Compose primero; laboratorios temporales AWS ECS/S3/SQS/Lambda/ALB; Terraform y limpieza; portabilidad Azure después.
- **Idiomas:** inglés y español de Chile. El XML tributario se rige por esquemas del país, no por traducciones UI.

### Dominios propuestos, no implementados aún
`tenant`, `catalog`, `fiscal-document`, `chile-sii-connector`, `notification`, `reporting`. Primera entrega vertical: DTE + simulador/conector SII + interfaz mínima. Microfrontends proyectados: facturas, terceros, operaciones, administración y shell.

## Guías
- [Visión](docs/es/vision.md) · [Arquitectura](docs/es/architecture.md) · [Hoja de ruta](docs/es/roadmap.md)
- [Selección secuencial de IA](docs/planning/AI-AGENT-STRATEGY.md) · [Stack objetivo](docs/planning/STACK-BASELINE.md) · [Primer desarrollo FW-002](docs/planning/M1-KICKOFF.md)
- [Coordinación de agentes y worktrees](docs/planning/MULTI_AGENT.md) · [Protección de datos personales de Chile](docs/privacy/README.md) · [Repositorios por país](docs/adr/0010-country-repository-strategy.md)
- [Backlog y Scrum](docs/planning/README.md) · [CI/CD](docs/planning/CICD.md) · [Práctica de entrevistas](docs/planning/INTERVIEWS.md)
- [FinOps](docs/planning/FINOPS.md) · [Cumplimiento SII](docs/planning/COMPLIANCE.md)
- [Redis/MongoDB](docs/planning/DATA-PLATFORMS.md) · [PFX/CAF, XSD y PDF417](docs/planning/SII-DTE-LIFECYCLE.md) · [Comparativa LibreDTE](docs/planning/PROVIDER-CAPABILITIES.md)
- [Localización](docs/planning/I18N.md) · [Instrucciones para agentes](AGENTS.md)
- [SOLID y estándares](docs/es/engineering-standards.md) · [Patrones de diseño](docs/architecture/pattern-catalog.md) · [Contrato de idempotencia](docs/architecture/idempotency-contract.md)
## Diagramas de arquitectura

[Ver galería bilingüe](docs/architecture/diagrams.md) con seis diagramas propuestos en SVG y sus archivos PlantUML originales.

![Mapa propuesto del sistema FiscalWave](docs/architecture/rendered/system-map.svg)

Para regenerar los diagramas: `bash scripts/render-diagrams.sh` (requiere PlantUML y Graphviz). Los SVG exportados tienen fondo blanco opaco y texto oscuro, por lo que se ven correctamente tanto en el modo claro como en el oscuro de GitHub. GitHub Actions comprueba la sincronización. **Son diseños propuestos, no servicios desplegados.**

## Colaboración y transparencia
Revisar [CONTRIBUTING](CONTRIBUTING.md) y [Definition of Done](docs/planning/QUALITY.md). No subir certificados, CAF reales, datos de clientes, claves ni secretos. Licenciamiento Community: [PolyForm Noncommercial 1.0.0](LICENSE) para versiones posteriores a FW-034; [licencias Apache 2.0 históricas](docs/legal/LICENSING.md) siguen vigentes para las versiones antiguas.

## Licenciamiento / Licensing
**Community: código source-available bajo [PolyForm Noncommercial License 1.0.0](LICENSE)** para publicaciones aplicables posteriores a la transición, con los usos no comerciales y las excepciones institucionales previstas en el texto oficial. **No es Open Source según la OSI.** Community tendrá un núcleo tributario completo, sin desactivaciones artificiales.

**Commercial:** los usos fuera de las autorizaciones públicas requerirán un contrato escrito independiente con el titular de derechos. Este README no constituye una licencia comercial, tarifa, certificación SII, garantía de producción ni SLA. **Enterprise:** módulos propietarios privados y servicios avanzados futuros; aún no publicados.

**Las autorizaciones anteriores bajo Apache-2.0 se conservan.** Las versiones publicadas antes de FW-034 siguen contando con los permisos concedidos válidamente, incluidos los usos comerciales permitidos por Apache-2.0. [LICENSE histórico anterior al cambio](https://github.com/devzaratech/fiscal-wave/blob/95315c0204394e00ad3852ac04daa2667d4d0dc7/LICENSE).

Detalles bilingües: [Política de licenciamiento](docs/legal/LICENSING.md) · [ADR-0012](docs/adr/0012-license-transition-and-commercial-model.md) · [FW-034](https://github.com/devzaratech/fiscal-wave/issues/21). Todo código de terceros, ROOSTER/NicDTE y contribución externa requiere revisión de derechos.
