# Primary Keys & Foreign Keys

## Why does this exist?

As databases grow, information is divided into multiple tables to reduce redundancy and improve maintainability. Once data is split, there must be a reliable way to uniquely identify records and connect related tables.

Primary Keys and Foreign Keys solve this problem by providing identity and relationships between tables.

---

## Problem it solves

Imagine storing customer information in every order.

| Order ID | Customer Name | Customer City | Product |
|----------|---------------|---------------|----------|
|1|Aradhya|Delhi|Laptop|
|2|Aradhya|Delhi|Mouse|
|3|Aradhya|Delhi|Keyboard|

Problems:

- Customer information is repeated.
- Changing customer details requires updating multiple rows.
- Inconsistent data may occur if some rows are missed.
- Tables become unnecessarily large.

Instead, we separate customer information.

### Customer Table

| customer_id | customer_name | city |
|-------------|---------------|------|
|101|Aradhya|Delhi|

### Orders Table

| order_id | customer_id | product |
|----------|-------------|----------|
|1|101|Laptop|
|2|101|Mouse|
|3|101|Keyboard|

Now customer information is stored once and referenced using `customer_id`.

---

## Definition

### Primary Key

A Primary Key is a column (or combination of columns) that uniquely identifies every record in a table.

Each table should have one Primary Key.

---

### Foreign Key

A Foreign Key is a column in one table that references the Primary Key of another table.

It creates relationships between tables and maintains data integrity.

---

## Primary Key

### Business Problem

Suppose two students have the same name.

| Roll No | Student Name |
|----------|--------------|
|101|Rahul|
|102|Rahul|

If a teacher asks:

> "Show me Rahul's marks."

Which Rahul?

Names cannot uniquely identify a student.

---

### Solution

Assign every student a unique Roll Number (Student ID).

| student_id | student_name |
|------------|--------------|
|101|Rahul|
|102|Rahul|

Now every student has a unique identity.

---

### Why it matters

A Primary Key:

- Uniquely identifies each record.
- Prevents duplicate identities.
- Makes updates and deletions accurate.
- Allows other tables to reference the record.

---

## Characteristics of a Good Primary Key

A good Primary Key should be:

- **Unique** – Every row must have a different value.
- **Not NULL** – Every record must have an identifier.
- **Stable** – The value should not change frequently.

---

## Examples of Good and Bad Primary Keys

| Candidate | Good Primary Key? | Reason |
|------------|------------------|--------|
| Student Name | ❌ No | Multiple students can have the same name. |
| Email Address | ❌ No | Can change over time. |
| Mobile Number | ❌ No | Can change or be reassigned. |
| Employee ID | ✅ Yes | Unique, stable, and organization-controlled. |
| Aadhaar Number | ✅ Yes | Unique and stable. |
| Passport Number | ✅ Yes | Unique and generally stable during its validity. |
| Customer ID | ✅ Yes | System-generated and stable. |

---

## Foreign Key

### Business Problem

Suppose every order stores the customer's name.

If the customer changes their name, every order record must be updated.

This creates:

- Data redundancy.
- Maintenance overhead.
- Inconsistent data.

---

### Solution

Store only the `customer_id` in the Orders table.

#### Customer Table

| customer_id | customer_name |
|-------------|---------------|
|101|Aradhya|

#### Orders Table

| order_id | customer_id |
|----------|-------------|
|1|101|
|2|101|
|3|101|

---

### Why it matters

A Foreign Key:

- Connects related tables.
- Eliminates redundant information.
- Maintains data consistency.
- Supports database normalization.

---

## Referential Integrity

A Foreign Key must always reference an existing Primary Key.

### Valid Example

#### Customers

| customer_id |
|-------------|
|101|
|102|

#### Orders

| order_id | customer_id |
|----------|-------------|
|1|101|

Valid because Customer **101** exists.

---

### Invalid Example

#### Orders

| order_id | customer_id |
|----------|-------------|
|2|105|

Invalid because Customer **105** does not exist.

This prevents orphan records and protects data quality.

---

## Primary Key vs Foreign Key

| Primary Key | Foreign Key |
|--------------|-------------|
| Uniquely identifies a record. | References a Primary Key in another table. |
| Must be unique. | Values can repeat. |
| Cannot be NULL. | May be NULL depending on business rules. |
| One per table. | Multiple Foreign Keys can exist in a table. |
| Represents identity. | Represents relationships. |

---

## Mental Model

```text
Customer
--------------------
customer_id (PK)
customer_name
city

          ▲
          │
          │
Orders
--------------------
order_id
customer_id (FK)
product
```

**Primary Key → Identifies**

**Foreign Key → Connects**

---

## Real-world Example

Imagine Amazon.

Instead of storing customer details with every order:

- Customer information is stored once.
- Every order stores only the `customer_id`.

This reduces redundancy and keeps customer information consistent.

---

## Business Example

### Advertiser Table

| advertiser_id | advertiser_name | country |
|---------------|-----------------|----------|
|1001|Nike|USA|

### Campaign Table

| campaign_id | advertiser_id |
|-------------|---------------|
|C101|1001|

Instead of storing:

- Advertiser Name
- Country

inside every campaign, Google stores only the `advertiser_id`.

Whenever advertiser details are needed, the Campaign table is joined with the Advertiser table.

Benefits:

- Less redundancy.
- Easier updates.
- Better data integrity.
- Smaller tables.
- Faster maintenance.

---

## Interview Explanation

Primary Keys and Foreign Keys are fundamental to relational databases.

Primary Keys uniquely identify records, while Foreign Keys create relationships between tables.

Together they reduce redundancy, maintain data integrity, and enable scalable database design.

---

## Interview Q&A ⭐

### Q1. What is a Primary Key?

#### Here's How I'd Answer

A Primary Key is a column that uniquely identifies every record in a table.

It must be unique, cannot be NULL, and should remain stable throughout the lifetime of the record.

---

### Q2. What is a Foreign Key?

#### Here's How I'd Answer

A Foreign Key is a column that references the Primary Key of another table.

It creates relationships between tables while reducing data duplication and maintaining consistency.

---

### Q3. Why shouldn't names be Primary Keys?

#### Here's How I'd Answer

Names are business attributes that may not be unique and can change over time.

Using names as Primary Keys can lead to duplicate records, difficult updates, and broken relationships.

System-generated IDs are a much better choice because they remain stable.

---

### Q4. Why do we use Foreign Keys instead of storing customer names?

#### Here's How I'd Answer

Foreign Keys reduce redundancy by storing only the unique identifier of a related record.

If customer information changes, it only needs to be updated in one place instead of every related record.

This keeps the database consistent and easier to maintain.

---

### Q5. What is Referential Integrity?

#### Here's How I'd Answer

Referential Integrity ensures that every Foreign Key references an existing Primary Key.

This prevents orphan records and guarantees that relationships between tables remain valid.

---

### Q6. Why does Google store advertiser_id instead of advertiser_name in the Campaign table?

#### Here's How I'd Answer

The Advertiser table already contains all advertiser information.

The Campaign table only needs to know which advertiser owns the campaign, so storing `advertiser_id` is sufficient.

This reduces redundancy, keeps the Campaign table lightweight, maintains referential integrity, and allows advertiser details to be retrieved using SQL JOINs whenever needed.

---

## Common Mistakes

❌ Using names, emails, or phone numbers as Primary Keys.

✅ Use stable, unique identifiers.

---

❌ Storing complete customer information in every transaction.

✅ Store only the Foreign Key.

---

❌ Allowing Foreign Keys that reference non-existent records.

✅ Enforce referential integrity.

---

## Key Takeaways

- Every table should have a Primary Key.
- Primary Keys identify records.
- Foreign Keys connect tables.
- IDs are preferred over business attributes.
- Foreign Keys improve consistency and reduce redundancy.
- Referential Integrity ensures valid relationships.
- Primary Keys and Foreign Keys are the foundation of SQL JOINs.

---

## Revision Notes

### Practical Decision Flow

Whenever you design a database, ask yourself:

1. What uniquely identifies this entity?
2. Can this identifier ever change?
3. Which information belongs to this table?
4. Which information belongs to another table?
5. How will these tables connect?

---

### Quick Interview Revision

| Concept | One-Line Summary |
|----------|------------------|
| Primary Key | Uniquely identifies a record. |
| Foreign Key | Connects one table to another. |
| Referential Integrity | Every Foreign Key must reference an existing Primary Key. |

### Memory Trick

- **Primary Key** → Identity
- **Foreign Key** → Relationship
- **Referential Integrity** → Protection

---

### One-Line Summary

> **Primary Keys identify records, Foreign Keys connect records, and together they form the foundation of every relational database.**
