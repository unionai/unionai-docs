---
title: TaskEnvironment
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# TaskEnvironment

A `TaskEnvironment` defines the hardware and software environment where your tasks run. Think of it as the container configuration for your code.

## A minimal example

Here's the simplest possible TaskEnvironment:

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def hello() -> str:
    return "Hello from Flyte!"
```

With just a `name`, you get Flyte's default container image and resource allocation. This is enough for simple tasks that only need Python and the Flyte SDK.

## What TaskEnvironment controls

A TaskEnvironment specifies two things:

**Hardware environment** - The compute resources allocated to each task:
- CPU cores
- Memory
- GPU type and count

**Software environment** - The container image your code runs in:
- Base image (Python version, OS)
- Installed packages and dependencies
- Environment variables

## Configuring resources

Use the `limits` parameter to specify compute resources:

```python
env = flyte.TaskEnvironment(
    name="compute_heavy",
    limits=flyte.Resources(cpu="4", mem="16Gi"),
)
```

For GPU workloads:

```python
env = flyte.TaskEnvironment(
    name="gpu_training",
    limits=flyte.Resources(cpu="8", mem="32Gi", gpu="1"),
    accelerator=flyte.GPUAccelerator.NVIDIA_A10G,
)
```

## Configuring container images

For tasks that need additional Python packages, specify a custom image:

```python
image = flyte.Image.from_debian_base().with_pip_packages("pandas", "scikit-learn")

env = flyte.TaskEnvironment(
    name="ml_env",
    image=image,
)
```

See [Container images](../task-configuration/container-images) for detailed image configuration options.

## Multiple tasks, one environment

All tasks decorated with the same `@env.task` share that environment's configuration:

```python
env = flyte.TaskEnvironment(
    name="data_processing",
    limits=flyte.Resources(cpu="2", mem="8Gi"),
)

@env.task
def load_data(path: str) -> dict:
    # Runs with 2 CPU, 8Gi memory
    ...

@env.task
def transform_data(data: dict) -> dict:
    # Also runs with 2 CPU, 8Gi memory
    ...
```

This is useful when multiple tasks have similar requirements.

## Multiple environments

When tasks have different requirements, create separate environments:

```python
light_env = flyte.TaskEnvironment(
    name="light",
    limits=flyte.Resources(cpu="1", mem="2Gi"),
)

heavy_env = flyte.TaskEnvironment(
    name="heavy",
    limits=flyte.Resources(cpu="8", mem="32Gi"),
)

@light_env.task
def preprocess(data: str) -> str:
    # Light processing
    ...

@heavy_env.task
def train_model(data: str) -> dict:
    # Resource-intensive training
    ...
```

## Next steps

Now that you understand TaskEnvironments, let's look at how to define [tasks](./tasks) that run inside them.
