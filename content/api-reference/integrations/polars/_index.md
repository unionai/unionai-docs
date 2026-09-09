---
title: Polars
icon: book
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# Polars



## Directory

### Classes

| Class | Description |
|-|-|
| [`ParquetToPolarsDecodingHandler`](./parquettopolarsdecodinghandler) |  |
| [`ParquetToPolarsLazyFrameDecodingHandler`](./parquettopolarslazyframedecodinghandler) |  |
| [`PolarsLazyFrameToParquetEncodingHandler`](./polarslazyframetoparquetencodinghandler) |  |
| [`PolarsToParquetEncodingHandler`](./polarstoparquetencodinghandler) |  |

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
    anonymous: bool = False,
) -> typing.Dict[str, str]
```
Get storage options in a format compatible with Polars.

Polars requires storage_options to be a flat dict with string keys and values,
unlike fsspec which accepts nested dicts and complex objects.


| Parameter | Type | Description |
|-|-|-|
| `protocol` | `typing.Optional[str]` | |
| `anonymous` | `bool` | |

