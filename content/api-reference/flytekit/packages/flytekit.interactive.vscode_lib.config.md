---
title: flytekit.interactive.vscode_lib.config
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.interactive.vscode_lib.config

## Directory

### Classes

| Class | Description |
|-|-|
| [`VscodeConfig`](.././flytekit.interactive.vscode_lib.config#flytekitinteractivevscode_libconfigvscodeconfig) | VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |

### Methods

| Method | Description |
|-|-|
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`field()`](#field) | Return an object to identify dataclass fields. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_CODE_SERVER_DIR_NAMES` | `dict` |  |
| `DEFAULT_CODE_SERVER_EXTENSIONS` | `list` |  |
| `DEFAULT_CODE_SERVER_REMOTE_PATHS` | `dict` |  |

## Methods

#### dataclass()

```python
def dataclass(
    cls,
    init,
    repr,
    eq,
    order,
    unsafe_hash,
    frozen,
    match_args,
    kw_only,
    slots,
    weakref_slot,
)
```
Add dunder methods based on the fields defined in the class.

Examines PEP 526 __annotations__ to determine fields.

If init is true, an __init__() method is added to the class. If repr
is true, a __repr__() method is added. If order is true, rich
comparison dunder methods are added. If unsafe_hash is true, a
__hash__() method is added. If frozen is true, fields may not be
assigned to after instance creation. If match_args is true, the
__match_args__ tuple is added. If kw_only is true, then by default
all fields are keyword-only. If slots is true, a new class with a
__slots__ attribute is returned.


| Parameter | Type |
|-|-|
| `cls` |  |
| `init` |  |
| `repr` |  |
| `eq` |  |
| `order` |  |
| `unsafe_hash` |  |
| `frozen` |  |
| `match_args` |  |
| `kw_only` |  |
| `slots` |  |
| `weakref_slot` |  |

#### field()

```python
def field(
    default,
    default_factory,
    init,
    repr,
    hash,
    compare,
    metadata,
    kw_only,
)
```
Return an object to identify dataclass fields.

default is the default value of the field.  default_factory is a
0-argument function called to initialize a field's value.  If init
is true, the field will be a parameter to the class's __init__()
function.  If repr is true, the field will be included in the
object's repr().  If hash is true, the field will be included in the
object's hash().  If compare is true, the field will be used in
comparison functions.  metadata, if specified, must be a mapping
which is stored but not otherwise examined by dataclass.  If kw_only
is true, the field will become a keyword-only parameter to
__init__().

It is an error to specify both default and default_factory.


| Parameter | Type |
|-|-|
| `default` |  |
| `default_factory` |  |
| `init` |  |
| `repr` |  |
| `hash` |  |
| `compare` |  |
| `metadata` |  |
| `kw_only` |  |

## flytekit.interactive.vscode_lib.config.VscodeConfig

VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths.



```python
class VscodeConfig(
    code_server_remote_paths: typing.Optional[typing.Dict[str, str]],
    code_server_dir_names: typing.Optional[typing.Dict[str, str]],
    extension_remote_paths: typing.Optional[typing.List[str]],
)
```
| Parameter | Type |
|-|-|
| `code_server_remote_paths` | `typing.Optional[typing.Dict[str, str]]` |
| `code_server_dir_names` | `typing.Optional[typing.Dict[str, str]]` |
| `extension_remote_paths` | `typing.Optional[typing.List[str]]` |

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


| Parameter | Type |
|-|-|
| `extensions` | `typing.Union[str, typing.List[str]]` |

