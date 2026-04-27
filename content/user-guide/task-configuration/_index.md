---
title: Configure tasks
weight: 10
variants: +flyte +union
llm_readable_bundle: true
---

# Configure tasks

{{< llm-bundle-note >}}

As we saw in [**Quickstart**](../quickstart), you can run any Python function as a task in Flyte just by decorating it with `@env.task`.

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
In this section we will explore the various configuration options available for tasks in Flyte.

## Task configuration levels

Task configuration is done at three levels. From most general to most specific, they are:

* The `TaskEnvironment` level: setting parameters when defining the `TaskEnvironment` object.
* The `@env.task` decorator level: Setting parameters in the `@env.task` decorator when defining a task function.
* The task invocation level: Using the `task.override()` method when invoking task execution.

Each level has its own set of parameters, and some parameters are shared across levels.
For shared parameters, the more specific level will override the more general one.

### Example

Here is an example of how these levels work together, showing each level with all available parameters:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/task_config.py" fragment="config-levels" lang="python" >}}

## Task configuration parameters

Each parameter is documented in detail on its dedicated page in this section.
For the complete parameter interaction matrix showing which parameters can be set at which level, and for full type signatures and constraints, see the [`TaskEnvironment` API reference](../../api-reference/flyte-sdk/packages/flyte/taskenvironment).

| Parameter | Set at | Details |
|-----------|--------|---------|
| **name** | `TaskEnvironment` only | [Additional task settings](./additional-task-settings) &bull; [`TaskEnvironment` API ref](../../api-reference/flyte-sdk/packages/flyte/taskenvironment) |
| **image** | `TaskEnvironment` only | [Container images](./container-images) &bull; [`Image` API ref](../../api-reference/flyte-sdk/packages/flyte/image) |
| **depends_on** | `TaskEnvironment` only | [Multiple environments](./multiple-environments) |
| **description** | `TaskEnvironment` only | [Additional task settings](./additional-task-settings) |
| **plugin_config** | `TaskEnvironment` only | [Task plugins](./task-plugins) |
| **resources** | `TaskEnvironment`, `override`\* | [Resources](./resources) &bull; [`Resources` API ref](../../api-reference/flyte-sdk/packages/flyte/resources) |
| **env_vars** | `TaskEnvironment`, `override`\* | [Additional task settings](./additional-task-settings#environment-variables) |
| **secrets** | `TaskEnvironment`, `override`\* | [Secrets](./secrets) &bull; [`Secret` API ref](../../api-reference/flyte-sdk/packages/flyte/secret) |
| **cache** | All three levels | [Caching](./caching) &bull; [`Cache` API ref](../../api-reference/flyte-sdk/packages/flyte/cache) |
| **pod_template** | All three levels | [Pod templates](./pod-templates) &bull; [`PodTemplate` API ref](../../api-reference/flyte-sdk/packages/flyte/podtemplate) |
| **reusable** | `TaskEnvironment`, `override` | [Reusable containers](./reusable-containers) &bull; [`ReusePolicy` API ref](../../api-reference/flyte-sdk/packages/flyte/reusepolicy) |
| **interruptible** | All three levels | [Interruptible tasks and queues](./interruptible-tasks-and-queues) |
| **queue** | All three levels | [Interruptible tasks and queues](./interruptible-tasks-and-queues) |
| **short_name** | `@env.task`, `override` | [Additional task settings](./additional-task-settings) |
| **retries** | `@env.task`, `override` | [Retries and timeouts](./retries-and-timeouts) &bull; [`RetryStrategy` API ref](../../api-reference/flyte-sdk/packages/flyte/retrystrategy) |
| **timeout** | `@env.task`, `override` | [Retries and timeouts](./retries-and-timeouts) &bull; [`Timeout` API ref](../../api-reference/flyte-sdk/packages/flyte/timeout) |
| **max_inline_io_bytes** | `@env.task`, `override` | [Additional task settings](./additional-task-settings#inline-io-threshold) |
| **links** | `@env.task`, `override` | [Additional task settings](./additional-task-settings#links) |
| **report** | `@env.task` only | [Additional task settings](./additional-task-settings#report) |
| **triggers** | `@env.task` only | [Triggers](./triggers) &bull; [`Trigger` API ref](../../api-reference/flyte-sdk/packages/flyte/trigger) |
| **docs** | `@env.task` only | [Additional task settings](./additional-task-settings#docs) |

\*When `reusable` is set, `resources`, `env_vars`, and `secrets` can only be overridden via `task.override()` with `reusable="off"` in the same call.

