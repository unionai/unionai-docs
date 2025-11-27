---
title: TaskExecutionIdentifier
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskExecutionIdentifier

**Package:** `flytekit.models.core.identifier`

```python
class TaskExecutionIdentifier(
    task_id,
    node_execution_id,
    retry_attempt,
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_id` |  | |
| `node_execution_id` |  | |
| `retry_attempt` |  | |

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
:rtype: flyteidl.core.identifier_pb2.TaskExecutionIdentifier


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `node_execution_id` |  | {{< multiline >}}:rtype: NodeExecutionIdentifier
{{< /multiline >}} |
| `retry_attempt` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `task_id` |  | {{< multiline >}}:rtype: Identifier
{{< /multiline >}} |

