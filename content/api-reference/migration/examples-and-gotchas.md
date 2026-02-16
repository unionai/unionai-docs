---
title: Examples and common gotchas
weight: 8
variants: +flyte +serverless +byoc +selfmanaged
---

# Examples and common gotchas

## Complete migration examples

### Example 1: Simple ML pipeline

{{< tabs "migration-example-ml" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import task, workflow, ImageSpec, Resources, current_context
from flytekit.types.file import FlyteFile
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

image = ImageSpec(
    name="ml-image",
    packages=["pandas", "scikit-learn", "joblib", "pyarrow"],
    builder="union",
)

@task(
    container_image=image,
    requests=Resources(cpu="2", mem="4Gi"),
    cache=True,
    cache_version="1.1",
)
def load_data() -> pd.DataFrame:
    CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    return pd.read_csv(CSV_URL)

@task(container_image=image)
def train_model(data: pd.DataFrame) -> FlyteFile:
    model = RandomForestClassifier()
    X = data.drop("species", axis=1)
    y = data["species"]
    model.fit(X, y)

    model_path = os.path.join(current_context().working_directory, "model.joblib")
    joblib.dump(model, model_path)
    return FlyteFile(path=model_path)

@task(container_image=image)
def evaluate(model_file: FlyteFile, data: pd.DataFrame) -> float:
    model = joblib.load(model_file.download())
    X = data.drop("species", axis=1)
    y = data["species"]
    return float(model.score(X, y))

@workflow
def ml_pipeline() -> float:
    data = load_data()
    model = train_model(data=data)
    score = evaluate(model_file=model, data=data)
    return score
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
import os
import joblib
import pandas as pd
import flyte
from flyte import TaskEnvironment, Resources, Image
from flyte.io import File
from sklearn.ensemble import RandomForestClassifier

# 1. Define the Image using the fluent builder API
image = (
    Image.from_debian_base(
        name="ml-image",
        python_version=(3, 11),
    )
    .with_pip_packages("pandas", "scikit-learn", "joblib", "pyarrow")
)

# 2. Define the TaskEnvironment
env = TaskEnvironment(
    name="ml_env",
    image=image,
    resources=Resources(cpu="2", memory="4Gi"),
    cache="auto",
)

@env.task
async def load_data() -> pd.DataFrame:
    CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    return pd.read_csv(CSV_URL)

@env.task
async def train_model(data: pd.DataFrame) -> File:
    model = RandomForestClassifier()
    X = data.drop("species", axis=1)
    y = data["species"]
    model.fit(X, y)

    root_dir = os.getcwd()
    model_path = os.path.join(root_dir, "model.joblib")
    joblib.dump(model, model_path)
    return await File.from_local(model_path)

@env.task
async def evaluate(model_file: File, data: pd.DataFrame) -> float:
    local_path = await model_file.download()
    model = joblib.load(local_path)
    X = data.drop("species", axis=1)
    y = data["species"]
    return float(model.score(X, y))

# 3. The workflow is now just an orchestrating task
@env.task
async def ml_pipeline() -> float:
    data = await load_data()
    model = await train_model(data)
    score = await evaluate(model, data)
    return score
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Example 2: Parallel processing with map_task

{{< tabs "migration-example-parallel" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import task, workflow, map_task, dynamic
from functools import partial

@task(cache=True, cache_version="1.0")
def get_chunks(n: int) -> list[int]:
    return list(range(n))

@task(cache=True, cache_version="1.0")
def process_chunk(chunk_id: int, multiplier: int) -> int:
    return chunk_id * multiplier

@workflow
def parallel_pipeline(n: int, multiplier: int) -> list[int]:
    chunk_ids = get_chunks(n)
    results = map_task(
        partial(process_chunk, multiplier=multiplier),
        concurrency=10,
    )(chunk_id=chunk_ids)
    return results
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2 Sync" >}}
{{< markdown >}}
```python
from functools import partial
import flyte

env = flyte.TaskEnvironment(name="parallel_env", cache="auto")

@env.task
def process_chunk(chunk_id: int, multiplier: int) -> int:
    return chunk_id * multiplier

@env.task
def main(n: int, multiplier: int) -> list[int]:
    chunk_ids = list(range(n))
    bound_task = partial(process_chunk, multiplier=multiplier)
    results = list(flyte.map(bound_task, chunk_ids, concurrency=10))
    return results
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2 Async" >}}
{{< markdown >}}
```python
import asyncio
import flyte

env = flyte.TaskEnvironment(name="parallel_env", cache="auto")

@env.task
async def process_chunk(chunk_id: int, multiplier: int) -> int:
    return chunk_id * multiplier

@env.task
async def main(n: int, multiplier: int) -> list[int]:
    chunk_ids = list(range(n))
    sem = asyncio.Semaphore(10)

    async def throttled_task(cid):
        async with sem:
            return await process_chunk(cid, multiplier)

    tasks = [throttled_task(cid) for cid in chunk_ids]
    results = await asyncio.gather(*tasks)
    return list(results)
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Common gotchas

### 1. current_context() is replaced

```python
# Flyte 1
ctx = flytekit.current_context()
secret = ctx.secrets.get(key="mykey", group="mygroup")
working_dir = ctx.working_directory
execution_id = ctx.execution_id

# Flyte 2 - Secrets via environment variables
secret = os.environ["MYGROUP_MYKEY"]

# Flyte 2 - Context via flyte.ctx()
ctx = flyte.ctx()
```

### 2. Workflow >> ordering notation is gone

```python
# Flyte 1: Using >> to indicate ordering
@workflow
def my_workflow():
    t1_result = task1()
    t2_result = task2()
    t1_result >> t2_result
    return t2_result

# Flyte 2: Sequential calls are naturally ordered (sync)
@env.task
def main():
    t1_result = task1()  # Runs first
    t2_result = task2()  # Runs second
    return t2_result

# Flyte 2: For async, use await to sequence
@env.task
async def main():
    t1_result = await task1()  # Runs first
    t2_result = await task2()  # Runs second
    return t2_result
```

### 3. flyte.map returns a generator

```python
# Flyte 1: map_task returns list directly
results = map_task(my_task)(items=my_list)

# Flyte 2: flyte.map returns generator - must convert to list
results = list(flyte.map(my_task, my_list))  # Add list()!

# Flyte 2 async: Use asyncio.gather for async parallel execution
tasks = [my_task(item) for item in my_list]
results = await asyncio.gather(*tasks)
```

### 4. Image configuration location

```python
# Flyte 1: Image per task
@task(container_image=my_image)
def task1(): ...

@task(container_image=my_image)  # Repeated
def task2(): ...

# Flyte 2: Image at TaskEnvironment level (DRY)
env = flyte.TaskEnvironment(name="my_env", image=my_image)

@env.task
def task1(): ...  # Uses env's image

@env.task
def task2(): ...  # Uses env's image
```

### 5. Resource configuration

```python
# Flyte 1: Resources per task
@task(requests=Resources(cpu="1"), limits=Resources(cpu="2"))
def my_task(): ...

# Flyte 2: Resources at TaskEnvironment level
env = flyte.TaskEnvironment(
    name="my_env",
    resources=flyte.Resources(cpu="1"),  # No separate limits
)
```

### 6. Cache version

```python
# Flyte 1: Explicit cache_version required
@task(cache=True, cache_version="1.0")
def my_task(): ...

# Flyte 2: Auto-versioning or explicit
@env.task(cache="auto")  # Auto-versioned
def my_task(): ...

@env.task(cache=flyte.Cache(behavior="auto", version_override="1.0"))
def my_task_explicit(): ...
```

### 7. Entrypoint task naming

```python
# Flyte 1: Workflow is the entrypoint
@workflow
def my_workflow(): ...

# Flyte 2: Use a main() task or any task name
@env.task
def main(): ...  # Common convention

# Run with: flyte run my_module.py main
```

### 8. Memory parameter name

```python
# Flyte 1
Resources(mem="2Gi")

# Flyte 2
flyte.Resources(memory="2Gi")  # Note: "memory" not "mem"
```

### 9. Type annotations

```python
# Flyte 1: Strict about type annotations
@task
def my_task(x: int) -> dict:  # Would fail, need dict[str, int]
    return {"a": x}

# Flyte 2: More lenient
@env.task
def my_task(x: int) -> dict:  # Works, v2 will pickle untyped I/O
    return {"a": x}
```

## Quick reference cheat sheet

```python
# FLYTE 2 MINIMAL TEMPLATE
import flyte
import asyncio

# 1. Define image
image = (
    flyte.Image.from_debian_base(python_version=(3, 11))
    .with_pip_packages("pandas", "numpy")
)

# 2. Create TaskEnvironment
env = flyte.TaskEnvironment(
    name="my_env",
    image=image,
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)

# 3. Define tasks
@env.task
async def process(x: int) -> int:
    return x * 2

# 4. Define main entrypoint
@env.task
async def main(items: list[int]) -> list[int]:
    tasks = [process(x) for x in items]
    results = await asyncio.gather(*tasks)
    return list(results)

# 5. Run
if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(main, items=[1, 2, 3, 4, 5])
    run.wait()
```

```bash
# CLI COMMANDS
flyte run my_module.py main --items '[1,2,3,4,5]'
flyte run --local my_module.py main --items '[1,2,3,4,5]'
flyte deploy my_module.py my_env
```
