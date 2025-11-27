---
title: Union
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Union

**Package:** `flytekit.models.literals`

```python
class Union(
    value,
    stored_type,
)
```
The runtime representation of a tagged union value. See `UnionType` for more details.



| Parameter | Type | Description |
|-|-|-|
| `value` |  | |
| `stored_type` |  | |

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
:rtype: flyteidl.core.literals_pb2.Union


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `stored_type` |  | {{< multiline >}}:rtype: flytekit.models.types.LiteralType
{{< /multiline >}} |
| `value` |  | {{< multiline >}}:rtype: flytekit.models.literals.Literal
{{< /multiline >}} |

