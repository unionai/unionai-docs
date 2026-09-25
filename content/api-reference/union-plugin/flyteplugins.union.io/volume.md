---
title: Volume
description: "A persistent volume identified by its metadata index."
icon: braces
version: 0.13.0
variants: -flyte +union
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
writes — see `fork` for the chunk-key disjointness guarantees
that make concurrent writes safe.


## Parameters

```python
class Volume(
    kind: typing.Literal['flyte.volume/v1'] = 'flyte.volume/v1',
    name: str,
    bucket: str,
    storage: typing.Literal['s3', 'gs', 'wasb'] = 's3',
    region: typing.Optional[str] = None,
    endpoint: typing.Optional[str] = None,
    index: typing.Optional[flyte.io._file.File] = None,
    metadata_store_type: typing.Optional[str] = None,
    report: typing.Optional[bool] = None,
    used_bytes: typing.Optional[int] = None,
    inode_count: typing.Optional[int] = None,
    index_bytes: typing.Optional[int] = None,
    message: typing.Optional[str] = None,
    produced_by: typing.Optional[flyteplugins.union.io._base_volume.ActionRef] = None,
    parent_produced_by: typing.Optional[flyteplugins.union.io._base_volume.ActionRef] = None,
    artifact: typing.Optional[flyteplugins.union.io._base_volume.VolumeArtifact] = None,
    published_artifact_version: typing.Optional[str] = None,
    last_published_artifact_name: typing.Optional[str] = None,
    last_published_artifact_version: typing.Optional[str] = None,
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
| `endpoint` | `typing.Optional[str]` | |
| `index` | `typing.Optional[flyte.io._file.File]` | |
| `metadata_store_type` | `typing.Optional[str]` | |
| `report` | `typing.Optional[bool]` | |
| `used_bytes` | `typing.Optional[int]` | |
| `inode_count` | `typing.Optional[int]` | |
| `index_bytes` | `typing.Optional[int]` | |
| `message` | `typing.Optional[str]` | |
| `produced_by` | `typing.Optional[flyteplugins.union.io._base_volume.ActionRef]` | |
| `parent_produced_by` | `typing.Optional[flyteplugins.union.io._base_volume.ActionRef]` | |
| `artifact` | `typing.Optional[flyteplugins.union.io._base_volume.VolumeArtifact]` | |
| `published_artifact_version` | `typing.Optional[str]` | |
| `last_published_artifact_name` | `typing.Optional[str]` | |
| `last_published_artifact_version` | `typing.Optional[str]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `locator` | `Optional[str]` | The object-store address of *this* published version, or ``None`` if the volume has never been sealed (a fresh `new` / `empty`).  It's the path of this version's metadata object (``produced_by.locator`` — the JSON value `_publish_metadata` writes), which carries the complete Volume: ``index``, ``bucket``, ``metadata_store_type``, stats, and lineage. Persist it anywhere (a task output, your own store, a config) and recover the exact version later with `from_locator` — that's the across-run handle that doesn't depend on name or live task context.  Available immediately off a `RWVolume.commit` / ``finalize`` / `fork` result, since each stamps ``produced_by`` on the version it publishes. ``None`` before the first seal — there's no version to point at yet.  Durability note: the address lives under the producing action's output path, so it stays resolvable as long as that action's artifacts are retained. |
| `mount_path` | `Optional[Path]` | Where this handle is currently mounted, or ``None`` if not mounted.  Set by `mount` and cleared by the terminal seal (`RWVolume.finalize` / auto-finalize). Use it to locate files without re-deriving the path: ``(vol.mount_path / "data.bin")``. |

## Methods

| Method | Description |
|-|-|
| [`commit()`](#commit) | **Deprecated.** Drain + unmount + publish, returning a new ``Volume``. |
| [`empty()`](#empty) | Declare a brand-new volume. |
| [`fork()`](#fork) | Snapshot the current metadata index and return a new ``Volume`` that points at the snapshot. |
| [`from_locator()`](#from_locator) | Load a previously published volume version by its `locator`. |
| [`get_artifact_metadata()`](#get_artifact_metadata) | Artifact declaration for the declarative (returned-as-output) publish path — flyte-sdk's output conversion calls this on every top-level task output exposing it and, when it returns metadata, emits a ``ProducedArtifact`` on the Outputs envelope; the backend registers the artifact atomically with the action record (no RPC from the task). |
| [`migrate_metadata_store_type()`](#migrate_metadata_store_type) | Re-host this Volume's metadata on ``new_metadata_store_type`` without copying data chunks. |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialize private attributes. |
| [`mount()`](#mount) | Format (if fresh) and mount the volume at ``mount_path`` in this process, and return the resolved mount point as a `Path` (also available afterwards via the `mount_path` property). |
| [`new()`](#new) | PRD §Lifecycle: create a fresh empty `RWVolume`. |
| [`recover_mount()`](#recover_mount) | Remount this volume after its mount daemon died under it. |


### commit()

```python
def commit(
    mount_path: Optional[str] = None,
    meta_dir: Optional[str] = None,
    timeout: float = 60.0,
    message: Optional[str] = None,
) -> 'Volume'
```
**Deprecated.** Drain + unmount + publish, returning a new ``Volume``.

Prefer the typed lifecycle: create an `RWVolume`
(`Volume.new` / `ROVolume.fork`), use
`RWVolume.commit` for a keep-alive snapshot, and let the type
transformer call `RWVolume.finalize` automatically when you
return an `RWVolume` from a task. This base-class method is
retained as a thin wrapper so existing ``Volume`` callers keep
working; it emits `DeprecationWarning`.


| Parameter | Type | Description |
|-|-|-|
| `mount_path` | `Optional[str]` | |
| `meta_dir` | `Optional[str]` | |
| `timeout` | `float` | |
| `message` | `Optional[str]` | |

### empty()

```python
def empty(
    name: str,
    bucket: Optional[str] = None,
    storage: Optional[StorageBackend] = None,
    region: Optional[str] = None,
    endpoint: Optional[str] = None,
    metadata_store_type: Optional[str] = None,
) -> 'Volume'
```
Declare a brand-new volume. The first ``mount()`` call will
bootstrap the namespace (the underlying client refuses to format
over a non-empty bucket prefix).

If ``bucket`` is omitted, it is derived from the currently active
task context as ``{raw_data_root}/{project}/{domain}/volumes`` —
following Flyte's own layout for offloaded data. Must be called
from inside a task in that case.

Regardless of store type, *mounting* the returned Volume needs a
FUSE-capable image and pod — the ``fuse3`` apt package and
``flyte.PodTemplate().allow_fuse()`` — see `mount` for the full
runtime requirements.

``metadata_store_type`` controls the in-pod metadata backend. When
omitted it resolves from ``$UNION_VOLUME_METADATA_STORE`` and
otherwise defaults to ``"badger"``.

* ``"badger"`` (default) keeps the namespace in an embedded BadgerDB
  directory — daemon-less like SQLite but with the highest metadata
  throughput of the three (~5x SQLite creates, ~27x cold random stats at
  1M files), published as a backup stream. Requires the forked client
  binary (checkpoint verbs and ``--slice-domain``), which
  ``flyteplugins-union`` bundles; a writable mount needs a claimed
  writer-session domain (the default domain-claim path provides one).
* ``"sqlite"`` keeps the namespace in a local SQLite file — runs
  in-process, needs no *extra* package beyond ``fuse3``, works on a
  stock juicefs binary, and supports `fork`.
* ``"redis"`` runs an in-process ``redis-server`` and persists the
  namespace as an RDB snapshot; additionally requires ``redis-server``
  in the image (installed by `with_high_throughput_volume_deps`,
  which also sets ``$UNION_VOLUME_METADATA_STORE=redis``). Now that the
  embedded Badger store is the high-throughput default, Redis is a
  legacy explicit choice.

The choice is baked into the Volume and travels with it through
lineage; subsequent mounts of the same Volume must use the same
store type (use `migrate_metadata_store_type` to change it).

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
| `endpoint` | `Optional[str]` | |
| `metadata_store_type` | `Optional[str]` | |

### fork()

```python
def fork(
    name: str,
    mount_path: Optional[str] = None,
    meta_dir: Optional[str] = None,
    timeout: float = 60.0,
    artifact: Any = Ellipsis,
) -> 'Volume'
```
Snapshot the current metadata index and return a new ``Volume``
that points at the snapshot.

``artifact`` controls the branch's artifact-registry identity. The
default (leave it unset) inherits ``self``'s: two published forks of a
version become sibling branches under the same artifact name. Pass
``artifact=None`` to detach the branch from the registry, or a
name/``Metadata`` (same forms as `new`) to start publishing it
as its own artifact. The last-published lineage pointer is inherited
either way, so a rebranded branch's first published seal still carries
a (cross-name) parent edge back to where it branched from.

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
| `mount_path` | `Optional[str]` | |
| `meta_dir` | `Optional[str]` | |
| `timeout` | `float` | |
| `artifact` | `Any` | |

### from_locator()

```python
def from_locator(
    locator: str,
) -> 'ROVolume'
```
Load a previously published volume version by its `locator`.

The inverse of `locator`: download the metadata object at
``locator`` (the full serialized Volume value) and reconstruct it as an
immutable `ROVolume` — ``index``, ``bucket``,
``metadata_store_type``, stats and lineage all recovered, so the result
is mountable read-only (or `fork`-able to branch + write) without
any other arguments. This is how you reference a specific volume version
across runs: stash ``vol.locator`` somewhere, then ``Volume.from_locator``
it back later.

Reads only the metadata object; the index and chunks are fetched lazily
by `mount`. Needs object-store credentials for ``locator`` but no
active task context. Raises `VolumeError` if ``locator`` is empty.


| Parameter | Type | Description |
|-|-|-|
| `locator` | `str` | |

### get_artifact_metadata()

```python
def get_artifact_metadata()
```
Artifact declaration for the declarative (returned-as-output)
publish path — flyte-sdk's output conversion calls this on every
top-level task output exposing it and, when it returns metadata, emits
a ``ProducedArtifact`` on the Outputs envelope; the backend registers
the artifact atomically with the action record (no RPC from the task).

Returns ``None`` — no declaration — when this volume carries no
artifact intent, or when this exact seal is already in the registry
(it was published imperatively via ``publish_artifact=True``;
re-declaring it would duplicate the version and emit a self-parent).

The version is left to the literal's content hash
(``version_from_content`` — the same identity hash an imperative
publish defaults to), because for a still-mounted ``RWVolume`` the
final seal doesn't exist until the transformer auto-finalizes during
conversion. For that same reason stats attrs reflect this handle's
last seal (or are absent on a fresh handle) rather than the final one;
the registered value itself always carries the authoritative numbers.


### migrate_metadata_store_type()

```python
def migrate_metadata_store_type(
    new_metadata_store_type: str,
    meta_dir: Optional[str] = None,
    new_meta_dir: Optional[str] = None,
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
random offset (same mechanism as `fork`) so that even if the
old store is still mounted somewhere, its writes can't collide with
the migrated store's writes in shared object-store keys.

Does not require a FUSE mount on either side. Safe to call from any
task pod running the Volume runtime (Redis tooling is only needed if
one of the stores is ``"redis"``).


| Parameter | Type | Description |
|-|-|-|
| `new_metadata_store_type` | `str` | |
| `meta_dir` | `Optional[str]` | |
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
    mount_path: Optional[str] = None,
    meta_dir: Optional[str] = None,
    cache_dir: Optional[str] = None,
    timeout: float = 120.0,
    writeback: bool = True,
    upload_delay: Optional[str] = None,
    max_uploads: int = 50,
    attr_cache: float = 60.0,
    entry_cache: float = 60.0,
    dir_entry_cache: float = 60.0,
    read_only: bool = False,
    shared_node_cache: Optional[bool] = None,
    cache_size_mb: Optional[int] = None,
) -> Path
```
Format (if fresh) and mount the volume at ``mount_path`` in this
process, and return the resolved mount point as a `Path`
(also available afterwards via the `mount_path` property).

Call once near the top of a task body before reading or writing under
``mount_path``.

``shared_node_cache`` selects the chunk cache shared by every pod on the
node, which the pod template exposes as ``$UNION_VOLUME_SHARED_NODE_CACHE_DIR``
(see `allow_volumes`). Every pod on the node mounting this volume
family then fetches each chunk from object storage once per *node*
rather than once per pod. The default ``None`` uses it **automatically
whenever it is present and the mount is read-only** -- a pod that never
heard of the flag still benefits, and still contributes chunks. ``True``
requires it (an error if the pod has none, or if the mount is writable);
``False`` never uses it. Writable mounts always get a per-pod cache: the
writeback staging queue lives inside the cache directory and is
per-writer. Clients sharing a directory each run their own eviction
against their own budget, so they can evict one another; the hit rate
depends on what else is mounted on that node.

``cache_size_mb`` caps the on-disk chunk cache for *this* mount. When
omitted, a mount whose cache lives on the volume that
``allow_volumes(cache_size=...)`` attached takes 90% of that volume's
size -- **per mount**: two volumes mounted in one task each get the full
budget, so a task that mounts several must split it here, or size the
volume for the sum, or kubelet evicts the pod for exceeding the
emptyDir. A cache anywhere else (an explicit ``cache_dir``, the node
cache) is left on the client's own default and its free-space guard.

**Runtime requirements** (both needed, or the mount fails):

* **Image** — the ``fuse3`` apt package. JuiceFS execs the
  ``fusermount3`` userspace helper to mount; the default minimal images
  don't ship it, so the mount client exits immediately with
  ``fuse: fuse is not installed``. Add it with
  ``flyte.Image...with_apt_packages("fuse3")`` (or use
  `with_high_throughput_volume_deps`, which includes it). A
  Redis-backed Volume additionally needs ``redis-server`` in the image —
  that helper installs it too.
* **Pod** — ``pod_template=flyte.PodTemplate().allow_fuse()`` on the
  `flyte.TaskEnvironment`, which grants the ``/dev/fuse`` device
  and the capability an unprivileged mount needs (the cluster must run a
  FUSE device plugin; the Union data plane ships one).

The mount point, ``meta_dir`` and ``cache_dir`` must also be writable by
the task user; the name-keyed defaults live under ``$HOME``, which the
default image owns.

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
with `RWVolume.commit` on whatever cadence they choose, and own
any resume-from-checkpoint policy at the usage layer.


| Parameter | Type | Description |
|-|-|-|
| `mount_path` | `Optional[str]` | |
| `meta_dir` | `Optional[str]` | |
| `cache_dir` | `Optional[str]` | |
| `timeout` | `float` | |
| `writeback` | `bool` | |
| `upload_delay` | `Optional[str]` | |
| `max_uploads` | `int` | |
| `attr_cache` | `float` | |
| `entry_cache` | `float` | |
| `dir_entry_cache` | `float` | |
| `read_only` | `bool` | |
| `shared_node_cache` | `Optional[bool]` | |
| `cache_size_mb` | `Optional[int]` | |

### new()

```python
def new(
    name: Optional[str] = None,
    bucket: Optional[str] = None,
    storage: Optional[StorageBackend] = None,
    region: Optional[str] = None,
    endpoint: Optional[str] = None,
    metadata_store_type: Optional[str] = None,
    artifact: Union[bool, str, 'ArtifactMetadata', 'VolumeArtifact', None] = None,
) -> 'RWVolume'
```
PRD §Lifecycle: create a fresh empty `RWVolume`.

Equivalent in mechanics to `empty`, but:

* ``name`` is optional (auto-generated when omitted, matching the
  PRD's ``flyte.Volume.new(name=None)`` signature).
* Returns the strictly-typed `RWVolume` rather than the
  generic `Volume`, so mypy / pyright can enforce a
  task's RO/RW contract at the signature boundary.

Prefer `new` in new code; `empty` is retained for
existing callers that already declare ``-> Volume``.

Creating the handle does no I/O; the first `mount` formats the
namespace and needs a FUSE-capable image + pod (``fuse3`` and
``allow_fuse()`` — see `mount`).

``artifact`` declares the volume's artifact-registry identity (see
`VolumeArtifact` for what identity does and doesn't control):

* ``True`` — publish under the volume's own ``name``;
* a string — publish under that artifact name;
* a ``flyte.artifacts.Metadata`` (or `VolumeArtifact`) — full
  identity: name, description, attrs;
* ``None`` (default) — no standing identity.


| Parameter | Type | Description |
|-|-|-|
| `name` | `Optional[str]` | |
| `bucket` | `Optional[str]` | |
| `storage` | `Optional[StorageBackend]` | |
| `region` | `Optional[str]` | |
| `endpoint` | `Optional[str]` | |
| `metadata_store_type` | `Optional[str]` | |
| `artifact` | `Union[bool, str, 'ArtifactMetadata', 'VolumeArtifact', None]` | |

### recover_mount()

```python
def recover_mount(
    timeout: float = 120.0,
) -> Path
```
Remount this volume after its mount daemon died under it.

The case: the client process is gone (crashed, or torn down without a
successor) and its FUSE connection was aborted — by the broker's
auto-abort or by `_broker.retire_channel` — so every access to
the old mount fails with ``ENOTCONN``. The metadata store and cache
directories are local to this pod and intact, so the same volume can
be served again from a fresh channel with nothing lost that had
reached them: writeback resumes uploading what it had staged.

Steps: stop whatever is left of the old adopter and drop its
bookkeeping; retire its channel lease (the main premount stays dead
for the pod's lifetime, so a later mount leases a runtime channel);
lease a fresh channel; start the client against the SAME meta and
cache dirs; repoint the requested-path symlink; restart the report.
Returns the new mount path. Only the broker path is supported — a
privileged in-pod mount would need fusermount on a dead superblock.

Raises `VolumeMountError` if this instance has no live mount
to recover, or the metadata dir is gone.


| Parameter | Type | Description |
|-|-|-|
| `timeout` | `float` | |

