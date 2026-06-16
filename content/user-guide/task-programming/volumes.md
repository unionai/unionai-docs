---
title: Volumes
weight: 2
variants: -flyte +union
description: A durable, versioned file system that tasks mount and read and write like a local directory, with cheap copy-on-write forks.
---

# Volumes

A **Volume** is a durable file system that your task mounts and uses like an
ordinary local directory — backed by object storage, but with real file-system
semantics: open, read, write, list, and seek over many files in place.

Unlike [`flyte.io.File` and `flyte.io.Dir`](./files-and-directories), which pass
a *snapshot* of data as a value between tasks, a Volume is **long-lived and
versioned**. You write to it during one run and commit it as an immutable
version; any later task or run can mount that version and pick up exactly where
you left off. Each commit is a new immutable version, and versions share
unchanged data, so keeping history is cheap.

## Volumes vs. files and directories

`File`/`Dir` and Volumes solve different problems. Use the one that matches how
your data is shaped and used.

| | `flyte.io.File` / `flyte.io.Dir` | Volume |
|---|---|---|
| **What it is** | A single file or folder passed as a value | A whole file system you mount |
| **Access** | Uploaded/downloaded as a unit | Mounted; read and written in place, like a local disk |
| **Lifetime** | Tied to the run that produced it | Long-lived; remount across tasks and runs |
| **Changing it** | Produce a new `File`/`Dir` | Fork, write, and commit a new version (copy-on-write) |
| **Best for** | Handing a finished artifact to the next task | Evolving, file-system-heavy state |

If you just need to hand a finished file or folder from one task to the next,
reach for [`flyte.io.File` or `flyte.io.Dir`](./files-and-directories) — they're
simpler and need no setup. Choose a Volume when you need a *mountable, durable
file system* that evolves over time.

> [!NOTE]
> A Volume is a durable, network-backed file system — not an in-memory cache.
> Use it when you want file-system semantics over durable, shared data
> (mounting, partial and random reads, tools that expect files on disk). It is
> **not** a way to speed up model loading: pulling weights into memory through a
> Volume is slower than streaming them directly from object storage with a
> purpose-built loader.

## When to use a Volume

Volumes fit AI and agentic workloads, where work is long-running, stateful, and
file-heavy:

- **Agent memory and state.** Give an agent a durable workspace it builds up
  across turns, tasks, and sessions — notes, intermediate artifacts, a growing
  working set of files — and resume exactly where it left off, instead of
  starting cold each run.
- **Sandboxes and code execution.** Back a [sandbox](../sandboxing/_index) or
  code-execution environment with a Volume so agent- or model-generated code has
  a real, writable file system to work in. Fork a clean base per session so
  concurrent runs stay isolated from each other.
- **Shared, durable datasets.** Keep a dataset, index, or other large working
  set on a Volume and mount it from many tasks to read — or fork and update — it
  as files, without re-fetching or re-uploading the whole thing each run.
- **Branching experiments.** Fork a base Volume per experiment or per run;
  copy-on-write makes each branch independent and cheap, with version history to
  compare against or roll back to.

More broadly, reach for a Volume whenever you need **long-lived, versioned
state** that carries forward across tasks or runs — anything you'd otherwise
rebuild from scratch every time.

## Read-write and read-only volumes

A Volume is always one of two types, and the type tells you what you can do with
it:

- **`RWVolume`** — a writable handle. `Volume.new()` returns one. Mount it,
  write to it, and `commit()` to record an immutable version. While it is
  mounted it is the **single writer**.
- **`ROVolume`** — an immutable, committed version. Mount it read-only to read
  its contents. To change it, `fork()` it into a new `RWVolume`.

Because the type is part of a task's signature, the read/write contract is
enforced at the task boundary: a task that declares `vol: ROVolume` can read
shared data but cannot mutate it. Returning a writable `RWVolume` from a task
commits it and hands the next task an `ROVolume`.

## Setup

Volumes are mounted inside the task pod, so the task environment must grant the
pod permission to mount a file system and install the `flyteplugins-union`
package. The mount permission comes from a pod template with `allow_fuse()`:

```python
import flyte
from flyteplugins.union.io import Volume, ROVolume

image = (
    flyte.Image.from_debian_base()
    .with_pip_packages("flyteplugins-union")
)

env = flyte.TaskEnvironment(
    name="volumes-demo",
    image=image,
    # grant the pod what it needs to mount a Volume
    pod_template=flyte.PodTemplate().allow_fuse(),
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)
```

> [!NOTE]
> `flyte.PodTemplate.allow_fuse()` is what makes a Volume mountable: it requests
> the FUSE device resource and grants the capability the mount needs, without
> running the container as privileged. Your cluster must run a FUSE device
> plugin for this — the Union data plane ships an opt-in one. (For clusters
> without it, `allow_fuse(privileged=True)` is a fallback that runs the
> container privileged instead.) A task whose environment doesn't apply
> `allow_fuse()` cannot mount a Volume.

## Get started

The lifecycle is: **create → mount → write → return**. Returning a writable
volume from a task commits it into an immutable `ROVolume`; downstream tasks
receive that and mount it read-only.

```python
from pathlib import Path
import flyte
from flyteplugins.union.io import Volume, RWVolume, ROVolume

@env.task
async def create_dataset() -> RWVolume:
    vol = Volume.new(name="my-dataset")   # a fresh writable RWVolume
    await vol.mount()                     # mounts at /workspace by default

    Path("/workspace/greeting.txt").write_text("hello from a volume\n")

    return vol                            # returning it commits the volume

@env.task
async def read_dataset(vol: ROVolume) -> str:
    await vol.mount()                     # ROVolume always mounts read-only
    return Path("/workspace/greeting.txt").read_text()

@env.task
async def main() -> str:
    dataset = await create_dataset()
    return await read_dataset(dataset)
```

`Volume.new()` hands you a writable `RWVolume`. When you return it from a task,
your writes are flushed and the volume is committed into an immutable `ROVolume`
— a durable version safe to pass between tasks. The next task receives that
`ROVolume` and mounts the exact same data.

> [!NOTE]
> Returning a mounted `RWVolume` commits and unmounts it for you. To attach a
> message to that final version, return `finalize()` explicitly:
> `return await vol.finalize(message="initial dataset")`. To record a version
> *partway* through a task without unmounting, use `commit()` — see
> [Checkpoint while you work](#checkpoint-while-you-work).

## Updating a volume by forking

An `ROVolume` is immutable, so you never edit one in place. Instead you **fork**
it — creating an independent, writable `RWVolume` branch — then write and commit
a new version:

```python
@env.task
async def add_file(vol: ROVolume) -> ROVolume:
    rw = await vol.fork(name="my-dataset-v2")  # copy-on-write writable branch
    await rw.mount()

    Path("/workspace/extra.txt").write_text("added in a later run\n")

    return await rw.finalize(message="add extra.txt")
```

Forking is **copy-on-write**: the branch shares all unchanged data with its
parent and only stores what you actually change, so it stays cheap even for very
large Volumes. The parent version is never touched, so you keep a clean lineage
of versions to compare against or roll back to. Forks are also isolated — two
branches (or two parallel runs) can write at the same time without clobbering
each other.

## Going further

### Checkpoint while you work

Use `commit()` to record a version **without unmounting** — useful in
long-running loops where you want a durable point you can resume from if the run
is interrupted:

```python
@env.task
async def train(base: ROVolume) -> ROVolume:
    rw = await base.fork(name="training-run")
    await rw.mount()

    for epoch in range(100):
        train_one_epoch()                       # writes to /workspace
        if epoch % 10 == 0:
            await rw.commit(message=f"epoch {epoch}")   # durable checkpoint

    return await rw.finalize(message="training complete")
```

Each `commit()` records a durable, immutable version you can resume from. Those
versions are **retained**, so commit on a cadence that matches how often you'd
actually want to roll back — checkpoint periodically rather than every step, and
prune versions you no longer need.

### High-throughput mode

The default configuration suits most workloads. For workloads that create or
update **very large numbers of files** — package installs, build trees, code
generation — switch on high-throughput mode by preparing the image with
`flyteplugins.union.io.with_high_throughput_volume_deps`:

```python
from flyteplugins.union.io import with_high_throughput_volume_deps

image = with_high_throughput_volume_deps(
    flyte.Image.from_debian_base().with_pip_packages("flyteplugins-union")
)

env = flyte.TaskEnvironment(
    name="high-throughput-volumes",
    image=image,
    pod_template=flyte.PodTemplate().allow_fuse(),
)
```

Volumes created in this environment automatically use the faster metadata path —
no change to your task code is required.

### Tuning the mount

`mount()` accepts options to match the I/O profile of your workload. The most
useful are the mount location and the metadata cache TTLs:

```python
await vol.mount(
    mount_path="/data",      # where to mount (default: /workspace)
    attr_cache=120.0,        # cache file metadata longer (default 60s)
    entry_cache=120.0,       # cache name lookups longer
    dir_entry_cache=120.0,   # cache directory listings longer
)
```

| Option | Default | Use it to… |
|---|---|---|
| `mount_path` | `/workspace` | Mount somewhere other than the default. |
| `attr_cache` / `entry_cache` / `dir_entry_cache` | `60.0` | Cache file metadata, name lookups, and directory listings longer to collapse repeated `stat`/listing calls. |

> [!NOTE]
> Raising the cache TTLs is safe because a Volume has a single writer while it is
> mounted. It helps most when a tool repeatedly stats or lists the same paths
> (common with package managers and build systems).

## Reference

- API: `Volume`, `RWVolume`, `ROVolume`, and
  `flyteplugins.union.io.with_high_throughput_volume_deps`.
- Related: [Files and directories](./files-and-directories) for passing
  snapshot data between tasks.
