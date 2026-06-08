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

`unionai-sandbox` (`union.sandbox`) runs untrusted Python or shell commands in a live, multi-turn session. You open a sandbox, send it many commands, watch state evolve on its work dir, and close it when you're done.

```
session ┐
        │  work dir + venv persist across calls ────┐
        ├─ run("write data.json")        net: blocked     │
        ├─ run("uv pip install numpy")   net: allowlist   │
        ├─ put_bytes / get_bytes         (push/pull files)│
        ├─ run("load data, compute")     net: blocked     │
        └─ close                                          ┘
```

It's built for the workloads where a one-shot container falls apart: an agent that needs to iterate on its own code, a notebook-style app that runs a sequence of related commands, a tool that compiles, executes, then inspects the result. State persists between calls, output streams as it arrives, and the security posture (network and filesystem) is set per call, not baked in at construction time.

## What you get

- **Built for agents and multi-turn apps.** Untrusted code (LLM-generated, third-party, multi-tenant) gets a real interactive session, not a fresh container per turn. The work dir and the session venv are still there on the next `run()`.
- **Like a long-lived machine.** The session keeps one venv on its work dir, so installing is just a `run()`: `run("uv pip install X")` persists, and a later `run("import X", script_type="python")` sees it — install once, import anywhere. The work dir is the persistent disk; `/tmp` is reset per command.
- **Explicit isolation, no silent downgrade.** You pick the backend per session (`bubblewrap`, user namespaces) — there's no auto-detection and no fallback to weaker isolation. You opt into [gVisor](https://gvisor.dev/), dedicated pods, and stricter capability drops only when the threat model calls for it.
- **Per-call security knobs.** Flip `network_mode` between `blocked`, `allowlist`, and `open` on each `run()`. The same session can execute a network-isolated tool call, then do an allow-listed `uv pip install`, then drop back to blocked, without tearing anything down.
- **First-class integration.** A remote sandbox is a regular Flyte task: observable in the Union console, governed by the same RBAC and project/domain scoping, serializable across task boundaries, recoverable independently of the caller. (On-device sessions skip the extra pod entirely and aren't serializable; pick remote when you need those properties.)
- **Embeddable.** One pip install, one `async with`, drops into any async Python. The on-device transport has no daemon and no Docker requirement; the remote transport adds a one-time per-cluster deploy.

The library exposes one `Session` API over two transports: in-process (`union.sandbox.on_device`) for sandboxing inside the current container or task pod, and a remote `sandbox-server` pod for everything else. The call sites are nearly identical; the choice is documented in [Deployment](./deployment).

## Quickstart

```sh
pip install unionai-sandbox
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

> [!IMPORTANT] Backends are explicit
> There's no auto-detection: you pass `backend="userns"`, `backend="bubblewrap"`, etc., and an unavailable backend fails loudly rather than downgrading to weaker isolation. `userns` runs in a vanilla pod; `bubblewrap` (the strongest, and the default) needs `CAP_SYS_ADMIN` + an unconfined AppArmor profile. See [Security model](./security-model).

> [!IMPORTANT] On-device is for development, remote is for production
> `sb.on_device.session()` shares a container with the calling code, which makes it ideal for laptop, CI, and install-check use, but it doesn't isolate the sandboxed process from your task's secrets and credentials. For production use cases (agent loops, multi-turn apps, anything running untrusted code in a real workload), use `sb.session()`, which runs in its own pod. See [Security model](./security-model) for the why, and [Deployment](./deployment) for the deploy step.

> [!NOTE]
> Examples on this page use bare `asyncio.run(main())` to keep the code short. In a Union codebase you'll typically open the session inside a `@env.task` instead. Examples on [Deployment](./deployment) show that shape.

### A more involved example

This is the shape interactive sessions are good at: the session is a small machine you keep around — write a file in one call, install a package in the next, and use both in a third. State persists across calls and the security posture changes per call. Shown with `sb.on_device.session()` for brevity; the same code is the body of a `@env.task` that opens `sb.session()` in production.

```python
import asyncio
from union import sandbox as sb

COMPUTE = """
import json, statistics
import requests  # proves the install from step 2 is visible
data = json.loads(open("data.json").read())
print(f"requests={requests.__version__} mean={statistics.mean(data)}")
"""

async def main():
    # Session-level network_mode sets the *ceiling* of what any run() can
    # reach. Per-call run(network_mode="blocked") narrows from there.
    async with sb.on_device.session(
        backend="userns",
        network_mode="allowlist",
        network_allowlist=sb.PYPI_HOSTS,
    ) as sbx:
        # 1. Write a file to the work dir (the persistent disk). Tighten to
        #    blocked for the untrusted step. cwd defaults to the work dir.
        proc = await sbx.run(
            'import json; open("data.json", "w").write(json.dumps([1, 2, 3, 4]))',
            script_type="python", stdout=True, stderr=True,
            network_mode="blocked",
        )
        _, err = await proc.communicate_text()
        assert proc.returncode == 0, err

        # 2. Install a package — just a run(). It lands in the session venv and
        #    persists. Uses the session default (allow-list to PyPI).
        proc = await sbx.run("uv pip install requests", stdout=True, stderr=True)
        _, err = await proc.communicate_text()
        assert proc.returncode == 0, err

        # 3. Back to blocked. Use the file from step 1 and the package from step 2.
        proc = await sbx.run(
            COMPUTE, script_type="python", stdout=True, stderr=True,
            network_mode="blocked",
        )
        out, err = await proc.communicate_text()
        assert proc.returncode == 0, err
        print(out.strip())  # e.g. "requests=2.32.3 mean=2.5"

asyncio.run(main())
```

The same code runs against a remote sandbox by swapping `sb.on_device.session(...)` for `await sb.session(...)`. The remote transport needs the deploy extra and a one-time per-cluster deploy:

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

- [Security model](./security-model). Isolation backends (bubblewrap, user namespaces, sandbox-exec, gVisor), explicit backend selection, blast radius for on-device vs remote, and which posture to pick for which trust level.
- [Running commands](./running-commands). The `run()` call, output handling, script types, the persistent venv, timeouts, and the error model.
- [Networking](./networking). Per-call `network_mode`, what the allow-list does and does not protect against.
- [Filesystem](./filesystem). The persistent work dir, `put_bytes` and `get_bytes`, the default allow-list, and how to extend it.
- [Deployment](./deployment). When to pick on-device vs remote, pod security for on-device backends, `unionai-sandbox-deploy`, `SandboxEnvironment`, custom images and resources, ownership and reference mode, and detached-lifetime sessions.
