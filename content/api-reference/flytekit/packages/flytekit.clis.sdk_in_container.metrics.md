---
title: flytekit.clis.sdk_in_container.metrics
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.metrics

## Directory

### Methods

| Method | Description |
|-|-|
| [`get_and_save_remote_with_click_context()`](#get_and_save_remote_with_click_context) | NB: This function will by default mutate the click Context. |


### Variables

| Property | Type | Description |
|-|-|-|
| `CTX_DEPTH` | `str` |  |
| `CTX_DOMAIN` | `str` |  |
| `CTX_PROJECT` | `str` |  |

## Methods

#### get_and_save_remote_with_click_context()

```python
def get_and_save_remote_with_click_context(
    ctx: click.core.Context,
    project: str,
    domain: str,
    save: bool,
    data_upload_location: typing.Optional[str],
) -> flytekit.remote.remote.FlyteRemote
```
NB: This function will by default mutate the click Context.obj dictionary, adding a remote key with value
of the created FlyteRemote object.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `project` | `str` |
| `domain` | `str` |
| `save` | `bool` |
| `data_upload_location` | `typing.Optional[str]` |

