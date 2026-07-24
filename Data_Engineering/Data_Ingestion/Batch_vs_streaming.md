# Batch vs Streaming

## Why does this exist?

Not every business requires real-time data. Choosing the correct ingestion strategy balances cost, latency, and business requirements.

---

# Batch Processing

## Definition

Data is collected over a period of time and processed together.

### Examples

* Payroll
* Daily Sales Reports
* Monthly Finance Reports

### Advantages

* Lower infrastructure cost
* Easier to maintain
* Efficient for historical analytics

### Disadvantages

* Delayed insights
* Not suitable for real-time decision-making

---

# Streaming Processing

## Definition

Data is ingested and processed continuously as events occur.

### Examples

* Fraud Detection
* Live Recommendations
* Ride Tracking
* Google Ads Clicks

### Advantages

* Near real-time insights
* Immediate business actions
* Better customer experience

### Disadvantages

* Higher infrastructure cost
* More operational complexity
* Continuous monitoring required

---

## Choosing Between Batch and Streaming

The decision should be based on **business requirements**, not technology preference.

| Business Need   | Recommended Approach |
| --------------- | -------------------- |
| Daily Reports   | Batch                |
| Fraud Detection | Streaming            |
| Monthly Payroll | Batch                |
| Live Dashboard  | Streaming            |

---

## Interview Explanation

Streaming is **not always better**.

Use streaming only when the business gains value from low-latency insights. Otherwise, batch processing is often simpler and more cost-effective.

---

## Common Mistakes

* Choosing streaming because it is "modern."
* Ignoring infrastructure costs.
* Forgetting that many business problems do not require real-time processing.

---

## Key Takeaways

* Batch = Scheduled processing.
* Streaming = Continuous processing.
* Business requirements drive the choice.
