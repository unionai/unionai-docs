---
title: Volumes
icon: hdd
weight: 2
variants: -flyte +union
description: A durable, versioned file system that tasks mount and read and write like a local directory, with cheap copy-on-write forks.
---

# Volumes

A **Volume** is a durable file system that your task mounts and uses like an
ordinary local directory, backed by object storage, but with real file-system
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
reach for [`flyte.io.File` or `flyte.io.Dir`](./files-and-directories). They're
simpler and need no setup. Choose a Volume when you need a *mountable, durable
file system* that evolves over time.

> [!NOTE]
> A Volume is a durable, network-backed file system, not an in-memory cache.
> Use it when you want file-system semantics over durable, shared data
> (mounting, partial and random reads, tools that expect files on disk). It is
> **not** a way to speed up model loading: pulling weights into memory through a
> Volume is slower than streaming them directly from object storage with a
> purpose-built loader.

## When to use a Volume

Volumes fit AI and agentic workloads, where work is long-running, stateful, and
file-heavy:

- **Agent memory and state.** Give an agent a durable workspace it builds up
  across turns, tasks, and sessions (notes, intermediate artifacts, a growing
  working set of files) and resume exactly where it left off, instead of
  starting cold each run.
- **Sandboxes and code execution.** Back a [sandbox](../../agents/sandboxing/_index) or
  code-execution environment with a Volume so agent- or model-generated code has
  a real, writable file system to work in. Fork a clean base per session so
  concurrent runs stay isolated from each other.
- **Shared, durable datasets.** Keep a dataset, index, or other large working
  set on a Volume and mount it from many tasks to read (or fork and update) it
  as files, without re-fetching or re-uploading the whole thing each run.
- **Branching experiments.** Fork a base Volume per experiment or per run;
  copy-on-write makes each branch independent and cheap, with version history to
  compare against or roll back to.

More broadly, reach for a Volume whenever you need **long-lived, versioned
state** that carries forward across tasks or runs: anything you'd otherwise
rebuild from scratch every time.

## Read-write and read-only volumes

A Volume is always one of two types, and the type tells you what you can do with
it:

- **`RWVolume`**: a writable handle. `Volume.new()` returns one. Mount it,
  write to it, and `commit()` to record an immutable version. While it is
  mounted it is the **single writer**.
- **`ROVolume`**: an immutable, committed version. Mount it read-only to read
  its contents. To change it, `fork()` it into a new `RWVolume`.

Because the type is part of a task's signature, the read/write contract is
enforced at the task boundary: a task that declares `vol: ROVolume` can read
shared data but cannot mutate it. Returning a writable `RWVolume` from a task
commits it and hands the next task an `ROVolume`.

## Setup

Volumes are mounted inside the task pod, so the task environment needs two
things: an **image** with the volume client (`flyteplugins-union`), and a **pod
template** that lets the pod reach the mount.

```python
import flyte
from flyteplugins.union.io import Volume, ROVolume, allow_volumes

image = (
    flyte.Image.from_debian_base()
    .with_pip_packages("flyteplugins-union")  # volume client (bundles the mount binary)
)

env = flyte.TaskEnvironment(
    name="volumes-demo",
    image=image,
    # let the pod mount Volumes (no privileges required)
    pod_template=allow_volumes(),
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)
```

> [!NOTE]
> **`allow_volumes()`** (from `flyteplugins.union.io`) is the only pod-level
> setup a Volume needs, and the mount runs fully **unprivileged**: no
> `CAP_SYS_ADMIN`, no `/dev/fuse`, no `fuse3` package.
>
> It relies on a mount broker running on the cluster. The Union data plane ships
> one; on a self-managed cluster an administrator
> [enables it](../../../deployment/selfmanaged/configuration/volumes).

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

## Going further

### Checkpoint while you work

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

### Reference a volume across runs

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

### Tuning the mount

`mount()` accepts options to match the I/O profile of your workload: where to
mount, how aggressively to upload, and how long to cache metadata:

```python
data = await vol.mount(
    mount_path="/tmp/data",  # a writable mount point (default: ~/flyte-volume)
    max_uploads=100,         # raise upload concurrency for write-heavy bursts (default 50)
    attr_cache=120.0,        # cache file metadata longer (default 60s)
    entry_cache=120.0,       # cache name lookups longer
    dir_entry_cache=120.0,   # cache directory listings longer
)
```

| Option | Default | Use it to… |
|---|---|---|
| `mount_path` | `~/flyte-volume` | Mount somewhere other than the default. |
| `max_uploads` | `50` | Raise the cap on concurrent uploads. Bump it during write-heavy bursts of many small files, where the default concurrency can't saturate the upload link to object storage. |
| `attr_cache` / `entry_cache` / `dir_entry_cache` | `60.0` | Cache file metadata, name lookups, and directory listings longer to collapse repeated `stat`/listing calls. |

> [!NOTE]
> Raising the cache TTLs is safe because a Volume has a single writer while it is
> mounted. It helps most when a tool repeatedly stats or lists the same paths
> (common with package managers and build systems).

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

## Inspecting a volume

To browse a volume without mounting it, use the CLI. `flyte explore volume`
opens an interactive view of a volume's file tree and its version history,
reading only the small metadata index (no FUSE mount and no file downloads):

```bash
# Explore the volume produced by a run (auto-discovers the volume output)
flyte explore volume <run-name>

# Pin a specific action and the exact output to inspect
flyte explore volume <run-name> <action-name> --op-name my_volume
```

It follows the version lineage, so you can step back through earlier commits and
jump to the action that produced any version. To open an index you already have
on disk, pass `--from-file <path> --store-type sqlite`.

## Performance and trade-offs

A Volume is a durable, object-store-backed file system, so it behaves
differently from a local disk. Know the trade-offs before reaching for one:

- **It is not local memory or disk.** Reads and writes go through a cache over
  object storage. Sequential, file-system-style I/O is fast, but small random
  operations have higher latency than `tmpfs` or a local SSD. For raw throughput
  into memory (streaming model weights, say), a purpose-built loader reading
  directly from object storage will beat mounting a Volume.
- **Writes are decoupled from durability.** With write-back (the default),
  writes land in a local cache and upload in the background; the cost of making
  them durable is paid at `commit()` / `finalize()`, not on each write. Budget
  for commit time separately from your write loop.
- **Per-file work dominates with many small files.** Mounting itself stays fast
  even with tens of thousands of files, but operations that touch every file
  (creating or traversing them) are bounded by per-file metadata cost. The
  [metadata cache TTLs](#tuning-the-mount) exist to absorb this; reach for them
  on file-count-heavy workloads.
- **Versions are retained.** Every commit keeps an immutable version, so commit
  on a deliberate cadence and prune versions you no longer need.

### Benchmark

Numbers from a single run on AWS (S3 storage, `us-east-2` region) on a
4 vCPU / 8 GiB pod, via `benchmarks/volume_benchmark.py`. They depend heavily on
cloud provider, region, file sizes, and instance type, so treat them as ballpark
and re-run the benchmark for your own environment.

Head-to-head against a local disk (the pod's container filesystem):

| Operation | Local disk | Volume |
|---|---|---|
| Sequential write (512 MB) | ~2,200 MB/s | ~930 MB/s |
| Commit 512 MB to durable storage | n/a | ~3.3 s (~160 MB/s) |
| Mount time, 100 → 50,000 files | n/a | ~0.55 s → ~0.63 s |

A Volume trades raw speed for durability and sharing. Sequential writes run
~0.4× local disk: even though uploads are async, each write still passes
through the FUSE layer and the client's chunking/hashing into the cache.
Mounting stays sub-second even at 50k files, and making 512 MB durable adds a
few seconds at `commit()`.

> [!NOTE]
> The per-file metadata figures from this run are not reproduced here: they were
> measured against the metadata store that used to be the default, and the
> current one is substantially faster for creates and stats. Re-run the
> benchmark in your own environment if file-count-heavy throughput is what you
> are sizing for.

## Reference

- API: `Volume`, `RWVolume`, `ROVolume`, and
  `flyteplugins.union.io.allow_volumes`.
- Related: [Files and directories](./files-and-directories) for passing
  snapshot data between tasks.
