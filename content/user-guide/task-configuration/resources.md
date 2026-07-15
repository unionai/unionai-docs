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
- **`gpu`**: GPU or other accelerator allocation — `"A100:2"`, integer count, or `flyte.GPU()`, `flyte.TPU()`, `flyte.AMD_GPU()`, or `flyte.Device()` for advanced config. See [Accelerators](#accelerators) below.
- **`disk`**: Ephemeral storage — `"10Gi"`.
- **`shm`**: Shared memory — `"1Gi"` or `"auto"`.

{{< variant union >}}
{{< markdown >}}
For how task resource requests interact with project-domain quotas as you scale across teams, see [Resource management and multi-team scaling](../project-patterns/resource-management).
{{< /markdown >}}
{{< /variant >}}

## Examples

### Usage in TaskEnvironment

Here's a complete example of defining a TaskEnvironment with resource specifications for a machine learning training workload:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="task-env" lang="python" >}}

### Usage in a task-specific override

{{< code file="/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="override" lang="python" >}}

For complete format specifications for each resource type (CPU, memory, GPU/TPU/Device, disk, shared memory), including accepted string formats, request/limit ranges, GPU partitioning, and supported accelerator types, see the [`Resources` API reference](../../api-reference/flyte-sdk/packages/flyte/resources).

## Accelerators

To run a task on a hardware accelerator — an NVIDIA or AMD GPU, a Google TPU, an AWS Trainium/Inferentia (Neuron) chip, or an Intel Habana Gaudi device — set the `gpu` parameter of `Resources`. Despite its name, `gpu` selects any supported accelerator type.

You can request an accelerator in three ways:

- **Type-and-count string** — `"<device>:<count>"`, for example `"T4:1"` or `"A100:8"`. This is the most common form.
- **Integer count** — `gpu=2` requests that many GPUs of whatever type is available.
- **Device object** — `flyte.GPU()`, `flyte.TPU()`, `flyte.AMD_GPU()`, or `flyte.Device()` for advanced configuration such as GPU partitioning (MIG) and TPU slice topologies.

The `gpu` value can be set on the `TaskEnvironment` (applying to every task in it) or on a per-task `override`, exactly like the other resource fields shown above.

### NVIDIA GPUs

Request an NVIDIA GPU by type and count:

```python
import flyte

env = flyte.TaskEnvironment(
    name="nvidia",
    resources=flyte.Resources(gpu="T4:1"),  # one NVIDIA T4
)
```

Supported NVIDIA types include `T4`, `L4`, `L40s`, `A10`, `A10G`, `A100`, `A100 80G`, `B200`, `H100`, `H200`, and `V100`.

#### GPU partitioning (MIG)

To request a Multi-Instance GPU (MIG) partition, use `flyte.GPU()` with a `partition`:

```python
resources=flyte.Resources(gpu=flyte.GPU(device="A100", quantity=1, partition="1g.5gb"))
```

Partitioning is available on `A100`, `A100 80G`, `H100`, and `H200`.

### Google TPUs

Use `flyte.TPU()` with the device type and, optionally, a slice topology:

```python
resources=flyte.Resources(gpu=flyte.TPU(device="V5P", partition="2x2x1"))
```

Supported TPU device types are `V5P` and `V6E`.

### AMD GPUs

Request an AMD GPU by type and count, or with `flyte.AMD_GPU()`:

```python
resources=flyte.Resources(gpu="MI300X:1")
```

Supported AMD types include `MI100`, `MI210`, `MI250`, `MI250X`, `MI300A`, `MI300X`, `MI325X`, `MI350X`, and `MI355X`.

### AWS Trainium and Inferentia (Neuron)

Request AWS Neuron accelerators — Trainium (`Trn`) or Inferentia (`Inf`) — by type and count:

```python
resources=flyte.Resources(gpu="Trn1:1")
```

Supported types include `Trn1`, `Trn1n`, `Trn2`, `Trn2u`, `Inf1`, and `Inf2`.

### Intel Habana Gaudi

Request an Intel Habana Gaudi accelerator by type and count:

```python
resources=flyte.Resources(gpu="Gaudi1:1")
```

> [!NOTE]
> Which accelerator types are actually available depends on your deployment and the node pools configured in your cluster. Requesting a type that no node provides will leave the task's pod `Pending`.

For the full list of accepted accelerator strings and device-configuration options, see the [`Resources` API reference](../../api-reference/flyte-sdk/packages/flyte/resources).
