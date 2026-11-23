---
title: Mount
description: "A block volume a session mounts: ``volumes={\"/data\": Mount(v, mode=\"rw\")}``."
icon: braces
version: 0.26.0
variants: -flyte +union
layout: py_api
---

# Mount

**Package:** `flyteplugins.union.sandbox`

A block volume a session mounts: ``volumes={"/data": Mount(v, mode="rw")}``.

``mode="ro"`` (the default) mounts it read-only. ``mode="rw"`` mounts it
read-write: what the session writes stays in its own copy until
``sb.volumes[path].commit()`` makes a new version of it. A bare
`ROBlockVolume` in ``volumes=`` is ``Mount(it)``.

Each mounted volume is a private copy of the version named, which is never
changed. What the session writes to a read-write one is kept only by
``sb.volumes[path].commit()``: a session that closes, is cancelled or fails
drops what it wrote since. A volume committed from a sandbox holds an ext4
filesystem its code wrote, which the kernel of whatever mounts it next reads:
for code you don't trust, mount volumes read-only, or none.


## Parameters

```python
class Mount(
    volume: ROBlockVolume,
    mode: MountMode = 'ro',
)
```
| Parameter | Type | Description |
|-|-|-|
| `volume` | `ROBlockVolume` | |
| `mode` | `MountMode` | |

