# Message Queues

## Why does this exist?

Modern applications often generate data faster than downstream systems can process it. Direct communication between producers and consumers can lead to bottlenecks, system failures, and data loss.

A message queue acts as an intermediary that decouples producers from consumers, allowing both systems to operate independently while ensuring reliable message delivery.

---

## Problem it Solves

Consider an e-commerce platform during a flash sale.

* Producers generate **100,000 orders per second**.
* The data warehouse can process only **20,000 orders per second**.

Without a message queue:

* Producers overwhelm consumers.
* Requests timeout or fail.
* Messages may be lost.
* Downstream systems become unstable.

With a message queue:

```text
Producers
     │
     ▼
Message Queue
     │
     ▼
Consumers
```

The queue temporarily stores incoming messages and allows consumers to process them at their own pace.

---

## What is a Message Queue?

> **A Message Queue is a middleware component that stores messages between producers and consumers, enabling asynchronous, reliable, and scalable communication between distributed systems.**

Instead of communicating directly, applications exchange data through the queue.

---

# How it Works

```text
Application
      │
      ▼
Producer
      │
      ▼
Message Queue (Kafka / Pub/Sub)
      │
      ▼
Consumer Group
      │
      ▼
Data Lake / Data Warehouse
```

### Producer

A producer publishes messages to the queue.

Example:

* Ad Click
* Order Created
* Payment Completed

---

### Consumer

A consumer reads messages from the queue and performs downstream processing such as:

* Writing to a Data Warehouse
* Updating dashboards
* Triggering notifications
* Running analytics pipelines

---

## Key Concepts

### 1. Consumer Groups

A **Consumer Group** is a collection of consumers that process messages from the same topic in parallel.

Characteristics:

* Each message is processed by only one consumer within the group.
* Consumers share the workload.
* Enables horizontal scaling.

Example:

```text
Topic
 │
 ├── Consumer A
 ├── Consumer B
 └── Consumer C
```

---

### 2. Partitions

A topic is divided into multiple **Partitions**.

Each partition:

* Preserves message order.
* Can be assigned to only one consumer within a consumer group.
* Enables parallel processing.

Example:

```text
Topic

Partition 0 → Consumer A

Partition 1 → Consumer B

Partition 2 → Consumer C
```

**Important Rule**

> The maximum parallelism of a consumer group is limited by the number of partitions.

For example:

| Partitions | Consumers | Active Consumers |
| ---------- | --------: | ---------------: |
| 4          |         2 |                2 |
| 4          |         4 |                4 |
| 4          |         6 |                4 |

---

### 3. Rebalancing

If a consumer joins or leaves the consumer group, the messaging system redistributes partitions among the available consumers.

Example:

```text
Before Failure

P0 → C1
P1 → C2
P2 → C3

After C2 Fails

P0 → C1
P1 → C1
P2 → C3
```

Rebalancing provides fault tolerance without manual intervention.

---

### 4. Offsets

Every message within a partition is assigned a unique **Offset**.

Consumers commit offsets after successfully processing messages.

Example:

```text
Offset 0 → Order 101

Offset 1 → Order 102

Offset 2 → Order 103

Offset 3 → Order 104
```

If the last committed offset is **2**, the consumer resumes processing from **Offset 3** after recovery.

Offsets allow consumers to:

* Resume after failures
* Track processing progress
* Prevent unnecessary reprocessing

---

### 5. Delivery Guarantees

Different applications require different reliability guarantees.

| Guarantee     | Data Loss | Duplicate Processing |
| ------------- | --------- | -------------------- |
| At-most-once  | Possible  | No                   |
| At-least-once | No        | Possible             |
| Exactly-once  | No        | No                   |

Most production systems prefer **At-least-once** delivery and rely on **Idempotency** to safely handle duplicate messages.

---

## Kafka vs Google Pub/Sub

| Kafka                                   | Google Pub/Sub                       |
| --------------------------------------- | ------------------------------------ |
| Self-managed                            | Fully managed                        |
| Full infrastructure control             | Google manages infrastructure        |
| Higher operational overhead             | Minimal operational effort           |
| Suitable for custom streaming platforms | Suitable for GCP-native applications |

**Choose Kafka when:**

* Fine-grained control is required.
* Building a custom streaming platform.
* Operating across multiple cloud providers or on-premises environments.

**Choose Pub/Sub when:**

* Running on Google Cloud.
* Infrastructure management should be minimized.
* Faster development is prioritized over operational control.

---

## Real-World Example

A user clicks an advertisement.

```text
User Click
     │
     ▼
Producer
     │
     ▼
Kafka Topic
     │
     ▼
Partition
     │
     ▼
Consumer Group
     │
     ▼
BigQuery
     │
     ▼
Looker Dashboard
```

If consumer traffic increases, additional consumers can be added to the consumer group. If a consumer fails, Kafka automatically rebalances partitions and processing continues from the last committed offset.

---

## Interview Explanation

A Message Queue improves scalability and reliability by decoupling producers from consumers.

Key interview points:

* Producers and consumers operate independently.
* Consumer Groups enable parallel processing.
* Partitions determine the maximum parallelism.
* Offsets enable recovery after failures.
* Rebalancing provides fault tolerance.
* Delivery guarantees determine the trade-off between duplicates and data loss.

---

## Common Mistakes

* Confusing a Topic with a Partition.
* Assuming every consumer receives every message.
* Believing additional consumers always improve throughput.
* Forgetting that offsets are maintained per partition.
* Ignoring the relationship between delivery guarantees and idempotency.

---

## Key Takeaways

* Message queues decouple producers and consumers.
* Consumer Groups provide horizontal scalability.
* Partitions enable parallel processing.
* Offsets track message processing progress.
* Rebalancing ensures resilience during consumer failures.
* Delivery guarantees define reliability and consistency trade-offs.
