# 🚀 CTE + Ranking Functions (4-Minute Interview Revision)

---

# CTE (Common Table Expression)

### Syntax

```sql
WITH cte_name AS (

    SELECT ...

)

SELECT *
FROM cte_name;
```

### Use When

✅ Breaking complex queries into steps

✅ Reusing intermediate results

✅ Improving readability

---

# Remember

```
Raw Data
   ↓
CTE
   ↓
Final Query
```

---

# Common Mistakes

❌ `{}` instead of `()`

❌ Forgetting final `SELECT`

❌ Using table aliases outside CTE

❌ Filtering before aggregation

---

# ROW_NUMBER()

```sql
ROW_NUMBER() OVER(
PARTITION BY department
ORDER BY salary DESC
)
```

### Properties

✔ Unique numbers

✔ No ties

Example

```
9000 → 1
9000 → 2
8000 → 3
7000 → 4
```

### Use

- Latest order
- First login
- Remove duplicates
- Exactly one top employee

---

# RANK()

```sql
RANK() OVER(
PARTITION BY department
ORDER BY salary DESC
)
```

### Properties

✔ Ties allowed

✔ Gaps exist

Example

```
9000 → 1
9000 → 1
8000 → 3
7000 → 4
```

### Use

Competition ranking

---

# DENSE_RANK()

```sql
DENSE_RANK() OVER(
PARTITION BY department
ORDER BY salary DESC
)
```

### Properties

✔ Ties allowed

✔ No gaps

Example

```
9000 → 1
9000 → 1
8000 → 2
7000 → 3
```

### Use

Nth highest salary

---

# Which One?

| Requirement | Function |
|-------------|----------|
|One row only|ROW_NUMBER()|
|Keep ties + gaps|RANK()|
|Keep ties + no gaps|DENSE_RANK()|

---

# Interview Patterns

### Total Spending

```
JOIN
↓
GROUP BY
↓
CTE
↓
WHERE
```

---

### Above Department Average

```
AVG() OVER()
↓
CTE
↓
Filter
```

---

### Highest Salary

```
ROW_NUMBER()

or

MAX() + Filter
```

---

### Second Highest Salary

```
DENSE_RANK()

↓

WHERE rank = 2
```

---

# Interview Checklist

Before writing SQL ask:

□ Need every row?
→ Window Function

□ Need one row per group?
→ GROUP BY

□ Need intermediate step?
→ CTE

□ Ties matter?
→ RANK / DENSE_RANK

□ Exactly one winner?
→ ROW_NUMBER

---

# SQL Templates

### CTE

```sql
WITH temp AS (

SELECT ...

)

SELECT *
FROM temp;
```

### ROW_NUMBER

```sql
ROW_NUMBER() OVER(
PARTITION BY col
ORDER BY col DESC
)
```

### RANK

```sql
RANK() OVER(
PARTITION BY col
ORDER BY col DESC
)
```

### DENSE_RANK

```sql
DENSE_RANK() OVER(
PARTITION BY col
ORDER BY col DESC
)
```

---

# ⭐ MAANG Interview Questions

1. Top employee per department
2. Second highest salary
3. Above department average
4. Top 3 employees
5. Latest order per customer
6. Remove duplicates
7. Above company average
8. Nth highest salary
9. Highest spending customer
10. Running total (LAG/LEAD next topic)

---

# Remember

**GROUP BY** → Reduces rows

**Window Function** → Keeps rows

**CTE** → Organizes logic
