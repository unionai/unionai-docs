---
title: VersionParameters
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# VersionParameters

**Package:** `flytekit.core.cache`

Parameters used for version hash generation.

param func: The function to generate a version for. This is an optional parameter and can be any callable
             that matches the specified parameter and return types.
:type func: Optional[Callable[P, FuncOut]]


```python
class VersionParameters(
    func: typing.Callable[~P, ~FuncOut],
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType],
    pod_template: typing.Optional[flytekit.core.pod_template.PodTemplate],
    pod_template_name: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Callable[~P, ~FuncOut]` | |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType]` | |
| `pod_template` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` | |
| `pod_template_name` | `typing.Optional[str]` | |

