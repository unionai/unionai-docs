---
title: Tasks and workflows
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Tasks and workflows

## Basic task migration

{{< tabs "migration-basic-task" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import task, Resources

@task(
    cache=True,
    cache_version="1.0",
    retries=3,
    timeout=3600,
    container_image="python:3.11",
    requests=Resources(cpu="1", mem="2Gi"),
    limits=Resources(cpu="2", mem="4Gi"),
)
def my_task(x: int) -> int:
    return x * 2
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    image="python:3.11",
    resources=flyte.Resources(cpu="1", memory="2Gi"),
    cache="auto",
)

@env.task(retries=3, timeout=3600)
def my_task(x: int) -> int:
    return x * 2
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Workflow to task migration

In Flyte 2 there is no `@workflow` decorator. Workflows are tasks that call other tasks.

{{< tabs "migration-workflow-to-task" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import task, workflow

@task
def step1(x: int) -> int:
    return x + 1

@task
def step2(y: int) -> int:
    return y * 2

@task
def step3(z: int) -> str:
    return f"Result: {z}"

@workflow
def my_workflow(x: int) -> str:
    a = step1(x=x)
    b = step2(y=a)
    c = step3(z=b)
    return c
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2 Sync" >}}
{{< markdown >}}
```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def step1(x: int) -> int:
    return x + 1

@env.task
def step2(y: int) -> int:
    return y * 2

@env.task
def step3(z: int) -> str:
    return f"Result: {z}"

@env.task
def main(x: int) -> str:
    a = step1(x)
    b = step2(a)
    c = step3(b)
    return c
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2 Async" >}}
{{< markdown >}}
```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def step1(x: int) -> int:
    return x + 1

@env.task
async def step2(y: int) -> int:
    return y * 2

@env.task
async def step3(z: int) -> str:
    return f"Result: {z}"

@env.task
async def main(x: int) -> str:
    a = await step1(x)
    b = await step2(a)
    c = await step3(b)
    return c
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

{{< note >}}
You can only `await` async tasks. If you try to `await` a sync task, it will fail. If your subtasks are sync, call them directly without `await` (they will execute synchronously/sequentially).
{{< /note >}}

## TaskEnvironment configuration

```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",                           # Required: unique name
    image=flyte.Image.from_debian_base(...), # Or string, or "auto"
    resources=flyte.Resources(
        cpu="2",
        memory="4Gi",
        gpu="A100:1",
        disk="10Gi",
        shm="auto",
    ),
    env_vars={"LOG_LEVEL": "INFO"},
    secrets=[
        flyte.Secret(key="api-key", as_env_var="API_KEY"),
    ],
    cache="auto",  # "auto", "override", "disable", or Cache object
    reusable=flyte.ReusePolicy(replicas=5, idle_ttl=60),
    queue="gpu-queue",
    interruptible=True,
)

# Task decorator can override some settings
@env.task(
    short_name="my_task",      # Display name
    cache="disable",           # Override cache
    retries=3,                 # Retry count
    timeout=3600,              # Seconds or timedelta
    report=True,               # Generate HTML report
)
def my_task(x: int) -> int:
    return x
```

## Parameter mapping: @task to TaskEnvironment + @env.task

| Flyte 1 `@task` parameter | Flyte 2 location | Notes |
|--------------------|-------------|-------|
| `container_image` | `TaskEnvironment(image=...)` | Env-level only |
| `requests` | `TaskEnvironment(resources=...)` | Env-level only |
| `limits` | `TaskEnvironment(resources=...)` | Combined with requests |
| `environment` | `TaskEnvironment(env_vars=...)` | Env-level only |
| `secret_requests` | `TaskEnvironment(secrets=...)` | Env-level only |
| `cache` | Both | Can override at task level |
| `cache_version` | `flyte.Cache(version_override=...)` | In Cache object |
| `retries` | `@env.task(retries=...)` | Task-level only |
| `timeout` | `@env.task(timeout=...)` | Task-level only |
| `interruptible` | Both | Can override at task level |
| `pod_template` | Both | Can override at task level |
| `deprecated` | N/A | Not in Flyte 2 |
| `docs` | `@env.task(docs=...)` | Task-level only |

For full details, see [Configure tasks](../../user-guide/task-configuration/_index).
