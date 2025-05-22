---
title: Connectors
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Connectors

Connectors are long-running, stateless services that receive execution requests via gRPC and initiate jobs with appropriate external or internal services. Each connector service is a Kubernetes deployment that receives gRPC requests when users trigger a particular type of task. (For example, the BigQuery connector is tiggered by the invocation of a BigQuery tasks.) The connector service then initiates a job with the appropriate service.

Connectors can be run locally as long as the appropriate connection secrets are locally available, since they are spawned in-process.

Connectors are designed to be scalable and can handle large workloads efficiently, and decrease load on the core system, since they run outside it.
You can also test connectors locally without having to change the backend configuration, streamlining workflow development.

Connectors enable two key use cases:

* **Asynchronously** launching jobs on hosted platforms (e.g. Databricks or Snowflake).
* Calling external **synchronous** services, such as access control, data retrieval, or model inferencing.

This section covers all currently available connectors:

{{< variant flyte >}}
{{< markdown >}}

* [Airflow connector](./airflow-connector/_index)
* [BigQuery connector](./bigquery-connector/_index)
* [OpenAI ChatGPT connector](./chatgpt-connector/_index)
* [OpenAI Batch connector](./openai-batch-connector/_index)
* [Databricks connector](./databricks-connector/_index)
* [Memory Machine Cloud connector](./mmcloud-connector/_index)
* [Perian connector](./perian-connector/_index)
* [Sagemaker connector](./sagemaker-inference-connector/_index)
* [Sensor connector](./sensor/_index)
* [Slurm connector](./slurm-connector/_index)
* [Snowflake connector](./snowflake-connector/_index)

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

* [Airflow connector](./airflow-connector/_index)
* [BigQuery connector](./bigquery-connector/_index)
* [OpenAI ChatGPT connector](./chatgpt-connector/_index)
* [OpenAI Batch connector](./openai-batch-connector/_index)
* [Databricks connector](./databricks-connector/_index)
* [Memory Machine Cloud connector](./mmcloud-connector/_index)
* [Perian connector](./perian-connector/_index)
* [Sagemaker connector](./sagemaker-inference-connector/_index)
* [File sensor connector](./sensor/_index)
* [Slurm connector](./slurm-connector/_index)
* [Snowflake connector](./snowflake-connector/_index)
* [DGX connector](./dgx-connector)

{{< /markdown >}}
{{< /variant >}}

## Creating a new connector

If none of the existing connectors meet your needs, you can implement your own connector.

There are two types of connectors: **async** and **sync**.
* **Async connectors** enable long-running jobs that execute on an external platform over time.
  They communicate with external services that have asynchronous APIs that support `create`, `get`, and `delete` operations.
  The vast majority of connectors are async connectors.
* **Sync connectors** enable request/response services that return immediate outputs (e.g. calling an internal API to fetch data or communicating with the OpenAI API).

> [!NOTE]
> While connectors can be written in any programming language since they use a protobuf interface,
> we currently only support Python connectors.
> We may support other languages in the future.

### Async connector interface specification

To create a new async connector, extend the `AsyncConnectorBase` and implement `create`, `get`, and `delete` methods. These methods must be idempotent.

- `create`: This method is used to initiate a new job. Users have the flexibility to use gRPC, REST, or an SDK to create a job.
- `get`: This method retrieves the job resource (job ID or output literal) associated with the task, such as a BigQuery job ID or Databricks task ID.
- `delete`: Invoking this method will send a request to delete the corresponding job.

For an example implementation, see the [BigQuery connector code](https://github.com/flyteorg/flytekit/blob/master/plugins/flytekit-bigquery/flytekitplugins/bigquery/connector.py).

### Sync connector interface specification

To create a new sync connector, extend the `SyncConnectorBase` class and implement a `do` method. This method must be idempotent.

- `do`: This method is used to execute the synchronous task, and the worker in {{< key product_name >}} will be blocked until the method returns.

For an example implementation, see the [ChatGPT connector code](https://github.com/flyteorg/flytekit/blob/master/plugins/flytekit-openai/flytekitplugins/openai/chatgpt/connector.py).

### Testing your connector locally

To test your connector locally, create a class for the connector task that inherits from [`AsyncConnectorExecutorMixin`](https://github.com/flyteorg/flytekit/blob/1bc8302bb7a6cf4c7048a7f93627ee25fc6b88c4/flytekit/extend/backend/base_connector.py#L354). This mixin can handle both asynchronous tasks and synchronous tasks and allows {{< key kit_name >}} to mimic the system's behavior in calling the connector.

For testing examples, see the [BigQuery connector](./bigquery-connector#local-testing) and [Databricks connector](./databricks-connector#local-testing) documentation.

{{< variant byoc selfmanaged >}}
{{< markdown >}}

## Enabling a connector in your {{< key product_name >}} deployment

To enable a connector in your {{< key product_name >}} deployment, contact the {{< key product_name >}} team.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

## Enabling a connector in your Flyte deployment

For information on setting up a connector in your Flyte deployment, see [Deployment > Connector setup](../../deployment/flyte-connectors/_index)

{{< /markdown >}}
{{< /variant >}}