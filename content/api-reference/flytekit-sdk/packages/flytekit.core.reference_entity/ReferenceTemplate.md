---
title: ReferenceTemplate
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ReferenceTemplate

**Package:** `flytekit.core.reference_entity`

```python
class ReferenceTemplate(
    id: flytekit.models.core.identifier.Identifier,
    resource_type: int,
)
```
A reference template encapsulates all the information necessary to use reference entities within other
workflows or dynamic tasks.



| Parameter | Type | Description |
|-|-|-|
| `id` | `flytekit.models.core.identifier.Identifier` | |
| `resource_type` | `int` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `id` |  | {{< multiline >}}User-specified information that uniquely identifies this reference.
:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `resource_type` |  | {{< multiline >}}The type of reference.
:rtype: flytekit.models.core.identifier.ResourceType
{{< /multiline >}} |

