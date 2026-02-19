---
title: Container
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Container

**Package:** `flytekit.models.task`

```python
class Container(
    image,
    command,
    args,
    resources,
    env,
    config,
    data_loading_config,
)
```
This defines a container target.  It will execute the appropriate command line on the appropriate image with
the given configurations.



| Parameter | Type | Description |
|-|-|-|
| `image` |  | |
| `command` |  | |
| `args` | `*args` | |
| `resources` |  | |
| `env` |  | |
| `config` |  | |
| `data_loading_config` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `args` | `None` | A list of arguments for the command.  i.e. ['s3://some/path', '/tmp/local/path'] rtype: list[Text] |
| `command` | `None` | A list of 'words' for the command.  i.e. ['aws', 's3', 'ls'] :rtype: list[Text] |
| `config` | `None` | A definition of key-value pairs for configuration.  Currently, only str-&gt;str is     supported. :rtype: dict[Text, Text] |
| `data_loading_config` | `None` | :rtype: DataLoadingConfig |
| `env` | `None` | A definition of key-value pairs for environment variables.  Currently, only str-&gt;str is     supported. :rtype: dict[Text, Text] |
| `image` | `None` | The fully-qualified identifier for the image. :rtype: Text |
| `is_empty` | `None` |  |
| `resources` | `None` | A definition of requisite compute resources. :rtype: Resources |

## Methods

| Method | Description |
|-|-|
| [`add_env()`](#add_env) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### add_env()

```python
def add_env(
    key: str,
    val: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` | `str` | |
| `val` | `str` | |

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.tasks_pb2.Container


