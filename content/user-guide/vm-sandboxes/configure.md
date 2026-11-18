---
title: Configure a sandbox
description: Size a VM sandbox, set its environment variables and secrets, bound its lifetime, and choose its queue and labels.
weight: 3
variants: -flyte +union
---

# Configure a sandbox

An agent that runs tests needs more CPU than one that evaluates a single expression. One that calls a model API needs a key. One that might hang needs a deadline. You declare all of this once, on a `sandbox.SandboxEnvironment`, and every session you open from it gets the same settings.

```python
from datetime import timedelta

import flyte
from flyteplugins.union import sandbox

test_runner = sandbox.SandboxEnvironment(
    name="test-runner",
    resources=flyte.Resources(cpu=2, memory="4Gi"),
    env_vars={"PYTHONUNBUFFERED": "1"},
    secrets=[flyte.Secret(key="github-read-token", as_env_var="GITHUB_TOKEN")],
    network=sandbox.Network.allow("github.com", "*.github.com", "pypi.org", "files.pythonhosted.org"),
    max_duration=timedelta(minutes=30),
    labels={"team": "agents"},
)
```

## Options

| Parameter | Default | What it sets |
| --- | --- | --- |
| `name` | Required | The environment's name. It appears in error messages. |
| `resources` | 1 vCPU, 1 GiB | The VM's size, from the `cpu` and `memory` of a `flyte.Resources`. |
| `env_vars` | None | Environment variables for every command in the session. |
| `secrets` | None | Union.ai secrets the session gets, as a task with them would. |
| `runtime_class` | `"microvm"` | What sessions run in: `"microvm"` or `"gvisor"`. Needs `flyteplugins-union` 0.22.0 or later. See [Choose a runtime](./runtimes). |
| `network` | `Network.blocked()` | Outbound network. See [Network and security](./network-and-security). |
| `max_duration` | 3600 seconds | The longest one session lives if its block doesn't exit first. Seconds or a `timedelta`. |
| `queue` | The run's queue | The queue sessions go to. See [Queues](../clusters-and-queues/queues). |
| `labels` | None | Labels on the runs of sessions started outside a task. |
| `publish` | `False` | Publish each session's disk as an artifact when it ends. See [Save and fork disks](./persist-and-fork#publish-a-disk-as-an-artifact). |
| `snapshot_every` | None | How often to write a running session's disk to storage, at least 30 seconds. Only useful with `publish`. It does not create a `SandboxSnapshot`. |
| `expiry` | None | How long disks committed from these sessions should be kept. Recorded on each volume as `expires_at`, and not enforced yet. |

## Size the VM

Set `resources` with a `flyte.Resources` that has `cpu` and `memory`:

```python
sandbox.SandboxEnvironment(name="builder", resources=flyte.Resources(cpu=4, memory="8Gi"))
```

A session's VM is sized by CPU and memory alone. Setting `gpu`, `disk`, or `shm` raises a `ValueError` when the environment is created. Each VM gets 7.8 GiB of disk.

## Set environment variables and secrets

`env_vars` and `secrets` work as they do on a `flyte.TaskEnvironment`. Every command in the session sees them.

```python
sandbox.SandboxEnvironment(
    name="llm-tool-runner",
    env_vars={"MPLBACKEND": "Agg"},
    secrets=[flyte.Secret(key="openai", as_env_var="OPENAI_API_KEY")],
    network=sandbox.Network.allow("api.openai.com"),
)
```

You can also pass `env` for a single command with `sb.run(command, env={...})`.

> [!WARNING] Code in the sandbox can read its secrets
> A secret given to a sandbox is readable by every command that runs in it, including the untrusted code you are isolating. Give a sandbox only secrets that code is allowed to have. Keep model API keys and other credentials in the task or script that drives the sandbox, and pass results in and out. See [Network and security](./network-and-security#secrets).

## Bound a session's lifetime

A session ends when its `async with` block exits, or when it reaches `max_duration`, whichever comes first. A session that reaches `max_duration` is ended, and any later call on it raises `SandboxSessionEnded`.

When a session closes, its commands get `SIGTERM`, then `SIGKILL` if they are still running 10 seconds later. Leaving the block returns once the sandbox has closed. To change the grace period (60 seconds at most), or to wait until the session itself has ended, close it yourself before the block exits:

```python
await sb.close(grace=30, wait=True)
```

`await sb.cancel()` aborts the session instead. Its commands are killed at once and the session ends as aborted, not succeeded.

There is no idle timeout. A session that you open and forget lives until `max_duration`, so set it close to the longest you expect a session to need.

Each `env.session()` call also takes a `ready_timeout` (default 120 seconds). If the session isn't ready in that time, the call raises `SandboxSessionError` and stops the session it asked for.

## Choose a queue

Sessions go to the queue of the run that starts them. Set `queue` to send them somewhere else, for example to a cluster that has a microVM node pool when your tasks run on another:

```python
sandbox.SandboxEnvironment(name="code-runner", queue="sandbox-queue")
```

## Label sessions

Outside a task, every session is a run of its own. Put the same label on all the sessions of a job to find them together:

```python
rollout_env = sandbox.SandboxEnvironment(name="rollout", labels={"job": "rollouts-1115"})
```

```bash
flyte get run --with-label job=rollouts-1115
```

Inside a task, a session is an action of the task's run and uses the run's labels. `labels` has no effect there.

## The sandbox image

A session runs the platform's base image: Debian 13 with Python, running as root, with `apt-get` and `pip`. It does not include `curl`, `git`, or `sudo` until you install them. To use your own tools, install them at runtime and commit the disk, then start later sessions on that disk. See [Save and fork disks](./persist-and-fork).

Custom images (`image=`) are not supported. See [Limits and errors](./limits) for the full description of the machine.
