# Hoja de ruta FiscalWave (ES)

**Horizonte:** hitos verificables, no fechas prometidas. Una entrega vertical funcionando tiene prioridad sobre desplegar todos los servicios. Consultar [backlog](../planning/BACKLOG.md) e [hitos](../planning/MILESTONES.md).

## Secuencia de hitos
| Hito | Objetivo | Evidencia |
|---|---|---|
| M0 - Fundamentos | Documentación bilingüe, diagramas, alcance, agentes y backlog Scrum | Revisión y merge de documentos sin afirmar funciones inexistentes |
| M1 - Sistema distribuido, estándares y CI | Dos servicios Java, shell/MFE, Docker, Postgres, FW-022 y FW-023 | Gate PR siempre ejecutado, builds y pruebas selectivas Java/React sin AWS, demostración |
| M2 - DTE XML/PDF offline | DTE sintéticos 33/34, PFX/CAF protegido, TED, XMLDSig y PDF417 | FW-025–027, XSD oficiales, pruebas de firma/timbre, impresión y concurrencia |
| M3 - Laboratorio AWS y entrega | IAM/S3/Lambda/SQS, ECS/ALB temporal y ensayo de FW-023 | Despliegue OIDC aprobado, smoke, failover, rollback, `terraform destroy` y costos |
| M4 - Integración oficial Chile | Certificación SII con emisor habilitado, muestras PDF417 e intercambio | Evidencia oficial de XML, emisión, estados, impresión e intercambio |
| M5 - Piloto y auditoría verificable | Seguridad, aislamiento multiempresa, respaldo, cadena SHA-256 y detección de alteraciones | Pruebas con datos sintéticos, piloto autorizado y procedimiento operativo |
| M6 - Expansión | Evaluar MongoDB/JSONB, funciones de otros DTE y países solo tras validar demanda | FW-024/028, ADR, fuentes SII y evidencia comercial |
| M7 - Anclaje criptográfico opcional | Evaluar checkpoints firmados, WORM, raíces Merkle y adaptador blockchain | PoC sintética con revisión de privacidad y costos; independiente de la emisión DTE |

## Primera meta operativa
Un usuario crea un borrador sintético desde UI bilingüe, lo emite contra un simulador, observa el estado y comprende la auditoría. En el siguiente incremento se robustece la corrección tributaria. Nunca posponer esto meses por microservicios vacíos.

## Evidencia laboral paralela
Ejercicios originales de Java, SQL y TypeScript cada semana; explicación arquitectónica; laboratorio cloud reproducible cuando el presupuesto lo permita. Las postulaciones pueden continuar antes de M4/M5.

**Puertas de salida:** requisitos trazables -> pruebas -> revisión seguridad/costos -> documentación bilingüe -> PR aprobado. La certificación ante el SII depende de un proceso externo.
