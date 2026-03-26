---
title: Data retention policies
weight: 7
variants: -flyte -byoc +selfmanaged
description: Implications of object storage retention or lifecycle policies on the default bucket and metadata.
---

# Data retention policies

{{< key product_name >}} relies on object storage for both **metadata** and **raw data** (your data that is passing through the workflow). Bucket-level retention and lifecycle policies (such as S3 lifecycle rules) that affect the metadata store can cause execution failures, broken history, and data loss.

## How {{< key product_name >}} uses the default bucket

The platform uses a **default object store bucket** in the data plane for two distinct purposes:

1. **Metadata store** — References, execution state, and pointers to task outputs. The control plane and UI use this metadata to schedule workflows, resolve task dependencies, display execution history, and resolve output locations. This data is required for the correct operation of the platform.

2. **Raw data store** — Large task inputs and outputs or complex types (for example `FlyteFile`, dataframes, etc.). The metadata store holds only pointers to these blobs; the actual bytes live in the raw data store.

Because the **default bucket contains the metadata store**, it must be treated as **durable storage**. Retention or lifecycle policies that delete or overwrite objects in this bucket are **not supported** and can lead to data loss and system failure. There is **no supported way** to recover from metadata loss.

## Impact of metadata loss

| Area | Impact |
|------|--------|
| **UI and APIs** | Execution list or detail views may show errors or "resource not found." Output previews may fail to load. |
| **Execution engine** | In-flight or downstream tasks that depend on a node's output can fail. Retry state may be lost. |
| **Caching** | Pointers to cached outputs may be lost, resulting in cache misses; tasks may re-run or fail. |
| **Traces** | [Trace](../../user-guide/task-programming/traces) checkpoint data (used by `@flyte.trace` for fine-grained recovery from system failures) may be lost, preventing resume-from-checkpoint. |
| **Data** | Raw blobs may still exist, but without metadata the system has no pointers to them. That data becomes **orphaned**. Downstream tasks that consume outputs by reference will fail at runtime. |
| **Operations** | Audit trails and the record of what ran, when, and with what outputs are lost. |

## Retention on a separate raw-data location

If you separate raw data from metadata, you can apply retention policies **only to the raw data location** while keeping metadata durable. This is the only supported approach for applying retention. You can do this either by configuring separate buckets using `configuration.storage.metadataContainer` and `configuration.storage.userDataContainer` in the [data plane chart](https://github.com/unionai/helm-charts/blob/master/charts/dataplane/values.yaml), or by using a metadata prefix within the same bucket (see [Customizing the metadata path](#customizing-the-metadata-path) below).

Be aware of the trade-offs:

- **Historical executions** that reference purged raw data will fail.
- **Cached task outputs** stored as raw data will be lost, causing cache misses and task re-execution.
- **Trace checkpoints** stored in the raw-data location will be purged, preventing resume-from-checkpoint for affected executions.

Data correctness is not silently violated, but the benefits of caching and trace-based recovery are lost for purged data.

## Customizing the metadata path

You can control where metadata is stored within the bucket via the **`config.core.propeller.metadata-prefix`** setting (e.g. `metadata/propeller` in the [data plane chart values](https://github.com/unionai/helm-charts/blob/master/charts/dataplane/values.yaml)). This lets you design lifecycle rules that **exclude** the metadata prefix (for example, in S3 lifecycle rules, apply expiration only to prefixes that do not include the metadata path) so that only non-metadata paths are subject to retention.

Confirm the exact prefix and bucket layout for your deployment from the chart configuration, and validate any retention rules in a non-production environment before applying them broadly.
