---
title: LaunchPlanMetadata
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LaunchPlanMetadata

**Package:** `flytekit.models.launch_plan`

```python
class LaunchPlanMetadata(
    schedule,
    notifications,
    launch_conditions,
)
```
| Parameter | Type | Description |
|-|-|-|
| `schedule` |  | |
| `notifications` |  | |
| `launch_conditions` |  | Additional metadata for launching |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | List of notifications based on Execution status transitions. |


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
List of notifications based on Execution status transitions
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlanMetadata


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `launch_conditions` |  |  |
| `notifications` |  | {{< multiline >}}List of notifications based on Execution status transitions
:rtype: list[flytekit.models.common.Notification]
{{< /multiline >}} |
| `schedule` |  | {{< multiline >}}Schedule to execute the Launch Plan
:rtype: flytekit.models.schedule.Schedule
{{< /multiline >}} |

