---
title: Run context
weight: 10
variants: +flyte +union
---

# Run context

Every Flyte run has a **run context** — a set of invocation-time parameters that control where the run executes, where its outputs are stored, how caching behaves, and more.

There are two sides to run context:

- **Write side**: `flyte.with_runcontext()` — set run parameters before the run starts (programmatic) or via CLI flags.
- **Read side**: `flyte.ctx()` — access run parameters inside a running task.

## Configuring a run with `flyte.with_runcontext()`

`flyte.with_runcontext()` returns a runner object. Call `.run(task, ...)` on it to start the run with the specified context:

{{< code file="/unionai-examples/v2/user-guide/task-deployment/run-context/run_context.py" fragment="basic" lang="python" >}}

All parameters are optional. Unset parameters inherit from the configuration file (`config.yaml`) or system defaults.

### Execution target

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `mode` | `"local"` \| `"remote"` \| `"hybrid"` | *from config* | Where the run executes. `"remote"` runs on the Flyte backend; `"local"` runs in-process. |
| `project` | `str` | *from config* | Project to run in. |
| `domain` | `str` | *from config* | Domain to run in (e.g. `"development"`, `"production"`). |
| `name` | `str` | *auto-generated* | Custom name for the run, visible in the UI. |
| `version` | `str` | *from code bundle* | Version string for the ephemeral task deployment. |
| `queue` | `str` | *from config* | Cluster queue to schedule tasks on. |
| `interruptible` | `bool` | *per-task setting* | Override the interruptible setting for all tasks in the run. `True` allows spot/preemptible instances; `False` forces non-interruptible instances. |

### Storage

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `raw_data_path` | `str` | *from config* | Storage prefix for offloaded data types ([Files](../task-programming/files-and-directories), [Dirs](../task-programming/files-and-directories), [DataFrames](../task-programming/dataframes), checkpoints). Accepts `s3://`, `gs://`, or local paths. |
| `run_base_dir` | `str` | *auto-generated* | Base directory for run metadata passed between tasks. Distinct from `raw_data_path`. |

To direct all task outputs to a specific bucket for a run:

{{< code file="/unionai-examples/v2/user-guide/task-deployment/run-context/run_context.py" fragment="raw-data-path" lang="python" >}}

The equivalent CLI flag is `--raw-data-path`. See [Run command options](./run-command-options#--raw-data-path) for CLI usage.

### Caching

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `overwrite_cache` | `bool` | `False` | Re-execute all tasks even if a cached result exists, and overwrite the cache with new results. |
| `disable_run_cache` | `bool` | `False` | Skip cache lookups and writes entirely for this run. |
| `cache_lookup_scope` | `"global"` \| ... | `"global"` | Scope for cache lookups. |

### Identity and resources

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `service_account` | `str` | *from config* | Kubernetes service account for task pods. |
| `env_vars` | `Dict[str, str]` | `None` | Additional environment variables to inject into task containers. |
| `labels` | `Dict[str, str]` | `None` | Kubernetes labels to apply to task pods. |
| `annotations` | `Dict[str, str]` | `None` | Kubernetes annotations to apply to task pods. |

### Logging

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `log_level` | `int` | *from config* | Python log level (e.g. `logging.DEBUG`). |
| `log_format` | `"console"` \| ... | `"console"` | Log output format. |
| `reset_root_logger` | `bool` | `False` | If `True`, preserve the root logger unchanged. |

### Code bundling

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `copy_style` | `"loaded_modules"` \| `"all"` \| `"none"` | `"loaded_modules"` | Code bundling strategy. See [Run command options](./run-command-options#--copy-style). |
| `dry_run` | `bool` | `False` | Build and upload the code bundle without executing the run. |
| `copy_bundle_to` | `Path` | `None` | When `dry_run=True`, copy the bundle to this local path. |
| `interactive_mode` | `bool` | *auto-detected* | Override interactive mode detection (set automatically for Jupyter notebooks). |
| `preserve_original_types` | `bool` | `False` | Keep native DataFrame types (e.g. `pd.DataFrame`) rather than converting to `flyte.io.DataFrame` when deserializing outputs. |

### Context propagation

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `custom_context` | `Dict[str, str]` | `None` | Metadata propagated through the entire task hierarchy. Readable inside any task via `flyte.ctx().custom_context`. See [Custom context](../task-programming/custom-context). |

---

## Reading context inside a task with `flyte.ctx()`

Inside a running task, `flyte.ctx()` returns a `TaskContext` object with information about the current execution. Outside of a task, it returns `None`.

{{< code file="/unionai-examples/v2/user-guide/task-deployment/run-context/run_context.py" fragment="read-ctx" lang="python" >}}

### `TaskContext` fields

| Field | Type | Description |
|-------|------|-------------|
| `action` | `ActionID` | Identity of this specific action (task invocation) within the run. |
| `mode` | `"local"` \| `"remote"` \| `"hybrid"` | Execution mode of the current run. |
| `version` | `str` | Version of the deployed task code bundle. |
| `raw_data_path` | `str` | Storage prefix where offloaded outputs are written. |
| `run_base_dir` | `str` | Base directory for run metadata. |
| `custom_context` | `Dict[str, str]` | Propagated context metadata from `with_runcontext()`. |
| `disable_run_cache` | `bool` | Whether run caching is disabled for this run. |
| `is_in_cluster()` | method | Returns `True` when `mode == "remote"`. Useful for branching local/remote behavior. |

### `ActionID` fields

The `ctx.action` object identifies this specific task invocation:

| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` | Unique identifier for this action. |
| `run_name` | `str` | Name of the parent run (defaults to `name` if not set). |
| `project` | `str \| None` | Project the action runs in. |
| `domain` | `str \| None` | Domain the action runs in. |
| `org` | `str \| None` | Organization. |

### Naming external resources

`ctx.action.run_name` is useful for tying external tool runs (experiment trackers, dashboards) to the corresponding Flyte run:

{{< code file="/unionai-examples/v2/user-guide/task-deployment/run-context/run_context.py" fragment="integration-naming" lang="python" >}}

This ensures that when you look up a run in Weights & Biases (or any other tool), its name matches what you see in the Flyte UI.
