---
title: PlatformConfig
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PlatformConfig

**Package:** `flytekit.configuration`

This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically).



```python
class PlatformConfig(
    endpoint: str,
    insecure: bool,
    insecure_skip_verify: bool,
    ca_cert_file_path: typing.Optional[str],
    console_endpoint: typing.Optional[str],
    command: typing.Optional[typing.List[str]],
    proxy_command: typing.Optional[typing.List[str]],
    client_id: typing.Optional[str],
    client_credentials_secret: typing.Optional[str],
    scopes: List[str],
    auth_mode: AuthType,
    audience: typing.Optional[str],
    rpc_retries: int,
    http_proxy_url: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |
| `insecure` | `bool` | |
| `insecure_skip_verify` | `bool` | |
| `ca_cert_file_path` | `typing.Optional[str]` | |
| `console_endpoint` | `typing.Optional[str]` | |
| `command` | `typing.Optional[typing.List[str]]` | |
| `proxy_command` | `typing.Optional[typing.List[str]]` | |
| `client_id` | `typing.Optional[str]` | |
| `client_credentials_secret` | `typing.Optional[str]` | |
| `scopes` | `List[str]` | |
| `auth_mode` | `AuthType` | |
| `audience` | `typing.Optional[str]` | |
| `rpc_retries` | `int` | |
| `http_proxy_url` | `typing.Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from Config file, and overrides from Environment variables. |
| [`for_endpoint()`](#for_endpoint) |  |


### auto()

```python
def auto(
    config_file: typing.Optional[typing.Union[str, ConfigFile]],
) -> PlatformConfig
```
Reads from Config file, and overrides from Environment variables. Refer to ConfigEntry for details


| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Optional[typing.Union[str, ConfigFile]]` | :return: |

### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
) -> PlatformConfig
```
| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |
| `insecure` | `bool` | |

