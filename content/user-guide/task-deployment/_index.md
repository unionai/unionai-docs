---
title: Task deployment and run
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Task deployment and run

You have seen how to configure and build the tasks that compose your project.
In this section we will explain how to deploy those tasks to the Flyte backend and execute them.

## Deployment

In Flyte, you move your code from your local machine to your Flyte backend by *deploying* the `TaskEnvironment`s that contain your tasks.

For example, let's say you have the following task environment and task defined in a file called `my_example.py`:

```python
# my_example.py

import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def my_task(name: str) -> str:
    return f"Hello, {name}!"
```

Assuming you have a [valid Flyte configuration]() (a `config.yaml` that points to your Flyte backend and includes a default project and domain)
and the [`flyte` package installed]() in your prevailing Python `venv`, then you can deploy your `my_env` task environment like this:

```bash
flyte deploy my_example.py env
```

This command triggers a sophisticated sequence of operations on your local machine before communicating with the Flyte backend. Here's exactly what happens locally:

#### Local Processing Steps

**1. CLI Command Processing and Module Loading**

The Flyte CLI parses your command and loads your Python file as a module:

```python
# Internally, Flyte does something equivalent to:
spec = importlib.util.spec_from_file_location("my_example", "my_example.py")
module = importlib.util.module_from_spec(spec)
sys.modules["my_example"] = module
spec.loader.exec_module(module)  # This executes your Python code
```

Your `my_example.py` file is executed, which creates the `TaskEnvironment` and registers tasks with the `@env.task` decorator. The system then discovers all `Environment` objects in the loaded module and extracts the specific environment variable `env` from the module's namespace.

**2. Environment and Task Analysis**

The system performs comprehensive analysis:
- Recursively discovers all environments and their dependencies
- Identifies all tasks decorated with `@env.task`
- Extracts task metadata: parameter types, return types, resource requirements
- Builds dependency graphs between environments
- Serializes each task into Flyte's protobuf format (`TaskTemplate`)

**3. Code Bundle Creation**

This is a critical step that packages your code for deployment:

```python
# Determines which files to include based on copy_style (default: "loaded_modules")
files_to_bundle = []
if copy_style == "loaded_modules":
    # Scans sys.modules for modules loaded from your source directory
    for module in sys.modules.values():
        if module.__file__ and is_in_source_directory(module.__file__):
            files_to_bundle.append(module.__file__)
elif copy_style == "all":
    # Includes all files in your project directory
    files_to_bundle = glob.glob("**/*.py", recursive=True)
```

The process:
- Creates a temporary directory
- Copies all relevant Python files into the temporary directory
- Creates a compressed tar.gz archive of your code
- Computes an MD5 hash of the bundle for versioning

**4. Image Building (if needed)**

If your `TaskEnvironment` specifies custom images:
- Docker images are built locally using your specified `Image` configuration
- Images are tagged and pushed to the configured container registry
- Image URIs are cached and referenced in task templates

**5. Backend Communication and Data Transfer**

Once local processing is complete, the CLI communicates with the backend:

*Code Bundle Upload:*
```python
# Requests a signed upload URL from the Flyte backend
resp = await client.dataproxy_service.CreateUploadLocation(
    CreateUploadLocationRequest(
        project=project,
        domain=domain,
        content_md5=md5_hash,
        filename="code_bundle.tgz"
    )
)

# Uploads your code bundle to cloud storage (S3, GCS, etc.)
await upload_file_to_signed_url(bundle_path, resp.signed_url)
```

*Task Registration:*
```python
# Registers each task with the Flyte backend
await client.task_service.DeployTask(
    DeployTaskRequest(
        task_spec=task_template,  # Your serialized task metadata
        code_bundle_uri=uploaded_bundle_uri,
        image_uri=built_image_uri
    )
)
```

#### What Gets Sent vs. What Stays Local

**Uploaded to Backend:**
- **Code Bundle**: Compressed tar.gz archive of your Python code
- **Task Templates**: Serialized task metadata (interfaces, configurations)
- **Container Images**: Pushed to configured container registry
- **Resource Specifications**: CPU, memory, GPU requirements
- **Environment Configuration**: Dependencies, secrets, environment variables

**Processed Locally (Not Uploaded):**
- Raw Python source file execution
- Module loading and dependency discovery
- Local environment state and temporary files
- Build artifacts and intermediate files

**Important**: Your Python functions are never directly transmitted as source code. Instead, they're packaged into bundles, uploaded to cloud storage, and referenced by the backend for later execution.

#### Fast Registration Architecture

The deployment uses Flyte's "fast registration" architecture:
- Your Python code is uploaded as a bundle but **not baked into container images**
- At runtime, a pre-built container image starts up
- Your code bundle is downloaded from storage into the running container
- The specific task function executes within that container context

This separation enables rapid iteration without rebuilding Docker images for every code change, allowing for:
- Code updates without image rebuilds
- Running different code versions with the same base image
- Sharing images across multiple projects
- Optimized caching and resource usage






### `flyte deploy`













When you run `flyte deploy my_example.py env` on your local machine, the task environment itself is what gets deployed to the backend. Here's what happens step by step:

### 1. Code Analysis & Bundling

The Flyte CLI scans your Python file (`my_example.py`) to identify all tasks decorated with `@env.task`. Your Python source code is then bundled and uploaded to the backend's **artifact store** (such as S3, GCS, or other cloud storage).

### 2. Container Image Building

The container image for the task environment is built and pushed to the configured container registry (or retrieved from cache if it already exists). **Importantly**, the container image includes:
- Python runtime environment.
- Flyte SDK and dependencies.
- All dependencies specified in the environment (Python packages, system packages, etc.).
- **But NOT the task code itself**. Your actual Python functions remain separate in the artifact store.

### 3. Task Registration

For each `@env.task` function found in your file, Flyte creates a **TaskTemplate** and registers it with the backend. This includes:
- Task metadata (name, interface, parameter types).
- Reference to the container image.
- Reference to the code bundle location in the artifact store.
- Resource specifications (CPU, memory, GPU requirements).
- Execution policies (retries, timeouts, caching, etc.).

### 4. Backend Registration

All of these entities are registered in the Flyte backend database, making the task environment and its individual tasks available for execution. The backend now knows:
- What container image to use for each task.
- Where to find your task code (artifact store location).
- How to execute each task with the proper configuration.
- Task interfaces and dependencies.

### 5. Runtime Execution

When a task is later executed via `flyte.run()`:

- The **container image** is used to spin up a Kubernetes pod.
- The **resource specification** is used to assign the container to the correct hardware and allocate appropriate resources.
- The **Flyte agent** downloads your task code bundle from the artifact store and injects it into the running container.
- Your Python function executes with the `TaskTemplate` configuration.

> [!NOTE]
> If the task environment is [reusable](), then a new container will not be spun up on each task invocation,
> instead, the task code bundle is injected into an existing container instance.

#### About "fast registration"

The injection of the task code into the pre-built container at runtime is a key design feature of Flyte.
It is sometimes referred to as "fast registration". It allows for rapid iteration and deployment of tasks without needing to rebuild container images for every code change.
This separation of container images and task code enables:
- Code updates without rebuilding images.
- Running different versions of code with the same base image.
- Sharing images across multiple projects.
- Optimized caching and resource usage.

However, you can also choose to bake your code directly into the container image if desired. See [XXX]() for details.

### flyte deploy

#### CLI

You can deploy a task environment from the command line using the `flyte deploy` command:

```bash
flyte deploy <source_file_path> <variable_of_task_environment>
```

For example, let's say you have a file `my_example.py` that defines a task environment and assigns it to the variable `env`, like this:

```python
# my_example.py
import flyte
env = flyte.TaskEnvironment(name="my_env")

@env.task
async def my_task(name: str) -> str:
    return f"Hello, {name}!"
```

You can deploy the `my_env` task environment using:

```bash
flyte deploy my_example.py env
```

Note that you specify the variable name of the task environment (`env`), not the task name (`my_env`).

#### SDK

You can also deploy a task environment programmatically using the `flyte.deploy()` function:

```python
# my_example.py
import flyte
env = flyte.TaskEnvironment(name="my_env")

@env.task
async def my_task(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    flyte.init_from_config()
    deployment = flyte.deploy(env)
    print(deployment[0].summary_repr())
```


[DONE TO HERE]()


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












## flyte run




- **Run**: Executes a specific task on the backend.
If a local source file and task name are specified, then the task environment of that task is first deployed (see above) and the task is run on the backend (this is a shortcut for deploying and running in one step).
Alternatively, you can run a previously deployed task directly on the backend (without redeploying).
These functionalities are provided by the CLI command `flyte run` and the SDK function `flyte.run()`.

Previously, in [Getting started](../getting-started/) we used the `flyte run` command to both deploy and run our example task.
In this section we will take a closer look at both deployment and run, starting with deployment.


In [Getting started](../getting-started/) we introduced the [`flyte run` CLI command]() and its [SDK equivalent `flyte.run()`]().
Here we will take a closer look at how they work.

The `run` command runs a specified task. It can do this in three ways: by deploying to the backen and running there, by running locally, or by running a previously deployed task on the backend.

### Deploy and run in one step

#### CLI

For a task that has not yet been deployed, `flyte run` automatically deploys the necessary task environment and then runs the specified task

```bash
flyte run
    <source_file_path>
    <task_name>
    [--<argument_1> <value_1> ...]
```

* `source_file_path`: Path to the Python file containing the task definition.
* `task_name`: Name of the task function to run.
* `[--<argument_1> <value_1> ...]`: Argument list. The names of the arguments match the task function parameters, with a `--` prefix.

Concretely, this might look like:

```bash
flyte run workflows/data_pipeline.py process_data --input_path "/data/raw" --batch_size 100
```

#### SDK

The programmatic equivalent of this is `flyte.run()`:

```python
r = flyte.run(
        task_name,          # Name of the task function
        argument_1=value_1, # Argument list
        ...
)
# Returns Union[R, Run]
```

More concretely:

```python
r = flyte.run(
    process_data,
    input_path="/data/raw",
    batch_size=100
)
```

### Local run

You can run a task on your local machine without deploying it to the backend.
On the command line, use the `--local` flag:

```bash
flyte run
    --local
    <source_file_path>
    <task_function>
    [ --<argument_1> <value_1>][...]
```

Concretely, this might look like:

```bash
flyte run --local workflows/data_pipeline.py process_data --input_path "/data/raw" --batch_size 100
```

In Python, local execution is determined by the absence of a configured client or by explicitly using `with_runcontext(mode="local")`:

If you do not have a configured Flyte client, `flyte.run()` defaults to local execution. For example:

```python
# No flyte.init_from_config() (or similar)
r = flyte.run(
        <task_function>,
        <argument_1>=<value_1>,[...],
    )
```

More concretely:

```python
# No flyte.init_from_config() (or similar)
r = flyte.with_runcontext(mode="local").run(my_task, name="World")
```

If a Flyte client is configured, you can still force local execution using `with_runcontext(mode="local")`:

```python
flyte.init_from_config()
flyte.with_runcontext(mode="local")
    .run(
        <task_function>,
        <argument_1>=<value_1>, ...
    )
```

More concretely:

```python
flyte.init_from_config()
r = flyte.with_runcontext(mode="local").run(my_task, name="World")
```





### Run a previously deployed task

For a task that has already been deployed, you can use the `flyte run` CLI command with the `deployed-task` sub-command to run the specified task directly:

```bash
flyte run
    deployed-task
    <task_name>
    [ --<argument_1> <value_1>]
    [...]
    [--<argument_n> <value_n>]
```

In Python, you can run a previously deployed task by obtaining a reference to it using `flyte.remote.Task.get()` and then invoking it with `flyte.run()`:

[TODO: simplify the example below and refer to a more detailed section elsewhere on rtemote funcionality]()
]
```python
import flyte

# Initialize your Flyte client
flyte.init_from_config()

# Get a reference to a deployed task by name and version
deployed_task = flyte.remote.Task.get(
    "my_env.my_task",
    version="v1.0.0"
)

# Or get the latest version
deployed_task = flyte.remote.Task.get(
    "my_env.my_task",
    auto_version="latest"
)

# Run the deployed task
result = flyte.run(
    deployed_task,
    arg1="value1",
    arg2="value2"
)

print(f"Task URL: {result.url}")
print(f"Run name: {result.name}")

# Wait for completion
result.wait()
```

### Additonal CLI flags

When using the `flyte run` command, you can specify additional flags:



If your [configuration specifies default
project and domain values](), you can omit the > `--project` and `--domain` flags.

* For a task that have already been deployed (it already exists on the backend), it simply runs the task directly.

```bash
flyte run
    --project <project-name>
    --domain development
    hello.py
    my_task
    --arg1 value1
    --arg2 value2
```


* For tasks that have not yet been deployed, it automatically deploys the necessary task environments and then runs the specified task.


allows you to quickly deploy and execute a specific task or workflow from your local machine without needing to manually deploy the task environments first.


you can use the CLI to deploy and run your code in one step with `flyte run`

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

