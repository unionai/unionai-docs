---
title: TaskContext
version: 2.1.10.dev6+ga8f3f9bfa
variants: +flyte +union
layout: py_api
---

# TaskContext

**Package:** `flyte.models`

A context class to hold the current task executions context.
This can be used to access various contextual parameters in the task execution by the user.



## Parameters

```python
class TaskContext(
    action: ActionID,
    version: str,
    raw_data_path: RawDataPath,
    input_path: str | None,
    output_path: str,
    run_base_dir: str,
    report: Report,
    group_data: GroupData | None,
    checkpoint_paths: CheckpointPaths | None,
    code_bundle: CodeBundle | None,
    compiled_image_cache: ImageCache | None,
    data: Dict[str, Any],
    mode: Literal['local', 'remote', 'hybrid'],
    interactive_mode: bool,
    custom_context: Dict[str, str],
    disable_run_cache: bool,
    in_driver_literal_conversion: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `action` | `ActionID` | The action ID of the current execution. This is always set, within a run. |
| `version` | `str` | The version of the executed task. This is set when the task is executed by an action and will be set on all sub-actions. |
| `raw_data_path` | `RawDataPath` | |
| `input_path` | `str \| None` | |
| `output_path` | `str` | |
| `run_base_dir` | `str` | |
| `report` | `Report` | |
| `group_data` | `GroupData \| None` | |
| `checkpoint_paths` | `CheckpointPaths \| None` | |
| `code_bundle` | `CodeBundle \| None` | |
| `compiled_image_cache` | `ImageCache \| None` | |
| `data` | `Dict[str, Any]` | |
| `mode` | `Literal['local', 'remote', 'hybrid']` | |
| `interactive_mode` | `bool` | |
| `custom_context` | `Dict[str, str]` | Context metadata for the action. If an action receives context, it'll automatically pass it to any actions it spawns. Context will not be used for cache key computation. |
| `disable_run_cache` | `bool` | |
| `in_driver_literal_conversion` | `bool` | Set by the runtime during nested-task literal marshalling; type transformers may use it to skip duplicate side effects (e.g. report tabs) outside true task-body I/O. |

## Properties

| Property | Type | Description |
|-|-|-|
| `attempt_number` | `int` | Get the attempt number for the current task. |
| `checkpoint` | `Optional[Checkpoint]` | Task checkpoint helper for the runtime `checkpoint_path` / `prev_checkpoint` prefixes.  Returns a lazily constructed `flyte.Checkpoint` cached on `flyte.models.TaskContext.data`, or `None` when no checkpoint output prefix is configured. In async tasks use `flyte.Checkpoint.load` and `flyte.Checkpoint.save`; in sync tasks use `flyte.Checkpoint.load_sync` and `flyte.Checkpoint.save_sync`. For a **single raw blob**, pass `bytes` to save; after a successful load, the blob is at `checkpoint.path / "payload"` when the remote object is not a tarball. |

## Methods

| Method | Description |
|-|-|
| [`is_in_cluster()`](#is_in_cluster) | Check if the task is running in a cluster. |
| [`replace()`](#replace) |  |


### is_in_cluster()

```python
def is_in_cluster()
```
Check if the task is running in a cluster.


**Returns:** bool

### replace()

```python
def replace(
    kwargs,
) -> TaskContext
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

