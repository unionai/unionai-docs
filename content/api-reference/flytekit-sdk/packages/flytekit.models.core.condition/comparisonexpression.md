---
title: ComparisonExpression
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ComparisonExpression

**Package:** `flytekit.models.core.condition`

```python
class ComparisonExpression(
    operator,
    left_value,
    right_value,
)
```
Defines a 2-level tree where the root is a comparison operator and Operands are primitives or known variables.
Each expression results in a boolean result.



| Parameter | Type | Description |
|-|-|-|
| `operator` |  | |
| `left_value` |  | |
| `right_value` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `left_value` | `None` | Gets the left value for the comparison expression. :rtype: Operand |
| `operator` | `None` | Gets the operator representing this comparison expression. :rtype: ComparisonExpression.Operator |
| `right_value` | `None` | Gets the right value for the comparison expression. :rtype: Operand |

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
:rtype: flyteidl.core.condition_pb2.ComparisonExpression


