# SQL Query Optimisation 

> Learn how the database executes queries, why some queries are slow, and how to think like a query optimiser instead of guessing fixes.

---

# Why does this exist?

Writing a correct SQL query is only the first step.

In production systems with millions or billions of rows, the biggest challenge is writing queries that execute efficiently.

This module introduces the fundamental concepts required to understand query performance and prepares you for SQL optimisation interviews at companies like Google, Meta, Microsoft, Amazon, Uber, and Airbnb.

---

# Problem it solves

Many developers assume that if a query is correct, it is also efficient.

However, a query can:

- Return the correct result
- Still take several minutes to execute
- Consume excessive CPU and memory
- Scan unnecessary data
- Increase cloud costs

Understanding query optimization helps identify these issues before they affect production systems.

---

# Learning Objectives

After completing this module, you should be able to:

- Explain why queries become slow.
- Understand what happens when a query executes.
- Differentiate between table scans and index operations.
- Understand selectivity.
- Identify when indexes are useful.
- Recognize index-friendly (SARGable) queries.
- Apply a structured process for investigating slow queries.

---

# How SQL Executes Internally

When a SQL query is submitted, the database does much more than simply execute it.

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

### Parser

Checks SQL syntax and converts the query into an internal representation.

### Optimizer

The optimizer evaluates multiple execution strategies and selects the one with the lowest estimated cost.

This is why two logically identical queries can have very different performance.

### Execution Plan

The execution plan describes **how** the database intends to retrieve the requested data.

### Storage Engine

Reads the required pages from disk or memory and returns the results.

---

# Full Table Scan

## Definition

A Full Table Scan occurs when the database reads every row in a table to evaluate the filtering condition.

Example:

```sql
SELECT *
FROM orders
WHERE customer_id = 105;
```

If there is no usable index on `customer_id`, the database must inspect every row.

---

## Why is it expensive?

A full table scan requires:

- Reading every data page.
- Evaluating the WHERE condition for every row.
- Large disk I/O.
- Increased CPU usage.
- Longer execution time as the table grows.

For a table containing 500 million rows, this can become extremely expensive.

---

# What is an Index?

## Definition

An index is a data structure that provides an efficient lookup path to rows.

Instead of reading every row, the database navigates directly to matching values.

Without an index:

```
Check Row 1
Check Row 2
Check Row 3
...
Check Row 500,000,000
```

With an index:

```
Jump directly to matching values
```

---

# Index Seek vs Index Scan

## Index Seek

An Index Seek navigates directly to the required values.

Characteristics:

- Reads only a small portion of the index.
- Very efficient.
- Preferred execution method.

Example:

```sql
WHERE customer_id = 105
```

---

## Index Scan

An Index Scan reads a large portion (or all) of the index.

Characteristics:

- Used when the optimizer cannot efficiently seek.
- More expensive than an Index Seek.
- Still often cheaper than a Full Table Scan.

---

# Selectivity

## Definition

Selectivity measures how effectively a condition filters data.

### High Selectivity

Very few rows satisfy the condition.

Example:

```sql
WHERE email = 'alice@example.com'
```

Excellent candidate for an index.

---

### Low Selectivity

Most rows satisfy the condition.

Example:

```sql
WHERE status = 'ACTIVE'
```

If 98% of rows are ACTIVE, using the index may be slower than scanning the table.

---

# Why Doesn't the Database Use an Existing Index?

Many people assume:

> "An index exists, so the database will always use it."

This is incorrect.

The optimizer decides whether using the index is actually cheaper.

Common reasons an index is ignored:

- Low selectivity.
- Query returns most of the table.
- Functions applied to indexed columns.
- Leading wildcard searches.
- Data type mismatch.
- Outdated optimizer statistics.

---

# SARGable Predicates

## Definition

A SARGable predicate allows the optimizer to efficiently use an index.

### Good Examples

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

### Poor Examples

```sql
WHERE YEAR(order_date) = 2026
```

```sql
WHERE UPPER(email) = 'JOHN@ABC.COM'
```

```sql
WHERE email LIKE '%gmail.com'
```

These expressions often prevent efficient index usage.

---

# Why SELECT * Should Be Avoided

Instead of:

```sql
SELECT *
```

Prefer:

```sql
SELECT customer_id,
       order_date
```

Benefits:

- Reads fewer columns.
- Reduces I/O.
- Reduces network transfer.
- May allow covering indexes.
- Improves overall performance.

---

# How to Investigate a Slow Query

When someone says:

> "This query is slow."

Avoid guessing.

Instead, follow this process:

1. Examine the execution plan.
2. Check whether appropriate indexes exist.
3. Verify whether those indexes are actually being used.
4. Avoid unnecessary columns (`SELECT *`).
5. Check partition pruning where applicable.
6. Rewrite the query only after understanding the execution plan.

---

# Common Interview Questions

### Why is a Full Table Scan slow?

Because the database must examine every row, resulting in high disk I/O and CPU usage.

---

### Does an existing index guarantee better performance?

No.

The optimizer chooses the execution plan with the lowest estimated cost.

---

### When are indexes most effective?

Indexes perform best on highly selective columns where only a small percentage of rows match the filtering condition.

---

### What is the difference between an Index Seek and an Index Scan?

Index Seek directly navigates to matching values.

Index Scan reads a significant portion of the index.

---

### Why is `LIKE 'abc%'` faster than `LIKE '%abc'`?

The optimizer knows the starting prefix (`abc`) and can seek into the index.

With `%abc`, the beginning of the string is unknown, so efficient seeking is generally not possible.

---

# Interview Takeaways

- Read the execution plan before changing a query.
- An index existing does not guarantee that it will be used.
- High selectivity favors index usage.
- Low selectivity often leads to scans.
- `LIKE 'abc%'` is generally index-friendly.
- `LIKE '%abc'` is generally not.
- Avoid wrapping indexed columns in functions.
- Avoid `SELECT *` unless every column is required.
- Optimize using evidence, not assumptions.

---

# Here's how I'd answer

**Q: A query on a 500-million-row table is taking 45 seconds. What would you check first?**

> I would begin by examining the execution plan using `EXPLAIN` to understand how the database is executing the query. Then I'd verify whether an appropriate index exists and whether the optimizer is actually using it. Next, I'd check if the query is retrieving unnecessary columns with `SELECT *`, whether the table is partitioned, and whether the predicate is selective enough to benefit from an index. Only after understanding the execution plan would I consider rewriting the query.

---

# Summary

In this module, you learned:

- How SQL queries execute internally.
- Why Full Table Scans are expensive.
- What indexes are and when they help.
- The difference between Index Seek and Index Scan.
- The concept of selectivity.
- Why indexes are sometimes ignored.
- What makes a predicate SARGable.
- A systematic approach to debugging slow SQL queries.

This module forms the foundation for understanding execution plans, indexing strategies, and advanced SQL optimization.

---

# Reading Execution Plans (`EXPLAIN`)

`EXPLAIN` shows **how** the optimizer plans to execute a query.

Example:

```sql
EXPLAIN
SELECT *
FROM employees
WHERE employee_id = 100;
```

## Important Columns

| Column  | Meaning                         |
| ------- | ------------------------------- |
| `table` | Table being accessed            |
| `type`  | Access method used              |
| `key`   | Index selected                  |
| `rows`  | Estimated rows examined         |
| `Extra` | Additional operations performed |

Always inspect the execution plan before attempting to optimize a query.

---

# Access Types

The `type` column in `EXPLAIN` indicates how efficiently the database accesses data.

Best → Worst

```text
system → const → eq_ref → ref → range → index → ALL
```

| Type     | Description                              |
| -------- | ---------------------------------------- |
| `const`  | Primary Key / UNIQUE lookup              |
| `eq_ref` | Join using a Primary or Unique Key       |
| `ref`    | Equality lookup using a non-unique index |
| `range`  | Reads a range of index values            |
| `index`  | Scans the entire index                   |
| `ALL`    | Full Table Scan                          |

> **Note:** The optimizer chooses the access type with the lowest estimated cost, not necessarily the highest-ranked one.

---

# Composite Indexes

A composite index stores multiple columns together.

Example:

```sql
INDEX(country, city, department)
```

The data is logically ordered as:

```text
Country
    ↓
City
    ↓
Department
```

## Leftmost Prefix Rule

For:

```sql
INDEX(A, B, C)
```

Efficient:

```sql
WHERE A = ...

WHERE A = ...
AND B = ...

WHERE A = ...
AND B = ...
AND C = ...
```

Partial Usage:

```sql
WHERE A = ...
AND C = ...
```

Only column **A** is efficiently used.

Not Efficient:

```sql
WHERE B = ...

WHERE C = ...
```

---

# Covering Index

A covering index contains every column required to execute a query.

This includes columns used in:

* `SELECT`
* `WHERE`
* `ORDER BY`
* `GROUP BY`

Example:

```sql
INDEX(first_name, salary)

SELECT salary
FROM employees
WHERE first_name = 'John';
```

Since both required columns exist in the index, the database can answer the query without reading the table.

> **Rule:** A covering index avoids table lookups.

---

# Join Optimization

The optimizer chooses different join algorithms depending on table size, indexes, and estimated cost.

| Situation                               | Preferred Join         |
| --------------------------------------- | ---------------------- |
| Small outer table + indexed inner table | Index Nested Loop Join |
| No useful index                         | Hash Join              |
| Both inputs already sorted              | Merge Join             |

Remember:

> The optimizer selects the join algorithm with the lowest estimated cost.

---

# ORDER BY Optimization

If an index already stores rows in the required order, the optimizer can avoid sorting.

Example:

```sql
INDEX(salary)

SELECT salary
FROM employees
ORDER BY salary;
```

The optimizer can read the index directly.

However,

```sql
SELECT *
FROM employees
ORDER BY salary;
```

may still require sorting because additional table lookups could be more expensive than scanning and sorting.

---

## Using filesort

`EXPLAIN` may show:

```text
Using filesort
```

This means the optimizer performed an explicit sort because it could not satisfy the requested ordering using an index.

> `Using filesort` does **not** necessarily mean sorting on disk.

---

# GROUP BY Optimization

Queries using `GROUP BY`, `DISTINCT`, or complex aggregations may require an intermediate structure during execution.

`EXPLAIN` may show:

```text
Using temporary
```

This indicates that the optimizer created a temporary structure while processing the query.

Indexes can often reduce or eliminate the need for temporary structures when grouping or ordering matches the index order.

---

# Additional Interview Takeaways

* The optimizer chooses the **lowest estimated cost**, not simply an available index.
* `rows` in `EXPLAIN` is an estimate, not an exact count.
* `key = NULL` means no index was chosen for the execution plan.
* Composite indexes follow the **Leftmost Prefix Rule**.
* A covering index avoids reading the base table.
* `Using filesort` indicates an explicit sort operation.
* `Using temporary` indicates an intermediate structure was created during execution.
* Always explain optimization decisions using the optimizer's estimated cost rather than assuming an index will always be used.







