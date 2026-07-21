# SQL Interview Handbook

> A complete SQL interview revision guide focused on pattern recognition rather than memorizing solutions.

---

# Why does this exist?

The goal of this document is to help identify SQL interview patterns quickly and solve problems confidently in technical interviews.

Instead of memorizing 100 different queries, learn the 15–20 reusable patterns that solve most interview questions.

---

# Mental Framework

Before writing any SQL query, ask yourself:

1. What is the output?
2. Am I returning rows or groups?
3. Do I need a JOIN?
4. Do I need a Window Function?
5. Do I need Aggregation?
6. Should I use WHERE or HAVING?
7. Do I need Ranking?
8. Am I finding the latest/earliest record?
9. Do I need DISTINCT?
10. Can I validate my answer with sample data?

---

# SQL Execution Order

SQL does NOT execute from top to bottom.

```
FROM
↓
WHERE
↓
GROUP BY
↓
HAVING
↓
SELECT
↓
DISTINCT
↓
ORDER BY
↓
LIMIT
```

## Interview Answer

> Whenever I get confused between WHERE and HAVING, I remember SQL execution order. WHERE filters rows before grouping, whereas HAVING filters groups after aggregation.

---

# Pattern 1 — Latest Record Per Group

## Recognize this pattern

Questions like:

- Latest order
- Most recent login
- Newest transaction
- Current salary
- Latest status

## Solution

```sql
ROW_NUMBER() OVER (
PARTITION BY key
ORDER BY date DESC
)
```

Then

```sql
WHERE rn = 1
```

---

# Pattern 2 — Top N Per Group

Recognize

- Top 3 salaries
- Top 5 products
- Highest revenue per region

Pattern

```sql
DENSE_RANK() OVER (
PARTITION BY group
ORDER BY metric DESC
)
```

Filter

```sql
WHERE rank <= N
```

---

# Pattern 3 — Department Average

Recognize

- Above department average
- Below team average

Pattern

```sql
AVG(salary)
OVER(PARTITION BY department)
```

### Interview Takeaway

Never write

```sql
AVG(...)
OVER(
PARTITION BY department
ORDER BY salary
)
```

unless the question asks for a **running average**.

Adding ORDER BY changes the meaning.

---

# Pattern 4 — Running Total

Recognize

- Running revenue
- Cumulative sales
- Running balance

Pattern

```sql
SUM(amount)
OVER(
ORDER BY date
)
```

---

# Pattern 5 — Consecutive Dates (Gaps & Islands)

Recognize

- Consecutive logins
- Consecutive purchases
- Consecutive attendance

Pattern

```sql
ROW_NUMBER()
```

then

```
date - row_number()
```

Group on the result.

---

# Pattern 6 — Customers Who Bought Every Product

Pattern

```sql
GROUP BY customer_id

HAVING COUNT(DISTINCT product_id)=
(
SELECT COUNT(*)
FROM products
)
```

Interview name

**Relational Division**

---

# Pattern 7 — Customers With No Orders

Pattern

```sql
LEFT JOIN

WHERE right_table.id IS NULL
```

---

# Pattern 8 — Self Join

Recognize

Employee ↔ Manager

Employee ↔ Mentor

Friend ↔ Friend

Pattern

```sql
employees e

JOIN employees m

ON e.manager_id =
m.employee_id
```

---

# Pattern 9 — Conditional Aggregation

Pattern

```sql
SUM(
CASE
WHEN condition
THEN value
ELSE 0
END
)
```

Used for

- Monthly revenue
- Pivot tables
- Category totals

---

# Pattern 10 — More Than N Records

Pattern

```sql
GROUP BY customer_id

HAVING COUNT(*) > N
```

---

# Ranking Functions

## ROW_NUMBER()

Every row gets a unique number.

```
100
100
90
```

↓

```
1
2
3
```

---

## RANK()

Ties share rank.

```
100
100
90
```

↓

```
1
1
3
```

---

## DENSE_RANK()

Ties share rank.

No gaps.

```
100
100
90
```

↓

```
1
1
2
```

---

# WHERE vs HAVING

WHERE

- Before GROUP BY
- Filters rows

HAVING

- After GROUP BY
- Filters groups

## Rule

If you see

- COUNT()
- AVG()
- SUM()
- MAX()
- MIN()

it usually belongs inside HAVING.

---

# Window Functions Cheat Sheet

| Function | Use |
|----------|-----|
| ROW_NUMBER() | Latest row |
| RANK() | Competition ranking |
| DENSE_RANK() | Top N |
| LAG() | Previous row |
| LEAD() | Next row |
| FIRST_VALUE() | First row |
| LAST_VALUE() | Last row |
| AVG() OVER() | Partition average |
| SUM() OVER() | Running total |

---

# Common Interview Mistakes

❌ Using WHERE with COUNT()

❌ Forgetting DESC for latest row

❌ Partitioning by the ranked column

❌ Adding ORDER BY inside AVG()

❌ Wrong self join direction

❌ INNER JOIN instead of LEFT JOIN

❌ Forgetting IS NULL

---

# SQL Pattern Recognition

| Question | Pattern |
|-----------|---------|
| Latest record | ROW_NUMBER() |
| Top N | DENSE_RANK() |
| Department average | AVG() OVER() |
| Running total | SUM() OVER() |
| Previous row | LAG() |
| Next row | LEAD() |
| Consecutive dates | Gaps & Islands |
| No matching rows | LEFT JOIN |
| Employee hierarchy | Self Join |
| More than N | GROUP BY + HAVING |

---

# My Personal Mistakes During Practice

- Used WHERE instead of HAVING.
- Forgot DESC while finding the latest record.
- Added ORDER BY inside AVG() OVER().
- Partitioned by the ranked column.
- Reversed the self join.
- Forgot IS NULL after LEFT JOIN.

---

# Interview Checklist

Before submitting the query:

☐ Correct JOIN?

☐ Correct GROUP BY?

☐ WHERE or HAVING?

☐ ASC or DESC?

☐ Window function needed?

☐ Partition correct?

☐ Ranking correct?

☐ Aggregate correct?

☐ NULL cases handled?

☐ Mentally tested with sample data?

---

# Here's how I'd answer

> I first identify whether the problem is asking for ranking, aggregation, filtering, or row-level calculations. Then I choose the appropriate SQL pattern rather than trying to invent the query from scratch. Finally, I validate the logic against a small sample dataset to ensure it handles edge cases correctly.

---

# Final Advice

Don't memorize 100 SQL solutions.

Memorize **20 reusable patterns**.

Those patterns solve nearly every SQL interview question asked at Google, Amazon, Microsoft, Meta, Uber, Airbnb, Atlassian, and most product companies.
