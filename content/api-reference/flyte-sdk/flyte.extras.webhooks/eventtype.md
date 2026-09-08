---
title: EventType
description: "Base for event constants: a real `str`, usable anywhere a pattern is."
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# EventType

**Package:** `flyte.extras.webhooks`

Base for event constants: a real `str`, usable anywhere a pattern is.

Subclass this in a provider plugin's `events` module, one class per event
type, with `ANY` as the bare type when the product splits type and action:

```python
class PullRequest(EventType):
    ANY = "pull_request"
    OPENED = "pull_request.opened"
```


## Parameters

```python
class EventType(
    *args,
    **kwds,
)
```
| Parameter | Type | Description |
|-|-|-|
| `*args` |  | |
| `**kwds` |  | |

