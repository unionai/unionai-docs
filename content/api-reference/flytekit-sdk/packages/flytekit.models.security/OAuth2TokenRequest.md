---
title: OAuth2TokenRequest
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OAuth2TokenRequest

**Package:** `flytekit.models.security`

```python
class OAuth2TokenRequest(
    name: str,
    client: flytekit.models.security.OAuth2Client,
    idp_discovery_endpoint: typing.Optional[str],
    token_endpoint: typing.Optional[str],
    type_: <enum 'Type'>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `client` | `flytekit.models.security.OAuth2Client` | |
| `idp_discovery_endpoint` | `typing.Optional[str]` | |
| `token_endpoint` | `typing.Optional[str]` | |
| `type_` | `<enum 'Type'>` | |

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
    pb2_object: flyteidl.core.security_pb2.OAuth2TokenRequest,
) -> OAuth2TokenRequest
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.OAuth2TokenRequest` | |

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

