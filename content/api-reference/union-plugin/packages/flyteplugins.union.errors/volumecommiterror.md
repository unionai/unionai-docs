---
title: VolumeCommitError
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# VolumeCommitError

**Package:** `flyteplugins.union.errors`

A keep-alive checkpoint could not be made durable: the writeback staging
queue did not finish uploading to object storage (it timed out, or its
progress couldn't be observed because the mount was wedged/gone), so
publishing the snapshot would seal a metadata index that references chunks
not yet in object storage. A later hard-kill would then lose those chunks,
leaving dangling references that read as EIO. The live mount is intact and
its data is not lost — retry the checkpoint once uploads catch up.


## Parameters

```python
class VolumeCommitError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

