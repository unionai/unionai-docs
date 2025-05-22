---
title: flytekit.image_spec.default_builder
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.image_spec.default_builder

## Directory

### Classes

| Class | Description |
|-|-|
| [`DefaultImageBuilder`](.././flytekit.image_spec.default_builder#flytekitimage_specdefault_builderdefaultimagebuilder) | Image builder using Docker and buildkit. |

### Methods

| Method | Description |
|-|-|
| [`create_docker_context()`](#create_docker_context) | Populate tmp_dir with Dockerfile as specified by the `image_spec`. |
| [`get_flytekit_for_pypi()`](#get_flytekit_for_pypi) | Get flytekit version on PyPI. |
| [`prepare_poetry_lock_command()`](#prepare_poetry_lock_command) |  |
| [`prepare_python_executable()`](#prepare_python_executable) |  |
| [`prepare_python_install()`](#prepare_python_install) |  |
| [`prepare_uv_lock_command()`](#prepare_uv_lock_command) |  |


## Methods

#### create_docker_context()

```python
def create_docker_context(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib._local.Path,
)
```
Populate tmp_dir with Dockerfile as specified by the `image_spec`.


| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
| `tmp_dir` | `pathlib._local.Path` |

#### get_flytekit_for_pypi()

```python
def get_flytekit_for_pypi()
```
Get flytekit version on PyPI.


#### prepare_poetry_lock_command()

```python
def prepare_poetry_lock_command(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib._local.Path,
) -> typing.Tuple[string.Template, typing.List[str]]
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
| `tmp_dir` | `pathlib._local.Path` |

#### prepare_python_executable()

```python
def prepare_python_executable(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> flytekit.image_spec.default_builder._PythonInstallTemplate
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### prepare_python_install()

```python
def prepare_python_install(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib._local.Path,
) -> str
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
| `tmp_dir` | `pathlib._local.Path` |

#### prepare_uv_lock_command()

```python
def prepare_uv_lock_command(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
    tmp_dir: pathlib._local.Path,
) -> typing.Tuple[string.Template, typing.List[str]]
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
| `tmp_dir` | `pathlib._local.Path` |

## flytekit.image_spec.default_builder.DefaultImageBuilder

Image builder using Docker and buildkit.


### Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build the docker image and push it to the registry. |
| [`should_build()`](#should_build) | Whether or not the builder should build the ImageSpec. |


#### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> str
```
Build the docker image and push it to the registry.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> bool
```
Whether or not the builder should build the ImageSpec.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

