---
title: flytekit.clis.sdk_in_container.utils
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekit.clis.sdk_in_container.utils

## Directory

### Classes

| Class | Description |
|-|-|
| [`ErrorHandlingCommand`](./flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilserrorhandlingcommand) | Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way. |
| [`PyFlyteParams`](./flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilspyflyteparams) |  |

### Methods

| Method | Description |
|-|-|
| [`get_option_from_metadata()`](#get_option_from_metadata) |  |
| [`make_click_option_field()`](#make_click_option_field) |  |
| [`pretty_print_exception()`](#pretty_print_exception) | This method will print the exception in a nice way. |
| [`pretty_print_grpc_error()`](#pretty_print_grpc_error) | This method will print the grpc error that us more human readable. |
| [`pretty_print_traceback()`](#pretty_print_traceback) | This method will print the Traceback of an error. |
| [`remove_unwanted_traceback_frames()`](#remove_unwanted_traceback_frames) | Custom function to remove certain frames from the traceback. |
| [`validate_package()`](#validate_package) | This method will validate the packages passed in by the user. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SOURCE_CODE` | `str` |  |

## Methods

#### get_option_from_metadata()

```python
def get_option_from_metadata(
    metadata: mappingproxy,
) -> click.core.Option
```
| Parameter | Type | Description |
|-|-|-|
| `metadata` | `mappingproxy` | |

#### make_click_option_field()

```python
def make_click_option_field(
    o: click.core.Option,
) -> dataclasses.Field
```
| Parameter | Type | Description |
|-|-|-|
| `o` | `click.core.Option` | |

#### pretty_print_exception()

```python
def pretty_print_exception(
    e: Exception,
    verbosity: int = 1,
)
```
This method will print the exception in a nice way. It will also check if the exception is a grpc.RpcError and
print it in a human-readable way.


| Parameter | Type | Description |
|-|-|-|
| `e` | `Exception` | |
| `verbosity` | `int` | |

#### pretty_print_grpc_error()

```python
def pretty_print_grpc_error(
    e: grpc.RpcError,
)
```
This method will print the grpc error that us more human readable.


| Parameter | Type | Description |
|-|-|-|
| `e` | `grpc.RpcError` | |

#### pretty_print_traceback()

```python
def pretty_print_traceback(
    e: Exception,
    verbosity: int = 1,
)
```
This method will print the Traceback of an error.
Print the traceback in a nice formatted way if verbose is set to True.


| Parameter | Type | Description |
|-|-|-|
| `e` | `Exception` | |
| `verbosity` | `int` | |

#### remove_unwanted_traceback_frames()

```python
def remove_unwanted_traceback_frames(
    tb: traceback,
    unwanted_module_names: typing.List[str],
) -> traceback
```
Custom function to remove certain frames from the traceback.


| Parameter | Type | Description |
|-|-|-|
| `tb` | `traceback` | |
| `unwanted_module_names` | `typing.List[str]` | |

#### validate_package()

```python
def validate_package(
    ctx,
    param,
    values,
)
```
This method will validate the packages passed in by the user. It will check that the packages are in the correct
format, and will also split the packages if the user passed in a comma separated list.


| Parameter | Type | Description |
|-|-|-|
| `ctx` |  | |
| `param` |  | |
| `values` |  | |

## flytekit.clis.sdk_in_container.utils.ErrorHandlingCommand

Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way.


### Parameters

```python
class ErrorHandlingCommand(
    *args: Any,
    **kwargs: Any,
)
```
Create RichGroup instance.


| Parameter | Type | Description |
|-|-|-|
| `*args` | `Any` | |
| `**kwargs` | `Any` | |

### Methods

| Method | Description |
|-|-|
| [`invoke()`](#invoke) | Given a context, this invokes the attached callback (if it exists). |


#### invoke()

```python
def invoke(
    ctx: click.core.Context,
) -> typing.Any
```
Given a context, this invokes the attached callback (if it exists)
in the right way.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

## flytekit.clis.sdk_in_container.utils.PyFlyteParams

### Parameters

```python
class PyFlyteParams(
    config_file: typing.Optional[str] = None,
    verbose: bool = False,
    pkgs: typing.List[str] = <factory>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Optional[str]` | |
| `verbose` | `bool` | |
| `pkgs` | `typing.List[str]` | |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |


#### from_dict()

```python
def from_dict(
    d: typing.Dict[str, typing.Any],
) -> PyFlyteParams
```
| Parameter | Type | Description |
|-|-|-|
| `d` | `typing.Dict[str, typing.Any]` | |

