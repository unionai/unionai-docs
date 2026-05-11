---
title: Data retention policies
weight: 7
variants: -flyte +union
description: Implications of object storage retention or lifecycle policies on the data plane bucket.
---

# Data retention policies

The data plane uses an object store bucket (S3, GCS, or ABS) to hold the **raw data** of your workflows — files, directories, dataframes, models, and other large values offloaded from task inputs and outputs. Bucket-level retention and lifecycle policies (such as S3 lifecycle rules) on this bucket purge raw data and can break historical executions, caches, and trace-based recovery.

## Where metadata vs. raw data lives

It helps to be precise about what "metadata" means here, because the term is used in two very different ways elsewhere in the industry.

**Metadata in {{< key product_name >}} lives in the control plane database.** It includes:

- Workflow, task, launch-plan, and artifact registrations.
- Execution status, history, schedules, and audit trail.
- The literal values of task inputs and outputs — primitives (ints, strings, etc.), JSON-serializable dataclasses, and similar small values that are passed *by value* between tasks. The DB stores these values directly.

**Raw data lives in the data plane object-store bucket.** It includes:

- `FlyteFile` / `FlyteDirectory` contents.
- `DataFrame` payloads.
- Models and other pickled / large objects.
- `Deck` data and artifact payloads.
- [Trace](../../../user-guide/task-programming/traces) checkpoints.

When a task input or output is *too large to be passed inline as a literal value*, it is offloaded: the bytes are written to the bucket as raw data, and the literal that the DB stores becomes a **pointer** (URI) into the bucket. The DB still holds the canonical record of the input/output — it just holds a reference instead of the value.

> [!NOTE] The bucket does not hold {{< key product_name >}} metadata
> The data plane bucket is the raw data store. {{< key product_name >}} metadata — registry data, execution status, and the literal values of small inputs/outputs — is stored in the control plane database, not the bucket. Retention policies on the bucket do not delete metadata. They can, however, leave DB-side pointers dangling when the raw data they reference is purged.

## Impact of raw data loss

A retention policy that purges raw data leaves the metadata in the control plane database intact, but the references it holds to offloaded values become **dangling pointers**. The effects:

| Area | Impact |
|------|--------|
| **UI and APIs** | Execution detail views still render (status, timing, structure all come from the DB), but input/output previews, `Deck` views, and artifact payload links resolve to purged blobs and fail with "resource not found." |
| **Execution engine** | Re-runs or downstream tasks that consume a purged upstream output fail at runtime. In-flight tasks that depend on a node whose output was just purged fail. |
| **Caching** | A cache hit may resolve to a pointer whose underlying raw data has been purged, producing cache misses, task re-execution, or failure. |
| **Traces** | [Trace](../../../user-guide/task-programming/traces) checkpoints used by `@flyte.trace` for fine-grained recovery are stored in the bucket; if purged, resume-from-checkpoint is not possible for affected executions. |
| **Operations** | The DB record of what ran, when, and with what *small literal* inputs/outputs is preserved. The record of what *large offloaded* inputs/outputs each task produced is lost wherever the raw data has been purged. |

## Applying retention deliberately

Retention on the raw-data bucket is a legitimate cost-management strategy as long as you accept the trade-off: historical executions that referenced purged data will no longer be re-runnable from cache or recoverable from trace checkpoints, and their UI views will show missing blobs. New executions are unaffected.

Be aware of the trade-offs in particular for:

- **Cached task outputs** — purging the cached raw data invalidates the cache; affected tasks re-execute on the next call.
- **Trace checkpoints** — purging prevents resume-from-checkpoint for executions whose checkpoints have aged out.
- **Historical execution previews** — purged raw data will show as "resource not found" in the UI even though the DB still has the rest of the record.

Data correctness is not silently violated: re-runs read from current raw data, and the DB record is the source of truth for what executed. You're trading off the ability to recover or inspect old offloaded values.

## Separating raw-data paths within the bucket

Self-managed deployments can split bucket content into separate paths (or separate buckets) so that lifecycle rules can target specific subsets — for example, purging old `Deck` data while keeping `FlyteFile` outputs. This is configured via `configuration.storage.metadataContainer` and `configuration.storage.userDataContainer` in the [data plane chart](https://github.com/unionai/helm-charts/blob/master/charts/dataplane/values.yaml).

> [!WARNING] Naming note
> The Helm chart setting `metadataContainer` and the related `config.core.propeller.metadata-prefix` setting refer to {{< key product_name >}}-internal system data (workflow state and similar engine artifacts that propeller writes into the bucket). They do **not** refer to {{< key product_name >}} metadata in the customer-facing sense — that lives in the control plane database. Be careful when designing lifecycle rules against these paths: purging the propeller "metadata" prefix can break in-flight and historical executions, while purging the user-data prefix purges raw data as described above. Validate any retention rules in a non-production environment before applying them broadly.

## Per-run customization

Both the raw-data location and the engine's run base directory can be overridden **per run** (or per trigger) via [`flyte.with_runcontext()`](../../../user-guide/task-deployment/run-context#storage):

- `raw_data_path` — storage prefix for offloaded raw data (`FlyteFile`, `FlyteDirectory`, `DataFrame`, checkpoints, etc.).
- `run_base_dir` — base directory for the engine's per-run system data passed between tasks.

This is the path BYOC customers have today for directing a run's raw data to a different bucket — for example, a customer-owned bucket with its own retention policy. Setting a deployment-wide default for these paths on BYOC is not currently supported.
