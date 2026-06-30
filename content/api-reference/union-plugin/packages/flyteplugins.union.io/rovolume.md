---
title: ROVolume
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# ROVolume

**Package:** `flyteplugins.union.io`

Immutable, versioned volume — PRD §Core Concepts.

Always mounts read-only. Obtain one by:

* calling :meth:`RWVolume.commit` on a writable working copy;
* reading ``run.outputs.&lt;name&gt;`` after a prior task returned an
  :class:`RWVolume` (auto-committed at task return);
* passing an already-resolved Volume value through one of the
  ``Volume.empty`` / ``Volume.new`` flows once it's been committed.

There is no ``commit`` method here — that's intentional. The only
path from RO back to a writable working copy is :meth:`fork`.


## Parameters

```python
class ROVolume(
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

## Properties

| Property | Type | Description |
|-|-|-|
| `locator` | `Optional[str]` | The object-store address of *this* published version, or ``None`` if the volume has never been sealed (a fresh :meth:`new` / :meth:`empty`).  It's the path of this version's metadata object (``produced_by.locator`` — the JSON value :func:`_publish_metadata` writes), which carries the complete Volume: ``index``, ``bucket``, ``metadata_store_type``, stats, and lineage. Persist it anywhere (a task output, your own store, a config) and recover the exact version later with :meth:`from_locator` — that's the across-run handle that doesn't depend on name or live task context.  Available immediately off a :meth:`RWVolume.commit` / ``finalize`` / :meth:`fork` result, since each stamps ``produced_by`` on the version it publishes. ``None`` before the first seal — there's no version to point at yet.  Durability note: the address lives under the producing action's output path, so it stays resolvable as long as that action's artifacts are retained. |
| `mount_path` | `Optional[Path]` | Where this handle is currently mounted, or ``None`` if not mounted.  Set by :meth:`mount` and cleared by the terminal seal (:meth:`RWVolume.finalize` / auto-finalize). Use it to locate files without re-deriving the path: ``(vol.mount_path / "data.bin")``. |

## Methods

| Method | Description |
|-|-|
| [`commit()`](#commit) | **Deprecated. |
| [`empty()`](#empty) | Declare a brand-new volume. |
| [`fork()`](#fork) | Branch this immutable into a new writable working copy. |
| [`from_locator()`](#from_locator) | Load a previously published volume version by its :attr:`locator`. |
| [`migrate_metadata_store_type()`](#migrate_metadata_store_type) | Re-host this Volume's metadata on ``new_metadata_store_type``. |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialize private attributes. |
| [`mount()`](#mount) | Mount this volume read-only at ``mount_path`` and return the path. |
| [`new()`](#new) | PRD §Lifecycle: create a fresh empty :class:`RWVolume`. |


### commit()

```python
def commit(
    mount_path: Optional[str],
    meta_dir: Optional[str],
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
| `mount_path` | `Optional[str]` | |
| `meta_dir` | `Optional[str]` | |
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

Regardless of store type, *mounting* the returned Volume needs a
FUSE-capable image and pod — the ``fuse3`` apt package and
``flyte.PodTemplate().allow_fuse()`` — see :meth:`mount` for the full
runtime requirements.

``metadata_store_type`` controls the in-pod metadata backend. When
omitted it resolves from ``$UNION_VOLUME_METADATA_STORE`` and
otherwise defaults to ``"sqlite"``.

* ``"sqlite"`` (default) keeps the namespace in a local SQLite file —
  runs in-process and needs no *extra* package beyond ``fuse3``, and
  supports :meth:`fork`.
* ``"redis"`` runs an in-process ``redis-server`` and persists the
  namespace as an RDB snapshot — faster than the embedded stores for
  metadata-heavy workloads, but additionally requires ``redis-server``
  in the image. Use :func:`with_high_throughput_volume_deps`, which
  installs ``fuse3`` + ``redis-server`` and sets
  ``$UNION_VOLUME_METADATA_STORE=redis`` so Redis is the default there.

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
    meta_dir: Optional[str],
    timeout: float,
) -> 'RWVolume'
```
Branch this immutable into a new writable working copy.

PRD §Lifecycle: ``ROVolume.fork() → RWVolume``. The new
:class:`RWVolume` shares chunk objects with ``self`` (copy-on-
write) but is allocator-disjoint so both can write without
colliding on shared keys.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `meta_dir` | `Optional[str]` | |
| `timeout` | `float` | |

### from_locator()

```python
def from_locator(
    locator: str,
) -> 'ROVolume'
```
Load a previously published volume version by its :attr:`locator`.

The inverse of :attr:`locator`: download the metadata object at
``locator`` (the full serialized Volume value) and reconstruct it as an
immutable :class:`ROVolume` — ``index``, ``bucket``,
``metadata_store_type``, stats and lineage all recovered, so the result
is mountable read-only (or :meth:`fork`-able to branch + write) without
any other arguments. This is how you reference a specific volume version
across runs: stash ``vol.locator`` somewhere, then ``Volume.from_locator``
it back later.

Reads only the metadata object; the index and chunks are fetched lazily
by :meth:`mount`. Needs object-store credentials for ``locator`` but no
active task context. Raises :class:`VolumeError` if ``locator`` is empty.


| Parameter | Type | Description |
|-|-|-|
| `locator` | `str` | |

### migrate_metadata_store_type()

```python
def migrate_metadata_store_type(
    new_metadata_store_type: str,
    meta_dir: Optional[str],
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
    mount_path: Optional[str],
    meta_dir: Optional[str],
    cache_dir: Optional[str],
    timeout: float,
    attr_cache: float,
    entry_cache: float,
    dir_entry_cache: float,
) -> Path
```
Mount this volume read-only at ``mount_path`` and return the path.

Unset paths default to this volume's name-keyed locations (see
:meth:`Volume.mount`). ``read_only`` is intentionally absent from the
signature — an :class:`ROVolume` is statically un-writable, so the
writeback / upload-delay knobs that only make sense for write-paths are
omitted too.


| Parameter | Type | Description |
|-|-|-|
| `mount_path` | `Optional[str]` | |
| `meta_dir` | `Optional[str]` | |
| `cache_dir` | `Optional[str]` | |
| `timeout` | `float` | |
| `attr_cache` | `float` | |
| `entry_cache` | `float` | |
| `dir_entry_cache` | `float` | |

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

Creating the handle does no I/O; the first :meth:`mount` formats the
namespace and needs a FUSE-capable image + pod (``fuse3`` and
``allow_fuse()`` — see :meth:`mount`).


| Parameter | Type | Description |
|-|-|-|
| `name` | `Optional[str]` | |
| `bucket` | `Optional[str]` | |
| `storage` | `Optional[StorageBackend]` | |
| `region` | `Optional[str]` | |
| `metadata_store_type` | `Optional[str]` | |

