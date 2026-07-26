# Monitoring & Observability

## Definition

**Monitoring** is the continuous measurement of a system's health using predefined metrics to detect failures and trigger alerts.

**Observability** is the ability to understand **why** a system failed by analysing metrics, logs, and traces.

---

# Monitoring vs Observability

| Monitoring | Observability |
|------------|---------------|
| Detects problems | Explains problems |
| "What happened?" | "Why did it happen?" |
| Uses predefined metrics | Uses metrics, logs & traces |
| Alerting | Root cause analysis |
| Reactive detection | Deep investigation |

---

# Monitoring Workflow

```text
Production System
        │
        ▼
 Collect Metrics
        │
        ▼
 Evaluate Thresholds
        │
   ┌────┴────┐
   │         │
Normal   Threshold Crossed
   │         │
   ▼         ▼
Continue  Trigger Alert
              │
              ▼
       Engineer Investigates
              │
              ▼
         Issue Resolved
```

---

# Three Pillars of Observability

| Pillar | Purpose | Answers |
|---------|---------|---------|
| Metrics | Measure system health | How much? |
| Logs | Record events | What happened? |
| Traces | Track request journey | Where & why? |

---

# Metrics vs Logs vs Traces

| Feature | Metrics | Logs | Traces |
|---------|----------|------|---------|
| Data Type | Numerical | Text | Request Flow |
| Purpose | Monitoring | Debugging | Root Cause |
| Example | CPU = 75% | DB Timeout | Payment Service = 14 sec |
| Best For | Trends | Events | Distributed Systems |

---

# Observability Flow

```text
Production System
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
Metrics Logs Traces
 └─────┼─────┘
       ▼
Root Cause Analysis
```

---

# Dashboards

> A dashboard provides a real-time visual view of system health.

Typical dashboard:

| Pipeline | Status | Duration |
|----------|--------|----------|
| Sales ETL | ✅ | 10 min |
| Orders ETL | ❌ | Failed |
| Payments ETL | ⚠️ | Running (40 min) |

---

# Alert Lifecycle

```text
Metric Collected
        │
        ▼
Threshold Check
        │
   ┌────┴────┐
   │         │
Normal   Alert
              │
              ▼
      Severity Assigned
              │
              ▼
 Notify Correct Team
              │
              ▼
 Incident Response
```

---

# Alert Severity

| Severity | Example | Action |
|----------|---------|--------|
| 🔵 Info | ETL Completed | Dashboard |
| 🟡 Warning | CPU > 75% | Monitor |
| 🟠 High | Pipeline Slow | Investigate |
| 🔴 Critical | Pipeline Failed | Immediate Action |

---

# Alert Fatigue

> Too many unnecessary alerts cause engineers to ignore notifications.

### Best Practices

- Threshold-based alerts
- Alert deduplication
- Severity levels
- Time-based thresholds
- Notify the correct team

---

# SLI vs SLO vs SLA

| Term | Meaning | Example |
|------|---------|---------|
| SLI | Actual measurement | Availability = 99.7% |
| SLO | Target | Availability ≥ 99.5% |
| SLA | Customer commitment | Guaranteed 99.5% uptime |

---

# Relationship

```text
Actual Performance
        │
        ▼
      SLI
        │
Compared Against
        │
        ▼
      SLO
        │
Promised To Customer
        │
        ▼
      SLA
```

---

# Golden Signals

| Signal | Measures | Question Answered |
|---------|----------|-------------------|
| Latency | Response Time | How fast? |
| Traffic | Request Volume | How much load? |
| Errors | Failed Requests | What is failing? |
| Saturation | Resource Usage | How close to capacity? |

---

# Golden Signals Summary

| Signal | Example |
|---------|---------|
| Latency | 250 ms |
| Traffic | 12,000 requests/min |
| Errors | 0.3% failed requests |
| Saturation | CPU = 94% |

---

# Relationship Between Golden Signals

```text
Traffic ↑
     │
     ▼
Saturation ↑
     │
     ▼
Latency ↑
     │
     ▼
Errors ↑
     │
     ▼
Customer Impact
```

---

# Incident Response Flow

```text
Monitoring

↓

Alert Triggered

↓

Logs + Metrics + Traces

↓

Root Cause Found

↓

Fix Applied

↓

Monitoring Confirms Recovery
```

---

# Best Practices

| Practice | Benefit |
|----------|---------|
| Monitor critical metrics | Detect failures early |
| Set meaningful thresholds | Reduce false alerts |
| Use dashboards | Quick visibility |
| Centralize logs | Easier debugging |
| Enable tracing | Faster root cause analysis |
| Define SLOs | Clear reliability targets |
| Review alerts regularly | Prevent alert fatigue |

---

# Common Mistakes

| Mistake | Impact |
|----------|--------|
| Monitoring everything | Alert fatigue |
| No alert thresholds | Too many notifications |
| Ignoring traces | Slow debugging |
| No dashboards | Poor visibility |
| Only monitoring infrastructure | Miss application issues |
| No SLOs | Undefined reliability goals |

---

# Interview Cheat Sheet

| Question | Answer |
|----------|--------|
| Monitoring? | Detect system health using metrics. |
| Observability? | Explain why failures occur using metrics, logs & traces. |
| Metrics? | Numerical measurements. |
| Logs? | Timestamped event records. |
| Traces? | End-to-end request journey. |
| Dashboard? | Visual view of system health. |
| Alert Fatigue? | Too many alerts causing engineers to ignore them. |
| SLI? | Actual measured performance. |
| SLO? | Target performance objective. |
| SLA? | Customer agreement on service quality. |
| Four Golden Signals? | Latency, Traffic, Errors, Saturation. |

---

# Key Takeaways

- Monitoring tells **what** happened.
- Observability explains **why** it happened.
- Metrics measure health.
- Logs record events.
- Traces follow request journeys.
- Dashboards provide real-time visibility.
- Alerts should be meaningful and actionable.
- SLI measures current performance.
- SLO defines the engineering target.
- SLA defines the customer commitment.
- Monitor the Four Golden Signals to maintain reliable systems.
