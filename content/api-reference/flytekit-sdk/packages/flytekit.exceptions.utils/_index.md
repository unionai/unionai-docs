---
title: flytekit.exceptions.utils
version: 1.16.14
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


| Parameter | Type | Description |
|-|-|-|
| `exception` | `flytekit.exceptions.user.FlyteUserException` | The exception to be annotated. |
| `fn` | `typing.Callable` | The function where the parameter is defined. |
| `param_name` | `typing.Optional[str]` | The name of the parameter in the function signature.  For example: exception: TypeError, 'a' has no type. Please add a type annotation to the input parameter. param_name: a, the position that arrow will point to. fn: &lt;function wf at 0x1065227a0&gt;  ╭─ TypeError ────────────────────────────────────────────────────────────────────────────────────╮ │ 23 @workflow(on_failure=t2)                                                                    │                                                                                                    │ │ 24 def wf(b: int = 3, a=4):                                                                    │ │                     # ^ 'a' has no type. Please add a type annotation to the input parameter.  │ ╰────────────────────────────────────────────────────────────────────────────────────────────────╯ |

#### get_source_code_from_fn()

```python
def get_source_code_from_fn(
    fn: typing.Callable,
    param_name: typing.Optional[str],
) -> (<class 'str'>, <class 'int'>)
```
Get the source code of the function and the column offset of the parameter defined in the input signature.


| Parameter | Type | Description |
|-|-|-|
| `fn` | `typing.Callable` | |
| `param_name` | `typing.Optional[str]` | |

