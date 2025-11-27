---
title: StructuredDatasetDecoder
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# StructuredDatasetDecoder

**Package:** `flytekit.types.structured.structured_dataset`

Helper class that provides a standard way to create an ABC using
inheritance.


```python
class StructuredDatasetDecoder(
    python_type: Type[DF],
    protocol: Optional[str],
    supported_format: Optional[str],
    additional_protocols: Optional[List[str]],
)
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type[DF]` | The dataframe class in question that you want to register this decoder with |
| `protocol` | `Optional[str]` | A prefix representing the storage driver (e.g. 's3, 'gs', 'bq', etc.). You can use either "s3" or "s3://". They are the same since the "://" will just be stripped by the constructor. If None, this decoder will be registered with all protocols that flytekit's data persistence layer is capable of handling. |
| `supported_format` | `Optional[str]` | Arbitrary string representing the format. If not supplied then an empty string will be used. An empty string implies that the decoder works with any format. If the format being asked for does not exist, the transformer enginer will look for the "" decoder instead and write a warning. |
| `additional_protocols` | `Optional[List[str]]` | |

## Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal. |


### decode()

```python
def decode(
    ctx: FlyteContext,
    flyte_value: literals.StructuredDataset,
    current_task_metadata: StructuredDatasetMetadata,
) -> Union[DF, typing.Iterator[DF]]
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `flyte_value` | `literals.StructuredDataset` | This will be a Flyte IDL StructuredDataset Literal - do not confuse this with the StructuredDataset class defined also in this module. |
| `current_task_metadata` | `StructuredDatasetMetadata` | Metadata object containing the type (and columns if any) for the currently executing task. This type may have more or less information than the type information bundled inside the incoming flyte_value. :return: This function can either return an instance of the dataframe that this decoder handles, or an iterator of those dataframes. |

## Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

