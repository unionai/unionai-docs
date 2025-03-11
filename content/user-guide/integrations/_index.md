---
title: Integrations
weight: 7
---

# Integrations

{@@ if serverless @@}
This section describes how to enable agent integrations that connect to other services, such as Apache Airflow, ChatGPT, Databricks, Snowflake, and more.
{@@ elif byoc @@}
This section describes how to enable integrations with AWS and GCP cloud resources as well as how to use integrations that connect to other services, such as Apache Airflow, ChatGPT, dbt, Databricks, NVidia DGX, Snowflake, and more.

## AWS cloud resources integrations

* [Enabling AWS S3](./enabling-aws-resources/enabling-aws-s3.md)
* [Enabling AWS ECR](./enabling-aws-resources/enabling-aws-ecr.md)
* [Enabling AWS Secrets Manager](./enabling-aws-resources/enabling-aws-secrets-manager.md)

## GCP cloud resources integrations

* [Enabling BigQuery](./enabling-gcp-resources/enabling-bigquery.md)
* [Enabling Google Artifact Registry](./enabling-gcp-resources/enabling-google-artifact-registry.md)
* [Enabling Google Secret Manager](./enabling-gcp-resources/enabling-google-secret-manager.md)

## Additional integrations

A variety of agents and plugins enable you to integrate Union with additional external services. If you don't see the integration you need, you can [create your own](./agents/index.md#creating-a-new-agent).

### AI integrations

* [OpenAI agents](./agents/openai-agents/index.md) Send prompts to ChatGPT and receive responses.

### Database integrations

* [DuckDB plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/duckdb_plugin/index.html) Run analytical queries using DuckDB.
* [Google BigQuery agent](./agents/bigquery-agent/index.md) Query Google BigQuery tables from your workflows.
* [SQL plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/sql_plugin/index.html) Execute SQL queries as tasks.

### Data pipeline integrations

* [Apache Airflow agent](./agents/airflow-agent/index.md) Run Apache Airflow jobs in your workflows.
* [Databricks agent](./agents/databricks-agent/index.md) Run Databricks jobs in your workflows.
* [dbt plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/dbt_plugin/index.html) Run and test your `dbt` pipelines in Flyte.
* [MemVerge Memory Machine Cloud agent](./agents/mmcloud-agent/index.md) Execute tasks using the MemVerge Memory Machine Cloud agent
* [NVIDIA DGX agent](./agents/dgx-agent.md) Run jobs on the NVIDIA DGX platform.
* [Snowflake agent](./agents/snowflake-agent/index.md) Run Snowflake jobs in your workflow.

### Data science tooling integrations

* [Modin plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/modin_plugin/index.html) Scale pandas workflows with `modin`.
* [Papermill plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/papermill_plugin/index.html) Execute Jupyter Notebooks with `papermill`.

### Data validation integrations

* [Dolt plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/dolt_plugin/index.html) Version your SQL database with `dolt`.
* [Great Expectations plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/greatexpectations_plugin/index.html) Validate data with `great_expectations`.
* [Pandera plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/pandera_plugin/index.html) Validate pandas dataframes with `pandera`.
* [whylogs plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/whylogs_plugin/index.html) The open standard for data logging.

### MLOps integrations

* [mlflow plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/mlflow_plugin/index.html) The open standard for model tracking.
* [ONNX plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/onnx_plugin/index.html) Convert ML models to ONNX models seamlessly.

### Misc

* [File sensor agent](./agents/file-sensor-agent/index.md) Detect files appearing in your local or remote filesystem.
{@@ endif @@}
