---
title: RWVolume
version: 0.4.2
variants: +flyte +union
layout: py_api
---

# RWVolume

**Package:** `flyteplugins.union.io`

Mutable working copy — PRD §Core Concepts.

Mounts read-write by default; can opt into a read-only mount via
``mount(read_only=True)`` when the caller wants to use the FUSE
projection without the write path engaged.

The canonical lifecycle is:

1. Obtain via :meth:`Volume.new` (empty) or :meth:`ROVolume.fork`
   (branched from an immutable parent).
2. Mount, write, optionally :meth:`commit` mid-task to capture a
   checkpoint as a sibling :class:`ROVolume`.
3. Return from a task — the type transformer auto-:meth:`finalize`-s
   the still-mounted volume into the run output as an
   :class:`ROVolume`.


## Parameters

```python
class RWVolume(
    kind: typing.Literal['flyte.volume/v1'],
    name: str,
    bucket: str,
    storage: typing.Literal['s3', 'gs', 'wasb'],
    region: typing.Optional[str],
    index: typing.Optional[flyte.io._file.File],
    metadata_store_type: typing.Optional[str],
    used_bytes: typing.Optional[int],
    inode_count: typing.Optional[int],
    index_bytes: typing.Optional[int],
    message: typing.Optional[str],
    produced_by: typing.Optional[flyteplugins.union.io._base_volume.ActionRef],
    parent_produced_by: typing.Optional[flyteplugins.union.io._base_volume.ActionRef],
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `kind` | `typing.Literal['flyte.volume/v1']` | |
| `name` | `str` | |
| `bucket` | `str` | |
| `storage` | `typing.Literal['s3', 'gs', 'wasb']` | |
| `region` | `typing.Optional[str]` | |
| `index` | `typing.Optional[flyte.io._file.File]` | |
| `metadata_store_type` | `typing.Optional[str]` | |
| `used_bytes` | `typing.Optional[int]` | |
| `inode_count` | `typing.Optional[int]` | |
| `index_bytes` | `typing.Optional[int]` | |
| `message` | `typing.Optional[str]` | |
| `produced_by` | `typing.Optional[flyteplugins.union.io._base_volume.ActionRef]` | |
| `parent_produced_by` | `typing.Optional[flyteplugins.union.io._base_volume.ActionRef]` | |

## Methods

| Method | Description |
|-|-|
| [`commit()`](#commit) | Drain writeback, then snapshot the current state as a new immutable. |
| [`empty()`](#empty) | Declare a brand-new volume. |
| [`finalize()`](#finalize) | Drain writeback, unmount, and publish as :class:`ROVolume`. |
| [`fork()`](#fork) | Branch this writable into another volume. |
| [`migrate_metadata_store_type()`](#migrate_metadata_store_type) | Re-host this Volume's metadata on ``new_metadata_store_type``. |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialize private attributes. |
| [`mount()`](#mount) | Format (if fresh) and mount the volume at ``mount_path`` in this. |
| [`new()`](#new) | PRD §Lifecycle: create a fresh empty :class:`RWVolume`. |


### commit()

```python
def commit(
    message: Optional[str],
    mount_path: str,
    meta_dir: str,
) -> ROVolume
```
Drain writeback, then snapshot the current state as a new immutable
:class:`ROVolume` — keeping this handle live and writable.

PRD §Lifecycle: subsequent commits produce a linear history. This is
the trace-style "checkpoint per epoch" pattern (UC2)::

    for epoch in range(10):
        train_one_epoch(...)
        versions.append(await ckpt.commit(message=f"epoch {epoch}"))

Because the writeback queue is drained before the snapshot, the
returned :class:`ROVolume` references durable chunks and is safe to
pass to a downstream task. Callers that want periodic keep-alive
checkpoints simply call this on their own cadence.

For the at-task-return commit (drain writeback, *unmount*, then
publish), see :meth:`finalize` — the type transformer drives that
path automatically when you return an :class:`RWVolume`.


| Parameter | Type | Description |
|-|-|-|
| `message` | `Optional[str]` | |
| `mount_path` | `str` | |
| `meta_dir` | `str` | |

### empty()

```python
def empty(
    name: str,
    bucket: Optional[str],
    storage: Optional[StorageBackend],
    region: Optional[str],
    metadata_store_type: Optional[str],
) -> 'Volume'
```
Declare a brand-new volume. The first ``mount()`` call will
bootstrap the namespace (the underlying client refuses to format
over a non-empty bucket prefix).

If ``bucket`` is omitted, it is derived from the currently active
task context as ``{raw_data_root}/{project}/{domain}/volumes`` —
following Flyte's own layout for offloaded data. Must be called
from inside a task in that case.

``metadata_store_type`` controls the in-pod metadata backend. When
omitted it resolves from ``$UNION_VOLUME_METADATA_STORE`` and
otherwise defaults to ``"sqlite"``.

* ``"sqlite"`` (default) keeps the namespace in a local SQLite file —
  runs in-process with no extra package in the task image, and supports
  :meth:`fork`.
* ``"redis"`` runs an in-process ``redis-server`` and persists the
  namespace as an RDB snapshot — faster than the embedded stores for
  metadata-heavy workloads, but requires ``redis-server`` in the image
  (see :func:`with_high_throughput_volume_deps`, which also sets
  ``$UNION_VOLUME_METADATA_STORE=redis`` so it is the default there).

The choice is baked into the Volume and travels with it through
lineage; subsequent mounts of the same Volume must use the same
store type (use :meth:`migrate_metadata_store_type` to change it).

``storage`` is the JuiceFS object-store backend. When omitted it is
inferred from the bucket URI scheme (``s3://`` → ``s3``, ``gs://`` →
``gs``, ``abfs(s)://`` → ``wasb``), so a GCS/Azure bucket — including
the default one derived from ``raw_data_path`` — gets the right
backend without the caller spelling it out.

``region`` pins the object-store region onto the Volume (S3 only —
it forms the endpoint host). When omitted it's derived from the ambient
``AWS_REGION`` / ``AWS_DEFAULT_REGION`` at mount time; pass it to make
the Volume self-describing so a cross-region remount doesn't depend on
the consumer's env.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `bucket` | `Optional[str]` | |
| `storage` | `Optional[StorageBackend]` | |
| `region` | `Optional[str]` | |
| `metadata_store_type` | `Optional[str]` | |

### finalize()

```python
def finalize(
    message: Optional[str],
    mount_path: str,
    meta_dir: str,
    timeout: float,
) -> ROVolume
```
Drain writeback, unmount, and publish as :class:`ROVolume`.

The terminal commit: tears the mount down (unlike :meth:`commit`,
which keeps it live), returns the strictly-typed :class:`ROVolume`,
and attaches ``message``. The :class:`VolumeTransformer` calls this
at task return when an :class:`RWVolume` is returned mounted —
explicit user calls are rare.


| Parameter | Type | Description |
|-|-|-|
| `message` | `Optional[str]` | |
| `mount_path` | `str` | |
| `meta_dir` | `str` | |
| `timeout` | `float` | |

### fork()

```python
def fork(
    name: str,
    as_: Literal['rw', 'ro'],
    mount_path: str,
    meta_dir: str,
    timeout: float,
) -> Union['RWVolume', ROVolume]
```
Branch this writable into another volume.

* ``as_="rw"`` (default) returns a parallel :class:`RWVolume`
  branch — both writers can proceed independently on disjoint
  chunk-key spaces (PRD §Lifecycle).
* ``as_="ro"`` returns a sibling :class:`ROVolume` snapshot of
  the current state. Distinct from :meth:`commit`: the
  resulting :class:`ROVolume` is a *branch* (sibling in the
  lineage DAG), not part of ``self``'s linear commit chain.

``self`` remains mounted and writable in both cases.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `as_` | `Literal['rw', 'ro']` | |
| `mount_path` | `str` | |
| `meta_dir` | `str` | |
| `timeout` | `float` | |

### migrate_metadata_store_type()

```python
def migrate_metadata_store_type(
    new_metadata_store_type: str,
    meta_dir: str,
    new_meta_dir: Optional[str],
) -> 'Volume'
```
Re-host this Volume's metadata on ``new_metadata_store_type``
without copying data chunks.

``new_metadata_store_type`` must differ from the current store type.
The full namespace is exported and re-imported into a fresh meta
store pointing at the *same* bucket. Chunks are addressed by stable
IDs that are preserved across the migration, so no chunk traffic is
required.

The returned Volume has a fresh ``index`` (snapshot of the loaded
meta store), ``parent_produced_by`` linking to the pre-migration
version, the same ``bucket`` / ``storage`` / ``name``, and the new
``metadata_store_type``.

Intent is *migration*, not fork: the old store is meant to be
retired. As a defense against accidental concurrent use, the loaded
store's chunk-slice / inode / session counters are advanced by a
random offset (same mechanism as :meth:`fork`) so that even if the
old store is still mounted somewhere, its writes can't collide with
the migrated store's writes in shared object-store keys.

Does not require a FUSE mount on either side. Safe to call from any
task pod running the Volume runtime (Redis tooling is only needed if
one of the stores is ``"redis"``).


| Parameter | Type | Description |
|-|-|-|
| `new_metadata_store_type` | `str` | |
| `meta_dir` | `str` | |
| `new_meta_dir` | `Optional[str]` | |

### model_post_init()

```python
def model_post_init(
    context: Any,
)
```
This function is meant to behave like a BaseModel method to initialize private attributes.

It takes context as an argument since that's what pydantic-core passes when calling it.



| Parameter | Type | Description |
|-|-|-|
| `context` | `Any` | The context. |

### mount()

```python
def mount(
    mount_path: str,
    meta_dir: str,
    cache_dir: str,
    timeout: float,
    writeback: bool,
    upload_delay: Optional[str],
    max_uploads: int,
    attr_cache: float,
    entry_cache: float,
    dir_entry_cache: float,
    read_only: bool,
)
```
Format (if fresh) and mount the volume at ``mount_path`` in this
process.

Call once near the top of a task body before reading or writing under
``mount_path``.

When ``writeback=True`` (default), writes land in the local cache
directory first and are uploaded asynchronously in the background.
This decouples write latency from object-store round-trips. The
pending upload queue is drained on ``commit()``; if the pod dies
before commit, in-flight chunks are lost — but that's fine because
the Volume itself is never published in that case.

``upload_delay`` (e.g. ``"1h"``, ``"30m"``, ``"5s"``) defers uploads
by the given duration. Useful for write-scratchy workloads — files
that are written and then overwritten / deleted within the delay
window are never uploaded at all. Default (``None``) is no extra
delay; the background uploader starts as soon as a chunk is written.
Has no effect without ``writeback=True``.

``max_uploads`` caps concurrent S3 PUTs (default 50; underlying
client default is 20). Bumping helps write-burst phases when the
chunks are small enough that 20 streams can't saturate the link.

``attr_cache`` / ``entry_cache`` / ``dir_entry_cache`` are kernel-side
TTLs in seconds for file attributes, name-to-inode lookups, and
directory listings respectively. Defaults are ``60.0`` for all three,
which collapses stat / getattr / lookup storms by an order of
magnitude on directory-heavy workloads (Go toolchain, package
managers, codegen). This is safe because a Volume is single-writer
for the duration of its mount — no external mutator is supported by
this mechanism. Concurrent-writer scenarios will be opt-in via a
separate API when added.

Periodic checkpointing and crash recovery are intentionally *not* part
of this method. Callers that want a keep-alive loop drive it themselves
with :meth:`RWVolume.commit` on whatever cadence they choose, and own
any resume-from-checkpoint policy at the usage layer.


| Parameter | Type | Description |
|-|-|-|
| `mount_path` | `str` | |
| `meta_dir` | `str` | |
| `cache_dir` | `str` | |
| `timeout` | `float` | |
| `writeback` | `bool` | |
| `upload_delay` | `Optional[str]` | |
| `max_uploads` | `int` | |
| `attr_cache` | `float` | |
| `entry_cache` | `float` | |
| `dir_entry_cache` | `float` | |
| `read_only` | `bool` | |

### new()

```python
def new(
    name: Optional[str],
    bucket: Optional[str],
    storage: Optional[StorageBackend],
    region: Optional[str],
    metadata_store_type: Optional[str],
) -> 'RWVolume'
```
PRD §Lifecycle: create a fresh empty :class:`RWVolume`.

Equivalent in mechanics to :meth:`empty`, but:

* ``name`` is optional (auto-generated when omitted, matching the
  PRD's ``flyte.Volume.new(name=None)`` signature).
* Returns the strictly-typed :class:`RWVolume` rather than the
  generic :class:`Volume`, so mypy / pyright can enforce a
  task's RO/RW contract at the signature boundary.

Prefer :meth:`new` in new code; :meth:`empty` is retained for
existing callers that already declare ``-&gt; Volume``.


| Parameter | Type | Description |
|-|-|-|
| `name` | `Optional[str]` | |
| `bucket` | `Optional[str]` | |
| `storage` | `Optional[StorageBackend]` | |
| `region` | `Optional[str]` | |
| `metadata_store_type` | `Optional[str]` | |

