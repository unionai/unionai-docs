---
title: Keep a sandbox and come back to it
description: Reach the same sandbox by name from Python or the CLI, suspend it when you leave, and start it again from the disk and snapshot recorded as an artifact.
weight: 11
variants: -flyte +union
---

# Keep a sandbox and come back to it

An agent has spent an hour in a sandbox: it cloned a repository, installed dependencies, and started a dev server. Then its process restarts, or your laptop goes to sleep. You want the same sandbox back, not a new one. `env.connect(name)` gives you the sandbox of that name, creates it if there is none, and records its state as an artifact when it stops, so you can start again from there.

```python
from datetime import timedelta

from flyteplugins.union import sandbox

vm = sandbox.SandboxEnvironment(name="agent-vm", network=sandbox.Network.internet())

async with vm.connect("agent-7", on_exit="suspend", keep=timedelta(minutes=30)) as sb:
    print(sb.connected, sb.generation)  # "created", 0 the first time
    await sb.run("apt-get update && apt-get install -y git")
    await sb.run("git clone https://github.com/octo/repo /work/repo")

# Later, from this process or any other:
async with vm.connect("agent-7") as sb:  # "resumed": files and processes as they were
    await sb.run("cd /work/repo && make test")
```

> [!NOTE]
> `env.connect`, `flyte connect sandbox`, and `flyte get sandbox` work with both [runtimes](./runtimes), from a script, an app, or a laptop. Initialize `flyte` with a project and a domain first, as for any [sandbox outside a task](./outside-tasks).

## What connect finds

`connect` uses the sandbox in whatever state it is in. `sb.connected` says which:

| The sandbox of that name | What `connect` does | `sb.connected` |
| --- | --- | --- |
| Does not exist | Creates it from the environment | `"created"` |
| Is starting, created by another caller | Waits for it, then connects | `"attached"` |
| Is running | Connects to it as it is | `"attached"` |
| Is suspended, within its `keep` | Resumes it in place, in milliseconds, with its processes as they were | `"resumed"` |
| Has ended: suspended past its `keep`, closed, or past `max_duration` | Starts it again as its next run, from what the last run recorded | `"restored"` |

A sandbox that already exists keeps its own settings. The environment's resources, network, and runtime are used only when `connect` creates one. The same holds for `volumes=`: a sandbox keeps the volumes it was created with, and mounts them again on every run. See [Mount volumes](./volumes#what-carries-the-volumes).

The name is used exactly as you give it: 1 to 30 letters, digits, `.`, `_`, and `-`, unique in the project and domain.

## Choose what leaving does

`on_exit` decides what happens to the sandbox when the block exits:

| `on_exit` | What happens | Use it when |
| --- | --- | --- |
| `"detach"` (the default) | The sandbox keeps running, for the next connect. | The work continues without you, such as a long test run. |
| `"suspend"` | The sandbox is paused for `keep` (10 minutes by default, 1 hour at most). A connect within that resumes it in milliseconds. | You are waiting on a person or a slow tool call and want the node's CPU back. |
| `"close"` | The sandbox's run ends and its disk is recorded. Leaving the block waits for that, so a connect right after starts the next run. | The session is finished and you want only its files kept. |

With `on_exit="suspend"` and `keep=0`, the paused sandbox is not kept on its node at all. Its run ends as soon as its snapshot is committed, which frees the node, and the next connect restores it.

Each run is still bounded by the environment's `max_duration`, however often you connect to it.

## State is recorded as an artifact

A sandbox you connect to is always kept resumable. You do not call `commit()` or set `publish_on_exit`:

- **The disk is recorded when a run ends.** When the sandbox's run ends, because it was closed, stayed suspended past its `keep`, or reached `max_duration`, its disk is published as an [artifact](../artifacts/_index) named after the sandbox. This happens whatever the environment's `publish_on_exit` says.
- **A suspended sandbox keeps its memory too.** A run that ended while suspended also keeps its snapshot: the memory and processes it had when it was paused.
- **The next connect starts from there.** Connecting to a sandbox whose run has ended starts its next run from that disk, and from its memory too when the last run ended suspended. `sb.connected` is `"restored"` and `sb.generation` is one higher.

```python
async with vm.connect("agent-7", on_exit="suspend", keep=0) as sb:
    await sb.start("python server.py")
# The snapshot is committed, the run ends, and the disk is recorded as artifact "agent-7".

# Tomorrow:
async with vm.connect("agent-7") as sb:
    print(sb.connected, sb.generation)  # "restored", 1
```

Because the disk is an ordinary published disk, you can also start other, separate sessions on copies of it:

```python
from flyteplugins.union.sandbox import SandboxVolume

disk = await SandboxVolume.from_artifact("agent-7")
async with vm.session("review-agent-7", volume=disk) as sb:
    ...
```

Things to know:

- **Restoring an ended sandbox needs platform support.** On a Union.ai platform that cannot yet start a sandbox again after its run has ended, `connect` raises `SandboxSessionError` with a message that says so. Resuming a suspended sandbox within its `keep` works everywhere. Connect to a new name to start over.
- **No scratch disks.** A connected sandbox cannot use a `ScratchVolume`, because its disk has to be recorded.
- **A disk belongs to its runtime.** A restored sandbox runs in the runtime that made its disk. See [Choose a runtime](./runtimes#disks-and-snapshots-belong-to-their-runtime).

> [!WARNING] Recorded state holds whatever the sandbox held
> The artifact is readable by anyone who can read artifacts in the project, and a snapshot contains the sandbox's memory, including any secret a process had read. A sandbox that ran untrusted code hands whatever that code left on disk to its next run. See [Network and security](./network-and-security#trade-offs-to-plan-for).

## Use it from the CLI

`flyte connect sandbox` is the same thing from a terminal. It opens a shell in the sandbox of that name, and creates the sandbox if there is none:

```bash
flyte connect sandbox my-agent
flyte connect sandbox my-agent --runtime gvisor --cpu 2 --memory 4Gi --network pypi
```

Press `Ctrl-]` to detach, or exit the shell. Unlike `env.connect`, leaving suspends the sandbox by default, for 10 minutes. Run the same command again to carry on: within that time the sandbox is resumed with its processes as they were, and after it the sandbox is restored from its recorded state. The shell itself is found again by name, unless it has exited.

| Option | Default | What it sets |
| --- | --- | --- |
| `--on-exit` | `suspend` | What leaving does: `suspend`, `detach`, or `close`. |
| `--keep` | `10m` | How long a suspended sandbox is kept, 1 hour at most. |
| `--runtime` | `microvm` | `microvm` or `gvisor`, for a sandbox this creates. |
| `--cpu`, `--memory` | 1 vCPU, 1 GiB | The size of a sandbox this creates. |
| `--network` | `none` | `none`, `pypi`, or `internet`, for a sandbox this creates. |
| `--max-duration` | 1 hour | The longest each run of a sandbox this creates lives, such as `2h`. |
| `--env` | None | A `SandboxEnvironment` to create the sandbox from: `module:variable` or `path/to/file.py:variable`. |
| `--with-volume` | None | `PATH=VOLUME`: mount a block volume, by its locator, read-only in a sandbox this creates. Repeatable. See [Mount volumes](./volumes#mount-a-volume-from-the-cli). |
| `--new-shell` | Off | Start a new shell instead of attaching to the running one. |

There is no separate command to create a sandbox. `flyte connect sandbox NAME` creates it the first time.

List the sandboxes in a project, or show one and the runs it has had:

```bash
flyte get sandbox
flyte get sandbox my-agent
```

Each time a sandbox is restored after its run ended, it gets a new run, counted by its generation.

Pause a running sandbox without opening a shell in it. A connect within `--keep` (10 minutes by default, 1 hour at most) resumes it where it was:

```bash
flyte suspend sandbox my-agent
flyte suspend sandbox my-agent --keep 1h
```

Delete sandboxes you are done with:

```bash
flyte delete sandbox my-agent
flyte delete sandbox agent-1 agent-2 --yes --reason "experiment finished"
```

A deleted sandbox is gone for good. Its run is aborted if one is running, the disks its runs kept are dropped, and it can't be connected to or resumed again. Its name is free for a new sandbox. The command asks for confirmation unless you pass `--yes`.

## Find a sandbox without creating one

Sometimes a missing sandbox is an error, not a reason to make one. An app that receives a command for sandbox `agent-7` should answer "not found" if there is no such sandbox. Pass `create=False`:

```python
try:
    async with vm.connect("agent-7", create=False) as sb:
        await sb.run("ls")
except sandbox.SandboxNotFound:
    ...  # no sandbox of that name
except sandbox.SandboxSessionError:
    ...  # it exists, but its run has ended
```

With `create=False`, `connect` only finds a sandbox:

- It connects to one that is running, and waits for one that is starting.
- It resumes one that is suspended within its `keep`.
- It never creates a sandbox. If there is none of that name, it raises `SandboxNotFound`, a kind of `SandboxSessionError`.
- It never starts a sandbox again after its run has ended. That raises `SandboxSessionError`.
- It takes no `volume` and no `volumes`, because it creates nothing.

It also reaches a sandbox that `env.session(name)` started outside a task, by its `sb.name`. Leaving the block does `on_exit`, as for any connect: by default the sandbox keeps running. See [Reconnect to a session](./outside-tasks#reconnect-to-a-session).

> [!NOTE] Coming from an earlier release
> `env.connect(name, create=False)` replaces `env.attach(name)` and `env.attach(name, resume=True)`. Unlike `attach` without `resume`, it resumes a suspended sandbox.
