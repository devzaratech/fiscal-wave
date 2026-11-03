-- Synthetic training data / Datos sintéticos para practicar SQL.
-- Use an isolated PostgreSQL schema/database. Not tax-authoritative.
CREATE TABLE practice_tenants (
    tenant_id TEXT PRIMARY KEY
);
CREATE TABLE practice_customers (
    tenant_id TEXT NOT NULL REFERENCES practice_tenants(tenant_id),
    customer_id TEXT NOT NULL,
    display_name TEXT NOT NULL,
    PRIMARY KEY (tenant_id, customer_id)
);
CREATE TABLE practice_invoices (
    tenant_id TEXT NOT NULL,
    invoice_id TEXT NOT NULL,
    customer_id TEXT NOT NULL,
    issued_on DATE NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('paid', 'partial', 'unpaid')),
    PRIMARY KEY (tenant_id, invoice_id),
    FOREIGN KEY (tenant_id, customer_id) REFERENCES practice_customers(tenant_id, customer_id)
);
CREATE TABLE practice_payments (
    tenant_id TEXT NOT NULL,
    payment_id TEXT NOT NULL,
    invoice_id TEXT NOT NULL,
    paid_on DATE NOT NULL,
    amount_clp BIGINT NOT NULL CHECK (amount_clp > 0),
    PRIMARY KEY (tenant_id, payment_id),
    FOREIGN KEY (tenant_id, invoice_id) REFERENCES practice_invoices(tenant_id, invoice_id)
);
INSERT INTO practice_tenants VALUES ('t1'), ('t2');
INSERT INTO practice_customers VALUES
 ('t1','c1','Synthetic Alpha'), ('t1','c2','Synthetic Beta'),
 ('t1','c3','Synthetic Gamma'), ('t2','c1','Synthetic Delta');
INSERT INTO practice_invoices VALUES
 ('t1','i1','c1','2026-10-03','paid'),
 ('t1','i2','c2','2026-10-05','paid'),
 ('t1','i3','c3','2026-10-06','unpaid'),
 ('t1','i4','c1','2026-10-28','partial'),
 ('t2','i1','c1','2026-10-10','paid'),
 ('t1','i5','c2','2026-11-02','paid');
INSERT INTO practice_payments VALUES
 ('t1','p1','i1','2026-10-05',10000),
 ('t1','p2','i2','2026-10-06',13000),
 ('t1','p3','i4','2026-10-30',4000),
 ('t1','p4','i4','2026-10-31',6000),
 ('t2','p1','i1','2026-10-11',25000),
 ('t1','p5','i5','2026-11-03',7500);
