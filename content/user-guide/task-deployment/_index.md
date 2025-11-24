---
title: Task deployment and run
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Task deployment and run

You have seen how to configure and build the tasks that compose your project.
In this section we will explain how to deploy those tasks to the Flyte or Union backend and execute them.

## Running tasks immediately

As we saw in [Getting started](../getting-started/) you can use the CLI to deploy and run your code in one step with `flyte run`:

```bash
flyte run <source_file_path> <task_name> --<input_1> <value_1> --<input_2> <value_2>
```

Here is a concrete example:

```bash
flyte run workflows/data_pipeline.py process_data --input_path "/data/raw" --batch_size 100
```

The programmatic equivalent of this is `flyte.run()`:

```python
import flyte
flyte.init_from_config()
result = flyte.run(<task_function>, <input_1>=<value_1>, <input_2>=<value_2>)
print(f"Task URL: {result.url}")
print(f"Run name: {result.name}")
```

Under the hood, the run command actually does a lot of work automatically. They:
* They deploy all task environments in the Specified python file Deploy the necessary task environments if they are not already deployed, and then execute the specified task on the backend.
But to fully leverage Flyte's capabilities, you will typically want to deploy your task environments explicitly and then run tasks or workflows as needed.

Let's explore how to do that in the sections below.

## Under the hood



To move your code from your local machine to a Flyte/Union backend, you must deploy the `TaskEnvironment`s that contain your tasks.

From there you can run theose tasks

The simplest


 covers how to deploy environments, run tasks, and execute workflows in Flyte 2.

In Flyte 2, tasks are organized into **Task Environments** which define the execution context, dependencies, and configuration for groups of related tasks.

## Terminology

You hav

### Task Environments

A **Task Environment** (`flyte.TaskEnvironment`) is the fundamental organizational unit in Flyte 2.
It groups related tasks together and defines their shared configuration including:

- **Container images** and dependencies
- **Resource requirements** (CPU, memory, GPU)
- **Environment variables** and secrets
- **Execution policies** (retries, timeouts, caching)

```python
import flyte

# Create a task environment
env = flyte.TaskEnvironment(
    name="data_processing",
    resources=flyte.Resources(memory="2Gi", cpu="1"),
    image=flyte.Image.from_debian_base().with_pip_packages("pandas", "numpy"),
    env_vars={"LOG_LEVEL": "INFO"}
)
```

See [Task configuration](../task-configuration/) for more details on task environments.

### Tasks

**Tasks** are Python functions decorated with `@env.task` that define individual units of work. Tasks can be synchronous or asynchronous:

```python
@env.task
async def process_data(input_path: str) -> str:
    # Task implementation
    return f"Processed {input_path}"

@env.task
def compute_metrics(data: str) -> dict:
    # Synchronous task
    return {"accuracy": 0.95, "loss": 0.05}
```

### Workflows

**Workflows** in Flyte 2 are simply tasks that call other tasks.
There's no separate workflow syntax.
Any task that orchestrates other tasks becomes a workflow:

```python
@env.task
async def data_pipeline(input_path: str) -> dict:
    # This is a workflow - it orchestrates other tasks
    processed_data = await process_data(input_path)
    metrics = await compute_metrics(processed_data)
    return metrics
```

## Deploying environments

### Basic deployment

Deploy a task environment using `flyte.deploy()`:

```python
import flyte

env = flyte.TaskEnvironment(name="my_workflow")

@env.task
async def hello_world(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    flyte.init_from_config()
    deployment = flyte.deploy(env)
    print(deployment[0].summary_repr())
```

### Command-line deployment

Deploy from the command line using the `flyte deploy` command:

```bash
# Deploy a specific environment from a Python file
flyte deploy my_workflow.py env

# Deploy with a specific version
flyte deploy --version "v1.0.0" my_workflow.py env

# Dry run to see what would be deployed
flyte deploy --dryrun my_workflow.py env
```

### Deployment options

The `flyte.deploy()` function accepts several parameters:

```python
deployment = flyte.deploy(
    env,                          # Environment to deploy
    dryrun=False,                # Set to True for dry run
    version="v1.0.0",            # Specific version tag
    copy_style="loaded_modules"   # How to copy dependencies
)
```

**Copy styles:**
- `"loaded_modules"` (default): Copy only loaded Python modules
- `"all"`: Copy all files in the project directory

## Running tasks and workflows

### Running tasks locally

Run tasks locally for testing and development:

```python
import flyte

env = flyte.TaskEnvironment(name="local_testing")

@env.task
async def process_file(filename: str) -> str:
    return f"Processing {filename}"

if __name__ == "__main__":
    flyte.init_from_config()

    # Run locally
    result = flyte.run(process_file, filename="data.csv")
    print(f"Task URL: {result.url}")
    print(f"Run name: {result.name}")

    # Wait for completion and stream logs
    result.wait()
```

### Running with command line

Execute tasks from the command line:

```bash
# Run a specific task
flyte run my_workflow.py process_file --filename "data.csv"

# Run with multiple parameters
flyte run my_workflow.py data_pipeline --input_path "/data" --batch_size 100
```

### Workflow execution patterns

#### Sequential workflows

Execute tasks in sequence:

```python
@env.task
async def extract_data(source: str) -> str:
    return f"Data from {source}"

@env.task
async def transform_data(data: str) -> str:
    return f"Transformed: {data}"

@env.task
async def load_data(data: str) -> str:
    return f"Loaded: {data}"

@env.task
async def etl_pipeline(source: str) -> str:
    # Sequential execution
    raw_data = await extract_data(source)
    transformed = await transform_data(raw_data)
    result = await load_data(transformed)
    return result
```

#### Parallel workflows

Execute tasks in parallel using `asyncio.gather()`:

```python
import asyncio

@env.task
async def process_batch(batch_id: int, data: str) -> str:
    return f"Batch {batch_id}: {data}"

@env.task
async def parallel_processing(data_batches: list[str]) -> list[str]:
    # Create tasks for parallel execution
    tasks = []
    for i, batch in enumerate(data_batches):
        tasks.append(process_batch(i, batch))

    # Execute in parallel
    results = await asyncio.gather(*tasks)
    return results
```

#### Dynamic workflows with grouping

Use `flyte.group()` to organize parallel tasks:

```python
@env.task
async def process_item(item: str) -> str:
    return f"Processed {item}"

@env.task
async def dynamic_workflow(items: list[str]) -> list[str]:
    results = []

    # Group related tasks for better visualization
    with flyte.group("batch-processing"):
        for item in items:
            results.append(process_item(item))

        # Execute all tasks in the group
        processed = await asyncio.gather(*results)

    return processed
```

## Multi-environment workflows

For complex workflows requiring different dependencies or configurations, use multiple environments:

### Creating environment dependencies

```python
# Environment for data preprocessing
prep_env = flyte.TaskEnvironment(
    name="preprocessing",
    image=flyte.Image.from_debian_base().with_pip_packages("pandas", "numpy")
)

# Environment for ML training
ml_env = flyte.TaskEnvironment(
    name="ml_training",
    depends_on=[prep_env],  # Dependency declaration
    image=flyte.Image.from_debian_base().with_pip_packages("torch", "sklearn"),
    resources=flyte.Resources(memory="8Gi", cpu="4")
)

# Environment for orchestration
orchestrator_env = flyte.TaskEnvironment(
    name="orchestrator",
    depends_on=[prep_env, ml_env]  # Must include all child dependencies
)
```

### Cross-environment task invocation

```python
@prep_env.task
async def preprocess_data(raw_data: str) -> str:
    return f"Cleaned: {raw_data}"

@ml_env.task
async def train_model(processed_data: str) -> str:
    return f"Model trained on: {processed_data}"

@orchestrator_env.task
async def ml_pipeline(raw_data: str) -> str:
    # This task calls tasks from different environments
    cleaned = await preprocess_data(raw_data)
    model = await train_model(cleaned)
    return model
```

### Deploying multi-environment workflows

Deploy the orchestrator environment which will deploy its dependencies:

```python
if __name__ == "__main__":
    flyte.init_from_config()
    # This deploys orchestrator_env and its dependencies
    deployment = flyte.deploy(orchestrator_env)

    # Run the multi-environment workflow
    result = flyte.run(ml_pipeline, raw_data="training_data.csv")
    result.wait()
```

## Advanced deployment patterns

### Dynamic environment selection

Create environments dynamically based on runtime conditions:

```python
import os

def create_environment():
    if flyte.current_domain() == "development":
        return flyte.TaskEnvironment(
            name="dev_env",
            image=flyte.Image.from_debian_base(),
            env_vars={"ENV": "dev"}
        )
    else:
        return flyte.TaskEnvironment(
            name="prod_env",
            image=flyte.Image.from_debian_base(),
            env_vars={"ENV": "prod"},
            resources=flyte.Resources(memory="4Gi", cpu="2")
        )

env = create_environment()
```

### Remote task references

Reference tasks from previously deployed environments:

```python
# Reference a task from another deployed environment
remote_task = flyte.remote.Task.get("other_env.process_data", auto_version="latest")

@env.task
async def orchestrator() -> str:
    # Call the remote task
    result = await remote_task(input="test_data")
    return result
```

### Container image customization

Use custom Docker images for specialized requirements:

```python
# Using a custom Dockerfile
env = flyte.TaskEnvironment(
    name="custom_image_env",
    image=flyte.Image.from_dockerfile(
        "Dockerfile",
        registry="ghcr.io/myorg",
        name="my_custom_image"
    )
)

# Building from existing image with packages
env = flyte.TaskEnvironment(
    name="ml_env",
    image=flyte.Image.from_registry("pytorch/pytorch:2.0-cuda11.7")
        .with_pip_packages("transformers", "datasets")
        .with_apt_packages("git", "curl")
)
```

## Monitoring and debugging

### Execution monitoring

Monitor workflow execution:

```python
if __name__ == "__main__":
    flyte.init_from_config()

    # Start execution
    run = flyte.run(my_workflow, input_data="test")

    # Monitor progress
    print(f"Execution URL: {run.url}")
    print(f"Run ID: {run.name}")

    # Stream logs to console
    run.wait()

    # Check execution status
    if run.status == "SUCCEEDED":
        print("Workflow completed successfully")
    else:
        print(f"Workflow failed with status: {run.status}")
```

### Error handling and retries

Configure retry policies and error handling:

```python
@env.task(
    retries=3,                    # Retry up to 3 times
    timeout=300,                  # 5 minute timeout
    interruptible=True            # Allow interruption for cost savings
)
async def resilient_task(data: str) -> str:
    try:
        # Task implementation
        return process_data(data)
    except Exception as e:
        # Log error for debugging
        print(f"Task failed: {e}")
        raise  # Re-raise to trigger retry
```

## Best practices

### Environment organization

1. **Group related tasks**: Keep tasks with similar dependencies in the same environment
2. **Minimize environment dependencies**: Only declare necessary `depends_on` relationships
3. **Use descriptive names**: Choose clear, descriptive names for environments and tasks

### Workflow design

1. **Keep tasks focused**: Each task should have a single, well-defined responsibility
2. **Use appropriate parallelism**: Leverage `asyncio.gather()` for independent parallel tasks
3. **Handle errors gracefully**: Implement proper error handling and retry strategies

### Deployment strategy

1. **Version your deployments**: Use semantic versioning for production deployments
2. **Test locally first**: Always test workflows locally before deploying
3. **Use dry-run**: Verify deployments with `--dryrun` before actual deployment

### Resource management

```python
# Configure appropriate resources for different task types
cpu_intensive_env = flyte.TaskEnvironment(
    name="cpu_tasks",
    resources=flyte.Resources(cpu="8", memory="16Gi")
)

gpu_env = flyte.TaskEnvironment(
    name="gpu_tasks",
    resources=flyte.Resources(cpu="4", memory="32Gi", gpu="1")
)

memory_intensive_env = flyte.TaskEnvironment(
    name="memory_tasks",
    resources=flyte.Resources(cpu="2", memory="64Gi")
)
```

This comprehensive guide covers the fundamental patterns for deploying and running workflows in Flyte v2. The key principle is that everything revolves around Task Environments which group related tasks and define their execution context, making workflows more maintainable and scalable.

