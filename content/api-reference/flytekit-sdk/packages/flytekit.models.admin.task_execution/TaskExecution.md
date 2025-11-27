---
title: TaskExecution
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskExecution

**Package:** `flytekit.models.admin.task_execution`

```python
class TaskExecution(
    id,
    input_uri,
    closure,
    is_parent,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `input_uri` |  | |
| `closure` |  | |
| `is_parent` |  | |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

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
:rtype: flyteidl.admin.task_execution_pb2.TaskExecution


## Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: TaskExecutionClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.TaskExecutionIdentifier
{{< /multiline >}} |
| `input_uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `is_parent` |  | {{< multiline >}}:rtype: bool
{{< /multiline >}} |

