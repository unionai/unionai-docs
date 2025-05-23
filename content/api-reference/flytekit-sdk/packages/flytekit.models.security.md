---
title: flytekit.models.security
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.security

## Directory

### Classes

| Class | Description |
|-|-|
| [`Identity`](.././flytekit.models.security#flytekitmodelssecurityidentity) |  |
| [`OAuth2Client`](.././flytekit.models.security#flytekitmodelssecurityoauth2client) |  |
| [`OAuth2TokenRequest`](.././flytekit.models.security#flytekitmodelssecurityoauth2tokenrequest) |  |
| [`Secret`](.././flytekit.models.security#flytekitmodelssecuritysecret) | See :std:ref:`cookbook:secrets` for usage examples. |
| [`SecurityContext`](.././flytekit.models.security#flytekitmodelssecuritysecuritycontext) | This is a higher level wrapper object that for the most part users shouldn't have to worry about. |

## flytekit.models.security.Identity

```python
class Identity(
    iam_role: typing.Optional[str],
    k8s_service_account: typing.Optional[str],
    oauth2_client: typing.Optional[flytekit.models.security.OAuth2Client],
    execution_identity: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `iam_role` | `typing.Optional[str]` |
| `k8s_service_account` | `typing.Optional[str]` |
| `oauth2_client` | `typing.Optional[flytekit.models.security.OAuth2Client]` |
| `execution_identity` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.Identity,
) -> Identity
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.Identity` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.security.OAuth2Client

```python
class OAuth2Client(
    client_id: str,
    client_secret: str,
)
```
| Parameter | Type |
|-|-|
| `client_id` | `str` |
| `client_secret` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.OAuth2Client,
) -> OAuth2Client
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.OAuth2Client` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.security.OAuth2TokenRequest

```python
class OAuth2TokenRequest(
    name: str,
    client: flytekit.models.security.OAuth2Client,
    idp_discovery_endpoint: typing.Optional[str],
    token_endpoint: typing.Optional[str],
    type_: <enum 'Type'>,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `client` | `flytekit.models.security.OAuth2Client` |
| `idp_discovery_endpoint` | `typing.Optional[str]` |
| `token_endpoint` | `typing.Optional[str]` |
| `type_` | `<enum 'Type'>` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.OAuth2TokenRequest,
) -> OAuth2TokenRequest
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.OAuth2TokenRequest` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.security.Secret

See :std:ref:`cookbook:secrets` for usage examples.



```python
class Secret(
    group: typing.Optional[str],
    key: typing.Optional[str],
    group_version: typing.Optional[str],
    mount_requirement: <enum 'MountType'>,
    env_var: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `group` | `typing.Optional[str]` |
| `key` | `typing.Optional[str]` |
| `group_version` | `typing.Optional[str]` |
| `mount_requirement` | `<enum 'MountType'>` |
| `env_var` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.Secret,
) -> Secret
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.Secret` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.security.SecurityContext

This is a higher level wrapper object that for the most part users shouldn't have to worry about. You should
be able to just use {{< py_class_ref flytekit.Secret >}} instead.


```python
class SecurityContext(
    run_as: typing.Optional[flytekit.models.security.Identity],
    secrets: typing.Optional[typing.List[flytekit.models.security.Secret]],
    tokens: typing.Optional[typing.List[flytekit.models.security.OAuth2TokenRequest]],
)
```
| Parameter | Type |
|-|-|
| `run_as` | `typing.Optional[flytekit.models.security.Identity]` |
| `secrets` | `typing.Optional[typing.List[flytekit.models.security.Secret]]` |
| `tokens` | `typing.Optional[typing.List[flytekit.models.security.OAuth2TokenRequest]]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.SecurityContext,
) -> SecurityContext
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.SecurityContext` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

