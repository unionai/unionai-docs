---
title: DefaultImages
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DefaultImages

**Package:** `flytekit.configuration.default_images`

We may want to load the default images from remote - maybe s3 location etc?



## Methods

| Method | Description |
|-|-|
| [`default_image()`](#default_image) |  |
| [`find_image_for()`](#find_image_for) |  |
| [`get_version_suffix()`](#get_version_suffix) |  |


### default_image()

```python
def default_image()
```
### find_image_for()

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

### get_version_suffix()

```python
def get_version_suffix()
```
