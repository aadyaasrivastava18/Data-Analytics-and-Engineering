# Snowflake Schema

## Why does this exist?

As businesses grow, Dimension Tables also become larger. These Dimension Tables often contain repeated descriptive information such as Continent, Region, Department, Category, or Manufacturer.

Snowflake Schema exists to further normalize Dimension Tables, reducing redundancy and improving maintainability while preserving the analytical capabilities of a Data Warehouse.

It is an extension of the Star Schema.

---

# Problem it solves

Consider the following Country Dimension.

## Country_Dim

| country_id | country_name | continent |
| ---------- | ------------ | --------- |
| 1          | India        | Asia      |
| 2          | China        | Asia      |
| 3          | Japan        | Asia      |
| 4          | Germany      | Europe    |
| 5          | France       | Europe    |
| 6          | Italy        | Europe    |

Notice that:

* Asia is repeated three times.
* Europe is repeated three times.
* If a continent name changes, every row must be updated.
* Storage increases as more countries are added.

Although this repetition is acceptable in a Star Schema for faster queries, some organizations prefer to eliminate this redundancy.

---

# Definition

A Snowflake Schema is a data warehouse design where one or more Dimension Tables are further normalized into multiple related tables.

Unlike a Star Schema, where every Dimension connects directly to the Fact Table, a Snowflake Schema allows Dimensions to connect to other Dimensions.

The Fact Table remains unchanged.

---

# How Snowflake Schema is Created

Start with a Star Schema.

## Star Schema

### Fact_Violations

| violation_id | country_id | policy_id | revenue_loss |
| ------------ | ---------- | --------- | ------------ |

↓

### Country_Dim

| country_id | country_name | continent |
| ---------- | ------------ | --------- |
| 1          | India        | Asia      |
| 2          | China        | Asia      |
| 3          | Japan        | Asia      |
| 4          | Germany      | Europe    |

---

Instead of repeating continent names, normalize the Dimension.

### Country_Dim

| country_id | country_name | continent_id |
| ---------- | ------------ | ------------ |
| 1          | India        | 1            |
| 2          | China        | 1            |
| 3          | Japan        | 1            |
| 4          | Germany      | 2            |

↓

### Continent_Dim

| continent_id | continent_name |
| ------------ | -------------- |
| 1            | Asia           |
| 2            | Europe         |

The repeated continent values now exist only once.

---

# Another Example

## Star Schema

### Product_Dim

| product_id | product_name | category  | department  |
| ---------- | ------------ | --------- | ----------- |
| 101        | iPhone       | Mobile    | Electronics |
| 102        | Galaxy       | Mobile    | Electronics |
| 103        | MacBook      | Laptop    | Electronics |
| 104        | Dining Table | Furniture | Home        |

Notice:

* Electronics repeats.
* Mobile repeats.
* Laptop repeats.

---

## Snowflake Schema

### Product_Dim

| product_id | product_name | category_id |
| ---------- | ------------ | ----------- |
| 101        | iPhone       | 1           |
| 102        | Galaxy       | 1           |
| 103        | MacBook      | 2           |
| 104        | Dining Table | 3           |

↓

### Category_Dim

| category_id | category_name | department_id |
| ----------- | ------------- | ------------- |
| 1           | Mobile        | 1             |
| 2           | Laptop        | 1             |
| 3           | Furniture     | 2             |

↓

### Department_Dim

| department_id | department_name |
| ------------- | --------------- |
| 1             | Electronics     |
| 2             | Home            |

This removes repeated Category and Department values.

---
Some Dimension Tables are normalized into additional Dimension Tables.

---

# Star Schema vs Snowflake Schema

| Feature           | Star Schema          | Snowflake Schema                      |
| ----------------- | -------------------- | ------------------------------------- |
| Dimension Tables  | Denormalized         | Normalized                            |
| Number of JOINs   | Fewer                | More                                  |
| Query Performance | Faster               | Slightly Slower                       |
| Storage Usage     | Higher               | Lower                                 |
| Redundancy        | More                 | Less                                  |
| Maintenance       | Easier for reporting | Easier for reference data consistency |
| Complexity        | Simpler              | More Complex                          |

---

# Mental Model

Think of Star Schema as:

> **Optimize for reporting performance.**

Think of Snowflake Schema as:

> **Optimize Dimension Table quality and reduce redundancy.**

---

# Business Example

Suppose a VP says:

> "Our Country Dimension has become extremely large and the same Continent, Region, and Currency values are repeated millions of times."

Instead of storing:

* Country
* Region
* Continent
* Currency

inside one Dimension Table,

Snowflake Schema splits them into:

* Country_Dim
* Region_Dim
* Continent_Dim
* Currency_Dim

This reduces redundancy and centralizes reference data.

---

# Advantages

* Reduces redundancy in Dimension Tables.
* Improves maintainability.
* Easier to update reference data.
* Better data consistency.
* Smaller Dimension Tables.
* Well suited for complex enterprise data models.

---

# Disadvantages

* Requires more SQL JOINs.
* Analytical queries become slower than Star Schema.
* More complex database design.
* Harder for beginners to understand.

---

# When Should You Use Snowflake Schema?

Use Snowflake Schema when:

* Dimension Tables contain significant repeated information.
* Storage optimization is important.
* Reference data changes frequently.
* Maintaining consistency is more important than query speed.
* Enterprise-scale data models require normalized reference data.

---

# Interview Explanation

Snowflake Schema is an extension of Star Schema where Dimension Tables are further normalized.

This reduces redundancy and improves maintainability, but increases the number of joins required for analytical queries.

The Fact Table remains unchanged.

---

# Interview Q&A ⭐

## Q1. What is a Snowflake Schema?

### Here's How I'd Answer

A Snowflake Schema is a data warehouse model where Dimension Tables are further normalized into multiple related tables. It reduces redundancy while improving maintainability, although it requires additional joins during analysis.

---

## Q2. How is Snowflake Schema different from Star Schema?

### Here's How I'd Answer

In a Star Schema, every Dimension Table connects directly to the Fact Table and remains denormalized.

In a Snowflake Schema, Dimension Tables are normalized into additional Dimension Tables, reducing redundancy but increasing the number of joins.

---

## Q3. Why would a company choose Snowflake Schema?

### Here's How I'd Answer

A company may choose Snowflake Schema when Dimension Tables contain significant repeated information. Normalizing these tables reduces storage, improves consistency, and simplifies maintenance of reference data.

---

## Q4. Does the Fact Table change in Snowflake Schema?

### Here's How I'd Answer

No. The Fact Table remains the same. Only the Dimension Tables are normalized into additional related tables.

---

## Q5. What is the biggest advantage of Snowflake Schema?

### Here's How I'd Answer

Its biggest advantage is reducing redundancy in Dimension Tables while improving maintainability and consistency of reference data.

---

## Q6. What is the biggest disadvantage of Snowflake Schema?

### Here's How I'd Answer

Because Dimension Tables are normalized, analytical queries require more joins, which can reduce query performance compared to a Star Schema.

---

## Q7. A VP says dashboards are slow because of too many joins. Should we convert to Star Schema?

### Here's How I'd Answer

I would first evaluate the business requirements rather than immediately changing the architecture.

If dashboard query performance is the highest priority and the additional storage is acceptable, a Star Schema may be more appropriate because it reduces joins.

If maintaining consistent reference data and reducing redundancy are more important, I would continue using Snowflake Schema.

The decision should balance performance, maintenance effort, storage, and business priorities.

---

# Common Mistakes

❌ Thinking Snowflake Schema changes the Fact Table.

✅ Only Dimension Tables are normalized.

---

❌ Assuming Snowflake Schema is always better.

✅ It depends on business priorities and performance requirements.

---

❌ Believing normalization always improves performance.

✅ Normalization improves maintainability but often increases joins, which can reduce analytical query performance.

---

# Key Takeaways

* Snowflake Schema is a normalized version of a Star Schema.
* Only Dimension Tables are normalized.
* Fact Tables remain unchanged.
* Reduces redundancy in Dimension Tables.
* Improves maintainability and consistency.
* Requires more joins than Star Schema.
* Best suited for enterprise environments where reference data management is important.

---

# Revision Notes

## Practical Decision Flow

When designing a warehouse, ask yourself:

1. Is the repeated information inside a Dimension Table?
2. Does that information naturally belong to another business entity?
3. Is reducing redundancy more important than minimizing joins?
4. If yes, normalize the Dimension Table into additional Dimensions.

---

## Quick Interview Revision

| Concept          | One-Line Summary                                  |
| ---------------- | ------------------------------------------------- |
| Star Schema      | Denormalized Dimensions for faster reporting.     |
| Snowflake Schema | Normalized Dimensions for better maintainability. |
| Fact Table       | Remains unchanged in both schemas.                |

### Memory Trick

* **Star Schema** → Fewer JOINs, Faster Queries
* **Snowflake Schema** → More JOINs, Less Redundancy

---

## One-Line Summary

> **A Snowflake Schema extends a Star Schema by normalizing Dimension Tables into additional related tables, reducing redundancy and improving maintainability while requiring more joins for analytical queries.**
