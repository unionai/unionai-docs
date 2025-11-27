---
title: flytekit.types.structured.basic_dfs
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.structured.basic_dfs

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrowToParquetEncodingHandler`](../flytekit.types.structured.basic_dfs/arrowtoparquetencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`CSVToPandasDecodingHandler`](../flytekit.types.structured.basic_dfs/csvtopandasdecodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`PandasToCSVEncodingHandler`](../flytekit.types.structured.basic_dfs/pandastocsvencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`PandasToParquetEncodingHandler`](../flytekit.types.structured.basic_dfs/pandastoparquetencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`ParquetToArrowDecodingHandler`](../flytekit.types.structured.basic_dfs/parquettoarrowdecodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`ParquetToPandasDecodingHandler`](../flytekit.types.structured.basic_dfs/parquettopandasdecodinghandler) | Helper class that provides a standard way to create an ABC using. |

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
| Parameter | Type | Description |
|-|-|-|
| `uri` | `str` | |
| `data_config` | `flytekit.configuration.DataConfig` | |
| `anonymous` | `bool` | |

