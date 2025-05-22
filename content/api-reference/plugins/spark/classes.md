---
title: Classes
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`flytekitplugins.spark.agent.DatabricksAgent`](../packages/flytekitplugins.spark.agent#flytekitpluginssparkagentdatabricksagent) |This is the base class for all async agents. |
| [`flytekitplugins.spark.agent.DatabricksAgentV2`](../packages/flytekitplugins.spark.agent#flytekitpluginssparkagentdatabricksagentv2) |Add DatabricksAgentV2 to support running the k8s spark and databricks spark together in the same workflow. |
| [`flytekitplugins.spark.agent.DatabricksJobMetadata`](../packages/flytekitplugins.spark.agent#flytekitpluginssparkagentdatabricksjobmetadata) | |
| [`flytekitplugins.spark.models.SparkJob`](../packages/flytekitplugins.spark.models#flytekitpluginssparkmodelssparkjob) | |
| [`flytekitplugins.spark.pyspark_transformers.PySparkPipelineModelTransformer`](../packages/flytekitplugins.spark.pyspark_transformers#flytekitpluginssparkpyspark_transformerspysparkpipelinemodeltransformer) |Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`flytekitplugins.spark.schema.SparkDataFrameSchemaReader`](../packages/flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframeschemareader) |Implements how SparkDataFrame should be read using the ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.SparkDataFrameSchemaWriter`](../packages/flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframeschemawriter) |Implements how SparkDataFrame should be written to using ``open`` method of FlyteSchema. |
| [`flytekitplugins.spark.schema.SparkDataFrameTransformer`](../packages/flytekitplugins.spark.schema#flytekitpluginssparkschemasparkdataframetransformer) |Transforms Spark DataFrame's to and from a Schema (typed/untyped). |
| [`flytekitplugins.spark.sd_transformers.ParquetToSparkDecodingHandler`](../packages/flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformersparquettosparkdecodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekitplugins.spark.sd_transformers.SparkDataFrameRenderer`](../packages/flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformerssparkdataframerenderer) |Render a Spark dataframe schema as an HTML table. |
| [`flytekitplugins.spark.sd_transformers.SparkToParquetEncodingHandler`](../packages/flytekitplugins.spark.sd_transformers#flytekitpluginssparksd_transformerssparktoparquetencodinghandler) |Helper class that provides a standard way to create an ABC using. |
| [`flytekitplugins.spark.task.Databricks`](../packages/flytekitplugins.spark.task#flytekitpluginssparktaskdatabricks) |Deprecated. |
| [`flytekitplugins.spark.task.DatabricksV2`](../packages/flytekitplugins.spark.task#flytekitpluginssparktaskdatabricksv2) |Use this to configure a Databricks task. |
| [`flytekitplugins.spark.task.PysparkFunctionTask`](../packages/flytekitplugins.spark.task#flytekitpluginssparktaskpysparkfunctiontask) |Actual Plugin that transforms the local python code for execution within a spark context. |
| [`flytekitplugins.spark.task.Spark`](../packages/flytekitplugins.spark.task#flytekitpluginssparktaskspark) |Use this to configure a SparkContext for a your task. |
