---
title: flyteplugins.union.io
version: 0.4.0
variants: +flyte +union
layout: py_api
---

# flyteplugins.union.io

Persistent, mountable :class:`Volume` type for the Flyte SDK v2.

A ``Volume`` materializes as a mountable filesystem inside a task pod, backed
by an object-store bucket (immutable data chunks) plus a metadata index. The
index rides through the normal Flyte literal system as a Pydantic model, so
lineage, caching, fork, and clone are first-class.

Public surface::

    from flyteplugins.union.io import ROVolume, RWVolume, Volume

The mount stack (JuiceFS client, metadata stores, subprocess plumbing) lives
under :mod:`flyteplugins.union.io._internal` and is not part of the public API.
## Directory

### Classes

| Class | Description |
|-|-|
| [`ActionRef`](../flyteplugins.union.io/actionref) | Provenance: the action (one task execution within a run) that. |
| [`ROVolume`](../flyteplugins.union.io/rovolume) | Immutable, versioned volume — PRD §Core Concepts. |
| [`RWVolume`](../flyteplugins.union.io/rwvolume) | Mutable working copy — PRD §Core Concepts. |
| [`Volume`](../flyteplugins.union.io/volume) | A persistent volume identified by its metadata index. |

### Methods

| Method | Description |
|-|-|
| [`with_high_throughput_volume_deps()`](#with_high_throughput_volume_deps) | Provision the in-pod Redis metadata daemon on ``base`` for Volumes that. |


## Methods

#### with_high_throughput_volume_deps()

```python
def with_high_throughput_volume_deps(
    base: Image,
) -> Image
```
Provision the in-pod Redis metadata daemon on ``base`` for Volumes that
use ``metadata_store_type="redis"``.

Returns a new :class:`flyte.Image` that, on top of ``base``:

* installs ``redis-server`` / ``redis-tools`` (the in-pod daemon the Redis
  store runs against), and
* sets ``UNION_VOLUME_METADATA_STORE=redis`` so volumes created in this
  image via :meth:`Volume.new` / :meth:`Volume.empty` *default* to Redis
  without the caller passing ``metadata_store_type=`` each time (still
  overridable per-volume).

This is the **only** image helper Volumes need. The default SQLite store
runs in-process and mounts via raw syscalls under ``CAP_SYS_ADMIN`` +
``/dev/fuse`` (``enable_fuse_mount=True`` on the
:class:`flyte.TaskEnvironment`) — so a plain image that pip-installs
``flyteplugins-union`` Just Works for it, no extra apt packages.


| Parameter | Type | Description |
|-|-|-|
| `base` | `Image` | |

