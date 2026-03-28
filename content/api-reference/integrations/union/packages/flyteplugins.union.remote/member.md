---
title: Member
version: 0.2.1
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# Member

**Package:** `flyteplugins.union.remote`

Represents a Union organization member (user or application).


## Parameters

```python
class Member(
    pb2: EnrichedIdentity,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `EnrichedIdentity` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `identity_type` | `None` |  |
| `is_application` | `None` |  |
| `is_user` | `None` |  |
| `name` | `None` |  |
| `subject` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`listall()`](#listall) | List all members in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Member.listall.aio()`.
```python
def listall(
    cls,
) -> AsyncIterator[Member]
```
List all members in the organization.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |

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

