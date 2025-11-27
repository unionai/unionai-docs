---
title: FlyteScopedSystemException
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteScopedSystemException

**Package:** `flytekit.exceptions.scopes`

Common base class for all non-exit exceptions.


```python
class FlyteScopedSystemException(
    exc_type,
    exc_value,
    exc_tb,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `exc_type` |  | |
| `exc_value` |  | |
| `exc_tb` |  | |
| `kwargs` | `**kwargs` | |

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
| `verbose_message` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

