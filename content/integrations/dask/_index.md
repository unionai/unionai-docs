---
title: Dask
weight: 1
variants: +flyte +union
sidebar_expanded: false
---

# Dask

The Dask plugin lets you run [Dask](https://www.dask.org/) jobs natively on Kubernetes. Flyte provisions a transient Dask cluster for each task execution using the [Dask Kubernetes Operator](https://kubernetes.dask.org/en/latest/operator.html) and tears it down on completion.

## When to use this plugin

- Parallel Python workloads that outgrow a single machine
- Distributed DataFrame operations on large datasets
- Workloads that use Dask's task scheduler for arbitrary computation graphs
- Jobs that need to scale NumPy, pandas, or scikit-learn workflows across multiple nodes

## Installation

```bash
pip install flyteplugins-dask
```

Your task image must also include the Dask distributed scheduler:

```python
image = flyte.Image.from_debian_base(name="dask").with_pip_packages("flyteplugins-dask")
```

## Configuration

Create a `Dask` configuration and pass it as `plugin_config` to a `TaskEnvironment`:

```python
from flyteplugins.dask import Dask, Scheduler, WorkerGroup

dask_config = Dask(
    scheduler=Scheduler(),
    workers=WorkerGroup(number_of_workers=4),
)

dask_env = flyte.TaskEnvironment(
    name="dask_env",
    plugin_config=dask_config,
    image=image,
)
```

### `Dask` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `scheduler` | `Scheduler` | Scheduler pod configuration (defaults to `Scheduler()`) |
| `workers` | `WorkerGroup` | Worker group configuration (defaults to `WorkerGroup()`) |

### `Scheduler` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `image` | `str` | Custom scheduler image (must include `dask[distributed]`) |
| `resources` | `Resources` | Resource requests for the scheduler pod |

### `WorkerGroup` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `number_of_workers` | `int` | Number of worker pods (default: `1`) |
| `image` | `str` | Custom worker image (must include `dask[distributed]`) |
| `resources` | `Resources` | Resource requests per worker pod |

> [!NOTE]
> The scheduler and all workers should use the same Python environment to avoid serialization issues.

### Accessing the Dask client

Inside a Dask task, create a `distributed.Client()` with no arguments. It automatically connects to the provisioned cluster:

```python
from distributed import Client

@dask_env.task
async def my_dask_task(n: int) -> list:
    client = Client()
    futures = client.map(lambda x: x + 1, range(n))
    return client.gather(futures)
```

## Example

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/dask/dask_example.py" lang="python" >}}

## API reference

See the [Dask API reference](../../api-reference/integrations/dask/_index) for full details.
