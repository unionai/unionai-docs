---
title: NodeOutput
version: 1.16.10
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

## Properties

| Property | Type | Description |
|-|-|-|
| `attr_path` |  | {{< multiline >}}The attribute path the promise will be resolved with.
:rtype: list[union[str, int]]
{{< /multiline >}} |
| `is_empty` |  |  |
| `node` |  | {{< multiline >}}Return Node object.
{{< /multiline >}} |
| `node_id` |  | {{< multiline >}}Override the underlying node_id property to refer to the Node's id. This is to make sure that overriding
node IDs from with_overrides gets serialized correctly.
:rtype: Text
{{< /multiline >}} |
| `var` |  | {{< multiline >}}Variable name must refer to an output variable for the node.
:rtype: Text
{{< /multiline >}} |

