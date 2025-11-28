---
title: flytekit.clis.sdk_in_container.serialize
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.serialize

## Directory

### Classes

| Class | Description |
|-|-|
| [`SerializationMode`](.././flytekit.clis.sdk_in_container.serialize#flytekitclissdk_in_containerserializeserializationmode) | Create a collection of name/value pairs. |

### Methods

| Method | Description |
|-|-|
| [`serialize_all()`](#serialize_all) | This function will write to the folder specified the following protobuf types. |


### Variables

| Property | Type | Description |
|-|-|-|
| `CTX_ENV` | `str` |  |
| `CTX_FLYTEKIT_VIRTUALENV_ROOT` | `str` |  |
| `CTX_IMAGE` | `str` |  |
| `CTX_LOCAL_SRC_ROOT` | `str` |  |
| `CTX_PACKAGES` | `str` |  |
| `CTX_PYTHON_INTERPRETER` | `str` |  |

## Methods

#### serialize_all()

```python
def serialize_all(
    pkgs: typing.List[str],
    local_source_root: typing.Optional[str],
    folder: typing.Optional[str],
    mode: typing.Optional[flytekit.clis.sdk_in_container.serialize.SerializationMode],
    image_config: typing.Optional[flytekit.configuration.ImageConfig],
    flytekit_virtualenv_root: typing.Optional[str],
    python_interpreter: typing.Optional[str],
    config_file: typing.Optional[str],
    env: typing.Optional[typing.Dict[str, str]],
)
```
This function will write to the folder specified the following protobuf types
```
flyteidl.admin.launch_plan_pb2.LaunchPlan
flyteidl.admin.workflow_pb2.WorkflowSpec
flyteidl.admin.task_pb2.TaskSpec
```

These can be inspected by calling (in the launch plan case)
```bash
flyte-cli parse-proto -f filename.pb -p flyteidl.admin.launch_plan_pb2.LaunchPlan
```

See {{< py_class_ref flytekit.models.core.identifier.ResourceType >}}   to match the trailing index in the file name with the
entity type.


| Parameter | Type | Description |
|-|-|-|
| `pkgs` | `typing.List[str]` | Dot-delimited Python packages/subpackages to look into for serialization. |
| `local_source_root` | `typing.Optional[str]` | Where to start looking for the code. |
| `folder` | `typing.Optional[str]` | Where to write the output protobuf files |
| `mode` | `typing.Optional[flytekit.clis.sdk_in_container.serialize.SerializationMode]` | Regular vs fast |
| `image_config` | `typing.Optional[flytekit.configuration.ImageConfig]` | ImageConfig object to use |
| `flytekit_virtualenv_root` | `typing.Optional[str]` | The full path of the virtual env in the container. |
| `python_interpreter` | `typing.Optional[str]` | |
| `config_file` | `typing.Optional[str]` | |
| `env` | `typing.Optional[typing.Dict[str, str]]` | |

## flytekit.clis.sdk_in_container.serialize.SerializationMode

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

  >>> Color.RED
  <Color.RED: 1>

- value lookup:

  >>> Color(1)
  <Color.RED: 1>

- name lookup:

  >>> Color['RED']
  <Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


