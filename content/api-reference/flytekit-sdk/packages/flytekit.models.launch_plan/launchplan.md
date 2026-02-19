---
title: LaunchPlan
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LaunchPlan

**Package:** `flytekit.models.launch_plan`

```python
class LaunchPlan(
    id,
    spec,
    closure,
    auto_activate,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `spec` |  | |
| `closure` |  | |
| `auto_activate` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` | :rtype: LaunchPlanClosure |
| `id` | `None` | :rtype: flytekit.models.core.identifier.Identifier |
| `is_empty` | `None` |  |
| `should_auto_activate` | `None` |  |
| `spec` | `None` | :rtype: LaunchPlanSpec |

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
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlan


