---
title: Integrations
weight: 8
sidebar_expanded: true
variants: +flyte -serverless +byoc +byok
---

# Integrations

This section describes how to enable integrations that connect to other services,
such as Apache Airflow, ChatGPT, dbt, Databricks, NVidia DGX, Snowflake, and
more.

## Additional integrations

A variety of connectors and plugins enable you to integrate {{< key product_name >}} with additional external services. If you don't see the integration you need, you can [create your own](./connectors#creating-a-new-connector).

### AI integrations

* [OpenAI connectors](./connectors/openai-connectors) Send prompts to ChatGPT and receive responses.

### Database integrations

* [DuckDB plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/duckdb_plugin/index.html) Run analytical queries using DuckDB.
* [Google BigQuery connector](./connectors/bigquery-connector) Query Google BigQuery tables from your workflows.
* [SQL plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/sql_plugin/index.html) Execute SQL queries as tasks.

### Data pipeline integrations

* [Apache Airflow connector](./connectors/airflow-connector) Run Apache Airflow jobs in your workflows.
* [Databricks connector](./connectors/databricks-connector) Run Databricks jobs in your workflows.
* [dbt plugin](https://docs.flyte.org/en/latest/flytesnacks/examples/dbt_plugin/index.html) Run and test your `dbt` pipelines in {{< key product_name >}}.
* [MemVerge Memory Machine Cloud connector](./connectors/mmcloud-connector) Execute tasks using the MemVerge Memory Machine Cloud connector
* [NVIDIA DGX connector](./connectors/dgx-connector) Run jobs on the NVIDIA DGX platform.
* [Snowflake connector](./connectors/snowflake-connector) Run Snowflake jobs in your workflow.

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

* [File sensor connector](./connectors/file-sensor-connector) Detect files appearing in your local or remote filesystem.
