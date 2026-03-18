---
title: Policy
version: 0.2.1
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Policy

**Package:** `flyteplugins.union.remote`

Represents a Union RBAC Policy.


## Parameters

```python
class Policy(
    pb2: PolicyPb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `PolicyPb2` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `bindings` | `None` |  |
| `description` | `None` |  |
| `name` | `None` |  |
| `organization` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Create a new policy. |
| [`delete()`](#delete) | Delete a policy. |
| [`get()`](#get) | Get a policy by name. |
| [`listall()`](#listall) | List all policies in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`update()`](#update) | Update a policy by diffing bindings and applying add/remove operations. |


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Policy.create.aio()`.
```python
def create(
    cls,
    name: str,
    description: str,
    bindings: list[dict] | None,
) -> Policy
```
Create a new policy.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `description` | `str` | |
| `bindings` | `list[dict] \| None` | |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Policy.delete.aio()`.
```python
def delete(
    cls,
    name: str,
)
```
Delete a policy.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Policy.get.aio()`.
```python
def get(
    cls,
    name: str,
) -> Policy
```
Get a policy by name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Policy.listall.aio()`.
```python
def listall(
    cls,
    limit: int,
) -> AsyncIterator[Policy]
```
List all policies in the organization.


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


### update()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Policy.update.aio()`.
```python
def update(
    cls,
    name: str,
    old_bindings: list[dict],
    new_bindings: list[dict],
) -> Policy
```
Update a policy by diffing bindings and applying add/remove operations.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `old_bindings` | `list[dict]` | |
| `new_bindings` | `list[dict]` | |

