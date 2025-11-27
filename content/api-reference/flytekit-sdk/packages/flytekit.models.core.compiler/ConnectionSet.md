---
title: ConnectionSet
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConnectionSet

**Package:** `flytekit.models.core.compiler`

```python
class ConnectionSet(
    upstream,
    downstream,
)
```
| Parameter | Type | Description |
|-|-|-|
| `upstream` |  | |
| `downstream` |  | |

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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.core.compiler_pb2.ConnectionSet


## Properties

| Property | Type | Description |
|-|-|-|
| `downstream` |  | {{< multiline >}}:rtype: dict[Text, ConnectionSet.IdList]
{{< /multiline >}} |
| `is_empty` |  |  |
| `upstream` |  | {{< multiline >}}:rtype: dict[Text, ConnectionSet.IdList]
{{< /multiline >}} |

