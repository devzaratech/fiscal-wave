# ADR-0003: Local first, AWS labs with explicit budget / Local primero, AWS autorizado

**Status / Estado:** Proposed / Propuesto · 2026-11-03

**Decision / Decisión:** Compose for default development; temporary IAM/S3/Lambda/SQS and ECS/ALB hands-on labs to demonstrate employable skills. Domain code uses storage/message interfaces for later Azure ports. Avoid long-running ALB/NAT Gateway/RDS/EKS in early labs. Terraform plans reviewed, explicit owner approval, alerting, tags and teardown. / Desarrollo local, laboratorios cloud acotados y destrucción verificada.

**Validation / Validación:** successful repeatable create/test/destroy drill, resources inventory, after-the-fact AWS billing review, logs and security rationale. / Crear-probar-destruir con evidencia.

**Limits / Límites:** Budget alerts can lag; they are not cost caps. No production DTE/customer secrets in labs. / Alertas no impiden todos los cargos.
