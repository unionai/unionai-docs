---
title: flytekit.types.structured.basic_dfs
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.structured.basic_dfs

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrowToParquetEncodingHandler`](../flytekit.types.structured.basic_dfs/arrowtoparquetencodinghandler) |  |
| [`CSVToPandasDecodingHandler`](../flytekit.types.structured.basic_dfs/csvtopandasdecodinghandler) |  |
| [`PandasToCSVEncodingHandler`](../flytekit.types.structured.basic_dfs/pandastocsvencodinghandler) |  |
| [`PandasToParquetEncodingHandler`](../flytekit.types.structured.basic_dfs/pandastoparquetencodinghandler) |  |
| [`ParquetToArrowDecodingHandler`](../flytekit.types.structured.basic_dfs/parquettoarrowdecodinghandler) |  |
| [`ParquetToPandasDecodingHandler`](../flytekit.types.structured.basic_dfs/parquettopandasdecodinghandler) |  |

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

