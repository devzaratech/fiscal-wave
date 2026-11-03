# AWS cost safety / Seguridad de costos AWS

**EN:** AWS is a temporary training environment until a justified pilot exists. **ES:** AWS será laboratorio temporal, no infraestructura obligatoriamente activa.

## Deployment approval gate / Aprobación antes del despliegue
- [ ] Owner explicitly approves account, region, resources, max runtime and estimated USD exposure / Aprobación explícita.
- [ ] Pricing Calculator estimate and known recurring charges attached / Estimación por servicio.
- [ ] Budgets + alerts (for example 25/50/75/100%) configured / Presupuestos y alertas.
- [ ] Spend limits checked for eligibility, paid-plan conditions and limits; **not assumed universally available** / Verificar elegibilidad.
- [ ] IAM least privilege; deny unnecessary costly regions/services and uncontrolled scale-out / Permisos mínimos y cuotas.
- [ ] `terraform plan` reviewed; resource tags `project=fiscal-wave`, `environment=lab`, `owner`, `delete-after` / Plan revisado.
- [ ] Egress/data transfer, public IPv4, ALB LCU/hour, NAT Gateway hourly+GB, CloudWatch logs, RDS, Fargate and storage costs considered / Considerar costos ocultos.
- [ ] No production customer data or live fiscal credentials in AWS labs / Solo datos sintéticos.
- [ ] `terraform destroy`, state inventory, manual console inspection and billing review planned / Destrucción y verificación.

## Optional Redis/Mongo and certificate custody costs / Costos de datos y bóveda
- Local Redis/Mongo with Docker first; managed ElastiCache, MongoDB Atlas or DocumentDB may incur ongoing compute/storage/network charges even for an idle MVP. / Probar local antes de contratar.
- Count vault storage, AWS Secrets Manager secret versions/API use, KMS keys/requests, private object storage, backups and certificate renewals. Check binary secret size restrictions and encryption authorization before design. / Costos de PFX/CAF y secretos.
- No actual certificate, CAF, taxpayer data or public-chain operation in paid cloud labs without explicit owner approval. / Sin credenciales reales en pruebas cloud.

## Costs you can forget / Costos fáciles de olvidar
NAT Gateway (hourly and data); load balancer (hour and capacity); IPv4 public address (hourly); ECS/Fargate running tasks; RDS instances/storage/backups; log ingestion and retention; egress and cross-AZ traffic; S3 requests/storage and recovery copies.

## Limits are not absolute / Los límites no son absolutos
**Standard AWS Budgets notifications are not hard spending caps.** Budgets data may lag. AWS Spend limits, where eligible, have different conditions and project scope; check official docs. / Alertas de presupuesto **no garantizan impedir cobros**. Los datos pueden demorarse. Verificar Spend limits por cuenta/proyecto.

Official docs: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html ; https://docs.aws.amazon.com/accounts/latest/reference/create-spend-limit.html .

## Laboratory order / Orden de laboratorios
1. Local Docker + Nginx reverse proxy + load balancing, no billable AWS.
2. IAM + private S3 + small bounded Lambda; event simulation and logging, resource cleanup.
3. SQS + DLQ, restricted concurrency, cost review.
4. **Time-boxed** ECS/Fargate + ALB with two replicas, health check and failover; teardown same session.
5. RDS or complex VPC only with justified budget; avoid always-on EKS/NAT in early labs.

## Teardown evidence / Evidencia de destrucción
Save redacted `terraform destroy` output, list residual resources (ALB, target groups, ENIs, public IPs, NAT, ECS tasks, RDS/snapshots, S3), verify forecast/actual after billing catches up. Never automatically destroy production.
