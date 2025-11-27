---
title: CSVToPandasDecodingHandler
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CSVToPandasDecodingHandler

**Package:** `flytekit.types.structured.basic_dfs`

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def CSVToPandasDecodingHandler()
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



## Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal. |


### decode()

```python
def decode(
    ctx: flytekit.core.context_manager.FlyteContext,
    flyte_value: flytekit.models.literals.StructuredDataset,
    current_task_metadata: flytekit.models.literals.StructuredDatasetMetadata,
) -> pd.DataFrame
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `flyte_value` | `flytekit.models.literals.StructuredDataset` | This will be a Flyte IDL StructuredDataset Literal - do not confuse this with the StructuredDataset class defined also in this module. |
| `current_task_metadata` | `flytekit.models.literals.StructuredDatasetMetadata` | Metadata object containing the type (and columns if any) for the currently executing task. This type may have more or less information than the type information bundled inside the incoming flyte_value. :return: This function can either return an instance of the dataframe that this decoder handles, or an iterator of those dataframes. |

## Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

