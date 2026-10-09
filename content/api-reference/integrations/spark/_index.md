---
title: Spark
icon: book
version: 2.11.2
variants: +flyte +union
layout: py_api
---

# Spark



## Directory

### Classes

| Class | Description |
|-|-|
| [`ParquetToSparkDecoder`](./parquettosparkdecoder) |  |
| [`Spark`](./spark) | Use this to configure a SparkContext for a your task. |
| [`SparkToParquetEncoder`](./sparktoparquetencoder) |  |

### Methods

| Method | Description |
|-|-|
| [`register_spark_df_transformers()`](#register_spark_df_transformers) | Register Spark DataFrame encoders and decoders with the DataFrameTransformerEngine. |


## Methods

#### register_spark_df_transformers()

```python
def register_spark_df_transformers()
```
Register Spark DataFrame encoders and decoders with the DataFrameTransformerEngine.

This function is called automatically via the flyte.plugins.types entry point
when flyte.init() is called with load_plugin_type_transformers=True (the default).


