---
title: PlatformConfig
version: 1.16.14
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
| `endpoint` | `str` | DNS for Flyte backend |
| `insecure` | `bool` | Whether or not to use SSL |
| `insecure_skip_verify` | `bool` | Whether to skip SSL certificate verification |
| `ca_cert_file_path` | `typing.Optional[str]` | [optional] str Root Cert to be loaded and used to verify admin |
| `console_endpoint` | `typing.Optional[str]` | endpoint for console if different from Flyte backend |
| `command` | `typing.Optional[typing.List[str]]` | This command is executed to return a token using an external process |
| `proxy_command` | `typing.Optional[typing.List[str]]` | This command is executed to return a token for proxy authorization using an external process |
| `client_id` | `typing.Optional[str]` | This is the public identifier for the app which handles authorization for a Flyte deployment. More details here: https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/. |
| `client_credentials_secret` | `typing.Optional[str]` | Used for service auth, which is automatically called during pyflyte. This will allow the Flyte engine to read the password directly from the environment variable. Note that this is less secure! Please only use this if mounting the secret as a file is impossible |
| `scopes` | `List[str]` | List of scopes to request. This is only applicable to the client credentials flow |
| `auth_mode` | `AuthType` | The OAuth mode to use. Defaults to pkce flow |
| `audience` | `typing.Optional[str]` | |
| `rpc_retries` | `int` | |
| `http_proxy_url` | `typing.Optional[str]` | [optional] HTTP Proxy to be used for OAuth requests |

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

