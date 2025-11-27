---
title: flytekit.core.launch_plan
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.launch_plan

## Directory

### Classes

| Class | Description |
|-|-|
| [`LaunchPlan`](../flytekit.core.launch_plan/launchplan) | Launch Plans are one of the core constructs of Flyte. |
| [`ReferenceLaunchPlan`](../flytekit.core.launch_plan/referencelaunchplan) | A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |

### Methods

| Method | Description |
|-|-|
| [`reference_launch_plan()`](#reference_launch_plan) | A reference launch plan is a pointer to a launch plan that already exists on your Flyte installation. |


## Methods

#### reference_launch_plan()

```python
def reference_launch_plan(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> Callable[[Callable[..., Any]], ReferenceLaunchPlan]
```
A reference launch plan is a pointer to a launch plan that already exists on your Flyte installation. This
object will not initiate a network call to Admin, which is why the user is asked to provide the expected interface
via the function definition.

If at registration time the interface provided causes an issue with compilation, an error will be returned.



| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | Flyte project name of the launch plan |
| `domain` | `str` | Flyte domain name of the launch plan |
| `name` | `str` | launch plan name |
| `version` | `str` | specific version of the launch plan to use |

