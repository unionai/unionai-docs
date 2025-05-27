---
title: flytekit.clients.auth.keyring
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.auth.keyring

## Directory

### Classes

| Class | Description |
|-|-|
| [`Credentials`](.././flytekit.clients.auth.keyring#flytekitclientsauthkeyringcredentials) | Stores the credentials together. |
| [`KeyringStore`](.././flytekit.clients.auth.keyring#flytekitclientsauthkeyringkeyringstore) | Methods to access Keyring Store. |

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

