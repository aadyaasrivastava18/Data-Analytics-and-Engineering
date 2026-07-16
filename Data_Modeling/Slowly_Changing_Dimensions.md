# Slowly Changing Dimensions (SCD)

## Why does this exist?

In a Data Warehouse, Fact Tables usually remain unchanged once an event has occurred. However, Dimension Tables contain descriptive information such as customer addresses, employee departments, advertiser billing addresses, or product categories.

Over time, these descriptive attributes change.

The challenge is deciding **what to do when a Dimension value changes**.

Should we overwrite the old value?

Should we preserve history?

Should we keep only the latest and the previous value?

Slowly Changing Dimensions (SCD) provide different strategies depending on the business requirement.

---

# Problem it solves

Consider the following Customer Dimension.

## Customer_Dim

| customer_id | customer_name | city  |
| ----------- | ------------- | ----- |
| 101         | Aradhya       | Delhi |

After six months, the customer moves to Bengaluru.

What should we do?

### Option A

Update the row.

| customer_id | customer_name | city      |
| ----------- | ------------- | --------- |
| 101         | Aradhya       | Bengaluru |

History is lost.

---

### Option B

Create a new row.

| customer_id | customer_name | city      |
| ----------- | ------------- | --------- |
| 101         | Aradhya       | Delhi     |
| 101         | Aradhya       | Bengaluru |

History is preserved.

---

Neither option is universally correct.

The correct choice depends entirely on the business requirement.

---

# Definition

A Slowly Changing Dimension (SCD) is a technique used in Data Warehouses to manage changes in Dimension Tables over time.

Different SCD types exist because different businesses have different requirements for maintaining historical data.

---

# SCD Type 1

## Business Requirement

The business only cares about the latest value.

Historical information is not required.

Example:

The organisation only wants the advertiser's current billing address.

---

## Solution

Overwrite the existing record.

### Before

| advertiser_id | advertiser_name | billing_address |
| ------------- | --------------- | --------------- |
| 101           | ABC Ltd.        | Delhi           |

---

### After

| advertiser_id | advertiser_name | billing_address |
| ------------- | --------------- | --------------- |
| 101           | ABC Ltd.        | Bengaluru       |

The previous value is permanently lost.

---

## Characteristics

* Updates the existing row.
* No history maintained.
* Simple implementation.
* Small storage requirement.

---

## Use Cases

* Current email address
* Current phone number
* Current billing address
* Current customer status

---

## Advantages

* Easy to implement.
* Minimal storage.
* Fast updates.

---

## Disadvantages

* Historical information is lost permanently.

---

# SCD Type 2

## Business Requirement

The business requires complete historical information.

Example:

The organisation must retain every billing address for auditing and historical reporting.

---

## Solution

Insert a new row whenever a tracked attribute changes.

### Before

| advertiser_id | advertiser_name | billing_address |
| ------------- | --------------- | --------------- |
| 101           | ABC Ltd.        | Delhi           |

---

### After

| surrogate_key | advertiser_id | advertiser_name | billing_address | start_date | end_date   | is_current |
| ------------- | ------------- | --------------- | --------------- | ---------- | ---------- | ---------- |
| 1             | 101           | ABC Ltd.        | Delhi           | 2024-01-01 | 2025-06-30 | No         |
| 2             | 101           | ABC Ltd.        | Bengaluru       | 2025-07-01 | NULL       | Yes        |

The previous record is preserved.

---

## Why use a Surrogate Key?

Notice both records have the same `advertiser_id`.

A surrogate key uniquely identifies each historical version.

| surrogate_key | advertiser_id |
| ------------- | ------------- |
| 1             | 101           |
| 2             | 101           |

Without a surrogate key, multiple historical records for the same business entity would violate the primary key constraint.

---

## Characteristics

* Inserts a new row.
* Preserves complete history.
* Supports historical reporting.
* Commonly used in enterprise Data Warehouses.

---

## Use Cases

* Customer address history
* Employee department history
* Product price history
* Advertiser billing history
* Regulatory and audit reporting

---

## Advantages

* Complete historical tracking.
* Supports auditing.
* Enables time-based analysis.

---

## Disadvantages

* Increased storage.
* More complex ETL logic.
* Larger Dimension Tables.

---

# SCD Type 3

## Business Requirement

The business only needs limited history.

Usually the current value and the immediately previous value.

Example:

The CEO wants to know only the customer's current city and previous city.

---

## Solution

Add additional columns to store previous values.

### Before

| customer_id | current_city |
| ----------- | ------------ |
| 101         | Delhi        |

---

Customer moves to Bengaluru.

### After

| customer_id | previous_city | current_city |
| ----------- | ------------- | ------------ |
| 101         | Delhi         | Bengaluru    |

Customer later moves to Mumbai.

| customer_id | previous_city | current_city |
| ----------- | ------------- | ------------ |
| 101         | Bengaluru     | Mumbai       |

Notice that the original city (Delhi) is no longer available.

Only limited history is retained.

---

## Characteristics

* Adds extra columns.
* Maintains limited history.
* Does not create additional rows.

---

## Use Cases

* Previous manager
* Previous department
* Previous city
* Previous account status

---

## Advantages

* Simple implementation.
* Less storage than Type 2.
* Useful when only recent history is required.

---

## Disadvantages

* Complete historical information is not preserved.
* Older values are overwritten.

---

# SCD Comparison

| Type       | Action                       | History    | Storage | Example                         |
| ---------- | ---------------------------- | ---------- | ------- | ------------------------------- |
| **Type 1** | Update existing row          | ❌ None     | Low     | Current billing address         |
| **Type 2** | Insert new row               | ✅ Complete | High    | Address history, audit data     |
| **Type 3** | Add previous/current columns | ⚠️ Limited | Medium  | Current and previous department |

---

# Mental Model

## SCD Type 1

```text
Old Value
     │
Overwrite
     │
Current Value
```

---

## SCD Type 2

```text
Old Record
     │
Keep
     │
Create New Record
```

History is preserved.

---

## SCD Type 3

```text
Previous Value
        │
Current Value
```

Only limited history is retained.

---

# Decision Flow

Whenever a Dimension changes, ask:

1. Does the business only care about the latest value?

→ Use **SCD Type 1**

---

2. Does the business require complete history?

→ Use **SCD Type 2**

---

3. Does the business require only limited history?

→ Use **SCD Type 3**

---

# Interview Explanation

Slowly Changing Dimensions define how changes in Dimension Tables are handled over time.

The correct SCD type depends on business requirements.

Some businesses only need current values, while others require complete historical tracking for reporting or auditing.

---

# Interview Q&A ⭐

## Q1. What is a Slowly Changing Dimension (SCD)?

### Here's How I'd Answer

A Slowly Changing Dimension is a Data Warehousing technique used to manage changes in Dimension Tables over time.

Different SCD types determine whether historical information is overwritten, preserved, or partially retained based on business requirements.

---

## Q2. What is SCD Type 1?

### Here's How I'd Answer

SCD Type 1 overwrites the existing value when a Dimension changes.

It does not preserve historical information and is used when only the latest value matters.

---

## Q3. What is SCD Type 2?

### Here's How I'd Answer

SCD Type 2 preserves complete history by inserting a new row whenever a tracked attribute changes.

Additional fields such as surrogate key, start date, end date, and current flag are commonly used to manage historical versions.

---

## Q4. Why do we use a surrogate key in SCD Type 2?

### Here's How I'd Answer

Because the same business entity can have multiple historical versions.

A surrogate key uniquely identifies each version while the business key remains the same.

---

## Q5. What is SCD Type 3?

### Here's How I'd Answer

SCD Type 3 stores limited history by adding additional columns, such as previous and current values.

It is used when businesses only need recent historical information rather than complete history.

---

## Q6. Which SCD type is most commonly used?

### Here's How I'd Answer

SCD Type 2 is the most commonly used because it supports historical reporting, auditing, and time-based analysis while preserving complete history.

---

## Q7. How do you decide which SCD type to use?

### Here's How I'd Answer

I first understand the business requirement.

If only the latest value matters, I use Type 1.

If complete historical tracking is required, I use Type 2.

If only limited history is needed, I use Type 3.

The business requirement should always drive the design decision.

---

# Common Mistakes

❌ Assuming SCD Type 2 should always be used.

✅ Choose the SCD type based on business requirements.

---

❌ Thinking Fact Tables use SCD.

✅ SCD applies to **Dimension Tables**, not Fact Tables.

---

❌ Using business keys as the primary key in SCD Type 2.

✅ Use a surrogate key to uniquely identify each historical version.

---

# Key Takeaways

* SCD manages changes in Dimension Tables.
* Business requirements determine the correct SCD type.
* Type 1 overwrites history.
* Type 2 preserves complete history.
* Type 3 preserves limited history.
* SCD Type 2 commonly uses surrogate keys.
* Fact Tables generally do not use SCD; Dimension Tables do.

---

# Revision Notes

## Practical Decision Flow

When a Dimension attribute changes, ask:

1. Do we only need the current value?
2. Do we need complete history?
3. Do we only need the previous value?

The answers map directly to SCD Type 1, Type 2, and Type 3.

---

## Quick Interview Revision

| Concept    | One-Line Summary                                    |
| ---------- | --------------------------------------------------- |
| SCD Type 1 | Overwrite the existing value.                       |
| SCD Type 2 | Insert a new row and preserve history.              |
| SCD Type 3 | Keep only limited history using additional columns. |

### Memory Trick

* **Type 1** → **Replace**
* **Type 2** → **Remember Everything**
* **Type 3** → **Remember the Previous Value**

---

## One-Line Summary

> **Slowly Changing Dimensions define how changes to Dimension Tables are handled over time, with different strategies depending on whether the business requires no history, complete history, or limited history.**
