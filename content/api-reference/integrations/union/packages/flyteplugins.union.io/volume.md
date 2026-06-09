---
title: Volume
version: 0.4.0
variants: +flyte +union
layout: py_api
---

# Volume

**Package:** `flyteplugins.union.io`

A persistent volume identified by its metadata index.

A ``Volume`` is content-addressable lineage on top of an object-store
bucket. The bucket holds the data chunks; the metadata store holds the
entire namespace (a SQLite ``.db`` or a Redis ``dump.rdb``, depending on
``metadata_store_type``). Cloning
the metadata produces an independent fork that initially sees the
same file tree and shares chunk objects but diverges as either side
writes — see :meth:`fork` for the chunk-key disjointness guarantees
that make concurrent writes safe.


## Parameters

```python
class Volume(
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
| [`commit()`](#commit) | **Deprecated. |
| [`empty()`](#empty) | Declare a brand-new volume. |
| [`fork()`](#fork) | Snapshot the current metadata index and return a new ``Volume``. |
| [`migrate_metadata_store_type()`](#migrate_metadata_store_type) | Re-host this Volume's metadata on ``new_metadata_store_type``. |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialize private attributes. |
| [`mount()`](#mount) | Format (if fresh) and mount the volume at ``mount_path`` in this. |
| [`new()`](#new) | PRD §Lifecycle: create a fresh empty :class:`RWVolume`. |


### commit()

```python
def commit(
    mount_path: str,
    meta_dir: str,
    timeout: float,
    message: Optional[str],
) -> 'Volume'
```
**Deprecated.** Drain + unmount + publish, returning a new ``Volume``.

Prefer the typed lifecycle: create an :class:`RWVolume`
(:meth:`Volume.new` / :meth:`ROVolume.fork`), use
:meth:`RWVolume.commit` for a keep-alive snapshot, and let the type
transformer call :meth:`RWVolume.finalize` automatically when you
return an :class:`RWVolume` from a task. This base-class method is
retained as a thin wrapper so existing ``Volume`` callers keep
working; it emits :class:`DeprecationWarning`.


| Parameter | Type | Description |
|-|-|-|
| `mount_path` | `str` | |
| `meta_dir` | `str` | |
| `timeout` | `float` | |
| `message` | `Optional[str]` | |

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

### fork()

```python
def fork(
    name: str,
    mount_path: str,
    meta_dir: str,
    timeout: float,
) -> 'Volume'
```
Snapshot the current metadata index and return a new ``Volume``
that points at the snapshot.

Both the original and the fork reference the same bucket. To keep
their writes from clobbering each other, the fork's chunk / inode /
session allocator counters are advanced by a random 56-bit offset
before publication. Object keys embed those allocator IDs, so the two
diverge into disjoint key spaces; without this, parent and fork would
race to allocate the same IDs and one side's writes would silently
overwrite the other's.

Works whether or not ``self`` is currently mounted:

* **Live** (mounted): flushes in-memory state (``SAVE`` for Redis,
  WAL checkpoint for SQLite) and snapshots the live on-disk index,
  bumps counters on the snapshot, and uploads it.
* **Cold** (not mounted): downloads ``self.index`` to a tempdir,
  bumps counters in place, and uploads. Stats are inherited from
  ``self`` since no writes can have occurred.

Note: cold-fork still avoids copying the data chunks (which dominate
bytes), but it does pull the metadata file through the pod — the
previous ``File.copy_to`` server-side path could not mutate counters
and was unsafe for the chunk-key reasons above.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
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

