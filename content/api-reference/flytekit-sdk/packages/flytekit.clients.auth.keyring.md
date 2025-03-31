---
title: flytekit.clients.auth.keyring
version: 1.15.4.dev2+g3e3ce2426
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

* [`NoKeyringError`](.././flytekit.clients.auth.keyring#flytekitclientsauthkeyringnokeyringerror)
* [`PasswordDeleteError`](.././flytekit.clients.auth.keyring#flytekitclientsauthkeyringpassworddeleteerror)

## flytekit.clients.auth.keyring.Credentials

Stores the credentials together


```python
def Credentials(
    access_token: str,
    refresh_token: typing.Optional[str],
    for_endpoint: str,
    expires_in: typing.Optional[int],
    id_token: typing.Optional[str],
):
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
| [`delete()`](#delete) | None |
| [`retrieve()`](#retrieve) | None |
| [`store()`](#store) | None |


#### delete()

```python
def delete(
    for_endpoint: str,
):
```
| Parameter | Type |
|-|-|
| `for_endpoint` | `str` |

#### retrieve()

```python
def retrieve(
    for_endpoint: str,
):
```
| Parameter | Type |
|-|-|
| `for_endpoint` | `str` |

#### store()

```python
def store(
    credentials: flytekit.clients.auth.keyring.Credentials,
):
```
| Parameter | Type |
|-|-|
| `credentials` | `flytekit.clients.auth.keyring.Credentials` |

## flytekit.clients.auth.keyring.NoKeyringError

Raised when there is no keyring backend


## flytekit.clients.auth.keyring.PasswordDeleteError

Raised when the password can't be deleted.


