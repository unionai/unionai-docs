---
title: Agents
weight: 8
variants: -flyte +union
---

# Agents

Interactive sandboxes are built for agent loops: an LLM (or agent framework) writes code, runs it, reads the result, and iterates — all against one live session whose filesystem and installed packages persist between turns. This page covers the patterns that matter when an agent generates code on the fly, whether that code is trusted (authored against your own prompts and tools) or untrusted (derived from end-user input).

## Why a session, not a container per turn

A one-shot container starts cold every turn: nothing the previous step wrote is there, nothing it installed is there. An agent that iterates on its own code wants the opposite: the file it wrote last turn, the package it installed two turns ago, and the ability to flip network access per step. A session gives it that:

- State persists: Files under the session work dir and packages in the shared session venv survive across `run()` calls (the writable scratch mounts like `/tmp` are fresh per command). So "write a script, run it, fix it, run it again" works without re-staging anything. See [Running commands](./running-commands#installing-packages-install-is-just-a-run).
- Security posture is per call: Flip `network_mode` between `blocked`, `allowlist`, and `open` on each `run()`. A turn that just executes the agent's code runs `blocked`; a turn that needs a package installs under `allowlist`; nothing is torn down in between. See [Networking](./networking).

## The shape of an agent loop

A typical loop stages inputs, lets the agent's tool loop write and execute code inside the sandbox, then collects the result:

```python
import os, tempfile
from union import sandbox as sb

async def run_agent(env_key: str) -> bytes:
    with tempfile.TemporaryDirectory() as work:
        async with sb.on_device.session(
            host_work_dir=work,                       # pin so we can interpolate paths
            network_mode="allowlist",
            network_allowlist=["api.anthropic.com"],  # the model endpoint
            backend="userns",
            timeout_s=1200,
        ) as sbx:
            # 1. Stage inputs into the work dir.
            await sbx.put_bytes(f"{work}/data.csv", _CSV)
            await sbx.put_bytes(f"{work}/driver.py", _driver(work).encode())

            # 2. Run the agent's driver. Its tool loop writes Python, executes
            #    it in the sandbox, and iterates until it writes answer.json.
            proc = await sbx.run(
                f"python {work}/driver.py",
                env={"ANTHROPIC_API_KEY": env_key},   # see the secret note below
                stdout=True, stderr=True, timeout_s=600,
            )
            out, err = await proc.communicate_text()
            assert proc.returncode == 0, f"agent failed rc={proc.returncode}\n{err}"

            # 3. Collect the result.
            return await sbx.get_bytes(f"{work}/answer.json")
```

`put_bytes` / `get_bytes` move data across the boundary without shelling out; pinning `host_work_dir` lets you interpolate a known path into both the driver script and the prompt. See [Filesystem](./filesystem).

## A failing command is signal, not an error

The single most important distinction for an agent loop: a non-zero exit of the sandboxed code is not an exception. When the agent writes code that raises, asserts or exits non-zero, `run()` still returns normally and you branch on `proc.returncode`. That's the feedback the agent learns from.

```python
proc = await sbx.run("python attempt.py", stdout=True, stderr=True)
out, err = await proc.communicate_text()
if proc.returncode != 0:
    feedback = err          # hand this back to the agent and let it retry
```

`communicate()` / `wait()` raise `SandboxExecutionError` only when the process never reached a real exit, e.g. a server-side spawn failure or a stream that died mid-flight. That means the sandbox itself misbehaved, which is a different category from "the agent's code failed its assertions" and usually warrants aborting the loop rather than retrying. (The one-shot `run_code()` and `exec(check=True)` helpers raise `SandboxCommandError` on a non-zero exit instead; use plain `run()` when you want the exit code as data.) See [Running commands](./running-commands#errors-vs-non-zero-exits).

## Match the isolation to the trust level

Pick the isolation by what the agent actually runs, not by the fact that it's an agent. For most agent workloads the process-level default is the right choice, and you only escalate when the inputs are genuinely hostile:

- **Trusted control flow** — the prompts, tools, and any generated code are authored or vetted by you and not exposed to end users or external input. The default backend (bubblewrap / userns) is the intended choice here: fast, cheap, and sufficient. Run on-device while developing; move to a remote session for production to get the pod boundary, observability, and an independent lifecycle.
- **Untrusted or multi-tenant** — the agent runs code derived from end-user input, or several tenants share the system. Use a remote session with `network_mode="blocked"`, stage inputs via `put_bytes`, and harden the pod with gVisor.

See [Security model](./security-model) for the full decision.

## Secrets forwarded into the sandbox

Agents that call a model need a credential, and the natural move is to forward it with `run(env=...)`. One thing to keep in mind: the sandboxed process can read its own environment, and the network allow-list — a proxy that only cooperating clients honour — won't stop code that opens a raw socket from sending the key out. So a forwarded key should be treated as readable by the sandboxed code:

- Use a **scoped, short-lived, low-limit** credential.
- Forward it explicitly per run (`run(env={...})`) rather than relying on env inheritance. A remote sandbox-server does not inherit the caller pod's full env anyway.

To keep the credential out of the sandbox entirely, call the model from the parent task and pass only prompts and results across the boundary with `put_bytes` / `get_bytes` — then the agent's code never holds the key. This is the right pattern when the generated code is untrusted; for trusted agents, forwarding a scoped key is a reasonable, deliberate trade-off.

## Related

- [Running commands](./running-commands). The error model, `exec()` / `run_code()`, and the shared-venv install model the loop relies on.
- [Networking](./networking). Per-call network flips and what the allow-list does and does not protect against.
- [Filesystem](./filesystem). `put_bytes` / `get_bytes` for staging inputs and collecting results.
- [Security model](./security-model). Choosing a posture by trust level, and when gVisor is worth it.
