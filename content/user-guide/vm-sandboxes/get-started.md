---
title: Get started
description: Install the plugin, open your first Sandbox VM from a task and from your laptop, and run code in it.
weight: 1
variants: -flyte +union
---

# Get started with Sandbox VMs

This page takes you from an empty file to code running in a Sandbox VM, first from a task and then from a script on your laptop.

## Prerequisites

- A Union.ai data plane that can run the runtime you use. The examples on this page use the default, a microVM, which needs special node configuration and setup: talk to your Union.ai solutions team if it is not enabled yet. To run them without microVM nodes, add `runtime_class="gvisor"` to each `SandboxEnvironment`. See [Choose a runtime](./runtimes).
- A working `flyte` configuration for your Union.ai control plane. See [Get started](../get-started/_index).
- Permission to create runs in the project you use. Opening a sandbox takes the same permission.

Install the plugin locally:

```bash
pip install "flyteplugins-union>=0.26.0"
```

## Open a sandbox from a task

Create `sandbox_hello.py`:

```python
import flyte
from flyteplugins.union import sandbox

# The sandbox: 1 vCPU and 1 GiB of memory, no network, closed after 10 minutes at most.
code_runner = sandbox.SandboxEnvironment(
    name="code-runner",
    resources=flyte.Resources(cpu=1, memory="1Gi"),
    max_duration=600,
)

# The task that drives it. Its image needs the plugin.
env = flyte.TaskEnvironment(
    name="sandbox-hello",
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-union>=0.26.0"),
    resources=flyte.Resources(cpu=1, memory="1Gi"),
)

# Code an LLM might have written. It runs in the VM, never in the task's pod.
GENERATED = """
import platform
print(f"{sum(range(10))} from {platform.node()}")
"""


@env.task
async def hello() -> str:
    async with code_runner.session("run-generated-code") as sb:
        print(f"sandbox {sb.name} ready in {sb.startup.total * 1000:.0f} ms")
        await sb.fs.write_text("main.py", GENERATED)  # relative paths are under /work
        result = await sb.run(["python", "main.py"])  # raises if it exits nonzero
        return result.stdout.strip()


if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(hello)
    print(run.url)
```

Run it:

```bash
python sandbox_hello.py
```

or with the CLI:

```bash
flyte run sandbox_hello.py hello
```

Open the run in the UI. The sandbox session appears as a child action of `hello`, named `run-generated-code`. The task's output is `45 from` followed by the VM's hostname, and its logs show how long the sandbox took to start:

```text
sandbox run-generated-code ready in ... ms
```

Here is what happened:

1. `sandbox.SandboxEnvironment` declares what each sandbox looks like. Nothing is created until a session starts, and nothing is built or registered when you deploy it.
2. `code_runner.session("run-generated-code")` asks for a microVM, waits until it answers, and yields a `Sandbox`. The name says what the session is for. It names the session's action, so a run's sessions read in order.
3. `sb.fs.write_text` writes a file into the VM. `sb.run` runs a command to the end and returns its exit code, stdout, and stderr.
4. Leaving the block closes the session. Its commands are stopped and the VM is torn down.

## Run several sandboxes at once

Each session is its own VM, so sessions run side by side. Add a task to `sandbox_hello.py` that opens one session per input with `asyncio.gather`:

```python
import asyncio


@env.task
async def fanout(n: int = 4) -> list[str]:
    async def one(i: int) -> str:
        async with code_runner.session(f"square-{i}") as sb:
            result = await sb.run(["python", "-c", f"print({i} * {i})"])
            return result.stdout.strip()

    return list(await asyncio.gather(*(one(i) for i in range(n))))
```

```bash
flyte run sandbox_hello.py fanout --n 8
```

The run shows eight child actions, `square-0` to `square-7`, that start in parallel. The task returns `["0", "1", "4", "9", "16", "25", "36", "49"]`.

## Open a sandbox from your laptop

You can open sessions without a task. This is useful when your agent loop or RL driver already runs somewhere else, or while you are developing.

```python
import asyncio

import flyte
from flyteplugins.union import sandbox

code_runner = sandbox.SandboxEnvironment(name="code-runner", max_duration=600)


async def main() -> None:
    async with code_runner.session("laptop-hello") as sb:
        result = await sb.run("uname -a && python --version")
        print(result.stdout)


if __name__ == "__main__":
    # Sessions outside a task are created in this project and domain.
    flyte.init_from_config(project="<your-project>", domain="development")
    asyncio.run(main())
```

Replace `<your-project>` with a project you can create runs in. The same VMs start in your data plane. Your laptop reaches them through the Union.ai data proxy, signed in as you, so each call takes longer than it does from a task. See [Use sandboxes outside a task](./outside-tasks).

## Install packages in the sandbox

A sandbox runs the platform's Debian base image with Python. To install packages, give it a network that reaches the package index:

```python
data_runner = sandbox.SandboxEnvironment(
    name="data-runner",
    network=sandbox.Network.pypi(),  # only pypi.org and files.pythonhosted.org
)

async with data_runner.session("analysis") as sb:
    await sb.run("pip install pandas")
    result = await sb.run(["python", "-c", "import pandas; print(pandas.__version__)"])
```

If you install the same packages for every session, install them once and commit the disk. Later sessions start on a copy of it in a couple of seconds. See [Save and fork disks](./persist-and-fork).

## Next steps

- [Configure a sandbox](./configure): resources, environment variables, secrets, and lifetime.
- [Run commands](./commands) and [work with files](./files).
- [Network and security](./network-and-security): what code in a sandbox can and cannot reach.
- [Save and fork disks](./persist-and-fork) and [snapshot, suspend, and resume](./snapshots).
