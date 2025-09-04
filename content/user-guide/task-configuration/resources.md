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

```python
resources = Resources(
    cpu: Union[int, float, str, Tuple[Union[int, float, str], Union[int, float, str]], None] = None,
    memory: Union[str, Tuple[str, str], None] = None,
    gpu: Union[str, int, Device, None] = None,  # Accelerators string, count, or Device object
    disk: Union[str, None] = None,
    shm: Union[str, Literal["auto"], None] = None
)
```

Each parameter is optional and allows you to specify different types of resources:

- **`cpu`**: CPU allocation - can be a number, string, or tuple for request/limit ranges (e.g., `2` or `(2, 4)`).
- **`memory`**: Memory allocation - string with units (e.g., `"4Gi"`) or tuple for ranges.
- **`gpu`**: GPU allocation - accelerator string (e.g., `"A100:2"`), count, or `Device` (a [`GPU`](#gpu-resources), [`TPU`](#tpu-resources) or [custom `Device` object](#custom-device-specifications)).
- **`disk`**: Ephemeral storage - string with units (e.g., `"10Gi"`).
- **`shm`**: Shared memory - string with units or `"auto"` for automatic sizing (e.g., `"8Gi"` or `"auto"`).

## Examples

### Usage in TaskEnvironment

Here's a complete example of defining a TaskEnvironment with resource specifications for a machine learning training workload:

```python
import flyte

# Define a TaskEnvironment for ML training tasks
ml_training_env = flyte.TaskEnvironment(
    name="ml-training",
    resources=flyte.Resources(
        cpu=("2", "8"),        # Request 2 cores, allow up to 8 cores for scaling
        memory=("8Gi", "32Gi"), # Request 8 GiB, allow up to 32 GiB for large datasets
        gpu="A100:2",          # 2 NVIDIA A100 GPUs for training
        disk="50Gi",           # 50 GiB ephemeral storage for checkpoints
        shm="8Gi"              # 8 GiB shared memory for efficient data loading
    )
)

# Use the environment for tasks
@ml_training_env.task
async def train_model(dataset_path: str) -> str:
    # This task will run with flexible resource allocation
    return "model_trained_successfully"
```

### Usage in a task-specific override

```python
from flyte import task

# Override resources for specific tasks
@task(
    resources=flyte.Resources(
        cpu="16",
        memory="64Gi",
        gpu="H100:2",
        disk="50Gi",
        shm="8Gi"
    )
)
async def heavy_training_task() -> str:
    return "heavy_model_trained"
```

## Resource types

### CPU resources

CPU can be specified in several formats:

```python
# String formats (Kubernetes-style)
flyte.Resources(cpu="500m")        # 500 milliCPU (0.5 cores)
flyte.Resources(cpu="2")           # 2 CPU cores
flyte.Resources(cpu="1.5")         # 1.5 CPU cores

# Numeric formats
flyte.Resources(cpu=1)             # 1 CPU core
flyte.Resources(cpu=0.5)           # 0.5 CPU cores

# Request and limit ranges
flyte.Resources(cpu=("1", "2"))    # Request 1 core, limit to 2 cores
flyte.Resources(cpu=(1, 4))        # Request 1 core, limit to 4 cores
```

### Memory resources

Memory specifications follow Kubernetes conventions:

```python
# Standard memory units
flyte.Resources(memory="512Mi")    # 512 MiB
flyte.Resources(memory="1Gi")      # 1 GiB
flyte.Resources(memory="2Gi")      # 2 GiB
flyte.Resources(memory="500M")     # 500 MB (decimal)
flyte.Resources(memory="1G")       # 1 GB (decimal)

# Request and limit ranges
flyte.Resources(memory=("1Gi", "4Gi"))  # Request 1 GiB, limit to 4 GiB
```

### GPU resources

Flyte supports various GPU types and configurations:

#### Simple GPU allocation

```python
# Basic GPU count
flyte.Resources(gpu=1)             # 1 GPU (any available type)
flyte.Resources(gpu=4)             # 4 GPUs

# Specific GPU types with quantity
flyte.Resources(gpu="T4:1")        # 1 NVIDIA T4 GPU
flyte.Resources(gpu="A100:2")      # 2 NVIDIA A100 GPUs
flyte.Resources(gpu="H100:8")      # 8 NVIDIA H100 GPUs
```

#### Advanced GPU configuration

You can also use the `GPU` helper class for more detailed configurations:

```python
# Using the GPU helper function
gpu_config = flyte.GPU(device="A100", quantity=2)
flyte.Resources(gpu=gpu_config)

# GPU with memory partitioning (A100 only)
partitioned_gpu = flyte.GPU(
    device="A100",
    quantity=1,
    partition="1g.5gb"  # 1/7th of A100 with 5GB memory
)
flyte.Resources(gpu=partitioned_gpu)

# A100 80GB with partitioning
large_partition = flyte.GPU(
    device="A100 80G",
    quantity=1,
    partition="7g.80gb"  # Full A100 80GB
)
```

#### Supported GPU types
- **T4**: Entry-level training and inference
- **L4**: Optimized for AI inference
- **L40s**: High-performance compute
- **A100**: High-end training and inference (40GB)
- **A100 80G**: High-end training with more memory (80GB)
- **H100**: Latest generation, highest performance

### Custom device specifications

You can also define custom devices if your infrastructure supports them:

```python
# Custom device configuration
custom_device = flyte.Device(
    device="custom_accelerator",
    quantity=2,
    partition="large"
)

resources = flyte.Resources(gpu=custom_device)
```

### TPU resources

For Google Cloud TPU workloads you can specify TPU resources using the `TPU` helper class:

```python
# TPU v5p configuration
tpu_config = flyte.TPU(device="V5P", partition="2x2x1")
flyte.Resources(gpu=tpu_config)  # Note: TPUs use the gpu parameter

# TPU v6e configuration
tpu_v6e = flyte.TPU(device="V6E", partition="4x4")
flyte.Resources(gpu=tpu_v6e)
```

### Storage resources

Flyte provides two types of storage resources for tasks: ephemeral disk storage and shared memory.
These resources are essential for tasks that need temporary storage for processing data, caching intermediate results, or sharing data between processes.

#### Disk storage

Ephemeral disk storage provides temporary space for your tasks to store intermediate files, downloaded datasets, model checkpoints, and other temporary data. This storage is automatically cleaned up when the task completes.

```python
flyte.Resources(disk="10Gi")       # 10 GiB ephemeral storage
flyte.Resources(disk="100Gi")      # 100 GiB ephemeral storage
flyte.Resources(disk="1Ti")        # 1 TiB for large-scale data processing

# Common use cases
flyte.Resources(disk="50Gi")       # ML model training with checkpoints
flyte.Resources(disk="200Gi")      # Large dataset preprocessing
flyte.Resources(disk="500Gi")      # Video/image processing workflows
```

#### Shared memory

Shared memory (`/dev/shm`) is a high-performance, RAM-based storage area that can be shared between processes within the same container. It's particularly useful for machine learning workflows that need fast data loading and inter-process communication.

```python
flyte.Resources(shm="1Gi")         # 1 GiB shared memory (/dev/shm)
flyte.Resources(shm="auto")        # Auto-sized shared memory
flyte.Resources(shm="16Gi")        # Large shared memory for distributed training
```
