---
title: Remote tasks
weight: 110
variants: +flyte +serverless +byoc +selfmanaged
---

# Remote tasks

Remote tasks let you use previously deployed tasks without importing their code or dependencies. This enables teams to share and reuse tasks without managing complex dependency chains or container images.

## Prerequisites

Remote tasks must be deployed before you can use them. See the [task deployment guide](../task-deployment) for details.

## Basic usage

Use `flyte.remote.Task.get()` to reference a deployed task:

```python
import flyte
import flyte.remote

env = flyte.TaskEnvironment(name="my_env")

# Get the latest version of a deployed task
data_processor = flyte.remote.Task.get(
    "data_team.spark_analyzer",
    auto_version="latest"
)

# Use it in your task
@env.task
async def my_task(data_path: str) -> flyte.io.DataFrame:
    # Call the reference task like any other task
    result = await data_processor(input_path=data_path)
    return result
```

You can run this directly without deploying it:

```bash
flyte run my_workflow.py my_task --data_path s3://my-bucket/data.parquet
```

## Understanding lazy loading

Remote tasks use **lazy loading** to keep module imports fast and enable flexible client configuration. When you call `flyte.remote.Task.get()`, it returns a lazy reference that doesn't actually fetch the task from the server until the first invocation.

### When tasks are fetched

The remote task is fetched from the server only when:

- You call `flyte.run()` with the task
- You call `flyte.deploy()` with code that uses the task
- You invoke the task with the `()` operator inside another task
- You explicitly call `.fetch()` on the lazy reference

```python
import flyte.remote

# This does NOT make a network call - returns a lazy reference
data_processor = flyte.remote.Task.get(
    "data_team.spark_analyzer",
    auto_version="latest"
)

# The task is fetched here when you invoke it
run = flyte.run(data_processor, input_path="s3://my-bucket/data.parquet")
```

### Benefits of lazy loading

**Fast module loading**: Since no network calls are made during import, your Python modules load quickly even when referencing many remote tasks.

**Late binding**: You can call `flyte.init()` after importing remote tasks, and the correct client will be bound when the task is actually invoked:

```python
import flyte
import flyte.remote

# Load remote task reference at module level
data_processor = flyte.remote.Task.get(
    "data_team.spark_analyzer",
    auto_version="latest"
)

# Initialize the client later
flyte.init_from_config()

# The task uses the client configured above
run = flyte.run(data_processor, input_path="s3://data.parquet")
```

### Error handling

Because of lazy loading, if a referenced task doesn't exist, you won't get an error when calling `get()`. Instead, the error occurs during invocation, raising a `flyte.errors.ReferenceTaskError`:

```python
import flyte
import flyte.remote
import flyte.errors

# This succeeds even if the task doesn't exist
data_processor = flyte.remote.Task.get(
    "nonexistent.task",
    auto_version="latest"
)

try:
    # Error occurs here during invocation
    run = flyte.run(data_processor, input_path="s3://data.parquet")
except flyte.errors.ReferenceTaskError as e:
    print(f"Task not found or invocation failed: {e}")
    # Handle the error - perhaps use a fallback task
    # or notify the user that the task needs to be deployed
```

You can also catch errors when using remote tasks within other tasks:

```python
@env.task
async def pipeline_with_fallback(data_path: str) -> dict:
    try:
        # Try to use the remote task
        result = await data_processor(input_path=data_path)
        return {"status": "success", "result": result}
    except flyte.errors.ReferenceTaskError as e:
        # Fallback to local processing
        print(f"Remote task failed: {e}, using local fallback")
        return {"status": "fallback", "result": local_process(data_path)}
```

### Eager fetching with `fetch()`

While lazy loading is convenient, you can explicitly fetch a task upfront using the `fetch()` method. This is useful for:

- **Catching errors early**: Validate that the task exists before execution starts
- **Caching**: Avoid the network call on first invocation when running multiple times
- **Service initialization**: Pre-load tasks when your service starts

```python
import flyte
import flyte.remote
import flyte.errors

# Get the lazy reference
data_processor = flyte.remote.Task.get(
    "data_team.spark_analyzer",
    auto_version="latest"
)

try:
    # Eagerly fetch the task details
    task_details = data_processor.fetch()

    # Now the task is cached - subsequent calls won't hit the remote service
    # You can pass either the original reference or task_details to flyte.run
    run1 = flyte.run(data_processor, input_path="s3://data1.parquet")
    run2 = flyte.run(task_details, input_path="s3://data2.parquet")

except flyte.errors.ReferenceTaskError as e:
    print(f"Task validation failed at startup: {e}")
    # Handle the error before any execution attempts
```

For async contexts, use `await fetch.aio()`:

```python
import flyte.remote

async def initialize_service():
    processor_ref = flyte.remote.Task.get(
        "data_team.spark_analyzer",
        auto_version="latest"
    )

    try:
        # Fetch asynchronously
        task_details = await processor_ref.fetch.aio()
        print(f"Task {task_details.name} loaded successfully")
        return processor_ref  # Return the cached reference
    except flyte.errors.ReferenceTaskError as e:
        print(f"Failed to load task: {e}")
        raise

# Initialize once at service startup
cached_processor = None

async def startup():
    global cached_processor
    cached_processor = await initialize_service()

# Later in your service
async def process_request(data_path: str):
    # The task is already cached from initialization
    # No network call on first invocation
    run = flyte.run(cached_processor, input_path=data_path)
    return run
```

**When to use eager fetching**:

- **Service startup**: Fetch all remote tasks during initialization to validate they exist and cache them
- **Multiple invocations**: If you'll invoke the same task many times, fetch once to cache it
- **Fail-fast validation**: Catch configuration errors before execution begins

**When lazy loading is better**:

- **Single-use tasks**: If you only invoke the task once, lazy loading is simpler
- **Import-time overhead**: Keep imports fast by deferring network calls
- **Conditional usage**: If the task may not be needed, don't fetch it upfront

### Module-level vs dynamic loading

**Module-level loading (recommended)**: Load remote tasks at the module level for cleaner, more maintainable code:

```python
import flyte.remote

# Module-level - clear and maintainable
data_processor = flyte.remote.Task.get(
    "data_team.spark_analyzer",
    auto_version="latest"
)

@env.task
async def my_task(data_path: str):
    return await data_processor(input_path=data_path)
```

**Dynamic loading**: You can also load remote tasks dynamically within a task if needed:

```python
@env.task
async def dynamic_pipeline(task_name: str, data_path: str):
    # Load the task based on runtime parameters
    processor = flyte.remote.Task.get(
        f"data_team.{task_name}",
        auto_version="latest"
    )

    try:
        result = await processor(input_path=data_path)
        return result
    except flyte.errors.ReferenceTaskError as e:
        raise ValueError(f"Task {task_name} not found: {e}")
```

## Complete example

This example shows how different teams can collaborate using remote tasks.

### Team A: Spark environment

Team A maintains Spark-based data processing tasks:

```python
# spark_env.py
from dataclasses import dataclass
import flyte

env = flyte.TaskEnvironment(name="spark_env")

@dataclass
class AnalysisResult:
    mean_value: float
    std_dev: float

@env.task
async def analyze_data(data_path: str) -> AnalysisResult:
    # Spark code here (not shown)
    return AnalysisResult(mean_value=42.5, std_dev=3.2)

@env.task
async def compute_score(result: AnalysisResult) -> float:
    # More Spark processing
    return result.mean_value / result.std_dev
```

Deploy the Spark environment:

```bash
flyte deploy spark_env/
```

### Team B: ML environment

Team B maintains PyTorch-based ML tasks:

```python
# ml_env.py
from pydantic import BaseModel
import flyte

env = flyte.TaskEnvironment(name="ml_env")

class PredictionRequest(BaseModel):
    feature_x: float
    feature_y: float

class Prediction(BaseModel):
    score: float
    confidence: float
    model_version: str

@env.task
async def run_inference(request: PredictionRequest) -> Prediction:
    # PyTorch model inference (not shown)
    return Prediction(
        score=request.feature_x * 2.5,
        confidence=0.95,
        model_version="v2.1"
    )
```

Deploy the ML environment:

```bash
flyte deploy ml_env/
```

### Team C: Orchestration

Team C builds a workflow using remote tasks from both teams without needing Spark or PyTorch dependencies:

```python
# orchestration_env.py
import flyte.remote

env = flyte.TaskEnvironment(name="orchestration")

# Reference tasks from other teams
analyze_data = flyte.remote.Task.get(
    "spark_env.analyze_data",
    auto_version="latest"
)

compute_score = flyte.remote.Task.get(
    "spark_env.compute_score",
    auto_version="latest"
)

run_inference = flyte.remote.Task.get(
    "ml_env.run_inference",
    auto_version="latest"
)

@env.task
async def orchestrate_pipeline(data_path: str) -> float:
    # Use Spark tasks without Spark dependencies
    analysis = await analyze_data(data_path=data_path)

    # Access attributes from the result
    # (Flyte creates a fake type that allows attribute access)
    print(f"Analysis: mean={analysis.mean_value}, std={analysis.std_dev}")

    data_score = await compute_score(result=analysis)

    # Use ML task without PyTorch dependencies
    # Pass Pydantic models as dictionaries
    prediction = await run_inference(
        request={
            "feature_x": analysis.mean_value,
            "feature_y": data_score
        }
    )

    # Access Pydantic model attributes
    print(f"Prediction: {prediction.score} (confidence: {prediction.confidence})")

    return prediction.score
```

Run the orchestration task directly (no deployment needed):

**Using Python API**:
```python
if __name__ == "__main__":
    flyte.init_from_config()

    run = flyte.run(
        orchestrate_pipeline,
        data_path="s3://my-bucket/data.parquet"
    )

    print(f"Execution URL: {run.url}")
    # You can wait for the execution
    run.wait()
    
    # You can then retrieve the outputs
    print(f"Pipeline result: {run.outputs()}")
```

**Using CLI**:
```bash
flyte run orchestration_env.py orchestrate_pipeline --data_path s3://my-bucket/data.parquet
```

## Invoke remote tasks in a script.

You can also run any remote task directly using a script in a similar way
```python
import flyte
import flyte.models
import flyte.remote

flyte.init_from_config()

# Fetch the task
remote_task = flyte.remote.Task.get("package-example.calculate_average", auto_version="latest")

# Create a run, note keyword arguments are required currently. In the future this will accept positional args based on the declaration order, but, we still recommend to use keyword args.
run = flyte.run(remote_task, numbers=[1.0, 2.0, 3.0])

print(f"Execution URL: {run.url}")
# you can view the phase

print(f"Current Phase: {run.phase}")
# You can wait for the execution
run.wait()

# Only available after flyte >= 2.0.0b39
print(f"Current phase: {run.phase}")

# Phases can be compared to
if run.phase == flyte.models.ActionPhase.SUCCEEDED:
    print(f"Run completed!")

# You can then retrieve the outputs
print(f"Pipeline result: {run.outputs()}")
```

## Why use remote tasks?

Remote tasks solve common collaboration and dependency management challenges:

**Cross-team collaboration**: Team A has deployed a Spark task that analyzes large datasets. Team B needs this analysis for their ML pipeline but doesn't want to learn Spark internals, install Spark dependencies, or build Spark-enabled container images. With remote tasks, Team B simply references Team A's deployed task.

**Platform reusability**: Platform teams can create common, reusable tasks (data validation, feature engineering, model serving) that other teams can use without duplicating code or managing complex dependencies.

**Microservices for data workflows**: Remote tasks work like microservices for long-running tasks or agents, enabling secure sharing while maintaining isolation.

## When to use remote tasks

Use remote tasks when you need to:

- Use functionality from another team without their dependencies
- Share common tasks across your organization
- Build reusable platform components
- Avoid dependency conflicts between different parts of your workflow
- Create modular, maintainable data pipelines

## How remote tasks work

### Security model

Remote tasks run in the **caller's project and domain** using the caller's compute resources, but execute with the **callee's service accounts, IAM roles, and secrets**. This ensures:

- Tasks are secure from misuse
- Resource usage is properly attributed
- Authentication and authorization are maintained
- Collaboration remains safe and controlled

### Type system

Remote tasks use Flyte's default types as inputs and outputs. Flyte's type system seamlessly translates data between tasks without requiring the original dependencies:

| Remote Task Type | Flyte Type |
|-------------------|------------|
| DataFrames (`pandas`, `polars`, `spark`, etc.) | `flyte.io.DataFrame` |
| Object store files | `flyte.io.File` |
| Object store directories | `flyte.io.Dir` |
| Pydantic models | Dictionary (Flyte creates a representation) |

Any DataFrame type (pandas, polars, spark) automatically becomes `flyte.io.DataFrame`, allowing seamless data exchange between tasks using different DataFrame libraries. You can also write custom integrations or explore Flyte's plugin system for additional types.

For Pydantic models specifically, you don't need the exact model locally. Pass a dictionary as input, and Flyte will handle the translation.

## Versioning options

Reference tasks support flexible versioning:

**Specific version**:

```python
task = flyte.remote.Task.get(
    "team_a.process_data",
    version="v1.2.3"
)
```

**Latest version** (`auto_version="latest"`):

```python
# Always use the most recently deployed version
task = flyte.remote.Task.get(
    "team_a.process_data",
    auto_version="latest"
)
```

**Current version** (`auto_version="current"`):

```python
# Use the same version as the calling task's deployment
# Useful when all environments deploy with the same version
# Can only be used from within a task context
task = flyte.remote.Task.get(
    "team_a.process_data",
    auto_version="current"
)
```

## Customizing remote tasks

Remote tasks can be customized by overriding various properties without modifying the original deployed task. This allows you to adjust resource requirements, retry strategies, caching behavior, and more based on your specific use case.

### Available overrides

The `override()` method on remote tasks accepts the following parameters:

- **short_name** (`str`): A short name for the task instance
- **resources** (`flyte.Resources`): CPU, memory, GPU, and storage limits
- **retries** (`int | flyte.RetryStrategy`): Number of retries or retry strategy
- **timeout** (`flyte.TimeoutType`): Task execution timeout
- **env_vars** (`Dict[str, str]`): Environment variables to set
- **secrets** (`flyte.SecretRequest`): Secrets to inject
- **max_inline_io_bytes** (`int`): Maximum size for inline IO in bytes
- **cache** (`flyte.Cache`): Cache behavior and settings
- **queue** (`str`): Execution queue to use

### Override examples

**Increase resources for a specific use case**:

```python
import flyte.remote

# Get the base task
data_processor = flyte.remote.Task.get(
    "data_team.spark_analyzer",
    auto_version="latest"
)

# Override with more resources for large dataset processing
large_data_processor = data_processor.override(
    resources=flyte.Resources(
        cpu="16",
        memory="64Gi",
        storage="200Gi"
    )
)

@env.task
async def process_large_dataset(data_path: str):
    # Use the customized version
    return await large_data_processor(input_path=data_path)
```

**Add retries and timeout**:

```python
# Override with retries and timeout for unreliable operations
reliable_processor = data_processor.override(
    retries=3,
    timeout="2h"
)

@env.task
async def robust_pipeline(data_path: str):
    return await reliable_processor(input_path=data_path)
```

**Configure caching**:

```python
# Override cache settings
cached_processor = data_processor.override(
    cache=flyte.Cache(
        behavior="override",
        version_override="v2",
        serialize=True
    )
)
```

**Set environment variables and secrets**:

```python
# Override with custom environment and secrets
custom_processor = data_processor.override(
    env_vars={
        "LOG_LEVEL": "DEBUG",
        "REGION": "us-west-2"
    },
    secrets=flyte.SecretRequest(
        secrets={"api_key": "my-secret-key"}
    )
)
```

**Multiple overrides**:

```python
# Combine multiple overrides
production_processor = data_processor.override(
    short_name="prod_spark_analyzer",
    resources=flyte.Resources(cpu="8", memory="32Gi"),
    retries=5,
    timeout="4h",
    env_vars={"ENV": "production"},
    queue="high-priority"
)

@env.task
async def production_pipeline(data_path: str):
    return await production_processor(input_path=data_path)
```

### Chain overrides

You can chain multiple `override()` calls to incrementally adjust settings:

```python
# Start with base task
processor = flyte.remote.Task.get("data_team.analyzer", auto_version="latest")

# Add resources
processor = processor.override(resources=flyte.Resources(cpu="4", memory="16Gi"))

# Add retries for production
if is_production:
    processor = processor.override(retries=5, timeout="2h")

# Use the customized task
result = await processor(input_path="s3://data.parquet")
```

## Best practices

### 1. Use meaningful task names

Remote tasks are accessed by name, so use clear, descriptive naming:

```python
# Good
customer_segmentation = flyte.remote.Task.get("ml_platform.customer_segmentation")

# Avoid
task1 = flyte.remote.Task.get("team_a.task1")
```

### 2. Document task interfaces

Since remote tasks abstract away implementation details, clear documentation of inputs, outputs, and behavior is essential:

```python
@env.task
async def process_customer_data(
    customer_ids: list[str],
    date_range: tuple[str, str]
) -> flyte.io.DataFrame:
    """
    Process customer data for the specified date range.

    Args:
        customer_ids: List of customer IDs to process
        date_range: Tuple of (start_date, end_date) in YYYY-MM-DD format

    Returns:
        DataFrame with processed customer features
    """
    ...
```

### 3. Prefer module-level loading

Load remote tasks at the module level rather than inside functions for cleaner code:

```python
import flyte.remote

# Good - module level
data_processor = flyte.remote.Task.get("team.processor", auto_version="latest")

@env.task
async def my_task(data: str):
    return await data_processor(input=data)
```

This approach:
- Makes dependencies clear and discoverable
- Reduces code duplication
- Works well with lazy loading (no performance penalty)

Dynamic loading within tasks is also supported when you need runtime flexibility.

### 4. Handle versioning thoughtfully

- Use `auto_version="latest"` during development for rapid iteration
- Use specific versions in production for stability and reproducibility
- Use `auto_version="current"` when coordinating multienvironment deployments

### 5. Deploy remote tasks first

Always deploy the remote tasks before using them. Tasks that reference them can be run directly without deployment:

```bash
# Deploy the Spark environment first
flyte deploy spark_env/

# Deploy the ML environment
flyte deploy ml_env/

# Now you can run the orchestration task directly (no deployment needed)
flyte run orchestration_env.py orchestrate_pipeline
```

If you want to deploy the orchestration task as well (for scheduled runs or to be referenced by other tasks), deploy it after its dependencies:

```bash
flyte deploy orchestration_env/
```

## Limitations

1. **Lazy error detection**: Because of lazy loading, errors about missing or invalid tasks only occur during invocation, not when calling `get()`. You'll receive a `flyte.errors.ReferenceTaskError` if the task doesn't exist or can't be invoked.

2. **Type fidelity**: While Flyte translates types seamlessly, you work with Flyte's representation of Pydantic models, not the exact original types

3. **Deployment order**: Referenced tasks must be deployed before tasks that reference them can be invoked

4. **Context requirement**: Using `auto_version="current"` requires running within a task context

5. **Dictionary inputs**: Pydantic models must be passed as dictionaries, which loses compile-time type checking

6. **No positional arguments**: Remote tasks currently only support keyword arguments (this may change in future versions)

## Next steps

- Learn about [task deployment](../task-deployment)
- Explore [task environments and configuration](../task-configuration)
