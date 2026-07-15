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
- **`memory`**: Memory with Kubernetes units — `"4Gi"`, or `(request, limit)` tuple. Leave headroom below a node's total RAM: its *allocatable* memory is smaller (the kubelet reserves overhead for the OS and system daemons), so a request near a node's nominal capacity can leave the pod stuck `Pending`.
- **`gpu`**: GPU allocation — `"A100:2"`, integer count, or `GPU()`/`TPU()`/`Device()` for advanced config.
- **`disk`**: Ephemeral storage — `"10Gi"`.
- **`shm`**: Shared memory — `"1Gi"` or `"auto"`.

{{< variant union >}}
{{< markdown >}}
For how task resource requests interact with project-domain quotas as you scale across teams, see [Resource management and multi-team scaling](../project-patterns/resource-management).
{{< /markdown >}}
{{< /variant >}}

## Ephemeral storage

The `disk` parameter requests *ephemeral storage* — node-local scratch disk for the task's container. Set it as a string with Kubernetes units, for example `"50Gi"`:

```python
env = flyte.TaskEnvironment(
    name="etl_env",
    resources=flyte.Resources(cpu=2, memory="4Gi", disk="50Gi"),
)
```

Under the hood, `disk` maps to the Kubernetes [`ephemeral-storage`](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#local-ephemeral-storage) resource on the task's container.

**What it covers.** Ephemeral storage is the local disk a task writes to while it runs: the container's writable filesystem and any temporary files your code creates on the local filesystem during execution (downloaded datasets, intermediate outputs, model checkpoints staged before offload). It is distinct from the offloaded storage backing `flyte.io.File` and `flyte.io.Dir`, which lives in the blob store rather than on the node.

**Lifecycle.** Ephemeral storage is tied to the task's pod: it is provisioned when the task starts and reclaimed when the pod terminates. Nothing written to it survives beyond the task run, so use it for scratch work — persist anything you need to keep to a `flyte.io.File` or `flyte.io.Dir` in object storage.

**Single value, not a request/limit range.** Unlike `cpu` and `memory`, `disk` takes a single string, not a `(request, limit)` tuple.

**Default behavior.** Flyte does not set an `ephemeral-storage` request or limit when `disk` is unset. (A cluster-level Kubernetes `LimitRange`, if configured, may still inject a default.) The pod can still write to node-local disk, but it may be evicted if the node comes under storage pressure. Tasks doing heavy local data processing should set `disk` explicitly.

{{< variant union >}}
{{< markdown >}}
For how ephemeral-storage sizing plays out as you scale across teams and quotas, see [Be explicit about ephemeral storage](../project-patterns/resource-management#be-explicit-about-ephemeral-storage).
{{< /markdown >}}
{{< /variant >}}

## Examples

### Usage in TaskEnvironment

Here's a complete example of defining a TaskEnvironment with resource specifications for a machine learning training workload:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="task-env" lang="python" >}}

### Usage in a task-specific override

{{< code file="/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="override" lang="python" >}}

For complete format specifications for each resource type (CPU, memory, GPU/TPU/Device, disk, shared memory), including accepted string formats, request/limit ranges, GPU partitioning, and supported accelerator types, see the [`Resources` API reference](../../api-reference/flyte-sdk/packages/flyte/resources).
