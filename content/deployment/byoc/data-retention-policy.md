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
   - Offloaded large values: `flyte.io.File`, `flyte.io.Dir`, `flyte.io.DataFrame`, and other reference-type payloads, both in their default location and in any custom location specified per run via `flyte.with_runcontext(raw_data_path=...)`.
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

## Separating raw data from metadata

You can route a run's **raw data** (offloaded values such as `flyte.io.File`, `flyte.io.Dir`, `flyte.io.DataFrame`, and checkpoints) to a different bucket or prefix than the rest of the run's data, for example, to a bucket with its own lifecycle rules. Only the raw offloaded contents move; the `inputs.pb` / `outputs.pb` payloads still land in the configured metadata bucket. For the conceptual map of what "raw data" versus "metadata" means, see [Where your data lives](../../user-guide/core-concepts/where-data-lives).

You can set the raw-data path **per run**, or as a **default for a whole project or domain**.

### Per run

Set `raw_data_path` on an individual run from the client:

```python
import flyte

flyte.init_from_config()

run = flyte.with_runcontext(
    raw_data_path="s3://my-other-bucket/some/prefix",
).run(my_task, x=1)
```

Or use the `--raw-data-path` flag on `flyte run`:

```shell
flyte run --raw-data-path s3://my-other-bucket/some/prefix my_workflow.py main
```

### As a project or domain default

To point **all** runs in a project and/or domain at a separate raw-data path by default, set the `storage.raw_data_path` setting. This is self-service (no redeployment required) and settings resolve from broadest to narrowest scope (org → domain → project), so you can set a wide default and override it more specifically.

Edit the settings for a project and domain interactively, then set `storage.raw_data_path` to your bucket or prefix:

```shell
flyte edit settings --domain production --project ml-pipeline
```

You can also configure this in the Union UI under the project's settings. See [Settings](../../user-guide/core-concepts/settings#available-settings) for the full list of available settings (including `storage.raw_data_path`) and how scopes are resolved.

## Data retention and task caching

Task caching is adjusted to match the retention period. To avoid attempts to retrieve cache data that has already been deleted, the cache `age` is configured to be less than the retention period.
