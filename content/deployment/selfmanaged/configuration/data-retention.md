---
title: Data retention policies
weight: 7
variants: -flyte +union
description: Implications of object storage retention or lifecycle policies on the default bucket and metadata.
---

# Data retention policies

{{< key product_name >}} relies on object storage for both **metadata** and **raw data** (your data that is passing through the workflow). Bucket-level retention and lifecycle policies (such as S3 lifecycle rules) that affect the metadata store can cause execution failures, broken history, and data loss.

## How {{< key product_name >}} uses the default bucket

The platform uses a **default object store bucket** in the data plane for two distinct purposes:

1. **Metadata store** — Task **inputs and outputs** passed between tasks at runtime, serialized as Protobuf literal messages. For primitive types (ints, strings, etc.) the literal carries the value directly; for offloaded types (`FlyteFile`, `FlyteDirectory`, `DataFrame`, etc.) it carries a pointer into the raw data store. The execution engine reads and writes these literals to pass results from one task to the next, and the UI reads them to render input/output values for both in-progress and historical runs.

   > [!NOTE] What "metadata" does *not* mean here
   > "Metadata" in this section refers strictly to data stored in the object store bucket — primarily task-to-task input/output literals and the {{< key product_name >}}-internal manifests that reference them. It does **not** refer to control plane database state (workflow and task registrations, execution status, schedules, audit history). That information lives in a separate relational database and is not affected by object-store retention policies.

2. **Raw data store** — The actual bytes of offloaded data types (`FlyteFile`, `FlyteDirectory`, `DataFrame` payloads, checkpoints, and similar large objects). The metadata store holds pointers to these blobs; the bytes themselves live here.

Because the **default bucket contains the metadata store**, it must be treated as **durable storage**. Retention or lifecycle policies that delete or overwrite objects in this bucket are **not supported** and can lead to data loss and system failure. There is **no supported way** to recover from metadata loss.

## Impact of metadata loss

| Area | Impact |
|------|--------|
| **UI and APIs** | Input/output previews may fail to load with "resource not found." Detail views may render incompletely where literals are missing. (The execution list itself is served from the control plane database and is unaffected.) |
| **Execution engine** | In-flight or downstream tasks that depend on a node's output can fail. Retry state may be lost. |
| **Caching** | Pointers to cached outputs may be lost, resulting in cache misses; tasks may re-run or fail. |
| **Traces** | [Trace](../../../user-guide/task-programming/traces) checkpoint data (used by `@flyte.trace` for fine-grained recovery from system failures) may be lost, preventing resume-from-checkpoint. |
| **Data** | Raw blobs may still exist, but without the literals that point to them the system can no longer resolve them. That data becomes **orphaned**. Downstream tasks that consume outputs by reference will fail at runtime. |
| **Operations** | The record of what each task actually produced — input/output values, deck data, artifact payloads — is lost. (The control plane audit log of *what ran when* is separate and unaffected.) |

## Retention on a separate raw-data location

If you separate raw data from metadata, you can apply retention policies **only to the raw data location** while keeping metadata durable. This is the only supported approach for applying retention. You can do this either by configuring separate buckets using `configuration.storage.metadataContainer` and `configuration.storage.userDataContainer` in the [data plane chart](https://github.com/unionai/helm-charts/blob/master/charts/dataplane/values.yaml), or by using a metadata prefix within the same bucket (see [Customizing the metadata path](#customizing-the-metadata-path) below).

Be aware of the trade-offs:

- **Historical executions** that reference purged raw data will fail.
- **Cached task outputs** stored as raw data will be lost, causing cache misses and task re-execution.
- **Trace checkpoints** stored in the raw-data location will be purged, preventing resume-from-checkpoint for affected executions.

Data correctness is not silently violated, but the benefits of caching and trace-based recovery are lost for purged data.

## Customizing the metadata path

> [!NOTE] Scope
> The Helm chart settings below apply to **self-managed** deployments where you operate the data plane chart directly. BYOC customers cannot set these values themselves; for per-run customization of the metadata or raw data location on BYOC, see [Per-run customization](#per-run-customization) below.

You can control where metadata is stored within the bucket via the **`config.core.propeller.metadata-prefix`** setting (e.g. `metadata/propeller` in the [data plane chart values](https://github.com/unionai/helm-charts/blob/master/charts/dataplane/values.yaml)). This lets you design lifecycle rules that **exclude** the metadata prefix (for example, in S3 lifecycle rules, apply expiration only to prefixes that do not include the metadata path) so that only non-metadata paths are subject to retention.

Confirm the exact prefix and bucket layout for your deployment from the chart configuration, and validate any retention rules in a non-production environment before applying them broadly.

## Per-run customization

Regardless of deployment type, both the metadata location and the raw data location can be overridden **per run** via [`flyte.with_runcontext()`](../../../user-guide/task-deployment/run-context#storage):

- `run_base_dir` — base directory for run metadata (inputs/outputs passed between tasks).
- `raw_data_path` — storage prefix for offloaded data (`FlyteFile`, `FlyteDirectory`, `DataFrame`, checkpoints).

The same parameters can be set per trigger. Setting a deployment-wide default for these paths on BYOC is not currently supported.
