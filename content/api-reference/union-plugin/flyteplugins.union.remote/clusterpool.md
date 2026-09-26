---
title: ClusterPool
description: "Represents a Union cluster pool — the configuration shared by its member clusters."
icon: braces
version: 0.14.0
variants: -flyte +union
layout: py_api
---

# ClusterPool

**Package:** `flyteplugins.union.remote`

Represents a Union cluster pool — the configuration shared by its member clusters.


## Parameters

```python
class ClusterPool(
    pb2: ClusterPoolPb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `ClusterPoolPb2` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `created_by` | `str` | Who created the object, or "" when the server did not say or sent only a subject. |
| `deleted_at` | `str` | When the pool was soft-deleted, or "" if it is live. |
| `has_authorship` | `bool` | True when at least one of ``created_by`` / ``updated_by`` renders as something readable. |
| `image_registry` | `str` |  |
| `is_deleted` | `bool` |  |
| `member_clusters` | `list[str]` |  |
| `name` | `str` |  |
| `object_store_endpoint` | `str` |  |
| `object_store_uri` | `str` |  |
| `organization` | `str` |  |
| `secret_store_locator` | `str` |  |
| `secret_store_type` | `str` |  |
| `updated_by` | `str` | Who last changed the object (spec, state, deletion or undeletion), or "" as above. |

## Methods

| Method | Description |
|-|-|
| [`authorship_rows()`](#authorship_rows) | Label / value rows for a detail view; empty when nothing renders. |
| [`create()`](#create) | Create a cluster pool. |
| [`delete()`](#delete) | Soft-delete a cluster pool by name. |
| [`get()`](#get) | Get a cluster pool by name. |
| [`listall()`](#listall) | List all cluster pools in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`undelete()`](#undelete) | Restore a soft-deleted cluster pool. |
| [`update()`](#update) | Update a cluster pool's configuration. |


### authorship_rows()

```python
def authorship_rows()
```
Label / value rows for a detail view; empty when nothing renders.


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ClusterPool.create.aio()`.
```python
def create(
    cls,
    name: str,
    object_store_uri: str,
    secret_store_type: str,
    object_store_endpoint: str = '',
    secret_store_locator: str = '',
    image_registry: str = '',
    member_clusters: list[str] | None = None,
)
```
Create a cluster pool.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | Pool name. |
| `object_store_uri` | `str` | Object store URI (required), e.g. ``s3://my-bucket/prefix``. |
| `secret_store_type` | `str` | Secret store type (required). One of `SECRET_STORE_TYPES`. |
| `object_store_endpoint` | `str` | Optional custom object store endpoint. |
| `secret_store_locator` | `str` | Optional secret store path/identifier. |
| `image_registry` | `str` | Optional image registry locator. |
| `member_clusters` | `list[str] \| None` | Optional cluster names to include in the pool. |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ClusterPool.delete.aio()`.
```python
def delete(
    cls,
    name: str,
)
```
Soft-delete a cluster pool by name.

The record is kept but marked deleted: the pool disappears from
``ClusterPool.get`` / ``ClusterPool.listall`` and can no longer be
assigned to a cluster or a queue. It keeps its name reserved —
``ClusterPool.create`` with the same name is rejected until the pool is
undeleted. Use ``ClusterPool.listall(deleted=True)`` to find deleted
pools and ``ClusterPool.undelete`` to restore one.

The pool must be empty: no member clusters and no live queues assigned to
it, otherwise the server rejects the request. Queues that are themselves
soft-deleted do not block the delete, but they can only be undeleted once
the pool is. Deleting an already deleted pool is rejected. The reserved
``default`` pool follows the same rules: deleting it requires draining
and deleting its ``default`` queue first, and while the pool is deleted,
``Cluster.create`` with no pool name is rejected instead of falling back
to it.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ClusterPool.get.aio()`.
```python
def get(
    cls,
    name: str,
) -> ClusterPool
```
Get a cluster pool by name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ClusterPool.listall.aio()`.
```python
def listall(
    cls,
    limit: int = 100,
    deleted: bool = False,
) -> AsyncIterator[ClusterPool]
```
List all cluster pools in the organization.

With ``deleted=True`` the server returns *only* soft-deleted pools (it
filters on the ``deleted_at`` marker, which live pools never carry) —
that is how a deleted pool is discovered before ``ClusterPool.undelete``.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | |
| `deleted` | `bool` | |

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

### undelete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ClusterPool.undelete.aio()`.
```python
def undelete(
    cls,
    name: str,
) -> ClusterPool
```
Restore a soft-deleted cluster pool.

The pool comes back with the config it had when it was deleted. Queues
and clusters that were soft-deleted while assigned to it stay deleted and
can now be undeleted too. Undeleting a pool that is not deleted is
rejected by the server.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### update()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ClusterPool.update.aio()`.
```python
def update(
    cls,
    name: str,
    object_store_uri: str,
    secret_store_type: str,
    object_store_endpoint: str = '',
    secret_store_locator: str = '',
    image_registry: str = '',
    member_clusters: list[str] | None = None,
)
```
Update a cluster pool's configuration.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `object_store_uri` | `str` | |
| `secret_store_type` | `str` | |
| `object_store_endpoint` | `str` | |
| `secret_store_locator` | `str` | |
| `image_registry` | `str` | |
| `member_clusters` | `list[str] \| None` | |

