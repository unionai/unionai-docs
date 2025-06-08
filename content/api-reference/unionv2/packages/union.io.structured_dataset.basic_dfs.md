---
title: union.io.structured_dataset.basic_dfs
version: 0.1.0
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# union.io.structured_dataset.basic_dfs

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrowToParquetEncodingHandler`](.././union.io.structured_dataset.basic_dfs#unioniostructured_datasetbasic_dfsarrowtoparquetencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`CSVToPandasDecodingHandler`](.././union.io.structured_dataset.basic_dfs#unioniostructured_datasetbasic_dfscsvtopandasdecodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`PandasToCSVEncodingHandler`](.././union.io.structured_dataset.basic_dfs#unioniostructured_datasetbasic_dfspandastocsvencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`PandasToParquetEncodingHandler`](.././union.io.structured_dataset.basic_dfs#unioniostructured_datasetbasic_dfspandastoparquetencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`ParquetToArrowDecodingHandler`](.././union.io.structured_dataset.basic_dfs#unioniostructured_datasetbasic_dfsparquettoarrowdecodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`ParquetToPandasDecodingHandler`](.././union.io.structured_dataset.basic_dfs#unioniostructured_datasetbasic_dfsparquettopandasdecodinghandler) | Helper class that provides a standard way to create an ABC using. |

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
    data_config,
    anonymous: bool,
) -> typing.Optional[typing.Dict]
```
| Parameter | Type |
|-|-|
| `uri` | `str` |
| `data_config` |  |
| `anonymous` | `bool` |

## union.io.structured_dataset.basic_dfs.ArrowToParquetEncodingHandler

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
    structured_dataset: union.io.structured_dataset.structured_dataset.StructuredDataset,
    structured_dataset_type: flyteidl.core.types_pb2.StructuredDatasetType,
) -> flyteidl.core.literals_pb2.StructuredDataset
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `structured_dataset` | `union.io.structured_dataset.structured_dataset.StructuredDataset` |
| `structured_dataset_type` | `flyteidl.core.types_pb2.StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## union.io.structured_dataset.basic_dfs.CSVToPandasDecodingHandler

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
    proto_value: flyteidl.core.literals_pb2.StructuredDataset,
    current_task_metadata: flyteidl.core.literals_pb2.StructuredDatasetMetadata,
) -> pd.DataFrame
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `proto_value` | `flyteidl.core.literals_pb2.StructuredDataset` |
| `current_task_metadata` | `flyteidl.core.literals_pb2.StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## union.io.structured_dataset.basic_dfs.PandasToCSVEncodingHandler

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
    structured_dataset: union.io.structured_dataset.structured_dataset.StructuredDataset,
    structured_dataset_type: flyteidl.core.types_pb2.StructuredDatasetType,
) -> flyteidl.core.literals_pb2.StructuredDataset
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `structured_dataset` | `union.io.structured_dataset.structured_dataset.StructuredDataset` |
| `structured_dataset_type` | `flyteidl.core.types_pb2.StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## union.io.structured_dataset.basic_dfs.PandasToParquetEncodingHandler

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
    structured_dataset: union.io.structured_dataset.structured_dataset.StructuredDataset,
    structured_dataset_type: flyteidl.core.types_pb2.StructuredDatasetType,
) -> flyteidl.core.literals_pb2.StructuredDataset
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `structured_dataset` | `union.io.structured_dataset.structured_dataset.StructuredDataset` |
| `structured_dataset_type` | `flyteidl.core.types_pb2.StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## union.io.structured_dataset.basic_dfs.ParquetToArrowDecodingHandler

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
    proto_value: flyteidl.core.literals_pb2.StructuredDataset,
    current_task_metadata: flyteidl.core.literals_pb2.StructuredDatasetMetadata,
) -> pa.Table
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `proto_value` | `flyteidl.core.literals_pb2.StructuredDataset` |
| `current_task_metadata` | `flyteidl.core.literals_pb2.StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

## union.io.structured_dataset.basic_dfs.ParquetToPandasDecodingHandler

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
    flyte_value: flyteidl.core.literals_pb2.StructuredDataset,
    current_task_metadata: flyteidl.core.literals_pb2.StructuredDatasetMetadata,
) -> pd.DataFrame
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `flyte_value` | `flyteidl.core.literals_pb2.StructuredDataset` |
| `current_task_metadata` | `flyteidl.core.literals_pb2.StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` |  |  |
| `python_type` |  |  |
| `supported_format` |  |  |

