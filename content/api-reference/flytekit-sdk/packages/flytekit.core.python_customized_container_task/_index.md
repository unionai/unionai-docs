---
title: flytekit.core.python_customized_container_task
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.python_customized_container_task

## Directory

### Classes

| Class | Description |
|-|-|
| [`PythonCustomizedContainerTask`](../flytekit.core.python_customized_container_task/pythoncustomizedcontainertask) | Please take a look at the comments for {{< py_class_ref flytekit.extend.ExecutableTemplateShimTask >}} as well. |
| [`TaskTemplateResolver`](../flytekit.core.python_customized_container_task/tasktemplateresolver) | This is a special resolver that resolves the task above at execution time, using only the ``TaskTemplate``,. |

### Variables

| Property | Type | Description |
|-|-|-|
| `TC` | `TypeVar` |  |
| `default_task_template_resolver` | `TaskTemplateResolver` |  |

