---
title: flytekit.core.reference
version: 1.16.14
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
)
```
See the documentation for {{&lt; py_class_ref flytekit.reference_task &gt;}} and {{&lt; py_class_ref flytekit.reference_workflow &gt;}} as well.

This function is the general form of the two aforementioned functions. It's better for programmatic usage, as
the interface is passed in as arguments instead of analyzed from type annotations.

&lt;!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_references.py
   :start-after: # docs_ref_start
   :end-before: # docs_ref_end
   :language: python
   :dedent: 4
--&gt;
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



| Parameter | Type | Description |
|-|-|-|
| `resource_type` | `int` | This is the type of entity it is. Must be one of {{&lt; py_class_ref flytekit.models.core.identifier.ResourceType &gt;}} |
| `project` | `str` | The project the entity you're looking for has been registered in. |
| `domain` | `str` | The domain the entity you're looking for has been registered in. |
| `name` | `str` | The name of the registered entity |
| `version` | `str` | The version the entity you're looking for has been registered with. |
| `inputs` | `Dict[str, Type]` | An ordered dictionary of input names as strings to their Python types. |
| `outputs` | `Dict[str, Type]` | An ordered dictionary of output names as strings to their Python types. :return: |

