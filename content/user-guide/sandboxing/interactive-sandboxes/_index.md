---
title: Interactive sandboxes
weight: 5
variants: -flyte +union
llm_readable_bundle: true
---

# Interactive sandboxes

{{< llm-bundle-note >}}

> [!NOTE]
> Interactive sandboxes are in Beta. APIs may change between releases. Reach out on Slack with feedback or feature requests.

`unionai-sandbox` (`union.sandbox`) runs untrusted Python or shell commands in a live, multi-turn session. You open a sandbox, send it many commands, watch state evolve on its filesystem, and close it when you're done.

```
session ┐
        │  filesystem state persists across calls ─┐
        ├─ run("write data.json")        net: blocked     │
        ├─ run("pip install numpy")      net: allowlist   │
        ├─ put_bytes / get_bytes         (push/pull files)│
        ├─ run("load data, compute")     net: blocked     │
        └─ close                                          ┘
```

It's built for the workloads where a one-shot container falls apart: an agent that needs to iterate on its own code, a notebook-style app that runs a sequence of related commands, a tool that compiles, executes, then inspects the result. State persists between calls, output streams as it arrives, and the security posture (network and filesystem) is set per call, not baked in at construction time.

## What you get

- **Built for agents and multi-turn apps.** Untrusted code (LLM-generated, third-party, multi-tenant) gets a real interactive session, not a fresh container per turn. Earlier output and on-disk artifacts are still there on the next `run()`.
- **Lightweight by default, hardened when you need to.** The defaults use `bubblewrap` or kernel user namespaces, which start in milliseconds and add negligible overhead. You opt into [gVisor](https://gvisor.dev/), dedicated pods, and stricter capability drops only when the threat model calls for it. The library makes picking the right mechanism easy.
- **Per-call security knobs.** Flip `network_mode` between `blocked`, `allowlist`, and `open` on each `run()`. The same session can execute a network-isolated tool call, then do an allow-listed `pip install`, then drop back to blocked, without tearing anything down.
- **First-class integration.** A remote sandbox is a regular Flyte task: observable in the Union console, governed by the same RBAC and project/domain scoping, serializable across task boundaries, recoverable independently of the caller. (Local sessions skip the pod entirely and aren't serializable; pick remote when you need those properties.)
- **Embeddable.** One pip install, one `async with`, drops into any async Python. The local transport has no daemon and no Docker requirement; the remote transport adds a one-time per-cluster deploy.

The library exposes one `Session` API over two transports: in-process (`union.sandbox.local`) for sandboxing inside the current container, and a remote `sandbox-server` pod for everything else. The call sites are identical; the choice is documented in [Deployment](./deployment).

## Quickstart

```sh
pip install 'unionai-sandbox[flyte]'
```

```python
import asyncio
from union import sandbox as sb

async def main():
    async with sb.on_device.session(backend="userns") as sbx:
        proc = await sbx.run("uname -a", stdout=True)
        out, _ = await proc.communicate_text()
        print(out)

asyncio.run(main())
```

That runs `uname -a` inside a sandboxed child process with no network and a restricted filesystem view. If that prints, your install works.

> [!NOTE] Pick the backend explicitly
> The on-device backend defaults to `"bubblewrap"`, which needs `CAP_SYS_ADMIN` + unconfined AppArmor on the pod. On a vanilla pod or a dev laptop, pass `backend="userns"` (as above) since it needs no extra capabilities. There's no auto-detection: an unavailable backend fails loudly rather than downgrading. See [Security model](./security-model#isolation-backends).

> [!IMPORTANT] On-device is for development, remote is for production
> `sb.on_device.session()` shares a container with the calling code, which makes it ideal for laptop, CI and install-check use, but it doesn't isolate the sandboxed process from your task's secrets and credentials. For production use cases (agent loops, multi-turn apps, anything running untrusted code in a real workload), use `sb.session()`, which runs in its own pod. See [Security model](./security-model) for the why and [Deployment](./deployment) for the deploy step.

> [!NOTE]
> Examples on this page use bare `asyncio.run(main())` to keep the code short. In a Union codebase you'll typically open the session inside a `@env.task` instead. Examples on [Deployment](./deployment) show that shape.

### A more involved example

This is the shape interactive sessions are good at: state persists across calls, the security posture changes per call, and a follow-up step uses what an earlier one produced. Shown with `sb.on_device.session()` for brevity; the same code is the body of a `@env.task` that opens `sb.session()` in production.

State that persists across `run()` calls lives in two places: the session **work dir** (the data file below) and the shared **session venv** (the `requests` install below). Each `run()` is otherwise its own isolated process. The writable scratch mounts (`/tmp`, `/dev/shm`) are a fresh tmpfs every command, so anything written to bare `/tmp` is gone by the next call. That's why the example writes its data file under the pinned work dir, not `/tmp`.

```python
import asyncio
import tempfile
from union import sandbox as sb

async def main():
    with tempfile.TemporaryDirectory() as work:
        WRITE_DATA = f"""
import json, pathlib
pathlib.Path("{work}/data.json").write_text(json.dumps([1, 2, 3, 4]))
"""
        COMPUTE = f"""
import json, statistics, requests   # the install from step 2 is visible here
data = json.loads(open("{work}/data.json").read())
print(f"requests={{requests.__version__}} mean={{statistics.mean(data)}}")
"""
        # Session-level network_mode sets the ceiling of what any run() can
        # reach. Per-call run(network_mode="blocked") narrows from there.
        async with sb.on_device.session(
            backend="userns",
            host_work_dir=work,                 # pin the work dir so we can interpolate it
            network_mode="allowlist",
            network_allowlist=sb.PYPI_HOSTS,
        ) as sbx:
            # 1. Write a file to the work dir (persists). Tighten to blocked.
            await sbx.run(WRITE_DATA, script_type="python", network_mode="blocked")

            # 2. Install into the shared session venv (uses the allow-list default).
            await sbx.run("uv pip install requests")

            # 3. Back to blocked. Use the file from step 1 and the package from step 2.
            out = await sbx.run_code(COMPUTE, network_mode="blocked")
            print(out.strip())  # e.g. "requests=2.32.3 mean=2.5"

asyncio.run(main())
```

The same code runs against a remote sandbox by swapping `sb.on_device.session(...)` for `await sb.session()`. The remote transport needs the deploy extra and a one-time per-cluster deploy:

```sh
pip install 'unionai-sandbox[deploy]'
unionai-sandbox-deploy
```

After that, `await sb.session(...)` works from any task. See [Deployment](./deployment) for the full picture.

## Choosing a sandbox

`unionai-sandbox` is one of three sandboxing options Flyte and Union ship. Pick by the shape of the workload, not by isolation strength:

- **One-shot, typed I/O.** Use [`flyte.sandbox.create()`](../code-sandboxing). It builds an ephemeral container, runs one invocation with declared inputs and outputs, and discards it. Simpler when you don't need a live session.
- **Sandboxed orchestration.** Use [workflow sandboxing](../workflow-sandboxing-flyte) when the thing you need to sandbox is the control flow (LLM-generated orchestration code that dispatches to known tools).
- **Interactive sessions.** This library. Pick it when you need state to persist between commands, want to stream output, or want per-call network and filesystem control.

The [main sandboxing index](../_index) has a full decision matrix.

## What's on the rest of these pages

The transports share one API, so the docs are organized by concept. Each page covers both on-device and remote, and calls out where they differ.

- [Security model](./security-model). Isolation backends (bubblewrap, user namespaces, sandbox-exec, gVisor), the explicit-backend contract, blast radius for on-device vs remote, and which posture to pick for which trust level.
- [Running commands](./running-commands). The `run()` call, the `exec()` / `run_code()` one-shot helpers, the shared-venv install model, output handling, script types, timeouts, and the error model.
- [Networking](./networking). Per-call `network_mode`, the deny-list and `CLOUD_METADATA_DENY`, bring-your-own proxy, and what the allow-list does and does not protect against.
- [Filesystem](./filesystem). `put_bytes` and `get_bytes`, the default allow-list, and how to extend it.
- [Deployment](./deployment). When to pick on-device vs remote, `unionai-sandbox-deploy`, `SandboxEnvironment`, custom images and resources, ownership and reference mode, and detached-lifetime sessions.
- [GPU](./gpu). Running CUDA / PyTorch in a sandbox, why GPU requires the bubblewrap backend, and resource sizing.
- [Agents](./agents). The agent-loop pattern: persistent state, per-call network flips, treating non-zero exits as signal, and secret handling.
