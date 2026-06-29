---
title: flyteplugins.union.utils
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# flyteplugins.union.utils

Public utilities for ``flyteplugins.union``.
## Directory

### Methods

| Method | Description |
|-|-|
| [`with_local_flyteplugins_union()`](#with_local_flyteplugins_union) | Layer the locally-built ``flyteplugins-union`` wheel onto ``img``. |


## Methods

#### with_local_flyteplugins_union()

```python
def with_local_flyteplugins_union(
    img: Image,
    pod_platform_hint: str,
) -> Image
```
Layer the locally-built ``flyteplugins-union`` wheel onto ``img``.

Walks up from this module to find the repo's ``pyproject.toml`` and
looks in ``dist/`` for a wheel whose platform tag contains
``pod_platform_hint`` (default ``"linux"`` — pod runtimes). Pure
``py3-none-any`` wheels and dev-machine wheels (``macosx_*``,
``win_amd64``) are explicitly rejected because:

* Pip won't install a macOS/Windows wheel into a Linux pod (tag
  mismatch).
* The pure wheel pip-installs everywhere but ships no juicefs
  binary, so the volume code fails at first ``mount()`` with
  ``'juicefs' not found``.

When the surrounding module is *not* in a source checkout (e.g. a
pip-installed copy inside the runtime container), returns ``img``
unchanged: the wheel was already baked in at build time on the driver
and the task pod is now running from it.

Mirrors the ergonomic of ``flyte.Image.with_local_v2()`` in flyte-sdk.


| Parameter | Type | Description |
|-|-|-|
| `img` | `Image` | |
| `pod_platform_hint` | `str` | |

