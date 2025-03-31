---
title: flytekit.clients.auth.keyring
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clients.auth.keyring

## Directory

### Classes

| Class | Description |
|-|-|
| [`Credentials`](.././flytekit.clients.auth.keyring#flytekitclientsauthkeyringcredentials) | Stores the credentials together. |
| [`KeyringStore`](.././flytekit.clients.auth.keyring#flytekitclientsauthkeyringkeyringstore) | Methods to access Keyring Store. |

### Errors

| Exception | Description |
|-|-|
| [`NoKeyringError`](.././flytekit.clients.auth.keyring#flytekitclientsauthkeyringnokeyringerror) | Raised when there is no keyring backend. |
| [`PasswordDeleteError`](.././flytekit.clients.auth.keyring#flytekitclientsauthkeyringpassworddeleteerror) | Raised when the password can't be deleted. |

### Methods

| Method | Description |
|-|-|
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |


## Methods

#### dataclass()

```python
def dataclass(
    cls,
    init,
    repr,
    eq,
    order,
    unsafe_hash,
    frozen,
    match_args,
    kw_only,
    slots,
    weakref_slot,
)
```
Add dunder methods based on the fields defined in the class.

Examines PEP 526 __annotations__ to determine fields.

If init is true, an __init__() method is added to the class. If repr
is true, a __repr__() method is added. If order is true, rich
comparison dunder methods are added. If unsafe_hash is true, a
__hash__() method is added. If frozen is true, fields may not be
assigned to after instance creation. If match_args is true, the
__match_args__ tuple is added. If kw_only is true, then by default
all fields are keyword-only. If slots is true, a new class with a
__slots__ attribute is returned.


| Parameter | Type |
|-|-|
| `cls` |  |
| `init` |  |
| `repr` |  |
| `eq` |  |
| `order` |  |
| `unsafe_hash` |  |
| `frozen` |  |
| `match_args` |  |
| `kw_only` |  |
| `slots` |  |
| `weakref_slot` |  |

## flytekit.clients.auth.keyring.Credentials

Stores the credentials together


```python
class Credentials(
    access_token: str,
    refresh_token: typing.Optional[str],
    for_endpoint: str,
    expires_in: typing.Optional[int],
    id_token: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `access_token` | `str` |
| `refresh_token` | `typing.Optional[str]` |
| `for_endpoint` | `str` |
| `expires_in` | `typing.Optional[int]` |
| `id_token` | `typing.Optional[str]` |

## flytekit.clients.auth.keyring.KeyringStore

Methods to access Keyring Store.


### Methods

| Method | Description |
|-|-|
| [`delete()`](#delete) |  |
| [`retrieve()`](#retrieve) |  |
| [`store()`](#store) |  |


#### delete()

```python
def delete(
    for_endpoint: str,
)
```
| Parameter | Type |
|-|-|
| `for_endpoint` | `str` |

#### retrieve()

```python
def retrieve(
    for_endpoint: str,
) -> typing.Optional[flytekit.clients.auth.keyring.Credentials]
```
| Parameter | Type |
|-|-|
| `for_endpoint` | `str` |

#### store()

```python
def store(
    credentials: flytekit.clients.auth.keyring.Credentials,
) -> flytekit.clients.auth.keyring.Credentials
```
| Parameter | Type |
|-|-|
| `credentials` | `flytekit.clients.auth.keyring.Credentials` |

## flytekit.clients.auth.keyring.NoKeyringError

Raised when there is no keyring backend


## flytekit.clients.auth.keyring.PasswordDeleteError

Raised when the password can't be deleted.


