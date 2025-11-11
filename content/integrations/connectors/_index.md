---
title: Connectors
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Connectors

Connectors are stateless, long‑running services that receive execution requests via gRPC and then submit work to external (or internal) systems. Each connector runs as its own Kubernetes deployment, and is triggered when a Flyte task of the matching type is executed. For example: when a `BigQueryTask` is launched, the BigQuery connector receives the request and creates a BigQuery job.

> [!NOTE]
> The first connector for Flyte 2, the BigQuery connector (and the matching `BigQueryTask`), is in development and will be available soon.

Although they normally run inside the control plane, you can also run connectors locally — as long as the required secrets/credentials are present — because connectors are just Python services that can be spawned in‑process.

Connectors are designed to scale horizontally and reduce load on the core Flyte backend because they execute *outside* the core system. This decoupling makes connectors efficient, resilient, and easy to iterate on. You can even test them locally without modifying backend configuration, which reduces friction during development.

## Creating a new connector

If none of the existing connectors meet your needs, you can build your own.

> [!NOTE]
> Connectors communicate via Protobuf, so in theory they can be implemented in any language.
> Today, only **Python** connectors are supported.

### Async connector interface

To implement a new async connector, extend `AsyncConnector` and implement the following methods — all of which **must be idempotent**:

| Method   | Purpose                                                     |
|----------|-------------------------------------------------------------|
| `create` | Launch the external job (via REST, gRPC, SDK, or other API) |
| `get`    | Fetch current job state (return job status or output)       |
| `delete` | Delete / cancel the external job                            |

To test the connector locally, the connector task should inherit from
[AsyncConnectorExecutorMixin](https://github.com/flyteorg/flyte-sdk/blob/1d49299294cd5e15385fe8c48089b3454b7a4cd1/src/flyte/connectors/_connector.py#L206).
This mixin simulates how the Flyte system executes asynchronous connector tasks, making it easier to validate your connector implementation before deploying it.


```python
from dataclasses import dataclass
from flyte.connectors import AsyncConnector, Resource, ResourceMeta
from flyteidl2.core.execution_pb2 import TaskExecution, TaskLog
from flyteidl2.core.tasks_pb2 import TaskTemplate
from google.protobuf import json_format
import typing
import httpx

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

        if r.status_code != 200:
            return Resource(phase=TaskExecution.RUNNING)

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

To actually use this connector, you must also define a task whose `task_type` matches the connector.

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
env = flyte.TaskEnvironment(name="hello_world", resources=flyte.Resources(memory="250Mi"))

model_train_task = ModelTrainTask(
    name="model_train",
    endpoint="https://example-mltrain.com",
)

@env.task
def data_prep() -> str:
    return "gs://my-bucket/dataset.csv"

@env.task
def train_model(epochs: int) -> flyte.io.File:
    dataset_uri = data_prep()
    return model_train_task(epochs=epochs, dataset_uri=dataset_uri)


```

## Build Connector Docker Image
Build the custom image when you're ready to deploy your connector to your cluster.
To build the Docker image for your connector, run the following script:

```python
import asyncio
from flyte import Image
from flyte.extend import ImageBuildEngine


async def build_flyte_connector_image(
    registry: str, name: str, builder: str = "local"
):
    """
    Build the SDK default connector image, optionally overriding
    the container registry and image name.

    Args:
        registry: e.g. "ghcr.io/my-org" or "123456789012.dkr.ecr.us-west-2.amazonaws.com".
        name:     e.g. "my-connector".
        builder:  e.g. "local" or "remote".
    """

    default_image = Image.from_debian_base(registry=registry, name=name).with_pip_packages(
        "flyteplugins-connectors[bigquery]", pre=True
    )
    await ImageBuildEngine.build(default_image, builder=builder)

if __name__ == "__main__":
    print("Building connector image...")
    asyncio.run(build_flyte_connector_image(registry="<YOUR_REGISTRY>", name="flyte-connectors", builder="local"))
```

{{< variant byoc selfmanaged >}}
{{< markdown >}}

## Enabling a connector in your {{< key product_name >}} deployment

To enable a connector in your {{< key product_name >}} deployment, contact the {{< key product_name >}} team.

{{< /markdown >}}
{{< /variant >}}
