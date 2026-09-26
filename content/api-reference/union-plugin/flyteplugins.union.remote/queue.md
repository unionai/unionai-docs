---
title: Queue
description: "Represents a Union scheduling queue."
icon: braces
version: 0.14.0
variants: -flyte +union
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
| `cluster_managed` | `bool` | True for the queue a cluster owns — the co-named one created with it.  Such a queue's clusters and cluster pool belong to the cluster and cannot be changed through ``Queue.update``; move the cluster with ``Cluster.update`` instead. Everything else stays editable. |
| `cluster_pool` | `str` |  |
| `clusters` | `list[str]` |  |
| `created_at` | `str` |  |
| `created_by` | `str` | Who created the object, or "" when the server did not say or sent only a subject. |
| `deleted_at` | `str` | When the queue was soft-deleted, or "" if it is live. |
| `depth` | `int` |  |
| `domain` | `str` |  |
| `fairness` | `str` |  |
| `has_authorship` | `bool` | True when at least one of ``created_by`` / ``updated_by`` renders as something readable. |
| `is_deleted` | `bool` |  |
| `max_resources` | `dict[str, str]` | Resource cap on the queue's dispatched, not-yet-completed actions, as ``{name: quantity}``.  Only the dimensions the cap names are present; an absent dimension is unlimited. An empty dict means the queue has no cap at all. |
| `name` | `str` |  |
| `organization` | `str` |  |
| `priority` | `str` |  |
| `project` | `str` |  |
| `run_concurrency` | `int` |  |
| `scheduling` | `str` | What the resource gate does when the head of the queue does not fit.  ``strict_fifo`` holds the line behind it; ``greedy_capacity`` skips it and keeps packing. An unset field reads as ``strict_fifo`` — that is what the scheduler applies. |
| `state_generation` | `int` | Server-owned counter of queue *state* changes (spec updates don't touch it).  State-changing requests carry the generation the caller observed, so a delayed request cannot apply to a state the caller never saw. Starts at 1 on creation; queues created before the counter existed read 0 until their first transition. |
| `status` | `str` |  |
| `updated_at` | `str` |  |
| `updated_by` | `str` | Who last changed the object (spec, state, deletion or undeletion), or "" as above. |

## Methods

| Method | Description |
|-|-|
| [`activate()`](#activate) | Re-activate a draining or drained queue. |
| [`authorship_rows()`](#authorship_rows) | Label / value rows for a detail view; empty when nothing renders. |
| [`create()`](#create) | Create a new queue. |
| [`delete()`](#delete) | Request deletion of a queue. |
| [`details()`](#details) | Get a single point-in-time metrics snapshot for a queue. |
| [`drain()`](#drain) | Begin draining a queue — stops new submissions, lets in-flight work complete. |
| [`get()`](#get) | Get a queue by name. |
| [`listall()`](#listall) | List queues in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`undelete()`](#undelete) | Restore a soft-deleted queue with the spec it had when it was deleted. |
| [`update()`](#update) | Update a queue's configuration. |
| [`watch()`](#watch) | Stream real-time queue metrics via gRPC server streaming. |
| [`watch_pool()`](#watch_pool) | Stream metrics for every live queue of the given pools (all pools when unset). |


### activate()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.activate.aio()`.
```python
def activate(
    cls,
    name: str,
    org: str | None = None,
    domain: str = '',
    project: str = '',
) -> Queue
```
Re-activate a draining or drained queue.

A ``deleting`` or ``deleted`` queue cannot be activated, and activating
a cluster-managed queue is rejected while its cluster is ``draining``
or ``drained`` — the queue follows its cluster.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |

### authorship_rows()

```python
def authorship_rows()
```
Label / value rows for a detail view; empty when nothing renders.


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.create.aio()`.
```python
def create(
    cls,
    name: str,
    org: str | None = None,
    domain: str = '',
    project: str = '',
    run_concurrency: int,
    action_concurrency: int,
    depth: int = 10000,
    priority: str = 'medium',
    fairness: str = 'round_robin',
    clusters: list[str] | None = None,
    cluster_pool: str | None = None,
    max_resources: Mapping[str, object] | None = None,
    scheduling: str = 'strict_fifo',
) -> Queue
```
Create a new queue.

``cluster_pool`` is optional: when unset, the server places the queue in
the pool named ``default``. Use ``Queue.update`` to move the queue to a
different pool later — that requires the queue to be drained first.

``clusters`` defaults to ``["*"]``, routing to every cluster in the
assigned pool; the wildcard cannot be mixed with explicit cluster names.

``max_resources`` caps the summed resource request of the queue's
dispatched, not-yet-completed actions, as ``{name: quantity}`` — e.g.
``{"gpu": "8", "memory": "512Gi"}``. Names are ``cpu``, ``gpu``,
``memory`` and ``ephemeral_storage``; values are Kubernetes quantities.
A dimension not named is unlimited (``0`` is a hard cap, not "unset");
``None`` or ``{}`` means no cap.

``scheduling`` is what the resource gate does when the action at the head
of the queue does not fit the remaining capacity: ``strict_fifo`` (the
default, and what an unset field means) holds the line behind it, while
``greedy_capacity`` skips it and keeps packing what does fit.

A taken name is rejected as already existing — an existing queue, a
soft-deleted one, or a cluster's co-named implicit queue (see
``Cluster.create``). Temporarily, only organization-scoped queues can
be created: the server rejects an id carrying ``project`` or ``domain``.


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
| `cluster_pool` | `str \| None` | |
| `max_resources` | `Mapping[str, object] \| None` | |
| `scheduling` | `str` | |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.delete.aio()`.
```python
def delete(
    cls,
    name: str,
    org: str | None = None,
    domain: str = '',
    project: str = '',
) -> Queue
```
Request deletion of a queue. What it does depends on the queue's state:

- ``drained``: the system has already confirmed the queue holds no
  work, so it is soft-deleted right away and comes back ``deleted``;
- ``draining``: the queue may still hold work, so it comes back
  ``deleting`` — it stays listed, and the system moves it to
  ``deleted`` once its remaining state is cleaned up. Deletion cannot
  be cancelled; a ``deleted`` queue can be brought back with
  ``Queue.undelete``;
- ``active``: rejected — a queue that is accepting work must first be
  drained (see ``Queue.drain``), so deleting a serving queue always
  takes two deliberate calls;
- ``deleting`` or ``deleted``: rejected, the deletion is already under
  way or done.

A deleted queue disappears from ``Queue.listall`` and is no longer
scheduled on — ``Queue.get`` still returns it, carrying ``deleted_at`` —
but it keeps its name reserved: ``Queue.create`` with the same name is
rejected until the queue is undeleted. Use ``Queue.listall(deleted=True)``
to find deleted queues and ``Queue.undelete`` to restore one.

A queue referenced as ``run.default_queue`` in settings at any scope
cannot be deleted until those settings are updated or unset. The
reserved ``default`` queue is no exception: it can be drained and
deleted like any other queue, but while it is deleted, runs that name
no queue (and have no ``run.default_queue`` setting) are rejected at
creation.

Returns the queue as the request left it (``deleted`` or ``deleting``).


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |

### details()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.details.aio()`.
```python
def details(
    cls,
    name: str,
    org: str | None = None,
    domain: str = '',
    project: str = '',
) -> dict
```
Get a single point-in-time metrics snapshot for a queue.

Reads the first message from the WatchQueueMetrics stream. For continuous
updates, use ``Queue.watch``. Works for a queue in any state, drained
included.


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
    org: str | None = None,
    domain: str = '',
    project: str = '',
) -> Queue
```
Begin draining a queue — stops new submissions, lets in-flight work complete.

Any live queue can be drained, including one referenced as
``run.default_queue`` in settings at any scope: a draining or drained
queue still resolves, and runs that land on a queue that is not
accepting work are rejected at creation with an actionable error. Only
deleting such a queue is refused (see ``Queue.delete``). A ``deleting``
or ``deleted`` queue cannot be drained. Use ``Queue.watch`` to follow
the drain to completion.


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
    org: str | None = None,
    domain: str = '',
    project: str = '',
) -> Queue
```
Get a queue by name.

Soft-deleted queues are returned too, carrying ``deleted_at``, so a
deleted queue's details stay reachable.


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
    org: str | None = None,
    limit: int = 100,
    deleted: bool = False,
    state: str | None = None,
) -> AsyncIterator[Queue]
```
List queues in the organization.

With ``deleted=True`` the server returns *only* soft-deleted queues (it
filters on the ``deleted_at`` marker, which live queues never carry) —
that is how a deleted queue is discovered before ``Queue.undelete``.

``state`` ("active", "draining", "drained", "deleting" or "deleted")
narrows the listing to queues in that state, server-side. A ``deleting``
queue is still live and listed like any other; a ``deleted`` one shows
up only under ``deleted=True``.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `org` | `str \| None` | |
| `limit` | `int` | |
| `deleted` | `bool` | |
| `state` | `str \| None` | |

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
> `result = await Queue.undelete.aio()`.
```python
def undelete(
    cls,
    name: str,
    org: str | None = None,
    domain: str = '',
    project: str = '',
) -> Queue
```
Restore a soft-deleted queue with the spec it had when it was deleted.

The queue always comes back in the ``drained`` state, whatever state
its deletion started from — call ``Queue.activate`` to make it accept
work again. A ``deleting`` queue cannot be undeleted: its deletion has
to finish first. Undeleting a queue that is not deleted is rejected by
the server.

Every cluster the queue routes to must be live and in the queue's pool,
and the pool itself must be live — a restored queue must never point at
something that is gone. A cluster's co-named queue therefore cannot be
undeleted while its cluster is deleted: undelete the *cluster* instead,
which brings the queue back with it (see ``Cluster.undelete``). While
the cluster is live, it undeletes like any other queue.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |

### update()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.update.aio()`.
```python
def update(
    cls,
    name: str,
    org: str | None = None,
    domain: str = '',
    project: str = '',
    run_concurrency: int | None = None,
    action_concurrency: int | None = None,
    depth: int | None = None,
    priority: str | None = None,
    fairness: str | None = None,
    clusters: list[str] | None = None,
    cluster_pool: str | None = None,
    max_resources: Mapping[str, object] | None = None,
    scheduling: str | None = None,
) -> Queue
```
Update a queue's configuration. Unset fields are read from the current spec.

``max_resources`` follows the same rule: ``None`` leaves the current cap
exactly as it is (an unrelated edit never drops it), a ``{name: quantity}``
mapping replaces it wholesale, and an empty ``{}`` removes it — the queue
becomes unlimited again. See ``Queue.create`` for the accepted names and
values. ``scheduling`` behaves like every other field: ``None`` keeps the
queue's current policy.

The server requires an explicit cluster pool on every UpdateQueue call and
rejects requests without one, so the queue's current pool is resent when
``cluster_pool`` is not given.

Passing a different ``cluster_pool`` moves the queue: the target pool must
already exist, the queue's ``clusters`` must be members of it, and the queue
must be in the ``drained`` state (see ``Queue.drain``) — the server rejects
the move otherwise.

A cluster's co-named implicit queue is the exception: its ``clusters`` and
``cluster_pool`` are managed by that cluster and any request changing
either is rejected — move the cluster with ``Cluster.update`` instead. Its
other fields (concurrency, depth, priority, fairness) stay editable.

A soft-deleted queue cannot be updated at all — undelete it first.


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
| `cluster_pool` | `str \| None` | |
| `max_resources` | `Mapping[str, object] \| None` | |
| `scheduling` | `str \| None` | |

### watch()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.watch.aio()`.
```python
def watch(
    cls,
    name: str,
    org: str | None = None,
    domain: str = '',
    project: str = '',
) -> AsyncIterator[dict]
```
Stream real-time queue metrics via gRPC server streaming.

Yields dicts shaped for the CLI watch UI: the queue's caps merged with
each ``QueueMetrics`` snapshot pushed by the server. The server controls
the cadence of updates. Works for a queue in any state — watch a
draining queue to see its in-flight runs and actions reach zero, and a
drained one to confirm it is idle before deleting or moving it.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `org` | `str \| None` | |
| `domain` | `str` | |
| `project` | `str` | |

### watch_pool()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Queue.watch_pool.aio()`.
```python
def watch_pool(
    cls,
    org: str | None = None,
    pools: list[str] | None = None,
) -> AsyncIterator[list[dict]]
```
Stream metrics for every live queue of the given pools (all pools when unset).

Yields the latest snapshot of all watched queues whenever any stream
reports. Pools are discovered from the queue listing; each pool is one
server stream, merged here.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `org` | `str \| None` | |
| `pools` | `list[str] \| None` | |

