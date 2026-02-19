---
title: KeyringStore
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# KeyringStore

**Package:** `flytekit.clients.auth.keyring`

Methods to access Keyring Store.



## Methods

| Method | Description |
|-|-|
| [`delete()`](#delete) |  |
| [`retrieve()`](#retrieve) |  |
| [`store()`](#store) |  |


### delete()

```python
def delete(
    for_endpoint: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `for_endpoint` | `str` | |

### retrieve()

```python
def retrieve(
    for_endpoint: str,
) -> typing.Optional[flytekit.clients.auth.keyring.Credentials]
```
| Parameter | Type | Description |
|-|-|-|
| `for_endpoint` | `str` | |

### store()

```python
def store(
    credentials: flytekit.clients.auth.keyring.Credentials,
) -> flytekit.clients.auth.keyring.Credentials
```
| Parameter | Type | Description |
|-|-|-|
| `credentials` | `flytekit.clients.auth.keyring.Credentials` | |

