---
title: flytekit.interactive.vscode_lib.config
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interactive.vscode_lib.config

## Directory

### Classes

| Class | Description |
|-|-|
| [`VscodeConfig`](.././flytekit.interactive.vscode_lib.config#flytekitinteractivevscode_libconfigvscodeconfig) | VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |

### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_CODE_SERVER_DIR_NAMES` | `dict` |  |
| `DEFAULT_CODE_SERVER_EXTENSIONS` | `list` |  |
| `DEFAULT_CODE_SERVER_REMOTE_PATHS` | `dict` |  |

## flytekit.interactive.vscode_lib.config.VscodeConfig

VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths.



```python
class VscodeConfig(
    code_server_remote_paths: typing.Optional[typing.Dict[str, str]],
    code_server_dir_names: typing.Optional[typing.Dict[str, str]],
    extension_remote_paths: typing.Optional[typing.List[str]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `code_server_remote_paths` | `typing.Optional[typing.Dict[str, str]]` | The URL of the code-server tarball. |
| `code_server_dir_names` | `typing.Optional[typing.Dict[str, str]]` | The name of the code-server directory. |
| `extension_remote_paths` | `typing.Optional[typing.List[str]]` | The URLs of the VSCode extensions. You can find all available extensions at https://open-vsx.org/. |

### Methods

| Method | Description |
|-|-|
| [`add_extensions()`](#add_extensions) | Add additional extensions to the extension_remote_paths list. |


#### add_extensions()

```python
def add_extensions(
    extensions: typing.Union[str, typing.List[str]],
)
```
Add additional extensions to the extension_remote_paths list.


| Parameter | Type | Description |
|-|-|-|
| `extensions` | `typing.Union[str, typing.List[str]]` | |

