---
title: Multiple environments
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
---

# Multiple environments

In many real-world applications, different components of your workflow may require different dependencies or configurations. Flyte enables you to manage this complexity by allowing multiple environments within a single project.

## Why use multiple environments?

Multiple environments are useful when:
- Different parts of your workflow need different dependencies
- Some tasks require specific CPU/GPU configurations
- You're integrating specialized tools that have conflicting requirements

## Multiple environment constraints

In a workflow with multiple environments, a task `task_1` in environment `env_1` can call a task `task_2` in another environment, `env_2`.

In this scenario, we say that `task_1` _depends on_ `task_2` because of two important constraints:

1. `env_2` must be deployed before `env_1`.
   * Otherwise, `env_1` might spin up and its `task_1` might try to call `task_2` before `env_2` is available.
   * To ensure this, you must explicitly declare the dependency relationship by adding the parameter `depends_on=[env_2]` to `TaskEnvironment` definition of `env_1`.

2. All dependencies in `env_2` must also be included in `env_1`.
   * Because, during the execution of `task_1`, the Python interpreter will initially load the function `task_2` into `env_1` before actually invoking the run of `task_2` in `env_2`.
   * To ensure this, all dependencies declared in `env_2`'s container image must also be included in `env_1`'s container image definition.

For example:

```python
import flyte

env_2 = flyte.TaskEnvironment(
    name="env_2",
    image="python:3.12-slim",
    # e2 dependencies
    packages=["numpy", "pandas"],
)

env_1 = flyte.TaskEnvironment(
    name="env_1",
    image


    image="python:3.12-slim",
    # e1 dependencies
    packages=["scikit-learn"],
    depends_on=[e2]
)




declaring in the definition of t1 that it depends on `e2`. This ensures that the system knows to deploy `e2` before `e1`.

In order comply with these constraints, the code must dotwo things:

1. All dependncies declared for `e2` must also be declared for `e1`. This is achieved by ensuring that the dependencies declared `e2`'s container image are also included in `e1`'s container image.

2. The definition of `e1` must declare that it depends on `e2` using, in order to ensure that the system knows to deploy `e2` before `e1`.

The first of these can be achieved by ensuring that the dependencies of `e2` are also included in `e1`.





2. the parent task's environment must include all dependencies from the child task's environment. This is because the parent task loads the child task during execution.

that uses a different environment.





When configuring and deploying a workflow with multiple environments you must take into account two constraints:

* Whne a tThere are two constraints that you must take into account when con environments







## The `depends_on` parameter

The `depends_on` parameter in `TaskEnvironment` can be used to provide deployment-time dependencies by establishing a relationship between one `TaskEnvironment` and another.







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
