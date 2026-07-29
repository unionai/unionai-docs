---
title: Spark
version: 1.16.26
variants: +flyte +union
layout: py_api
---

# Spark



## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekitplugins.spark.connector.DatabricksConnector`](packages/flytekitplugins.spark.connector/databricksconnector) |  |
| [`flytekitplugins.spark.connector.DatabricksConnectorV2`](packages/flytekitplugins.spark.connector/databricksconnectorv2) | Add DatabricksConnectorV2 to support running the k8s spark and databricks spark together in the same workflow. |
| [`flytekitplugins.spark.connector.DatabricksJobMetadata`](packages/flytekitplugins.spark.connector/databricksjobmetadata) |  |
| [`flytekitplugins.spark.generic_task.GenericSparkConf`](packages/flytekitplugins.spark.generic_task/genericsparkconf) |  |
| [`flytekitplugins.spark.generic_task.GenericSparkTask`](packages/flytekitplugins.spark.generic_task/genericsparktask) |  |
| [`flytekitplugins.spark.models.SparkJob`](packages/flytekitplugins.spark.models/sparkjob) |  |
| [`flytekitplugins.spark.models.SparkType`](packages/flytekitplugins.spark.models/sparktype) |  |
| [`flytekitplugins.spark.pyspark_transformers.PySparkPipelineModelTransformer`](packages/flytekitplugins.spark.pyspark_transformers/pysparkpipelinemodeltransformer) |  |
| [`flytekitplugins.spark.schema.ClassicSparkDataFrameSchemaReader`](packages/flytekitplugins.spark.schema/classicsparkdataframeschemareader) | Implements how Classic SparkDataFrame should be read using the ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.ClassicSparkDataFrameSchemaWriter`](packages/flytekitplugins.spark.schema/classicsparkdataframeschemawriter) | Implements how Classic SparkDataFrame should be written using ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.ClassicSparkDataFrameTransformer`](packages/flytekitplugins.spark.schema/classicsparkdataframetransformer) | Transforms Classic Spark DataFrame's to and from a Schema (typed/untyped). |
| [`flytekitplugins.spark.schema.SparkDataFrameSchemaReader`](packages/flytekitplugins.spark.schema/sparkdataframeschemareader) | Implements how SparkDataFrame should be read using the ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.SparkDataFrameSchemaWriter`](packages/flytekitplugins.spark.schema/sparkdataframeschemawriter) | Implements how SparkDataFrame should be written to using ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.SparkDataFrameTransformer`](packages/flytekitplugins.spark.schema/sparkdataframetransformer) | Transforms Spark DataFrame's to and from a Schema (typed/untyped). |
| [`flytekitplugins.spark.sd_transformers.ClassicSparkToParquetEncodingHandler`](packages/flytekitplugins.spark.sd_transformers/classicsparktoparquetencodinghandler) |  |
| [`flytekitplugins.spark.sd_transformers.ParquetToClassicSparkDecodingHandler`](packages/flytekitplugins.spark.sd_transformers/parquettoclassicsparkdecodinghandler) |  |
| [`flytekitplugins.spark.sd_transformers.ParquetToSparkDecodingHandler`](packages/flytekitplugins.spark.sd_transformers/parquettosparkdecodinghandler) |  |
| [`flytekitplugins.spark.sd_transformers.SparkDataFrameRenderer`](packages/flytekitplugins.spark.sd_transformers/sparkdataframerenderer) | Render a Spark dataframe schema as an HTML table. |
| [`flytekitplugins.spark.sd_transformers.SparkToParquetEncodingHandler`](packages/flytekitplugins.spark.sd_transformers/sparktoparquetencodinghandler) |  |
| [`flytekitplugins.spark.task.Databricks`](packages/flytekitplugins.spark.task/databricks) | Deprecated. |
| [`flytekitplugins.spark.task.DatabricksV2`](packages/flytekitplugins.spark.task/databricksv2) | Use this to configure a Databricks task. |
| [`flytekitplugins.spark.task.PysparkFunctionTask`](packages/flytekitplugins.spark.task/pysparkfunctiontask) | Actual Plugin that transforms the local python code for execution within a spark context. |
| [`flytekitplugins.spark.task.Spark`](packages/flytekitplugins.spark.task/spark) | Use this to configure a SparkContext for a your task. |

### Packages

| Package | Description |
|-|-|
| [`flytekitplugins.spark.connector`](packages/flytekitplugins.spark.connector/_index) |  |
| [`flytekitplugins.spark.generic_task`](packages/flytekitplugins.spark.generic_task/_index) |  |
| [`flytekitplugins.spark.models`](packages/flytekitplugins.spark.models/_index) |  |
| [`flytekitplugins.spark.pyspark_transformers`](packages/flytekitplugins.spark.pyspark_transformers/_index) |  |
| [`flytekitplugins.spark.schema`](packages/flytekitplugins.spark.schema/_index) |  |
| [`flytekitplugins.spark.sd_transformers`](packages/flytekitplugins.spark.sd_transformers/_index) |  |
| [`flytekitplugins.spark.task`](packages/flytekitplugins.spark.task/_index) |  |
| [`flytekitplugins.spark.utils`](packages/flytekitplugins.spark.utils/_index) |  |

