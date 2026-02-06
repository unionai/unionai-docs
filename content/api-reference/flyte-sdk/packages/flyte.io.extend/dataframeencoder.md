---
title: DataFrameEncoder
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DataFrameEncoder

**Package:** `flyte.io.extend`

Helper class that provides a standard way to create an ABC using
inheritance.


```python
class DataFrameEncoder(
    python_type: Type[T],
    protocol: Optional[str],
    supported_format: Optional[str],
)
```
Extend this abstract class, implement the encode function, and register your concrete class with the
DataFrameTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the DataFrameEncoder



| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type[T]` | The dataframe class in question that you want to register this encoder with |
| `protocol` | `Optional[str]` | A prefix representing the storage driver (e.g. 's3, 'gs', 'bq', etc.). You can use either "s3" or "s3://". They are the same since the "://" will just be stripped by the constructor. If None, this encoder will be registered with all protocols that flytekit's data persistence layer is capable of handling. |
| `supported_format` | `Optional[str]` | Arbitrary string representing the format. If not supplied then an empty string will be used. An empty string implies that the encoder works with any format. If the format being asked for does not exist, the transformer engine will look for the "" encoder instead and write a warning. |

## Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the. |


### encode()

```python
def encode(
    dataframe: DataFrame,
    structured_dataset_type: types_pb2.StructuredDatasetType,
) -> literals_pb2.StructuredDataset
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type | Description |
|-|-|-|
| `dataframe` | `DataFrame` | This is a DataFrame wrapper object. See more info above. |
| `structured_dataset_type` | `types_pb2.StructuredDatasetType` | This the DataFrameType, as found in the LiteralType of the interface of the task that invoked this encoding call. It is passed along to encoders so that authors of encoders can include it in the returned literals.DataFrame. See the IDL for more information on why this literal in particular carries the type information along with it. If the encoder doesn't supply it, it will also be filled in after the encoder runs by the transformer engine. :return: This function should return a DataFrame literal object. Do not confuse this with the DataFrame wrapper class used as input to this function - that is the user facing Python class. This function needs to return the IDL DataFrame. |

