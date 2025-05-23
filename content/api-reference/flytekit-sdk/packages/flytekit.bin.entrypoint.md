---
title: flytekit.bin.entrypoint
version: 0.1.dev2192+g7c539c3.d20250403
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
| `SERIALIZED_CONTEXT_ENV_VAR` | `str` |  |

## Methods

#### get_container_error_timestamp()

```python
def get_container_error_timestamp(
    e: typing.Optional[Exception],
) -> n: Timestamp to be reported in ContainerError
```
Get timestamp for ContainerError.

If a flyte exception is passed, use its timestamp, otherwise, use the current time.



| Parameter | Type |
|-|-|
| `e` | `typing.Optional[Exception]` |

#### get_one_of()

```python
def get_one_of(
    args,
) -> n: The first defined value in the environment, or an empty string if nothing is found.
```
Helper function to iterate through a series of different environment variables. This function exists because for
some settings reference multiple environment variables for legacy reasons.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |

#### get_traceback_str()

```python
def get_traceback_str(
    e: Exception,
) -> str
```
| Parameter | Type |
|-|-|
| `e` | `Exception` |

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
| Parameter | Type |
|-|-|
| `raw_output_data_prefix` | `typing.Optional[str]` |
| `checkpoint_path` | `typing.Optional[str]` |
| `prev_checkpoint` | `typing.Optional[str]` |

#### setup_execution()

```python
def setup_execution(
    raw_output_data_prefix: str,
    output_metadata_prefix: typing.Optional[str],
    checkpoint_path: typing.Optional[str],
    prev_checkpoint: typing.Optional[str],
    dynamic_addl_distro: typing.Optional[str],
    dynamic_dest_dir: typing.Optional[str],
) -> n:
```
| Parameter | Type |
|-|-|
| `raw_output_data_prefix` | `str` |
| `output_metadata_prefix` | `typing.Optional[str]` |
| `checkpoint_path` | `typing.Optional[str]` |
| `prev_checkpoint` | `typing.Optional[str]` |
| `dynamic_addl_distro` | `typing.Optional[str]` |
| `dynamic_dest_dir` | `typing.Optional[str]` |

