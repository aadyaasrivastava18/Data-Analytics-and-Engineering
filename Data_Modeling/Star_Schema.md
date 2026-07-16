# Star Schema

## Why does this exist?

As organisations grow, they collect millions or even billions of business events such as orders, transactions, clicks, searches, and policy violations.

Business users need to analyse this data quickly from different perspectives like country, product, customer, analyst, or date.

Star Schema organizes data for fast analytical queries by separating measurable business events from descriptive information.

It is the most widely used data model in Data Warehouses and Business Intelligence systems.

---

# Problem it solves

Imagine storing everything in one large table.

| Revenue Loss | Country | Policy            | Analyst | Date   | Severity |
| ------------ | ------- | ----------------- | ------- | ------ | -------- |
| 1000         | India   | Misrepresentation | John    | 01-Jan | High     |
| 1500         | India   | Misrepresentation | John    | 02-Jan | High     |
| 2000         | USA     | Counterfeit       | Alice   | 03-Jan | Medium   |

Problems:

* Country repeats thousands of times.
* Policy repeats thousands of times.
* Analyst information repeats.
* Storage increases.
* Updating descriptive information becomes difficult.
* Queries become slower as data grows.

A better design is to separate business events from descriptive information.

---

# Definition

A Star Schema is a data warehouse design where one central **Fact Table** is connected directly to multiple **Dimension Tables**.

The Fact Table stores measurable business events, while Dimension Tables store descriptive information used for analysis.

The schema resembles a star, which is where its name comes from.

---

# Components of a Star Schema

## Fact Table

The Fact Table stores business events.

Each row represents one event.

It contains:

* Foreign Keys pointing to Dimension Tables.
* Business metrics.

Example:

### Fact_Violations

| violation_id | country_id | policy_id | analyst_id | date_id  | severity_id | revenue_loss | investigation_time |
| ------------ | ---------- | --------- | ---------- | -------- | ----------- | ------------ | ------------------ |
| V101         | 1          | 101       | 501        | 20260101 | 1           | 1000         | 12                 |

Notice:

* IDs connect to Dimensions.
* Metrics describe the event.

---

## Dimension Tables

Dimension Tables provide descriptive information about the event.

### Country_Dim

| country_id | country_name |
| ---------- | ------------ |
| 1          | India        |
| 2          | USA          |

---

### Policy_Dim

| policy_id | policy_name       |
| --------- | ----------------- |
| 101       | Misrepresentation |
| 102       | Counterfeit       |

---

### Analyst_Dim

| analyst_id | analyst_name |
| ---------- | ------------ |
| 501        | John         |
| 502        | Alice        |

---

### Date_Dim

| date_id  | day | month   | year |
| -------- | --- | ------- | ---- |
| 20260101 | 1   | January | 2026 |

---

### Severity_Dim

| severity_id | severity |
| ----------- | -------- |
| 1           | High     |
| 2           | Medium   |

---

# Why is it called a Star Schema?

The Fact Table sits at the center.

Every Dimension Table connects directly to it.

```text
                Country_Dim
                     │
                     │
Policy_Dim ─── Fact_Violations ─── Analyst_Dim
                     │
                     │
                 Date_Dim
                     │
                     │
               Severity_Dim
```

The structure visually resembles a star.

---

# Mental Model

Think of a Fact Table as the answer to:

> **What happened?**

Think of Dimension Tables as the answer to:

* Who?
* What?
* Where?
* When?
* Which?

---
# Another Business Example (E-commerce)

Business Question:

> Show Revenue by Product, Customer, Date, and Region.

### Business Event

Sale

### Fact Table

Fact_Sales

Metrics:

* Revenue
* Quantity Sold
* Discount

### Dimension Tables

* Product
* Customer
* Date
* Region

---

# How to Design a Star Schema

## Step 1

Identify the business event.

Examples:

* Sale
* Click
* Search
* Policy Violation
* Payment

↓

Fact Table

---

## Step 2

Identify the metrics.

Examples:

* Revenue
* Revenue Loss
* Click Count
* Investigation Time
* Search Latency

↓

Fact Columns

---

## Step 3

Identify descriptive information.

Examples:

* Customer
* Country
* Product
* Policy
* Analyst
* Date
* Device

↓

Dimension Tables

---

# Star Schema Workflow

```text
Business Question
        │
        ▼
Business Event
        │
        ▼
Fact Table
        │
        ▼
Metrics
        │
        ▼
Dimension Tables
        │
        ▼
Dashboard / Reports
```

---

# Advantages

* Fast analytical queries.
* Simple SQL JOINs.
* Easy dashboard creation.
* Easy aggregation.
* Scalable for large datasets.
* Widely used in BI tools.

---

# Disadvantages

* Some descriptive information is intentionally duplicated inside Dimension Tables.
* Requires additional storage compared to highly normalized OLTP databases.
* Not suitable for transactional systems.

---

# Star Schema vs OLTP Design

| OLTP Database                     | Star Schema                      |
| --------------------------------- | -------------------------------- |
| Highly normalized                 | Lightly denormalized             |
| Optimized for inserts and updates | Optimized for analytical queries |
| Many JOINs                        | Fewer JOINs                      |
| Used by applications              | Used by dashboards and reporting |

---

# Interview Explanation

A Star Schema is a data warehouse design that places one Fact Table at the center and connects it directly to multiple Dimension Tables.

The Fact Table stores business events and metrics, while Dimension Tables provide descriptive information for analysis.

This design simplifies analytical queries and improves reporting performance.

---

# Interview Q&A ⭐

## Q1. What is a Star Schema?

### Here's How I'd Answer

A Star Schema is a data warehouse model consisting of one central Fact Table connected directly to multiple Dimension Tables.

It is designed for fast analytical queries and reporting.

---

## Q2. Why is it called a Star Schema?

### Here's How I'd Answer

The Fact Table sits at the center with Dimension Tables surrounding it, forming a star-like structure.

---

## Q3. What is stored in a Fact Table?

### Here's How I'd Answer

A Fact Table stores business events along with measurable metrics and foreign keys that reference Dimension Tables.

For example, a Fact_Violations table may store Revenue Loss, Investigation Time, and foreign keys to Country, Policy, Analyst, Date, and Severity.

---

## Q4. What is stored in Dimension Tables?

### Here's How I'd Answer

Dimension Tables store descriptive information such as Customer, Country, Product, Policy, Date, Analyst, or Device.

They provide context for analyzing business metrics.

---

## Q5. Why is Star Schema used in Data Warehouses?

### Here's How I'd Answer

Star Schema simplifies analytical queries by reducing the number of joins required.

It improves dashboard performance and makes reporting easier for business users.

---

## Q6. Why is Revenue stored in the Fact Table while Country is stored in a Dimension Table?

### Here's How I'd Answer

Revenue is a measurable business metric, so it belongs in the Fact Table.

Country provides descriptive context for analyzing that metric, so it belongs in a Dimension Table.

---

## Q7. What is the first step when designing a Star Schema?

### Here's How I'd Answer

The first step is identifying the business event because the Fact Table represents business events, not just metrics.

Once the event is identified, metrics become Fact columns and descriptive attributes become Dimension Tables.

---

# Common Mistakes

❌ Thinking the Fact Table stores only metrics.

✅ The Fact Table stores business events, metrics, and foreign keys.

---

❌ Naming the Fact Table after a metric.

✅ Name the Fact Table after the business event.

Examples:

* Fact_Sales
* Fact_Orders
* Fact_Searches
* Fact_Violations

---

❌ Treating metrics as Dimensions.

✅ Metrics are measurable values.

Dimensions provide descriptive context.

---

❌ Normalizing every Dimension Table.

✅ Star Schema intentionally keeps Dimension Tables slightly denormalized to improve query performance.

---

# Key Takeaways

* A Star Schema has one central Fact Table.
* Fact Tables store business events.
* Metrics are columns inside Fact Tables.
* Dimension Tables describe business events.
* Every Dimension connects directly to the Fact Table.
* Star Schema is optimized for analytical reporting.

---

# Revision Notes

## Practical Decision Flow

Whenever designing a Star Schema, ask yourself:

1. What business event happened?
2. What metrics describe that event?
3. What descriptive information explains the event?
4. Which attributes should become Dimension Tables?

---

## Quick Interview Revision

| Concept         | One-Line Summary                                                |
| --------------- | --------------------------------------------------------------- |
| Fact Table      | Stores business events and metrics.                             |
| Dimension Table | Stores descriptive information.                                 |
| Star Schema     | One Fact Table connected directly to multiple Dimension Tables. |

### Memory Trick

* **Business Event** → Fact Table
* **Metric** → Fact Column
* **Description** → Dimension Table
* **Everything connects to the Fact Table**

---

## One-Line Summary

> **A Star Schema organizes analytical data by placing business events in a central Fact Table and connecting them directly to Dimension Tables for fast and efficient reporting.**
