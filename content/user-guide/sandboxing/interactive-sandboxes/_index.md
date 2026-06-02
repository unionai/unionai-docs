---
title: Interactive sandboxes
weight: 5
variants: -flyte +union
llm_readable_bundle: true
---

# Interactive sandboxes

{{< llm-bundle-note >}}

The `unionai-sandbox` library (`union.sandbox`) is a small, embeddable code-execution sandbox for running untrusted Python or shell commands in an **interactive session**: you open a sandbox once, send it many commands, and close it when you're done.

```
open → run() → run() → run() → … → close
```

Unlike [`flyte.sandbox.create()`](../code-sandboxing), which builds an ephemeral container, runs **one** typed-I/O invocation, and discards it, an interactive sandbox is a **live session**. State on the sandbox filesystem persists between calls, you stream stdout/stderr as it arrives, and you set the network and filesystem posture per call. This is the right tool for REPL-style agents, multi-turn apps, and any workflow that runs a sequence of related commands.

The library exposes **one session contract** over **two transports**:

| | **Local** (`union.sandbox.local`) | **Remote** (`union.sandbox`) |
|---|---|---|
| Where it runs | Sandboxed child processes **inside the current container**, via a Rust extension | A separate `sandbox-server` **pod**, launched as a Flyte task, reached over Connect-RPC |
| Isolation | Auto-detected on the host: `bubblewrap` → `userns` → `sandbox-exec` (macOS) → `none` | A whole pod per session; optional kernel-level **gVisor** runtime |
| Requires Union | No — works anywhere (laptop, CI, notebook) | Yes |
| Serializable | No (`LocalSession` cannot cross task boundaries) | Yes (`SandboxSession` can be passed between tasks) |
| Lifetime | Tied to the calling process | Independent — survives the caller, observable and recoverable |

Both transports implement the same `Session` API, so your `run()` / `put_bytes` / `get_bytes` code is identical regardless of which one you choose. See [Sandbox sessions](./sessions) for that shared API, and [Local sandboxes](./local-sandboxes) / [Remote sandboxes](./remote-sandboxes) for transport specifics.

## Install

```sh
pip install unionai-sandbox            # local transport only — no Flyte required
pip install unionai-sandbox[remote]    # add the remote (Connect-RPC) transport
pip install unionai-sandbox[deploy]    # add tooling to build/deploy custom sandbox environments
```

The import path is `union.sandbox`:

```python
from union import sandbox as sb
```

## Quickstart

### Local (in-process)

```python
import asyncio
import flyte
from union import sandbox as sb

async def main():
    async with sb.local.session(resources=flyte.Resources(cpu="500m", memory="512Mi")) as sbx:
        proc = await sbx.run("python3 -c 'print(2+2)'", stdout=True, timeout_s=10)
        out, _ = await proc.communicate_text()
        print(out)  # "4"

asyncio.run(main())
```

### Remote (sandbox-server pod)

Deploy the default sandbox task once per cluster (see [Remote sandboxes](./remote-sandboxes)):

```sh
flyte deploy --all python/union/sandbox/task/_server.py
```

Then open a session from any task:

```python
from datetime import timedelta
from union import sandbox as sb

async with await sb.session(timeout=timedelta(minutes=30)) as sbx:
    proc = await sbx.run("uname -a", stdout=True)
    out, _ = await proc.communicate_text()
    print(sbx.name, sbx.ip, sbx.created_at)
```

## Local vs remote: when to use which

A local sandbox is the default for isolating a single task's code execution. Reach for a remote sandbox when the sandbox's **lifetime, ownership, or isolation** needs to outlive or stand apart from the caller.

### Use a local sandbox when

- You need to isolate a single task's code execution — lowest latency, no extra pod, no orchestration.
- You're running **anywhere** Union isn't available — a laptop, CI, or a notebook. The local transport needs no deployment.
- The sandbox's lifetime equals the caller's and it never needs to be shared. `LocalSession` is **not serializable**, so it cannot cross task boundaries.

### Use a remote sandbox when

- **Apps and services** — a long-lived `SandboxSession` backing a serving app or UI (for example, one sandbox per user in a Streamlit app), driven across many turns.
- **Passing a sandbox between tasks** — the owner task launches one sandbox pod and passes the serializable `SandboxSession` to child tasks, which run against it in *reference mode*. This enables fan-out with `asyncio.gather`. Local sessions cannot do this.
- **Detached, recoverable lifetime** — the sandbox runs as its own Flyte-task pod with an independent lifecycle. It survives the caller, is observable in the Union console (`sbx.url`), can be explicitly owned and aborted, and is **not** torn down the instant the caller's container exits, the way a local sandbox is.
- **Stronger or multi-tenant isolation** — a separate pod per session, optionally hardened with the **gVisor** runtime (see [Remote sandboxes](./remote-sandboxes)).
- **Independent resources or image** — the sandbox pod gets its own resources and image (GPU, large dependencies) via `SandboxEnvironment`, decoupled from the caller task's environment.

### Security trade-off

The two transports differ in **blast radius** — what an escaping process can reach.

> [!WARNING] Local sandboxes share the caller's container
> A **local** sandbox runs *inside your task's own container*. The isolation backend (bubblewrap, userns, etc.) constrains the child process, but it shares the task pod's blast radius: a sandbox escape lands the code in the **same container as your task**, where it can reach the **task's own code, mounted secrets, and service-account / cloud credentials**. Local isolation is only as strong as the task pod around it — unless the **task itself** runs under gVisor, a breakout is contained only at the pod boundary.

A **remote** sandbox runs in a **separate pod** with its own (typically minimal) image, its own service account, and no access to the caller task's code or secrets — and can additionally be hardened with gVisor. The escape blast radius is the sandbox pod, not your workload.

**So:** for genuinely untrusted code (LLM-generated, third-party, or multi-tenant) where the caller task holds sensitive credentials or runs without gVisor, prefer a **remote** sandbox (optionally with gVisor). Use a **local** sandbox when the code is semi-trusted, the task pod is itself low-privilege or hardened, or latency and simplicity outweigh the stronger boundary.

## Learn more

- [Sandbox sessions](./sessions) — the transport-agnostic `Session` API: `run()`, output helpers, byte transfer, error model, and network policy.
- [Local sandboxes](./local-sandboxes) — in-process isolation backends and the filesystem allow-list.
- [Remote sandboxes](./remote-sandboxes) — deploying sandbox pods, `SandboxEnvironment`, gVisor, and passing sessions between tasks.
