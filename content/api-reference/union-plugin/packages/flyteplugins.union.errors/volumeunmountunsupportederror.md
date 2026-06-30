---
title: VolumeUnmountUnsupportedError
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# VolumeUnmountUnsupportedError

**Package:** `flyteplugins.union.errors`

The runtime cannot unmount the FUSE client at all because ``fusermount``
can't reach its mount table (``/etc/mtab`` is missing, read-only, or
unwritable). Unlike a transient :class:`VolumeUnmountError` (EBUSY), retrying
won't help — the image is missing the ``/etc/mtab`` → ``/proc/self/mounts``
symlink most base images carry. The terminal seal treats this as recoverable:
it falls back to a keep-alive (live) commit, leaving the mount in place. A
kind of :class:`VolumeUnmountError`, so ``except VolumeUnmountError`` catches
it too.


## Parameters

```python
class VolumeUnmountUnsupportedError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

