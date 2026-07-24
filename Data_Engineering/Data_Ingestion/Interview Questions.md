# Interview Questions

---

## 1. Why do we need a Message Queue?

**Answer**

A Message Queue decouples producers from consumers by buffering messages between them. It absorbs traffic spikes, prevents producer-consumer bottlenecks, and enables scalable, asynchronous communication without data loss.

---

## 2. What is a Producer?

**Answer**

A Producer is a service that publishes events or messages to a messaging system such as Kafka or Google Pub/Sub.

---

## 3. What is a Consumer?

**Answer**

A Consumer reads messages from the queue, executes business logic, and writes the processed data to downstream systems such as Data Warehouses, dashboards, or other services.

---

## 4. What is a Consumer Group?

**Answer**

A Consumer Group is a collection of consumers that process messages from the same topic in parallel. Within a consumer group, each partition is assigned to only one consumer at a time.

---

## 5. Why are Partitions required?

**Answer**

Partitions divide a topic into multiple ordered streams, enabling parallel processing while preserving message order within each partition.

---

## 6. A Topic has 5 Partitions and 8 Consumers. What happens?

**Answer**

Only five consumers actively process messages because each partition can be assigned to only one consumer within a consumer group. The remaining three consumers remain idle until partitions become available.

---

## 7. Does increasing Partitions always increase throughput?

**Answer**

No. Increasing partitions increases the maximum available parallelism, but overall throughput is still limited by downstream bottlenecks such as consumer processing speed, CPU, network bandwidth, or Data Warehouse capacity.

---

## 8. What happens if a Consumer crashes?

**Answer**

Kafka detects the failure and performs a rebalance, automatically reassigning the failed consumer's partitions to the remaining consumers in the same consumer group.

---

## 9. What is an Offset?

**Answer**

An Offset is the unique position of a message within a Kafka partition. Consumers commit offsets after successful processing so Kafka can resume from the correct position after failures.

---

## 10. A Consumer processes Offset 156 but crashes before committing it. What happens?

**Answer**

Kafka resumes from Offset 156 because it was never committed. The message is processed again, resulting in duplicate processing. This follows the At-least-once delivery model and relies on idempotency to safely handle duplicates.

---

## 11. Explain the Delivery Guarantees.

**Answer**

* **At-most-once:** Messages may be lost but are never processed twice.
* **At-least-once:** Messages are never lost but may be processed more than once.
* **Exactly-once:** Messages are processed exactly once without duplicates or data loss.

---

## 12. Kafka vs Google Pub/Sub

**Answer**

Kafka provides full control over infrastructure and is suitable for custom streaming platforms. Google Pub/Sub is a fully managed messaging service that reduces operational overhead and is ideal for GCP-native applications.

---

## 13. Explain the end-to-end flow of a message.

**Answer**

Application → Producer → Kafka Topic → Partition → Consumer Group → Consumer → Offset Commit → Data Lake/Data Warehouse → Analytics Dashboard

---

## Quick Revision

* Producer vs Consumer
* Producer–Consumer mismatch
* Message Queue
* Consumer Group
* Partitions
* Rebalancing
* Offsets
* Delivery Guarantees
* Kafka vs Pub/Sub
* End-to-End Architecture
