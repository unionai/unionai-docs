---
title: flyteplugins.union.utils.image
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# flyteplugins.union.utils.image

Shared helpers for building :class:`flyte.Image` layers from this repo.

Right now there's exactly one helper — :func:`with_local_flyteplugins_union`
— but the module is named generically because the pattern (find a wheel
in the local repo's ``dist/`` and bake it via :class:`PythonWheels`) is
likely to recur for any future Image factory we ship from this package.
## Directory

### Methods

| Method | Description |
|-|-|
| [`local_dist_folder()`](#local_dist_folder) | Locate the repo's ``dist/`` directory by walking up from this file. |
| [`with_local_flyteplugins_union()`](#with_local_flyteplugins_union) | Layer the locally-built ``flyteplugins-union`` wheel onto ``img``. |


## Methods

#### local_dist_folder()

```python
def local_dist_folder()
```
Locate the repo's ``dist/`` directory by walking up from this file
until ``pyproject.toml`` is found.

Returns ``None`` from a pip-installed copy where no ``pyproject.toml``
exists in any parent — callers should treat that as "nothing to bake
in, we're already running from the installed wheel".


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

