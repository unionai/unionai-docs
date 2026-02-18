---
title: flyteplugins.polars.df_transformer
version: 2.0.0b60
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyteplugins.polars.df_transformer

## Directory

### Classes

| Class | Description |
|-|-|
| [`ParquetToPolarsDecodingHandler`](../flyteplugins.polars.df_transformer/parquettopolarsdecodinghandler) |  |
| [`ParquetToPolarsLazyFrameDecodingHandler`](../flyteplugins.polars.df_transformer/parquettopolarslazyframedecodinghandler) |  |
| [`PolarsLazyFrameToParquetEncodingHandler`](../flyteplugins.polars.df_transformer/polarslazyframetoparquetencodinghandler) |  |
| [`PolarsToParquetEncodingHandler`](../flyteplugins.polars.df_transformer/polarstoparquetencodinghandler) |  |

### Methods

| Method | Description |
|-|-|
| [`get_polars_storage_options()`](#get_polars_storage_options) | Get storage options in a format compatible with Polars. |


### Variables

| Property | Type | Description |
|-|-|-|
| `PARQUET` | `str` |  |

## Methods

#### get_polars_storage_options()

```python
def get_polars_storage_options(
    protocol: typing.Optional[str],
    anonymous: bool,
) -> typing.Dict[str, str]
```
Get storage options in a format compatible with Polars.

Polars requires storage_options to be a flat dict with string keys and values,
unlike fsspec which accepts nested dicts and complex objects.


| Parameter | Type | Description |
|-|-|-|
| `protocol` | `typing.Optional[str]` | |
| `anonymous` | `bool` | |

