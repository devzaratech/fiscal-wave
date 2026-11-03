# Visión de producto (ES)

**Objetivo de producto:** que un contribuyente chileno debidamente habilitado pueda emitir y seguir un documento tributario electrónico mediante una API segura y auditable, con tratamiento confiable de errores y portal bilingüe.

## Cliente y necesidad
Primeros usuarios: desarrolladores que integran ERP y pequeñas empresas que necesitan facturación programable. Valor inicial: ciclo documental seguro, no solo fabricar XML.

## Primera entrega vertical (MVP)
Datos sintéticos de emisor y receptor; modelo y cálculos DTE 33/34; simulación de CAF/folios antes de habilitación real; firma y validación XML basadas en especificaciones oficiales verificadas; conector a pruebas SII cuando existan autorizaciones; máquina de estados; MFE mínimo de facturas y operaciones; eventos persistidos; ejecución local.

## Ciclo fiscal completo / Complete fiscal document scope
El MVP deberá custodiar PFX/P12 autorizado **separado** del CAF y su clave de timbre, validar XSD oficiales, generar XML firmado inmutable, renderizar PDF417 y conservar el XML. La certificación exige pruebas, muestras impresas e intercambio bajo autorización SII. Redis y MongoDB no deben impedir emitir un DTE. [Ciclo SII](../planning/SII-DTE-LIFECYCLE.md) · [Matriz de proveedores](../planning/PROVIDER-CAPABILITIES.md). Todavía son capacidades pendientes.

## Fuera del alcance inicial
Custodia de dinero, adquirencia, suscripciones, fiscalidad internacional, multinube activa-activa, afirmar certificación SII, facturación productiva, datos reales y AWS encendido permanentemente.

## Diferenciación a validar
API para desarrolladores, errores claros, auditoría, UX bilingüe, contratos estables y costos cloud controlables. No afirmar validación comercial antes de entrevistar clientes.

## Resultado comercial y laboral
- Producto: un flujo chileno de DTE completo y probado, con evidencia SII oficial cuando corresponda.
- Portafolio: Java/Spring, SQL, REST, eventos, React/TypeScript, Docker, IAM/S3/Lambda, ALB y Terraform demostrables.
- Negocio: piloto solo tras cumplir requisitos fiscales, legales y de seguridad.

Estas son metas, no capacidades ya entregadas.
