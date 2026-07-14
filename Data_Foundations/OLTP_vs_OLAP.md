# OLTP vs OLAP

## OLTP (Online Transaction Processing)

Purpose:

Handle day-to-day business transactions.

Examples:

- Payments
- Orders
- Login
- Ride Booking

Characteristics:

- High transaction volume.
- Fast inserts and updates.
- Current operational data.

---

## OLAP (Online Analytical Processing)

Purpose:

Analyze business data.

Examples:

- Revenue by Country.
- Monthly Sales.
- Top Advertisers.

Characteristics:

- Historical analysis.
- Complex queries.
- Read-heavy workloads.

---

## Why Don't We Analyze OLTP Directly?

- Slows down transactions.
- Data changes continuously.
- Expensive analytical queries.
- Poor user experience.

---

## Comparison

| OLTP | OLAP |
|------|------|
| Transactions | Analytics |
| Write-heavy | Read-heavy |
| Current data | Historical data |
| Fast updates | Complex queries |

---

## Key Takeaways

- OLTP = Operations.
- OLAP = Analytics.
