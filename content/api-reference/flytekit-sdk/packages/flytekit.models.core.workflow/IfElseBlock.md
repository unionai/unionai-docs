---
title: IfElseBlock
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# IfElseBlock

**Package:** `flytekit.models.core.workflow`

```python
class IfElseBlock(
    case,
    other,
    else_node,
    error,
)
```
Defines a series of if/else blocks. The first branch whose condition evaluates to true is the one to execute.
If no conditions were satisfied, the else_node or the error will execute.



| Parameter | Type | Description |
|-|-|-|
| `case` |  | |
| `other` |  | |
| `else_node` |  | |
| `error` |  | |

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
:rtype: flyteidl.core.workflow_pb2.IfElseBlock


## Properties

| Property | Type | Description |
|-|-|-|
| `case` |  | {{< multiline >}}First condition to evaluate.

:rtype: IfBlock
{{< /multiline >}} |
| `else_node` |  | {{< multiline >}}The node to execute in case none of the branches were taken.

:rtype: Node
{{< /multiline >}} |
| `error` |  | {{< multiline >}}An error to throw in case none of the branches were taken.

:rtype: flytekit.models.types.Error
{{< /multiline >}} |
| `is_empty` |  |  |
| `other` |  | {{< multiline >}}Additional branches to evaluate.

:rtype: list[IfBlock]
{{< /multiline >}} |

