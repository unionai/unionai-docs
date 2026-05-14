---
title: Secret
version: 2.3.1
variants: +flyte +union
layout: py_api
---

# Secret

**Package:** `flyte.remote`

## Parameters

```python
class Secret(
    pb2: definition_pb2.Secret,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `definition_pb2.Secret` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `name` | `str` | Get the name of the secret. |
| `type` | `str` | Get the type of the secret as a string ("regular" or "image_pull"). |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Create a new secret. |
| [`delete()`](#delete) | Delete a secret by name. |
| [`get()`](#get) | Retrieve a secret by name. |
| [`listall()`](#listall) | List all secrets in the current project and domain. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.create.aio()`.
```python
def create(
    cls,
    name: str,
    value: Union[str, bytes],
    type: SecretTypes,
    cluster_pool: str | None,
)
```
Create a new secret.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the secret. |
| `value` | `Union[str, bytes]` | The secret value as a string or bytes. |
| `type` | `SecretTypes` | Type of secret - either "regular" or "image_pull". |
| `cluster_pool` | `str \| None` | Optional cluster pool name. When set, the secret is scoped to the cluster pool and project/domain must not be set. |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.delete.aio()`.
```python
def delete(
    cls,
    name,
    cluster_pool: str | None,
)
```
Delete a secret by name.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` |  | The name of the secret to delete. |
| `cluster_pool` | `str \| None` | Optional cluster pool name. When set, the secret is looked up in the cluster pool scope and project/domain must not be set. |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.get.aio()`.
```python
def get(
    cls,
    name: str,
    cluster_pool: str | None,
) -> Secret
```
Retrieve a secret by name.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the secret to retrieve. |
| `cluster_pool` | `str \| None` | Optional cluster pool name. When set, the secret is looked up in the cluster pool scope and project/domain must not be set. |

**Returns:** A Secret object.

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.listall.aio()`.
```python
def listall(
    cls,
    limit: int,
    cluster_pool: str | None,
) -> AsyncIterator[Secret]
```
List all secrets in the current project and domain.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | Maximum number of secrets to return per page. |
| `cluster_pool` | `str \| None` | Optional cluster pool name. When set, secrets are listed from the cluster pool scope and project/domain must not be set. |

**Returns:** An async iterator of Secret objects.

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

