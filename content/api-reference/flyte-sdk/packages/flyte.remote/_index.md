---
title: flyte.remote
version: 2.0.0b57
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.remote


Remote Entities that are accessible from the Union Server once deployed or created.

## Directory

### Classes

| Class | Description |
|-|-|
| [`Action`](../flyte.remote/action) | A class representing an action. |
| [`ActionDetails`](../flyte.remote/actiondetails) | A class representing an action. |
| [`ActionInputs`](../flyte.remote/actioninputs) | A class representing the inputs of an action. |
| [`ActionOutputs`](../flyte.remote/actionoutputs) | A class representing the outputs of an action. |
| [`App`](../flyte.remote/app) |  |
| [`Project`](../flyte.remote/project) | A class representing a project in the Union API. |
| [`Run`](../flyte.remote/run) | A class representing a run of a task. |
| [`RunDetails`](../flyte.remote/rundetails) | A class representing a run of a task. |
| [`Secret`](../flyte.remote/secret) |  |
| [`Task`](../flyte.remote/task) |  |
| [`TaskDetails`](../flyte.remote/taskdetails) |  |
| [`Trigger`](../flyte.remote/trigger) | Represents a trigger in the Flyte platform. |
| [`User`](../flyte.remote/user) | Represents a user in the Flyte platform. |

### Methods

| Method | Description |
|-|-|
| [`auth_metadata()`](#auth_metadata) | This context manager allows you to pass contextualized auth metadata downstream to the Flyte authentication system. |
| [`create_channel()`](#create_channel) | Creates a new gRPC channel with appropriate authentication interceptors. |
| [`upload_dir()`](#upload_dir) | Uploads a directory to a remote location and returns the remote URI. |
| [`upload_file()`](#upload_file) | Uploads a file to a remote location and returns the remote URI. |


## Methods

#### auth_metadata()

```python
def auth_metadata(
    kv: typing.Tuple[str, str],
)
```
This context manager allows you to pass contextualized auth metadata downstream to the Flyte authentication system.

This is only useful if flyte.init_passthrough() has been called.

Example:
```python

flyte.init_passthrough("my-endpoint")

...

with auth_metadata((key1, value1), (key2, value2)):
    ...
```



| Parameter | Type | Description |
|-|-|-|
| `kv` | `typing.Tuple[str, str]` | |

#### create_channel()

```python
def create_channel(
    endpoint: str | None,
    api_key: str | None,
    insecure: typing.Optional[bool],
    insecure_skip_verify: typing.Optional[bool],
    ca_cert_file_path: typing.Optional[str],
    ssl_credentials: typing.Optional[ssl_channel_credentials],
    grpc_options: typing.Optional[typing.Sequence[typing.Tuple[str, typing.Any]]],
    compression: typing.Optional[grpc.Compression],
    http_session: httpx.AsyncClient | None,
    proxy_command: typing.Optional[typing.List[str]],
    kwargs,
) -> grpc.aio._base_channel.Channel
```
Creates a new gRPC channel with appropriate authentication interceptors.

This function creates either a secure or insecure gRPC channel based on the provided parameters,
and adds authentication interceptors to the channel. If SSL credentials are not provided,
they are created based on the insecure_skip_verify and ca_cert_file_path parameters.

The function is async because it may need to read certificate files asynchronously
and create authentication interceptors that perform async operations.



| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str \| None` | The endpoint URL for the gRPC channel |
| `api_key` | `str \| None` | API key for authentication; if provided, it will be used to detect the endpoint and credentials. |
| `insecure` | `typing.Optional[bool]` | Whether to use an insecure channel (no SSL) |
| `insecure_skip_verify` | `typing.Optional[bool]` | Whether to skip SSL certificate verification |
| `ca_cert_file_path` | `typing.Optional[str]` | Path to CA certificate file for SSL verification |
| `ssl_credentials` | `typing.Optional[ssl_channel_credentials]` | Pre-configured SSL credentials for the channel |
| `grpc_options` | `typing.Optional[typing.Sequence[typing.Tuple[str, typing.Any]]]` | Additional gRPC channel options |
| `compression` | `typing.Optional[grpc.Compression]` | Compression method for the channel |
| `http_session` | `httpx.AsyncClient \| None` | Pre-configured HTTP session to use for requests |
| `proxy_command` | `typing.Optional[typing.List[str]]` | List of strings for proxy command configuration |
| `kwargs` | `**kwargs` | Additional arguments passed to various functions - For grpc.aio.insecure_channel/secure_channel: - root_certificates: Root certificates for SSL credentials - private_key: Private key for SSL credentials - certificate_chain: Certificate chain for SSL credentials - options: gRPC channel options - compression: gRPC compression method - For proxy configuration: - proxy_env: Dict of environment variables for proxy - proxy_timeout: Timeout for proxy connection - For authentication interceptors (passed to create_auth_interceptors and create_proxy_auth_interceptors): - auth_type: The authentication type to use ("Pkce", "ClientSecret", "ExternalCommand", "DeviceFlow") - command: Command to execute for ExternalCommand authentication - client_id: Client ID for ClientSecret authentication - client_secret: Client secret for ClientSecret authentication - client_credentials_secret: Client secret for ClientSecret authentication (alias) - scopes: List of scopes to request during authentication - audience: Audience for the token - http_proxy_url: HTTP proxy URL - verify: Whether to verify SSL certificates - ca_cert_path: Optional path to CA certificate file - header_key: Header key to use for authentication - redirect_uri: OAuth2 redirect URI for PKCE authentication - add_request_auth_code_params_to_request_access_token_params: Whether to add auth code params to token request - request_auth_code_params: Parameters to add to login URI opened in browser - request_access_token_params: Parameters to add when exchanging auth code for access token - refresh_access_token_params: Parameters to add when refreshing access token :return: grpc.aio.Channel with authentication interceptors configured |

#### upload_dir()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await upload_dir.aio()`.
```python
def upload_dir(
    dir_path: pathlib._local.Path,
    verify: bool,
    prefix: str | None,
) -> str
```
Uploads a directory to a remote location and returns the remote URI.



| Parameter | Type | Description |
|-|-|-|
| `dir_path` | `pathlib._local.Path` | The directory path to upload. |
| `verify` | `bool` | Whether to verify the certificate for HTTPS requests. :return: The remote URI of the uploaded directory. |
| `prefix` | `str \| None` | |

#### upload_file()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await upload_file.aio()`.
```python
def upload_file(
    fp: pathlib._local.Path,
    verify: bool,
    fname: str | None,
) -> typing.Tuple[str, str]
```
Uploads a file to a remote location and returns the remote URI.



| Parameter | Type | Description |
|-|-|-|
| `fp` | `pathlib._local.Path` | The file path to upload. |
| `verify` | `bool` | Whether to verify the certificate for HTTPS requests. |
| `fname` | `str \| None` | Optional file name for the remote path. :return: Tuple of (MD5 digest hex string, remote native URL). |

