---
title: flyteplugins.union.io
version: 0.4.3
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
| [`with_high_throughput_volume_deps()`](#with_high_throughput_volume_deps) | Prepare ``base`` for high-throughput (Redis-backed) Volumes. |


## Methods

#### with_high_throughput_volume_deps()

```python
def with_high_throughput_volume_deps(
    base: Image,
) -> Image
```
Prepare ``base`` for high-throughput (Redis-backed) Volumes.

Returns a new :class:`flyte.Image` that, on top of ``base``:

* installs ``fuse3`` — the ``fusermount3`` userspace helper JuiceFS execs to
  mount the FUSE filesystem. *Every* Volume mount needs this under the
  default unprivileged :meth:`flyte.PodTemplate.allow_fuse`; without it the
  mount client exits immediately with ``fuse: fuse is not installed``;
* installs ``redis-server`` / ``redis-tools`` (the in-pod daemon the Redis
  store runs against), and
* sets ``UNION_VOLUME_METADATA_STORE=redis`` so volumes created in this
  image via :meth:`Volume.new` / :meth:`Volume.empty` *default* to Redis
  without the caller passing ``metadata_store_type=`` each time (still
  overridable per-volume).

With this helper the image is complete: just add
``pod_template=flyte.PodTemplate().allow_fuse()`` to the
:class:`flyte.TaskEnvironment` and Volumes mount and run. For the default
SQLite store you don't need Redis, but you *do* still need ``fuse3`` —
install it with ``image.with_apt_packages("fuse3")`` (see :meth:`Volume.mount`).


| Parameter | Type | Description |
|-|-|-|
| `base` | `Image` | |

