# Volume benchmark

`volume_benchmark.py` measures the performance characteristics of Flyte
[Volumes](../content/user-guide/task-programming/volumes.md) that the user guide
describes. Numbers depend on your object store, region, and instance type, so run
it in the environment you want to characterize rather than relying on a single
published figure.

## What it measures

| Benchmark | Metric |
|---|---|
| `mount_vs_files` | `mount()` time for a volume already holding N files (metadata-bound) |
| `write_throughput` | Sequential write MB/s to the volume vs. `tmpfs` (`/dev/shm`) vs. local disk — **excluding** commit |
| `commit_cost` | Time to make written data durable via `finalize()` |
| `metadata_throughput` | Small-file create rate and `stat` traversal rate |

The **metadata-bound** benchmarks (`mount_vs_files`, `metadata_throughput`) run
once per metadata **mode** — the default mode and high-throughput mode — so you
can compare them. The **data-path** benchmarks (`write_throughput`,
`commit_cost`) are mode-agnostic and run once. High-throughput mode keeps the
whole namespace resident in memory (RAM scales with file count) for faster
metadata operations, while the default mode keeps it on disk — so it trades
memory (and a slightly slower mount) for metadata speed.

## Run it

```bash
flyte run benchmarks/volume_benchmark.py main
```

Tune the workload:

```bash
flyte run benchmarks/volume_benchmark.py main \
    --file_counts '[100, 1000, 10000, 50000]' \
    --write_mb 1024 --commit_mb 1024 --meta_files 20000 \
    --modes '["default", "high-throughput"]'
```

`main` returns the flat `metric -> value` map and logs a Markdown table you can
paste into the docs.

> The benchmark image installs the dependencies for **both** modes so they can
> be compared in one run; it does not switch the default. A production image
> that wants high-throughput mode everywhere should use
> `with_high_throughput_volume_deps` instead.

## Requirements

- The task environment enables FUSE (`pod_template=flyte.PodTemplate().allow_fuse()`)
  and installs `flyteplugins-union` — both already set up in the script.
- The cluster must run a FUSE device plugin (the Union data plane ships one).
