---
title: RawOutputDataConfig
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RawOutputDataConfig

**Package:** `flytekit.models.common`

```python
class RawOutputDataConfig(
    output_location_prefix,
)
```
| Parameter | Type | Description |
|-|-|-|
| `output_location_prefix` |  | |

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
    pb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` |  | |

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
:rtype: flyteidl.admin.common_pb2.Auth


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `output_location_prefix` |  |  |

