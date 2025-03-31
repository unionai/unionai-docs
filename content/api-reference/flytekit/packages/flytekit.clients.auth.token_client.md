---
title: flytekit.clients.auth.token_client
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clients.auth.token_client

## Directory

### Classes

| Class | Description |
|-|-|
| [`DeviceCodeResponse`](.././flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientdevicecoderesponse) | Response from device auth flow endpoint. |
| [`GrantType`](.././flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientgranttype) | str(object='') -> str. |
| [`datetime`](.././flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientdatetime) | datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`timedelta`](.././flytekit.clients.auth.token_client#flytekitclientsauthtoken_clienttimedelta) | Difference between two datetime values. |

### Errors

| Exception | Description |
|-|-|
| [`AuthenticationError`](.././flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientauthenticationerror) | This is raised for any AuthenticationError. |
| [`AuthenticationPending`](.././flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientauthenticationpending) | This is raised if the token endpoint returns authentication pending. |

### Methods

| Method | Description |
|-|-|
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`get_basic_authorization_header()`](#get_basic_authorization_header) | This function transforms the client id and the client secret into a header that conforms with http basic auth. |
| [`get_device_code()`](#get_device_code) | Retrieves the device Authentication code that can be done to authenticate the request using a browser on a. |
| [`get_token()`](#get_token) | retrieved from the IDP, the third is the expiration in seconds. |
| [`poll_token_endpoint()`](#poll_token_endpoint) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `error_auth_pending` | `str` |  |
| `error_slow_down` | `str` |  |
| `logger` | `Logger` |  |
| `utf_8` | `str` |  |

## Methods

#### dataclass()

```python
def dataclass(
    cls,
    init,
    repr,
    eq,
    order,
    unsafe_hash,
    frozen,
    match_args,
    kw_only,
    slots,
    weakref_slot,
)
```
Add dunder methods based on the fields defined in the class.

Examines PEP 526 __annotations__ to determine fields.

If init is true, an __init__() method is added to the class. If repr
is true, a __repr__() method is added. If order is true, rich
comparison dunder methods are added. If unsafe_hash is true, a
__hash__() method is added. If frozen is true, fields may not be
assigned to after instance creation. If match_args is true, the
__match_args__ tuple is added. If kw_only is true, then by default
all fields are keyword-only. If slots is true, a new class with a
__slots__ attribute is returned.


| Parameter | Type |
|-|-|
| `cls` |  |
| `init` |  |
| `repr` |  |
| `eq` |  |
| `order` |  |
| `unsafe_hash` |  |
| `frozen` |  |
| `match_args` |  |
| `kw_only` |  |
| `slots` |  |
| `weakref_slot` |  |

#### get_basic_authorization_header()

```python
def get_basic_authorization_header(
    client_id: str,
    client_secret: str,
) -> str
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
) -> (Text,Text,Int) The first element is the access token retrieved from the IDP, the second is the refresh token
```
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

## flytekit.clients.auth.token_client.AuthenticationError

This is raised for any AuthenticationError


## flytekit.clients.auth.token_client.AuthenticationPending

This is raised if the token endpoint returns authentication pending


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

## flytekit.clients.auth.token_client.GrantType

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.


```python
class GrantType(
    args,
    kwds,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwds` |  |

## flytekit.clients.auth.token_client.datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.


## flytekit.clients.auth.token_client.timedelta

Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.


