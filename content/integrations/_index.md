---
title: Integrations
weight: 5
variants: +flyte -serverless +byoc +selfmanaged
top_menu: true
sidebar_expanded: true
---

# Integrations

{{< variant flyte >}}
{{< markdown >}}

Flyte is designed to be highly extensible and can be customized in multiple ways.

> [!NOTE]
> Want to contribute an integration example? Check out the [contribution guide](../community/contribute/contribute-examples).

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}

Union supports integration with a variety of third-party services and systems.

{{< /markdown >}}
{{< /variant >}}

## Connectors

{{< key product_name >}} supports [the following connectors out-of-the-box](./connectors/_index).
If you don't see the connector you need below, have a look at [Creating a new connector](./connectors#creating-a-new-connector).

| Agent | Description |
|-------|-------------|
| [SageMaker connector](./connectors/sagemaker-inference-connector/_index) | Deploy models and create, as well as trigger inference endpoints on AWS SageMaker. |
| [Airflow connector](./connectors/airflow-connector/_index) | Run Airflow jobs in your workflows with the Airflow connector. |
| [BigQuery connector](./connectors/bigquery-connector/_index) | Run BigQuery jobs in your workflows with the BigQuery connector. |
| [ChatGPT connector](./connectors/chatgpt-connector/_index) | Run ChatGPT jobs in your workflows with the ChatGPT connector. |
| [Databricks connector](./connectors/databricks-connector/_index) | Run Databricks jobs in your workflows with the Databricks connector. |
| [Memory Machine Cloud connector](./connectors/mmcloud-connector/_index) | Execute tasks using the MemVerge Memory Machine Cloud connector. |
| [OpenAI Batch connector](./connectors/openai-batch-connector/_index) | Submit requests for asynchronous batch processing on OpenAI. |
| [Perian connector](./connectors/perian-connector/_index) | Execute tasks on Perian Job Platform. |
| [Sensor connector](./connectors/sensor/_index) | Run sensor jobs in your workflows with the sensor connector. |
| [Slurm connector](./connectors/slurm-connector/_index) | Run Slurm jobs in your workflows with the Slurm connector. |
| [Snowflake connector](./connectors//snowflake-connector/_index) | Run Snowflake jobs in your workflows with the Snowflake connector. |


{{< variant flyte >}}
{{< markdown >}}

## Flytekit plugins

Flytekit plugins can be implemented purely in Python, unit tested locally, and allow extending
Flytekit functionality. For comparison, these plugins can be thought of like
[Airflow operators](https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/index.html).

| Plugin | Description |
|--------|-------------|
| [Comet](./flytekit-plugins/comet-ml-plugin/_index) | `comet-ml`: Comet’s machine learning platform. |
| [DBT](./flytekit-plugins/dbt-plugin/_index) | Run and test your `dbt` pipelines in Flyte. |
| [Dolt](./flytekit-plugins/dolt-plugin/_index) | Version your SQL database with `dolt`. |
| [DuckDB](./flytekit-plugins/duckdb-plugin/_index) | Run analytical queries using DuckDB. |
| [Great Expectations](./flytekit-plugins/greatexpectations-plugin/_index) | Validate data with `great_expectations`. |
| [Memray](./flytekit-plugins/memray-plugin/_index) | `memray`: Memory profiling with memray. |
| [MLFlow](./flytekit-plugins/mlflow-plugin/_index) | `mlflow`: the open standard for model tracking. |
| [Modin](./flytekit-plugins/modin-plugin/_index) | Scale pandas workflows with `modin`. |
| [Neptune](./flytekit-plugins/neptune-plugin/_index) | `neptune`: Neptune is the MLOps stack component for experiment tracking. |
| [NIM](./flytekit-plugins/nim-plugin/_index) | Serve optimized model containers with NIM. |
| [Ollama](./flytekit-plugins/ollama-plugin/_index) | Serve fine-tuned LLMs with Ollama in a Flyte workflow. |
| [ONNX](./flytekit-plugins/onnx-plugin/_index) | Convert ML models to ONNX models seamlessly. |
| [Pandera](./flytekit-plugins/pandera-plugin/_index) | Validate pandas dataframes with `pandera`. |
| [Papermill](./flytekit-plugins/papermill-plugin/_index) | Execute Jupyter Notebooks with `papermill`. |
| [SQL](./flytekit-plugins/sql-plugin/_index) | Execute SQL queries as tasks. |
| [Weights and Biases](./flytekit-plugins/wandb-plugin/_index) | `wandb`: Machine learning platform to build better models faster. |
| [WhyLogs](./flytekit-plugins/whylogs-plugin/_index) | `whylogs`: the open standard for data logging. |

### Using Flytekit plugins

Data is automatically marshalled and unmarshalled in and out of the plugin. Users should mostly implement the `flytekit.core.base-task.PythonTask` API defined in Flytekit.

Flytekit plugins are lazily loaded and can be released independently like libraries. The naming convention is `flytekitplugins-*`, where `*` indicates the package to be integrated into Flytekit. For example, `flytekitplugins-papermill` enables users to author Flytekit tasks using [Papermill](https://papermill.readthedocs.io/en/latest/).

You can find the plugins maintained by the core Flyte team [here](https://github.com/flyteorg/flytekit/tree/master/plugins).

## Native backend plugins

Native backend plugins can be executed without any external service dependencies because the compute is orchestrated by Flyte itself, within its provisioned Kubernetes clusters.

| Plugin | Description |
|--------|-------------|
| [Kubeflow PyTorch](./native-backend-plugins/kfpytorch-plugin/_index) | Run distributed PyTorch training jobs using `Kubeflow`. |
| [Kubeflow TensorFlow](./native-backend-plugins/kftensorflow-plugin/_index) | Run distributed TensorFlow training jobs using `Kubeflow`. |
| [Kubernetes cluster Dask jobs](./native-backend-plugins/k8s-dask-plugin/_index) | Run Dask jobs on a Kubernetes Cluster. |
| [Kubernetes cluster Spark jobs](./native-backend-plugins/k8s-spark-plugin/_index) | Run Spark jobs on a Kubernetes Cluster. |
| [MPI Operator](./native-backend-plugins/kfmpi-plugin/_index) | Run distributed deep learning training jobs using Horovod and MPI. |
| [Ray](./native-backend-plugins/ray-plugin/_index) | Run Ray jobs on a K8s Cluster. |

<!-- TODO: Include this above? | [Kubernetes pods](./native-backend-plugins/k8s-pod-plugin/_index) | Execute Kubernetes pods for arbitrary workloads. | -->

## External service backend plugins

As the term suggests, these plugins rely on external services to handle the workload defined in the Flyte task that uses the plugin.

| Plugin | Description |
|--------|-------------|
| [AWS Athena](./external-service-backend-plugins/athena-plugin/_index) | Execute queries using AWS Athena |
| [AWS Batch](./external-service-backend-plugins/aws-batch-plugin/_index) | Running tasks and workflows on AWS batch service |
| [Flyte Interactive](./external-service-backend-plugins/flyteinteractive-plugin/_index) | Execute tasks using Flyte Interactive to debug. |
| [Hive](./external-service-backend-plugins/hive-plugin/_index) | Run Hive jobs in your workflows. |

## Enabling backend plugins

To enable a backend plugin, you must add the `ID` of the plugin to the enabled plugins list. The `enabled-plugins` is available under the `tasks > task-plugins` section of FlytePropeller's configuration.
The plugin configuration structure is defined [here](https://pkg.go.dev/github.com/flyteorg/flytepropeller@v0.6.1/pkg/controller/nodes/task/config#TaskPluginConfig). An example of the config follows:

```yaml
tasks:
  task-plugins:
    enabled-plugins:
      - container
      - sidecar
      - k8s-array
    default-for-task-types:
      container: container
      sidecar: sidecar
      container_array: k8s-array
```

**Finding the `ID` of the backend plugin**

To find the `ID` of the backend plugin, look at the source code of the plugin. For examples, in the case of Spark, the value of `ID` is used [here](https://github.com/flyteorg/flyteplugins/blob/v0.5.25/go/tasks/plugins/k8s/spark/spark.go#L424), defined as [spark](https://github.com/flyteorg/flyteplugins/blob/v0.5.25/go/tasks/plugins/k8s/spark/spark.go#L41).

## Flyte operators

Flyte can be integrated with other orchestrators to help you leverage Flyte's
constructs natively within other orchestration tools.

| Operator | Description |
|----------|-------------|
| [Airflow](./flyte-operators/airflow-plugin/_index) | Trigger Flyte executions from Airflow. |

{{< /markdown >}}
{{< /variant >}}