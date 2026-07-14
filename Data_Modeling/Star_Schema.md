# ⭐ Star Schema

## What is a Star Schema?

A **Star Schema** is a data modeling technique used in Data Warehouses where a central **Fact Table** is connected to multiple **Dimension Tables**. The structure resembles a star, making analytical queries simpler and faster.

---

# Why do we use Star Schema?

- Reduces data duplication.
- Improves query performance.
- Simplifies dashboard creation.
- Makes maintenance easier.
- Ensures consistent business definitions.

---

# Fact Table

A Fact Table stores the **business event**, **metrics**, and **foreign keys**.

It contains:

- IDs (Foreign Keys)
- Numerical values (Metrics)

Examples:

- Revenue Loss
- Investigation Time
- Violation Count
- Spend
- Clicks

### Memory Trick

> **Fact = Event + IDs + Numbers**

---

# Dimension Table

A Dimension Table stores descriptive information about the event.

Examples:

- Country
- Policy
- Advertiser
- Analyst
- Date
- Business Category

### Memory Trick

> **Dimension = Who? Where? When? Which?**

---

# Metrics vs Dimensions

## Metric

Ask:

> **What am I measuring?**

Examples:

- Revenue
- Revenue Loss
- Spend
- Investigation Time
- Violation Count

---

## Dimension

Ask:

> **How am I grouping or viewing the data?**

Examples:

- Country
- Policy
- Advertiser
- Analyst
- Month

---

# Dashboard Thinking

Every business question can be broken into three parts:

```
Metric
↓
Dimension
↓
Filter(s)
```

Example:

**Average Revenue Loss by Country for Travel advertisers during July 2026**

Metric:
- Average Revenue Loss

Dimension:
- Country

Filters:
- Business Category = Travel
- Month = July 2026

---

# The Dashboard Trick ⭐

Imagine the final dashboard.

The **first column** is almost always the **Dimension**.

Example:

| Country | Revenue Loss |
|----------|-------------:|
| India | ₹5,000 |
| USA | ₹3,000 |

Dimension = Country

---

# Why Not One Big Table?

Suppose "India" appears 10 billion times.

Problems:

- Wasted storage
- Slower queries
- Difficult updates
- Inconsistent values

Instead:

Store "India" once.

```
dim_country

country_id | country
-----------|---------
1          | India
2          | USA
```

Fact Table:

```
country_id | policy_id | revenue_loss
-----------|-----------|-------------
1          | 10        | 500
1          | 11        | 700
2          | 10        | 900
```

---

# Benefits of Star Schema

1. Less duplication
2. Easier maintenance
3. Faster joins
4. Better consistency
5. Simpler reporting

---

# Interview Framework

Before writing SQL:

1. Understand the business question.
2. Identify the Metric.
3. Identify the Dimension.
4. Identify the Filters.
5. Visualize the dashboard.
6. Write SQL.

---

# Key Takeaways

- Fact Table stores events and measurements.
- Dimension Tables store descriptions.
- Use IDs in Fact Tables.
- Store details in Dimension Tables.
- Think about the dashboard before thinking about SQL.
