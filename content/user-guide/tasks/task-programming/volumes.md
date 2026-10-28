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

> [!TIP] Many small files, one writer?
> Build caches, package caches, virtualenvs and source trees spend most of
> their time on per-file metadata. A [block volume](./block-volumes) stores the
> volume as one ext4 image the kernel mounts directly, which brings these
> workloads close to local-disk speed.

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

## Where to go next

The rest of this topic is split by what you are trying to do:

- [**Work with a volume on your machine**](./volumes-local): mount a volume on
  a laptop, a dev box or a CI runner and read and write it like any other
  directory — including offline. The quickest way to get your hands on one.
- [**Use a volume in a task**](./volumes-in-tasks): the create → mount → write →
  return lifecycle, forking to update a version, writing in parallel,
  checkpointing mid-task, and what a custom image needs.
- [**Versions, artifacts and lineage**](./volumes-versions): publish each sealed
  version to the artifact registry, and pin a specific version from an unrelated
  run by locator.
- [**Performance, caching and tuning**](./volumes-performance): the chunk cache
  (the single biggest lever on read performance), the shared node cache, mount
  options, measured trade-offs, and how to debug a slow or wedged mount.
- [**Block volumes**](./block-volumes): a Volume stored as one ext4 image, for
  small-file, single-writer workloads that need near-local-disk speed.

## Reference

- API: `Volume`, `RWVolume`, `ROVolume`, and
  `flyteplugins.union.io.allow_volumes`.
- Artifact publication: `Volume.new(artifact=...)`, `fork(artifact=...)`, and
  `publish_artifact=` / `artifact_version=` on `commit()` and `finalize()` —
  see [Tracking versions as artifacts](./volumes-versions#tracking-versions-as-artifacts).
- Reporting: `vol.report = True` or `$UNION_VOLUME_REPORT` — see
  [Debugging a mount](./volumes-performance#debugging-a-mount).
- Caching: `allow_volumes(cache_size=...)` and
  `mount(cache_dir=..., cache_size_mb=...)` — see
  [The chunk cache](./volumes-performance#the-chunk-cache);
  `allow_volumes(shared_node_cache=True)` and `mount(shared_node_cache=...)` —
  see [Shared node cache](./volumes-performance#shared-node-cache).
- Client memory: `$UNION_VOLUME_CLIENT_MEMORY_LIMIT`. See
  [Tuning the mount](./volumes-performance#tuning-the-mount).
- CLI: `flyte create volume`, `flyte mount volume`, `flyte warmup volume`,
  `flyte status volume`, `flyte unmount volume`, `flyte forget volume` — see
  [Work with a volume on your machine](./volumes-local);
  `flyte explore volume` — see
  [Inspecting a volume](./volumes-local#inspecting-a-volume).
- Related: [Block volumes](./block-volumes) for small-file, single-writer
  workloads; [Files and directories](./files-and-directories) for passing
  snapshot data between tasks.
