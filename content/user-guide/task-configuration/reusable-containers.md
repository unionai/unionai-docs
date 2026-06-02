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

## How It Works

With reusable containers, the system maintains a pool of persistent containers that can handle multiple task executions.
When you configure a `TaskEnvironment` with a `ReusePolicy`, the system does the following:

1. Creates a pool of persistent containers.
2. Routes task executions to available container instances.
3. Manages container lifecycle with configurable timeouts.
4. Supports concurrent task execution within containers (for async tasks).
5. Preserves the Python execution environment across task executions, allowing you to maintain state through global variables.

## Basic Usage

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

Here is a simple, but complete, example of reuse with concurrency

First, import the needed modules, set upf logging:

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
