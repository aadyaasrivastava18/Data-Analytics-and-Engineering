# Data Mart

## Definition

A **Data Mart** is a **subject-oriented subset of a Data Warehouse** designed for a specific business function or department (e.g., Finance, Marketing, HR).

It contains curated, business-ready data tailored to a team's analytical needs.

---

# Why Use a Data Mart?

As organisations grow, a single Enterprise Data Warehouse serves multiple departments. Allowing every team to query the entire warehouse can lead to:

- Increased query latency
- Higher compute costs
- Complex SQL
- Unnecessary data access
- Difficult governance

A Data Mart provides each department with a focused, optimised view of the data.

---

# Architecture

```text
Operational Databases
        │
        ▼
     Data Lake
        │
        ▼
 Enterprise Data Warehouse
        │
 ┌──────┼────────┬───────┐
 ▼      ▼        ▼
Finance Marketing HR
 Mart     Mart    Mart
```

---

# Data Warehouse vs Data Mart

| Feature | Data Warehouse | Data Mart |
|----------|----------------|-----------|
| Scope | Enterprise-wide | Department-specific |
| Users | Entire organization | Individual business unit |
| Data | All business domains | Subject-oriented subset |
| Purpose | Central analytics platform | Department analytics |
| Size | Large | Smaller |
| Example | Enterprise Sales Data | Finance Revenue Mart |

---

# Benefits

| Benefit | Explanation |
|----------|-------------|
| Faster Queries | Smaller datasets reduce scan time. |
| Better Security | Departments access only relevant data. |
| Lower Cost | Less data scanned means lower compute costs. |
| Simpler Analytics | Users work with business-specific datasets. |
| Clear Ownership | Each department owns its analytical models. |
| Failure Isolation | Issues in one Data Mart do not affect others. |

---

# Data Flow

```text
Enterprise Data Warehouse
          │
          ├──────────► Finance Mart
          │
          ├──────────► Marketing Mart
          │
          └──────────► HR Mart
```

Each Data Mart consumes curated data from the Enterprise Data Warehouse.

---

# Metric Placement

| Metric Type | Store In |
|--------------|----------|
| Enterprise KPI (Revenue, Net Profit Margin, CLV) | Data Warehouse |
| Department-specific metric | Data Mart |

**Rule:** Shared business metrics should have a **Single Source of Truth (SSOT)** in the Data Warehouse. Department-specific calculations can live in the corresponding Data Mart.

---

# Production Example

### Amazon

**Enterprise Data Warehouse**

- Orders
- Customers
- Payments
- Products
- Inventory

↓

**Finance Mart**

- Revenue
- Profit
- Refunds
- Taxes

↓

**Marketing Mart**

- Campaign Performance
- CTR
- Conversion Rate
- Customer Segments

↓

**HR Mart**

- Employee Count
- Attrition
- Salary Analytics

Each team queries only the data relevant to its domain.

---

# Best Practices

- Build Data Marts from the Enterprise Data Warehouse.
- Keep enterprise KPIs in the Data Warehouse.
- Create department-specific models in each Data Mart.
- Apply role-based access control.
- Avoid duplicating business logic across multiple Data Marts.

---

# Common Mistakes

- Treating a Data Mart as an independent data source.
- Duplicating enterprise metrics across multiple Data Marts.
- Allowing departments to bypass the Data Warehouse.
- Giving all teams access to the entire warehouse.
- Creating unnecessary Data Marts for very small organizations.

---

# Interview Cheat Sheet

### What is a Data Mart?

A department-specific subset of a Data Warehouse optimized for a particular business function.

---

### Why use a Data Mart?

To improve performance, simplify analytics, strengthen access control, reduce compute costs, and provide clear data ownership.

---

### Data Warehouse vs Data Mart?

- **Data Warehouse:** Enterprise-wide analytical repository.
- **Data Mart:** Subject-oriented subset for a specific department.

---

### Can one Data Mart affect another?

No. Data Marts are independent consumers of the Enterprise Data Warehouse. Failures in one Data Mart should not impact others.

---

### Does every company need Data Marts?

No.

Small organizations often work effectively with only a Data Warehouse. Data Marts become valuable as the number of departments, users, and analytical workloads grows.

---

# Key Takeaways

- A Data Mart is a **subject-oriented subset** of a Data Warehouse.
- It improves performance, security, governance, and usability.
- Enterprise KPIs belong in the Data Warehouse to maintain **SSOT**.
- Department-specific metrics belong in the corresponding Data Mart.
- Independent Data Marts reduce the blast radius of failures and simplify analytics.
