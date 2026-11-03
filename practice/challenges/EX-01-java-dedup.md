# EX-01 — Deduplicate invoice requests / Deduplicar solicitudes de factura

**EN:** Given an ordered list of requests containing `tenantId`, `externalId` and `amount`, return the **first occurrence** of every unique `(tenantId, externalId)`, preserving input order. The duplicate's amount must not change the retained record. Compare IDs case-sensitively. Reject null IDs. Do not modify input.

**ES:** Dada una lista ordenada con `tenantId`, `externalId` y `amount`, retornar la **primera aparición** de cada clave compuesta preservando orden. El monto de duplicados no reemplaza la original. IDs sensibles a mayúsculas; IDs nulos inválidos; no mutar entrada.

## Example / Ejemplo
Input:
```text
(t1, ext-1, 1000)
(t2, ext-1, 2500)
(t1, ext-1, 9999)
(t1, ext-2, 1500)
```
Expected / Esperado:
```text
(t1, ext-1, 1000)
(t2, ext-1, 2500)
(t1, ext-2, 1500)
```

## Tests / Pruebas
Empty input, all unique, all duplicated, same external ID across tenants, null ID rejection, immutable input, 100k entries. Describe time and space complexity and thread-safety limitations. / Casos vacíos, duplicados, aislamiento y complejidad.

**Hint policy:** no implementation is shipped. Your solution belongs in a separately authored exercise PR with its own tests. / Sin solución prefabricada.
