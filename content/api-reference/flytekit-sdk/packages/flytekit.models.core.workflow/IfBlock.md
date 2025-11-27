---
title: IfBlock
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# IfBlock

**Package:** `flytekit.models.core.workflow`

```python
class IfBlock(
    condition,
    then_node,
)
```
Defines a condition and the execution unit that should be executed if the condition is satisfied.



| Parameter | Type | Description |
|-|-|-|
| `condition` |  | |
| `then_node` |  | |

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
:rtype: flyteidl.core.workflow_pb2.IfBlock


## Properties

| Property | Type | Description |
|-|-|-|
| `condition` |  | {{< multiline >}}:rtype: flytekit.models.core.condition.BooleanExpression
{{< /multiline >}} |
| `is_empty` |  |  |
| `then_node` |  | {{< multiline >}}:rtype: Node
{{< /multiline >}} |

