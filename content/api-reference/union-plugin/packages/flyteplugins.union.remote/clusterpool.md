---
title: ClusterPool
version: 0.4.3
variants: +flyte +union
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
| `image_registry` | `str` |  |
| `member_clusters` | `list[str]` |  |
| `name` | `str` |  |
| `object_store_endpoint` | `str` |  |
| `object_store_uri` | `str` |  |
| `organization` | `str` |  |
| `secret_store_locator` | `str` |  |
| `secret_store_type` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Create a cluster pool. |
| [`delete()`](#delete) | Delete a cluster pool by name. |
| [`get()`](#get) | Get a cluster pool by name. |
| [`listall()`](#listall) | List all cluster pools in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`update()`](#update) | Update a cluster pool's configuration. |


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
    object_store_endpoint: str,
    secret_store_locator: str,
    image_registry: str,
    member_clusters: list[str] | None,
)
```
Create a cluster pool.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | Pool name. |
| `object_store_uri` | `str` | Object store URI (required), e.g. ``s3://my-bucket/prefix``. |
| `secret_store_type` | `str` | Secret store type (required). One of :data:`SECRET_STORE_TYPES`. |
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
Delete a cluster pool by name.


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
    limit: int,
) -> AsyncIterator[ClusterPool]
```
List all cluster pools in the organization.


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
> `result = await ClusterPool.update.aio()`.
```python
def update(
    cls,
    name: str,
    object_store_uri: str,
    secret_store_type: str,
    object_store_endpoint: str,
    secret_store_locator: str,
    image_registry: str,
    member_clusters: list[str] | None,
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

