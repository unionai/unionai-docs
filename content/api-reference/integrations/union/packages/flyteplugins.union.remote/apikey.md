---
title: ApiKey
version: 0.2.2
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# ApiKey

**Package:** `flyteplugins.union.remote`

Represents a Union API Key (OAuth Application).

API Keys in Union are OAuth 2.0 applications that can be used for
headless authentication. They support client credentials flow for
machine-to-machine authentication.



## Parameters

```python
class ApiKey(
    pb2: App,
    organization: str | None,
    encoded_credentials: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `App` | The underlying protobuf App message |
| `organization` | `str \| None` | The organization this API key belongs to (for serverless) |
| `encoded_credentials` | `str \| None` | Base64-encoded credentials for UNION_API_KEY env var |

## Properties

| Property | Type | Description |
|-|-|-|
| `client_id` | `str` | The OAuth client ID. |
| `client_name` | `str` | The human-readable name of the API key. |
| `client_secret` | `str` | The OAuth client secret (only available on creation). |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Create a new API key. |
| [`delete()`](#delete) | Delete an API key. |
| [`get()`](#get) | Get an API key by client ID. |
| [`listall()`](#listall) | List all API keys. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`update()`](#update) | Update an API key. |


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ApiKey.create.aio()`.
```python
def create(
    cls,
    name: str,
    redirect_uris: list[str] | None,
) -> ApiKey
```
Create a new API key.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | Human-readable name for the API key |
| `redirect_uris` | `list[str] \| None` | OAuth redirect URIs (defaults to localhost callback) |

**Returns**

ApiKey instance with client_secret populated


**Raises**

| Exception | Description |
|-|-|
| `Exception` | If API key creation fails |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ApiKey.delete.aio()`.
```python
def delete(
    cls,
    client_id: str,
)
```
Delete an API key.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `client_id` | `str` | The OAuth client ID to delete |

**Raises**

| Exception | Description |
|-|-|
| `Exception` | If deletion fails |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ApiKey.get.aio()`.
```python
def get(
    cls,
    client_id: str,
) -> ApiKey
```
Get an API key by client ID.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `client_id` | `str` | The OAuth client ID |

**Returns**

ApiKey instance


**Raises**

| Exception | Description |
|-|-|
| `Exception` | If API key not found |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ApiKey.listall.aio()`.
```python
def listall(
    cls,
    limit: int,
) -> AsyncIterator[ApiKey]
```
List all API keys.

Yields:
    ApiKey instances



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | Maximum number of keys to return |

### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.



**Returns:** dict: A dictionary representation of the object.

### to_json()

```python
def to_json()
```
Convert the object to a JSON string.



**Returns:** str: A JSON string representation of the object.

### update()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ApiKey.update.aio()`.
```python
def update(
    cls,
    client_id: str,
    client_name: str | None,
    redirect_uris: list[str] | None,
) -> ApiKey
```
Update an API key.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `client_id` | `str` | The OAuth client ID to update |
| `client_name` | `str \| None` | New name for the API key |
| `redirect_uris` | `list[str] \| None` | New redirect URIs |

**Returns**

Updated ApiKey instance


**Raises**

| Exception | Description |
|-|-|
| `Exception` | If update fails |

