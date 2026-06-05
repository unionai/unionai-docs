---
title: Data retention policy
weight: 8
variants: -flyte +union
---

# Data retention policy

Data retention policies let you control how long workflow data is kept in the data plane object store. They are a cost-management tool: you trade the ability to inspect or re-run aged-out executions against storage cost.

For the conceptual map of what's in the data plane bucket versus the control plane database, see [Where your data lives](../../user-guide/core-concepts/where-data-lives). This page describes the **policy interface** — what categories you can configure, what the policy values mean, and what happens when data is deleted.

As a {{< key product_name >}} administrator, retention policies are specified in discussion with the {{< key product_name >}} team when you set up your {{< key product_name >}} instance. They are not adjustable through the UI or CLI.

## Data categories

The retention policy system distinguishes the following categories of data:

1. **Workflow execution data** — the per-run artifacts written during task execution:
   - Task inputs and outputs (the `inputs.pb` / `outputs.pb` protobuf payloads written by the platform during run setup and task execution).
   - Offloaded large values: `flyte.io.File`, `flyte.io.Dir`, `flyte.io.DataFrame`, and other reference-type payloads — both in their default location and in any custom location specified per run via `flyte.with_runcontext(raw_data_path=...)`.
   - `Deck` and report artifacts.
   - Trace checkpoints.

2. **Fast-registered code** — the local code artifacts that are uploaded by `flyte deploy` or `flyte run --copy-style all` so the cluster can run your local Python without rebuilding the container image.

Each category is stored with object versioning enabled, which means two retention values can be specified for each category — one for current versions and one for non-current versions.

> [!NOTE] Object versions are not the same as {{< key product_name >}} entity versions
> The versions discussed here are at the object level and are not related to the versions of workflows, tasks, and other {{< key product_name >}} entities that you see in the {{< key product_name >}} UI.

## How policies are specified

A policy determines how long data in a given category and version-state (current vs. non-current) is retained in the object store before being automatically deleted.

A policy is specified as a time period in days, or `unlimited` (in which case automatic data deletion is disabled for that category and version-state).

## Deletion of current versions

For current versions, deletion due to a retention period running out means moving the object to a non-current version — *soft-deletion*.

## Deletion of non-current versions

For non-current versions, deletion due to a retention period running out means permanent deletion.

## Defaults

|                     | Workflow execution data | Fast-registered code |
| ------------------- | ----------------------- | -------------------- |
| Current version     | unlimited               | unlimited            |
| Non-current version | 7 days                  | 7 days               |

By default:

- The retention policy for **current versions in all categories** is `unlimited`, meaning that auto-deletion is disabled.
  - If you change this to a specified number of days, then auto-deletion will occur after that time period, but because it applies to current versions the data object will be soft-deleted (that is, moved to a non-current version), not permanently deleted.
- The retention policy for **non-current versions in all categories** is `7 days`, meaning that auto-deletion will occur after 7 days and that the data will be permanently deleted.

## Attempting to access deleted data

If you attempt to access deleted data, you will receive an error:

- When task input/output data is deleted, the Input/Output tabs in the UI display a *Not Found* error.
- When `Deck` data is deleted, the `Deck` view in the UI displays a *Not Found* error.
- When artifact references resolve to deleted blobs, the UI shows a URL that points to a no longer existing object.

To remedy these types of errors, you have to re-run the workflow that generated the data in question.

- When fast-registered code data is deleted, executions that depend on it will fail.

To remedy this, you have to both re-register and re-run the workflow.

## Separate sets of policies per cluster

If you have a multi-cluster setup, you can specify a different set of retention policies (one per category) for each cluster.

## Data retention and task caching

When data retention is enabled, task caching is adjusted accordingly. To avoid attempts to retrieve cache data that has already been deleted, the cache `age` is configured to be less than the sum of both retention periods.
