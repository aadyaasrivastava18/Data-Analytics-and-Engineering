# Monitoring & Observability

## Definition

**Monitoring** is the continuous tracking of predefined metrics and events to detect system issues.

**Observability** is the ability to investigate and determine **why** a system behaves a certain way using logs, metrics, traces, and metadata.

---

# Why It Exists

Production pipelines can:

- Fail completely
- Run slower than expected
- Produce incorrect data despite succeeding
- Fail silently without obvious errors

Monitoring detects these issues early, while observability helps identify their root cause.

---

# Monitoring vs Observability

| Monitoring | Observability |
|------------|---------------|
| Detects known issues | Investigates unknown issues |
| Uses predefined metrics & alerts | Uses logs, metrics, traces & metadata |
| Answers **"Is something wrong?"** | Answers **"Why is it wrong?"** |

---

# Monitoring Layers

```text
Infrastructure
│
├── CPU
├── Memory
├── Network
└── Storage

↓

Pipeline
│
├── Success / Failure
├── Duration
├── Retries
└── Task Status

↓

Data Quality
│
├── Row Count
├── NULL %
├── Duplicates
├── Missing Partitions
├── Schema Drift
└── Business KPI Validation
```

A production system should monitor **all three layers**, not just whether the pipeline succeeded.

---

# Workflow

```text
Pipeline Starts
      │
      ▼
Monitoring Collects Metrics
      │
      ▼
Is there an anomaly?
      │
 ┌────┴────┐
 │         │
No        Yes
 │         │
 ▼         ▼
Pipeline  Alert Triggered
Success        │
               ▼
      Root Cause Analysis
               │
               ▼
        Observability
```

---

# Core Concepts

### Metrics

Numerical values that measure system health.

Examples:

- Pipeline duration
- Rows processed
- CPU usage
- Memory usage
- Retry count

---

### Logs

Detailed records of pipeline execution.

Example:

```text
02:01 Extract Started
02:05 Extract Completed
02:06 Validation Failed
Reason: Database Timeout
```

Logs explain **what happened** during execution.

---

### Alerts

Notifications generated when predefined thresholds are exceeded.

Examples:

- Pipeline failed
- Runtime exceeded SLA
- Row count dropped by 90%
- High CPU usage

Alerts should be meaningful to avoid **alert fatigue**.

---

### Data Quality Monitoring

A pipeline can complete successfully while producing incorrect data.

Example:

```text
Yesterday Orders : 1,000,000

Today Orders : 12
```

Pipeline Status:

```text
SUCCESS ✅
```

Data Status:

```text
ABNORMAL ⚠️
```

This should trigger a **data quality alert**, even though no technical failure occurred.

---

# Monitoring vs Data Validation

| Pipeline Monitoring | Data Quality Monitoring |
|---------------------|-------------------------|
| Did the job run? | Is the output correct? |
| Did any task fail? | Are row counts reasonable? |
| Were retries successful? | Are NULL values acceptable? |
| How long did it take? | Did business KPIs change unexpectedly? |

Both are equally important in production.

---

# Production Debugging Process

When a dashboard shows incorrect data:

```text
Dashboard Incorrect
        │
        ▼
Check Pipeline Status
        │
        ▼
Check Logs
        │
        ▼
Check Metrics
        │
        ▼
Validate Data
        │
        ▼
Root Cause Analysis
```

**Good engineers investigate the system before investigating the data.**

---

# Production Example

```text
Pipeline Started
       │
       ▼
Extract
       │
       ▼
Transform
       │
       ▼
Load
       │
       ▼
Pipeline Success ✅
       │
       ▼
Row Count Validation
       │
       ▼
Unexpected Drop
       │
       ▼
Alert Data Engineer
       │
       ▼
Investigate Logs, Metrics & Data
```

Monitoring detects the anomaly.

Observability explains the root cause.

---

# Popular Tools

| Monitoring | Observability |
|------------|---------------|
| Prometheus | OpenTelemetry |
| Grafana | Jaeger |
| Datadog | Datadog |
| CloudWatch | Cloud Logging |
| Google Cloud Monitoring | Cloud Trace |

---

# Best Practices

- Monitor infrastructure, pipelines, and data quality.
- Define meaningful alert thresholds.
- Collect structured logs.
- Monitor historical trends instead of only failures.
- Reduce false alerts to avoid alert fatigue.
- Build dashboards for operational visibility.

---

# Interview Cheat Sheet

### Monitoring vs Observability?

Monitoring tells you **that** something is wrong.

Observability helps explain **why** it is wrong.

---

### What should be monitored?

- Infrastructure
- Pipeline execution
- Data quality

---

### Can a pipeline succeed but still produce incorrect results?

Yes.

A pipeline may complete successfully while loading incomplete, corrupted, duplicated, or unexpected data. This requires **data quality monitoring**, not just pipeline monitoring.

---

### What is the first thing you check when a dashboard shows incorrect data?

1. Pipeline status
2. Logs
3. Metrics
4. Data validation
5. Root cause analysis

---

# Key Takeaways

- Monitoring answers **"Is the system healthy?"**
- Observability answers **"Why is the system behaving this way?"**
- Logs, metrics, alerts, and traces are the foundation of observability.
- Production systems monitor **Infrastructure + Pipeline + Data Quality**.
- A successful pipeline does **not** guarantee correct data.
