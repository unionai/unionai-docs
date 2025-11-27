---
title: flyte.io
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.io


## IO data types

This package contains additional data types beyond the primitive data types in python to abstract data flow
of large datasets in Union.


## Directory

### Classes

| Class | Description |
|-|-|
| [`DataFrame`](../flyte.io/dataframe) | This is the user facing DataFrame class. |
| [`DataFrameDecoder`](../flyte.io/dataframedecoder) | Helper class that provides a standard way to create an ABC using. |
| [`DataFrameEncoder`](../flyte.io/dataframeencoder) | Helper class that provides a standard way to create an ABC using. |
| [`DataFrameTransformerEngine`](../flyte.io/dataframetransformerengine) | Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`Dir`](../flyte.io/dir) | A generic directory class representing a directory with files of a specified format. |
| [`File`](../flyte.io/file) | A generic file class representing a file with a specified format. |

### Methods

| Method | Description |
|-|-|
| [`lazy_import_dataframe_handler()`](#lazy_import_dataframe_handler) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `PARQUET` | `str` |  |

## Methods

#### lazy_import_dataframe_handler()

```python
def lazy_import_dataframe_handler()
```
