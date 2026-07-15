# Database Normalization

## Why does this exist?

As databases grow, the same information often gets stored multiple times across different rows. This leads to data redundancy, inconsistent updates, increased storage requirements, and higher maintenance effort.

Normalization was introduced to organize data efficiently by ensuring that every piece of information is stored exactly once, where it logically belongs.

---

## Problem it solves

Without normalization:

* Data redundancy increases.
* Updating data becomes difficult.
* Different rows may contain conflicting information.
* Storage requirements increase unnecessarily.
* Queries become more complex and harder to maintain.

### Example

| Student ID | Student | Class | Teacher    | Teacher Phone |
| ---------- | ------- | ----- | ---------- | ------------- |
| 101        | Aradhya | 10    | Mr. Sharma | 9999999999    |
| 102        | Rahul   | 10    | Mr. Sharma | 9999999999    |
| 103        | Priya   | 10    | Mr. Sharma | 9999999999    |

If Mr. Sharma changes his phone number, every row must be updated.

Missing even one row results in inconsistent data.

---

## Definition

Normalization is a database design technique used to reduce data redundancy and improve data consistency by organizing data into logically related tables.

The objective is to ensure that every piece of information is stored exactly once and referenced wherever required.

---

## 1NF (First Normal Form)

### Business Problem

A single column contains multiple values.

| Student | Subjects               |
| ------- | ---------------------- |
| Aradhya | Math, Science, English |

Business questions become difficult:

* Find all students studying Math.
* Count students studying Science.
* Add a new subject.
* Remove one subject.

### Solution

Store only one value per cell.

| Student | Subject |
| ------- | ------- |
| Aradhya | Math    |
| Aradhya | Science |
| Aradhya | English |

### Why it matters

* Easier filtering.
* Easier aggregation.
* Simpler SQL queries.
* Better scalability.

---

## 2NF (Second Normal Form)

### Business Problem

Some information depends only on part of the record, causing repeated data.

| Student | Subject | Teacher    |
| ------- | ------- | ---------- |
| 101     | Math    | Mr. Sharma |
| 102     | Math    | Mr. Sharma |
| 103     | Math    | Mr. Sharma |

### Observation

Teacher depends on **Subject**, not **Student**.

### Solution

Move Teacher information into a separate Subject table.

#### Student-Subject Table

| Student | Subject |
| ------- | ------- |

#### Subject Table

| Subject | Teacher    |
| ------- | ---------- |
| Math    | Mr. Sharma |

### Why it matters

If the Math teacher changes, only one row needs updating instead of hundreds.

---

## 3NF (Third Normal Form)

### Business Problem

One descriptive attribute depends on another descriptive attribute.

| Student | Department       | HOD        |
| ------- | ---------------- | ---------- |
| Aradhya | Computer Science | Dr. Sharma |
| Rahul   | Computer Science | Dr. Sharma |

### Observation

HOD depends on **Department**, not **Student**.

### Solution

Move Department information into a separate Department table.

#### Student Table

| Student | Department |
| ------- | ---------- |

#### Department Table

| Department       | HOD        |
| ---------------- | ---------- |
| Computer Science | Dr. Sharma |

### Why it matters

If the HOD changes, only one row needs updating instead of thousands.

---

## Comparison: 1NF vs 2NF vs 3NF

| Normal Form                  | Business Problem                                                                   | Observation                                              | Solution                                            | Example                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **1NF (First Normal Form)**  | A single column stores multiple values, making querying and maintenance difficult. | Every cell should contain only one value (Atomic Value). | Store one value per cell by creating separate rows. | Instead of storing `Math, Science, English` in one cell, create three separate rows.                   |
| **2NF (Second Normal Form)** | Some information depends only on part of the record, leading to repeated data.     | Teacher depends on **Subject**, not **Student**.         | Move Teacher into a separate **Subject** table.     | Instead of repeating `Mr. Sharma` for every student studying Math, store it once in the Subject table. |
| **3NF (Third Normal Form)**  | One descriptive attribute depends on another descriptive attribute.                | HOD depends on **Department**, not **Student**.          | Move HOD into a separate **Department** table.      | Instead of repeating the HOD for every student, store it once in the Department table.                 |

---

## Easy Way to Remember

### 1NF

Ask yourself:

> **Does every cell contain exactly one value?**

If **No**, split the values into separate rows.

---

### 2NF

Ask yourself:

> **Does every attribute depend on the entire record?**

If **No**, move that information into its own table.

---

### 3NF

Ask yourself:

> **Does one descriptive column depend on another descriptive column?**

If **Yes**, move it into a separate table.

---

## Mental Model

```text
Messy Table
      ↓
Multiple values in one cell?
      ↓
1NF

Still seeing repeated information?
      ↓
Does it depend on only part of the record?
      ↓
2NF

Still seeing repeated descriptive information?
      ↓
Does one descriptive field depend on another?
      ↓
3NF
```

---

## Real-world Example

Imagine an e-commerce company.

Instead of storing the customer's name, city, and phone number with every order, the company stores customer information once in a **Customer** table and references it using **Customer ID**.

Benefits:

* Easier updates
* Reduced redundancy
* Better consistency
* Improved scalability

---

## Business Example

Suppose every Ads policy violation stores:

* Advertiser Name
* Country
* Policy Name
* Policy Description

These values repeat millions of times.

Instead:

* Advertiser information is stored once in the **Advertiser** table.
* Policy information is stored once in the **Policy** table.
* Each violation stores only the corresponding IDs.

Benefits:

* Less redundancy
* Faster updates
* Better data consistency
* Easier maintenance

---

## Interview Explanation

Normalisation is about solving business problems rather than following database rules.

It helps:

* Reduce redundancy.
* Improve consistency.
* Simplify updates.
* Improve maintainability.
* Build scalable database designs.

---

## Here's How I'd Answer in an Interview 

**Q. Why do we normalize databases?**

Normalization is a database design technique used to reduce data redundancy and improve data consistency.

Instead of storing the same information repeatedly across multiple rows, we store it once and reference it wherever required.

This makes updates easier, reduces storage requirements, prevents inconsistent data, and simplifies long-term maintenance.

For example, instead of storing a teacher's details for every student, we store the teacher once in a separate table and reference it using a Teacher ID.

---

## Common Mistakes

❌ Thinking normalization only reduces storage.

✅ Its primary purpose is to improve consistency, maintainability, and reduce redundancy.

---

❌ Memorizing the definitions of 1NF, 2NF, and 3NF.

✅ Understand the business problem each normal form solves.

---

❌ Designing tables around reports.

✅ Design tables around business entities and their relationships.

---

## Key Takeaways

* Store each piece of information exactly once, where it logically belongs.
* Remove unnecessary duplication.
* Update data in one place.
* Think in terms of dependencies, not definitions.
* Good database design improves both performance and maintainability.

---

## Revision Notes

### Practical Decision Flow

Whenever you see a table, ask yourself:

1. What information is repeating?
2. Why is it repeating?
3. Does this information belong to another business entity?
4. Can I store it only once?
5. If this value changes, how many rows would I need to update?

If the answer is **many rows**, your database can likely be normalized further.

---

### Quick Interview Revision

| Normal Form | One-Line Summary                                                                           |
| ----------- | ------------------------------------------------------------------------------------------ |
| **1NF**     | One value per cell (Atomic values).                                                        |
| **2NF**     | Every non-key attribute should depend on the whole key.                                    |
| **3NF**     | Non-key attributes should not depend on another non-key attribute (transitive dependency). |

### Memory Trick

* **1NF** → Atomic Values
* **2NF** → Whole Key Dependency
* **3NF** → No Transitive Dependency

---

### One-Line Summary

> **Normalization is the process of storing each piece of information exactly once, in the place where it logically belongs.**
