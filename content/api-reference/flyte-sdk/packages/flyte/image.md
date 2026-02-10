---
title: Image
version: 2.0.0b56
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Image

**Package:** `flyte`

This is a representation of Container Images, which can be used to create layered images programmatically.

Use by first calling one of the base constructor methods. These all begin with `from` or `default_`
The image can then be amended with additional layers using the various `with_*` methods.

Invariant for this class: The construction of Image objects must be doable everywhere. That is, if a
  user has a custom image that is not accessible, calling .with_source_file on a file that doesn't exist, the
  instantiation of the object itself must still go through. Further, the .identifier property of the image must
  also still go through. This is because it may have been already built somewhere else.
  Use validate() functions to check each layer for actual errors. These are invoked at actual
  build time. See self.id for more information


```python
class Image(
    base_image: Optional[str],
    dockerfile: Optional[Path],
    registry: Optional[str],
    name: Optional[str],
    platform: Tuple[Architecture, ...],
    python_version: Tuple[int, int],
    _ref_name: Optional[str],
    _layers: Tuple[Layer, ...],
    _image_registry_secret: Optional[Secret],
)
```
| Parameter | Type | Description |
|-|-|-|
| `base_image` | `Optional[str]` | |
| `dockerfile` | `Optional[Path]` | |
| `registry` | `Optional[str]` | |
| `name` | `Optional[str]` | |
| `platform` | `Tuple[Architecture, ...]` | |
| `python_version` | `Tuple[int, int]` | |
| `_ref_name` | `Optional[str]` | |
| `_layers` | `Tuple[Layer, ...]` | |
| `_image_registry_secret` | `Optional[Secret]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `uri` | `None` | Returns the URI of the image in the format &lt;registry&gt;/&lt;name&gt;:&lt;tag&gt; |

## Methods

| Method | Description |
|-|-|
| [`clone()`](#clone) | Use this method to clone the current image and change the registry and name. |
| [`from_base()`](#from_base) | Use this method to start with a pre-built base image. |
| [`from_debian_base()`](#from_debian_base) | Use this method to start using the default base image, built from this library's base Dockerfile. |
| [`from_dockerfile()`](#from_dockerfile) | Use this method to create a new image with the specified dockerfile. |
| [`from_ref_name()`](#from_ref_name) |  |
| [`from_uv_script()`](#from_uv_script) | Use this method to create a new image with the specified uv script. |
| [`validate()`](#validate) |  |
| [`with_apt_packages()`](#with_apt_packages) | Use this method to create a new image with the specified apt packages layered on top of the current image. |
| [`with_commands()`](#with_commands) | Use this method to create a new image with the specified commands layered on top of the current image. |
| [`with_dockerignore()`](#with_dockerignore) |  |
| [`with_env_vars()`](#with_env_vars) | Use this method to create a new image with the specified environment variables layered on top of. |
| [`with_local_v2()`](#with_local_v2) | Use this method to create a new image with the local v2 builder. |
| [`with_pip_packages()`](#with_pip_packages) | Use this method to create a new image with the specified pip packages layered on top of the current image. |
| [`with_poetry_project()`](#with_poetry_project) | Use this method to create a new image with the specified pyproject. |
| [`with_requirements()`](#with_requirements) | Use this method to create a new image with the specified requirements file layered on top of the current image. |
| [`with_source_file()`](#with_source_file) | Use this method to create a new image with the specified local file layered on top of the current image. |
| [`with_source_folder()`](#with_source_folder) | Use this method to create a new image with the specified local directory layered on top of the current image. |
| [`with_uv_project()`](#with_uv_project) | Use this method to create a new image with the specified uv. |
| [`with_workdir()`](#with_workdir) | Use this method to create a new image with the specified working directory. |


### clone()

```python
def clone(
    registry: Optional[str],
    registry_secret: Optional[str | Secret],
    name: Optional[str],
    base_image: Optional[str],
    python_version: Optional[Tuple[int, int]],
    addl_layer: Optional[Layer],
) -> Image
```
Use this method to clone the current image and change the registry and name



| Parameter | Type | Description |
|-|-|-|
| `registry` | `Optional[str]` | Registry to use for the image |
| `registry_secret` | `Optional[str \| Secret]` | Secret to use to pull/push the private image. |
| `name` | `Optional[str]` | Name of the image |
| `base_image` | `Optional[str]` | |
| `python_version` | `Optional[Tuple[int, int]]` | Python version for the image, if not specified, will use the current Python version |
| `addl_layer` | `Optional[Layer]` | Additional layer to add to the image. This will be added to the end of the layers. :return: |

### from_base()

```python
def from_base(
    image_uri: str,
) -> Image
```
Use this method to start with a pre-built base image. This image must already exist in the registry of course.



| Parameter | Type | Description |
|-|-|-|
| `image_uri` | `str` | The full URI of the image, in the format &lt;registry&gt;/&lt;name&gt; :return: |

### from_debian_base()

```python
def from_debian_base(
    python_version: Optional[Tuple[int, int]],
    flyte_version: Optional[str],
    install_flyte: bool,
    registry: Optional[str],
    registry_secret: Optional[str | Secret],
    name: Optional[str],
    platform: Optional[Tuple[Architecture, ...]],
) -> Image
```
Use this method to start using the default base image, built from this library's base Dockerfile
Default images are multi-arch amd/arm64



| Parameter | Type | Description |
|-|-|-|
| `python_version` | `Optional[Tuple[int, int]]` | If not specified, will use the current Python version |
| `flyte_version` | `Optional[str]` | Flyte version to use |
| `install_flyte` | `bool` | If True, will install the flyte library in the image |
| `registry` | `Optional[str]` | Registry to use for the image |
| `registry_secret` | `Optional[str \| Secret]` | Secret to use to pull/push the private image. |
| `name` | `Optional[str]` | Name of the image if you want to override the default name |
| `platform` | `Optional[Tuple[Architecture, ...]]` | Platform to use for the image, default is linux/amd64, use tuple for multiple values Example: ("linux/amd64", "linux/arm64")  :return: Image |

### from_dockerfile()

```python
def from_dockerfile(
    file: Path,
    registry: str,
    name: str,
    platform: Union[Architecture, Tuple[Architecture, ...], None],
) -> Image
```
Use this method to create a new image with the specified dockerfile. Note you cannot use additional layers
after this, as the system doesn't attempt to parse/understand the Dockerfile, and what kind of setup it has
(python version, uv vs poetry, etc), so please put all logic into the dockerfile itself.

Also since Python sees paths as from the calling directory, please use Path objects with absolute paths. The
context for the builder will be the directory where the dockerfile is located.



| Parameter | Type | Description |
|-|-|-|
| `file` | `Path` | path to the dockerfile |
| `registry` | `str` | registry to use for the image |
| `name` | `str` | name of the image |
| `platform` | `Union[Architecture, Tuple[Architecture, ...], None]` | architecture to use for the image, default is linux/amd64, use tuple for multiple values Example: ("linux/amd64", "linux/arm64")  :return: |

### from_ref_name()

```python
def from_ref_name(
    name: str,
) -> Image
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

### from_uv_script()

```python
def from_uv_script(
    script: Path | str,
    name: str,
    registry: str | None,
    registry_secret: Optional[str | Secret],
    python_version: Optional[Tuple[int, int]],
    index_url: Optional[str],
    extra_index_urls: Union[str, List[str], Tuple[str, ...], None],
    pre: bool,
    extra_args: Optional[str],
    platform: Optional[Tuple[Architecture, ...]],
    secret_mounts: Optional[SecretRequest],
) -> Image
```
Use this method to create a new image with the specified uv script.
It uses the header of the script to determine the python version, dependencies to install.
The script must be a valid uv script, otherwise an error will be raised.

Usually the header of the script will look like this:
Example:
```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
```

For more information on the uv script format, see the documentation:
[UV: Declaring script dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies)



| Parameter | Type | Description |
|-|-|-|
| `script` | `Path \| str` | path to the uv script |
| `name` | `str` | name of the image |
| `registry` | `str \| None` | registry to use for the image |
| `registry_secret` | `Optional[str \| Secret]` | Secret to use to pull/push the private image. |
| `python_version` | `Optional[Tuple[int, int]]` | Python version for the image, if not specified, will use the current Python version |
| `index_url` | `Optional[str]` | index url to use for pip install, default is None |
| `extra_index_urls` | `Union[str, List[str], Tuple[str, ...], None]` | extra index urls to use for pip install, default is True |
| `pre` | `bool` | whether to allow pre-release versions, default is False |
| `extra_args` | `Optional[str]` | extra arguments to pass to pip install, default is None |
| `platform` | `Optional[Tuple[Architecture, ...]]` | architecture to use for the image, default is linux/amd64, use tuple for multiple values |
| `secret_mounts` | `Optional[SecretRequest]` | |

### validate()

```python
def validate()
```
### with_apt_packages()

```python
def with_apt_packages(
    packages: str,
    secret_mounts: Optional[SecretRequest],
) -> Image
```
Use this method to create a new image with the specified apt packages layered on top of the current image



| Parameter | Type | Description |
|-|-|-|
| `packages` | `str` | list of apt packages to install |
| `secret_mounts` | `Optional[SecretRequest]` | list of secret mounts to use for the build process. :return: Image |

### with_commands()

```python
def with_commands(
    commands: List[str],
    secret_mounts: Optional[SecretRequest],
) -> Image
```
Use this method to create a new image with the specified commands layered on top of the current image
Be sure not to use RUN in your command.



| Parameter | Type | Description |
|-|-|-|
| `commands` | `List[str]` | list of commands to run |
| `secret_mounts` | `Optional[SecretRequest]` | list of secret mounts to use for the build process. :return: Image |

### with_dockerignore()

```python
def with_dockerignore(
    path: Path,
) -> Image
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `Path` | |

### with_env_vars()

```python
def with_env_vars(
    env_vars: Dict[str, str],
) -> Image
```
Use this method to create a new image with the specified environment variables layered on top of
the current image. Cannot be used in conjunction with conda



| Parameter | Type | Description |
|-|-|-|
| `env_vars` | `Dict[str, str]` | dictionary of environment variables to set :return: Image |

### with_local_v2()

```python
def with_local_v2()
```
Use this method to create a new image with the local v2 builder
This will override any existing builder

:return: Image


### with_pip_packages()

```python
def with_pip_packages(
    packages: str,
    index_url: Optional[str],
    extra_index_urls: Union[str, List[str], Tuple[str, ...], None],
    pre: bool,
    extra_args: Optional[str],
    secret_mounts: Optional[SecretRequest],
) -> Image
```
Use this method to create a new image with the specified pip packages layered on top of the current image
Cannot be used in conjunction with conda

Example:
```python
@flyte.task(image=(flyte.Image.from_debian_base().with_pip_packages("requests", "numpy")))
def my_task(x: int) -> int:
    import numpy as np
    return np.sum([x, 1])
```

To mount secrets during the build process to download private packages, you can use the `secret_mounts`.
In the below example, "GITHUB_PAT" will be mounted as env var "GITHUB_PAT",
 and "apt-secret" will be mounted at /etc/apt/apt-secret.
Example:
```python
private_package = "git+https://$GITHUB_PAT@github.com/flyteorg/flytex.git@2e20a2acebfc3877d84af643fdd768edea41d533"
@flyte.task(
    image=(
        flyte.Image.from_debian_base()
        .with_pip_packages("private_package", secret_mounts=[Secret(key="GITHUB_PAT")])
        .with_apt_packages("git", secret_mounts=[Secret(key="apt-secret", mount="/etc/apt/apt-secret")])
)
def my_task(x: int) -> int:
    import numpy as np
    return np.sum([x, 1])
```



| Parameter | Type | Description |
|-|-|-|
| `packages` | `str` | list of pip packages to install, follows pip install syntax |
| `index_url` | `Optional[str]` | index url to use for pip install, default is None |
| `extra_index_urls` | `Union[str, List[str], Tuple[str, ...], None]` | extra index urls to use for pip install, default is None |
| `pre` | `bool` | whether to allow pre-release versions, default is False |
| `extra_args` | `Optional[str]` | extra arguments to pass to pip install, default is None |
| `secret_mounts` | `Optional[SecretRequest]` | list of secret to mount for the build process. :return: Image |

### with_poetry_project()

```python
def with_poetry_project(
    pyproject_file: str | Path,
    poetry_lock: Path | None,
    extra_args: Optional[str],
    secret_mounts: Optional[SecretRequest],
    project_install_mode: typing.Literal['dependencies_only', 'install_project'],
)
```
Use this method to create a new image with the specified pyproject.toml layered on top of the current image.
Must have a corresponding pyproject.toml file in the same directory.
Cannot be used in conjunction with conda.

By default, this method copies the entire project into the image,
including files such as pyproject.toml, poetry.lock, and the src/ directory.

If you prefer not to install the current project, you can pass through `extra_args`
`--no-root`. In this case, the image builder will only copy pyproject.toml and poetry.lock
into the image.



| Parameter | Type | Description |
|-|-|-|
| `pyproject_file` | `str \| Path` | Path to the pyproject.toml file. A poetry.lock file must exist in the same directory unless `poetry_lock` is explicitly provided. |
| `poetry_lock` | `Path \| None` | Path to the poetry.lock file. If not specified, the default is the file named 'poetry.lock' in the same directory as `pyproject_file` (pyproject.parent / "poetry.lock"). |
| `extra_args` | `Optional[str]` | Extra arguments to pass through to the package installer/resolver, default is None. |
| `secret_mounts` | `Optional[SecretRequest]` | Secrets to make available during dependency resolution/build (e.g., private indexes). |
| `project_install_mode` | `typing.Literal['dependencies_only', 'install_project']` | whether to install the project as a package or only dependencies, default is "dependencies_only" :return: Image |

### with_requirements()

```python
def with_requirements(
    file: str | Path,
    secret_mounts: Optional[SecretRequest],
) -> Image
```
Use this method to create a new image with the specified requirements file layered on top of the current image
Cannot be used in conjunction with conda



| Parameter | Type | Description |
|-|-|-|
| `file` | `str \| Path` | path to the requirements file, must be a .txt file |
| `secret_mounts` | `Optional[SecretRequest]` | list of secret to mount for the build process. :return: |

### with_source_file()

```python
def with_source_file(
    src: Path,
    dst: str,
) -> Image
```
Use this method to create a new image with the specified local file layered on top of the current image.
If dest is not specified, it will be copied to the working directory of the image



| Parameter | Type | Description |
|-|-|-|
| `src` | `Path` | root folder of the source code from the build context to be copied |
| `dst` | `str` | destination folder in the image :return: Image |

### with_source_folder()

```python
def with_source_folder(
    src: Path,
    dst: str,
    copy_contents_only: bool,
) -> Image
```
Use this method to create a new image with the specified local directory layered on top of the current image.
If dest is not specified, it will be copied to the working directory of the image



| Parameter | Type | Description |
|-|-|-|
| `src` | `Path` | root folder of the source code from the build context to be copied |
| `dst` | `str` | destination folder in the image |
| `copy_contents_only` | `bool` | If True, will copy the contents of the source folder to the destination folder, instead of the folder itself. Default is False. :return: Image |

### with_uv_project()

```python
def with_uv_project(
    pyproject_file: str | Path,
    uvlock: Path | None,
    index_url: Optional[str],
    extra_index_urls: Union[List[str], Tuple[str, ...], None],
    pre: bool,
    extra_args: Optional[str],
    secret_mounts: Optional[SecretRequest],
    project_install_mode: typing.Literal['dependencies_only', 'install_project'],
) -> Image
```
Use this method to create a new image with the specified uv.lock file layered on top of the current image
Must have a corresponding pyproject.toml file in the same directory
Cannot be used in conjunction with conda

By default, this method copies the pyproject.toml and uv.lock files into the image.

If `project_install_mode` is "install_project", it will also copy directory
 where the pyproject.toml file is located into the image.



| Parameter | Type | Description |
|-|-|-|
| `pyproject_file` | `str \| Path` | path to the pyproject.toml file |
| `uvlock` | `Path \| None` | path to the uv.lock file, if not specified, will use the default uv.lock file in the same directory as the pyproject.toml file if it exists. (pyproject.parent / uv.lock) |
| `index_url` | `Optional[str]` | index url to use for pip install, default is None |
| `extra_index_urls` | `Union[List[str], Tuple[str, ...], None]` | extra index urls to use for pip install, default is None |
| `pre` | `bool` | whether to allow pre-release versions, default is False |
| `extra_args` | `Optional[str]` | extra arguments to pass to pip install, default is None |
| `secret_mounts` | `Optional[SecretRequest]` | list of secret mounts to use for the build process. |
| `project_install_mode` | `typing.Literal['dependencies_only', 'install_project']` | whether to install the project as a package or only dependencies, default is "dependencies_only" :return: Image |

### with_workdir()

```python
def with_workdir(
    workdir: str,
) -> Image
```
Use this method to create a new image with the specified working directory
This will override any existing working directory



| Parameter | Type | Description |
|-|-|-|
| `workdir` | `str` | working directory to use :return: |

