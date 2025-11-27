---
title: RunLevelComputedParams
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RunLevelComputedParams

**Package:** `flytekit.clis.sdk_in_container.run`

This class is used to store the computed parameters that are used to run a workflow / task / launchplan.
Computed parameters are created during the execution


```python
class RunLevelComputedParams(
    project_root: typing.Optional[str],
    module: typing.Optional[str],
    temp_file_name: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `project_root` | `typing.Optional[str]` | |
| `module` | `typing.Optional[str]` | |
| `temp_file_name` | `typing.Optional[str]` | |

