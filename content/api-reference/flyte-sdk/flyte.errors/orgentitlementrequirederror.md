---
title: OrgEntitlementRequiredError
description: "This error is raised when the server refuses a request because the organization isn't entitled to a capability, for example a private control plane endpoint."
icon: exclamation-triangle
version: 2.14.1
variants: +flyte +union
layout: py_api
---

# OrgEntitlementRequiredError

**Package:** `flyte.errors`

This error is raised when the server refuses a request because the organization isn't entitled to a capability,
for example a private control plane endpoint. Retrying does not help: the org's plan has to include it.



## Parameters

```python
class OrgEntitlementRequiredError(
    message: str,
    entitlement: str = '',
    values: list[str] | None = None,
    upgrade_url: str = '',
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `entitlement` | `str` | The entitlement's name, e.g. `private_control_plane_endpoint`. |
| `values` | `list[str] \| None` | For a list entitlement (e.g. `allowed_clouds`), the requested values the org isn't entitled to. |
| `upgrade_url` | `str` | Where to ask for the entitlement; empty when the server didn't say. |

