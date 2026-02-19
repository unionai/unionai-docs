---
title: TFRecordDatasetConfig
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TFRecordDatasetConfig

**Package:** `flytekit.extras.tensorflow.record`

TFRecordDatasetConfig can be used while creating tf.data.TFRecordDataset comprising
record of one or more TFRecord files.



```python
class TFRecordDatasetConfig(
    compression_type: typing.Optional[str],
    buffer_size: typing.Optional[int],
    num_parallel_reads: typing.Optional[int],
    name: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `compression_type` | `typing.Optional[str]` | A scalar evaluating to one of "" (no compression), "ZLIB", or "GZIP". |
| `buffer_size` | `typing.Optional[int]` | The number of bytes in the read buffer. If None, a sensible default for both local and remote file systems is used. |
| `num_parallel_reads` | `typing.Optional[int]` | The number of files to read in parallel. If greater than one, the record of files read in parallel are outputted in an interleaved order. |
| `name` | `typing.Optional[str]` | A name for the operation. |

## Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` | |
| `infer_missing` |  | |

### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` | |
| `parse_float` |  | |
| `parse_int` |  | |
| `parse_constant` |  | |
| `infer_missing` |  | |
| `kw` |  | |

### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type | Description |
|-|-|-|
| `infer_missing` | `bool` | |
| `only` |  | |
| `exclude` |  | |
| `many` | `bool` | |
| `context` |  | |
| `load_only` |  | |
| `dump_only` |  | |
| `partial` | `bool` | |
| `unknown` |  | |

### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type | Description |
|-|-|-|
| `encode_json` |  | |

### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `skipkeys` | `bool` | |
| `ensure_ascii` | `bool` | |
| `check_circular` | `bool` | |
| `allow_nan` | `bool` | |
| `indent` | `typing.Union[int, str, NoneType]` | |
| `separators` | `typing.Tuple[str, str]` | |
| `default` | `typing.Callable` | |
| `sort_keys` | `bool` | |
| `kw` |  | |

