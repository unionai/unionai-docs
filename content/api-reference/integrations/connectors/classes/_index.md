---
title: Classes
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`flyteplugins.connectors.bigquery.BigQueryConfig`](../packages/flyteplugins.connectors.bigquery/bigqueryconfig) |BigQueryConfig should be used to configure a BigQuery Task. |
| [`flyteplugins.connectors.bigquery.BigQueryConnector`](../packages/flyteplugins.connectors.bigquery/bigqueryconnector) |This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`flyteplugins.connectors.bigquery.BigQueryTask`](../packages/flyteplugins.connectors.bigquery/bigquerytask) |This mixin class is used to run the connector task locally, and it's only used for local execution. |
| [`flyteplugins.connectors.bigquery.connector.BigQueryConnector`](../packages/flyteplugins.connectors.bigquery.connector/bigqueryconnector) |This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`flyteplugins.connectors.bigquery.connector.BigQueryMetadata`](../packages/flyteplugins.connectors.bigquery.connector/bigquerymetadata) | |
| [`flyteplugins.connectors.bigquery.task.BigQueryConfig`](../packages/flyteplugins.connectors.bigquery.task/bigqueryconfig) |BigQueryConfig should be used to configure a BigQuery Task. |
| [`flyteplugins.connectors.bigquery.task.BigQueryTask`](../packages/flyteplugins.connectors.bigquery.task/bigquerytask) |This mixin class is used to run the connector task locally, and it's only used for local execution. |
| [`flyteplugins.connectors.databricks.Databricks`](../packages/flyteplugins.connectors.databricks/databricks) |Use this to configure a Databricks task. |
| [`flyteplugins.connectors.databricks.DatabricksConnector`](../packages/flyteplugins.connectors.databricks/databricksconnector) |This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`flyteplugins.connectors.databricks.connector.DatabricksConnector`](../packages/flyteplugins.connectors.databricks.connector/databricksconnector) |This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`flyteplugins.connectors.databricks.connector.DatabricksJobMetadata`](../packages/flyteplugins.connectors.databricks.connector/databricksjobmetadata) | |
| [`flyteplugins.connectors.databricks.task.Databricks`](../packages/flyteplugins.connectors.databricks.task/databricks) |Use this to configure a Databricks task. |
| [`flyteplugins.connectors.databricks.task.DatabricksFunctionTask`](../packages/flyteplugins.connectors.databricks.task/databricksfunctiontask) |Actual Plugin that transforms the local python code for execution within a spark context. |
| [`flyteplugins.connectors.snowflake.Snowflake`](../packages/flyteplugins.connectors.snowflake/snowflake) |This mixin class is used to run the connector task locally, and it's only used for local execution. |
| [`flyteplugins.connectors.snowflake.SnowflakeConfig`](../packages/flyteplugins.connectors.snowflake/snowflakeconfig) |SnowflakeConfig should be used to configure a Snowflake Task. |
| [`flyteplugins.connectors.snowflake.SnowflakeConnector`](../packages/flyteplugins.connectors.snowflake/snowflakeconnector) |This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`flyteplugins.connectors.snowflake.connector.SnowflakeConnector`](../packages/flyteplugins.connectors.snowflake.connector/snowflakeconnector) |This is the base class for all async connectors, and it defines the interface that all connectors must implement. |
| [`flyteplugins.connectors.snowflake.connector.SnowflakeJobMetadata`](../packages/flyteplugins.connectors.snowflake.connector/snowflakejobmetadata) | |
| [`flyteplugins.connectors.snowflake.task.Snowflake`](../packages/flyteplugins.connectors.snowflake.task/snowflake) |This mixin class is used to run the connector task locally, and it's only used for local execution. |
| [`flyteplugins.connectors.snowflake.task.SnowflakeConfig`](../packages/flyteplugins.connectors.snowflake.task/snowflakeconfig) |SnowflakeConfig should be used to configure a Snowflake Task. |
