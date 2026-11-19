---
title: Limits and errors
description: What a VM sandbox's machine looks like, what sandboxes don't support, and the errors they raise.
weight: 11
variants: -flyte +union
---

# Limits and errors

## The machine

| | |
| --- | --- |
| Operating system | Debian 13, running as root, with Python, `apt-get`, and `pip` |
| Not installed | `curl`, `git`, `sudo`. Install them with `apt-get`. |
| CPU and memory | 1 vCPU and 1 GiB by default. Set with `resources`. |
| Disk | 7.8 GiB. One command may write a file of at most 4 GiB. |
| Working directory | `/work`. Relative paths in `sb.fs` and `cwd` are under it. |
| File transfers | At most 512 MiB per file through `sb.fs` |
| Command output kept | The last 64 MiB of stdout and of stderr per command |
| cgroups | Not mounted. Mount `cgroup2` yourself if a program needs it, such as a Docker daemon. |

A microVM has its own kernel, so it can run software a container usually cannot, such as a Docker daemon of its own. A gVisor sandbox cannot: use `runtime_class="microvm"` for Docker, kernel modules, and mounts. See [Choose a runtime](./runtimes). Docker's `overlay2` driver needs a disk image of its own to live on, because the root disk is an overlay. The kernel has no nftables, so a Docker daemon must use iptables.

## Not supported

These raise a `ValueError` when you create the `SandboxEnvironment`, rather than being ignored:

- **Custom images** (`image=`). A session runs the platform's base image. Install what it needs at runtime and commit the disk. See [Save and fork disks](./persist-and-fork).
- **GPU, disk, and shm resources.** A VM is sized by `cpu` and `memory` only.
- **Pod settings**: `pod_template`, `service_account`, `interruptible`, and `include`. A session is a microVM, not a pod.

These are not available:

- **An idle timeout.** A session lives until its block exits or it reaches `max_duration`.
- **Passing `flyte.io.File` or `flyte.io.Dir` into a sandbox directly.** Download them in the task and copy them with `sb.fs`. See [Work with files](./files).
- **Reaching a task's session from outside the cluster.** A script outside the cluster can only reach sessions it started or connected to.
- **Removing disks by age.** Nothing deletes a committed or published disk when it gets old. See [Save and fork disks](./persist-and-fork#disks-are-not-removed-by-age).

## Full nodes

A session goes to one of the microVM nodes in your cluster. A node without room for it refuses it, and the session ends with a `SandboxSessionError` whose message says it was refused, about 15 seconds after it was requested. Another node may have room. For workloads that start many sessions at once, retry a refused session a few times:

```python
import asyncio
import contextlib

from flyteplugins.union import sandbox


@contextlib.asynccontextmanager
async def open_session(env: sandbox.SandboxEnvironment, name: str, tries: int = 6, **kwargs):
    async with contextlib.AsyncExitStack() as stack:
        for attempt in range(tries):
            try:
                sb = await stack.enter_async_context(env.session(name, **kwargs))
                break
            except sandbox.SandboxSessionError as e:
                if "refused" not in str(e) or attempt == tries - 1:
                    raise
                await asyncio.sleep(2)
        yield sb
```

Ask your Union.ai solutions team to size your microVM node pool for your peak number of concurrent sessions.

## Errors

All are in `flyteplugins.union.sandbox`. Each is a Flyte user error: a task that lets one escape fails as its own error, and isn't retried as a system failure.

| Error | Raised when |
| --- | --- |
| `SandboxSessionError` | A session could not start, was not ready within `ready_timeout`, or ended before it was ready. Also raised by `env.connect(name, create=False)` when no sandbox has that name or it has ended. |
| `SandboxSessionEnded` | A call failed because the session had ended: its VM was lost, it reached `max_duration`, or it was cancelled. The message says which. A subclass of `SandboxSessionError`. |
| `SandboxCommandFailed` | A command run with `sb.run()` or waited on with `p.wait()` exited nonzero and `check` was on. `.result` is its `CommandResult`. |
| `SandboxCommandTimedOut` | A command ran past its `timeout`. A subclass of `SandboxCommandFailed`. |
| `SandboxUsageError` | A session was used in a way that can't work: after its block ended, while suspended, or committing a `ScratchVolume` session. |
| `ProcessError` | A started command could not be reattached with `sb.process(id)`, for example because it ended more than 10 minutes ago. A subclass of `SandboxSessionError`. |
| `ProcessUnsupported` | `sb.start()` with `stdin` or `tty`, or `sb.process(id)`, was called on a microVM node that predates those features. A subclass of `ProcessError`. Ask your Union.ai solutions team to update the node pool. |
