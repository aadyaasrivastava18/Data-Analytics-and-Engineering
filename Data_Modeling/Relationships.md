# Relationships

## Why does this exist?

In a relational database, data is stored in multiple tables to reduce redundancy and improve maintainability. Once the data is split into different tables, there must be a way to define how these tables are connected.

Relationships define how business entities interact with each other and enable databases to retrieve related information efficiently.

Without relationships, databases would contain duplicated information, inconsistent data, and complex maintenance.

---

## Problem it solves

Imagine storing customer details inside every order.

| Order ID | Customer Name | Customer City | Product  |
| -------- | ------------- | ------------- | -------- |
| 1        | Aradhya       | Delhi         | Laptop   |
| 2        | Aradhya       | Delhi         | Mouse    |
| 3        | Aradhya       | Delhi         | Keyboard |

Problems:

* Customer information is repeated.
* Updating customer details requires changing multiple rows.
* Missing one update creates inconsistent data.
* Storage requirements increase unnecessarily.

Instead, relational databases separate business entities into different tables and connect them using relationships.

---

## Definition

A relationship defines how two or more business entities are connected in a relational database.

Relationships are established using **Primary Keys** and **Foreign Keys** and help maintain data integrity while reducing redundancy.

---

# One-to-One (1:1)

## Business Problem

Every employee is assigned one company laptop.

Every company laptop belongs to exactly one employee.

---

### Employee

| employee_id | employee_name |
| ----------- | ------------- |
| 101         | Aradhya       |

---

### Laptop

| laptop_id | employee_id |
| --------- | ----------- |
| L101      | 101         |

---

## Observation

* One Employee → One Laptop
* One Laptop → One Employee

This is a **One-to-One Relationship**.

---

## Why separate tables?

Employee and Laptop are two different business entities.

Laptop information such as:

* Serial Number
* RAM
* Processor
* Warranty

belongs to the Laptop entity, not the Employee.

Separating them:

* Reduces redundancy.
* Improves maintainability.
* Allows each entity to evolve independently.

---

# One-to-Many (1:N)

## Business Problem

One customer can place many orders.

Each order belongs to only one customer.

---

### Customer

| customer_id | customer_name |
| ----------- | ------------- |
| 101         | Aradhya       |

---

### Orders

| order_id | customer_id |
| -------- | ----------- |
| 1        | 101         |
| 2        | 101         |
| 3        | 101         |

---

## Observation

* One Customer → Many Orders
* One Order → One Customer

This is a **One-to-Many Relationship**.

---

## Why use this design?

Instead of storing customer details in every order:

* Customer information is stored once.
* Orders reference the customer using `customer_id`.

Benefits:

* Less redundancy.
* Easier updates.
* Better consistency.
* Simpler maintenance.

---

# Many-to-Many (M:N)

## Business Problem

One engineer can work on multiple projects.

One project can have multiple engineers.

---

### Engineers

| engineer_id | engineer_name |
| ----------- | ------------- |
| E101        | Aradhya       |
| E102        | Rahul         |

---

### Projects

| project_id | project_name |
| ---------- | ------------ |
| P1         | Ads Safety   |
| P2         | YouTube ML   |

---

## Observation

* One Engineer → Many Projects
* One Project → Many Engineers

This is a **Many-to-Many Relationship**.

---

## Incorrect Design

| Engineer | Projects               |
| -------- | ---------------------- |
| Aradhya  | Ads Safety, YouTube ML |

Problems:

* Violates **1NF** (multiple values in one cell).
* Difficult to query.
* Difficult to update.
* Poor scalability.

---

# Junction (Bridge) Table

Many-to-Many relationships cannot be implemented directly.

Instead, we introduce a third table called a **Junction Table** (or **Bridge Table**).

---

### Engineer

| engineer_id | engineer_name |
| ----------- | ------------- |
| E101        | Aradhya       |
| E102        | Rahul         |

---

### Project

| project_id | project_name |
| ---------- | ------------ |
| P1         | Ads Safety   |
| P2         | YouTube ML   |

---

### Engineer_Project

| engineer_id | project_id |
| ----------- | ---------- |
| E101        | P1         |
| E101        | P2         |
| E102        | P1         |

The bridge table stores relationships instead of repeating data.

---

# Relationship Attributes

Sometimes the relationship itself has information.

Example:

Engineer assigned to Project.

We may need to store:

* Start Date
* End Date
* Role
* Allocation %
* Assignment Status

These attributes do **not** belong to the Engineer.

They do **not** belong to the Project.

They belong to the **relationship** between them.

Therefore, they are stored in the **Bridge Table**.

---

### Engineer_Project

| engineer_id | project_id | start_date | end_date | role      | allocation |
| ----------- | ---------- | ---------- | -------- | --------- | ---------- |
| E101        | P1         | 01-Jan     | 31-Dec   | Developer | 100%       |

---

# Relationship Comparison

| Relationship           | Description                                                                    | Example           |
| ---------------------- | ------------------------------------------------------------------------------ | ----------------- |
| **One-to-One (1:1)**   | One record relates to exactly one other record.                                | Employee ↔ Laptop |
| **One-to-Many (1:N)**  | One record relates to multiple records, but each child belongs to one parent.  | Customer → Orders |
| **Many-to-Many (M:N)** | Multiple records relate to multiple records. Implemented using a Bridge Table. | Student ↔ Course  |

---

# Mental Model

```text
One-to-One

Employee
     │
     │
Laptop
```

```text
One-to-Many

Customer
     │
     ├────► Order
     ├────► Order
     └────► Order
```

```text
Many-to-Many

Engineer
     │
     ▼
Engineer_Project
     ▲
     │
Project
```

---

# Real-world Example

### University Management System

One student can enroll in many courses.

One course can have many students.

A bridge table stores:

* Student ID
* Course ID
* Enrollment Date
* Final Grade
* Completion Status

---

# Interview Q&A ⭐

## Q1. What is a relationship in a database?

### Here's How I'd Answer

A relationship defines how two or more business entities are connected in a relational database.

Relationships are established using Primary Keys and Foreign Keys to reduce redundancy and maintain data integrity.

---

## Q2. What is a One-to-One relationship?

### Here's How I'd Answer

A One-to-One relationship exists when one record in a table relates to exactly one record in another table.

For example, one employee is assigned one company laptop, and each laptop belongs to only one employee.

---

## Q3. What is a One-to-Many relationship?

### Here's How I'd Answer

A One-to-Many relationship exists when one parent record can have multiple child records, while each child belongs to only one parent.

For example, one customer can place many orders, but each order belongs to exactly one customer.

---

## Q4. What is a Many-to-Many relationship?

### Here's How I'd Answer

A Many-to-Many relationship exists when multiple records from one table relate to multiple records in another table.

Examples include Students and Courses or Engineers and Projects.

These relationships are implemented using a Bridge Table.

---

## Q5. Why do we need a Bridge Table?

### Here's How I'd Answer

A Bridge Table resolves a Many-to-Many relationship by storing references to both entities.

It also stores attributes that describe the relationship itself, such as role, allocation percentage, start date, or enrollment date.

---

## Q6. Why should Start Date and Role be stored in the Bridge Table?

### Here's How I'd Answer

These attributes describe the assignment between an engineer and a project rather than the engineer or project individually.

Therefore, they belong to the relationship and should be stored in the Bridge Table.

---

## Q7. How are relationships connected to SQL JOINs?

### Here's How I'd Answer

SQL JOINs use Primary Keys and Foreign Keys defined through relationships to retrieve related information from multiple tables.

Without relationships, JOIN operations would not be meaningful.

---

# Common Mistakes

❌ Storing multiple values in one column.

✅ Create separate rows or a Bridge Table.

---

❌ Storing relationship-specific attributes in the parent table.

✅ Store them in the Bridge Table.

---

❌ Thinking relationships exist only for SQL JOINs.

✅ Relationships model how the business actually works.

---

❌ Treating unrelated business entities as one table.

✅ Each table should represent one business entity.

---

# Key Takeaways

* Relationships connect business entities.
* One table should represent one business entity.
* One-to-One links one record to one record.
* One-to-Many is the most common database relationship.
* Many-to-Many requires a Bridge Table.
* Relationship-specific attributes belong in the Bridge Table.
* Well-designed relationships reduce redundancy and improve maintainability.

---

# Revision Notes

## Practical Decision Flow

Whenever designing a database, ask yourself:

1. What are the business entities?
2. How do these entities interact?
3. Is the relationship 1:1, 1:N, or M:N?
4. Does the relationship itself have attributes?
5. If yes, create a Bridge Table.

---

## Quick Interview Revision

| Concept      | One-Line Summary                                                        |
| ------------ | ----------------------------------------------------------------------- |
| One-to-One   | One record relates to one record.                                       |
| One-to-Many  | One parent relates to many children.                                    |
| Many-to-Many | Many records relate to many records.                                    |
| Bridge Table | Resolves Many-to-Many relationships and stores relationship attributes. |

### Memory Trick

* **1:1** → One ↔ One
* **1:N** → One → Many
* **M:N** → Many ↔ Many → Bridge Table

---

## One-Line Summary

> **Relationships model how business entities interact, while Bridge Tables resolve many-to-many relationships and store information about those relationships.**
