---
title: Integrations
weight: 4
variants: +flyte +union
top_menu: true
llm_readable_bundle: true
---

# Integrations

{{< llm-bundle-note >}}

Flyte 2 is designed to be extensible by default. While the core platform covers the most common orchestration needs, many production workloads require specialized infrastructure, external services or execution semantics that go beyond the core runtime.

Flyte 2 exposes these capabilities through integrations.

Under the hood, integrations are implemented using Flyte 2's plugin system, which provides a consistent way to extend the platform without modifying core execution logic.

An integration allows you to declaratively enable new capabilities such as distributed compute frameworks or third-party services without manually managing infrastructure. You specify what you need, and Flyte takes care of how it is provisioned, used and cleaned up.

This page covers:

- The types of integrations Flyte 2 supports today
- How integrations fit into Flyte 2's execution model
- How to use integrations in your tasks
- The integrations available out of the box

If you need functionality that doesn't exist yet, Flyte 2's plugin system is intentionally open-ended. You can build and register your own integrations using the same architecture described here.

## Integration categories

Flyte 2 integrations fall into the following categories:

1. **Distributed compute**: Provision transient compute clusters to run tasks across multiple nodes, with automatic lifecycle management.
2. **Agentic AI**: Support for various common aspects of agentic AI applications.
3. **Configuration**: Compose and pass hierarchical configuration objects between tasks, with type-safe schemas and CLI/YAML composition.
4. **Experiment tracking**: Integrate with experiment tracking platforms for logging metrics, parameters, and artifacts.
5. **Data validation**: Enforce schema contracts on dataframes flowing between tasks, with automatic validation reports.
6. **Data types**: Add native support for additional file and dataframe types as task inputs and outputs.
7. **Connectors**: Stateless, long-running services that receive execution requests via gRPC and then submit work to external (or internal) systems.
8. **LLM Serving**: Deploy and serve large language models with an OpenAI-compatible API.
9. **Notebook execution**: Run parameterized Jupyter notebooks as typed Flyte tasks with cell-level reports.
10. **Observability**: Patterns for connecting tasks to external tracing and observability tooling.

## Distributed compute

Distributed compute integrations allow tasks to run on dynamically provisioned clusters. These clusters are created just-in-time, scoped to the task execution and torn down automatically when the task completes.

This enables large-scale parallelism without requiring users to operate or maintain long-running infrastructure.

### Supported distributed compute integrations

| Plugin                      | Description                                      | Common use cases                                       |
| --------------------------- | ------------------------------------------------ | ------------------------------------------------------ |
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

## Agentic AI

Agentic AI integrations provide drop-in replacements for LLM provider SDKs. They let you use Flyte tasks as agent tools so that tool calls run with full Flyte observability, retries, and caching.

### Supported agentic AI integrations

| Plugin                              | Description                                                    | Common use cases                         |
| ----------------------------------- | -------------------------------------------------------------- | ---------------------------------------- |
| [OpenAI](./openai/_index)           | Drop-in replacement for OpenAI Agents SDK `function_tool`      | Agentic workflows with OpenAI models     |
| [Anthropic](./anthropic/_index)     | Agent loop and `function_tool` for the Anthropic Claude SDK    | Agentic workflows with Claude            |
| [Gemini](./gemini/_index)           | Agent loop and `function_tool` for the Google Gemini SDK       | Agentic workflows with Gemini            |
| [Code generation](./codegen/_index) | LLM-driven code generation with automatic testing in sandboxes | Data processing, ETL, analysis pipelines |

## Experiment tracking

Experiment tracking integrations let you log metrics, parameters, and artifacts to external tracking platforms during Flyte task execution.

### Supported experiment tracking integrations

| Plugin                               | Description                  | Common use cases                                 |
| ------------------------------------ | ---------------------------- | ------------------------------------------------ |
| [MLflow](./mlflow/_index)            | MLflow experiment tracking   | Experiment tracking, autologging, model registry |
| [Weights and Biases](./wandb/_index) | Weights & Biases integration | Experiment tracking and hyperparameter tuning    |

## Configuration

Configuration integrations let you compose and pass hierarchical configuration objects between Flyte tasks, with type-safe schemas and CLI/YAML composition.

### Supported configuration integrations

| Plugin                          | Description                                                       | Common use cases                                                                  |
| ------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [OmegaConf](./omegaconf/_index) | `DictConfig` / `ListConfig` as native task input and output types | Passing composed configs between tasks, structured configs, YAML-driven pipelines |
| [Hydra](./hydra/_index)         | Hydra config composition and sweep submission for Flyte tasks     | YAML-driven experiment composition, grid and Bayesian sweeps, hardware presets    |

## Data validation

Data validation integrations enforce schema contracts on the dataframes flowing between tasks. They validate data at task boundaries, catch type and constraint violations early, and produce HTML reports visible in the Flyte UI.

### Supported data validation integrations

| Plugin                      | Description                                                | Common use cases                                            |
| --------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| [Pandera](./pandera/_index) | Validates dataframes with pandera `DataFrameModel` schemas | Schema enforcement, data quality checks, validation reports |

## Data types

Data type integrations add native support for additional file and dataframe types as task inputs and outputs. They register typed encoders and decoders with Flyte's type engine, so you can annotate task signatures with the type directly and let Flyte handle serialization.

### Supported data type integrations

| Plugin                    | Description                                                          | Common use cases                                            |
| ------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------- |
| [JSONL](./jsonl/_index)   | Typed `JsonlFile` / `JsonlDir` for streaming JSON Lines data         | LLM dataset pipelines, event logs, large line-delimited I/O |
| [Polars](./polars/_index) | Native `pl.DataFrame` / `pl.LazyFrame` support via Parquet           | High-performance dataframe ETL, feature engineering         |

## Connectors

Connectors are stateless, long‑running services that receive execution requests via gRPC and then submit work to external (or internal) systems. Each connector runs as its own Kubernetes deployment, and is triggered when a Flyte task of the matching type is executed.

Although they normally run inside the data plane, you can also run connectors locally as long as the required secrets/credentials are present locally. This is useful because connectors are just Python services that can be spawned in‑process.

Connectors are designed to scale horizontally and reduce load on the core Flyte backend because they execute _outside_ the core system. This decoupling makes connectors efficient, resilient, and easy to iterate on. You can even test them locally without modifying backend configuration, which reduces friction during development.

### Supported connectors

| Connector                         | Description                                 | Common use cases                         |
| --------------------------------- | ------------------------------------------- | ---------------------------------------- |
| [Snowflake](./snowflake/_index)   | Run SQL queries on Snowflake asynchronously | Data warehousing, ETL, analytics queries |
| [BigQuery](./bigquery/_index)     | Run SQL queries on Google BigQuery          | Data warehousing, ETL, analytics queries |
| [Databricks](./databricks/_index) | Run PySpark jobs on Databricks clusters     | Large-scale data processing, Spark ETL   |

### Creating a new connector

If none of the existing connectors meet your needs, you can build your own.

> [!NOTE]
> Connectors communicate via Protobuf, so in theory they can be implemented in any language.
> Today, only **Python** connectors are supported.

### Async connector interface

To implement a new async connector, extend `AsyncConnector` and implement the following methods, all of which must be idempotent:

| Method     | Purpose                                                     |
| ---------- | ----------------------------------------------------------- |
| `create`   | Launch the external job (via REST, gRPC, SDK, or other API) |
| `get`      | Fetch current job state (return job status or output)       |
| `delete`   | Delete / cancel the external job                            |
| `get_logs` | Stream paginated log lines to the Flyte UI                  |

To test the connector locally, the connector task should inherit from
[AsyncConnectorExecutorMixin](https://github.com/flyteorg/flyte-sdk/blob/1d49299294cd5e15385fe8c48089b3454b7a4cd1/src/flyte/connectors/_connector.py#L206). This mixin simulates how the Flyte 2 system executes asynchronous connector tasks, making it easier to validate your connector implementation before deploying it.

### Example: Batch job connector

The following example implements a connector that simulates submitting and polling an external batch job. Replace the mock logic with real API calls for your use case.

**Connector** (`my_connector/connector.py`):

{{< code file="/unionai-examples/v2/integrations/connectors/batch_job/connector.py" lang=python >}}

**Task plugin** (`my_connector/task.py`):

{{< code file="/unionai-examples/v2/integrations/connectors/batch_job/task.py" lang=python >}}

**Usage**:

```python
import flyte
from my_connector.task import BatchJobConfig, BatchJobTask

batch_job = BatchJobTask(
    name="my_batch_job",
    plugin_config=BatchJobConfig(timeout_seconds=60),
    inputs={"name": str},
    outputs={"result": str},
)

flyte.TaskEnvironment.from_task("batch-job-env", batch_job)
```

### Connector-level secrets

If your connector needs credentials (API keys, tokens) shared across all tasks, pass them as environment variables into the connector process.

{{< variant union >}}
{{< markdown >}}
Add secrets to `ConnectorEnvironment`:

```python
connector = flyte.app.ConnectorEnvironment(
    name="batch-job-connector",
    image=image,
    include=["my_connector"],
    secrets=[flyte.Secret(key="MY_API_KEY")],
)
```
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
Set environment variables on the connector Kubernetes deployment:

```bash
kubectl set env deployment/<connector-deployment> MY_API_KEY=<value> -n <flyte-namespace>
```
{{< /markdown >}}
{{< /variant >}}

Inside the connector, read the secret from the environment:

```python
import os

api_key = os.environ["MY_API_KEY"]
```

See [Secrets](../user-guide/task-configuration/secrets) for how to store and manage secrets.

### Deploy a custom connector

{{< variant union >}}
{{< markdown >}}
Deploy your connector as a long-running service using `flyte.app.ConnectorEnvironment`. Union handles building the image, pushing it, and keeping the service running — no manual Kubernetes configuration required.

See the **Connector app** guide (`user-guide/build-apps/connector-app`) for a complete walkthrough.
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
Deploying a connector requires two steps: building a Docker image that contains your connector code and then patching the connector Kubernetes deployment to use it.

**Step 1: Build the connector image**

```python
import asyncio
from flyte import Image
from flyte.extend import ImageBuildEngine


async def build_connector_image(registry: str, name: str, builder: str = "local"):
    image = Image.from_debian_base(
        registry=registry, name=name
    ).with_pip_packages("flyte[connector]", "my-connector-package")
    await ImageBuildEngine.build(image, builder=builder)


if __name__ == "__main__":
    asyncio.run(
        build_connector_image(
            registry="<YOUR_REGISTRY>", name="my-connector", builder="local"
        )
    )
```

**Step 2: Override the connector deployment image**

Once the image is pushed, patch the connector Kubernetes deployment to use it:

```bash
kubectl set image deployment/<connector-deployment-name> \
    connector=<YOUR_REGISTRY>/my-connector:<TAG> \
    -n <flyte-namespace>
```

Replace `<connector-deployment-name>` with the name of your connector deployment (e.g. `flyte-connector`), and `<flyte-namespace>` with the namespace where Flyte is installed (typically `flyte`).
{{< /markdown >}}
{{< /variant >}}

## LLM serving

LLM serving integrations let you deploy and serve large language models as Flyte apps with an OpenAI-compatible API. They handle model loading, GPU management, and autoscaling.

### Supported LLM serving integrations

| Plugin                                        | Description                                         | Common use cases             |
| --------------------------------------------- | --------------------------------------------------- | ---------------------------- |
| [SGLang](../user-guide/native-app-integrations/sglang-app) | Deploy models with SGLang's high-throughput runtime | LLM inference, model serving |
| [vLLM](../user-guide/native-app-integrations/vllm-app)     | Deploy models with vLLM's PagedAttention engine     | LLM inference, model serving |

For full setup instructions including multi-GPU deployment, model prefetching, and autoscaling, see the [SGLang app](../user-guide/native-app-integrations/sglang-app) and [vLLM app](../user-guide/native-app-integrations/vllm-app) pages.

## Notebook execution

Notebook execution integrations let you run Jupyter notebooks as first-class Flyte tasks with typed inputs and outputs, HTML reports surfaced in the Flyte UI, and the ability to call other Flyte tasks from within the notebook.

### Supported notebook execution integrations

| Plugin                          | Description                                                                                | Common use cases                                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| [Papermill](./papermill/_index) | Parameterize and execute `.ipynb` files via [papermill](https://papermill.readthedocs.io/) | Productionizing exploratory notebooks, cell-by-cell HTML reports, notebook-driven analysis pipelines |

## Observability

Patterns for connecting Flyte tasks to external tracing and observability backends. Unlike the entries above, these are not plugins — they are usage patterns built on top of Flyte's [custom context](../user-guide/task-programming/custom-context) primitive plus the standard libraries from the relevant ecosystem.

### Supported observability integrations

| Integration                              | Description                                                                                                | Common use cases                                     |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| [OpenTelemetry](./opentelemetry/_index)  | Propagate W3C trace context across task boundaries so workflow traces unify with downstream service traces | Distributed tracing, debugging cross-service latency |
