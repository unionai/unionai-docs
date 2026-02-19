---
title: SerializationSettings
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SerializationSettings

**Package:** `flytekit.configuration`

These settings are provided while serializing a workflow and task, before registration. This is required to get
runtime information at serialization time, as well as some defaults.

Attributes:
    project (str): The project (if any) with which to register entities under.
    domain (str): The domain (if any) with which to register entities under.
    version (str): The version (if any) with which to register entities under.
    image_config (ImageConfig): The image config used to define task container images.
    env (Optional[Dict[str, str]]): Environment variables injected into task container definitions.
    default_resources (Optional[ResourceSpec]): The resources to request for the task - this is useful
        if users need to override the default resource spec of an entity at registration time.
    flytekit_virtualenv_root (Optional[str]):  During out of container serialize the absolute path of the flytekit
        virtualenv at serialization time won't match the in-container value at execution time. This optional value
        is used to provide the in-container virtualenv path
    python_interpreter (Optional[str]): The python executable to use. This is used for spark tasks in out of
        container execution.
    entrypoint_settings (Optional[EntrypointSettings]): Information about the command, path and version of the
        entrypoint program.
    fast_serialization_settings (Optional[FastSerializationSettings]): If the code is being serialized so that it
        can be fast registered (and thus omit building a Docker image) this object contains additional parameters
        for serialization.
    source_root (Optional[str]): The root directory of the source code.



```python
class SerializationSettings(
    image_config: ImageConfig,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    version: typing.Optional[str],
    env: Optional[Dict[str, str]],
    default_resources: Optional[ResourceSpec],
    git_repo: Optional[str],
    python_interpreter: str,
    flytekit_virtualenv_root: Optional[str],
    fast_serialization_settings: Optional[FastSerializationSettings],
    source_root: Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `image_config` | `ImageConfig` | |
| `project` | `typing.Optional[str]` | |
| `domain` | `typing.Optional[str]` | |
| `version` | `typing.Optional[str]` | |
| `env` | `Optional[Dict[str, str]]` | |
| `default_resources` | `Optional[ResourceSpec]` | |
| `git_repo` | `Optional[str]` | |
| `python_interpreter` | `str` | |
| `flytekit_virtualenv_root` | `Optional[str]` | |
| `fast_serialization_settings` | `Optional[FastSerializationSettings]` | |
| `source_root` | `Optional[str]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `entrypoint_settings` | `None` |  |
| `serialized_context` | `None` | :return: returns the serialization context as a base64encoded, gzip compressed, json strinnn |

## Methods

| Method | Description |
|-|-|
| [`default_entrypoint_settings()`](#default_entrypoint_settings) | Assumes the entrypoint is installed in a virtual-environment where the interpreter is. |
| [`for_image()`](#for_image) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_transport()`](#from_transport) |  |
| [`new_builder()`](#new_builder) | Creates a ``SerializationSettings. |
| [`schema()`](#schema) |  |
| [`should_fast_serialize()`](#should_fast_serialize) | Whether or not the serialization settings specify that entities should be serialized for fast registration. |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |
| [`venv_root_from_interpreter()`](#venv_root_from_interpreter) | Computes the path of the virtual environment root, based on the passed in python interpreter path. |
| [`with_serialized_context()`](#with_serialized_context) | Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext. |


### default_entrypoint_settings()

```python
def default_entrypoint_settings(
    interpreter_path: str,
) -> EntrypointSettings
```
Assumes the entrypoint is installed in a virtual-environment where the interpreter is


| Parameter | Type | Description |
|-|-|-|
| `interpreter_path` | `str` | |

### for_image()

```python
def for_image(
    image: str,
    version: str,
    project: str,
    domain: str,
    python_interpreter_path: str,
) -> SerializationSettings
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `str` | |
| `version` | `str` | |
| `project` | `str` | |
| `domain` | `str` | |
| `python_interpreter_path` | `str` | |

### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` | |
| `infer_missing` |  | |

### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` | |
| `parse_float` |  | |
| `parse_int` |  | |
| `parse_constant` |  | |
| `infer_missing` |  | |
| `kw` |  | |

### from_transport()

```python
def from_transport(
    s: str,
) -> SerializationSettings
```
| Parameter | Type | Description |
|-|-|-|
| `s` | `str` | |

### new_builder()

```python
def new_builder()
```
Creates a ``SerializationSettings.Builder`` that copies the existing serialization settings parameters and
allows for customization.


### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type | Description |
|-|-|-|
| `infer_missing` | `bool` | |
| `only` |  | |
| `exclude` |  | |
| `many` | `bool` | |
| `context` |  | |
| `load_only` |  | |
| `dump_only` |  | |
| `partial` | `bool` | |
| `unknown` |  | |

### should_fast_serialize()

```python
def should_fast_serialize()
```
Whether or not the serialization settings specify that entities should be serialized for fast registration.


### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type | Description |
|-|-|-|
| `encode_json` |  | |

### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `skipkeys` | `bool` | |
| `ensure_ascii` | `bool` | |
| `check_circular` | `bool` | |
| `allow_nan` | `bool` | |
| `indent` | `typing.Union[int, str, NoneType]` | |
| `separators` | `typing.Tuple[str, str]` | |
| `default` | `typing.Callable` | |
| `sort_keys` | `bool` | |
| `kw` |  | |

### venv_root_from_interpreter()

```python
def venv_root_from_interpreter(
    interpreter_path: str,
) -> str
```
Computes the path of the virtual environment root, based on the passed in python interpreter path
for example /opt/venv/bin/python3 -&gt; /opt/venv


| Parameter | Type | Description |
|-|-|-|
| `interpreter_path` | `str` | |

### with_serialized_context()

```python
def with_serialized_context()
```
Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext
This is useful in transporting SerializedContext to serialized and registered tasks.
The setting will be available in the `env` field with the key `SERIALIZED_CONTEXT_ENV_VAR`
:return: A newly constructed SerializationSettings, or self, if it already has the serializationSettings


