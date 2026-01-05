---
title: Secret
version: 2.0.0b43
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

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) |  |
| [`delete()`](#delete) |  |
| [`get()`](#get) |  |
| [`listall()`](#listall) |  |
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
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `value` | `Union[str, bytes]` | |
| `type` | `SecretTypes` | |

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
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` |  | |

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
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

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
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | |

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


## Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` |  |
| `type` | `None` |  |

