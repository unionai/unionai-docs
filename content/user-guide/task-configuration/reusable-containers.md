---
title: Reusable containers
weight: 5
variants: +flyte +union
---

# Reusable containers

By default, each task execution in Flyte and Union runs in a fresh container instance that is created just for that execution and then discarded.
With reusable containers, the same container can be reused across multiple executions and tasks.
This approach reduces start up overhead and improves resource efficiency.

{{< variant flyte >}}
{{< markdown >}}

> [!NOTE]
> The reusable container feature is only available when running your Flyte code on a Union backend.
> See [one of the Union.ai product variants of this page]({{< docs_home union v2 >}}/user-guide/reusable-containers) for details.

{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< markdown >}}

> [!NOTE]
> The reusable container feature is only available when running your Flyte code on a Union backend.

## Why use reusable containers

The default fresh-container-per-execution model gives every execution strong isolation, but it pays a cold-start cost on every execution: the container has to be created, the image pulled, and the Python process initialized before your code runs.
When that startup cost is large relative to how long the task actually runs, the overhead dominates.
Reusable containers address this by keeping a pool of warm containers ready to accept work.
Reach for them when you have:

- **Many short tasks with high per-execution startup cost.** Fan-out and map-style workloads — where the same small task runs hundreds or thousands of times — benefit most, because the startup overhead is paid once per container instead of once per execution.
- **Expensive in-memory state to keep warm.** Because the same container (and its Python process) is reused across executions, you can load a model or dataset once and reuse it on subsequent invocations — for example by caching it in a global variable or with an in-memory cache — instead of reloading it every time. Prefer in-memory artifacts for this; a long-lived connection can go stale (credential rotation, idle timeouts), so if you cache one, guard it with a health check and reconnect when needed.
- **A need for higher throughput and better resource utilization.** A reusable environment can process multiple async task executions concurrently within each container. Total capacity is `max_replicas × concurrency`, so you can drive up utilization without provisioning a fresh container per task. See [Scale your workflows](../run-scaling/scale-your-workflows) for how this fits into a broader scaling strategy.

Stick with the default (non-reusable) model when tasks are long-running, run infrequently, or need strong isolation between executions — in those cases the startup cost is negligible and container reuse adds no benefit.

## How it works

With reusable containers, the system maintains a pool of persistent containers that can handle multiple task executions.
When you configure a `TaskEnvironment` with a `ReusePolicy`, the system does the following:

1. Creates a pool of persistent containers.
2. Routes task executions to available container instances.
3. Manages container lifecycle with configurable timeouts.
4. Supports concurrent task execution within containers (for async tasks).
5. Preserves the Python execution environment across task executions, allowing you to maintain state through global variables.

## Basic usage

> [!NOTE]
> The reusable containers feature currently requires a dedicated runtime library
> ([`unionai-reuse`](https://pypi.org/project/unionai-reuse/)) to be installed in the task image used by the reusable task.
> You can add this library to your task image using the `flyte.Image.with_pip_packages` method, as shown below.
> This library only needs to be added to the task image.
> It does not need to be installed in your local development environment.

Enable container reuse by adding a `ReusePolicy` to your `TaskEnvironment`:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-configuration/reusable-containers/reuse.py" lang="python" >}}
{{< markdown >}}

## `ReusePolicy` parameters

For complete parameter documentation, including accepted types, defaults, capacity math, and lifecycle behavior, see the [`ReusePolicy` API reference](../../api-reference/flyte-sdk/packages/flyte/reusepolicy).

## Understanding parameter relationships

The four `ReusePolicy` parameters work together to control different aspects of container management:

```python
reuse_policy = flyte.ReusePolicy(
    replicas=4,                           # Infrastructure: How many containers?
    concurrency=3,                        # Throughput: How many tasks per container?
    scaledown_ttl=timedelta(minutes=10),  # Individual: When do idle containers shut down?
    idle_ttl=timedelta(hours=1)           # Environment: When does the whole pool shut down?
)
# Total capacity: 4 × 3 = 12 concurrent tasks
# Individual containers shut down after 10 minutes of inactivity
# Entire environment shuts down after 1 hour of no tasks
```

### Key relationships

- **Total throughput** = `replicas × concurrency`
- **Resource usage** = `replicas × TaskEnvironment.resources`
- **Cost efficiency**: Higher `concurrency` reduces container overhead, more `replicas` provides better isolation
- **Lifecycle management**:  `scaledown_ttl` manages individual containers, `idle_ttl` manages the environment

## Simple example

Here is a simple, but complete, example of reuse with concurrency.

First, import the needed modules and set up logging:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-configuration/reusable-containers/reuse_concurrency.py" fragment="import" lang="python" >}}
{{< markdown >}}

Next, we set up the reusable task environment. Note that, currently, the image used for a reusable environment requires an extra package to be installed:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-configuration/reusable-containers/reuse_concurrency.py" fragment="env" lang="python" >}}
{{< markdown >}}

Now, we define the `reuse_concurrency` task (the main driver task of the workflow) and the `noop` task that will be executed multiple times reusing the same containers:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-configuration/reusable-containers/reuse_concurrency.py" fragment="tasks" lang="python" >}}
{{< markdown >}}

Finally, we deploy and run the workflow programmatically, so all you have to do is execute `python reuse_concurrency.py` to see it in action:

{{< /markdown >}}
{{< code file="/unionai-examples/v2/user-guide/task-configuration/reusable-containers/reuse_concurrency.py" fragment="run" lang="python" >}}
{{< /variant >}}
