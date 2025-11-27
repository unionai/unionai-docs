---
title: FlyteScopedUserException
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteScopedUserException

**Package:** `flytekit.exceptions.scopes`

Common base class for all non-exit exceptions.


```python
class FlyteScopedUserException(
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

