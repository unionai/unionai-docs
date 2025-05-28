---
title: flytekit.tools.module_loader
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.tools.module_loader

## Directory

### Methods

| Method | Description |
|-|-|
| [`add_sys_path()`](#add_sys_path) | Temporarily add given path to `sys. |
| [`just_load_modules()`](#just_load_modules) | This one differs from the above in that we don't yield anything, just load all the modules. |
| [`load_object_from_module()`](#load_object_from_module) | TODO: Handle corner cases, like where the first part is [] maybe. |
| [`module_load_error_handler()`](#module_load_error_handler) |  |


## Methods

#### add_sys_path()

```python
def add_sys_path(
    path: typing.Union[str, os.PathLike],
) -> typing.Iterator[NoneType]
```
Temporarily add given path to `sys.path`.


| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |

#### just_load_modules()

```python
def just_load_modules(
    pkgs: typing.List[str],
)
```
This one differs from the above in that we don't yield anything, just load all the modules.


| Parameter | Type |
|-|-|
| `pkgs` | `typing.List[str]` |

#### load_object_from_module()

```python
def load_object_from_module(
    object_location: str,
) -> typing.Any
```
TODO: Handle corner cases, like where the first part is [] maybe


| Parameter | Type |
|-|-|
| `object_location` | `str` |

#### module_load_error_handler()

```python
def module_load_error_handler(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

