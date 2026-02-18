---
title: Secret
version: 2.0.0b59
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Secret

**Package:** `flyte.remote`

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
| `name` | `None` | Get the name of the secret. |
| `type` | `None` | Get the type of the secret as a string ("regular" or "image_pull"). |

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
)
```
Create a new secret.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the secret. |
| `value` | `Union[str, bytes]` | The secret value as a string or bytes. |
| `type` | `SecretTypes` | Type of secret - either "regular" or "image_pull". |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.delete.aio()`.
```python
def delete(
    cls,
    name,
)
```
Delete a secret by name.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` |  | The name of the secret to delete. |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.get.aio()`.
```python
def get(
    cls,
    name: str,
) -> Secret
```
Retrieve a secret by name.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the secret to retrieve. :return: A Secret object. |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.listall.aio()`.
```python
def listall(
    cls,
    limit: int,
) -> AsyncIterator[Secret]
```
List all secrets in the current project and domain.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | Maximum number of secrets to return per page. :return: An async iterator of Secret objects. |

### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


