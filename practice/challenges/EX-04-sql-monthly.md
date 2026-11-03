# EX-04 — Top customers by payments / Clientes con mayores pagos

**EN:** Using [synthetic fixtures](../sql/fixtures.sql), report the top 3 customers per tenant and calendar month by **actual payments collected**. Include tenant, month, customer and total paid in CLP. Rank ties deterministically by customer ID. Ignore unpaid invoices. Treat each payment once. State how to handle refunds if they are introduced later.

**ES:** Con el [fixture sintético](../sql/fixtures.sql), obtener los tres clientes por empresa y mes con **mayor pago efectivamente cobrado**. Mostrar empresa, mes, cliente y total CLP. Desempatar por ID; omitir impagos; evitar dobles conteos. Explicar tratamiento futuro de reembolsos.

## Constraints / Restricciones
- PostgreSQL SQL, with JOIN + GROUP BY and a window function (ROW_NUMBER or equivalent).
- Explain indexing strategy and why a query is not enough to prevent duplicate folios.
- Test two tenants sharing IDs, more than one payment per invoice, ties, month boundary and empty months.

**Expected fixture facts / Hechos del fixture:** tenant t1 has multiple October 2026 payments and tenant t2 must remain isolated. Do not hard-code ranks.
