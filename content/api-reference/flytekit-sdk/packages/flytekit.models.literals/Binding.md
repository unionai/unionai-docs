---
title: Binding
version: 1.16.10
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


## Properties

| Property | Type | Description |
|-|-|-|
| `binding` |  | {{< multiline >}}Data to use to bind this variable.
:rtype: BindingData
{{< /multiline >}} |
| `is_empty` |  |  |
| `var` |  | {{< multiline >}}A variable name, must match an input or output variable of the node.
:rtype: Text
{{< /multiline >}} |

