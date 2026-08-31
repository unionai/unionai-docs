---
title: Configure tasks
description: Define `TaskEnvironment`s for container images, resources, secrets, caching, retries, and more; use triggers for schedules.
icon: gear
weight: 1
variants: +flyte +union
---

# Configure tasks

As we saw in [**Quickstart**](../../get-started/quickstart), you can run any Python function as a task in Flyte just by decorating it with `@env.task`.

This allows you to run your Python code in a distributed manner, with each function running in its own container.
Flyte manages the spinning up of the containers, the execution of the code, and the passing of data between the tasks.

The simplest possible case is a `TaskEnvironment` with only a `name` parameter, and an `env.task` decorator, with no parameters:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/task_config.py" fragment="simple" lang="python" >}}

> [!NOTE]
> Notice how the `TaskEnvironment` is assigned to the variable `env` and then that variable is
> used in the `@env.task`. This is what connects the `TaskEnvironment` to the task definition.
>
> In the following we will often use `@env.task` generically to refer to the decorator,
> but it is important to remember that it is actually a decorator attached to a specific
> `TaskEnvironment` object, and the `env` part can be any variable name you like.

This will run your task in the default container environment with default settings.

But, of course, one of the key advantages of Flyte is the ability to control the software environment, hardware environment, and other execution parameters for each task, right in your Python code.

## Task configuration levels

Task configuration is done at three levels. From most general to most specific, they are:

* The `TaskEnvironment` level: setting parameters when defining the `TaskEnvironment` object.
* The `@env.task` decorator level: Setting parameters in the `@env.task` decorator when defining a task function.
* The task invocation level: Using the [`task.override()`](./overrides) method when invoking task execution.

Each level has its own set of parameters, and some parameters are shared across levels.
For shared parameters, the more specific level will override the more general one.

### Example

Here is an example of how these levels work together, showing each level with all available parameters:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/task_config.py" fragment="config-levels" lang="python" >}}

## Task configuration parameters

Each parameter is documented in detail on its dedicated page in this section.
For the complete parameter interaction matrix showing which parameters can be set at which level, and for full type signatures and constraints, see the [`TaskEnvironment` API reference](../../../api-reference/flyte-sdk/flyte/taskenvironment).

{{< variant flyte >}}
{{< markdown >}}

| Parameter | Set at | Details |
|-----------|--------|---------|
| **name** | `TaskEnvironment` only | [Additional task settings](./additional-task-settings) &bull; [`TaskEnvironment` API ref](../../../api-reference/flyte-sdk/flyte/taskenvironment) |
| **image** | `TaskEnvironment` only | [Container images](./container-images) &bull; [`Image` API ref](../../../api-reference/flyte-sdk/flyte/image) |
| **depends_on** | `TaskEnvironment` only | [Multiple environments](./multiple-environments) |
| **description** | `TaskEnvironment` only | [Additional task settings](./additional-task-settings) |
| **plugin_config** | `TaskEnvironment` only | [Task plugins](./task-plugins) |
| **resources** | `TaskEnvironment`, `override`\* | [Resources](./resources) &bull; [`Resources` API ref](../../../api-reference/flyte-sdk/flyte/resources) |
| **env_vars** | `TaskEnvironment`, `override`\* | [Additional task settings](./additional-task-settings#environment-variables) |
| **secrets** | `TaskEnvironment`, `override`\* | [Secrets](./secrets) &bull; [`Secret` API ref](../../../api-reference/flyte-sdk/flyte/secret) |
| **cache** | All three levels | [Caching](./caching) &bull; [`Cache` API ref](../../../api-reference/flyte-sdk/flyte/cache) |
| **pod_template** | All three levels | [Pod templates](./pod-templates) &bull; [`PodTemplate` API ref](../../../api-reference/flyte-sdk/flyte/podtemplate) |
| **reusable** | `TaskEnvironment`, `override` | [Reusable containers](./reusable-containers) &bull; [`ReusePolicy` API ref](../../../api-reference/flyte-sdk/flyte/reusepolicy) |
| **interruptible** | All three levels | [Interruptible tasks](./interruptible-tasks-and-queues) |
| **short_name** | `@env.task`, `override` | [Additional task settings](./additional-task-settings) |
| **retries** | `@env.task`, `override` | [Retries and timeouts](./retries-and-timeouts) &bull; [`RetryStrategy` API ref](../../../api-reference/flyte-sdk/flyte/retrystrategy) |
| **timeout** | `@env.task`, `override` | [Retries and timeouts](./retries-and-timeouts) &bull; [`Timeout` API ref](../../../api-reference/flyte-sdk/flyte/timeout) |
| **max_inline_io_bytes** | `@env.task`, `override` | [Additional task settings](./additional-task-settings#inline-io-threshold) |
| **links** | `@env.task`, `override` | [Additional task settings](./additional-task-settings#links) |
| **report** | `@env.task` only | [Additional task settings](./additional-task-settings#report) |
| **triggers** | `@env.task` only | [Triggers](./triggers) &bull; [`Trigger` API ref](../../../api-reference/flyte-sdk/flyte/trigger) |
| **docs** | `@env.task` only | [Additional task settings](./additional-task-settings#docs) |

{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}

| Parameter | Set at | Details |
|-----------|--------|---------|
| **name** | `TaskEnvironment` only | [Additional task settings](./additional-task-settings) &bull; [`TaskEnvironment` API ref](../../../api-reference/flyte-sdk/flyte/taskenvironment) |
| **image** | `TaskEnvironment` only | [Container images](./container-images) &bull; [`Image` API ref](../../../api-reference/flyte-sdk/flyte/image) |
| **depends_on** | `TaskEnvironment` only | [Multiple environments](./multiple-environments) |
| **description** | `TaskEnvironment` only | [Additional task settings](./additional-task-settings) |
| **plugin_config** | `TaskEnvironment` only | [Task plugins](./task-plugins) |
| **resources** | `TaskEnvironment`, `override`\* | [Resources](./resources) &bull; [`Resources` API ref](../../../api-reference/flyte-sdk/flyte/resources) |
| **env_vars** | `TaskEnvironment`, `override`\* | [Additional task settings](./additional-task-settings#environment-variables) |
| **secrets** | `TaskEnvironment`, `override`\* | [Secrets](./secrets) &bull; [`Secret` API ref](../../../api-reference/flyte-sdk/flyte/secret) |
| **cache** | All three levels | [Caching](./caching) &bull; [`Cache` API ref](../../../api-reference/flyte-sdk/flyte/cache) |
| **pod_template** | All three levels | [Pod templates](./pod-templates) &bull; [`PodTemplate` API ref](../../../api-reference/flyte-sdk/flyte/podtemplate) |
| **reusable** | `TaskEnvironment`, `override` | [Reusable containers](./reusable-containers) &bull; [`ReusePolicy` API ref](../../../api-reference/flyte-sdk/flyte/reusepolicy) |
| **interruptible** | All three levels | [Interruptible tasks](./interruptible-tasks-and-queues) |
| **queue** | All three levels | [Queues](./queues) |
| **short_name** | `@env.task`, `override` | [Additional task settings](./additional-task-settings) |
| **retries** | `@env.task`, `override` | [Retries and timeouts](./retries-and-timeouts) &bull; [`RetryStrategy` API ref](../../../api-reference/flyte-sdk/flyte/retrystrategy) |
| **timeout** | `@env.task`, `override` | [Retries and timeouts](./retries-and-timeouts) &bull; [`Timeout` API ref](../../../api-reference/flyte-sdk/flyte/timeout) |
| **max_inline_io_bytes** | `@env.task`, `override` | [Additional task settings](./additional-task-settings#inline-io-threshold) |
| **links** | `@env.task`, `override` | [Additional task settings](./additional-task-settings#links) |
| **report** | `@env.task` only | [Additional task settings](./additional-task-settings#report) |
| **triggers** | `@env.task` only | [Triggers](./triggers) &bull; [`Trigger` API ref](../../../api-reference/flyte-sdk/flyte/trigger) |
| **docs** | `@env.task` only | [Additional task settings](./additional-task-settings#docs) |

{{< /markdown >}}
{{< /variant >}}

\*When `reusable` is set, `resources`, `env_vars`, and `secrets` can only be overridden via `task.override()` with `reusable="off"` in the same call.

## Distributed tasks with a clustered environment

Everything above configures a task that runs in a single container. Some tasks instead need a *gang*
of pods working together as one distributed job — the classic case being multi-node, multi-GPU model
training. For those, use a specialized `flyte.clustered.ClusteredTaskEnvironment` instead of a plain
`TaskEnvironment`. It inherits all the configuration above and adds a few fields that describe the
cluster shape: `replicas` (pods) and `nproc_per_node` (worker processes per pod). When you run the
task, the backend launches a Kubernetes JobSet of identical pods, sets up a `torchrun` rendezvous
across them, and runs your task body once per worker.

```python
import flyte
from flyte.clustered import ClusteredTaskEnvironment, TorchRun

env = ClusteredTaskEnvironment(
    name="ddp_env",
    image=flyte.Image.from_debian_base().with_pip_packages("torch"),
    resources=flyte.Resources(cpu=(2, 4), memory=("4Gi", "8Gi"), gpu="L4:1"),
    replicas=2,            # number of pods (nodes)
    nproc_per_node=1,      # worker processes per pod => world_size = 2 x 1
    runtime=TorchRun(),
)
```

See [Clustered task environment](./clustered-task-environment) for the full guide, including DDP,
FSDP, and framework-integration examples.
