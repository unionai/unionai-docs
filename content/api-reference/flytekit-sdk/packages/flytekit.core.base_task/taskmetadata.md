---
title: TaskMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskMetadata

**Package:** `flytekit.core.base_task`

Metadata for a Task. Things like retries and whether or not caching is turned on, and cache version are specified
here.

See the :std:ref:`IDL &lt;idl:protos/docs/core/core:taskmetadata&gt;` for the protobuf definition.

Attributes:
    cache (bool): Indicates if caching should be enabled. See :std:ref:`Caching &lt;cookbook:caching&gt;`.
    cache_serialize (bool): Indicates if identical (i.e. same inputs) instances of this task should be executed in serial when caching is enabled. See :std:ref:`Caching &lt;cookbook:caching&gt;`.
    cache_version (str): Version to be used for the cached value.
    cache_ignore_input_vars (Tuple[str, ...]): Input variables that should not be included when calculating hash for cache.
    interruptible (Optional[bool]): Indicates that this task can be interrupted and/or scheduled on nodes with lower QoS guarantees that can include pre-emption.
    deprecated (str): Can be used to provide a warning message for a deprecated task. An absence or empty string indicates that the task is active and not deprecated.
    retries (int): for retries=n; n &gt; 0, on failures of this task, the task will be retried at-least n number of times.
    timeout (Optional[Union[datetime.timedelta, int]]): The maximum duration for which one execution of this task should run. The execution will be terminated if the runtime exceeds this timeout.
    pod_template_name (Optional[str]): The name of an existing PodTemplate resource in the cluster which will be used for this task.
    generates_deck (bool): Indicates whether the task will generate a Deck URI.
    is_eager (bool): Indicates whether the task should be treated as eager.
    labels (Optional[dict[str, str]]): Labels to be applied to the task resource.
    annotations (Optional[dict[str, str]]): Annotations to be applied to the task resource.



```python
class TaskMetadata(
    cache: bool,
    cache_serialize: bool,
    cache_version: str,
    cache_ignore_input_vars: typing.Tuple[str, ...],
    interruptible: typing.Optional[bool],
    deprecated: str,
    retries: int,
    timeout: typing.Union[datetime.timedelta, int, NoneType],
    pod_template_name: typing.Optional[str],
    generates_deck: bool,
    is_eager: bool,
    labels: typing.Optional[dict[str, str]],
    annotations: typing.Optional[dict[str, str]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `cache` | `bool` | |
| `cache_serialize` | `bool` | |
| `cache_version` | `str` | |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` | |
| `interruptible` | `typing.Optional[bool]` | |
| `deprecated` | `str` | |
| `retries` | `int` | |
| `timeout` | `typing.Union[datetime.timedelta, int, NoneType]` | |
| `pod_template_name` | `typing.Optional[str]` | |
| `generates_deck` | `bool` | |
| `is_eager` | `bool` | |
| `labels` | `typing.Optional[dict[str, str]]` | |
| `annotations` | `typing.Optional[dict[str, str]]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `retry_strategy` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`to_taskmetadata_model()`](#to_taskmetadata_model) | Converts to _task_model. |


### to_taskmetadata_model()

```python
def to_taskmetadata_model()
```
Converts to _task_model.TaskMetadata


