---
title: ExecutionError
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ExecutionError

**Package:** `flytekit.models.core.execution`

```python
class ExecutionError(
    code: str,
    message: str,
    error_uri: str,
    kind: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `message` | `str` | |
| `error_uri` | `str` | |
| `kind` | `int` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `code` | `None` | :rtype: Text |
| `error_uri` | `None` | :rtype: Text |
| `is_empty` | `None` |  |
| `kind` | `None` | Enum value from ErrorKind |
| `message` | `None` | :rtype: Text |

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
:rtype: flyteidl.core.execution_pb2.ExecutionError


