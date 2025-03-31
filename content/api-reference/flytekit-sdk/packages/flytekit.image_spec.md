---
title: flytekit.image_spec
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.image_spec


==========
ImageSpec
==========

.. currentmodule:: flytekit.image_spec

This module contains the ImageSpec class parameters and methods.

.. autosummary::
   :nosignatures:
   :template: custom.rst
   :toctree: generated/

   ImageSpec

## Directory

### Classes

| Class | Description |
|-|-|
| [`DefaultImageBuilder`](.././flytekit.image_spec#flytekitimage_specdefaultimagebuilder) | Image builder using Docker and buildkit. |
| [`ImageBuildEngine`](.././flytekit.image_spec#flytekitimage_specimagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`ImageSpec`](.././flytekit.image_spec#flytekitimage_specimagespec) | This class is used to specify the docker image that will be used to run the task. |

## flytekit.image_spec.DefaultImageBuilder

Image builder using Docker and buildkit.


### Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build the docker image and push it to the registry |
| [`should_build()`](#should_build) | Whether or not the builder should build the ImageSpec |


#### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
Build the docker image and push it to the registry.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
Whether or not the builder should build the ImageSpec.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

## flytekit.image_spec.ImageBuildEngine

ImageBuildEngine contains a list of builders that can be used to build an ImageSpec.


### Methods

| Method | Description |
|-|-|
| [`build()`](#build) | None |
| [`get_registry()`](#get_registry) | None |
| [`register()`](#register) | None |


#### build()

```python
def build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### get_registry()

```python
def get_registry()
```
#### register()

```python
def register(
    builder_type: str,
    image_spec_builder: flytekit.image_spec.image_spec.ImageSpecBuilder,
    priority: int,
):
```
| Parameter | Type |
|-|-|
| `builder_type` | `str` |
| `image_spec_builder` | `flytekit.image_spec.image_spec.ImageSpecBuilder` |
| `priority` | `int` |

## flytekit.image_spec.ImageSpec

This class is used to specify the docker image that will be used to run the task.



```python
def ImageSpec(
    name: str,
    python_version: str,
    builder: typing.Optional[str],
    source_root: typing.Optional[str],
    env: typing.Optional[typing.Dict[str, str]],
    registry: typing.Optional[str],
    packages: typing.Optional[typing.List[str]],
    conda_packages: typing.Optional[typing.List[str]],
    conda_channels: typing.Optional[typing.List[str]],
    requirements: typing.Optional[str],
    apt_packages: typing.Optional[typing.List[str]],
    cuda: typing.Optional[str],
    cudnn: typing.Optional[str],
    base_image: typing.Union[str, ForwardRef('ImageSpec'), NoneType],
    platform: str,
    pip_index: typing.Optional[str],
    pip_extra_index_url: typing.Optional[typing.List[str]],
    pip_secret_mounts: typing.Optional[typing.List[typing.Tuple[str, str]]],
    pip_extra_args: typing.Optional[str],
    registry_config: typing.Optional[str],
    entrypoint: typing.Optional[typing.List[str]],
    commands: typing.Optional[typing.List[str]],
    tag_format: typing.Optional[str],
    source_copy_mode: typing.Optional[flytekit.constants.CopyFileDetection],
    copy: typing.Optional[typing.List[str]],
    python_exec: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `python_version` | `str` |
| `builder` | `typing.Optional[str]` |
| `source_root` | `typing.Optional[str]` |
| `env` | `typing.Optional[typing.Dict[str, str]]` |
| `registry` | `typing.Optional[str]` |
| `packages` | `typing.Optional[typing.List[str]]` |
| `conda_packages` | `typing.Optional[typing.List[str]]` |
| `conda_channels` | `typing.Optional[typing.List[str]]` |
| `requirements` | `typing.Optional[str]` |
| `apt_packages` | `typing.Optional[typing.List[str]]` |
| `cuda` | `typing.Optional[str]` |
| `cudnn` | `typing.Optional[str]` |
| `base_image` | `typing.Union[str, ForwardRef('ImageSpec'), NoneType]` |
| `platform` | `str` |
| `pip_index` | `typing.Optional[str]` |
| `pip_extra_index_url` | `typing.Optional[typing.List[str]]` |
| `pip_secret_mounts` | `typing.Optional[typing.List[typing.Tuple[str, str]]]` |
| `pip_extra_args` | `typing.Optional[str]` |
| `registry_config` | `typing.Optional[str]` |
| `entrypoint` | `typing.Optional[typing.List[str]]` |
| `commands` | `typing.Optional[typing.List[str]]` |
| `tag_format` | `typing.Optional[str]` |
| `source_copy_mode` | `typing.Optional[flytekit.constants.CopyFileDetection]` |
| `copy` | `typing.Optional[typing.List[str]]` |
| `python_exec` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`exist()`](#exist) | Check if the image exists in the registry |
| [`force_push()`](#force_push) | Builder that returns a new image spec with force push enabled |
| [`from_env()`](#from_env) | Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment |
| [`image_name()`](#image_name) | Full image name with tag |
| [`is_container()`](#is_container) | Check if the current container image in the pod is built from current image spec |
| [`with_apt_packages()`](#with_apt_packages) | Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process |
| [`with_commands()`](#with_commands) | Builder that returns a new image spec with an additional list of commands that will be executed during the building process |
| [`with_copy()`](#with_copy) | Builder that returns a new image spec with the source files copied to the destination directory |
| [`with_packages()`](#with_packages) | Builder that returns a new image speck with additional python packages that will be installed during the building process |


#### exist()

```python
def exist()
```
Check if the image exists in the registry.
Return True if the image exists in the registry, False otherwise.
Return None if failed to check if the image exists due to the permission issue or other reasons.


#### force_push()

```python
def force_push()
```
Builder that returns a new image spec with force push enabled.


#### from_env()

```python
def from_env(
    pinned_packages: typing.Optional[typing.List[str]],
    kwargs,
):
```
Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment.


| Parameter | Type |
|-|-|
| `pinned_packages` | `typing.Optional[typing.List[str]]` |
| `kwargs` | ``**kwargs`` |

#### image_name()

```python
def image_name()
```
Full image name with tag.


#### is_container()

```python
def is_container()
```
Check if the current container image in the pod is built from current image spec.
:return: True if the current container image in the pod is built from current image spec, False otherwise.


#### with_apt_packages()

```python
def with_apt_packages(
    apt_packages: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process.


| Parameter | Type |
|-|-|
| `apt_packages` | `typing.Union[str, typing.List[str]]` |

#### with_commands()

```python
def with_commands(
    commands: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with an additional list of commands that will be executed during the building process.


| Parameter | Type |
|-|-|
| `commands` | `typing.Union[str, typing.List[str]]` |

#### with_copy()

```python
def with_copy(
    src: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with the source files copied to the destination directory.


| Parameter | Type |
|-|-|
| `src` | `typing.Union[str, typing.List[str]]` |

#### with_packages()

```python
def with_packages(
    packages: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image speck with additional python packages that will be installed during the building process.


| Parameter | Type |
|-|-|
| `packages` | `typing.Union[str, typing.List[str]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| tag |  |  |

