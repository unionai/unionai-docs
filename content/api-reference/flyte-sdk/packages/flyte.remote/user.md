---
title: User
version: 2.0.6
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# User

**Package:** `flyte.remote`

Represents a user in the Flyte platform.



```python
class User(
    pb2: UserInfoResponse,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `UserInfoResponse` | |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Fetches information about the currently logged in user. |
| [`name()`](#name) | Get the name of the user. |
| [`subject()`](#subject) | Get the subject identifier of the user. |


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await User.get.aio()`.
```python
def get(
    cls,
) -> User
```
Fetches information about the currently logged in user.
Returns: A User object containing details about the user.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |

### name()

```python
def name()
```
Get the name of the user.


### subject()

```python
def subject()
```
Get the subject identifier of the user.


