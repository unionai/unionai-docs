---
title: DataFrameDecoder
version: 2.0.0b57
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DataFrameDecoder

**Package:** `flyte.io.extend`

```python
class DataFrameDecoder(
    python_type: Type[DF],
    protocol: Optional[str],
    supported_format: Optional[str],
    additional_protocols: Optional[List[str]],
)
```
Extend this abstract class, implement the decode function, and register your concrete class with the
DataFrameTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the DataFrameEncoder



| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type[DF]` | The dataframe class in question that you want to register this decoder with |
| `protocol` | `Optional[str]` | A prefix representing the storage driver (e.g. 's3, 'gs', 'bq', etc.). You can use either "s3" or "s3://". They are the same since the "://" will just be stripped by the constructor. If None, this decoder will be registered with all protocols that flytekit's data persistence layer is capable of handling. |
| `supported_format` | `Optional[str]` | Arbitrary string representing the format. If not supplied then an empty string will be used. An empty string implies that the decoder works with any format. If the format being asked for does not exist, the transformer enginer will look for the "" decoder instead and write a warning. |
| `additional_protocols` | `Optional[List[str]]` | |

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
    flyte_value: literals_pb2.StructuredDataset,
    current_task_metadata: literals_pb2.StructuredDatasetMetadata,
) -> Union[DF, typing.AsyncIterator[DF]]
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type | Description |
|-|-|-|
| `flyte_value` | `literals_pb2.StructuredDataset` | This will be a Flyte IDL DataFrame Literal - do not confuse this with the DataFrame class defined also in this module. |
| `current_task_metadata` | `literals_pb2.StructuredDatasetMetadata` | Metadata object containing the type (and columns if any) for the currently executing task. This type may have more or less information than the type information bundled inside the incoming flyte_value. :return: This function can either return an instance of the dataframe that this decoder handles, or an iterator of those dataframes. |

