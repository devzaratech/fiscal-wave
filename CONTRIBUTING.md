# Contributing / Contribuir

**EN:** This project is in discovery. Open an issue/PR linked to an `FW-xxx` backlog item. State scope, test evidence, EN/ES documentation changes and whether SII or cloud costs are affected. Use synthetic data. Never commit secrets. Prefer small PRs with independent review. No unsupported claims about SII authorization.

**ES:** Proyecto en descubrimiento. Vincula cada issue/PR a un `FW-xxx`; documenta alcance, pruebas, cambios EN/ES e impacto tributario/costos. Usa datos sintéticos, no subas secretos y evita declaraciones no verificadas de certificación.

## PR checklist / Lista de revisión
- [ ] Backlog ID and acceptance criteria / ID y criterios de aceptación
- [ ] Tests executed and results described / Evidencia real de pruebas
- [ ] EN/ES reviewed / Idiomas revisados
- [ ] Security and tenant isolation checked / Seguridad y aislamiento
- [ ] Cost estimate and teardown if AWS used / Costo y destrucción si usa AWS
- [ ] Architecture/API/event contracts updated / Contratos y diagramas
- [ ] SII evidence linked if fiscal behavior changed / Evidencia SII si aplica

Branch convention: `feat/FW-xxx-summary`, `docs/FW-xxx-summary`, `fix/FW-xxx-summary`.
