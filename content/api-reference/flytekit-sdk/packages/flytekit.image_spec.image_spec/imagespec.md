---
title: ImageSpec
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ImageSpec

**Package:** `flytekit.image_spec.image_spec`

This class is used to specify the docker image that will be used to run the task.

Attributes:
    name (str): Name of the image.
    python_version (str): Python version of the image. Use default python in the base image if None.
    builder (Optional[str]): Type of plugin to build the image. Use envd by default.
    source_root (Optional[str]): Source root of the image.
    env (Optional[Dict[str, str]]): Environment variables of the image.
    registry (Optional[str]): Registry of the image.
    packages (Optional[List[str]]): List of python packages to install.
    conda_packages (Optional[List[str]]): List of conda packages to install.
    conda_channels (Optional[List[str]]): List of conda channels.
    requirements (Optional[str]): Path to the requirements.txt file.
    apt_packages (Optional[List[str]]): List of apt packages to install.
    cuda (Optional[str]): Version of cuda to install.
    cudnn (Optional[str]): Version of cudnn to install.
    base_image (Optional[Union[str, 'ImageSpec']]): Base image of the image.
    platform (Optional[str]): Specify the target platforms for the build output (for example, windows/amd64 or linux/amd64,darwin/arm64).
    pip_index (Optional[str]): Specify the custom pip index url.
    pip_extra_index_url (Optional[List[str]]): Specify one or more pip index urls as a list.
    pip_secret_mounts (Optional[List[Tuple[str, str]]]): Specify a list of tuples to mount secret for pip install. Each tuple should contain the path to
        the secret file and the mount path. For example, [(".gitconfig", "/etc/gitconfig")]. This is experimental and
        the interface may change in the future. Configuring this should not change the built image.
    pip_extra_args (Optional[str]): Specify one or more extra pip install arguments as a space-delimited string.
    registry_config (Optional[str]): Specify the path to a JSON registry config file.
    entrypoint (Optional[List[str]]): List of strings to overwrite the entrypoint of the base image with, set to [] to remove the entrypoint.
    commands (Optional[List[str]]): Command to run during the building process.
    tag_format (Optional[str]): Custom string format for image tag. The ImageSpec hash passed in as `spec_hash`. For example,
        to add a "dev" suffix to the image tag, set `tag_format="{spec_hash}-dev"`.
    source_copy_mode (Optional[CopyFileDetection]): This option allows the user to specify which source files to copy from the local host, into the image.
        Not setting this option means to use the default flytekit behavior. The default behavior is:
            - if fast register is used, source files are not copied into the image (because they're already copied
              into the fast register tar layer).
            - if fast register is not used, then the LOADED_MODULES (aka 'auto') option is used to copy loaded
              Python files into the image.
        If the option is set by the user, then that option is of course used.
    copy (Optional[List[str]]): List of files/directories to copy to /root. e.g. ["src/file1.txt", "src/file2.txt"].
    python_exec (Optional[str]): Python executable to use for install packages.
    runtime_packages (Optional[List[str]]): List of packages to be installed during runtime. `runtime_packages` requires `pip` to be installed
        in your base image.
            - If you are using an ImageSpec as your base image, please include `pip` into your packages:
              `ImageSpec(..., packages=["pip"])`.
            - If you want to install runtime packages into a fixed base_image and not use an image builder, you can
              use `builder="noop"`: `ImageSpec(base_image="ghcr.io/name/my-custom-image", builder="noop").with_runtime_packages(["numpy"])`.
    builder_options (Optional[Dict[str, Any]]): Additional options for the builder. This is a dictionary that will be passed to the builder.
        The options are builder-specific and may not be supported by all builders.
    builder_config (Optional[typing.Dict[str, typing.Any]]): Custom builder images configuration, such as uv and micromamba images.



```python
class ImageSpec(
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
    platform: typing.Optional[str],
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
    runtime_packages: typing.Optional[typing.List[str]],
    builder_options: typing.Optional[typing.Dict[str, typing.Any]],
    builder_config: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `python_version` | `str` | |
| `builder` | `typing.Optional[str]` | |
| `source_root` | `typing.Optional[str]` | |
| `env` | `typing.Optional[typing.Dict[str, str]]` | |
| `registry` | `typing.Optional[str]` | |
| `packages` | `typing.Optional[typing.List[str]]` | |
| `conda_packages` | `typing.Optional[typing.List[str]]` | |
| `conda_channels` | `typing.Optional[typing.List[str]]` | |
| `requirements` | `typing.Optional[str]` | |
| `apt_packages` | `typing.Optional[typing.List[str]]` | |
| `cuda` | `typing.Optional[str]` | |
| `cudnn` | `typing.Optional[str]` | |
| `base_image` | `typing.Union[str, ForwardRef('ImageSpec'), NoneType]` | |
| `platform` | `typing.Optional[str]` | |
| `pip_index` | `typing.Optional[str]` | |
| `pip_extra_index_url` | `typing.Optional[typing.List[str]]` | |
| `pip_secret_mounts` | `typing.Optional[typing.List[typing.Tuple[str, str]]]` | |
| `pip_extra_args` | `typing.Optional[str]` | |
| `registry_config` | `typing.Optional[str]` | |
| `entrypoint` | `typing.Optional[typing.List[str]]` | |
| `commands` | `typing.Optional[typing.List[str]]` | |
| `tag_format` | `typing.Optional[str]` | |
| `source_copy_mode` | `typing.Optional[flytekit.constants.CopyFileDetection]` | |
| `copy` | `typing.Optional[typing.List[str]]` | |
| `python_exec` | `typing.Optional[str]` | |
| `runtime_packages` | `typing.Optional[typing.List[str]]` | |
| `builder_options` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `builder_config` | `typing.Optional[typing.Dict[str, typing.Any]]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `id` | `None` | Calculate a unique hash as the ID for the ImageSpec, and it will be used to 1. Identify the imageSpec in the ImageConfig in the serialization context. 2. Check if the current container image in the pod is built from this image spec in `is_container()`.  ImageConfig: - deduced abc: flyteorg/flytekit:123 - deduced xyz: flyteorg/flytekit:456  The result of this property also depends on whether or not update_image_spec_copy_handling was called.  :return: a unique identifier of the ImageSpec |
| `tag` | `None` | Calculate a hash from the image spec. The hash will be the tag of the image. We will also read the content of the requirement file and the source root to calculate the hash. Therefore, it will generate different hash if new dependencies are added or the source code is changed.  Keep in mind the fields source_root and copy may be changed by update_image_spec_copy_handling, so when you call this property in relation to that function matter will change the output. |

## Methods

| Method | Description |
|-|-|
| [`exist()`](#exist) | Check if the image exists in the registry. |
| [`force_push()`](#force_push) | Builder that returns a new image spec with force push enabled. |
| [`from_env()`](#from_env) | Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment. |
| [`image_name()`](#image_name) | Full image name with tag. |
| [`is_container()`](#is_container) | Check if the current container image in the pod is built from current image spec. |
| [`with_apt_packages()`](#with_apt_packages) | Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process. |
| [`with_builder_options()`](#with_builder_options) | Builder that returns a new image spec with additional builder options. |
| [`with_commands()`](#with_commands) | Builder that returns a new image spec with an additional list of commands that will be executed during the building process. |
| [`with_copy()`](#with_copy) | Builder that returns a new image spec with the source files copied to the destination directory. |
| [`with_packages()`](#with_packages) | Builder that returns a new image speck with additional python packages that will be installed during the building process. |
| [`with_runtime_packages()`](#with_runtime_packages) | Builder that returns a new image spec with runtime packages. |


### exist()

```python
def exist()
```
Check if the image exists in the registry.
Return True if the image exists in the registry, False otherwise.
Return None if failed to check if the image exists due to the permission issue or other reasons.


### force_push()

```python
def force_push()
```
Builder that returns a new image spec with force push enabled.


### from_env()

```python
def from_env(
    pinned_packages: typing.Optional[typing.List[str]],
    kwargs,
) -> ImageSpec
```
Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment.


| Parameter | Type | Description |
|-|-|-|
| `pinned_packages` | `typing.Optional[typing.List[str]]` | |
| `kwargs` | `**kwargs` | |

### image_name()

```python
def image_name()
```
Full image name with tag.


### is_container()

```python
def is_container()
```
Check if the current container image in the pod is built from current image spec.
:return: True if the current container image in the pod is built from current image spec, False otherwise.


### with_apt_packages()

```python
def with_apt_packages(
    apt_packages: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process.


| Parameter | Type | Description |
|-|-|-|
| `apt_packages` | `typing.Union[str, typing.List[str]]` | |

### with_builder_options()

```python
def with_builder_options(
    builder_options: typing.Dict[str, typing.Any],
) -> ImageSpec
```
Builder that returns a new image spec with additional builder options.


| Parameter | Type | Description |
|-|-|-|
| `builder_options` | `typing.Dict[str, typing.Any]` | |

### with_commands()

```python
def with_commands(
    commands: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with an additional list of commands that will be executed during the building process.


| Parameter | Type | Description |
|-|-|-|
| `commands` | `typing.Union[str, typing.List[str]]` | |

### with_copy()

```python
def with_copy(
    src: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with the source files copied to the destination directory.


| Parameter | Type | Description |
|-|-|-|
| `src` | `typing.Union[str, typing.List[str]]` | |

### with_packages()

```python
def with_packages(
    packages: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image speck with additional python packages that will be installed during the building process.


| Parameter | Type | Description |
|-|-|-|
| `packages` | `typing.Union[str, typing.List[str]]` | |

### with_runtime_packages()

```python
def with_runtime_packages(
    runtime_packages: typing.List[str],
) -> ImageSpec
```
Builder that returns a new image spec with runtime packages. Dev packages will be installed during runtime.


| Parameter | Type | Description |
|-|-|-|
| `runtime_packages` | `typing.List[str]` | |

