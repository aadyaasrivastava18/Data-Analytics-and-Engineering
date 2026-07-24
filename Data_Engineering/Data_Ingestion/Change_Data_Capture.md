# Change Data Capture (CDC)

## Why does this exist?

Copying an entire database repeatedly is expensive and inefficient. CDC synchronizes only the changes made to the source database.

---

## Problem it solves

Instead of copying millions of records every hour, CDC transfers only the rows that have changed.

Benefits:

* Reduced database load
* Lower network usage
* Faster synchronization
* Better scalability

---

# Types of CDC

## 1. Timestamp-Based Incremental Loading

Uses a column such as:

```text
last_updated_timestamp
```

Example:

```sql
SELECT *
FROM orders
WHERE last_updated_timestamp > LAST_SYNC_TIME;
```

### Advantages

* Simple to implement
* Good for inserts and updates

### Limitations

* Cannot reliably detect deleted records.
* Requires querying production tables.

---

## 2. Log-Based CDC

Instead of querying tables, the CDC system reads the database's transaction log.

Example log:

```text
INSERT Order 101
UPDATE Order 101
DELETE Order 102
```

### Advantages

* Captures inserts, updates, and deletes.
* Minimal impact on the production database.
* Near real-time synchronization.
* Preferred for large-scale production systems.

---

# Initial Snapshot

CDC only captures changes after it starts.

Therefore, implementation typically follows:

```text
Initial Snapshot
        +
Continuous CDC
        =
Always Up-to-Date Warehouse
```

---

# Timestamp-Based vs Log-Based CDC

| Timestamp-Based             | Log-Based CDC                         |
| --------------------------- | ------------------------------------- |
| Uses `last_updated` column  | Reads transaction log                 |
| Detects inserts and updates | Detects inserts, updates, and deletes |
| Higher database load        | Lower database impact                 |
| Simpler                     | More scalable                         |

---

## Real-World Example

A new analytics warehouse is created.

1. Copy all historical data (Initial Snapshot).
2. Enable CDC.
3. Continuously synchronize new changes.

---

## Interview Explanation

A common misconception is that CDC always uses timestamps.

In reality, timestamp-based loading is one implementation. Modern production systems often use **log-based CDC**, which captures all database changes with minimal overhead.

---

## Common Mistakes

* Confusing incremental loading with log-based CDC.
* Assuming timestamps can detect deletes.
* Forgetting the need for an initial snapshot.

---

## Key Takeaways

* CDC transfers only changed data.
* Timestamp-based CDC is simple but limited.
* Log-based CDC is the preferred production approach.
* Initial Snapshot + CDC keeps data synchronized.
