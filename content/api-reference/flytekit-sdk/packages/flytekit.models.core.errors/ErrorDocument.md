---
title: ErrorDocument
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ErrorDocument

**Package:** `flytekit.models.core.errors`

```python
class ErrorDocument(
    error,
)
```
| Parameter | Type | Description |
|-|-|-|
| `error` |  | |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

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
:rtype: flyteidl.core.errors_pb2.ErrorDocument


## Properties

| Property | Type | Description |
|-|-|-|
| `error` |  | {{< multiline >}}:rtype: ContainerError
{{< /multiline >}} |
| `is_empty` |  |  |

