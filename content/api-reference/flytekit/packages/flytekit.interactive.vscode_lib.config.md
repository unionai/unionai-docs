---
title: flytekit.interactive.vscode_lib.config
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.interactive.vscode_lib.config

## Directory

### Classes

| Class | Description |
|-|-|
| [`VscodeConfig`](.././flytekit.interactive.vscode_lib.config#flytekitinteractivevscode_libconfigvscodeconfig) | VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |

## flytekit.interactive.vscode_lib.config.VscodeConfig

VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths.



```python
def VscodeConfig(
    code_server_remote_paths: typing.Optional[typing.Dict[str, str]],
    code_server_dir_names: typing.Optional[typing.Dict[str, str]],
    extension_remote_paths: typing.Optional[typing.List[str]],
):
```
| Parameter | Type |
|-|-|
| `code_server_remote_paths` | `typing.Optional[typing.Dict[str, str]]` |
| `code_server_dir_names` | `typing.Optional[typing.Dict[str, str]]` |
| `extension_remote_paths` | `typing.Optional[typing.List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`add_extensions()`](#add_extensions) | Add additional extensions to the extension_remote_paths list |


#### add_extensions()

```python
def add_extensions(
    extensions: typing.Union[str, typing.List[str]],
):
```
Add additional extensions to the extension_remote_paths list.


| Parameter | Type |
|-|-|
| `extensions` | `typing.Union[str, typing.List[str]]` |

