---
title: Queue
version: 0.4.0
variants: +flyte +union
layout: py_api
---

# Queue

**Package:** `flyteplugins.union.remote`

Represents a Union scheduling queue.



## Parameters

```python
class Queue(
    pb2: queue_pb2.Queue,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `queue_pb2.Queue` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `action_concurrency` | `int` |  |
| `clusters` | `list[str]` |  |
| `created_at` | `str` |  |
| `depth` | `int` |  |
| `domain` | `str` |  |
| `fairness` | `str` |  |
| `name` | `str` |  |
| `organization` | `str` |  |
| `priority` | `str` |  |
| `project` | `str` |  |
| `run_concurrency` | `int` |  |
| `status` | `str` |  |
| `updated_at` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`activate()`](#activate) | Re-activate a draining or drained queue. |
| [`create()`](#create) | Create a new queue. |
| [`details()`](#details) | Get a single point-in-time metrics snapshot for a queue. |
| [`drain()`](#drain) | Begin draining a queue — stops new submissions, lets in-flight work complete. |
| [`get()`](#get) | Get a queue by name. |
| [`listall()`](#listall) | List all queues in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`update()`](#update) | Update a queue's configuration. |
| [`watch()`](#watch) | Stream real-time queue metrics via gRPC server streaming. |


### activate()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.activate.aio()`.
```python
def activate(
    cls,
    name: str,
    org: str | None,
    domain: str,
    project: str,
) -> Queue
```
Re-activate a draining or drained queue.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |

### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.create.aio()`.
```python
def create(
    cls,
    name: str,
    org: str | None,
    domain: str,
    project: str,
    run_concurrency: int,
    action_concurrency: int,
    depth: int,
    priority: str,
    fairness: str,
    clusters: list[str] | None,
) -> Queue
```
Create a new queue.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |
| `run_concurrency` | `int` | |
| `action_concurrency` | `int` | |
| `depth` | `int` | |
| `priority` | `str` | |
| `fairness` | `str` | |
| `clusters` | `list[str] \| None` | |

### details()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.details.aio()`.
```python
def details(
    cls,
    name: str,
    org: str | None,
    domain: str,
    project: str,
) -> dict
```
Get a single point-in-time metrics snapshot for a queue.

Reads the first message from the WatchQueueMetrics stream. For continuous
updates, use ``Queue.watch``.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |

### drain()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.drain.aio()`.
```python
def drain(
    cls,
    name: str,
    org: str | None,
    domain: str,
    project: str,
) -> Queue
```
Begin draining a queue — stops new submissions, lets in-flight work complete.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.get.aio()`.
```python
def get(
    cls,
    name: str,
    org: str | None,
    domain: str,
    project: str,
) -> Queue
```
Get a queue by name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.listall.aio()`.
```python
def listall(
    cls,
    org: str | None,
    limit: int,
) -> AsyncIterator[Queue]
```
List all queues in the organization.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `org` | `str \| None` | |
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
> `result = await Queue.update.aio()`.
```python
def update(
    cls,
    name: str,
    org: str | None,
    domain: str,
    project: str,
    run_concurrency: int | None,
    action_concurrency: int | None,
    depth: int | None,
    priority: str | None,
    fairness: str | None,
    clusters: list[str] | None,
) -> Queue
```
Update a queue's configuration. Unset fields are read from the current spec.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |
| `run_concurrency` | `int \| None` | |
| `action_concurrency` | `int \| None` | |
| `depth` | `int \| None` | |
| `priority` | `str \| None` | |
| `fairness` | `str \| None` | |
| `clusters` | `list[str] \| None` | |

### watch()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.watch.aio()`.
```python
def watch(
    cls,
    name: str,
    org: str | None,
    domain: str,
    project: str,
) -> AsyncIterator[dict]
```
Stream real-time queue metrics via gRPC server streaming.

Yields dicts shaped for the CLI watch UI: the queue's caps merged with
each ``QueueMetrics`` snapshot pushed by the server. The server controls
the cadence of updates.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |

