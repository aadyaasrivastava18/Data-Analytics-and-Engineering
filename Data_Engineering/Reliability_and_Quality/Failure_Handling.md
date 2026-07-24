# Failure Handling

## Why does this exist?

Data pipelines operate across multiple systems, including databases, APIs, message queues, storage services, and Data Warehouses. Since these systems are distributed, failures are inevitable.

Failure Handling ensures that pipelines can detect failures, minimise business impact, recover safely, and maintain data reliability without compromising data quality.

---

# Problem it solves

Without proper failure handling:

* Pipelines stop unexpectedly.
* Data may be lost or duplicated.
* Reports become inaccurate.
* Manual intervention increases operational overhead.
* Business decisions are made using incomplete or inconsistent data.

A reliable pipeline is designed to expect failures rather than assume everything will always work correctly.

---

# Definition

Failure Handling is the process of detecting, classifying, diagnosing, and recovering from failures that occur during data ingestion and processing.

The objective is to restore the pipeline while maintaining data correctness and minimising downtime.

---

# Failure Handling Workflow

```text
Failure Detected
        ↓
Identify Failure Type
        ↓
Root Cause Analysis
        ↓
Choose Recovery Strategy
        ↓
Resume Pipeline
        ↓
Validate Data Integrity
```

Recovery should only begin after understanding the cause of the failure.

---

## Failure Types Comparison

| Failure Type               | Cause                                                                    | Examples                                                                   | Business Impact                                                                     | Recovery Strategy                                                                                   |
| -------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Dependency Failure**     | An external system required by the pipeline becomes unavailable.         | Database unavailable, API timeout, Kafka unavailable, Cloud Storage outage | Pipeline cannot read or write data until the dependency recovers.                   | Wait for the dependency to become healthy, then safely resume processing.                           |
| **Infrastructure Failure** | The execution environment becomes unhealthy.                             | Disk full, Server crash, Memory exhaustion, VM failure                     | Pipeline execution stops due to resource or hardware limitations.                   | Restore infrastructure, verify system health, and resume the pipeline.                              |
| **Data Failure**           | Incoming data is invalid, incomplete, or incompatible with the pipeline. | Corrupted CSV, Missing columns, Schema mismatch, Invalid data types        | Incorrect or incomplete data may enter downstream systems if not detected.          | Reject or quarantine the data, notify the source owner, and prevent invalid data from being loaded. |
| **Application Failure**    | Errors or bugs within the pipeline implementation.                       | NullPointerException, Logic bug, Configuration error, Unhandled exception  | Pipeline execution fails even though infrastructure and source systems are healthy. | Investigate logs, identify the root cause, fix the application, redeploy, and rerun the pipeline.   |


# Root Cause Analysis

Before implementing any recovery strategy, identify why the failure occurred.

Questions to ask:

* Which component failed?
* Is the failure temporary or permanent?
* Is the source system healthy?
* Has any partial data already been processed?
* What is the business impact?

Root cause analysis prevents repeated failures and ineffective fixes.

---

# Temporary vs Permanent Failures

| Temporary Failure          | Permanent Failure         |
| -------------------------- | ------------------------- |
| Network timeout            | Corrupted CSV             |
| Database restart           | Missing mandatory columns |
| Temporary API outage       | Schema mismatch           |
| Short service interruption | Application bug           |

Temporary failures often recover automatically, while permanent failures require corrective action.

---

# Recovery Principles

A reliable recovery strategy should:

* Prevent data loss.
* Avoid duplicate processing.
* Minimise downtime.
* Preserve data consistency.
* Reduce manual intervention.

Recovery is not simply restarting the pipeline—it is restoring the system without compromising data integrity.

---

# Real-World Example

An ingestion pipeline reads customer transactions from PostgreSQL every night at **2:00 AM**.

During scheduled maintenance, the database is unavailable for **15 minutes**.

The pipeline identifies this as a **Dependency Failure**. Instead of treating it as an application issue, it waits until the database becomes available and resumes processing without compromising data integrity.

---

# Interview Explanation

Failure Handling is the practice of detecting, classifying, and recovering from pipeline failures while maintaining data reliability. The first responsibility of an engineer is to identify the failure type before selecting an appropriate recovery strategy.

---

# Common Mistakes

* Assuming every failure requires a retry.
* Restarting pipelines without identifying the root cause.
* Treating all failures as infrastructure issues.
* Loading invalid data into production systems.
* Accepting manual recovery as a permanent solution.

---

# Key Takeaways

* Failures are expected in distributed systems.
* Every failure should first be classified before recovery begins.
* Different failure types require different recovery strategies.
* Reliable pipelines prioritise data integrity over rapid recovery.
* Root cause analysis is more valuable than repeatedly restarting failed pipelines.
