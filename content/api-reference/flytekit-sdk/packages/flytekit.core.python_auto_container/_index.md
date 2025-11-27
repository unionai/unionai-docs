---
title: flytekit.core.python_auto_container
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.python_auto_container

## Directory

### Classes

| Class | Description |
|-|-|
| [`DefaultNotebookTaskResolver`](../flytekit.core.python_auto_container/defaultnotebooktaskresolver) | This resolved is used when the task is defined in a notebook. |
| [`DefaultTaskResolver`](../flytekit.core.python_auto_container/defaulttaskresolver) | Please see the notes in the TaskResolverMixin as it describes this default behavior. |
| [`PickledEntity`](../flytekit.core.python_auto_container/pickledentity) | Represents the structure of the pickled object stored in the. |
| [`PickledEntityMetadata`](../flytekit.core.python_auto_container/pickledentitymetadata) | Metadata for a pickled entity containing version information. |
| [`PythonAutoContainerTask`](../flytekit.core.python_auto_container/pythonautocontainertask) | A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |

### Methods

| Method | Description |
|-|-|
| [`get_registerable_container_image()`](#get_registerable_container_image) | Resolve the image to the real image name that should be used for registration. |
| [`update_image_spec_copy_handling()`](#update_image_spec_copy_handling) | This helper function is where the relationship between fast register and ImageSpec is codified. |


### Variables

| Property | Type | Description |
|-|-|-|
| `PICKLE_FILE_PATH` | `str` |  |
| `RUNTIME_PACKAGES_ENV_NAME` | `str` |  |
| `T` | `TypeVar` |  |
| `default_notebook_task_resolver` | `DefaultNotebookTaskResolver` |  |
| `default_task_resolver` | `DefaultTaskResolver` |  |

## Methods

#### get_registerable_container_image()

```python
def get_registerable_container_image(
    img: Optional[Union[str, ImageSpec]],
    cfg: ImageConfig,
) -> str
```
Resolve the image to the real image name that should be used for registration.
1. If img is a ImageSpec, it will be built and the image name will be returned
2. If img is a placeholder string (e.g. {{.image.default.fqn}}:{{.image.default.version}}),
    it will be resolved using the cfg and the image name will be returned



| Parameter | Type | Description |
|-|-|-|
| `img` | `Optional[Union[str, ImageSpec]]` | Configured image or image spec |
| `cfg` | `ImageConfig` | Registration configuration :return: |

#### update_image_spec_copy_handling()

```python
def update_image_spec_copy_handling(
    image_spec: ImageSpec,
    settings: SerializationSettings,
)
```
This helper function is where the relationship between fast register and ImageSpec is codified.
If fast register is not enabled, then source root is used and then files are copied.
See the copy option in ImageSpec for more information.

Currently the relationship is incidental. Because serialization settings are not passed into the image spec
build command (and it probably shouldn't be), the builder has no concept of which files to copy, when, and
from where. (or to where but that is hard-coded)


| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `ImageSpec` | |
| `settings` | `SerializationSettings` | |

