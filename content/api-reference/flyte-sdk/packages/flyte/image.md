---
title: Image
version: 2.2.2
variants: +flyte +union
layout: py_api
---

# Image

**Package:** `flyte`

Container image specification built using a fluent, two-step pattern:

1. Create a base image with a `from_*` constructor
2. Customize with `with_*` methods (each returns a new `Image`)

```python
image = (
    flyte.Image.from_debian_base(python="3.12")
    .with_pip_packages("pandas", "scikit-learn")
    .with_apt_packages("curl", "git")
)
```

**Base constructors** (`from_*`):

- `from_debian_base()` — Debian-based image with a specified Python version
- `from_base()` — Any base image by name (e.g., `"python:3.12-slim"`)
- `from_uv_script()` — Image from a `uv`-compatible script with inline dependencies
- `from_dockerfile()` — Image from a custom Dockerfile
- `from_ref_name()` — Reference to a pre-built image by name

**Customization methods** (`with_*`):

- `with_pip_packages()` — Add pip packages
- `with_apt_packages()` — Add system packages via apt-get
- `with_commands()` — Run arbitrary shell commands
- `with_env_vars()` — Set environment variables
- `with_requirements()` — Install from a requirements.txt file
- `with_uv_project()` — Install from a uv/pyproject.toml project
- `with_poetry_project()` — Install from a Poetry project
- `with_source_folder()` — Include a source directory
- `with_source_file()` — Include a single source file
- `with_code_bundle()` — Include a code bundle
- `with_workdir()` — Set the working directory
- `with_dockerignore()` — Add a .dockerignore
- `with_local_v2()` — Configure for local v2 execution


## Parameters

```python
class Image(
    base_image: Optional[str],
    dockerfile: Optional[Path],
    registry: Optional[str],
    name: Optional[str],
    platform: Tuple[Architecture, ...],
    python_version: Tuple[int, int],
    extendable: bool,
    _is_cloned: bool,
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
| `extendable` | `bool` | |
| `_is_cloned` | `bool` | |
| `_ref_name` | `Optional[str]` | |
| `_layers` | `Tuple[Layer, ...]` | |
| `_image_registry_secret` | `Optional[Secret]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `uri` | `str` | Returns the URI of the image in the format &lt;registry&gt;/&lt;name&gt;:&lt;tag&gt; |

## Methods

| Method | Description |
|-|-|
| [`clone()`](#clone) | Clone an existing image, optionally with a new name or registry. |
| [`from_base()`](#from_base) | Use this method to start with a pre-built base image. |
| [`from_debian_base()`](#from_debian_base) | Use this method to start using the default base image, built from this library's base Dockerfile. |
| [`from_dockerfile()`](#from_dockerfile) | Use this method to create a new image with the specified dockerfile. |
| [`from_ref_name()`](#from_ref_name) |  |
| [`from_uv_script()`](#from_uv_script) | Use this method to create a new image with the specified uv script. |
| [`validate()`](#validate) |  |
| [`with_apt_packages()`](#with_apt_packages) | Use this method to create a new image with the specified apt packages layered on top of the current image. |
| [`with_code_bundle()`](#with_code_bundle) | Configure this image to automatically copy source code from root_dir. |
| [`with_commands()`](#with_commands) | Use this method to create a new image with the specified commands layered on top of the current image. |
| [`with_dockerignore()`](#with_dockerignore) |  |
| [`with_env_vars()`](#with_env_vars) | Use this method to create a new image with the specified environment variables layered on top of. |
| [`with_local_v2()`](#with_local_v2) | Use this method to create a new image with the local v2 builder. |
| [`with_local_v2_plugins()`](#with_local_v2_plugins) | Use this method to create a new image with the local v2 builder. |
| [`with_pip_packages()`](#with_pip_packages) | Use this method to create a new image with the specified pip packages layered on top of the current image. |
| [`with_poetry_project()`](#with_poetry_project) | Use this method to create a new image with the specified pyproject. |
| [`with_requirements()`](#with_requirements) | Use this method to create a new image with the specified requirements file layered on top of the current image. |
| [`with_source_file()`](#with_source_file) | Use this method to create a new image with the specified local file(s) layered on top of the current image. |
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
    extendable: Optional[bool],
) -> Image
```
Clone an existing image, optionally with a new name or registry.

All `with_*` methods already produce a new immutable `Image`; use
`clone()` when you need an independent copy with a different name,
registry, or other base properties.



| Parameter | Type | Description |
|-|-|-|
| `registry` | `Optional[str]` | Registry to use for the image |
| `registry_secret` | `Optional[str \| Secret]` | Secret to use to pull/push the private image. |
| `name` | `Optional[str]` | Name of the image |
| `base_image` | `Optional[str]` | Base image to use for the image |
| `python_version` | `Optional[Tuple[int, int]]` | Python version for the image, if not specified, will use the current Python version |
| `addl_layer` | `Optional[Layer]` | Additional layer to add to the image. This will be added to the end of the layers. |
| `extendable` | `Optional[bool]` | Whether the image is extendable by other images. If True, the image can be used as a base image for other images, and additional layers can be added on top of it. If False, the image cannot be used as a base image for other images, and additional layers cannot be added on top of it. If None (default), defaults to False for safety. |

### from_base()

```python
def from_base(
    image_uri: str,
) -> Image
```
Use this method to start with a pre-built base image. This image must already exist in the registry of course.



| Parameter | Type | Description |
|-|-|-|
| `image_uri` | `str` | The full URI of the image, in the format &lt;registry&gt;/&lt;name&gt; |

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
| `platform` | `Optional[Tuple[Architecture, ...]]` | Platform to use for the image, default is linux/amd64, use tuple for multiple values Example: ("linux/amd64", "linux/arm64") |

**Returns:** Image

### from_dockerfile()

```python
def from_dockerfile(
    file: Union[Path, str],
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
| `file` | `Union[Path, str]` | path to the dockerfile |
| `registry` | `str` | registry to use for the image |
| `name` | `str` | name of the image |
| `platform` | `Union[Architecture, Tuple[Architecture, ...], None]` | architecture to use for the image, default is linux/amd64, use tuple for multiple values Example: ("linux/amd64", "linux/arm64") |

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

**Returns:** Image

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
| `secret_mounts` | `Optional[SecretRequest]` | list of secret mounts to use for the build process. |

**Returns:** Image

### with_code_bundle()

```python
def with_code_bundle(
    copy_style: Literal['loaded_modules', 'all'],
    dst: str,
) -> Image
```
Configure this image to automatically copy source code from root_dir
when the runner's copy_style is "none".

When the runner's copy_style is not "none", this is a no-op.



| Parameter | Type | Description |
|-|-|-|
| `copy_style` | `Literal['loaded_modules', 'all']` | Which files to copy into the image. "loaded_modules" copies only imported Python modules. "all" copies all files from root_dir. |
| `dst` | `str` | Destination directory in the container. Defaults to working dir. |

**Returns:** Image

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
| `secret_mounts` | `Optional[SecretRequest]` | list of secret mounts to use for the build process. |

**Returns:** Image

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
| `env_vars` | `Dict[str, str]` | dictionary of environment variables to set |

**Returns:** Image

### with_local_v2()

```python
def with_local_v2()
```
Use this method to create a new image with the local v2 builder
This will override any existing builder



**Returns:** Image

### with_local_v2_plugins()

```python
def with_local_v2_plugins(
    plugins: str | list[str] | None,
) -> Image
```
Use this method to create a new image with the local v2 builder
This will override any existing builder



| Parameter | Type | Description |
|-|-|-|
| `plugins` | `str \| list[str] \| None` | plugin name or list of plugin names to install, default is None, e.g. flyteplugins-hitl, flyteplugins-vllm, flyteplugins-sglang, etc. |

**Returns:** Image

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

```python
@flyte.task(image=(flyte.Image.from_debian_base().with_pip_packages("requests", "numpy")))
def my_task(x: int) -> int:
    import numpy as np
    return np.sum([x, 1])
```

To mount secrets during the build process to download private packages, you can use the `secret_mounts`.
In the below example, "GITHUB_PAT" will be mounted as env var "GITHUB_PAT",
 and "apt-secret" will be mounted at /etc/apt/apt-secret.
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
| `secret_mounts` | `Optional[SecretRequest]` | list of secret to mount for the build process. |

**Returns:** Image

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
| `project_install_mode` | `typing.Literal['dependencies_only', 'install_project']` | whether to install the project as a package or only dependencies, default is "dependencies_only" |

**Returns:** Image

### with_requirements()

```python
def with_requirements(
    file: str | Path,
    index_url: Optional[str],
    extra_index_urls: Union[str, List[str], Tuple[str, ...], None],
    pre: bool,
    extra_args: Optional[str],
    secret_mounts: Optional[SecretRequest],
) -> Image
```
Use this method to create a new image with the specified requirements file layered on top of the current image
Cannot be used in conjunction with conda



| Parameter | Type | Description |
|-|-|-|
| `file` | `str \| Path` | path to the requirements file, must be a .txt file |
| `index_url` | `Optional[str]` | index url to use for pip install, default is None |
| `extra_index_urls` | `Union[str, List[str], Tuple[str, ...], None]` | extra index urls to use for pip install, default is None |
| `pre` | `bool` | if True, install pre-release packages, default is False |
| `extra_args` | `Optional[str]` | extra arguments to pass to pip install, default is None |
| `secret_mounts` | `Optional[SecretRequest]` | list of secret to mount for the build process. |

### with_source_file()

```python
def with_source_file(
    src: typing.Union[Path, typing.List[Path]],
    dst: str,
) -> Image
```
Use this method to create a new image with the specified local file(s) layered on top of the current image.
If dest is not specified, it will be copied to the working directory of the image



| Parameter | Type | Description |
|-|-|-|
| `src` | `typing.Union[Path, typing.List[Path]]` | file or list of files from the build context to be copied |
| `dst` | `str` | destination folder in the image |

**Returns:** Image

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
| `copy_contents_only` | `bool` | If True, will copy the contents of the source folder to the destination folder, instead of the folder itself. Default is False. |

**Returns:** Image

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
| `project_install_mode` | `typing.Literal['dependencies_only', 'install_project']` | whether to install the project as a package or only dependencies, default is "dependencies_only" |

**Returns:** Image

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
| `workdir` | `str` | working directory to use |

