---
title: Save and fork disks
description: Commit a VM sandbox's disk, start new sandboxes on copy-on-write copies of it, fork running sandboxes, pass disks between tasks, and publish them as artifacts.
weight: 6
variants: -flyte +union
---

# Save and fork disks

Setting up an environment is slow. Cloning a repository and installing its dependencies can take minutes, and a coding agent might want to try ten fixes against it. VM sandboxes let you do the setup once, commit the disk, and start every attempt on its own copy. Each copy is copy-on-write, so it starts in a couple of seconds and no attempt sees another's writes.

```python
from flyteplugins.union import sandbox

build_env = sandbox.SandboxEnvironment(name="build", network=sandbox.Network.internet())
attempt_env = sandbox.SandboxEnvironment(name="attempt")  # no network

async with build_env.session("build-testbed") as sb:
    await sb.run("apt-get update && apt-get install -y git")
    await sb.run("git clone https://github.com/octo/repo /testbed && pip install -e /testbed")
    testbed = await sb.commit()  # a SandboxVolume

async with attempt_env.session("attempt-0", volume=testbed) as sb:
    result = await sb.run("cd /testbed && pytest -x", check=False)
```

Sandboxes are durable this way. A committed disk is stored in your data plane's object store and outlives the session that made it. You can pass it to another task, return it from a run, or publish it as an artifact and start from it next week.

## Choose how to save state

Every way to keep a sandbox's state answers two questions: what is kept, and what happens to the session you took it from.

| Call | Keeps | The session afterwards | A new session from it starts in | Use it to |
| --- | --- | --- | --- | --- |
| `sb.commit()` | Disk | Keeps running | About 2 seconds | Build an environment once and start many sessions on copies of it. |
| `sb.fork_close()` | Disk | Closed | About 2 seconds | Keep the result of a session that is finished. |
| `sb.fork(name)` | Disk | Parent and child both run | About 2 seconds | Try alternatives side by side from the same files. |
| `sb.fork(name, memory=True)` | Disk, memory, processes | Parent and child both run | About 2 seconds | Branch a running process, such as a loaded interpreter. |
| `sb.snapshot()` | Disk, memory, processes | Keeps running, after a pause of about half a second for a 1 GiB VM | About 2 seconds | Start many sessions from one warmed-up state. |
| `sb.suspend()` | Disk, memory, processes | Paused for up to `keep` (1 hour at most) | Milliseconds when resumed in place, about 2 seconds otherwise | Wait on a person or a long tool call. |
| `SandboxEnvironment(publish=...)` | Disk | Published when the session ends cleanly | About 2 seconds | Keep a disk beyond a run and find it by name. |

This page covers the calls that keep a disk. For the ones that keep memory and processes, see [Snapshot, suspend, and resume](./snapshots).

## The disk a session runs on

Every session runs on one of three kinds of disk:

| You pass | The session's disk | Can be committed or forked |
| --- | --- | --- |
| Nothing: `env.session("build")` | A new, empty `SandboxVolume`. The default. | Yes |
| `volume=v`, a `SandboxVolume` | A copy-on-write copy of `v`. `v` itself is never changed. | Yes |
| `volume=sandbox.ScratchVolume()` | A disk on the node that ends with the session. | No |

Use `ScratchVolume()` for throwaway work you never need to keep. Committing, forking, snapshotting, or suspending a scratch session raises `SandboxUsageError`.

## Commit a disk

`await sb.commit()` commits the session's disk as it is at that moment and returns a `SandboxVolume`. The session keeps running. Its writes wait while the disk is frozen for the commit.

A `SandboxVolume` is immutable. Any number of sessions, on any node in the same cluster, can start on copies of it at the same time.

To close a session and keep its disk in one step, use `fork_close()`. Its commands are stopped first, so the disk is committed as they left it:

```python
volume = await sb.fork_close()
```

Leaving the `async with` block after `fork_close()` does nothing more.

## Fork a running sandbox

`sb.fork(name)` commits the disk and opens a new session on a copy of it. The child boots fresh with every file the parent had. Both keep running independently.

This example tries three candidate fixes at once, each on its own fork, and keeps the one that passes:

```python
import asyncio
from typing import Optional

import flyte
from flyteplugins.union import sandbox
from flyteplugins.union.sandbox import SandboxVolume

runner = sandbox.SandboxEnvironment(name="fix-runner", max_duration=600)
env = flyte.TaskEnvironment(
    name="fix-bug",
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-union>=0.21.2"),
)

STATS = "def mean(xs):\n    return sum(xs) / len(xs)\n"
TEST = "from stats import mean\nassert mean([1, 2]) == 1.5\nassert mean([]) == 0\nprint('ok')\n"
CANDIDATES = [
    "def mean(xs):\n    return sum(xs) / max(len(xs), 1) if xs else None\n",
    "def mean(xs):\n    return sum(xs) // len(xs) if xs else 0\n",
    "def mean(xs):\n    return sum(xs) / len(xs) if xs else 0\n",
]


@env.task
async def fix_bug() -> SandboxVolume:
    async with runner.session("workspace") as workspace:
        await workspace.fs.write_text("stats.py", STATS)
        await workspace.fs.write_text("test_stats.py", TEST)

        async def attempt(i: int, fix: str) -> Optional[SandboxVolume]:
            async with workspace.fork(f"trial-{i}") as trial:
                await trial.fs.write_text("stats.py", fix)
                result = await trial.run(["python", "test_stats.py"], check=False)
                return await trial.fork_close() if result.ok else None

        results = await asyncio.gather(*(attempt(i, fix) for i, fix in enumerate(CANDIDATES)))

    fixed = next((v for v in results if v is not None), None)
    if fixed is None:
        raise RuntimeError("no candidate passed")
    return fixed


@env.task
async def review(fixed: SandboxVolume) -> str:
    async with runner.session("verify-fix", volume=fixed) as sb:
        return (await sb.run(["python", "test_stats.py"])).stdout.strip()


@env.task
async def main() -> str:
    return await review(await fix_bug())
```

`sb.fork(name, memory=True)` copies memory and running processes too. See [Snapshot, suspend, and resume](./snapshots).

## Pass disks between tasks

A `SandboxVolume` is a regular task input and output. In the example above, `fix_bug` returns the disk of the trial that passed, and `review`, another task, starts a session on a copy of it.

Because it is a task output, a `SandboxVolume` works with [caching](../tasks/task-configuration/caching). Put an expensive environment build in a cached task, and later runs reuse the committed disk instead of building it again:

```python
@env.task(cache="auto")
async def build_testbed(repo: str, commit: str) -> SandboxVolume:
    async with build_env.session("build") as sb:
        await sb.run("apt-get update && apt-get install -y git")
        await sb.run(["git", "clone", repo, "/testbed"])  # lists keep inputs out of the shell
        await sb.run(["git", "checkout", commit], cwd="/testbed")
        await sb.run("pip install -e /testbed")
        return await sb.commit()
```

## Publish a disk as an artifact

To keep a disk beyond a run, have the platform publish it as an [artifact](../artifacts/_index). Set `publish` on the environment. When each session ends, its disk is committed and published, with no call in your code:

```python
builder = sandbox.SandboxEnvironment(
    name="builder",
    network=sandbox.Network.internet(),
    publish="python-data-stack",  # True names the artifact after the session
    snapshot_every=60,
)

async with builder.session("build") as sb:
    await sb.run("pip install pandas polars duckdb")
# The block has exited. The disk is committed and published as the session ends.
```

Later, in any run, task, app, or script in the same project and domain, start a session on the latest version:

```python
from flyteplugins.union.sandbox import SandboxVolume

disk = await SandboxVolume.from_artifact("python-data-stack")  # or version="..."
async with runner.session("analysis", volume=disk) as sb:
    await sb.run(["python", "-c", "import pandas, polars, duckdb"])
```

How publishing works:

- **Named by you, versioned by content.** `publish="name"` names the artifact. `publish=True` names it after the session. Each version is the disk's own hash.
- **Only clean endings publish.** A session that is closed, or reaches its `max_duration`, publishes its disk. Closing stops its commands first (`SIGTERM`, then `SIGKILL` after a grace period), so the disk is published as they left it. A session that is cancelled or fails publishes nothing. If a build fails partway, call `await sb.cancel()` so the half-built disk is not published.
- **Published by the worker.** The session's worker commits the disk and reports it, and the platform registers the artifact shortly after the session's action succeeds. A task that reads the artifact right after the session closes may need to wait and retry.
- **`snapshot_every` shortens the final commit.** It writes a running session's disk to storage that often (at least every 30 seconds), without committing it. Despite its name, it does not produce a `SandboxSnapshot` or a `SandboxVolume`, and nothing can start from these writes. They leave less to write when the session ends.
- **Same cluster.** A published disk starts sessions on the cluster that committed it.

Publishing needs task artifacts enabled on your cluster. Ask your Union.ai solutions team if `from_artifact` finds nothing after a session closes cleanly.

## Record an expiry on disks

Set `expiry` to record how long disks committed from an environment's sessions should be kept. Each volume carries it as `expires_at`.

```python
from datetime import timedelta

sandbox.SandboxEnvironment(name="scratchpad", expiry=timedelta(days=7))
```

> [!NOTE] Expiry is recorded, not enforced
> In this release, `expires_at` is only recorded on the volume. Nothing deletes a disk when it passes. Do not rely on `expiry` to remove data, such as disks that hold files written by untrusted code.
