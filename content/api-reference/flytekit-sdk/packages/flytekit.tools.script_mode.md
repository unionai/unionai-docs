---
title: flytekit.tools.script_mode
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.tools.script_mode

## Directory

### Methods

| Method | Description |
|-|-|
| [`add_imported_modules_from_source()`](#add_imported_modules_from_source) | Copies modules into destination that are in modules. |
| [`compress_scripts()`](#compress_scripts) | Compresses the single script while maintaining the folder structure for that file. |
| [`get_all_modules()`](#get_all_modules) | Import python file with module_name in source_path and return all modules. |
| [`list_all_files()`](#list_all_files) |  |
| [`list_imported_modules_as_files()`](#list_imported_modules_as_files) | Copies modules into destination that are in modules. |
| [`ls_files()`](#ls_files) | user_modules_and_packages is a list of the Python modules and packages, expressed as absolute paths, that the. |
| [`tar_strip_file_attributes()`](#tar_strip_file_attributes) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `EXCLUDE_DIRS` | `set` |  |

## Methods

#### add_imported_modules_from_source()

```python
def add_imported_modules_from_source(
    source_path: str,
    destination: str,
    modules: List[ModuleType],
)
```
Copies modules into destination that are in modules. The module files are copied only if:

1. Not a site-packages. These are installed packages and not user files.
2. Not in the sys.base_prefix or sys.prefix. These are also installed and not user files.
3. Does not share a common path with the source_path.


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `destination` | `str` |
| `modules` | `List[ModuleType]` |

#### compress_scripts()

```python
def compress_scripts(
    source_path: str,
    destination: str,
    modules: List[ModuleType],
)
```
Compresses the single script while maintaining the folder structure for that file.

For example, given the follow file structure:
.
├── flyte
│   ├── __init__.py
│   └── workflows
│       ├── example.py
│       ├── another_example.py
│       ├── yet_another_example.py
│       ├── unused_example.py
│       └── __init__.py

Let's say you want to compress `example.py` imports `another_example.py`. And `another_example.py`
imports on `yet_another_example.py`. This will  produce a tar file that contains only that
file alongside with the folder structure, i.e.:

.
├── flyte
│   ├── __init__.py
│   └── workflows
│       ├── example.py
│       ├── another_example.py
│       ├── yet_another_example.py
│       └── __init__.py


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `destination` | `str` |
| `modules` | `List[ModuleType]` |

#### get_all_modules()

```python
def get_all_modules(
    source_path: str,
    module_name: Optional[str],
) -> List[ModuleType]
```
Import python file with module_name in source_path and return all modules.


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `module_name` | `Optional[str]` |

#### list_all_files()

```python
def list_all_files(
    source_path: str,
    deref_symlinks,
    ignore_group: Optional[IgnoreGroup],
) -> List[str]
```
| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `deref_symlinks` |  |
| `ignore_group` | `Optional[IgnoreGroup]` |

#### list_imported_modules_as_files()

```python
def list_imported_modules_as_files(
    source_path: str,
    modules: List[ModuleType],
) -> List[str]
```
Copies modules into destination that are in modules. The module files are copied only if:

1. Not a site-packages. These are installed packages and not user files.
2. Not in the sys.base_prefix or sys.prefix. These are also installed and not user files.
3. Does not share a common path with the source_path.


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `modules` | `List[ModuleType]` |

#### ls_files()

```python
def ls_files(
    source_path: str,
    copy_file_detection: CopyFileDetection,
    deref_symlinks: bool,
    ignore_group: Optional[IgnoreGroup],
) -> Tuple[List[str], str]
```
user_modules_and_packages is a list of the Python modules and packages, expressed as absolute paths, that the
user has run this pyflyte command with. For pyflyte run for instance, this is just a list of one.
This is used for two reasons.
  - Everything in this list needs to be returned. Files are returned and folders are walked.
  - A common source path is derived from this is, which is just the common folder that contains everything in the
    list. For ex. if you do
    $ pyflyte --pkgs a.b,a.c package
    Then the common root is just the folder a/. The modules list is filtered against this root. Only files
    representing modules under this root are included

If the copy enum is set to loaded_modules, then the loaded sys modules will be used.


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `copy_file_detection` | `CopyFileDetection` |
| `deref_symlinks` | `bool` |
| `ignore_group` | `Optional[IgnoreGroup]` |

#### tar_strip_file_attributes()

```python
def tar_strip_file_attributes(
    tar_info: tarfile.TarInfo,
) -> tarfile.TarInfo
```
| Parameter | Type |
|-|-|
| `tar_info` | `tarfile.TarInfo` |

