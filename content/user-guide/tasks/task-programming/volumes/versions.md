---
title: Versions, artifacts and lineage
icon: diagram-3
weight: 3
variants: -flyte +union
description: Publish each sealed Volume version to the artifact registry with a stable name and parent edges, and pin a specific version from an unrelated run by locator.
---

# Versions, artifacts and lineage

A volume's version history is durable on its own. This page is about reaching
it from outside: publishing versions to the artifact registry so they have
stable names and visible parent edges, and addressing one exact version from
somewhere that has no task input to receive it.

## Tracking versions as artifacts

Every commit gives you an immutable version, but that history lives
inside the volume. Declaring the volume as an **artifact** also publishes each
sealed version to the artifact registry, where it has a stable name, is
searchable across runs, and carries an explicit parent edge to the version it
came from.

Declare the identity once, when the volume is created:

```python
@env.task
async def build_index() -> RWVolume:
    vol = Volume.new(name="search-index", artifact=True)
    data = await vol.mount()

    build_into(data)

    return vol    # the committed version is published as artifact "search-index"
```

`artifact=True` publishes under the volume's own name. Pass a string to publish
under a different name, or a `flyte.artifacts.Metadata` when you want a
description and your own attributes:

```python
from flyte.artifacts import Metadata

vol = Volume.new(
    name="search-index",
    artifact=Metadata(
        name="product-search-index",
        description="FAISS index over the product catalog",
        attrs={"team": "search"},
    ),
)
```

Artifact identity belongs to the *lineage*, not to any one version, so you set
it when the volume is created or when you
[branch it](#branching-under-a-different-artifact) - never per commit. That is
why `commit()` and `finalize()` take no artifact name: renaming mid-stream would
split one version graph into two.

> [!NOTE]
> `Metadata(version=...)` and `Metadata(card=...)` are rejected on a volume.
> Versions are per-seal, and the card is rendered from each seal.

### Publishing a version

Returning the volume from a task publishes that seal as part of writing the
task's outputs: no extra call in your code, and no registry round trip inside
the task.

To publish a checkpoint partway through a task, ask for it on the commit:

```python
for epoch in range(100):
    train_one_epoch(data)
    if epoch % 10 == 0:
        await rw.commit(message=f"epoch {epoch}", publish_artifact=True)

return await rw.finalize(message="training complete")   # published too, if the volume declares an artifact
```

`publish_artifact=True` works even on a volume that declared no identity; the
artifact name then defaults to the volume's name.

Commits you don't publish are still durable versions - they are simply not in
the registry, much as a local commit is real but has not been pushed. The registry holds
the versions you chose to publish.

### Versions and parents

A published version defaults to the seal's **identity hash**, which covers the
committed index and where its chunks live. Every seal writes a new index, so
every seal is its own version; publishing the *same* seal twice is idempotent
rather than duplicating it. Pass `artifact_version="v3"` to `commit()` or
`finalize()` to choose the version string yourself.

Each version records a parent edge pointing at the previous *published* version
of the same artifact, so the registry mirrors the branching shape of the
volume's own lineage. Alongside any attributes you set, every published version
carries:

| Attribute | What it holds |
|---|---|
| `volume/name` | The volume's name |
| `volume/locator` | The locator for this exact version, for `Volume.from_locator()` |
| `volume/used_bytes` | Bytes used at the seal |
| `volume/inode_count` | Files, directories and symlinks at the seal |
| `volume/metadata_store` | The metadata store backing the volume |

### Branching under a different artifact

`fork()` inherits its parent's artifact identity, so a branch keeps publishing
under the same name and the registry shows it as a continuation.

Give a branch its own artifact when it is genuinely a different thing. The first
version published under the new name still records the old one as its parent, so
the lineage stays connected across the rename:

```python
candidate = await base.fork(
    name="index-candidate",
    artifact="product-search-index-candidate",
)
```

Pass `artifact=None` to detach a branch from the registry entirely: it still
commits durable versions, it just publishes none of them.

> [!NOTE]
> Publishing is best-effort by design. If the registry is unreachable the seal
> still succeeds, your data is still durable and still addressable by locator,
> and a warning records that the registry entry is missing. Local executions
> skip publishing altogether.

## Reference a volume across runs

The usual way to receive a volume is as a typed task input or from
`run.outputs`. When you instead want to pin a **specific version** and reach it
from an unrelated run (a config value, a scheduled job, an external system),
save its **locator**. Every committed version exposes one via the `locator`
property: a stable object-store address you can store anywhere.

```python
@env.task
async def publish() -> str:
    vol = Volume.new(name="my-dataset")
    await vol.mount()
    # ... write data ...
    ro = await vol.finalize(message="v1")
    return ro.locator                       # e.g. persist this string somewhere
```

Later, in a different run, with no shared task input, load it back with
`Volume.from_locator`. It returns a read-only `ROVolume` with everything
recovered (the data index, bucket, store type, stats and lineage), so you can
mount it directly or `fork()` it to branch and write:

```python
@env.task
async def consume(addr: str) -> int:
    ro = await Volume.from_locator(addr)    # -> ROVolume, no task context needed
    data = await ro.mount()                 # read-only
    return len(list(data.glob("**/*")))
```

The locator stays resolvable as long as the producing run's outputs are
retained. `locator` is `None` for a freshly created volume that hasn't been
committed yet: there's no published version to point at.

## Next

- [Performance, caching and tuning](./performance) - commit cost is
  part of the write path; this is where the numbers are.
- [Use a volume in a task](./in-tasks) - where commits come from.
