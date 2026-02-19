---
title: OAuthHTTPServer
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OAuthHTTPServer

**Package:** `flytekit.clients.auth.auth_client`

A simple wrapper around the BaseHTTPServer.HTTPServer implementation that binds an authorization_client for handling
authorization code callbacks.



```python
class OAuthHTTPServer(
    server_address: typing.Tuple[str, int],
    remote_metadata: EndpointMetadata,
    request_handler_class: typing.Type[_BaseHTTPServer.BaseHTTPRequestHandler],
    bind_and_activate: bool,
    redirect_path: str,
    queue: Queue,
)
```
Constructor.  May be extended, do not override.


| Parameter | Type | Description |
|-|-|-|
| `server_address` | `typing.Tuple[str, int]` | |
| `remote_metadata` | `EndpointMetadata` | |
| `request_handler_class` | `typing.Type[_BaseHTTPServer.BaseHTTPRequestHandler]` | |
| `bind_and_activate` | `bool` | |
| `redirect_path` | `str` | |
| `queue` | `Queue` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `redirect_path` | `None` |  |
| `remote_metadata` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`close_request()`](#close_request) | Called to clean up an individual request. |
| [`fileno()`](#fileno) | Return socket file number. |
| [`finish_request()`](#finish_request) | Finish one request by instantiating RequestHandlerClass. |
| [`get_request()`](#get_request) | Get the request and client address from the socket. |
| [`handle_authorization_code()`](#handle_authorization_code) |  |
| [`handle_error()`](#handle_error) | Handle an error gracefully. |
| [`handle_request()`](#handle_request) | Handle one request, possibly blocking. |
| [`handle_timeout()`](#handle_timeout) | Called if no new request arrives within self. |
| [`process_request()`](#process_request) | Call finish_request. |
| [`serve_forever()`](#serve_forever) | Handle one request at a time until shutdown. |
| [`server_activate()`](#server_activate) | Called by constructor to activate the server. |
| [`server_bind()`](#server_bind) | Override server_bind to store the server name. |
| [`server_close()`](#server_close) | Called to clean-up the server. |
| [`service_actions()`](#service_actions) | Called by the serve_forever() loop. |
| [`shutdown()`](#shutdown) | Stops the serve_forever loop. |
| [`shutdown_request()`](#shutdown_request) | Called to shutdown and close an individual request. |
| [`verify_request()`](#verify_request) | Verify the request. |


### close_request()

```python
def close_request(
    request,
)
```
Called to clean up an individual request.


| Parameter | Type | Description |
|-|-|-|
| `request` |  | |

### fileno()

```python
def fileno()
```
Return socket file number.

Interface required by selector.


### finish_request()

```python
def finish_request(
    request,
    client_address,
)
```
Finish one request by instantiating RequestHandlerClass.


| Parameter | Type | Description |
|-|-|-|
| `request` |  | |
| `client_address` |  | |

### get_request()

```python
def get_request()
```
Get the request and client address from the socket.

May be overridden.


### handle_authorization_code()

```python
def handle_authorization_code(
    auth_code: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `auth_code` | `str` | |

### handle_error()

```python
def handle_error(
    request,
    client_address,
)
```
Handle an error gracefully.  May be overridden.

The default is to print a traceback and continue.


| Parameter | Type | Description |
|-|-|-|
| `request` |  | |
| `client_address` |  | |

### handle_request()

```python
def handle_request(
    queue: Queue,
) -> typing.Any
```
Handle one request, possibly blocking.

Respects self.timeout.


| Parameter | Type | Description |
|-|-|-|
| `queue` | `Queue` | |

### handle_timeout()

```python
def handle_timeout()
```
Called if no new request arrives within self.timeout.

Overridden by ForkingMixIn.


### process_request()

```python
def process_request(
    request,
    client_address,
)
```
Call finish_request.

Overridden by ForkingMixIn and ThreadingMixIn.


| Parameter | Type | Description |
|-|-|-|
| `request` |  | |
| `client_address` |  | |

### serve_forever()

```python
def serve_forever(
    poll_interval,
)
```
Handle one request at a time until shutdown.

Polls for shutdown every poll_interval seconds. Ignores
self.timeout. If you need to do periodic tasks, do them in
another thread.


| Parameter | Type | Description |
|-|-|-|
| `poll_interval` |  | |

### server_activate()

```python
def server_activate()
```
Called by constructor to activate the server.

May be overridden.


### server_bind()

```python
def server_bind()
```
Override server_bind to store the server name.


### server_close()

```python
def server_close()
```
Called to clean-up the server.

May be overridden.


### service_actions()

```python
def service_actions()
```
Called by the serve_forever() loop.

May be overridden by a subclass / Mixin to implement any code that
needs to be run during the loop.


### shutdown()

```python
def shutdown()
```
Stops the serve_forever loop.

Blocks until the loop has finished. This must be called while
serve_forever() is running in another thread, or it will
deadlock.


### shutdown_request()

```python
def shutdown_request(
    request,
)
```
Called to shutdown and close an individual request.


| Parameter | Type | Description |
|-|-|-|
| `request` |  | |

### verify_request()

```python
def verify_request(
    request,
    client_address,
)
```
Verify the request.  May be overridden.

Return True if we should proceed with this request.


| Parameter | Type | Description |
|-|-|-|
| `request` |  | |
| `client_address` |  | |

