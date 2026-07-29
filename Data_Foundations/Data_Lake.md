# Data Lake

## Definition

A **Data Lake** is a centralized repository that stores **structured, semi-structured, and unstructured data** in its native format. Data is stored first and transformed later (**Schema-on-Read**).

---

# Why Use a Data Lake?

Traditional databases are optimized for transactions, not large-scale storage of diverse data.

Modern applications generate data such as:

- Transactional data
- Application logs
- Clickstream events
- IoT sensor data
- Images & Videos
- PDFs
- JSON/XML
- Machine Learning datasets

A Data Lake provides scalable, low-cost storage for all of these.

---

# Data Types

| Type | Examples |
|-------|----------|
| Structured | Orders, Customers, Payments |
| Semi-Structured | JSON, XML, Event Logs |
| Unstructured | Images, Videos, PDFs, Audio |

---

# Why Not Store Everything in a Database?

| Database Limitation | Explanation |
|---------------------|-------------|
| Poor scalability | Expensive at large scale |
| High storage cost | Optimized for transactions |
| Limited data formats | Poor support for unstructured data |
| Historical storage | Inefficient for long-term archival |

---

# Typical Architecture

```text
Operational Databases
Application Logs
IoT Devices
External APIs
Customer Files
        │
        ▼
    Data Lake
```

---

# Medallion Architecture

Modern Data Lakes organize data into three quality layers.

```text
                 Data Lake

             🥉 Bronze
                 │
                 ▼
             🥈 Silver
                 │
                 ▼
              🥇 Gold
```

## Layer Comparison

| Layer | Purpose | Quality | Operations | Users | Examples |
|--------|---------|---------|------------|-------|----------|
| 🥉 Bronze | Store raw source data | Raw | Ingestion only | Data Engineers | JSON logs, CSVs, clickstream |
| 🥈 Silver | Clean and validate | Clean | Deduplication, validation, standardization | Data Engineers, Data Scientists | Clean Orders, Customers |
| 🥇 Gold | Business-ready datasets | Curated | Aggregation, enrichment, KPIs | BI Teams, Executives | Revenue, CLV, Sales Dashboard |

---

# Data Flow

```text
Raw Sources
      │
      ▼
🥉 Bronze
(Raw)
      │
Cleaning
Validation
Transformation
      ▼
🥈 Silver
(Clean)
      │
Aggregation
Enrichment
Business Rules
      ▼
🥇 Gold
(Business Ready)
      │
      ▼
Data Warehouse
      │
      ▼
Dashboards • Reports • ML
```

---

# Layer Cheat Sheet

| Question | Bronze | Silver | Gold |
|-----------|---------|---------|------|
| Raw data? | ✅ | ❌ | ❌ |
| Cleaned? | ❌ | ✅ | ✅ |
| Business-ready? | ❌ | ⚠️ Partially | ✅ |
| Source of truth? | ✅ | ❌ | ❌ |
| Immutable? | ✅ | ❌ | ❌ |
| Used by BI teams? | ❌ | Sometimes | ✅ |

---

# Why Bronze Must Be Immutable

Never modify Bronze data.

Benefits:

- Source of truth
- Auditing
- Debugging
- Reprocessing
- Disaster recovery

Always perform transformations in Silver or Gold.

---

# Data Swamp

A poorly governed Data Lake becomes a **Data Swamp**.

Symptoms:

- Duplicate datasets
- Unknown data ownership
- Inconsistent naming
- No metadata
- Difficult discovery

Prevent using:

- Medallion Architecture
- Metadata catalogues
- Data governance
- Naming conventions

---

# Database vs Data Lake vs Data Warehouse

| Feature | Database (OLTP) | Data Lake | Data Warehouse (OLAP) |
|----------|-----------------|-----------|------------------------|
| Purpose | Transactions | Raw Storage | Analytics |
| Data | Structured | Any Format | Structured |
| Schema | Schema-on-Write | Schema-on-Read | Schema-on-Write |
| Users | Applications | Data Engineers | Analysts |
| Cost | High | Low | Medium |
| Examples | MySQL, PostgreSQL | Amazon S3, Azure Data Lake, Google Cloud Storage | BigQuery, Snowflake, Redshift |

---

# When to Use What?

| Scenario | Best Choice |
|----------|-------------|
| Banking Transactions | Database |
| Store JSON Logs | Data Lake |
| Dashboard Queries | Data Warehouse |
| Machine Learning Data | Data Lake |
| Business Reporting | Data Warehouse |

---

# Startup vs Enterprise

## Startup

```text
Application
      │
      ▼
Database
      │
      ▼
Data Warehouse
      │
      ▼
Dashboards
```

Use this when:

- Small team
- Low data volume
- Limited budget
- Few data sources

Avoid unnecessary complexity.

---

## Enterprise

```text
Operational Database
        │
        ▼
     Data Lake
 Bronze → Silver → Gold
        │
        ▼
 Data Warehouse
        │
        ▼
Dashboards • ML • Reporting
```

As data volume, variety, and use cases grow, introducing a Data Lake becomes valuable.

---

# Production Example

### Netflix

```
Users
      │
      ▼
Video Streams
Click Events
Payments
Application Logs
      │
      ▼
Data Lake
      │
      ▼
Bronze
      │
      ▼
Silver
      │
      ▼
Gold
      │
      ▼
BigQuery / Snowflake
      │
      ▼
Dashboards & Recommendation Models
```

---

# Best Practices

- Store data in its native format.
- Keep Bronze immutable.
- Use Bronze → Silver → Gold layering.
- Store data using columnar formats (Parquet, ORC).
- Partition large datasets.
- Maintain metadata and governance.
- Monitor data quality continuously.
- Archive historical data instead of deleting it.

---

# Common Mistakes

- Using a Data Lake as a transactional database.
- Editing Bronze data.
- Mixing raw and curated datasets.
- Duplicate copies of the same dataset.
- Poor folder structure.
- Missing metadata.
- Allowing a Data Swamp to form.
- Building a Data Lake when a database is sufficient.

---

# Interview Cheat Sheet

### What is a Data Lake?

A centralized repository that stores structured, semi-structured, and unstructured data in its native format.

---

### Why use a Data Lake?

To store massive amounts of diverse data cheaply for analytics, reporting, and machine learning.

---

### What is Medallion Architecture?

A layered approach to organizing data:

- 🥉 Bronze → Raw
- 🥈 Silver → Cleaned & Validated
- 🥇 Gold → Business Ready

---

### Why is Bronze immutable?

To preserve the source of truth for auditing, debugging, and safe reprocessing.

---

### Database vs Data Lake vs Data Warehouse

- **Database:** Run applications (OLTP)
- **Data Lake:** Store raw data
- **Data Warehouse:** Run analytics (OLAP)

---

### Does every company need a Data Lake?

No.

Use the simplest architecture that satisfies current business needs. Small companies may only require a Database and a Data Warehouse. Introduce a Data Lake as data volume, variety, and analytical requirements increase.

---

# Key Takeaways

- Data Lakes store **any type of data** in its native format.
- They complement—not replace—databases and data warehouses.
- Bronze is **immutable** and serves as the source of truth.
- Silver improves data quality through cleaning and validation.
- Gold contains curated datasets for analytics.
- Good governance prevents a Data Lake from becoming a Data Swamp.
- Build architectures based on business requirements—not company size or trends.
