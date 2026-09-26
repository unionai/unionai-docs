---
title: Cluster
description: "Represents a Union cluster."
icon: braces
version: 0.14.0
variants: -flyte +union
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
| `created_by` | `str` | Who created the object, or "" when the server did not say or sent only a subject. |
| `dataplane_ingress_enabled` | `bool` |  |
| `deleted_at` | `str` | When the cluster was soft-deleted, or "" if it is live. |
| `drain_display` | `str` | Detailed drain state shown by the single-cluster view. |
| `drain_short` | `str` | Compact drain state used by the cluster list view. |
| `drain_state` | `str` | Control-plane lifecycle: ``active``, ``draining``, ``drained``, ``deleting`` or ``deleted``.  Distinct from ``state``, which the cluster's dataplane reports about itself: this one is owned and written by the control plane through ``Cluster.drain`` / ``Cluster.activate`` / ``Cluster.delete``. A cluster whose state never changed reads as ``active``. |
| `drain_status` | `ClusterDrainStatus` | Control-plane-owned drain status reported for this cluster.  Protobuf message fields return their default instance when unset, so callers can safely inspect this value for clusters created before the drain lifecycle was introduced. |
| `gcp_project_id` | `str` |  |
| `git_branch` | `str` |  |
| `has_authorship` | `bool` | True when at least one of ``created_by`` / ``updated_by`` renders as something readable. |
| `health` | `str` |  |
| `health_display` | `str` |  |
| `helm_app_version` | `str` |  |
| `helm_chart_version` | `str` |  |
| `is_deleted` | `bool` |  |
| `metadata_bucket_prefix` | `str` |  |
| `monitoring_info` | `list[dict]` |  |
| `name` | `str` |  |
| `operator_app_id` | `str` |  |
| `organization` | `str` |  |
| `pool` | `str` | Name of the cluster pool this cluster belongs to, if any. |
| `queues` | `list[dict]` |  |
| `state` | `str` |  |
| `storage_type` | `str` |  |
| `synced_at` | `str` |  |
| `synced_config_id` | `str` |  |
| `tunnel_status` | `str` |  |
| `tunnel_status_display` | `str` |  |
| `tunnel_url` | `str` |  |
| `unhealthy_reasons` | `list[str]` |  |
| `updated_by` | `str` | Who last changed the object (spec, state, deletion or undeletion), or "" as above. |
| `user_role` | `str` |  |

## Methods

| Method | Description |
|-|-|
| [`activate()`](#activate) | Re-activate a draining or drained cluster. |
| [`authorship_rows()`](#authorship_rows) | Label / value rows for a detail view; empty when nothing renders. |
| [`create()`](#create) | Register a new cluster in the organization. |
| [`delete()`](#delete) | Delete a cluster. |
| [`drain()`](#drain) | Begin draining a cluster — it stops receiving new work. |
| [`get()`](#get) | Get a cluster by name. |
| [`listall()`](#listall) | List all clusters in the organization. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`undelete()`](#undelete) | Restore a soft-deleted cluster. |
| [`update()`](#update) | Move a cluster to a different cluster pool. |


### activate()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Cluster.activate.aio()`.
```python
def activate(
    cls,
    name: str,
) -> Cluster
```
Re-activate a draining or drained cluster.

Activation resets the recorded drain progress; the cluster starts
receiving new work again, and its co-named queue is activated with it —
even when that queue had been drained on its own. A queue that was
*deleted* on its own is not brought back by the cluster: undelete it
separately (``Queue.undelete``). A ``deleting`` or ``deleted`` cluster
cannot be activated.

Returns the cluster as the request left it.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### authorship_rows()

```python
def authorship_rows()
```
Label / value rows for a detail view; empty when nothing renders.


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Cluster.create.aio()`.
```python
def create(
    cls,
    name: str,
    cluster_pool_name: str = '',
)
```
Register a new cluster in the organization.

Creating a cluster also creates its *implicit* queue: a queue with the
same name, in the same pool, routing to this cluster and nothing else.
That queue's routing and pool are managed by the cluster from then on and
cannot be changed through ``Queue.update``.

A cluster therefore owns its name in the queue namespace: creating a
cluster whose name is already taken by a queue is rejected, and so is
``Queue.create`` for a name a cluster owns. The name ``default`` is
reserved (it collides with the organization's default queue) and cannot
be used for a cluster at all.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | Cluster name. |
| `cluster_pool_name` | `str` | Optional cluster pool to associate the cluster with. Defaults to the reserved pool named ``default``; any other pool must already exist and be live. When the default pool has been deleted, this is required — name a pool or undelete the default pool. |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Cluster.delete.aio()`.
```python
def delete(
    cls,
    name: str,
) -> Cluster
```
Delete a cluster. What it does depends on the cluster's state:

- ``drained``: the system has already confirmed the cluster holds no
  work, so it is soft-deleted right away and comes back ``deleted``;
- ``active`` or ``draining``: it comes back ``deleting`` — the system
  disconnects its workers, reschedules its runs on other clusters, and
  moves it to ``deleted`` once that cleanup is done. Deletion does not
  wait for running work and cannot be cancelled; pods left on the
  dataplane are the caller's responsibility. Apps assigned to the
  cluster are ignored: deletion neither evicts nor reassigns them, so
  any app pods still on the dataplane are the caller's to clean up like
  the rest of its pods.

``deleted`` is a soft delete: the record is kept, the cluster disappears
from ``Cluster.get`` / ``Cluster.listall``, is no longer routed to, and
stops accepting heartbeats and status updates — but it keeps its name
reserved: ``Cluster.create`` with the same name is rejected until the
cluster is undeleted. Use ``Cluster.listall(deleted=True)`` to find
deleted clusters and ``Cluster.undelete`` to restore one. Deleting a
``deleting`` or ``deleted`` cluster is rejected.

The cluster's co-named implicit queue is deleted with it, by the same
rule applied to the queue's own state: a drained queue goes straight to
deleted, any other live state goes to deleting; one already deleted on
its own is left as it is. Any other live queue that explicitly pins the
cluster blocks the delete and has to be unpinned first; a queue that is
already soft-deleted does not block it and keeps its reference, so it
can only be undeleted once the cluster is.

The cluster's nodepool inventory is dropped when the cluster reaches
``deleted`` and is *not* restored by ``Cluster.undelete``.

Returns the cluster as the request left it (``deleted`` or ``deleting``).


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### drain()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Cluster.drain.aio()`.
```python
def drain(
    cls,
    name: str,
) -> Cluster
```
Begin draining a cluster — it stops receiving new work.

Work already on the cluster keeps running, and the drain can be
reverted with ``Cluster.activate`` at any time. To take a cluster out
of service without waiting for its work, delete it instead
(``Cluster.delete``).

A drain cannot start while apps are assigned to the cluster, and the
cluster's co-named implicit queue is set to draining with it (a queue
already deleted on its own is left as it is). Any other live queue
explicitly pinning this cluster blocks the drain and must be unpinned
first. A ``deleting`` or ``deleted`` cluster cannot be drained.

The drain completes asynchronously: watch ``Cluster.get(name).drain_state``
until it reaches ``drained``. A drained cluster can be moved to another
pool, deleted, or activated again.

Returns the cluster as the request left it.


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

Soft-deleted clusters are returned too, carrying ``deleted_at``, so a
deleted cluster's record stays inspectable after deletion.


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
    limit: int = 100,
    deleted: bool = False,
) -> AsyncIterator[Cluster]
```
List all clusters in the organization.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | Maximum number of clusters to return. |
| `deleted` | `bool` | When True the server returns *only* soft-deleted clusters (it filters on the ``deleted_at`` marker, which live clusters never carry) — that is how a deleted cluster is discovered before ``Cluster.undelete``. |

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
> `result = await Cluster.undelete.aio()`.
```python
def undelete(
    cls,
    name: str,
) -> Cluster
```
Restore a soft-deleted cluster.

The cluster comes back with the spec, status and pool assignment it had
when it was deleted, always in the ``drained`` state — whatever state
its deletion started from — and must be activated with
``Cluster.activate`` before it takes work again. A ``deleting`` cluster
cannot be undeleted: its deletion has to finish first.

Its co-named implicit queue, if deleted, is restored with it, also
``drained`` — including when that queue had been deleted on its own
before the cluster was. Undeleting the cluster is in fact the *only*
way to bring that queue back: while the cluster is deleted
``Queue.undelete`` refuses it, since the queue would have no cluster to
route to. A co-named queue still ``deleting`` (its own teardown not yet
confirmed) is not touched — it finishes deleting on its own.

The cluster's pool must not itself be soft-deleted; undelete the pool
first (see ``ClusterPool.undelete``). Undeleting a cluster that is not
deleted is rejected by the server.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

### update()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Cluster.update.aio()`.
```python
def update(
    cls,
    name: str,
    cluster_pool_name: str = '',
)
```
Move a cluster to a different cluster pool.

That is the only thing this call changes: everything else about a cluster
is either fixed at creation or reported by its dataplane.

The cluster must exist and not be soft-deleted, and ``cluster_pool_name``
must name a *different* pool — re-assigning a cluster to the pool it is
already in is rejected as already existing. The target pool must already
exist and be live; a move never creates a pool, the reserved ``default``
one included.

The cluster's co-named implicit queue moves with it, so the move carries
the same precondition repointing a queue at another pool does: that queue
must be ``drained`` first (see ``Queue.drain``). Any other live queue that
explicitly pins the cluster blocks the move and must be unpinned first; a
soft-deleted one does not block it and has the cluster dropped from its
routing instead. The cluster and its queue change pool in one
transaction — either both move or neither does.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | Cluster name. |
| `cluster_pool_name` | `str` | Cluster pool to move the cluster to. |

