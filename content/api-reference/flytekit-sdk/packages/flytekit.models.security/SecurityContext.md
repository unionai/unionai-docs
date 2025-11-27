---
title: SecurityContext
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SecurityContext

**Package:** `flytekit.models.security`

This is a higher level wrapper object that for the most part users shouldn't have to worry about. You should
be able to just use {{< py_class_ref flytekit.Secret >}} instead.


```python
class SecurityContext(
    run_as: typing.Optional[flytekit.models.security.Identity],
    secrets: typing.Optional[typing.List[flytekit.models.security.Secret]],
    tokens: typing.Optional[typing.List[flytekit.models.security.OAuth2TokenRequest]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `run_as` | `typing.Optional[flytekit.models.security.Identity]` | |
| `secrets` | `typing.Optional[typing.List[flytekit.models.security.Secret]]` | |
| `tokens` | `typing.Optional[typing.List[flytekit.models.security.OAuth2TokenRequest]]` | |

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
    pb2_object: flyteidl.core.security_pb2.SecurityContext,
) -> SecurityContext
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.SecurityContext` | |

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
## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

