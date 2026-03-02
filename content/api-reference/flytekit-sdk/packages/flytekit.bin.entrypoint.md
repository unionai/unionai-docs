---
title: flytekit.bin.entrypoint
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.bin.entrypoint

## Directory

### Methods

| Method | Description |
|-|-|
| [`get_container_error_timestamp()`](#get_container_error_timestamp) | Get timestamp for ContainerError. |
| [`get_one_of()`](#get_one_of) | Helper function to iterate through a series of different environment variables. |
| [`get_traceback_str()`](#get_traceback_str) |  |
| [`get_version_message()`](#get_version_message) |  |
| [`normalize_inputs()`](#normalize_inputs) |  |
| [`setup_execution()`](#setup_execution) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `FLYTE_FAIL_ON_ERROR` | `str` |  |
| `RUNTIME_PACKAGES_ENV_NAME` | `str` |  |
| `SERIALIZED_CONTEXT_ENV_VAR` | `str` |  |

## Methods

#### get_container_error_timestamp()

```python
def get_container_error_timestamp(
    e: typing.Optional[Exception],
) -> google.protobuf.timestamp_pb2.Timestamp
```
Get timestamp for ContainerError.

If a flyte exception is passed, use its timestamp, otherwise, use the current time.



| Parameter | Type | Description |
|-|-|-|
| `e` | `typing.Optional[Exception]` | Exception that has occurred. Optional. :return: Timestamp to be reported in ContainerError |

#### get_one_of()

```python
def get_one_of(
    args,
) -> str
```
Helper function to iterate through a series of different environment variables. This function exists because for
some settings reference multiple environment variables for legacy reasons.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | List of environment variables to look for. :return: The first defined value in the environment, or an empty string if nothing is found. |

#### get_traceback_str()

```python
def get_traceback_str(
    e: Exception,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `e` | `Exception` | |

#### get_version_message()

```python
def get_version_message()
```
#### normalize_inputs()

```python
def normalize_inputs(
    raw_output_data_prefix: typing.Optional[str],
    checkpoint_path: typing.Optional[str],
    prev_checkpoint: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `raw_output_data_prefix` | `typing.Optional[str]` | |
| `checkpoint_path` | `typing.Optional[str]` | |
| `prev_checkpoint` | `typing.Optional[str]` | |

#### setup_execution()

```python
def setup_execution(
    raw_output_data_prefix: str,
    output_metadata_prefix: typing.Optional[str],
    checkpoint_path: typing.Optional[str],
    prev_checkpoint: typing.Optional[str],
    dynamic_addl_distro: typing.Optional[str],
    dynamic_dest_dir: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `raw_output_data_prefix` | `str` | Where to write offloaded data (files, directories, dataframes). |
| `output_metadata_prefix` | `typing.Optional[str]` | Where to write primitive outputs. |
| `checkpoint_path` | `typing.Optional[str]` | |
| `prev_checkpoint` | `typing.Optional[str]` | |
| `dynamic_addl_distro` | `typing.Optional[str]` | Works in concert with the other dynamic arg. If present, indicates that if a dynamic task were to run, it should set fast serialize to true and use these values in FastSerializationSettings |
| `dynamic_dest_dir` | `typing.Optional[str]` | See above. :return: |

