---
title: flytekitplugins.polars.sd_transformers
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.polars.sd_transformers

## Directory

### Classes

| Class | Description |
|-|-|
| [`ParquetToPolarsDataFrameDecodingHandler`](.././flytekitplugins.polars.sd_transformers#flytekitpluginspolarssd_transformersparquettopolarsdataframedecodinghandler) |  |
| [`ParquetToPolarsLazyFrameDecodingHandler`](.././flytekitplugins.polars.sd_transformers#flytekitpluginspolarssd_transformersparquettopolarslazyframedecodinghandler) |  |
| [`PolarsDataFrameRenderer`](.././flytekitplugins.polars.sd_transformers#flytekitpluginspolarssd_transformerspolarsdataframerenderer) | The Polars DataFrame summary statistics are rendered as an HTML table. |
| [`PolarsDataFrameToParquetEncodingHandler`](.././flytekitplugins.polars.sd_transformers#flytekitpluginspolarssd_transformerspolarsdataframetoparquetencodinghandler) |  |
| [`PolarsLazyFrameToParquetEncodingHandler`](.././flytekitplugins.polars.sd_transformers#flytekitpluginspolarssd_transformerspolarslazyframetoparquetencodinghandler) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `PARQUET` | `str` |  |

## flytekitplugins.polars.sd_transformers.ParquetToPolarsDataFrameDecodingHandler

```python
def ParquetToPolarsDataFrameDecodingHandler()
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

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
) -> polars.dataframe.frame.DataFrame
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `flyte_value` | `flytekit.models.literals.StructuredDataset` | This will be a Flyte IDL StructuredDataset Literal - do not confuse this with the StructuredDataset class defined also in this module. |
| `current_task_metadata` | `flytekit.models.literals.StructuredDatasetMetadata` | Metadata object containing the type (and columns if any) for the currently executing task. This type may have more or less information than the type information bundled inside the incoming flyte_value. :return: This function can either return an instance of the dataframe that this decoder handles, or an iterator of those dataframes. |

## flytekitplugins.polars.sd_transformers.ParquetToPolarsLazyFrameDecodingHandler

```python
def ParquetToPolarsLazyFrameDecodingHandler()
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

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
) -> polars.lazyframe.frame.LazyFrame
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `flyte_value` | `flytekit.models.literals.StructuredDataset` | This will be a Flyte IDL StructuredDataset Literal - do not confuse this with the StructuredDataset class defined also in this module. |
| `current_task_metadata` | `flytekit.models.literals.StructuredDatasetMetadata` | Metadata object containing the type (and columns if any) for the currently executing task. This type may have more or less information than the type information bundled inside the incoming flyte_value. :return: This function can either return an instance of the dataframe that this decoder handles, or an iterator of those dataframes. |

## flytekitplugins.polars.sd_transformers.PolarsDataFrameRenderer

The Polars DataFrame summary statistics are rendered as an HTML table.



### Methods

| Method | Description |
|-|-|
| [`to_html()`](#to_html) |  |


#### to_html()

```python
def to_html(
    df: typing.Union[polars.dataframe.frame.DataFrame, polars.lazyframe.frame.LazyFrame],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `df` | `typing.Union[polars.dataframe.frame.DataFrame, polars.lazyframe.frame.LazyFrame]` | |

## flytekitplugins.polars.sd_transformers.PolarsDataFrameToParquetEncodingHandler

```python
def PolarsDataFrameToParquetEncodingHandler()
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

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
) -> flytekit.models.literals.StructuredDataset
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `structured_dataset` | `flytekit.types.structured.structured_dataset.StructuredDataset` | This is a StructuredDataset wrapper object. See more info above. |
| `structured_dataset_type` | `flytekit.models.types.StructuredDatasetType` | This the StructuredDatasetType, as found in the LiteralType of the interface of the task that invoked this encoding call. It is passed along to encoders so that authors of encoders can include it in the returned literals.StructuredDataset. See the IDL for more information on why this literal in particular carries the type information along with it. If the encoder doesn't supply it, it will also be filled in after the encoder runs by the transformer engine. :return: This function should return a StructuredDataset literal object. Do not confuse this with the StructuredDataset wrapper class used as input to this function - that is the user facing Python class. This function needs to return the IDL StructuredDataset. |

## flytekitplugins.polars.sd_transformers.PolarsLazyFrameToParquetEncodingHandler

```python
def PolarsLazyFrameToParquetEncodingHandler()
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

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
) -> flytekit.models.literals.StructuredDataset
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `structured_dataset` | `flytekit.types.structured.structured_dataset.StructuredDataset` | This is a StructuredDataset wrapper object. See more info above. |
| `structured_dataset_type` | `flytekit.models.types.StructuredDatasetType` | This the StructuredDatasetType, as found in the LiteralType of the interface of the task that invoked this encoding call. It is passed along to encoders so that authors of encoders can include it in the returned literals.StructuredDataset. See the IDL for more information on why this literal in particular carries the type information along with it. If the encoder doesn't supply it, it will also be filled in after the encoder runs by the transformer engine. :return: This function should return a StructuredDataset literal object. Do not confuse this with the StructuredDataset wrapper class used as input to this function - that is the user facing Python class. This function needs to return the IDL StructuredDataset. |

