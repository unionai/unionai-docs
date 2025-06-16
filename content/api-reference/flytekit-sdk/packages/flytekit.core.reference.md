---
title: flytekit.core.reference
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.reference

## Directory

### Methods

| Method | Description |
|-|-|
| [`get_reference_entity()`](#get_reference_entity) | See the documentation for {{< py_class_ref flytekit.reference_task >}} and {{< py_class_ref flytekit.reference_workflow >}} as well. |


## Methods

#### get_reference_entity()

```python
def get_reference_entity(
    resource_type: int,
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, Type],
    outputs: Dict[str, Type],
) -> n:
```
See the documentation for {{< py_class_ref flytekit.reference_task >}} and {{< py_class_ref flytekit.reference_workflow >}} as well.

This function is the general form of the two aforementioned functions. It's better for programmatic usage, as
the interface is passed in as arguments instead of analyzed from type annotations.

<!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_references.py
   :start-after: # docs_ref_start
   :end-before: # docs_ref_end
   :language: python
   :dedent: 4
-->
```python
ref_entity = get_reference_entity(
    _identifier_model.ResourceType.WORKFLOW,
    "project",
    "dev",
    "my.other.workflow",
    "abc123",
    inputs=kwtypes(a=str, b=int),
    outputs={},
)
```



| Parameter | Type |
|-|-|
| `resource_type` | `int` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `inputs` | `Dict[str, Type]` |
| `outputs` | `Dict[str, Type]` |

