---
title: DefaultImages
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# DefaultImages

**Package:** `flytekit.configuration`

We may want to load the default images from remote - maybe s3 location etc?


## Methods

### default_image()

```python
def default_image()
```
No parameters
### find_image_for()

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
### get_version_suffix()

```python
def get_version_suffix()
```
No parameters
