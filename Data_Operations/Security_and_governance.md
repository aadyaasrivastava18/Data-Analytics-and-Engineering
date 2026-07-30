# Security & Governance

> **Goal:** Build secure, compliant, and trustworthy data platforms that protect sensitive information while enabling authorized users to access the data they need.

---

# Why Security & Governance Matter

Imagine your company stores millions of customer records.

Each record contains:

- Customer Name
- Email
- Phone Number
- Credit Card Number
- Purchase History

Now imagine:

- An intern accidentally downloads all customer data.
- A hacker gains access to the warehouse.
- A dashboard displays incorrect revenue.
- A customer requests deletion of their personal data.
- An executive asks where a KPI originated.

Security and Governance ensure that data is:

- Protected
- Trusted
- Traceable
- Compliant
- Accessible only to the right people

---

# Security vs Governance

| Security | Governance |
|-----------|------------|
| Protects data from unauthorized access | Ensures data is managed correctly |
| Focuses on confidentiality, integrity, availability | Focuses on quality, ownership, compliance and lifecycle |
| Answers **"Who can access this?"** | Answers **"Can we trust and manage this data?"** |

---

# 1. Principle of Least Privilege (PoLP)

## Definition

Every user, service, or application should receive **only the minimum permissions required** to perform its job.

Never give more access than necessary.

---

## Example

Customer table

| Column |
|---------|
| Customer_ID |
| Name |
| Email |
| Credit Card |
| Revenue |

### Marketing Analyst

Needs:

- Customer_ID
- Revenue

Should NOT access:

- Credit Card
- Email

---

## Why?

Giving unnecessary permissions increases:

- Data leaks
- Insider threats
- Compliance violations
- Attack surface
- Operational risk

---

## Interview Tip

> Give minimum permissions by default and increase access only when justified.

---

# 2. Role-Based Access Control (RBAC)

## Definition

Permissions are assigned to **roles**, not individual users.

Users inherit permissions from their assigned role.

---

## Example

```text
Marketing Analyst
        │
        ├── Revenue Dashboard
        ├── Campaign Metrics
        └── Customer Segments

Finance Manager
        │
        ├── Financial Reports
        └── Revenue Tables

Software Engineer
        │
        ├── Source Code
        └── Deployment Pipelines
```

Instead of configuring hundreds of employees individually, configure the role once.

---

## Benefits

- Easier onboarding
- Easier offboarding
- Consistent permissions
- Scalable administration

---

# 3. Attribute-Based Access Control (ABAC)

## Definition

Access is determined using attributes instead of only roles.

Possible attributes include:

- Role
- Department
- Location
- Time
- Device
- Data Classification

---

## Example

Allow access only if:

- Role = Data Analyst
- Department = Finance
- Location = India
- Time = 9 AM – 6 PM

If any condition fails, access is denied.

---

## RBAC vs ABAC

| RBAC | ABAC |
|------|------|
| Role-based | Attribute-based |
| Simple | Fine-grained |
| Easier to manage | More flexible |
| Best for straightforward systems | Best for enterprise-scale security |

---

## Interview Tip

Many organizations combine RBAC and ABAC for scalable and context-aware access control.

---

# 4. Authentication vs Authorization

| Authentication | Authorization |
|---------------|---------------|
| Verifies identity | Determines permissions |
| "Who are you?" | "What can you do?" |
| Login | Access Control |

---

Example:

```
Login
      │
      ▼
Authentication

      │
      ▼
Authorization

      │
      ▼
Access Granted
```

---

# 5. Encryption

## Definition

Encryption converts readable data into unreadable ciphertext using cryptographic keys.

Only someone with the correct key can recover the original data.

---

## Encryption at Rest

Protects stored data.

Examples:

- Database
- Data Warehouse
- Cloud Storage
- Backup Files

---

## Encryption in Transit

Protects data while moving across networks.

Examples:

- HTTPS
- TLS
- Secure APIs

---

## Why?

Even if storage devices or network traffic are compromised, attackers cannot read encrypted data.

---

# 6. Hashing

## Definition

Hashing converts data into a fixed-length value.

Unlike encryption, hashing is **one-way**.

Original value cannot be recovered.

---

## Example

Passwords

```
Password

↓

Hash

↓

Store Hash
```

Never store passwords as plain text.

---

## Salt

A random value added before hashing.

Purpose:

- Prevent rainbow table attacks
- Ensure identical passwords generate different hashes

---

# Encryption vs Hashing vs Encoding

| Encoding | Encryption | Hashing |
|-----------|------------|----------|
| Data representation | Protect confidentiality | Verify integrity / store passwords |
| Reversible | Reversible with key | One-way |
| Base64 | AES, RSA | SHA-256, bcrypt |

---

# 7. Data Minimization

## Definition

Collect and expose only the data necessary for a specific purpose.

---

Example:

ML model only needs:

- Customer_ID
- Revenue

Do NOT expose:

- Credit Card
- Email
- Phone Number

---

## Benefits

- Better privacy
- Reduced compliance risk
- Smaller attack surface

---

# 8. Data Masking

## Definition

Hide part of sensitive information while preserving readability.

Example

```
4111111111111234

↓

**** **** **** 1234
```

Used for:

- Dashboards
- Customer Support
- Reporting

---

# 9. Tokenization

## Definition

Replace sensitive values with meaningless tokens.

```
Customer_ID

↓

TK_98F2AB
```

Only a secure mapping system can recover the original value.

---

## Masking vs Tokenization

| Masking | Tokenization |
|----------|--------------|
| Partially hides data | Completely replaces data |
| Human readable | Meaningless token |
| Often reversible visually | Requires secure mapping |

---

# 10. Data Lineage

## Definition

Data Lineage tracks the journey of data from its source to its final destination.

---

Example

```text
CRM Database
      │
      ▼
Raw Orders
      │
      ▼
Cleaning
      │
      ▼
Business Logic
      │
      ▼
Warehouse
      │
      ▼
Dashboard
```

---

## Why?

- Root cause analysis
- Impact analysis
- Compliance
- Debugging
- Trust

---

## Example

Dashboard shows:

Revenue = ₹52 Million

Lineage helps answer:

- Which source produced this number?
- Which transformations were applied?
- Which pipeline generated it?

---

# 11. Data Catalog

## Definition

A centralized inventory of datasets and metadata.

Think of it as **Google Search for your organization's data assets.**

---

Example

Search:

```
Customer_Transactions
```

Returns:

- Owner
- Description
- Schema
- Refresh Frequency
- Certification
- Data Classification
- Lineage
- Downstream Dashboards

---

## Benefits

- Faster data discovery
- Better collaboration
- Reduced tribal knowledge
- Easier onboarding

---

# Data Catalog vs Data Lineage

| Data Catalog | Data Lineage |
|---------------|--------------|
| Finds datasets | Traces data flow |
| Stores metadata | Stores relationships |
| Discovery | Debugging & Impact Analysis |

---

# 12. Data Classification

## Definition

Categorize data according to its sensitivity.

Different categories require different security controls.

---

Example

| Classification | Example |
|---------------|----------|
| Public | Company Website |
| Internal | Operational Dashboards |
| Confidential | Customer Emails |
| Restricted | Credit Card Numbers |

---

## Why?

Not all datasets require the same level of protection.

Higher sensitivity requires stronger controls.

Examples:

- Encryption
- RBAC
- ABAC
- Tokenization
- Audit Logging

---

# 13. Audit Logs

## Definition

Audit Logs record every important action performed on data.

They answer:

- Who?
- What?
- When?
- Where?
- Was it successful?

---

Example

```
Time: 09:15

User:
alice@company.com

Action:
SELECT

Table:
Customer_Payment

Status:
Success
```

---

## Why?

- Security investigations
- Compliance
- Accountability
- Incident response

---

## Best Practices

Audit logs should be:

- Immutable
- Tamper-resistant
- Timestamped
- Retained according to policy

---

# 14. Data Retention

## Definition

A Data Retention Policy defines:

- How long data is stored
- When it is archived
- When it is deleted

---

Example

| Data | Retention |
|------|-----------|
| Logs | 90 Days |
| Transactions | 7 Years |
| Support Chats | 2 Years |
| Temporary Files | 30 Days |

---

## Why?

- Reduce storage costs
- Meet legal obligations
- Reduce security risks
- Ensure consistent lifecycle management

---

## Interview Tip

Data should **not** be retained forever or deleted arbitrarily. Retention should follow business, legal, and regulatory requirements.

---

# 15. Compliance

## Definition

Compliance ensures that data handling follows legal, regulatory, and organizational requirements.

Examples include:

- GDPR
- CCPA

---

## Common Requirements

- Obtain consent where required
- Protect personal data
- Support access requests
- Support deletion requests (where legally applicable)
- Retain required records for mandated periods
- Maintain audit trails

---

## Role of a Data Engineer

A Data Engineer enables compliance by building systems that support:

- Secure storage
- Access controls
- Encryption
- Audit logging
- Data lineage
- Data catalogs
- Retention policies
- Automated deletion workflows

---

# Production Workflow

```text
Collect Data
      │
      ▼
Classify Data
      │
      ▼
Grant Access (RBAC / ABAC)
      │
      ▼
Encrypt Sensitive Data
      │
      ▼
Mask / Tokenize PII
      │
      ▼
Track Lineage
      │
      ▼
Register in Data Catalog
      │
      ▼
Record Audit Logs
      │
      ▼
Apply Retention Policy
      │
      ▼
Comply with Regulations
```

---

# FAANG Interview Cheat Sheet

### Security

- Principle of Least Privilege
- RBAC
- ABAC
- Authentication vs Authorization
- Encryption
- Hashing
- Masking
- Tokenization

---

### Governance

- Data Lineage
- Data Catalog
- Data Classification
- Audit Logs
- Data Retention
- Compliance

---

# Key Takeaways

- Give users the minimum permissions necessary.
- Protect sensitive data using encryption, masking, and tokenization.
- Use RBAC and ABAC for scalable access control.
- Track where data comes from using Data Lineage.
- Make datasets discoverable using a Data Catalog.
- Classify data based on sensitivity.
- Maintain immutable audit logs for accountability.
- Define retention policies instead of keeping data indefinitely.
- Build systems that satisfy privacy and regulatory requirements.
- Strong governance creates trustworthy, secure, and scalable data platforms.
