"""Benchmark job for Flyte Volumes.

Measures the metrics surfaced in the Volumes user guide so they can be
reproduced (and re-measured) per environment — object store, region, and
instance type all affect the results, so there is no single "right" number.

What it measures
----------------
1. **Mount time vs. number of files** — how long ``mount()`` takes for a volume
   that already contains N files (metadata-bound; grows with file count).
2. **Write throughput (excluding commit)** — sequential write MB/s to the
   volume mount compared against an in-memory path (``/dev/shm``, tmpfs) and a
   local-disk path (the pod's container filesystem). Commit/upload is *not*
   counted here — this is the write path into the local cache.
3. **Commit cost** — time to make a given amount of written data durable via
   ``finalize()`` (the cost that write-throughput intentionally excludes).
4. **Metadata throughput** — small-file create rate (files/s) and a full
   ``stat`` traversal rate over the resulting tree.

Run it
------
    flyte run benchmarks/volume_benchmark.py main

Tune the workload with inputs, e.g.:

    flyte run benchmarks/volume_benchmark.py main \
        --file_counts '[100, 1000, 10000, 50000]' \
        --write_mb 1024 --commit_mb 1024 --meta_files 20000

The ``main`` workflow returns a dict of results and logs a Markdown table you
can paste straight into the docs.
"""

from __future__ import annotations

import logging
import os
import shutil
import tempfile
import time
from pathlib import Path

import flyte
from flyteplugins.union.io import ROVolume, Volume

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
logger = logging.getLogger("volume-bench")

image = (
    flyte.Image.from_debian_base()
    .with_apt_packages("fuse")  # JuiceFS execs /bin/fusermount to mount the volume
    # fusermount reads /etc/mtab on unmount; minimal images lack it. Point it at
    # the kernel mount table so unmount/finalize succeeds.
    .with_commands(["ln -sf /proc/mounts /etc/mtab"])
    .with_pip_packages("flyteplugins-union")
)

env = flyte.TaskEnvironment(
    name="volume-benchmark",
    image=image,
    pod_template=flyte.PodTemplate().allow_fuse(),
    # Give the cache room and enough CPU/mem that I/O, not the instance, is the
    # bottleneck. Adjust to match the environment you want to characterize.
    resources=flyte.Resources(cpu="4", memory="8Gi"),
)

_CHUNK = 8 * 1024 * 1024  # 8 MiB write buffer


def _paths(name: str) -> tuple[str, str, str]:
    """Per-volume mount point, metadata dir, and cache dir — all writable.

    Two reasons everything is keyed by the (unique) volume name:
    * The defaults (``/workspace``, ``/var/lib``, ``/var/cache``) aren't
      writable from an unprivileged FUSE container, so we put them under
      ``/tmp``.
    * A unique path per volume avoids mounting two volumes onto the same point.
    """
    base = os.path.join(tempfile.gettempdir(), "fv", name)
    mnt = os.path.join(base, "mnt")
    meta = os.path.join(base, "meta")
    cache = os.path.join(base, "cache")
    for p in (mnt, meta, cache):
        os.makedirs(p, exist_ok=True)
    return mnt, meta, cache


def _write_bytes(path: str, total_bytes: int, chunk: int = _CHUNK) -> float:
    """Write ``total_bytes`` sequentially to ``path``; return throughput in MB/s.

    Uses unbuffered I/O so we measure the filesystem under test, not Python's
    buffer. Does NOT fsync or commit — this is the write-path cost only.
    """
    buf = b"\0" * chunk
    written = 0
    t0 = time.perf_counter()
    with open(path, "wb", buffering=0) as f:
        while written < total_bytes:
            n = min(chunk, total_bytes - written)
            f.write(buf if n == chunk else buf[:n])
            written += n
    dt = time.perf_counter() - t0
    return (total_bytes / 1e6) / dt if dt > 0 else float("nan")


def _fits(path_dir: str, want_bytes: int) -> int:
    """Return a write size that fits in ``path_dir`` (cap at its free space)."""
    try:
        free = shutil.disk_usage(path_dir).free
    except OSError:
        return want_bytes
    return min(want_bytes, int(free * 0.8))


@env.task
async def mount_vs_files(file_counts: list[int]) -> dict[str, float]:
    """Mount time (seconds) for a volume already containing N small files."""
    results: dict[str, float] = {}
    for n in file_counts:
        vol = Volume.new()  # auto-unique name; avoids "storage not empty" collisions
        mnt, meta, cache = _paths(vol.name)
        await vol.mount(mount_path=mnt, meta_dir=meta, cache_dir=cache)
        d = Path(mnt) / "files"
        d.mkdir(parents=True, exist_ok=True)
        for i in range(n):
            (d / f"f{i:07d}.bin").write_bytes(b"x")
        ro = await vol.finalize(message=f"{n} files", mount_path=mnt, meta_dir=meta)  # unmounts

        t0 = time.perf_counter()
        await ro.mount(mount_path=mnt, meta_dir=meta, cache_dir=cache)
        results[str(n)] = round(time.perf_counter() - t0, 4)
        logger.info("mount with %d files: %.4fs", n, results[str(n)])
    return results


@env.task
async def write_throughput(write_mb: int = 1024) -> dict[str, float]:
    """Sequential write MB/s to the volume vs. tmpfs vs. local disk (no commit).

    Each target is best-effort: a path that can't hold the payload (e.g. a small
    /dev/shm) is capped to its free space, and any failure is recorded as -1 so
    one bad path doesn't sink the whole run.
    """
    total = write_mb * 1024 * 1024
    vol = Volume.new()
    mnt, meta, cache = _paths(vol.name)
    await vol.mount(mount_path=mnt, meta_dir=meta, cache_dir=cache)

    tmp = tempfile.gettempdir()  # local container filesystem
    targets = {
        "volume": (os.path.join(mnt, "bench.bin"), total),
        "tmpfs": ("/dev/shm/bench.bin", _fits("/dev/shm", total)),   # in-memory
        "local_disk": (os.path.join(tmp, "bench.bin"), _fits(tmp, total)),
    }
    results: dict[str, float] = {}
    for kind, (path, n) in targets.items():
        try:
            results[kind] = round(_write_bytes(path, n), 1)
            logger.info("write %s: %.1f MB/s (%d MiB)", kind, results[kind], n // (1024 * 1024))
        except OSError as e:
            logger.warning("write %s failed: %s", kind, e)
            results[kind] = -1.0
        finally:
            try:
                os.remove(path)
            except FileNotFoundError:
                pass
    return results


@env.task
async def commit_cost(commit_mb: int = 1024) -> dict[str, float]:
    """Time to make ``commit_mb`` of written data durable via finalize()."""
    total = commit_mb * 1024 * 1024
    vol = Volume.new()
    mnt, meta, cache = _paths(vol.name)
    await vol.mount(mount_path=mnt, meta_dir=meta, cache_dir=cache)
    _write_bytes(os.path.join(mnt, "payload.bin"), total)  # not timed

    t0 = time.perf_counter()
    await vol.finalize(message=f"commit {commit_mb} MiB", mount_path=mnt, meta_dir=meta)
    secs = time.perf_counter() - t0
    return {
        "commit_seconds": round(secs, 3),
        "effective_MBps": round((total / 1e6) / secs, 1) if secs > 0 else float("nan"),
    }


@env.task
async def metadata_throughput(meta_files: int = 20000) -> dict[str, float]:
    """Small-file create rate and stat-traversal rate."""
    vol = Volume.new()
    mnt, meta, cache = _paths(vol.name)
    await vol.mount(mount_path=mnt, meta_dir=meta, cache_dir=cache)
    d = Path(mnt) / "many"
    d.mkdir(parents=True, exist_ok=True)

    t0 = time.perf_counter()
    for i in range(meta_files):
        (d / f"f{i:07d}").write_bytes(b"")
    create_s = time.perf_counter() - t0

    t0 = time.perf_counter()
    count = 0
    for root, _dirs_, files in os.walk(d):
        for f in files:
            os.stat(os.path.join(root, f))
            count += 1
    stat_s = time.perf_counter() - t0

    return {
        "create_files_per_s": round(meta_files / create_s, 1) if create_s > 0 else float("nan"),
        "stat_files_per_s": round(count / stat_s, 1) if stat_s > 0 else float("nan"),
    }


def _md_table(rows: list[tuple[str, str]]) -> str:
    out = ["| Metric | Value |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in rows]
    return "\n".join(out)


@env.task
async def main(
    file_counts: list[int] | None = None,
    write_mb: int = 1024,
    commit_mb: int = 1024,
    meta_files: int = 20000,
) -> dict[str, dict[str, float]]:
    """Run all benchmarks and log a Markdown summary."""
    file_counts = file_counts or [100, 1000, 10000, 50000]

    mounts = await mount_vs_files(file_counts=file_counts)
    writes = await write_throughput(write_mb=write_mb)
    commit = await commit_cost(commit_mb=commit_mb)
    meta = await metadata_throughput(meta_files=meta_files)

    rows: list[tuple[str, str]] = []
    rows += [(f"mount time @ {n} files (s)", f"{v}") for n, v in mounts.items()]
    rows += [(f"write throughput — {k} (MB/s)", f"{v}") for k, v in writes.items()]
    rows += [(f"commit — {k}", f"{v}") for k, v in commit.items()]
    rows += [(f"metadata — {k}", f"{v}") for k, v in meta.items()]
    logger.info("Benchmark results:\n%s", _md_table(rows))

    return {"mount_vs_files": mounts, "write_throughput": writes, "commit_cost": commit, "metadata": meta}


if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(main)
    print(run.url)
