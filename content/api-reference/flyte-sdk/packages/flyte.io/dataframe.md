---
title: DataFrame
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# DataFrame

**Package:** `flyte.io`

A Flyte meta DataFrame object, that wraps all other dataframe types (usually available as plugins, pandas.DataFrame
and pyarrow.Table are supported natively, just install these libraries).

Known eco-system plugins that supply other dataframe encoding plugins are,
1. `flyteplugins-polars` - pl.DataFrame
2. `flyteplugins-spark` - pyspark.DataFrame

You can add other implementations by extending following `flyte.io.extend`.

The Flyte DataFrame object serves 2 main purposes:
1. Interoperability between various dataframe objects. A task can generate a pandas.DataFrame and another task
 can accept a flyte.io.DataFrame, which can be converted to any dataframe.
2. Allows for non materialized access to DataFrame objects. So, for example you can accept any dataframe as a
flyte.io.DataFrame and this is just a reference and will not materialize till you force `.all()` or `.iter()` etc


## Parameters

```python
class DataFrame(
    uri: typing.Optional[str],
    format: typing.Optional[str],
    hash: typing.Optional[str],
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `uri` | `typing.Optional[str]` | |
| `format` | `typing.Optional[str]` | |
| `hash` | `typing.Optional[str]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `lazy_uploader` | `None` |  |
| `literal` | `None` |  |
| `metadata` | `None` |  |
| `val` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`all_sync()`](#all_sync) |  |
| [`column_names()`](#column_names) |  |
| [`columns()`](#columns) |  |
| [`deserialize_dataframe()`](#deserialize_dataframe) |  |
| [`from_df()`](#from_df) | Deprecated: Please use wrap_df, as that is the right name. |
| [`from_existing_remote()`](#from_existing_remote) | Create a DataFrame reference from an existing remote dataframe. |
| [`from_local()`](#from_local) | This method is useful to upload the dataframe eagerly and get the actual DataFrame. |
| [`from_local_sync()`](#from_local_sync) | This method is useful to upload the dataframe eagerly and get the actual DataFrame. |
| [`iter()`](#iter) |  |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialize private attributes. |
| [`open()`](#open) | Load the handler if needed. |
| [`schema_match()`](#schema_match) |  |
| [`serialize_dataframe()`](#serialize_dataframe) |  |
| [`set_literal()`](#set_literal) | A public wrapper method to set the DataFrame Literal. |
| [`wrap_df()`](#wrap_df) | Wrapper to create a DataFrame from a dataframe. |


### all()

```python
def all()
```
### all_sync()

```python
def all_sync()
```
### column_names()

```python
def column_names()
```
### columns()

```python
def columns()
```
### deserialize_dataframe()

```python
def deserialize_dataframe(
    info,
) -> DataFrame
```
| Parameter | Type | Description |
|-|-|-|
| `info` |  | |

### from_df()

```python
def from_df(
    val: typing.Optional[typing.Any],
    uri: typing.Optional[str],
) -> DataFrame
```
Deprecated: Please use wrap_df, as that is the right name.

Creates a new Flyte DataFrame from any registered DataFrame type (For example, pandas.DataFrame).
Other dataframe types are usually supported through plugins like `flyteplugins-polars`, `flyteplugins-spark`
etc.


| Parameter | Type | Description |
|-|-|-|
| `val` | `typing.Optional[typing.Any]` | |
| `uri` | `typing.Optional[str]` | |

### from_existing_remote()

```python
def from_existing_remote(
    remote_path: str,
    format: typing.Optional[str],
    kwargs,
) -> 'DataFrame'
```
Create a DataFrame reference from an existing remote dataframe.



| Parameter | Type | Description |
|-|-|-|
| `remote_path` | `str` | The remote path to the existing dataframe |
| `format` | `typing.Optional[str]` | Format of the stored dataframe |
| `kwargs` | `**kwargs` | |

### from_local()

```python
def from_local(
    df: typing.Any,
    columns: typing.OrderedDict[str, type[typing.Any]] | None,
    remote_destination: str | None,
    hash_method: HashMethod | str | None,
) -> DataFrame
```
This method is useful to upload the dataframe eagerly and get the actual DataFrame.

This is useful to upload small local datasets onto Flyte and also upload dataframes from notebooks. This
uses signed urls and is thus not the most efficient way of uploading.

In tasks (at runtime) it uses the task context and the underlying fast storage sub-system to upload the data.

At runtime it is recommended to use `DataFrame.wrap_df` as it is simpler.

Example (With hash_method for cache key computation):

```python
import pandas as pd
from flyte.io import DataFrame, HashFunction

def hash_pandas_dataframe(df: pd.DataFrame) -> str:
    return str(pd.util.hash_pandas_object(df).sum())

@env.task
async def foo() -> DataFrame:
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    hash_method = HashFunction.from_fn(hash_pandas_dataframe)
    return await DataFrame.from_local(df, hash_method=hash_method)
```



| Parameter | Type | Description |
|-|-|-|
| `df` | `typing.Any` | The dataframe object to be uploaded and converted. |
| `columns` | `typing.OrderedDict[str, type[typing.Any]] \| None` | Optionally, any column information to be stored as part of the metadata |
| `remote_destination` | `str \| None` | Optional destination URI to upload to, if not specified, this is automatically determined based on the current context. For example, locally it will use flyte:// automatic data management system to upload data (this is slow and useful for smaller datasets). On remote it will use the storage configuration and the raw data directory setting in the task context. |
| `hash_method` | `HashMethod \| str \| None` | Optional HashMethod or string to use for cache key computation. If a string is provided, it will be used as a precomputed cache key. If a HashMethod is provided, it will compute the hash from the dataframe. If not specified, the cache key will be based on dataframe attributes.  Returns: DataFrame object. |

### from_local_sync()

```python
def from_local_sync(
    df: typing.Any,
    columns: typing.OrderedDict[str, type[typing.Any]] | None,
    remote_destination: str | None,
    hash_method: HashMethod | str | None,
) -> DataFrame
```
This method is useful to upload the dataframe eagerly and get the actual DataFrame.

This is useful to upload small local datasets onto Flyte and also upload dataframes from notebooks. This
uses signed urls and is thus not the most efficient way of uploading.

In tasks (at runtime) it uses the task context and the underlying fast storage sub-system to upload the data.

At runtime it is recommended to use `DataFrame.wrap_df` as it is simpler.

Example (With hash_method for cache key computation):

```python
import pandas as pd
from flyte.io import DataFrame, HashFunction

def hash_pandas_dataframe(df: pd.DataFrame) -> str:
    return str(pd.util.hash_pandas_object(df).sum())

@env.task
def foo() -> DataFrame:
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    hash_method = HashFunction.from_fn(hash_pandas_dataframe)
    return DataFrame.from_local_sync(df, hash_method=hash_method)
```



| Parameter | Type | Description |
|-|-|-|
| `df` | `typing.Any` | The dataframe object to be uploaded and converted. |
| `columns` | `typing.OrderedDict[str, type[typing.Any]] \| None` | Optionally, any column information to be stored as part of the metadata |
| `remote_destination` | `str \| None` | Optional destination URI to upload to, if not specified, this is automatically determined based on the current context. For example, locally it will use flyte:// automatic data management system to upload data (this is slow and useful for smaller datasets). On remote it will use the storage configuration and the raw data directory setting in the task context. |
| `hash_method` | `HashMethod \| str \| None` | Optional HashMethod or string to use for cache key computation. If a string is provided, it will be used as a precomputed cache key. If a HashMethod is provided, it will compute the hash from the dataframe. If not specified, the cache key will be based on dataframe attributes.  Returns: DataFrame object. |

### iter()

```python
def iter()
```
### model_post_init()

```python
def model_post_init(
    context: Any,
)
```
This function is meant to behave like a BaseModel method to initialize private attributes.

It takes context as an argument since that's what pydantic-core passes when calling it.



| Parameter | Type | Description |
|-|-|-|
| `context` | `Any` | The context. |

### open()

```python
def open(
    dataframe_type: Type[DF],
)
```
Load the handler if needed. For the use case like:
@task
def t1(df: DataFrame):
  import pandas as pd
  df.open(pd.DataFrame).all()

pandas is imported inside the task, so panda handler won't be loaded during deserialization in type engine.


| Parameter | Type | Description |
|-|-|-|
| `dataframe_type` | `Type[DF]` | |

### schema_match()

```python
def schema_match(
    incoming: dict,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `incoming` | `dict` | |

### serialize_dataframe()

```python
def serialize_dataframe()
```
### set_literal()

```python
def set_literal(
    expected: types_pb2.LiteralType,
)
```
A public wrapper method to set the DataFrame Literal.

This method provides external access to the internal _set_literal method.


| Parameter | Type | Description |
|-|-|-|
| `expected` | `types_pb2.LiteralType` | |

### wrap_df()

```python
def wrap_df(
    val: typing.Optional[typing.Any],
    uri: typing.Optional[str],
) -> DataFrame
```
Wrapper to create a DataFrame from a dataframe.
Other dataframe types are usually supported through plugins like `flyteplugins-polars`, `flyteplugins-spark`
etc.


| Parameter | Type | Description |
|-|-|-|
| `val` | `typing.Optional[typing.Any]` | |
| `uri` | `typing.Optional[str]` | |

