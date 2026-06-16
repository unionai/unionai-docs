---
title: Volumes
weight: 2
variants: -flyte +union
description: Persistent, mountable filesystems that tasks can read and write like a local directory, with versioning and cheap copy-on-write forks.
---

# Volumes

A **Volume** is a persistent file system that your task mounts and uses like an
ordinary local directory. Unlike [`flyte.io.File` and `flyte.io.Dir`](./files-and-directories),
which pass a *snapshot* of data between tasks, a Volume is **long-lived and
versioned**: you write to it during one run, seal it into an immutable version,
and any later task or run can mount that version again — picking up exactly where
you left off.

Every time you seal a Volume you get a new immutable version, and versions share
unchanged data, so keeping history is cheap. Forking a Volume is a
copy-on-write operation: you get an independent, writable branch without copying
the underlying data.

## When to use a Volume

Volumes are built for AI and agentic workloads, where work is long-running,
stateful, and file-heavy:

- **Agent memory and state.** Give an agent a durable workspace it builds up
  across turns, tasks, and sessions — notes, intermediate artifacts, a growing
  working set of files — and resume exactly where it left off on the next run,
  instead of starting cold each time.
- **Sandboxes and code execution.** Back a [sandbox](../sandboxing/_index) or
  code-execution environment with a Volume so agent- or model-generated code has
  a real, writable file system to read and write many files in. Fork a clean
  base per session so concurrent runs stay isolated from each other.
- **Model and dataset caching.** Pull a model, dataset, or package cache into a
  Volume once and mount it across runs instead of re-downloading gigabytes each
  time. This pays off most with
  [reusable containers](../task-configuration/reusable-containers), where the
  container — and the cache it has already loaded — stays warm across runs.
- **Branching experiments and parallel runs.** Fork a base Volume per
  experiment or per agent run; copy-on-write makes each branch independent and
  cheap, with full version history to compare or roll back.

More broadly, reach for a Volume whenever you need **long-lived, versioned
state** that carries forward across tasks or runs — anything you'd otherwise
rebuild from scratch every time.

If you only need to hand a finished file or folder from one task to the next,
use [`flyte.io.File` or `flyte.io.Dir`](./files-and-directories) instead — they're
simpler and need no setup.

## Setup

Volumes are mounted inside the task pod, so the task environment must grant the
pod permission to mount a filesystem and install the `flyteplugins-union`
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
volume from a task automatically seals it into an immutable `ROVolume`;
downstream tasks receive that and mount it read-only.

```python
from pathlib import Path
import flyte
from flyteplugins.union.io import Volume, RWVolume, ROVolume

@env.task
async def create_dataset() -> RWVolume:
    vol = Volume.new(name="my-dataset")   # a fresh writable RWVolume
    await vol.mount()                     # mounts at /workspace by default

    Path("/workspace/greeting.txt").write_text("hello from a volume\n")

    return vol                            # returning it seals the volume automatically

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
your writes are flushed and the volume is sealed into an immutable `ROVolume` —
a durable version safe to pass between tasks. The next task receives that
`ROVolume` and mounts the exact same data.

> [!NOTE]
> To attach a description to the sealed version, or to seal partway through a
> task instead of at return, call `finalize()` explicitly — for example
> `await vol.finalize(message="initial dataset")`. It returns the immutable
> `ROVolume`.

### Updating an existing Volume

An `ROVolume` is immutable, so to change one you **fork** it into a new writable
branch, edit, and seal again:

```python
@env.task
async def add_file(vol: ROVolume) -> ROVolume:
    rw = await vol.fork(name="my-dataset-v2")  # writable copy-on-write branch
    await rw.mount()

    Path("/workspace/extra.txt").write_text("added in a later run\n")

    return await rw.finalize(message="add extra.txt")
```

The fork shares all unchanged data with its parent, so this is fast and cheap
even for very large Volumes. The original `ROVolume` is untouched, giving you a
clean version history.

## Going further

### Checkpoint while you work

Use `commit()` to snapshot the current state **without unmounting** — ideal for
long-running loops like training, where you want a durable checkpoint every few
steps but intend to keep writing:

```python
@env.task
async def train(base: ROVolume) -> ROVolume:
    rw = await base.fork(name="training-run")
    await rw.mount()

    checkpoints = []
    for epoch in range(100):
        train_one_epoch()                       # writes to /workspace
        if epoch % 10 == 0:
            snap = await rw.commit(message=f"epoch {epoch}")
            checkpoints.append(snap)            # each is an immutable ROVolume

    return await rw.finalize(message="training complete")
```

Each `commit()` returns an immutable `ROVolume` you can keep, branch from, or
hand to another task, while the mount stays live and writable.

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

`mount()` accepts options to match the I/O profile of your workload:

```python
await vol.mount(
    mount_path="/data",      # where to mount (default: /workspace)
    max_uploads=100,         # more concurrent uploads for write-heavy bursts
    upload_delay="30m",      # defer uploads; skip files deleted before then (scratch space)
    attr_cache=120.0,        # cache file metadata longer (default 60s)
    entry_cache=120.0,       # cache name lookups longer
    dir_entry_cache=120.0,   # cache directory listings longer
)
```

| Option | Default | Use it to… |
|---|---|---|
| `mount_path` | `/workspace` | Mount somewhere other than the default. |
| `max_uploads` | `50` | Raise upload concurrency for write-heavy bursts. |
| `upload_delay` | `None` | Defer uploads (e.g. `"1h"`); useful for scratch files that are deleted before the delay elapses, so they're never uploaded. |
| `attr_cache` / `entry_cache` / `dir_entry_cache` | `60.0` | Cache metadata, name lookups, and directory listings longer to collapse repeated `stat`/listing calls. |

> [!NOTE]
> The larger caching values above are safe because a Volume has a single writer
> while it is mounted. Raise them when a tool repeatedly stats or lists the same
> paths (common with package managers and build systems).

## Reference

- API: `Volume`, `RWVolume`, `ROVolume`, and
  `flyteplugins.union.io.with_high_throughput_volume_deps`.
- Related: [Files and directories](./files-and-directories) for passing
  snapshot data between tasks.
