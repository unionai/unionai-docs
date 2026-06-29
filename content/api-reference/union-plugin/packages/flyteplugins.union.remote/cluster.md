---
title: Cluster
version: 0.4.3
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
| `assigned_config_id` | `str` |  |
| `bucket_name` | `str` |  |
| `bucket_region` | `str` |  |
| `build_time` | `str` |  |
| `build_version` | `str` |  |
| `capacity` | `str` | Compact capacity for table view: ``'64c/512G/8g'`` (cpu/memory/gpu).  Returns an empty string when the cluster reports no capacity (e.g. disabled or never-reported clusters) — table renderers should display that as ``—``. Memory is rounded to GiB when ≥ 1 GiB, otherwise reported in MiB. The GPU segment is omitted when the cluster has no GPUs. |
| `cloud_host_name` | `str` |  |
| `config_drift` | `bool` | True when the cluster has not yet synced to the assigned config. |
| `dataplane_ingress_enabled` | `bool` |  |
| `gcp_project_id` | `str` |  |
| `git_branch` | `str` |  |
| `health` | `str` |  |
| `health_display` | `str` |  |
| `helm_app_version` | `str` |  |
| `helm_chart_version` | `str` |  |
| `metadata_bucket_prefix` | `str` |  |
| `monitoring_info` | `list[dict]` |  |
| `name` | `str` |  |
| `operator_app_id` | `str` |  |
| `organization` | `str` |  |
| `pools` | `list[str]` | Names of the cluster pools this cluster belongs to. |
| `queues` | `list[dict]` |  |
| `state` | `str` |  |
| `storage_type` | `str` |  |
| `synced_at` | `str` |  |
| `synced_config_id` | `str` |  |
| `tunnel_status` | `str` |  |
| `tunnel_status_display` | `str` |  |
| `tunnel_url` | `str` |  |
| `unhealthy_reasons` | `list[str]` |  |
| `user_role` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Register a new cluster in the organization. |
| [`delete()`](#delete) | Delete a cluster by name. |
| [`get()`](#get) | Get a cluster by name. |
| [`listall()`](#listall) | List all clusters in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Cluster.create.aio()`.
```python
def create(
    cls,
    name: str,
    cluster_pool_name: str,
)
```
Register a new cluster in the organization.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | Cluster name. |
| `cluster_pool_name` | `str` | Optional cluster pool to associate the cluster with. |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Cluster.delete.aio()`.
```python
def delete(
    cls,
    name: str,
)
```
Delete a cluster by name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

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

