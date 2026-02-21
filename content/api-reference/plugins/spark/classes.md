---
title: Classes
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`flytekitplugins.spark.connector.DatabricksConnector`](../packages/flytekitplugins.spark.connector#flytekitpluginssparkconnectordatabricksconnector) | |
| [`flytekitplugins.spark.connector.DatabricksConnectorV2`](../packages/flytekitplugins.spark.connector#flytekitpluginssparkconnectordatabricksconnectorv2) |Add DatabricksConnectorV2 to support running the k8s spark and databricks spark together in the same workflow. |
| [`flytekitplugins.spark.connector.DatabricksJobMetadata`](../packages/flytekitplugins.spark.connector#flytekitpluginssparkconnectordatabricksjobmetadata) | |
| [`flytekitplugins.spark.generic_task.GenericSparkConf`](../packages/flytekitplugins.spark.generic_task#flytekitpluginssparkgeneric_taskgenericsparkconf) | |
| [`flytekitplugins.spark.generic_task.GenericSparkTask`](../packages/flytekitplugins.spark.generic_task#flytekitpluginssparkgeneric_taskgenericsparktask) | |
| [`flytekitplugins.spark.models.SparkJob`](../packages/flytekitplugins.spark.models#flytekitpluginssparkmodelssparkjob) | |
| [`flytekitplugins.spark.models.SparkType`](../packages/flytekitplugins.spark.models#flytekitpluginssparkmodelssparktype) | |
| [`flytekitplugins.spark.pyspark_transformers.PySparkPipelineModelTransformer`](../packages/flytekitplugins.spark.pyspark_transformers#flytekitpluginssparkpyspark_transformerspysparkpipelinemodeltransformer) | |
| [`flytekitplugins.spark.schema.ClassicSparkDataFrameSchemaReader`](../packages/flytekitplugins.spark.schema#flytekitpluginssparkschemaclassicsparkdataframeschemareader) |Implements how Classic SparkDataFrame should be read using the ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.ClassicSparkDataFrameSchemaWriter`](../packages/flytekitplugins.spark.schema#flytekitpluginssparkschemaclassicsparkdataframeschemawriter) |Implements how Classic SparkDataFrame should be written using ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.ClassicSparkDataFrameTransformer`](../packages/flytekitplugins.spark.schema#flytekitpluginssparkschemaclassicsparkdataframetransformer) |Transforms Classic Spark DataFrame's to and from a Schema (typed/untyped). |
| [`flytekitplugins.spark.schema.SparkDataFrameSchemaReader`](../packages/flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframeschemareader) |Implements how SparkDataFrame should be read using the ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.SparkDataFrameSchemaWriter`](../packages/flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframeschemawriter) |Implements how SparkDataFrame should be written to using ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.SparkDataFrameTransformer`](../packages/flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframetransformer) |Transforms Spark DataFrame's to and from a Schema (typed/untyped). |
| [`flytekitplugins.spark.sd_transformers.ClassicSparkToParquetEncodingHandler`](../packages/flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformersclassicsparktoparquetencodinghandler) | |
| [`flytekitplugins.spark.sd_transformers.ParquetToClassicSparkDecodingHandler`](../packages/flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformersparquettoclassicsparkdecodinghandler) | |
| [`flytekitplugins.spark.sd_transformers.ParquetToSparkDecodingHandler`](../packages/flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformersparquettosparkdecodinghandler) | |
| [`flytekitplugins.spark.sd_transformers.SparkDataFrameRenderer`](../packages/flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformerssparkdataframerenderer) |Render a Spark dataframe schema as an HTML table. |
| [`flytekitplugins.spark.sd_transformers.SparkToParquetEncodingHandler`](../packages/flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformerssparktoparquetencodinghandler) | |
| [`flytekitplugins.spark.task.Databricks`](../packages/flytekitplugins.spark.task#flytekitpluginssparktaskdatabricks) |Deprecated. |
| [`flytekitplugins.spark.task.DatabricksV2`](../packages/flytekitplugins.spark.task#flytekitpluginssparktaskdatabricksv2) |Use this to configure a Databricks task. |
| [`flytekitplugins.spark.task.PysparkFunctionTask`](../packages/flytekitplugins.spark.task#flytekitpluginssparktaskpysparkfunctiontask) |Actual Plugin that transforms the local python code for execution within a spark context. |
| [`flytekitplugins.spark.task.Spark`](../packages/flytekitplugins.spark.task#flytekitpluginssparktaskspark) |Use this to configure a SparkContext for a your task. |
