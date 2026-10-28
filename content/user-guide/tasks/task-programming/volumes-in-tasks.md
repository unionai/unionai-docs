---
title: Use a volume in a task
icon: code
weight: 4
variants: -flyte +union
description: The create, mount, write and return lifecycle of a Volume inside a task - forking to update a version, writing in parallel, and checkpointing mid-task.
---

# Use a volume in a task

A task mounts a Volume and uses it like a local directory. Most of this page
follows from one property: a Volume has exactly **one writer** while it is
mounted. That is why you change a version by forking it, why parallel writers
each get their own fork, and why a long task checkpoints rather than sharing.

It assumes the image and pod template from [Setup](./volumes#setup).

## Get started

The lifecycle is: **create → mount → write → return**. Returning a writable
volume from a task commits it into an immutable `ROVolume`; downstream tasks
receive that and mount it read-only.

```python
import flyte
from flyteplugins.union.io import Volume, RWVolume, ROVolume

@env.task
async def create_dataset() -> RWVolume:
    vol = Volume.new(name="my-dataset")   # a fresh writable RWVolume
    data = await vol.mount()              # mount (default: ~/flyte-volume); returns the path

    (data / "greeting.txt").write_text("hello from a volume\n")

    return vol                            # auto-committed; the next task receives an ROVolume

@env.task
async def read_dataset(vol: ROVolume) -> str:
    data = await vol.mount()              # ROVolume always mounts read-only
    return (data / "greeting.txt").read_text()

@env.task
async def main() -> str:
    dataset = await create_dataset()
    return await read_dataset(dataset)
```

`Volume.new()` hands you a writable `RWVolume`. When you return it from a task,
your writes are flushed and the volume is committed into an immutable `ROVolume`:
a durable version safe to pass between tasks. The next task receives that
`ROVolume` and mounts the exact same data.

> [!NOTE]
> Returning a mounted `RWVolume` commits and unmounts it for you. To attach a
> message to that final version, return `finalize()` explicitly:
> `return await vol.finalize(message="initial dataset")`. To record a version
> *partway* through a task without unmounting, use `commit()`. See
> [Checkpoint while you work](#checkpoint-while-you-work).

## Updating a volume by forking

An `ROVolume` is immutable, so you never edit one in place. Instead you **fork**
it (creating an independent, writable `RWVolume` branch), then write and commit
a new version:

```python
@env.task
async def add_file(vol: ROVolume) -> ROVolume:
    rw = await vol.fork(name="my-dataset-v2")  # copy-on-write writable branch
    data = await rw.mount()

    (data / "extra.txt").write_text("added in a later run\n")

    return await rw.finalize(message="add extra.txt")
```

Forking is **copy-on-write**: the branch shares all unchanged data with its
parent and only stores what you actually change, so it stays cheap even for very
large Volumes. The parent version is never touched, so you keep a clean lineage
of versions to compare against or roll back to. Forks are also isolated: two
branches (or two parallel runs) can write at the same time without clobbering
each other.

## Writing in parallel

A Volume has a **single writer** while it is mounted. One task mounts an
`RWVolume`, writes, and commits; mounting the *same* volume read-write from two
tasks at once is not supported, and there is no distributed file locking.

To write in parallel, don't share one mount: **fork**. Each fork is an
independent `RWVolume` on a disjoint key space, so branches never collide, even
when they run at the same time:

```python
import asyncio

@env.task
async def process_shard(base: ROVolume, i: int) -> ROVolume:
    branch = await base.fork(name=f"shard-{i}")   # isolated writable branch
    data = await branch.mount()
    (data / f"shard-{i}.bin").write_bytes(compute_shard(i))
    return await branch.finalize(message=f"shard {i}")

@env.task
async def fan_out(base: ROVolume) -> list[ROVolume]:
    # each shard runs as its own action, writing its own fork concurrently
    return await asyncio.gather(*(process_shard(base, i) for i in range(8)))
```

Each branch commits its own immutable version; downstream you can read them
independently or fork a new branch from any of them. Reading is never
restricted: any number of tasks can mount the same `ROVolume` read-only at once.

## Checkpoint while you work

Use `commit()` to record a version **without unmounting**: useful in
long-running loops where you want a durable point you can resume from if the run
is interrupted:

```python
@env.task
async def train(base: ROVolume) -> ROVolume:
    rw = await base.fork(name="training-run")
    data = await rw.mount()

    for epoch in range(100):
        train_one_epoch(data)                   # writes under the mounted volume
        if epoch % 10 == 0:
            await rw.commit(message=f"epoch {epoch}")   # durable checkpoint

    return await rw.finalize(message="training complete")
```

Each `commit()` records a durable, immutable version you can resume from. Those
versions are **retained**, so commit on a cadence that matches how often you'd
actually want to roll back: checkpoint periodically rather than every step, and
prune versions you no longer need.

## Custom images

The setup above works on top of any image built from
`flyte.Image.from_debian_base()`. If you bring a **fully custom image** (your own
Dockerfile / base), it needs one thing: **the volume client**,
`pip install flyteplugins-union`. The wheel bundles the mount binary, so
there's nothing else to fetch.

In a Dockerfile that's:

```dockerfile
RUN pip install flyteplugins-union
```

That is the whole image contract: no FUSE userspace tools are needed.

> [!NOTE]
> The container also needs to run as a user that can write the volume's
> `mount_path`, `meta_dir`, and `cache_dir`. The defaults live under the task
> user's `$HOME`, which the default image owns; if your image runs as a
> different user or root, either keep those dirs writable or pass explicit
> writable paths to `mount()`.

## Next

- [Versions, artifacts and lineage](./volumes-versions) - publish each sealed
  version, and reach a specific version from an unrelated run.
- [Performance, caching and tuning](./volumes-performance) - the chunk cache,
  mount options, and the measured trade-offs.
- [Work with a volume on your machine](./volumes-local) - the same volume from
  a laptop.
