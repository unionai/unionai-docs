---
title: Spark
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# Spark



## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekitplugins.spark.connector.DatabricksConnector`](flytekitplugins.spark.connector#flytekitpluginssparkconnectordatabricksconnector) |  |
| [`flytekitplugins.spark.connector.DatabricksConnectorV2`](flytekitplugins.spark.connector#flytekitpluginssparkconnectordatabricksconnectorv2) | Add DatabricksConnectorV2 to support running the k8s spark and databricks spark together in the same workflow. |
| [`flytekitplugins.spark.connector.DatabricksJobMetadata`](flytekitplugins.spark.connector#flytekitpluginssparkconnectordatabricksjobmetadata) | Metadata persisted for a Databricks run. |
| [`flytekitplugins.spark.databricks_auth.DatabricksAuth`](flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authdatabricksauth) | Interface for obtaining a bearer token for Databricks API calls. |
| [`flytekitplugins.spark.databricks_auth.DatabricksAuthError`](flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authdatabricksautherror) | Raised when Databricks authentication cannot be obtained. |
| [`flytekitplugins.spark.databricks_auth.OAuthM2MAuth`](flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authoauthm2mauth) | Authenticate a Databricks service principal with client credentials. |
| [`flytekitplugins.spark.databricks_auth.OIDCConnectorAuth`](flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authoidcconnectorauth) | Exchange the connector workload's projected JWT for a Databricks token. |
| [`flytekitplugins.spark.databricks_auth.OIDCNamespaceServiceAccountAuth`](flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authoidcnamespaceserviceaccountauth) | Federate as a ServiceAccount discovered in the workflow namespace. |
| [`flytekitplugins.spark.databricks_auth.PATAuth`](flytekitplugins.spark.databricks_auth#flytekitpluginssparkdatabricks_authpatauth) | Delegate to the connector's existing multi-tenant PAT lookup. |
| [`flytekitplugins.spark.generic_task.GenericSparkConf`](flytekitplugins.spark.generic_task#flytekitpluginssparkgeneric_taskgenericsparkconf) |  |
| [`flytekitplugins.spark.generic_task.GenericSparkTask`](flytekitplugins.spark.generic_task#flytekitpluginssparkgeneric_taskgenericsparktask) |  |
| [`flytekitplugins.spark.models.SparkJob`](flytekitplugins.spark.models#flytekitpluginssparkmodelssparkjob) |  |
| [`flytekitplugins.spark.models.SparkType`](flytekitplugins.spark.models#flytekitpluginssparkmodelssparktype) |  |
| [`flytekitplugins.spark.pyspark_transformers.PySparkPipelineModelTransformer`](flytekitplugins.spark.pyspark_transformers#flytekitpluginssparkpyspark_transformerspysparkpipelinemodeltransformer) |  |
| [`flytekitplugins.spark.schema.ClassicSparkDataFrameSchemaReader`](flytekitplugins.spark.schema#flytekitpluginssparkschemaclassicsparkdataframeschemareader) | Implements how Classic SparkDataFrame should be read using the ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.ClassicSparkDataFrameSchemaWriter`](flytekitplugins.spark.schema#flytekitpluginssparkschemaclassicsparkdataframeschemawriter) | Implements how Classic SparkDataFrame should be written using ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.ClassicSparkDataFrameTransformer`](flytekitplugins.spark.schema#flytekitpluginssparkschemaclassicsparkdataframetransformer) | Transforms Classic Spark DataFrame's to and from a Schema (typed/untyped). |
| [`flytekitplugins.spark.schema.SparkDataFrameSchemaReader`](flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframeschemareader) | Implements how SparkDataFrame should be read using the ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.SparkDataFrameSchemaWriter`](flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframeschemawriter) | Implements how SparkDataFrame should be written to using ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.SparkDataFrameTransformer`](flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframetransformer) | Transforms Spark DataFrame's to and from a Schema (typed/untyped). |
| [`flytekitplugins.spark.sd_transformers.ClassicSparkToParquetEncodingHandler`](flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformersclassicsparktoparquetencodinghandler) |  |
| [`flytekitplugins.spark.sd_transformers.ParquetToClassicSparkDecodingHandler`](flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformersparquettoclassicsparkdecodinghandler) |  |
| [`flytekitplugins.spark.sd_transformers.ParquetToSparkDecodingHandler`](flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformersparquettosparkdecodinghandler) |  |
| [`flytekitplugins.spark.sd_transformers.SparkDataFrameRenderer`](flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformerssparkdataframerenderer) | Render a Spark dataframe schema as an HTML table. |
| [`flytekitplugins.spark.sd_transformers.SparkToParquetEncodingHandler`](flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformerssparktoparquetencodinghandler) |  |
| [`flytekitplugins.spark.task.Databricks`](flytekitplugins.spark.task#flytekitpluginssparktaskdatabricks) | Deprecated. |
| [`flytekitplugins.spark.task.DatabricksV2`](flytekitplugins.spark.task#flytekitpluginssparktaskdatabricksv2) | Use this to configure a Databricks task. |
| [`flytekitplugins.spark.task.PysparkFunctionTask`](flytekitplugins.spark.task#flytekitpluginssparktaskpysparkfunctiontask) | Actual Plugin that transforms the local python code for execution within a spark context. |
| [`flytekitplugins.spark.task.Spark`](flytekitplugins.spark.task#flytekitpluginssparktaskspark) | Use this to configure a SparkContext for a your task. |

### Functions

| Function | Description |
|-|-|
| [`flytekitplugins.spark.connector.get_databricks_token()`](flytekitplugins.spark.connector#get_databricks_token) | Get the Databricks access token with multi-tenant support. |
| [`flytekitplugins.spark.connector.get_header()`](flytekitplugins.spark.connector#get_header) | Get the authorization header for Databricks API calls. |
| [`flytekitplugins.spark.connector.get_secret_from_k8s()`](flytekitplugins.spark.connector#get_secret_from_k8s) | Read a secret from Kubernetes using the Kubernetes Python client. |
| [`flytekitplugins.spark.connector.list_serviceaccounts_in_k8s()`](flytekitplugins.spark.connector#list_serviceaccounts_in_k8s) | List labelled ServiceAccounts in a workflow namespace. |
| [`flytekitplugins.spark.connector.result_state_is_available()`](flytekitplugins.spark.connector#result_state_is_available) |  |
| [`flytekitplugins.spark.databricks_auth.build_auth()`](flytekitplugins.spark.databricks_auth#build_auth) | Rebuild an auth strategy from persisted connector metadata. |
| [`flytekitplugins.spark.databricks_auth.select_auth()`](flytekitplugins.spark.databricks_auth#select_auth) | Select an explicitly configured strategy, defaulting to PAT. |
| [`flytekitplugins.spark.databricks_auth.validate_connector_config()`](flytekitplugins.spark.databricks_auth#validate_connector_config) | Validate an explicitly configured connector-wide auth type. |
| [`flytekitplugins.spark.task.new_spark_session()`](flytekitplugins.spark.task#new_spark_session) | Optionally creates a new spark session and returns it. |
| [`flytekitplugins.spark.utils.is_serverless_config()`](flytekitplugins.spark.utils#is_serverless_config) | Detect if the Databricks configuration is for serverless compute. |

### Packages

| Package | Description |
|-|-|
| [`flytekitplugins.spark.connector`](flytekitplugins.spark.connector) |  |
| [`flytekitplugins.spark.databricks_auth`](flytekitplugins.spark.databricks_auth) | Authentication strategies for the Databricks connector. |
| [`flytekitplugins.spark.generic_task`](flytekitplugins.spark.generic_task) |  |
| [`flytekitplugins.spark.models`](flytekitplugins.spark.models) |  |
| [`flytekitplugins.spark.pyspark_transformers`](flytekitplugins.spark.pyspark_transformers) |  |
| [`flytekitplugins.spark.schema`](flytekitplugins.spark.schema) |  |
| [`flytekitplugins.spark.sd_transformers`](flytekitplugins.spark.sd_transformers) |  |
| [`flytekitplugins.spark.task`](flytekitplugins.spark.task) |  |
| [`flytekitplugins.spark.utils`](flytekitplugins.spark.utils) |  |

