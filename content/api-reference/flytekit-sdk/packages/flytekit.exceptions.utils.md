---
title: flytekit.exceptions.utils
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.exceptions.utils

## Directory

### Methods

| Method | Description |
|-|-|
| [`annotate_exception_with_code()`](#annotate_exception_with_code) | Annotate the exception with the source code, and will be printed in the rich panel. |
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

