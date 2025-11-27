---
title: LaunchPlanClosure
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LaunchPlanClosure

**Package:** `flytekit.models.launch_plan`

```python
class LaunchPlanClosure(
    state,
    expected_inputs,
    expected_outputs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `state` |  | |
| `expected_inputs` |  | |
| `expected_outputs` |  | |

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
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlanClosure


## Properties

| Property | Type | Description |
|-|-|-|
| `expected_inputs` |  | {{< multiline >}}:rtype: flytekit.models.interface.ParameterMap
{{< /multiline >}} |
| `expected_outputs` |  | {{< multiline >}}:rtype: flytekit.models.interface.VariableMap
{{< /multiline >}} |
| `is_empty` |  |  |
| `state` |  | {{< multiline >}}:rtype: LaunchPlanState
{{< /multiline >}} |

