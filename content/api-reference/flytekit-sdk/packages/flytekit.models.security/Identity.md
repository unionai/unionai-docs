---
title: Identity
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Identity

**Package:** `flytekit.models.security`

```python
class Identity(
    iam_role: typing.Optional[str],
    k8s_service_account: typing.Optional[str],
    oauth2_client: typing.Optional[flytekit.models.security.OAuth2Client],
    execution_identity: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `iam_role` | `typing.Optional[str]` | |
| `k8s_service_account` | `typing.Optional[str]` | |
| `oauth2_client` | `typing.Optional[flytekit.models.security.OAuth2Client]` | |
| `execution_identity` | `typing.Optional[str]` | |

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
    pb2_object: flyteidl.core.security_pb2.Identity,
) -> Identity
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.Identity` | |

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

