---
title: Configure tasks
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Configure tasks

As we saw in [**Quickstart**](../quickstart), you can run any Python function as a task in Flyte just by decorating it with `@env.task`.

This allows you to run your Python code in a distributed manner, with each function running in its own container.
Flyte manages the spinning up of the containers, the execution of the code, and the passing of data between the tasks.

The simplest possible case is a `TaskEnvironment` with only a `name` parameter, and an `env.task` decorator, with no parameters:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/task_config.py" fragment="simple" lang="python" >}}

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

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/task_config.py" fragment="config-levels" lang="python" >}}

### Parameter interaction

Here is an overview of all task configuration parameters available at each level and how they interact:

| Parameter               | `TaskEnvironment`  | `@env.task` decorator      | `override` on task invocation |
|-------------------------|--------------------|----------------------------|-------------------------------|
| **name**                | ✅ Yes (required)  | ❌ No                      | ❌ No                         |
| **short_name**          | ❌ No              | ✅ Yes                     | ✅ Yes                        |
| **image**               | ✅ Yes             | ❌ No                      | ❌ No                         |
| **resources**           | ✅ Yes             | ❌ No                      | ✅ Yes (if not `reusable`)    |
| **env_vars**            | ✅ Yes             | ❌ No                      | ✅ Yes (if not `reusable`)    |
| **secrets**             | ✅ Yes             | ❌ No                      | ✅ Yes (if not `reusable`)    |
| **cache**               | ✅ Yes             | ✅ Yes                     | ✅ Yes                        |
| **pod_template**        | ✅ Yes             | ✅ Yes                     | ✅ Yes                        |
| **reusable**            | ✅ Yes             | ❌ No                      | ✅ Yes                        |
| **depends_on**          | ✅ Yes             | ❌ No                      | ❌ No                         |
| **description**         | ✅ Yes             | ❌ No                      | ❌ No                         |
| **plugin_config**       | ✅ Yes             | ❌ No                      | ❌ No                         |
| **report**              | ❌ No              | ✅ Yes                     | ❌ No                         |
| **max_inline_io_bytes** | ❌ No              | ✅ Yes                     | ✅ Yes                        |
| **retries**             | ❌ No              | ✅ Yes                     | ✅ Yes                        |
| **timeout**             | ❌ No              | ✅ Yes                     | ✅ Yes                        |
| **triggers**            | ❌ No              | ✅ Yes                     | ❌ No                         |
| **interruptible**       | ✅ Yes             | ✅ Yes                     | ✅ Yes                        |
| **queue**               | ✅ Yes             | ✅ Yes                     | ✅ Yes                        |
| **docs**                | ❌ No              | ✅ Yes                     | ❌ No                         |

## Task configuration parameters

The full set of parameters available for configuring a task environment, task definition, and task invocation are:

### `name`

* Type: `str` (required)

* Defines the name of the `TaskEnvironment`.
  Since it specifies the name *of the environment*, it cannot, logically, be overridden at the `@env.task` decorator or the `task.override()` invocation level.

  It is used in conjunction with the name of each `@env.task` function to define the fully-qualified name of the task.
  The fully qualified name is always the `TaskEnvironment` name (the one above) followed by a period and then the task function name (the name of the Python function being decorated).
  For example:

  {{< code file="/external/unionai-examples/v2/user-guide/task-configuration/task_config.py" fragment="simple" lang="python" >}}

  Here, the name of the TaskEnvironment is `my_env` and the fully qualified name of the task is `my_env.my_task`.
  The `TaskEnvironment` name and fully qualified name of a task name are both fixed and cannot be overridden.

<!-- TODO: Add when available
* See [Names and descriptions](./names-and-descriptions).
-->

### `short_name`

* Type: `str` (required)

* Defines the short name of the task or action (the execution of a task).
  Since it specifies the name *of the task*, it is not, logically, available to be set at the ``TaskEnvironment` level.

  By default, the short name of a task is the name of the task function (the name of the Python function being decorated).
  The short name is used, for example, in parts of the UI.
  Overriding it does not change the fully qualified name of the task.

<!-- TODO: Add when available
* See [Names and descriptions](./names-and-descriptions).
-->

### `image`

* Type: `Union[str, Image, Literal['auto']]`

* Specifies the Docker image to use for the task container.
  Can be a URL reference to a Docker image, an [`Image` object](../../api-reference/flyte-sdk/packages/flyte/image), or the string `auto`.
  If set to `auto`, or if this parameter is not set, the [default image]() will be used.

* Only settable at the `TaskEnvironment` level.

* See [Container images](./container-images).

### `resources`

* Type: `Optional[Resources]`

* Specifies the compute resources, such as CPU and Memory, required by the task environment using a
  [`Resources`](../../api-reference/flyte-sdk/packages/flyte/resources) object.

* Can be set at the `TaskEnvironment` level and overridden at the `task.override()` invocation level
  (but only if `reuseable` is not in effect).

* See [Resources](./resources).

### `env_vars`

* Type: `Optional[Dict[str, str]]`

* A dictionary of environment variables to be made available in the task container.
  These variables can be used to configure the task at runtime, such as setting API keys or other configuration values.

<!-- TODO: Add when available
* See [Environment variables](./env-vars).
-->

### `secrets`

* Type: `Optional[SecretRequest]` where `SecretRequest` is an alias for `Union[str, Secret, List[str | Secret]]`

* The secrets to be made available in the task container.

* Can be set at the `TaskEnvironment` level and overridden at the `task.override()` invocation level, but only if `reuseable` is not in effect.

* See [Secrets](./secrets) and the API docs for the [`Secret` object](../../api-reference/flyte-sdk/packages/flyte/secret).

### `cache`

* Type: `Union[CacheRequest]` where `CacheRequest` is an alias for `Literal["auto", "override", "disable", "enabled"] | Cache`.

* Specifies the caching policy to be used for this task.

* Can be set at the `TaskEnvironment` level and overridden at the `@env.task` decorator level
  and at the `task.override()` invocation level.

* See [Caching](./caching).

### `pod_template`

* Type: `Optional[Union[str, kubernetes.client.V1PodTemplate]]`

* A pod template that defines the Kubernetes pod configuration for the task.
  A string reference to a named template or a `kubernetes.client.V1PodTemplate` object.

* Can be set at the `TaskEnvironment` level and overridden at the `@env.task` decorator level and the `task.override()` invocation level.

* See [Pod templates](./pod-templates).

### `reusable`

{{< variant flyte >}}
{{< markdown >}}

> [!NOTE]
> The `reusable` setting controls the [**reusable containers** feature](./reusable-containers).
> This feature is only available when running your Flyte code on a Union.ai backend.
> See [one of the Union.ai product variants of this page]({{< docs_home byoc v2 >}}/user-guide/reusable-containers) for details.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}

* Type: `ReusePolicy | None`

* A `ReusePolicy` that defines whether the task environment can be reused.
  If set, the task environment will be reused across multiple task invocations.

* When a `TaskEnvironment` has `reusable` set, then `resources`, `env_vars`, and `secrets` can only be overridden in `task.override()`
  if accompanied by an explicit `reusable="off"` in the same `task.override()` invocation.
  Additionally, `secrets` can only be overridden at the `@env.task` decorator level if the `TaskEnvironment` (`env`) does not have `reusable` set.

* See [Reusable containers](./reusable-containers) and the API docs for the [`ReusePolicy` object](../../api-reference/flyte-sdk/packages/flyte/reusepolicy).

{{< /markdown >}}
{{< /variant >}}

### `depends_on`

* Type: `List[Environment]`

* A list of [`Environment`](../../api-reference/flyte-sdk/packages/flyte/environment) objects that this `TaskEnvironment` depends on.
   When deploying this `TaskEnvironment`, the system will ensure that any dependencies of the listed `Environment`s are also available.
   This is useful when you have a set of task environments that depend on each other.

* Can only be set at the `TaskEnvironment` level, not at the `@env.task` decorator level or the `task.override()` invocation level.

* See [Multiple environments](./multiple-environments)

### `description`

* Type: `Optional[str]`

* A description of the task environment.
  This can be used to provide additional context about the task environment, such as its purpose or usage.

* Can only be set at the `TaskEnvironment` level, not at the `@env.task` decorator level
  or the `task.override()` invocation level.

<!--
* See [Names and descriptions](./names-and-descriptions).
-->

### `plugin_config`

* Type: `Optional[Any]`

* Additional configuration for plugins that can be used with the task environment.
  This can include settings for specific plugins that are used in the task environment.

* Can only be set at the `TaskEnvironment` level, not at the `@env.task` decorator level
  or the `task.override()` invocation level.

<!--
* See [Plugin configuration](./plugin-configuration).
-->

### `report`

* Type: `bool`

* Whether to generate the HTML report for the task.
  If set to `True`, the task will generate an HTML report that can be viewed in the Flyte UI.

* Can only be set at the `@env.task` decorator level,
  not at the `TaskEnvironment` level or the `task.override()` invocation level.

* See [Reports](../task-programming/reports).

<!--
* See [Configuring reports](../task-configuration/configuring-reports) and [Reports](../task-programming/reports).
-->

### `max_inline_io_bytes`

* Type: `int`

* Maximum allowed size (in bytes) for all inputs and outputs passed directly to the task
  (e.g., primitives, strings, dictionaries).
  Does not apply to [`flyte.io.File`, `flyte.io.Dir`](../task-programming/files-and-directories), or [`flyte.DataFrame`](../task-programming/dataclasses-and-structures) (since these are passed by reference).

* Can be set at the `@env.task` decorator level and overridden at the `task.override()` invocation level.
  If not set, the default value is `MAX_INLINE_IO_BYTES` (which is 100 MiB).

<!-- TODO: Add when available
* See [Maximum inline I/O](./maximum-inline-io).
-->

### `retries`

* Type: `Union[int, RetryStrategy]`

* The number of retries for the task, or a `RetryStrategy` object that defines the retry behavior.
  If set to `0`, no retries will be attempted.

* Can be set at the `@env.task` decorator level and overridden at the `task.override()` invocation level.

* See [Retries and timeouts](./retries-and-timeouts).

### `timeout`

* Type: `Union[timedelta, int]`

* The timeout for the task, either as a `timedelta` object or an integer representing seconds.
  If set to `0`, no timeout will be applied.

* Can be set at the `@env.task` decorator level and overridden at the `task.override()` invocation level.

* See [Retries and timeouts](./retries-and-timeouts).

### `triggers`

* Type: `Tuple[Trigger, ...] | Trigger`

* A trigger or tuple of triggers that define when the task should be executed.

* Can only be set at the `@env.task` decorator level. It cannot be overridden.

*  See [Triggers](./triggers).

### `interruptible`

* Type: `bool`

* Specifies whether the task is interruptible.
  If set to `True`, the task can be scheduled on a spot instance, otherwise it can only be scheduled on on-demand instances.

* Can be set at the `TaskEnvironment` level and overridden at the `@env.task` decorator level and at the `task.override()` invocation level.

<!-- TODO: Add when available
* See [Interruptible tasks](./interruptible-tasks).
-->

### `queue`

* Type: `Optional[str]`

* Specifies the queue to which the task should be directed, where the queue is identified by its name.
  If set to `None`, the default queue will be used.
  Queues serve to point to a specific partitions of your compute infrastructure (for example, a specific cluster in multi-cluster setup).
  They are configured as part of your Union/Flyte deployment.

* Can be set at the `TaskEnvironment` level and overridden at the `@env.task` decorator level
  and at the `task.override()` invocation level.

<!-- TODO: Add when available
* See [Queues](./queues).
-->

### `docs`

* Type: `Optional[Documentation]`

* Documentation for the task, including usage examples and explanations of the task's behavior.

* Can only be set at the `@env.task` decorator level. It cannot be overridden.

<!-- TODO: Add when available
* See [Names and descriptions](./names-and-descriptions).
-->
