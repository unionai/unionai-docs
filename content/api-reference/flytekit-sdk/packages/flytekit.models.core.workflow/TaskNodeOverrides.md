---
title: TaskNodeOverrides
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskNodeOverrides

**Package:** `flytekit.models.core.workflow`

```python
class TaskNodeOverrides(
    resources: typing.Optional[flytekit.models.task.Resources],
    extended_resources: typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources],
    container_image: typing.Optional[str],
    pod_template: typing.Optional[flytekit.core.pod_template.PodTemplate],
)
```
| Parameter | Type | Description |
|-|-|-|
| `resources` | `typing.Optional[flytekit.models.task.Resources]` | |
| `extended_resources` | `typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]` | |
| `container_image` | `typing.Optional[str]` | |
| `pod_template` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


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
## Properties

| Property | Type | Description |
|-|-|-|
| `container_image` |  |  |
| `extended_resources` |  |  |
| `is_empty` |  |  |
| `pod_template` |  |  |
| `resources` |  |  |

