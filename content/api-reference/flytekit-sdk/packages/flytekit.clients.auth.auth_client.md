---
title: flytekit.clients.auth.auth_client
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.auth.auth_client

## Directory

### Classes

| Class | Description |
|-|-|
| [`AuthorizationClient`](.././flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientauthorizationclient) | Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the. |
| [`AuthorizationCode`](.././flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientauthorizationcode) |  |
| [`EndpointMetadata`](.././flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientendpointmetadata) | This class can be used to control the rendering of the page on login successful or failure. |
| [`OAuthCallbackHandler`](.././flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientoauthcallbackhandler) | A simple wrapper around BaseHTTPServer. |
| [`OAuthHTTPServer`](.././flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientoauthhttpserver) | A simple wrapper around the BaseHTTPServer. |

## flytekit.clients.auth.auth_client.AuthorizationClient

Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the
credentials. NOTE: This will open an web browser to retrieve the credentials.


```python
class AuthorizationClient(
    endpoint: str,
    auth_endpoint: str,
    token_endpoint: str,
    audience: typing.Optional[str],
    scopes: typing.Optional[typing.List[str]],
    client_id: typing.Optional[str],
    redirect_uri: typing.Optional[str],
    endpoint_metadata: typing.Optional[EndpointMetadata],
    verify: typing.Optional[typing.Union[bool, str]],
    session: typing.Optional[requests.Session],
    request_auth_code_params: typing.Optional[typing.Dict[str, str]],
    request_access_token_params: typing.Optional[typing.Dict[str, str]],
    refresh_access_token_params: typing.Optional[typing.Dict[str, str]],
    add_request_auth_code_params_to_request_access_token_params: typing.Optional[bool],
)
```
Create new AuthorizationClient



| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `auth_endpoint` | `str` |
| `token_endpoint` | `str` |
| `audience` | `typing.Optional[str]` |
| `scopes` | `typing.Optional[typing.List[str]]` |
| `client_id` | `typing.Optional[str]` |
| `redirect_uri` | `typing.Optional[str]` |
| `endpoint_metadata` | `typing.Optional[EndpointMetadata]` |
| `verify` | `typing.Optional[typing.Union[bool, str]]` |
| `session` | `typing.Optional[requests.Session]` |
| `request_auth_code_params` | `typing.Optional[typing.Dict[str, str]]` |
| `request_access_token_params` | `typing.Optional[typing.Dict[str, str]]` |
| `refresh_access_token_params` | `typing.Optional[typing.Dict[str, str]]` |
| `add_request_auth_code_params_to_request_access_token_params` | `typing.Optional[bool]` |

### Methods

| Method | Description |
|-|-|
| [`get_creds_from_remote()`](#get_creds_from_remote) | This is the entrypoint method. |
| [`refresh_access_token()`](#refresh_access_token) |  |


#### get_creds_from_remote()

```python
def get_creds_from_remote()
```
This is the entrypoint method. It will kickoff the full authentication
flow and trigger a web-browser to retrieve credentials. Because this
needs to open a port on localhost and may be called from a
multithreaded context (e.g. pyflyte register), this call may block
multiple threads and return a cached result for up to 60 seconds.


#### refresh_access_token()

```python
def refresh_access_token(
    credentials: Credentials,
) -> Credentials
```
| Parameter | Type |
|-|-|
| `credentials` | `Credentials` |

## flytekit.clients.auth.auth_client.AuthorizationCode

```python
class AuthorizationCode(
    code,
    state,
)
```
| Parameter | Type |
|-|-|
| `code` |  |
| `state` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `code` |  |  |
| `state` |  |  |

## flytekit.clients.auth.auth_client.EndpointMetadata

This class can be used to control the rendering of the page on login successful or failure


```python
class EndpointMetadata(
    endpoint: str,
    success_html: typing.Optional[bytes],
    failure_html: typing.Optional[bytes],
)
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `success_html` | `typing.Optional[bytes]` |
| `failure_html` | `typing.Optional[bytes]` |

## flytekit.clients.auth.auth_client.OAuthCallbackHandler

A simple wrapper around BaseHTTPServer.BaseHTTPRequestHandler that handles a callback URL that accepts an
authorization token.


```python
class OAuthCallbackHandler(
    request,
    client_address,
    server,
)
```
| Parameter | Type |
|-|-|
| `request` |  |
| `client_address` |  |
| `server` |  |

### Methods

| Method | Description |
|-|-|
| [`address_string()`](#address_string) | Return the client address. |
| [`date_time_string()`](#date_time_string) | Return the current date and time formatted for a message header. |
| [`do_GET()`](#do_get) |  |
| [`end_headers()`](#end_headers) | Send the blank line ending the MIME headers. |
| [`finish()`](#finish) |  |
| [`flush_headers()`](#flush_headers) |  |
| [`handle()`](#handle) | Handle multiple requests if necessary. |
| [`handle_expect_100()`](#handle_expect_100) | Decide what to do with an "Expect: 100-continue" header. |
| [`handle_login()`](#handle_login) |  |
| [`handle_one_request()`](#handle_one_request) | Handle a single HTTP request. |
| [`log_date_time_string()`](#log_date_time_string) | Return the current time formatted for logging. |
| [`log_error()`](#log_error) | Log an error. |
| [`log_message()`](#log_message) | Log an arbitrary message. |
| [`log_request()`](#log_request) | Log an accepted request. |
| [`parse_request()`](#parse_request) | Parse a request (internal). |
| [`send_error()`](#send_error) | Send and log an error reply. |
| [`send_header()`](#send_header) | Send a MIME header to the headers buffer. |
| [`send_response()`](#send_response) | Add the response header to the headers buffer and log the. |
| [`send_response_only()`](#send_response_only) | Send the response header only. |
| [`setup()`](#setup) |  |
| [`version_string()`](#version_string) | Return the server software version string. |


#### address_string()

```python
def address_string()
```
Return the client address.


#### date_time_string()

```python
def date_time_string(
    timestamp,
)
```
Return the current date and time formatted for a message header.


| Parameter | Type |
|-|-|
| `timestamp` |  |

#### do_GET()

```python
def do_GET()
```
#### end_headers()

```python
def end_headers()
```
Send the blank line ending the MIME headers.


#### finish()

```python
def finish()
```
#### flush_headers()

```python
def flush_headers()
```
#### handle()

```python
def handle()
```
Handle multiple requests if necessary.


#### handle_expect_100()

```python
def handle_expect_100()
```
Decide what to do with an "Expect: 100-continue" header.

If the client is expecting a 100 Continue response, we must
respond with either a 100 Continue or a final response before
waiting for the request body. The default is to always respond
with a 100 Continue. You can behave differently (for example,
reject unauthorized requests) by overriding this method.

This method should either return True (possibly after sending
a 100 Continue response) or send an error response and return
False.


#### handle_login()

```python
def handle_login(
    data: dict,
)
```
| Parameter | Type |
|-|-|
| `data` | `dict` |

#### handle_one_request()

```python
def handle_one_request()
```
Handle a single HTTP request.

You normally don't need to override this method; see the class
__doc__ string for information on how to handle specific HTTP
commands such as GET and POST.


#### log_date_time_string()

```python
def log_date_time_string()
```
Return the current time formatted for logging.


#### log_error()

```python
def log_error(
    format,
    args,
)
```
Log an error.

This is called when a request cannot be fulfilled.  By
default it passes the message on to log_message().

Arguments are the same as for log_message().

XXX This should go to the separate error log.


| Parameter | Type |
|-|-|
| `format` |  |
| `args` | ``*args`` |

#### log_message()

```python
def log_message(
    format,
    args,
)
```
Log an arbitrary message.

This is used by all other logging functions.  Override
it if you have specific logging wishes.

The first argument, FORMAT, is a format string for the
message to be logged.  If the format string contains
any % escapes requiring parameters, they should be
specified as subsequent arguments (it's just like
printf!).

The client ip and current date/time are prefixed to
every message.

Unicode control characters are replaced with escaped hex
before writing the output to stderr.


| Parameter | Type |
|-|-|
| `format` |  |
| `args` | ``*args`` |

#### log_request()

```python
def log_request(
    code,
    size,
)
```
Log an accepted request.

This is called by send_response().


| Parameter | Type |
|-|-|
| `code` |  |
| `size` |  |

#### parse_request()

```python
def parse_request()
```
Parse a request (internal).

The request should be stored in self.raw_requestline; the results
are in self.command, self.path, self.request_version and
self.headers.

Return True for success, False for failure; on failure, any relevant
error response has already been sent back.


#### send_error()

```python
def send_error(
    code,
    message,
    explain,
)
```
Send and log an error reply.

Arguments are
* code:    an HTTP error code
           3 digits
* message: a simple optional 1 line reason phrase.
           *( HTAB / SP / VCHAR / %x80-FF )
           defaults to short entry matching the response code
* explain: a detailed message defaults to the long entry
           matching the response code.

This sends an error response (so it must be called before any
output has been generated), logs the error, and finally sends
a piece of HTML explaining the error to the user.


| Parameter | Type |
|-|-|
| `code` |  |
| `message` |  |
| `explain` |  |

#### send_header()

```python
def send_header(
    keyword,
    value,
)
```
Send a MIME header to the headers buffer.


| Parameter | Type |
|-|-|
| `keyword` |  |
| `value` |  |

#### send_response()

```python
def send_response(
    code,
    message,
)
```
Add the response header to the headers buffer and log the
response code.

Also send two standard headers with the server software
version and the current date.


| Parameter | Type |
|-|-|
| `code` |  |
| `message` |  |

#### send_response_only()

```python
def send_response_only(
    code,
    message,
)
```
Send the response header only.


| Parameter | Type |
|-|-|
| `code` |  |
| `message` |  |

#### setup()

```python
def setup()
```
#### version_string()

```python
def version_string()
```
Return the server software version string.


## flytekit.clients.auth.auth_client.OAuthHTTPServer

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


| Parameter | Type |
|-|-|
| `server_address` | `typing.Tuple[str, int]` |
| `remote_metadata` | `EndpointMetadata` |
| `request_handler_class` | `typing.Type[_BaseHTTPServer.BaseHTTPRequestHandler]` |
| `bind_and_activate` | `bool` |
| `redirect_path` | `str` |
| `queue` | `Queue` |

### Methods

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


#### close_request()

```python
def close_request(
    request,
)
```
Called to clean up an individual request.


| Parameter | Type |
|-|-|
| `request` |  |

#### fileno()

```python
def fileno()
```
Return socket file number.

Interface required by selector.


#### finish_request()

```python
def finish_request(
    request,
    client_address,
)
```
Finish one request by instantiating RequestHandlerClass.


| Parameter | Type |
|-|-|
| `request` |  |
| `client_address` |  |

#### get_request()

```python
def get_request()
```
Get the request and client address from the socket.

May be overridden.


#### handle_authorization_code()

```python
def handle_authorization_code(
    auth_code: str,
)
```
| Parameter | Type |
|-|-|
| `auth_code` | `str` |

#### handle_error()

```python
def handle_error(
    request,
    client_address,
)
```
Handle an error gracefully.  May be overridden.

The default is to print a traceback and continue.


| Parameter | Type |
|-|-|
| `request` |  |
| `client_address` |  |

#### handle_request()

```python
def handle_request(
    queue: Queue,
) -> typing.Any
```
Handle one request, possibly blocking.

Respects self.timeout.


| Parameter | Type |
|-|-|
| `queue` | `Queue` |

#### handle_timeout()

```python
def handle_timeout()
```
Called if no new request arrives within self.timeout.

Overridden by ForkingMixIn.


#### process_request()

```python
def process_request(
    request,
    client_address,
)
```
Call finish_request.

Overridden by ForkingMixIn and ThreadingMixIn.


| Parameter | Type |
|-|-|
| `request` |  |
| `client_address` |  |

#### serve_forever()

```python
def serve_forever(
    poll_interval,
)
```
Handle one request at a time until shutdown.

Polls for shutdown every poll_interval seconds. Ignores
self.timeout. If you need to do periodic tasks, do them in
another thread.


| Parameter | Type |
|-|-|
| `poll_interval` |  |

#### server_activate()

```python
def server_activate()
```
Called by constructor to activate the server.

May be overridden.


#### server_bind()

```python
def server_bind()
```
Override server_bind to store the server name.


#### server_close()

```python
def server_close()
```
Called to clean-up the server.

May be overridden.


#### service_actions()

```python
def service_actions()
```
Called by the serve_forever() loop.

May be overridden by a subclass / Mixin to implement any code that
needs to be run during the loop.


#### shutdown()

```python
def shutdown()
```
Stops the serve_forever loop.

Blocks until the loop has finished. This must be called while
serve_forever() is running in another thread, or it will
deadlock.


#### shutdown_request()

```python
def shutdown_request(
    request,
)
```
Called to shutdown and close an individual request.


| Parameter | Type |
|-|-|
| `request` |  |

#### verify_request()

```python
def verify_request(
    request,
    client_address,
)
```
Verify the request.  May be overridden.

Return True if we should proceed with this request.


| Parameter | Type |
|-|-|
| `request` |  |
| `client_address` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `redirect_path` |  |  |
| `remote_metadata` |  |  |

