---
title: Block volumes
icon: hdd
weight: 3
variants: -flyte +union
description: A Volume whose content is one ext4 disk image, for small-file, single-writer workloads like build and package caches that need near-local-disk speed.
---

# Block volumes

A **block volume** is a [Volume](./volumes) whose content is a single ext4
disk image rather than a tree of individual files. When you mount it, the image
is attached as a loop device and mounted as an ordinary ext4 file system, so
the kernel handles every `open`, `stat` and `mkdir` itself instead of making a
network-backed round trip for each one.

Everything else is still a Volume: it lives in object storage, `commit()` records
immutable versions, forks are copy-on-write and share unchanged data, and you
pass it between tasks like any other Volume. What changes is the trade-off:
block volumes are much faster on workloads made of many small files, in return
for a size limit, a single writer, and a cluster-level opt-in.

## When to use a block volume

Reach for a block volume when a **single task writes and reads many small
files**, and the same state should carry over from one run to the next:

- **Build caches.** BuildKit, Go (`GOCACHE`), Bazel, `ccache`, Gradle.
- **Package caches and environments.** pip and uv caches, virtualenvs,
  `node_modules`, Cargo and Maven repositories.
- **Source trees and workspaces.** Checkouts that a build or agent churns through
  file by file.

These workloads are dominated by per-file metadata operations, which is exactly
where a regular Volume pays the most. Measured on the same cluster:

| Workload | Local disk | Regular Volume | Block volume |
|---|---|---|---|
| Write 5,000 small files | n/a | 6.9 s | 0.44 s |
| BuildKit build, cold cache | 59 s | 125 s | 67 s |
| `go build`, cold cache | 304 s | 677 s | 322 s |

Stay with a **regular Volume** when:

- **Many tasks read the same data at once.** A block volume mounts read-write
  only, so every reader works on its own fork. Regular Volumes allow any number
  of concurrent read-only mounts.
- **You want to browse or inspect individual files** from outside a task. The
  files of a block volume exist only inside its image.
- **The data is mostly large files.** Sequential I/O on large files is already
  fast on a regular Volume, and it has no size limit to manage.
- **The code writing to it is untrusted.** See [Setup](#setup).

| | Regular Volume | Block volume |
|---|---|---|
| **Content** | Each file stored separately | One ext4 image |
| **Small-file performance** | Network round trip per operation | Near local disk |
| **Size** | Unlimited | Fixed; grow it with `grow()` |
| **Immutable version type** | `ROVolume` | `ROBlockVolume` (an `ROVolume`) |
| **Read-only mounts** | Yes, any number at once | No: fork, then mount the fork |
| **Browse files without mounting** | Yes (`flyte explore volume`) | No |
| **Cluster setup** | Mount broker | Mount broker **and** an administrator opt-in |

## Setup

A block volume uses the same image and pod template as any Volume. See
[Volumes: Setup](./volumes#setup).

```python
import flyte
from flyteplugins.union.io import BlockVolume, ROBlockVolume, ROVolume, RWVolume, allow_volumes

env = flyte.TaskEnvironment(
    name="builds",
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-union"),
    pod_template=allow_volumes(cache_size="50Gi"),
    resources=flyte.Resources(cpu="4", memory="8Gi"),
)
```

Attaching an image makes the node's kernel parse a file system whose bytes the
task controls. The mount broker therefore allows block volumes only for the
workloads the cluster administrator permits, by namespace, by service account,
or both. By default, a cluster in low-privilege mode allows none and any other
cluster allows every pod. If a task isn't allowed, its
`mount()` fails with the broker's reason. On a self-managed cluster, see
[Enable block volumes](../../../deployment/selfmanaged/configuration/volumes#enable-block-volumes).

> [!NOTE]
> **Privileged pods without the broker**, such as a BuildKit builder, can use
> block volumes too. The client then attaches the image itself with `losetup`
> and `mount`, so the image needs `util-linux` and `e2fsprogs`. The task code is
> the same.

## Create and use a block volume

`BlockVolume.new()` takes a `size`, the most the file system can hold. The image
is **sparse**: only what ext4 actually writes is stored or uploaded, so a
generous size costs nothing up front.

```python
@env.task
async def warm_cache() -> ROBlockVolume:
    cache = BlockVolume.new(name="go-build-cache", size="64G")
    root = await cache.mount()          # an ext4 mount, used like any directory

    run_build(gocache=root / "go")

    return await cache.finalize(message="warm")
```

The first `mount()` creates and formats the image. Sizes use binary units
(`"512M"`, `"64G"`, `"1T"`).

## Use it in a later task: fork, then mount

`finalize()` and `commit()` on a block volume return an `ROBlockVolume`, the
immutable version of a block volume. It is an `ROVolume`, so anything that
accepts an `ROVolume` accepts it.

Because a block image can only be mounted read-write, a downstream task
**forks** it and mounts the fork, even when it only needs to read. The fork is
a `BlockVolume` again, and it shares every unchanged block with its parent, so
forking a large cache is cheap:

```python
@env.task
async def build(cache: ROBlockVolume) -> ROBlockVolume:
    work = await cache.fork(name="go-build-cache")   # a writable BlockVolume
    root = await work.mount()

    run_build(gocache=root / "go")

    return await work.finalize(message="after build")
```

Declaring the input as `ROBlockVolume` makes the requirement part of the task
signature: passing a regular volume fails at the task boundary, not partway
through the task. An input declared `ROVolume` accepts either kind. A block
volume still arrives as an `ROBlockVolume`, and `is_block` tells you which kind
you received:

```python
@env.task
async def inspect(vol: ROVolume) -> int:
    if vol.is_block:                                  # an ROBlockVolume
        vol = await vol.fork(name="inspect-scratch")  # fork to read it
    root = await vol.mount()
    return len(list(root.rglob("*")))
```

Calling `mount()` on an `ROBlockVolume` raises an error that tells you to fork
it.

## Checkpoint while you work

`commit()` records a version without unmounting, as on any Volume. Before each
snapshot the client trims the space ext4 has freed, so deleted files stop
costing storage.

```python
await work.commit(message="after step 1")
```

By default the snapshot is taken **without pausing writers**. It is
*crash-consistent*, like a snapshot of a running disk: when a fork of it is
mounted, ext4 replays its journal and the file system is consistent, but a
write that was in progress when the snapshot was taken may be missing from it.

When you need a clean image instead, for example at a point where you know all
writes are complete, pass `freeze=True`:

```python
await work.commit(message="release", freeze=True)
```

This freezes the file system for the moment it takes to pin the snapshot:
writers wait, then resume before the snapshot is uploaded. If the freeze had to
be released early, the commit fails rather than publish a snapshot it can't
vouch for.

As on every Volume, `commit()`, not `fsync`, is what makes data durable.

## Grow a block volume

A block volume that runs out of space fails writes with `ENOSPC`, the same
as a full disk. Grow it while it is mounted; the image and the file system grow
together, and writers keep running:

```python
await work.grow("128G")
print(work.size)            # "128G"
```

Block volumes never shrink. The new size is recorded on the volume, so its
commits and forks keep it.

> [!NOTE]
> ext4 allocates one inode per 16 KiB of image, so a volume of very many tiny
> files can run out of inodes before it runs out of bytes. Growing the volume
> adds inodes too.

## Convert between regular and block volumes

There is no in-place conversion: the two layouts store data differently and
share nothing. Converting creates a new volume and copies every file into it,
preserving permissions, timestamps, symlinks and hard links. Top-level entries
are copied in parallel (`workers=8` by default), so two hard links under
*different* top-level directories become two files; pass `workers=1` to keep
every link.

```python
@env.task
async def to_block(src: ROVolume) -> ROBlockVolume:
    bv = await BlockVolume.from_volume(src, name="source-tree-blk")
    return await bv.finalize(message="converted from source-tree")

@env.task
async def to_regular(src: ROBlockVolume) -> ROVolume:
    rw = await RWVolume.from_block(src, name="source-tree")
    return await rw.finalize(message="converted from source-tree-blk")
```

`from_volume` sizes the image from the source's recorded usage, counting both
bytes and files, with headroom. Pass `size=` to choose it yourself. Both
methods return the new volume already mounted, so you can keep working in it
before you finalize it. The source isn't modified.

## Trade-offs

- **A size limit.** Choose a generous `size`: an unused size costs nothing. Grow
  the volume when it fills.
- **One writer at a time.** This is true of every mounted Volume, but a block
  volume also has no read-only mounts. Fork it for every additional reader.
- **Only where the cluster allows it.** Attaching an image exposes the node
  kernel to the task's file system bytes, so administrators of shared clusters
  may restrict block volumes to trusted workloads.
- **More upload on heavy churn.** The client stores the image in fixed-size
  pieces, and a small change rewrites a whole piece. Workloads that rewrite
  many files between commits upload more than the same work on a regular
  Volume.

## Reference

- API: `BlockVolume` (`new()`, `commit()`, `grow()`, `from_volume()`),
  `ROBlockVolume` (`fork()`), `RWVolume.from_block()` and `Volume.is_block`.
- The rest of the Volume model (forking, artifacts, locators and the chunk
  cache) works the same way. See [Volumes](./volumes).
- Cluster setup: [Enable block volumes](../../../deployment/selfmanaged/configuration/volumes#enable-block-volumes).
