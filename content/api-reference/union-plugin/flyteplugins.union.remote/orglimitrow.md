---
title: OrgLimitRow
description: "One limit or entitlement of an org: what it runs with, the tier default, and why they differ."
icon: braces
version: 0.26.0
variants: -flyte +union
layout: py_api
---

# OrgLimitRow

**Package:** `flyteplugins.union.remote`

One limit or entitlement of an org: what it runs with, the tier default, and why they differ.

``value`` and ``tier_default`` are the raw proto values: an int for a limit (0 means
unlimited), a bool for an entitlement, a list of strings for ``allowed_clouds``.
``tier_default`` is None when the org's plan has no tier defaults. ``status`` is
``"default"``, ``"lifted"`` (a per-org override above the tier default) or
``"enterprise"`` (gated to the Enterprise tier), or None when the server did not say.


## Parameters

```python
class OrgLimitRow(
    name: str,
    value: Any,
    tier_default: Any,
    status: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `value` | `Any` | |
| `tier_default` | `Any` | |
| `status` | `str \| None` | |

