---
title: Configure tasks
weight: 1
variants: +flyte +byoc +selfmanaged
sidebar_expanded: false
llm_readable_bundle: true
---

# Configure tasks

{{< llm-bundle-note >}}

As we saw in [**Quickstart**](../getting-started/quickstart), you can run any Python function as a task in Flyte just by decorating it with `@env.task`.

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

### Parameter interaction

Here is an overview of all task configuration parameters available at each level and how they interact:

| Parameter               | `TaskEnvironment`  | `@env.task` decorator      | `override` on task invocation |
|-------------------------|--------------------|----------------------------|-------------------------------|
| [**name**](./additional-task-settings)                           | ✅ Yes (required)  | ❌ No                      | ❌ No                         |
| [**short_name**](./additional-task-settings)                     | ❌ No              | ✅ Yes                     | ✅ Yes                        |
| [**image**](./container-images)                                  | ✅ Yes             | ❌ No                      | ❌ No                         |
| [**resources**](./resources)                                     | ✅ Yes             | ❌ No                      | ✅ Yes (if not `reusable`)    |
| [**env_vars**](./additional-task-settings#environment-variables) | ✅ Yes             | ❌ No                      | ✅ Yes (if not `reusable`)    |
| [**secrets**](./secrets)                                         | ✅ Yes             | ❌ No                      | ✅ Yes (if not `reusable`)    |
| [**cache**](./caching)                                           | ✅ Yes             | ✅ Yes                     | ✅ Yes                        |
| [**pod_template**](./pod-templates)                              | ✅ Yes             | ✅ Yes                     | ✅ Yes                        |
| [**reusable**](./reusable-containers)                            | ✅ Yes             | ❌ No                      | ✅ Yes                        |
| [**depends_on**](./multiple-environments)                        | ✅ Yes             | ❌ No                      | ❌ No                         |
| [**description**](./additional-task-settings)                    | ✅ Yes             | ❌ No                      | ❌ No                         |
| [**plugin_config**](./task-plugins)                              | ✅ Yes             | ❌ No                      | ❌ No                         |
| [**report**](./additional-task-settings#report)                  | ❌ No              | ✅ Yes                     | ❌ No                         |
| [**max_inline_io_bytes**](./additional-task-settings#inline-io-threshold) | ❌ No    | ✅ Yes                     | ✅ Yes                        |
| [**retries**](./retries-and-timeouts)                            | ❌ No              | ✅ Yes                     | ✅ Yes                        |
| [**timeout**](./retries-and-timeouts)                            | ❌ No              | ✅ Yes                     | ✅ Yes                        |
| [**triggers**](./triggers)                                       | ❌ No              | ✅ Yes                     | ❌ No                         |
| [**links**](./additional-task-settings#links)                    | ❌ No              | ✅ Yes                     | ✅ Yes                        |
| [**interruptible**](./interruptible-tasks-and-queues)            | ✅ Yes             | ✅ Yes                     | ✅ Yes                        |
| [**queue**](./interruptible-tasks-and-queues)                    | ✅ Yes             | ✅ Yes                     | ✅ Yes                        |
| [**docs**](./additional-task-settings#docs)                      | ❌ No              | ✅ Yes                     | ❌ No                         |

## Task configuration parameters

Each parameter is documented in detail on its dedicated page or in the API reference. For full type signatures and constraints, see the [`TaskEnvironment` API reference](../../api-reference/flyte-sdk/packages/flyte/taskenvironment).

| Parameter | Details |
|-----------|---------|
| **name**, **short_name**, **description**, **docs** | [Additional task settings](./additional-task-settings) |
| **image** | [Container images](./container-images) &bull; [`Image` API ref](../../api-reference/flyte-sdk/packages/flyte/image) |
| **resources** | [Resources](./resources) &bull; [`Resources` API ref](../../api-reference/flyte-sdk/packages/flyte/resources) |
| **env_vars** | [Additional task settings](./additional-task-settings#environment-variables) |
| **secrets** | [Secrets](./secrets) &bull; [`Secret` API ref](../../api-reference/flyte-sdk/packages/flyte/secret) |
| **cache** | [Caching](./caching) &bull; [`Cache` API ref](../../api-reference/flyte-sdk/packages/flyte/cache) |
| **pod_template** | [Pod templates](./pod-templates) &bull; [`PodTemplate` API ref](../../api-reference/flyte-sdk/packages/flyte/podtemplate) |
| **reusable** | [Reusable containers](./reusable-containers) &bull; [`ReusePolicy` API ref](../../api-reference/flyte-sdk/packages/flyte/reusepolicy) |
| **depends_on** | [Multiple environments](./multiple-environments) |
| **plugin_config** | [Task plugins](./task-plugins) |
| **report** | [Additional task settings](./additional-task-settings#report) |
| **max_inline_io_bytes** | [Additional task settings](./additional-task-settings#inline-io-threshold) |
| **retries**, **timeout** | [Retries and timeouts](./retries-and-timeouts) &bull; [`RetryStrategy`](../../api-reference/flyte-sdk/packages/flyte/retrystrategy), [`Timeout`](../../api-reference/flyte-sdk/packages/flyte/timeout) API refs |
| **triggers** | [Triggers](./triggers) &bull; [`Trigger` API ref](../../api-reference/flyte-sdk/packages/flyte/trigger) |
| **links** | [Additional task settings](./additional-task-settings#links) |
| **interruptible**, **queue** | [Interruptible tasks and queues](./interruptible-tasks-and-queues) |

