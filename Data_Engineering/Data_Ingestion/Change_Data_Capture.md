# Change Data Capture (CDC)

## Why does this exist?

Continuously copying an entire database is slow, expensive, and inefficient. Change Data Capture (CDC) synchronizes **only the data that has changed**, making data pipelines faster and more scalable.

---

## Problem it Solves

Suppose an `orders` table contains **100 million rows**, but only **2,000 rows** change every hour.

Without CDC:

```text
Copy all 100M rows every hour
```

With CDC:

```text
Copy only the 2,000 changed rows
```

This significantly reduces:

* Database load
* Network traffic
* Processing time
* Storage overhead

---

## What is CDC?

> **Change Data Capture (CDC) is the process of identifying and transferring only the changes (INSERT, UPDATE, DELETE) made to a source database instead of copying the entire dataset.**

---

# Types of CDC

## 1. Timestamp-Based CDC

Tracks changes using a timestamp column (e.g., `last_updated_timestamp`).

```sql
SELECT *
FROM orders
WHERE last_updated_timestamp > LAST_SYNC_TIME;
```

### Advantages

* Simple to implement
* Efficient for inserts and updates

### Limitations

* Cannot reliably detect deleted records
* Requires querying the production database

---

## 2. Log-Based CDC

Reads the database's **transaction log** instead of querying the table.

Example:

```text
INSERT Order 101
UPDATE Order 101
DELETE Order 102
```

### Advantages

* Captures inserts, updates, and deletes
* Minimal impact on the production database
* Near real-time synchronization
* Preferred in large-scale production systems

---

## Initial Snapshot

CDC captures **future changes only**.

Existing records must first be copied using an **Initial Snapshot**.

```text
Initial Snapshot
        +
Continuous CDC
        =
Always Up-to-Date Warehouse
```

---

## Comparison

| Timestamp-Based CDC        | Log-Based CDC                      |
| -------------------------- | ---------------------------------- |
| Uses `last_updated` column | Reads transaction log              |
| Detects inserts & updates  | Detects inserts, updates & deletes |
| Queries production tables  | Reads database logs                |
| Simple to implement        | More scalable & efficient          |

---

## Real-World Example

A company launches a new Data Warehouse.

1. Perform an **Initial Snapshot** to copy historical data.
2. Enable **CDC**.
3. Continuously synchronize new inserts, updates, and deletes.

---

## Interview Explanation

Interviewers often ask why modern systems prefer **Log-Based CDC**.

A strong answer:

> Timestamp-based CDC works well for inserts and updates but cannot reliably detect deletes. Log-based CDC reads the database's transaction log, capturing inserts, updates, and deletes with minimal impact on the production database.

---

## Common Mistakes

* Assuming CDC always uses timestamps.
* Confusing incremental loading with log-based CDC.
* Forgetting that CDC requires an Initial Snapshot.
* Assuming timestamps can detect deleted records.

---

## Key Takeaways

* CDC transfers **only changed data**.
* Timestamp-based CDC is simple but has limitations.
* Log-based CDC is the preferred production approach.
* Initial Snapshot + CDC keeps the destination continuously synchronized.
