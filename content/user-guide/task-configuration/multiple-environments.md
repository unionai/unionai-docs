---
title: Multiple environments
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
---

# Multiple environments

Flyte allows you to define multiple task environments within a single project, enabling you to organize tasks with different requirements and configurations.
The `depends_on` parameter in `TaskEnvironment` can be used to provide deployment hints by establishing a relationship between one `TaskEnvironment` and another.

## Core concepts

### TaskEnvironment independence

`TaskEnvironment`s are functionally independent.
The `depends_on` parameter is a **deployment hint only**, not a runtime dependency.
It ensures environments are deployed in a specific order but doesn't affect task execution.

### Deployment orchestration

The `depends_on` parameter:
- **ONLY** affects deployment order to the cluster.
- **Does NOT** create runtime dependencies between tasks.
- Helps organize logical relationships between environments.

## Basic usage

```python
import flyte

# Base environment: No dependencies
base_env = flyte.TaskEnvironment(
    name="base-utils",
    image="python:3.12-slim",
    resources=flyte.Resources(cpu="1", memory="2Gi")
)

# ML environment: Depends on base for deployment order
ml_env = flyte.TaskEnvironment(
    name="ml-training",
    image="pytorch:latest",
    resources=flyte.Resources(cpu="8", memory="16Gi", gpu="A100:2"),
    depends_on=[base_env]  # Deploy base_env first
)

# Tasks run independently regardless of environment dependencies
@base_env.task
async def load_config() -> dict:
    return {"model_path": "/models/latest"}

@ml_env.task
async def train_model() -> str:
    # Runs fine even if load_config() never executes
    return "model_trained"

# Runtime dependencies are created in workflows
@base_env.task
async def ml_pipeline() -> str:
    config = await load_config()      # Creates actual runtime dependency
    model = await train_model(config) # Data flows between tasks
    return model
```

## TaskEnvironment management

### Dependency specification

Define dependencies at `TaskEnvironment` creation time or add them dynamically:

```python
# Option 1: Define dependencies in constructor
base_env = flyte.TaskEnvironment(name="base", image="python:3.12")
ml_env = flyte.TaskEnvironment(
    name="ml-training",
    image="pytorch:latest",
    depends_on=[base_env]  # Specify dependencies in constructor
)

# Option 2: Add dependencies after creation
api_env = flyte.TaskEnvironment(name="api", image="fastapi:latest")
api_env.add_dependency(ml_env)  # Add dependency dynamically
```

### Deployment order

Flyte automatically handles deployment order based on dependencies:

```python
base_env = flyte.TaskEnvironment(name="base", image="python:3.12")
ml_env = flyte.TaskEnvironment(name="ml", image="pytorch:latest", depends_on=[base_env])
api_env = flyte.TaskEnvironment(name="api", image="fastapi:latest", depends_on=[ml_env])

# During deployment, Flyte ensures: base_env → ml_env → api_env
# You don't need to manually manage deployment order
```

### TaskEnvironment cloning

You can also create variations of existing `TaskEnvironment`s through cloning:

```python
base_template = flyte.TaskEnvironment(
    name="base-template",
    image="python:3.12-slim",
    resources=flyte.Resources(cpu="2", memory="4Gi")
)

# Clone with modifications
training_env = base_template.clone_with(
    name="training-specialized",
    resources=flyte.Resources(cpu="8", memory="32Gi", gpu="A100:2"),
    depends_on=[base_template]
)
```

## Best practices

- **Use meaningful names**: Follow consistent naming conventions (e.g., `data-processing`, `ml-training`).
- **Organize by function**: Group environments by domain or purpose.
- **Document relationships**: Use descriptions to explain environment purposes.
- **Avoid circular dependencies**: Flyte validates and prevents circular references.
- **Keep dependencies minimal**: Only add dependencies for logical deployment ordering.

Multiple environments enable organized, scalable workflows with clear separation of concerns and controlled deployment orchestration.
