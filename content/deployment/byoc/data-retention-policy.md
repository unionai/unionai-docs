---
title: Data retention policy
weight: 8
variants: -flyte +union
---

# Data retention policy

Data retention policies determine how long workflow data is kept in the data plane object store. After the retention period expires, the data is automatically deleted.

For the conceptual map of what's in the data plane bucket versus the control plane database, see [Where your data lives](../../user-guide/core-concepts/where-data-lives). This page describes which data is covered by the retention policy and what happens when data is deleted.

Retention periods are set by your {{< key product_name >}} plan:

| Plan | Retention period |
| ---- | ---------------- |
| Teams | 30 days |
| Enterprise | 1 year |

Retention periods are not adjustable through the UI or CLI.

## Data categories

The retention policy applies to the following data:

1. **Workflow execution data**: the per-run artifacts written during task execution:
   - Task inputs and outputs (the `inputs.pb` / `outputs.pb` protobuf payloads written by the platform during run setup and task execution).
   - Offloaded large values: `flyte.io.File`, `flyte.io.Dir`, `flyte.io.DataFrame`, and other reference-type payloads — both in their default location and in any custom location specified per run via `flyte.with_runcontext(raw_data_path=...)`.
   - `Deck` and report artifacts.
   - Trace checkpoints.

2. **Workflow code**: The code that is uploaded by `flyte deploy` or `flyte run --copy-style all` and that make up the logic of your tasks and apps and other Flyte entities.

When the age of the data reaches the plan's retention period, it is deleted.

## Attempting to access deleted data

If you attempt to access deleted data, you will receive an error:

- When task input/output data is deleted, the Input/Output tabs in the UI display a *Not Found* error.
- When `Deck` data is deleted, the `Deck` view in the UI displays a *Not Found* error.
- When artifact references resolve to deleted blobs, the UI shows a URL that points to a no longer existing object.

To remedy these types of errors, you have to re-run the workflow that generated the data in question.

- When workflow code is deleted, executions that depend on it will fail.

To remedy this, you have to both re-deploy and re-run the workflow.

## Data retention and task caching

Task caching is adjusted to match the retention period. To avoid attempts to retrieve cache data that has already been deleted, the cache `age` is configured to be less than the retention period.
