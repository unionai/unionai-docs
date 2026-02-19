---
title: ConjunctionExpression
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConjunctionExpression

**Package:** `flytekit.models.core.condition`

```python
class ConjunctionExpression(
    operator,
    left_expression,
    right_expression,
)
```
Defines a conjunction expression of two boolean expressions.


| Parameter | Type | Description |
|-|-|-|
| `operator` |  | |
| `left_expression` |  | |
| `right_expression` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `left_expression` | `None` | Gets the left value for the conjunction expression. :rtype: Operand |
| `operator` | `None` | Gets the operator representing this conjunction expression. :rtype: ConjunctionExpression.LogicalOperator |
| `right_expression` | `None` | Gets the right value for the conjunction expression. :rtype: Operand |

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
:rtype: flyteidl.core.condition_pb2.ConjunctionExpression


