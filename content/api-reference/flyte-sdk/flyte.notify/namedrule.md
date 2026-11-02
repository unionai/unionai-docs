---
title: NamedRule
description: "Reference a pre-defined notification rule by name."
icon: braces
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# NamedRule

**Package:** `flyte.notify`

Reference a pre-defined notification rule by name.

Not yet supported: no backend resolves named rules, and there is no way to
create one yet. A run or trigger that references a named rule is rejected,
or sends no notification. Use an inline notification such as `Slack` or
`Email` instead.

Named rules will define both the phases to monitor and the delivery
channels to use.



## Parameters

```python
class NamedRule(
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the pre-defined rule (scoped to project/domain). |

