---
title: LiteralCollection
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LiteralCollection

**Package:** `flytekit.models.literals`

```python
class LiteralCollection(
    literals,
)
```
| Parameter | Type | Description |
|-|-|-|
| `literals` |  | |

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
:rtype: flyteidl.core.literals_pb2.LiteralCollection


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `literals` |  | {{< multiline >}}:rtype: list[Literal]
{{< /multiline >}} |

