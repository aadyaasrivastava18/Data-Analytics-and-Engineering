# Data Sources

## Why does this exist?

Organizations generate data from different systems. An ingestion pipeline collects this data and moves it into a centralized storage system for analysis.

---

## Common Data Sources

| Source        | Examples                      | Typical Ingestion        |
| ------------- | ----------------------------- | ------------------------ |
| Databases     | MySQL, PostgreSQL             | Database Connector / CDC |
| APIs          | Payment APIs, Weather APIs    | HTTP/API Calls           |
| Files         | CSV, Excel, JSON, Parquet     | File Loader              |
| Event Streams | Website Clicks, Mobile Events | Streaming Pipeline       |
| Logs          | Application, Server Logs      | Log Ingestion            |
| IoT Devices   | Sensors, Smart Devices        | Streaming Pipeline       |

---

## Key Principle

Different data sources require different ingestion mechanisms because they differ in:

* Format
* Frequency
* Communication protocol

Despite these differences, they typically feed into the same centralised storage layer.

---

## Interview Takeaway

> Use **source-specific connectors** for data collection while maintaining a **common destination** such as a Data Lake or Data Warehouse.

---

## Revision Notes

* Multiple sources → One centralized storage.
* Different sources → Different ingestion methods.
* Common destination, source-specific connectors.
