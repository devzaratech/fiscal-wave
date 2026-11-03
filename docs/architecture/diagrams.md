# FiscalWave diagrams / Diagramas

**EN:** Architecture proposals only, not running services or SII authorization. PlantUML (`.puml`) is the sole source of truth; the SVG images are generated from it.

**ES:** Solo propuestas de arquitectura, no servicios operativos ni autorización del SII. PlantUML (`.puml`) es la única fuente de verdad; los SVG se generan desde esos archivos.

To regenerate / Para regenerar: `bash scripts/render-diagrams.sh` (PlantUML + Graphviz required). CI validates syntax and checks the generated images.

All SVGs have an opaque white background and dark labels for reliable viewing in light and dark GitHub themes. / Los SVG usan fondo blanco opaco y texto oscuro.

## Temporary AWS lab / Laboratorio AWS temporal

[PlantUML source / Código PlantUML](aws-lab.puml) · [SVG](rendered/aws-lab.svg)

![Temporary AWS lab / Laboratorio AWS temporal](rendered/aws-lab.svg)

## DTE lifecycle / Ciclo de vida DTE

[PlantUML source / Código PlantUML](dte-lifecycle.puml) · [SVG](rendered/dte-lifecycle.svg)

![DTE lifecycle / Ciclo de vida DTE](rendered/dte-lifecycle.svg)

## Idempotent issuance / Emisión idempotente

[PlantUML source / Código PlantUML](idempotency-sequence.puml) · [SVG](rendered/idempotency-sequence.svg)

![Idempotent issuance / Emisión idempotente](rendered/idempotency-sequence.svg)

## Personal-data boundaries / Límites de datos personales

[PlantUML source / Código PlantUML](privacy-boundaries.puml) · [SVG](rendered/privacy-boundaries.svg)

![Personal-data boundaries / Límites de datos personales](rendered/privacy-boundaries.svg)

## SII signing and PDF / Firma SII y PDF

[PlantUML source / Código PlantUML](sii-signing-and-pdf.puml) · [SVG](rendered/sii-signing-and-pdf.svg)

![SII signing and PDF / Firma SII y PDF](rendered/sii-signing-and-pdf.svg)

## System map / Mapa del sistema

[PlantUML source / Código PlantUML](system-map.puml) · [SVG](rendered/system-map.svg)

![System map / Mapa del sistema](rendered/system-map.svg)
