# Retry Strategies

## Why does this exist?

Distributed systems frequently encounter transient failures such as temporary network issues, service restarts, or database outages. Immediately treating these failures as permanent can lead to unnecessary job failures, while excessive retries can overload recovering services.

Retry Strategies provide a controlled mechanism to recover from temporary failures while protecting system stability.

---

# Problem it solves

Without an appropriate retry strategy:

* Temporary failures cause unnecessary pipeline failures.
* Aggressive retries overload recovering services.
* Compute and network resources are wasted.
* Large numbers of clients may create Retry Storms.
* Recovery becomes slower instead of faster.

A well-designed retry strategy balances fast recovery with system protection.

---

# Definition

A Retry Strategy defines **when**, **how often**, and **how long** a pipeline should attempt an operation again after a transient failure.

The objective is to maximise successful recovery while minimising unnecessary load on dependent systems.

---

# Retry Workflow

```text
Operation
     │
     ▼
Failure
     │
     ▼
Classify Failure
     │
     ├── Permanent Failure
     │       │
     │       ▼
     │   Stop & Investigate
     │
     └── Transient Failure
             │
             ▼
      Execute Retry Strategy
             │
             ▼
Success or Retry Limit Reached
```

---

# Retry Preconditions

Retries should only be attempted when:

* The failure is temporary.
* The dependency is expected to recover.
* Retrying will not compromise data integrity.
* The operation can be safely executed again.

---

# Retry Strategies Comparison

| Strategy                         | Retry Pattern                                                           | Advantages                                                                         | Disadvantages                                                                                            | Best Use Case                                                  | Example                                                                |
| -------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Immediate Retry**              | Retry immediately after failure.                                        | Fastest recovery for momentary glitches.                                           | Can overload recovering services and create Retry Storms.                                                | Very short-lived network glitches or local operations.         | Retry instantly after a connection timeout.                            |
| **Fixed Delay Retry**            | Retry after a constant interval (e.g., every 30 seconds).               | Simple, predictable, and easy to configure.                                        | Does not adapt to outage duration; may be too slow for short outages or too aggressive for long outages. | Small-scale applications or low-traffic systems.               | Retry every 30 seconds until the service recovers.                     |
| **Exponential Backoff**          | Increase the delay after each failed attempt (1s → 2s → 4s → 8s → ...). | Reduces pressure on recovering services and adapts to longer outages.              | Multiple clients may still retry at the same time, causing synchronized traffic spikes.                  | Standard retry strategy in distributed systems.                | Database temporarily unavailable during maintenance.                   |
| **Exponential Backoff + Jitter** | Exponential Backoff with a random delay added to each retry.            | Prevents synchronized retries, distributes traffic, and improves service recovery. | Slightly more complex to implement.                                                                      | Large-scale distributed systems and cloud-native applications. | Kafka consumers, cloud SDKs, large ingestion pipelines, microservices. |

---

# Choosing the Right Retry Strategy

| Scenario                               | Recommended Strategy           | Reason                                                                          |
| -------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------- |
| Temporary network timeout              | Immediate Retry or Fixed Delay | The service is likely to recover almost instantly.                              |
| Database restart (30–60 seconds)       | Exponential Backoff            | Balances quick recovery with reduced system load.                               |
| Large-scale distributed system         | Exponential Backoff + Jitter   | Prevents Retry Storms by spreading retries across time.                         |
| API rate limiting (HTTP 429)           | Exponential Backoff + Jitter   | Gives the service time to recover while avoiding repeated bursts of traffic.    |
| Corrupted CSV or invalid schema        | **Do Not Retry**               | The issue is permanent and requires data correction.                            |
| Application bug or configuration error | **Do Not Retry**               | Retrying cannot fix a software defect; the application must be corrected first. |

---

# Immediate Retry

Retries are attempted immediately after a failure.

### Advantages

* Fast recovery for momentary failures.

### Limitations

* High risk of overloading recovering services.
* Can create Retry Storms in distributed systems.

---

# Fixed Delay Retry

A constant delay is maintained between retry attempts.

Example:

```text
Retry
 ↓
30 seconds
 ↓
Retry
 ↓
30 seconds
 ↓
Retry
```

### Advantages

* Simple and predictable.
* Easy to implement.

### Limitations

* Does not adapt to outage duration.
* May increase recovery time for short outages.

---

# Exponential Backoff

The retry delay increases after every failed attempt.

Example:

```text
1 second
 ↓
2 seconds
 ↓
4 seconds
 ↓
8 seconds
 ↓
16 seconds
 ↓
32 seconds
```

### Advantages

* Adapts to longer outages.
* Reduces pressure on recovering services.

### Limitation

* Clients may still retry simultaneously.

---

# Jitter

Jitter introduces a small random delay into every retry.

Instead of:

```text
8 s
8 s
8 s
8 s
```

Retries become:

```text
7.3 s
8.8 s
6.9 s
9.1 s
```

### Benefits

* Distributes retry traffic.
* Prevents synchronized retries.
* Reduces Retry Storms.
* Improves recovery of distributed systems.

**Production Recommendation:** Use **Exponential Backoff + Jitter** for large-scale distributed systems.

---

# Retry Storm

A Retry Storm occurs when many clients repeatedly retry failed operations simultaneously, overwhelming a recovering service.

Example:

```text
Database Down
      │
      ▼
10,000 Pipelines Fail
      │
      ▼
All Retry Together
      │
      ▼
Database Recovers
      │
      ▼
Traffic Spike
      │
      ▼
Possible Service Overload
```

---

# Maximum Retry Limit

A pipeline should never retry indefinitely.

Every retry policy should define:

* Maximum retry attempts.
* Maximum retry duration.
* Job execution deadline.
* Timeout before marking the job as failed.

Once the retry limit is reached:

* Stop retrying.
* Mark the job as failed.
* Generate alerts.
* Notify the operations team.
* Investigate the root cause.

---

# Retry Decision Matrix

| Failure Scenario          | Retry? | Reason                              |
| ------------------------- | :----: | ----------------------------------- |
| Temporary network timeout |    ✅   | Expected to recover automatically.  |
| Database restart          |    ✅   | Temporary dependency failure.       |
| API rate limiting (429)   |    ✅   | Retry after waiting.                |
| Corrupted CSV             |    ❌   | Requires data correction.           |
| Schema mismatch           |    ❌   | Retry cannot fix invalid data.      |
| Application bug           |    ❌   | Code must be fixed before retrying. |

---

# Real-World Example

A pipeline reads transaction data from PostgreSQL every minute.

The database restarts for maintenance and becomes unavailable for **30 seconds**.

The pipeline identifies the issue as a **transient dependency failure**, applies **Exponential Backoff with Jitter**, retries safely, and resumes processing once the database becomes available.

---

# Interview Explanation

Retry Strategies define how distributed systems recover from transient failures. A production-ready retry mechanism classifies failures first, retries only temporary failures, applies Exponential Backoff with Jitter, and enforces retry limits to prevent infinite execution and Retry Storms.

---

# Common Mistakes

* Retrying every failure without classification.
* Using immediate retries in production.
* Retrying permanent failures.
* Allowing infinite retries.
* Ignoring synchronized retries.
* Forgetting to alert operators after retry exhaustion.

---

# Key Takeaways

* Retry only transient failures.
* Always classify failures before retrying.
* Immediate retries can overload recovering services.
* Fixed delays are simple but not adaptive.
* Exponential Backoff reduces retry frequency over time.
* Jitter prevents synchronized retries.
* Define retry limits to avoid infinite execution.
* A successful retry strategy balances recovery speed with system stability.
