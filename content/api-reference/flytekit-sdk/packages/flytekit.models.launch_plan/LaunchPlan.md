---
title: LaunchPlan
version: 1.16.10
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


## Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: LaunchPlanClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `is_empty` |  |  |
| `should_auto_activate` |  |  |
| `spec` |  | {{< multiline >}}:rtype: LaunchPlanSpec
{{< /multiline >}} |

