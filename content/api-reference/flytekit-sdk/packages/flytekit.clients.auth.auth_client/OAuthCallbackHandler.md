---
title: OAuthCallbackHandler
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OAuthCallbackHandler

**Package:** `flytekit.clients.auth.auth_client`

A simple wrapper around BaseHTTPServer.BaseHTTPRequestHandler that handles a callback URL that accepts an
authorization token.


```python
class OAuthCallbackHandler(
    request,
    client_address,
    server,
)
```
| Parameter | Type | Description |
|-|-|-|
| `request` |  | |
| `client_address` |  | |
| `server` |  | |

## Methods

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


### address_string()

```python
def address_string()
```
Return the client address.


### date_time_string()

```python
def date_time_string(
    timestamp,
)
```
Return the current date and time formatted for a message header.


| Parameter | Type | Description |
|-|-|-|
| `timestamp` |  | |

### do_GET()

```python
def do_GET()
```
### end_headers()

```python
def end_headers()
```
Send the blank line ending the MIME headers.


### finish()

```python
def finish()
```
### flush_headers()

```python
def flush_headers()
```
### handle()

```python
def handle()
```
Handle multiple requests if necessary.


### handle_expect_100()

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


### handle_login()

```python
def handle_login(
    data: dict,
)
```
| Parameter | Type | Description |
|-|-|-|
| `data` | `dict` | |

### handle_one_request()

```python
def handle_one_request()
```
Handle a single HTTP request.

You normally don't need to override this method; see the class
__doc__ string for information on how to handle specific HTTP
commands such as GET and POST.


### log_date_time_string()

```python
def log_date_time_string()
```
Return the current time formatted for logging.


### log_error()

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


| Parameter | Type | Description |
|-|-|-|
| `format` |  | |
| `args` | `*args` | |

### log_message()

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


| Parameter | Type | Description |
|-|-|-|
| `format` |  | |
| `args` | `*args` | |

### log_request()

```python
def log_request(
    code,
    size,
)
```
Log an accepted request.

This is called by send_response().


| Parameter | Type | Description |
|-|-|-|
| `code` |  | |
| `size` |  | |

### parse_request()

```python
def parse_request()
```
Parse a request (internal).

The request should be stored in self.raw_requestline; the results
are in self.command, self.path, self.request_version and
self.headers.

Return True for success, False for failure; on failure, any relevant
error response has already been sent back.


### send_error()

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


| Parameter | Type | Description |
|-|-|-|
| `code` |  | |
| `message` |  | |
| `explain` |  | |

### send_header()

```python
def send_header(
    keyword,
    value,
)
```
Send a MIME header to the headers buffer.


| Parameter | Type | Description |
|-|-|-|
| `keyword` |  | |
| `value` |  | |

### send_response()

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


| Parameter | Type | Description |
|-|-|-|
| `code` |  | |
| `message` |  | |

### send_response_only()

```python
def send_response_only(
    code,
    message,
)
```
Send the response header only.


| Parameter | Type | Description |
|-|-|-|
| `code` |  | |
| `message` |  | |

### setup()

```python
def setup()
```
### version_string()

```python
def version_string()
```
Return the server software version string.


