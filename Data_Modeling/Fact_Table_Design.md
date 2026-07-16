# Fact Table Design

## Why does this exist?

Every business generates events such as orders, payments, clicks, searches, policy violations, or transactions.

These events contain measurable information that organizations analyze to make business decisions.

A Fact Table is designed to capture these business events efficiently while linking them to descriptive information stored in Dimension Tables.

It is the central table in a Star Schema or Snowflake Schema.

---

# Problem it solves

Imagine storing everything in one table.

| Violation ID | Country | Policy            | Analyst | Revenue Loss | Investigation Time |
| ------------ | ------- | ----------------- | ------- | ------------ | ------------------ |
| V101         | India   | Misrepresentation | John    | 1000         | 12                 |
| V102         | India   | Misrepresentation | John    | 1500         | 15                 |

Problems:

* Country repeats.
* Policy repeats.
* Analyst repeats.
* Storage increases.
* Updating descriptive information becomes difficult.
* Data inconsistency may occur.

Instead, a Fact Table stores only business events, metrics, and foreign keys to Dimension Tables.

---

# Definition

A Fact Table stores measurable business events.

Each row represents a single business event and contains:

* Business Event Identifier
* Foreign Keys referencing Dimension Tables
* Measurable business metrics

It is the central table in a Data Warehouse.

---

# Components of a Fact Table

A well-designed Fact Table consists of three parts.

## 1. Business Event

The event being measured.

Examples:

* Sale
* Order
* Payment
* Search
* Click
* Policy Violation
* Shipment

Example:

```text
Fact_Violations
```

Every row represents one policy violation.

---

## 2. Foreign Keys

Foreign Keys connect the Fact Table to Dimension Tables.

Example:

| Column        |
| ------------- |
| advertiser_id |
| policy_id     |
| country_id    |
| analyst_id    |
| date_id       |
| severity_id   |

These columns describe the business event.

---

## 3. Metrics (Facts)

Metrics are measurable values.

Examples:

* Revenue
* Revenue Loss
* Quantity
* Profit
* Investigation Time
* Click Count
* Search Latency

Example:

| Metric             |
| ------------------ |
| revenue_loss       |
| investigation_time |

---

# Example

## Fact_Violations

| violation_id | advertiser_id | policy_id | country_id | analyst_id | date_id  | severity_id | revenue_loss | investigation_time |
| ------------ | ------------- | --------- | ---------- | ---------- | -------- | ----------- | ------------ | ------------------ |
| V101         | 101           | 5         | 1          | 501        | 20260101 | 1           | 1000         | 12                 |

Notice:

The table stores:

* IDs
* Metrics

No descriptive text.

---

# What Should NOT Be Stored?

Do not store descriptive attributes.

❌ Incorrect

| country_name |
| ------------ |
| India        |

Correct

| country_id |
| ---------- |
| 1          |

The description belongs in the Country Dimension.

---

# Why Store IDs Instead of Names?

Suppose India changes its official naming convention.

If "India" is stored in millions of Fact rows:

Every row must be updated.

Instead:

Country_Dim

| country_id | country_name |
| ---------- | ------------ |
| 1          | India        |

Only one row changes.

Benefits:

* Less redundancy
* Better consistency
* Easier maintenance
* Smaller Fact Tables

---

# Design Principles

A good Fact Table should:

* Store one business event per row.
* Store only measurable metrics.
* Store only foreign keys for descriptive information.
* Avoid descriptive text.
* Support analytical queries efficiently.

---

# Grain of a Fact Table ⭐

One of the first decisions in Fact Table design is defining its **grain**.

The grain specifies what **one row** represents.

Examples:

### Fact_Sales

One row = One sales transaction.

---

### Fact_Clicks

One row = One user click.

---

### Fact_Violations

One row = One policy violation.

The grain should be clearly defined before adding columns.

---
# Real-world Example (E-commerce)

Business Question:

> Show Revenue by Product, Customer, Region, and Month.

### Business Event

Sale

### Fact Table

Fact_Sales

Metrics:

* Revenue
* Quantity
* Discount

Foreign Keys:

* Customer ID
* Product ID
* Date ID
* Region ID

---

# Mental Model

Whenever designing a Fact Table, think:

```text
Business Event
        │
        ▼
Foreign Keys
        │
        ▼
Metrics
```

---

# Fact Table Checklist

Before finalizing a Fact Table, ask:

✅ What business event does each row represent?

✅ What metrics describe that event?

✅ Which Dimension Tables describe the event?

✅ Have I stored only IDs instead of descriptive text?

---

# Interview Explanation

A Fact Table stores measurable business events.

Each row represents one event and contains:

* Foreign Keys to Dimension Tables
* Measurable metrics

Descriptive information belongs in Dimension Tables to reduce redundancy and improve maintainability.

---

# Interview Q&A ⭐

## Q1. What is a Fact Table?

### Here's How I'd Answer

A Fact Table stores measurable business events.

It contains business metrics along with foreign keys that reference Dimension Tables.

Each row represents one business event.

---

## Q2. What should be stored in a Fact Table?

### Here's How I'd Answer

A Fact Table should contain:

* Business event identifier
* Foreign keys to Dimension Tables
* Measurable business metrics

It should avoid storing descriptive text.

---

## Q3. Why should descriptive text not be stored in a Fact Table?

### Here's How I'd Answer

Descriptive information belongs in Dimension Tables.

Storing names such as country or policy directly in the Fact Table creates redundancy, increases storage, and makes maintenance difficult.

Using foreign keys improves consistency and simplifies updates.

---

## Q4. What is the grain of a Fact Table?

### Here's How I'd Answer

The grain defines what a single row in the Fact Table represents.

For example, one row may represent one sale, one click, one payment, or one policy violation.

The grain should always be defined before designing the table.

---

## Q5. Why is the Fact Table placed at the center of a Star Schema?

### Here's How I'd Answer

The Fact Table represents the business event being analyzed.

Dimension Tables provide descriptive context about that event.

Since all analytical questions revolve around business events, the Fact Table naturally becomes the center of the schema.

---

## Q6. How do you decide whether a column belongs in the Fact Table?

### Here's How I'd Answer

I ask three questions:

1. Is it the business event or does it describe the event?
2. Is it a measurable metric?
3. Is it descriptive information?

Metrics and foreign keys belong in the Fact Table, while descriptive attributes belong in Dimension Tables.

---

# Common Mistakes

❌ Storing descriptive text in the Fact Table.

✅ Store foreign keys instead.

---

❌ Mixing multiple business events in one Fact Table.

✅ One Fact Table should have one clearly defined grain.

---

❌ Creating a Fact Table without defining its grain.

✅ Always define what one row represents first.

---

❌ Naming the Fact Table after a metric.

✅ Name it after the business event.

Examples:

* Fact_Sales
* Fact_Orders
* Fact_Clicks
* Fact_Searches
* Fact_Violations

---

# Key Takeaways

* A Fact Table stores business events.
* One row represents one business event.
* Store metrics in the Fact Table.
* Store foreign keys to Dimension Tables.
* Avoid descriptive text.
* Define the grain before designing the table.

---

# Revision Notes

## Practical Decision Flow

Whenever designing a Fact Table:

1. Identify the business event.
2. Define the grain.
3. Identify the metrics.
4. Identify the Dimension Tables.
5. Store only foreign keys and metrics.

---

## Quick Interview Revision

| Concept        | One-Line Summary                       |
| -------------- | -------------------------------------- |
| Business Event | What happened?                         |
| Grain          | What does one row represent?           |
| Foreign Keys   | Describe the event through Dimensions. |
| Metrics        | Measure the event.                     |

### Memory Trick

* **Business Event** → Fact Table
* **One Row** → One Event
* **Metrics** → Facts
* **Descriptions** → Dimension Tables

---

## One-Line Summary

> **A Fact Table stores one business event per row, along with its measurable metrics and foreign keys to Dimension Tables, enabling fast and scalable analytical reporting.**
