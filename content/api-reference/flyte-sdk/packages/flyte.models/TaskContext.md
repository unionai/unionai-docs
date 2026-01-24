---
title: TaskContext
version: 2.0.0b50
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskContext

**Package:** `flyte.models`

A context class to hold the current task executions context.
This can be used to access various contextual parameters in the task execution by the user.



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
    checkpoints: Checkpoints | None,
    code_bundle: CodeBundle | None,
    compiled_image_cache: ImageCache | None,
    data: Dict[str, Any],
    mode: Literal['local', 'remote', 'hybrid'],
    interactive_mode: bool,
    custom_context: Dict[str, str],
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
| `checkpoints` | `Checkpoints \| None` | |
| `code_bundle` | `CodeBundle \| None` | |
| `compiled_image_cache` | `ImageCache \| None` | |
| `data` | `Dict[str, Any]` | |
| `mode` | `Literal['local', 'remote', 'hybrid']` | |
| `interactive_mode` | `bool` | |
| `custom_context` | `Dict[str, str]` | Context metadata for the action. If an action receives context, it'll automatically pass it to any actions it spawns. Context will not be used for cache key computation. |

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
:return: bool


### replace()

```python
def replace(
    kwargs,
) -> TaskContext
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

