---
title: flytekit.clients.auth.token_client
version: 1.15.4.dev2+g3e3ce2426
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

* [`AuthenticationError`](.././flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientauthenticationerror)
* [`AuthenticationPending`](.././flytekit.clients.auth.token_client#flytekitclientsauthtoken_clientauthenticationpending)

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
def DeviceCodeResponse(
    device_code: str,
    user_code: str,
    verification_uri: str,
    expires_in: int,
    interval: int,
):
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
| [`from_json_response()`](#from_json_response) | None |


#### from_json_response()

```python
def from_json_response(
    j: typing.Dict,
):
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
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.


```python
def GrantType(
    args,
    kwds,
):
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


