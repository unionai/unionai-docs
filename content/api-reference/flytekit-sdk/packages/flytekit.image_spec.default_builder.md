---
title: flytekit.image_spec.default_builder
version: 1.16.16
variants: +flyte +union
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



| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | image spec of the task. |

**Returns:** fully_qualified_image_name: Fully qualified image name. If None, then `image_spec.image_name()` is used.

#### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> bool
```
Whether or not the builder should build the ImageSpec.



| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | image spec of the task. |

**Returns**

True if the image should be built, otherwise it returns False.


**Raises**

| Exception | Description |
|-|-|
| `RuntimeError` | If FLYTE_IMG_FAST_FAIL is set to True and ImageSpec fails to check if the image exists due to a permission issue or other reason. |

