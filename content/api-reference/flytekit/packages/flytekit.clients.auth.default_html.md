---
title: flytekit.clients.auth.default_html
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clients.auth.default_html

## Directory

### Classes

| Class | Description |
|-|-|
| [`suppress`](.././flytekit.clients.auth.default_html#flytekitclientsauthdefault_htmlsuppress) | Context manager to suppress specified exceptions. |

### Methods

| Method | Description |
|-|-|
| [`get_default_success_html()`](#get_default_success_html) |  |


## Methods

#### get_default_success_html()

```python
def get_default_success_html(
    endpoint: str,
) -> str
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |

## flytekit.clients.auth.default_html.suppress

Context manager to suppress specified exceptions

After the exception is suppressed, execution proceeds with the next
statement following the with statement.

with suppress(FileNotFoundError):
os.remove(somefile)
# Execution still resumes here if the file was already removed


```python
class suppress(
    exceptions,
)
```
| Parameter | Type |
|-|-|
| `exceptions` |  |

