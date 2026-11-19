---
title: Choose a runtime
description: Run a sandbox as a Firecracker microVM or as a gVisor sandbox, and understand what each needs from your cluster and what each isolates.
weight: 2
variants: -flyte +union
---

# Choose a runtime: microVM or gVisor

You want to give your agent a sandbox today, but your data plane has no nodes that can run virtual machines. Or your agent has to build a container image, so it needs Docker inside the sandbox. Both are settled by one setting, `runtime_class`, which decides what a sandbox runs in.

```python
from flyteplugins.union import sandbox

# A gVisor sandbox. Runs on any node, with no special node pool.
code_runner = sandbox.SandboxEnvironment(name="code-runner", runtime_class="gvisor")

# A Firecracker microVM, the default. Needs nodes set up for microVMs.
image_builder = sandbox.SandboxEnvironment(name="image-builder", runtime_class="microvm")
```

Everything else is the same. You open sessions, run commands, and move files with the same calls, whichever runtime you choose.

## Compare the runtimes

| | `"microvm"` (default) | `"gvisor"` |
| --- | --- | --- |
| What a session is | A Firecracker microVM | A gVisor sandbox |
| Kernel | A Linux guest kernel of its own | A user-space kernel that handles the sandbox's system calls |
| Nodes it needs | Nodes with hardware virtualization: bare metal, or instance types with nested virtualization | Any node |
| Setup in your data plane | Special node configuration and setup. Talk to your Union.ai solutions team. | No special node resources |
| Docker, kernel modules, mounting file systems | Yes | No. Use a microVM for these. |
| Use from a task, an app, or a laptop | Yes | Yes |
| Suspend and resume | Yes | Yes |
| Saved disks and snapshots | Start only microVM sessions | Start only gVisor sessions |

## Which one to use

Use `"gvisor"` when:

- You want to start now, on the nodes you already have.
- The code needs a Python and shell environment: run scripts, install packages, run tests.
- You do not want to operate a separate node pool for sandboxes.

Use `"microvm"` when:

- The code needs a real kernel: a Docker daemon, kernel modules, or its own mounts.
- You want the strongest boundary between untrusted code and your nodes. See [Isolation trade-offs](#isolation-trade-offs).
- Your Union.ai solutions team has set up microVM nodes in your data plane.

## Use it from your laptop, and suspend and resume

Both runtimes work from a task, from an app, and from a script on your laptop, and both can be suspended and resumed. This script opens a gVisor sandbox from a laptop, pauses it, and picks it up again with its files and processes as they were:

```python
import asyncio

import flyte
from flyteplugins.union import sandbox

scratch = sandbox.SandboxEnvironment(name="scratch", runtime_class="gvisor", max_duration=1800)


async def main() -> None:
    async with scratch.session("notes") as sb:
        await sb.fs.write_text("notes.txt", "remember this\n")
        snap = await sb.suspend(keep=600)  # paused; kept for up to 10 minutes

    async with scratch.session("notes", snapshot=snap) as sb:
        print((await sb.run("cat notes.txt")).stdout)


if __name__ == "__main__":
    flyte.init_from_config(project="<your-project>", domain="development")
    asyncio.run(main())
```

To open a shell in a sandbox from a terminal, pick the runtime with `--runtime`:

```bash
flyte connect sandbox my-sandbox --runtime gvisor
```

Leaving that shell suspends the sandbox, and the same command resumes it. See [Keep a sandbox and come back to it](./reconnect), [Use sandboxes outside a task](./outside-tasks), and [Snapshot, suspend, and resume](./snapshots).

## Disks and snapshots belong to their runtime

A committed disk, a published disk, or a snapshot can only start sessions of the runtime that made it. A disk committed by a gVisor session does not start a microVM session, and a microVM's disk does not start a gVisor session.

If you use both runtimes, build your environment once for each. A session restored from a snapshot runs in the runtime that took the snapshot, whatever `runtime_class` the environment you restore it through has.

## Isolation trade-offs

Both runtimes keep untrusted code away from the node's kernel. They do it in different ways, and the difference matters when you decide how much to trust the boundary.

- **A microVM is a hardware virtual machine.** The code runs on its own guest kernel. An exploit of that kernel is still inside the VM, and has to get through the hypervisor to reach the node. MicroVMs run on a dedicated node pool, separate from the nodes that run your task pods.
- **A gVisor sandbox is a process on the node.** A user-space kernel handles the code's system calls, so the code does not call the node's kernel directly. There is no hardware virtualization boundary: an escape from gVisor lands on a node that also runs other workloads.

For code you consider hostile, or for workloads where sandboxes of different customers share nodes, use `"microvm"`. For code from your own models and agents, where the main risks are mistakes and prompt injection, `"gvisor"` is a reasonable place to start. The rest of what you put in a sandbox carries the same risk in both runtimes: secrets, network access, and published disks. See [Network and security](./network-and-security).

## Requirements

- `flyteplugins-union` 0.23.0 or later.
- For `"microvm"`: a data plane with microVM support enabled. This needs special node configuration and setup. Talk to your Union.ai solutions team.
- For `"gvisor"` inside a task: a `flyte` release recent enough to schedule gVisor sessions. With an older one, opening the session raises `SandboxUsageError` with a message that says to upgrade `flyte`. Sessions opened outside a task do not have this requirement.
