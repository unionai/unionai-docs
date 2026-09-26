---
title: flyteplugins.union.io
description: "Persistent, mountable :class:`Volume` type for the Flyte SDK v2."
icon: box-seam
version: 0.14.0
variants: -flyte +union
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
| [`ActionRef`](../flyteplugins.union.io/actionref) | Provenance: the action (one task execution within a run) that produced a particular `Volume` version, plus the output slot it was returned as. |
| [`ROVolume`](../flyteplugins.union.io/rovolume) | Immutable, versioned volume — PRD §Core Concepts. |
| [`RWVolume`](../flyteplugins.union.io/rwvolume) | Mutable working copy — PRD §Core Concepts. |
| [`Volume`](../flyteplugins.union.io/volume) | A persistent volume identified by its metadata index. |

### Methods

| Method | Description |
|-|-|
| [`allow_volumes()`](#allow_volumes) | Enable `Volume` mounts in a task pod with **zero privileges**. |
| [`with_high_throughput_volume_deps()`](#with_high_throughput_volume_deps) | Prepare ``base`` for high-throughput (Redis-backed) Volumes. |
| [`with_local_flyteplugins()`](#with_local_flyteplugins) | Package the **locally checked-out** flyteplugins-union (built to a wheel) and an optional local ``juicefs`` binary into ``base`` — for iterating on an *unreleased* plugin build against a real cluster. |


### Variables

| Property | Type | Description |
|-|-|-|
| `BROKER_CHANNEL_LABEL` | `str` |  |

## Methods

#### allow_volumes()

```python
def allow_volumes(
    pod_template: Optional['PodTemplate'] = None,
    channel_dir: str = '/uvol',
    driver: str = 'volumes.union.ai',
    primary_container_name: str = 'primary',
    staging_dir: str = '/var/run/uvol-staging',
    staging_size: Optional[str] = '2Gi',
    cache_dir: str = '/var/cache/uvol',
    cache_size: Optional[str] = None,
    shared_node_cache: bool = False,
    shared_node_cache_dir: str = '/var/cache/uvol-shared-node',
) -> 'PodTemplate'
```
Enable `Volume` mounts in a task pod with **zero privileges**.

Add this to a task's ``pod_template`` to mount Volumes without
``CAP_SYS_ADMIN`` or ``/dev/fuse``. It attaches an **ephemeral CSI
volume** served by the node mount broker: the broker premounts a FUSE
channel and the in-pod JuiceFS client *adopts its file descriptor* over a
socket — so the pod performs no ``mount(2)`` syscall and needs no
capabilities, no ``/dev/fuse``, and no ``hostPath``. `Volume.mount`
auto-detects the channel via ``$UVOL_CHANNEL_DIR`` and mounts through the
broker automatically. (Contrast `flyte.PodTemplate.allow_fuse`,
which enables an in-process mount and therefore requires CAP_SYS_ADMIN.)

``pod_template`` is modified-by-copy when given, else a fresh
`flyte.PodTemplate` is returned. The copy gains exactly what a
brokered mount needs and nothing else: the CSI channel volume, its
``HostToContainer`` mount at ``channel_dir``, the ``UVOL_CHANNEL_DIR``
env, the ``volumes.union.ai/channel`` label (so an admission webhook can
select these pods — a CSI driver is not expressible as a selector), and
(unless ``staging_size=None``) the memory-backed passthrough staging
volume. No ``securityContext`` is set — the pod keeps whatever
identity and capabilities it would otherwise run with, because the fd
handoff is what removes the need for privileges, not a capability drop.
Requires the mount-broker DaemonSet + ``CSIDriver`` on the cluster
(unionai/cloud nodeobserver ``uvolMountBroker``).

``cache_size`` attaches a **disk-backed** ``emptyDir`` at ``cache_dir`` and
points the chunk cache at it via ``$UNION_VOLUME_CACHE_DIR``. Without it
the cache falls back to ``$HOME``, which on every managed Kubernetes is the
container's overlayfs — the slowest writable thing on the node, and a place
where the cache has no declared size at all. Note this does **not** take
the cache out of ephemeral-storage accounting: Kubernetes counts
``emptyDir`` usage there too. What it buys is an enforced ``sizeLimit``, a
budget the client is actually told about (see ``$UNION_VOLUME_CACHE_SIZE_MB``
below), and a seam to put the cache on a different device.
An ``emptyDir`` lands on kubelet's root directory, which is
the node's instance-store NVMe wherever the AMI relocates it there (EKS
AL2/AL2023 with ``setup-local-disks raid0``, which is also what puts
``/mnt/k8s-disks/0`` under mount-s3's cache) and the root EBS volume
otherwise. **The plugin cannot tell which**, and neither can a task: verify
per cluster before assuming the fast path, e.g. by comparing
``findmnt -no SOURCE --target`` on the cache dir against the node's disk
layout.

Left at ``None`` for backwards compatibility — turning it on unprompted
would put a cache on a disk the caller never budgeted for.

``shared_node_cache=True`` asks the mount broker for the node-shared chunk
cache -- a second inline volume from the same CSI driver, tagged
``volumes.union.ai/kind=node-cache`` -- and publishes where it lands as
``$UNION_VOLUME_SHARED_NODE_CACHE_DIR``. Every read-only
`Volume.mount` in the pod then uses it automatically
(``shared_node_cache=None``), so pods mounting the same volume family fetch
each chunk from object storage once per *node* rather than once per *pod*.
**No hostPath and no privilege in the pod**: the broker bind-mounts a
per-*namespace* subtree of the node cache into the pod, so pods of other
namespaces on the node never see these chunks, and the DaemonSet -- which
is privileged already -- owns the directory. The dataplane must run the
broker with ``uvolBroker.nodeCacheDir`` set (``uvolMountBroker.nodeCache``
in the chart); a pod that asks on a node without it fails to start with a
clear ``FailedPrecondition`` from the driver rather than mounting anything
privileged. Only read-only mounts share it: a writable mount keeps its
per-pod cache (``shared_node_cache=True`` on a writable mount is an error),
because JuiceFS keeps its writeback staging queue inside the cache
directory and it is per-writer. Pods of one namespace share the directory
world-writable; that is the trust boundary, and it is a namespace, not a
node.

Usage::

    env = flyte.TaskEnvironment(
        name="my-task",
        image=with_high_throughput_volume_deps(flyte.Image.from_debian_base()),
        pod_template=allow_volumes(),
    )


| Parameter | Type | Description |
|-|-|-|
| `pod_template` | `Optional['PodTemplate']` | |
| `channel_dir` | `str` | |
| `driver` | `str` | |
| `primary_container_name` | `str` | |
| `staging_dir` | `str` | |
| `staging_size` | `Optional[str]` | |
| `cache_dir` | `str` | |
| `cache_size` | `Optional[str]` | |
| `shared_node_cache` | `bool` | |
| `shared_node_cache_dir` | `str` | |

#### with_high_throughput_volume_deps()

```python
def with_high_throughput_volume_deps(
    base: Image,
) -> Image
```
Prepare ``base`` for high-throughput (Redis-backed) Volumes.

Returns a new `flyte.Image` that, on top of ``base``:

* installs ``fuse3`` — the ``fusermount3`` userspace helper JuiceFS execs to
  mount the FUSE filesystem. *Every* Volume mount needs this under the
  default unprivileged `flyte.PodTemplate.allow_fuse`; without it the
  mount client exits immediately with ``fuse: fuse is not installed``;
* installs ``redis-server`` / ``redis-tools`` (the in-pod daemon the Redis
  store runs against), and
* sets ``UNION_VOLUME_METADATA_STORE=redis`` so volumes created in this
  image via `Volume.new` / `Volume.empty` *default* to Redis
  without the caller passing ``metadata_store_type=`` each time (still
  overridable per-volume).

With this helper the image is complete: just add
``pod_template=flyte.PodTemplate().allow_fuse()`` to the
`flyte.TaskEnvironment` and Volumes mount and run. For the default
SQLite store you don't need Redis, but you *do* still need ``fuse3`` —
install it with ``image.with_apt_packages("fuse3")`` (see `Volume.mount`).


| Parameter | Type | Description |
|-|-|-|
| `base` | `Image` | |

#### with_local_flyteplugins()

```python
def with_local_flyteplugins(
    base: Image,
    juicefs: Optional[str] = None,
) -> Image
```
Package the **locally checked-out** flyteplugins-union (built to a
wheel) and an optional local ``juicefs`` binary into ``base`` — for
iterating on an *unreleased* plugin build against a real cluster.

The shipped path is `with_high_throughput_volume_deps` plus the
platform wheel's bundled ``juicefs``; reach for this only when the plugin
itself is being developed. Builds the wheel from the installed editable
source into the SDK's local-plugin dist folder, bundles it via
`flyte.Image.with_local_v2_plugins`, and (if ``juicefs`` is given)
drops that binary on ``PATH`` so `_juicefs_binary` resolves it.


| Parameter | Type | Description |
|-|-|-|
| `base` | `Image` | |
| `juicefs` | `Optional[str]` | |

