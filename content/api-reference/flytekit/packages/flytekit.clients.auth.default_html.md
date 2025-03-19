---
title: flytekit.clients.auth.default_html
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clients.auth.default_html

## Directory

### Classes

| Class | Description |
|-|-|
| [`suppress`](.././flytekit.clients.auth.default_html#flytekitclientsauthdefault_htmlsuppress) | Context manager to suppress specified exceptions. |

## flytekit.clients.auth.default_html.suppress

Context manager to suppress specified exceptions

After the exception is suppressed, execution proceeds with the next
statement following the with statement.

with suppress(FileNotFoundError):
os.remove(somefile)
# Execution still resumes here if the file was already removed


```python
def suppress(
    exceptions,
):
```
| Parameter | Type |
|-|-|
| `exceptions` |  |

