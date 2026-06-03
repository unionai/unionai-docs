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

- Task, trigger and app definitions.
- Execution status, history, schedules, and audit trail.
- The literal values of task inputs and outputs — primitives (ints, strings, etc.), JSON-serializable dataclasses, and similar small values that are passed *by value* between tasks. The DB stores these values directly.

**Raw data lives in the data plane object-store bucket.** It includes:

- `flyte.io.File` / `flyte.io.Dir` contents.
- `flyte.io.DataFrame` payloads.
- Models and other pickled / large objects.
- `Deck` data and artifact payloads.
- [Trace](../../../user-guide/task-programming/traces) checkpoints.

When a task input or output is *too large to be passed inline as a literal value*, it is offloaded: the bytes are written to the bucket as raw data, and the literal that the DB stores becomes a **pointer** (URI) into the bucket. The DB still holds the canonical record of the input/output — it just holds a reference instead of the value.

## Impact of raw data loss

A retention policy that purges raw data leaves the metadata in the control plane database intact, but the references it holds to offloaded values become **dangling pointers**. The effects:

| Area | Impact |
|------|--------|
| **UI and APIs** | Execution detail views still render (status, timing, structure all come from the DB), but input/output previews for offloaded values, `Deck` views, and artifact payload links resolve to purged blobs and fail with "resource not found." |
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

## Designing lifecycle rules

The {{< key product_name >}} data plane organizes execution data under a single configured storage prefix, with sub-prefixes per project, domain, run, and action. Two broad categories of object share this layout:

- **Execution working files** — `inputs.pb` and `outputs.pb` per run/attempt, `Deck` HTML reports, and similar small per-execution artifacts. These are required for in-flight workflows to complete and for historical-execution input/output and `Deck` previews to render. Despite some legacy naming conventions, this is **not** {{< key product_name >}} metadata in the customer-facing sense — that lives in the control plane database (see [above](#where-metadata-vs-raw-data-lives)).
- **Offloaded raw data** — `flyte.io.File` / `flyte.io.Dir` contents, `flyte.io.DataFrame` payloads, checkpoint data, and other values too large to inline. By default these land under the same configured storage prefix; they can be routed elsewhere per run via `flyte.with_runcontext(raw_data_path=...)` (see [Run context](../../../user-guide/task-deployment/run-context#storage)).

When designing S3 lifecycle rules (or the GCS/ABS equivalent), **scope expiration to the offloaded raw-data subpaths** rather than applying a bucket-wide rule. The execution working files (`inputs.pb`, `outputs.pb`, Decks) must remain durable for in-flight executions to complete and for historical-execution previews to render. Typical patterns are rules scoped to domain/project prefixes, or to per-run raw-data paths that have been routed to dedicated buckets via `raw_data_path`.

Validate any retention rule in a non-production environment before applying it broadly. For the full developer-facing map of what's in the bucket, see [Where your data lives](../../../user-guide/core-concepts/where-data-lives).
