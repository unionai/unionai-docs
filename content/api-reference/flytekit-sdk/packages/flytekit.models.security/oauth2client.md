---
title: OAuth2Client
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OAuth2Client

**Package:** `flytekit.models.security`

```python
class OAuth2Client(
    client_id: str,
    client_secret: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `client_id` | `str` | |
| `client_secret` | `str` | |

## Properties

| Property | Type | Description |
|-|-|-|
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
    pb2_object: flyteidl.core.security_pb2.OAuth2Client,
) -> OAuth2Client
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.OAuth2Client` | |

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
