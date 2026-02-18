---
title: FastAPIPassthroughAuthMiddleware
version: 2.0.0b59
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FastAPIPassthroughAuthMiddleware

**Package:** `flyte.app.extras`

FastAPI middleware that automatically sets Flyte auth metadata from request headers.

This middleware extracts authentication headers from incoming HTTP requests and
sets them in the Flyte context using the auth_metadata() context manager. This
eliminates the need to manually wrap endpoint handlers with auth_metadata().

The middleware is highly configurable:
- Custom header extractors can be provided
- Specific paths can be excluded from auth requirements
- Auth can be optional or required

Attributes:
    app: The FastAPI application (this is a mandatory framework parameter)
    header_extractors: List of functions to extract headers from requests
    excluded_paths: Set of URL paths that bypass auth extraction

Thread Safety:
    This middleware is async-safe and properly isolates auth metadata per request
    using Python's contextvars. Multiple concurrent requests with different
    authentication will not interfere with each other.



```python
class FastAPIPassthroughAuthMiddleware(
    app,
    header_extractors: list[HeaderExtractor] | None,
    excluded_paths: set[str] | None,
)
```
Initialize the Flyte authentication middleware.



| Parameter | Type | Description |
|-|-|-|
| `app` |  | The FastAPI/Starlette application |
| `header_extractors` | `list[HeaderExtractor] \| None` | List of functions to extract headers. Each function takes a Request and returns (key, value) tuple or None. Defaults to [extract_authorization_header, extract_cookie_header]. |
| `excluded_paths` | `set[str] \| None` | Set of URL paths to exclude from auth extraction. Requests to these paths proceed without setting auth context. |

## Methods

| Method | Description |
|-|-|
| [`dispatch()`](#dispatch) | Process each request, extracting auth headers and setting Flyte context. |
| [`extract_authorization_header()`](#extract_authorization_header) | Extract the Authorization header from the request. |
| [`extract_cookie_header()`](#extract_cookie_header) | Extract the Cookie header from the request. |
| [`extract_custom_header()`](#extract_custom_header) | Create a header extractor for a custom header name. |


### dispatch()

```python
def dispatch(
    request: 'Request',
    call_next,
) -> 'Response'
```
Process each request, extracting auth headers and setting Flyte context.



| Parameter | Type | Description |
|-|-|-|
| `request` | `'Request'` | The incoming HTTP request |
| `call_next` |  | The next middleware or route handler to call |

### extract_authorization_header()

```python
def extract_authorization_header(
    request: 'Request',
) -> tuple[str, str] | None
```
Extract the Authorization header from the request.



| Parameter | Type | Description |
|-|-|-|
| `request` | `'Request'` | The FastAPI/Starlette request object |

### extract_cookie_header()

```python
def extract_cookie_header(
    request: 'Request',
) -> tuple[str, str] | None
```
Extract the Cookie header from the request.



| Parameter | Type | Description |
|-|-|-|
| `request` | `'Request'` | The FastAPI/Starlette request object |

### extract_custom_header()

```python
def extract_custom_header(
    header_name: str,
) -> HeaderExtractor
```
Create a header extractor for a custom header name.



| Parameter | Type | Description |
|-|-|-|
| `header_name` | `str` | The name of the header to extract (case-insensitive) |

