---
title: Binding
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Binding

**Package:** `flytekit.models.literals`

```python
class Binding(
    var,
    binding,
)
```
An input/output binding of a variable to either static value or a node output.



| Parameter | Type | Description |
|-|-|-|
| `var` |  | |
| `binding` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `binding` | `None` | Data to use to bind this variable. :rtype: BindingData |
| `is_empty` | `None` |  |
| `var` | `None` | A variable name, must match an input or output variable of the node. :rtype: Text |

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
:rtype: flyteidl.core.literals_pb2.Binding


