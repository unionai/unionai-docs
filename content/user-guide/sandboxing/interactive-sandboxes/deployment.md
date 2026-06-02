---
title: Deployment
weight: 6
variants: -flyte +union
---

# Deployment

`unionai-sandbox` ships two transports with identical `Session` APIs. This page covers how to install and deploy each, when to use which, and how to customise the remote-pod environment.

## Pick a transport

The two transports cover different stages of a sandbox workflow:

- **Local** (`sb.local.session(...)`): development, CI, and install checks. Runs sandboxed child processes inside the current container. Needs no Union connection, no pod, no deploy. Lowest latency. Not for production: it shares a container with your task's code and credentials. See [Security model](./security-model) for the blast-radius argument.
- **Remote** (`sb.session(...)`): production. Runs the sandbox in its own Flyte-task pod with a minimal image, its own service account, and an independent lifecycle. Serializable across task boundaries, observable in the UI, optionally hardened with gVisor.

In other words: develop locally, ship remote. The call sites are nearly identical (`sb.local.session(...)` vs `await sb.session(...)`), so promoting a working local prototype to production is a one-token change plus a one-time deploy.

## Local: install and go

```sh
pip install unionai-sandbox
```

That's it. `sb.local.session(...)` works inside any async Python: a notebook, a script on your laptop, a CI runner, a Flyte task you're iterating on before shipping. The library auto-detects the strongest available backend (`bubblewrap` → `userns` → `sandbox-exec` → `none`) and reports it on each process as `proc.backend`.

### Running a local script

If the script calls `asyncio.run(main())` at module scope, run it directly:

```sh
python my_agent.py
```

If the code is wrapped in a `flyte.TaskEnvironment` + `@env.task` (which is the recommended shape inside a Union codebase), the same file still runs as a plain script. Flyte's local executor picks up the `@env.task` and runs it in-process:

```sh
python my_agent.py
```

No Union cluster needed, no `flyte run` invocation. The local sandbox spawns inside whatever container or virtualenv you launched `python` in.

## Remote: one-time deploy, then per-run sessions

Install the deploy extra:

```sh
pip install 'unionai-sandbox[deploy]'
```

Deploy the default sandbox task envs once per cluster:

```sh
union-sandbox-deploy
```

This runs `flyte deploy --all` against the installed `_server.py`. Project and domain come from your Flyte config (`~/.flyte/config.yaml`) or environment variables (`FLYTE_PROJECT`, `FLYTE_DOMAIN`):

```sh
FLYTE_PROJECT=my-project FLYTE_DOMAIN=development union-sandbox-deploy
```

After deploy, open sessions from any task. The caller task's image must have `unionai-sandbox` installed.

```python
import flyte
from datetime import timedelta
from union import sandbox as sb

env = flyte.TaskEnvironment(
    name="agent",
    image=flyte.Image.from_debian_base(platform=("linux/amd64",)).with_pip_packages(
        "unionai-sandbox[remote]"
    ),
)

@env.task
async def main() -> str:
    async with await sb.session(timeout=timedelta(minutes=30)) as sbx:
        proc = await sbx.run("uname -a", stdout=True)
        out, _ = await proc.communicate_text()
        print(sbx.name, sbx.ip, sbx.created_at, sbx.url)
        return out
```

> [!IMPORTANT] Caller image must install `unionai-sandbox`
> Pin the image platform to the cluster's architecture (`linux/amd64` for most Union clusters) and pip-install `unionai-sandbox[remote]` so the Connect-RPC transport is available. Without an explicit pin, a wheel built for your laptop can end up inside a Linux pod and fail to load with an `invalid ELF header` error.

Bringup is split into two phases so your setup work overlaps with pod startup: `sb.session(...)` submits the run and returns instantly; `async with` (or `await sbx`) waits for the pod to become addressable; the transport health-check is deferred to the first `run()`.

### Running a remote script

A script that opens `sb.session(...)` is invoked through the Flyte CLI, which dispatches the calling task to the cluster. The sandbox pod then comes up alongside it:

```sh
flyte run my_agent.py main
```

To target a specific project and domain:

```sh
flyte run --project my-project --domain development my_agent.py main
```

`my_agent.py` here is the file containing your `@env.task async def main(...)` definition; `main` is the task name. The `sb.session(...)` call inside `main` submits the deployed sandbox task as its own run.

For local iteration against a remote sandbox (the caller task runs on your laptop, the sandbox pod lives on the cluster), use `--local`:

```sh
flyte run --local my_agent.py main
```

A `SandboxSession` exposes this metadata:

| Field        | Meaning                                                     |
| ------------ | ----------------------------------------------------------- |
| `name`       | Session name (equals the Flyte run name).                   |
| `endpoint`   | URL the transport opens against.                            |
| `ip`         | Pod IP, once surfaced.                                      |
| `created_at` | UTC construction timestamp.                                 |
| `is_owner`   | `True` on the side that created the run (and can abort it). |
| `url`        | Union console URL for the run (owner side).                 |

`sb.session()` arguments worth knowing:

| Argument                         | Default               | What it does                                                                                                  |
| -------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------- |
| `environment`                    | `DEFAULT_SANDBOX_ENV` | The `SandboxEnvironment` to launch. See below.                                                                |
| `name`                           | random `sbx-<16hex>`  | Run name. Set to make the run discoverable in the UI.                                                         |
| `timeout`                        | `timedelta(hours=1)`  | Soft per-session timeout. Hard ceiling of 24h is baked into the task decorator as a safety net.               |
| `project`, `domain`              | inherited             | Where to launch the sandbox run.                                                                              |
| `resources`                      | env's default         | Per-launch override. Rewrites the deployed task's resources and resizes the in-pod sandbox cgroup ceiling.    |
| `network_mode`, `network_allowlist` | `"blocked"`, `None`   | Session default for every `run()`. On remote this also sets the pod-level network posture, so the per-call proxy can dial out. Per-call `run(network_mode=...)` still overrides for that one call. |

## Defining a custom `SandboxEnvironment`

`sb.session()` launches `sb.DEFAULT_SANDBOX_ENV` unless you pass your own. Define one to control the image, resources, secrets, and isolation.

The deploy CLI (`flyte deploy --all <file>`) discovers task envs by scanning a Python file for module-level objects. So a custom environment lives in two parts: the `SandboxEnvironment` itself, and a thin deploy module that exposes its `task_env` at module scope.

`my_sandboxes.py`: define the environment:

```python
import flyte
from union import sandbox as sb

ml_sandbox = sb.SandboxEnvironment(
    name="ml-sandbox",
    image=sb.base_sandbox_image.with_pip_packages("torch", "transformers"),
    resources=flyte.Resources(cpu="8", memory="32Gi", gpu="L4:1"),
    secrets=[flyte.Secret(group="hf", key="HF_TOKEN")],
    env_vars={"HF_HOME": "/tmp/hf"},
    sandbox_mode="userns",        # "userns" | "bwrap"
    runtime="container",          # "container" | "gvisor"
    description="ML inference sandbox",
)
```

`deploy_my_sandboxes.py`: the deploy entrypoint. Re-export the `task_env` at module scope so the deploy CLI can find it:

```python
from my_sandboxes import ml_sandbox

# Module-scope name; flyte deploy discovers this via isinstance(v, flyte.Environment).
ml_sandbox_env = ml_sandbox.task_env
```

Deploy once:

```sh
flyte deploy --all deploy_my_sandboxes.py
```

Then launch sessions against it from any task:

```python
import flyte
from union import sandbox as sb
from my_sandboxes import ml_sandbox

env = flyte.TaskEnvironment(
    name="agent",
    image=flyte.Image.from_debian_base(platform=("linux/amd64",)).with_pip_packages(
        "unionai-sandbox[remote]"
    ),
)

@env.task
async def run_inference() -> str:
    async with await sb.session(environment=ml_sandbox) as sbx:
        proc = await sbx.run(
            "python3 -c 'import torch; print(torch.__version__)'",
            stdout=True,
        )
        out, _ = await proc.communicate_text()
        return out
```

The built-in `union-sandbox-deploy` is exactly this pattern applied to the library's own defaults; your custom envs follow the same recipe.

| Parameter      | Notes                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------- |
| `name`         | Task-environment identifier; `session()` resolves `{name}.sandbox_server`.                   |
| `image`        | Defaults to `sb.base_sandbox_image`; extend with `.with_pip_packages(...)` etc.              |
| `resources`    | Default per-session `flyte.Resources`. Override per launch with `sb.session(resources=...)`. |
| `secrets`      | `flyte.Secret`s forwarded to the sandbox pod.                                                |
| `env_vars`     | Environment variables forwarded to the pod.                                                  |
| `sandbox_mode` | In-pod isolation backend: `"userns"` (default) or `"bwrap"`.                                 |
| `runtime`      | Pod runtime: `"container"` (default) or `"gvisor"`.                                          |

Two ready-built defaults are exported: `sb.DEFAULT_SANDBOX_ENV` (userns, container runtime) and `sb.DEFAULT_SANDBOX_ENV_BWRAP` (bubblewrap, container runtime).

## Passing a sandbox between tasks

A `SandboxSession` is serializable, so the task that launches the sandbox can pass it to other tasks. The launcher is the **owner**; a receiver lands in **reference mode**.

```python
import asyncio
from datetime import timedelta
from union import sandbox as sb

@env.task
async def child(sbx: sb.SandboxSession, script: str) -> dict:
    # Reference mode: no `async with` needed. Endpoint round-tripped via
    # serialization; first run() lazily opens the transport.
    proc = await sbx.run(script, stdout=True)
    out, _ = await proc.communicate_text()
    return {"script": script, "stdout": out, "returncode": proc.returncode}

@env.task
async def parent() -> list[dict]:
    # Owner mode: we launched the pod, so we own its lifetime and abort on exit.
    async with await sb.session(timeout=timedelta(minutes=15)) as sbx:
        return await asyncio.gather(
            child(sbx, "echo one"),
            child(sbx, "echo two"),
        )
```

Only the **owner** can abort the run. Calling `close()` on a reference-mode session shuts that receiver's transport only; the run keeps going until the owner aborts it (or the session times out).

## Detached lifetime

A remote `SandboxSession` doesn't require `async with`. Keep the handle and manage the lifetime yourself, useful for apps and services where the sandbox outlives a single block of code:

```python
import flyte
from datetime import timedelta
from union import sandbox as sb

env = flyte.TaskEnvironment(
    name="long-running-service",
    image=flyte.Image.from_debian_base(platform=("linux/amd64",)).with_pip_packages(
        "unionai-sandbox[remote]"
    ),
)

@env.task
async def serve_user_session(user_id: str) -> str:
    sbx = await sb.session(timeout=timedelta(minutes=30))
    await sbx                       # wait for the pod to surface, fail fast on a bad launch
    try:
        proc = await sbx.run("uname -a", stdout=True)
        out, _ = await proc.communicate_text()
        return out
    finally:
        await sbx.close()           # closes the transport and aborts the run (owner side)
```

The same pattern works outside a task for local development. To attach to a `sandbox-server` you started yourself, use `sb.remote.session(endpoint=...)` instead of `sb.session()`.

## Per-session timeout vs hard ceiling

Two timeouts protect a sandbox pod from leaking forever:

- **Per-session soft timeout** (default 1 hour, settable via `sb.session(timeout=...)`). Enforced inside the task body. On expiry, the body signals the sandbox binary (SIGTERM, then SIGKILL after 10s) and exits cleanly.
- **Hard ceiling** (24 hours, baked into the task decorator). The Flyte runtime kills the action after this. If a session owner crashes without calling `close()` and the soft timeout doesn't fire, the action still terminates within 24h.

Design your soft timeouts to be well below the hard ceiling. The ceiling is a safety net, not a parameter.

## Related

- [Security model](./security-model). When to pick local vs remote, when to enable gVisor.
- [Networking](./networking). Per-call `network_mode` and what the allow-list does and does not protect against.
- [Filesystem](./filesystem). `read_only_paths` and `read_write_paths` extensions, volumes roadmap.
