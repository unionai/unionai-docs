---
title: Resources
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Resources

Flyte allows you to specify precise resource requirements for your tasks, including CPU, memory, GPU, and storage. Proper resource allocation ensures optimal performance while managing costs effectively.

## Overview

The `Resources` class provides a comprehensive way to define computational requirements for tasks. You can specify both resource requests (minimum guaranteed resources) and limits (maximum allowed resources).

```python
import flyte

# Basic resource allocation
resources = flyte.Resources(
    cpu="2",           # 2 CPU cores
    memory="4Gi",      # 4 GiB of memory
    gpu="A100:1",      # 1 NVIDIA A100 GPU
    disk="10Gi"        # 10 GiB of ephemeral storage
)

env = flyte.TaskEnvironment(
    name="ml-training",
    resources=resources
)
```

## Resource Types

### CPU Resources

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

### Memory Resources

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

### GPU Resources

Flyte supports various GPU types and configurations:

#### Simple GPU Allocation
```python
# Basic GPU count
flyte.Resources(gpu=1)             # 1 GPU (any available type)
flyte.Resources(gpu=4)             # 4 GPUs

# Specific GPU types with quantity
flyte.Resources(gpu="T4:1")        # 1 NVIDIA T4 GPU
flyte.Resources(gpu="A100:2")      # 2 NVIDIA A100 GPUs
flyte.Resources(gpu="H100:8")      # 8 NVIDIA H100 GPUs
```

#### Advanced GPU Configuration
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

#### Supported GPU Types
- **T4**: Entry-level training and inference
- **L4**: Optimized for AI inference
- **L40s**: High-performance compute
- **A100**: High-end training and inference (40GB)
- **A100 80G**: High-end training with more memory (80GB)
- **H100**: Latest generation, highest performance

### TPU Resources

For Google Cloud TPU workloads:

```python
# TPU v5p configuration
tpu_config = flyte.TPU(device="V5P", partition="2x2x1")
flyte.Resources(gpu=tpu_config)  # Note: TPUs use the gpu parameter

# TPU v6e configuration
tpu_v6e = flyte.TPU(device="V6E", partition="4x4")
flyte.Resources(gpu=tpu_v6e)
```

### Storage Resources

#### Disk Storage
```python
flyte.Resources(disk="10Gi")       # 10 GiB ephemeral storage
flyte.Resources(disk="100Gi")      # 100 GiB ephemeral storage
```

#### Shared Memory
```python
flyte.Resources(shm="1Gi")         # 1 GiB shared memory (/dev/shm)
flyte.Resources(shm="auto")        # Auto-sized shared memory
```

## Resource Patterns

### Development vs Production

```python
# Development environment - minimal resources
dev_resources = flyte.Resources(
    cpu="500m",
    memory="1Gi"
)

# Production environment - guaranteed resources
prod_resources = flyte.Resources(
    cpu=("2", "4"),      # Request 2, limit to 4 cores
    memory=("4Gi", "8Gi"), # Request 4Gi, limit to 8Gi
    disk="50Gi"
)
```

### Machine Learning Workloads

```python
# Training environment
training_resources = flyte.Resources(
    cpu="8",
    memory="32Gi",
    gpu="A100:4",        # 4 A100 GPUs for distributed training
    disk="100Gi",
    shm="16Gi"           # Large shared memory for data loading
)

# Inference environment
inference_resources = flyte.Resources(
    cpu="2",
    memory="4Gi",
    gpu="T4:1",          # Single T4 for inference
    disk="20Gi"
)

# Large model inference with partitioning
efficient_inference = flyte.Resources(
    cpu="4",
    memory="16Gi",
    gpu=flyte.GPU(device="A100", quantity=1, partition="3g.20gb"),
    disk="50Gi"
)
```

### Data Processing Workloads

```python
# Memory-intensive data processing
data_processing_resources = flyte.Resources(
    cpu="4",
    memory="16Gi",       # High memory for in-memory processing
    disk="200Gi"         # Large disk for temporary data
)

# Distributed computing
spark_resources = flyte.Resources(
    cpu=("2", "8"),      # Flexible CPU allocation
    memory=("8Gi", "32Gi"), # Flexible memory allocation
    disk="100Gi"
)
```

## Usage in TaskEnvironment

### Environment-Level Resources

Set default resources for all tasks in an environment:

```python
# All tasks in this environment get these resources
ml_env = flyte.TaskEnvironment(
    name="ml-training",
    resources=flyte.Resources(
        cpu="4",
        memory="8Gi",
        gpu="A100:1"
    )
)

@ml_env.task
async def train_model(data: str) -> str:
    # This task uses the environment's resources
    return "model_trained"
```

### Task-Specific Resource Override

```python
from flyte import task

# Override resources for specific tasks
@task(
    resources=flyte.Resources(
        cpu="8",
        memory="16Gi",
        gpu="H100:2"
    )
)
async def heavy_training_task() -> str:
    return "heavy_model_trained"
```

## Advanced Configurations

### Custom Device Specifications

```python
# Custom device configuration
custom_device = flyte.Device(
    device="custom_accelerator",
    quantity=2,
    partition="large"
)

resources = flyte.Resources(gpu=custom_device)
```

### Resource Validation

The Resources class includes built-in validation:

```python
# This will raise a ValueError
try:
    invalid_resources = flyte.Resources(cpu=-1)  # CPU must be >= 0
except ValueError as e:
    print(f"Invalid resource: {e}")

# This will raise a ValueError
try:
    invalid_gpu = flyte.Resources(gpu="InvalidGPU:1")
except ValueError as e:
    print(f"Invalid GPU: {e}")
```

## Best Practices

### Right-Sizing Resources

```python
# ✅ Good: Match resources to workload
light_task_resources = flyte.Resources(
    cpu="500m",          # Adequate for light processing
    memory="1Gi"
)

# ❌ Avoid: Over-provisioning wastes resources
wasteful_resources = flyte.Resources(
    cpu="16",            # Too much for a simple task
    memory="64Gi"
)
```

### Using Resource Ranges

```python
# ✅ Good: Allow flexible scaling
flexible_resources = flyte.Resources(
    cpu=("1", "4"),      # Scale from 1-4 cores based on load
    memory=("2Gi", "8Gi") # Scale memory accordingly
)
```

### GPU Resource Management

```python
# ✅ Good: Use appropriate GPU types
inference_gpu = flyte.Resources(
    gpu="T4:1"           # T4 sufficient for inference
)

training_gpu = flyte.Resources(
    gpu="A100:4"         # A100s needed for large model training
)

# ✅ Good: Use partitioning for cost efficiency
partitioned_gpu = flyte.Resources(
    gpu=flyte.GPU(device="A100", quantity=1, partition="1g.5gb")
)
```

### Memory and Storage

```python
# ✅ Good: Allocate sufficient shared memory for data loading
data_heavy_resources = flyte.Resources(
    cpu="4",
    memory="8Gi",
    shm="2Gi",           # Shared memory for efficient data loading
    disk="50Gi"          # Adequate temporary storage
)
```

## Monitoring and Optimization

### Resource Utilization

Monitor your tasks to optimize resource allocation:

```python
# Start conservative, then optimize based on usage
initial_resources = flyte.Resources(
    cpu="1",
    memory="2Gi"
)

# After monitoring, adjust as needed
optimized_resources = flyte.Resources(
    cpu=("2", "4"),      # Found we need more CPU flexibility
    memory="4Gi"         # Memory usage was higher than expected
)
```

### Cost Optimization

```python
# Use spot instances with appropriate resource ranges
spot_resources = flyte.Resources(
    cpu=("2", "8"),      # Wide range for spot instance flexibility
    memory=("4Gi", "16Gi")
)

# Use GPU partitioning for cost efficiency
cost_efficient_gpu = flyte.Resources(
    gpu=flyte.GPU(device="A100", quantity=1, partition="2g.10gb")
)
```

## Integration with Other Features

Resources work seamlessly with other Flyte features:

```python
# Resources with reusable containers
reusable_env = flyte.TaskEnvironment(
    name="reusable-ml",
    resources=flyte.Resources(cpu="2", memory="4Gi", gpu="T4:1"),
    reusable=flyte.ReusePolicy(
        replicas=2,
        concurrency=3,
        idle_ttl=300
    )
)

# Resources with caching
cached_env = flyte.TaskEnvironment(
    name="cached-processing",
    resources=flyte.Resources(cpu="4", memory="8Gi"),
    cache=flyte.Cache(ttl="1h")
)
```

Resource allocation is fundamental to achieving optimal performance and cost efficiency in your Flyte workflows. Start with conservative estimates and refine based on monitoring and profiling data.
