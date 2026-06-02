---
title: Remote sandboxes
weight: 4
variants: -flyte +union
---

# Remote sandboxes

A remote sandbox launches a long-lived `sandbox-server` **pod** as a Flyte task and connects to it over Connect-RPC. The session is a serializable dataclass, so it can be passed between tasks, and the pod has an independent lifecycle that outlives the caller. Remote sandboxes require Union.

The session implements the shared [`Session` API](./sessions) — `run()`, output helpers, byte transfer, and network policy are identical to the [local transport](./local-sandboxes).

## Deploy the sandbox task

Deploy the default sandbox task environments once per cluster:

```sh
flyte deploy --all python/union/sandbox/task/_server.py
```

After that, `sb.session(...)` resolves the deployed task by name and launches a fresh pod per session.

> [!NOTE] Networking
> The remote transport reaches the pod through a dataproxy. The default URL can be overridden with the `UNION_SANDBOX_DATAPROXY_URL` environment variable.

## Open a session

```python
from datetime import timedelta
from union import sandbox as sb

async with await sb.session(timeout=timedelta(minutes=30)) as sbx:
    proc = await sbx.run("uname -a", stdout=True)
    out, _ = await proc.communicate_text()
    print(sbx.name, sbx.ip, sbx.created_at)
```

Bringup is split into two phases so your setup work overlaps with pod startup: `sb.session(...)` submits the run and returns instantly, `async with` (or `await sbx`) waits for the pod to become addressable, and the transport health-check is deferred to the first `run()`.

A `SandboxSession` exposes this metadata:

| Field | Meaning |
|---|---|
| `name` | Session name (equals the Flyte run name). |
| `endpoint` | URL the transport opens against. |
| `ip` | Pod IP, once surfaced. |
| `created_at` | UTC construction timestamp. |
| `is_owner` | `True` on the side that created the run (and can abort it). |
| `url` | Union console URL for the run (owner side). |

## Sandbox environments

`sb.session()` launches `sb.DEFAULT_SANDBOX_ENV` (userns isolation, container runtime) unless you pass your own `SandboxEnvironment`. Define one to control the image, resources, secrets, and isolation:

```python
import flyte
from union import sandbox as sb

my_sandbox = sb.SandboxEnvironment(
    name="ml-sandbox",
    image=sb.base_sandbox_image.with_pip_packages("torch", "transformers"),
    resources=flyte.Resources(cpu="8", memory="32Gi", gpu="L4:1"),
    secrets=[flyte.Secret(group="hf", key="HF_TOKEN")],
    env_vars={"HF_HOME": "/tmp/hf"},
    sandbox_mode="userns",        # "userns" | "bwrap"
    runtime="container",          # "container" | "gvisor"
    description="ML inference sandbox",
)

# Deploy once, then launch a session against it:
async with await sb.session(environment=my_sandbox, resources=flyte.Resources(cpu="4")) as sbx:
    proc = await sbx.run("python3 -c 'import torch; print(torch.__version__)'", stdout=True)
    out, _ = await proc.communicate_text()
```

| Parameter | Notes |
|---|---|
| `name` | Task-environment identifier; `session()` resolves `{name}.sandbox_server`. |
| `image` | Defaults to `sb.base_sandbox_image`; extend it with `base_sandbox_image.with_pip_packages(...)` etc. |
| `resources` | Default per-session `flyte.Resources`. Override per launch with `sb.session(resources=...)`. |
| `secrets` | `flyte.Secret`s forwarded to the sandbox pod. |
| `env_vars` | Environment variables forwarded to the pod. |
| `sandbox_mode` | In-pod isolation backend: `"userns"` (default) or `"bwrap"`. |
| `runtime` | Pod runtime: `"container"` (default) or `"gvisor"`. |

Two ready-built defaults are exported: `sb.DEFAULT_SANDBOX_ENV` (userns, container runtime) and `sb.DEFAULT_SANDBOX_ENV_BWRAP` (bubblewrap, container runtime).

## gVisor isolation

`sandbox_mode` and `runtime` are **independent** knobs:

- `sandbox_mode` (`"userns"` / `"bwrap"`) selects the in-pod isolation backend that constrains the sandboxed process.
- `runtime` (`"container"` / `"gvisor"`) selects how the **pod itself** is run.

Setting `runtime="gvisor"` puts `runtimeClassName: gvisor` on the sandbox pod, so its syscalls are intercepted by the [gVisor](https://gvisor.dev/) application kernel rather than hitting the host kernel directly. This is stronger than the default `"container"` runtime and is the recommended posture for untrusted, multi-tenant code.

```python
hardened = sb.SandboxEnvironment(
    name="hardened-sandbox",
    runtime="gvisor",
)
```

> [!NOTE] gVisor must be enabled on the cluster
> `runtime="gvisor"` requires the `gvisor` RuntimeClass to be installed and enabled in your cluster. In most cases, **talk to your Union solutions engineer** to enable gVisor for your deployment. gVisor applies to remote sandboxes only — a [local sandbox](./local-sandboxes) picks its backend on the host it already runs in.

## Passing a sandbox between tasks

Because a `SandboxSession` is serializable, the task that launches the sandbox can pass it to other tasks. The launcher is the **owner**; a task that receives the session lands in **reference mode**.

```python
import asyncio
from datetime import timedelta
from union import sandbox as sb

@env.task
async def child(sbx: sb.SandboxSession, script: str) -> dict:
    # Reference mode: no `async with` needed. The endpoint round-tripped via
    # serialization, and the first run() lazily opens the transport.
    proc = await sbx.run(script, stdout=True)
    out, _ = await proc.communicate_text()
    return {"script": script, "stdout": out, "returncode": proc.returncode}

@env.task
async def parent() -> list[dict]:
    # Owner mode: we launched the pod, so we own its lifetime and abort it on exit.
    async with await sb.session(timeout=timedelta(minutes=15)) as sbx:
        return await asyncio.gather(
            child(sbx, "echo one"),
            child(sbx, "echo two"),
        )
```

Only the **owner** can abort the run. Calling `close()` on a reference-mode session shuts that receiver's transport only — the run keeps going until the owner aborts it (or the session times out).

## Detached lifetime

A remote `SandboxSession` does not require `async with`. Keep the handle and manage the lifetime yourself — useful for apps and services where the sandbox outlives a single block of code:

```python
from datetime import timedelta
from union import sandbox as sb

sbx = await sb.session(timeout=timedelta(minutes=30))
await sbx                       # wait for the pod to surface — fail fast on a bad launch
try:
    proc = await sbx.run("uname -a", stdout=True)
    out, _ = await proc.communicate_text()
finally:
    await sbx.close()           # closes the transport and aborts the run (owner side)
```

To attach to a `sandbox-server` you started elsewhere, use `sb.remote.session(endpoint=...)`.
