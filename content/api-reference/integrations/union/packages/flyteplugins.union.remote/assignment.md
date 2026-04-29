---
title: Assignment
version: 0.2.2
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# Assignment

**Package:** `flyteplugins.union.remote`

Represents role/policy assignments for an identity.


## Parameters

```python
class Assignment(
    pb2: IdentityAssignment,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `IdentityAssignment` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `policies` | `list[str]` |  |
| `roles` | `list[str]` |  |
| `subject` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Assign a policy to an identity. |
| [`get()`](#get) | Get assignments for an identity. |
| [`listall()`](#listall) | List assignments for all members in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`unassign()`](#unassign) | Unassign a policy from an identity. |


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Assignment.create.aio()`.
```python
def create(
    cls,
    user_subject: str | None,
    creds_subject: str | None,
    email: str | None,
    policy: str,
) -> Assignment
```
Assign a policy to an identity.

Exactly one of user_subject, creds_subject, or email must be provided.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `user_subject` | `str \| None` | User subject identifier. |
| `creds_subject` | `str \| None` | Client credentials application subject. |
| `email` | `str \| None` | User email for lookup. |
| `policy` | `str` | Policy name to assign. |

**Returns:** Assignment for the identity after the policy is assigned.

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Assignment.get.aio()`.
```python
def get(
    cls,
    user_subject: str | None,
    creds_subject: str | None,
) -> Assignment
```
Get assignments for an identity.

One of user_subject or creds_subject must be provided.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `user_subject` | `str \| None` | |
| `creds_subject` | `str \| None` | |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Assignment.listall.aio()`.
```python
def listall(
    cls,
    limit: int,
) -> AsyncIterator[Assignment]
```
List assignments for all members in the organization.


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

### unassign()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Assignment.unassign.aio()`.
```python
def unassign(
    cls,
    user_subject: str | None,
    creds_subject: str | None,
    policy: str,
)
```
Unassign a policy from an identity.

One of user_subject or creds_subject must be provided.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `user_subject` | `str \| None` | |
| `creds_subject` | `str \| None` | |
| `policy` | `str` | |

