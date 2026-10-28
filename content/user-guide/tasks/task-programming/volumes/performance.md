---
title: Performance, caching and tuning
icon: speedometer2
weight: 4
variants: -flyte +union
description: The chunk cache, the shared node cache, mount options, measured trade-offs against local disk, and how to tell a slow mount from a wedged one.
---

# Performance, caching and tuning

A Volume is a file system over object storage, so caching and mount options
decide most of what you will feel. Read the first section even if you skip the
rest: the default cache location is the worst one available, and fixing it is a
single argument.

## The chunk cache

Reads go through a local **chunk cache**. Where that cache lives is the single
biggest lever on read performance, and by default it is in the worst place:
unset, it falls back to `$HOME`, which on every managed Kubernetes is the
container's overlayfs - the slowest writable thing on the node, with no size
limit the client knows about.

**Give it a real disk.** `cache_size` attaches a sized `emptyDir` and tells the
client its budget:

```python
pod_template = allow_volumes(cache_size="50Gi")
```

The budget matters as much as the disk. Without it the client keeps its own
100 GiB default, overruns the `emptyDir`'s limit, and kubelet evicts the pod -
a worse failure than a cache that is merely smaller than you hoped. The
published budget is about 90% of the size you give, leaving headroom for the
client's own bookkeeping and the imprecision of its accounting. It is per
mount: split it with `mount(cache_size_mb=...)` when one task mounts several
volumes.

## Shared node cache

With `shared_node_cache=True`, read-only mounts in the pod use a chunk cache
shared by every pod on that node, so a chunk is fetched from object storage
once per *node* rather than once per *pod*:

```python
pod_template = allow_volumes(cache_size="50Gi", shared_node_cache=True)
```

This is worth reaching for when many pods on a node read the same volume - a
fan-out over one dataset, or several tasks sharing a model. It is not a
general speed-up: pods reading unrelated volumes share nothing but the disk.

The task pod gains no privilege from it. The shared directory arrives as an
inline CSI volume from the same mount broker that serves the volume channel,
and the broker bind-mounts a per-namespace subtree of the node's cache - so
other namespaces are not visible, and the pod still has no `hostPath` and no
capabilities. It needs a broker configured with a node cache directory, which
the dataplane chart enables by default (`uvolMountBroker.nodeCache`); a pod
that asks for one where the broker has none fails to start rather than quietly
falling back.

> [!NOTE]
> **Read-only only, and that is a correctness rule rather than a policy.**
> JuiceFS keeps its write-back staging queue *inside* the cache directory, so
> two writers sharing one directory would interleave each other's
> not-yet-uploaded blocks. A writable mount therefore never shares:
> `shared_node_cache=True` on one raises an error, and the per-mount default
> falls back to the pod's own cache.

Per mount, `mount(shared_node_cache=...)` decides:

| Value | Behavior |
|---|---|
| unset (default) | Use the shared cache when the pod exposes one and the mount is read-only; otherwise use the pod's own. |
| `True` | Require it. Errors if the pod exposes none, or if the mount is writable. |
| `False` | Never share; always use the pod's own cache. |

An explicit `mount(cache_dir=...)` wins over all of it.

> [!NOTE]
> Every client sharing the directory runs its own eviction against its own
> budget, so they can evict each other. Expect hit rates to vary with whatever
> else is mounted on the node - it is a shared cache, not a reservation.

## Tuning the mount

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

The volume client runs in the task's pod, so its memory counts toward the
task's `memory` in `flyte.Resources`. Leave room for it. By default, the
client's Go memory is held near 2 GiB. This is a soft limit (`GOMEMLIMIT`),
and the client can go over it. Requires `flyteplugins-union` 0.15.5 or later.
To change the limit, set `UNION_VOLUME_CLIENT_MEMORY_LIMIT` in the task
environment's `env_vars` to a Go size such as `1536MiB`, or to `off` for no
limit. A value that isn't a Go size falls back to `2GiB`, with a warning. A
`GOMEMLIMIT` set on the task does not reach the client.

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

## Debugging a mount

When a volume is slow, or a task looks stuck on file I/O, turn on the **volume
report**. It samples the live mount while the task runs and publishes a `Volume`
tab on the task's [report](../reports): throughput over time, a marker at each
`commit()`, `fork()` and `finalize()`, and a health line.

```python
vol = Volume.new(name="my-dataset")
vol.report = True          # set before mount(); sampling starts at mount
data = await vol.mount()
```

The setting belongs to that handle only. It does not travel with the volume, so
a branch from `fork()`, or a volume a later task receives, needs it set again.
To cover every mount without per-handle code, set the environment variable on
the task environment instead:

```python
env = flyte.TaskEnvironment(
    name="my-env",
    env_vars={"UNION_VOLUME_REPORT": "1"},
)
```

The report is flushed at every seal point, so the charts survive a task that
fails later.

Read the health line first, because it separates the two situations that look
identical from inside the task:

- **healthy** - requests are being served, and the number waiting is shown. Slow
  is then a tuning question: see [Tuning the mount](#tuning-the-mount) and
  [Performance and trade-offs](#performance-and-trade-offs).
- **wedged** - requests have sat unmoved long enough that nothing inside the pod
  will recover them. The line names the channel, how many requests are waiting
  and for how long. Abort the channel or replace the pod; waiting will not help.
- **unknown** - no health answer is available, which is what you see when the
  mount does not go through the node's mount broker.

> [!NOTE]
> The report can never fail a mount. If sampling cannot start or a probe goes
> unanswered, the task runs exactly as it would have without it.

## Next

- [Block volumes](../block-volumes) - if per-file metadata cost is what is
  hurting, this is the bigger lever than any option here.
- [Use a volume in a task](./in-tasks) - where `mount()` is called.
