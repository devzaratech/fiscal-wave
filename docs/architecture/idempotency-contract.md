# FiscalWave idempotency contract / Contrato de idempotencia

**FW-022 · Proposed protocol, not running software. / Protocolo propuesto, no implementado.** Complete HTTP and event contract tests in M2 before any real DTE issuance.

## HTTP command / Comando HTTP
- Require `Idempotency-Key` for issuance and other side-effect commands; UUID or another opaque bounded key. / Exigir clave opaca para comandos de emisión.
- Compute a versioned canonical request fingerprint after validation; include endpoint/action and legal domain identity. Do not log sensitive request bodies. / Huella canónica y versionada sin exponer payload.
- Store a unique record scoped to **tenant + operation + idempotency key**, linked to request fingerprint and durable outcome; authenticate tenant on the backend first. / Restricción única por tenant, operación y clave.
- **First attempt / Primer intento:** atomically reserve the key and operation intent under DB transaction. Concurrent attempts use unique constraint/locking; never allow a second folio. / Concurrencia controlada por BD.
- **Same key + same fingerprint / Misma clave y solicitud:** return the stored completed result (document ID, HTTP status and safe body) or a stable pending response (`202 Accepted` + `Location` / status resource) when still in progress. Never execute twice. / Repetición devuelve el resultado, sin doble ejecución.
- **Same key + different fingerprint / Misma clave y distinto contenido:** return `409 Conflict` with a documented error code, without side effects. / Conflicto sin efectos.
- Keys are not global across tenants; access to any result is authorized again, no cross-tenant leakage. / Aislamiento estricto.
- Define bounded key length, request limits and retention; even after key expiry, the *fiscal/business uniqueness* and folio constraints must prevent illegal duplicate issuance. Do not silently promise infinite deduplication. / Caducidad documentada, restricciones fiscales perdurables.
- Failures: distinguish transient transport errors, business rejection and indeterminate acceptance by the SII. Reconcile externally unknown outcomes **before** considering a resubmission. / Conciliar respuestas inciertas antes de reenvío.

## Event handling / Eventos
- Transactional Outbox persists state change + outgoing event atomically; consumer Inbox stores processed event ID and outcome with transaction. At-least-once delivery is assumed. / Outbox + inbox y entrega al menos una vez.
- Deduplicate by event ID and bounded domain identity; event payloads carry schema version, correlation ID, tenant and immutable document reference. No direct cross-service SQL writes. / Deduplicación con ID de evento y correlación.
- Retried connector jobs must not produce multiple legal documents or unaudited transitions. DLQ + backoff with jitter and alerting for poisoned messages. / Retries limitados y auditoría.
- The external SII may accept a document before HTTP timeout; **no blind retry** of submission until an authoritative reconciliation path is evaluated. / Timeout no implica rechazo.

## Tests required / Pruebas requeridas
1. 1, 2 and 100 concurrent identical commands → one persistent intent and at most one folio / Concurrencia.
2. Same key + changed amount / fingerprint → 409 and no side effect / Conflicto.
3. Same key after process restart → same durable state / Persistencia.
4. Different tenants with same key → isolated results / Aislamiento.
5. Event delivered multiple times/out of order → no duplicate side effect, observable ordering policy / Reentrega.
6. Timeout after simulated remote acceptance → unknown + reconciliation, not resubmit / Resultado incierto.
7. Expired key behavior explicitly tested with legal/business identity controls / Caducidad.
8. No secrets or full personal/tax payloads in logs / Privacidad.

## Design consequences / Consecuencias
HTTP idempotency, DB uniqueness and broker deduplication solve **different layers**; combine all three. Network exactly-once guarantees are not assumed. Code should expose typed results and documented error responses. See [lifecycle diagram](dte-lifecycle.puml) and [pattern catalog](pattern-catalog.md).
