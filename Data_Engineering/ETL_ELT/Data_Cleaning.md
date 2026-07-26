# Data Cleaning

## Definition

Data Cleaning is the process of identifying, correcting, removing, or quarantining inaccurate, incomplete, inconsistent, or duplicate data to ensure high-quality, reliable datasets for downstream analytics and machine learning.

---

# Why Data Cleaning Matters

Poor-quality data leads to:

- Incorrect business decisions
- Inaccurate dashboards
- Poor ML model performance
- Financial losses
- Compliance risks

> **Principle:** Data cleaning should improve data quality **without changing business meaning**.

---

# Data Cleaning Workflow

```text
Raw Data
    │
    ▼
Profile Data
    │
    ▼
Identify Issues
    │
    ▼
Validate Against Business Rules
    │
    ▼
Clean / Standardise / Quarantine
    │
    ▼
Validated Dataset
```

---

# Common Data Quality Issues

| Issue | Example | Typical Action |
|--------|---------|----------------|
| Missing Values | Age = NULL | Keep, Impute or Reject |
| Invalid Values | Age = -5 | Investigate → Reject if invalid |
| Out-of-range Values | Age = 250 | Validate against business rules |
| Duplicate Records | Same Order ID twice | Verify before deduplication |
| Inconsistent Formatting | INDIA / india | Standardise |
| Invalid Categories | "Ind" | Map or Reject |
| Incorrect Data Types | "Twenty" instead of 20 | Convert or Reject |

---

# Cleaning Decision Framework

```text
Issue Detected
      │
      ▼
Business Rule Exists?
      │
 ┌────┴────┐
 │         │
No        Yes
 │         │
 ▼         ▼
Investigate Apply Rule
 │         │
 └────┬────┘
      ▼
Clean / Keep / Quarantine / Reject
```

---

# Handling Missing Values

| Scenario | Action |
|----------|--------|
| Primary Key Missing | Reject / Quarantine |
| Optional Field Missing | Keep NULL |
| Numerical Feature | Impute if business allows |
| Large % Missing | Investigate upstream |

---

# Handling Duplicates

Never assume duplicates are bad.

Possible causes:

- Pipeline retry
- CDC updates
- Upstream bug
- Manual backfill
- Message reprocessing

Always determine whether the record is:

- True duplicate
- Legitimate update
- Historical version

---

# Handling Outliers

Outliers are **not always errors**.

Example:

```text
Transaction = £1,250,000
```

Possible reasons:

- Enterprise customer
- Government purchase
- Fraud
- Data corruption
- Currency conversion issue

Always investigate before removing.

---

# Standardisation

Convert multiple representations into one canonical format.

Example:

```text
INDIA
india
India
IN

↓

India
```

---

# Quarantine vs Reject

| Action | When Used |
|---------|-----------|
| Reject | Record is unusable |
| Quarantine | Record needs investigation |
| Keep | Valid according to business rules |
| Correct | Safe automatic correction exists |

---

# Real Production Example

### Scenario

Google Ads receives **500M click events/day**.

Problems detected:

- Duplicate click events
- Missing advertiser IDs
- Invalid timestamps
- Mixed country formats

Pipeline:

```text
Raw Events
      │
      ▼
Validation
      │
      ▼
Invalid Records
      │
      ├──► Quarantine
      │
      ▼
Standardisation
      │
      ▼
Deduplication
      │
      ▼
Clean Dataset
      │
      ▼
BigQuery
```

Outcome:

- Accurate billing
- Reliable dashboards
- Better ML models
- Easier debugging

---

# Best Practices

- Never clean data without understanding business rules.
- Preserve raw data whenever possible.
- Automate repeatable cleaning steps.
- Maintain audit logs of transformations.
- Validate data before loading into production systems.

---

# Common Mistakes

❌ Delete NULL values immediately

❌ Remove every outlier

❌ Deduplicate without investigation

❌ Ignore upstream pipeline issues

❌ Assume formatting differences are different entities

---

# Interview Cheat Sheet

| Question | Answer |
|----------|--------|
| What is data cleaning? | Improving data quality by correcting, validating, standardising or removing bad data. |
| Should NULL values always be removed? | No, it depends on business requirements. |
| Should duplicates always be deleted? | No, first determine whether they are true duplicates or valid updates (e.g., CDC). |
| Should outliers always be removed? | No, investigate whether they represent valid business events. |
| What is quarantine? | Isolating suspicious records for investigation instead of loading them into production. |

---

# Key Takeaways

- Business rules drive every cleaning decision.
- Investigate before modifying data.
- Preserve business meaning.
- Quarantine suspicious data instead of immediately deleting it.
- Data cleaning is an ongoing pipeline process, not a one-time task.
