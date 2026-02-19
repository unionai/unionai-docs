---
title: Envs
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Envs

**Package:** `flytekit.models.common`

```python
class Envs(
    envs: typing.Dict[str, str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `envs` | `typing.Dict[str, str]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `envs` | `None` |  |
| `is_empty` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2: flyteidl.admin.common_pb2.Envs,
) -> flyteidl.admin.common_pb2.Envs
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `flyteidl.admin.common_pb2.Envs` | |

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
