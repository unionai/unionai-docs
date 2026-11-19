---
title: Sandbox VMs
description: Run untrusted code in fast, isolated microVMs on your own Kubernetes clusters, with disks and memory you can save, fork, and restore.
icon: shield-lock
weight: 8
variants: -flyte +union
mermaid: true
---

# Sandbox VMs

> [!NOTE] Early access preview
> Sandbox VMs are in early access. The API can change between releases. A sandbox runs as a microVM, the default, or as a gVisor sandbox. MicroVM support is not enabled by default: it needs special node configuration and setup in your data plane. To enable it in your Union.ai environment, talk to your Union.ai solutions team. gVisor sandboxes need no special node resources. See [Choose a runtime](./runtimes).
>
> Sandbox VMs require `flyteplugins-union` 0.23.0 or later: `pip install "flyteplugins-union>=0.23.0"`.

A Sandbox VM is a lightweight virtual machine with its own Linux kernel. Where you don't have nodes that can run virtual machines, the same API runs a [gVisor sandbox](./runtimes) on any node. You start one from Python, run commands and move files in it, and throw it away when you are done. Use Sandbox VMs when you need to run code you did not write and do not trust: code from an LLM, from a coding agent, from your users, or from a reinforcement learning policy.

## Why Sandbox VMs

A coding agent is fixing a bug in a customer's repository. Every turn, the model writes a shell command, and your agent has to run it somewhere. The command might be `pytest`. It might also be `curl` to an address the model picked up from a prompt injection, a `pip install` of a typosquatted package, or `rm -rf /`.

If you run that command in your task's container, it runs with your task's identity. It can read the task's secrets, call your cloud's metadata server for credentials, and reach other services in your cluster. A Sandbox VM gives the command a machine of its own instead:

```python
import flyte
from flyteplugins.union import sandbox

# A VM with no network: the default.
code_runner = sandbox.SandboxEnvironment(name="code-runner")

env = flyte.TaskEnvironment(
    name="agent",
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-union>=0.23.0"),
)


@env.task
async def run_untrusted(code: str) -> str:
    async with code_runner.session("run-model-code") as sb:
        await sb.fs.write_text("main.py", code)
        result = await sb.run("python main.py", check=False)  # a failing script is a result, not an error
        return result.stdout + result.stderr
```

The code runs in a microVM that has no network and none of your task's secrets. The VM is torn down when the `async with` block exits. A new sandbox is ready in about a quarter of a second, and each later command on it takes a few milliseconds.

## What you get

- **A kernel per sandbox.** By default, each session is a Firecracker microVM with its own guest kernel, not a container that shares the node's kernel.
- **A choice of runtime.** Set `runtime_class="gvisor"` to run sessions as gVisor sandboxes on the nodes you already have, with no special node resources. Both runtimes work from a task, an app, or a laptop, and both suspend and resume. See [Choose a runtime](./runtimes).
- **Closed network by default.** A sandbox starts with no outbound network. You can open it to the internet, or allow a list of hostnames such as PyPI or your package mirror. The cloud metadata server is unreachable in every mode, so code in a sandbox cannot read your node's cloud credentials.
- **Runs in your cloud.** Sandboxes run on your own Kubernetes clusters, in your data plane. The code, the data it touches, and the VMs themselves stay in your cloud account.
- **Durable state.** Commit a sandbox's disk and start new sandboxes on copies of it. Fork a running sandbox into several. Snapshot or suspend one with its memory and processes, and resume it later. Publish a disk as an artifact that later runs can start from. Saved disks and snapshots are stored in your data plane's object store.
- **Part of Union.ai.** A sandbox started from a task is an action of that task's run, so it shows up in the run in the UI, and it uses the same identity, projects, and queues as the rest of your workloads.

## The API in one minute

You declare a `SandboxEnvironment` once. It is the template: size, network, secrets, and lifetime. Everything else is two choices.

**Two ways to get a sandbox.** Both give you a `Sandbox`, usually named `sb`, that you run commands and move files with.

| Call | What you get | When the block exits |
| --- | --- | --- |
| `env.session(name)` | A new sandbox for this block. The name is a label that says what it is for. | The sandbox is closed. |
| `env.connect(name)` | The sandbox of that exact name, created if there is none. The same one every time, from any process. | The sandbox keeps running, unless you ask to suspend or close it. |

Use `session` for work that starts and ends in one place: run this code, run this attempt. Use `connect` for a sandbox you come back to, such as an agent's workspace. See [Keep a sandbox and come back to it](./reconnect).

**Two ways to keep its state.** A sandbox's state is gone when it ends, unless you keep it.

| Call | What it keeps | What you get |
| --- | --- | --- |
| `sb.commit()` | The disk | A `SandboxVolume`. Start new sandboxes on copies of it with `env.session(name, volume=v)`. |
| `sb.snapshot()` | The disk, memory, and running processes | A `SandboxSnapshot`. Restore new sandboxes from it with `env.session(name, snapshot=s)`. |

The other calls are these two combined with something else. `sb.fork(name)` is a commit and a new sandbox on it. `sb.close(commit=True)` closes the sandbox and returns its disk. `sb.suspend()` pauses the sandbox and returns its snapshot. See [Save and fork disks](./persist-and-fork) and [Snapshot, suspend, and resume](./snapshots).

## How it works

These pages call one running sandbox a session, whichever of the two calls started it.

```mermaid
flowchart LR
    subgraph dp["Your data plane (your cloud account)"]
        subgraph tn["Task nodes"]
            T["your task<br/>(pod)"]
        end
        subgraph vn["microVM node pool"]
            V1["sandbox<br/>microVM"]
            V2["sandbox<br/>microVM"]
        end
        S[("object store<br/>disks, snapshots")]
    end
    L["laptop or script"] -. "through the data proxy" .-> V2
    T -- "commands, files" --> V1
    V1 -. "commit, snapshot" .-> S
```

1. You declare a `sandbox.SandboxEnvironment` once: its CPU and memory, network, secrets, environment variables, and how long a session may live.
2. Your code opens a session with `env.session(name)`. Union.ai schedules a microVM on a node in your microVM node pool, or a gVisor sandbox on any node if the environment sets `runtime_class="gvisor"`. No pod is started for it.
3. The session is yielded as a `Sandbox` object once it answers. You call `sb.run()`, `sb.start()`, and `sb.fs` to work in it.
4. When the block exits, the session's commands are stopped and the VM is torn down.

MicroVMs need nodes that can run hardware virtualization: bare-metal instances, or instance types with nested virtualization enabled. These nodes also need configuration that ordinary task nodes do not have, so you cannot enable microVMs by adding a node pool yourself. Your Union.ai solutions team sets up the microVM node pool in your data plane. gVisor sandboxes need none of this. See [Choose a runtime](./runtimes).

You can open sessions from a task, from an app, or from a laptop or script outside your cluster. Tasks and apps talk to the sandbox directly, which is the fastest path. From outside the cluster, every call goes through the Union.ai data proxy, signed in as you, which adds latency to each command. See [Use sandboxes outside a task](./outside-tasks).

## When to use Sandbox VMs

Flyte offers other ways to run untrusted code. See [Sandboxing](../agents/sandboxing/_index) for the full picture.

| | Sandbox VM | [Code sandbox](../agents/sandboxing/code-sandboxing) | [Workflow sandbox](../agents/sandboxing/workflow-sandboxing-flyte) |
| --- | --- | --- | --- |
| Isolation | microVM with its own kernel, or a gVisor sandbox | Container | Sandboxed Python interpreter |
| Interaction | Interactive: many commands, files, and processes over one session | One script or command, then discarded | One orchestration program |
| State | Disk, memory, and processes can be saved, forked, and restored | None | None |
| Start | About 0.25 seconds | Seconds | Microseconds |
| Capabilities | Root in a full Linux VM: `apt`, `pip`, Docker, servers | Full Python and shell in a container image | Pure Python control flow that calls registered tasks |
| Best for | Coding agents, RL rollouts, live code execution in apps, per-user environments | One-shot jobs with known dependencies | LLM-generated orchestration code |

Use Sandbox VMs for:

- **Coding agents.** Give each agent task its own machine to write files, install packages, and run tests. Allow only the package hosts it needs. Discard the VM when the task ends.
- **Reinforcement learning rollouts.** Build an environment once, then start each rollout on its own copy-on-write fork of it, in parallel. See the [SWE-Gym rollouts tutorial](../../tutorials/reinforcement-learning/swe-gym-sandboxes/_index).
- **Code execution in live products.** Run user or model code inside a data analysis assistant or an in-app code runner, at interactive speed.
- **Long-lived workspaces.** Suspend an agent's sandbox while it waits on a person or a long tool call, and resume it with its processes intact.

## Requirements

- For microVMs, the default runtime: a Union.ai data plane with microVM support enabled. This needs special node configuration and setup. Talk to your Union.ai solutions team to enable it.
- For gVisor sandboxes: no special node resources. See [Choose a runtime](./runtimes).
- `flyteplugins-union` 0.23.0 or later, which needs `flyte` 2.13.4 or later and earlier than 2.15.0.
- Python 3.10 or later.

{{< subpage-cards >}}
