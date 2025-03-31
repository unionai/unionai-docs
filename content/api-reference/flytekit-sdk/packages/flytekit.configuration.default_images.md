---
title: flytekit.configuration.default_images
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.configuration.default_images

## Directory

### Classes

| Class | Description |
|-|-|
| [`DefaultImages`](.././flytekit.configuration.default_images#flytekitconfigurationdefault_imagesdefaultimages) | We may want to load the default images from remote - maybe s3 location etc?. |
| [`PythonVersion`](.././flytekit.configuration.default_images#flytekitconfigurationdefault_imagespythonversion) | Create a collection of name/value pairs. |
| [`suppress`](.././flytekit.configuration.default_images#flytekitconfigurationdefault_imagessuppress) | Context manager to suppress specified exceptions. |

## flytekit.configuration.default_images.DefaultImages

We may want to load the default images from remote - maybe s3 location etc?


### Methods

| Method | Description |
|-|-|
| [`default_image()`](#default_image) | None |
| [`find_image_for()`](#find_image_for) | None |
| [`get_version_suffix()`](#get_version_suffix) | None |


#### default_image()

```python
def default_image()
```
#### find_image_for()

```python
def find_image_for(
    python_version: typing.Optional[flytekit.configuration.default_images.PythonVersion],
    flytekit_version: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `python_version` | `typing.Optional[flytekit.configuration.default_images.PythonVersion]` |
| `flytekit_version` | `typing.Optional[str]` |

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


## flytekit.configuration.default_images.suppress

Context manager to suppress specified exceptions

After the exception is suppressed, execution proceeds with the next
statement following the with statement.

with suppress(FileNotFoundError):
os.remove(somefile)
# Execution still resumes here if the file was already removed


```python
def suppress(
    exceptions,
):
```
| Parameter | Type |
|-|-|
| `exceptions` |  |

