---
title: flytekit.exceptions.utils
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.exceptions.utils

## Directory

### Errors

| Exception | Description |
|-|-|
| [`FlyteUserException`](.././flytekit.exceptions.utils#flytekitexceptionsutilsflyteuserexception) | Common base class for all non-exit exceptions. |

### Methods

| Method | Description |
|-|-|
| [`annotate_exception_with_code()`](#annotate_exception_with_code) | Annotate the exception with the source code, and will be printed in the rich panel. |
| [`get_function_param_location()`](#get_function_param_location) | Get the line and column number of the parameter in the source code of the function definition. |
| [`get_source_code_from_fn()`](#get_source_code_from_fn) | Get the source code of the function and the column offset of the parameter defined in the input signature. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SOURCE_CODE` | `str` |  |

## Methods

#### annotate_exception_with_code()

```python
def annotate_exception_with_code(
    exception: flytekit.exceptions.user.FlyteUserException,
    fn: typing.Callable,
    param_name: typing.Optional[str],
) -> flytekit.exceptions.user.FlyteUserException
```
Annotate the exception with the source code, and will be printed in the rich panel.


| Parameter | Type |
|-|-|
| `exception` | `flytekit.exceptions.user.FlyteUserException` |
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

#### get_function_param_location()

```python
def get_function_param_location(
    func: typing.Callable,
    param_name: str,
) -> (<class 'int'>, <class 'int'>)
```
Get the line and column number of the parameter in the source code of the function definition.


| Parameter | Type |
|-|-|
| `func` | `typing.Callable` |
| `param_name` | `str` |

#### get_source_code_from_fn()

```python
def get_source_code_from_fn(
    fn: typing.Callable,
    param_name: typing.Optional[str],
) -> (<class 'str'>, <class 'int'>)
```
Get the source code of the function and the column offset of the parameter defined in the input signature.


| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

## flytekit.exceptions.utils.FlyteUserException

Common base class for all non-exit exceptions.


```python
class FlyteUserException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

