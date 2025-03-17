---
title: VersionParameters
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# VersionParameters

**Package:** `flytekit`

Parameters used for version hash generation.

param func: The function to generate a version for. This is an optional parameter and can be any callable
that matches the specified parameter and return types.
:type func: Optional[Callable[P, FuncOut]]


```python
def VersionParameters(
    func: typing.Callable[~P, ~FuncOut],
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType],
    pod_template: typing.Optional[flytekit.core.pod_template.PodTemplate],
    pod_template_name: typing.Optional[str],
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `func` | `typing.Callable[~P, ~FuncOut]` |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType]` |
| `pod_template` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |
| `pod_template_name` | `typing.Optional[str]` |
## Methods

