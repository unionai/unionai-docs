---
title: Integrations
weight: 6
variants: +flyte -serverless -byoc -byok
top_menu: true
sidebar_expanded: true
---

# Integrations

Flyte is designed to be highly extensible and can be customized in multiple ways.

> [!NOTE]
> Want to contribute an integration example? Check out the {ref}`Tutorials and integration examples contribution guide <contribute_examples>`.

## Flytekit plugins

Flytekit plugins can be implemented purely in Python, unit tested locally, and allow extending
Flytekit functionality. For comparison, these plugins can be thought of like
[Airflow operators](https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/index.html).

| Plugin | Description |
|--------|-------------|
| [Comet](</auto_examples/comet_ml_plugin/index>) | `comet-ml`: Comet’s machine learning platform. |
| [DBT](</auto_examples/dbt_plugin/index>) | Run and test your `dbt` pipelines in Flyte. |
| [Dolt](</auto_examples/dolt_plugin/index>) | Version your SQL database with `dolt`. |
| [DuckDB](</auto_examples/duckdb_plugin/index>) | Run analytical queries using DuckDB. |
| [Great Expectations](</auto_examples/greatexpectations_plugin/index>) | Validate data with `great_expectations`. |
| [Memray](</auto_examples/memray_plugin/index>) | `memray`: Memory profiling with memray. |
| [MLFlow](</auto_examples/mlflow_plugin/index>) | `mlflow`: the open standard for model tracking. |
| [Modin](</auto_examples/modin_plugin/index>) | Scale pandas workflows with `modin`. |
| [Neptune](</auto_examples/neptune_plugin/index>) | `neptune`: Neptune is the MLOps stack component for experiment tracking. |
| [NIM](</auto_examples/nim_plugin/index>) | Serve optimized model containers with NIM. |
| [Ollama](</auto_examples/ollama_plugin/index>) | Serve fine-tuned LLMs with Ollama in a Flyte workflow. |
| [ONNX](</auto_examples/onnx_plugin/index>) | Convert ML models to ONNX models seamlessly. |
| [Pandera](</auto_examples/pandera_plugin/index>) | Validate pandas dataframes with `pandera`. |
| [Papermill](</auto_examples/papermill_plugin/index>) | Execute Jupyter Notebooks with `papermill`. |
| [SQL](</auto_examples/sql_plugin/index>) | Execute SQL queries as tasks. |
| [Weights and Biases](</auto_examples/wandb_plugin/index>) | `wandb`: Machine learning platform to build better models faster. |
| [WhyLogs](</auto_examples/whylogs_plugin/index>) | `whylogs`: the open standard for data logging. |

## Using Flytekit plugins

Data is automatically marshalled and unmarshalled in and out of the plugin. Users should mostly implement the `flytekit.core.base_task.PythonTask` API defined in Flytekit.

Flytekit plugins are lazily loaded and can be released independently like libraries. The naming convention is `flytekitplugins-*`, where `*` indicates the package to be integrated into Flytekit. For example, `flytekitplugins-papermill` enables users to author Flytekit tasks using [Papermill](https://papermill.readthedocs.io/en/latest/).

You can find the plugins maintained by the core Flyte team [here](https://github.com/flyteorg/flytekit/tree/master/plugins).

## Native backend plugins

Native backend plugins can be executed without any external service dependencies because the compute is orchestrated by Flyte itself, within its provisioned Kubernetes clusters.

| Plugin | Description |
|--------|-------------|
| [Kubeflow PyTorch](</auto_examples/kfpytorch_plugin/index>) | Run distributed PyTorch training jobs using `Kubeflow`. |
| [Kubeflow TensorFlow](</auto_examples/kftensorflow_plugin/index>) | Run distributed TensorFlow training jobs using `Kubeflow`. |
| [Kubernetes pods](</auto_examples/k8s_pod_plugin/index>) | Execute Kubernetes pods for arbitrary workloads. |
| [Kubernetes cluster Dask jobs](</auto_examples/k8s_dask_plugin/index>) | Run Dask jobs on a Kubernetes Cluster. |
| [Kubernetes cluster Spark jobs](</auto_examples/k8s_spark_plugin/index>) | Run Spark jobs on a Kubernetes Cluster. |
| [MPI Operator](</auto_examples/kfmpi_plugin/index>) | Run distributed deep learning training jobs using Horovod and MPI. |
| [Ray](</auto_examples/ray_plugin/index>) | Run Ray jobs on a K8s Cluster. |


## Flyte agents

[Flyte agents](https://docs.flyte.org/en/latest/flyte_agents/index.html) are long-running, stateless services that receive execution requests via gRPC and initiate jobs with appropriate external or internal services. Each agent service is a Kubernetes deployment that receives gRPC requests from FlytePropeller when users trigger a particular type of task. (For example, the BigQuery agent handles BigQuery tasks.) The agent service then initiates a job with the appropriate service. If you don't see the agent you need below, see "[Developing agents](https://docs.flyte.org/en/latest/flyte_agents/developing_agents.html)" to learn how to develop a new agent.

| Agent | Description |
|-------|-------------|
| [AWS SageMaker Inference agent](</auto_examples/sagemaker_inference_agent/index>) | Deploy models and create, as well as trigger inference endpoints on AWS SageMaker. |
| [Airflow agent](</auto_examples/airflow_agent/index>) | Run Airflow jobs in your workflows with the Airflow agent. |
| [BigQuery agent](</auto_examples/bigquery_agent/index>) | Run BigQuery jobs in your workflows with the BigQuery agent. |
| [ChatGPT agent](</auto_examples/chatgpt_agent/index>) | Run ChatGPT jobs in your workflows with the ChatGPT agent. |
| [Databricks agent](</auto_examples/databricks_agent/index>) | Run Databricks jobs in your workflows with the Databricks agent. |
| [Memory Machine Cloud agent](</auto_examples/mmcloud_agent/index>) | Execute tasks using the MemVerge Memory Machine Cloud agent. |
| [OpenAI Batch](</auto_examples/openai_batch_agent/index>) | Submit requests for asynchronous batch processing on OpenAI. |
| [PERIAN Job Platform agent](</auto_examples/perian_agent/index>) | Execute tasks on PERIAN Job Platform. |
| [Sensor agent](</auto_examples/sensor/index>) | Run sensor jobs in your workflows with the sensor agent. |
| [Slurm agent](</auto_examples/slurm_agent/index>) | Run Slurm jobs in your workflows with the Slurm agent. |
| [Snowflake agent](</auto_examples/snowflake_agent/index>) | Run Snowflake jobs in your workflows with the Snowflake agent. |


## External service backend plugins

As the term suggests, these plugins rely on external services to handle the workload defined in the Flyte task that uses the plugin.

| Plugin | Description |
|--------|-------------|
| [AWS Athena](</auto_examples/athena_plugin/index>) | Execute queries using AWS Athena |
| [AWS Batch](</auto_examples/aws_batch_plugin/index>) | Running tasks and workflows on AWS batch service |
| [Flyte Interactive](</auto_examples/flyteinteractive_plugin/index>) | Execute tasks using Flyte Interactive to debug. |
| [Hive](</auto_examples/hive_plugin/index>) | Run Hive jobs in your workflows. |


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


## SDKs for writing tasks and workflows

The [Flyte community](../community/_index) would love to help you build new SDKs. Currently, the available SDKs are:

| SDK | Description |
|-----|-------------|
| [flytekit](https://github.com/flyteorg/flytekit) | The Python SDK for Flyte. |
| [flytekit-java](https://github.com/flyteorg/flytekit-java) | The Java/Scala SDK for Flyte. |

## Flyte operators

Flyte can be integrated with other orchestrators to help you leverage Flyte's
constructs natively within other orchestration tools.

| Operator | Description |
|----------|-------------|
| [Airflow](</auto_examples/airflow_plugin/index>) | Trigger Flyte executions from Airflow. |

