---
title: Resources
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Resources

Task resources specify the computational limits and requests (CPU, memory, GPU, storage) that will be allocated to each task's container during execution.

To specify resource requirements for your task, instantiate a `Resources` object with the desired parameters and assign it to either
the `resources` parameter of the `TaskEnvironment` or the `resources` parameter of the `Task` decorator.

Every task defined using that `TaskEnvironment` will run with the specified resources.
If a specific task has its own `resources` defined in the decorator, it will override the environment's resources for that task only.

If neither `TaskEnvironment` nor the task decorator specifies `resources`, the default resource allocation will be used.

## Resources dataclass

The `Resources` dataclass provides the following initialization parameters:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="params" lang="python" >}}

Each parameter is optional and allows you to specify different types of resources:

- **`cpu`**: CPU allocation - can be a number, string, or tuple for request/limit ranges (e.g., `2` or `(2, 4)`).
- **`memory`**: Memory allocation - string with units (e.g., `"4Gi"`) or tuple for ranges.
- **`gpu`**: GPU allocation - accelerator string (e.g., `"A100:2"`), count, or `Device` (a [`GPU`](#gpu-resources), [`TPU`](#tpu-resources) or [custom `Device` object](#custom-device-specifications)).
- **`disk`**: Ephemeral storage - string with units (e.g., `"10Gi"`).
- **`shm`**: Shared memory - string with units or `"auto"` for automatic sizing (e.g., `"8Gi"` or `"auto"`).

## Examples

### Usage in TaskEnvironment

Here's a complete example of defining a TaskEnvironment with resource specifications for a machine learning training workload:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="task-env" lang="python" >}}

### Usage in a task-specific override

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="override" lang="python" >}}

## Resource types

### CPU resources

CPU can be specified in several formats:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="cpu" lang="python" >}}

### Memory resources

Memory specifications follow Kubernetes conventions:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="memory" lang="python" >}}

### GPU resources

Flyte supports various GPU types and configurations:

#### Simple GPU allocation

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="gpu" lang="python" >}}

#### Advanced GPU configuration

You can also use the `GPU` helper class for more detailed configurations:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="advanced-gpu" lang="python" >}}

#### Supported GPU types
- **T4**: Entry-level training and inference
- **L4**: Optimized for AI inference
- **L40s**: High-performance compute
- **A100**: High-end training and inference (40GB)
- **A100 80G**: High-end training with more memory (80GB)
- **H100**: Latest generation, highest performance

### Custom device specifications

You can also define custom devices if your infrastructure supports them:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="custom" lang="python" >}}

### TPU resources

For Google Cloud TPU workloads you can specify TPU resources using the `TPU` helper class:

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="tpu" lang="python" >}}

### Storage resources

Flyte provides two types of storage resources for tasks: ephemeral disk storage and shared memory.
These resources are essential for tasks that need temporary storage for processing data, caching intermediate results, or sharing data between processes.

#### Disk storage

Ephemeral disk storage provides temporary space for your tasks to store intermediate files, downloaded datasets, model checkpoints, and other temporary data. This storage is automatically cleaned up when the task completes.

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="disk" lang="python" >}}

#### Shared memory

Shared memory (`/dev/shm`) is a high-performance, RAM-based storage area that can be shared between processes within the same container. It's particularly useful for machine learning workflows that need fast data loading and inter-process communication.

{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/resources/resources.py" fragment="shm" lang="python" >}}
