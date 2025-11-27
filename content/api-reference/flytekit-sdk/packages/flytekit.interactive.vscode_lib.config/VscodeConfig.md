---
title: VscodeConfig
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# VscodeConfig

**Package:** `flytekit.interactive.vscode_lib.config`

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
| `code_server_remote_paths` | `typing.Optional[typing.Dict[str, str]]` | |
| `code_server_dir_names` | `typing.Optional[typing.Dict[str, str]]` | |
| `extension_remote_paths` | `typing.Optional[typing.List[str]]` | |

## Methods

| Method | Description |
|-|-|
| [`add_extensions()`](#add_extensions) | Add additional extensions to the extension_remote_paths list. |


### add_extensions()

```python
def add_extensions(
    extensions: typing.Union[str, typing.List[str]],
)
```
Add additional extensions to the extension_remote_paths list.


| Parameter | Type | Description |
|-|-|-|
| `extensions` | `typing.Union[str, typing.List[str]]` | |

