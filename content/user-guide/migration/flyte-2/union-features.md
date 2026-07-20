---
title: Union features
weight: 12
variants: -flyte +union
---

# Migrating Union-specific features

A couple of constructs that were specific to Union in Flyte 1 — **Actors** and **Apps** — have direct equivalents in Flyte 2. Apps, in particular, are now part of the open-source Flyte SDK rather than a Union-only add-on. See [Migration](./migration) for the overall approach.

## Actors → reusable containers

Flyte 1 **Actors** kept a pool of warm containers alive so that many short tasks could skip the cold-start cost and share in-memory state. In Flyte 2 this is **reusable containers**: instead of a separate `ActorEnvironment`, you add a `flyte.ReusePolicy` to an ordinary `TaskEnvironment`, and its tasks are plain `@env.task`s.

{{< tabs "migration-actors" >}}
{{< tab "Flyte 1 (Actors)" >}}
{{< markdown >}}
```python
import union

actor = union.ActorEnvironment(
    name="my-actor",
    replica_count=2,
    ttl_seconds=300,
    requests=union.Resources(cpu="1", mem="1Gi"),
)


@actor.task
def compute(x: int) -> int:
    return x * x
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2 (reusable containers)" >}}
{{< markdown >}}
```python
from datetime import timedelta

import flyte

# The reusable-container runtime library must be in the task image.
image = flyte.Image.from_debian_base().with_pip_packages("unionai-reuse>=0.1.10")

env = flyte.TaskEnvironment(
    name="my-reusable-env",
    image=image,
    resources=flyte.Resources(cpu="1", memory="1Gi"),
    reusable=flyte.ReusePolicy(
        replicas=2,                          # pool size (was replica_count)
        concurrency=1,                       # tasks per container (new)
        scaledown_ttl=timedelta(minutes=5),  # idle single-container shutdown
        idle_ttl=timedelta(minutes=30),      # idle whole-pool shutdown
    ),
)


@env.task
async def compute(x: int) -> int:
    return x * x
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

| Flyte 1 `ActorEnvironment` | Flyte 2 `ReusePolicy` | Notes |
|---|---|---|
| `replica_count` | `replicas` | Pool size |
| `ttl_seconds` | `scaledown_ttl` / `idle_ttl` | Split into per-container and whole-pool timeouts |
| `requests` | `TaskEnvironment(resources=...)` | Resources move to the environment |
| N/A | `concurrency` | New: async tasks per container (total capacity is `replicas × concurrency`) |
| `@actor.task` | `@env.task` | A regular task |

Reusable containers require the [`unionai-reuse`](https://pypi.org/project/unionai-reuse/) package in the task image and, as in Flyte 1, run on a Union backend. See [Reusable containers](../../task-configuration/reusable-containers) for the full parameter reference and capacity math.

## Apps → the Flyte SDK

Flyte 1 **Apps** (`union.app.App`) were a Union-only way to serve long-running web apps and model endpoints. In Flyte 2 the same capability is built into the open-source **Flyte SDK** as `flyte.app.AppEnvironment`, deployed with `flyte.serve` (development) or `flyte.deploy` (production).

{{< tabs "migration-apps" >}}
{{< tab "Flyte 1 (union.app)" >}}
{{< markdown >}}
```python
from union import ImageSpec, Resources
from union.app import App

app = App(
    name="my-app",
    container_image=ImageSpec(name="my-app", packages=["fastapi", "union-runtime"]),
    limits=Resources(cpu="1", mem="1Gi"),
    port=8080,
    include=["./main.py"],
    args="fastapi run --port 8080",
    requires_auth=False,
)
```

Deploy with the `union deploy apps` CLI.
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2 (flyte.app)" >}}
{{< markdown >}}
```python
import flyte
import flyte.app

app_env = flyte.app.AppEnvironment(
    name="my-app",
    image=flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn"),
    args=["fastapi", "run", "--port", "8080"],
    port=8080,
    resources=flyte.Resources(cpu="1", memory="1Gi"),
    requires_auth=False,
)

if __name__ == "__main__":
    flyte.init_from_config()
    app = flyte.serve(app_env)   # or flyte.deploy(app_env) for production
    print(app.url)
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Because apps are now part of the OSS SDK, the same `flyte.app` API covers dashboards (Streamlit, Gradio), REST and webhook backends (FastAPI, Flask), and model serving. For LLM serving specifically, use the `flyteplugins-vllm` or SGLang integrations. See:

- [Configure apps](../../configure-apps/_index) — the `AppEnvironment` configuration reference
- [Build apps](../../build-apps/_index) and [Serve and deploy apps](../../serve-and-deploy-apps/_index)
- [Native app integrations](../../native-app-integrations/_index) — Streamlit, FastAPI, vLLM, SGLang

## Next

- [New in Flyte 2](./new-in-flyte-2) — real-time serving, batch inference, and sandboxing
- [Considerations](./considerations) — caveats of the new execution model
