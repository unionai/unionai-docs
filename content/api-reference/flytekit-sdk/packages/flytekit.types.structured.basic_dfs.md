---
title: flytekit.types.structured.basic_dfs
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.structured.basic_dfs

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrowToParquetEncodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsarrowtoparquetencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`CSVToPandasDecodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfscsvtopandasdecodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`PandasToCSVEncodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspandastocsvencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`PandasToParquetEncodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspandastoparquetencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`ParquetToArrowDecodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsparquettoarrowdecodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`ParquetToPandasDecodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsparquettopandasdecodinghandler) | Helper class that provides a standard way to create an ABC using. |

### Methods

| Method | Description |
|-|-|
| [`get_pandas_storage_options()`](#get_pandas_storage_options) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `CSV` | `str` |  |
| `PARQUET` | `str` |  |
| `T` | `TypeVar` |  |

## Methods

#### get_pandas_storage_options()

```python
def get_pandas_storage_options(
    uri: str,
    data_config: flytekit.configuration.DataConfig,
    anonymous: bool,
) -> typing.Optional[typing.Dict]
```
| Parameter | Type |
|-|-|
| `uri` | `str` |
| `data_config` | `flytekit.configuration.DataConfig` |
| `anonymous` | `bool` |

## flytekit.types.structured.basic_dfs.ArrowToParquetEncodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def ArrowToParquetEncodingHandler()
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the. |


#### encode()

```python
def encode(
    ctx: flytekit.core.context_manager.FlyteContext,
    structured_dataset: flytekit.types.structured.structured_dataset.StructuredDataset,
    structured_dataset_type: flytekit.models.types.StructuredDatasetType,
) -> n: This function should return a StructuredDataset literal object. Do not confuse this with the
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `structured_dataset` | `flytekit.types.structured.structured_dataset.StructuredDataset` |
| `structured_dataset_type` | `flytekit.models.types.StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## flytekit.types.structured.basic_dfs.CSVToPandasDecodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def CSVToPandasDecodingHandler()
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal. |


#### decode()

```python
def decode(
    ctx: flytekit.core.context_manager.FlyteContext,
    flyte_value: flytekit.models.literals.StructuredDataset,
    current_task_metadata: flytekit.models.literals.StructuredDatasetMetadata,
) -> n: This function can either return an instance of the dataframe that this decoder handles, or an iterator
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `flyte_value` | `flytekit.models.literals.StructuredDataset` |
| `current_task_metadata` | `flytekit.models.literals.StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## flytekit.types.structured.basic_dfs.PandasToCSVEncodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def PandasToCSVEncodingHandler()
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the. |


#### encode()

```python
def encode(
    ctx: flytekit.core.context_manager.FlyteContext,
    structured_dataset: flytekit.types.structured.structured_dataset.StructuredDataset,
    structured_dataset_type: flytekit.models.types.StructuredDatasetType,
) -> n: This function should return a StructuredDataset literal object. Do not confuse this with the
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `structured_dataset` | `flytekit.types.structured.structured_dataset.StructuredDataset` |
| `structured_dataset_type` | `flytekit.models.types.StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## flytekit.types.structured.basic_dfs.PandasToParquetEncodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def PandasToParquetEncodingHandler()
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the. |


#### encode()

```python
def encode(
    ctx: flytekit.core.context_manager.FlyteContext,
    structured_dataset: flytekit.types.structured.structured_dataset.StructuredDataset,
    structured_dataset_type: flytekit.models.types.StructuredDatasetType,
) -> n: This function should return a StructuredDataset literal object. Do not confuse this with the
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `structured_dataset` | `flytekit.types.structured.structured_dataset.StructuredDataset` |
| `structured_dataset_type` | `flytekit.models.types.StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## flytekit.types.structured.basic_dfs.ParquetToArrowDecodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def ParquetToArrowDecodingHandler()
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal. |


#### decode()

```python
def decode(
    ctx: flytekit.core.context_manager.FlyteContext,
    flyte_value: flytekit.models.literals.StructuredDataset,
    current_task_metadata: flytekit.models.literals.StructuredDatasetMetadata,
) -> n: This function can either return an instance of the dataframe that this decoder handles, or an iterator
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `flyte_value` | `flytekit.models.literals.StructuredDataset` |
| `current_task_metadata` | `flytekit.models.literals.StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## flytekit.types.structured.basic_dfs.ParquetToPandasDecodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def ParquetToPandasDecodingHandler()
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal. |


#### decode()

```python
def decode(
    ctx: flytekit.core.context_manager.FlyteContext,
    flyte_value: flytekit.models.literals.StructuredDataset,
    current_task_metadata: flytekit.models.literals.StructuredDatasetMetadata,
) -> n: This function can either return an instance of the dataframe that this decoder handles, or an iterator
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `flyte_value` | `flytekit.models.literals.StructuredDataset` |
| `current_task_metadata` | `flytekit.models.literals.StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

