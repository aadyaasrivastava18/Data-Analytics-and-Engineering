# Data Warehouse Table Design

## Why does this exist?

A Data Warehouse is designed to answer business questions quickly and efficiently. To achieve this, data is organized into two specialized table types:

* **Fact Tables** — store measurable business events.
* **Dimension Tables** — store descriptive information about those events.

Understanding how to design both tables is essential for building scalable analytical systems, Star Schemas, and Snowflake Schemas.

---

# Learning Objectives

After completing this chapter, you should be able to:

* Design Fact Tables.
* Design Dimension Tables.
* Define the grain of a Fact Table.
* Decide what belongs in a Fact Table vs a Dimension Table.
* Apply Star Schema design principles.
* Explain design decisions during interviews.

---

# Chapter Structure

```text
Data Warehouse Table Design
│
├── Part 1: Fact Table Design
│
└── Part 2: Dimension Table Design
```

---

# Part 1 — Fact Table Design

## What is a Fact Table?

A Fact Table stores measurable business events.

Each row represents one business event and contains:

* Business Event Identifier
* Foreign Keys
* Business Metrics

Examples of business events:

* Sale
* Order
* Search
* Payment
* Click
* Policy Violation

---

## Components of a Fact Table

### 1. Business Event

Every Fact Table begins with identifying the business event.

Examples:

* Fact_Sales
* Fact_Orders
* Fact_Searches
* Fact_Clicks
* Fact_Violations

---

### 2. Foreign Keys

Foreign Keys connect the Fact Table to Dimension Tables.

Example:

* customer_id
* product_id
* country_id
* policy_id
* analyst_id
* date_id

---

### 3. Metrics

Metrics measure the business event.

Examples:

* Revenue
* Revenue Loss
* Quantity
* Investigation Time
* Click Count
* Search Latency

---

## Example

### Fact_Violations

| violation_id | advertiser_id | policy_id | country_id | analyst_id | date_id | severity_id | revenue_loss | investigation_time |
| ------------ | ------------- | --------- | ---------- | ---------- | ------- | ----------- | ------------ | ------------------ |

---

## Grain

The grain defines what one row represents.

Examples:

* One row = One Sale
* One row = One Order
* One row = One Click
* One row = One Policy Violation

Always define the grain before designing the table.

---

## Design Principles

A good Fact Table should:

* Store one business event per row.
* Store only measurable metrics.
* Store only foreign keys for descriptive information.
* Avoid descriptive text.
* Have a clearly defined grain.

---

## Common Mistakes

❌ Storing descriptive text such as country names.

✅ Store only IDs.

---

❌ Mixing multiple business events.

✅ One Fact Table = One Business Event.

---

❌ Forgetting to define the grain.

✅ Always define the grain first.

---

# Interview Explanation

### Here's How I'd Answer

A Fact Table stores measurable business events.

Each row represents one business event and contains foreign keys to Dimension Tables along with business metrics.

The Fact Table is placed at the center of a Star Schema because all business analysis revolves around business events.

---

# Part 2 — Dimension Table Design

> **This section will be completed in the next lesson.**

Topics that will be covered:

* What is a Dimension Table?
* Characteristics of a Dimension Table.
* Natural Keys vs Surrogate Keys.
* Conformed Dimensions.
* Junk Dimensions.
* Degenerate Dimensions.
* Role-Playing Dimensions.
* Hierarchies.
* Designing robust Dimension Tables.
* Google Trust & Safety examples.
* Common interview questions.

---

# Fact Table vs Dimension Table

| Feature   | Fact Table                              | Dimension Table                  |
| --------- | --------------------------------------- | -------------------------------- |
| Purpose   | Stores business events                  | Stores descriptive information   |
| Data Type | Mostly numeric metrics and foreign keys | Mostly descriptive attributes    |
| Size      | Usually very large                      | Usually much smaller             |
| Updates   | Frequent inserts                        | Less frequent updates            |
| Position  | Center of Star Schema                   | Around the Fact Table            |
| Examples  | Revenue, Sales, Clicks                  | Customer, Country, Product, Date |

---

# Mental Model

```text
Business Event
        │
        ▼
Fact Table
        │
        ▼
Foreign Keys
        │
        ▼
Dimension Tables
        │
        ▼
Business Reports & Dashboards
```

---

# Decision Flow

Whenever designing a Data Warehouse, ask:

1. What business event happened?
2. What metrics describe that event?
3. What descriptive information explains that event?
4. Which attributes become Dimensions?
5. What is the grain of the Fact Table?

---

# Interview Q&A ⭐

## Q1. Why do Data Warehouses use Fact and Dimension Tables?

### Here's How I'd Answer

Fact Tables store measurable business events, while Dimension Tables provide descriptive information about those events.

Separating the two reduces redundancy, improves maintainability, and enables fast analytical queries.

---

## Q2. What should never be stored in a Fact Table?

### Here's How I'd Answer

Descriptive attributes such as country names, customer names, or policy names should not be stored directly in a Fact Table.

Instead, the Fact Table should store foreign keys pointing to Dimension Tables.

---

## Q3. What is the first step when designing a Fact Table?

### Here's How I'd Answer

The first step is identifying the business event and defining the grain.

Once the grain is defined, metrics and Dimension relationships become much easier to identify.

---

# Key Takeaways

* A Data Warehouse consists primarily of Fact Tables and Dimension Tables.
* Fact Tables store business events.
* Dimension Tables describe those events.
* Define the grain before designing a Fact Table.
* Store foreign keys instead of descriptive text.
* Every analytical query starts with a business event.

---

# Revision Notes

## Quick Revision

| Concept         | Summary                             |
| --------------- | ----------------------------------- |
| Fact Table      | Stores business events and metrics. |
| Dimension Table | Stores descriptive attributes.      |
| Grain           | Defines what one row represents.    |
| Foreign Keys    | Connect Fact Tables to Dimensions.  |

---

## One-Line Summary

> **A well-designed Data Warehouse separates measurable business events into Fact Tables and descriptive business context into Dimension Tables, enabling scalable, maintainable, and high-performance analytics.**
