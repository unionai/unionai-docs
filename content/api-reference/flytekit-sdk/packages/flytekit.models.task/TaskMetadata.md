---
title: TaskMetadata
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskMetadata

**Package:** `flytekit.models.task`

```python
class TaskMetadata(
    discoverable,
    runtime,
    timeout,
    retries,
    interruptible,
    discovery_version,
    deprecated_error_message,
    cache_serializable,
    pod_template_name,
    cache_ignore_input_vars,
    is_eager: bool,
    generates_deck: bool,
    k8s_object_metadata: typing.Optional[ForwardRef('K8sObjectMetadata')],
)
```
Information needed at runtime to determine behavior such as whether or not outputs are discoverable, timeouts,
and retries.



| Parameter | Type | Description |
|-|-|-|
| `discoverable` |  | |
| `runtime` |  | |
| `timeout` |  | |
| `retries` |  | |
| `interruptible` |  | |
| `discovery_version` |  | |
| `deprecated_error_message` |  | |
| `cache_serializable` |  | |
| `pod_template_name` |  | The name of the existing PodTemplate resource which will be used in this task. |
| `cache_ignore_input_vars` |  | Input variables that should not be included when calculating hash for cache. |
| `is_eager` | `bool` | |
| `generates_deck` | `bool` | |
| `k8s_object_metadata` | `typing.Optional[ForwardRef('K8sObjectMetadata')]` | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.TaskMetadata,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.TaskMetadata` | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_pb2.TaskMetadata


## Properties

| Property | Type | Description |
|-|-|-|
| `cache_ignore_input_vars` |  | {{< multiline >}}Input variables that should not be included when calculating hash for cache.
:rtype: tuple[Text]
{{< /multiline >}} |
| `cache_serializable` |  | {{< multiline >}}Whether or not caching operations are executed in serial. This means only a single instance over identical
inputs is executed, other concurrent executions wait for the cached results.
:rtype: bool
{{< /multiline >}} |
| `deprecated_error_message` |  | {{< multiline >}}This string can be used to mark the task as deprecated.  Consumers of the task will receive deprecation
warnings.
:rtype: Text
{{< /multiline >}} |
| `discoverable` |  | {{< multiline >}}Whether or not the outputs of this task should be cached for discovery.
:rtype: bool
{{< /multiline >}} |
| `discovery_version` |  | {{< multiline >}}This is the version used to create a logical version for data in the cache.
This is only used when `discoverable` is true.  Data is considered discoverable if: the inputs to a given
task are the same and the discovery_version is also the same.
:rtype: Text
{{< /multiline >}} |
| `generates_deck` |  | {{< multiline >}}Whether the task will generate a Deck.
:rtype: bool
{{< /multiline >}} |
| `interruptible` |  | {{< multiline >}}Whether or not the task is interruptible.
:rtype: bool
{{< /multiline >}} |
| `is_eager` |  |  |
| `is_empty` |  |  |
| `k8s_object_metadata` |  | {{< multiline >}}Kubernetes metadata for the task.
:rtype: K8sObjectMetadata
{{< /multiline >}} |
| `pod_template_name` |  | {{< multiline >}}The name of the existing PodTemplate resource which will be used in this task.
:rtype: Text
{{< /multiline >}} |
| `retries` |  | {{< multiline >}}Retry strategy for this task.  0 retries means only try once.
:rtype: flytekit.models.literals.RetryStrategy
{{< /multiline >}} |
| `runtime` |  | {{< multiline >}}Metadata describing the runtime environment for this task.
:rtype: RuntimeMetadata
{{< /multiline >}} |
| `timeout` |  | {{< multiline >}}The amount of time to wait before timing out.  This includes queuing and scheduler latency.
:rtype: datetime.timedelta
{{< /multiline >}} |

