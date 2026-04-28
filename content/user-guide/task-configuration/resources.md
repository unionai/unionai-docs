---
title: Resources
weight: 2
variants: +flyte +union
---

# Resources

Task resources specify the computational limits and requests (CPU, memory, GPU, storage) that will be allocated to each task's container during execution.

To specify resource requirements for your task, instantiate a `Resources` object with the desired parameters and assign it to either
the `resources` parameter of the `TaskEnvironment` or the `resources` parameter of the `override` function (for invocation overrides).

Every task defined using that `TaskEnvironment` will run with the specified resources.
If a specific task has its own `resources` defined in the decorator, it will override the environment's resources for that task only.

If neither `TaskEnvironment` nor the task decorator specifies `resources`, the default resource allocation will be used.

## Resources data class

For the full class definition, parameter types, and accepted formats, see the [`Resources` API reference](../../api-reference/flyte-sdk/packages/flyte/resources).

The main parameters are:

- **`cpu`**: CPU allocation — number, string (`"500m"`), or `(request, limit)` tuple.
- **`memory`**: Memory with Kubernetes units — `"4Gi"`, or `(request, limit)` tuple.
- **`gpu`**: GPU allocation — `"A100:2"`, integer count, or `GPU()`/`TPU()`/`Device()` for advanced config.
- **`disk`**: Ephemeral storage — `"10Gi"`.
- **`shm`**: Shared memory — `"1Gi"` or `"auto"`.

## Examples

### Usage in TaskEnvironment

Here's a complete example of defining a TaskEnvironment with resource specifications for a machine learning training workload:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="task-env" lang="python" >}}

### Usage in a task-specific override

{{< code file="/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="override" lang="python" >}}

For complete format specifications for each resource type (CPU, memory, GPU/TPU/Device, disk, shared memory), including accepted string formats, request/limit ranges, GPU partitioning, and supported accelerator types, see the [`Resources` API reference](../../api-reference/flyte-sdk/packages/flyte/resources).
