---
title: Data retention policies
weight: 7
variants: -flyte -serverless -byoc +selfmanaged
description: Implications of object storage retention or lifecycle policies on the default bucket and metadata.
---

# Data retention policies

This document provides guidance for administrators and operators on the use of **bucket-level retention** and **lifecycle policies** (such as S3 lifecycle rules or cloud provider policies that automatically delete or transition objects) in relation to the object store used by {{< key product_name >}}. It explains how the platform uses storage, what happens when metadata or data is removed by such policies, and what configurations are supported.

## Overview

{{< key product_name >}} relies on object storage for both **metadata** and **workflow data**. Applying retention or lifecycle rules that delete or overwrite objects in the bucket used for metadata can cause execution failures, broken history, and data loss. This page describes the architecture, risks, and recommended practices so that retention policies can be configured safely where supported.

## How {{< key product_name >}} uses the default bucket

The platform uses a **default object store bucket** in the dataplane for two distinct purposes:

1. **Metadata store**  
   The system stores references, execution state, and pointers to task outputs in the object store. The control plane and the user interface use this metadata to schedule workflows, resolve task dependencies, display execution history, and resolve output locations. This data is required for the correct operation of the platform.

2. **Raw data store**  
   By default, large task inputs and outputs or complex types (for example `FlyteFile`, dataframes, etc) are also written to this bucket. The metadata store holds only pointers to these blobs; the actual bytes live in the raw data store.

You can use a separate S3-compliant bucket for each purpose, simplifying the design of retention policies.

Because the **default bucket contains the metadata store**, it must be treated as **durable storage**. Retention or lifecycle policies that delete or overwrite objects in this bucket are **not supported** and can lead to data loss and system failure.

## Risks of configuring retention on the default bucket

Configuring bucket-level retention (or any policy that deletes or overwrites objects) on the **entire** default bucket is **not safe**.

If such a policy removes objects from the default bucket:

- **Metadata** (references, execution state, and pointers to blobs) may be deleted.
- The system can no longer reliably resolve task outputs, reconstruct execution history, or run downstream tasks that depend on those outputs.
- The control plane and the UI depend on this metadata; without it, executions can fail and the interface may show errors or missing data.

Administrators should **not** apply retention or lifecycle rules that delete or overwrite objects to the default bucket. The default bucket should be retained for the lifetime of the deployment, or until data is migrated under a supported process.

## Impact of metadata loss

The following table summarizes the **concrete effects** of metadata loss (for example, due to a retention policy that deletes metadata objects).

| Area | Impact |
|------|--------|
| **UI and APIs** | Execution list or detail views may show errors or “resource not found.” Node-level status, timing, and output previews may fail to load (e.g. “failed to load output”). |
| **Execution engine** | In-flight or downstream tasks that depend on a node’s output can fail when resolving outputs from metadata. Retry state may be lost, leading to inconsistent or failed retries. |
| **Caching** | Cache metadata or pointers to cached outputs may be lost, resulting in cache misses or “failed to load cached output”; tasks may re-run or fail. |
| **Data** | Raw blobs may still exist in the bucket, but without metadata the system has no pointers to them. That data becomes **orphaned** and is no longer associated with any execution or node. Downstream tasks that consume outputs by reference will fail at runtime. |
| **Operations** | A reliable record of what ran, when, and what the declared outputs were is lost; debugging and audit trails are compromised. |

There is **no supported way** to recover from metadata loss caused by retention policies. The system assumes that metadata in the default bucket is durable and not subject to automatic deletion.

## Task caching and retention

When **task caching** is enabled, task outputs are stored in the raw data store and referenced via metadata. Two cases are relevant:

- **Retention on the default bucket**  
  Retention that affects the default bucket (and thus the metadata store) remains **unsafe**. The primary risk is metadata loss; caching does not change this. Retention must not be applied to the default bucket.

- **Retention only on a separate raw-data location**  
  If retention is applied **only** to a separate bucket or prefix used exclusively for raw data (with metadata left intact), then:
  - Cached task outputs are stored as raw data. If retention deletes those blobs, a subsequent “cache hit” may attempt to load an output that no longer exists.
  - The result is **cache misses** and task **re-execution**. Data correctness is not silently violated, but the **benefit of caching is lost** for purged data.

Administrators who configure retention on a separate raw-data location should expect that historical executions that reference purged data may fail, and that cached results may be invalidated for that data.

## Flyte V2 and Traces

In **Flyte V2**, the **Traces** feature provides fine-grained observability and checkpointing within a task. Functions decorated with `@trace` have their inputs and outputs checkpointed so that execution can resume from the last successful checkpoint on failure, and so that non-deterministic behavior can be observed and recovered.

Trace checkpoints are stored in the same object store used for execution data (the default bucket or the configured raw-data location, depending on deployment). Therefore:

- **Retention on the default bucket** remains **unsafe**. If the bucket holds metadata or pointers to trace checkpoints, deleting objects can remove that metadata or the checkpoint blobs themselves. Trace-based recovery will then fail (e.g. “checkpoint not found” or “failed to load trace”), and tasks may need to re-run from the start instead of resuming from a checkpoint.
- **Retention only on a separate raw-data location** that holds trace checkpoint blobs has the same trade-off as for cached outputs: purged checkpoints invalidate trace-based recovery for those executions. Affected runs will not be able to resume from a checkpoint and may re-execute from the beginning.

The same retention guidance applies: do not apply retention to the default bucket; if retention is applied to a separate raw-data store, understand that trace checkpoints there may be deleted and recovery from those checkpoints will no longer be possible.

## Recommendations

| Configuration | Supported? | Guidance |
|---------------|------------|----------|
| **Retention on the default bucket** (metadata and default raw data) | **No** | Do not configure bucket-level retention or lifecycle policies that delete or overwrite objects on the default bucket. This can cause metadata loss and execution failures. |
| **Retention only on a separate raw-data bucket or prefix** (e.g. via raw data prefix or output location) | **Use with care** | Metadata is unaffected. However, deleting raw data can break historical executions that still reference it and can invalidate cached outputs. Use only if re-execution and possible failures for old or cached data are acceptable. |


## Customizing the metadata path

You can control where metadata is stored within the bucket via the **`config.core.propeller.metadata-prefix`** setting (e.g. `metadata/propeller` in the [dataplane chart values](https://github.com/unionai/helm-charts/blob/master/charts/dataplane/values.yaml)). This prefix defines the path under which the backend writes metadata in the bucket. When planning retention policies, you can design lifecycle rules that **exclude** this metadata prefix (for example, in S3 lifecycle rules, apply expiration only to prefixes that do not include the metadata path). That way, only non-metadata paths (such as raw output) are subject to retention, and the metadata store remains durable. Confirm the exact prefix and bucket layout for your deployment from the chart configuration or documentation, and validate any retention rules in a non-production environment before applying them broadly.


## Summary

- The **default bucket** holds the metadata store and, by default, raw data. It must **not** be subject to retention or lifecycle policies that delete or overwrite objects.
- **Metadata loss** (e.g. from such policies) can cause execution failures, broken UI and APIs, unresolvable outputs, and orphaned blobs; recovery is not supported.
- **Task caching** does not change the requirement to keep the default bucket durable; retention on a separate raw-data location may invalidate cache entries and cause re-runs or errors.
- **Flyte V2 Traces** (checkpointing) store checkpoint data in the same object store; the same retention rules apply. Retention on the default bucket can break trace-based recovery; retention on a separate raw-data location can invalidate checkpoint blobs and prevent resume-from-checkpoint.
- {{< variant selfmanaged >}} **Self-managed** deployments can use `config.core.propeller.metadata-prefix` to isolate metadata in the bucket and design retention to exclude that path (see [Configuration](#configuration) above). {{< /variant >}}
- Administrators should keep the default bucket durable. If retention is required, it should be limited to a **separate** raw-data bucket or prefix, with full understanding of the impact on historical runs, caching, and (in Flyte V2) trace checkpoints.
