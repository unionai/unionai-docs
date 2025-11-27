---
title: SecretsManager
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SecretsManager

**Package:** `flytekit.core.context_manager`

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
| Parameter | Type | Description |
|-|-|-|
| `secrets_cfg` | `typing.Optional[SecretsConfig]` | |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Retrieves a secret using the resolution order -> Env followed by file. |
| [`get_secrets_env_var()`](#get_secrets_env_var) | Returns a string that matches the ENV Variable to look for the secrets. |
| [`get_secrets_file()`](#get_secrets_file) | Returns a path that matches the file to look for the secrets. |


### get()

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


| Parameter | Type | Description |
|-|-|-|
| `group` | `Optional[str]` | |
| `key` | `Optional[str]` | |
| `group_version` | `Optional[str]` | |
| `encode_mode` | `str` | |

### get_secrets_env_var()

```python
def get_secrets_env_var(
    group: Optional[str],
    key: Optional[str],
    group_version: Optional[str],
) -> str
```
Returns a string that matches the ENV Variable to look for the secrets


| Parameter | Type | Description |
|-|-|-|
| `group` | `Optional[str]` | |
| `key` | `Optional[str]` | |
| `group_version` | `Optional[str]` | |

### get_secrets_file()

```python
def get_secrets_file(
    group: Optional[str],
    key: Optional[str],
    group_version: Optional[str],
) -> str
```
Returns a path that matches the file to look for the secrets


| Parameter | Type | Description |
|-|-|-|
| `group` | `Optional[str]` | |
| `key` | `Optional[str]` | |
| `group_version` | `Optional[str]` | |

