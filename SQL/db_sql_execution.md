# Learn how databases execute SQL queries, why some queries become slow, and how to think like a database optimizer.

---

# Why does this exist?

Writing a SQL query that returns the correct answer is only half the job.

In real-world applications, databases often contain millions or even billions of rows. A query that works correctly may still be too slow for production.

Understanding query optimization helps us write SQL that is both **correct** and **efficient**.

---

# Learning Objectives

After completing this module, you should be able to:

- Explain how a database executes a SQL query.
- Understand why Full Table Scans are expensive.
- Explain what indexes are and when they are useful.
- Differentiate between Index Seek and Index Scan.
- Understand selectivity.
- Recognize SARGable queries.
- Explain why an index may not be used.
- Read basic `EXPLAIN` output.
- Follow a systematic approach for debugging slow queries.

---

# How Does SQL Execute Internally?

When a SQL query is executed, the database doesn't immediately start reading rows.

Instead, it follows this process:

```
SQL Query
      │
      ▼
Parser
      │
      ▼
Optimizer
      │
      ▼
Execution Plan
      │
      ▼
Storage Engine
      │
      ▼
Results
```

---

## Step 1: Parser

The parser validates the SQL.

It checks:

- SQL syntax
- Table names
- Column names
- User permissions

Example

```sql
SELECT customer_id
FROM orders;
```

Valid.

Example

```sql
SELECT customer
FROM orders;
```

Invalid because the column doesn't exist.

---

## Step 2: Optimizer

The optimizer is the brain of the database.

Its responsibility is to determine the **least expensive** execution strategy.

Example

Plan A

```
Full Table Scan
Cost = 500
```

Plan B

```
Index Seek
Cost = 20
```

The optimizer chooses the plan with the lowest estimated cost.

Important:

> The optimizer does **not** always choose an index.

It chooses the cheapest execution plan.

---

## Step 3: Execution Plan

An execution plan describes **how** the database will execute the SQL query.

It does **not** show the query result.

We view it using:

```sql
EXPLAIN
SELECT *
FROM orders
WHERE customer_id = 105;
```

---

# Full Table Scan

## Definition

A Full Table Scan occurs when the database reads every row in a table.

Example

```sql
SELECT *
FROM orders
WHERE customer_id = 105;
```

Without an index:

```
Row 1
↓

Row 2
↓

Row 3
↓

...

↓

Row 500,000,000
```

---

## Why is it slow?

Because the database must:

- Read every data page.
- Evaluate every row.
- Perform high disk I/O.
- Spend more CPU time.

As table size grows, execution time increases significantly.

---

# What is an Index?

An index is a data structure that allows the database to locate rows efficiently.

Instead of scanning every row, it navigates directly to the required values.

Without an index

```
Read every row
```

With an index

```
Jump directly to matching values
```

---

# Index Seek vs Index Scan

## Index Seek

The database directly navigates to matching values.

Characteristics:

- Reads only the required portion of the index.
- Very fast.
- Preferred execution strategy.

Example

```sql
WHERE customer_id = 105
```

---

## Index Scan

The database reads a significant portion (or all) of the index.

Characteristics:

- Slower than an Index Seek.
- Faster than a Full Table Scan in many cases.

---

# Selectivity

## Definition

Selectivity measures how effectively a condition filters rows.

---

## High Selectivity

Few rows satisfy the condition.

Example

```sql
WHERE email = 'alice@example.com'
```

Excellent candidate for an index.

---

## Low Selectivity

Most rows satisfy the condition.

Example

```sql
WHERE status = 'ACTIVE'
```

If 98% of rows are ACTIVE, the optimizer may ignore the index because scanning the table is cheaper.

---

# Why Might an Index Not Be Used?

An existing index does not guarantee that the optimizer will use it.

Common reasons include:

- Low selectivity.
- The query returns most rows.
- Functions applied to indexed columns.
- Leading wildcard searches (`LIKE '%abc'`).
- Data type mismatch.
- Outdated optimizer statistics.

---

# SARGable Queries

A SARGable predicate allows the optimizer to efficiently use an index.

## Good Examples

```sql
WHERE customer_id = 100
```

```sql
WHERE order_date >= '2026-01-01'
```

```sql
WHERE email LIKE 'john%'
```

---

## Poor Examples

```sql
WHERE YEAR(order_date) = 2026
```

```sql
WHERE UPPER(email) = 'JOHN@ABC.COM'
```

```sql
WHERE email LIKE '%gmail.com'
```

These often prevent efficient index usage.

---

# Why Avoid SELECT *?

Instead of

```sql
SELECT *
```

Prefer

```sql
SELECT customer_id,
       order_date
```

Benefits

- Reads fewer columns.
- Reduces disk I/O.
- Reduces network traffic.
- May enable covering indexes.

---

# Reading an Execution Plan

Example

| table | type | key | rows |
|--------|------|------|------|
| orders | ALL | NULL | 500000000 |

Interpretation

## table

The table being accessed.

```
orders
```

---

## type

How the database accesses the table.

Examples:

```
const
```

Excellent.

```
ALL
```

Full Table Scan.

---

## key

Which index the optimizer decided to use.

```
PRIMARY
```

Index used.

```
NULL
```

No index was used.

---

## rows

Estimated number of rows the optimizer expects to read.

Examples

```
rows = 1
```

Excellent.

```
rows = 500000000
```

Likely expensive.

---

# Access Type Ranking

Best

```
system
```

↓

```
const
```

↓

```
eq_ref
```

↓

```
ref
```

↓

```
range
```

↓

```
index
```

↓

```
ALL
```

Worst

*(We'll study these access types in detail in the next module.)*

---

# How to Investigate a Slow Query

When someone says:

> "This query is slow."

Don't immediately rewrite it.

Instead:

1. Read the execution plan (`EXPLAIN`).
2. Check whether an index exists.
3. Verify whether the optimizer is using the index.
4. Check the access type.
5. Look at the estimated row count.
6. Reduce unnecessary columns.
7. Rewrite the query only after understanding the execution plan.

---

# Common Interview Questions

## Why is a Full Table Scan slow?

Because every row must be read and evaluated, resulting in high disk I/O and CPU usage.

---

## Does an existing index guarantee better performance?

No.

The optimizer chooses the lowest-cost execution plan.

---

## Why might an optimizer ignore an index?

Because using the index may be more expensive than scanning the table.

---

## What is the difference between an Index Seek and an Index Scan?

Index Seek navigates directly to matching values.

Index Scan reads much or all of the index.

---

## Why is `LIKE 'abc%'` generally faster than `LIKE '%abc'`?

The known prefix (`abc`) allows the optimizer to efficiently seek into the index.

A leading wildcard prevents efficient index navigation.

---

# Interview Takeaways

- A correct query is not always an efficient query.
- The optimizer chooses the cheapest execution plan, not necessarily an index.
- Full Table Scans become expensive as data grows.
- High selectivity makes indexes more useful.
- Low selectivity often results in scans.
- `LIKE 'abc%'` is generally index-friendly.
- `LIKE '%abc'` is generally not.
- Avoid wrapping indexed columns in functions.
- Avoid `SELECT *` unless every column is required.
- Read the execution plan before optimizing.

---
## Biggest Mindset Shift

When writing SQL, think like an **Analyst**.

- Understand the business problem.
- Write the correct query.

When optimizing SQL, think like the **Database Optimizer**.

Ask yourself:

- Which execution plan is cheapest?
- Is an index being used?
- How many rows will be read?
- Is this a seek or a scan?
- Can I reduce I/O?

---

# Summary

This module introduced the foundations of SQL query optimization.

I learned:

- How SQL executes internally.
- The role of the parser, optimizer, and execution plan.
- Why Full Table Scans are slow.
- How indexes improve performance.
- The difference between Index Seek and Index Scan.
- The importance of selectivity.
- What makes a query SARGable.
- How to read basic `EXPLAIN` output.
- How to approach slow query debugging systematically.

This knowledge forms the foundation for understanding execution plans, indexing strategies, and advanced database performance tuning.
