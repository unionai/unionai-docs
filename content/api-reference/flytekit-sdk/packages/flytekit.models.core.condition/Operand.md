---
title: Operand
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Operand

**Package:** `flytekit.models.core.condition`

```python
class Operand(
    primitive,
    var,
    scalar,
)
```
Defines an operand to a comparison expression.


| Parameter | Type | Description |
|-|-|-|
| `primitive` |  | |
| `var` |  | |
| `scalar` |  | |

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
:rtype: flyteidl.core.condition_pb2.Operand


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `primitive` |  | {{< multiline >}}:rtype: flytekit.models.literals.Primitive
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}:rtype: flytekit.models.literals.Scalar
{{< /multiline >}} |
| `var` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

