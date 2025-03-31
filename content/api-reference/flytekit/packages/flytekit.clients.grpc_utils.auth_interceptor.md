---
title: flytekit.clients.grpc_utils.auth_interceptor
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clients.grpc_utils.auth_interceptor

## Directory

### Classes

| Class | Description |
|-|-|
| [`AuthUnaryInterceptor`](.././flytekit.clients.grpc_utils.auth_interceptor#flytekitclientsgrpc_utilsauth_interceptorauthunaryinterceptor) | This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication. |
| [`Authenticator`](.././flytekit.clients.grpc_utils.auth_interceptor#flytekitclientsgrpc_utilsauth_interceptorauthenticator) | Base authenticator for all authentication flows. |

### Methods

| Method | Description |
|-|-|
| [`namedtuple()`](#namedtuple) | Returns a new subclass of tuple with named fields. |


## Methods

#### namedtuple()

```python
def namedtuple(
    typename,
    field_names,
    rename,
    defaults,
    module,
)
```
Returns a new subclass of tuple with named fields.

>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point.__doc__                   # docstring for the new class
'Point(x, y)'
>>> p = Point(11, y=22)             # instantiate with positional args or keywords
>>> p[0] + p[1]                     # indexable like a plain tuple
33
>>> x, y = p                        # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y                       # fields also accessible by name
33
>>> d = p._asdict()                 # convert to a dictionary
>>> d['x']
11
>>> Point(**d)                      # convert from a dictionary
Point(x=11, y=22)
>>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
Point(x=100, y=22)


| Parameter | Type |
|-|-|
| `typename` |  |
| `field_names` |  |
| `rename` |  |
| `defaults` |  |
| `module` |  |

## flytekit.clients.grpc_utils.auth_interceptor.AuthUnaryInterceptor

This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication
is needed.


```python
class AuthUnaryInterceptor(
    get_authenticator: typing.Callable[[], flytekit.clients.auth.authenticator.Authenticator],
)
```
| Parameter | Type |
|-|-|
| `get_authenticator` | `typing.Callable[[], flytekit.clients.auth.authenticator.Authenticator]` |

### Methods

| Method | Description |
|-|-|
| [`intercept_unary_stream()`](#intercept_unary_stream) | Handles a stream call and adds authentication metadata if needed. |
| [`intercept_unary_unary()`](#intercept_unary_unary) | Intercepts unary calls and adds auth metadata if available. |


#### intercept_unary_stream()

```python
def intercept_unary_stream(
    continuation,
    client_call_details,
    request,
)
```
Handles a stream call and adds authentication metadata if needed


| Parameter | Type |
|-|-|
| `continuation` |  |
| `client_call_details` |  |
| `request` |  |

#### intercept_unary_unary()

```python
def intercept_unary_unary(
    continuation: typing.Callable,
    client_call_details: grpc.ClientCallDetails,
    request: typing.Any,
)
```
Intercepts unary calls and adds auth metadata if available. On Unauthenticated, resets the token and refreshes
and then retries with the new token


| Parameter | Type |
|-|-|
| `continuation` | `typing.Callable` |
| `client_call_details` | `grpc.ClientCallDetails` |
| `request` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `authenticator` |  |  |

## flytekit.clients.grpc_utils.auth_interceptor.Authenticator

Base authenticator for all authentication flows


```python
class Authenticator(
    endpoint: str,
    header_key: str,
    credentials: flytekit.clients.auth.keyring.Credentials,
    http_proxy_url: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
)
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `header_key` | `str` |
| `credentials` | `flytekit.clients.auth.keyring.Credentials` |
| `http_proxy_url` | `typing.Optional[str]` |
| `verify` | `typing.Union[bool, str, NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) |  |
| [`get_credentials()`](#get_credentials) |  |
| [`refresh_credentials()`](#refresh_credentials) |  |


#### fetch_grpc_call_auth_metadata()

```python
def fetch_grpc_call_auth_metadata()
```
#### get_credentials()

```python
def get_credentials()
```
#### refresh_credentials()

```python
def refresh_credentials()
```
