---
title: Volume
description: "A persistent volume identified by its metadata index."
icon: braces
version: 0.20.2
variants: -flyte +union
layout: py_api
---

# Volume

**Package:** `flyteplugins.union.io`

A persistent volume identified by its metadata index.

A ``Volume`` is content-addressable lineage on top of an object-store
bucket. The bucket holds the data chunks; the metadata store (an embedded
Badger database) holds the entire namespace. Cloning
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
    chunk_prefix: typing.Optional[str] = None,
    index: typing.Optional[flyte.io._file.File] = None,
    metadata_store_type: typing.Optional[str] = None,
    block_size: typing.Optional[str] = None,
    block_journal_blocks: typing.Optional[typing.List[int]] = None,
    metadata_prefix: typing.Optional[str] = None,
    chunk_branch: typing.Optional[str] = None,
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
| `chunk_prefix` | `typing.Optional[str]` | |
| `index` | `typing.Optional[flyte.io._file.File]` | |
| `metadata_store_type` | `typing.Optional[str]` | |
| `block_size` | `typing.Optional[str]` | |
| `block_journal_blocks` | `typing.Optional[typing.List[int]]` | |
| `metadata_prefix` | `typing.Optional[str]` | |
| `chunk_branch` | `typing.Optional[str]` | |
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
| `family` | `str` | The STORAGE identity: exactly the set of versions whose chunk keys are interchangeable.  This is ``chunk_prefix`` -- JuiceFS's ``Format.Name``, the name the volume was *formatted* under, which is where its chunks live relative to the bucket root. It is inherited by every fork and commit, because a fork copies the metadata index forward and only a fresh volume is formatted. That is what makes a local chunk cache warmed on version N still valid for N+1, and it is why the cache and the local working copy are keyed on this rather than on ``name``, which a fork changes.  Falls back to ``name`` for a volume old enough to have no recorded ``chunk_prefix``. That fallback is not equivalent -- such a volume's forks each get their own family and so cannot share a cache -- but it is the pre-existing behaviour and better than failing to mount.  Not the same as ``artifact``, which is the *catalog* identity: optional, and the only name a human can type. |
| `is_block` | `bool` | Whether this is a block-mode volume (one ext4 image; see `BlockVolume`). Carried on every version, so a task receiving any Volume can tell: forks of a block volume are block volumes, and they mount read-write only. |
| `locator` | `Optional[str]` | The object-store address of *this* published version, or ``None`` if the volume has never been sealed (a fresh `new` / `empty`).  It's the path of this version's metadata object (``produced_by.locator`` — the JSON value `_publish_metadata` writes), which carries the complete Volume: ``index``, ``bucket``, ``metadata_store_type``, stats, and lineage. Persist it anywhere (a task output, your own store, a config) and recover the exact version later with `from_locator` — that's the across-run handle that doesn't depend on name or live task context.  Available immediately off a `RWVolume.commit` / ``finalize`` / `fork` result, since each stamps ``produced_by`` on the version it publishes. ``None`` before the first seal — there's no version to point at yet.  Durability note: the address lives under the producing action's output path, so it stays resolvable as long as that action's artifacts are retained. |
| `mount_path` | `Optional[Path]` | Where this handle is currently mounted, or ``None`` if not mounted.  Set by `mount` and cleared by the terminal seal (`RWVolume.finalize` / auto-finalize). Use it to locate files without re-deriving the path: ``(vol.mount_path / "data.bin")``. |

## Methods

| Method | Description |
|-|-|
| [`abandon()`](#abandon) | Let go of a live mount **without committing**: for a volume whose client died under it, where the sealing teardown would only block. |
| [`clone()`](#clone) | Copy this volume into ``destination`` and return the copy. |
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


### abandon()

```python
def abandon(
    timeout: float = 30.0,
)
```
Let go of a live mount **without committing**: for a volume whose
client died under it, where the sealing teardown would only block.

Best-effort and bounded, every step on its own: detach the block
device, stop the client's process group, retire the broker channel
(aborted, never handed out again: the superblock it served is dead),
stop the metadata store, close the writer's slice domain. Nothing is
uploaded or published; the last commit stands. Without this a caller
that gives up on a dead volume leaked its block attachment and channel
in the node's broker, which refuses new ones past a per-volume cap, so
a pod that kept recovering would eventually be unable to remount.
Idempotent; a no-op when nothing is mounted.


| Parameter | Type | Description |
|-|-|-|
| `timeout` | `float` | |

### clone()

```python
def clone(
    destination: str,
    name: Optional[str] = None,
    region: Optional[str] = None,
    metadata_prefix: Optional[str] = None,
    artifact: Any = Ellipsis,
    concurrency: int = 64,
    since: Optional['Volume'] = None,
    publish_artifact: bool = False,
    artifact_version: Optional[str] = None,
) -> 'Volume'
```
Copy this volume into ``destination`` and return the copy.

``destination`` is a bucket URI (``s3://other-bucket/volumes``) and
becomes the clone's ``bucket``. The published index and the chunk
objects it references -- nothing else -- are copied, and the result is a
volume of the same class that reads and writes only ``destination``: the
source can be deleted, expired or lose access without affecting it.

Built for promotion: iterate on a volume in a dev bucket, clone v10 into
staging, iterate on, clone v15 into the same destination. Clones of one
volume family (the volume, its versions and its forks) into one
destination share a filesystem identity there -- a JuiceFS name and
UUID of their own, recorded under ``<destination>/_uvol/clones/`` -- so
their chunks are shared too, and each clone copies only the chunks the
destination doesn't already hold. Different families, or different
destinations, share nothing.

What the destination holds is judged against a *baseline*: an earlier
clone of the family there, whose index is compared slice by slice with
this one's, so the cost of a clone follows the size of one version's
metadata, not of everything ever cloned into the destination. By
default the baseline is the last clone of the family into
``destination`` (each clone records itself next to the family's
identity); pass ``since=`` -- e.g. the latest staging version found
through an artifact query -- to choose it. Without a usable baseline
the destination's chunks are listed instead. A baseline can only make a
clone copy more than it needs, never less than it must.

A clone can be forked and written in the destination like any volume.
Its slice allocator is moved past the source family's, so what is
written there can never take the key of a chunk a later clone brings
over; and its identity is not the source's, so not even a node-shared
chunk cache mixes the two.

Every chunk is copied server-side (S3 ``CopyObject``, GCS rewrite,
Azure Copy Blob): no data passes through this process. Within one
bucket that works on every backend; between two S3 buckets it needs
``boto3``. Other pairs raise
`VolumeCloneUnsupported`.

As for every volume, the chunks live at the root of the destination
bucket under the volume's JuiceFS name (``<bucket>/<fs-name>/chunks/``);
the object store client ignores the path part of the bucket URI. The
path still scopes what the plugin keeps there itself: the clone
identities, the writer-session ledger and, outside a task, the versions.

* ``name`` -- the clone's name; defaults to ``self.name``.
* ``region`` -- the destination bucket's region (S3); defaults to
  ``self.region``.
* ``metadata_prefix`` -- where the clone's versions are written (see
  `new`); not inherited, so by default they follow the clone's own
  bucket or task rather than the source's.
* ``artifact`` -- the clone's artifact identity, as for `fork`.
* ``concurrency`` -- copy requests in flight.
* ``since`` -- the baseline: an earlier clone of this volume's family
  into ``destination``. A volume that isn't one is refused.
* ``publish_artifact`` / ``artifact_version`` -- register the clone in
  the artifact registry now, under its artifact identity, as
  `RWVolume.commit` does: the promotion flow looks the latest
  version up there for the next clone's ``since=``.

Clones the last *published* version: on a live mount, writes since the
last `commit` are not included. A failed clone leaves only
unreferenced objects behind and can simply be retried; the retry skips
what was already copied.


| Parameter | Type | Description |
|-|-|-|
| `destination` | `str` | |
| `name` | `Optional[str]` | |
| `region` | `Optional[str]` | |
| `metadata_prefix` | `Optional[str]` | |
| `artifact` | `Any` | |
| `concurrency` | `int` | |
| `since` | `Optional['Volume']` | |
| `publish_artifact` | `bool` | |
| `artifact_version` | `Optional[str]` | |

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

The namespace lives in an embedded BadgerDB directory, published as a
store archive. It needs the forked client binary (checkpoint verbs and
``--slice-domain``), which ``flyteplugins-union`` bundles, and a
writable mount needs a claimed writer-session domain (the default
domain-claim path provides one). ``metadata_store_type`` is accepted for
compatibility and must be one of ``METADATA_STORE_TYPES``.

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

* **Live** (mounted): flushes in-memory state and snapshots the live
  on-disk index,
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
    passthrough: Optional[bool] = None,
    enable_xattr: bool = False,
    transport: str = 'auto',
    credentials: str = 'auto',
    log_path: Optional[str] = None,
    on_existing_index: str = 'replace',
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
  ``flyte.Image...with_apt_packages("fuse3")``.
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
| `transport` | `str` | |
| `credentials` | `str` | |
| `log_path` | `Optional[str]` | |
| `on_existing_index` | `str` | |

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
    metadata_prefix: Optional[str] = None,
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

