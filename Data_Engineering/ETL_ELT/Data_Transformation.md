# Data Transformation

## Definition

Data Transformation is the process of converting, restructuring, enriching, or deriving data into a format that is better suited for analytics, reporting, machine learning, or downstream business processes.

> **Purpose:** Make data more useful, not necessarily cleaner.

---

# Why Data Transformation Matters

Raw data is rarely in a format that businesses can directly consume.

Transformation helps to:

- Improve analytical usability
- Apply business rules
- Create meaningful features
- Integrate multiple datasets
- Prepare data for dashboards and ML models

---

# Data Transformation Workflow

```text
Raw Data
    │
    ▼
Business Requirements
    │
    ▼
Transformation Logic
    │
    ▼
Derived / Restructured Data
    │
    ▼
Analytics / BI / ML
```

---

# Data Cleaning vs Data Transformation

| Data Cleaning | Data Transformation |
|---------------|---------------------|
| Improves data quality | Improves data usability |
| Fixes incorrect or inconsistent data | Changes structure or representation |
| Removes duplicates | Creates new business features |
| Handles missing values | Aggregates, joins and derives data |
| Standardises incorrect values | Reshapes data for analytics |

---

# Common Transformations

## 1. Standardisation

```text
india
INDIA
India

↓

India
```

Purpose:

Maintain a consistent representation.

---

## 2. Derivation

```text
Salary

↓

Salary Band
```

Example:

| Salary | Salary Band |
|---------|-------------|
| £20,000 | Low |
| £45,000 | Medium |
| £80,000 | High |

---

## 3. Aggregation

```text
Daily Revenue

↓

Monthly Revenue
```

Example:

| Date | Revenue |
|------|--------:|
| 01-Jan | £100 |
| 02-Jan | £200 |
| 03-Jan | £300 |

↓

| Month | Revenue |
|-------|--------:|
| January | £600 |

---

## 4. Join

```text
Customers
      │
      ├──────────┐
      │          │
      ▼          ▼
            Orders
                │
                ▼
              JOIN
                │
                ▼
      Enriched Dataset
```

Example:

| Customer ID | Name |
|-------------|------|
|101|Alice|

+

| Order ID | Customer ID | Amount |
|----------|-------------|--------:|
|O1|101|£500|

↓

| Order ID | Name | Amount |
|----------|------|--------:|
|O1|Alice|£500|

---

## 5. Merge

```text
First Name + Last Name

↓

Full Name
```

---

## 6. Split

```text
Full Name

↓

First Name
Last Name
```

---

## 7. Filtering

```text
All Customers

↓

Active Customers
```

---

## 8. Data Type Conversion

```text
"25"

↓

25
```

---

## 9. Pivot / Unpivot

Convert data between rows and columns for reporting and analytics.

---

# Summary of Transformation Types

| Transformation | Purpose | Example |
|----------------|---------|---------|
| Standardisation | Consistent format | `india → India` |
| Derivation | Create new columns | Salary → Salary Band |
| Aggregation | Summarise data | Daily → Monthly Revenue |
| Join | Combine datasets | Orders + Customers |
| Filter | Keep required records | Active customers only |
| Merge | Combine columns | First Name + Last Name |
| Split | Break one column into many | Full Name → First + Last |
| Data Type Conversion | Change data type | `"25"` → `25` |
| Pivot / Unpivot | Reshape data | Rows ↔ Columns |

---

# Real Production Example

### Scenario

A Google Ads reporting pipeline receives:

- Click Events
- Advertiser Data
- Campaign Data

Business wants a dashboard showing:

- Advertiser Name
- Campaign Name
- Daily Spend
- Spend Category

Pipeline:

```text
Click Events
      │
      ├──────────────┐
      │              │
Advertisers      Campaigns
      │              │
      └──────┬───────┘
             ▼
           JOIN
             │
             ▼
      Aggregate Spend
             │
             ▼
 Create Spend Category
             │
             ▼
 Reporting Dataset
```

Result:

- Richer dashboards
- Faster reporting
- Better business insights

---

# Best Practices

- Preserve raw data whenever possible.
- Make transformations deterministic and reproducible.
- Document every business rule.
- Keep transformation logic modular.
- Validate transformed data before publishing.

---

# Common Mistakes

❌ Confusing cleaning with transformation

❌ Hardcoding business rules

❌ Losing raw data

❌ Applying transformations without understanding business requirements

❌ Mixing multiple transformation stages into one large job

---

# Interview Cheat Sheet

| Question | Answer |
|----------|--------|
| What is data transformation? | Converting or restructuring data into a business-friendly format. |
| Why is transformation needed? | Raw data is rarely suitable for analytics or reporting. |
| Is creating Salary Band a transformation? | Yes, it is a derived feature. |
| Is Daily → Monthly Revenue a transformation? | Yes, it is an aggregation. |
| Is joining two datasets a transformation? | Yes, it enriches data by combining related information. |

---

# Key Takeaways

- Transformation focuses on **business usability**, not data quality.
- Business rules drive transformation logic.
- Aggregation, joins, derivation, filtering and merging are common transformation types.
- Most production pipelines perform multiple transformations before data reaches analytics.
- Always preserve raw data and make transformation logic reproducible.
