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
# 📄 Data_Ingestion_Interview_Questions.md

# Data Ingestion – Interview Questions

---

## 14. What is Data Ingestion?

**Answer**

Data Ingestion is the process of collecting data from one or more source systems and moving it into a central storage or processing platform, such as a Data Lake or Data Warehouse. It enables organisations to consolidate data for analytics, reporting, machine learning, and operational workflows.

---

## 15. How would you ingest data from multiple sources into a single Data Warehouse?

**Answer**

Design a dedicated ingestion pipeline for each source based on how the data is generated. Load the data into a common landing zone or Data Lake before making it available in the Data Warehouse. Choose the ingestion strategy according to the characteristics of each source (Batch, Streaming, or CDC).

---

## 16. How do you decide between Batch and Streaming Ingestion?

**Answer**

The choice depends on business latency requirements.

* **Batch Ingestion** is suitable when data can be processed periodically (hourly, daily, weekly).
* **Streaming Ingestion** is used when data must be available with minimal latency for real-time analytics, monitoring, or operational decisions.

---

## 17. Your application generates millions of events every second. Would you choose Batch or Streaming?

**Answer**

Streaming Ingestion is the preferred choice because it processes events continuously with low latency. Batch processing would delay data availability, slowing dashboards, monitoring, fraud detection, and other real-time business operations.

---

## 18. You need to migrate 10 TB of historical data into a new Data Warehouse. After migration, only new transactions need to be synchronised. How would you design the ingestion pipeline?

**Answer**

Perform a one-time Batch Ingestion to migrate the historical dataset. After the initial load, switch to incremental ingestion using CDC so that only new or modified records are synchronised, reducing unnecessary data movement and processing costs.

---

## 19. A database contains 500 million records, but only 2,000 change each day. Why is Batch Ingestion a poor choice?

**Answer**

Batch Ingestion would repeatedly scan and process the entire dataset to capture a very small number of changes. This wastes compute resources, network bandwidth, storage I/O, and increases ingestion time.

---

## 20. Why is Change Data Capture (CDC) the preferred solution?

**Answer**

CDC captures only inserts, updates, and deletes from the source database. Instead of reprocessing the full dataset, it ingests only changed records, making the pipeline significantly more efficient and scalable.

---

## 21. How does CDC reduce cost and improve performance?

**Answer**

By processing only changed records, CDC reduces data movement, CPU utilisation, storage I/O, and network traffic. This lowers infrastructure costs while keeping downstream systems synchronised with minimal latency.

---

## 22. Can CDC replace Batch Ingestion?

**Answer**

No. Batch Ingestion is still required for initial historical loads and large-scale migrations. CDC complements Batch by efficiently synchronising incremental changes after the initial load.

---

## 23. Does Data Ingestion always transform data?

**Answer**

No. Data Ingestion focuses on collecting and moving data from source systems to a destination. Data transformation is typically performed later as part of ETL or ELT pipelines.

---

## 24. What factors influence the choice of an ingestion strategy?

**Answer**

The ingestion strategy depends on:

* Business latency requirements
* Data volume
* Frequency of data changes
* Source system capabilities
* Cost and infrastructure constraints
* Reliability and scalability requirements

---

## 25. Explain an end-to-end Data Ingestion pipeline.

**Answer**

**Source Systems → Ingestion Pipeline → Landing Zone / Data Lake → Data Warehouse → Analytics, Reporting, Machine Learning, or Business Applications**

---
# 📄 Data_Ingestion_Interview_Questions_2.md

# Data Ingestion – Advanced Interview Questions

---

## 26. A daily Batch Ingestion pipeline runs at midnight. The CEO wants dashboards to refresh every 5 minutes. How would you redesign the architecture?

**Answer**

Start by understanding which datasets actually require a 5-minute refresh. Rather than replacing the entire Batch pipeline, design a hybrid architecture where business-critical datasets use Streaming Ingestion while non-time-sensitive workloads continue using Batch Ingestion. This balances latency requirements with infrastructure cost and operational complexity.

---

## 27. The CEO insists that every dashboard must refresh every 5 minutes. Would you convert the entire platform to Streaming?

**Answer**

Not immediately. First, define latency SLAs for each dataset by working with business stakeholders. Many datasets, such as payroll, finance, or compliance reports, do not require real-time updates. Converting every pipeline to Streaming increases infrastructure cost, monitoring complexity, and operational overhead. A hybrid architecture usually provides the best balance between business value and engineering cost.

---

## 28. A 100 GB CSV Batch Ingestion job fails after loading 80 GB. What problems can this create?

**Answer**

A partial load can result in incomplete reports, inconsistent analytics, duplicate records after retries, and corrupted business metrics. Users may make incorrect decisions if the Data Warehouse contains partially loaded data.

---

## 29. How would you design the pipeline so it doesn't restart from 0 GB after a failure?

**Answer**

Implement checkpointing so the pipeline periodically records its progress. If a failure occurs, the pipeline resumes from the last successful checkpoint instead of restarting the entire ingestion job, reducing recovery time and compute cost.

---

## 30. How would you ensure the Data Warehouse never contains partial or corrupted data?

**Answer**

Load the data into a staging table first, perform validation and quality checks, and only commit the data to the production Data Warehouse after the entire load succeeds. If validation fails, roll back the transaction so incomplete data is never exposed to downstream users.

---
