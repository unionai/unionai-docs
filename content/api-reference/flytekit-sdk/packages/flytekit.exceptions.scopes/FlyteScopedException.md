---
title: FlyteScopedException
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteScopedException

**Package:** `flytekit.exceptions.scopes`

Common base class for all non-exit exceptions.


```python
class FlyteScopedException(
    context,
    exc_type,
    exc_value,
    exc_tb,
    top_trim,
    bottom_trim,
    kind,
)
```
| Parameter | Type | Description |
|-|-|-|
| `context` |  | |
| `exc_type` |  | |
| `exc_value` |  | |
| `exc_tb` |  | |
| `top_trim` |  | |
| `bottom_trim` |  | |
| `kind` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `error_code` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `kind` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `traceback` |  |  |
| `type` |  |  |
| `value` |  |  |
| `verbose_message` |  |  |

