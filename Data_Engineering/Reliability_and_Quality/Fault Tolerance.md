# Fault Tolerance

## Why Does This Exist?

Distributed systems are designed with the expectation that failures **will happen**. Hardware crashes, network outages, software bugs, and database failures are inevitable. Fault Tolerance ensures the system continues operating with minimal disruption by automatically detecting failures and recovering from them.

---

# Definition

> **Fault Tolerance is the ability of a system to continue operating correctly even when one or more of its components fail.**

**Goal:** Ensure **business continuity**, **high reliability**, and **minimal downtime**.

---

# Fault Tolerance at a Glance

| Aspect | Description |
|--------|-------------|
| Definition | Ability of a system to continue operating despite component failures. |
| Goal | Minimise downtime and maintain business continuity. |
| Focus | Automatic detection, recovery, and failover. |
| Prevents | Complete system outages caused by a single failure. |
| Common Techniques | Redundancy, Replication, Health Checks, Load Balancing, Failover, Retry, Idempotency. |

---

# Why is Fault Tolerance Important?

| Without Fault Tolerance | With Fault Tolerance |
|-------------------------|----------------------|
| Service outage | Service continues running |
| Revenue loss | Business continuity |
| Poor customer experience | Better user experience |
| SLA violations | Higher availability |
| Manual recovery | Automatic recovery |
| Single Point of Failure (SPOF) | Redundant components |

---

# Core Components

| Component | Purpose | Example |
|-----------|---------|---------|
| Failure Detection | Detect failed components | Heartbeats, Monitoring |
| Health Checks | Identify healthy servers | Ping every few seconds |
| Redundancy | Keep backup resources | Replica Database |
| Replication | Maintain multiple copies of data | Primary → Replica |
| Load Balancer | Distribute traffic | Nginx, AWS ALB |
| Failover | Switch to backup resource | Replica becomes Primary |
| Retry Strategy | Retry temporary failures | Network retry |
| Idempotency | Prevent duplicate processing | Payment processed once |

---

# Fault Tolerance Workflow

| Step | Action | Purpose |
|------|--------|---------|
| 1 | Component fails | Failure occurs |
| 2 | Health check detects failure | Identify unhealthy component |
| 3 | Remove component from pool | Prevent additional failures |
| 4 | Failover starts | Activate healthy backup |
| 5 | Load balancer redirects traffic | Maintain service availability |
| 6 | Retry failed requests | Recover transient failures |
| 7 | Idempotency validates requests | Prevent duplicate processing |
| 8 | Root cause analysis | Prevent future failures |

---

# Redundancy vs Replication vs Failover

| Feature | Redundancy | Replication | Failover |
|----------|------------|-------------|----------|
| Purpose | Backup resources | Copy data | Switch to backup |
| Trigger | Exists before failure | Continuous process | Happens after failure |
| Example | Backup Server | Replica Database | Replica becomes Primary |
| Business Benefit | Removes SPOF | Data availability | Service continuity |

---

# Load Balancing Example

| Server | CPU Usage | Available Capacity | Traffic Assigned |
|---------|----------:|-------------------:|-----------------:|
| Server A | 95% | 5% | Very Low |
| Server B | 20% | 80% | High |
| Server C | 15% | 85% | Highest |

> **Principle:** Traffic should be routed based on **server health and available capacity**, not necessarily equally.

---

# Active-Passive vs Active-Active

| Feature | Active-Passive | Active-Active |
|----------|----------------|---------------|
| Active Servers | One | Multiple |
| Backup Server | Idle | Active |
| Performance | Moderate | High |
| Scalability | Moderate | Excellent |
| Consistency | Easier | More Difficult |
| Cost | Lower | Higher |
| Complexity | Low | High |
| Best For | Banking, Payments | Streaming, Social Media |

---

# Health Check Decision Table

| Health Status | Load Balancer Action |
|---------------|----------------------|
| Healthy | Continue routing traffic |
| High CPU Usage | Reduce incoming requests |
| No Heartbeat | Mark server unhealthy |
| Server Crash | Remove from server pool |
| Server Recovered | Add back to pool |

---

# Common Failures & Recovery Mechanisms

| Failure | Recovery Mechanism |
|----------|--------------------|
| Server crash | Failover |
| Database failure | Replica Database |
| Network timeout | Retry Strategy |
| Duplicate request | Idempotency |
| High traffic | Load Balancer |
| Hardware failure | Redundancy |
| Data centre outage | Multi-region deployment |

---

# Fault Tolerance vs Related Concepts

| Concept | Focus | Key Question |
|---------|-------|--------------|
| Failure Handling | Detect and respond to failures | What failed? |
| Retry Strategy | Retry temporary failures | Should I retry? |
| Idempotency | Prevent duplicate effects | Has this already been processed? |
| Fault Tolerance | Continue operating during failures | How do I keep the system running? |
| High Availability | Reduce downtime | How quickly can I recover? |

---

# Real-World Examples

| Company/System | Fault Tolerance Technique |
|----------------|---------------------------|
| Google Search | Load Balancing + Replication |
| Amazon | Multi-AZ + Automatic Failover |
| Netflix | Active-Active + Auto Scaling |
| Banking Systems | Active-Passive + Idempotency |
| Apache Kafka | Partition Replication |
| Kubernetes | Health Checks + Self-Healing |

---

# Best Practices

| Practice | Benefit |
|----------|---------|
| Eliminate Single Points of Failure | Improves system reliability |
| Replicate critical data | Ensures data availability |
| Perform regular health checks | Detect failures early |
| Implement automatic failover | Minimise downtime |
| Use intelligent load balancing | Prevent server overload |
| Retry transient failures | Improve request success rate |
| Make operations idempotent | Prevent duplicate processing |
| Continuously monitor systems | Detect issues proactively |

---

# Common Mistakes

| Mistake | Impact |
|----------|--------|
| Single database/server | Single Point of Failure |
| No health checks | Slow failure detection |
| No redundancy | Complete service outage |
| Equal traffic distribution regardless of server health | Server overload |
| Missing retry mechanism | Temporary failures become permanent |
| No idempotency | Duplicate transactions |
| Lack of monitoring | Delayed incident response |

---

# Interview Cheat Sheet

| Question | Answer |
|----------|--------|
| What is Fault Tolerance? | Ability of a system to continue operating despite failures. |
| Why is Fault Tolerance important? | Ensures reliability, availability, and business continuity. |
| What is a Single Point of Failure (SPOF)? | A component whose failure can bring down the entire system. |
| What is Redundancy? | Maintaining backup resources for failures. |
| What is Replication? | Keeping multiple copies of the same data. |
| What is Failover? | Automatically switching to a healthy backup resource. |
| What are Health Checks? | Periodic checks to determine server health. |
| What does a Load Balancer do? | Distributes requests across healthy servers. |
| Active-Passive vs Active-Active? | Simplicity and consistency vs scalability and throughput. |
| How do Retry and Idempotency work together? | Retries recover failed requests while idempotency prevents duplicate processing. |

---

# Summary

Fault Tolerance is a system design principle that enables applications to remain operational despite failures. By combining **Redundancy**, **Replication**, **Health Checks**, **Load Balancing**, **Failover**, **Retry Strategies**, and **Idempotency**, modern distributed systems achieve high reliability, minimal downtime, and uninterrupted business operations.
