---
title: flytekit.configuration.default_images
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.configuration.default_images

## Directory

### Classes

| Class | Description |
|-|-|
| [`DefaultImages`](.././flytekit.configuration.default_images#flytekitconfigurationdefault_imagesdefaultimages) | We may want to load the default images from remote - maybe s3 location etc?. |
| [`PythonVersion`](.././flytekit.configuration.default_images#flytekitconfigurationdefault_imagespythonversion) | Create a collection of name/value pairs. |

### Variables

| Property | Type | Description |
|-|-|-|
| `FLYTE_INTERNAL_IMAGE_ENV_VAR` | `str` |  |

## flytekit.configuration.default_images.DefaultImages

We may want to load the default images from remote - maybe s3 location etc?


### Methods

| Method | Description |
|-|-|
| [`default_image()`](#default_image) |  |
| [`find_image_for()`](#find_image_for) |  |
| [`get_version_suffix()`](#get_version_suffix) |  |


#### default_image()

```python
def default_image()
```
#### find_image_for()

```python
def find_image_for(
    python_version: typing.Optional[flytekit.configuration.default_images.PythonVersion],
    flytekit_version: typing.Optional[str],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `python_version` | `typing.Optional[flytekit.configuration.default_images.PythonVersion]` | |
| `flytekit_version` | `typing.Optional[str]` | |

#### get_version_suffix()

```python
def get_version_suffix()
```
## flytekit.configuration.default_images.PythonVersion

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

  >>> Color.RED
  <Color.RED: 1>

- value lookup:

  >>> Color(1)
  <Color.RED: 1>

- name lookup:

  >>> Color['RED']
  <Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


