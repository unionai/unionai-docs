---
title: BooleanExpression
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# BooleanExpression

**Package:** `flytekit.models.core.condition`

```python
class BooleanExpression(
    conjunction,
    comparison,
)
```
Defines a boolean expression tree. It can be a simple or a conjunction expression.
Multiple expressions can be combined using a conjunction or a disjunction to result in a final boolean result.



| Parameter | Type | Description |
|-|-|-|
| `conjunction` |  | |
| `comparison` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `comparison` | `None` | Comparison expression or None if not set. :rtype: ComparisonExpression |
| `conjunction` | `None` | Conjunction expression or None if not set. :rtype: ConjunctionExpression |
| `is_empty` | `None` |  |

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
:rtype: flyteidl.core.condition_pb2.BooleanExpression


