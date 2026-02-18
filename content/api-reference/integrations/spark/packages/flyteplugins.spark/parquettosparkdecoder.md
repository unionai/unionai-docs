---
title: ParquetToSparkDecoder
version: 2.0.0b59
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ParquetToSparkDecoder

**Package:** `flyteplugins.spark`

```python
def ParquetToSparkDecoder()
```
Extend this abstract class, implement the decode function, and register your concrete class with the
DataFrameTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the DataFrameEncoder



## Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal. |


### decode()

```python
def decode(
    flyte_value: flyteidl2.core.literals_pb2.StructuredDataset,
    current_task_metadata: flyteidl2.core.literals_pb2.StructuredDatasetMetadata,
) -> pyspark.sql.dataframe.DataFrame
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type | Description |
|-|-|-|
| `flyte_value` | `flyteidl2.core.literals_pb2.StructuredDataset` | This will be a Flyte IDL DataFrame Literal - do not confuse this with the DataFrame class defined also in this module. |
| `current_task_metadata` | `flyteidl2.core.literals_pb2.StructuredDatasetMetadata` | Metadata object containing the type (and columns if any) for the currently executing task. This type may have more or less information than the type information bundled inside the incoming flyte_value. :return: This function can either return an instance of the dataframe that this decoder handles, or an iterator of those dataframes. |

