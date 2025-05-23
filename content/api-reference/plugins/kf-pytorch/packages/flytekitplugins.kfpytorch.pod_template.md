---
title: flytekitplugins.kfpytorch.pod_template
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.kfpytorch.pod_template

## Directory

### Methods

| Method | Description |
|-|-|
| [`add_shared_mem_volume_to_pod_template()`](#add_shared_mem_volume_to_pod_template) | Add shared memory volume and volume mount to the pod template. |


## Methods

#### add_shared_mem_volume_to_pod_template()

```python
def add_shared_mem_volume_to_pod_template(
    pod_template: flytekit.core.pod_template.PodTemplate,
)
```
Add shared memory volume and volume mount to the pod template.


| Parameter | Type |
|-|-|
| `pod_template` | `flytekit.core.pod_template.PodTemplate` |

