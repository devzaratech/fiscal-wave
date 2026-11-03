# Decisiones de arquitectura (ES)

## Principios
1. **Múltiples servicios desplegables y un dueño fiscal.** Dominios previstos: tenant, catalog, fiscal-document, chile-sii-connector, notification, reporting. Activar solo los necesarios por incremento vertical.
2. **Microfrontends:** el shell administra navegación, sesión, idioma y empresa; las aplicaciones facturas/terceros/operaciones/administración poseen rutas. Validar composición React/TypeScript (p. ej. Module Federation) con un spike.
3. **Consistencia fuerte:** combinación emisor + tipo DTE + folio única, asignación transaccional con restricción e integración de concurrencia. Documentos firmados inmutables. Fiscal-document es dueño de estado tributario; conector controla intentos de entrega.
4. **Integración:** OpenAPI HTTP para sincronía, contratos AsyncAPI, outbox transaccional e inbox/deduplicación para eventos. No asumir entrega exactamente una vez; reconciliar respuestas inciertas del SII.
5. **Datos:** propiedad por servicio, esquemas/bases y credenciales aislados; almacenamiento de objetos para artefactos, adaptador compatible S3 en local; prohibidas escrituras cruzadas de base de datos.
6. **Seguridad:** OIDC, validación de tenant en backend, permisos mínimos, CAF/certificados fuera de Git y secretos administrados cuando corresponda.
7. **Nube:** Docker Compose por defecto; AWS ALB/ECS para laboratorio de balanceo e IAM/S3/Lambda/SQS para funciones reales; Terraform con destrucción; Azure después.
8. **Idiomas:** UI en inglés y español chileno; formatos regionales separados de cálculos fiscales y XML firmado.
9. **Evidencia:** sin afirmar madurez productiva o certificación hasta validación oficial.

## Registros de decisión propuestos
ADR-001 monorepo con microservicios; ADR-002 AWS-first pero dominio portable; ADR-003 dueño fiscal transaccional único; ADR-004 shell y MFEs por dominio. Confirmar en el primer hito.

## Criptografía SII, XML/PDF y persistencia políglota
FW-024 incluye Redis como caché opcional y MongoDB para proyecciones solo cuando supere alternativas como PostgreSQL JSONB. PostgreSQL mantiene folios e idempotencia. FW-025 separa el PFX del firmante de la llave privada CAF/RSASK para timbrar; FW-026 exige XSD oficiales, TED y XMLDSig; FW-027 renderiza PDF417 desde XML inmutable; FW-028 compara funciones públicas de LibreDTE y otros proveedores. Ver [datos](../planning/DATA-PLATFORMS.md), [ciclo SII](../planning/SII-DTE-LIFECYCLE.md), [proveedores](../planning/PROVIDER-CAPABILITIES.md), [ADR-0008](../adr/0008-polyglot-persistence.md), [ADR-0009](../adr/0009-credential-custody-and-signing.md), [PlantUML](../architecture/sii-signing-and-pdf.puml). **Ninguna de estas funciones está implementada.**

## Calidad de ingeniería / Engineering quality
FW-022 incorpora [SOLID y estándares de programación](engineering-standards.md), [selección de patrones](../architecture/pattern-catalog.md), [semántica de idempotencia](../architecture/idempotency-contract.md) y [ADR-0006](../adr/0006-engineering-standards.md). Son requisitos propuestos, no implementación probada. Cada patrón exige justificación concreta y pruebas; herramientas de CI se integran progresivamente.

## Criterios no funcionales (objetivos, no resultados)
- Contratos probados y datos sintéticos; cero accesos cruzados entre tenants en pruebas de autorización.
- Repetir una petición no asigna un folio adicional.
- Caída del SII genera estado observable y conciliación, no duplicación silenciosa.
- Cada laboratorio cloud con etiquetas, presupuesto, aprobación y destrucción verificable.
- Auditoría sin secretos ni certificados completos.

[Mapa de sistema](../architecture/system-map.puml) · [Ciclo documental](../architecture/dte-lifecycle.puml) · [Laboratorio AWS](../architecture/aws-lab.puml)
