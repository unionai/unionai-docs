---
title: NodeOutput
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NodeOutput

**Package:** `flytekit.core.promise`

```python
class NodeOutput(
    node: Node,
    var: str,
    attr_path: Optional[List[Union[str, int]]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `node` | `Node` | |
| `var` | `str` | The name of the variable this NodeOutput references |
| `attr_path` | `Optional[List[Union[str, int]]]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `attr_path` | `None` | The attribute path the promise will be resolved with. :rtype: list[union[str, int]] |
| `is_empty` | `None` |  |
| `node` | `None` | Return Node object. |
| `node_id` | `None` | Override the underlying node_id property to refer to the Node's id. This is to make sure that overriding node IDs from with_overrides gets serialized correctly. :rtype: Text |
| `var` | `None` | Variable name must refer to an output variable for the node. :rtype: Text |

## Methods

| Method | Description |
|-|-|
| [`deepcopy()`](#deepcopy) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`with_attr()`](#with_attr) |  |


### deepcopy()

```python
def deepcopy()
```
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


### with_attr()

```python
def with_attr(
    key,
) -> NodeOutput
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |

