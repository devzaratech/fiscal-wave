# Personal data inventory / Inventario de datos personales

**Template only; verify each row with the actual implementation and contracts. / Plantilla; validar con hechos.** [Chile readiness](CHILE-21719.md).

| Data class / Categoría | Example / Ejemplo | Purpose / Finalidad | Controller vs processor decision / Rol | Proposed store / Almacén | Retention / Retención | Protection / Protección |
|---|---|---|---|---|---|---|
| Account identity / Usuario | Name, email, role, OIDC subject | Authentication/authorization / Acceso | TBD per relationship / Por definir | tenant DB | TBD | RBAC, MFA for privileged users, audit |
| Natural-person tax identifiers / RUT natural | Issuer/recipient RUT, names, addresses | Authorized DTE issuance / Emisión | Customer vs platform contract, assess / Evaluar | signed XML + indexed metadata | Tax-rule review required / Fuente SII | Tenant-scoped access, private storage |
| Fiscal documents / Documentos | XML DTE 33/34, line items, references | Tax evidence / Evidencia | TBD | immutable object store | Legal/tax review / Norma tributaria | Cryptographic hash, limited access |
| PDF representation / PDF | Derived invoices with TED/PDF417 | Display/print/share / Impresión | TBD | private object store | Based on legal purpose / Según finalidad | Signed URLs limited, access logs |
| Certificates/CAF / Credenciales | PFX, private keys, CAF RSASK | Authorized signature/stamp / Firma | Specific custodian/tenant | vault / bóveda | Until legal/business need, rotation policy | Separated encryption keys, no logs |
| Contact/delivery / Contacto | Recipient email, webhook URL | Exchange and notifications / Entrega | TBD | appropriate service DB | Proportionate / Proporcional | Access control, domain validation |
| Security logs / Auditoría | Request ID, actor, IP if collected | Incident/security compliance / Seguridad | Often platform controller; assess | restricted log store | Time-bound / Plazo limitado | Redaction, encryption, access audit |
| Support cases / Soporte | Tickets, attached files | Service support / Soporte | Contract-specific / Según contrato | restricted service | Defined by purpose | No production XML in AI ticket prompts |
| Redis ephemeral / Caché | Rate-limit keys, minimal non-sensitive metadata | Performance/abuse limits / Rendimiento | Same as originating flow | Redis optional | Short TTL | Do not store PFX/CAF/PII |
| Mongo read projection / NoSQL | Optional metadata | Query/read / Consultas | Same as originating flow | Mongo optional | Derived, rebuildable | Tenant scoping, deletion propagation |

**For each row:** record actual owner, lawful basis (consent/contract/legal duty/etc), precise fields, data origin, recipients, third-party vendor, country/region and backup copies, erasure path, legal hold, documented protection and evidence. / Completar el registro por flujo antes de almacenar datos reales.

- [ ] Complete inventory after first domain code / Completar al implementar.
- [ ] Map each consumer/provider, remote access and international transfer / Proveedores y transferencias.
- [ ] Select true retention schedule with Chilean legal review; no invented fixed years / Retención verificada.
- [ ] Review privacy notice and processor terms / Contratos y transparencia.
