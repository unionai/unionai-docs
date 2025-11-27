---
title: TaskNode
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskNode

**Package:** `flytekit.models.core.workflow`

```python
class TaskNode(
    reference_id,
    overrides: typing.Optional[flytekit.models.core.workflow.TaskNodeOverrides],
)
```
Refers to the task that the Node is to execute.
This is currently a oneof in protobuf, but there's only one option currently.
This code should be updated when more options are available.



| Parameter | Type | Description |
|-|-|-|
| `reference_id` |  | |
| `overrides` | `typing.Optional[flytekit.models.core.workflow.TaskNodeOverrides]` | |

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
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.core.workflow_pb2.TaskNode


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `overrides` |  |  |
| `reference_id` |  | {{< multiline >}}A globally unique identifier for the task. This should map to the identifier in Flyte Admin.

:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |

