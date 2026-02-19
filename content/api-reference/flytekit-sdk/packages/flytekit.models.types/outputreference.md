---
title: OutputReference
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OutputReference

**Package:** `flytekit.models.types`

```python
class OutputReference(
    node_id,
    var,
    attr_path: typing.List[typing.Union[str, int]],
)
```
A reference to an output produced by a node. The type can be retrieved -and validated- from
    the underlying interface of the node.



| Parameter | Type | Description |
|-|-|-|
| `node_id` |  | |
| `var` |  | |
| `attr_path` | `typing.List[typing.Union[str, int]]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `attr_path` | `None` | The attribute path the promise will be resolved with. :rtype: list[union[str, int]] |
| `is_empty` | `None` |  |
| `node_id` | `None` | Node id must exist at the graph layer. :rtype: Text |
| `var` | `None` | Variable name must refer to an output variable for the node. :rtype: Text |

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
:rtype: flyteidl.core.types.OutputReference


