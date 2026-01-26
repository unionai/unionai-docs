# Flyte 2 Reference Card

> Condensed reference for LLM context. For full documentation: https://union.ai/docs/v2/byoc/

## What is Flyte 2

Flyte 2 is a workflow orchestration platform for AI/ML pipelines. Key differences from Flyte 1:
- **Pure Python execution** - no `@workflow` decorator, workflows are just tasks calling tasks
- **Async-native** - use `async/await` and `asyncio.gather` for parallelism
- **TaskEnvironment** - container configuration is defined once, shared across tasks

## Quick Setup

### Install
```bash
pip install --pre flyte
```

### Configure
```bash
flyte create config \
    --endpoint my-org.company.com \
    --project my-project \
    --domain development \
    --builder remote  # Use 'local' for OSS Flyte
```

Creates `.flyte/config.yaml`. Check with `flyte get config`.

### Initialize in Python
```python
import flyte
flyte.init_from_config()  # Reads from config file
# or
flyte.init(endpoint="dns:///my-org.company.com", project="my-project", domain="development")
```

## Core Concepts

### TaskEnvironment
Defines the container image and resources for tasks:

```python
import flyte

env = flyte.TaskEnvironment(
    name="my-env",
    image=flyte.Image.from_debian_base().with_pip_packages("pandas", "scikit-learn"),
    limits=flyte.Resources(cpu="2", mem="4Gi"),
)
```

Multiple tasks can share the same environment.

### Tasks
Python functions decorated with `@env.task` run in containers:

```python
@env.task
def process_data(x: int) -> int:
    return x * 2

@env.task
def pipeline(x: int) -> int:
    # Tasks can call other tasks - this is how you build "workflows"
    result = process_data(x)
    return result + 10
```

### Runs and Actions
- **Run**: The complete execution you initiate (e.g., `flyte run script.py pipeline`)
- **Action**: Each individual task execution within a run

### Apps
Long-running services (APIs, inference endpoints):

```python
from flyte.app.extras import FastAPIAppEnvironment
from fastapi import FastAPI

fastapi_app = FastAPI()

@fastapi_app.get("/predict")
def predict(x: int) -> dict:
    return {"result": x * 2}

env = FastAPIAppEnvironment(
    name="my-api",
    app=fastapi_app,
    image=flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn"),
)
```

## Running Tasks

### CLI
```bash
# Run remotely
flyte run script.py task_name --arg1 value1

# Run locally (for testing)
flyte run --local script.py task_name --arg1 value1
```

### Python
```python
flyte.init_from_config()
result = flyte.run(pipeline, x=5)  # Remote execution
# or
result = flyte.with_runcontext(mode="local").run(pipeline, x=5)  # Local
```

## Deployment

### Deploy tasks (register without running)
```bash
flyte deploy script.py task_name
```

### Serve apps
```bash
flyte serve app.py env_name
```

### Python deployment
```python
flyte.deploy(env)  # Deploy task environment
flyte.serve(app_env)  # Serve app (auto-activates)
```

## Data Types

### Files and Directories
```python
from flyte.io import File, Dir

@env.task
def process_file(input_file: File) -> File:
    # input_file.path gives local path after download
    output = File(path="/tmp/output.csv")
    # Write to output.path, return File object
    return output

@env.task
def process_dir(input_dir: Dir) -> Dir:
    # Similar pattern for directories
    return Dir(path="/tmp/output_dir")
```

### DataFrames
```python
from flyte.io import DataFrame
import pandas as pd

@env.task
def process_df(df: DataFrame) -> DataFrame:
    pandas_df = df.to_pandas()
    # Process...
    return DataFrame(pandas_df)
```

Data is passed by reference (stored in object storage), not serialized in memory.

## Parallelism

### Using flyte.map (sync)
```python
@env.task
def process_item(x: int) -> int:
    return x * 2

@env.task
def parallel_pipeline(items: list[int]) -> list[int]:
    return flyte.map(process_item, items)
```

### Using asyncio (async)
```python
import asyncio

@env.task
async def process_item(x: int) -> int:
    return x * 2

@env.task
async def parallel_pipeline(items: list[int]) -> list[int]:
    return await asyncio.gather(*[process_item(x) for x in items])
```

### Calling sync tasks from async
```python
@env.task
def sync_task(x: int) -> int:
    return x * 2

@env.task
async def async_pipeline(items: list[int]) -> list[int]:
    return await asyncio.gather(*[sync_task.aio(x) for x in items])
```

## Resource Configuration

### Basic resources
```python
env = flyte.TaskEnvironment(
    name="gpu-env",
    limits=flyte.Resources(cpu="4", mem="16Gi", gpu="1"),
    requests=flyte.Resources(cpu="2", mem="8Gi"),
)
```

### GPU specification
```python
limits=flyte.Resources(cpu="4", mem="32Gi", gpu="A100:2")  # 2x A100 GPUs
```

### Per-task override
```python
@env.task(limits=flyte.Resources(mem="32Gi"))
def memory_intensive_task(): ...
```

## Caching

Cache task results based on inputs:

```python
@env.task(cache=True, cache_version="v1")
def expensive_computation(x: int) -> int:
    # Only runs once per unique input
    return x * 2
```

## Secrets

### Create a secret
```bash
flyte create secret MY_API_KEY
# Enter value when prompted
```

### Use in task
```python
@env.task(secrets=["MY_API_KEY"])
def call_api() -> str:
    import os
    api_key = os.environ["MY_API_KEY"]
    # Use api_key...
```

## Error Handling

### Try/except with resource retry
```python
@env.task
def robust_pipeline(data: list) -> list:
    try:
        return memory_intensive_task(data)
    except MemoryError:
        # Retry with more resources
        return memory_intensive_task.with_overrides(
            limits=flyte.Resources(mem="64Gi")
        )(data)
```

### Retries and timeouts
```python
@env.task(retries=3, timeout="1h")
def flaky_task(): ...
```

## Traces (Checkpointing)

Fine-grained recovery within tasks:

```python
import flyte

@env.task
def pipeline_with_checkpoints():
    result1 = step1()

    @flyte.trace
    def call_expensive_api(x):
        # This is checkpointed - if task crashes after this,
        # the result is recovered on retry
        return expensive_api_call(x)

    result2 = call_expensive_api(result1)
    return result2
```

## Triggers

### Scheduled execution
```python
env = flyte.TaskEnvironment(
    name="scheduled-env",
    triggers=[
        flyte.Trigger.cron("0 0 * * *")  # Daily at midnight
    ],
)

@env.task
def daily_job(): ...
```

## Reusable Containers (Union only)

Eliminate container startup overhead:

```python
env = flyte.TaskEnvironment(
    name="fast-env",
    container_reuse=flyte.ContainerReuse(
        enable=True,
        max_idle_seconds=300,
    ),
)
```

## Container Images

### Fluent image builder
```python
image = (
    flyte.Image.from_debian_base()
    .with_pip_packages("pandas", "numpy", "scikit-learn")
    .with_apt_packages("libgomp1")
    .with_env({"MY_VAR": "value"})
)
```

### From existing image
```python
image = flyte.Image.from_ref_name("my-registry.com/my-image:latest")
```

### With Dockerfile
```python
image = flyte.Image.from_dockerfile(
    name="my-image",
    dockerfile="./Dockerfile",
    context=".",
)
```

## Apps: FastAPI

```python
from fastapi import FastAPI
from flyte.app.extras import FastAPIAppEnvironment
import flyte

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(x: int) -> dict:
    return {"result": x * 2}

env = FastAPIAppEnvironment(
    name="my-api",
    app=app,
    image=flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn"),
    limits=flyte.Resources(cpu="2", mem="4Gi"),
)

if __name__ == "__main__":
    flyte.init_from_config()
    flyte.serve(env)
```

## Apps: LLM Serving (vLLM)

```python
from flyteplugins.vllm import VLLMAppEnvironment
import flyte

vllm_app = VLLMAppEnvironment(
    name="llm-serving",
    model_hf_path="Qwen/Qwen3-0.6B",
    model_id="qwen",
    resources=flyte.Resources(cpu="4", mem="16Gi", gpu="L40s:1"),
)

if __name__ == "__main__":
    flyte.init_from_config()
    flyte.serve(vllm_app)
```

## Apps: Autoscaling

```python
env = FastAPIAppEnvironment(
    name="scalable-api",
    scaling=flyte.app.Scaling(
        replicas=(0, 10),  # min, max
        scaledown_after=300,  # seconds idle before scale down
    ),
    # ...
)
```

## Remote Tasks

Call previously deployed tasks:

```python
from flyte.remote import Task

@env.task
def pipeline():
    # Get a deployed task
    remote_task = Task.get(name="deployed_task", project="other-project")

    # Run it
    result = remote_task(x=5)
    return result
```

## Key CLI Commands

| Command | Description |
|---------|-------------|
| `flyte run script.py task` | Run task remotely |
| `flyte run --local script.py task` | Run task locally |
| `flyte deploy script.py task` | Deploy/register task |
| `flyte serve script.py env` | Serve an app |
| `flyte get run <id>` | Get run status |
| `flyte get config` | Show current config |
| `flyte create secret NAME` | Create a secret |
| `flyte create config --endpoint URL` | Create config file |

## Important Considerations

### No global state
Each task runs in its own container. Global variables don't persist across tasks.

```python
# DON'T do this - counter won't persist
counter = 0

@env.task
def increment():
    global counter
    counter += 1  # Always starts at 0
```

### Deterministic execution
For recovery to work correctly, task behavior should be deterministic. Avoid:
- Random values without seeding
- Time-dependent branching
- External state that changes between retries

### Driver pod sizing
Parent tasks that call many subtasks need adequate resources to orchestrate:

```python
@env.task(limits=flyte.Resources(cpu="2", mem="4Gi"))  # Size for orchestration
def orchestrator():
    # Kicks off many subtasks
    results = flyte.map(heavy_task, large_list)
    return aggregate(results)
```

### Pass by reference vs value
- `flyte.io.File`, `flyte.io.Dir`, `flyte.io.DataFrame`: Pass by reference (efficient for large data)
- Primitives (`int`, `str`, `list`, etc.): Serialized and passed by value

### Memory with large outputs
If a subtask returns large data (not File/Dir/DataFrame), that data is materialized in the parent:

```python
@env.task
def parent():
    huge_list = subtask_returning_huge_list()  # This loads into parent's memory!
    # Use File or DataFrame for large data instead
```

## Common Patterns

### ETL Pipeline
```python
@env.task
def extract() -> DataFrame:
    return DataFrame(load_from_source())

@env.task
def transform(df: DataFrame) -> DataFrame:
    return DataFrame(process(df.to_pandas()))

@env.task
def load(df: DataFrame) -> None:
    save_to_destination(df.to_pandas())

@env.task
def etl_pipeline():
    raw = extract()
    processed = transform(raw)
    load(processed)
```

### Fan-out / Fan-in
```python
@env.task
async def fan_out_fan_in(items: list[int]) -> int:
    # Fan out
    results = await asyncio.gather(*[process(x) for x in items])
    # Fan in
    return sum(results)
```

### Conditional execution
```python
@env.task
def conditional_pipeline(data: DataFrame) -> DataFrame:
    if len(data.to_pandas()) > 1000:
        return heavy_processing(data)
    else:
        return light_processing(data)
```

### Training + Serving
```python
# Training task
@env.task
def train_model(data: DataFrame) -> File:
    model = train(data.to_pandas())
    model_path = "/tmp/model.pkl"
    save_model(model, model_path)
    return File(path=model_path)

# Serving app that uses training output
from flyte.app import RunOutput

app_env = FastAPIAppEnvironment(
    name="model-server",
    parameters=[
        flyte.app.Parameter(
            name="model_file",
            value=RunOutput(type="file", run_name="training-run-id"),
        )
    ],
    # ...
)
```

## Version Information

- **Flyte 2.0.x** - Current version
- **flyte** package - Python SDK
- **flyte CLI** - Command-line interface

For Union.ai commercial features (reusable containers, cloud image builder), see Union documentation.
