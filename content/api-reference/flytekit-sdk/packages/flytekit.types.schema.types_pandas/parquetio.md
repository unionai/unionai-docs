---
title: ParquetIO
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ParquetIO

**Package:** `flytekit.types.schema.types_pandas`

## Methods

| Method | Description |
|-|-|
| [`read()`](#read) |  |
| [`write()`](#write) | Writes data frame as a chunk to the local directory owned by the Schema object. |


### read()

```python
def read(
    files: os.PathLike,
    columns: typing.Optional[typing.List[str]],
    kwargs,
) -> pandas.DataFrame
```
| Parameter | Type | Description |
|-|-|-|
| `files` | `os.PathLike` | |
| `columns` | `typing.Optional[typing.List[str]]` | |
| `kwargs` | `**kwargs` | |

### write()

```python
def write(
    df: pandas.DataFrame,
    to_file: os.PathLike,
    coerce_timestamps: str,
    allow_truncated_timestamps: bool,
    kwargs,
)
```
Writes data frame as a chunk to the local directory owned by the Schema object.  Will later be uploaded to s3.


| Parameter | Type | Description |
|-|-|-|
| `df` | `pandas.DataFrame` | data frame to write as parquet |
| `to_file` | `os.PathLike` | Sink file to write the dataframe to |
| `coerce_timestamps` | `str` | format to store timestamp in parquet. 'us', 'ms', 's' are allowed values. Note: if your timestamps will lose data due to the coercion, your write will fail!  Nanoseconds are problematic in the Parquet format and will not work. See allow_truncated_timestamps. |
| `allow_truncated_timestamps` | `bool` | default False. Allow truncation when coercing timestamps to a coarser resolution. |
| `kwargs` | `**kwargs` | |

