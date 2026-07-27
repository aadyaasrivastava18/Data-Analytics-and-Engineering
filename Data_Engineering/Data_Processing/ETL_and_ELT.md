# ETL vs ELT

## Definition

**ETL (Extract → Transform → Load)** transforms data before loading it into the data warehouse.

**ELT (Extract → Load → Transform)** loads raw data first and performs transformations inside the data warehouse.

---

# Why ETL Exists

Operational databases are optimized for **transactions**, not analytics.

Problems with querying production databases directly:

- Heavy analytical queries slow down transactions
- Data is spread across multiple systems
- Inconsistent formats and missing values
- Business metrics are not precomputed
- Analytics can impact production performance

---

# ETL Workflow

```text
Operational Databases
        │
        ▼
     Extract
        │
        ▼
 Transform
(Clean, Validate, Join)
        │
        ▼
 Load to Warehouse
        │
        ▼
 Analytics / BI
```

---

# ELT Workflow

```text
Operational Databases
        │
        ▼
     Extract
        │
        ▼
 Load Raw Data
        │
        ▼
Cloud Data Warehouse
        │
        ▼
 Transform
(SQL / Spark)
        │
        ▼
 Analytics / ML
```

---

# ETL vs ELT

| Feature | ETL | ELT |
|---------|-----|-----|
| Transformation | Before loading | After loading |
| Processing | ETL Server | Data Warehouse |
| Best For | Sensitive & regulated data | Large-scale cloud analytics |
| Performance | Limited by ETL server | Distributed compute |
| Scalability | Moderate | High |
| Raw Data Storage | Usually No | Yes |

---

# Typical Transformations

| Transformation | Example |
|---------------|---------|
| Validation | Remove invalid records |
| Cleaning | Handle nulls & duplicates |
| Standardisation | "India", "INDIA" → "India" |
| Joins | Orders + Customers |
| Enrichment | Add customer segment |
| Aggregation | Revenue by month |

---

# ETL Bottleneck

```text
Extract
   │
   ▼
Transform (Small Server)
   │
   ▼
Load

❌ Limited CPU
❌ Long processing time
❌ Difficult to scale
```

---

# Why ELT Became Popular

```text
Extract
   │
   ▼
Load
   │
   ▼
Cloud Warehouse
(BigQuery / Snowflake)
   │
   ▼
Distributed Transformations

✓ Parallel Processing
✓ Massive Scale
✓ Faster Analytics
```

---

# When to Use ETL

- Sensitive data requires masking
- Regulatory compliance (GDPR, PCI DSS, HIPAA)
- Data must be validated before storage
- Small to medium workloads
- Legacy on-premise systems

---

# When to Use ELT

- Cloud-native architecture
- BigQuery, Snowflake, Redshift, Databricks
- TB–PB scale datasets
- Preserve raw data
- High-performance analytical workloads

---

# Hybrid Architecture (Modern Approach)

```text
Extract
    │
    ├──────────────┐
    │              │
    ▼              ▼
Mask PII       Load Raw Data
(ETL)             (ELT)
    │              │
    └──────┬───────┘
           ▼
Cloud Data Warehouse
           │
           ▼
SQL Transformations
           │
           ▼
Dashboards / ML
```

---

# Decision Matrix

| Scenario | Choice |
|----------|--------|
| Banking | ETL |
| Healthcare | ETL |
| Google Analytics | ELT |
| BigQuery Pipeline | ELT |
| Sensitive Data + Cloud | Hybrid |

---

# Interview Cheat Sheet

| Question | Answer |
|----------|--------|
| What is ETL? | Transform data before loading. |
| What is ELT? | Load raw data first, transform later. |
| Why ETL? | Security, validation, compliance. |
| Why ELT? | Scalability and distributed processing. |
| Why BigQuery prefers ELT? | Warehouse compute scales better than ETL servers. |
| Does ELT replace ETL? | No. Modern architectures often use a hybrid approach. |

---

# Key Takeaways

- ETL prepares data **before** loading.
- ELT transforms data **after** loading.
- ETL is ideal for compliance and sensitive data.
- ELT leverages cloud warehouse compute for large-scale processing.
- Most modern data platforms use a **Hybrid (ETL + ELT)** approach.
