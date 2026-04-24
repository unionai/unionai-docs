---
title: User
version: 0.2.2
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# User

**Package:** `flyteplugins.union.remote`

Represents a Union user.


## Parameters

```python
class User(
    pb2: UserPb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `UserPb2` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `email` | `str` |  |
| `first_name` | `str` |  |
| `last_name` | `str` |  |
| `subject` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Create (invite) a new user. |
| [`delete()`](#delete) | Delete a user. |
| [`get()`](#get) | Get a user by subject identifier. |
| [`listall()`](#listall) | List all users in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await User.create.aio()`.
```python
def create(
    cls,
    first_name: str,
    last_name: str,
    email: str,
) -> User
```
Create (invite) a new user.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `first_name` | `str` | The user's first name. |
| `last_name` | `str` | The user's last name. |
| `email` | `str` | The user's email address. |

**Returns:** User instance for the newly created user.

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await User.delete.aio()`.
```python
def delete(
    cls,
    subject: str,
)
```
Delete a user.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `subject` | `str` | |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await User.get.aio()`.
```python
def get(
    cls,
    subject: str,
) -> User
```
Get a user by subject identifier.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `subject` | `str` | |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await User.listall.aio()`.
```python
def listall(
    cls,
    limit: int,
    email: str | None,
) -> AsyncIterator[User]
```
List all users in the organization.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | Maximum number of users to return. |
| `email` | `str \| None` | Filter by email (server-side, exact match). |

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

