---
title: flytekit.clients.auth.token_client
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.auth.token_client

## Directory

### Classes

| Class | Description |
|-|-|
| [`DeviceCodeResponse`](.././flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientdevicecoderesponse) | Response from device auth flow endpoint. |

### Methods

| Method | Description |
|-|-|
| [`get_basic_authorization_header()`](#get_basic_authorization_header) | This function transforms the client id and the client secret into a header that conforms with http basic auth. |
| [`get_device_code()`](#get_device_code) | Retrieves the device Authentication code that can be done to authenticate the request using a browser on a. |
| [`get_token()`](#get_token) | :rtype: (Text,Text,Int) The first element is the access token retrieved from the IDP, the second is the refresh token. |
| [`poll_token_endpoint()`](#poll_token_endpoint) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `error_auth_pending` | `str` |  |
| `error_slow_down` | `str` |  |
| `utf_8` | `str` |  |

## Methods

#### get_basic_authorization_header()

```python
def get_basic_authorization_header(
    client_id: str,
    client_secret: str,
) -> e: str
```
This function transforms the client id and the client secret into a header that conforms with http basic auth.
It joins the id and the secret with a : then base64 encodes it, then adds the appropriate text. Secrets are
first URL encoded to escape illegal characters.



| Parameter | Type |
|-|-|
| `client_id` | `str` |
| `client_secret` | `str` |

#### get_device_code()

```python
def get_device_code(
    device_auth_endpoint: str,
    client_id: str,
    audience: typing.Optional[str],
    scope: typing.Optional[typing.List[str]],
    http_proxy_url: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
    session: typing.Optional[requests.sessions.Session],
) -> flytekit.clients.auth.token_client.DeviceCodeResponse
```
Retrieves the device Authentication code that can be done to authenticate the request using a browser on a
separate device


| Parameter | Type |
|-|-|
| `device_auth_endpoint` | `str` |
| `client_id` | `str` |
| `audience` | `typing.Optional[str]` |
| `scope` | `typing.Optional[typing.List[str]]` |
| `http_proxy_url` | `typing.Optional[str]` |
| `verify` | `typing.Union[bool, str, NoneType]` |
| `session` | `typing.Optional[requests.sessions.Session]` |

#### get_token()

```python
def get_token(
    token_endpoint: str,
    scopes: typing.Optional[typing.List[str]],
    authorization_header: typing.Optional[str],
    client_id: typing.Optional[str],
    device_code: typing.Optional[str],
    audience: typing.Optional[str],
    grant_type: <enum 'GrantType'>,
    http_proxy_url: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
    session: typing.Optional[requests.sessions.Session],
    refresh_token: typing.Optional[str],
) -> e: (Text,Text,Int) The first element is the access token retrieved from the IDP, the second is the refresh token
```
:rtype: (Text,Text,Int) The first element is the access token retrieved from the IDP, the second is the refresh token
retrieved from the IDP, the third is the expiration in seconds


| Parameter | Type |
|-|-|
| `token_endpoint` | `str` |
| `scopes` | `typing.Optional[typing.List[str]]` |
| `authorization_header` | `typing.Optional[str]` |
| `client_id` | `typing.Optional[str]` |
| `device_code` | `typing.Optional[str]` |
| `audience` | `typing.Optional[str]` |
| `grant_type` | `<enum 'GrantType'>` |
| `http_proxy_url` | `typing.Optional[str]` |
| `verify` | `typing.Union[bool, str, NoneType]` |
| `session` | `typing.Optional[requests.sessions.Session]` |
| `refresh_token` | `typing.Optional[str]` |

#### poll_token_endpoint()

```python
def poll_token_endpoint(
    resp: flytekit.clients.auth.token_client.DeviceCodeResponse,
    token_endpoint: str,
    client_id: str,
    audience: typing.Optional[str],
    scopes: typing.Optional[str],
    http_proxy_url: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
) -> typing.Tuple[str, str, int]
```
| Parameter | Type |
|-|-|
| `resp` | `flytekit.clients.auth.token_client.DeviceCodeResponse` |
| `token_endpoint` | `str` |
| `client_id` | `str` |
| `audience` | `typing.Optional[str]` |
| `scopes` | `typing.Optional[str]` |
| `http_proxy_url` | `typing.Optional[str]` |
| `verify` | `typing.Union[bool, str, NoneType]` |

## flytekit.clients.auth.token_client.DeviceCodeResponse

Response from device auth flow endpoint
{'device_code': 'code',
     'user_code': 'BNDJJFXL',
     'verification_uri': 'url',
     'expires_in': 600,
     'interval': 5}


```python
class DeviceCodeResponse(
    device_code: str,
    user_code: str,
    verification_uri: str,
    expires_in: int,
    interval: int,
)
```
| Parameter | Type |
|-|-|
| `device_code` | `str` |
| `user_code` | `str` |
| `verification_uri` | `str` |
| `expires_in` | `int` |
| `interval` | `int` |

### Methods

| Method | Description |
|-|-|
| [`from_json_response()`](#from_json_response) |  |


#### from_json_response()

```python
def from_json_response(
    j: typing.Dict,
) -> DeviceCodeResponse
```
| Parameter | Type |
|-|-|
| `j` | `typing.Dict` |

