---
title: Environment
description: "One environment version with its full spec, scaling and per-cluster status snapshots."
icon: braces
version: 0.13.0
variants: -flyte +union
layout: py_api
---

# Environment

**Package:** `flyteplugins.union.remote`

One environment version with its full spec, scaling and per-cluster status snapshots.



## Parameters

```python
class Environment(
    pb2: GetEnvironmentResponse,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `GetEnvironmentResponse` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `actions` | `list[tuple[str, EnvironmentAction]]` | Every reported pending/assigned action as ``(cluster, action)``. |
| `cluster_statuses` | `list[EnvironmentClusterStatus]` |  |
| `id` | `EnvironmentId` |  |
| `name` | `str` |  |
| `recent_worker_errors` | `list[tuple[str, WorkerError]]` |  |
| `scaling` | `None` |  |
| `spec` | `None` |  |
| `state` | `str` |  |
| `version` | `str` |  |
| `workers` | `list[tuple[str, Worker]]` | Every reported worker as ``(cluster, worker)``. |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Get one environment version with its full per-cluster status. |
| [`listall()`](#listall) | List environment versions in a project/domain, most recently active version first per name. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Environment.get.aio()`.
```python
def get(
    cls,
    name: str,
    version: str | None = None,
    project: str | None = None,
    domain: str | None = None,
) -> Environment
```
Get one environment version with its full per-cluster status.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | Environment name. |
| `version` | `str \| None` | Version to get. Defaults to the name's most recently active version. |
| `project` | `str \| None` | Project of the environment. Defaults to the configured project. |
| `domain` | `str \| None` | Domain of the environment. Defaults to the configured domain. |

**Raises**

| Exception | Description |
|-|-|
| `ValueError` | No version is given and no environment with this name exists. |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Environment.listall.aio()`.
```python
def listall(
    cls,
    project: str | None = None,
    domain: str | None = None,
    name: str | None = None,
    limit: int = 100,
) -> AsyncIterator[EnvironmentVersion]
```
List environment versions in a project/domain, most recently active version first per name.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `project` | `str \| None` | Project to list. Defaults to the configured project. |
| `domain` | `str \| None` | Domain to list. Defaults to the configured domain. |
| `name` | `str \| None` | Only yield versions of this environment name. The server has no name filter, so this pages through every environment client-side. |
| `limit` | `int` | Maximum number of versions to yield. |

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

