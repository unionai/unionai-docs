---
title: BlockVolume
description: "A writable Volume whose content is one ext4 filesystem image."
icon: braces
version: 0.15.0
variants: -flyte +union
layout: py_api
---

# BlockVolume

**Package:** `flyteplugins.union.io`

A writable Volume whose content is one ext4 filesystem image.

Use it for single-writer, small-file workloads — build caches (BuildKit),
package caches, virtualenvs, ``node_modules``, source trees. `mount`
attaches the image as a loop device and returns the ext4 mount, so file
metadata is handled in the kernel instead of a FUSE round trip per
operation. Measured on dogfood: BuildKit cold build 67 s vs 125 s on a
plain Volume (59 s on local disk); 5,000 small files 0.44 s vs 6.9 s.

Everything else is a Volume: `commit` snapshots it (after trimming
freed blocks), forks share unchanged blocks, and returning it from a task
finalizes it. Forks of a block volume are block volumes. A commit is
crash-consistent by default -- like snapshotting a live disk; ext4 replays
its journal when a fork mounts it -- and does not stall writers;
``commit(freeze=True)`` takes a clean snapshot at the cost of a brief
write stall.

Trade-offs versus a plain Volume:

* **Trusted workloads only.** Attaching makes the node kernel parse the
  image. Behind the uvol mount broker it is allowed only for pods matching
  the cluster's ``blockAllow`` rules; a privileged pod without the broker
  attaches it itself.
* **One writer, no read-only mounts, not browsable file by file.** Fork it
  to read it elsewhere.
* **A size limit**, set here and grown online with `grow`.
* More object-store traffic on file-heavy work (whole blocks are
  rewritten).

::

    cache = BlockVolume.new(size="64G")
    path = await cache.mount()          # ext4 mount point
    ...
    await cache.grow("128G")             # online
    return cache                         # finalized at task return


## Parameters

```python
class BlockVolume(
    kind: typing.Literal['flyte.volume/v1'] = 'flyte.volume/v1',
    name: str,
    bucket: str,
    storage: typing.Literal['s3', 'gs', 'wasb'] = 's3',
    region: typing.Optional[str] = None,
    endpoint: typing.Optional[str] = None,
    index: typing.Optional[flyte.io._file.File] = None,
    metadata_store_type: typing.Optional[str] = None,
    block_size: typing.Optional[str] = None,
    metadata_prefix: typing.Optional[str] = None,
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
| `block_size` | `typing.Optional[str]` | |
| `metadata_prefix` | `typing.Optional[str]` | |
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
| `is_block` | `bool` | Whether this is a block-mode volume (one ext4 image; see `BlockVolume`). Carried on every version, so a task receiving any Volume can tell: forks of a block volume are block volumes, and they mount read-write only. |
| `locator` | `Optional[str]` | The object-store address of *this* published version, or ``None`` if the volume has never been sealed (a fresh `new` / `empty`).  It's the path of this version's metadata object (``produced_by.locator`` — the JSON value `_publish_metadata` writes), which carries the complete Volume: ``index``, ``bucket``, ``metadata_store_type``, stats, and lineage. Persist it anywhere (a task output, your own store, a config) and recover the exact version later with `from_locator` — that's the across-run handle that doesn't depend on name or live task context.  Available immediately off a `RWVolume.commit` / ``finalize`` / `fork` result, since each stamps ``produced_by`` on the version it publishes. ``None`` before the first seal — there's no version to point at yet.  Durability note: the address lives under the producing action's output path, so it stays resolvable as long as that action's artifacts are retained. |
| `mount_path` | `Optional[Path]` | Where this handle is currently mounted, or ``None`` if not mounted.  Set by `mount` and cleared by the terminal seal (`RWVolume.finalize` / auto-finalize). Use it to locate files without re-deriving the path: ``(vol.mount_path / "data.bin")``. |
| `size` | `str` | The image size this volume was declared or last grown to. |

## Methods

| Method | Description |
|-|-|
| [`commit()`](#commit) | Snapshot the live image as a new immutable version (see `RWVolume.commit`). |
| [`empty()`](#empty) | Declare a brand-new volume. |
| [`finalize()`](#finalize) | Detach, unmount and publish as an `ROBlockVolume` (see `RWVolume.finalize`). |
| [`fork()`](#fork) | Branch this block volume (see `RWVolume.fork`): a `BlockVolume`, or an `ROBlockVolume` snapshot with ``as_="ro"``. |
| [`from_block()`](#from_block) | A new regular volume holding a copy of a block volume's files -- the reverse of `BlockVolume.from_volume`, with the same copy semantics. ext4's ``lost+found`` is not copied. |
| [`from_locator()`](#from_locator) | Load a previously published volume version by its `locator`. |
| [`from_volume()`](#from_volume) | A new block volume holding a copy of a regular volume's files. |
| [`get_artifact_metadata()`](#get_artifact_metadata) | Artifact declaration for the declarative (returned-as-output) publish path — flyte-sdk's output conversion calls this on every top-level task output exposing it and, when it returns metadata, emits a ``ProducedArtifact`` on the Outputs envelope; the backend registers the artifact atomically with the action record (no RPC from the task). |
| [`grow()`](#grow) | Grow the image and its filesystem online, while mounted. |
| [`migrate_metadata_store_type()`](#migrate_metadata_store_type) | Re-host this Volume's metadata on ``new_metadata_store_type`` without copying data chunks. |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialize private attributes. |
| [`mount()`](#mount) | Format (if fresh) and mount the volume at ``mount_path`` in this process, and return the resolved mount point as a `Path` (also available afterwards via the `mount_path` property). |
| [`new()`](#new) | Declare a new, empty block volume of ``size`` (e.g. ``"64G"``, binary units). |
| [`recover_mount()`](#recover_mount) | Remount this volume after its mount daemon died under it. |


### commit()

```python
def commit(
    message: Optional[str] = None,
    mount_path: Optional[str] = None,
    meta_dir: Optional[str] = None,
    publish_artifact: bool = False,
    artifact_version: Optional[str] = None,
    freeze: bool = False,
) -> 'ROBlockVolume'
```
Snapshot the live image as a new immutable version (see `RWVolume.commit`).

``freeze=False`` (default): no writer stall; the snapshot is
crash-consistent, and ext4 replays its journal when a fork mounts it.
``freeze=True``: freeze the filesystem for the snapshot so it is clean
(no replay needed); writers stall until the snapshot is pinned (with a
JuiceFS client that announces the pin; older clients hold the freeze
through the whole checkpoint, drain included), and the commit fails
rather than publish if the freeze had to be released early.


| Parameter | Type | Description |
|-|-|-|
| `message` | `Optional[str]` | |
| `mount_path` | `Optional[str]` | |
| `meta_dir` | `Optional[str]` | |
| `publish_artifact` | `bool` | |
| `artifact_version` | `Optional[str]` | |
| `freeze` | `bool` | |

### empty()

```python
def empty(
    name: str,
    bucket: Optional[str] = None,
    storage: Optional[StorageBackend] = None,
    region: Optional[str] = None,
    endpoint: Optional[str] = None,
    metadata_store_type: Optional[str] = None,
    metadata_prefix: Optional[str] = None,
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

``metadata_prefix`` is where this volume's new versions (their index and
metadata objects) are written. Leave it unset inside a task (the
action's output path is used); outside one -- an app, a sidecar, a
script -- it defaults to ``$UNION_VOLUME_METADATA_PREFIX`` and then to
``<bucket>/versions``, so a Volume works anywhere with no task context.

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
| `metadata_prefix` | `Optional[str]` | |

### finalize()

```python
def finalize(
    message: Optional[str] = None,
    timeout: float = 60.0,
    publish_artifact: bool = False,
    artifact_version: Optional[str] = None,
) -> 'ROBlockVolume'
```
Detach, unmount and publish as an `ROBlockVolume` (see `RWVolume.finalize`).


| Parameter | Type | Description |
|-|-|-|
| `message` | `Optional[str]` | |
| `timeout` | `float` | |
| `publish_artifact` | `bool` | |
| `artifact_version` | `Optional[str]` | |

### fork()

```python
def fork(
    name: str,
    as_: Literal['rw', 'ro'] = 'rw',
    mount_path: Optional[str] = None,
    meta_dir: Optional[str] = None,
    timeout: float = 60.0,
    artifact: object = Ellipsis,
) -> Union['BlockVolume', 'ROBlockVolume']
```
Branch this block volume (see `RWVolume.fork`): a `BlockVolume`,
or an `ROBlockVolume` snapshot with ``as_="ro"``.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `as_` | `Literal['rw', 'ro']` | |
| `mount_path` | `Optional[str]` | |
| `meta_dir` | `Optional[str]` | |
| `timeout` | `float` | |
| `artifact` | `object` | |

### from_block()

```python
def from_block(
    source: Volume,
    name: Optional[str] = None,
    workers: int = 8,
    mount_path: Optional[str] = None,
) -> 'RWVolume'
```
A new regular volume holding a copy of a block volume's files --
the reverse of `BlockVolume.from_volume`, with the same copy
semantics. ext4's ``lost+found`` is not copied.

A block source that is mounted by this task is read from its live ext4
mount (do not write to it meanwhile); otherwise a temporary fork of it
is mounted for the copy and torn down after (a block image mounts
read-write only). Returns the new volume mounted.


| Parameter | Type | Description |
|-|-|-|
| `source` | `Volume` | |
| `name` | `Optional[str]` | |
| `workers` | `int` | |
| `mount_path` | `Optional[str]` | |

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

### from_volume()

```python
def from_volume(
    source: Volume,
    name: Optional[str] = None,
    size: Optional[str] = None,
    workers: int = 8,
    mount_path: Optional[str] = None,
) -> 'BlockVolume'
```
A new block volume holding a copy of a regular volume's files.

There is no in-place conversion: a regular volume stores each file as
its own JuiceFS file and a block volume stores one ext4 image, and
neither layout's data can be reused by the other. This mounts both and
copies the tree (modes, timestamps, symlinks and hard links, as
``cp -a``; see ``workers`` for hard links across top-level entries).

``size`` defaults to the source's recorded usage with headroom -- by
bytes and by file count, since ext4 has one inode per 16 KiB of image
(`block_size_for`).
A source that is mounted by this task is read from its live mount (do
not write to it meanwhile); otherwise it is mounted read-only for the
copy and unmounted after.

Returns the new volume mounted: keep working in it, `commit` it,
or return it from the task (which publishes it).


| Parameter | Type | Description |
|-|-|-|
| `source` | `Volume` | |
| `name` | `Optional[str]` | |
| `size` | `Optional[str]` | |
| `workers` | `int` | |
| `mount_path` | `Optional[str]` | |

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


### grow()

```python
def grow(
    size: str,
)
```
Grow the image and its filesystem online, while mounted. Never shrinks.

The new size is recorded on this handle, so later commits and forks
carry it.


| Parameter | Type | Description |
|-|-|-|
| `size` | `str` | |

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
    passthrough: Optional[bool] = None,
    enable_xattr: bool = False,
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
emptyDir. The default cache anywhere else is on the container's
writable layer, which counts against the pod's ephemeral-storage limit
while the client's free-space guard reads the node's disk; there the
mount leases a budget from the limit `allow_volumes` publishes:
half of the ephemeral share not already leased by other mounts (the
share is half the limit), at least 1 GiB, returned at unmount. So a
30 GiB pod's first mount gets 7.5 GiB and the next 3.75 GiB. An explicit
``cache_dir`` and the node cache are left on the client's own default
and its free-space guard.

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

``passthrough`` selects the FUSE passthrough fast-write path: ``None``
(default) means on for writable mounts unless ``UNION_JUICEFS_PASSTHROUGH=0``
is set; ``True``/``False`` force it. Read-only mounts never use it.
``enable_xattr`` turns on extended attributes for the mount (off by
JuiceFS default). Both matter when the volume is used as an overlayfs
layer (for example as a container snapshotter's root): overlayfs needs
``trusted.overlay.*`` xattrs, and the kernel refuses a passthrough FUSE
superblock as a layer ("maximum fs stacking depth exceeded"), so such
a mount needs ``enable_xattr=True, passthrough=False``.

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
| `passthrough` | `Optional[bool]` | |
| `enable_xattr` | `bool` | |

### new()

```python
def new(
    name: Optional[str] = None,
    bucket: Optional[str] = None,
    size: str,
    storage: Optional[StorageBackend] = None,
    region: Optional[str] = None,
    endpoint: Optional[str] = None,
    metadata_store_type: Optional[str] = None,
    artifact: Union[bool, str, 'ArtifactMetadata', 'VolumeArtifact', None] = None,
    metadata_prefix: Optional[str] = None,
) -> 'BlockVolume'
```
Declare a new, empty block volume of ``size`` (e.g. ``"64G"``, binary units).

The image is created sparse on the first `mount` — only what
ext4 writes is ever stored or uploaded.


| Parameter | Type | Description |
|-|-|-|
| `name` | `Optional[str]` | |
| `bucket` | `Optional[str]` | |
| `size` | `str` | |
| `storage` | `Optional[StorageBackend]` | |
| `region` | `Optional[str]` | |
| `endpoint` | `Optional[str]` | |
| `metadata_store_type` | `Optional[str]` | |
| `artifact` | `Union[bool, str, 'ArtifactMetadata', 'VolumeArtifact', None]` | |
| `metadata_prefix` | `Optional[str]` | |

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

