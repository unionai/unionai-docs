---
title: Role
version: 0.2.2
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Role

**Package:** `flyteplugins.union.remote`

Represents a Union RBAC Role.


## Parameters

```python
class Role(
    pb2: RolePb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `RolePb2` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `actions` | `None` |  |
| `description` | `None` |  |
| `name` | `None` |  |
| `organization` | `None` |  |
| `role_type` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Create a new role. |
| [`delete()`](#delete) | Delete a role. |
| [`get()`](#get) | Get a role by name. |
| [`listall()`](#listall) | List all roles in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`update()`](#update) | Update a role. |


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Role.create.aio()`.
```python
def create(
    cls,
    name: str,
    description: str,
    actions: list[str] | None,
) -> Role
```
Create a new role.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `description` | `str` | |
| `actions` | `list[str] \| None` | |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Role.delete.aio()`.
```python
def delete(
    cls,
    name: str,
)
```
Delete a role.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Role.get.aio()`.
```python
def get(
    cls,
    name: str,
) -> Role
```
Get a role by name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Role.listall.aio()`.
```python
def listall(
    cls,
    limit: int,
) -> AsyncIterator[Role]
```
List all roles in the organization.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | |

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
> `result = await Role.update.aio()`.
```python
def update(
    cls,
    name: str,
    description: str,
    actions: list[str] | None,
)
```
Update a role.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `description` | `str` | |
| `actions` | `list[str] \| None` | |

