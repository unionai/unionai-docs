---
title: LiteralMapBlob
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LiteralMapBlob

**Package:** `flytekit.models.execution`

```python
class LiteralMapBlob(
    values,
    uri,
)
```
| Parameter | Type | Description |
|-|-|-|
| `values` |  | |
| `uri` |  | |

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
    pb,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb` |  | |

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
:rtype: flyteidl.admin.execution_pb2.LiteralMapBlob


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `values` |  | {{< multiline >}}:rtype: flytekit.models.literals.LiteralMap
{{< /multiline >}} |

