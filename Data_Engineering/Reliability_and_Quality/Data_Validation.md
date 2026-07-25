# Data Validation

## Why Does This Exist?

Data is one of an organisation's most valuable assets. However, **incorrect, incomplete, duplicate, or inconsistent data** can lead to poor business decisions, inaccurate reports, financial losses, and unreliable machine learning models.

Data Validation ensures that only **accurate, complete, and meaningful** data enters downstream systems such as Data Warehouses, Dashboards, and ML pipelines.

> **Principle:** *Garbage In → Garbage Out (GIGO).*

---

# Definition

> **Data Validation is the process of verifying that incoming data meets predefined quality, business, and integrity rules before it is processed or stored.**

**Goal:** Ensure data is **accurate, complete, consistent, reliable, and usable**.

---

# Data Validation at a Glance

| Aspect | Description |
|---------|-------------|
| Purpose | Ensure data quality before processing |
| Goal | Prevent incorrect data from entering the system |
| Focus | Accuracy, Completeness, Consistency |
| Prevents | Incorrect reports, wrong business decisions, poor ML predictions |
| Common Techniques | NULL Checks, Data Type Validation, Range Checks, Referential Integrity, Business Rules |

---

# Why is Data Validation Important?

| Without Data Validation | With Data Validation |
|--------------------------|----------------------|
| Incorrect dashboards | Reliable dashboards |
| Wrong KPIs | Accurate KPIs |
| Financial reporting errors | Trustworthy reporting |
| Poor ML predictions | Better model performance |
| Duplicate records | Clean datasets |
| Business decisions based on incorrect data | Data-driven decisions |

---

# Where Should Data Validation Happen?

> **Best Practice:** Validate as early as possible and verify continuously.

| Stage | Validation Examples | Purpose |
|--------|---------------------|---------|
| Source/Application | Required fields, input format, mandatory fields | Prevent invalid data from entering the system |
| ETL/ELT Pipeline | NULL checks, data types, duplicates, business rules | Clean and transform incoming data |
| Data Warehouse | Referential integrity, row counts, reconciliation | Ensure stored data is complete and consistent |
| Reporting Layer | KPI validation, freshness checks, anomaly detection | Ensure business users see reliable data |

---

# Data Validation Pipeline

```text
                Source System
                     │
                     ▼
          Source Validation
                     │
                     ▼
            ETL / ELT Pipeline
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      Validation Pass      Validation Fail
          │                     │
          ▼                     ▼
   Data Warehouse       Quarantine Table
          │                     │
          ▼                     ▼
 Business Dashboards     Investigation
          │
          ▼
 Business Decisions
```

---

# Common Validation Rules

| Validation Type | Example | Purpose |
|-----------------|---------|---------|
| NULL Check | Customer_ID cannot be NULL | Prevent incomplete records |
| Data Type Validation | Sales must be DECIMAL | Ensure correct data type |
| Range Validation | Sales ≥ £0 | Prevent invalid values |
| Format Validation | Email format | Validate structured fields |
| Business Rule Validation | Quantity > 0 | Follow business requirements |
| Uniqueness Validation | Order_ID must be unique | Prevent duplicates |
| Referential Integrity | Customer_ID exists in Customer table | Maintain relationships |
| Schema Validation | Expected columns exist | Prevent schema mismatch |
| Anomaly Detection | £5,000,000 order | Detect unusual values |

---

# Validation Types Explained

| Validation | Example | Action |
|------------|---------|--------|
| Required Field | Customer_ID = NULL | Reject / Quarantine |
| Data Type | "ABC" in Amount column | Reject |
| Range Check | Quantity = -5 | Reject |
| Duplicate Check | Duplicate Order_ID | Reject / Merge |
| Format Check | Invalid Email | Reject |
| Business Rule | Age < 18 for adult account | Reject |
| Referential Integrity | Customer doesn't exist | Retry or Quarantine (depends on cause) |
| Anomaly Detection | Extremely high transaction amount | Flag for review |

---

# Business Impact of Bad Data

| Problem | Business Impact |
|----------|-----------------|
| Incorrect Revenue | Wrong financial reports |
| Missing Customers | Lost customer insights |
| Duplicate Orders | Incorrect sales figures |
| Invalid Transactions | Poor business decisions |
| Bad Training Data | Poor ML model accuracy |
| Incorrect KPIs | Loss of stakeholder trust |

---

# Range Validation Example

| Order_ID | Sales (£) | Result |
|----------|----------:|--------|
| 101 | 250 | ✅ Valid |
| 102 | -500 | ❌ Reject |
| 103 | 950 | ✅ Valid |
| 104 | 5,000,000 | ⚠️ Investigate (Possible anomaly) |

> **Rule:** A value can be technically valid but still be statistically unusual.

---

# Validation Decision Flow

```text
Incoming Record
       │
       ▼
Basic Validation
(NULL, Type, Format)
       │
 ┌─────┴─────┐
 │           │
Pass       Fail
 │           │
 ▼           ▼
Business Rules
            Quarantine
 │
 ▼
Range Validation
 │
 ▼
Referential Integrity
 │
 ▼
Warehouse
```

---

# What Should Happen to Invalid Data?

**Do not stop the entire pipeline because of a few bad records.**

| Option | Result | Recommendation |
|---------|--------|----------------|
| Reject Entire Batch | High downtime | ❌ Not Recommended |
| Load Everything | Poor data quality | ❌ Not Recommended |
| Load Valid Records + Quarantine Invalid Records | Business continuity + Data quality | ✅ Best Practice |

---

# Quarantine Table

A **Quarantine Table** stores records that fail data validation for later investigation.

```text
Incoming Data
      │
      ▼
Validation
      │
 ┌────┴────┐
 │         │
 ▼         ▼
Valid   Invalid
 │         │
 ▼         ▼
Warehouse  Quarantine
             │
             ▼
      Investigation
             │
      ┌──────┴──────┐
      ▼             ▼
 Fix & Reload   Archive/Reject
```

---

# Retry vs Quarantine vs Dead Letter Queue

| Situation | Retry | Quarantine | Dead Letter Queue |
|-----------|:-----:|:----------:|:-----------------:|
| Network Timeout | ✅ | ❌ | After retry limit |
| API Unavailable | ✅ | ❌ | After retry limit |
| Database Connection Lost | ✅ | ❌ | After retry limit |
| NULL Customer_ID | ❌ | ✅ | ❌ |
| Negative Sales | ❌ | ✅ | ❌ |
| Invalid Email | ❌ | ✅ | ❌ |
| Message failed after all retries | ❌ | ❌ | ✅ |

---

# Quarantine vs Dead Letter Queue (DLQ)

| Feature | Quarantine Table | Dead Letter Queue |
|----------|------------------|-------------------|
| Purpose | Store invalid data | Store failed messages |
| Failure Type | Data quality issue | Processing failure |
| Retry Later | After data correction | After system recovery |
| Example | Missing Customer_ID | API timeout after retries |
| Owner | Data Engineering | Platform Engineering |

> **Rule:** Ask yourself **"Is the data bad or is the system bad?"**

- **Bad Data → Quarantine**
- **System Failure → Retry → DLQ**

---

# Referential Integrity

> **Referential Integrity ensures that relationships between tables remain valid.**

Example:

### Customers

| Customer_ID | Name |
|-------------|------|
| C101 | Alice |
| C102 | Bob |

### Orders

| Order_ID | Customer_ID |
|----------|-------------|
| O1001 | C999 ❌ |

Customer **C999** does not exist.

### Decision

```text
Order Arrives
      │
      ▼
Customer Exists?
      │
 ┌────┴────┐
 │         │
Yes       No
 │         │
 ▼         ▼
Load   Retry / Quarantine
```

---

# Strong vs Eventual Consistency

| Strong Consistency | Eventual Consistency |
|--------------------|----------------------|
| Parent record must exist immediately | Parent may arrive later |
| Common in Banking | Common in Distributed Systems |
| Reject missing references | Retry until dependency arrives |
| Higher consistency | Higher scalability |

---

# Data Validation Best Practices

| Practice | Benefit |
|----------|---------|
| Validate early | Prevent bad data entering the pipeline |
| Use business rules | Improve data accuracy |
| Quarantine invalid records | Avoid blocking the pipeline |
| Retry transient failures | Recover temporary issues |
| Maintain audit logs | Improve traceability |
| Continuously monitor quality | Detect issues proactively |
| Review validation rules regularly | Adapt to business changes |

---

# Common Mistakes

| Mistake | Impact |
|----------|--------|
| Only validating in the warehouse | Bad data travels too far |
| Rejecting entire batches | Unnecessary downtime |
| Loading all records | Poor data quality |
| Deleting invalid records immediately | Loss of audit history |
| Infinite retries | Pipeline blockage |
| Ignoring anomalies | Incorrect business insights |
| Missing referential integrity checks | Broken relationships |

---

# Real-World Examples

| Company/System | Validation Example |
|----------------|--------------------|
| Amazon | Validate orders before fulfilment |
| Google Ads | Validate advertiser and campaign data |
| Banking | Validate account and transaction details |
| Healthcare | Validate patient records |
| Uber | Validate trip and driver information |
| Netflix | Validate viewing event data before analytics |

---

# Interview Cheat Sheet

| Question | Short Answer |
|----------|--------------|
| What is Data Validation? | Process of ensuring data meets predefined quality rules before processing. |
| Why is it important? | Prevents incorrect reports, KPIs, and business decisions. |
| Where should validation happen? | Source, ETL/ELT, Warehouse, and Reporting layers. |
| What is a Quarantine Table? | Stores invalid records for investigation. |
| What is a DLQ? | Stores messages that failed processing after all retries. |
| Difference between Quarantine and DLQ? | Quarantine = bad data; DLQ = processing failures. |
| What is Referential Integrity? | Ensures foreign keys reference valid parent records. |
| Why use anomaly detection? | Detect unusual but potentially valid records. |
| Why not reject an entire batch? | Preserve business continuity while isolating bad records. |

---

# Summary

Data Validation is the foundation of trustworthy data engineering. By combining **validation rules**, **business logic**, **referential integrity**, **quarantine tables**, **retry strategies**, and **dead letter queues**, organisations ensure that only reliable, high-quality data reaches downstream systems, enabling accurate reporting, dependable machine learning models, and confident business decision-making.
