---
title: Snapshot, suspend, and resume
description: Save a VM sandbox's disk, memory, and running processes, restore new sandboxes from that point, and pause a sandbox while it waits.
weight: 7
variants: -flyte +union
---

# Snapshot, suspend, and resume

A notebook kernel has loaded a 2 GB dataframe. An agent has started a dev server and is waiting for a person to approve its plan. A committed disk would lose both: the dataframe and the server live in memory. A snapshot keeps the whole machine, its disk, memory, and processes, so a sandbox restored from it continues from the same instant.

```python
async with notebook_env.session("kernel") as sb:
    kernel = await sb.start(["python", "-i", "-q"], stdin=True)
    await kernel.stdin.write("import pandas as pd; df = pd.read_parquet('big.parquet')\n")
    snap = await sb.suspend(keep=600)  # pause; no CPU used while paused

# Later, while the snapshot is kept: resume in milliseconds, df still in memory.
async with notebook_env.session("kernel", snapshot=snap) as sb:
    ...
```

## Take a snapshot

`await sb.snapshot()` captures the session's disk, memory, and processes at one instant and returns a `SandboxSnapshot` once it is committed. The session keeps running.

Start a new session from it with `env.session(name, snapshot=snap)`. The new session's processes run on from that instant, on a copy of the disk. You can restore any number of sessions from one snapshot, and each runs independently.

```python
async with env.session("warm") as sb:
    await sb.start("python serve_model.py")  # loads weights, then waits
    await sb.run("until [ -f /tmp/ready ]; do sleep 0.5; done")
    warm = await sb.snapshot()

async def episode(i: int) -> str:
    async with env.session(f"episode-{i}", snapshot=warm) as ep:
        return (await ep.run("python run_episode.py")).stdout

results = await asyncio.gather(*(episode(i) for i in range(8)))
```

Timing, for a 1 GiB VM:

- The VM pauses for about half a second while its memory is written on the node. Later snapshots of the same session write only what changed.
- Committing takes about as long again.
- With `sb.snapshot(wait=False)`, the call returns as soon as the VM runs again, with a `SnapshotFuture`. `await fut.wait()` returns the snapshot when it is committed. Until then, writes to the disk wait, about 1.8 seconds in all. CPU, memory, and reads don't.

A restored session starts in about two seconds.

### What a snapshot resets

- **Connections.** Writing a snapshot resets the sandbox's connections. A `sb.run()` in flight is cut and its command stopped. Commands started with `sb.start()` keep running. Network connections inside the VM close.
- **Time.** A restored session's processes see the time between as a stall: their clock jumps. Timeouts and leases may have expired.
- **Shared state.** Every restored session shares what the processes held at the snapshot: secrets they read, random state already drawn, and locks taken. Reseed random number generators after restoring if sessions must differ.
- **Hardware.** A restored session needs the snapshot's CPU and memory, and a node like the one it was taken on.

To start a session on a snapshot's disk only, without memory, pass it as a volume: `env.session(name, volume=snap)`.

## Fork with memory

`sb.fork(name, memory=True)` takes a snapshot and restores a child session from it in one call. The child continues from where the parent was, processes and all:

```python
async with sb.fork("branch-a", memory=True) as child:
    await child.run("python try_approach_a.py")
```

Without `memory=True`, `fork` copies only the disk. See [Save and fork disks](./persist-and-fork#fork-a-running-sandbox).

## Suspend and resume

`await sb.suspend(keep=...)` pauses the session where it is and returns its `SandboxSnapshot`. Use it when a session has to wait: on a person, on a long tool call, or between turns of a conversation.

- **Resume in place.** While the VM is kept on its node, `env.session(name, snapshot=snap)` on the same `SandboxEnvironment` object, in the same process, resumes it there in milliseconds. It keeps its name.
- **`keep` bounds the pause.** The VM stays paused for `keep` (default 5 minutes, at most 1 hour), and no longer than the session's `max_duration`, which keeps counting while it is paused.
- **Restore after `keep`.** If it isn't resumed in time, the session ends and succeeds. Its snapshot outlives it, and `env.session(name, snapshot=snap)` restores a new session from it, in this task or another.
- **Discard it.** `await sb.cancel()` discards a suspended session.

Suspending takes about 2 seconds for a 1 GiB VM, most of it committing the snapshot. The VM is paused within the first few hundred milliseconds. `sb.suspend(wait=False)` returns as soon as the VM is paused, with a `SnapshotFuture`. You can pass the future straight to `env.session(snapshot=fut)`, which waits for the commit if it is still running.

After a suspend, `Process` handles from `sb.start()` end. Their commands keep running in the VM, and you can reattach to them with `sb.process(id)` after resuming. A `sb.run()` in flight is cut.

## Pass snapshots between tasks

A `SandboxSnapshot` is a task input and output, like a `SandboxVolume`. One task can warm up a sandbox and return its snapshot, and others can restore from it:

```python
from flyteplugins.union.sandbox import SandboxSnapshot


@env.task
async def warm_up() -> SandboxSnapshot:
    async with sandbox_env.session("warm-up") as sb:
        await sb.run("python -c 'import torch'")  # warms the page cache
        return await sb.snapshot()


@env.task
async def rollout(warm: SandboxSnapshot, seed: int) -> float:
    async with sandbox_env.session(f"rollout-{seed}", snapshot=warm) as sb:
        result = await sb.run(["python", "rollout.py", "--seed", str(seed)])
        return float(result.stdout)
```

Snapshots are stored in your data plane's object store.

> [!WARNING] Snapshots copy memory
> A snapshot contains everything in the VM's memory, including any secret a process has read. Treat a snapshot with the same care as the secrets the sandbox had. See [Network and security](./network-and-security#snapshots-and-forks-with-memory).
