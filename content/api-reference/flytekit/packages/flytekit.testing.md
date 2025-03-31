---
title: flytekit.testing
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.testing


=====================
Unit Testing
=====================

.. currentmodule:: flytekit.testing

The imports exposed in this package will help you unit test your Flyte tasks. These are particularly helpful when
testing workflows that contain tasks that cannot run locally (a Hive task for instance).

.. autosummary::
   :template: custom.rst
   :toctree: generated/

   patch - A decorator similar to the regular one you're probably used to
   task_mock - Non-decorative function


## Directory

### Classes

| Class | Description |
|-|-|
| [`SecretsManager`](.././flytekit.testing#flytekittestingsecretsmanager) | This provides a secrets resolution logic at runtime. |

### Methods

| Method | Description |
|-|-|
| [`patch()`](#patch) | This is a decorator used for testing. |
| [`task_mock()`](#task_mock) | Use this method to mock a task declaration. |


## Methods

#### patch()

```python
def patch(
    target: typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.workflow.WorkflowBase, flytekit.core.reference_entity.ReferenceEntity],
)
```
This is a decorator used for testing.


| Parameter | Type |
|-|-|
| `target` | `typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.workflow.WorkflowBase, flytekit.core.reference_entity.ReferenceEntity]` |

#### task_mock()

```python
def task_mock(
    t: flytekit.core.base_task.PythonTask,
) -> typing.Generator[unittest.mock.MagicMock, NoneType, NoneType]
```
Use this method to mock a task declaration. It can mock any Task in Flytekit as long as it has a python native
interface associated with it.

The returned object is a MagicMock and allows to perform all such methods. This MagicMock, mocks the execute method
on the PythonTask

Usage:

.. code-block:: python

@task
def t1(i: int) -> int:
pass

with task_mock(t1) as m:
m.side_effect = lambda x: x
t1(10)
# The mock is valid only within this context


| Parameter | Type |
|-|-|
| `t` | `flytekit.core.base_task.PythonTask` |

## flytekit.testing.SecretsManager

This provides a secrets resolution logic at runtime.
The resolution order is
- Try env var first. The env var should have the configuration.SECRETS_ENV_PREFIX. The env var will be all upper
cased
- If not then try the file where the name matches lower case
``configuration.SECRETS_DEFAULT_DIR/<group>/configuration.SECRETS_FILE_PREFIX<key>``

All configuration values can always be overridden by injecting an environment variable


```python
class SecretsManager(
    secrets_cfg: typing.Optional[SecretsConfig],
)
```
| Parameter | Type |
|-|-|
| `secrets_cfg` | `typing.Optional[SecretsConfig]` |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Retrieves a secret using the resolution order -> Env followed by file. |
| [`get_secrets_env_var()`](#get_secrets_env_var) | Returns a string that matches the ENV Variable to look for the secrets. |
| [`get_secrets_file()`](#get_secrets_file) | Returns a path that matches the file to look for the secrets. |


#### get()

```python
def get(
    group: Optional[str],
    key: Optional[str],
    group_version: Optional[str],
    encode_mode: str,
) -> str
```
Retrieves a secret using the resolution order -> Env followed by file. If not found raises a ValueError
param encode_mode, defines the mode to open files, it can either be "r" to read file, or "rb" to read binary file


| Parameter | Type |
|-|-|
| `group` | `Optional[str]` |
| `key` | `Optional[str]` |
| `group_version` | `Optional[str]` |
| `encode_mode` | `str` |

#### get_secrets_env_var()

```python
def get_secrets_env_var(
    group: Optional[str],
    key: Optional[str],
    group_version: Optional[str],
) -> str
```
Returns a string that matches the ENV Variable to look for the secrets


| Parameter | Type |
|-|-|
| `group` | `Optional[str]` |
| `key` | `Optional[str]` |
| `group_version` | `Optional[str]` |

#### get_secrets_file()

```python
def get_secrets_file(
    group: Optional[str],
    key: Optional[str],
    group_version: Optional[str],
) -> str
```
Returns a path that matches the file to look for the secrets


| Parameter | Type |
|-|-|
| `group` | `Optional[str]` |
| `key` | `Optional[str]` |
| `group_version` | `Optional[str]` |

