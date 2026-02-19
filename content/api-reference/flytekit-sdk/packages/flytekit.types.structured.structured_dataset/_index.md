---
title: flytekit.types.structured.structured_dataset
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.structured.structured_dataset

## Directory

### Classes

| Class | Description |
|-|-|
| [`StructuredDataset`](../flytekit.types.structured.structured_dataset/structureddataset) | This is the user facing StructuredDataset class. |
| [`StructuredDatasetDecoder`](../flytekit.types.structured.structured_dataset/structureddatasetdecoder) |  |
| [`StructuredDatasetEncoder`](../flytekit.types.structured.structured_dataset/structureddatasetencoder) |  |
| [`StructuredDatasetTransformerEngine`](../flytekit.types.structured.structured_dataset/structureddatasettransformerengine) | Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |

### Errors

| Exception | Description |
|-|-|
| [`DuplicateHandlerError`](../flytekit.types.structured.structured_dataset/duplicatehandlererror) |  |

### Methods

| Method | Description |
|-|-|
| [`convert_schema_type_to_structured_dataset_type()`](#convert_schema_type_to_structured_dataset_type) |  |
| [`extract_cols_and_format()`](#extract_cols_and_format) | Helper function, just used to iterate through Annotations and extract out the following information:. |
| [`flatten_dict()`](#flatten_dict) |  |
| [`get_supported_types()`](#get_supported_types) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `CSV` | `str` |  |
| `DF` | `TypeVar` |  |
| `GENERIC_FORMAT` | `str` |  |
| `GENERIC_PROTOCOL` | `str` |  |
| `MESSAGEPACK` | `str` |  |
| `PARQUET` | `str` |  |
| `T` | `TypeVar` |  |
| `flyte_dataset_transformer` | `StructuredDatasetTransformerEngine` |  |

## Methods

#### convert_schema_type_to_structured_dataset_type()

```python
def convert_schema_type_to_structured_dataset_type(
    column_type: int,
) -> int
```
| Parameter | Type | Description |
|-|-|-|
| `column_type` | `int` | |

#### extract_cols_and_format()

```python
def extract_cols_and_format(
    t: typing.Any,
) -> typing.Tuple[Type[T], Optional[typing.OrderedDict[str, Type]], Optional[str], Optional['pa.lib.Schema']]
```
Helper function, just used to iterate through Annotations and extract out the following information:
  - base type, if not Annotated, it will just be the type that was passed in.
  - column information, as a collections.OrderedDict,
  - the storage format, as a ``StructuredDatasetFormat`` (str),
  - pa.lib.Schema

If more than one of any type of thing is found, an error will be raised.
If no instances of a given type are found, then None will be returned.

If we add more things, we should put all the returned items in a dataclass instead of just a tuple.



| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Any` | The incoming type which may or may not be Annotated :return: Tuple representing the original type, optional OrderedDict of columns, optional str for the format, optional pyarrow Schema |

#### flatten_dict()

```python
def flatten_dict(
    sub_dict: dict,
    parent_key: str,
) -> typing.Dict
```
| Parameter | Type | Description |
|-|-|-|
| `sub_dict` | `dict` | |
| `parent_key` | `str` | |

#### get_supported_types()

```python
def get_supported_types()
```
