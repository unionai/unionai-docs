---
title: flyte.config
version: 0.2.0b4.dev1+g1e3e3e4
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.config

## Directory

### Classes

| Class | Description |
|-|-|
| [`Config`](.././flyte.config#flyteconfigconfig) | This the parent configuration object and holds all the underlying configuration object types. |
| [`PlatformConfig`](.././flyte.config#flyteconfigplatformconfig) | This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`TaskConfig`](.././flyte.config#flyteconfigtaskconfig) |  |

### Methods

| Method | Description |
|-|-|
| [`set_if_exists()`](#set_if_exists) | Given a dict ``d`` sets the key ``k`` with value of config ``v``, if the config value ``v`` is set. |


### Variables

| Property | Type | Description |
|-|-|-|
| `TYPE_CHECKING` | `bool` |  |

## Methods

#### set_if_exists()

```python
def set_if_exists(
    d: dict,
    k: str,
    val: typing.Any,
) -> dict
```
Given a dict ``d`` sets the key ``k`` with value of config ``v``, if the config value ``v`` is set
and return the updated dictionary.


| Parameter | Type |
|-|-|
| `d` | `dict` |
| `k` | `str` |
| `val` | `typing.Any` |

## flyte.config.Config

This the parent configuration object and holds all the underlying configuration object types. An instance of
this object holds all the config necessary to

1. Interactive session with Flyte backend
2. Some parts are required for Serialization, for example Platform Config is not required
3. Runtime of a task


```python
class Config(
    platform: PlatformConfig,
    task: TaskConfig,
    source: pathlib.Path | None,
)
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig` |
| `task` | `TaskConfig` |
| `source` | `pathlib.Path \| None` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Automatically constructs the Config Object. |
| [`with_params()`](#with_params) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
) -> 'Config'
```
Automatically constructs the Config Object. The order of precedence is as follows
  1. first try to find any env vars that match the config vars specified in the FLYTE_CONFIG format.
  2. If not found in environment then values ar read from the config file
  3. If not found in the file, then the default values are used.



| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile, None]` |

#### with_params()

```python
def with_params(
    platform: PlatformConfig | None,
    task: TaskConfig | None,
) -> 'Config'
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig \| None` |
| `task` | `TaskConfig \| None` |

## flyte.config.PlatformConfig

This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically).



```python
class PlatformConfig(
    endpoint: str | None,
    insecure: bool,
    insecure_skip_verify: bool,
    ca_cert_file_path: typing.Optional[str],
    console_endpoint: typing.Optional[str],
    command: typing.Optional[typing.List[str]],
    proxy_command: typing.Optional[typing.List[str]],
    client_id: typing.Optional[str],
    client_credentials_secret: typing.Optional[str],
    scopes: typing.List[str],
    auth_mode: 'AuthType',
    audience: typing.Optional[str],
    rpc_retries: int,
    http_proxy_url: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `endpoint` | `str \| None` |
| `insecure` | `bool` |
| `insecure_skip_verify` | `bool` |
| `ca_cert_file_path` | `typing.Optional[str]` |
| `console_endpoint` | `typing.Optional[str]` |
| `command` | `typing.Optional[typing.List[str]]` |
| `proxy_command` | `typing.Optional[typing.List[str]]` |
| `client_id` | `typing.Optional[str]` |
| `client_credentials_secret` | `typing.Optional[str]` |
| `scopes` | `typing.List[str]` |
| `auth_mode` | `'AuthType'` |
| `audience` | `typing.Optional[str]` |
| `rpc_retries` | `int` |
| `http_proxy_url` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from a config file, and overrides from Environment variables. |
| [`for_endpoint()`](#for_endpoint) |  |


#### auto()

```python
def auto(
    config_file: typing.Optional[typing.Union[str, ConfigFile]],
) -> 'PlatformConfig'
```
Reads from a config file, and overrides from Environment variables. Refer to ConfigEntry for details


| Parameter | Type |
|-|-|
| `config_file` | `typing.Optional[typing.Union[str, ConfigFile]]` |

#### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
) -> 'PlatformConfig'
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |

## flyte.config.TaskConfig

```python
class TaskConfig(
    org: str | None,
    project: str | None,
    domain: str | None,
)
```
| Parameter | Type |
|-|-|
| `org` | `str \| None` |
| `project` | `str \| None` |
| `domain` | `str \| None` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from a config file, and overrides from Environment variables. |


#### auto()

```python
def auto(
    config_file: typing.Optional[typing.Union[str, ConfigFile]],
) -> 'TaskConfig'
```
Reads from a config file, and overrides from Environment variables. Refer to ConfigEntry for details


| Parameter | Type |
|-|-|
| `config_file` | `typing.Optional[typing.Union[str, ConfigFile]]` |

