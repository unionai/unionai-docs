---
title: Overrides
weight: 15
variants: +flyte +union
---

# Overrides

Most task configuration is set when you define a task: on the `TaskEnvironment` or in the `@env.task` decorator.
But you often need to change some of that configuration for a **single invocation** of a task: give one call more memory, point it at a different secret, or bump its retries.

The `task.override()` method does exactly this.
It returns a **new task** with the specified parameters changed, leaving the original task definition untouched, so you can invoke the overridden task in place of the original:

```python
import flyte

env = flyte.TaskEnvironment(
    name="training",
    resources=flyte.Resources(cpu=1, memory="512Mi"),
)

@env.task
async def train(data: str) -> str:
    return f"trained on {data}"

@env.task
async def main() -> str:
    # Invoke train with its environment-level resources.
    baseline = await train("small.csv")

    # Invoke train with overridden resources for this call only.
    heavy = await train.override(
        resources=flyte.Resources(cpu="4", memory="24Gi"),
    )("large.csv")

    return heavy
```

The key idiom is `task.override(...)(args)`: `override()` returns a callable task, which you then invoke with the task's arguments. Note the two sets of parentheses.

## What you can override

`override()` accepts the parameters that are settable at the task-invocation level:

{{< variant flyte >}}
{{< markdown >}}
| Parameter | Details |
|-----------|---------|
| **short_name** | [Additional task settings](./additional-task-settings) |
| **resources** | [Resources](./resources) &bull; [`Resources` API ref](../../api-reference/flyte-sdk/packages/flyte/resources) |
| **cache** | [Caching](./caching) &bull; [`Cache` API ref](../../api-reference/flyte-sdk/packages/flyte/cache) |
| **retries** | [Retries and timeouts](./retries-and-timeouts) &bull; [`RetryStrategy` API ref](../../api-reference/flyte-sdk/packages/flyte/retrystrategy) |
| **timeout** | [Retries and timeouts](./retries-and-timeouts) &bull; [`Timeout` API ref](../../api-reference/flyte-sdk/packages/flyte/timeout) |
| **reusable** | [Reusable containers](./reusable-containers) &bull; [`ReusePolicy` API ref](../../api-reference/flyte-sdk/packages/flyte/reusepolicy) |
| **env_vars** | [Additional task settings](./additional-task-settings#environment-variables) |
| **secrets** | [Overriding secrets](#overriding-secrets) &bull; [Secrets](./secrets) &bull; [`Secret` API ref](../../api-reference/flyte-sdk/packages/flyte/secret) |
| **max_inline_io_bytes** | [Additional task settings](./additional-task-settings#inline-io-threshold) |
| **pod_template** | [Pod templates](./pod-templates) &bull; [`PodTemplate` API ref](../../api-reference/flyte-sdk/packages/flyte/podtemplate) |
| **interruptible** | [Interruptible tasks](./interruptible-tasks-and-queues) |
| **links** | [Additional task settings](./additional-task-settings#links) |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
| Parameter | Details |
|-----------|---------|
| **short_name** | [Additional task settings](./additional-task-settings) |
| **resources** | [Resources](./resources) &bull; [`Resources` API ref](../../api-reference/flyte-sdk/packages/flyte/resources) |
| **cache** | [Caching](./caching) &bull; [`Cache` API ref](../../api-reference/flyte-sdk/packages/flyte/cache) |
| **retries** | [Retries and timeouts](./retries-and-timeouts) &bull; [`RetryStrategy` API ref](../../api-reference/flyte-sdk/packages/flyte/retrystrategy) |
| **timeout** | [Retries and timeouts](./retries-and-timeouts) &bull; [`Timeout` API ref](../../api-reference/flyte-sdk/packages/flyte/timeout) |
| **reusable** | [Reusable containers](./reusable-containers) &bull; [`ReusePolicy` API ref](../../api-reference/flyte-sdk/packages/flyte/reusepolicy) |
| **env_vars** | [Additional task settings](./additional-task-settings#environment-variables) |
| **secrets** | [Overriding secrets](#overriding-secrets) &bull; [Secrets](./secrets) &bull; [`Secret` API ref](../../api-reference/flyte-sdk/packages/flyte/secret) |
| **max_inline_io_bytes** | [Additional task settings](./additional-task-settings#inline-io-threshold) |
| **pod_template** | [Pod templates](./pod-templates) &bull; [`PodTemplate` API ref](../../api-reference/flyte-sdk/packages/flyte/podtemplate) |
| **queue** | [Queues](./queues) |
| **interruptible** | [Interruptible tasks](./interruptible-tasks-and-queues) |
| **links** | [Additional task settings](./additional-task-settings#links) |
{{< /markdown >}}
{{< /variant >}}

For the full parameter interaction matrix showing which parameters can be set at which level, see [Task configuration levels](_index#task-configuration-levels).

> [!NOTE] Overrides replace, they don't merge
> When you override a collection-valued parameter such as `resources`, `env_vars`, or `secrets`, the value you pass **replaces** the environment's value for that invocation. It is not merged with it.
> To keep some of the original entries, include them in the override.

## What you cannot override

`name`, `image`, `docs`, and the task's interface (its input and output types) **cannot** be overridden. Attempting to override them raises an error.
To run a task with a different image, define it in a separate `TaskEnvironment` (see [Container images](./container-images) and [Multiple environments](./multiple-environments)).

## Overriding when a task is reusable

When a task uses a [reusable container](./reusable-containers) (`reusable` is set), its `resources`, `env_vars`, and `secrets` come from the parent environment and **cannot** be overridden while reuse is active. The container is already running.

To override any of these on a reusable task, turn reuse off in the same `override()` call by passing `reusable="off"`:

```python
result = await my_task.override(
    reusable="off",
    resources=flyte.Resources(cpu="4", memory="8Gi"),
)(data)
```

## Overriding secrets

Just as you can override resources per invocation, you can override the [secrets](./secrets) injected into a task for a single call.
This is useful when the same task needs different credentials depending on how it's invoked: for example, calling an external API with a different key per tenant, or supplying a secret that the task's environment doesn't declare.

Pass `secrets` to `override()` exactly as you would to the `TaskEnvironment`: a secret key, a `Secret` object, or a list of either.

```python
import flyte
from flyte import Secret

env = flyte.TaskEnvironment(
    name="model_calls",
    secrets=Secret("openai-key", as_env_var="LLM_API_KEY"),
)

@env.task
async def call_model(prompt: str) -> str:
    import os
    api_key = os.environ["LLM_API_KEY"]
    ...  # call the model using api_key
    return "response"

@env.task
async def main() -> str:
    # Use the environment's default secret.
    default = await call_model("hello")

    # Override the secret for this invocation, mounting a different
    # store key into the same LLM_API_KEY environment variable.
    alternate = await call_model.override(
        secrets=Secret("anthropic-key", as_env_var="LLM_API_KEY"),
    )("hello")

    return alternate
```

> [!NOTE]
> If the task's environment uses **reusable containers** (`reusable` is set), overriding `secrets`, like `resources` and `env_vars`, requires passing `reusable="off"` in the **same** `override()` call. Otherwise the override is rejected.

As with the environment-level `secrets` parameter, the secret is injected at runtime and accessed inside the task: typically as an environment variable via `os.environ` (or mounted as a file).
See [Secrets](./secrets) for how to create secrets and how they are injected, and remember that the overriding `secrets` value **replaces** the environment's secrets for that invocation rather than adding to them.

> [!NOTE]
> A task can only access a secret if the secret's scope includes the project and domain where the task's `TaskEnvironment` is deployed. Overriding the secret at invocation time does not change this.

> [!WARNING]
> Do not return secret values from tasks. Returned values are stored in plaintext in your data plane's object store and shown in the UI and to downstream tasks, defeating the secret store's protections.
