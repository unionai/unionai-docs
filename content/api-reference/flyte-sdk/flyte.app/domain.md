---
title: Domain
description: "Subdomain to use for the domain."
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# Domain

**Package:** `flyte.app`

Subdomain to use for the domain. Either a literal string, or a `Subdomain` resolved against the
deployment project and domain. If not set, the default subdomain will be used.


## Parameters

```python
class Domain(
    subdomain: typing.Union[str, flyte.app._types.Subdomain, NoneType] = None,
    custom_domain: typing.Optional[str] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `subdomain` | `typing.Union[str, flyte.app._types.Subdomain, NoneType]` | |
| `custom_domain` | `typing.Optional[str]` | |

