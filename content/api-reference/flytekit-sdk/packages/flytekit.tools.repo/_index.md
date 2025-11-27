---
title: flytekit.tools.repo
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.tools.repo

## Directory

### Errors

| Exception | Description |
|-|-|
| [`NoSerializableEntitiesError`](../flytekit.tools.repo/noserializableentitieserror) | Common base class for all non-exit exceptions. |

### Methods

| Method | Description |
|-|-|
| [`find_common_root()`](#find_common_root) | Given an arbitrary list of folders and files, this function will use the script mode function to walk up. |
| [`list_packages_and_modules()`](#list_packages_and_modules) | This is a helper function that returns the input list of python packages/modules as a dot delinated list. |
| [`package()`](#package) | Package the given entities and the source code (if fast is enabled) into a package with the given name in output. |
| [`print_registration_status()`](#print_registration_status) |  |
| [`register()`](#register) | Temporarily, for fast register, specify both the fast arg as well as copy_style. |
| [`serialize_and_package()`](#serialize_and_package) | Fist serialize and then package all entities. |
| [`serialize_get_control_plane_entities()`](#serialize_get_control_plane_entities) | See {{< py_class_ref flytekit.models.core.identifier.ResourceType >}} to match the trailing index in the file name with the. |
| [`serialize_load_only()`](#serialize_load_only) | See {{< py_class_ref flytekit.models.core.identifier.ResourceType >}} to match the trailing index in the file name with the. |
| [`serialize_to_folder()`](#serialize_to_folder) | Serialize the given set of python packages to a folder. |


## Methods

#### find_common_root()

```python
def find_common_root(
    pkgs_or_mods: typing.Union[typing.Tuple[str], typing.List[str]],
) -> pathlib.Path
```
Given an arbitrary list of folders and files, this function will use the script mode function to walk up
the filesystem to find the first folder without an init file. If all the folders and files resolve to
the same root folder, then that Path is returned. Otherwise an error is raised.



| Parameter | Type | Description |
|-|-|-|
| `pkgs_or_mods` | `typing.Union[typing.Tuple[str], typing.List[str]]` | :return: The common detected root path, the output of _find_project_root |

#### list_packages_and_modules()

```python
def list_packages_and_modules(
    project_root: pathlib.Path,
    pkgs_or_mods: typing.List[str],
) -> typing.List[str]
```
This is a helper function that returns the input list of python packages/modules as a dot delinated list
relative to the given project_root.



| Parameter | Type | Description |
|-|-|-|
| `project_root` | `pathlib.Path` | |
| `pkgs_or_mods` | `typing.List[str]` | :return: List of packages/modules, dot delineated. |

#### package()

```python
def package(
    serializable_entities: typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]],
    source: str,
    output: str,
    deref_symlinks: bool,
    fast_options: typing.Optional[flytekit.tools.fast_registration.FastPackageOptions],
)
```
Package the given entities and the source code (if fast is enabled) into a package with the given name in output


| Parameter | Type | Description |
|-|-|-|
| `serializable_entities` | `typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]]` | Entities that can be serialized |
| `source` | `str` | source folder |
| `output` | `str` | output package name with suffix |
| `deref_symlinks` | `bool` | if enabled then symlinks are dereferenced during packaging |
| `fast_options` | `typing.Optional[flytekit.tools.fast_registration.FastPackageOptions]` | Temporarily, for fast register, specify both the fast arg as well as copy_style fast == True with copy_style == None means use the old fast register tar'ring method. In the future the fast bool will be removed, and copy_style == None will mean do not fast register. |

#### print_registration_status()

```python
def print_registration_status(
    i: flytekit.models.core.identifier.Identifier,
    success: bool,
    activation: bool,
    dry_run: bool,
    console_url: str,
    verbosity: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `i` | `flytekit.models.core.identifier.Identifier` | |
| `success` | `bool` | |
| `activation` | `bool` | |
| `dry_run` | `bool` | |
| `console_url` | `str` | |
| `verbosity` | `int` | |

#### register()

```python
def register(
    project: str,
    domain: str,
    image_config: flytekit.configuration.ImageConfig,
    output: str,
    destination_dir: str,
    service_account: str,
    raw_data_prefix: str,
    version: typing.Optional[str],
    deref_symlinks: bool,
    package_or_module: typing.Tuple[str],
    remote: flytekit.remote.remote.FlyteRemote,
    copy_style: <enum 'CopyFileDetection'>,
    env: typing.Optional[typing.Dict[str, str]],
    default_resources: typing.Optional[flytekit.core.resources.ResourceSpec],
    dry_run: bool,
    activate_launchplans: bool,
    skip_errors: bool,
    show_files: bool,
    verbosity: int,
)
```
Temporarily, for fast register, specify both the fast arg as well as copy_style.
fast == True with copy_style == None means use the old fast register tar'ring method.


| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | |
| `domain` | `str` | |
| `image_config` | `flytekit.configuration.ImageConfig` | |
| `output` | `str` | |
| `destination_dir` | `str` | |
| `service_account` | `str` | |
| `raw_data_prefix` | `str` | |
| `version` | `typing.Optional[str]` | |
| `deref_symlinks` | `bool` | |
| `package_or_module` | `typing.Tuple[str]` | |
| `remote` | `flytekit.remote.remote.FlyteRemote` | |
| `copy_style` | `<enum 'CopyFileDetection'>` | |
| `env` | `typing.Optional[typing.Dict[str, str]]` | |
| `default_resources` | `typing.Optional[flytekit.core.resources.ResourceSpec]` | |
| `dry_run` | `bool` | |
| `activate_launchplans` | `bool` | |
| `skip_errors` | `bool` | |
| `show_files` | `bool` | |
| `verbosity` | `int` | |

#### serialize_and_package()

```python
def serialize_and_package(
    pkgs: typing.List[str],
    settings: flytekit.configuration.SerializationSettings,
    source: str,
    output: str,
    deref_symlinks: bool,
    options: typing.Optional[flytekit.core.options.Options],
    fast_options: typing.Optional[flytekit.tools.fast_registration.FastPackageOptions],
)
```
Fist serialize and then package all entities
Temporarily for fast package, specify both the fast arg as well as copy_style.
fast == True with copy_style == None means use the old fast register tar'ring method.


| Parameter | Type | Description |
|-|-|-|
| `pkgs` | `typing.List[str]` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `source` | `str` | |
| `output` | `str` | |
| `deref_symlinks` | `bool` | |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |
| `fast_options` | `typing.Optional[flytekit.tools.fast_registration.FastPackageOptions]` | |

#### serialize_get_control_plane_entities()

```python
def serialize_get_control_plane_entities(
    settings: flytekit.configuration.SerializationSettings,
    local_source_root: typing.Optional[str],
    options: typing.Optional[flytekit.core.options.Options],
    is_registration: bool,
) -> typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]]
```
See {{< py_class_ref flytekit.models.core.identifier.ResourceType >}} to match the trailing index in the file name with the
entity type.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | SerializationSettings to be used |
| `local_source_root` | `typing.Optional[str]` | Where to start looking for the code. |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |
| `is_registration` | `bool` | Whether this is happening for registration. |

#### serialize_load_only()

```python
def serialize_load_only(
    pkgs: typing.List[str],
    settings: flytekit.configuration.SerializationSettings,
    local_source_root: typing.Optional[str],
)
```
See {{< py_class_ref flytekit.models.core.identifier.ResourceType >}} to match the trailing index in the file name with the
entity type.


| Parameter | Type | Description |
|-|-|-|
| `pkgs` | `typing.List[str]` | Dot-delimited Python packages/subpackages to look into for serialization. |
| `settings` | `flytekit.configuration.SerializationSettings` | SerializationSettings to be used |
| `local_source_root` | `typing.Optional[str]` | Where to start looking for the code. |

#### serialize_to_folder()

```python
def serialize_to_folder(
    pkgs: typing.List[str],
    settings: flytekit.configuration.SerializationSettings,
    local_source_root: typing.Optional[str],
    folder: str,
    options: typing.Optional[flytekit.core.options.Options],
)
```
Serialize the given set of python packages to a folder


| Parameter | Type | Description |
|-|-|-|
| `pkgs` | `typing.List[str]` | |
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `local_source_root` | `typing.Optional[str]` | |
| `folder` | `str` | |
| `options` | `typing.Optional[flytekit.core.options.Options]` | |

