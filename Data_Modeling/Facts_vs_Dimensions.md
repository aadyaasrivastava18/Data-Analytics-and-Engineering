# Facts vs Dimensions

## Why does this exist?

Businesses generate massive amounts of data every day. However, data alone has little value unless we can measure business performance and analyze it from different perspectives.

Fact and Dimension tables organize analytical data so that businesses can answer questions efficiently while minimizing redundancy and maximizing scalability.

This concept forms the foundation of Data Warehousing, Business Intelligence, Star Schema, and SQL Analytics.

---

## Problem it solves

Suppose a company stores all information in one large table.

| Revenue Loss | Country | Policy            | Analyst | Month | Severity |
| ------------ | ------- | ----------------- | ------- | ----- | -------- |
| 1000         | India   | Misrepresentation | John    | Jan   | High     |
| 2000         | India   | Misrepresentation | John    | Feb   | High     |
| 3000         | USA     | Counterfeit       | Alice   | Jan   | Medium   |

Problems:

* Country repeats many times.
* Policy repeats many times.
* Analyst repeats many times.
* Storage increases unnecessarily.
* Updating descriptive information becomes difficult.
* Data becomes harder to maintain.

Instead, analytical databases separate measurable values from descriptive information.

---

## Definition

A **Fact** is a measurable business event or numerical value.

A **Dimension** is descriptive information that provides context for analyzing a Fact.

Think of it like this:

> **Facts answer "How much?"**

> **Dimensions answer "By what?", "Where?", "Who?", "When?"**

---

# Fact (Metric)

## Business Problem

A manager asks:

> "Show me the total Revenue Loss."

The value being measured is:

**Revenue Loss**

This is a Fact because it represents a measurable business outcome.

---

## Characteristics of Facts

Facts are usually:

* Numeric
* Measurable
* Aggregated using SUM, COUNT, AVG, MIN, or MAX
* Stored in Fact Tables

Examples:

* Revenue
* Revenue Loss
* Sales
* Profit
* Order Count
* Investigation Time
* Clicks
* Impressions

---

# Dimensions

## Business Problem

A manager asks:

> "Show me Revenue Loss by Country."

The company still wants to measure:

**Revenue Loss**

But now they want to analyze it using:

* Country

Country provides context for the metric.

Therefore, Country is a Dimension.

---

## Characteristics of Dimensions

Dimensions describe Facts.

They answer questions such as:

* Who?
* What?
* Where?
* When?
* Which?

Examples:

* Customer
* Country
* Product
* Policy
* Date
* Month
* Analyst
* Advertiser
* Device
* Department

---

# Facts vs Dimensions

| Fact                      | Dimension                                     |
| ------------------------- | --------------------------------------------- |
| Measurable business event | Descriptive information                       |
| Usually numeric           | Usually text or descriptive attributes        |
| Answers "How much?"       | Answers "By what?", "Who?", "Where?", "When?" |
| Stored in Fact Tables     | Stored in Dimension Tables                    |
| Can be aggregated         | Used for grouping and filtering               |

---

# Business Questions

## Example 1

**Show total Revenue Loss by Country.**

| Component | Answer       |
| --------- | ------------ |
| Fact      | Revenue Loss |
| Dimension | Country      |
| Filter    | None         |

---

## Example 2

**Show average Investigation Time for each Analyst during Q1 2026.**

| Component | Answer                     |
| --------- | -------------------------- |
| Fact      | Average Investigation Time |
| Dimension | Analyst                    |
| Filter    | Q1 2026                    |

---

## Example 3

**Show total Revenue Loss by Country for High Severity violations in 2026.**

| Component | Answer              |
| --------- | ------------------- |
| Fact      | Revenue Loss        |
| Dimension | Country             |
| Filters   | High Severity, 2026 |

---

## Mental Model

Whenever someone asks a business question:

### Step 1

Identify the number they want.

↓

**Fact**

---

### Step 2

Identify how they want to analyze that number.

↓

**Dimension**

---

### Step 3

Identify any conditions.

↓

**Filters**

---

Example:

```text
Revenue Loss
      │
      ├── Country
      ├── Policy
      ├── Analyst
      └── Month
```

The metric remains the same.

Only the perspective changes.

---

# Real-world Example

Imagine Amazon.

The CEO asks:

* Revenue by Product
* Revenue by Country
* Revenue by Month
* Revenue by Salesperson

The Fact is always:

**Revenue**

The Dimensions change depending on the business question.

---
# Interview Explanation

Facts represent measurable business events.

Dimensions describe those events.

Businesses measure Facts while using Dimensions to group, filter, and analyze those measurements.

Understanding this distinction is the foundation of analytical database design.

---

# Interview Q&A ⭐

## Q1. What is a Fact?

### Here's How I'd Answer

A Fact is a measurable business event or numerical value that organizations analyze.

Examples include Revenue, Sales, Order Count, Revenue Loss, and Investigation Time.

Facts are stored in Fact Tables.

---

## Q2. What is a Dimension?

### Here's How I'd Answer

A Dimension is descriptive information that provides context to a Fact.

Examples include Customer, Country, Product, Date, Analyst, and Policy.

Dimensions are used to group, filter, and analyze Facts.

---

## Q3. How do you identify a Fact?

### Here's How I'd Answer

I first ask what the business wants to measure.

If it is a measurable value that can be aggregated, it is a Fact.

---

## Q4. How do you identify a Dimension?

### Here's How I'd Answer

I ask what information provides context to the metric.

If it helps group or filter the metric, it is a Dimension.

---

## Q5. Why is Revenue Loss a Fact but Country a Dimension?

### Here's How I'd Answer

Revenue Loss is the measurable business event.

Country provides context for analyzing that metric.

Many records can share the same country, so Country belongs in a Dimension Table while Revenue Loss belongs in the Fact Table.

---

## Q6. What is the relationship between Facts and Dimensions?

### Here's How I'd Answer

Fact Tables store measurable events and reference Dimension Tables through foreign keys.

Dimension Tables provide descriptive information that allows businesses to analyze Facts from different perspectives.

---

# Common Mistakes

❌ Assuming Facts are simply changing values.

✅ Facts are measurable business events.

---

❌ Assuming Dimensions change frequently.

✅ Dimensions provide descriptive context regardless of how often they change.

---

❌ Confusing Filters with Dimensions.

✅ Filters are conditions applied to Dimensions or Facts during analysis.

---

# Key Takeaways

* Facts are numbers the business measures.
* Dimensions describe those numbers.
* One Fact can be analyzed using many Dimensions.
* Business questions are built using Facts, Dimensions, and Filters.
* Facts are stored in Fact Tables.
* Dimensions are stored in Dimension Tables.

---

# Revision Notes

## Practical Decision Flow

Whenever you hear a business question:

1. What number is the business trying to measure?
2. What information is being used to analyze that number?
3. Are there any filters?

This immediately identifies the Fact, Dimension, and Filter.

---

## Quick Interview Revision

| Concept   | One-Line Summary                                 |
| --------- | ------------------------------------------------ |
| Fact      | The measurable business value.                   |
| Dimension | The descriptive context for a Fact.              |
| Filter    | A condition that limits the data being analyzed. |

### Memory Trick

* **Fact** → **How much?**
* **Dimension** → **By what?**
* **Filter** → **Which subset?**

---

## One-Line Summary

> **Facts measure the business, Dimensions describe the business, and Filters narrow the business question.**
