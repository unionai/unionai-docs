---
title: ROVolume
description: "Immutable, versioned volume — PRD §Core Concepts."
icon: braces
version: 0.14.0
variants: -flyte +union
layout: py_api
---

# ROVolume

**Package:** `flyteplugins.union.io`

Immutable, versioned volume — PRD §Core Concepts.

Always mounts read-only. Obtain one by:

* calling `RWVolume.commit` on a writable working copy;
* reading ``run.outputs.<name>`` after a prior task returned an
  `RWVolume` (auto-committed at task return);
* passing an already-resolved Volume value through one of the
  ``Volume.empty`` / ``Volume.new`` flows once it's been committed.

There is no ``commit`` method here — that's intentional. The only
path from RO back to a writable working copy is `fork`.


## Parameters

```python
class ROVolume(
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
| [`fork()`](#fork) | Branch this immutable into a new writable working copy. |
| [`from_locator()`](#from_locator) | Load a previously published volume version by its `locator`. |
| [`get_artifact_metadata()`](#get_artifact_metadata) | Artifact declaration for the declarative (returned-as-output) publish path — flyte-sdk's output conversion calls this on every top-level task output exposing it and, when it returns metadata, emits a ``ProducedArtifact`` on the Outputs envelope; the backend registers the artifact atomically with the action record (no RPC from the task). |
| [`migrate_metadata_store_type()`](#migrate_metadata_store_type) | Re-host this Volume's metadata on ``new_metadata_store_type`` without copying data chunks. |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialize private attributes. |
| [`mount()`](#mount) | Mount this volume read-only at ``mount_path`` and return the path. |
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
    meta_dir: Optional[str] = None,
    timeout: float = 60.0,
    artifact: object = Ellipsis,
) -> 'RWVolume'
```
Branch this immutable into a new writable working copy.

PRD §Lifecycle: ``ROVolume.fork() → RWVolume``. The new
`RWVolume` shares chunk objects with ``self`` (copy-on-
write) but is allocator-disjoint so both can write without
colliding on shared keys.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `meta_dir` | `Optional[str]` | |
| `timeout` | `float` | |
| `artifact` | `object` | |

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
    attr_cache: float = 60.0,
    entry_cache: float = 60.0,
    dir_entry_cache: float = 60.0,
    shared_node_cache: Optional[bool] = None,
    cache_size_mb: Optional[int] = None,
    enable_xattr: bool = False,
) -> Path
```
Mount this volume read-only at ``mount_path`` and return the path.

Unset paths default to this volume's name-keyed locations (see
`Volume.mount`). ``read_only`` is intentionally absent from the
signature — an `ROVolume` is statically un-writable, so the
writeback / upload-delay knobs that only make sense for write-paths are
omitted too.

``shared_node_cache`` matters *more* here than on the base class:
`Volume.mount` only ever shares for read-only mounts, so an
`ROVolume` is what actually uses a node-shared chunk cache --
automatically when the pod exposes one. ``cache_size_mb`` caps this
mount's on-disk cache. ``enable_xattr`` exposes extended attributes
(needed when the mount is an overlayfs lower layer). See
`Volume.mount` for all three. ``passthrough`` is absent: a
read-only mount never uses the passthrough write path.


| Parameter | Type | Description |
|-|-|-|
| `mount_path` | `Optional[str]` | |
| `meta_dir` | `Optional[str]` | |
| `cache_dir` | `Optional[str]` | |
| `timeout` | `float` | |
| `attr_cache` | `float` | |
| `entry_cache` | `float` | |
| `dir_entry_cache` | `float` | |
| `shared_node_cache` | `Optional[bool]` | |
| `cache_size_mb` | `Optional[int]` | |
| `enable_xattr` | `bool` | |

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

