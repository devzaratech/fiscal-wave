# FiscalWave diagrams / Diagramas

**EN:** Proposed architecture only, not implemented services or SII authorization. PlantUML (`.puml`) is the source of truth. SVGs and supported Mermaid views are derived.

**ES:** Arquitectura propuesta, no servicios implementados ni autorización del SII. PlantUML (`.puml`) es la fuente de verdad. SVG y Mermaid son vistas derivadas.

Generate / Generar from the repository root: `bash scripts/render-diagrams.sh`. CI validates both rendered SVG and deterministic Mermaid output.

Conversion is strict and limited to the PlantUML constructs in this repository. Unsupported syntax fails CI rather than producing an incomplete diagram. Mermaid may use simplified shapes/layout, and visual equivalence still requires human review.

## Temporary AWS lab / Laboratorio AWS temporal

[PlantUML source](aws-lab.puml) · [Mermaid source](mermaid/aws-lab.mmd) · [SVG](rendered/aws-lab.svg)

![Temporary AWS lab / Laboratorio AWS temporal](rendered/aws-lab.svg)

<details>
<summary>Mermaid / Diagrama Mermaid</summary>

```mermaid
%% Generated from aws-lab.puml; edit the PlantUML source, not this file.
flowchart TD
    Dev["Developer PC / local CI"]
    subgraph group_1["AWS account - sandbox only"]
    Static["CloudFront + S3<br/>MFE static artifacts (optional lab)"]
    ALB["Application Load Balancer<br/>Hourly/LCU charges"]
    subgraph group_2["ECS / Fargate (short lived)"]
    A["Fiscal API task A"]
    B["Fiscal API task B"]
    end
    SQS["SQS / DLQ"]
    Lambda["Lambda Java"]
    S3["S3 private documents"]
    RDS[("RDS (optional; costly)")]
    Guard["IAM + budget alerts + tags<br/>Terraform destroy"]
    end
    Dev -->|browser| Static
    Dev -->|test HTTPS| ALB
    ALB -->|health checks + routes| A
    ALB -->|health checks + routes| B
    A -->|event| SQS
    SQS -->|worker| Lambda
    Lambda -->|IAM role only| S3
    A -->|optional lab| RDS
    B -->|optional lab| RDS
    Guard -.- ALB
    Guard -.- RDS
    Guard -.- Lambda
    note_1["Note: No always-on NAT Gateway, EKS or RDS in the initial lab. Budget alerts are not a guaranteed hard spending cap. All billable resources require owner approval and teardown."]
```

</details>

## DTE lifecycle / Ciclo de vida DTE

[PlantUML source](dte-lifecycle.puml) · [Mermaid source](mermaid/dte-lifecycle.mmd) · [SVG](rendered/dte-lifecycle.svg)

![DTE lifecycle / Ciclo de vida DTE](rendered/dte-lifecycle.svg)

<details>
<summary>Mermaid / Diagrama Mermaid</summary>

```mermaid
%% Generated from dte-lifecycle.puml; edit the PlantUML source, not this file.
sequenceDiagram
    actor User as Operator / Operador
    participant UI as Invoices MFE
    participant Fiscal as Fiscal Document Service
    participant DB as Fiscal DB + Outbox
    participant Broker as Message broker
    participant Connector as Chile SII Connector
    participant SII as SII test/authorized
    User->>UI: Create draft / Crear borrador
    UI->>Fiscal: POST draft (idempotency key)
    Fiscal->>DB: Validate and persist
    Fiscal-->>UI: Draft ID + validation errors
    User->>UI: Request issuance / Solicitar emisión
    UI->>Fiscal: Issue (idempotency key)
    Fiscal->>DB: Transaction: unique folio, signed XML, outbox
    DB-->>Fiscal: committed
    Fiscal-->>UI: Pending dispatch / Pendiente
    DB->>Broker: Publish via outbox worker
    Broker->>Connector: Delivery command (deduplicated)
    Connector->>SII: Submit when authorized
    alt accepted / aceptado
    SII-->>Connector: Reference + status
    Connector->>Broker: accepted result
    else rejected / rechazado
    SII-->>Connector: Reason code
    Connector->>Broker: rejected result
    else timeout / resultado incierto
    Connector->>Broker: needs reconciliation
    Note right of Connector: No blind resubmission / no reenvío ciego
    end
    Broker->>Fiscal: Status event (idempotent)
    Fiscal->>DB: Store state + audit
    UI->>Fiscal: Query status
    Fiscal-->>UI: Current state / Estado vigente
```

</details>

## Idempotent issuance / Emisión idempotente

[PlantUML source](idempotency-sequence.puml) · [Mermaid source](mermaid/idempotency-sequence.mmd) · [SVG](rendered/idempotency-sequence.svg)

![Idempotent issuance / Emisión idempotente](rendered/idempotency-sequence.svg)

<details>
<summary>Mermaid / Diagrama Mermaid</summary>

```mermaid
%% Generated from idempotency-sequence.puml; edit the PlantUML source, not this file.
sequenceDiagram
    actor Client as Client
    participant API as Fiscal API
    participant DB as Fiscal DB<br/>(Idempotency + DTE + Outbox)
    participant Q as Event broker
    participant SII as SII Connector
    Client->>API: POST /issue + Idempotency-Key
    API->>DB: Authenticate tenant; reserve scoped key + fingerprint
    alt new / nueva
    DB-->>API: reserved
    API->>DB: Transaction: allocate unique folio,<br/>sign document, save outbox + result
    DB-->>API: committed document ID
    API-->>Client: 202 Accepted + Location
    else same key and same fingerprint / repetida
    DB-->>API: stored result/pending
    API-->>Client: same result or 202 + status URI
    else same key, different fingerprint / contenido distinto
    DB-->>API: conflict
    API-->>Client: 409 Conflict
    end
    DB->>Q: outbox publisher (at least once)
    Q->>SII: event ID, document ref
    SII->>SII: inbox deduplication
    Note right of SII: External timeout != rejection. Reconcile unknown status before resubmission.
```

</details>

## Personal-data boundaries / Límites de datos personales

[PlantUML source](privacy-boundaries.puml) · [Mermaid source](mermaid/privacy-boundaries.mmd) · [SVG](rendered/privacy-boundaries.svg)

![Personal-data boundaries / Límites de datos personales](rendered/privacy-boundaries.svg)

<details>
<summary>Mermaid / Diagrama Mermaid</summary>

```mermaid
%% Generated from privacy-boundaries.puml; edit the PlantUML source, not this file.
flowchart LR
    Subject["Individual data subject<br/>Titular de datos"]
    Tenant["Tenant organization<br/>Empresa cliente"]
    subgraph group_1["FiscalWave (proposed)"]
    Identity["Tenant identity/roles<br/>OIDC + authorization"]
    Fiscal["Fiscal Document Service<br/>legal XML owner"]
    Rights["Privacy request workflow<br/>DSAR + exception review"]
    Sii["SII Connector"]
    Audit["Audit / incident response<br/>redacted metadata"]
    Pg[("PostgreSQL scoped by tenant<br/>idempotency + indexes")]
    Store["Private document storage<br/>signed XML, PDF, retention"]
    Vault["Credential vault<br/>PFX vs CAF separate"]
    Cache["Optional Redis/Mongo<br/>non-authoritative and controlled"]
    end
    SII["Chilean SII (authorized)"]
    Vendors["Approved processors/regions<br/>transfer review required"]
    Tenant -->|login and role / acceso| Identity
    Tenant -->|create DTE / emitir| Fiscal
    Fiscal -->|transaction and indexes| Pg
    Fiscal -->|signed XML / PDF| Store
    Fiscal -->|authorized signing / claves| Vault
    Fiscal -->|authorized delivery / envío| Sii
    Sii -->|SII tests/production if allowed| SII
    Fiscal -->|safe audit / auditoría| Audit
    Subject -->|verified legal request / derechos| Rights
    Rights -->|eligibility, profile| Identity
    Rights -->|eligible personal metadata| Pg
    Rights -->|tax retention legal review| Store
    Rights -->|decision evidence| Audit
    Identity -->|only assessed / proveedor autorizado| Vendors
    note_1["Note: No automatic deletion of signed XML. Apply verified statutory exceptions and record decision."]
    Rights -.-> note_1
    note_2["Note: Separate Git repositories do NOT provide residency or transfer compliance."]
    Vendors -.-> note_2
```

</details>

## SII signing and PDF / Firma SII y PDF

[PlantUML source](sii-signing-and-pdf.puml) · [Mermaid source](mermaid/sii-signing-and-pdf.mmd) · [SVG](rendered/sii-signing-and-pdf.svg)

![SII signing and PDF / Firma SII y PDF](rendered/sii-signing-and-pdf.svg)

<details>
<summary>Mermaid / Diagrama Mermaid</summary>

```mermaid
%% Generated from sii-signing-and-pdf.puml; edit the PlantUML source, not this file.
sequenceDiagram
    autonumber
    actor User as Authorized issuer / Emisor autorizado
    participant MFE as Invoices MFE
    participant Fiscal as Fiscal Document Service
    participant DB as PostgreSQL<br/>folios and idempotency
    participant PFX as Signer credential port<br/>PKCS#12 (.pfx/.p12)
    participant CAF as CAF credential port<br/>RSASK private timbre key
    participant XSD as Official XSD validator<br/>versioned offline bundle
    participant PDF as PDF renderer<br/>PDF417
    participant Store as Private object storage<br/>immutable signed XML + PDF
    participant SII as SII Connector
    User->>MFE: Issue synthetic DTE / Emitir DTE de prueba
    MFE->>Fiscal: issue(idempotency key, issuer)
    Fiscal->>DB: Unique issuer + type + folio; store intent
    DB-->>Fiscal: Authorized range reserved
    Fiscal->>Fiscal: Construct TED DD payload
    Fiscal->>CAF: Authorize issuer/type/range; sign DD in isolated key port
    CAF-->>Fiscal: FRMT signature + public CAF metadata
    Fiscal->>Fiscal: Assemble TED (DD + FRMT)
    Fiscal->>XSD: Validate document XML
    XSD-->>Fiscal: Schema + business checks
    Fiscal->>PFX: Sign whole XML with authorized signer
    PFX-->>Fiscal: XMLDSig result
    Fiscal->>XSD: Validate final signed document
    XSD-->>Fiscal: Valid or error
    Fiscal->>Store: Persist immutable signed XML
    Fiscal->>PDF: Render stored signed XML including TED
    PDF-->>Fiscal: PDF + scannable PDF417
    Fiscal->>Store: Persist derived PDF
    Fiscal->>DB: Audit metadata + outbox
    Fiscal-->>MFE: Document ID and pending status
    DB->>SII: Async outbox submission command (when authorized)
    Note right of CAF: CAF private timbre key != PFX signer key Never store secrets in Redis/Mongo.
    Note right of PDF: PDF is representation, XML is tax document; print sample tests pending.
    Note over SII: No real submissions without authorized issuer and SII process.
```

</details>

## System map / Mapa del sistema

[PlantUML source](system-map.puml) · [Mermaid source](mermaid/system-map.mmd) · [SVG](rendered/system-map.svg)

![System map / Mapa del sistema](rendered/system-map.svg)

<details>
<summary>Mermaid / Diagrama Mermaid</summary>

```mermaid
%% Generated from system-map.puml; edit the PlantUML source, not this file.
flowchart LR
    Operator["Operator / Operador"]
    OIDC["OIDC Provider"]
    SII["Chilean SII (external)"]
    subgraph group_1["Frontend Shell (React + TS)"]
        Shell["Frontend Shell (React + TS)"]
    Invoices["Invoices MFE"]
    Partners["Partners MFE"]
    Operations["Operations MFE"]
    Admin["Admin MFE"]
    end
    API["Ingress / API BFF"]
    subgraph group_2["FiscalWave services (target)"]
    Tenant["Tenant Service"]
    Catalog["Catalog Service"]
    Fiscal["Fiscal Document Service<br/>(sole folio owner)"]
    Connector["Chile SII Connector"]
    Notify["Notifications"]
    Reporting["Reporting"]
    end
    DB[("PostgreSQL<br/>per-service data ownership")]
    Queue["Event bus / SQS (lab)"]
    Storage["Object storage / S3 (lab)"]
    Operator -->|HTTPS| Shell
    Shell -->|OIDC login| OIDC
    Shell -->|REST| API
    API --> Tenant
    API --> Catalog
    API --> Fiscal
    API --> Reporting
    Fiscal -->|transaction + outbox| DB
    Tenant --> DB
    Catalog --> DB
    Reporting --> DB
    Fiscal -->|signed artifacts| Storage
    Fiscal -->|document prepared| Queue
    Queue -->|delivery intent| Connector
    Connector -->|controlled test / authorized only| SII
    Connector -->|delivery result| Queue
    Queue --> Notify
    Queue --> Reporting
    note_1["Note: CAF, folio, signing and fiscal state must remain under one owner"]
    Fiscal -.-> note_1
    note_2["Note: Never issue folios. Unknown results require reconciliation before retry."]
    Connector -.-> note_2
```

</details>
