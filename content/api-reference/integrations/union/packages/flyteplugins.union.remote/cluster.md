---
title: Cluster
version: 0.2.2
variants: +flyte +union
layout: py_api
---

# Cluster

**Package:** `flyteplugins.union.remote`

Represents a Union cluster.


## Parameters

```python
class Cluster(
    pb2: ClusterPb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `ClusterPb2` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `health` | `None` |  |
| `health_display` | `None` |  |
| `monitoring_info` | `None` |  |
| `name` | `None` |  |
| `organization` | `None` |  |
| `state` | `None` |  |
| `tunnel_status` | `None` |  |
| `tunnel_status_display` | `None` |  |
| `tunnel_url` | `None` |  |
| `unhealthy_reasons` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Get a cluster by name. |
| [`listall()`](#listall) | List all clusters in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Cluster.get.aio()`.
```python
def get(
    cls,
    name: str,
) -> Cluster
```
Get a cluster by name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Cluster.listall.aio()`.
```python
def listall(
    cls,
    limit: int,
) -> AsyncIterator[Cluster]
```
List all clusters in the organization.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | Maximum number of clusters to return. |

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

