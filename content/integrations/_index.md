---
title: Integrations
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
top_menu: true
sidebar_expanded: true
---

# Integrations

Flyte 2 is designed to be extensible by default. While the core platform covers the most common orchestration needs, many production workloads require specialized infrastructure, external services or execution semantics that go beyond the core runtime.

Flyte 2 exposes these capabilities through integrations.

Under the hood, integrations are implemented using Flyte 2's plugin system, which provides a consistent way to extend the platform without modifying core execution logic.

| Plugin | Description |
| ------ | ----------- |
| [Ray](./flyte-plugins/ray) | Run Ray jobs on your Flyte cluster |
| [Spark](./flyte-plugins/spark) | Run Spark jobs on your Flyte cluster |
| [OpenAI](./flyte-plugins/openai) | Integrate with OpenAI SDKs in your Flyte workflows |
| [Connectors](./flyte-plugins/connectors) | Integrate with external services and platforms |
An integration allows you to declaratively enable new capabilities such as distributed compute frameworks or third-party services without manually managing infrastructure. You specify what you need, and Flyte takes care of how it is provisioned, used and cleaned up.

This page covers:

- The types of integrations Flyte 2 supports today
- How integrations fit into Flyte 2's execution model
- How to use integrations in your tasks
- The integrations are available out of the box

If you need functionality that doesn't exist yet, Flyte 2's plugin system is intentionally open-ended. You can build and register your own integrations using the same architecture described here.

## Integration categories

Flyte 2 integrations generally fall into three broad categories:

1. **Distributed compute**: Provision transient compute clusters to run tasks across multiple nodes, with automatic lifecycle management.
2. **External services**: Enable Flyte to interact with third-party systems such as APIs, platforms, and SaaS services.
3. **Connectors**: Stateless, long‑running services that receive execution requests via gRPC and then submit work to external (or internal) systems.

## Distributed compute

Distributed compute integrations allow tasks to run on dynamically provisioned clusters. These clusters are created just-in-time, scoped to the task execution and torn down automatically when the task completes.

This enables large-scale parallelism without requiring users to operate or maintain long-running infrastructure.

### Supported distributed compute integrations

| Plugin               | Description                                      | Common use cases                                       |
| -------------------- | ------------------------------------------------ | ------------------------------------------------------ |
| [Ray](./ray/_index)         | Provisions Ray clusters via KubeRay              | Distributed Python, ML training, hyperparameter tuning |
| [Spark](./spark/_index)     | Provisions Spark clusters via Spark Operator     | Large-scale data processing, ETL pipelines             |
| [Dask](./dask/_index)       | Provisions Dask clusters via Dask Operator       | Parallel Python workloads, dataframe operations        |
| [PyTorch](./pytorch/_index) | Distributed PyTorch training with elastic launch | Single-node and multi-node training                    |

Each plugin encapsulates:

- Cluster provisioning
- Resource configuration
- Networking and service discovery
- Lifecycle management and teardown

From the task author's perspective, these details are abstracted away.

### How the plugin system works

At a high level, Flyte 2's distributed compute plugin architecture follows a simple and consistent pattern.

#### 1. Registration

Each plugin registers itself with Flyte 2's core plugin registry:

- **`TaskPluginRegistry`**: The central registry for all distributed compute plugins
- Each plugin declares:
  - Its configuration schema
  - How that configuration maps to execution behavior

This registration step makes the plugin discoverable by the runtime.

#### 2. Task environments and plugin configuration

Integrations are activated through a `TaskEnvironment`.

A `TaskEnvironment` bundles:

- A container image
- Execution settings
- A plugin configuration object enabled with `plugin_config`

The plugin configuration describes _what_ infrastructure or integration the task requires.

#### 3. Automatic provisioning and execution

When a task associated with a `TaskEnvironment` runs:

1. Flyte inspects the environment's plugin configuration
2. The plugin provisions the required infrastructure or integration
3. The task executes with access to that capability
4. Flyte cleans up all transient resources after completion

### Example: Using the Dask plugin

Below is a complete example showing how a task gains access to a Dask cluster simply by running inside an environment configured with the Dask plugin.

```python
from flyteplugins.dask import Dask, WorkerGroup
import flyte

# Define the Dask cluster configuration
dask_config = Dask(
    workers=WorkerGroup(number_of_workers=4)
)

# Create a task environment that enables Dask
env = flyte.TaskEnvironment(
    name="dask_env",
    plugin_config=dask_config,
    image=image,
)

# Any task in this environment has access to the Dask cluster
@env.task
async def process_data(data: list) -> list:
    from distributed import Client

    client = Client()  # Automatically connects to the provisioned cluster
    futures = client.map(transform, data)
    return client.gather(futures)
```

When `process_data` executes, Flyte performs the following steps:

1. Provisions a Dask cluster with 4 workers
2. Executes the task with network access to the cluster
3. Tears down the cluster once the task completes

No cluster management logic appears in the task code. The task only expresses intent.

### Key design principle

All distributed compute integrations follow the same mental model:

- You declare the required capability via configuration
- You attach that configuration to a task environment
- Tasks decorated with that environment automatically gain access to the capability

This makes it easy to swap execution backends or introduce distributed compute incrementally without rewriting workflows.

## External services

External service integrations allow Flyte to interact with third-party services in a structured, first-class way.

These integrations typically handle:

- Authentication and credentials
- API lifecycle management
- Standardized interfaces for task authors

### Supported external integration integrations

| Plugin                        | Description                                   | Common use cases                              |
| ----------------------------- | --------------------------------------------- | --------------------------------------------- |
| [OpenAI](./openai)            | Drop-in replacement for OpenAI `FunctionTool` | Agentic workflows                             |
| [Weights and Biases](./wandb/_index) | Weights & Biases integration                  | Experiment tracking and hyperparameter tuning |

## Connectors

Connectors are stateless, long‑running services that receive execution requests via gRPC and then submit work to external (or internal) systems. Each connector runs as its own Kubernetes deployment, and is triggered when a Flyte task of the matching type is executed.

Although they normally run inside the control plane, you can also run connectors locally as long as the required secrets/credentials are present locally. This is useful because connectors are just Python services that can be spawned in‑process.

Connectors are designed to scale horizontally and reduce load on the core Flyte backend because they execute _outside_ the core system. This decoupling makes connectors efficient, resilient, and easy to iterate on. You can even test them locally without modifying backend configuration, which reduces friction during development.

### Supported connectors

| Connector                | Description                                 | Common use cases                         |
| ------------------------ | ------------------------------------------- | ---------------------------------------- |
| [Snowflake](./snowflake/_index) | Run SQL queries on Snowflake asynchronously | Data warehousing, ETL, analytics queries |

### Creating a new connector

If none of the existing connectors meet your needs, you can build your own.

> [!NOTE]
> Connectors communicate via Protobuf, so in theory they can be implemented in any language.
> Today, only **Python** connectors are supported.

### Async connector interface

To implement a new async connector, extend `AsyncConnector` and implement the following methods, all of which must be idempotent:

| Method   | Purpose                                                     |
| -------- | ----------------------------------------------------------- |
| `create` | Launch the external job (via REST, gRPC, SDK, or other API) |
| `get`    | Fetch current job state (return job status or output)       |
| `delete` | Delete / cancel the external job                            |

To test the connector locally, the connector task should inherit from
[AsyncConnectorExecutorMixin](https://github.com/flyteorg/flyte-sdk/blob/1d49299294cd5e15385fe8c48089b3454b7a4cd1/src/flyte/connectors/_connector.py#L206). This mixin simulates how the Flyte 2 system executes asynchronous connector tasks, making it easier to validate your connector implementation before deploying it.

### Example: Model training connector

The following example implements a connector that launches a model training job on an external training service.

```python
import typing
from dataclasses import dataclass

import httpx
from flyte.connectors import AsyncConnector, Resource, ResourceMeta
from flyteidl2.core.execution_pb2 import TaskExecution, TaskLog
from flyteidl2.core.tasks_pb2 import TaskTemplate
from google.protobuf import json_format


@dataclass
class ModelTrainJobMeta(ResourceMeta):
    job_id: str
    endpoint: str


class ModelTrainingConnector(AsyncConnector):
    """
    Example connector that launches a ML model training job on an external training service.

    POST → launch training job
    GET  → poll training progress
    DELETE → cancel training job
    """

    name = "Model Training Connector"
    task_type_name = "external_model_training"
    metadata_type = ModelTrainJobMeta

    async def create(
        self,
        task_template: TaskTemplate,
        inputs: typing.Optional[typing.Dict[str, typing.Any]],
        **kwargs,
    ) -> ModelTrainJobMeta:
        """
        Submit training job via POST.
        Response returns job_id we later use in get().
        """
        custom = json_format.MessageToDict(task_template.custom) if task_template.custom else None
        async with httpx.AsyncClient() as client:
            r = await client.post(
                custom["endpoint"],
                json={"dataset_uri": inputs["dataset_uri"], "epochs": inputs["epochs"]},
            )
        r.raise_for_status()
        return ModelTrainJobMeta(job_id=r.json()["job_id"], endpoint=custom["endpoint"])

    async def get(self, resource_meta: ModelTrainJobMeta, **kwargs) -> Resource:
        """
        Poll external API until training job finishes.
        Must be safe to call repeatedly.
        """
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{resource_meta.endpoint}/{resource_meta.job_id}")

        data = r.json()

        if data["status"] == "finished":
            return Resource(
                phase=TaskExecution.SUCCEEDED,
                log_links=[TaskLog(name="training-dashboard", uri=f"https://example-mltrain.com/train/{resource_meta.job_id}")],
                outputs={"results": data["results"]},
            )

        return Resource(phase=TaskExecution.RUNNING)

    async def delete(self, resource_meta: ModelTrainJobMeta, **kwargs):
        """
        Optionally call DELETE on external API.
        Safe even if job already completed.
        """
        async with httpx.AsyncClient() as client:
            await client.delete(f"{resource_meta.endpoint}/{resource_meta.job_id}")
```

To use this connector, you should define a task whose `task_type` matches the connector.

```python
import flyte.io
from typing import Any, Dict, Optional

from flyte.extend import TaskTemplate
from flyte.connectors import AsyncConnectorExecutorMixin
from flyte.models import NativeInterface, SerializationContext


class ModelTrainTask(AsyncConnectorExecutorMixin, TaskTemplate):
    _TASK_TYPE = "external_model_training"

    def __init__(
        self,
        name: str,
        endpoint: str,
        **kwargs,
    ):
        super().__init__(
            name=name,
            interface=NativeInterface(
                inputs={"epochs": int, "dataset_uri": str},
                outputs={"results": flyte.io.File},
            ),
            task_type=self._TASK_TYPE,
            **kwargs,
        )
        self.endpoint = endpoint

    def custom_config(self, sctx: SerializationContext) -> Optional[Dict[str, Any]]:
        return {"endpoint": self.endpoint}
```

Here is an example of how to use the `ModelTrainTask`:

```python
import flyte
from flyteplugins.model_training import ModelTrainTask

model_train_task = ModelTrainTask(
    name="model_train",
    endpoint="https://example-mltrain.com",
)

model_train_env = flyte.TaskEnvironment.from_task("model_train_env", model_train_task)

env = flyte.TaskEnvironment(
    name="hello_world",
    resources=flyte.Resources(memory="250Mi"),
    image=flyte.Image.from_debian_base(name="model_training").with_pip_packages(
        "flyteplugins-model-training", pre=True
    ),
    depends_on=[model_train_env],
)


@env.task
def data_prep() -> str:
    return "gs://my-bucket/dataset.csv"


@env.task
def train_model(epochs: int) -> flyte.io.File:
    dataset_uri = data_prep()
    return model_train_task(epochs=epochs, dataset_uri=dataset_uri)
```

### Build a custom connector image

Build a custom image when you're ready to deploy your connector to your cluster.
To build the Docker image for your connector, run the following script:

```python
import asyncio
from flyte import Image
from flyte.extend import ImageBuildEngine


async def build_flyte_connector_bigquery_image(registry: str, name: str, builder: str = "local"):
    """
    Build the SDK default connector image optionally overriding
    the container registry and image name.

    Args:
        registry: e.g. "ghcr.io/my-org" or "123456789012.dkr.ecr.us-west-2.amazonaws.com".
        name:     e.g. "my-connector".
        builder:  e.g. "local" or "remote".
    """

    default_image = Image.from_debian_base(
        registry=registry, name=name
    ).with_pip_packages("flyteintegrations-bigquery", pre=True)
    await ImageBuildEngine.build(default_image, builder=builder)


if __name__ == "__main__":
    print("Building connector image...")
    asyncio.run(
        build_flyte_connector_bigquery_image(
            registry="<YOUR_REGISTRY>", name="flyte-bigquery", builder="local"
        )
    )
```
