---
title: Images
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Images

**Package:** `flytekit.configuration.internal`

## Methods

| Method | Description |
|-|-|
| [`get_specified_images()`](#get_specified_images) | This section should contain options, where the option name is the friendly name of the image and the corresponding. |


### get_specified_images()

```python
def get_specified_images(
    cfg: typing.Optional[flytekit.configuration.file.ConfigFile],
) -> typing.Dict[str, str]
```
This section should contain options, where the option name is the friendly name of the image and the corresponding
value is actual FQN of the image. Example of how the section is structured
[images]
my_image1=docker.io/flyte:tag
# Note that the tag is optional. If not specified it will be the default version identifier specified
my_image2=docker.io/flyte

:returns a dictionary of name: image&lt;fqn+version&gt; Version is optional


| Parameter | Type | Description |
|-|-|-|
| `cfg` | `typing.Optional[flytekit.configuration.file.ConfigFile]` | |

