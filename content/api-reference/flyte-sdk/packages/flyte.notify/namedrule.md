---
title: NamedRule
version: 2.0.11
variants: +flyte +union
layout: py_api
---

# NamedRule

**Package:** `flyte.notify`

Reference a pre-defined notification rule by name.

Use this when your Flyte admin has configured a named notification rule
that you want to apply to your runs. Named rules define both the phases
to monitor and the delivery channels to use.



## Parameters

```python
class NamedRule(
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the pre-defined rule (scoped to project/domain). |

