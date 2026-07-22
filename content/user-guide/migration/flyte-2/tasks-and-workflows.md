---
title: Tasks and workflows
weight: 4
variants: +flyte +union
---

# Tasks and workflows

The biggest structural change in Flyte 2 is that **everything is a task**. The `@task`, `@workflow`, and `@dynamic` decorators all collapse into a single `@env.task` on a `flyte.TaskEnvironment`, and a "workflow" is just a task that calls other tasks. This page covers the basic structure; see [Task configuration](./configuration) for the environment settings and [Migration](./overview) for the big picture.

## Hello world: tasks and workflows

A `@task` plus `@workflow` becomes two `@env.task`s, where the entrypoint task calls the others. Sequential calls are naturally ordered; no `>>` operator required.

{{< tabs "migration-hello-world" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/hello_world_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/hello_world_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Chaining and ordering

In Flyte 1 you sometimes used `>>` to force ordering between tasks with no data dependency. In Flyte 2, sequential (synchronous) calls run in the order they're written, and `await`ing async tasks in sequence does the same. The `>>` operator is gone.

{{< tabs "migration-chained" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/chained_tasks_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/chained_tasks_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Subworkflows

A `@workflow` invoked by another `@workflow` (for example, a reusable preprocessing pipeline) becomes a task that calls other tasks; nest them as deeply as you like.

{{< tabs "migration-subworkflow" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/subworkflow_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/subworkflow_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## TaskEnvironment configuration

The `TaskEnvironment` holds the configuration that Flyte 1 spread across the `@task` decorator. The task decorator can still override a few settings per-task.

```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",                           # Required: unique name
    image=flyte.Image.from_debian_base(),    # Or a string, or "auto"
    resources=flyte.Resources(
        cpu="2",
        memory="4Gi",
        gpu="A100:1",
        disk="10Gi",
    ),
    env_vars={"LOG_LEVEL": "INFO"},
    secrets=[flyte.Secret(key="api-key", as_env_var="API_KEY")],
    cache="auto",                            # "auto", "override", "disable", or a Cache object
    reusable=flyte.ReusePolicy(replicas=5, idle_ttl=60),
    interruptible=True,
)

# The task decorator can override some settings:
@env.task(
    short_name="my_task",   # Display name
    cache="disable",        # Override cache
    retries=3,              # Retry count
    timeout=3600,           # Seconds or a timedelta
    report=True,            # Generate an HTML report
)
def my_task(x: int) -> int:
    return x
```

## Parameter mapping: `@task` → `TaskEnvironment` + `@env.task`

| Flyte 1 `@task` parameter | Flyte 2 location | Notes |
|---|---|---|
| `container_image` | `TaskEnvironment(image=...)` | Env-level only |
| `requests` | `TaskEnvironment(resources=...)` | Env-level only |
| `limits` | `TaskEnvironment(resources=...)` | Combined with requests (single value) |
| `environment` | `TaskEnvironment(env_vars=...)` | Env-level only |
| `secret_requests` | `TaskEnvironment(secrets=...)` | Env-level only |
| `cache` | Both | Can override at task level |
| `cache_version` | `flyte.Cache(version_override=...)` | In a `Cache` object |
| `retries` | `@env.task(retries=...)` | Task-level only |
| `timeout` | `@env.task(timeout=...)` | Task-level only |
| `interruptible` | Both | Can override at task level |
| `pod_template` | Both | Can override at task level |
| `deprecated` | N/A | Not in Flyte 2 |
| `docs` | `@env.task(docs=...)` | Task-level only |

For image, resource, secret, and caching detail, see [Task configuration](./configuration).

## Next

- [Task configuration](./configuration): image, resources, caching, secrets, and scheduling
- [Control flow](./control-flow): conditionals, dynamic behavior, and error handling
- [Parallelism and fan-out](./parallelism): running tasks in parallel
