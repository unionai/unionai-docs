---
title: flytekit.testing
version: 1.15.4.dev2+g3e3ce2426
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

## flytekit.testing.SecretsManager

This provides a secrets resolution logic at runtime.
The resolution order is
- Try env var first. The env var should have the configuration.SECRETS_ENV_PREFIX. The env var will be all upper
cased
- If not then try the file where the name matches lower case
``configuration.SECRETS_DEFAULT_DIR/<group>/configuration.SECRETS_FILE_PREFIX<key>``

All configuration values can always be overridden by injecting an environment variable


```python
def SecretsManager(
    secrets_cfg: typing.Optional[SecretsConfig],
):
```
| Parameter | Type |
|-|-|
| `secrets_cfg` | `typing.Optional[SecretsConfig]` |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Retrieves a secret using the resolution order -> Env followed by file |
| [`get_secrets_env_var()`](#get_secrets_env_var) | Returns a string that matches the ENV Variable to look for the secrets |
| [`get_secrets_file()`](#get_secrets_file) | Returns a path that matches the file to look for the secrets |


#### get()

```python
def get(
    group: Optional[str],
    key: Optional[str],
    group_version: Optional[str],
    encode_mode: str,
):
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
):
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
):
```
Returns a path that matches the file to look for the secrets


| Parameter | Type |
|-|-|
| `group` | `Optional[str]` |
| `key` | `Optional[str]` |
| `group_version` | `Optional[str]` |

