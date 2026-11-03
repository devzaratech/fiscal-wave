# Hoja de ruta FiscalWave (ES)

**Horizonte:** hitos verificables, no fechas prometidas. Una entrega vertical funcionando tiene prioridad sobre desplegar todos los servicios. Consultar [backlog](../planning/BACKLOG.md) e [hitos](../planning/MILESTONES.md).

## Secuencia de hitos
| Hito | Objetivo | Evidencia |
|---|---|---|
| M0 - Fundamentos | Documentación bilingüe, diagramas, alcance, agentes y backlog Scrum | Revisión y merge de documentos sin afirmar funciones inexistentes |
| M1 - Sistema distribuido y estándares | Dos servicios Java, shell/MFE, Docker, Postgres y FW-022 | CI, pruebas smoke y contratos, format/lint/arquitectura con evidencia y demostración |
| M2 - Dominio fiscal offline | DTE sintéticos 33/34, firma, folios y comandos idempotentes | Pruebas de concurrencia, replay, conflictos y deduplicación; XML/XSD con fuentes SII |
| M3 - Laboratorio AWS | IAM/S3/Lambda/SQS y demo ECS/ALB temporales con costo aprobado | IaC, presupuesto, logs, failover, `terraform destroy` y revisión de costo |
| M4 - Integración oficial Chile | Pruebas SII y proceso formal con emisor habilitado | Evidencia oficial; no afirmar certificación prematuramente |
| M5 - Piloto y auditoría verificable | Seguridad, aislamiento multiempresa, respaldo, cadena SHA-256 y detección de alteraciones | Pruebas con datos sintéticos, piloto autorizado y procedimiento operativo |
| M6 - Expansión | Otro país, facturación recurrente o pagos solo tras descubrir demanda | ADR, investigación y validación por jurisdicción |
| M7 - Anclaje criptográfico opcional | Evaluar checkpoints firmados, WORM, raíces Merkle y adaptador blockchain | PoC sintética con revisión de privacidad y costos; independiente de la emisión DTE |

## Primera meta operativa
Un usuario crea un borrador sintético desde UI bilingüe, lo emite contra un simulador, observa el estado y comprende la auditoría. En el siguiente incremento se robustece la corrección tributaria. Nunca posponer esto meses por microservicios vacíos.

## Evidencia laboral paralela
Ejercicios originales de Java, SQL y TypeScript cada semana; explicación arquitectónica; laboratorio cloud reproducible cuando el presupuesto lo permita. Las postulaciones pueden continuar antes de M4/M5.

**Puertas de salida:** requisitos trazables -> pruebas -> revisión seguridad/costos -> documentación bilingüe -> PR aprobado. La certificación ante el SII depende de un proceso externo.
