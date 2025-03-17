---
title: PlatformConfig
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# PlatformConfig

**Package:** `flytekit.configuration`

This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically).



```python
def PlatformConfig(
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
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
| `insecure_skip_verify` | `bool` |
| `ca_cert_file_path` | `typing.Optional[str]` |
| `console_endpoint` | `typing.Optional[str]` |
| `command` | `typing.Optional[typing.List[str]]` |
| `proxy_command` | `typing.Optional[typing.List[str]]` |
| `client_id` | `typing.Optional[str]` |
| `client_credentials_secret` | `typing.Optional[str]` |
| `scopes` | `List[str]` |
| `auth_mode` | `AuthType` |
| `audience` | `typing.Optional[str]` |
| `rpc_retries` | `int` |
| `http_proxy_url` | `typing.Optional[str]` |
## Methods

### auto()

```python
def auto(
    config_file: typing.Optional[typing.Union[str, ConfigFile]],
):
```
Reads from Config file, and overrides from Environment variables. Refer to ConfigEntry for details


| Parameter | Type |
|-|-|
| `config_file` | `typing.Optional[typing.Union[str, ConfigFile]]` |
### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
):
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
