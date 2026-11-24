---
title: MountedVolume
description: "A block volume a session mounts (``sb.volumes[\"/ckpt\"]``): a private copy of `volume`, at `path`, read-only or read-write."
icon: braces
version: 0.26.0
variants: -flyte +union
layout: py_api
---

# MountedVolume

**Package:** `flyteplugins.union.sandbox`

A block volume a session mounts (``sb.volumes["/ckpt"]``): a private
copy of `volume`, at `path`, read-only or read-write.

What the session writes to it is kept only by `commit`: a session
that closes, is cancelled or fails drops what it wrote since. A volume
committed from a sandbox holds an ext4 filesystem its code wrote, which
the kernel of whatever mounts it next reads: for code you don't trust,
mount volumes read-only, or none.


## Parameters

```python
class MountedVolume(
    sb: 'Sandbox',
    path: str,
    volume: ROBlockVolume,
    mode: MountMode,
)
```
| Parameter | Type | Description |
|-|-|-|
| `sb` | `'Sandbox'` | |
| `path` | `str` | |
| `volume` | `ROBlockVolume` | |
| `mode` | `MountMode` | |

## Methods

| Method | Description |
|-|-|
| [`commit()`](#commit) | Commits the session's copy of the volume as it is now, and returns it as a new `ROBlockVolume`: a task input or output, and what another session mounts. |


### commit()

```python
def commit()
```
Commits the session's copy of the volume as it is now, and
returns it as a new `ROBlockVolume`: a task input or output,
and what another session mounts. The session runs on; its writes to
the volume wait while it is frozen for the commit. The session's own
disk is not committed (that is `Sandbox.commit`).

It is the only way to keep what the session wrote to the volume:
whatever is not committed when the session ends is dropped. A
read-only volume can't be committed (``SandboxUsageError``).

What it returns holds a filesystem the session's code wrote: mounting
it in a task pod, or a gVisor session, has that node's kernel read
it.


