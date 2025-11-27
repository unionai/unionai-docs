---
title: UrlBlob
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# UrlBlob

**Package:** `flytekit.models.common`

```python
class UrlBlob(
    url,
    bytes,
)
```
| Parameter | Type | Description |
|-|-|-|
| `url` |  | |
| `bytes` |  | |

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
:rtype: flyteidl.admin.common_pb2.UrlBlob


## Properties

| Property | Type | Description |
|-|-|-|
| `bytes` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `is_empty` |  |  |
| `url` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

