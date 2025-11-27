---
title: flytekit.image_spec.default_builder
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.image_spec.default_builder

## Directory

### Classes

| Class | Description |
|-|-|
| [`DefaultImageBuilder`](../flytekit.image_spec.default_builder/defaultimagebuilder) | Image builder using Docker and buildkit. |

### Methods

| Method | Description |
|-|-|
| [`create_docker_context()`](#create_docker_context) | Populate tmp_dir with Dockerfile as specified by the `image_spec`. |
| [`get_flytekit_for_pypi()`](#get_flytekit_for_pypi) | Get flytekit version on PyPI. |
| [`prepare_poetry_lock_command()`](#prepare_poetry_lock_command) |  |
| [`prepare_python_executable()`](#prepare_python_executable) |  |
| [`prepare_python_install()`](#prepare_python_install) |  |
| [`prepare_uv_lock_command()`](#prepare_uv_lock_command) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_MICROMAMBA_IMAGE` | `str` |  |
| `DEFAULT_UV_IMAGE` | `str` |  |

## Methods

#### create_docker_context()

```python
def create_docker_context(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib.Path,
)
```
Populate tmp_dir with Dockerfile as specified by the `image_spec`.


| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | |
| `tmp_dir` | `pathlib.Path` | |

#### get_flytekit_for_pypi()

```python
def get_flytekit_for_pypi()
```
Get flytekit version on PyPI.


#### prepare_poetry_lock_command()

```python
def prepare_poetry_lock_command(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib.Path,
) -> typing.Tuple[string.Template, typing.List[str]]
```
| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | |
| `tmp_dir` | `pathlib.Path` | |

#### prepare_python_executable()

```python
def prepare_python_executable(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> flytekit.image_spec.default_builder._PythonInstallTemplate
```
| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | |

#### prepare_python_install()

```python
def prepare_python_install(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib.Path,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | |
| `tmp_dir` | `pathlib.Path` | |

#### prepare_uv_lock_command()

```python
def prepare_uv_lock_command(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib.Path,
) -> typing.Tuple[string.Template, typing.List[str]]
```
| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | |
| `tmp_dir` | `pathlib.Path` | |

